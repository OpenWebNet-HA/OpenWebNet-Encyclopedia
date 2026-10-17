"""Allocate identities only for newly selected accepted Device definitions.

This is an explicit contributor action, never part of a routine build. Existing
document/heading and chunk mappings must remain byte-for-byte equivalent data.
"""
import argparse
import json
import re
from pathlib import Path

from build_ir import ROOT, build
from source_topology import device_sources


def allocate(root: Path) -> dict:
    inputs = root / "knowledge/inputs"
    identity_path = inputs / "identities.json"
    chunk_path = inputs / "chunk-identities.json"
    old = json.loads(identity_path.read_text(encoding="utf-8"))
    chunks = json.loads(chunk_path.read_text(encoding="utf-8"))
    selected = {r["path"] for r in device_sources(root) if r["state"] == "integrated"}
    result = build(root, inputs / "canonical-sources.jsonl", identity_path, bootstrap=True)
    if any(result["identities"].get(path) != entry for path, entry in old.items()):
        raise ValueError("existing document/heading identity changed; semantic review is required")
    if set(result["identities"]) - set(old) - selected:
        raise ValueError("allocator may add only explicitly selected Device documents")
    expected = {s["id"] for d in result["documents"] for s in d["sections"] if s["blocks"]}
    if set(chunks) - expected:
        raise ValueError("existing chunk section disappeared; lifecycle review is required")
    history = json.loads((inputs / "id-registry.json").read_text(encoding="utf-8"))["ids"]
    maximum = max([0] + [int(m[1]) for identity in [*chunks.values(), *(r["id"] for r in history)]
                        if (m := re.fullmatch(r"ownkb:chunk:r(\d+)", identity))])
    for section in sorted(expected - set(chunks)):
        maximum += 1
        chunks[section] = f"ownkb:chunk:r{maximum:06d}"
    for path, value in ((identity_path, result["identities"]), (chunk_path, chunks)):
        path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return {"new_documents": len(result["identities"]) - len(old), "chunks": len(chunks)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    print(json.dumps(allocate(args.root.resolve()), sort_keys=True))
