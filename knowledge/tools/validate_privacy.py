#!/usr/bin/env python3
"""Reject concrete private values in generated machine-knowledge artifacts."""

from __future__ import annotations

import re
import sys
from pathlib import Path


KNOWLEDGE_ROOT = Path(__file__).resolve().parents[1]
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
    "concrete Device ID": re.compile(
        r"(?i)\b(?:device[ _-]?id|device identifier)\b[^\n]{0,40}\b[0-9a-f]{8}\b"
    ),
    "credential assignment": re.compile(
        r"(?i)\b(?:password|passwd|secret|api[ _-]?key|access[ _-]?token|cookie)\b\s*[:=]\s*(?![\"']?\[REDACTED\](?=[^A-Za-z0-9_]|$))[\"']?[^\s\"'<>]{4,}"
    ),
    "private filesystem path": re.compile(
        r"(?i)(?:/home/[^/\s]+|/users/[^/\s]+|[a-z]:\\users\\[^\\\s]+)"
    ),
}


def generated_files() -> list[Path]:
    files: list[Path] = []
    for root in GENERATED_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.name == "README.md":
                continue
            if path.suffix.lower() in GENERATED_SUFFIXES or path.name in GENERATED_NAMES:
                files.append(path)
    return sorted(files)


def main() -> int:
    violations: list[tuple[Path, int, str]] = []
    for path in generated_files():
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for label, pattern in PATTERNS.items():
                if pattern.search(line):
                    violations.append((path.relative_to(KNOWLEDGE_ROOT.parent), line_number, label))

    if violations:
        for path, line_number, label in violations:
            print(f"{path}:{line_number}: prohibited {label}", file=sys.stderr)
        print("privacy validation failed", file=sys.stderr)
        return 1

    print(f"privacy validation passed ({len(generated_files())} generated artifacts scanned)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
