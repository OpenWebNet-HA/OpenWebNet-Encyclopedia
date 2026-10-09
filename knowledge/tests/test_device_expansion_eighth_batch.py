"""Guard accepted controls, sensing, conversion and transport boundaries in KB migration."""
import json
import re
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class EighthDeviceExpansionTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.claims=[json.loads(s) for s in (ROOT/'knowledge/claims/claims.jsonl').read_text().splitlines()]
 def rows(self,n):return [c for c in self.claims if c['label'].startswith(f'OWN-DEV-{n:04d}:')]
 def has(self,n,text):return any(text in c['statement'] for c in self.rows(n))
 def test_catalogue_identity_is_independent_of_pdf_and_physical_outputs(self):
  for n,sku in [(110,'067584'),(111,'067585'),(112,'067586'),(113,'067587')]:
   self.assertTrue(self.has(n,sku));self.assertTrue(self.has(n,'Established catalogue identity'))
   unknown=[c for c in self.rows(n) if ': Physical and electrical characteristics:' in c['label'] and c['value']['state']=='unknown']
   self.assertTrue(unknown)
   for c in unknown:self.assertEqual('unknown',c['value']['state']);self.assertTrue(c['questions'])
  self.assertTrue(self.has(108,'Only `344622` records video'))
  self.assertTrue(self.has(116,'not an Alexa Object'))
  self.assertTrue(self.has(119,'slots `2` or `4` only'))
 def test_excluded_defaults_are_not_repaired(self):
  for n,filter_id in [(109,3308),(112,3655),(113,4618),(114,3835),(115,3852),(116,3851),(118,4041),(125,1102)]:
   rows=[c for c in self.rows(n) if 'Object/Firmware restrictions:' in c['label'] and f'Filter ID `{filter_id}`' in c['statement']]
   defaults=[c for c in rows if ': Reusable default:' in c['label']]
   self.assertEqual(1,len(defaults));self.assertEqual(0,defaults[0]['value']['integer']);self.assertTrue(defaults[0]['questions'])
  self.assertTrue(self.has(109,'step 0.5 °C'));self.assertTrue(self.has(109,'step 5 s'));self.assertTrue(self.has(109,'step 1 min'))
  self.assertTrue(self.has(109,'only if both heating and cooling'))
 def test_complete_meter_conversion_boundaries_and_no_alias_invention(self):
  for n,rule_counts in [(120,{700:256,730:256,760:256}),(121,{800:275}),(122,{411:63}),(123,{411:63}),(124,{411:63})]:
   rows=[c for c in self.rows(n) if 'Device-specific conversions:' in c['label'] and 'Referenced rule:' in c['statement']]
   for rule,count in rule_counts.items():self.assertEqual(count,sum(f'Referenced rule: `{rule}`;' in c['statement'] for c in rows))
   if n in [120,121]:
    vals=[int(m[1]) for c in rows if (m:=re.search(r'`A123` = `(\d+)`',c['statement']))]
    self.assertEqual(set(range(256)),set(vals))
    self.assertTrue(all(c['cautions'] for c in rows))
  self.assertTrue(self.has(121,'`TOLLERANCE`'));self.assertTrue(self.has(121,'no alias equivalence'))
  for n in [122,123,124]:self.assertTrue(self.has(n,'64–69'));self.assertTrue(self.has(n,'no priority 0') or self.has(n,'Priority 0') or self.has(n,'priority 0'))
 def test_sensing_roles_and_connectors_do_not_expand_physical_capability(self):
  self.assertTrue(self.has(122,'not a protective residual-current circuit breaker'))
  self.assertTrue(self.has(123,'no documented integrated consumption sensor'))
  self.assertTrue(self.has(124,'does not establish an integrated consumption sensor'))
  self.assertTrue(self.has(125,'RJ45 does not mean Ethernet'))
  self.assertTrue(self.has(126,'Do not connect the RJ45 SCS bus to Ethernet'))
  self.assertTrue(self.has(126,'Do not mix DALI and DSI'))
  rows=[c for c in self.rows(126) if 'Device-specific conversions:' in c['label'] and 'Referenced rule:' in c['statement']]
  self.assertEqual(80,len(rows))
  for slot,rule in enumerate(range(7206,7214),1):
   rr=[c for c in rows if f'Referenced rule: `{rule}`;' in c['statement']];self.assertEqual(10,len(rr))
   for c in rr:
    a=int(re.search(r'`A=(\d+)`',c['statement'])[1]);pl=int(re.search(r'`PL` = `(\d+)`',c['statement'])[1]);self.assertEqual(0 if a==0 else slot,pl)
 def test_material_conflicts_are_reciprocal_and_qualified(self):
  for n,label,values in [(108,'depth',{'22 mm','25 mm'}),(109,'operating temperature',{'0..40 °C','-5..35 °C'}),(115,'standby current',{'9 mA','6 mA'}),(116,'mounting orientation',{'horizontal','vertical'}),(118,'LED lamp count',{'10 lamps','2 lamps'}),(125,'open-field radio range',{'approximately 150 m','100 m'}),(127,'depth 345020',{'22 mm','20 mm'})]:
   rows=[c for c in self.rows(n) if f': source-specific {label}:' in c['label']];self.assertEqual(2,len(rows));self.assertEqual(values,{c['value']['text'] for c in rows})
   for a,b in (rows,rows[::-1]):self.assertEqual([b['id']],a['claim_links']['contradicts']);self.assertTrue(a['questions']);self.assertTrue(a['cautions'])
  self.assertFalse(any(c['epistemic_status']=='observed' for n in range(108,128) for c in self.rows(n)))
if __name__=='__main__':unittest.main()
