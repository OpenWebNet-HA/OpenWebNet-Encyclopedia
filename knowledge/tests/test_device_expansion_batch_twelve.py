"""Keypad configuration routes and source conflicts remain bounded."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class KeypadBoundaries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        records = json.loads((ROOT / 'knowledge/inputs/claim-records.json').read_text())['claims']
        cls.claims = [c for c in records if c['label'].startswith('OWN-DEV-0169:')]
        cls.text = '\n'.join(c['statement'] for c in cls.claims)

    def test_central_relay_discrepancy_is_source_specific_and_reciprocal(self):
        pair = [c for c in self.claims if ': source-specific central relay operation:' in c['label']]
        self.assertEqual(2, len(pair))
        self.assertEqual(2, len({c['source_id'] for c in pair}))
        for c in pair:
            self.assertEqual({p['id'] for p in pair if p is not c}, set(c['claim_links']['contradicts']))
            self.assertTrue(c['questions'])
            self.assertTrue(c['claim_links']['qualifies'])

    def test_address_conversion_does_not_create_an_absent_object_field(self):
        for token in ['100 branches', 'Object `481`', 'no reusable AC_ADDRESS_AB field',
                      'those fields belong to Object `480`', 'no textual selection predicate']:
            self.assertTrue(token in self.text, token)

    def test_credential_roles_and_resident_topology_are_not_flattened(self):
        for token in ['program but do not unlock', 'unlock but do not program',
                      'one per apartment', '352000/352100', '20 visitor codes',
                      'M=22', 'unavailable on risers', 'future application']:
            self.assertTrue(token in self.text, token)

    def test_relay_scope_reset_and_unexamined_payloads_remain_qualified(self):
        for token in ['255', 'RELAY_OFF', 'absent-T', '4 s',
                      'erases all stored codes', 'at least 1 minute', 'unexamined', '********']:
            self.assertTrue(token in self.text, token)


if __name__ == '__main__':
    unittest.main()
