"""Join reviewed evidence observations to claims and sections, without inferring methods."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from jsonschema import Draft202012Validator
from serialization import json_bytes


def load_reviews(root: Path, ir: dict, references: dict, claim_ids: set[str]) -> dict:
    value = json.loads((root / "knowledge/inputs/evidence-reviews.json").read_text())
    schema = json.loads((root / "knowledge/schema/evidence-reviews.schema.json").read_text())
    Draft202012Validator(schema).validate(value)
    refs = {r["id"]: r for group in references.values() for r in group}
    sections = {s["id"]: (d, s) for d in ir["documents"] for s in d["sections"]}
    by_claim, by_section = defaultdict(list), defaultdict(list)
    seen = set()
    for finding in value["findings"]:
        identity = finding["id"]
        if identity in seen:
            raise ValueError(f"duplicate evidence finding: {identity}")
        seen.add(identity)
        if finding["section_id"] not in sections:
            raise ValueError(f"evidence finding has missing section: {identity}")
        if set(finding["claim_ids"]) - claim_ids:
            raise ValueError(f"evidence finding has dangling claims: {identity}")
        if finding["disposition"] in {"claimed", "corroborates"} and not finding["claim_ids"]:
            raise ValueError(f"materialized evidence finding lacks claims: {identity}")
        if finding["disposition"] in {"deferred", "excluded"} and finding["claim_ids"]:
            raise ValueError(f"unmaterialized evidence finding has claims: {identity}")
        review = root / finding["review_path"]
        if not review.is_file() or finding["review_locator"] not in review.read_text():
            raise ValueError(f"evidence finding has unresolvable review locator: {identity}")
        doc, section = sections[finding["section_id"]]
        supports = []
        for support in finding["supports"]:
            source = refs.get(support["source_id"])
            if not source or source["kind"] != "source" or "artifact_locator" not in source:
                raise ValueError(f"evidence finding lacks an original artifact source: {identity}")
            locator = source["artifact_locator"]
            examination = support["examination"]
            if locator["kind"] == "git_file":
                code = examination.get("code_location")
                if not code or code["start_line"] > code["end_line"] or code["end_line"] > locator["line_count"]:
                    raise ValueError(f"evidence code location exceeds pinned file: {identity}")
                if locator["repository"].startswith("MyOpenCommunity/") and support["evidence_class"] != "implementation_artifact":
                    raise ValueError(f"archived implementation misclassified: {identity}")
            if "artifact_location" in examination:
                offsets = examination["artifact_location"]
                if offsets["start_offset"] > offsets["end_offset"]:
                    raise ValueError(f"reversed artifact location: {identity}")
            if "execution" in examination:
                run = examination["execution"]
                run_record = root / run["record_path"]
                if not run_record.is_file() or run["record_locator"] not in run_record.read_text():
                    raise ValueError(f"unresolvable execution record: {identity}")
            if set(examination["claim_ids"]) - set(finding["claim_ids"]):
                raise ValueError(f"examination refers outside finding: {identity}")
            entry = {"source_id": source["id"], "evidence_class": support["evidence_class"],
                     "location": {"document_id": doc["id"], "path": doc["path"], "section_id": section["id"]},
                     "examination": {**examination, "finding_id": identity,
                                     "review_path": finding["review_path"]}}
            supports.append(entry)
        materialized = {"finding_id": identity, "summary": finding["summary"],
                        "disposition": finding["disposition"], "reason": finding["reason"],
                        "claim_ids": finding["claim_ids"], "provenance": sorted(supports, key=json_bytes)}
        by_section[section["id"]].append(materialized)
        for claim_id in finding["claim_ids"]:
            by_claim[claim_id].extend(e for e in supports if claim_id in e["examination"]["claim_ids"])
    return {"claims": dict(by_claim), "sections": dict(by_section)}


def join_claim_evidence(claims: list[dict], reviews: dict, references: dict) -> None:
    """Keep explanatory-document provenance distinct from underlying support."""
    refs = {r["id"]: r for group in references.values() for r in group}
    canonical = {r["provenance"][0]["location"]["document_id"]: r["id"]
                 for r in references["source"] if r["source_type"] == "canonical_documentation"}
    for claim in claims:
        entries = reviews["claims"].get(claim["id"], [])
        if not entries:
            if refs.get(claim["provenance"][0].get("source_id"), {}).get("artifact_locator") is not None:
                raise ValueError(f"pinned artifact claim lacks reviewed examination: {claim['id']}")
            continue
        location = claim["provenance"][0]["location"]
        if any(e["location"] != location for e in entries):
            raise ValueError(f"claim/finding section mismatch: {claim['id']}")
        primary = claim["provenance"][0]
        if refs.get(primary.get("source_id"), {}).get("artifact_locator") is not None:
            matching = [e for e in entries if e["source_id"] == primary["source_id"]
                        and e["examination"]["relationship"] == "supports"]
            if not matching:
                raise ValueError(f"implementation claim lacks primary examination: {claim['id']}")
            primary.update(matching[0])
            locator = refs[primary["source_id"]]["artifact_locator"]
            if locator.get("repository", "").startswith("MyOpenCommunity/") and claim["applicability"]["domain"] != "implementation":
                raise ValueError(f"implementation-only claim has wider applicability: {claim['id']}")
            if locator.get("revision", locator.get("version")) not in claim["applicability"]["version"].get("expression", ""):
                raise ValueError(f"implementation claim lacks exact revision scope: {claim['id']}")
        for entry in entries:
            if entry not in claim["provenance"]:
                claim["provenance"].append(entry)
        doc_source = canonical[location["document_id"]]
        if not any(e.get("source_id") == doc_source and e["evidence_class"] == "canonical_documentation"
                   for e in claim["provenance"]):
            claim["provenance"].append({"location": location, "source_id": doc_source,
                                        "evidence_class": "canonical_documentation",
                                        "evidence_note": "Explanatory Encyclopedia section; not independent original evidence."})
        claim["provenance"].sort(key=json_bytes)


def corpus_evidence(findings: list[dict], sources: dict) -> list[str]:
    lines = []
    for finding in findings:
        lines.extend([f"Evidence finding `{finding['finding_id']}` ({finding['disposition']}): {finding['summary']}",
                      f"Disposition reason: {finding['reason']}"])
        if finding["claim_ids"]:
            lines.append("Individual claims: " + ", ".join(f"`{i}`" for i in finding["claim_ids"]))
        for entry in finding["provenance"]:
            ex = entry["examination"]
            locator = sources[entry["source_id"]]["artifact_locator"]
            if locator["kind"] == "git_file":
                code = ex["code_location"]
                original = (f"[{locator['repository']} - {code['symbol']}]({locator['public_uri']}"
                            f"#L{code['start_line']}-L{code['end_line']}) at `{locator['revision']}`")
            else:
                original = f"{locator['label']} at `{locator['version']}`, SHA-256 `{locator['sha256']}`"
                if "public_uri" in locator:
                    original = f"[{original}]({locator['public_uri']})"
                original += "; " + json.dumps(ex.get("artifact_location", ex.get("code_location")), sort_keys=True)
            lines.append(f"- `{entry['source_id']}`: {ex['method']}; {ex['implementation_role']}; "
                         f"{ex['conclusion_kind']}; {ex['relationship']}. "
                         f"{original}. Review: `{ex['review_path']}`.")
            lines.append("  Examination claims: " + (", ".join(ex["claim_ids"]) or "none - review context or unmaterialized finding"))
            for label in ("conditions", "limitations"):
                if ex[label]:
                    lines.append(f"  {label.capitalize()}: " + "; ".join(ex[label]))
            if "execution" in ex:
                run = ex["execution"]
                lines.append(f"  Execution record: {run['material']} - {run['result']}; {run['setup']}. "
                             f"Inputs: {'; '.join(run['inputs'])}. Record: `{run['record_path']}` ({run['record_locator']}).")
        lines.append("")
    return lines
