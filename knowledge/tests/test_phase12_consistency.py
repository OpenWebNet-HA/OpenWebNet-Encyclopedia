"""Phase 12 cross-artifact consistency and change-impact checks."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "knowledge/tools"))


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CONSISTENCY = load("ownkb_consistency", ROOT / "knowledge/tools/validate_consistency.py")
IMPACT = load("ownkb_diff_impact", ROOT / "diff_impact.py")


class Phase12ConsistencyTests(unittest.TestCase):
    def test_complete_cross_artifact_report_matches_current_corpus(self):
        manifest = json.loads((ROOT / "knowledge/manifest.json").read_text())
        report = CONSISTENCY.validate_cross_artifact(ROOT, ROOT, manifest)
        self.assertEqual(134, report["canonical"]["documents"])
        self.assertEqual(7342, report["claims"]["records"])
        self.assertEqual(1149, report["retrieval"]["chunks"])
        self.assertEqual(manifest["coverage"]["references"]["records"], report["references"]["records"])
        self.assertEqual(651, report["claims"]["domains"]["protocol"]["claims"])
        self.assertEqual(311, report["claims"]["domains"]["scenario-engine"]["claims"])

    def test_canonical_change_maps_stable_and_transitive_records(self):
        report = IMPACT.analyze_changes(
            ROOT, [{"status": "M", "path": "protocol/README.md"}])
        change = report["changes"][0]
        self.assertFalse(report["full_review_required"])
        self.assertEqual("ownkb:document:d000102", change["document_id"])
        self.assertEqual(8, len(change["section_ids"]))
        self.assertIn("ownkb:claim:c000101", change["direct_claim_ids"])
        self.assertGreaterEqual(len(change["claim_ids"]), len(change["direct_claim_ids"]))
        self.assertTrue(change["chunk_ids"])
        self.assertTrue(change["reference_ids"])

    def test_guide_change_never_maps_canonical_claims(self):
        report = IMPACT.analyze_changes(
            ROOT, [{"status": "M", "path": "guides/retrieve-configured-cen-buttons.md"}])
        change = report["changes"][0]
        self.assertFalse(report["full_review_required"])
        self.assertTrue(change["guide_fact_review_required"])
        self.assertEqual([], change["claim_ids"])
        self.assertEqual([], change["reference_ids"])

    def test_identity_and_build_semantics_require_full_review(self):
        for path in ("knowledge/inputs/identities.json", "knowledge/tools/build_ir.py"):
            with self.subTest(path=path):
                report = IMPACT.analyze_changes(ROOT, [{"status": "M", "path": path}])
                self.assertTrue(report["full_review_required"])

    def test_name_status_parser_handles_rename(self):
        parsed = IMPACT.parse_name_status(
            "M\tprotocol/README.md\nR100\tprotocol/old.md\tprotocol/new.md\n")
        self.assertEqual(
            [
                {"status": "M", "path": "protocol/README.md"},
                {"status": "R", "old_path": "protocol/old.md", "path": "protocol/new.md"},
            ],
            parsed,
        )

    def test_worktree_diff_includes_untracked_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.name", "test"], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.email", "test@example.invalid"], check=True)
            (root / "tracked.txt").write_text("one\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(root), "add", "tracked.txt"], check=True)
            subprocess.run(["git", "-C", str(root), "commit", "-qm", "base"], check=True)
            (root / "untracked.txt").write_text("two\n", encoding="utf-8")
            self.assertIn(
                {"status": "A", "path": "untracked.txt"},
                IMPACT.git_changes(root, "HEAD", "WORKTREE"),
            )


if __name__ == "__main__":
    unittest.main()
