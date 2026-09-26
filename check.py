#!/usr/bin/env python3
"""Check deterministic Machine KB build outputs without modifying the repository."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "knowledge" / "tools"))
from serialization import json_bytes, jsonl_bytes  # noqa: E402
from validate_consistency import validate_cross_artifact  # noqa: E402
from validate_references import REFERENCE_FILES, validate_integrity  # noqa: E402
from validate_schema import validate_jsonl  # noqa: E402


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_keys)


def validate_manifest(path: Path) -> dict:
    schema = load_json(ROOT / "knowledge/schema/manifest.schema.json")
    value = load_json(path)
    Draft202012Validator(schema).validate(value)
    if path.read_bytes() != json_bytes(value):
        raise ValueError("manifest does not use canonical JSON bytes")
    paths = [entry["path"] for entry in value["artifacts"]]
    if paths != sorted(set(paths), key=lambda item: item.encode("utf-8")):
        raise ValueError("manifest artifact paths are unsorted or duplicated")
    return value


def validate_chunks(path: Path) -> list[dict]:
    schema = load_json(ROOT / "knowledge/schema/retrieval-chunks.schema.json")
    privacy = load_json(ROOT / "knowledge/schema/privacy-metadata.schema.json")
    registry = Registry().with_resources((item["$id"], Resource.from_contents(item)) for item in (schema, privacy))
    validator = Draft202012Validator(schema, registry=registry)
    content = path.read_bytes()
    if content.startswith(b"\xef\xbb\xbf") or (content and not content.endswith(b"\n")):
        raise ValueError("chunks contain a BOM or lack a final LF")
    records = [json.loads(line, object_pairs_hook=reject_duplicate_keys) for line in content.decode("utf-8").splitlines()]
    for record in records:
        validator.validate(record)
    if content != jsonl_bytes(records):
        raise ValueError("chunks do not use canonical JSONL bytes")
    return records


def validate_corpus(path: Path, expected_documents: int) -> None:
    content = path.read_text(encoding="utf-8")
    if content.startswith("\ufeff") or not content.endswith("\n") or "\r" in content:
        raise ValueError("LLM corpus has invalid text encoding or line endings")
    if unicodedata.normalize("NFC", content) != content:
        raise ValueError("LLM corpus contains non-NFC text")
    if content.count("# Document: ownkb:document:") != expected_documents:
        raise ValueError("LLM corpus document boundary count does not match manifest")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def artifact_path(entry: dict, output_root: Path) -> Path:
    path = Path(entry["path"])
    return ROOT / path if entry["kind"] == "schema" else output_root / path


def validate_artifacts(manifest: dict, output_root: Path) -> None:
    for entry in manifest["artifacts"]:
        path = artifact_path(entry, output_root)
        if not path.is_file():
            raise ValueError(f"manifest artifact is missing: {entry['path']}")
        if sha256(path) != entry["sha256"]:
            raise ValueError(f"manifest artifact hash is stale: {entry['path']}")
    chunks = validate_chunks(output_root / "knowledge/retrieval/chunks.jsonl")
    registries = validate_integrity(output_root, chunks)
    claims = validate_jsonl((output_root / "knowledge/claims/claims.jsonl").read_bytes())
    refs = {record["id"]: record for group in registries.values() for record in group}
    source_sections = {chunk["section_id"]: chunk for chunk in chunks}
    claim_ids = {claim["id"] for claim in claims}
    if len(claim_ids) != len(claims):
        raise ValueError("duplicate claim ID")
    for claim in claims:
        if claim["subject_id"] not in refs or refs[claim["subject_id"]]["kind"] != "entity":
            raise ValueError(f"dangling claim subject: {claim['id']}")
        if claim["context"]["namespace_id"] not in refs or refs[claim["context"]["namespace_id"]]["kind"] != "namespace":
            raise ValueError(f"dangling claim namespace: {claim['id']}")
        location = claim["provenance"][0]["location"]
        section = source_sections.get(location["section_id"])
        if not section or (section["document_id"], section["source_path"]) != (location["document_id"], location["path"]):
            raise ValueError(f"invalid claim section provenance: {claim['id']}")
        for provenance in claim["provenance"]:
            if provenance["source_id"] not in refs or refs[provenance["source_id"]]["kind"] != "source":
                raise ValueError(f"dangling claim source: {claim['id']}")
        for field, kind in (("cautions", "caution"), ("questions", "question")):
            if any(refs.get(x, {}).get("kind") != kind for x in claim[field]):
                raise ValueError(f"dangling claim {field}: {claim['id']}")
        for relation, targets in claim["claim_links"].items():
            for target in targets:
                if target == claim["id"] or target not in claim_ids:
                    raise ValueError(f"dangling claim {relation}: {claim['id']}")
                if relation == "contradicts":
                    peer = next(x for x in claims if x["id"] == target)
                    if claim["id"] not in peer["claim_links"]["contradicts"] or not claim["questions"] or not peer["questions"]:
                        raise ValueError(f"unqualified or asymmetric claim contradiction: {claim['id']}")
    claim_entry = next((entry for entry in manifest["artifacts"] if entry["kind"] == "claim_records"), None)
    if not claim_entry or claim_entry["record_count"] != len(claims) or manifest["coverage"]["claims"]["records"] != len(claims):
        raise ValueError("claim inventory or coverage mismatch")
    retrieval = manifest["coverage"]["retrieval"]
    if len(chunks) != retrieval["emitted_chunks"]:
        raise ValueError("retrieval chunk count does not match coverage")
    corpus_count = next(entry["record_count"] for entry in manifest["artifacts"] if entry["kind"] == "llm_corpus")
    chunk_count = next(entry["record_count"] for entry in manifest["artifacts"] if entry["kind"] == "retrieval_chunks")
    if len(chunks) != chunk_count:
        raise ValueError("retrieval chunk count does not match manifest")
    reference_count = sum(len(records) for records in registries.values())
    if reference_count != manifest["coverage"]["references"]["records"]:
        raise ValueError("reference record count does not match coverage")
    reference_entries = {Path(entry["path"]).name: entry for entry in manifest["artifacts"]
                         if entry["kind"] == "reference_registry"}
    if set(reference_entries) != set(REFERENCE_FILES.values()):
        raise ValueError("manifest reference registry inventory is incomplete")
    for kind, records in registries.items():
        entry = reference_entries[REFERENCE_FILES[kind]]
        if entry["record_count"] != len(records):
            raise ValueError(f"reference registry count does not match manifest: {entry['path']}")
    validate_corpus(output_root / "knowledge/llm/llm-corpus.md", corpus_count)


def command_build(output_root: Path) -> None:
    result = subprocess.run([sys.executable, str(ROOT / "build.py"), "--root", str(ROOT),
                             "--output-root", str(output_root)], text=True, capture_output=True, check=False)
    if result.returncode:
        raise ValueError(result.stderr.strip() or "build command failed")


def compare_outputs(first: Path, second: Path, manifest: dict) -> None:
    expected = ["knowledge/manifest.json", *[entry["path"] for entry in manifest["artifacts"] if entry["kind"] != "schema"]]
    for relative in expected:
        if (first / relative).read_bytes() != (second / relative).read_bytes():
            raise ValueError(f"double build produced different bytes for {relative}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    if args.root.resolve() != ROOT:
        print("Machine KB check failed: this check must run from its repository root", file=sys.stderr)
        return 1
    try:
        with tempfile.TemporaryDirectory(prefix="ownkb-check-") as temporary:
            base = Path(temporary)
            first, second = base / "first", base / "second"
            command_build(first)
            command_build(second)
            manifest = validate_manifest(first / "knowledge/manifest.json")
            compare_outputs(first, second, manifest)
            validate_artifacts(manifest, first)
            validate_cross_artifact(ROOT, first, manifest)
            committed = ROOT / "knowledge/manifest.json"
            if not committed.is_file() or committed.read_bytes() != (first / "knowledge/manifest.json").read_bytes():
                raise ValueError("committed manifest is missing or stale; run python build.py")
            committed_manifest = validate_manifest(committed)
            validate_artifacts(committed_manifest, ROOT)
            validate_cross_artifact(ROOT, ROOT, committed_manifest)
        privacy = subprocess.run([sys.executable, str(ROOT / "knowledge/tools/validate_privacy.py")], cwd=ROOT,
                                 text=True, capture_output=True, check=False)
        if privacy.returncode:
            raise ValueError(privacy.stderr.strip() or "privacy validation failed")
        print("Machine KB check passed: deterministic artifacts, manifest, schemas, cross-artifact consistency, references, and privacy gate")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"Machine KB check failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
