"""Representative safety checks for reviewed claim seeds and their IR join."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "knowledge/tools"))
from build_ir import build as build_ir  # noqa: E402
from render_claims import claim_coverage_metrics, claim_records  # noqa: E402
from render_references import reference_records  # noqa: E402


class ClaimFrameworkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ir = build_ir(ROOT, ROOT / "knowledge/inputs/canonical-sources.jsonl",
                          ROOT / "knowledge/inputs/identities.json")
        cls.refs, _ = reference_records(cls.ir, ROOT / "knowledge/inputs/reference-records.json")
        cls.seeds = json.loads((ROOT / "knowledge/inputs/claim-records.json").read_text())
        cls.sample_seeds = {"claims": cls.seeds["claims"][:8]}

    def render(self, seeds=None, ir=None):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "claims.json"
            path.write_text(json.dumps(seeds if seeds is not None else self.seeds))
            return claim_records(ir if ir is not None else self.ir, self.refs, path)

    def test_representative_claims_and_conflict_survive(self):
        claims = self.render()
        self.assertEqual(len(claims), 3533)
        by_id = {r["id"]: r for r in claims}
        a, b = by_id["ownkb:claim:c000007"], by_id["ownkb:claim:c000008"]
        self.assertEqual((a["value"]["text"], b["value"]["text"]), ("copen", "sope>"))
        self.assertEqual(a["claim_links"]["contradicts"], [b["id"]])
        self.assertEqual(b["claim_links"]["contradicts"], [a["id"]])
        self.assertEqual(a["epistemic_status"], "unresolved")
        self.assertEqual(by_id["ownkb:claim:c000006"]["value"]["state"], "unresolved")
        self.assertEqual(by_id["ownkb:claim:c000005"]["value"]["integer"], 15)
        self.assertEqual(by_id["ownkb:claim:c000005"]["claim_links"]["supports"],
                         ["ownkb:claim:c000006"])
        self.assertEqual(by_id["ownkb:claim:c000004"]["subject_id"],
                         "ownkb:entity:device-model:virgin-object")
        left, right = by_id["ownkb:claim:c000009"], by_id["ownkb:claim:c000010"]
        self.assertEqual(left["claim_links"]["contradicts"], [right["id"]])
        self.assertEqual(right["claim_links"]["contradicts"], [left["id"]])
        self.assertIn("30 seconds", left["statement"])
        self.assertIn("30 minutes", right["statement"])

    def test_changed_source_section_requires_review(self):
        ir = copy.deepcopy(self.ir)
        section = next(s for d in ir["documents"] for s in d["sections"]
                       if s["id"] == "ownkb:section:d000105:s000006")
        section["title"] += " revised"
        with self.assertRaisesRegex(ValueError, "source section changed"):
            self.render(self.sample_seeds, ir=ir)

    def test_invalid_links_context_and_provenance_fail_closed(self):
        for alteration in (lambda x: x[6]["claim_links"]["contradicts"].clear(),
                           lambda x: x[0].__setitem__("subject_id", "ownkb:entity:who:missing"),
                           lambda x: x[0].__setitem__("namespace_id", "ownkb:namespace:missing"),
                           lambda x: x[0].__setitem__("source_id", "ownkb:source:missing"),
                           lambda x: x[0].__setitem__("section_sha256", "0" * 64),
                           lambda x: x[0]["claim_links"]["supports"].append("ownkb:claim:missing")):
            with self.subTest(alteration=alteration), self.assertRaises(ValueError):
                seed = copy.deepcopy(self.sample_seeds)
                alteration(seed["claims"])
                self.render(seed)

    def test_duplicate_semantic_claim_is_rejected(self):
        seed = copy.deepcopy(self.sample_seeds)
        duplicate = copy.deepcopy(seed["claims"][0])
        duplicate["id"] = "ownkb:claim:c999999"
        seed["claims"].append(duplicate)
        with self.assertRaisesRegex(ValueError, "duplicate semantic claim"):
            self.render(seed)

    def test_bounded_coverage_is_complete_and_counted(self):
        claims = self.render()
        metrics = claim_coverage_metrics(
            self.ir, claims, ROOT / "knowledge/inputs/claim-coverage.json")
        self.assertEqual(3533, metrics["records"])
        self.assertEqual(
            {"claims": 651, "documents": 11, "reviewed_nonclaim_sections": 10,
             "sections": 96, "sections_with_claims": 86},
            metrics["bounded_domains"]["protocol"],
        )
        self.assertEqual(
            {"claims": 2877, "documents": 60, "reviewed_nonclaim_sections": 26,
             "sections": 422, "sections_with_claims": 396},
            metrics["bounded_domains"]["functional"],
        )


if __name__ == "__main__":
    unittest.main()
