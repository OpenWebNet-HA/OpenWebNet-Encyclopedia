#!/usr/bin/env python3
"""Build current deterministic Machine KB infrastructure and manifest."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "knowledge" / "tools"))
from build_ir import build as build_ir  # noqa: E402
from serialization import json_bytes, write_bytes  # noqa: E402

GENERATOR_VERSION = "ownkb-build-0.1.0"
SCHEMA_COMPATIBILITY_VERSION = "0.1.0"
MANIFEST_FORMAT_VERSION = "0.1.0"


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def public_artifacts(root: Path) -> list[dict[str, object]]:
    """Inventory current public data contracts; later renderers add their own specs here."""
    paths = sorted((root / "knowledge" / "schema").glob("*.schema.json"),
                   key=lambda path: path.as_posix().encode("utf-8"))
    return [{
        "format_version": SCHEMA_COMPATIBILITY_VERSION,
        "kind": "schema",
        "path": str(path.relative_to(root)),
        "sha256": sha256_bytes(path.read_bytes()),
    } for path in paths]


def manifest(root: Path) -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="ownkb-ir-") as temporary:
        ir = build_ir(root, root / "knowledge/inputs/canonical-sources.jsonl",
                      root / "knowledge/inputs/identities.json")
        # `identities` repeats a curated input map, so it is not semantic IR output.
        ir.pop("identities", None)
        input_digest = sha256_bytes(json_bytes(ir))
    return {
        "artifacts": public_artifacts(root),
        "format_version": MANIFEST_FORMAT_VERSION,
        "generator_version": GENERATOR_VERSION,
        "input_content_sha256": input_digest,
        "schema_compatibility_version": SCHEMA_COMPATIBILITY_VERSION,
    }


def build(root: Path, output_root: Path) -> Path:
    result = manifest(root)
    target = output_root / "knowledge" / "manifest.json"
    write_bytes(target, json_bytes(result))
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root")
    parser.add_argument("--output-root", type=Path, default=ROOT,
                        help="root for generated files; use an empty temporary directory in CI")
    args = parser.parse_args()
    try:
        root = args.root.resolve()
        output_root = args.output_root.resolve()
        target = build(root, output_root)
        print(f"wrote {target.relative_to(output_root)} with {len(manifest(root)['artifacts'])} artifacts")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"Machine KB build failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
