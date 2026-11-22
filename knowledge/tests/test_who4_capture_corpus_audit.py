"""Prevent false live-capture conclusions in the bounded corpus scanner."""
import importlib.util
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[2] / "project/review/checks/audit_who4_output_capture_corpus.py"
SPEC = importlib.util.spec_from_file_location("who4_corpus_audit", PATH)
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class CaptureCorpusAuditTests(unittest.TestCase):
    def test_timing_does_not_pair_different_actuators(self):
        rows = [{"raw": "*#4*1#3*#20*100##", "timestamp": "0.102285"},
                {"raw": "*#4*1#3*20*100##", "timestamp": "0.385077"},
                {"raw": "*#4*2#3*#20*100##", "timestamp": "0.431430"},
                {"raw": "*#4*2#3*20*100##", "timestamp": "0.455671"}]
        pairs = AUDIT.paired_intervals(rows)
        self.assertEqual(["1#3", "2#3"], [p["where"] for p in pairs])
        self.assertEqual(["282.792000", "24.241000"], [p["interval_ms"] for p in pairs])

    def test_both_valve_sides_and_hash20_values_are_counted(self):
        result = AUDIT.summary(["*#4*1*19*0*14##", "*#4*1*19*155*0##",
                                "*#4*1#3*#20*200##"])
        self.assertEqual(3, result["output_payload_occurrences"])
        self.assertEqual(1, result["target_range_occurrences"]["14..16"])
        self.assertEqual(2, result["target_range_occurrences"]["101..200"])

    def test_requests_and_empty_fields_do_not_invent_values(self):
        result = AUDIT.summary(["*#4*1*19##", "*#4*1*20##", "*#4*1*19*0*##"])
        self.assertEqual(1, result["output_payload_occurrences"])
        self.assertEqual({"0": 1}, result["value_histogram"])

    def test_capture_metadata_examples_are_not_payloads(self):
        value = {"capture": {"example": "*#4*1*19*14*15##"},
                 "frames": [{"raw": "*#4*1*19*0*1##"}]}
        self.assertEqual(["*#4*1*19*0*1##"], list(AUDIT.literal_frames(value)))

    def test_nested_oracle_marker_overrides_capture_shape(self):
        value = {"capture": {"kind": "trace", "synthetic": True}}
        self.assertEqual("synthetic_or_oracle", AUDIT.classification("normal.json", value))
        self.assertEqual("synthetic_or_oracle", AUDIT.classification("oracle/example.json", {}))

    def test_uncertain_origin_is_not_certified_as_physical(self):
        self.assertEqual("retained_fixture_or_log_origin_not_independently_certified",
                         AUDIT.classification("export.json", {}))


if __name__ == "__main__":
    unittest.main()
