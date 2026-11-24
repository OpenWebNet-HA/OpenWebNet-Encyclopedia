"""Verify WHO 4 four-zone central-unit (4695) and 13-gateway compatibility curations."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SEC_ADDR = "ownkb:section:d000068:s000008"
SEC_WHAT = "ownkb:section:d000070:s000007"
SEC_DIMS = "ownkb:section:d000069:s000024"

EXPECTED_FIRMWARE = {
    "ownkb:source:s001226": (
        "4695 FW 010103 flat_0E0000_0FFFFF.bin",
        "254e3daed3534a4bcbf31a42534f75c3a8148e4e65fdcbcd0ea73aa4c16c91e9",
    ),
    "ownkb:source:s001227": (
        "MH200 FW 020102 bt_termo",
        "33ddcc24da367192b303202314f0c9ec82bf9280da44045a2983a137a0c1d4f9",
    ),
    "ownkb:source:s001228": (
        "H4684 FW 020054 bt_termo",
        "c21fceaaefd9e19601ecc3f959e88ebdb8f506e02b81d99dfcead502adbaa143",
    ),
    "ownkb:source:s001217": (
        "MH200N FW 010108 bt_termo",
        "fa2e45e707b1a6d6ce31d04a54490e1ec7453bd2932b44aba23fc5bfeeac2b4c",
    ),
    "ownkb:source:s001229": (
        "F453AV FW 030014 bt_termo",
        "45d4c4529876dd7e64bac2153382f138005838f186a26955c7c563ec6ec6a3e0",
    ),
    "ownkb:source:s001230": (
        "F453 FW 010100 bt_termo",
        "b28d02b1ec8ac565bc23c6c621d2b1d4a791c67c8f2bc2c1924e671198f6590f",
    ),
    "ownkb:source:s001218": (
        "F454 FW 020051 bt_termo",
        "d2c9f8e5f62d45e836f5b52780f8353d89cad57acd40540f6852b3be5461870f",
    ),
    "ownkb:source:s001231": (
        "F459 FW 020105 bt_termo",
        "7925ff014a6708a4591fe6c7241ee004ae840589c9c97e86e0ad5c222f0c2a69",
    ),
    "ownkb:source:s001232": (
        "F450 FW 020010 bt_termo",
        "963cf11bddd078a8e2ad86c8d98efd0136f1cf83c3c79792064eb834f087cd3d",
    ),
    "ownkb:source:s001233": (
        "MH202 FW 010024 coso",
        "6865c2d1d441d25effa31275080ded70ad3538a8a49288e3002ffb196b066175",
    ),
    "ownkb:source:s001220": (
        "MyHomeServer1 FW 028206 bt_termo",
        "ef2054ede288b166d5c8ea1e8951316b0172691f47f36181c2bb998caa1c45c6",
    ),
    "ownkb:source:s001223": (
        "F461 FW 020011 bt_termo",
        "23958a97b4808421de65c13ab254bc76c0f68b10416e3c6f24b9adb108bcf29f",
    ),
    "ownkb:source:s001234": (
        "F460 FW 020012 bt_termo",
        "8df7400eb9364f77a23c9ca170b2238586e95ecb12acc32591177cd7b1c7b0d5",
    ),
    "ownkb:source:s001235": (
        "3488 FW 030205 bt_termo",
        "f755a29d1d6604b215d34925fcf23e9b270e6ad4cf86d840c0565db5ee1af25d",
    ),
}


def iter_rows(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            yield json.loads(line)


class Who4FourZoneCentralUnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sources = {
            r["id"]: r
            for r in iter_rows(ROOT / "knowledge/reference/sources.jsonl")
        }
        cls.review_text = (ROOT / "project/review/who4-4695-four-zone-central-unit.md").read_text(encoding="utf-8")
        target_secs = {SEC_ADDR, SEC_WHAT, SEC_DIMS}
        cls.local = [
            r for r in iter_rows(ROOT / "knowledge/claims/claims.jsonl")
            if any(p["location"]["section_id"] in target_secs for p in r["provenance"])
        ]
        cls.by_id = {r["id"]: r for r in cls.local}

    def test_claim_inventory_and_implementation_scope(self) -> None:
        self.assertEqual(14, len(self.local))
        expected_ids = {f"ownkb:claim:c{i:06d}" for i in range(74201, 74215)}
        self.assertEqual(expected_ids, set(self.by_id))
        for cid, claim in self.by_id.items():
            self.assertEqual("observed", claim["epistemic_status"], cid)
            self.assertEqual("implementation", claim["applicability"]["domain"], cid)
            self.assertEqual("specified", claim["applicability"]["version"]["state"], cid)
            self.assertIn("4695 FW 010103 flat_0E0000_0FFFFF.bin", claim["applicability"]["version"]["expression"], cid)

    def test_firmware_binaries_and_publication_hygiene(self) -> None:
        for sha in (
            "b01630d5f4d4fb45ee3392279635cde4e3575778fe69afae505d71a7c211a3be",
            "6d71fe6e03f38ceaafc3f28e41a2fce5be774ed34c78413d518d8318a931c1b3",
            "3a760549e6c9b376308e29a1a6b46f5bb8f57a1b6f2715fff2f063324588ed01",
        ):
            self.assertIn(sha, self.review_text)

        for sid, (ver_label, sha) in EXPECTED_FIRMWARE.items():
            src = self.sources[sid]
            self.assertEqual("firmware_interface", src["source_type"])
            loc = src["artifact_locator"]
            self.assertEqual("immutable_artifact", loc["kind"])
            self.assertEqual(sha, loc["sha256"])
            self.assertEqual(ver_label, loc["version"])
            self.assertIn(sha, self.review_text)

        for claim in self.local:
            for p in claim["provenance"]:
                if "examination" not in p:
                    continue
                exam = p["examination"]
                self.assertNotIn("execution", exam)
                if p["source_id"] in EXPECTED_FIRMWARE:
                    self.assertEqual("static_firmware_analysis", exam["method"])
                    self.assertEqual(0, exam["artifact_location"]["start_offset"])
                    self.assertEqual(0, exam["artifact_location"]["end_offset"])

    def test_core_4695_and_gateway_protocol_facts(self) -> None:
        self.assertIn("ZA * 10 + ZB", self.by_id["ownkb:claim:c074201"]["statement"])
        self.assertIn("1..99", self.by_id["ownkb:claim:c074201"]["statement"])
        self.assertIn("$04 90", self.by_id["ownkb:claim:c074202"]["statement"])
        self.assertIn("B4=0xC2", self.by_id["ownkb:claim:c074203"]["statement"])
        self.assertIn("B7 00 31 01", self.by_id["ownkb:claim:c074204"]["statement"])
        self.assertIn("*#4*100*20*0##", self.by_id["ownkb:claim:c074204"]["statement"])
        self.assertIn("MH200 firmware 020102", self.by_id["ownkb:claim:c074205"]["statement"])
        self.assertIn("MH200N firmware 010108", self.by_id["ownkb:claim:c074206"]["statement"])
        self.assertIn("*4*1*1##", self.by_id["ownkb:claim:c074206"]["statement"])
        self.assertIn("C1 01 FF 00", self.by_id["ownkb:claim:c074208"]["statement"])
        self.assertIn("*4*3100*#0#C##", self.by_id["ownkb:claim:c074208"]["statement"])
        self.assertIn("Protection", self.by_id["ownkb:claim:c074209"]["statement"])
        self.assertIn("TX=[]", self.by_id["ownkb:claim:c074209"]["statement"])
        self.assertIn("115#PROGRAM", self.by_id["ownkb:claim:c074210"]["statement"])
        self.assertIn("B5=0x15/0x25/0x05", self.by_id["ownkb:claim:c074210"]["statement"])
        self.assertIn("*4*31*#0#C##", self.by_id["ownkb:claim:c074211"]["statement"])
        self.assertIn("*#4*#0#C*#14*T*3##", self.by_id["ownkb:claim:c074212"]["statement"])
        self.assertIn("0x0A..0x46", self.by_id["ownkb:claim:c074212"]["statement"])
        self.assertIn("B5=0x12", self.by_id["ownkb:claim:c074212"]["statement"])
        self.assertIn("$04 99 <CU> 30 0E", self.by_id["ownkb:claim:c074213"]["statement"])
        self.assertIn("DIMENSION 12", self.by_id["ownkb:claim:c074214"]["statement"])

    def test_pinned_own_firmware_oracle_tsvs_are_registered(self) -> None:
        oracle_sources = {
            f"ownkb:source:s{idx:06d}": self.sources[f"ownkb:source:s{idx:06d}"]
            for idx in range(1236, 1255)
        }
        self.assertEqual(19, len(oracle_sources))
        revisions = set()
        for sid, src in oracle_sources.items():
            self.assertEqual("public_experiment", src["source_type"], sid)
            loc = src["artifact_locator"]
            self.assertEqual("git_file", loc["kind"], sid)
            self.assertEqual("OpenWebNet-HA/own-firmware-oracle", loc["repository"], sid)
            self.assertEqual(40, len(loc["revision"]), sid)
            revisions.add(loc["revision"])
            self.assertIn(loc["git_blob"], self.review_text)
            self.assertIn(loc["sha256"], self.review_text)
        self.assertEqual(1, len(revisions))
        oracle_rev = next(iter(revisions))
        self.assertIn(oracle_rev, self.review_text)

    def test_holiday_program_and_mh202_exception_keep_original_evidence_scope(self) -> None:
        holiday = self.by_id["ownkb:claim:c074210"]["statement"]
        self.assertIn("daily Holiday mode", holiday)
        self.assertIn("weekly return program 1..3", holiday)
        self.assertNotIn("three scenarios", holiday)
        # The original user manual describes the program resumed after Holiday,
        # independently of the controller model's choice of opcode names.
        self.assertIn("U1809F_U_EN.pdf", self.sources["ownkb:source:s000348"]["title"])
        self.assertIn("`ownkb:source:s000348`", self.review_text)
        self.assertIn("`ownkb:source:s000349`", self.review_text)
        self.assertNotIn("`ownkb:source:s000319`", self.review_text)

        actuator = self.by_id["ownkb:claim:c074204"]
        self.assertIn("MH202 010024 returns NACK with no bus output", actuator["statement"])
        self.assertNotIn("outbound *#4*#0#1*20## on Generation C and D", actuator["statement"])
        # This exception is bound to the actual MH202 result, not inferred from
        # the four-generation grouping or the clean-room central-unit model.
        observations = [
            p["examination"] for p in actuator["provenance"]
            if p["source_id"] == "ownkb:source:s001252"
        ]
        self.assertEqual(1, len(observations))
        self.assertEqual("qualifies", observations[0]["relationship"])
        self.assertEqual((25, 25), (
            observations[0]["code_location"]["start_line"],
            observations[0]["code_location"]["end_line"],
        ))

    def test_simulated_controller_is_not_independent_firmware_corroboration(self) -> None:
        plant_sources = {
            f"ownkb:source:s{idx:06d}" for idx in (1241, 1245, 1247, 1249, 1251, 1254)
        }
        plant_observations = [
            p["examination"] for claim in self.local for p in claim["provenance"]
            if p["source_id"] in plant_sources
        ]
        self.assertTrue(plant_observations)
        for exam in plant_observations:
            self.assertEqual("qualifies", exam["relationship"])
            self.assertEqual("interpretation", exam["conclusion_kind"])
            self.assertEqual("gateway", exam["implementation_role"])
            self.assertTrue(any("clean-room Python models" in c for c in exam["conditions"]))
            self.assertTrue(any("original-controller execution remains unrecorded" in c
                                for c in exam["limitations"]))
        season = self.by_id["ownkb:claim:c074209"]
        self.assertFalse(any(
            p["evidence_class"] == "public_experiment"
            and p["examination"]["relationship"] == "corroborates"
            for p in season["provenance"]
        ))
        self.assertIn("No retained original-controller execution record is supplied", self.review_text)

    def test_sections_chunks_and_coverage_preserved(self) -> None:
        identities = json.loads((ROOT / "knowledge/inputs/identities.json").read_text(encoding="utf-8"))
        self.assertEqual(
            SEC_ADDR,
            identities["functional/who-4-temperature-control/addressing.md"]["sections"][
                "four-zone-central-unit-0-c-addressing-and-gateway-compatibility-1"
            ],
        )
        self.assertEqual(
            SEC_WHAT,
            identities["functional/who-4-temperature-control/what.md"]["sections"][
                "four-zone-central-unit-4695-what-behavior-1"
            ],
        )
        self.assertEqual(
            SEC_DIMS,
            identities["functional/who-4-temperature-control/dimensions.md"]["sections"][
                "four-zone-central-unit-0-c-dimension-14-and-zone-status-behavior-1"
            ],
        )

        chunks = json.loads((ROOT / "knowledge/inputs/chunk-identities.json").read_text(encoding="utf-8"))
        self.assertEqual("ownkb:chunk:r007943", chunks[SEC_ADDR])
        self.assertEqual("ownkb:chunk:r007944", chunks[SEC_WHAT])
        self.assertEqual("ownkb:chunk:r007945", chunks[SEC_DIMS])

        coverage = json.loads((ROOT / "knowledge/inputs/claim-coverage.json").read_text(encoding="utf-8"))
        sections = {r["section_id"]: r for d in coverage["domains"] for r in d["sections"]}
        self.assertEqual(("claimed", 6), (sections[SEC_ADDR]["status"], sections[SEC_ADDR]["claim_count"]))
        self.assertEqual(("claimed", 5), (sections[SEC_WHAT]["status"], sections[SEC_WHAT]["claim_count"]))
        self.assertEqual(("claimed", 3), (sections[SEC_DIMS]["status"], sections[SEC_DIMS]["claim_count"]))


if __name__ == "__main__":
    unittest.main()
