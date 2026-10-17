"""Device selection, acceptance and row conservation fail closed."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "knowledge/tools"))
from source_topology import GATES, canonical_paths, device_sources, semantic_area
from device_units import source_units, validate_device_units
from render_claims import section_digest
from prepare_sources import sanitize
from build_ir import build
from allocate_device_identities import allocate
from claim_context import reviewed_block_indexes


class DeviceIngestionTests(unittest.TestCase):
    def test_public_document_reference_and_url_are_not_private_identity(self):
        public = "The device uses ST-00002701-REV2-EN.pdf and https://example.org/home/productsheets/1234."
        self.assertEqual((public, []), sanitize(public))
        for public_reference in ("LE15098AA", "RA00224AA_EN", "ST_00000218_IT"):
            text = "Device documentation reference " + public_reference
            self.assertEqual((text, []), sanitize(text))
        private = "The installed Device ID is `A1B2C3D4`. Local path `/home/synthetic-user/file`."
        cleaned, classes = sanitize(private)
        self.assertNotIn("A1B2C3D4", cleaned)
        self.assertNotIn("synthetic-user", cleaned)
        self.assertEqual(["device_id", "other"], classes)
        self.assertNotIn("synthetic-user", sanitize("file:///home/synthetic-user/file")[0])
        self.assertNotIn("A1B2C3D4", sanitize("Device ID ST-A1B2C3D4-EN.pdf")[0])

    def tree(self, root):
        path = "devices/definitions/own-dev-0001-synthetic-product.md"
        target = root / path
        target.parent.mkdir(parents=True)
        target.write_text("# Synthetic product\n\n## Summary\n\nA synthetic device is used only as a fixture.\n")
        (target.parent / "README.md").write_text("# Not an ingestion source\n")
        inputs = root / "knowledge/inputs"
        inputs.mkdir(parents=True)
        inventory = {"format_version": "0.1.0", "definitions": [
            {"device_id": "OWN-DEV-0001", "path": path, "state": "pending"}]}
        (inputs / "device-sources.json").write_text(json.dumps(inventory))
        return path, inventory

    def save(self, root, inventory):
        (root / "knowledge/inputs/device-sources.json").write_text(json.dumps(inventory))

    def test_pending_is_excluded_and_inventory_closed(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path, inventory = self.tree(root)
            self.assertEqual([], canonical_paths(root))
            self.assertEqual("device-model", semantic_area(path))
            inventory["definitions"].append(copy.deepcopy(inventory["definitions"][0]))
            self.save(root, inventory)
            with self.assertRaisesRegex(ValueError, "duplicate"):
                device_sources(root)

    def test_only_accepted_complete_gate_can_enter(self):
        import yaml
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path, inventory = self.tree(root)
            inventory["definitions"][0]["state"] = "integrated"
            self.save(root, inventory)
            item = {"state": "review-ready", "outcome": {"device_ids": ["OWN-DEV-0001"]},
                    "review": {"final_review": "complete", "review_gate": {g: "complete" for g in GATES}}}
            queue = root / "devices/work-queue.yaml"
            queue.write_text(yaml.safe_dump({"items": {"1": item}}))
            with self.assertRaisesRegex(ValueError, "accepted"):
                canonical_paths(root)
            item["state"] = "reviewed"
            queue.write_text(yaml.safe_dump({"items": {"1": item}}))
            self.assertEqual([path], canonical_paths(root))
            item["review"]["review_gate"]["claim_evidence"] = "pending"
            queue.write_text(yaml.safe_dump({"items": {"1": item}}))
            with self.assertRaisesRegex(ValueError, "accepted"):
                canonical_paths(root)

    def fixture_review(self):
        section = {"id": "ownkb:section:d900001:s000001", "blocks": [{"type": "table",
                   "header": [{"text": "Field"}, {"text": "Domain"}],
                   "rows": [[{"text": "SYNTHETIC"}, {"text": "0..9"}]]}]}
        doc = {"id": "ownkb:document:d900001", "path": "devices/definitions/own-dev-0001-synthetic-product.md", "sections": [section]}
        claim = {"id": "ownkb:claim:c900001", "statement": "For synthetic Field SYNTHETIC, the Domain is 0..9.",
                 "provenance": [{"location": {"document_id": doc["id"], "section_id": section["id"]}}]}
        unit = source_units(section)[0]
        review = {"format_version": "0.1.0", "documents": [{"path": doc["path"], "document_id": doc["id"],
                  "review_note": "Synthetic review only", "sections": [{"section_id": section["id"],
                  "section_sha256": section_digest(section), "units": [{"key": unit["key"], "sha256": unit["sha256"],
                  "status": "claimed", "claim_ids": [claim["id"]], "reason": "Header and cell values retained"}]}]}]}
        return {"documents": [doc]}, [claim], review

    def test_row_header_change_and_omission_are_detected(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "review.json"
            ir, claims, review = self.fixture_review()
            path.write_text(json.dumps(review))
            self.assertEqual(1, validate_device_units(ir, claims, path)["claimed"])
            review["documents"][0]["sections"][0]["units"] = []
            path.write_text(json.dumps(review))
            with self.assertRaisesRegex(ValueError, "omitted"):
                validate_device_units(ir, claims, path)
            ir, claims, review = self.fixture_review()
            ir["documents"][0]["sections"][0]["blocks"][0]["header"][1]["text"] = "Default"
            path.write_text(json.dumps(review))
            with self.assertRaisesRegex(ValueError, "source changed"):
                validate_device_units(ir, claims, path)

    def test_wrongly_scoped_claim_fails(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "review.json"
            ir, claims, review = self.fixture_review()
            claims[0]["provenance"][0]["location"]["section_id"] = "ownkb:section:d900002:s000001"
            path.write_text(json.dumps(review))
            with self.assertRaisesRegex(ValueError, "wrongly scoped"):
                validate_device_units(ir, claims, path)

    def test_claim_cannot_drop_a_source_cell(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "review.json"
            ir, claims, review = self.fixture_review()
            claims[0]["statement"] = "For synthetic Field SYNTHETIC, the Domain is unknown."
            path.write_text(json.dumps(review))
            with self.assertRaisesRegex(ValueError, "lost source-cell"):
                validate_device_units(ir, claims, path)

    def test_incremental_allocation_respects_retired_history(self):
        import yaml
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path, inventory = self.tree(root)
            inputs = root / "knowledge/inputs"
            inventory["definitions"][0]["state"] = "integrated"
            self.save(root, inventory)
            queue = {"items": {"1": {"state": "reviewed", "outcome": {"device_ids": ["OWN-DEV-0001"]},
                     "review": {"final_review": "complete", "review_gate": {g: "complete" for g in GATES}}}}}
            (root / "devices/work-queue.yaml").write_text(yaml.safe_dump(queue))
            (inputs / "identities.json").write_text("{}")
            (inputs / "chunk-identities.json").write_text("{}")
            (inputs / "id-registry.json").write_text(json.dumps({"ids": [
                {"id": "ownkb:document:d900000", "lifecycle": "retired"},
                {"id": "ownkb:chunk:r900000", "lifecycle": "retired"}]}))
            (inputs / "canonical-sources.jsonl").write_text(json.dumps({"source_path": path,
                "source_id": "ownkb:source:s900001", "source_type": "canonical_documentation", "classification": "publishable"}) + "\n")
            self.assertEqual(1, allocate(root)["new_documents"])
            identities = json.loads((inputs / "identities.json").read_text())
            self.assertEqual("ownkb:document:d900001", identities[path]["id"])
            self.assertEqual({"ownkb:chunk:r900001"}, set(json.loads((inputs / "chunk-identities.json").read_text()).values()))
            self.assertEqual(0, allocate(root)["new_documents"])
            (root / path).write_text("# Synthetic product\n\n## Renamed meaning\n\nNew text.\n")
            with self.assertRaisesRegex(ValueError, "stale|existing"):
                allocate(root)

    def test_reviewed_unit_is_used_instead_of_lexical_guess(self):
        section = {"provenance": {"path": "devices/definitions/own-dev-0001-synthetic-product.md"},
                   "blocks": [{"type": "paragraph", "text": "Repeated synthetic wording."},
                              {"type": "paragraph", "text": "Repeated synthetic wording."}]}
        self.assertEqual([1], reviewed_block_indexes("Repeated synthetic wording.", section,
                         {"review_status": "reviewed-device-pilot", "source_unit_key": "b1"}))
        with self.assertRaisesRegex(ValueError, "unknown source unit"):
            reviewed_block_indexes("Repeated synthetic wording.", section,
                                   {"review_status": "reviewed-device-pilot", "source_unit_key": "b2"})


if __name__ == "__main__":
    unittest.main()
