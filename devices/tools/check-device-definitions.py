#!/usr/bin/env python3
"""Validate completed Device definitions against canonical catalogue surfaces."""
from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from pathlib import Path
from catalogue_source import catalogue_path

import yaml

ROOT = Path(__file__).resolve().parents[2]
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



def broken_table_rows(text: str) -> list[int]:
    """Return line numbers where a Markdown table row starts but is not terminated on that line."""
    bad = []
    for lineno, line in enumerate(text.splitlines(), 1):
        if line.startswith("|") and not line.rstrip().endswith("|"):
            bad.append(lineno)
    return bad

def blank_table_continuations(text: str) -> list[int]:
    """Return blank line numbers that split what Markdown would otherwise treat as one table."""
    lines = text.splitlines()
    bad = []
    for i, line in enumerate(lines):
        if line.strip():
            continue
        j = i - 1
        while j >= 0 and not lines[j].strip():
            j -= 1
        k = i + 1
        while k < len(lines) and not lines[k].strip():
            k += 1
        if j >= 0 and k < len(lines) and lines[j].startswith("|") and lines[k].startswith("|"):
            bad.append(i + 1)
    return bad


def markdown_table_blocks_with_columns(text: str):
    """Return contiguous Markdown table blocks as (start_line, end_line, column_counts)."""
    lines = text.splitlines()
    blocks = []
    i = 0
    while i < len(lines):
        if not lines[i].startswith("|"):
            i += 1
            continue
        start = i + 1
        counts = []
        while i < len(lines) and lines[i].startswith("|"):
            counts.append(len(lines[i].strip("|").split("|")))
            i += 1
        blocks.append((start, i, counts))
    return blocks

def section_body(text: str, heading: str) -> str:
    marker = f"## {heading}\n"
    pos = text.find(marker)
    if pos < 0:
        return ""
    start = pos + len(marker)
    next_pos = text.find("\n## ", start)
    return text[start:] if next_pos < 0 else text[start:next_pos]

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


def table_rows(body: str):
    """Yield labelled cells, preserving identifier namespaces from column headers."""
    header = None
    for line in body.splitlines():
        if not line.startswith("|"):
            header = None
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            continue
        if header is None:
            header = cells
        elif len(header) == len(cells):
            yield dict(zip(header, cells))


def definition_device_ids(text: str) -> set[str]:
    """Read the identity field; cross-references do not identify the containing page."""
    return {
        value
        for row in table_rows(section(text, "Summary"))
        if row.get("Field") == "Device ID"
        for value in re.findall(r"`(OWN-DEV-\d{4})`", row.get("Value", ""))
    }


def catalogue_semantic_errors(text: str, con: sqlite3.Connection, fids: list[int]) -> list[str]:
    """Check the demonstrated semantic regressions, independently of token coverage."""
    errors = []
    for name in ("Firmware-scoped configuration", "Object configuration surfaces"):
        if re.search(r"catalogue-defined|catalogue-scoped", section(text, name)):
            errors.append(f"{name}: unresolved placeholder hides configuration values/defaults")
    firmware = section(text, "Firmware and hardware")
    if "wildcard / unspecified applicability retained" in firmware:
        errors.append("Firmware and hardware: wildcard applicability used as catalogue Status")
    for row in table_rows(firmware):
        status = row.get("Status", row.get("Catalogue status", ""))
        if re.fullmatch(r"`?-?\d+`?", status):
            errors.append("Firmware and hardware: raw numeric catalogue Status")
        if re.fullmatch(r"`?[01]`?", row.get("Default", "")):
            errors.append("Firmware and hardware: raw catalogue Default flag")
    marks = ",".join("?" for _ in fids)
    placements = {
        row["id_slot"]: row for row in con.execute(
            f"""select s.id_slot,s.first_slot,a.id_firmware,k.id_key_object,k.key_object
                from EN_SLOTS s join AS_OBJECT_FIRMWARE a using(id_object_firmware)
                join EN_KEY_OBJECT k using(id_key_object)
                where a.id_firmware in ({marks})""", fids)
    }
    topology = section(text, "Module, Object, and Virgin Object model")
    for row in table_rows(topology):
        if "Catalogue slot row ID" in row and "Module slot" in row:
            ids = re.findall(r"`(\d+)`", row["Catalogue slot row ID"])
            for raw_id in ids:
                expected = placements.get(int(raw_id))
                if expected and row["Module slot"] != token(expected["first_slot"]):
                    errors.append(f"topology: slot row {raw_id} must place Module slot {expected['first_slot']}")
                if expected and "External Object" in row and not row["External Object"].startswith(token(expected["key_object"])):
                    errors.append(f"topology: slot row {raw_id} has wrong external Object number")
        elif "Slot(s)" in row:
            for value in re.findall(r"\d+", row["Slot(s)"]):
                expected = placements.get(int(value))
                if expected and expected["id_slot"] != expected["first_slot"]:
                    errors.append(f"topology: database slot row {value} is labelled as a Module slot")
    mismatches = {
        row["id_key_object"]: row["key_object"] for row in placements.values()
        if row["id_key_object"] != row["key_object"]
    }
    for row in table_rows(section(text, "Diagnostic applicability")):
        if row.get("Diagnostic surface") == token("DIMENSION 30"):
            for database_id, external in mismatches.items():
                if token(database_id) in row.get("Device-specific use", ""):
                    errors.append(f"DIMENSION 30: database Object key {database_id} must not replace external KEYO {external}")
    return errors


