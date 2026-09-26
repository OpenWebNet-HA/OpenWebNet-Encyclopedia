#!/usr/bin/env python3
"""Validate cross-artifact Machine KB consistency and emit deterministic coverage reports."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

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
