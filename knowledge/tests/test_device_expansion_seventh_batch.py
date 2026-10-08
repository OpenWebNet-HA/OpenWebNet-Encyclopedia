"""Protect hotel-role, production-lot, timing, source-conflict and package boundaries."""
import json
import re
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]

class SeventhDeviceExpansionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.claims = [json.loads(s) for s in (ROOT/'knowledge/claims/claims.jsonl').read_text().splitlines()]
        cls.entities = [json.loads(s) for s in (ROOT/'knowledge/reference/entities.jsonl').read_text().splitlines()]
    def rows(self,n):
        return [c for c in self.claims if c['label'].startswith(f'OWN-DEV-{n:04d}:')]
    def has(self,n,text):
        return any(text in c['statement'] for c in self.rows(n))
    def test_commercial_and_module_identity_does_not_merge_indicator_and_reader(self):
        for n,object_id in [(104,489),(105,488),(106,488),(107,32)]:
            modules=[e for e in self.entities if e['label'].startswith(f'OWN-DEV-{n:04d}: Firmware') and e.get('entity_type')=='module']
            self.assertEqual(4 if n==107 else 1,len(modules))
            self.assertTrue(self.has(n,f'Object `{object_id}`'))
        self.assertTrue(self.has(105,'NO RFID'))
        self.assertTrue(self.has(106,'13.56 MHz'))
        self.assertTrue(self.has(106,'14w40'))
        self.assertTrue(self.has(104,'not an Ethernet port') or self.has(104,'external MH201'))
        self.assertTrue(self.has(107,'item `1340`'))
    def test_excluded_room_defaults_and_distinct_timer_layers_are_preserved(self):
        for n,filter_id in [(105,3106),(106,3105)]:
            rows=[c for c in self.rows(n) if 'Object/Firmware restrictions:' in c['label'] and f'Filter ID `{filter_id}`' in c['statement']]
            defaults=[c for c in rows if 'Reusable default:' in c['label']]
            domains=[c for c in rows if 'Effective catalogue domain:' in c['label']]
            self.assertEqual(1,len(defaults));self.assertEqual(1,len(domains))
            self.assertIn('`01`',defaults[0]['statement']);self.assertEqual(1,defaults[0]['value']['integer']);self.assertTrue(defaults[0]['questions'])
            self.assertIn('`0`',domains[0]['statement'])
        self.assertTrue(self.has(106,'`T=0`'))
        self.assertTrue(self.has(106,'`0.5 s`'))
        self.assertTrue(self.has(106,'value / 10'))
        self.assertTrue(self.has(106,'no attached conversion'))
        self.assertTrue(self.has(106,'All cards are accepted until a master'))
        self.assertTrue(self.has(106,'deletes every stored card'))
        self.assertTrue(self.has(104,'no physical procedure'))
    def test_true_conflicts_remain_reciprocal_but_revision_and_sku_changes_do_not(self):
        for n,label,values in [(105,'bell terminal notation',{'L / L1','L1 / L2'}),(107,'advanced scenario time requirement',{'obligatory','conditional'}),(107,'seasonal program capacity',{'5 program entries','3 summer / 3 winter programs'})]:
            rows=[c for c in self.rows(n) if 'source-specific '+label+':' in c['label']]
            self.assertEqual(2,len(rows));self.assertEqual(values,{c['value']['text'] for c in rows})
            for a,b in (rows,rows[::-1]):
                self.assertEqual([b['id']],a['claim_links']['contradicts']);self.assertTrue(a['questions'])
        radio=[c for c in self.rows(106) if 'variant-specific bidirectional radio:' in c['label']]
        self.assertEqual({'Yes','No'},{c['value']['text'] for c in radio})
        self.assertEqual(2,len({c['provenance'][0]['source_id'] for c in radio}))
        for c in radio:self.assertFalse(c['claim_links']['contradicts']);self.assertTrue(c['questions'])
        cards=[c for c in self.rows(107) if 'revision-specific bundled SD card:' in c['label']]
        self.assertEqual({'512 MB','2 GB'},{c['value']['text'] for c in cards})
        for c in cards:self.assertFalse(c['claim_links']['contradicts']);self.assertEqual('specified',c['applicability']['version']['state'])
    def test_complete_ranges_and_parameter_scope_are_not_installed_support(self):
        data=json.loads((ROOT/'devices/inventory/touch-screen-package-unicode-ranges.json').read_text())
        rows=[c for c in self.rows(107) if ': Canonical package character ranges (prepared supplement) / Package range associations ' in c['label']]
        self.assertEqual(4534,len(rows));actual=set()
        for c in rows:
            m=re.search(r'Unicode set: `(\d+)`; Range key: `(\d+)`; Minimum hexadecimal: `([0-9A-F]+)`; Maximum hexadecimal: `([0-9A-F]+)`',c['statement']);self.assertIsNotNone(m);actual.add(m.groups())
            self.assertEqual('public_database',c['provenance'][0]['evidence_class']);self.assertEqual('catalogue_documented',c['epistemic_status']);self.assertEqual('3.5.38',c['applicability']['version']['expression']);self.assertTrue(c['cautions'])
        self.assertEqual({(str(r['id_unicode_set']),str(r['id_unicode_range']),r['Min'],r['Max']) for r in data['ranges']},actual)
        self.assertTrue(self.has(107,'All 8 parameter-file associations'))
        self.assertTrue(self.has(107,'Package payloads remain unexamined'))
        self.assertTrue(self.has(107,'Serial is physically documented'))
        self.assertFalse(any(c['epistemic_status']=='observed' for n in range(104,108) for c in self.rows(n)))
    def test_unknown_physical_values_remain_unknown(self):
        rows=[c for c in self.rows(105) if ': Physical and electrical characteristics:' in c['label'] and 'Not established by' in c['statement']]
        self.assertEqual(1,len(rows));self.assertEqual('unknown',rows[0]['value']['state']);self.assertTrue(rows[0]['questions'])

if __name__ == '__main__':
    unittest.main()
