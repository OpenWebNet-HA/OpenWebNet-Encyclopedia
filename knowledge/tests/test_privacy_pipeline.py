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
    sys.path.insert(0, str(PREPARE.parent))
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

    def test_installed_device_id_forms_are_sanitized_before_ir(self):
        tick = chr(96)
        examples = (
            "Device A1B2C3D4 demonstrated a behavior.",
            f"Device {tick}1A2B3C4D{tick} demonstrated a behavior.",
            f"Observed device: {tick}2B3C4D5E{tick}.",
            "Device identifier 3C4D5E6F was recorded.",
            "Installed unit ID 4D5E6F7A was recorded.",
        )
        for source in examples:
            with self.subTest(source=source):
                text, removed = self.pipeline.sanitize(source)
                self.assertEqual(["device_id"], removed)
                self.assertIn("[DEVICE_ID]", text)
                self.assertNotRegex(text, r"(?i)\b[0-9a-f]{8}\b")

    def test_installed_device_id_lists_are_fully_sanitized(self):
        tick = chr(96)
        source = (
            f"The observed Devices {tick}6F7A8B9C{tick}, "
            f"{tick}7A8B9C0D{tick}, and {tick}8B9C0D1E{tick} showed the same behavior."
        )
        text, removed = self.pipeline.sanitize(source)
        self.assertEqual(["device_id"], removed)
        self.assertEqual(3, text.count("[DEVICE_ID]"))
        self.assertNotRegex(text, r"(?i)\b[0-9a-f]{8}\b")

    def test_device_id_false_positive_controls_remain_public(self):
        source = (
            "Catalogue identifier A1B2C3D4; SHA-256 prefix 1A2B3C4D; "
            "public protocol value 2B3C4D5E; source identifier 3C4D5E6F; "
            "Device type 4D5E6F7A."
        )
        text, removed = self.pipeline.sanitize(source)
        self.assertEqual(source, text)
        self.assertEqual([], removed)

    def test_real_sanitized_source_declares_removed_device_ids(self):
        records = self.pipeline.prepare(
            ROOT / "knowledge/inputs/canonical-sources.jsonl", ROOT
        )
        record = next(item for item in records if item["source_path"] == "diagnostics/dim30-modules.md")
        self.assertEqual("sanitized", record["privacy"]["classification"])
        self.assertIn("device_id", record["privacy"]["removed_value_classes"])
        self.assertNotRegex(record["text"], self.pipeline.DEVICE_ID_PATTERN)
        self.assertNotRegex(record["text"], self.pipeline.DEVICE_ID_LIST_PATTERN)

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

    def test_final_scanner_rejects_contextual_device_id_markdown(self):
        output = ROOT / "knowledge/retrieval/test-private-device-shape.jsonl"
        tick = chr(96)
        try:
            output.write_text(
                '{"text":"Observed Device ' + tick + '5E6F7A8B' + tick + '"}\n',
                encoding="utf-8",
            )
            result = subprocess.run([sys.executable, str(SCANNER)], cwd=ROOT, capture_output=True, text=True, check=False)
            self.assertNotEqual(0, result.returncode)
            self.assertIn("concrete Device ID", result.stderr)
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


    def test_contextual_device_identifier_variants_are_punctuation_independent(self):
        tick = chr(96)
        examples = (
            "Device IDs: A0B1C2D3, B1C2D3E4",
            "Installed device identifiers A1C2E3F4 and B2D3F4A5",
            "Observed Devices: C3D4E5F6, D4E5F6A7",
            "Devices\n- E5F6A7B8\n- F6A7B8C9",
            "The **Device IDs** are " + tick + "A7B8C9D0" + tick + ", B8C9D0E1",
            "Mixed text before; scanned Device identifier C9D0E1F2 and text after",
        )
        for source in examples:
            with self.subTest(source=source):
                sanitized, removed = self.pipeline.sanitize(source)
                self.assertEqual(["device_id"], removed)
                self.assertNotRegex(sanitized, r"(?i)(?<![0-9a-f])[0-9a-f]{8}(?![0-9a-f])")

    def test_contextual_detector_preserves_public_hex_controls(self):
        controls = (
            "Protocol constant A0B1C2D3 and frame field B1C2D3E4.",
            "Catalogue ID C3D4E5F6; firmware ID D4E5F6A7.",
            "Source hash prefix E5F6A7B8 and SHA-256 F6A7B8C9.",
            "Device type A7B8C9D0 and Device model B8C9D0E1.",
        )
        for source in controls:
            with self.subTest(source=source):
                self.assertEqual((source, []), self.pipeline.sanitize(source))

    def test_end_to_end_plural_device_ids_prepare_and_final_scan(self):
        tools = ROOT / "knowledge/tools"
        sys.path.insert(0, str(tools))
        import validate_privacy as scanner
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "docs").mkdir()
            (root / "docs/example.md").write_text(
                "Installed Device IDs:\n- A2B3C4D5\n- B3C4D5E6", encoding="utf-8"
            )
            manifest = self.write_manifest(root, [{
                "source_id": "ownkb:source:synthetic",
                "source_path": "docs/example.md",
                "source_type": "canonical_documentation",
                "classification": "sanitize",
            }])
            record = self.pipeline.prepare(manifest, root)[0]
            self.assertEqual(["device_id"], record["privacy"]["removed_value_classes"])
            artifact = root / "artifact.jsonl"
            artifact.write_text(json.dumps(record, sort_keys=True) + "\n", encoding="utf-8")
            generated_manifest = root / "knowledge-manifest.json"
            generated_manifest.write_text(json.dumps({"artifacts": []}), encoding="utf-8")
            old = (scanner.ROOT, scanner.KNOWLEDGE_ROOT, scanner.MANIFEST,
                   scanner.SOURCE_MANIFEST, scanner.GENERATED_ROOTS)
            try:
                scanner.ROOT = root
                scanner.KNOWLEDGE_ROOT = root
                scanner.MANIFEST = generated_manifest
                scanner.SOURCE_MANIFEST = manifest
                scanner.GENERATED_ROOTS = (root,)
                self.assertEqual(0, scanner.main())
                artifact.write_text('{"text":"Device IDs: A2B3C4D5, B3C4D5E6"}\n', encoding="utf-8")
                self.assertEqual(1, scanner.main())
            finally:
                (scanner.ROOT, scanner.KNOWLEDGE_ROOT, scanner.MANIFEST,
                 scanner.SOURCE_MANIFEST, scanner.GENERATED_ROOTS) = old


if __name__ == "__main__":
    unittest.main()
