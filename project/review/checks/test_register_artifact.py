#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[2] / "tools" / "register_artifact.py"
SPEC = importlib.util.spec_from_file_location("register_artifact", MODULE_PATH)
assert SPEC and SPEC.loader
register_artifact = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(register_artifact)


BASE = """schema_version: 1
fingerprint_algorithm: SHA-256
artifacts:
- id: firmware-a
  kind: firmware
  publisher: Example
  media_type: application/zip
  filename: a.fwz
  size: 1
  sha256: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  storage:
    bucket: openwebnet-software
    object_key: sha256/aa/aa/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    visibility: private
  redistribution_status: private-archive-only
- id: firmware-z
  kind: firmware
  publisher: Example
  media_type: application/zip
  filename: z.fwz
  size: 1
  sha256: cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
  storage:
    bucket: openwebnet-software
    object_key: sha256/cc/cc/cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    visibility: private
  redistribution_status: private-archive-only
"""


def sample() -> dict:
    return {
        "id": "firmware-m",
        "kind": "firmware",
        "publisher": "Example",
        "media_type": "application/zip",
        "filename": "m.fwz",
        "size": 2,
        "sha256": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
        "storage": {
            "bucket": "openwebnet-software",
            "visibility": "private",
        },
        "redistribution_status": "private-archive-only",
    }


class RegisterArtifactTests(unittest.TestCase):
    def test_derives_object_key(self):
        item = register_artifact.canonicalize(sample())
        self.assertEqual(
            item["storage"]["object_key"],
            "sha256/bb/bb/bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
        )

    def test_inserts_within_kind_block(self):
        item = register_artifact.canonicalize(sample())
        updated, status = register_artifact.insert_artifact(BASE, item)
        self.assertEqual(status, "registered")
        self.assertLess(updated.index("- id: firmware-a"), updated.index("- id: firmware-m"))
        self.assertLess(updated.index("- id: firmware-m"), updated.index("- id: firmware-z"))

    def test_same_id_and_sha_is_idempotent(self):
        item = register_artifact.canonicalize(sample())
        updated, _ = register_artifact.insert_artifact(BASE, item)
        again, status = register_artifact.insert_artifact(updated, item)
        self.assertEqual(status, "already-registered")
        self.assertEqual(updated, again)

    def test_duplicate_sha_under_new_id_is_rejected(self):
        item = register_artifact.canonicalize(sample())
        updated, _ = register_artifact.insert_artifact(BASE, item)
        other = sample()
        other["id"] = "firmware-other"
        with self.assertRaisesRegex(ValueError, "sha256 already represented"):
            register_artifact.insert_artifact(updated, register_artifact.canonicalize(other))

    def test_bad_object_key_is_rejected(self):
        item = sample()
        item["storage"]["object_key"] = "sha256/not-correct"
        with self.assertRaisesRegex(ValueError, "storage.object_key must be"):
            register_artifact.canonicalize(item)


if __name__ == "__main__":
    unittest.main()
