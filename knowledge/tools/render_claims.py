"""Join reviewed atomic assertions to the privacy-gated canonical IR."""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

from serialization import json_bytes
from validate_schema import validate_record


def section_digest(section: dict) -> str:
    # Anchor the reviewed assertion to the entire prepared section, including structure.
    return hashlib.sha256(json_bytes(section)).hexdigest()


DEICTIC_FRAGMENT = re.compile(r"^(?:These include|These definitions|They should be interpreted)\b", re.IGNORECASE)
EPISTEMIC_META = re.compile(
    r"^(?:(?:Level|Outcome|Status)\b.*\binferred\b|Do not\b.*\binferred\b|"
    r"The inferred evidence label\b)",
    re.IGNORECASE,
)
DIRECT_IMPLEMENTATION_ASSERTION = re.compile(
    r"(?:implementation data distinguishes operations|Established implementation role|"
    r"^The exact MyHOME_Suite templates|^The MyHOME_Suite labels distinguish)",
    re.IGNORECASE,
)
WHO17_IMPLEMENTATION = {f"ownkb:claim:c{number:06d}" for number in range(2181, 2193)}
WHO4_IMPLEMENTATION = {f"ownkb:claim:c{number:06d}" for number in range(3210, 3229)}
ADDRESS_IMPLEMENTATION = {
    "ownkb:claim:c000225", "ownkb:claim:c000265", "ownkb:claim:c000266",
    "ownkb:claim:c000267", "ownkb:claim:c000268", "ownkb:claim:c000269",
}
EXAMPLE_SCOPES = {
    **{f"ownkb:claim:c{number:06d}": "192" for number in range(4270, 4285)},
    **{f"ownkb:claim:c{number:06d}": "157" for number in range(5724, 5730)},
    **{f"ownkb:claim:c{number:06d}": "157" for number in range(5801, 5811)},
    **{f"ownkb:claim:c{number:06d}": "157" for number in range(6078, 6085)},
    **{f"ownkb:claim:c{number:06d}": "157" for number in range(6252, 6258)},
}
NEGATED_POLICY = {
    "ownkb:claim:c004733", "ownkb:claim:c004734", "ownkb:claim:c004735",
    "ownkb:claim:c004736", "ownkb:claim:c004737",
    "ownkb:claim:c006004", "ownkb:claim:c006005", "ownkb:claim:c006006",
    "ownkb:claim:c006007", "ownkb:claim:c006494", "ownkb:claim:c006495",
}
EPISTEMIC_META_REVIEW = {
    "ownkb:claim:c006460", "ownkb:claim:c006494", "ownkb:claim:c006633",
    "ownkb:claim:c006900", "ownkb:claim:c007081", "ownkb:claim:c007420",
}
GENUINE_INFERENCES = {
    "ownkb:claim:c000230", "ownkb:claim:c006339", "ownkb:claim:c006827",
}
EVIDENCE_LABELS = {f"ownkb:claim:c{number:06d}" for number in range(7417, 7421)}
DIRECT_IMPLEMENTATION_SOURCES = {
    "ownkb:claim:c001338": "ownkb:source:s000125",
    "ownkb:claim:c001339": "ownkb:source:s000124",
    "ownkb:claim:c001558": "ownkb:source:s000125",
    "ownkb:claim:c001566": "ownkb:source:s000125",
    "ownkb:claim:c001571": "ownkb:source:s000125",
    "ownkb:claim:c002195": "ownkb:source:s000126",
    "ownkb:claim:c002542": "ownkb:source:s000125",
    "ownkb:claim:c002579": "ownkb:source:s000125",
    "ownkb:claim:c002611": "ownkb:source:s000125",
    "ownkb:claim:c003193": "ownkb:source:s000126",
    "ownkb:claim:c003233": "ownkb:source:s000126",
    "ownkb:claim:c003261": "ownkb:source:s000126",
    "ownkb:claim:c003278": "ownkb:source:s000125",
    "ownkb:claim:c003314": "ownkb:source:s000126",
}


