#!/usr/bin/env python3
"""Reject implementation representation leakage from public Machine KB text."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Iterator

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = Path("knowledge/manifest.json")

PATTERNS = (
    ("serialized Markdown parser/AST structure",
     re.compile(r"(?:\{\s*['\"]text['\"]\s*:[^\n]{0,500}['\"]inline['\"]\s*:\s*\[|['\"]inline['\"]\s*:\s*\[[^\n]{0,200}\{\s*['\"]type['\"]\s*:)")),
    ("JavaScript object coercion", re.compile(r"\[object Object\]")),
    ("Python runtime object representation",
     re.compile(r"<(?:[A-Za-z_][A-Za-z0-9_.]* object|function [A-Za-z_][A-Za-z0-9_.]*) at 0x[0-9A-Fa-f]+>")),
    ("Python traceback",
     re.compile(r"(?:Traceback \(most recent call last\):|(?:^|\n)\s*File \"[^\"\n]+\", line [0-9]+(?:, in [^\n]+)?)")),
    ("internal execution filesystem path",
     re.compile(r"(?:/workspace/|/mnt/data/|/home/runner/work/|/tmp/ownkb-[A-Za-z0-9_.-]+|/tmp/tmp[A-Za-z0-9_.-]+)")),
)


def text_violation_labels(value: str) -> list[str]:
    return [label for label, pattern in PATTERNS if pattern.search(value)]


def iter_strings(value: object, path: str = "$") -> Iterator[tuple[str, str]]:
    if isinstance(value, str):
        yield path, value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield from iter_strings(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from iter_strings(item, f"{path}[{index}]")


def _safe_artifact_path(output_root: Path, relative: str) -> Path:
    base = output_root.resolve()
    path = (base / relative).resolve()
    try:
        path.relative_to(base)
    except ValueError as error:
        raise ValueError(f"text-hygiene artifact escapes output root: {relative}") from error
    if not path.is_file():
        raise ValueError(f"text-hygiene artifact is missing: {relative}")
    return path


def _scan_json_value(value: object, artifact: str, record: str | None = None) -> list[str]:
    violations = []
    prefix = f"{artifact}:record={record}" if record else artifact
    for field, text in iter_strings(value):
        for label in text_violation_labels(text):
            violations.append(f"{prefix}:{field}: prohibited {label}")
    return violations


def scan_artifact(path: Path, relative: str) -> list[str]:
    if path.name == "llm-corpus.md":
        violations = []
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for label in text_violation_labels(line):
                violations.append(f"{relative}:line={line_number}: prohibited {label}")
        return violations
    if path.suffix == ".jsonl":
        violations = []
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line:
                continue
            value = json.loads(line)
            record = value.get("id") if isinstance(value, dict) and isinstance(value.get("id"), str) else f"line-{line_number}"
            violations.extend(_scan_json_value(value, relative, record))
        return violations
    if path.suffix == ".json":
        return _scan_json_value(json.loads(path.read_text(encoding="utf-8")), relative)
    raise ValueError(f"text-hygiene scanner does not support public artifact: {relative}")


def validate_generated_text(output_root: Path, manifest: dict | None = None) -> int:
    output_root = output_root.resolve()
    if manifest is None:
        manifest = json.loads(_safe_artifact_path(output_root, str(MANIFEST_PATH)).read_text(encoding="utf-8"))

    selected = [str(MANIFEST_PATH)]
    for entry in manifest.get("artifacts", []):
        if not isinstance(entry, dict):
            raise ValueError("text-hygiene manifest artifact entry is invalid")
        if entry.get("kind") == "schema":
            continue
        relative = entry.get("path")
        if not isinstance(relative, str):
            raise ValueError("text-hygiene manifest artifact path is invalid")
        selected.append(relative)
    if len(selected) != len(set(selected)):
        raise ValueError("text-hygiene artifact inventory is duplicated")

    violations = []
    for relative in sorted(selected, key=str.encode):
        violations.extend(scan_artifact(_safe_artifact_path(output_root, relative), relative))
    if violations:
        preview = violations[:100]
        suffix = "" if len(violations) <= 100 else f"\n... {len(violations) - 100} additional violations"
        raise ValueError("generated-text hygiene validation failed:\n" + "\n".join(preview) + suffix)
    return len(selected)


def main() -> int:
    try:
        count = validate_generated_text(ROOT)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        return 1
    print(f"generated-text hygiene validation passed ({count} public generated surfaces scanned)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
