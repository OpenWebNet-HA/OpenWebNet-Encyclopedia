"""Verify WHO 13 DIMENSION 27 physical-capture, firmware-oracle, and framing boundaries."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SECTION = "ownkb:section:d000036:s000018"
TOPIC = "ownkb:entity:topic:d000036-s000018"
CHUNK = "ownkb:chunk:r007941"
MYHOME_REV = "eca7e51091ef75a2c10b74d0305fc9a8708624e4"
ORACLE_REV = "836843800a25def1d14f40aa82d09dd0bf901db0"

EXPECTED_ORACLE = {
    "F450": ("020010", "each", "ack", "out", "own:*#13**27*72#79#83#84##"),
    "F453": ("010100", "0", "ack", "out", "own:*#13**27*66#84#87#69#66##"),
    "F453AV": ("030014", "0", "ack", "out", "own:*#13**27*66#84#87#69#66##"),
    "F454": ("020051", "0", "ack", "out", "own:*#13**27*72#79#83#84##"),
    "F459": ("020105", "0", "ack", "out", "own:*#13**27*72#79#83#84##"),
    "F460": ("020012", "0", "ack", "out", "own:*#13**27*72#79#83#84##"),
    "F461": ("020011", "0", "ack", "out", "own:*#13**27*72#79#83#84##"),
    "H4684": ("020054", "0", "nack", "silent", "-"),
    "MH200": ("020102", "0", "-", "out", "own:*#13**27*#*#*1##"),
    "MH200N": ("010108", "0", "-", "out", "own:*#13**27*#*#*1##"),
    "MH202": ("010024", "0", "ack", "out", "own:*#13**27*72#79#83#84##"),
    "MyHomeServer1": ("028206", "0", "-", "out", "own:*#13**27*#*#*1##"),
}


def rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


class Who13Dimension27Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.claims = rows(ROOT / "knowledge/claims/claims.jsonl")
        cls.sources = {r["id"]: r for r in rows(ROOT / "knowledge/reference/sources.jsonl")}
        cls.review_text = (ROOT / "project/review/who13-dimension-27-model-name.md").read_text(encoding="utf-8")
        cls.local = [
            r for r in cls.claims
            if any(p["location"]["section_id"] == SECTION for p in r["provenance"])
        ]

    def test_registry_absence_and_client_framing_boundary(self) -> None:
        self.assertEqual(16, len(self.local))
        by_id = {r["id"]: r for r in self.local}
        absence = by_id["ownkb:claim:c074171"]
        self.assertEqual("observed", absence["epistemic_status"])
        self.assertEqual("3.5.38", absence["applicability"]["version"]["expression"])
        self.assertTrue(any(p.get("source_id") == "ownkb:source:s000125" for p in absence["provenance"]))
        self.assertIn("OPEN.db", absence["statement"])

        boundary = by_id["ownkb:claim:c074186"]
        self.assertEqual("corroborated_interpretation", boundary["epistemic_status"])
        self.assertEqual("protocol", boundary["applicability"]["domain"])
        self.assertIn("*#13**27*#*#*1##", boundary["statement"])
        self.assertIn("HOST", boundary["statement"])
        self.assertIn("BTWEB", boundary["statement"])

    def test_physical_captures_preserve_exact_provenance_and_scope(self) -> None:
        physical = [
            r for r in self.local
            if any(p["evidence_class"] == "public_capture" and "examination" in p for p in r["provenance"])
        ]
        self.assertEqual(2, len(physical))
        expected = {
            "ownkb:claim:c074172": ("2.0.11", "*#13**27*70#52#54#49##", (6358, 6411), 9954),
            "ownkb:claim:c074173": (
                "3.87.13",
                "*#13**27*77#121#72#111#109#101#83#101#114#118#101#114#49##",
                (1300, 1353),
                6840,
            ),
        }
        for claim in physical:
            fw, frame, span, line_count = expected[claim["id"]]
            self.assertEqual("observed", claim["epistemic_status"])
            self.assertEqual(TOPIC, claim["subject_id"])
            self.assertIn(MYHOME_REV, claim["applicability"]["version"]["expression"])
            self.assertIn(fw, claim["applicability"]["version"]["expression"])
            self.assertIn(frame, claim["statement"])
            prov = next(p for p in claim["provenance"] if "examination" in p)
            exam = prov["examination"]
            self.assertEqual("source_inspection", exam["method"])
            self.assertEqual("gateway", exam["implementation_role"])
            self.assertNotIn("execution", exam)
            self.assertEqual(span, (exam["code_location"]["start_line"], exam["code_location"]["end_line"]))
            loc = self.sources[prov["source_id"]]["artifact_locator"]
            self.assertEqual("OpenWebNet-HA/MyHOME", loc["repository"])
            self.assertEqual(MYHOME_REV, loc["revision"])
            self.assertEqual(line_count, loc["line_count"])
            self.assertIn(loc["git_blob"], self.review_text)
            self.assertIn(loc["sha256"], self.review_text)

    def test_oracle_v3_matrix_covers_all_twelve_emulated_gateways(self) -> None:
        oracle_claims = [
            r for r in self.local
            if any(p["evidence_class"] == "public_experiment" and "examination" in p for p in r["provenance"])
        ]
        self.assertEqual(12, len(oracle_claims))
        seen_products = set()
        for claim in oracle_claims:
            prov = next(p for p in claim["provenance"] if "examination" in p)
            exam = prov["examination"]
            src = self.sources[prov["source_id"]]
            loc = src["artifact_locator"]
            product, fw = loc["path"].split("/")[1:3]
            seen_products.add(product)
            exp_fw, exp_reset, exp_reply, exp_verdict, exp_out = EXPECTED_ORACLE[product]
            self.assertEqual(exp_fw, fw)
            self.assertEqual("OpenWebNet-HA/own-firmware-oracle", loc["repository"])
            self.assertEqual(ORACLE_REV, loc["revision"])
            self.assertEqual(25, loc["line_count"])
            self.assertIn(loc["git_blob"], self.review_text)
            self.assertIn(loc["sha256"], self.review_text)
            self.assertEqual((25, 25), (exam["code_location"]["start_line"], exam["code_location"]["end_line"]))
            self.assertEqual("source_inspection", exam["method"])
            self.assertEqual("firmware", exam["implementation_role"])
            self.assertNotIn("execution", exam)
            ver_expr = claim["applicability"]["version"]["expression"]
            self.assertIn(ORACLE_REV, ver_expr)
            self.assertIn(f"reset={exp_reset}", ver_expr)
            self.assertIn("settle_ms=3000", ver_expr)
            self.assertIn(f"reply={exp_reply}", claim["statement"])
            self.assertIn(f"verdict={exp_verdict}", claim["statement"])
            if exp_out != "-":
                self.assertIn(exp_out, claim["statement"])
        self.assertEqual(set(EXPECTED_ORACLE), seen_products)

    def test_identities_and_claim_coverage_preserve_existing_sections(self) -> None:
        identities = json.loads((ROOT / "knowledge/inputs/identities.json").read_text(encoding="utf-8"))
        d36_secs = identities["functional/who-13-integration-gateway/dimensions.md"]["sections"]
        self.assertEqual("ownkb:section:d000036:s000015", d36_secs["observed-implementation-extension-dimension-40-1"])
        self.assertEqual("ownkb:section:d000036:s000016", d36_secs["numeric-ids-not-transferable-across-variants-1"])
        self.assertEqual("ownkb:section:d000036:s000017", d36_secs["historical-touchscreen-platform-properties-1"])
        self.assertEqual(SECTION, d36_secs["observed-implementation-extension-dimension-27-1"])

        chunks = json.loads((ROOT / "knowledge/inputs/chunk-identities.json").read_text(encoding="utf-8"))
        self.assertEqual(CHUNK, chunks[SECTION])

        coverage = json.loads((ROOT / "knowledge/inputs/claim-coverage.json").read_text(encoding="utf-8"))
        sections = {r["section_id"]: r for d in coverage["domains"] for r in d["sections"]}
        self.assertEqual(("claimed", 16), (sections[SECTION]["status"], sections[SECTION]["claim_count"]))


if __name__ == "__main__":
    unittest.main()
