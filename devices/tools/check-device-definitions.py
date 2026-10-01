#!/usr/bin/env python3
"""Validate completed Device definitions against canonical catalogue surfaces."""
from __future__ import annotations

import re
import sqlite3
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "sources" / "myhome-suite" / "3.5.38" / "databases" / "MHCatalogue.db"
QUEUE = ROOT / "devices" / "work-queue.yaml"
DEFINITIONS = ROOT / "devices" / "definitions"
BT = chr(96)

REQUIRED_TABLE_SECTIONS = (
    "Commercial identities",
    "Documentation",
    "Physical and electrical characteristics",
    "Identity",
    "Firmware and hardware",
    "Module, Object, and Virgin Object model",
    "Configuration modes",
    "Firmware-scoped configuration",
    "Object configuration surfaces",
    "Conditions, filters, and conversions",
    "Diagnostic applicability",
)


def section(text: str, name: str) -> str:
    match = re.search(r"(?ms)^## " + re.escape(name) + r"\n(.*?)(?=^## |\Z)", text)
    return match.group(1) if match else ""


def table_blocks(text: str) -> int:
    blocks = 0
    in_table = False
    for line in text.splitlines():
        now = bool(re.match(r"^\|.*\|$", line))
        if now and not in_table:
            blocks += 1
        in_table = now
    return blocks


def token(value: object) -> str:
    return BT + str(value) + BT


def fail(errors: list[str]) -> int:
    print("Device definition completeness check failed:", file=sys.stderr)
    for error in errors:
        print("- " + error, file=sys.stderr)
    return 1


