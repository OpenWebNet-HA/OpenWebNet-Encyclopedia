"""Preserve material source/model boundaries in the first expansion batch."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class DeviceExpansionSemanticsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.claims = [json.loads(line) for line in (ROOT / 'knowledge/claims/claims.jsonl').read_text().splitlines()]
        cls.entities = [json.loads(line) for line in (ROOT / 'knowledge/reference/entities.jsonl').read_text().splitlines()]

    def rows(self, device):
        return [c for c in self.claims if c['label'].startswith(device + ':')]

    def test_scenario_delete_thresholds_remain_attributable_and_conflicting(self):
        rows = [c for c in self.rows('OWN-DEV-0011') if 'source-specific single-scenario deletion:' in c['label']]
        self.assertEqual(2, len(rows))
        self.assertEqual({'8 seconds minimum', '10 seconds minimum'}, {c['value']['text'] for c in rows})
        self.assertEqual(2, len({c['provenance'][0]['source_id'] for c in rows}))
        for a, b in (rows, rows[::-1]):
            self.assertEqual([b['id']], a['claim_links']['contradicts'])
            self.assertTrue(a['questions'])
            self.assertEqual('official_specification', a['provenance'][0]['evidence_class'])
            self.assertIn('no hardware revision cutoff established', a['applicability']['target'])

    def test_published_m2_does_not_silently_repair_the_firmware_enum(self):
        rows = self.rows('OWN-DEV-0008')
        domain = [c for c in rows if c['label'].startswith('OWN-DEV-0008: Firmware-scoped configuration:')
                  and 'Field `M`' in c['statement'] and 'has Catalogue domain' in c['statement']]
        self.assertEqual(1, len(domain))
        self.assertEqual('`0..1`; `3..4`; `11` = `SLA`; `15` = `PUL`; `9` = `O/I`', domain[0]['value']['text'])
        reconciliation = [c for c in rows if 'genuine published physical mode' in c['statement']]
        self.assertEqual(1, len(reconciliation))
        self.assertNotEqual('observed', reconciliation[0]['epistemic_status'])

    def test_missing_enum_meanings_do_not_erase_a_known_default(self):
        rows = [c for c in self.rows('OWN-DEV-0013') if 'Field `PEOPLE_S`' in c['statement']]
        domain = next(c for c in rows if 'has Reusable domain' in c['statement'])
        default = next(c for c in rows if 'has Reusable default' in c['statement'])
        self.assertIn('`1` = ?; `2` = ?', domain['value']['text'])
        self.assertTrue(domain['questions'])
        self.assertEqual({'state': 'known', 'integer': 0}, default['value'])
        self.assertEqual(domain['subject_id'], default['subject_id'])

    def test_touch_sockets_and_fifth_module_remain_separate(self):
        modules = [e for e in self.entities if e['label'].startswith('OWN-DEV-0009: Firmware') and e['entity_type'] == 'module']
        self.assertEqual(5, len(modules))
        boundary = [c for c in self.rows('OWN-DEV-0009') if 'Database/document mapping boundary:' in c['label']]
        self.assertEqual(2, len(boundary))
        self.assertTrue(all(c['questions'] for c in boundary))
        self.assertTrue(any('No equivalence' in c['statement'] for c in boundary))

    def test_incomplete_predicates_are_preserved_without_repaired_tokens(self):
        rows = [c for c in self.rows('OWN-DEV-0003') if 'Source irregularities affecting selection:' in c['label']
                and 'incomplete/unresolved' in c['statement']]
        self.assertEqual(1, len(rows))
        self.assertIn('`A2<>GE`, standalone `A2`, and `A2<>`', rows[0]['statement'])
        self.assertIn('Do not repair missing tokens or infer condition precedence', rows[0]['statement'])
        self.assertTrue(rows[0]['questions'])

    def test_display_tool_associations_are_not_examined_payloads_or_extra_slots(self):
        rows = self.rows('OWN-DEV-0013')
        parameters = [c for c in rows if 'Parameter and package associations: relationship:' in c['label']]
        self.assertEqual(6, len(parameters))
        self.assertTrue(all(c['epistemic_status'] == 'catalogue_documented' for c in parameters))
        self.assertTrue(any('have not been inspected' in c['statement'] for c in rows))
        self.assertTrue(any('powered and not physically configured' in c['statement'] for c in rows))
        modules = [e for e in self.entities if e['label'].startswith('OWN-DEV-0013: Firmware') and e['entity_type'] == 'module']
        self.assertEqual(10, len(modules))  # five slots per distinct firmware definition


if __name__ == '__main__':
    unittest.main()
