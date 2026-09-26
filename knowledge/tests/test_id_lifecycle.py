import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "knowledge/tools"))
from id_lifecycle import validate_lifecycle  # noqa: E402

class IdLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.registry = {
            "aliases": [],
            "ids": [{"first_release": "0.1.0", "id": "ownkb:claim:c000001", "lifecycle": "live"}],
        }

    def test_live_inventory_must_match(self):
        self.assertEqual(validate_lifecycle(self.registry, {"ownkb:claim:c000001"})["live"], 1)
        with self.assertRaises(ValueError):
            validate_lifecycle(self.registry, set())

    def test_duplicate_canonical_id_is_rejected(self):
        value = copy.deepcopy(self.registry)
        value["ids"].append(copy.deepcopy(value["ids"][0]))
        with self.assertRaises(ValueError):
            validate_lifecycle(value, {"ownkb:claim:c000001"})

    def test_alias_cannot_be_emitted(self):
        value = copy.deepcopy(self.registry)
        value["aliases"] = [{"alias": "ownkb:claim:c000002", "canonical_id": "ownkb:claim:c000001",
                             "first_release": "0.1.0", "reason": "rename"}]
        with self.assertRaises(ValueError):
            validate_lifecycle(value, {"ownkb:claim:c000001", "ownkb:claim:c000002"})

    def test_retired_id_cannot_be_emitted_and_needs_tombstone(self):
        value = {"aliases": [], "ids": [
            {"first_release": "0.1.0", "id": "ownkb:claim:c000001", "last_release": "0.1.0",
             "lifecycle": "retired", "reason": "withdrawn", "replaced_by": ["ownkb:claim:c000002"]},
            {"first_release": "0.1.0", "id": "ownkb:claim:c000002", "lifecycle": "live"},
        ]}
        self.assertEqual(validate_lifecycle(value, {"ownkb:claim:c000002"})["retired"], 1)
        with self.assertRaises(ValueError):
            validate_lifecycle(value, {"ownkb:claim:c000001", "ownkb:claim:c000002"})

if __name__ == "__main__":
    unittest.main()
