"""Regression checks for material boundaries in accepted Device ingestion 0128–0147."""
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

class BatchNineBoundaries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.claims=json.loads((ROOT/"knowledge/inputs/claim-records.json").read_text())["claims"]
        cls.byid={c["id"]:c for c in cls.claims}

    def text(self,n):
        return "\n".join(c["statement"] for c in self.claims if c["label"].startswith(f"OWN-DEV-{n:04d}:"))

    def test_conflicting_ballast_and_fuse_claims_are_reciprocal(self):
        for n,token in [(128,"DALI ballast capacity"),(143,"fuse drawing")]:
            group=[c for c in self.claims if c["label"].startswith(f"OWN-DEV-{n:04d}: source-specific {token}")]
            self.assertEqual(len(group),2)
            self.assertNotEqual(group[0]["source_id"],group[1]["source_id"])
            for c in group:
                other=next(x for x in group if x is not c)
                self.assertIn(other["id"],c["claim_links"]["contradicts"])
                self.assertTrue(c["questions"])

    def test_excluded_literal_defaults_have_specific_open_questions(self):
        for n in [128,130,139,142,143]:
            rows=[c for c in self.claims if c["label"].startswith(f"OWN-DEV-{n:04d}:") and ": Reusable default:" in c["label"] and "MIN_LEVEL_ADV" in c["statement"]]
            self.assertTrue(rows)
            for c in rows:
                self.assertEqual(0,c["value"]["integer"])
                self.assertTrue(c["questions"])

    def test_analogue_surface_does_not_become_dali_hardware(self):
        t=self.text(142)
        self.assertIn("excludes both 5 and 6",t)
        self.assertIn("MIN_LEVEL_ADV",t)
        self.assertIn("not physical-port evidence",t)

    def test_virgin_admission_does_not_become_legacy_direct_placement(self):
        t=self.text(146)
        self.assertIn("Virgin admission is not proof",t)
        self.assertIn("16W09",t)
        self.assertIn("translation defect",t)

    def test_network_defaults_are_prepared_and_not_installed_state(self):
        for n in [131,134,135,138]:
            t=self.text(n)
            self.assertIn("[NETWORK_ADDRESS]",t)
            self.assertNotIn("192.168.",t)
            self.assertNotIn("10.0.0.",t)

    def test_two_relay_zone_collision_and_firmware_default_survive(self):
        t=self.text(147)
        self.assertIn("without stored precedence",t)
        self.assertIn("6.0.0",t)
        self.assertIn("7.0.0",t)
        self.assertIn("Advanced mode is linked only to 14",t)

    def test_source_assertions_pin_the_actual_supporting_row(self):
        for n,label,token in [(134,"operating temperature: 2","5..40"),(136,"update classification: 2","firmware-update workflow"),(143,"fuse drawing: 2","T5H")]:
            c=next(x for x in self.claims if x["label"]==f"OWN-DEV-{n:04d}: source-specific {label}")
            self.assertIn(token,c["evidence_note"])
            self.assertTrue(c["claim_links"]["qualifies"])
            governing=self.byid[c["claim_links"]["qualifies"][0]]
            self.assertIn(token,governing["statement"])
            self.assertIn(governing["statement"],c["statement"])
