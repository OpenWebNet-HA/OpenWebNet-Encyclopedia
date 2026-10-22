"""Preserve function scope, harness history and privacy-projected physical evidence."""
import csv
import hashlib
import io
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEN = 'ownkb:section:d000061:s000014'
CONTACT = 'ownkb:section:d000062:s000006'
SCENE = 'ownkb:section:d000060:s000006'
NAVIGATION = 'ownkb:section:d000060:s000007'
OLD = 'af8ec0ceaff4c82a1a71f2a3ac5d01ad2095de7b'
CURRENT = '8a61bbeb1d26354241debac84a7310142e5ab3a5'
CAPTURE = ROOT / 'evidence/cap-mh200-who25-boundary-20261022'
INPUTS = {'*25*21#1*21##', '*25*23#8*233##'}
PROBES = {'*25*21#1*21##', '*25*11#0*11##', '*#25*21##', '*25*11#121*10##',
          '*25*12*131##', '*25*23#8*233##', '*25*31#1*339##', '*25*32#1*33##'}


def rows(path):
    return [json.loads(line) for line in path.read_text().splitlines()]


class Who25GatewayCompatibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.claims = rows(ROOT / 'knowledge/claims/claims.jsonl')
        cls.sources = {r['id']: r for r in rows(ROOT / 'knowledge/reference/sources.jsonl')}
        cls.local = [r for r in cls.claims if any(
            p['location']['section_id'] in {CEN, CONTACT, SCENE} for p in r['provenance'])]

    def test_each_function_retains_its_own_published_table(self):
        for section, source in [(CEN, 'ownkb:source:s000142'),
                                (CONTACT, 'ownkb:source:s000148')]:
            claims = [r for r in self.local if any(
                p['location']['section_id'] == section and
                p['evidence_class'] == 'official_specification' for p in r['provenance'])]
            supported = [r for r in claims if 'gateway compatibility table identifies' in r['statement']]
            self.assertEqual(7, len(supported))
            self.assertTrue(all(r['epistemic_status'] == 'specified' for r in claims))
            self.assertTrue(all(any(p['source_id'] == source for p in r['provenance']) for r in claims))
            self.assertIn('as unsupported', next(r['statement'] for r in supported if 'firmware 1.0.19' in r['statement']))
            self.assertIn('as supported', next(r['statement'] for r in supported if 'firmware 2.1.7' in r['statement']))

    def test_both_oracle_versions_preserve_original_bytes_and_scope(self):
        observations = [r for r in self.local if any(
            self.sources[p['source_id']].get('artifact_locator', {}).get('repository') ==
            'OpenWebNet-HA/own-firmware-oracle' for p in r['provenance'])]
        self.assertEqual(10, len(observations))
        counts = {OLD: 0, CURRENT: 0}
        for claim in observations:
            p = next(p for p in claim['provenance'] if 'examination' in p)
            source = self.sources[p['source_id']]
            loc = source['artifact_locator']; revision = loc['revision']; counts[revision] += 1
            product, version = loc['path'].split('/')[1:3]
            folder = ROOT / 'project/review/fixtures/who25-gateway-compatibility'
            if revision == CURRENT:
                folder /= 'oracle-v3'
            raw = (folder / f'{product}-{version}.tsv').read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), loc['sha256'])
            self.assertEqual(hashlib.sha1(f'blob {len(raw)}\0'.encode() + raw).hexdigest(), loc['git_blob'])
            data = '\n'.join(l for l in raw.decode().splitlines() if not l.startswith('#'))
            selected = [r for r in csv.DictReader(io.StringIO(data), delimiter='\t') if r['input'] in INPUTS]
            self.assertEqual(INPUTS, {r['input'] for r in selected})
            expected = (('ack', 'silent') if product == 'MH202' else ('nack', 'out')) if revision == OLD else (
                ('nack', 'silent') if product == 'MH200' else
                ('nack', 'out') if product == 'MyHomeServer1' else ('ack', 'out'))
            self.assertEqual({expected}, {(r['reply'], r['verdict']) for r in selected})
            for key, value in zip(('reply', 'verdict'), expected):
                self.assertIn(f'{key}={value}', claim['statement'])
            self.assertEqual('source_inspection', p['examination']['method'])
            self.assertNotIn('execution', p['examination'])
            self.assertIn(revision, claim['applicability']['version']['expression'])
            self.assertRegex(source['id'], r'^ownkb:source:s\d{6}$')
            if revision == OLD:
                self.assertIn('Historical', claim['statement'])
                self.assertTrue(any('Superseded' in s for s in p['examination']['limitations']))
        self.assertEqual({OLD: 4, CURRENT: 6}, counts)

    def test_corrected_harness_qualifies_historical_results(self):
        current = [r for r in self.local if CURRENT in r['applicability']['version'].get('expression', '')]
        targets = {t for c in current for t in c['claim_links']['qualifies']}
        self.assertEqual({f'ownkb:claim:c{n:06d}' for n in range(74010, 74014)}, targets)
        self.assertTrue(all('reset=0' in c['applicability']['version']['expression'] for c in current))
        self.assertTrue(all('settle_ms=3000' in c['applicability']['version']['expression'] for c in current))

    def test_physical_claims_use_only_replacement_capture(self):
        physical = [r for r in self.local if any(
            p['evidence_class'] == 'public_capture' and 'examination' in p for p in r['provenance'])]
        self.assertEqual(9, len(physical))
        manifest = json.loads((CAPTURE / 'manifest.json').read_text())
        self.assertEqual({r['id'] for r in physical}, set(manifest['machine_kb_claims']))
        for c in physical:
            self.assertEqual('observed', c['epistemic_status'])
            self.assertEqual('implementation', c['applicability']['domain'])
            self.assertIn('2026-10-22', c['applicability']['version']['expression'])
            self.assertIn('2.1.0', c['applicability']['version']['expression'])
            p = next(p for p in c['provenance'] if 'examination' in p)
            self.assertEqual('source_inspection', p['examination']['method'])
            self.assertNotIn('execution', p['examination'])
            self.assertTrue(any('not established' in s for s in p['examination']['limitations']))
            if any(p['location']['section_id'] == SCENE for p in c['provenance']):
                self.assertEqual('ownkb:entity:topic:d000060-s000006', c['subject_id'])

    def test_projection_preserves_every_probe_and_measured_reply(self):
        data = rows(CAPTURE / 'session-log.jsonl')
        found = set()
        for index, r in enumerate(data):
            if r['dir'] != 'tx' or r['raw'] not in PROBES:
                continue
            found.add(r['raw'])
            reply = next(x for x in data[index + 1:] if x['session'] == 'command' and x['dir'] == 'rx')
            self.assertEqual('*#*0##', reply['raw'])
            latency = reply['t_rel_ms'] - r['t_rel_ms']
            claim = next(c for c in self.local if
                         c['id'].startswith('ownkb:claim:c0741') and
                         f'literal command-session probe {r["raw"]} received' in c['statement'])
            self.assertIn(f'{latency:.3f} ms', claim['statement'])
            events = [x for x in data if x['session'] == 'event' and
                      r['t_rel_ms'] <= x['t_rel_ms'] < r['t_rel_ms'] + 2000]
            self.assertFalse(any(x['raw'].startswith(('*25*', '*#25*')) for x in events))
        self.assertEqual(PROBES, found)

    def test_projection_removes_live_identifiers_authentication_and_clock(self):
        frames = rows(CAPTURE / 'frames.jsonl'); sessions = rows(CAPTURE / 'session-log.jsonl')
        self.assertEqual(42, len(frames)); self.assertEqual(len(frames), len(sessions))
        self.assertTrue(all(f['seq'] == i + 1 for i, f in enumerate(frames)))
        for f, r in zip(frames, sessions):
            self.assertEqual((f['raw'], f['dir']), (r['raw'], r['dir']))
            self.assertEqual(f['t_rel_ms'], round(r['t_rel_ms']))
            self.assertFalse(f['raw'].startswith(('*99*', '*#13**22')))
            if f['who'] == 1:
                self.assertEqual('99', f['where'])
        serialized = '\n'.join(p.read_text() for p in CAPTURE.glob('*.json*'))
        self.assertNotRegex(serialized, r'(?i)\b[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}\b')
        self.assertNotIn('OPEN_PASSWORD_HASH', serialized)
        self.assertNotIn('NONCE', serialized)
        self.assertIn('synthetic', serialized.lower())
        projection = json.loads((CAPTURE / 'projection.json').read_text())
        source_hash = next(r['sha256'] for r in projection['original_files'] if r['file'] == 'raw-session-log.jsonl')
        sources = [r for r in self.sources.values() if r.get('artifact_locator', {}).get('sha256') == source_hash]
        self.assertEqual(1, len(sources))
        self.assertIn('no explicit final', projection['window_limit'])

    def test_incoming_events_and_invalid_contact_target_are_not_generalized(self):
        c = next(c for c in self.local if c['id'] == 'ownkb:claim:c074156')
        self.assertIn('incoming WHO 25 event handling remains untested', c['statement'])
        text = (ROOT / 'functional/who-25-transversal/dry-contact-ir.md').read_text()
        self.assertIn('WHERE 339', text)
        self.assertIn('outside the published address forms', text)
        self.assertIn('31 for ON/detection and 32 for OFF/no detection', text)
        for c in self.local:
            if 'public_capture' in {p['evidence_class'] for p in c['provenance']}:
                self.assertNotIn('immediate', c['statement'])

    def test_normative_ack_source_and_existing_identity_boundaries(self):
        claims = {c['id']: c for c in self.claims}
        for identity in ('ownkb:claim:c002972', 'ownkb:claim:c002988', 'ownkb:claim:c002989'):
            self.assertIn('published', claims[identity]['statement'].lower())
            self.assertTrue(any(p['source_id'] == 'ownkb:source:s000142' for p in claims[identity]['provenance']))
        chunks = json.loads((ROOT / 'knowledge/inputs/chunk-identities.json').read_text())
        for n in range(3):
            self.assertEqual(f'ownkb:chunk:r{1174+n:06d}', chunks[f'ownkb:section:d000136:s{2+n:06d}'])
        self.assertEqual(3, len({chunks[s] for s in (CEN, CONTACT, NAVIGATION)}))
        identities = json.loads((ROOT / 'knowledge/inputs/identities.json').read_text())
        self.assertEqual(SCENE, identities['functional/who-25-transversal/README.md']['sections']['historical-scenarioplus-controls-1'])
        self.assertEqual('ownkb:section:d000062:s000005', identities['functional/who-25-transversal/dry-contact-ir.md']['sections']['historical-contact-interpretation-1'])

    def test_substantive_sections_are_claimed_and_navigation_is_not(self):
        coverage = json.loads((ROOT / 'knowledge/inputs/claim-coverage.json').read_text())
        sections = {r['section_id']: r for d in coverage['domains'] for r in d['sections']}
        for s in (CEN, CONTACT, SCENE):
            self.assertEqual('claimed', sections[s]['status'])
            self.assertGreater(sections[s]['claim_count'], 0)
        self.assertEqual(('nonclaim', 0), (sections[NAVIGATION]['status'], sections[NAVIGATION]['claim_count']))


if __name__ == '__main__':
    unittest.main()