def numeric_intervals(values):
    """Normalize inclusive integer domains without expanding large ranges."""
    intervals = []
    for value in values:
        match = re.fullmatch(r"(-?\d+)(?:\.\.(-?\d+))?", str(value))
        if match:
            intervals.append((int(match[1]), int(match[2] or match[1])))
    merged = []
    for low, high in sorted(intervals):
        if merged and low <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(high, merged[-1][1]))
        else:
            merged.append((low, high))
    return merged


def configuration_value_errors(text: str, con: sqlite3.Connection, fids: list[int]) -> list[str]:
    """Compare declared legal numeric values and defaults, not just field-name tokens."""
    errors = []
    marks = ",".join("?" for _ in fids)
    object_keys = dict(con.execute(
        f"""select distinct a.id_key_object,k.key_object from AS_OBJECT_FIRMWARE a
            join EN_KEY_OBJECT k using(id_key_object) where a.id_firmware in ({marks})""", fids))
    owners = [("Firmware", fid, fid) for fid in fids]
    owners += [("Object", key, external) for key, external in object_keys.items()]
    for kind, owner, external in owners:
        if kind == "Firmware":
            body = section(text, "Firmware-scoped configuration")
            rows = [row for row in table_rows(body) if row.get("Firmware") == token(owner)]
            fields = con.execute("select id_conf,conf_name from EN_CONF where id_firmware=? and id_key_object=0", (owner,))
            domain_header, default_header = "Catalogue domain", "Catalogue default"
        else:
            all_objects = section(text, "Object configuration surfaces")
            match = re.search(r"(?ms)^### Object " + re.escape(token(external)) + r" -.*?\n(.*?)(?=^### |\Z)", all_objects)
            rows = list(table_rows(match[1] if match else ""))
            fields = con.execute("select id_conf,conf_name from EN_CONF where id_key_object=? and id_firmware=0", (owner,))
            domain_header, default_header = "Reusable domain", "Reusable default"
        for field in fields:
            candidates = [row for row in rows if row.get("Field") == token(field["conf_name"]) and domain_header in row]
            label = f"{kind} {external} field {field['conf_name']}"
            if not candidates:
                errors.append(label + ": missing structured domain/default row")
                continue
            row = candidates[0]
            ranges = list(con.execute('select * from EN_CONF_RANGE where id_conf=?', (field['id_conf'],)))
            expected = []
            for entry in ranges:
                if entry["value"] not in (None, ""):
                    expected.append(str(entry["value"]))
                elif entry["min_value"] is not None and entry["max_value"] is not None:
                    expected.append(f"{entry['min_value']}..{entry['max_value']}")
            domain = row[domain_header]
            actual = re.findall(r"`([^`]+)`", domain)
            if numeric_intervals(expected) != numeric_intervals(actual):
                errors.append(label + ": numeric legal domain differs from canonical source")
            expected_defaults = {str(entry["default"]) for entry in ranges if entry["default"] not in (None, "")}
            actual_defaults = set(re.findall(r"`([^`]+)`", row.get(default_header, "")))
            if expected_defaults != actual_defaults:
                errors.append(label + ": default differs from canonical source")
            if not expected_defaults and "Not specified in source" not in row.get(default_header, ""):
                errors.append(label + ": unspecified default needs explicit source context")
    return errors


