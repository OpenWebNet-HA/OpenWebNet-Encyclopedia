"""Reference-registry and high-risk semantic boundary tests."""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BUILD = load("ownkb_reference_build", ROOT / "build.py")
VALIDATE = load("ownkb_reference_validation", ROOT / "knowledge/tools/validate_references.py")


class ReferenceRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory()
        cls.output = Path(cls.temporary.name)
        BUILD.build(ROOT, cls.output)
        cls.chunks = [json.loads(line) for line in
                      (cls.output / "knowledge/retrieval/chunks.jsonl").read_text().splitlines()]
        cls.registries = VALIDATE.validate_integrity(cls.output, cls.chunks)
        cls.by_id = {record["id"]: record for values in cls.registries.values() for record in values}

    @classmethod
    def tearDownClass(cls):
        cls.temporary.cleanup()

    def test_canonical_source_registry_covers_every_document(self):
        canonical = [record for record in self.registries["source"]
                     if record["source_type"] == "canonical_documentation"]
        external = [record for record in self.registries["source"]
                    if record["source_type"] != "canonical_documentation"]
        self.assertEqual(123, len(canonical))
        self.assertEqual(12, len(external))
        self.assertEqual({chunk["document_id"] for chunk in self.chunks},
                         {record["provenance"][0]["location"]["document_id"]
                          for record in canonical})

    def test_identity_and_address_records_are_explicitly_distinct(self):
        distinctions = {(record["subject_id"], record["object_id"])
                        for record in self.registries["relationship"]
                        if record["predicate"] == "distinct_from"}
        device_id = "ownkb:entity:diagnostic:installed-device-id"
        self.assertIn((device_id, "ownkb:entity:diagnostic:where"), distinctions)
        self.assertIn((device_id, "ownkb:entity:where:functional"), distinctions)
        self.assertEqual("protocol_identity", self.by_id[device_id]["entity_type"])
        self.assertEqual("address", self.by_id["ownkb:entity:diagnostic:where"]["entity_type"])
        self.assertEqual("address", self.by_id["ownkb:entity:where:functional"]["entity_type"])

    def test_device_model_boundaries_have_one_canonical_glossary_definition(self):
        expected = {
            "physical-device": "physical_device", "firmware": "firmware", "module": "module",
            "object": "object", "configuration": "configuration",
        }
        for key, entity_type in expected.items():
            term_id = f"ownkb:term:{key}"
            entity_id = f"ownkb:entity:device-model:{key}"
            with self.subTest(key=key):
                self.assertIn("definition", self.by_id[term_id])
                self.assertNotIn("definition", self.by_id[entity_id])
                self.assertEqual(entity_type, self.by_id[entity_id]["entity_type"])
                self.assertIn(term_id, self.by_id[entity_id]["description"])
                self.assertTrue(any(record["subject_id"] == entity_id and
                                    record["object_id"] == term_id and
                                    record["predicate"] == "defined_in"
                                    for record in self.registries["relationship"]))

    def test_retrieval_chunks_reference_canonical_records(self):
        by_section = {chunk["section_id"]: chunk for chunk in self.chunks}
        identity = set(by_section["ownkb:section:d000108:s000004"]["reference_ids"])
        self.assertIn("ownkb:caution:k000002", identity)
        self.assertIn("ownkb:relationship:x000018", identity)
        model = set(by_section["ownkb:section:d000006:s000001"]["reference_ids"])
        self.assertIn("ownkb:term:physical-device", model)
        self.assertIn("ownkb:entity:device-model:physical-device", model)
        question = set(by_section["ownkb:section:d000121:s000003"]["reference_ids"])
        self.assertIn("ownkb:question:q000001", question)

    def test_dangling_reference_is_rejected(self):
        original = self.chunks[0]["reference_ids"]
        self.chunks[0]["reference_ids"] = [*original, "ownkb:term:missing"]
        self.chunks[0]["reference_ids"].sort(key=str.encode)
        try:
            with self.assertRaisesRegex(ValueError, "dangling chunk reference"):
                VALIDATE.validate_integrity(self.output, self.chunks)
        finally:
            self.chunks[0]["reference_ids"] = original


if __name__ == "__main__":
    unittest.main()
