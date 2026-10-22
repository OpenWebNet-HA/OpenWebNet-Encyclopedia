"""Exercise storage policy against real temporary Git indexes and commit histories."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("git_storage", Path(__file__).parents[1] / "check_git_storage.py")
storage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(storage)


class GitStorageTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Synthetic fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "commit.gpgsign", "false")
        self.git("config", "core.autocrlf", "false")
        self.git("config", "core.hooksPath", str(self.root / "no-hooks"))
        self.baseline = {"format_version": 1, "baseline_commit": "a" * 40,
                         "reason": "Synthetic legacy storage", "ordinary_blobs": []}
        self.write_baseline()
        self.save()
        self.base = self.git("rev-parse", "HEAD").decode().strip()
        limit = patch.object(storage, "MAX_BLOB_BYTES", 1024)
        limit.start()
        self.addCleanup(limit.stop)

    def git(self, *args):
        env = {key: value for key, value in os.environ.items()
               if key not in {"GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE"}}
        env.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1")
        return subprocess.run(["git", *args], cwd=self.root, check=True,
                              env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout

    def put(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        self.git("add", "--", name)

    def write_baseline(self):
        self.put(storage.BASELINE_PATH, json.dumps(self.baseline).encode())

    def save(self):
        self.git("commit", "-qm", "Synthetic storage fixture")

    def pointer(self, content=b"Synthetic retained review evidence\n"):
        return (f"version https://git-lfs.github.com/spec/v1\n"
                f"oid sha256:{hashlib.sha256(content).hexdigest()}\nsize {len(content)}\n").encode()

    def test_size_limit_checks_staged_bytes_not_worktree_or_attributes(self):
        self.put("large.txt", b"x" * 1025)
        (self.root / "large.txt").write_bytes(b"small unstaged replacement")
        self.assertTrue(storage.check_storage(self.root))
        self.put("large.txt", b"small staged replacement")
        (self.root / "large.txt").write_bytes(b"x" * 2048)
        self.assertEqual([], storage.check_storage(self.root))

    def test_exact_boundary_and_unusual_filename(self):
        name = "a space\tand\na newline.txt"
        self.put(name, b"x" * 1024)
        self.assertEqual([], storage.check_storage(self.root))
        self.put(name, b"x" * 1025)
        self.assertEqual(1, len(storage.check_storage(self.root)))

    def test_lfs_attribute_alone_does_not_exempt_unconverted_content(self):
        self.put(".gitattributes", b"large.txt filter=lfs diff=lfs merge=lfs -text\n")
        self.put("large.txt", b"x" * 1025)
        self.assertTrue(storage.check_storage(self.root))

    def test_review_tables_require_real_pointer_syntax_even_when_small(self):
        name = "project/review/synthetic.tsv"
        for content in (b"column\nvalue\n", self.pointer().replace(b"sha256:", b"sha1:")):
            self.put(name, content)
            self.assertTrue(storage.check_storage(self.root))
        self.put(name, self.pointer())
        self.assertEqual([], storage.check_storage(self.root))

    def test_pointer_payload_size_does_not_count_as_an_ordinary_git_blob(self):
        pointer = self.pointer().rsplit(b"size ", 1)[0] + b"size 900000000\n"
        self.put("project/review/synthetic.tsv", pointer)
        self.assertEqual([], storage.check_storage(self.root))

    def test_legacy_exception_is_exact_path_and_blob_not_a_permanent_path_exemption(self):
        self.put("legacy.txt", b"x" * 1500)
        oid = self.git("rev-parse", ":legacy.txt").decode().strip()
        self.baseline["ordinary_blobs"] = [{"path": "legacy.txt", "git_blob": oid, "size_bytes": 1500}]
        self.write_baseline()
        self.assertEqual([], storage.check_storage(self.root))
        self.put("copy.txt", b"x" * 1500)
        self.assertEqual(1, len(storage.check_storage(self.root)))
        self.put("copy.txt", b"small")
        self.put("legacy.txt", b"y" * 1500)
        self.assertEqual(1, len(storage.check_storage(self.root)))

    def test_added_then_removed_large_blob_still_fails_history_check(self):
        self.put("temporary.txt", b"x" * 1500)
        self.save()
        self.git("rm", "temporary.txt")
        self.save()
        self.assertEqual([], storage.check_storage(self.root, "HEAD"))
        errors = storage.check_storage(self.root, "HEAD", self.base)
        self.assertEqual(1, len(errors))
        self.assertIn("New history blob", errors[0])

    def test_migration_does_not_reject_existing_large_history(self):
        self.put("project/review/synthetic.tsv", b"x" * 1500)
        self.save()
        before = self.git("rev-parse", "HEAD").decode().strip()
        self.put("project/review/synthetic.tsv", self.pointer())
        self.save()
        self.assertEqual([], storage.check_storage(self.root, "HEAD", before))

    def test_committed_tree_does_not_use_dirty_index_or_worktree(self):
        self.put("committed.txt", b"small")
        self.save()
        self.put("committed.txt", b"x" * 1500)
        self.assertEqual([], storage.check_storage(self.root, "HEAD", self.base))
        self.assertTrue(storage.check_storage(self.root))

    def test_baseline_is_read_from_index_and_its_sizes_are_verified(self):
        (self.root / storage.BASELINE_PATH).write_text("invalid unstaged JSON")
        self.assertEqual([], storage.check_storage(self.root))
        self.put("legacy.txt", b"x" * 1500)
        oid = self.git("rev-parse", ":legacy.txt").decode().strip()
        self.baseline["ordinary_blobs"] = [{"path": "legacy.txt", "git_blob": oid, "size_bytes": 1600}]
        self.write_baseline()
        with self.assertRaisesRegex(ValueError, "incorrect size"):
            storage.check_storage(self.root)

    def test_missing_revision_or_nonancestor_cannot_silently_skip_history(self):
        with self.assertRaises(subprocess.CalledProcessError):
            storage.check_storage(self.root, "missing-revision", self.base)
        self.put("later.txt", b"small")
        self.save()
        later = self.git("rev-parse", "HEAD").decode().strip()
        with self.assertRaisesRegex(ValueError, "ancestor"):
            storage.check_storage(self.root, self.base, later)


if __name__ == "__main__":
    unittest.main()
