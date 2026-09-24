"""Validate pre-release Machine KB records and curated IDs without network access.

Requires jsonschema 4.25.1 (see knowledge/tools/requirements-schema.txt).
"""

import json
import sys
import unicodedata
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

SCHEMA_DIR = Path(__file__).resolve().parents[1] / "schema"
COMMON = json.loads((SCHEMA_DIR / "common.schema.json").read_text())
RECORD = json.loads((SCHEMA_DIR / "record.schema.json").read_text())
IDS = json.loads((SCHEMA_DIR / "id-registry.schema.json").read_text())
RESOURCES = Registry().with_resources(
    (schema["$id"], Resource.from_contents(schema)) for schema in (COMMON, RECORD, IDS)
)
RECORD_VALIDATOR = Draft202012Validator(RECORD, registry=RESOURCES)
IDS_VALIDATOR = Draft202012Validator(IDS, registry=RESOURCES)
SAFE_INT = 9007199254740991


def _reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_float(value):
    raise ValueError(f"floating-point JSON number: {value}")


def _parse(line):
    return json.loads(line, object_pairs_hook=_reject_duplicate_keys,
                      parse_float=_reject_float,
                      parse_constant=_reject_float)


def _walk(value):
    if isinstance(value, str):
        if unicodedata.normalize("NFC", value) != value:
            raise ValueError("non-NFC string")
    elif type(value) is int:
        if abs(value) > SAFE_INT:
            raise ValueError("integer outside interoperable range")
    elif isinstance(value, dict):
        for k, v in value.items():
            _walk(k)
            _walk(v)
    elif isinstance(value, list):
        for item in value:
            _walk(item)


def canonical_json(value):
    _walk(value)
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def _sorted_sets(value):
    """All arrays in Phase 2 schemas represent sets; ordered sequences come later."""
    if isinstance(value, dict):
        for key, item in value.items():
            if isinstance(item, list):
                if key in {"provenance", "ids", "aliases"}:
                    index = {"provenance": lambda x: canonical_json(x),
                             "ids": lambda x: x["id"].encode("ascii"),
                             "aliases": lambda x: x["alias"].encode("ascii")}[key]
                else:
                    index = lambda x: (x if isinstance(x, str) else canonical_json(x))
                if item != sorted(item, key=index):
                    raise ValueError(f"unsorted set array: {key}")
                if len({canonical_json(x) for x in item}) != len(item):
                    raise ValueError(f"duplicate set entry: {key}")
            _sorted_sets(item)
    elif isinstance(value, list):
        for item in value:
            _sorted_sets(item)


def validate_record(value):
    RECORD_VALIDATOR.validate(value)
    _walk(value)
    _sorted_sets(value)
    if value["kind"] == "relationship" and value["subject_id"] == value["object_id"]:
        raise ValueError("self relationship")


def validate_registry(value):
    IDS_VALIDATOR.validate(value)
    _walk(value)
    _sorted_sets(value)
    canonical = {entry["id"]: entry for entry in value["ids"]}
    if len(canonical) != len(value["ids"]):
        raise ValueError("duplicate canonical ID")
    alias_names = [entry["alias"] for entry in value["aliases"]]
    if len(set(alias_names)) != len(alias_names):
        raise ValueError("duplicate alias")
    for alias in value["aliases"]:
        if alias["alias"] in canonical or alias["canonical_id"] not in canonical:
            raise ValueError("alias collision, chain, or dangling target")
        if alias["alias"].split(":")[1] != alias["canonical_id"].split(":")[1]:
            raise ValueError("alias kind mismatch")
    for entry in value["ids"]:
        for target in entry.get("replaced_by", []):
            if target not in canonical or canonical[target]["lifecycle"] == "retired":
                raise ValueError("invalid replacement target")


def validate_jsonl(data):
    if not data:
        return []
    if data.startswith(b"\xef\xbb\xbf") or not data.endswith(b"\n"):
        raise ValueError("BOM or missing final LF")
    lines = data.decode("utf-8").splitlines(keepends=True)
    if any(not line.endswith("\n") or "\r" in line for line in lines):
        raise ValueError("invalid line ending")
    records = []
    for line in lines:
        value = _parse(line)
        validate_record(value)
        if line.encode("utf-8") != canonical_json(value) + b"\n":
            raise ValueError("noncanonical JSON bytes")
        records.append(value)
    ids = [record["id"] for record in records]
    if ids != sorted(set(ids), key=lambda x: x.encode("ascii")):
        raise ValueError("unsorted or duplicate record IDs")
    return records


if __name__ == "__main__":
    try:
        for path in map(Path, sys.argv[1:]):
            if path.suffix == ".jsonl":
                validate_jsonl(path.read_bytes())
            else:
                value = _parse(path.read_text(encoding="utf-8"))
                (validate_registry if path.name.endswith("id-registry.json") else validate_record)(value)
        print(f"Schema/serialization validation passed: {len(sys.argv) - 1} files")
    except Exception as exc:
        print(f"Schema/serialization validation failed: {exc}", file=sys.stderr)
        sys.exit(1)
