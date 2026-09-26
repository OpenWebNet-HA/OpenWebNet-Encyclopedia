#!/usr/bin/env python3
"""Classify and sanitize source text before it can enter Machine KB derivation.

This command writes only a constrained, public intermediate JSONL form.  It is
deliberately not a corpus generator: later phases must consume its output rather
than raw source files.  It uses no network service or model.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


SOURCE_TYPES = {
    "canonical_documentation",
    "public_specification",
    "public_implementation_evidence",
    "capture",
    "log",
    "inventory",
    "configuration_export",
    "screenshot",
    "private_submission",
}
CLASSIFICATIONS = {"publishable", "sanitize", "prohibited"}
PROHIBITED_TYPES = {
    "capture", "log", "inventory", "configuration_export", "screenshot", "private_submission"
}
PROHIBITED_SUFFIXES = {".pcap", ".pcapng", ".har", ".log"}
PROHIBITED_PATH_WORDS = {
    "capture", "captures", "log", "logs", "inventory", "inventories",
    "configuration", "configurations", "screenshot", "screenshots", "export", "exports",
}

OCTET = r"(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})"
DEVICE_ID_PATTERN = re.compile(
    r"(?ix)"
    r"(?P<prefix>\b(?:"
    r"(?:(?:installed|observed|physical|scanned|test|light-control-only)\s+)?"
    r"device(?:\s+(?:id|identifier))?"
    r"|(?:installed|observed|scanned|test)\s+unit(?:\s+(?:id|identifier))?"
    r")\b"
    r"(?!\s+(?:type|model|class|family|firmware|catalog(?:ue)?|code))"
    r"[^0-9a-f\n]{0,24}[\x60'\"\[]?)"
    r"(?P<value>[0-9a-f]{8})"
    r"(?P<suffix>[\x60'\"\]]?)"
)
HEX8_PATTERN = re.compile(r"(?i)\b[0-9a-f]{8}\b")
DEVICE_ID_LIST_PATTERN = re.compile(
    r"(?ix)\b(?:observed|installed|scanned|test)\s+devices\b"
    r"(?!\s+(?:types|models|classes|families|firmware|catalog(?:ue)?|codes))"
    r"[^.\n]{0,320}\b[0-9a-f]{8}\b[^.\n]{0,320}\."
)


def redact_device_id_list(match: re.Match[str]) -> str:
    return HEX8_PATTERN.sub("[DEVICE_ID]", match.group(0))


def device_id_values(text: str) -> set[str]:
    values = {match.group("value") for match in DEVICE_ID_PATTERN.finditer(text)}
    for match in DEVICE_ID_LIST_PATTERN.finditer(text):
        values.update(HEX8_PATTERN.findall(match.group(0)))
    return values


TRANSFORMS = (
    ("network_address", re.compile(rf"(?<![0-9]){OCTET}(?:\.{OCTET}){{3}}(?![0-9])"), "[NETWORK_ADDRESS]"),
    ("network_address", re.compile(rf"(?<![0-9]){OCTET}(?:\*{OCTET}){{3}}(?![0-9])"), "[NETWORK_ADDRESS]"),
    ("network_address", re.compile(r"(?i)(?<![0-9a-f:])(?:[0-9a-f]{1,4}:){2,7}[0-9a-f]{0,4}(?![0-9a-f:])"), "[NETWORK_ADDRESS]"),
    ("hardware_id", re.compile(r"(?i)(?<![0-9a-f])(?:[0-9a-f]{2}[:-]){5}[0-9a-f]{2}(?![0-9a-f])"), "[MAC_ADDRESS]"),
    ("hardware_id", re.compile(r"(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b"), "[INSTANCE_IDENTIFIER]"),
    ("device_id", DEVICE_ID_PATTERN, r"\g<prefix>[DEVICE_ID]\g<suffix>"),
    ("device_id", DEVICE_ID_LIST_PATTERN, redact_device_id_list),
    ("person_identifier", re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"), "[PERSONAL_IDENTIFIER]"),
    ("other", re.compile(r"(?i)(?:/home/[^/\s]+|/users/[^/\s]+|[a-z]:\\users\\[^\\\s]+)"), "[LOCAL_PATH]"),
    ("credential", re.compile(r"(?i)\b(password|passwd|secret|api[ _-]?key|access[ _-]?token|cookie)\b\s*[:=]\s*[\"']?[^\s\"'<>]{4,}"), r"\1=[REDACTED]"),
)


def read_manifest(path: Path) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"{path}:{number}: invalid JSON: {error.msg}") from error
        if not isinstance(record, dict):
            raise ValueError(f"{path}:{number}: manifest record must be an object")
        records.append(record)
    return records


def validate_manifest_record(record: dict[str, object], label: str) -> None:
    expected = {"source_id", "source_path", "source_type", "classification"}
    if set(record) != expected:
        raise ValueError(f"{label}: manifest fields must be exactly {sorted(expected)}")
    if not all(isinstance(record[key], str) for key in expected):
        raise ValueError(f"{label}: all manifest fields must be strings")
    if not re.fullmatch(r"ownkb:source:[a-z0-9]+(?:-[a-z0-9]+)*", str(record["source_id"])):
        raise ValueError(f"{label}: invalid source_id")
    source_path = str(record["source_path"])
    if not re.fullmatch(r"[A-Za-z0-9._/-]+", source_path) or source_path.startswith("/") or ".." in Path(source_path).parts:
        raise ValueError(f"{label}: source_path must be a safe relative path")
    if record["source_type"] not in SOURCE_TYPES or record["classification"] not in CLASSIFICATIONS:
        raise ValueError(f"{label}: invalid source type or classification")
    parts = set(Path(source_path).parts)
    if (str(record["source_type"]) in PROHIBITED_TYPES or Path(source_path).suffix.lower() in PROHIBITED_SUFFIXES or parts & PROHIBITED_PATH_WORDS) and record["classification"] != "prohibited":
        raise ValueError(f"{label}: private-source form must be classified prohibited")
    if record["classification"] == "prohibited" and str(record["source_type"]) not in PROHIBITED_TYPES:
        raise ValueError(f"{label}: prohibited classification requires a prohibited source type")


def sanitize(text: str) -> tuple[str, list[str]]:
    removed: list[str] = []
    for value_class, pattern, replacement in TRANSFORMS:
        text, count = pattern.subn(replacement, text)
        if count and value_class not in removed:
            removed.append(value_class)
    return text, sorted(removed)


def safe_source_file(source_root: Path, source_path: str) -> Path:
    candidate = (source_root / source_path).resolve()
    if source_root.resolve() not in candidate.parents:
        raise ValueError("source_path escapes source root")
    return candidate


def prepare(manifest: Path, source_root: Path) -> list[dict[str, object]]:
    prepared: list[dict[str, object]] = []
    for index, record in enumerate(read_manifest(manifest), 1):
        label = f"{manifest}:{index}"
        validate_manifest_record(record, label)
        if record["classification"] == "prohibited":
            continue
        path = safe_source_file(source_root, str(record["source_path"]))
        if not path.is_file():
            raise ValueError(f"{label}: publishable source file is missing")
        original = path.read_text(encoding="utf-8")
        text, removed = sanitize(original)
        if record["classification"] == "publishable" and removed:
            raise ValueError(f"{label}: publishable source has sensitive values; classify it sanitize")
        if record["classification"] == "sanitize" and not removed:
            raise ValueError(f"{label}: sanitize source had no recognized sensitive value; classify it publishable or refine the deterministic policy")
        privacy = {"classification": "sanitized" if removed else "public", "removed_value_classes": removed}
        prepared.append({"source_id": record["source_id"], "source_path": record["source_path"], "privacy": privacy, "text": text})
    return sorted(prepared, key=lambda item: (str(item["source_id"]), str(item["source_path"])))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        prepared = prepare(args.manifest, args.source_root)
        output = "".join(json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n" for record in prepared)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8", newline="\n")
    except (OSError, ValueError) as error:
        print(f"pre-extraction privacy validation failed: {error}", file=sys.stderr)
        return 1
    print(f"prepared {len(prepared)} publishable source records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
