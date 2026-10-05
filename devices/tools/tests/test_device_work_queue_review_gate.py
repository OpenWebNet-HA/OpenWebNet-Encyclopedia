from __future__ import annotations

import copy
import importlib.util
import sys
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
SPEC = importlib.util.spec_from_file_location("device_work_queue", TOOLS / "build-device-work-queue.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ReviewGateTests(unittest.TestCase):
    def reviewed_fixture(self):
        data = copy.deepcopy(MODULE.load())
        item_id, entry = next(
            (item_id, entry)
            for item_id, entry in data["items"].items()
            if entry.get("outcome") and entry["outcome"].get("device_ids")
        )
        entry["state"] = "reviewed"
        for key in [
            "commercial_identities",
            "database_extraction",
            "documentation_discovery",
            "source_reconciliation",
            "definition",
            "final_review",
        ]:
            entry["review"][key] = "complete"
        entry["review"]["review_gate"] = {key: "complete" for key in MODULE.REVIEW_GATE_CHECKS}
        return data, item_id

    def test_reviewed_allows_hardware_pending(self):
        data, item_id = self.reviewed_fixture()
        data["items"][item_id]["review"]["hardware_corroboration"] = "pending"
        MODULE.validate(data)

    def test_reviewed_rejects_pending_gate(self):
        data, item_id = self.reviewed_fixture()
        data["items"][item_id]["review"]["review_gate"]["identity_scope"] = "pending"
        with self.assertRaises(SystemExit):
            MODULE.validate(data)

    def test_final_review_rejects_pending_gate_before_transition(self):
        data, item_id = self.reviewed_fixture()
        data["items"][item_id]["state"] = "review-ready"
        data["items"][item_id]["review"]["review_gate"]["validation"] = "pending"
        with self.assertRaises(SystemExit):
            MODULE.validate(data)


if __name__ == "__main__":
    unittest.main()
