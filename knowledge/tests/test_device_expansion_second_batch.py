"""Material boundaries in the second accepted-Device KB expansion."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class SecondDeviceExpansionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.claims = [json.loads(x) for x in (ROOT/'knowledge/claims/claims.jsonl').read_text().splitlines()]
        cls.entities = [json.loads(x) for x in (ROOT/'knowledge/reference/entities.jsonl').read_text().splitlines()]
        cls.sources = [json.loads(x) for x in (ROOT/'knowledge/reference/sources.jsonl').read_text().splitlines()]

    def rows(self, n):
        return [c for c in self.claims if c['label'].startswith(f'OWN-DEV-{n:04d}:')]

    def test_source_specific_soft_touch_selector_conflict(self):
        rows = [c for c in self.rows(24) if 'source-specific two-second selector:' in c['label']]
        self.assertEqual(2, len(rows))
        self.assertEqual({'SPE=7, M=1', 'SPE=8, M=1'}, {c['value']['text'] for c in rows})
        self.assertEqual(2, len({c['provenance'][0]['source_id'] for c in rows}))
        for a, b in (rows, rows[::-1]):
            self.assertEqual([b['id']], a['claim_links']['contradicts'])
            self.assertTrue(a['questions'])
            self.assertNotEqual('observed', a['epistemic_status'])

    def test_display_firmware_defaults_and_unexamined_payloads(self):
        rows = self.rows(15)
        defaults = [c for c in rows if c['label'].startswith('OWN-DEV-0015: Firmware-scoped configuration:')
                    and 'Field `FW_VER`' in c['statement'] and 'has Catalogue default' in c['statement']]
        self.assertEqual(4, len(defaults))
        self.assertTrue(all(c['value'] == {'state':'known','text':'`3.0.0`'} for c in defaults))
        associations = [c for c in rows if 'Parameter and package associations: relationship:' in c['label']]
        self.assertEqual(102, len(associations))  # 82 tool associations and 20 package rows
        self.assertTrue(all(c['epistemic_status']=='catalogue_documented' for c in associations))
        self.assertTrue(any('not been inspected' in c['statement'] for c in rows))
        self.assertTrue(any('not an installed-version observation' in c['statement'] for c in rows))

    def test_source_internal_shutter_conflict_and_separate_ui_contexts(self):
        rows = [c for c in self.rows(15) if 'source-internal Normal movement:' in c['label']]
        self.assertEqual(2, len(rows))
        self.assertEqual({'stops on release','requires Stop'}, {c['value']['text'] for c in rows})
        for a, b in (rows, rows[::-1]):
            self.assertEqual([b['id']], a['claim_links']['contradicts'])
            self.assertTrue(a['questions'])
        loads = [c for c in self.rows(15) if 'page load reactivation' in c['label'] or 'screen load reactivation' in c['label']]
        self.assertEqual(2, len(loads))
        self.assertEqual({'4 hours', '2 h 30 min'}, {c['value']['text'] for c in loads})
        self.assertTrue(all(c['questions'] and not c['claim_links']['contradicts'] for c in loads))
        self.assertEqual(2, len({c['applicability']['target'] for c in loads}))

    def test_unretained_local_display_figures_are_unresolved(self):
        rows = [c for c in self.rows(18) if 'unretained U1063B copy previously supplied' in c['statement']]
        self.assertEqual(1, len(rows))
        self.assertEqual('unresolved', rows[0]['value']['state'])
        self.assertEqual('unresolved', rows[0]['epistemic_status'])
        self.assertEqual('undetermined', rows[0]['confidence'])
        self.assertTrue(rows[0]['questions'])
        self.assertNotIn('text', rows[0]['value'])
        self.assertIn('not accepted ratings', rows[0]['statement'])

    def test_shared_roles_do_not_prove_hardware_capabilities(self):
        self.assertTrue(any('PIR-only' in c['statement'] and ('ultrasonic' in c['statement'] or 'US' in c['statement']) for c in self.rows(16)))
        modules = [e for e in self.entities if e['label'].startswith('OWN-DEV-0016: Firmware') and e['entity_type']=='module']
        self.assertEqual(17, len(modules))
        self.assertTrue(any('rather than as a stand-alone internal power stage' in c['statement'] for c in self.rows(27)))
        self.assertTrue(any('DALI/DSI' in c['statement'] and 'do not establish those electrical outputs' in c['statement'] for c in self.rows(25)))
        self.assertTrue(any('guide excludes' in c['statement'] and '`AUX`' in c['statement'] for c in self.rows(14)))

    def test_load_priority_conversions_remain_absent(self):
        rows = [c for c in self.rows(20) if 'Referenced conversion rule absent' in c['statement']]
        self.assertEqual(4, len(rows))
        self.assertTrue(all(c['questions'] for c in rows))
        self.assertTrue(any('EN_CONV_RULE' in c['statement'] and 'does not fabricate' in c['statement'] for c in self.rows(20)))
        self.assertTrue(any('maximum' in c['statement'] and '63' in c['statement'] for c in self.rows(20)))

    def test_receiver_current_discrepancy_remains_attributable(self):
        rows = [c for c in self.rows(29) if 'source-specific receiver ' in c['label']]
        self.assertEqual(3, len(rows))
        self.assertEqual({'2 mA','18 mA','22 mA maximum'}, {c['value']['text'] for c in rows})
        for c in rows:
            self.assertEqual({b['id'] for b in rows if b is not c}, set(c['claim_links']['contradicts']))
            self.assertTrue(c['questions'])
            self.assertNotEqual('observed', c['epistemic_status'])
        domain = [c for c in self.rows(29) if 'Field `MOD`' in c['statement'] and 'has Reusable domain' in c['statement']]
        self.assertEqual(1, len(domain))
        self.assertNotIn('`0`', domain[0]['value']['text'])
        self.assertTrue(any('self-learning' in c['statement'] and '`0`' in c['statement'] for c in self.rows(29)))

    def test_ean_html_originals_are_registered_catalogue_sources(self):
        sources = [s for s in self.sources if s['label'].endswith('.html') and s['provenance'][0]['location']['section_id'].startswith(('ownkb:section:d000157:', 'ownkb:section:d000158:'))]
        self.assertGreaterEqual(len(sources), 2)
        self.assertTrue(all(s['source_type']=='official_catalogue' and 'SHA-256' in s['title'] for s in sources))


if __name__ == '__main__':
    unittest.main()
