"""High-risk semantic boundaries exercised by the representative pilot."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class DevicePilotSemanticsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.claims = [json.loads(line) for line in (ROOT / "knowledge/claims/claims.jsonl").read_text().splitlines()]
        cls.pilot = [c for c in cls.claims if c["provenance"][0]["location"]["path"].startswith("devices/definitions/")]

    def test_missing_product_pdf_does_not_unresolve_catalogue_identity(self):
        commercial = [c for c in self.pilot if c["label"].startswith("OWN-DEV-0209: Commercial identities: relationship:")]
        self.assertEqual(1, len(commercial))
        c = commercial[0]
        self.assertEqual("known", c["value"]["state"])
        self.assertEqual("catalogue_documented", c["epistemic_status"])
        self.assertEqual("public_database", c["provenance"][0]["evidence_class"])
        self.assertIn("2697", c["statement"])
        self.assertIn("2335", c["statement"])
        gaps = [c for c in self.pilot if c["label"].startswith("OWN-DEV-0209: Physical and electrical characteristics")]
        self.assertTrue(gaps)
        self.assertTrue(all(c["value"]["state"] == "unknown" and c["questions"] for c in gaps))

    def test_empty_subset_is_unresolved_but_reusable_default_is_retained(self):
        rows = [c for c in self.pilot if c["label"].startswith("OWN-DEV-0010:") and "Filter ID `2455`" in c["statement"]]
        self.assertEqual(2, len(rows))
        unknown = next(c for c in rows if "has Effective catalogue domain" in c["statement"])
        default = next(c for c in rows if "has Reusable default" in c["statement"])
        self.assertEqual("unresolved", unknown["value"]["state"])
        self.assertTrue(unknown["questions"])
        self.assertEqual({"state": "known", "integer": 100}, default["value"])
        self.assertEqual(unknown["subject_id"], default["subject_id"])

    def test_shutter_pulse_units_and_filter_conflict_survive(self):
        pulses = [c for c in self.pilot if c["label"].startswith("OWN-DEV-0045: Object configuration surfaces")
                  and "Field `STOP_PULSE_DURATION`" in c["statement"] and "has Reusable domain" in c["statement"]]
        self.assertEqual(1, len(pulses))
        self.assertIn("`1` = 0.1 s", pulses[0]["statement"])
        self.assertIn("`100` = 10 s", pulses[0]["statement"])
        conflict = [c for c in self.pilot if c["label"].startswith("OWN-DEV-0045:") and "Filter ID `601`" in c["statement"]]
        self.assertTrue(conflict)
        self.assertTrue(all("outside this subset" in c["statement"] for c in conflict))

    def test_reusable_firmware_default_is_not_installed_f460_release(self):
        defaults = [c for c in self.pilot if c["label"].startswith("OWN-DEV-0207: Object configuration surfaces")
                    and "Field `FW_VER`" in c["statement"] and "has Reusable default" in c["statement"]]
        self.assertEqual(1, len(defaults))
        self.assertEqual({"state": "known", "text": "3.0.0"}, defaults[0]["value"])
        self.assertNotEqual("observed", defaults[0]["epistemic_status"])
        self.assertIn("does not establish physical support or installed state", defaults[0]["statement"])

    def test_temperature_conflict_is_reciprocal_and_has_open_resolution(self):
        rows = [c for c in self.pilot if c["label"].startswith("OWN-DEV-0001:") and c["claim_links"]["contradicts"]]
        self.assertEqual(2, len(rows))
        self.assertEqual([rows[1]["id"]], rows[0]["claim_links"]["contradicts"])
        self.assertEqual([rows[0]["id"]], rows[1]["claim_links"]["contradicts"])
        self.assertTrue(all(c["questions"] for c in rows))

    def test_virgin_only_roles_are_not_runtime_support_claims(self):
        rows = [c for c in self.pilot if "Virgin-only candidate" in c["label"]]
        self.assertTrue(rows)
        self.assertTrue(all(c["epistemic_status"] != "observed" for c in rows))
        self.assertTrue(all("does not establish physical support or installed state" in c["statement"] for c in rows))

    def test_calibration_steps_keep_order_source_and_key_referents(self):
        by_id = {claim['id']: claim for claim in self.claims}
        for start, source in ((8940, 'both sheets, printed/PDF p. 4'),
                              (72441, 'ST-00002495-EN.pdf')):
            for offset in range(6):
                claim = by_id[f'ownkb:claim:c{start + offset:06}']
                text = claim['statement']
                self.assertIn(source, text)
                self.assertIn(f'step {offset + 1} of 6', text)
                self.assertNotEqual('observed', claim['epistemic_status'])
                if offset:
                    self.assertIn('Prerequisite preceding steps in order', text)
                    self.assertIn('Hold the configuration key', text)
                if offset == 1:
                    self.assertIn('refers to the configuration key held in step 1', text)
                if offset == 4:
                    self.assertTrue('the moving shutter' in text or 'the actuator that measures' in text)


if __name__ == "__main__":
    unittest.main()
