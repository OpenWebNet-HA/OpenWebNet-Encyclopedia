"""Preserve cross-layer, variant and source-conflict boundaries in batch six."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class SixthDeviceExpansionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.claims = [json.loads(x) for x in (ROOT / 'knowledge/claims/claims.jsonl').read_text().splitlines()]
        cls.entities = [json.loads(x) for x in (ROOT / 'knowledge/reference/entities.jsonl').read_text().splitlines()]

    def rows(self, n):
        return [c for c in self.claims if c['label'].startswith(f'OWN-DEV-{n:04d}:')]

    def modules(self, n):
        return [e for e in self.entities if e['label'].startswith(f'OWN-DEV-{n:04d}: Firmware') and e.get('entity_type') == 'module']

    def has(self, n, text, question=False):
        return any(text in c['statement'] and (not question or c['questions']) for c in self.rows(n))

    def conflict(self, n, label, values):
        rows = [c for c in self.rows(n) if 'source-specific ' + label + ':' in c['label']]
        self.assertEqual(2, len(rows))
        self.assertEqual(values, {c['value']['text'] for c in rows})
        self.assertEqual(rows[0]['subject_id'], rows[1]['subject_id'])
        for a, b in (rows, rows[::-1]):
            self.assertEqual([b['id']], a['claim_links']['contradicts'])
            self.assertTrue(a['questions'])
            self.assertNotEqual('observed', a['epistemic_status'])

    def test_alarm_domains_and_recovery_remain_unknown_or_source_conflicted(self):
        for n, expected in [(87, 3), (88, 1), (95, 2)]:
            self.assertEqual(expected, len(self.modules(n)))
        for n, fields in [(87, ['NUM_GSM', 'NUM_PSTN', 'FW_VER']), (95, ['NUM_PSTN', 'FW_VER'])]:
            for field in fields:
                rows = [c for c in self.rows(n) if 'Reusable domain:' in c['label'] and 'Field `' + field + '`' in c['statement']]
                self.assertEqual(1, len(rows))
                self.assertEqual('unknown', rows[0]['value']['state'])
                self.assertTrue(rows[0]['questions'])
        self.conflict(87, 'antenna cable length', {'3 m', '1.5 m'})
        self.conflict(88, 'armed state for recovery', {'armed', 'disarmed'})
        self.assertTrue(self.has(88, 'do not establish equivalence'))

    def test_webserver_variant_defaults_and_network_enumerations_are_distinct(self):
        for n in [89, 90]:
            self.assertEqual(2, len(self.modules(n)))
            self.assertTrue(self.has(n, '`LAN_IP_ADDR_TYPE`'))
            self.assertTrue(self.has(n, '`CONNECTION_METHOD`'))
            self.assertTrue(self.has(n, '`0` = Static IP'))
            self.assertTrue(self.has(n, '`0` = Dynamic IP'))
        self.conflict(89, 'WWZ transfer direction', {'device to PC', 'onto Device'})
        self.assertTrue(self.has(90, 'Do not borrow `F453AV` or successor `F454` ratings'))

    def test_all_energy_conversion_branches_survive_without_widening_domains(self):
        for n in [91, 92, 93, 96]:
            rows = [c for c in self.rows(n) if ' / Device-specific conversions: relationship:' in c['label'] and 'Referenced rule: `520`' in c['statement']]
            self.assertEqual(256, len(rows))
            self.assertTrue(any('`A1=2; A2=5; A3=5`' in c['statement'] and '`A123` = `255`' in c['statement'] for c in rows))
            self.assertEqual(1, len(self.modules(n)))
        self.assertTrue(self.has(91, '`0..127`'))
        self.assertTrue(self.has(93, 'key `452`'))
        self.assertTrue(self.has(96, '256..299', question=True))
        self.assertTrue(self.has(92, '56'))

    def test_old_control_and_missing_shutter_placement_are_not_filled(self):
        self.assertEqual(2, len(self.modules(94)))
        self.assertTrue(self.has(94, 'OLD'))
        self.assertTrue(self.has(94, 'Deprecated'))
        self.assertEqual(1, len(self.modules(98)))
        self.assertTrue(self.has(98, 'two Modules', question=True))
        self.assertTrue(self.has(99, 'MIN_LEVEL_ADV', question=True))
        for n in [90, 94, 95]:
            rows = [c for c in self.rows(n) if ': Physical and electrical characteristics:' in c['label'] and 'Not established' in c['statement']]
            self.assertEqual(1, len(rows))
            self.assertEqual('unknown', rows[0]['value']['state'])
            self.assertTrue(rows[0]['questions'])

    def test_stereo_maintenance_and_relay_conflicts_stay_separate(self):
        self.assertEqual(1, len(self.modules(100)))
        self.assertTrue(self.has(100, '`M2=9`'))
        self.assertTrue(self.has(100, 'No built-in radio'))
        self.conflict(100, 'excessive signal LED colour', {'orange', 'red'})
        self.conflict(100, 'signal level control', {'buttons', 'potentiometer'})
        self.assertEqual(8, len(self.modules(101)))
        self.assertTrue(self.has(101, '`1894`', question=True))
        self.conflict(101, 'relay mechanism', {'bistable', 'normally-open monostable'})

    def test_touchscreen_complete_package_ranges_are_scoped_catalogue_assertions(self):
        data = json.loads((ROOT / 'devices/inventory/touch-screen-package-unicode-ranges.json').read_text())
        rows = [c for c in self.rows(102) if ': Canonical package character ranges (prepared supplement) / Package range associations ' in c['label']]
        self.assertEqual(4534, len(rows))
        expected = {(str(r['id_unicode_set']), str(r['id_unicode_range']), r['Min'], r['Max']) for r in data['ranges']}
        import re
        actual = set()
        for c in rows:
            match = re.search(r'Unicode set: `(\d+)`; Range key: `(\d+)`; Minimum hexadecimal: `([0-9A-F]+)`; Maximum hexadecimal: `([0-9A-F]+)`', c['statement'])
            self.assertIsNotNone(match)
            actual.add(match.groups())
            self.assertEqual('public_database', c['provenance'][0]['evidence_class'])
            self.assertEqual('catalogue_documented', c['epistemic_status'])
            self.assertEqual('3.5.38', c['applicability']['version']['expression'])
            self.assertTrue(c['cautions'])
        self.assertEqual(expected, actual)
        self.assertEqual(4, len(self.modules(102)))
        self.conflict(102, 'mounting screw direction', {'clockwise', 'anticlockwise'})
        self.conflict(102, 'display terminology', {'LCD', 'LED'})
        self.conflict(102, 'seasonal program capacity', {'5 programs', '3 summer / 3 winter programs'})
        self.assertTrue(self.has(102, 'Package payloads remain unexamined'))

    def test_eight_key_control_ui_virgin_default_and_accessory_boundaries(self):
        self.assertEqual(9, len(self.modules(103)))
        self.assertTrue(self.has(103, 'slots `1..8`, not slot `9`'))
        self.assertTrue(self.has(103, 'external Object `462`'))
        rows = [c for c in self.rows(103) if 'domain:' in c['label'] and 'TYPE_CONTACT' in c['statement'] and 'No legal values specified' in c['statement']]
        self.assertEqual(2, len(rows))
        self.assertTrue(all(c['value']['state'] == 'unknown' and c['questions'] for c in rows))
        self.conflict(103, 'A5 label stock colour', {'3541 black / 3542 white', '3541 white / 3542 black'})
        self.assertTrue(self.has(103, 'not Object `130` level numbers'))


if __name__ == '__main__':
    unittest.main()
