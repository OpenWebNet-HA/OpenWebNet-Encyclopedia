"""Accepted video-entry and interface boundaries retained in the shared KB."""
import json
import re
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class BatchElevenBoundaries(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.claims=json.loads((ROOT/'knowledge/inputs/claim-records.json').read_text())['claims'];cls.byid={c['id']:c for c in cls.claims}
 def device(self,n):return [c for c in self.claims if c['label'].startswith(f'OWN-DEV-{n:04d}:')]
 def text(self,n):return '\n'.join(c['statement'] for c in self.device(n))
 def test_conflicts_have_distinct_sources_reciprocal_links_and_governing_units(self):
  for n,label,count in [(159,'width',3),(159,'HomeKit support',2),(160,'monitor height',2),(165,'handsfree operation',2),(166,'camera classification',2),(168,'camera field',2)]:
   g=[c for c in self.device(n) if c['label'].startswith(f'OWN-DEV-{n:04d}: source-specific {label}:')];self.assertEqual(count,len(g));self.assertEqual(count,len({c['source_id'] for c in g}))
   for c in g:
    self.assertEqual({z['id'] for z in g if z is not c},set(c['claim_links']['contradicts']));self.assertTrue(c['questions']);p=self.byid[c['claim_links']['qualifies'][0]];self.assertIn(p['statement'],c['statement'])
 def test_hometouch_does_not_import_eos_or_newer_server_support(self):
  t=self.text(156)
  for token in ['incompatible with Classe 300EOS','compatible only with MyHOMEServer1','additional supply','4hours','country','not a scenario programming editor']:self.assertIn(token.lower(),t.lower())
 def test_classe100_generations_and_invalid_port_remain_qualified(self):
  t=self.text(157)
  for token in ['mutually incompatible firmware','black background','purple','65536','valid 16-bit port','344782','inductive loop to 344682']:self.assertIn(token,t)
 def test_easykit_components_do_not_transfer_between_skus(self):
  t=self.text(158)
  for token in ['not 318011','kit-wide counts','20m','80/100m','CLASSE100X','deletes all associated account']:self.assertIn(token,t)
  t=self.text(160)
  for token in ['one connected IU per family','SP102','not `365225`','French wording','24 V']:self.assertIn(token,t)
 def test_eos_capacities_and_future_terminal_remain_revision_scoped(self):
  t=self.text(159)
  for token in ['future application','175','350','F422A','one simultaneously connected installer','physically configured','25 high-resolution15 s','35']:self.assertIn(token,t)
 def test_shutter_filter_keeps_default_outside_subset(self):
  rows=[c for c in self.device(161) if 'Filter ID `4620`' in c['statement']]
  self.assertTrue(rows);self.assertTrue(any('Standard with slats' in c['statement'] for c in rows));self.assertTrue(any('outside this subset' in c['evidence_note'] for c in rows))
  t=self.text(161)
  for token in ['Virgin-only','>5 s','>3 s','MX5220','Y4672M2S','unit typo']:self.assertIn(token,t)
 def test_shared_ip_object_does_not_merge_hardware_or_network_workflows(self):
  a=self.text(162);b=self.text(163)
  for token in ['1..4000','101..190','2..4','100-IP-device','C=0..9']:self.assertIn(token,a)
  for token in ['RS232','D45/IP interface Config 2.0','TiDeviceIP_0400','Do not use Ethernet RJ45 pin assumptions','examples, not universal']:self.assertIn(token,b)
 def test_sfera_camera_and_hierarchy_limits_do_not_backport(self):
  for n in [166,167,168]:
   t=self.text(n)
   for token in ['01.02.31','builds 25 and 30','100..255','default 0','not proof that this module is an IP gateway']:self.assertIn(token,t)
  self.assertIn('does not contain a camera',self.text(166));self.assertIn('92° horizontal',self.text(167));self.assertIn('135° horizontal',self.text(168));self.assertIn('not transferred to 351300',self.text(168))
 def test_new_network_and_authentication_literals_are_prepared(self):
  for n in [156,159,162,163]:
   t=json.dumps(self.device(n));self.assertNotIn('192.168.',t);self.assertIn('[NETWORK_ADDRESS]',t)
  self.assertNotIn('12345',json.dumps(self.device(165)))
if __name__=='__main__':unittest.main()
