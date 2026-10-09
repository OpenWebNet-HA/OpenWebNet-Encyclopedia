"""The hosted gate requires the trusted private validator's exact-commit result."""
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import catalogue_source
import catalogue_ci_status as status


class CatalogueStatusTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        names = ('devices/definitions/example.md', 'devices/index.md', 'devices/work-queue.yaml',
                 'devices/tools/check-device-definitions.py', 'sources/manifest.yaml',
                 'sources/artifact-manifest.yaml', 'check.py', '.github/workflows/machine-kb.yml')
        for name in names:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('Synthetic public fixture: ' + name)
        self.commit = 'a' * 40
        self.proof = {'commit': self.commit, 'creator': status.VALIDATOR, 'state': 'success',
                      'context': status.CONTEXT, 'description': status.PREFIX + status.input_digest(self.root)}

    def test_exact_committed_inputs_and_trusted_result_are_required(self):
        status.validate_proof(self.proof, self.commit, self.root)
        for field, value in [('creator', 'untrusted-validator'), ('commit', 'b' * 40),
                             ('state', 'pending'), ('state', 'failure'), ('context', 'Other check')]:
            with self.subTest(field=field, value=value):
                with self.assertRaises(ValueError):
                    status.validate_proof(dict(self.proof, **{field: value}), self.commit, self.root)
        with self.assertRaises(ValueError):
            status.validate_proof(dict(self.proof, arbitrary='field'), self.commit, self.root)

    def test_changed_gate_code_definition_index_ledger_and_source_need_revalidation(self):
        for name in ('devices/definitions/example.md', 'devices/index.md', 'devices/work-queue.yaml',
                     'devices/tools/check-device-definitions.py', 'sources/manifest.yaml',
                     'sources/artifact-manifest.yaml', 'check.py', '.github/workflows/machine-kb.yml'):
            path = self.root / name
            old = path.read_bytes()
            with self.subTest(path=name):
                path.write_bytes(old + b' changed')
                with self.assertRaisesRegex(ValueError, 'inputs changed'):
                    status.validate_proof(self.proof, self.commit, self.root)
                path.write_bytes(old)

    def test_added_definition_and_escaping_symlink_cannot_reuse_result(self):
        new = self.root / 'devices/definitions/new.md'
        new.write_text('Synthetic additional Device')
        with self.assertRaisesRegex(ValueError, 'inputs changed'):
            status.validate_proof(self.proof, self.commit, self.root)
        new.unlink()
        with tempfile.TemporaryDirectory() as directory:
            outside = Path(directory) / 'outside.md'
            outside.write_text('External fixture')
            new.symlink_to(outside)
            with self.assertRaisesRegex(ValueError, 'escapes'):
                status.input_digest(self.root)

    def test_private_cache_and_interpreter_cache_are_not_status_inputs(self):
        path = self.root / 'devices/tools/__pycache__/fixture.pyc'
        path.parent.mkdir()
        path.write_bytes(b'Synthetic interpreter cache')
        private = self.root / 'sources/myhome-suite/3.5.38/databases/MHCatalogue.db'
        private.parent.mkdir(parents=True)
        private.write_bytes(b'Synthetic private cache')
        status.validate_proof(self.proof, self.commit, self.root)

    def test_remote_verification_does_not_accept_superseded_success(self):
        rows = [[{'context': status.CONTEXT, 'state': 'failure', 'creator': {'login': status.VALIDATOR},
                  'description': 'failed'},
                 {'context': status.CONTEXT, 'state': 'success', 'creator': {'login': status.VALIDATOR},
                  'description': self.proof['description']}]]
        output = self.root / 'proof.json'
        with patch.object(status, 'gh', return_value=json.dumps(rows)):
            with self.assertRaisesRegex(ValueError, 'has not passed'):
                status.verify_remote(self.commit, output, 0)
        self.assertFalse(output.exists())

    def test_missing_result_fails_instead_of_silently_skipping(self):
        with patch.object(status, 'gh', return_value='[[]]'):
            with self.assertRaisesRegex(ValueError, 'missing or pending'):
                status.verify_remote(self.commit, self.root / 'proof.json', 0)

    def test_authenticated_matching_result_creates_only_public_status_metadata(self):
        rows = [[{'context': status.CONTEXT, 'state': 'success', 'creator': {'login': status.VALIDATOR},
                  'description': self.proof['description']}]]
        output = self.root / 'proof.json'
        with patch.object(status, 'ROOT', self.root), patch.object(status, 'gh', return_value=json.dumps(rows)):
            status.verify_remote(self.commit, output, 0)
        self.assertEqual(self.proof, json.loads(output.read_text()))

    def test_short_or_non_hex_commit_identifier_is_not_an_exact_candidate(self):
        for commit in ('main', 'a' * 7, 'g' * 40):
            with self.assertRaises(ValueError):
                status.commit_id(commit)

    def test_explicit_private_copy_is_verified_and_cannot_fall_back(self):
        path = self.root / 'private.db'
        data = b'synthetic private-source bytes'
        entry = {'sha256': hashlib.sha256(data).hexdigest(), 'size': len(data)}
        path.write_bytes(data)
        with patch.dict(os.environ, {'OPENWEBNET_CATALOGUE_PATH': str(path)}), patch.object(catalogue_source, '_entry', return_value=entry):
            self.assertEqual(path, catalogue_source.catalogue_path())
            path.write_bytes(b'invalid')
            with self.assertRaisesRegex(RuntimeError, 'fingerprint mismatch'):
                catalogue_source.catalogue_path()
            path.unlink()
            with self.assertRaisesRegex(RuntimeError, 'unavailable'):
                catalogue_source.catalogue_path()


if __name__ == '__main__':
    unittest.main()
