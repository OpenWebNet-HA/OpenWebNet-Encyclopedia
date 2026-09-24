"""Run with python -m unittest discover -s knowledge/tools -p 'test_schema.py'."""

import copy
import json
import sys
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_schema import (COMMON, IDS, RECORD, _parse, canonical_json,
                             validate_jsonl, validate_record, validate_registry)

FIXTURES = Path(__file__).resolve().parents[1] / "schema" / "fixtures"


class SchemaTests(unittest.TestCase):
    def test_schemas_are_valid_draft_2020_12(self):
        for schema in (COMMON, RECORD, IDS):
            with self.subTest(schema=schema["$id"]):
                Draft202012Validator.check_schema(schema)

    def test_valid_fixtures(self):
        for path in sorted((FIXTURES / "valid").glob("*.json")):
            with self.subTest(path=path.name):
                obj = _parse(path.read_text())
                (validate_registry if path.name == "id-registry.json" else validate_record)(obj)

    def test_invalid_fixtures(self):
        for path in sorted((FIXTURES / "invalid").glob("*.json")):
            with self.subTest(path=path.name):
                obj = _parse(path.read_text())
                with self.assertRaises(Exception):
                    (validate_registry if path.name.endswith("id-registry.json") else validate_record)(obj)

    def test_golden_jsonl(self):
        data = (FIXTURES / "valid" / "golden.jsonl").read_bytes()
        records = validate_jsonl(data)
        self.assertEqual(data, b"".join(canonical_json(r) + b"\n" for r in records))
        self.assertEqual(validate_jsonl(b""), [])

    def test_invalid_serialization(self):
        data = (FIXTURES / "valid" / "golden.jsonl").read_bytes()
        first = _parse(data.splitlines()[0])
        cases = [data[:-1], b"\xef\xbb\xbf" + data, data.replace(b"\n", b"\r\n"),
                 data.splitlines(keepends=True)[::-1], data.replace(b'"id":', b'"id":"ownkb:claim:another","id":', 1),
                 data.replace(b'"kind":', b'"kind": "claim", "kind":', 1),
                 data.replace(b'"confidence":"high"', b'"confidence":"high","float":1.0', 1)]
        for candidate in cases:
            raw = b"".join(candidate) if isinstance(candidate, list) else candidate
            with self.subTest(raw=raw[:60]), self.assertRaises(Exception):
                validate_jsonl(raw)
        first["label"] = "Cafe\u0301"
        with self.assertRaises(ValueError):
            validate_record(first)
        first["label"] = "Lighting"
        first["relationships"] = ["ownkb:relationship:x000002", "ownkb:relationship:x000001"]
        with self.assertRaises(ValueError):
            validate_record(first)

    def test_value_and_epistemic_states(self):
        claim = _parse((FIXTURES / "valid" / "claim.json").read_text())
        for state in ("unknown", "unresolved", "contradictory"):
            value = copy.deepcopy(claim)
            value["value"] = {"state": state, "reason": "Evidence is incomplete"}
            validate_record(value)
            value["value"]["text"] = "invented"
            with self.assertRaises(Exception):
                validate_record(value)
        value = copy.deepcopy(claim)
        value["epistemic_status"] = "contradicted"
        with self.assertRaises(Exception):
            validate_record(value)
        value["relationships"] = ["ownkb:relationship:x000001"]
        value["questions"] = ["ownkb:question:q000001"]
        validate_record(value)

    def test_provenance_scope_and_id_boundaries(self):
        obj = _parse((FIXTURES / "valid" / "entity.json").read_text())
        cases = []
        a = copy.deepcopy(obj)
        a["provenance"][0]["evidence_class"] = "official_specification"
        cases.append(a)  # External evidence requires a public source ID.
        a = copy.deepcopy(obj)
        a["id"] = "ownkb:entity:who:" + "a" * 64
        cases.append(a)
        a = copy.deepcopy(obj)
        a["provenance"][0]["location"]["section_id"] = "ownkb:section:UPPER"
        cases.append(a)
        a = copy.deepcopy(obj)
        a["applicability"]["version"] = {"state": "specified"}
        cases.append(a)
        for value in cases:
            with self.subTest(value=value), self.assertRaises(Exception):
                validate_record(value)
        obj["provenance"][0].update(evidence_class="official_specification", source_id="ownkb:source:s000001")
        obj["privacy"] = {"classification": "sanitized", "removed_value_classes": ["device_id"]}
        validate_record(obj)


if __name__ == "__main__":
    unittest.main()
