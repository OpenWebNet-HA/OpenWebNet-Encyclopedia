"""Credential redaction precedes Device parsing without consuming prose/domains."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from privacy_detection import sanitize_privacy_text
from validate_privacy import PATTERNS


class FactoryCredentialPreparation(unittest.TestCase):
    def test_numeric_table_credentials_keep_qualifications(self):
        for text in [
            "| Default OPEN password | `12345; published factory value` | Manual |",
            "| OPEN default password | `12345` | Factory documentation |",
        ]:
            prepared, classes = sanitize_privacy_text(text)
            self.assertNotIn("12345", prepared)
            self.assertIn("[REDACTED]", prepared)
            self.assertIn("credential", classes)
            self.assertIn(text.split(" | ")[-1], prepared)
        self.assertIn("published factory value", sanitize_privacy_text(
            "| Default OPEN password | `12345; published factory value` | Manual |"
        )[0])

    def test_recovery_literal_is_redacted_everywhere(self):
        text = "Answering both questions resets it to basic_gw; IP recovery differs."
        prepared, classes = sanitize_privacy_text(text)
        self.assertEqual("Answering both questions resets it to [REDACTED]; IP recovery differs.", prepared)
        self.assertIn("credential", classes)
        self.assertTrue(PATTERNS["credential factory literal"].search(text))

    def test_unlock_code_missing_space_is_redacted(self):
        text = "Published defaults: installer unlock code12345. Not installation data."
        prepared, classes = sanitize_privacy_text(text)
        self.assertNotIn("12345", prepared)
        self.assertIn("unlock code[REDACTED]", prepared)
        self.assertIn("credential", classes)
        self.assertTrue(PATTERNS["credential unlock code"].search(text))

    def test_abstract_domains_and_explanatory_table_prose_survive(self):
        for text in [
            "| New web password length | `8..10 characters` | Manual |",
            "| Local menu password | Changed on the local menu. | Manual |",
            "| Wi-Fi or password change | Reset the smartphone association. | Manual |",
            "| Authentication uses a password | `RA00344` documentation | Source |",
            "Protocol numeric domain 0..65535; public code 12345 is unrelated.",
        ]:
            self.assertEqual((text, []), sanitize_privacy_text(text))

    def test_source_unit_metadata_is_not_a_credential_assignment(self):
        import json
        root = Path(__file__).resolve().parents[2]
        for name in ["claims/claims.jsonl", "reference/questions.jsonl"]:
            for line in (root / "knowledge" / name).read_text().splitlines():
                record = json.loads(line)
                if "OWN-DEV-0152" in record.get("label", ""):
                    self.assertFalse(PATTERNS["credential assignment"].search(line), record["id"])
        self.assertTrue(PATTERNS["credential assignment"].search("password: b0:r6"))
        self.assertFalse(PATTERNS["credential assignment"].search("password (source unit b0:r6)"))

    def test_redaction_is_idempotent_and_final_scanner_accepts_it(self):
        text = "| OPEN default password | `12345` | public default |"
        once, _ = sanitize_privacy_text(text)
        self.assertEqual(once, sanitize_privacy_text(once)[0])
        self.assertFalse(any(pattern.search(once) for pattern in PATTERNS.values()))


if __name__ == "__main__":
    unittest.main()
