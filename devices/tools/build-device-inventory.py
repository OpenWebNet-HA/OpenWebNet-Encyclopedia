#!/usr/bin/env python3
"""Export a private research inventory from the registered canonical catalogue."""

from __future__ import annotations

import argparse
import hashlib
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path
from catalogue_source import catalogue_path

ROOT = Path(__file__).resolve().parents[2]


def md(value) -> str:
    if value is None:
        return "-"
    text = str(value).replace("\r", " ").replace("\n", " ").replace("|", "\\|").strip()
    return text or "-"


def rows(con, sql, args=()):
    return [dict(r) for r in con.execute(sql, args)]


def scalar(con, sql, args=()):
    return con.execute(sql, args).fetchone()[0]


def qmarks(values):
    return ",".join("?" for _ in values)


def fw_label(fw, builds):
    if builds:
        build = ",".join(sorted({str(x["firmware_b"]) for x in builds}))
    else:
        build = "?"
    return f'{fw["firmware_V"]}.{fw["firmware_R"]}.{build} ({fw["slots"]} slots)'


def item_details(con, item_id):
    systems = rows(
        con,
        """
        select s.name, s.descr, a.modobj, a.main
        from AS_ITEM_SYSTEM a
        join EN_SYSTEM s on s.id_system=a.id_system
        where a.id_item=?
        order by a.main desc, s.descr, s.name
        """,
        (item_id,),
    )
    fws = rows(
        con,
        """
        select id_firmware, firmware_V, firmware_R, slots, FW_default
        from EN_FIRMWARE
        where id_item=?
        order by FW_default desc, firmware_V, firmware_R, id_firmware
        """,
        (item_id,),
    )
    fw_ids = [x["id_firmware"] for x in fws]
    build_map = defaultdict(list)
    if fw_ids:
        for b in rows(
            con,
            f"select id_firmware, firmware_b from EN_BUILDS where id_firmware in ({qmarks(fw_ids)}) order by id_firmware, firmware_b",
            fw_ids,
        ):
            build_map[b["id_firmware"]].append(b)

    direct_objects = set()
    slot_ids = []
    virgin_objects = set()
    modes = set()
    connections = set()
    fw_conf = 0

    if fw_ids:
        for r in rows(
            con,
            f"select distinct id_key_object from AS_OBJECT_FIRMWARE where id_firmware in ({qmarks(fw_ids)})",
            fw_ids,
        ):
            direct_objects.add(r["id_key_object"])

        for r in rows(
            con,
            f"""
            select s.id_slot
            from EN_SLOTS s
            join AS_OBJECT_FIRMWARE a on a.id_object_firmware=s.id_object_firmware
            where a.id_firmware in ({qmarks(fw_ids)})
            """,
            fw_ids,
        ):
            slot_ids.append(r["id_slot"])

        for r in rows(
            con,
            f"select distinct id_virgin_key_object from AS_FIRMWARE_VIRGIN_OBJECT where id_firmware in ({qmarks(fw_ids)})",
            fw_ids,
        ):
            virgin_objects.add(r["id_virgin_key_object"])

        for r in rows(
            con,
            f"""
            select distinct m.descr
            from AS_FIRMWARE_CONFIG_MODE a
            join EN_CONFIG_MODE m on m.id_config_mode=a.id_config_mode
            where a.id_firmware in ({qmarks(fw_ids)})
            order by m.descr
            """,
            fw_ids,
        ):
            modes.add(r["descr"])

        for r in rows(
            con,
            f"""
            select distinct c.modality_connection
            from AS_CONNECTION_FIRMWARE a
            join EN_CONNECTION c on c.id_connection=a.id_connection
            where a.id_firmware in ({qmarks(fw_ids)})
            order by c.modality_connection
            """,
            fw_ids,
        ):
            if r["modality_connection"]:
                connections.add(r["modality_connection"])

        fw_conf = scalar(
            con,
            f"select count(*) from EN_CONF where id_firmware in ({qmarks(fw_ids)})",
            fw_ids,
        )

    candidate_objects = set(direct_objects)
    if virgin_objects:
        for r in rows(
            con,
            f"""
            select distinct id_key_object
            from AS_OBJECT_VIRGIN_OBJECT
            where id_virgin_key_object in ({qmarks(list(virgin_objects))})
            """,
            list(virgin_objects),
        ):
            candidate_objects.add(r["id_key_object"])

    object_conf = 0
    if candidate_objects:
        object_conf = scalar(
            con,
            f"""
            select count(*)
            from EN_CONF
            where id_firmware=0 and id_key_object in ({qmarks(list(candidate_objects))})
            """,
            list(candidate_objects),
        )

    conditions = 0
    rules = 0
    if slot_ids:
        conditions = scalar(
            con,
            f"select count(*) from AS_SLOT_CONDITION where id_slot in ({qmarks(slot_ids)})",
            slot_ids,
        )
        rules = scalar(
            con,
            f"""
            select count(distinct c.id_conv_rule)
            from AS_SLOT_CONDITION a
            join EN_CONDITION c on c.id_condition=a.id_condition
            where a.id_slot in ({qmarks(slot_ids)})
              and c.id_conv_rule is not null
              and c.id_conv_rule not in ('', 0)
            """,
            slot_ids,
        )

    return {
        "systems": systems,
        "firmwares": [fw_label(f, build_map[f["id_firmware"]]) for f in fws],
        "firmware_count": len(fws),
        "max_slots": max((int(f["slots"]) for f in fws), default=0),
        "direct_objects": len(direct_objects),
        "candidate_objects": len(candidate_objects),
        "virgin_objects": len(virgin_objects),
        "fw_conf": fw_conf,
        "object_conf": object_conf,
        "conditions": conditions,
        "rules": rules,
        "modes": sorted(modes),
        "connections": sorted(connections),
    }


