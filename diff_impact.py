#!/usr/bin/env python3
"""Map a Git diff to Machine KB records that require review."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
CANONICAL_AREAS = (
    "protocol", "functional", "diagnostics", "programming", "device-model",
    "internals", "reverse-engineering", "scenario-engine",
)
GLOBAL_INPUTS = {
    "knowledge/inputs/identities.json",
    "knowledge/inputs/chunk-identities.json",
    "knowledge/inputs/canonical-sources.jsonl",
}
CLAIM_INPUTS = {
    "knowledge/inputs/claim-records.json",
    "knowledge/inputs/claim-coverage.json",
}
REFERENCE_INPUTS = {"knowledge/inputs/reference-records.json"}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def ownkb_ids(value: Any) -> set[str]:
    result: set[str] = set()
    if isinstance(value, str):
        if value.startswith("ownkb:"):
            result.add(value)
    elif isinstance(value, dict):
        for item in value.values():
            result.update(ownkb_ids(item))
    elif isinstance(value, list):
        for item in value:
            result.update(ownkb_ids(item))
    return result


def parse_name_status(text: str) -> list[dict[str, str]]:
    changes = []
    for line in text.splitlines():
        if not line:
            continue
        fields = line.split("\t")
        status = fields[0]
        kind = status[0]
        if kind in {"R", "C"} and len(fields) == 3:
            changes.append({"status": kind, "old_path": fields[1], "path": fields[2]})
        elif len(fields) == 2:
            changes.append({"status": kind, "path": fields[1]})
        else:
            raise ValueError(f"unrecognized git name-status line: {line}")
    return changes


def git_changes(root: Path, base: str, head: str) -> list[dict[str, str]]:
    if head == "WORKTREE":
        command = ["git", "-C", str(root), "diff", "--name-status", "-M", base, "--"]
    else:
        command = ["git", "-C", str(root), "diff", "--name-status", "-M", base, head, "--"]
    result = subprocess.run(command, text=True, capture_output=True, check=False)
    if result.returncode:
        raise ValueError(result.stderr.strip() or "git diff failed")
    changes = parse_name_status(result.stdout)
    if head == "WORKTREE":
        untracked = subprocess.run(
            ["git", "-C", str(root), "ls-files", "--others", "--exclude-standard"],
            text=True, capture_output=True, check=False,
        )
        if untracked.returncode:
            raise ValueError(untracked.stderr.strip() or "git ls-files failed")
        known = {change["path"] for change in changes}
        known.update(change.get("old_path", "") for change in changes)
        for path in untracked.stdout.splitlines():
            if path and path not in known:
                changes.append({"status": "A", "path": path})
    return sorted(changes, key=lambda item: (item["path"], item["status"]))


def canonical_path(path: str) -> bool:
    return path.endswith(".md") and path.split("/", 1)[0] in CANONICAL_AREAS


def seed_indices(root: Path) -> dict[str, Any]:
    identities = load_json(root / "knowledge/inputs/identities.json")
    chunks = load_json(root / "knowledge/inputs/chunk-identities.json")
    claims = load_json(root / "knowledge/inputs/claim-records.json")["claims"]
    references = load_json(root / "knowledge/inputs/reference-records.json")["records"]

    generated_refs = []
    for path in sorted((root / "knowledge/reference").glob("*.jsonl")):
        generated_refs.extend(load_jsonl(path))

    claims_by_section: dict[str, set[str]] = {}
    claim_by_id = {claim["id"]: claim for claim in claims}
    for claim in claims:
        claims_by_section.setdefault(claim["section_id"], set()).add(claim["id"])

    refs_by_section: dict[str, set[str]] = {}
    ref_by_id = {record["id"]: record for record in references}
    for record in references:
        section_id = record.get("section_id")
        if section_id:
            refs_by_section.setdefault(section_id, set()).add(record["id"])

    source_ids_by_path: dict[str, set[str]] = {}
    for record in generated_refs:
        if record.get("kind") != "source":
            continue
        for provenance in record.get("provenance", []):
            path = provenance.get("location", {}).get("path")
            if path:
                source_ids_by_path.setdefault(path, set()).add(record["id"])

    return {
        "identities": identities,
        "chunks": chunks,
        "claims": claims,
        "claim_by_id": claim_by_id,
        "claims_by_section": claims_by_section,
        "references": references,
        "ref_by_id": ref_by_id,
        "refs_by_section": refs_by_section,
        "source_ids_by_path": source_ids_by_path,
    }


def close_reference_dependencies(index: dict[str, Any], direct: set[str]) -> set[str]:
    impacted = set(direct)
    changed = True
    while changed:
        changed = False
        for record in index["references"]:
            if record["id"] in impacted:
                continue
            if ownkb_ids(record) & impacted:
                impacted.add(record["id"])
                changed = True
    return impacted


def close_claim_dependencies(index: dict[str, Any], direct_claims: set[str], impacted_refs: set[str]) -> set[str]:
    impacted = set(direct_claims)
    changed = True
    while changed:
        changed = False
        for claim in index["claims"]:
            if claim["id"] in impacted:
                continue
            referenced = ownkb_ids({
                "subject_id": claim.get("subject_id"),
                "namespace_id": claim.get("namespace_id"),
                "source_id": claim.get("source_id"),
                "cautions": claim.get("cautions", []),
                "questions": claim.get("questions", []),
                "claim_links": claim.get("claim_links", {}),
            })
            if referenced & (impacted_refs | impacted):
                impacted.add(claim["id"])
                changed = True
    return impacted


def canonical_impact(index: dict[str, Any], path: str, status: str) -> dict[str, Any]:
    identity = index["identities"].get(path)
    if not identity:
        return {
            "path": path,
            "status": status,
            "classification": "canonical_documentation",
            "full_review_required": True,
            "reason": "canonical path has no curated identity; structural allocation/review required",
        }

    sections = set(identity["sections"].values())
    direct_claims = set().union(*(index["claims_by_section"].get(s, set()) for s in sections))
    direct_refs = set().union(*(index["refs_by_section"].get(s, set()) for s in sections))
    source_refs = index["source_ids_by_path"].get(path, set())
    refs = close_reference_dependencies(index, direct_refs | source_refs)
    claims = close_claim_dependencies(index, direct_claims, refs)
    chunks = {index["chunks"][s] for s in sections if s in index["chunks"]}

    return {
        "path": path,
        "status": status,
        "classification": "canonical_documentation",
        "document_id": identity["id"],
        "section_ids": sorted(sections),
        "chunk_ids": sorted(chunks),
        "reference_ids": sorted(refs),
        "claim_ids": sorted(claims),
        "direct_claim_ids": sorted(direct_claims),
        "full_review_required": status in {"A", "D", "R"},
        "review_scope": "document_and_transitive_records",
    }


def analyze_changes(root: Path, changes: list[dict[str, str]]) -> dict[str, Any]:
    index = seed_indices(root)
    impacts = []
    full_review = False
    generated_outputs_changed = False

    for change in changes:
        status = change["status"]
        paths = [change["path"]]
        if "old_path" in change:
            paths.insert(0, change["old_path"])

        for path in paths:
            if canonical_path(path):
                impact = canonical_impact(index, path, status)
            elif path.startswith("guides/") and path.endswith(".md"):
                impact = {
                    "path": path,
                    "status": status,
                    "classification": "procedural_guide",
                    "claim_ids": [],
                    "reference_ids": [],
                    "full_review_required": False,
                    "guide_fact_review_required": True,
                    "reason": "guides are excluded from canonical claims/corpus but guide-only fact detection must rerun",
                }
            elif path in GLOBAL_INPUTS:
                impact = {
                    "path": path,
                    "status": status,
                    "classification": "stable_identity_or_source_topology",
                    "full_review_required": True,
                    "reason": "stable identity/source topology change can affect every projection",
                }
            elif path in CLAIM_INPUTS:
                impact = {
                    "path": path,
                    "status": status,
                    "classification": "reviewed_claim_input",
                    "full_review_required": False,
                    "claim_subsystem_review_required": True,
                    "reason": "reviewed claim or coverage input changed",
                }
            elif path in REFERENCE_INPUTS:
                impact = {
                    "path": path,
                    "status": status,
                    "classification": "reviewed_reference_input",
                    "full_review_required": False,
                    "reference_subsystem_review_required": True,
                    "reason": "reviewed reference input changed",
                }
            elif path.startswith("knowledge/schema/") or path.startswith("knowledge/tools/") or path in {"build.py", "check.py", "diff_impact.py"}:
                impact = {
                    "path": path,
                    "status": status,
                    "classification": "build_or_schema_infrastructure",
                    "full_review_required": True,
                    "reason": "schema/build semantics can affect the complete public dataset",
                }
            elif path.startswith("knowledge/claims/") or path.startswith("knowledge/reference/") or path.startswith("knowledge/retrieval/") or path.startswith("knowledge/llm/") or path == "knowledge/manifest.json":
                generated_outputs_changed = True
                impact = {
                    "path": path,
                    "status": status,
                    "classification": "generated_output",
                    "full_review_required": False,
                    "generated_output_review_required": True,
                    "reason": "generated outputs must be reproduced by build.py rather than hand-edited",
                }
            elif path.startswith("sources/"):
                impact = {
                    "path": path,
                    "status": status,
                    "classification": "public_evidence_source",
                    "full_review_required": False,
                    "evidence_review_required": True,
                    "reason": "public evidence change requires provenance-scoped review",
                }
            else:
                impact = {
                    "path": path,
                    "status": status,
                    "classification": "non_machine_kb_or_control",
                    "full_review_required": False,
                }
            impacts.append(impact)
            full_review = full_review or bool(impact.get("full_review_required"))

    impacts.sort(key=lambda item: (item["path"], item["status"]))
    return {
        "format_version": "0.1.0",
        "full_review_required": full_review,
        "generated_outputs_changed": generated_outputs_changed,
        "changes": impacts,
        "summary": {
            "changed_paths": len(impacts),
            "affected_claim_ids": len({x for item in impacts for x in item.get("claim_ids", [])}),
            "affected_reference_ids": len({x for item in impacts for x in item.get("reference_ids", [])}),
            "affected_chunk_ids": len({x for item in impacts for x in item.get("chunk_ids", [])}),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--base", default="HEAD")
    parser.add_argument("--head", default="WORKTREE",
                        help="Git revision to compare, or WORKTREE for staged+unstaged changes")
    parser.add_argument("--fail-on-full-review", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        changes = git_changes(root, args.base, args.head)
        report = analyze_changes(root, changes)
        print(json.dumps(report, indent=2, sort_keys=True))
        if args.fail_on_full_review and report["full_review_required"]:
            return 2
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"Machine KB diff impact failed: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
