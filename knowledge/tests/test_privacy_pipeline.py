"""Tests use synthetic or reserved documentation values only, never private data."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PREPARE = ROOT / "knowledge/tools/prepare_sources.py"
SCANNER = ROOT / "knowledge/tools/validate_privacy.py"
FIXTURES = ROOT / "knowledge/tests/fixtures"


def load_prepare_module():
    spec = importlib.util.spec_from_file_location("prepare_sources", PREPARE)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PrivacyPipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pipeline = load_prepare_module()

    def write_manifest(self, root: Path, records: list[dict[str, str]]) -> Path:
        manifest = root / "manifest.jsonl"
        manifest.write_text("".join(json.dumps(record) + "\n" for record in records), encoding="utf-8")
        return manifest

    def test_prohibited_capture_is_excluded_without_being_read(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            manifest = self.write_manifest(root, [{"source_id": "ownkb:source:lab-capture", "source_path": "captures/never-read.pcapng", "source_type": "capture", "classification": "prohibited"}])
            self.assertEqual([], self.pipeline.prepare(manifest, root))

    def test_safe_and_prohibited_manifest_fixtures_follow_closed_rules(self):
        valid = self.pipeline.read_manifest(FIXTURES / "valid-public-source-manifest.jsonl")[0]
        prohibited = self.pipeline.read_manifest(FIXTURES / "prohibited-capture-manifest.jsonl")[0]
        self.pipeline.validate_manifest_record(valid, "valid fixture")
        self.pipeline.validate_manifest_record(prohibited, "prohibited fixture")
        invalid = self.pipeline.read_manifest(FIXTURES / "invalid-source-manifest.jsonl")[0]
        with self.assertRaisesRegex(ValueError, "classified prohibited"):
            self.pipeline.validate_manifest_record(invalid, "invalid fixture")

    def test_privacy_schema_is_closed_and_publishable_only(self):
        schema = json.loads((ROOT / "knowledge/schema/privacy-metadata.schema.json").read_text(encoding="utf-8"))
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(["public", "sanitized"], schema["properties"]["classification"]["enum"])
        self.assertNotIn("private", schema["properties"]["classification"]["enum"])
        self.assertNotIn("unknown", schema["properties"]["classification"]["enum"])

    def test_sensitive_publishable_text_is_sanitized_before_output(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "docs").mkdir()
            address = ".".join(("203", "0", "113", "23"))  # RFC 5737 documentation address.
            (root / "docs/example.md").write_text(f"Example endpoint {address} is illustrative.", encoding="utf-8")
            manifest = self.write_manifest(root, [{"source_id": "ownkb:source:public-example", "source_path": "docs/example.md", "source_type": "canonical_documentation", "classification": "sanitize"}])
            record = self.pipeline.prepare(manifest, root)[0]
            self.assertEqual({"classification": "sanitized", "removed_value_classes": ["network_address"]}, record["privacy"])
            self.assertEqual("Example endpoint [NETWORK_ADDRESS] is illustrative.", record["text"])

    def test_publishable_text_with_sensitive_shape_fails_closed(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "docs").mkdir()
            (root / "docs/example.md").write_text("Address " + ".".join(("203", "0", "113", "24")), encoding="utf-8")
            manifest = self.write_manifest(root, [{"source_id": "ownkb:source:public-example", "source_path": "docs/example.md", "source_type": "canonical_documentation", "classification": "publishable"}])
            with self.assertRaisesRegex(ValueError, "classify it sanitize"):
                self.pipeline.prepare(manifest, root)

    def test_safe_protocol_placeholders_remain_public(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "docs").mkdir()
            (root / "docs/example.md").write_text("Payload uses IP1*IP2*IP3*IP4 and MAC1*MAC2*MAC3*MAC4*MAC5*MAC6.", encoding="utf-8")
            manifest = self.write_manifest(root, [{"source_id": "ownkb:source:protocol-placeholders", "source_path": "docs/example.md", "source_type": "canonical_documentation", "classification": "publishable"}])
            record = self.pipeline.prepare(manifest, root)[0]
            self.assertEqual({"classification": "public", "removed_value_classes": []}, record["privacy"])

    def test_final_scanner_rejects_synthetic_protocol_shape(self):
        output = ROOT / "knowledge/retrieval/test-private-shape.jsonl"
        try:
            output.write_text('{"text":"' + ".".join(("203", "0", "113", "25")) + '"}\n', encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCANNER)], cwd=ROOT, capture_output=True, text=True, check=False)
            self.assertNotEqual(0, result.returncode)
            self.assertIn("IPv4 address", result.stderr)
        finally:
            output.unlink(missing_ok=True)

    def test_final_scanner_accepts_typed_redaction_marker(self):
        output = ROOT / "knowledge/retrieval/test-redaction-marker.jsonl"
        try:
            output.write_text('{"text":"password=[REDACTED]"}\n', encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCANNER)], cwd=ROOT, capture_output=True, text=True, check=False)
            self.assertEqual(0, result.returncode, result.stderr)
        finally:
            output.unlink(missing_ok=True)

    def test_manifest_rejects_unreviewed_fields_and_misclassified_log(self):
        record = {"source_id": "ownkb:source:observations", "source_path": "logs/session.txt", "source_type": "log", "classification": "publishable", "note": "unreviewed"}
        with self.assertRaisesRegex(ValueError, "manifest fields"):
            self.pipeline.validate_manifest_record(record, "test")


if __name__ == "__main__":
    unittest.main()
