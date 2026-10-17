"""Evidence boundaries in accepted Device migration 0030 through 0044."""
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

class ThirdDeviceExpansionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.claims=[json.loads(x) for x in (ROOT/'knowledge/claims/claims.jsonl').read_text().splitlines()]
        cls.entities=[json.loads(x) for x in (ROOT/'knowledge/reference/entities.jsonl').read_text().splitlines()]
    def rows(self,n):return [c for c in self.claims if c['label'].startswith(f'OWN-DEV-{n:04d}:')]
    def conflict(self,rows):
        self.assertEqual(2,len(rows))
        for a,b in (rows,rows[::-1]):
            self.assertEqual([b['id']],a['claim_links']['contradicts']);self.assertTrue(a['questions']);self.assertNotEqual('observed',a['epistemic_status'])
    def test_sensor_source_revision_conflict(self):
        rows=[c for c in self.rows(31) if 'source-specific M8:' in c['label']];self.conflict(rows)
        self.assertEqual(2,len({c['provenance'][0]['source_id'] for c in rows}))
        self.assertTrue(any('does not substantiate the ultrasonic' in c['statement'] for c in self.rows(31)))
    def test_card_identity_conflict_crosses_devices(self):
        rows=[c for n in [36,39] for c in self.rows(n) if 'source-specific 572736 identity:' in c['label']];self.conflict(rows)
        self.assertEqual({'public_database','official_specification'},{c['provenance'][0]['evidence_class'] for c in rows})
        self.assertTrue(any('not credential authorization' in c['statement'] for c in self.rows(39)))
    def test_local_display_filter_conflict_is_not_normalized(self):
        rows=[c for c in self.rows(37) if c['claim_links']['contradicts']];self.conflict(rows)
        domain=next(c for c in rows if 'has Effective catalogue domain' in c['statement'])
        self.assertIn('Vantage 8051',domain['value']['text'])
        self.assertTrue(any('FUN=5' in c['statement'] and 'enum' in c['statement'] for c in self.rows(37)))
    def test_gateway_topology_defaults_and_payload_boundaries(self):
        modules=[e for e in self.entities if e['label'].startswith('OWN-DEV-0033: Firmware') and e.get('entity_type')=='module'];self.assertEqual(3,len(modules))
        rows=self.rows(33);v=[c for c in rows if 'Field `FW_VER`' in c['statement'] and 'has Catalogue default' in c['statement']];self.assertEqual(1,len(v));self.assertEqual({'state':'known','text':'`3.0.0`'},v[0]['value'])
        self.assertTrue(any('physical USB connector' in c['statement'] for c in rows));self.assertTrue(any('not been inspected' in c['statement'] for c in rows))
        self.assertTrue(any('[NETWORK_ADDRESS]' in c['statement'] for c in rows))
    def test_probe_defaults_and_physical_features_stay_bounded(self):
        for n in [38,40,41]:
            rows=self.rows(n);self.assertTrue(any('ninth' in c['statement'] or 'eight-slave' in c['statement'] for c in rows));self.assertTrue(any('outside this subset' in c['statement'] and c['questions'] for c in rows));self.assertFalse(any(c['epistemic_status']=='observed' for c in rows))
        self.assertTrue(any('1500 m' in c['statement'] and 'error' in c['statement'] for c in self.rows(38)))
    def test_batteryless_temperature_sources_remain_distinct(self):
        rows=[c for c in self.rows(35) if 'source-specific batteryless temperature:' in c['label']];self.conflict(rows);self.assertEqual({'-5..35 °C','5..35 °C'},{c['value']['text'] for c in rows})
    def test_central_unit_full_parameter_associations(self):
        rows=[c for c in self.rows(42) if 'Parameter and package associations: relationship:' in c['label']];self.assertEqual(6,len(rows));self.assertTrue(any('UNAVAILABLE_0000' in c['statement'] for c in rows));self.assertTrue(any('do not encode all UI schedules' in c['statement'] or 'encode all UI schedules' in c['statement'] for c in self.rows(42)))
    def test_control_boundary_and_enum_hole(self):
        self.assertTrue(any('associated actuator' in c['statement'] and 'TYPE socket' in c['statement'] for c in self.rows(44)));self.assertTrue(any('DEST_LEV omits 14' in c['statement'] and c['questions'] for c in self.rows(44)))
        self.assertTrue(any('M=CEN' in c['statement'] and 'absent' in c['statement'] for c in self.rows(43)))

if __name__=='__main__':unittest.main()
