"""Verify WHO 4 DIMENSION 19, DIMENSION 20, and #20 output-code curations."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SECTION = "ownkb:section:d000069:s000023"
TOPIC = "ownkb:entity:topic:d000069-s000023"
CHUNK = "ownkb:chunk:r007942"
LIVE_REV = "3590d0fabce43f8bccc52c804d32749d0bbfe7a1"
LIVE_BLOB = "9b450640c11ed6194c20ff6cb5ee7020570dce25"
LIVE_SHA = "2ae9b60d22a30d5dc7a5e8eb91450637922935c699b0256503c122cb44b6a346"

EXPECTED_FIRMWARE = {
    "ownkb:source:s001217": (
        "MH200N",
        "010108",
        "bt_termo",
        "fa2e45e707b1a6d6ce31d04a54490e1ec7453bd2932b44aba23fc5bfeeac2b4c",
    ),
    "ownkb:source:s001218": (
        "F454",
        "020051",
        "bt_termo",
        "d2c9f8e5f62d45e836f5b52780f8353d89cad57acd40540f6852b3be5461870f",
    ),
    "ownkb:source:s001219": (
        "MH202",
        "010024",
        "libplug_thermo_tr.so",
        "5e2da864f01b19f4f14dde76e11786234b36c97f4f6778966d6a32f597d1452b",
    ),
    "ownkb:source:s001220": (
        "MyHomeServer1",
        "028206",
        "bt_termo",
        "ef2054ede288b166d5c8ea1e8951316b0172691f47f36181c2bb998caa1c45c6",
    ),
    "ownkb:source:s001221": (
        "MyHomeServer1",
        "028206",
        "bt_thermo_manager",
        "f4bd0eb5af3c7e0fb18722eabfa3a87dcc1d79fb1a836479363eedff361e3c66",
    ),
    "ownkb:source:s001222": (
        "MyHomeServer1",
        "028206",
        "bt_thermo_central_unit",
        "ab8fb396e52bbba43908b71328865b1abbb202c9f5925e0552efd8a57ee01911",
    ),
    "ownkb:source:s001223": (
        "F461",
        "020011",
        "bt_termo",
        "23958a97b4808421de65c13ab254bc76c0f68b10416e3c6f24b9adb108bcf29f",
    ),
}


def iter_rows(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            yield json.loads(line)


class Who4Dim19And20OutputCodesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        wanted_sources = {"ownkb:source:s000138", "ownkb:source:s001216", *EXPECTED_FIRMWARE}
        cls.sources = {
            r["id"]: r
            for r in iter_rows(ROOT / "knowledge/reference/sources.jsonl")
            if r["id"] in wanted_sources
        }
        cls.review_text = (ROOT / "project/review/who4-dim19-20-output-codes.md").read_text(encoding="utf-8")
        cls.local = [
            r for r in iter_rows(ROOT / "knowledge/claims/claims.jsonl")
            if any(p["location"]["section_id"] == SECTION for p in r["provenance"])
        ]
        cls.by_id = {r["id"]: r for r in cls.local}
        cls.s12_claims = {
            r["id"]: r
            for r in iter_rows(ROOT / "knowledge/claims/claims.jsonl")
            if any(p["location"]["section_id"] == "ownkb:section:d000069:s000012" for p in r["provenance"])
        }

    def test_section_claim_count_and_epistemic_separation(self) -> None:
        self.assertEqual(14, len(self.local))
        expected_ids = {f"ownkb:claim:c{i:06}" for i in range(74187, 74201)}
        self.assertEqual(expected_ids, set(self.by_id))

        spec = self.by_id["ownkb:claim:c074187"]
        self.assertEqual("specified", spec["epistemic_status"])
        self.assertEqual("protocol", spec["applicability"]["domain"])
        self.assertEqual({"ownkb:source:s000138"}, {p["source_id"] for p in spec["provenance"]})
        self.assertIn("0..8", spec["statement"])
        self.assertIn("read-only", spec["statement"])

        for cid in (
            "ownkb:claim:c074188",
            "ownkb:claim:c074189",
            "ownkb:claim:c074190",
            "ownkb:claim:c074191",
            "ownkb:claim:c074192",
            "ownkb:claim:c074193",
            "ownkb:claim:c074194",
            "ownkb:claim:c074195",
            "ownkb:claim:c074196",
            "ownkb:claim:c074199",
        ):
            self.assertEqual("observed", self.by_id[cid]["epistemic_status"])
            self.assertEqual("implementation", self.by_id[cid]["applicability"]["domain"])

        for cid, qid in (("ownkb:claim:c074197", "ownkb:question:q303173"),
                         ("ownkb:claim:c074198", "ownkb:question:q303174")):
            claim = self.by_id[cid]
            self.assertEqual("unresolved", claim["epistemic_status"])
            self.assertEqual("unresolved", claim["value"]["state"])
            self.assertEqual([qid], claim["questions"])

        boundary = self.by_id["ownkb:claim:c074200"]
        self.assertEqual("corroborated_interpretation", boundary["epistemic_status"])
        self.assertEqual(["ownkb:question:q303175"], boundary["questions"])
        self.assertIn("14..16", boundary["statement"])
        self.assertIn("101..200", boundary["statement"])
        self.assertIn("read-only", boundary["statement"])

        c3276 = self.s12_claims["ownkb:claim:c003276"]
        self.assertIn("MyHomeServer1 FW 028206", c3276["statement"])
        self.assertIn("F461 FW 020011", c3276["statement"])
        self.assertEqual("implementation", c3276["applicability"]["domain"])
        self.assertEqual("specified", c3276["applicability"]["version"]["state"])
        original = [p for p in c3276["provenance"] if "examination" in p]
        self.assertEqual({"ownkb:source:s001220", "ownkb:source:s001223"},
                         {p["source_id"] for p in original})
        self.assertTrue(all(p["examination"]["method"] == "static_firmware_analysis"
                            for p in original))
        self.assertTrue(all(p["location"]["section_id"] == "ownkb:section:d000069:s000012"
                            for p in original))
        self.assertNotIn("observed in real WHO 4 status responses", c3276["statement"])

    def test_live_capture_source_and_frame_line_spans(self) -> None:
        live_src = self.sources["ownkb:source:s001216"]
        self.assertEqual("public_capture", live_src["source_type"])
        loc = live_src["artifact_locator"]
        self.assertEqual("git_file", loc["kind"])
        self.assertEqual("OpenWebNet-HA/MyHOME", loc["repository"])
        self.assertEqual(LIVE_REV, loc["revision"])
        self.assertEqual(
            "tests/fixtures/traces/issue_908/myhome_trace_MyHomeServer1_fancoil_dim20_100_2026-11-14.json",
            loc["path"],
        )
        self.assertEqual(LIVE_BLOB, loc["git_blob"])
        self.assertEqual(LIVE_SHA, loc["sha256"])
        self.assertEqual(1729, loc["line_count"])
        self.assertIn(LIVE_BLOB, self.review_text)
        self.assertIn(LIVE_SHA, self.review_text)

        capture_claim = self.by_id["ownkb:claim:c074196"]
        self.assertEqual(TOPIC, capture_claim["subject_id"])
        self.assertIn(LIVE_REV, capture_claim["applicability"]["version"]["expression"])
        self.assertIn("*#4*1#3*#20*100##", capture_claim["statement"])
        self.assertIn("*#4*2#3*20*100##", capture_claim["statement"])
        self.assertIn("*#4*2#1*#20*0##", capture_claim["statement"])
        for interval in ("282.792", "24.241", "17.264"):
            self.assertIn(interval, capture_claim["statement"])
        self.assertIn("no response-time guarantee", capture_claim["statement"])
        self.assertNotIn("~45 ms", capture_claim["statement"])
        spans = {
            (p["examination"]["code_location"]["start_line"], p["examination"]["code_location"]["end_line"])
            for p in capture_claim["provenance"]
            if "examination" in p
        }
        self.assertEqual(
            {
                (1183, 1194),
                (1195, 1207),
                (1208, 1220),
                (1221, 1233),
                (1234, 1246),
                (1625, 1636),
                (1637, 1649),
            },
            spans,
        )

    def test_firmware_binaries_proportional_matrix_and_classifiers(self) -> None:
        for sid, (model, fw, binary, sha) in EXPECTED_FIRMWARE.items():
            src = self.sources[sid]
            self.assertEqual("firmware_interface", src["source_type"])
            loc = src["artifact_locator"]
            self.assertEqual("immutable_artifact", loc["kind"])
            self.assertEqual(sha, loc["sha256"])
            self.assertEqual(f"{model} FW {fw} {binary}", loc["version"])
            self.assertIn(sha, self.review_text)

        for cid in range(74188, 74201):
            claim = self.by_id[f"ownkb:claim:c{cid:06}"]
            ver_expr = claim["applicability"]["version"].get("expression", "")
            for p in claim["provenance"]:
                if "examination" not in p:
                    continue
                exam = p["examination"]
                self.assertNotIn("execution", exam)
                if p["source_id"] in EXPECTED_FIRMWARE:
                    self.assertEqual("static_firmware_analysis", exam["method"])
                    self.assertIn(self.sources[p["source_id"]]["artifact_locator"]["version"], ver_expr)
                    self.assertEqual(0, exam["artifact_location"]["start_offset"])
                    self.assertEqual(0, exam["artifact_location"]["end_offset"])

        self.assertIn("does not support", self.by_id["ownkb:claim:c074192"]["statement"].lower())
        self.assertIn("drops scs actuator bytes 0x80..0xe4", self.by_id["ownkb:claim:c074192"]["statement"].lower())
        self.assertIn("DIMENSION 20 only", self.by_id["ownkb:claim:c074193"]["statement"])
        self.assertIn("DIMENSION 19 (CV/HV), DIMENSION 20, and #20", self.by_id["ownkb:claim:c074194"]["statement"])
        self.assertIn("*#4*Z#N*#20*200##", self.by_id["ownkb:claim:c074195"]["statement"])
        self.assertIn("speed_pct + 100", self.by_id["ownkb:claim:c074195"]["statement"])
        self.assertIn("{0, 3, 5, 13, 14, 15, 16, 17, 100}", self.by_id["ownkb:claim:c074190"]["statement"])
        self.assertIn("{0, 3, 5, 13, 17, 100}", self.by_id["ownkb:claim:c074191"]["statement"])
        self.assertIn("23..99", self.by_id["ownkb:claim:c074199"]["statement"])
        self.assertIn("> 200", self.by_id["ownkb:claim:c074199"]["statement"])
        self.assertIn("*#4*1*19*0*##", self.by_id["ownkb:claim:c074199"]["statement"])
        self.assertIn("*#4*1*19*0*##", self.review_text)

    def test_identities_coverage_and_existing_sections_preserved(self) -> None:
        identities = json.loads((ROOT / "knowledge/inputs/identities.json").read_text(encoding="utf-8"))
        d69_secs = identities["functional/who-4-temperature-control/dimensions.md"]["sections"]
        self.assertEqual("ownkb:section:d000069:s000012", d69_secs["dimension-19-valve-status-1"])
        self.assertEqual("ownkb:section:d000069:s000013", d69_secs["dimension-20-actuator-status-1"])
        self.assertEqual(
            SECTION,
            d69_secs["observed-firmware-and-live-output-codes-for-dimension-19-dimension-20-and-20-1"],
        )

        chunks = json.loads((ROOT / "knowledge/inputs/chunk-identities.json").read_text(encoding="utf-8"))
        self.assertEqual(CHUNK, chunks[SECTION])

        coverage = json.loads((ROOT / "knowledge/inputs/claim-coverage.json").read_text(encoding="utf-8"))
        sections = {r["section_id"]: r for d in coverage["domains"] for r in d["sections"]}
        self.assertEqual(("claimed", 13), (sections["ownkb:section:d000069:s000012"]["status"], sections["ownkb:section:d000069:s000012"]["claim_count"]))
        self.assertEqual(("claimed", 7), (sections["ownkb:section:d000069:s000013"]["status"], sections["ownkb:section:d000069:s000013"]["claim_count"]))
        self.assertEqual(("claimed", 14), (sections[SECTION]["status"], sections[SECTION]["claim_count"]))

    def test_corpus_absence_is_bounded_and_original_sources_retained(self) -> None:
        claim = self.by_id["ownkb:claim:c074200"]
        for sid in {"ownkb:source:s001216", *EXPECTED_FIRMWARE,
                    "ownkb:source:s001224", "ownkb:source:s001225"}:
            self.assertIn(sid, {p["source_id"] for p in claim["provenance"]})
        self.assertIn("separate bench captures", claim["statement"])
        self.assertIn("a881a4be711e7b8f03f044505c3810cfffcad403", claim["statement"])
        self.assertIn("d04e453ea99b2b5dcaf36b2bfccc073eda522c48", claim["statement"])
        self.assertNotIn("Zero live plant captures across the curated corpus", claim["statement"])


if __name__ == "__main__":
    unittest.main()