def main() -> int:
    queue = yaml.safe_load(QUEUE.read_text(encoding="utf-8"))
    items = queue.get("items", {})
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    errors: list[str] = []
    checked = 0

    for item_id, entry in items.items():
        review = entry.get("review", {})
        if review.get("definition") != "complete":
            continue
        outcome = entry.get("outcome") or {}
        device_ids = outcome.get("device_ids") or []
        for device_id in device_ids:
            match = re.fullmatch(r"OWN-DEV-(\d{4})", str(device_id))
            if not match or int(match.group(1)) < 1:
                continue

            candidates = []
            for path in DEFINITIONS.glob("own-dev-*.md"):
                body = path.read_text(encoding="utf-8")
                if token(device_id) in body or ("Device ID | " + token(device_id)) in body:
                    candidates.append((path, body))
            if len(candidates) != 1:
                errors.append(f"{device_id}: expected exactly one definition, found {len(candidates)}")
                continue

            path, text = candidates[0]
            checked += 1
            prefix = path.name

            for marker in ("Ã", "Â", "â€", "�"):
                if marker in text:
                    errors.append(f"{prefix}: apparent text-encoding corruption marker {marker!r}")

            firmware_hardware = section(text, "Firmware and hardware")
            if int(match.group(1)) <= 30:
                if "Declared slots" in firmware_hardware:
                    errors.append(
                        f"{prefix}: Firmware and hardware exposes implementation slots instead of formal Declared Modules"
                    )
                if re.search(r"(?m)^\|.*\|\s*`[01]`\s*\|\s*`[01]`\s*\|\s*$", firmware_hardware):
                    errors.append(
                        f"{prefix}: Firmware and hardware exposes raw catalogue default/status flags"
                    )

            if table_blocks(text) < 8:
                errors.append(f"{prefix}: only {table_blocks(text)} table blocks; completed definitions require at least 8")

            summary_body = section(text, "Summary")
            for label in (
                "Catalogue item",
                "Main catalogue system",
                "Item model / `modobj`",
                "Firmware definition",
                "Declared Modules",
                "Categories",
            ):
                if f"| {label} |" not in summary_body:
                    errors.append(f"{prefix}: Summary is missing baseline field {label}")

            documentation_body = section(text, "Documentation")
            expected_doc_header = (
                "| Document | Type | Revision / date | Coverage | "
                "Archived original | Publisher source |"
            )
            if expected_doc_header not in documentation_body:
                errors.append(
                    f"{prefix}: Documentation must separate archived originals from publisher sources"
                )

            physical_body = section(text, "Physical and electrical characteristics")
            if "| Property | Value | Evidence |" not in physical_body:
                errors.append(
                    f"{prefix}: Physical and electrical characteristics must use a Property/Value/Evidence table"
                )
            physical_rows = [
                line for line in physical_body.splitlines()
                if line.startswith("|")
                and "---" not in line
                and not line.startswith("| Property |")
            ]
            if len(physical_rows) < 3:
                errors.append(
                    f"{prefix}: Physical and electrical characteristics has only {len(physical_rows)} fact rows"
                )

            diagnostic_body = section(text, "Diagnostic applicability")
            if "| Diagnostic surface | Device-specific use | Canonical reference |" not in diagnostic_body:
                errors.append(
                    f"{prefix}: Diagnostic applicability must use the Device-specific baseline table"
                )
            for generic in (
                "Identify the Device model/family and compare it with catalogue identity.",
                "Resolve Module/Object topology, especially when candidates share a slot.",
                "Inspect addressing for the resolved Module/Object when exposed.",
                "Corroborate firmware/Object configuration and physical/software relationships.",
            ):
                if generic in diagnostic_body:
                    errors.append(
                        f"{prefix}: Diagnostic applicability still contains generic boilerplate: {generic}"
                    )

            for name in REQUIRED_TABLE_SECTIONS:
                body = section(text, name)
                if not body:
                    errors.append(f"{prefix}: missing section {name}")
                elif not re.search(r"(?m)^\|.*\|$", body):
                    errors.append(f"{prefix}: section {name} has no table")

            documentation = section(text, "Documentation")
            if review.get("documentation_archive") == "complete":
                if "sources/devices/documents/" not in documentation:
                    errors.append(f"{prefix}: archive is marked complete but Documentation has no direct archived file link")

            identity = section(text, "Identity")
            expected_item = int(item_id)
            if token(expected_item) not in identity:
                errors.append(f"{prefix}: Identity does not account for catalogue item {expected_item}")

            identities = section(text, "Commercial identities")
            if review.get("commercial_identities") == "complete":
                for row in con.execute("select code from EN_DEVICE where id_item=? order by id_device", (expected_item,)):
                    if row["code"] and token(row["code"]) not in identities:
                        errors.append(f"{prefix}: commercial identity {row['code']} is missing")

            firmware = list(con.execute(
                "select id_firmware from EN_FIRMWARE where id_item=? order by id_firmware",
                (expected_item,),
            ))
            fids = [row["id_firmware"] for row in firmware]
            if not fids:
                continue

            placeholders = ",".join("?" * len(fids))
            firmware_body = section(text, "Firmware-scoped configuration")
            for raw_marker in ("Catalogue range rows", "| Flags |", "visible=", "type-id=", "range -..-"):
                if raw_marker in firmware_body:
                    errors.append(f"{prefix}: Firmware-scoped configuration contains raw catalogue serialization marker {raw_marker!r}")
            object_human_body = section(text, "Object configuration surfaces")
            reconciled_match = re.search(
                r"(?ms)^### Reconciled Object notes\n(.*?)(?=^## |\Z)",
                object_human_body,
            )
            if reconciled_match and not re.search(r"(?m)^\|.*\|$", reconciled_match.group(1)):
                errors.append(
                    f"{prefix}: Reconciled Object notes must structure enumerable Object facts as a table"
                )
            for raw_marker in ("Catalogue range rows", "| Flags |", "visible=", "type-id=", "range -..-"):
                if raw_marker in object_human_body:
                    errors.append(f"{prefix}: Object configuration surfaces contains raw catalogue serialization marker {raw_marker!r}")
            for row in con.execute(
                f"""select distinct conf_name from EN_CONF
                    where id_firmware in ({placeholders}) and id_firmware<>0 and conf_name is not null
                    order by conf_name""",
                fids,
            ):
                if token(row["conf_name"]) not in firmware_body:
                    errors.append(f"{prefix}: firmware field {row['conf_name']} is not accounted for")

            object_rows = list(con.execute(
                f"""select id_object_firmware,id_key_object from AS_OBJECT_FIRMWARE
                    where id_firmware in ({placeholders})
                    order by id_object_firmware""",
                fids,
            ))
            topology = section(text, "Module, Object, and Virgin Object model")
            object_body = section(text, "Object configuration surfaces")
            object_ids = sorted({row["id_key_object"] for row in object_rows})
            for object_id in object_ids:
                if token(object_id) not in topology:
                    errors.append(f"{prefix}: Object {object_id} is missing from topology")
                obj_match = re.search(
                    r"(?ms)^### Object " + re.escape(token(object_id)) + r"\s+-.*?\n(.*?)(?=^### Object |\Z)",
                    object_body,
                )
                if not obj_match:
                    errors.append(f"{prefix}: Object {object_id} has no configuration subsection")
                    continue
                obj_section = obj_match.group(1)
                for conf in con.execute(
                    """select conf_name from EN_CONF
                       where id_key_object=? and id_key_object<>0 and conf_name is not null
                       order by progressive,id_conf""",
                    (object_id,),
                ):
                    if token(conf["conf_name"]) not in obj_section:
                        errors.append(
                            f"{prefix}: Object {object_id} field {conf['conf_name']} is not accounted for"
                        )

            virgin_rows = list(con.execute(
                f"""select fv.id_virgin_key_object
                    from AS_FIRMWARE_VIRGIN_OBJECT fv
                    where fv.id_firmware in ({placeholders})
                    order by fv.id_virgin_key_object""",
                fids,
            ))
            for row in virgin_rows:
                if token(row["id_virgin_key_object"]) not in topology:
                    errors.append(f"{prefix}: Virgin Object {row['id_virgin_key_object']} is missing from topology")

            conditions_body = section(text, "Conditions, filters, and conversions")
            object_firmware_ids = [row["id_object_firmware"] for row in object_rows]
            if object_firmware_ids:
                of_placeholders = ",".join("?" * len(object_firmware_ids))
                for row in con.execute(
                    f"""select distinct id_filter from EN_FILTER
                        where id_object_firmware in ({of_placeholders})
                        order by id_filter""",
                    object_firmware_ids,
                ):
                    if token(row["id_filter"]) not in conditions_body:
                        errors.append(f"{prefix}: filter {row['id_filter']} is not accounted for")

                slot_rows = list(con.execute(
                    f"""select id_slot from EN_SLOTS
                        where id_object_firmware in ({of_placeholders})
                        order by id_slot""",
                    object_firmware_ids,
                ))
                slot_ids = [row["id_slot"] for row in slot_rows]
                if slot_ids:
                    slot_placeholders = ",".join("?" * len(slot_ids))
                    for row in con.execute(
                        f"""select distinct id_condition from AS_SLOT_CONDITION
                            where id_slot in ({slot_placeholders})
                            order by id_condition""",
                        slot_ids,
                    ):
                        if token(row["id_condition"]) not in conditions_body:
                            errors.append(f"{prefix}: slot condition {row['id_condition']} is not accounted for")

    con.close()
    if errors:
        return fail(errors)
    print(f"Device definition completeness check passed ({checked} completed definitions from OWN-DEV-0001 onward)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
