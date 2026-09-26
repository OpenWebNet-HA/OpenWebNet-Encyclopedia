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

from privacy_detection import (
    DEVICE_ID_LIST_PATTERN,
    DEVICE_ID_PATTERN,
    device_id_values,
    sanitize_privacy_text,
)


def sanitize(text: str) -> tuple[str, list[str]]:
    return sanitize_privacy_text(text)


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
