"""Synthetic semantic fixtures; no observed installation values."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'knowledge/tools'))
from build_ir import AREAS, build, canonical_paths  # noqa: E402


class IRPipelineTests(unittest.TestCase):
    def fixture_tree(self, root):
        fixture = ROOT / 'knowledge/tests/fixtures/ir'
        for area in (*AREAS, 'guides'):
            target = root / area
            target.mkdir()
            (target / 'example.md').write_text((fixture / area / 'example.md').read_text())
        records = [{'classification':'publishable','source_id':f'ownkb:source:s{i:06d}',
                    'source_path':p,'source_type':'canonical_documentation'}
                   for i,p in enumerate(canonical_paths(root), 1)]
        manifest = root / 'manifest.jsonl'
        manifest.write_text(''.join(json.dumps(r) + '\n' for r in records))
        return manifest, root / 'identities.json'

    def test_all_areas_one_ir_and_deterministic_identity(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            manifest, identities = self.fixture_tree(root)
            first = build(root, manifest, identities, bootstrap=True)
            self.assertEqual(7, len(first['documents']))
            self.assertTrue(all(d['privacy']['classification'] == 'public' for d in first['documents']))
            self.assertFalse(any(d['path'].startswith('guides/') for d in first['documents']))
            self.assertTrue(first['guide_remediation'])
            identities.write_text(json.dumps(first['identities']))
            self.assertEqual(first, build(root, manifest, identities))
            protocol = next(d for d in first['documents'] if d['path'].startswith('protocol/'))
            section = protocol['sections'][1]
            self.assertEqual(protocol['sections'][0]['id'], section['parent'])
            self.assertEqual('table', section['blocks'][1]['type'])
            self.assertEqual('link', section['blocks'][0]['links'][0]['type'])
            diagnostics = next(d for d in first['documents'] if d['path'].startswith('diagnostics/'))
            self.assertIn('unresolved', diagnostics['sections'][1]['blocks'][0]['uncertainty'])
            self.assertIn('do not', diagnostics['sections'][1]['blocks'][0]['cautions'])

    def test_guide_and_stale_identity_fail_closed(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            manifest, identities = self.fixture_tree(root)
            rows = [json.loads(s) for s in manifest.read_text().splitlines()]
            rows.append({'classification':'publishable','source_id':'ownkb:source:s999999',
                         'source_path':'guides/example.md','source_type':'canonical_documentation'})
            manifest.write_text(''.join(json.dumps(r)+'\n' for r in rows))
            with self.assertRaisesRegex(ValueError, 'manifest differs|guide'):
                build(root, manifest, identities, bootstrap=True)
            manifest.write_text(''.join(json.dumps(r)+'\n' for r in rows[:-1]))
            first = build(root, manifest, identities, bootstrap=True)
            identities.write_text(json.dumps(first['identities']))
            (root/'protocol/example.md').write_text('# Renamed\n')
            with self.assertRaisesRegex(ValueError, 'missing curated section identity'):
                build(root, manifest, identities)

    def test_unsupported_construct_fails(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            manifest, identities = self.fixture_tree(root)
            (root/'protocol/example.md').write_text('# Frame\n\n<div>raw markup</div>\n')
            with self.assertRaisesRegex(ValueError, 'unsupported raw HTML'):
                build(root, manifest, identities, bootstrap=True)


if __name__ == '__main__':
    unittest.main()
