#!/usr/bin/env python3
"""Build deterministic Machine KB artifacts from the one shared semantic IR."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "knowledge" / "tools"))
from build_ir import build as build_ir  # noqa: E402
from render_artifacts import (bootstrap_chunk_identities, chunk_records, corpus,
                              load_chunk_identities)  # noqa: E402
from render_references import REFERENCE_FILES, reference_records  # noqa: E402
from render_claims import claim_coverage_metrics, claim_records  # noqa: E402
from serialization import json_bytes, jsonl_bytes, write_bytes  # noqa: E402

GENERATOR_VERSION = "ownkb-build-0.7.0"
SCHEMA_COMPATIBILITY_VERSION = "0.1.0"
MANIFEST_FORMAT_VERSION = "0.1.0"
CHUNK_IDENTITIES = ROOT / "knowledge/inputs/chunk-identities.json"


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def artifact(path: str, kind: str, content: bytes, record_count: int | None = None) -> dict[str, object]:
    result: dict[str, object] = {"format_version": SCHEMA_COMPATIBILITY_VERSION, "kind": kind,
                                 "path": path, "sha256": sha256_bytes(content)}
    if record_count is not None:
        result["record_count"] = record_count
    return result


def public_artifacts(root: Path, output_root: Path, document_count: int, chunk_count: int,
                     reference_counts: dict[str, int], claim_count: int) -> list[dict[str, object]]:
    schemas = [artifact(str(path.relative_to(root)), "schema", path.read_bytes())
               for path in (root / "knowledge/schema").glob("*.schema.json")]
    generated = [
        artifact("knowledge/claims/claims.jsonl", "claim_records",
                 (output_root / "knowledge/claims/claims.jsonl").read_bytes(), claim_count),
        artifact("knowledge/llm/llm-corpus.md", "llm_corpus",
                 (output_root / "knowledge/llm/llm-corpus.md").read_bytes(), document_count),
        artifact("knowledge/retrieval/chunks.jsonl", "retrieval_chunks",
                 (output_root / "knowledge/retrieval/chunks.jsonl").read_bytes(), chunk_count),
    ]
    generated.extend(artifact(f"knowledge/reference/{filename}", "reference_registry",
                              (output_root / "knowledge/reference" / filename).read_bytes(), reference_counts[kind])
                     for kind, filename in REFERENCE_FILES.items())
    return sorted([*schemas, *generated], key=lambda entry: str(entry["path"]).encode("utf-8"))


def coverage(ir: dict[str, object], chunk_metrics: dict[str, int], reference_counts: dict[str, int], claim_metrics: dict) -> dict[str, object]:
    documents = ir["documents"]
    assert isinstance(documents, list)
    return {
        "canonical": {"documents": len(documents), "sections": sum(len(document["sections"]) for document in documents),
                      "sanitized_documents": sum(document["privacy"]["classification"] == "sanitized" for document in documents)},
        "guides": {"excluded_documents": len({item["path"] for item in ir["guide_remediation"]}),
                   "remediation_hints": len(ir["guide_remediation"])},
        "llm_corpus": {"included_documents": len(documents),
                       "included_sections": sum(len(document["sections"]) for document in documents)},
        "references": {"records": sum(reference_counts.values())},
        "claims": claim_metrics,
        "retrieval": chunk_metrics,
    }


def manifest(ir: dict[str, object], output_root: Path, root: Path, chunk_metrics: dict[str, int],
             reference_records_by_kind: dict[str, list[dict[str, object]]], claims: list[dict], claim_metrics: dict) -> dict[str, object]:
    ir_digest = dict(ir)
    ir_digest.pop("identities", None)
    documents = ir["documents"]
    assert isinstance(documents, list)
    reference_counts = {kind: len(records) for kind, records in reference_records_by_kind.items()}
    return {
        "artifacts": public_artifacts(root, output_root, len(documents), chunk_metrics["emitted_chunks"], reference_counts, len(claims)),
        "coverage": coverage(ir, chunk_metrics, reference_counts, claim_metrics),
        "format_version": MANIFEST_FORMAT_VERSION,
        "generator_version": GENERATOR_VERSION,
        "input_content_sha256": sha256_bytes(json_bytes({"ir": ir_digest, "references": reference_records_by_kind, "claims": claims})),
        "schema_compatibility_version": SCHEMA_COMPATIBILITY_VERSION,
    }


def build(root: Path, output_root: Path) -> Path:
    ir = build_ir(root, root / "knowledge/inputs/canonical-sources.jsonl", root / "knowledge/inputs/identities.json")
    references, section_references = reference_records(ir, root / "knowledge/inputs/reference-records.json")
    claims = claim_records(ir, references, root / "knowledge/inputs/claim-records.json")
    claim_metrics = claim_coverage_metrics(ir, claims, root / "knowledge/inputs/claim-coverage.json")
    namespace_ids = {}
    for document in ir["documents"]:
        namespace = document["namespace_context"]["namespace"]
        namespace_ids[document["id"]] = ("ownkb:namespace:who" if namespace.startswith("who:") else
                                         "ownkb:namespace:diagnostic" if namespace == "diagnostic" else
                                         "ownkb:namespace:device-model" if document["namespace_context"]["area"] == "device-model" else
                                         "ownkb:namespace:openwebnet")
    identities = load_chunk_identities(root / "knowledge/inputs/chunk-identities.json")
    records, metrics = chunk_records(ir, identities, section_references, namespace_ids)
    expected_sections = {section["id"] for document in ir["documents"] for section in document["sections"] if section["blocks"]}
    if set(identities) != expected_sections:
        raise ValueError("curated retrieval chunk identity mapping is stale or incomplete")
    target_corpus = output_root / "knowledge/llm/llm-corpus.md"
    target_chunks = output_root / "knowledge/retrieval/chunks.jsonl"
    write_bytes(target_corpus, corpus(ir))
    write_bytes(target_chunks, jsonl_bytes(records))
    write_bytes(output_root / "knowledge/claims/claims.jsonl", jsonl_bytes(claims))
    for kind, filename in REFERENCE_FILES.items():
        write_bytes(output_root / "knowledge/reference" / filename, jsonl_bytes(references[kind]))
    target_manifest = output_root / "knowledge/manifest.json"
    write_bytes(target_manifest, json_bytes(manifest(ir, output_root, root, metrics, references, claims, claim_metrics)))
    return target_manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root")
    parser.add_argument("--output-root", type=Path, default=ROOT,
                        help="root for generated files; use a clean temporary directory in CI")
    parser.add_argument("--bootstrap-chunk-identities", action="store_true",
                        help="one-time initial allocation; review and commit before routine builds")
    args = parser.parse_args()
    try:
        root, output_root = args.root.resolve(), args.output_root.resolve()
        if args.bootstrap_chunk_identities:
            ir = build_ir(root, root / "knowledge/inputs/canonical-sources.jsonl", root / "knowledge/inputs/identities.json")
            mapping = bootstrap_chunk_identities(ir)
            write_bytes(root / "knowledge/inputs/chunk-identities.json", json_bytes(mapping))
            print(f"allocated {len(mapping)} curated retrieval chunk identities")
            return 0
        target = build(root, output_root)
        print(f"wrote {target.relative_to(output_root)}")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"Machine KB build failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
