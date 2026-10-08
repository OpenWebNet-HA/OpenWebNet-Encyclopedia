import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from large_files import require_kb_hydrated, require_hydrated, POINTER_HEADER

class LargeFileTransportTests(unittest.TestCase):
    def test_pointer_requires_explicit_hydration_without_fetching(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); path=root/"knowledge/inputs/claim-records.json"
            path.parent.mkdir(parents=True)
            path.write_bytes(POINTER_HEADER+b"oid sha256:"+b"a"*64+b"\nsize 100\n")
            with self.assertRaisesRegex(ValueError,"git lfs pull"):
                require_kb_hydrated(root)
            self.assertTrue(path.read_bytes().startswith(POINTER_HEADER))

    def test_full_offline_bytes_unchanged(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/"claims.jsonl"; data=b'{"id":"ownkb:claim:c000001"}\n'
            path.write_bytes(data); before=hashlib.sha256(data).digest()
            require_hydrated(path)
            self.assertEqual(before,hashlib.sha256(path.read_bytes()).digest())

    def test_empty_fixture_does_not_require_large_artifacts(self):
        with tempfile.TemporaryDirectory() as directory:
            require_kb_hydrated(Path(directory))
