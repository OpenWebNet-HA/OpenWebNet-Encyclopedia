"""Preserve consequential boundaries in the contact/interface/controller migration."""
import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]

class FifthDeviceExpansionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.claims = [json.loads(x) for x in (ROOT/'knowledge/claims/claims.jsonl').read_text().splitlines()]
        cls.entities = [json.loads(x) for x in (ROOT/'knowledge/reference/entities.jsonl').read_text().splitlines()]
    def rows(self, n):
        return [c for c in self.claims if c['label'].startswith(f'OWN-DEV-{n:04d}:')]
    def modules(self, n):
        return [e for e in self.entities if e['label'].startswith(f'OWN-DEV-{n:04d}: Firmware') and e.get('entity_type') == 'module']
    def has(self, n, text, question=False):
        return any(text in c['statement'] and (not question or c['questions']) for c in self.rows(n))
    def conflict(self, n, label):
        rows = [c for c in self.rows(n) if 'source-specific '+label+':' in c['label']]
        self.assertEqual(2, len(rows))
        a, b = rows
        self.assertEqual(a['subject_id'], b['subject_id'])
        for a, b in (rows, rows[::-1]):
            self.assertEqual([b['id']], a['claim_links']['contradicts'])
            self.assertTrue(a['questions'])
            self.assertNotEqual('observed', a['epistemic_status'])
        return rows
    def test_scenario_capacity_does_not_multiply_modules_and_timeout_stays_conflicted(self):
        self.assertEqual(1, len(self.modules(66)))
        rows = self.conflict(66, 'scenario abort timeout')
        self.assertEqual({'30 minutes', '30 seconds'}, {c['value']['text'] for c in rows})
        self.conflict(66, 'scenario module consumption')
    def test_dali_capacity_language_and_temperature_conflicts_remain_attributable(self):
        self.assertEqual(8, len(self.modules(69)))
        rows = self.conflict(69, 'DALI devices per output')
        self.assertEqual({'16 devices', '6 devices'}, {c['value']['text'] for c in rows})
        self.conflict(69, 'operating temperature')
        self.assertTrue(self.has(69, 'DALI2'))
    def test_contacts_slot_specific_results_and_literal_field_mismatches_survive(self):
        for n, count in [(70, 2), (71, 1), (72, 2)]:
            self.assertEqual(count, len(self.modules(n)))
        self.conflict(70, 'separate ON/OFF input assignment')
        self.conflict(70, 'scenario physical address')
        for n in [70, 72]:
            self.assertTrue(self.has(n, '`T_TIME `', question=True))
            self.assertTrue(self.has(n, 'SOURCE=0' if n == 70 else 'SOURCE 0', question=True))
        self.assertTrue(self.has(72, 'FAKE', question=True))
    def test_dimmer_dual_output_copied_rating_is_not_promoted(self):
        self.assertEqual(1, len(self.modules(73)))
        self.assertEqual(2, len(self.modules(74)))
        self.assertTrue(self.has(74, '2 × 1.7 A'))
        self.assertTrue(self.has(74, 'graphic is not adopted'))
    def test_controller_roles_are_separate_from_physical_channels(self):
        for n, count in [(75, 5), (77, 5), (79, 3), (82, 2)]:
            self.assertEqual(count, len(self.modules(n)))
        self.conflict(75, 'supply range')
        self.conflict(75, 'CFL ballast rating units')
        self.conflict(77, 'switched LED rating')
        self.conflict(77, 'motor terminal labels')
        self.conflict(77, 'usable local bus ports')
        self.conflict(79, 'supply range')
        self.assertTrue(self.has(82, 'not adopted as an independent'))
    def test_interface_firmware_reachability_and_bitmap_holes_are_not_filled(self):
        self.assertEqual(2, len(self.modules(78)))
        self.assertTrue(self.has(78, 'Firmware 722 has no such direct candidate'))
        self.assertTrue(self.has(78, '161..168', question=True))
        self.assertTrue(self.has(78, '169..175', question=True))
    def test_scenario_software_version_and_unexamined_parameter_stay_scoped(self):
        self.assertEqual(1, len(self.modules(80)))
        params = [c for c in self.rows(80) if 'Parameter and package associations: relationship:' in c['label']]
        self.assertEqual(1, len(params))
        self.assertTrue(self.has(80, 'provenance, not proof'))
        self.assertTrue(self.has(80, 'static-LAN requirement conflicts with reusable DHCP'))
    def test_sensor_catalogue_roles_do_not_establish_ultrasonic_hardware(self):
        self.assertEqual(17, len(self.modules(84)))
        self.assertTrue(self.has(84, 'No claim of ultrasonic hardware'))
        self.assertFalse(any(c['epistemic_status'] == 'observed' for c in self.rows(84)))
    def test_alarm_identity_unknown_domains_and_update_reset_are_separate(self):
        self.assertEqual(3, len(self.modules(85)))
        self.assertEqual(1, len(self.modules(86)))
        for field in ['NUM_PSTN', 'FW_VER']:
            rows = [c for c in self.rows(85) if 'Reusable domain:' in c['label'] and 'Field `'+field+'`' in c['statement']]
            self.assertEqual(1, len(rows))
            self.assertEqual('unknown', rows[0]['value']['state'])
            self.assertTrue(rows[0]['questions'])
        self.assertTrue(self.has(86, 'identity independently of the missing hardware manual'))
        self.assertTrue(self.has(86, 'not documented as a factory erase'))

if __name__ == '__main__':
    unittest.main()
