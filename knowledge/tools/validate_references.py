"""Cross-file referential-integrity checks for public Machine KB registries."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from render_references import REFERENCE_FILES
from validate_schema import validate_jsonl


def load_registries(output_root: Path) -> dict[str, list[dict[str, Any]]]:
    result = {}
    for kind, filename in REFERENCE_FILES.items():
        records = validate_jsonl((output_root / "knowledge/reference" / filename).read_bytes())
        if any(record["kind"] != kind for record in records):
            raise ValueError(f"reference registry kind mismatch: {filename}")
        result[kind] = records
    return result


def validate_integrity(output_root: Path, chunks: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    registries = load_registries(output_root)
    records = [record for values in registries.values() for record in values]
    by_id = {record["id"]: record for record in records}
    if len(by_id) != len(records):
        raise ValueError("reference registries contain a duplicate stable ID")

    documents = {chunk["document_id"]: chunk["source_path"] for chunk in chunks}
    sections = {chunk["section_id"]: (chunk["document_id"], chunk["source_path"]) for chunk in chunks}
    chunk_ids = {chunk["id"] for chunk in chunks}
    known = set(by_id) | set(documents) | set(sections) | chunk_ids
    namespaces = {record["id"] for record in registries["namespace"]}
    sources = {record["id"] for record in registries["source"]}

    for record in records:
        if record["context"]["namespace_id"] not in namespaces:
            raise ValueError(f"dangling namespace reference in {record['id']}")
        for field, kind in (("relationships", "relationship"), ("cautions", "caution"), ("questions", "question")):
            for target in record[field]:
                if target not in by_id or by_id[target]["kind"] != kind:
                    raise ValueError(f"dangling {field} reference in {record['id']}: {target}")
        for provenance in record["provenance"]:
            location = provenance["location"]
            if location["document_id"] not in documents or documents[location["document_id"]] != location["path"]:
                raise ValueError(f"invalid provenance document/path in {record['id']}")
            if location["section_id"] not in sections or sections[location["section_id"]] != (location["document_id"], location["path"]):
                raise ValueError(f"invalid provenance section in {record['id']}")
            if "source_id" in provenance and provenance["source_id"] not in sources:
                raise ValueError(f"dangling provenance source in {record['id']}")
        if record["kind"] == "relationship":
            for field in ("subject_id", "object_id"):
                if record[field] not in known:
                    raise ValueError(f"dangling relationship endpoint in {record['id']}: {record[field]}")

    source_by_document = {}
    for source in (record for record in registries["source"]
                   if record["source_type"] == "canonical_documentation"):
        document_id = source["provenance"][0]["location"]["document_id"]
        if document_id in source_by_document:
            raise ValueError(f"multiple canonical source records for {document_id}")
        source_by_document[document_id] = source["id"]
    if set(source_by_document) != set(documents):
        raise ValueError("public source registry does not cover the canonical document set")

    for chunk in chunks:
        references = chunk["reference_ids"]
        if references != sorted(set(references), key=str.encode):
            raise ValueError(f"unsorted or duplicate chunk reference IDs: {chunk['id']}")
        if any(reference not in by_id for reference in references):
            raise ValueError(f"dangling chunk reference in {chunk['id']}")
        if source_by_document[chunk["document_id"]] not in references:
            raise ValueError(f"chunk omits its canonical source record: {chunk['id']}")
        if not any(reference.startswith("ownkb:namespace:") for reference in references):
            raise ValueError(f"chunk omits namespace reference: {chunk['id']}")
    return registries
