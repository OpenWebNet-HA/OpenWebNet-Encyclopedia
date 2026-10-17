"""Original evidence, examination methods and scope use public synthetic fixtures."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'knowledge/tools'))
from evidence_reviews import load_reviews, join_claim_evidence, corpus_evidence
from render_artifacts import chunk_records, corpus

REV = 'a' * 40
SID = 'ownkb:source:archive'
CID = 'ownkb:claim:example'
LOC = {'document_id': 'ownkb:document:example', 'path': 'protocol/example.md',
       'section_id': 'ownkb:section:example'}


class OriginalEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.addCleanup(self.tmp.cleanup)
        for directory in ('knowledge/inputs', 'knowledge/schema', 'project/review'):
            (self.root / directory).mkdir(parents=True)
        schema = json.loads((ROOT / 'knowledge/schema/evidence-reviews.schema.json').read_text())
        self.validator = Draft202012Validator(schema)
        (self.root / 'knowledge/schema/evidence-reviews.schema.json').write_text(json.dumps(schema))
        (self.root / 'project/review/example.md').write_text('## Synthetic review\nRecorded execution case.\n')
        self.source = {'id': SID, 'kind': 'source', 'source_type': 'implementation_artifact',
                       'artifact_locator': {'kind': 'git_file', 'repository': 'MyOpenCommunity/libqtdevices',
                                            'revision': REV, 'line_count': 20,
                                            'public_uri': 'https://github.com/example/public/blob/' + REV + '/example.cpp'}}
        self.refs = {'source': [self.source, {'id': 'ownkb:source:explanation', 'kind': 'source',
                                            'source_type': 'canonical_documentation',
                                            'provenance': [{'location': LOC}]}]}
        self.ir = {'documents': [{'id': LOC['document_id'], 'path': LOC['path'],
                                 'sections': [{'id': LOC['section_id']}]}]}
        ex = {'method': 'source_inspection', 'implementation_role': 'library',
              'conclusion_kind': 'direct', 'relationship': 'supports', 'claim_ids': [CID],
              'code_location': {'symbol': 'publicHelper', 'start_line': 3, 'end_line': 8},
              'conditions': [], 'limitations': ['Pinned source only; no hardware observation.']}
        self.finding = {'id': 'moc-e9999', 'section_id': LOC['section_id'], 'summary': 'Scoped helper',
                        'disposition': 'claimed', 'reason': 'Direct pinned implementation finding.',
                        'claim_ids': [CID], 'review_path': 'project/review/example.md',
                        'review_locator': 'Synthetic review',
                        'supports': [{'source_id': SID, 'evidence_class': 'implementation_artifact',
                                      'examination': ex}]}
        self.claim = {'id': CID, 'confidence': 'high', 'provenance': [
            {'source_id': SID, 'evidence_class': 'implementation_artifact', 'location': LOC}],
                      'applicability': {'domain': 'implementation', 'version': {'expression': REV}}}

    def run_record(self):
        return {'material': 'original_helper_in_adapted_harness', 'setup': 'Controlled callbacks.',
                'inputs': ['Public input'], 'result': 'One recorded comparison passed.',
                'record_path': 'project/review/example.md', 'record_locator': 'Recorded execution case'}

    def load(self, finding=None):
        value = {'format_version': '2.0.0', 'findings': [finding or self.finding]}
        (self.root / 'knowledge/inputs/evidence-reviews.json').write_text(json.dumps(value))
        return load_reviews(self.root, self.ir, self.refs, {CID})

    def test_inspection_cannot_masquerade_as_execution(self):
        for method in ('source_inspection', 'test_expectation_inspection', 'static_firmware_analysis'):
            value = copy.deepcopy(self.finding)
            value['supports'][0]['examination'].update(method=method, execution=self.run_record())
            with self.subTest(method=method), self.assertRaises(Exception):
                self.load(value)
        for method in ('helper_execution', 'dynamic_firmware_oracle', 'hardware_observation'):
            value = copy.deepcopy(self.finding)
            value['supports'][0]['examination']['method'] = method
            with self.subTest(method=method), self.assertRaises(Exception):
                self.load(value)

    def test_execution_material_cannot_hide_a_different_method(self):
        for method, material in [('helper_execution', 'physical_hardware'),
                                 ('dynamic_firmware_oracle', 'original_test_suite'),
                                 ('hardware_observation', 'simulator')]:
            finding = copy.deepcopy(self.finding)
            ex = finding['supports'][0]['examination']
            ex.update(method=method, execution=self.run_record())
            ex['execution']['material'] = material
            with self.subTest(method=method), self.assertRaises(Exception):
                self.load(finding)

    def test_original_execution_conditions_and_record_are_preserved(self):
        ex = self.finding['supports'][0]['examination']
        ex.update(method='helper_execution', execution=self.run_record(), conditions=['Controlled callbacks.'])
        joined = self.load()
        join_claim_evidence([self.claim], joined, self.refs)
        original = next(e for e in self.claim['provenance'] if 'examination' in e)
        self.assertEqual(self.run_record(), original['examination']['execution'])
        self.assertEqual(['Controlled callbacks.'], original['examination']['conditions'])
        self.assertEqual('high', self.claim['confidence'])
        ex['execution']['record_locator'] = 'Unrecorded result'
        with self.assertRaisesRegex(ValueError, 'execution record'):
            self.load()

    def test_artifact_and_explanatory_page_stay_separate(self):
        joined = self.load()
        join_claim_evidence([self.claim], joined, self.refs)
        entries = self.claim['provenance']
        self.assertEqual({SID, 'ownkb:source:explanation'}, {e['source_id'] for e in entries})
        self.assertTrue(all(e['location'] == LOC for e in entries))
        self.assertIn('not independent', next(e for e in entries if 'examination' not in e)['evidence_note'])
        self.assertEqual(REV, self.refs['source'][0]['artifact_locator']['revision'])

    def test_source_scope_and_revision_are_required(self):
        for domain, revision in [('protocol', REV), ('implementation', 'b' * 40)]:
            value = copy.deepcopy(self.claim)
            value['applicability'] = {'domain': domain, 'version': {'expression': revision}}
            with self.subTest(domain=domain), self.assertRaises(ValueError):
                join_claim_evidence([value], self.load(), self.refs)
        with self.assertRaisesRegex(ValueError, 'lacks reviewed examination'):
            join_claim_evidence([self.claim], {'claims': {}, 'sections': {}}, self.refs)

    def test_expected_test_context_is_not_inherited_by_every_atom(self):
        test = copy.deepcopy(self.finding['supports'][0])
        test['examination']['method'] = 'test_expectation_inspection'
        test['examination']['claim_ids'] = []
        test['examination']['limitations'] = ['Context inspection; no mapped assertion.']
        self.finding['supports'].append(test)
        joined = self.load()
        join_claim_evidence([self.claim], joined, self.refs)
        self.assertEqual(2, len(joined['sections'][LOC['section_id']][0]['provenance']))
        self.assertEqual(['source_inspection'], [e['examination']['method'] for e in self.claim['provenance'] if 'examination' in e])

    def test_mixed_section_does_not_reclassify_specification_claim(self):
        normative = {'id': 'ownkb:claim:published', 'confidence': 'medium', 'provenance': [
            {'source_id': 'ownkb:source:explanation', 'evidence_class': 'official_specification', 'location': LOC}],
                     'applicability': {'domain': 'protocol', 'version': {'state': 'unknown'}}}
        before = copy.deepcopy(normative)
        join_claim_evidence([self.claim, normative], self.load(), self.refs)
        self.assertEqual(before, normative)
        self.assertEqual('high', self.claim['confidence'])

    def test_missing_original_locator_and_invalid_line_bounds_fail(self):
        self.source.pop('artifact_locator')
        with self.assertRaisesRegex(ValueError, 'original artifact'):
            self.load()
        self.setUp()
        for start, end in [(9, 8), (3, 21)]:
            self.finding['supports'][0]['examination']['code_location'].update(start_line=start, end_line=end)
            with self.subTest(bounds=(start, end)), self.assertRaisesRegex(ValueError, 'code location'):
                self.load()

    def test_dangling_claim_and_outside_finding_mapping_fail(self):
        self.finding['claim_ids'] = ['ownkb:claim:missing']
        with self.assertRaisesRegex(ValueError, 'dangling'):
            self.load()
        self.finding['claim_ids'] = [CID]
        self.finding['supports'][0]['examination']['claim_ids'] = ['ownkb:claim:outside']
        with self.assertRaisesRegex(ValueError, 'outside finding'):
            self.load()

    def test_deferred_reason_and_original_evidence_survive_reading(self):
        self.finding.update(disposition='deferred', claim_ids=[], reason='Needs captured hardware behavior.')
        self.finding['supports'][0]['examination']['claim_ids'] = []
        joined = self.load()
        self.assertFalse(joined['claims'])
        text = '\n'.join(corpus_evidence(joined['sections'][LOC['section_id']], {SID: self.source}))
        self.assertIn('Needs captured hardware behavior.', text)
        self.assertIn('source_inspection', text)
        self.assertIn(REV, text)
        self.finding['claim_ids'] = [CID]
        with self.assertRaisesRegex(ValueError, 'unmaterialized'):
            self.load()

    def test_future_static_firmware_and_dynamic_oracle_are_distinct(self):
        self.source['artifact_locator'] = {'kind': 'immutable_artifact', 'label': 'Public synthetic firmware',
                                          'version': 'public-build', 'sha256': 'a' * 64}
        ex = self.finding['supports'][0]['examination']
        ex.pop('code_location')
        ex.update(method='static_firmware_analysis', implementation_role='firmware',
                  artifact_location={'address_space': 'file bytes', 'start_offset': 0, 'end_offset': 8})
        self.finding['id'] = 'firmware-static-example'
        static = self.load()
        self.assertNotIn('execution', static['claims'][CID][0]['examination'])
        self.assert_firmware_exports(static, 'static_firmware_analysis')
        self.finding['id'] = 'firmware-oracle-example'
        ex.update(method='dynamic_firmware_oracle', execution=self.run_record())
        ex['execution']['material'] = 'firmware_oracle'
        dynamic = self.load()
        self.assertEqual('firmware_oracle', dynamic['claims'][CID][0]['examination']['execution']['material'])
        self.assert_firmware_exports(dynamic, 'dynamic_firmware_oracle')
        ex['artifact_location']['start_offset'] = 9
        with self.assertRaisesRegex(ValueError, 'reversed artifact'):
            self.load()

    def assert_firmware_exports(self, reviewed, method):
        """A future firmware finding must survive claims, reading and validated search."""
        ir = copy.deepcopy(self.ir)
        document = ir['documents'][0]
        context = {'area': 'protocol', 'namespace': 'openwebnet'}
        document.update(source_id='ownkb:source:explanation', namespace_context=context)
        section = document['sections'][0]
        section.update(title='Synthetic firmware finding', level=1, parent=None,
                       namespace_context=context,
                       privacy={'classification': 'public', 'removed_value_classes': []},
                       provenance={**LOC, 'source_id': document['source_id'],
                                   'evidence_class': 'canonical_documentation'},
                       blocks=[{'type': 'paragraph',
                                'inline': [{'type': 'text', 'text': 'Synthetic finding.'}],
                                'applicability': [], 'cautions': [], 'uncertainty': [],
                                'provenance_references': []}])
        sources = {source['id']: source for source in self.refs['source']}
        chunks, _ = chunk_records(ir, {LOC['section_id']: 'ownkb:chunk:r999999'}, {},
                                  {LOC['document_id']: 'ownkb:namespace:openwebnet'},
                                  reviewed['sections'], sources)
        schemas = [json.loads((ROOT / 'knowledge/schema' / name).read_text()) for name in
                   ('retrieval-chunks.schema.json', 'common.schema.json', 'privacy-metadata.schema.json')]
        registry = Registry().with_resources((s['$id'], Resource.from_contents(s)) for s in schemas)
        Draft202012Validator(schemas[0], registry=registry).validate(chunks[0])
        support = chunks[0]['evidence_support'][0]
        self.assertEqual(self.finding['id'], support['finding_id'])
        self.assertEqual(reviewed['claims'][CID], support['provenance'])
        claim = copy.deepcopy(self.claim)
        claim['applicability'] = {'domain': 'firmware', 'version': {'expression': 'public-build'}}
        join_claim_evidence([claim], reviewed, self.refs)
        self.assertEqual('high', claim['confidence'])
        original = next(e for e in claim['provenance'] if 'examination' in e)
        self.assertEqual(method, original['examination']['method'])
        self.assertEqual('execution' in original['examination'], method == 'dynamic_firmware_oracle')
        reading = corpus(ir, reviewed['sections'], sources).decode()
        for text in (chunks[0]['text'], reading):
            self.assertIn(self.finding['id'], text)
            self.assertIn(method, text)
            self.assertIn('public-build', text)
            self.assertIn('Pinned source only; no hardware observation.', text)
            if method == 'dynamic_firmware_oracle':
                self.assertIn('One recorded comparison passed.', text)

    def test_finding_id_grammar_matches_all_projections(self):
        schemas = {name: json.loads((ROOT / 'knowledge/schema' / name).read_text()) for name in
                   ('common.schema.json', 'evidence-reviews.schema.json', 'retrieval-chunks.schema.json')}
        definitions = [schemas['common.schema.json']['$defs']['examination']['properties']['finding_id'],
                       schemas['evidence-reviews.schema.json']['properties']['findings']['items']['properties']['id'],
                       schemas['retrieval-chunks.schema.json']['properties']['evidence_support']['items']['properties']['finding_id']]
        for value, accepted in [('moc-e0170', True), ('firmware-static-example', True),
                                ('firmware-oracle-example', True), ('Firmware', False),
                                ('../private', False), ('x' * 65, False)]:
            for definition in definitions:
                with self.subTest(finding=value, definition=definition):
                    self.assertEqual(accepted, Draft202012Validator(definition).is_valid(value))


if __name__ == '__main__':
    unittest.main()
