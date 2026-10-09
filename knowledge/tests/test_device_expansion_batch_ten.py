"""Material source, conversion and privacy boundaries for Devices0148–0155."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class BatchTenBoundaries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.claims = json.loads((ROOT / "knowledge/inputs/claim-records.json").read_text())["claims"]
        cls.byid = {c["id"]: c for c in cls.claims}

    def device_claims(self, n):
        return [c for c in self.claims if c["label"].startswith(f"OWN-DEV-{n:04d}:")]

    def text(self, n):
        return "\n".join(c["statement"] for c in self.device_claims(n))

    def test_source_discrepancies_are_reciprocal_and_pin_support(self):
        for n, label, tokens in [(148, "export height", ["105", "90"]),
                                 (153, "impact code", ["IK40", "IK04"]),
                                 (153, "relay count", ["four-relay", "two"]),
                                 (155, "depth", ["22", "25"])]:
            group = [c for c in self.device_claims(n) if c["label"].startswith(f"OWN-DEV-{n:04d}: source-specific {label}:")]
            self.assertEqual(2, len(group))
            self.assertNotEqual(group[0]["source_id"], group[1]["source_id"])
            for c, token in zip(group, tokens):
                self.assertIn(token, c["evidence_note"])
                other = next(x for x in group if x is not c)
                self.assertIn(other["id"], c["claim_links"]["contradicts"])
                self.assertTrue(c["questions"])
                governing = self.byid[c["claim_links"]["qualifies"][0]]
                self.assertIn(token, governing["statement"])
                self.assertIn(governing["statement"], c["statement"])

    def test_pump_and_virgin_admission_keep_physical_prohibition(self):
        t = self.text(148)
        for token in ["6.0.0", "5.0.0", "direct pump 52 appears only under 13",
                      "Virgin-only", "physical zone 00", "without", "units-only"]:
            self.assertIn(token, t)

    def test_all_pulse_conversion_addresses_survive_with_illegal_scope(self):
        rows = [c for c in self.device_claims(150) if " / Device-specific conversions:" in c["label"] and "Item-side condition:" in c["evidence_note"]]
        self.assertEqual(256, len(rows))
        outputs = {int(re.search(r"Object configuration result: `A123` = `(\d+)`", c["evidence_note"])[1]) for c in rows}
        self.assertEqual(set(range(256)), outputs)
        t = self.text(150)
        self.assertIn("outside", t)
        self.assertIn("128..255", t)
        self.assertIn("1..10000", t)
        self.assertIn("30 ms signal", t)

    def test_sparse_stop_time_and_unknown_build_are_not_filled(self):
        c = next(c for c in self.device_claims(153) if " / Object `7`" in c["label"] and ": Reusable domain:" in c["label"] and "STOP_TIME" in c["statement"])
        numbers = {int(v) for v in re.findall(r"`(\d+)`\s*=", c["value"]["text"])}
        self.assertNotIn(18, numbers)
        self.assertNotIn(61, numbers)
        self.assertIn(19, numbers)
        for n in [153, 154]:
            self.assertIn("No build row", self.text(n))
            self.assertIn("Missing build rows mean unknown build, not build zero", self.text(n))

    def test_gateway_metadata_does_not_override_manufacturer_exclusion(self):
        t = self.text(152)
        self.assertIn("explicit SDK/integration prohibition", t)
        self.assertIn("1.0.0", t)
        self.assertIn("3.0.0", t)
        self.assertIn("both security questions", t)
        self.assertIn("F455_1_1_2", t)

    def test_sanitized_new_devices_publish_no_credential_or_network_literals(self):
        for n in [149, 151, 152, 155]:
            data = json.dumps(self.device_claims(n))
            self.assertNotIn("basic_gw", data)
            self.assertNotIn("12345", data)
            self.assertNotIn("192.168.", data)
            self.assertIn("[REDACTED]", data)

    def test_video_entry_limits_and_dated_app_prerequisite_remain_qualified(self):
        t = self.text(155)
        for token in ["cannot coexist", "does not establish a firmware boundary", "344622", "1.15.0", "1.13.0", "not the latest release", "PEOPLE_S"]:
            self.assertIn(token, t)


if __name__ == "__main__":
    unittest.main()
