"""Keep published gateway availability separate from scoped recorded replies."""
import csv
import hashlib
import io
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEN = "ownkb:section:d000061:s000014"
CONTACT = "ownkb:section:d000062:s000006"
NAVIGATION = "ownkb:section:d000060:s000007"
REVISION = "af8ec0ceaff4c82a1a71f2a3ac5d01ad2095de7b"
INPUTS = {"*25*21#1*21##", "*25*23#8*233##"}


class Who25GatewayCompatibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.claims = [json.loads(line) for line in
                      (ROOT / "knowledge/claims/claims.jsonl").read_text().splitlines()]
        cls.sources = {r["id"]: r for r in map(json.loads,
                       (ROOT / "knowledge/reference/sources.jsonl").read_text().splitlines())}
        cls.new_claims = [r for r in cls.claims if any(
            p["location"]["section_id"] in {CEN, CONTACT} for p in r["provenance"])]

    def test_each_function_has_its_own_published_compatibility_claims(self):
        for section, source in [(CEN, "ownkb:source:s000142"),
                                (CONTACT, "ownkb:source:s000148")]:
            claims = [r for r in self.new_claims if any(
                p["location"]["section_id"] == section and
                p["evidence_class"] == "official_specification"
                for p in r["provenance"])]
            supported = [r for r in claims if "gateway compatibility table identifies" in r["statement"]]
            self.assertEqual(7, len(supported))
            self.assertTrue(all(r["epistemic_status"] == "specified" for r in claims))
            self.assertTrue(all(any(p["source_id"] == source for p in r["provenance"])
                                for r in claims))
            old = next(r for r in supported if "firmware 1.0.19" in r["statement"])
            new = next(r for r in supported if "firmware 2.1.7" in r["statement"])
            self.assertIn("as unsupported", old["statement"])
            self.assertIn("as supported", new["statement"])
            self.assertNotIn("every firmware", " ".join(r["statement"] for r in supported))

    def test_recorded_reply_and_bus_verdict_survive_with_original_evidence(self):
        observations = [r for r in self.new_claims if any(
            self.sources[p["source_id"]].get("artifact_locator", {}).get("repository") == "OpenWebNet-HA/own-firmware-oracle"
            for p in r["provenance"])]
        self.assertEqual(4, len(observations))
        for claim in observations:
            provenance = next(p for p in claim["provenance"] if "examination" in p)
            source = self.sources[provenance["source_id"]]
            locator = source["artifact_locator"]
            self.assertRegex(source["id"], r"^ownkb:source:s\d{6}$")
            product, version = locator["path"].split("/")[1:3]
            data = (ROOT / "project/review/fixtures/who25-gateway-compatibility" /
                    f"{product}-{version}.tsv").read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), locator["sha256"])
            self.assertEqual(hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest(),
                             locator["git_blob"])
            text = "\n".join(line for line in data.decode().splitlines() if not line.startswith("#"))
            rows = [r for r in csv.DictReader(io.StringIO(text), delimiter="\t")
                    if r["input"] in INPUTS]
            self.assertEqual(INPUTS, {r["input"] for r in rows})
            expected = ("ack", "silent") if product == "MH202" else ("nack", "out")
            self.assertEqual({expected}, {(r["reply"], r["verdict"]) for r in rows})
            self.assertIn("reply=" + expected[0], claim["statement"])
            self.assertIn("verdict=" + expected[1], claim["statement"])
            self.assertTrue(all((r["output"] != "-") == (r["verdict"] == "out") for r in rows))
            self.assertEqual("source_inspection", provenance["examination"]["method"])
            self.assertNotIn("execution", provenance["examination"])
            self.assertEqual("public_experiment", provenance["evidence_class"])
            self.assertEqual("implementation", claim["applicability"]["domain"])
            self.assertIn(REVISION, claim["applicability"]["version"]["expression"])
            self.assertIn(version, claim["applicability"]["version"]["expression"])
            self.assertTrue(provenance["examination"]["limitations"])

    def test_missing_bench_evidence_does_not_become_a_runtime_claim(self):
        for claim in self.new_claims:
            self.assertNotEqual("experimentally_confirmed", claim["epistemic_status"])
            for p in claim["provenance"]:
                self.assertNotEqual("hardware_observation", p.get("examination", {}).get("method"))
            if "MH200" in claim["statement"] and "MH200N" not in claim["statement"]:
                self.assertNotIn("immediate", claim["statement"])
                self.assertNotIn("NACK", claim["statement"])
        claims = {r["id"]: r for r in self.claims}
        for identity in ("ownkb:claim:c002972", "ownkb:claim:c002988", "ownkb:claim:c002989"):
            self.assertIn("published", claims[identity]["statement"].lower())
            self.assertTrue(any(p["source_id"] == "ownkb:source:s000142"
                                for p in claims[identity]["provenance"]))

    def test_substantive_sections_are_claimed_and_navigation_is_not(self):
        coverage = json.loads((ROOT / "knowledge/inputs/claim-coverage.json").read_text())
        rows = {r["section_id"]: r for d in coverage["domains"] for r in d["sections"]}
        for section in (CEN, CONTACT):
            self.assertEqual("claimed", rows[section]["status"])
            self.assertGreater(rows[section]["claim_count"], 0)
        self.assertEqual(("nonclaim", 0), (rows[NAVIGATION]["status"], rows[NAVIGATION]["claim_count"]))

    def test_existing_device_and_historical_section_ids_are_preserved(self):
        chunks = json.loads((ROOT / "knowledge/inputs/chunk-identities.json").read_text())
        for n in range(3):
            self.assertEqual(f"ownkb:chunk:r{1174+n:06d}",
                             chunks[f"ownkb:section:d000136:s{2+n:06d}"])
        self.assertEqual(3, len({chunks[s] for s in (CEN, CONTACT, NAVIGATION)}))
        self.assertTrue(all(int(chunks[s].rsplit("r", 1)[-1]) > 7929
                            for s in (CEN, CONTACT, NAVIGATION)))
        identities = json.loads((ROOT / "knowledge/inputs/identities.json").read_text())
        base = "functional/who-25-transversal/"
        self.assertEqual("ownkb:section:d000060:s000006",
                         identities[base + "README.md"]["sections"]["historical-scenarioplus-controls-1"])
        self.assertEqual("ownkb:section:d000062:s000005",
                         identities[base + "dry-contact-ir.md"]["sections"]["historical-contact-interpretation-1"])


if __name__ == "__main__":
    unittest.main()