def main_system(detail):
    if not detail["systems"]:
        return "-"
    s = detail["systems"][0]
    return f'{s["descr"] or s["name"]} / modobj {s["modobj"]}'


def build(con, output_dir, db):
    devices = rows(
        con,
        """
        select d.id_device, d.code, d.name, d.id_item, d.is_gateway,
               b.brand_name, l.line_name, i.descr as item_descr
        from EN_DEVICE d
        join EN_BRAND b on b.id_brand=d.id_brand
        join EN_LINE l on l.id_line=d.id_line
        join EN_ITEM i on i.id_item=d.id_item
        order by lower(b.brand_name), lower(l.line_name), lower(d.code), d.id_device
        """,
    )

    by_item = defaultdict(list)
    for d in devices:
        by_item[d["id_item"]].append(d)

    item_ids = sorted(by_item)
    details = {item_id: item_details(con, item_id) for item_id in item_ids}
    source_sha = hashlib.sha256(db.read_bytes()).hexdigest()

    shared_items = sum(1 for values in by_item.values() if len(values) > 1)
    shared_records = sum(len(values) for values in by_item.values() if len(values) > 1)

    overview = [
        "# Device Database Inventory",
        "",
        "> Generated by devices/tools/build-device-inventory.py. Do not hand-edit generated tables.",
        "",
        "This private research export lists raw canonical MyHOME Suite catalogue records. It is not a curated Device reference or an acceptance ledger.",
        "",
        "A row in EN_DEVICE is treated here as a commercial catalogue record. Records sharing one EN_ITEM are grouped as a technical-item cluster because they share a catalogue capability core. Explicit SKU-to-item associations establish catalogue identities; shared capability does not prove identical hardware or installed behavior.",
        "",
        "## Source",
        "",
        "- Database: sources/myhome-suite/3.5.38/databases/MHCatalogue.db",
        f"- SHA-256: {source_sha}",
        "",
        "## Coverage",
        "",
        "| Measure | Count |",
        "| --- | ---: |",
        f"| Commercial Device records | {len(devices)} |",
        f"| Shared technical items used by those records | {len(item_ids)} |",
        f'| Brand labels represented | {len({d["brand_name"] for d in devices})} |',
        f'| Product-line labels represented | {len({d["line_name"] for d in devices})} |',
        f'| Gateway Device records | {sum(1 for d in devices if d["is_gateway"])} |',
        f"| Technical items used by more than one commercial record | {shared_items} |",
        f"| Commercial records belonging to shared items | {shared_records} |",
        "",
        "Every commercial Device record in this source revision has at least one system mapping and at least one firmware definition.",
        "",
        "## Views",
        "",
        "- [Commercial Device Records](commercial-records.md) - all EN_DEVICE rows, optimized for SKU/brand Ctrl-F lookup.",
        "- [Technical Item Clusters](technical-items.md) - shared capability cores that are natural starting points for curated OWN-DEV definitions.",
        "",
        "## Interpretation",
        "",
        "- Item is the shared EN_ITEM capability identity.",
        "- Model is the item-level AS_ITEM_SYSTEM.modobj for the main system mapping.",
        "- Firmware lists catalogue applicability definitions, not necessarily firmware observed on physical hardware.",
        "- Direct Objects counts firmware/Object associations; candidate Objects additionally includes Objects permitted through Virgin Objects.",
        "- FW conf counts firmware-scoped configuration fields; Object conf counts reusable Object configuration fields reachable from direct or Virgin Object candidates.",
        "- Conditions and conversion rules quantify topology/configuration logic that should be preserved when a Device definition is curated.",
        "- Shared item membership must not by itself choose a canonical SKU or erase package, brand, or region differences.",
        "",
    ]

    commercial = [
        "# Commercial Device Records",
        "",
        "> Generated from the canonical MHCatalogue.db. Do not hand-edit.",
        "",
        f"Source SHA-256: {source_sha}",
        "",
        "One row is emitted for every EN_DEVICE record. Use Ctrl-F for an exact SKU/reference.",
        "",
        "| Brand | Line | SKU / reference | Catalogue name | Item | Main system / model | Firmware | Max slots | Direct / candidate Objects | Virgin Objects | FW / Object conf | Gateway | Records sharing item |",
        "| --- | --- | --- | --- | ---: | --- | --- | ---: | ---: | ---: | ---: | --- | ---: |",
    ]
    for d in devices:
        det = details[d["id_item"]]
        commercial.append(
            "| "
            + " | ".join(
                [
                    md(d["brand_name"]),
                    md(d["line_name"]),
                    md(d["code"]),
                    md(d["name"]),
                    str(d["id_item"]),
                    md(main_system(det)),
                    md("; ".join(det["firmwares"])),
                    str(det["max_slots"]),
                    f'{det["direct_objects"]} / {det["candidate_objects"]}',
                    str(det["virgin_objects"]),
                    f'{det["fw_conf"]} / {det["object_conf"]}',
                    "Yes" if d["is_gateway"] else "No",
                    str(len(by_item[d["id_item"]])),
                ]
            )
            + " |"
        )
    commercial.append("")

    technical = [
        "# Technical Item Clusters",
        "",
        "> Generated from the canonical MHCatalogue.db. Do not hand-edit.",
        "",
        f"Source SHA-256: {source_sha}",
        "",
        "Each row groups all commercial Device records sharing one EN_ITEM. Treat this as a review queue for technical Device definitions, not as an automatic synonym table.",
        "",
        "| Item | Description | Main system / model | Commercial records | SKUs / references | Firmware defs | Firmware applicability | Max slots | Direct / candidate Objects | Virgin Objects | FW / Object conf | Conditions | Conversion rules | Modes | Connections | Gateway records |",
        "| ---: | --- | --- | ---: | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: |",
    ]
    for item_id in item_ids:
        ds = by_item[item_id]
        det = details[item_id]
        skus = ", ".join(d["code"] for d in sorted(ds, key=lambda x: x["code"].casefold()))
        technical.append(
            "| "
            + " | ".join(
                [
                    str(item_id),
                    md(ds[0]["item_descr"]),
                    md(main_system(det)),
                    str(len(ds)),
                    md(skus),
                    str(det["firmware_count"]),
                    md("; ".join(det["firmwares"])),
                    str(det["max_slots"]),
                    f'{det["direct_objects"]} / {det["candidate_objects"]}',
                    str(det["virgin_objects"]),
                    f'{det["fw_conf"]} / {det["object_conf"]}',
                    str(det["conditions"]),
                    str(det["rules"]),
                    md(", ".join(det["modes"])),
                    md(", ".join(det["connections"])),
                    str(sum(1 for d in ds if d["is_gateway"])),
                ]
            )
            + " |"
        )
    technical.append("")

    return {
        output_dir / "README.md": "\n".join(overview),
        output_dir / "commercial-records.md": "\n".join(commercial),
        output_dir / "technical-items.md": "\n".join(technical),
    }


def run(output_dir, check=False):
    output_dir = output_dir.resolve()
    if output_dir.is_relative_to(ROOT):
        raise SystemExit("Research exports must remain outside the public repository")
    db = catalogue_path()
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    outputs = build(con, output_dir, db)
    con.close()

    stale = False
    for path, content in outputs.items():
        content = content.rstrip() + "\n"
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                print(f"out of date: {path}", file=sys.stderr)
                stale = True
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            print(path)

    if stale:
        raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True, type=Path,
                        help="Private research export directory outside the public repository")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    run(args.output_dir, check=args.check)
