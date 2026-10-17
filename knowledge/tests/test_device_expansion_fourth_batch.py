"""Material boundaries in accepted Device migration 0046 through 0065."""
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

class FourthDeviceExpansionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.claims=[json.loads(x) for x in (ROOT/'knowledge/claims/claims.jsonl').read_text().splitlines()]
        cls.entities=[json.loads(x) for x in (ROOT/'knowledge/reference/entities.jsonl').read_text().splitlines()]
    def rows(self,n):return [c for c in self.claims if c['label'].startswith(f'OWN-DEV-{n:04d}:')]
    def modules(self,n):return [e for e in self.entities if e['label'].startswith(f'OWN-DEV-{n:04d}: Firmware') and e.get('entity_type')=='module']
    def conflict(self,n,label):
        rows=[c for c in self.rows(n) if 'source-specific '+label+':' in c['label']];self.assertEqual(2,len(rows))
        a,b=rows;self.assertEqual(a['subject_id'],b['subject_id'])
        for a,b in (rows,rows[::-1]):
            self.assertEqual([b['id']],a['claim_links']['contradicts']);self.assertTrue(a['questions']);self.assertNotEqual('observed',a['epistemic_status'])
        return rows
    def test_thermostat_revision_current_and_factory_conflicts(self):
        self.conflict(46,'production cutoff');self.conflict(46,'backlight-off current')
        r=self.conflict(46,'cooling eco default');self.assertEqual({'28 °C','25 °C'},{c['value']['text'] for c in r})
        self.assertEqual(2,len(self.modules(46)))
        self.assertTrue(any('PL `10..15`' in c['statement'] and c['questions'] for c in self.rows(46)))
    def test_touchscreen_variant_and_parameter_scopes(self):
        for n,count,modules in [(47,30,3),(49,20,2),(50,2,2)]:
            params=[c for c in self.rows(n) if 'Parameter and package associations: relationship:' in c['label']];self.assertEqual(count,len(params));self.assertEqual(modules,len(self.modules(n)))
        self.assertTrue(any('not extra catalogue Module slots' in c['statement'] for c in self.rows(47)))
        self.assertTrue(any('neither is catalogue default' in c['statement'] for c in self.rows(49)))
        self.assertTrue(any('physical Ethernet socket' in c['statement'] for c in self.rows(50)))
    def test_energy_display_pages_and_coefficient_are_not_invented_hardware(self):
        self.assertEqual(10,len(self.modules(48)))
        self.assertTrue(any('scaling relationship is suggested but not established' in c['statement'] for c in self.rows(48)))
        self.assertTrue(any('M 1=9 remains undocumented' in c['statement'] for c in self.rows(48)))
    def test_sensor_software_slots_and_source_conflicts(self):
        for n in [51,53,54,55,56,57,58,61,63]:
            self.assertEqual(17,len(self.modules(n)));self.assertFalse(any(c['epistemic_status']=='observed' for c in self.rows(n)))
        for n in [51,54]:self.conflict(n,'sensor consumption');self.conflict(n,'factory light threshold')
        self.conflict(54,'US coverage at3m medium');self.conflict(55,'enclosure protection')
        for n in [55,56,57,61]:self.conflict(n,'technical threshold range');self.conflict(n,'factory Auto')
        self.assertTrue(any('do not establish ultrasonic hardware' in c['statement'] for c in self.rows(51)))
        self.assertTrue(any('do not reinterpret these as a physical' in c['statement'].lower() for c in self.rows(53)))
    def test_missing_pdfs_keep_catalogue_identity_established(self):
        for n in [62,63]:
            self.assertTrue(any('Missing physical documentation does not make either identity unresolved' in c['statement'] for c in self.rows(n)))
            self.assertTrue(any('Physical ratings' in c['statement'] and 'not established' in c['statement'] for c in self.rows(n)))
        self.assertTrue(any('do not prove a wired connector' in c['statement'] for c in self.rows(63)))
    def test_basic_actuator_timing_input_and_unlabelled_value(self):
        self.assertTrue(any('M=`1..4` maps' in c['statement'] and '60/120/180/240' in c['statement'] for c in self.rows(59)))
        self.assertTrue(any('LOCAL_BUTTON` 60' in c['statement'] and c['questions'] for c in self.rows(60)))
        self.assertTrue(any('no conversion is stored' in c['statement'] for c in self.rows(60)))
    def test_controller_total_limit_and_fragment_scope(self):
        self.assertEqual(3,len(self.modules(64)));self.conflict(64,'supply range');self.conflict(64,'operating temperature')
        self.assertTrue(any('cannot be treated as 32 A aggregate' in c['statement'] for c in self.rows(64)))
        self.assertTrue(any('nominal missing pages 3–4' in c['statement'] for c in self.rows(64)))
    def test_memory_topology_exception_and_restoration_are_documented(self):
        self.assertEqual(1,len(self.modules(65)))
        self.assertTrue(any('exception is physical expansion' in c['statement'] for c in self.rows(65)))
        self.assertTrue(any('400 ms' in c['statement'] and '10 s' in c['statement'] for c in self.rows(65)))
        self.assertFalse(any(c['epistemic_status']=='observed' for c in self.rows(65)))

if __name__=='__main__':unittest.main()
