#!/usr/bin/env python3
"""Reject concrete private values in generated machine-knowledge artifacts."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from prepare_sources import (
    DEVICE_ID_LIST_PATTERN,
    DEVICE_ID_PATTERN,
    device_id_values,
    read_manifest,
    safe_source_file,
)


KNOWLEDGE_ROOT = Path(__file__).resolve().parents[1]
ROOT = KNOWLEDGE_ROOT.parent
MANIFEST = KNOWLEDGE_ROOT / "manifest.json"
SOURCE_MANIFEST = KNOWLEDGE_ROOT / "inputs" / "canonical-sources.jsonl"
GENERATED_ROOTS = (
    KNOWLEDGE_ROOT / "llm",
    KNOWLEDGE_ROOT / "retrieval",
    KNOWLEDGE_ROOT / "claims",
    KNOWLEDGE_ROOT / "reference",
)
GENERATED_SUFFIXES = {".json", ".jsonl", ".yaml", ".yml"}
GENERATED_NAMES = {"llm-corpus.md"}

OCTET = r"(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})"
PATTERNS = {
    "IPv4 address": re.compile(rf"(?<![0-9]){OCTET}(?:\.{OCTET}){{3}}(?![0-9])"),
    "IPv4 protocol payload": re.compile(rf"(?<![0-9]){OCTET}(?:\*{OCTET}){{3}}(?![0-9])"),
    "IPv6 address": re.compile(
        r"(?i)(?<![0-9a-f:])(?:[0-9a-f]{1,4}:){2,7}[0-9a-f]{0,4}(?![0-9a-f:])"
    ),
    "MAC address": re.compile(
        r"(?i)(?<![0-9a-f])(?:[0-9a-f]{2}[:-]){5}[0-9a-f]{2}(?![0-9a-f])"
    ),
    "email address": re.compile(
        r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"
    ),
    "UUID": re.compile(
        r"(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b"
    ),
    "concrete Device ID": DEVICE_ID_PATTERN,
    "concrete Device ID list": DEVICE_ID_LIST_PATTERN,
    "credential assignment": re.compile(
        r"(?i)\b(?:password|passwd|secret|api[ _-]?key|access[ _-]?token|cookie)\b\s*[:=]\s*(?![\"']?\[REDACTED\](?=[^A-Za-z0-9_]|$))[\"']?[^\s\"'<>]{4,}"
    ),
    "private filesystem path": re.compile(
        r"(?i)(?:/home/[^/\s]+|/users/[^/\s]+|[a-z]:\\users\\[^\\\s]+)"
    ),
}


def generated_files() -> list[Path]:
    files: set[Path] = {MANIFEST}
    if not MANIFEST.is_file():
        raise ValueError("generated manifest is missing")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for artifact in manifest.get("artifacts", []):
        relative = artifact.get("path")
        if not isinstance(relative, str):
            raise ValueError("manifest artifact path is invalid")
        path = (ROOT / relative).resolve()
        if ROOT.resolve() not in path.parents or not path.is_file():
            raise ValueError("manifest artifact is missing or escapes the repository")
        files.add(path)
    for root in GENERATED_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.name == "README.md":
                continue
            if path.suffix.lower() in GENERATED_SUFFIXES or path.name in GENERATED_NAMES:
                files.add(path)
    return sorted(files)


def removed_device_ids() -> set[str]:
    values: set[str] = set()
    for record in read_manifest(SOURCE_MANIFEST):
        if record.get("classification") != "sanitize":
            continue
        path = safe_source_file(ROOT, str(record["source_path"]))
        text = path.read_text(encoding="utf-8")
        values.update(device_id_values(text))
    return values


def main() -> int:
    violations: list[tuple[Path, int, str]] = []
    try:
        files = generated_files()
        source_values = removed_device_ids()
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"privacy validation failed: {error}", file=sys.stderr)
        return 1
    for path in files:
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for label, pattern in PATTERNS.items():
                if pattern.search(line):
                    violations.append((path.relative_to(KNOWLEDGE_ROOT.parent), line_number, label))
            if any(value in line for value in source_values):
                violations.append(
                    (path.relative_to(KNOWLEDGE_ROOT.parent), line_number, "value removed from sanitized source")
                )

    if violations:
        for path, line_number, label in violations:
            print(f"{path}:{line_number}: prohibited {label}", file=sys.stderr)
        print("privacy validation failed", file=sys.stderr)
        return 1

    print(f"privacy validation passed ({len(files)} generated artifacts and metadata surfaces scanned)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
