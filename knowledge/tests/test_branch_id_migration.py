"""Guard the revision-scoped reconciliation of independently allocated IDs."""
import collections
import json
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]


class BranchIdMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.migration = json.loads((ROOT / "project/review/myopencommunity-branch-id-migration-2026-10-09.json").read_text())
        cls.mapping = {row["previous_id"]: row["current_id"] for row in cls.migration["mappings"]}
        registry = json.loads((ROOT / "knowledge/inputs/id-registry.json").read_text())
        cls.registry = {row["id"]: row for row in registry["ids"]}
        cls.aliases = {row["alias"] for row in registry["aliases"]}

    def test_distinct_published_and_branch_claims_remain_resolvable(self):
        claims = {row["id"]: row for row in json.loads((ROOT / "knowledge/inputs/claim-records.json").read_text())["claims"]}
        self.assertNotEqual(claims["ownkb:claim:c007528"]["statement"],
                            claims["ownkb:claim:moc-c007528"]["statement"])
        reviews = json.loads((ROOT / "knowledge/inputs/evidence-reviews.json").read_text())["findings"]
        claim_ids = {value for finding in reviews for value in finding["claim_ids"]}
        self.assertNotIn("ownkb:claim:c007528", claim_ids)
        self.assertIn("ownkb:claim:moc-c007528", claim_ids)
        for old, new in self.mapping.items():
            if old.startswith("ownkb:claim:"):
                self.assertIn(old, claims)
                self.assertIn(new, claims)

    def test_mapping_is_revision_scoped_and_one_to_one(self):
        self.assertEqual("85cdc049393b6aa9f315107327fce0cf12f0ba6f", self.migration["source_revision"])
        self.assertIn("not global aliases", self.migration["scope"])
        self.assertEqual(475, len(self.mapping))
        self.assertEqual(len(self.mapping), len(set(self.mapping.values())))
        self.assertEqual({"claim": 304, "source": 86, "chunk": 67, "document": 1, "section": 17},
                         dict(collections.Counter(key.split(":")[1] for key in self.mapping)))
        for old, new in self.mapping.items():
            self.assertNotEqual(old, new)
            self.assertNotIn(old, self.aliases)
            if new in self.registry:
                self.assertEqual("live", self.registry[new]["lifecycle"])
        reserved = set(self.mapping.values()) - self.registry.keys()
        self.assertEqual(2, len(reserved))
        self.assertTrue(all(value.startswith("ownkb:section:moc-d000136:") for value in reserved))

    def test_chunk_schema_accepts_only_the_defined_numeric_forms(self):
        schema = json.loads((ROOT / "knowledge/schema/retrieval-chunks.schema.json").read_text())
        validator = Draft202012Validator(schema["properties"]["id"])
        for value in ("ownkb:chunk:r001174", "ownkb:chunk:moc-r001174"):
            validator.validate(value)
        for value in ("ownkb:chunk:moc-r1174", "ownkb:chunk:moc-r001174-extra",
                      "ownkb:chunk:other-r001174", "ownkb:claim:moc-r001174"):
            with self.subTest(value=value), self.assertRaises(Exception):
                validator.validate(value)


if __name__ == "__main__":
    unittest.main()
