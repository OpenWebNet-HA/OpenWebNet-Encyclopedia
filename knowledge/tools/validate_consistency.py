#!/usr/bin/env python3
"""Validate cross-artifact Machine KB consistency and emit deterministic coverage reports."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from id_lifecycle import emitted_ids, validate_lifecycle

ROOT = Path(__file__).resolve().parents[2]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        raise ValueError(f"missing generated artifact: {path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}")
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def validate_cross_artifact(root: Path, output_root: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    identities = load_json(root / "knowledge/inputs/identities.json")
    chunk_identities = load_json(root / "knowledge/inputs/chunk-identities.json")
    claim_seeds = load_json(root / "knowledge/inputs/claim-records.json")["claims"]
    coverage = load_json(root / "knowledge/inputs/claim-coverage.json")

    claims = load_jsonl(output_root / "knowledge/claims/claims.jsonl")
    chunks = load_jsonl(output_root / "knowledge/retrieval/chunks.jsonl")

    reference_entries = [
        entry for entry in manifest["artifacts"]
        if entry["kind"] == "reference_registry"
    ]
    reference_records: list[dict[str, Any]] = []
    for entry in reference_entries:
        reference_records.extend(load_jsonl(output_root / entry["path"]))

    canonical = manifest["coverage"]["canonical"]
    retrieval = manifest["coverage"]["retrieval"]
    claim_metrics = manifest["coverage"]["claims"]
    reference_metrics = manifest["coverage"]["references"]
    lifecycle_entries = [entry for entry in manifest["artifacts"] if entry["kind"] == "id_registry"]
    if len(lifecycle_entries) != 1:
        raise ValueError("manifest must contain exactly one ID lifecycle registry")
    lifecycle = load_json(output_root / lifecycle_entries[0]["path"])
    lifecycle_metrics = validate_lifecycle(lifecycle, emitted_ids(claims, chunks, reference_records))

    if canonical["documents"] != len(identities):
        raise ValueError("canonical document coverage does not match curated identities")
    if retrieval["emitted_chunks"] != len(chunks):
        raise ValueError("retrieval coverage does not match generated chunk count")
    if set(chunk_identities.values()) != {record["id"] for record in chunks}:
        raise ValueError("retrieval chunk identities differ from generated chunks")
    if set(chunk_identities) != {record["section_id"] for record in chunks}:
        raise ValueError("retrieval section identities differ from generated chunks")
    if claim_metrics["records"] != len(claims) or len(claims) != len(claim_seeds):
        raise ValueError("claim coverage, generated claims, and reviewed claim seeds disagree")
    if {record["id"] for record in claims} != {record["id"] for record in claim_seeds}:
        raise ValueError("generated claim IDs differ from reviewed claim IDs")
    if reference_metrics["records"] != len(reference_records):
        raise ValueError("reference coverage does not match generated registry count")
    if any(record["source_path"].startswith("guides/") for record in chunks):
        raise ValueError("procedural guide entered retrieval output")
    if any(
        claim["provenance"][0]["location"]["path"].startswith("guides/")
        for claim in claims
    ):
        raise ValueError("procedural guide entered claim output")

    # Reviewed underlying evidence must survive both claim and retrieval generation.
    ledger = load_json(root / "knowledge/inputs/evidence-reviews.json")["findings"]
    published_findings = {f["finding_id"]: (chunk, f) for chunk in chunks
                          for f in chunk.get("evidence_support", [])}
    if set(published_findings) != {f["id"] for f in ledger}:
        raise ValueError("reviewed evidence dispositions differ from retrieval output")
    by_claim = {c["id"]: c for c in claims}
    sources = {r["id"]: r for r in reference_records if r["kind"] == "source"}
    for finding in ledger:
        chunk, public = published_findings[finding["id"]]
        if chunk["section_id"] != finding["section_id"]:
            raise ValueError("evidence finding entered the wrong retrieval section")
        for key in ("summary", "disposition", "reason", "claim_ids"):
            if public[key] != finding[key]:
                raise ValueError("retrieval evidence lost reviewed qualification")
        expected = []
        for support in finding["supports"]:
            source = sources.get(support["source_id"])
            if not source or "artifact_locator" not in source or source["id"] not in chunk["reference_ids"]:
                raise ValueError("retrieval evidence lost original source reference")
            entry = {"source_id": support["source_id"], "evidence_class": support["evidence_class"],
                     "location": {"document_id": chunk["document_id"], "path": chunk["source_path"],
                                  "section_id": chunk["section_id"]},
                     "examination": {**support["examination"], "finding_id": finding["id"],
                                     "review_path": finding["review_path"]}}
            expected.append(entry)
            for claim_id in entry["examination"]["claim_ids"]:
                if claim_id not in by_claim or entry not in by_claim[claim_id]["provenance"]:
                    raise ValueError("claim output lost its reviewed original examination")
        if len(expected) != len(public["provenance"]) or any(e not in public["provenance"] for e in expected):
            raise ValueError("retrieval output lost reviewed examination conditions")

    bounded = claim_metrics["bounded_domains"]
    if sum(domain["claims"] for domain in bounded.values()) != len(claims):
        raise ValueError("bounded-domain claim totals do not match generated claim count")

    coverage_by_area = {domain["area"]: domain for domain in coverage["domains"]}
    if set(coverage_by_area) != set(bounded):
        raise ValueError("reviewed claim coverage areas differ from manifest bounded domains")

    for area, metrics in bounded.items():
        rows = coverage_by_area[area]["sections"]
        claimed = sum(row["status"] == "claimed" for row in rows)
        nonclaim = sum(row["status"] == "nonclaim" for row in rows)
        if len(rows) != metrics["sections"]:
            raise ValueError(f"section coverage mismatch: {area}")
        if claimed != metrics["sections_with_claims"]:
            raise ValueError(f"claimed-section coverage mismatch: {area}")
        if nonclaim != metrics["reviewed_nonclaim_sections"]:
            raise ValueError(f"nonclaim-section coverage mismatch: {area}")
        if claimed + nonclaim != len(rows):
            raise ValueError(f"unaccounted claim coverage section: {area}")

    report = {
        "canonical": {
            "documents": canonical["documents"],
            "sections": canonical["sections"],
        },
        "claims": {
            "records": len(claims),
            "domains": {
                area: {
                    "claims": bounded[area]["claims"],
                    "documents": bounded[area]["documents"],
                    "reviewed_nonclaim_sections": bounded[area]["reviewed_nonclaim_sections"],
                    "sections": bounded[area]["sections"],
                    "sections_with_claims": bounded[area]["sections_with_claims"],
                }
                for area in sorted(bounded)
            },
        },
        "guides": {
            "excluded_documents": manifest["coverage"]["guides"]["excluded_documents"],
            "remediation_hints": manifest["coverage"]["guides"]["remediation_hints"],
        },
        "id_lifecycle": lifecycle_metrics,
        "references": {"records": len(reference_records)},
        "retrieval": {
            "chunks": len(chunks),
            "empty_sections": retrieval["empty_sections"],
        },
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output-root", type=Path)
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    output_root = (args.output_root or root).resolve()
    try:
        manifest = load_json(output_root / "knowledge/manifest.json")
        report = validate_cross_artifact(root, output_root, manifest)
        if args.report:
            print(json.dumps(report, indent=2, sort_keys=True))
        else:
            print("Machine KB cross-artifact consistency passed")
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"Machine KB cross-artifact consistency failed: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
