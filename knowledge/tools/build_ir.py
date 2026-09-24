#!/usr/bin/env python3
"""Prepare canonical Markdown through the privacy gate, then parse one shared IR."""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

from prepare_sources import prepare, read_manifest

ROOT = Path(__file__).resolve().parents[2]
AREAS = ("protocol", "functional", "diagnostics", "programming", "device-model", "internals", "reverse-engineering")
MANIFEST = ROOT / "knowledge/inputs/canonical-sources.jsonl"
IDENTITIES = ROOT / "knowledge/inputs/identities.json"


def canonical_paths(root: Path) -> list[str]:
    return sorted(str(p.relative_to(root)) for area in AREAS for p in (root / area).rglob("*.md"))


def guide_findings(root: Path, canonical: list[str]) -> list[dict[str, object]]:
    """Conservative remediation hints, never an extraction source or a factual claim."""
    corpus = {re.sub(r"\s+", " ", line.strip().lower()) for path in canonical
              for line in (root / path).read_text(encoding="utf-8").splitlines()}
    result = []
    for path in sorted((root / "guides").rglob("*.md")):
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            value = re.sub(r"\s+", " ", line.strip().lower())
            # A flag invites human review. It does not assert that a guide has a unique fact.
            if (len(value) >= 45 and value not in corpus and not value.startswith(("#", "| ---", "```"))
                    and re.search(r"\b(?:is|are|means|uses|returns|reports|contains|requires|identifies|indicates|supports|cannot|must)\b", value)):
                result.append({"path": str(path.relative_to(root)), "line": number, "status": "review-guide-only-fact"})
    return result


def build(root: Path, manifest: Path, identities: Path, bootstrap: bool = False) -> dict:
    paths = canonical_paths(root)
    entries = read_manifest(manifest)
    declared = [r["source_path"] for r in entries if r["source_type"] == "canonical_documentation"]
    if sorted(declared) != paths or len(set(declared)) != len(declared):
        raise ValueError("closed source manifest differs from complete canonical documentation tree")
    if any(str(r["source_path"]).startswith("guides/") for r in entries):
        raise ValueError("procedural guide included in canonical source manifest")
    records = prepare(manifest, root)
    mapping = json.loads(identities.read_text(encoding="utf-8")) if identities.exists() else {}
    if set(mapping) - set(paths):
        raise ValueError("stale document identity; update mapping without recycling IDs")
    node = os.environ.get("CODEX_PRIMARY_RUNTIME_NODE", "node")
    modules = os.environ.get("CODEX_PRIMARY_RUNTIME_NODE_MODULES", "")
    env = dict(os.environ)
    if modules:
        env["NODE_PATH"] = modules
    command = [node, str(Path(__file__).with_name("parse_markdown.mjs"))]
    result = subprocess.run(command, input=json.dumps({"records": records, "identities": mapping, "bootstrap": bootstrap}),
                            text=True, capture_output=True, env=env, check=False)
    if result.returncode:
        # Parser diagnostics contain paths and construct names, never input text.
        raise ValueError(result.stderr.strip().splitlines()[0] if result.stderr else "Markdown parser failed")
    output = json.loads(result.stdout)
    if len(output["documents"]) != len(paths):
        raise ValueError("canonical document count mismatch")
    document_ids = [doc["id"] for doc in output["documents"]]
    section_ids = [section["id"] for doc in output["documents"] for section in doc["sections"]]
    if len(set(document_ids)) != len(document_ids) or len(set(section_ids)) != len(section_ids):
        raise ValueError("duplicate curated document or section identity")
    if any(not re.fullmatch(r"ownkb:document:[a-z][a-z0-9-]*", identity) for identity in document_ids):
        raise ValueError("invalid curated document identity")
    if any(not re.fullmatch(r"ownkb:section:[a-z][a-z0-9-]*:[a-z][a-z0-9-]*", identity) for identity in section_ids):
        raise ValueError("invalid curated section identity")
    output["guide_remediation"] = guide_findings(root, paths)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    parser.add_argument("--identities", type=Path, default=IDENTITIES)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--bootstrap-identities", action="store_true", help="initial allocation only; review and commit mapping")
    args = parser.parse_args()
    try:
        result = build(args.root, args.manifest, args.identities, args.bootstrap_identities)
        if args.bootstrap_identities:
            args.identities.parent.mkdir(parents=True, exist_ok=True)
            args.identities.write_text(json.dumps(result["identities"], ensure_ascii=False, sort_keys=True,
                                                   separators=(",", ":")) + "\n", encoding="utf-8")
        del result["identities"]
        # The IR is an internal build product. Never publish it as a release artifact.
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(unicodedata.normalize("NFC", json.dumps(result, ensure_ascii=False, sort_keys=True,
                             separators=(",", ":"))) + "\n", encoding="utf-8")
        print(f"parsed {len(result['documents'])} canonical documents; {len(result['guide_remediation'])} guide review hints")
    except (OSError, ValueError) as error:
        print(f"IR build failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
