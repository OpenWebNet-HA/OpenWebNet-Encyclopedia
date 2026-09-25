"""Tests for deterministic build infrastructure using only public synthetic values."""
from __future__ import annotations

import copy
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


BUILD = load("ownkb_build", ROOT / "build.py")
CHECK = load("ownkb_check", ROOT / "check.py")
SERIALIZATION = load("ownkb_serialization", ROOT / "knowledge/tools/serialization.py")


class BuildInfrastructureTests(unittest.TestCase):
    def test_serialization_is_canonical_and_rejects_unsafe_numbers(self):
        self.assertEqual('{"a":"é","b":1}\n'.encode(), SERIALIZATION.json_bytes({"b": 1, "a": "é"}))
        self.assertEqual(b"", SERIALIZATION.jsonl_bytes([]))
        records = [{"id": "ownkb:chunk:a"}, {"id": "ownkb:chunk:b"}]
        self.assertEqual(b'{"id":"ownkb:chunk:a"}\n{"id":"ownkb:chunk:b"}\n', SERIALIZATION.jsonl_bytes(records))
        with self.assertRaisesRegex(ValueError, "floating"):
            SERIALIZATION.json_bytes({"value": 1.5})
        with self.assertRaisesRegex(ValueError, "NFC"):
            SERIALIZATION.json_bytes({"value": "e\u0301"})

    def test_clean_temporary_outputs_are_byte_identical(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            one, two = root / "one", root / "two"
            first = BUILD.build(ROOT, one)
            second = BUILD.build(ROOT, two)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            CHECK.validate_manifest(first)
            manifest = json.loads(first.read_text())
            self.assertEqual(sorted(entry["path"] for entry in manifest["artifacts"]),
                             [entry["path"] for entry in manifest["artifacts"]])
            self.assertTrue(all(len(entry["sha256"]) == 64 for entry in manifest["artifacts"]))
            self.assertNotIn("guides/", first.read_text())
            self.assertEqual(134, manifest["coverage"]["canonical"]["documents"])
            self.assertEqual(1149, manifest["coverage"]["retrieval"]["emitted_chunks"])
            self.assertEqual(7342, manifest["coverage"]["claims"]["records"])
            self.assertEqual(651, manifest["coverage"]["claims"]["bounded_domains"]["protocol"]["claims"])
            self.assertEqual(2877, manifest["coverage"]["claims"]["bounded_domains"]["functional"]["claims"])
            self.assertEqual(922, manifest["coverage"]["claims"]["bounded_domains"]["diagnostics"]["claims"])
            self.assertEqual(891, manifest["coverage"]["claims"]["bounded_domains"]["programming"]["claims"])
            self.assertEqual(876, manifest["coverage"]["claims"]["bounded_domains"]["device-model"]["claims"])

    def test_rendered_artifacts_preserve_context_and_exclude_guides(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            manifest_path = BUILD.build(ROOT, output)
            manifest = json.loads(manifest_path.read_text())
            corpus = (output / "knowledge/llm/llm-corpus.md").read_text()
            chunks = [json.loads(line) for line in (output / "knowledge/retrieval/chunks.jsonl").read_text().splitlines()]
            self.assertIn("Source path: `protocol/", corpus)
            self.assertIn("Namespace context:", corpus)
            self.assertIn("Section ID:", corpus)
            self.assertNotIn("Source path: `guides/", corpus)
            self.assertEqual(manifest["coverage"]["retrieval"]["emitted_chunks"], len(chunks))
            self.assertEqual(manifest["coverage"]["retrieval"]["candidate_sections"],
                             manifest["coverage"]["retrieval"]["emitted_chunks"] + manifest["coverage"]["retrieval"]["empty_sections"])
            self.assertTrue(all(not record["source_path"].startswith("guides/") for record in chunks))
            self.assertTrue(all(record["section_path"] and record["qualification_cues"] for record in chunks))
            CHECK.validate_artifacts(manifest, output)

    def test_manifest_schema_rejects_unknown_and_invalid_artifacts(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = BUILD.build(ROOT, Path(temporary))
            value = json.loads(path.read_text())
        invalid = copy.deepcopy(value)
        invalid["unexpected"] = "value"
        with self.assertRaises(Exception):
            CHECK.Draft202012Validator(CHECK.load_json(ROOT / "knowledge/schema/manifest.schema.json")).validate(invalid)
        invalid = copy.deepcopy(value)
        invalid["artifacts"][0]["path"] = "/private/path.json"
        with self.assertRaises(Exception):
            CHECK.Draft202012Validator(CHECK.load_json(ROOT / "knowledge/schema/manifest.schema.json")).validate(invalid)


if __name__ == "__main__":
    unittest.main()
