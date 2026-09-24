"""Join reviewed atomic assertions to the privacy-gated canonical IR."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from serialization import json_bytes
from validate_schema import validate_record


def section_digest(section: dict) -> str:
    # Anchor the reviewed assertion to the entire prepared section, including structure.
    return hashlib.sha256(json_bytes(section)).hexdigest()


def claim_records(ir: dict, references: dict, seed_path: Path) -> list[dict]:
    seeds = json.loads(seed_path.read_text(encoding="utf-8"))
    if set(seeds) != {"claims"} or not isinstance(seeds["claims"], list):
        raise ValueError("claim input must contain only a claims array")
    sections = {section["id"]: (doc, section) for doc in ir["documents"] for section in doc["sections"]}
    refs = {r["id"]: r for group in references.values() for r in group}
    sources = {doc["id"]: doc["source_id"] for doc in ir["documents"]}
    records = []
    allowed = {"id", "label", "statement", "subject_id", "namespace_id", "section_id",
               "section_sha256", "evidence_class", "source_id", "evidence_note", "epistemic_status",
               "confidence", "applicability", "cautions", "questions", "claim_links", "value"}
    required = allowed - {"source_id", "evidence_note"}
    for seed in seeds["claims"]:
        if set(seed) - allowed or not required <= set(seed):
            raise ValueError(f"invalid claim seed fields: {seed.get('id', '<unknown>')}")
        identity = seed["id"]
        if seed["section_id"] not in sections:
            raise ValueError(f"claim section missing: {identity}")
        doc, section = sections[seed["section_id"]]
        digest = section_digest(section)
        if digest != seed["section_sha256"]:
            raise ValueError(f"claim source section changed; review and repin {identity}: {doc['path']}")
        subject = refs.get(seed["subject_id"])
        if not subject or subject["kind"] != "entity":
            raise ValueError(f"claim subject is not a canonical entity: {identity}")
        if seed["namespace_id"] not in refs or refs[seed["namespace_id"]]["kind"] != "namespace":
            raise ValueError(f"claim namespace missing: {identity}")
        source_id = seed.get("source_id", sources[doc["id"]])
        if source_id not in refs or refs[source_id]["kind"] != "source":
            raise ValueError(f"claim public source missing: {identity}")
        if seed["evidence_class"] == "canonical_documentation" and source_id != sources[doc["id"]]:
            raise ValueError(f"canonical source does not match section: {identity}")
        for field, kind in (("cautions", "caution"), ("questions", "question")):
            if any(target not in refs or refs[target]["kind"] != kind for target in seed[field]):
                raise ValueError(f"claim has dangling {field}: {identity}")
        provenance = {"evidence_class": seed["evidence_class"], "source_id": source_id,
                      "location": {"document_id": doc["id"], "path": doc["path"], "section_id": section["id"]}}
        if "evidence_note" in seed:
            provenance["evidence_note"] = seed["evidence_note"]
        record = {"id": identity, "kind": "claim", "label": seed["label"], "statement": seed["statement"],
                  "subject_id": seed["subject_id"], "context": {"namespace_id": seed["namespace_id"],
                  "description": subject["label"]}, "source_section_sha256": digest,
                  "provenance": [provenance], "privacy": doc["privacy"], "applicability": seed["applicability"],
                  "epistemic_status": seed["epistemic_status"], "confidence": seed["confidence"],
                  "relationships": [], "cautions": seed["cautions"], "questions": seed["questions"],
                  "claim_links": seed["claim_links"], "value": seed["value"]}
        validate_record(record)
        records.append(record)
    by_id = {r["id"]: r for r in records}
    if len(by_id) != len(records):
        raise ValueError("duplicate claim ID")
    for record in records:
        links = record["claim_links"]
        for relation, targets in links.items():
            for target in targets:
                if target == record["id"] or target not in by_id:
                    raise ValueError(f"dangling or self claim link: {record['id']} -> {target}")
                if relation == "contradicts":
                    peer = by_id[target]
                    if record["id"] not in peer["claim_links"]["contradicts"]:
                        raise ValueError(f"asymmetric contradiction: {record['id']} -> {target}")
                    if record["subject_id"] != peer["subject_id"] or record["context"]["namespace_id"] != peer["context"]["namespace_id"]:
                        raise ValueError(f"contradiction lacks common subject and namespace: {record['id']}")
                    if not record["questions"] or not peer["questions"]:
                        raise ValueError("contradiction needs open resolution on both assertions")
    return sorted(records, key=lambda r: r["id"].encode("ascii"))
