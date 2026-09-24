#!/usr/bin/env python3
"""Check deterministic Machine KB build outputs without modifying the repository."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "knowledge" / "tools"))
from serialization import json_bytes  # noqa: E402


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_manifest(path: Path) -> None:
    schema = load_json(ROOT / "knowledge/schema/manifest.schema.json")
    value = load_json(path)
    Draft202012Validator(schema).validate(value)
    if path.read_bytes() != json_bytes(value):
        raise ValueError("manifest does not use canonical JSON bytes")
    entries = value["artifacts"]
    paths = [entry["path"] for entry in entries]
    if paths != sorted(set(paths), key=lambda item: item.encode("utf-8")):
        raise ValueError("manifest artifact paths are unsorted or duplicated")


def command_build(output_root: Path) -> None:
    result = subprocess.run([sys.executable, str(ROOT / "build.py"), "--root", str(ROOT),
                             "--output-root", str(output_root)], text=True,
                            capture_output=True, check=False)
    if result.returncode:
        raise ValueError(result.stderr.strip() or "build command failed")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    if args.root.resolve() != ROOT:
        print("Machine KB check failed: this check must run from its repository root", file=sys.stderr)
        return 1
    try:
        with tempfile.TemporaryDirectory(prefix="ownkb-check-") as temporary:
            base = Path(temporary)
            first, second = base / "first", base / "second"
            command_build(first)
            command_build(second)
            one = first / "knowledge/manifest.json"
            two = second / "knowledge/manifest.json"
            if one.read_bytes() != two.read_bytes():
                raise ValueError("double build produced different manifest bytes")
            validate_manifest(one)
            committed = ROOT / "knowledge/manifest.json"
            if not committed.is_file() or committed.read_bytes() != one.read_bytes():
                raise ValueError("committed manifest is missing or stale; run python build.py")
        privacy = subprocess.run([sys.executable, str(ROOT / "knowledge/tools/validate_privacy.py")],
                                 cwd=ROOT, text=True, capture_output=True, check=False)
        if privacy.returncode:
            raise ValueError(privacy.stderr.strip() or "privacy validation failed")
        print("Machine KB check passed: canonical manifest, double-build determinism, and privacy gate")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"Machine KB check failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