def validate_claim_context(seed: dict, source_id: str) -> None:
    """Fail closed on the context and provenance boundaries repaired in Phase 16."""
    identity, statement = seed["id"], seed["statement"].strip()
    if statement in {"Do not:", "This section uses:"} or DEICTIC_FRAGMENT.search(statement):
        raise ValueError(f"claim is not standalone and context-preserving: {identity}")
    if seed["epistemic_status"] == "inferred" and EPISTEMIC_META.search(statement):
        raise ValueError(f"epistemic keyword leaked into claim classification: {identity}")
    if seed["evidence_class"] == "official_specification" and DIRECT_IMPLEMENTATION_ASSERTION.search(statement):
        raise ValueError(f"implementation assertion uses official-spec provenance: {identity}")

    if identity in WHO17_IMPLEMENTATION | WHO4_IMPLEMENTATION | ADDRESS_IMPLEMENTATION:
        version = seed["applicability"]["version"]
        if (seed["evidence_class"], source_id, seed["applicability"]["domain"],
                version.get("expression"), version["state"]) not in {
                    ("public_database", "ownkb:source:s000125", "implementation", "3.5.38", "specified"),
                    ("public_database", "ownkb:source:s000126", "implementation", "3.5.38", "specified"),
                }:
            raise ValueError(f"curated implementation provenance regressed: {identity}")
    if identity in EXAMPLE_SCOPES:
        version = seed["applicability"]["version"]
        if version != {"expression": EXAMPLE_SCOPES[identity], "state": "specified"}:
            raise ValueError(f"firmware example scope regressed: {identity}")
    if identity in NEGATED_POLICY and not re.match(r"^Do not\b", statement, re.IGNORECASE):
        raise ValueError(f"governing list negation was lost: {identity}")
    if identity in EPISTEMIC_META_REVIEW and seed["epistemic_status"] == "inferred":
        raise ValueError(f"reviewed epistemic meta-claim regressed: {identity}")
    if identity in GENUINE_INFERENCES and seed["epistemic_status"] != "inferred":
        raise ValueError(f"reviewed genuine inference regressed: {identity}")
    if identity in EVIDENCE_LABELS and seed["evidence_class"] != "canonical_documentation":
        raise ValueError(f"evidence-label vocabulary provenance regressed: {identity}")
    if identity in DIRECT_IMPLEMENTATION_SOURCES:
        version = seed["applicability"]["version"]
        if (seed["evidence_class"], source_id, seed["applicability"]["domain"], version) != (
                "public_database", DIRECT_IMPLEMENTATION_SOURCES[identity], "implementation",
                {"expression": "3.5.38", "state": "specified"}):
            raise ValueError(f"direct implementation provenance regressed: {identity}")


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
        validate_claim_context(seed, source_id)
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
    semantic_units: dict[tuple, str] = {}
    labelled_units: dict[tuple, dict] = {}
    for record in records:
        normalized = re.sub(r"\s+", " ", unicodedata.normalize("NFC", record["statement"])).strip().casefold()
        scope = json.dumps(record["applicability"], sort_keys=True, separators=(",", ":"))
        semantic_key = (record["subject_id"], record["context"]["namespace_id"], scope, normalized)
        if semantic_key in semantic_units:
            raise ValueError(f"duplicate semantic claim: {semantic_units[semantic_key]} and {record['id']}")
        semantic_units[semantic_key] = record["id"]
        labelled_key = (record["subject_id"], record["context"]["namespace_id"], scope,
                        record["label"].strip().casefold())
        previous = labelled_units.get(labelled_key)
        if previous and record["id"] not in {target for values in previous["claim_links"].values() for target in values}:
            raise ValueError(f"incompatible duplicate claim label: {previous['id']} and {record['id']}")
        labelled_units[labelled_key] = record
    return sorted(records, key=lambda r: r["id"].encode("ascii"))


def claim_coverage_metrics(ir: dict, claims: list[dict], coverage_path: Path) -> dict:
    """Validate the reviewed bounded-batch ledger and return manifest metrics."""
    value = json.loads(coverage_path.read_text(encoding="utf-8"))
    if set(value) != {"format_version", "domains"} or value["format_version"] != "0.1.0":
        raise ValueError("claim coverage input has an unsupported shape or format version")
    if not isinstance(value["domains"], list):
        raise ValueError("claim coverage domains must be an array")
    bounded_areas = ("protocol", "functional", "diagnostics", "programming", "device-model",
                     "internals", "reverse-engineering", "scenario-engine")
    target_documents = {area: [document for document in ir["documents"]
                               if document["path"].startswith(area + "/")]
                        for area in bounded_areas}
    actual_counts = Counter(claim["provenance"][0]["location"]["section_id"] for claim in claims)
    metrics = {"records": len(claims), "bounded_domains": {}}
    seen_areas = set()
    for domain in value["domains"]:
        if set(domain) != {"area", "documents", "sections"} or domain["area"] not in target_documents:
            raise ValueError("claim coverage domain has unknown fields or area")
        area = domain["area"]
        if area in seen_areas:
            raise ValueError(f"duplicate claim coverage area: {area}")
        seen_areas.add(area)
        documents = target_documents[area]
        expected = {section["id"]: document["path"] for document in documents for section in document["sections"]}
        if domain["documents"] != len(documents):
            raise ValueError(f"claim coverage document count mismatch: {area}")
        rows = domain["sections"]
        by_section = {row.get("section_id"): row for row in rows}
        if len(by_section) != len(rows) or set(by_section) != set(expected):
            raise ValueError(f"claim coverage sections are stale, duplicate, or incomplete: {area}")
        claimed = nonclaim = claim_count = 0
        for section_id, row in by_section.items():
            if set(row) != {"claim_count", "path", "reason", "section_id", "status"}:
                raise ValueError(f"claim coverage row has unknown fields: {section_id}")
            if row["path"] != expected[section_id] or row["status"] not in {"claimed", "nonclaim"}:
                raise ValueError(f"invalid claim coverage row: {section_id}")
            count = actual_counts[section_id]
            if row["claim_count"] != count:
                raise ValueError(f"claim coverage count mismatch: {section_id}")
            if row["status"] == "claimed" and count < 1:
                raise ValueError(f"claimed section has no claim: {section_id}")
            if row["status"] == "nonclaim" and count != 0:
                raise ValueError(f"nonclaim section has claims: {section_id}")
            claimed += row["status"] == "claimed"
            nonclaim += row["status"] == "nonclaim"
            claim_count += count
        metrics["bounded_domains"][area] = {
            "claims": claim_count, "documents": len(documents), "sections": len(rows),
            "sections_with_claims": claimed, "reviewed_nonclaim_sections": nonclaim,
        }
    if seen_areas != set(target_documents):
        raise ValueError("claim coverage omits a bounded domain")
    return metrics
