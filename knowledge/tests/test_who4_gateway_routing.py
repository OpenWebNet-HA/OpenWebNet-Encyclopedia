"""Verify WHO 4 #4#INTERFACE routing and dimensionless actuator-request oracle claims."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WHO4_SEC = "ownkb:section:d000068:s000007"
PROTO_SEC = "ownkb:section:d000104:s000016"
ORACLE_REV = "de87a34e251b677a299917c98fcfcea3b409bf34"


def rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


class Who4GatewayRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.claims = rows(ROOT / "knowledge/claims/claims.jsonl")
        cls.sources = {r["id"]: r for r in rows(ROOT / "knowledge/reference/sources.jsonl")}
        cls.who4_claims = [
            r for r in cls.claims
            if any(p["location"]["section_id"] == WHO4_SEC for p in r["provenance"])
        ]
        cls.proto_claims = [
            r for r in cls.claims
            if any(p["location"]["section_id"] == PROTO_SEC for p in r["provenance"])
        ]

    def test_twelve_emulated_gateways_are_pinned_and_scoped(self) -> None:
        observations = [
            r for r in self.who4_claims
            if any(
                self.sources[p["source_id"]].get("artifact_locator", {}).get("revision") == ORACLE_REV
                and p.get("examination", {}).get("conclusion_kind") == "direct"
                for p in r["provenance"]
            )
        ]
        self.assertEqual(12, len(observations))
        for claim in observations:
            self.assertEqual("observed", claim["epistemic_status"])
            self.assertEqual("implementation", claim["applicability"]["domain"])
            expr = claim["applicability"]["version"]["expression"]
            self.assertIn(ORACLE_REV, expr)
            self.assertIn("oracle_version=3", expr)
            expected_reset = "reset=each" if claim["id"] == "ownkb:claim:c074157" else "reset=0"
            self.assertIn(expected_reset, expr)
            self.assertIn("settle_ms=3000", expr)
            self.assertIn("zero interface-routed $06EC or $06E4", claim["statement"])
            if claim["id"] in {"ownkb:claim:c074157", "ownkb:claim:c074160", "ownkb:claim:c074161",
                                "ownkb:claim:c074162", "ownkb:claim:c074163", "ownkb:claim:c074168"}:
                self.assertIn("reply=nack, verdict=out", claim["statement"])
            exam = next(p["examination"] for p in claim["provenance"] if "examination" in p)
            self.assertEqual("source_inspection", exam["method"])
            self.assertEqual("firmware", exam["implementation_role"])

    def test_derived_guidance_retains_original_sources_and_firmware_scope(self) -> None:
        claims = {c["id"]: c for c in self.claims}
        expected_sources = {f"ownkb:source:s{n:06d}" for n in range(1190, 1202)}
        for identity in ("ownkb:claim:c074169", "ownkb:claim:c074170"):
            c = claims[identity]
            self.assertEqual("implementation", c["applicability"]["domain"])
            self.assertEqual("corroborated_interpretation", c["epistemic_status"])
            expression = c["applicability"]["version"]["expression"]
            self.assertIn(ORACLE_REV, expression)
            self.assertIn("F450 FW 020010", expression)
            self.assertIn("MyHomeServer1 FW 028206", expression)
            support = [p for p in c["provenance"] if "examination" in p]
            self.assertEqual(expected_sources, {p["source_id"] for p in support})
            self.assertTrue(all(p["examination"]["method"] == "source_inspection" for p in support))
            self.assertTrue(all(p["examination"]["conclusion_kind"] == "interpretation" for p in support))
            self.assertTrue(all("execution" not in p["examination"] for p in support))

    def test_mh202_crash_and_trailing_token_behavior_is_explicit(self) -> None:
        mh202 = next(r for r in self.who4_claims if r["id"] == "ownkb:claim:c074167")
        self.assertIn("$0499843110", mh202["statement"])
        self.assertIn("verdict=crash", mh202["statement"])
        self.assertIn("*#4*2#1##", mh202["statement"])
        self.assertIn("*#4*2#4#01##", mh202["statement"])

    def test_protocol_boundary_does_not_extrapolate_level4_routing_to_who4(self) -> None:
        self.assertEqual(1, len(self.proto_claims))
        boundary = self.proto_claims[0]
        self.assertEqual("ownkb:claim:c074170", boundary["id"])
        self.assertIn("must not be generalized to WHO 4", boundary["statement"])


if __name__ == "__main__":
    unittest.main()