def fail(errors: list[str]) -> int:
    print("Device definition completeness check failed:", file=sys.stderr)
    for error in errors:
        print("- " + error, file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, help="Read-only canonical catalogue copy (default: registered source cache)")
    args = parser.parse_args()
    queue = yaml.safe_load(QUEUE.read_text(encoding="utf-8"))
    items = queue.get("items", {})
    db = args.database if args.database is not None else catalogue_path()
    con = sqlite3.connect(f"file:{db.resolve()}?mode=ro", uri=True)
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
                if device_id in definition_device_ids(body):
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
            if firmware_hardware:
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
            for lineno in broken_table_rows(text):
                errors.append(f"{prefix}:{lineno}: Markdown table row is split or unterminated")
            for start, end, counts in markdown_table_blocks_with_columns(text):
                if len(set(counts)) != 1:
                    errors.append(f"{prefix}:{start}: Markdown table has inconsistent column counts")

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
            for doc_line in documentation_body.splitlines():
                if not doc_line.startswith("|") or "---" in doc_line or doc_line.startswith("| Document |"):
                    continue
                cells = [cell.strip() for cell in doc_line.strip("|").split("|")]
                if len(cells) >= 6:
                    publisher_cell = cells[5]
                    if re.match(r"https?://", publisher_cell):
                        errors.append(f"{prefix}: Documentation Publisher source exposes a raw URL instead of a descriptive Markdown link")
                    if publisher_cell not in ("-", "") and "http" in publisher_cell and not re.search(r"\[[^\]]+\]\(https?://", publisher_cell):
                        errors.append(f"{prefix}: Documentation Publisher source must use descriptive Markdown link text")
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
            for physical_line in physical_body.splitlines():
                if not physical_line.startswith("|") or "---" in physical_line or physical_line.startswith("| Property |"):
                    continue
                cells = [cell.strip() for cell in physical_line.strip("|").split("|")]
                if len(cells) >= 2:
                    value_cell = cells[1]
                    stripped = re.sub(r"`[^`]*`", "", value_cell)
                    if re.search(r"(?<![\w.])(?:\d+(?:\.\d+)?(?:\.\.\d+(?:\.\d+)?)?|\d+\s*x\s*\d+(?:\s*x\s*\d+)?)\s*(?:Vdc|Vac|mA|A|W|kW|Hz|kHz|MHz|GHz|mm|cm|°C|inch)\b", stripped):
                        errors.append(f"{prefix}: Physical/electrical exact measurement literal should use inline code: {value_cell}")
            physical_rows = [
                line for line in physical_body.splitlines()
                if line.startswith("|")
                and "---" not in line
                and not line.startswith("| Property |")
            ]
            if not physical_rows:
                errors.append(
                    f"{prefix}: Physical and electrical characteristics must account for known facts or explicitly state the evidence gap"
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
                archive_link = re.search(
                    r"https://archive\.openwebnet-ha\.org/"
                    r"sha256/[0-9a-f]{2}/[0-9a-f]{2}/[0-9a-f]{64}\.pdf",
                    documentation,
                )
                if not archive_link:
                    errors.append(
                        f"{prefix}: archive is marked complete but Documentation has no canonical R2 archived file link"
                    )

            identity = section(text, "Identity")
            expected_item = int(item_id)
            if token(expected_item) not in identity:
                errors.append(f"{prefix}: Identity does not account for catalogue item {expected_item}")

            identities = section(text, "Commercial identities")
            for commercial_line in identities.splitlines():
                if not commercial_line.startswith("|") or "---" in commercial_line or commercial_line.startswith("| Brand"):
                    continue
                cells = [cell.strip() for cell in commercial_line.strip("|").split("|")]
                if len(cells) >= 4:
                    brand_line, relationship = cells[0], cells[2]
                    if " / " in brand_line or "Undefined" in brand_line or "catalogue combined code" in brand_line:
                        errors.append(f"{prefix}: Commercial Brand / line uses catalogue/presentation metadata instead of normalized human-facing vocabulary: {brand_line}")
                    if re.search(r"\b(?:MyHOME|Classe 300X|L/N/NT)\b", brand_line):
                        errors.append(f"{prefix}: Commercial Brand / line uses a system/family or internal catalogue grouping instead of a marketed line: {brand_line}")
                    if re.fullmatch(r"`?\d+`?", relationship):
                        errors.append(f"{prefix}: Commercial Relationship must be semantic prose, not a raw implementation ID: {relationship}")
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

            errors.extend(f"{prefix}: {error}" for error in catalogue_semantic_errors(text, con, fids))
            errors.extend(f"{prefix}: {error}" for error in configuration_value_errors(text, con, fids))
            object_rows = list(con.execute(
                f"""select a.id_object_firmware,a.id_key_object,k.key_object from AS_OBJECT_FIRMWARE a
                    join EN_KEY_OBJECT k using(id_key_object)
                    where id_firmware in ({placeholders})
                    order by id_object_firmware""",
                fids,
            ))
            topology = section(text, "Module, Object, and Virgin Object model")
            object_body = section(text, "Object configuration surfaces")
            object_ids = sorted({row["id_key_object"] for row in object_rows})
            for object_id in object_ids:
                external = next(row["key_object"] for row in object_rows if row["id_key_object"] == object_id)
                if token(object_id) not in topology:
                    errors.append(f"{prefix}: Object {object_id} is missing from topology")
                obj_match = re.search(
                    r"(?ms)^### Object " + re.escape(token(external)) + r"\s+-.*?\n(.*?)(?=^### Object |\Z)",
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
    for rel in ("devices/index.md", "devices/coverage.md"):
        index_path = ROOT / rel
        index_text = index_path.read_text(encoding="utf-8")
        for lineno in blank_table_continuations(index_text):
            errors.append(f"{rel}:{lineno}: blank line splits a Markdown table")
        for lineno in broken_table_rows(index_text):
            errors.append(f"{rel}:{lineno}: Markdown table row is split or unterminated")

    index_text = (ROOT / "devices/index.md").read_text(encoding="utf-8")
    index_body = section_body(index_text, "Devices")
    index_blocks = markdown_table_blocks_with_columns(index_body)
    if len(index_blocks) != 1:
        errors.append(f"devices/index.md: Devices section must contain exactly one continuous table; found {len(index_blocks)}")
    elif len(set(index_blocks[0][2])) != 1 or index_blocks[0][2][0] != 5:
        errors.append("devices/index.md: Devices table must have exactly 5 columns on every row")

    coverage_text = (ROOT / "devices/coverage.md").read_text(encoding="utf-8")
    coverage_body = section_body(coverage_text, "Device definitions")
    coverage_blocks = markdown_table_blocks_with_columns(coverage_body)
    if len(coverage_blocks) != 1:
        errors.append(f"devices/coverage.md: Device definitions section must contain exactly one table followed only by prose; found {len(coverage_blocks)} table blocks")
    elif len(set(coverage_blocks[0][2])) != 1 or coverage_blocks[0][2][0] != 10:
        errors.append("devices/coverage.md: Device definitions table must have exactly 10 columns on every row")
    lines = coverage_body.splitlines()
    table_end = coverage_blocks[0][1] if coverage_blocks else 0
    if table_end < len(lines) and table_end > 0 and lines[table_end].strip():
        errors.append("devices/coverage.md: prose after Device definitions table must be separated by a blank line")

    if errors:
        return fail(errors)
    print(f"Device definition completeness check passed ({checked} completed definitions from OWN-DEV-0001 onward)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
