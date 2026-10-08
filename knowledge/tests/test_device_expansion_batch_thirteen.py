"""Guard material scope boundaries in the accepted Sfera/Vigik migration."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class DeviceExpansionThirteen(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        records = json.loads((ROOT / 'knowledge/inputs/claim-records.json').read_text())['claims']
        cls.claims = {n: [c for c in records if c['label'].startswith(f'OWN-DEV-{n:04d}:')]
                      for n in range(170, 190)}

    def text(self, n):
        return '\n'.join(c['statement'] for c in self.claims[n])

    def require(self, n, *tokens):
        for token in tokens:
            self.assertIn(token, self.text(n), (n, token))

    def test_disagreements_have_attributable_reciprocal_assertions(self):
        groups = {173: ['camera illumination'],
                  180: ['protection labels', 'mounting classification'],
                  181: ['regional mains and load rating'],
                  184: ['regional mains and load rating'],
                  185: ['auxiliary supply', 'auxiliary accessory rating'],
                  186: ['SCS maximum draw', 'external supply'],
                  187: ['programmer connectors'], 189: ['system capacity wording']}
        for n, labels in groups.items():
            for label in labels:
                pair = [c for c in self.claims[n] if f': source-specific {label}:' in c['label']]
                self.assertEqual(2, len(pair), (n, label))
                self.assertEqual(2, len({c['source_id'] for c in pair}), (n, label))
                for c in pair:
                    self.assertEqual({p['id'] for p in pair if p is not c},
                                     set(c['claim_links']['contradicts']))
                    self.assertTrue(c['questions'])
                    self.assertTrue(c['claim_links']['qualifies'])

    def test_reader_destructive_procedures_and_conversion_asymmetry_survive(self):
        self.require(170, 'selected-apartment deletion', 'exact erase scope is unresolved',
                     'Object `483`', 'no AB/C address fields', 'Object `482`',
                     'RELAY_OFF', 'future application', '13.56 NHz', 'Mifare Classic 1K')
        branches = [c for c in self.claims[170] if 'AC_A=' in c['statement']
                    and 'Item-side condition:' in c['statement']]
        self.assertEqual(100, len(branches))

    def test_sfera_ui_counts_and_language_positions_are_scoped(self):
        self.require(171, 'ten language-pack positions', 'DL=0..7',
                     'no extended software domain', 'not fixed language names')
        self.require(172, '4000', 'requires 353000', 'BEEP', 'binary Object domain does not encode')
        self.require(173, 'at 50 cm', 'white', 'infrared')

    def test_touchscreen_accessories_do_not_create_neighbour_capabilities(self):
        self.require(175, '335919', 'do not add an unsupported direct catalogue connection')
        self.require(176, 'does not import', '80 mA', 'LN4890A')
        self.require(177, 'not assigned to HW4684', 'box dimensions', 'does not state a 3.5-inch')
        self.require(178, 'distributor', 'telephone sockets', 'not load contacts')
        self.require(179, '574044', 'not established', '2+3')

    def test_actuator_missing_fields_and_invalid_defaults_stay_unresolved(self):
        self.require(174, 'MIN_LEVEL_ADV', 'outside', 'no replacement default', 'DALI')
        self.require(180, 'MODE', 'absent', 'another Object scope', 'M=1,2,12,13',
                     'Type=2', 'calibration', '16 A', '16 mA')
        self.require(181, 'M=3/4', 'VA', 'W', 'No LED-load compatibility')
        self.require(183, 'omits `M=1`', 'third physical socket', 'at least 3 m')
        self.require(184, '100..400', '60..400', 'no applicable correction')

    def test_vigik_managed_data_and_service_are_not_local_hardware(self):
        self.require(186, 'AC_MODE', 'outside this subset', '100 stored central-address branches',
                     'Vigik services remain unchanged', 'not active until associated')
        self.require(187, 'No reusable fields', 'software-managed data', 'NiMH',
                     'Even an On-line site', 'complete AD revision is outside')
        self.require(188, 'does not establish a physical Ethernet port',
                     'not a current subscription guarantee', 'GPRS connects hourly')

    def test_ip_address_domains_are_not_capacities_or_normalized_endpoints(self):
        self.require(189, 'address values, not capacity', '103999', '100090',
                     'strict inequalities', 'includes the endpoints 112 and 3209',
                     'Class 100', 'Both endpoints must physically exist', 'polling')


if __name__ == '__main__':
    unittest.main()
