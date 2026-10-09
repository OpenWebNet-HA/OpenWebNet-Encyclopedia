#!/usr/bin/env python3
"""Register one external artifact without reserializing the whole manifest."""

from __future__ import annotations

import argparse
import copy
import json
import subprocess
import sys
from pathlib import Path

import yaml


FIELD_ORDER = [
    "id",
    "kind",
    "publisher",
    "product",
    "title",
    "media_type",
    "filename",
    "version_label",
    "size",
    "sha256",
    "source_page",
    "source_url",
    "storage",
    "redistribution_status",
    "language",
    "language_evidence",
    "repository_history",
    "notes",
]

REQUIRED = {"id", "kind", "publisher", "filename", "size", "sha256", "media_type", "storage"}


def expected_object_key(artifact: dict) -> str:
    digest = artifact["sha256"]
    suffix = ".pdf" if artifact["kind"] == "documentation" else ""
    return f"sha256/{digest[:2]}/{digest[2:4]}/{digest}{suffix}"


def canonicalize(artifact: dict) -> dict:
    unknown = [key for key in artifact if key not in FIELD_ORDER]
    if unknown:
        raise ValueError(f"unsupported artifact field(s): {', '.join(sorted(unknown))}")
    missing = [key for key in REQUIRED if key not in artifact]
    if missing:
        raise ValueError(f"missing required artifact field(s): {', '.join(sorted(missing))}")

    digest = artifact["sha256"]
    if not isinstance(digest, str) or len(digest) != 64 or digest.lower() != digest:
        raise ValueError("sha256 must be a 64-character lowercase digest")
    try:
        int(digest, 16)
    except ValueError as exc:
        raise ValueError("sha256 must be hexadecimal") from exc

    if not isinstance(artifact["size"], int) or artifact["size"] <= 0:
        raise ValueError("size must be a positive integer")

    storage = artifact["storage"]
    if not isinstance(storage, dict):
        raise ValueError("storage must be an object")
    expected = expected_object_key(artifact)
    supplied = storage.get("object_key")
    if supplied is None:
        storage = copy.deepcopy(storage)
        storage["object_key"] = expected
        artifact = copy.deepcopy(artifact)
        artifact["storage"] = storage
    elif supplied != expected:
        raise ValueError(f"storage.object_key must be {expected}")

    ordered: dict = {}
    for key in FIELD_ORDER:
        if key in artifact:
            ordered[key] = artifact[key]
    return ordered


def artifact_blocks(text: str) -> list[tuple[int, int, dict]]:
    lines = text.splitlines(keepends=True)
    starts = [i for i, line in enumerate(lines) if line.startswith("- id: ")]
    blocks: list[tuple[int, int, dict]] = []
    for pos, start in enumerate(starts):
        end = starts[pos + 1] if pos + 1 < len(starts) else len(lines)
        block_text = "".join(lines[start:end])
        parsed = yaml.safe_load(block_text)
        if not isinstance(parsed, list) or len(parsed) != 1 or not isinstance(parsed[0], dict):
            raise ValueError(f"cannot parse artifact block beginning on line {start + 1}")
        blocks.append((start, end, parsed[0]))
    return blocks


def insert_artifact(text: str, artifact: dict) -> tuple[str, str]:
    manifest = yaml.safe_load(text)
    existing = manifest.get("artifacts", [])
    if not isinstance(existing, list):
        raise ValueError("manifest artifacts must be a list")

    for current in existing:
        if current.get("id") == artifact["id"]:
            if current.get("sha256") == artifact["sha256"]:
                return text, "already-registered"
            raise ValueError(f"artifact id already exists with different bytes: {artifact['id']}")
        if current.get("sha256") == artifact["sha256"]:
            raise ValueError(
                f"sha256 already represented by {current.get('id')}: {artifact['sha256']}"
            )

    blocks = artifact_blocks(text)
    same_kind = [block for block in blocks if block[2].get("kind") == artifact["kind"]]
    if same_kind:
        insert_line = same_kind[-1][1]
        for start, _end, current in same_kind:
            if str(current.get("id", "")) > artifact["id"]:
                insert_line = start
                break
    else:
        insert_line = blocks[-1][1] if blocks else len(text.splitlines(keepends=True))

    rendered = yaml.safe_dump(
        [artifact],
        sort_keys=False,
        allow_unicode=True,
        width=1000000,
        default_flow_style=False,
    )
    lines = text.splitlines(keepends=True)
    lines.insert(insert_line, rendered)
    return "".join(lines), "registered"


def run_checks(root: Path) -> None:
    subprocess.run(
        [sys.executable, "project/review/checks/check_artifact_manifest.py"],
        cwd=root,
        check=True,
    )
    subprocess.run(
        ["git", "diff", "--check", "--", "sources/artifact-manifest.yaml"],
        cwd=root,
        check=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("descriptor", type=Path, help="JSON file containing one artifact object")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=None,
        help="manifest path (defaults to sources/artifact-manifest.yaml)",
    )
    parser.add_argument(
        "--no-validate",
        action="store_true",
        help="skip repository-wide validation (intended only for unit tests)",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    manifest_path = args.manifest or (root / "sources" / "artifact-manifest.yaml")
    artifact = canonicalize(json.loads(args.descriptor.read_text(encoding="utf-8")))
    original = manifest_path.read_text(encoding="utf-8")
    updated, status = insert_artifact(original, artifact)

    if status == "already-registered":
        print(f"already registered: {artifact['id']} {artifact['sha256']}")
        return 0

    manifest_path.write_text(updated, encoding="utf-8")
    if not args.no_validate:
        try:
            run_checks(root)
        except Exception:
            manifest_path.write_text(original, encoding="utf-8")
            raise

    print(f"registered: {artifact['id']} {artifact['sha256']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
