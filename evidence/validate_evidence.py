#!/usr/bin/env python3
"""Validator for OpenWebNet Encyclopedia Field Evidence Packages (RFC #536 & #509).

Enforces schema compliance, frame chronology, frame count consistency,
privacy sanitization constraints, and formatting rules across all evidence packages.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

EVIDENCE_DIR = Path(__file__).resolve().parent
SCHEMA_DIR = EVIDENCE_DIR / "schema"


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        raise ValueError(f"{path.name} lacks a trailing newline")
    return json.loads(text, object_pairs_hook=reject_duplicate_keys)


def validate_evidence_package(pkg_dir: Path, manifest_val: Draft202012Validator, frame_val: Draft202012Validator, privacy_val: Draft202012Validator) -> None:
    manifest_path = pkg_dir / "manifest.json"
    frames_path = pkg_dir / "frames.jsonl"
    privacy_path = pkg_dir / "privacy.json"

    if not manifest_path.is_file():
        raise FileNotFoundError(f"Missing manifest.json in {pkg_dir.name}")
    if not frames_path.is_file():
        raise FileNotFoundError(f"Missing frames.jsonl in {pkg_dir.name}")
    if not privacy_path.is_file():
        raise FileNotFoundError(f"Missing privacy.json in {pkg_dir.name}")

    # Validate manifest.json
    manifest = load_json(manifest_path)
    manifest_val.validate(manifest)

    # Validate privacy.json
    privacy = load_json(privacy_path)
    privacy_val.validate(privacy)

    # Validate frames.jsonl
    content = frames_path.read_bytes()
    if content.startswith(b"\xef\xbb\xbf"):
        raise ValueError(f"{frames_path} contains a UTF-8 BOM")
    if content and not content.endswith(b"\n"):
        raise ValueError(f"{frames_path} lacks a trailing newline")

    lines = content.decode("utf-8").splitlines()
    if len(lines) != manifest["frame_count"]:
        raise ValueError(
            f"Frame count mismatch in {pkg_dir.name}: manifest declares {manifest['frame_count']}, but frames.jsonl has {len(lines)}"
        )

    last_t_rel = -1
    for expected_seq, line in enumerate(lines, start=1):
        frame = json.loads(line, object_pairs_hook=reject_duplicate_keys)
        frame_val.validate(frame)

        if frame["seq"] != expected_seq:
            raise ValueError(f"{pkg_dir.name}: frame seq out of order: expected {expected_seq}, got {frame['seq']}")
        if frame["t_rel_ms"] < last_t_rel:
            raise ValueError(
                f"{pkg_dir.name}: non-chronological timestamp at seq {expected_seq}: {frame['t_rel_ms']} < {last_t_rel}"
            )
        last_t_rel = frame["t_rel_ms"]


def main() -> int:
    manifest_schema = load_json(SCHEMA_DIR / "evidence-manifest.schema.json")
    frame_schema = load_json(SCHEMA_DIR / "evidence-frame.schema.json")
    privacy_schema = load_json(SCHEMA_DIR / "evidence-privacy.schema.json")

    manifest_val = Draft202012Validator(manifest_schema)
    frame_val = Draft202012Validator(frame_schema)
    privacy_val = Draft202012Validator(privacy_schema)

    packages = sorted([p for p in EVIDENCE_DIR.iterdir() if p.is_dir() and p.name != "schema" and not p.name.startswith(".")])

    if not packages:
        print("No evidence packages found to validate.", file=sys.stderr)
        return 1

    print(f"Validating {len(packages)} evidence packages in {EVIDENCE_DIR}...")
    errors: list[str] = []
    for pkg in packages:
        try:
            validate_evidence_package(pkg, manifest_val, frame_val, privacy_val)
            print(f"  [PASS] {pkg.name}")
        except Exception as e:
            errors.append(f"  [FAIL] {pkg.name}: {e}")
            print(f"  [FAIL] {pkg.name}: {e}", file=sys.stderr)

    if errors:
        print(f"\nEvidence validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"\nAll {len(packages)} evidence packages passed validation cleanly!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
