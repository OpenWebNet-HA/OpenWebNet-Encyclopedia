"""Build canonical reference registries from curated seeds joined to the shared IR."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from validate_schema import validate_record

REFERENCE_FILES = {
    "namespace": "namespaces.jsonl",
    "term": "glossary.jsonl",
    "source": "sources.jsonl",
    "entity": "entities.jsonl",
    "relationship": "relationships.jsonl",
    "caution": "cautions.jsonl",
    "question": "questions.jsonl",
}
COMMON_SEED_FIELDS = {"id", "kind", "label", "namespace_id", "section_id", "applicability",
                      "cautions", "confidence", "epistemic_status", "questions"}
KIND_SEED_FIELDS = {
    "namespace": {"description"}, "term": {"definition"},
    "entity": {"description", "entity_type"},
    "source": {"title", "publisher", "source_type"},
    "relationship": {"subject_id", "predicate", "object_id", "qualification"},
    "caution": {"text"}, "question": {"text", "resolution_state", "resolution_note"},
}
KIND_REQUIRED_FIELDS = {
    "namespace": {"description"}, "term": {"definition"},
    "entity": {"description", "entity_type"},
    "source": {"title", "publisher", "source_type"},
    "relationship": {"subject_id", "predicate", "object_id"},
    "caution": {"text"}, "question": {"text"},
}


def _index_ir(ir: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    documents = {document["id"]: document for document in ir["documents"]}
    sections = {section["id"]: {"document": document, "section": section}
                for document in ir["documents"] for section in document["sections"]}
    return documents, sections


def _namespace_for_document(document: dict[str, Any]) -> str:
    namespace = document["namespace_context"]["namespace"]
    if namespace.startswith("who:"):
        return "ownkb:namespace:who"
    if namespace == "diagnostic":
        return "ownkb:namespace:diagnostic"
    if document["namespace_context"]["area"] == "device-model":
        return "ownkb:namespace:device-model"
    return "ownkb:namespace:openwebnet"


def _applicability(namespace_id: str) -> dict[str, Any]:
    if namespace_id in {"ownkb:namespace:device-model", "ownkb:namespace:mhcatalogue"}:
        return {"domain": "device_model", "state": "applies", "target": "OpenWebNet Device Model",
                "version": {"state": "unknown"}}
    if namespace_id in {"ownkb:namespace:diagnostic", "ownkb:namespace:open-db"}:
        return {"domain": "diagnostic", "state": "applies", "target": "OpenWebNet diagnostics",
                "version": {"state": "unknown"}}
    if namespace_id == "ownkb:namespace:scenario-devices":
        return {"domain": "implementation", "state": "applies", "target": "MyHOME Suite Scenario Engine",
                "version": {"expression": "3.5.38", "state": "specified"}}
    return {"domain": "protocol", "state": "applies", "target": "OpenWebNet",
            "version": {"state": "unknown"}}


def _base(seed: dict[str, Any], section_index: dict[str, dict[str, Any]]) -> dict[str, Any]:
    if not isinstance(seed, dict) or seed.get("kind") not in KIND_SEED_FIELDS:
        raise ValueError("reference seed has an unknown or missing kind")
    required = {"id", "kind", "label", "namespace_id", "section_id"} | KIND_REQUIRED_FIELDS[seed["kind"]]
    if not required <= set(seed):
        raise ValueError(f"reference seed is missing fields: {seed.get('id', '<unknown>')}")
    unknown = set(seed) - COMMON_SEED_FIELDS - KIND_SEED_FIELDS[seed["kind"]]
    if unknown:
        raise ValueError(f"reference seed has unknown fields: {seed['id']}: {sorted(unknown)}")
    located = section_index.get(seed["section_id"])
    if located is None:
        raise ValueError(f"reference seed has unknown section: {seed['section_id']}")
    document, section = located["document"], located["section"]
    namespace_id = seed["namespace_id"]
    record: dict[str, Any] = {
        "applicability": seed.get("applicability", _applicability(namespace_id)),
        "cautions": sorted(seed.get("cautions", []), key=str.encode),
        "confidence": seed.get("confidence", "high"),
        "context": {"description": f"{seed['label']} in {namespace_id}", "namespace_id": namespace_id},
        "epistemic_status": seed.get("epistemic_status", "corroborated_interpretation"),
        "id": seed["id"],
        "kind": seed["kind"],
        "label": seed["label"],
        "privacy": document["privacy"],
        "provenance": [{"evidence_class": "canonical_documentation", "location": {
            "document_id": document["id"], "path": document["path"], "section_id": section["id"]}}],
        "questions": sorted(seed.get("questions", []), key=str.encode),
        "relationships": [],
    }
    for key in ("description", "definition", "entity_type", "subject_id", "predicate", "object_id",
                "qualification", "text", "resolution_state", "resolution_note", "title", "publisher", "source_type"):
        if key in seed:
            record[key] = seed[key]
    if seed["kind"] == "question":
        record.setdefault("resolution_state", "open")
    return record


def _canonical_sources(ir: dict[str, Any]) -> list[dict[str, Any]]:
    records = []
    for document in ir["documents"]:
        first = document["sections"][0]
        label = first["title"] or document["path"]
        namespace_id = _namespace_for_document(document)
        record = {
            "applicability": _applicability(namespace_id), "cautions": [], "confidence": "high",
            "context": {"description": f"Canonical documentation source in {namespace_id}",
                        "namespace_id": namespace_id},
            "epistemic_status": "corroborated_interpretation", "id": document["source_id"],
            "kind": "source", "label": label, "privacy": document["privacy"],
            "provenance": [{"evidence_class": "canonical_documentation", "location": {
                "document_id": document["id"], "path": document["path"], "section_id": first["id"]}}],
            "publisher": "OpenWebNet Encyclopedia", "questions": [], "relationships": [],
            "source_type": "canonical_documentation", "title": label,
        }
        records.append(record)
    return records


def reference_records(ir: dict[str, Any], seed_path: Path) -> tuple[dict[str, list[dict[str, Any]]], dict[str, list[str]]]:
    _, sections = _index_ir(ir)
    value = json.loads(seed_path.read_text(encoding="utf-8"))
    if set(value) != {"records"} or not isinstance(value["records"], list):
        raise ValueError("reference input must contain only a records array")
    records = [_base(seed, sections) for seed in value["records"]]
    records.extend(_canonical_sources(ir))
    by_id = {record["id"]: record for record in records}
    if len(by_id) != len(records):
        raise ValueError("duplicate curated or generated reference ID")
    relationship_sets: dict[str, set[str]] = defaultdict(set)
    for record in records:
        if record["kind"] == "relationship":
            relationship_sets[record["subject_id"]].add(record["id"])
            relationship_sets[record["object_id"]].add(record["id"])
    for identity, links in relationship_sets.items():
        if identity in by_id:
            by_id[identity]["relationships"] = sorted(links, key=str.encode)
    grouped = {kind: sorted((record for record in records if record["kind"] == kind),
                            key=lambda record: record["id"].encode("ascii"))
               for kind in REFERENCE_FILES}
    for record in records:
        validate_record(record)
    section_refs: dict[str, set[str]] = defaultdict(set)
    for record in records:
        section_refs[record["provenance"][0]["location"]["section_id"]].add(record["id"])
    return grouped, {key: sorted(items, key=str.encode) for key, items in section_refs.items()}
