"""Preserve scope boundaries in the final accepted Device ingestion batch."""
import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]

class FinalDeviceExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        records = json.loads((ROOT/'knowledge/inputs/claim-records.json').read_text())['claims']
        cls.claims = {n: [c for c in records if c['label'].startswith(f'OWN-DEV-{n:04d}:')]
                      for n in [190,191,192,193,194,195,196,197,198,199,201,202,203,204,205,206,208]}
    def require(self, n, *tokens):
        text = '\n'.join(c['statement'] for c in self.claims[n])
        for token in tokens: self.assertIn(token, text, (n,token))
    def test_material_disagreements_are_reciprocal_and_attributable(self):
        groups={191:['mechanical depth'],194:['mains supply'],198:['supply classification','documented interfaces'],
                201:['operating temperature'],202:['operating temperature'],203:['maximum draw'],204:['server version boundary'],
                205:['relay rating','guide relay rating'],206:['relay rating'],208:['scenario capacity','native user application']}
        for n,labels in groups.items():
            for label in labels:
                pair=[c for c in self.claims[n] if f': source-specific {label}:' in c['label']]
                self.assertEqual(2,len(pair));self.assertEqual(2,len({c['source_id'] for c in pair}))
                for c in pair:
                    self.assertEqual({p['id'] for p in pair if p is not c},set(c['claim_links']['contradicts']))
                    self.assertTrue(c['questions']);self.assertTrue(c['claim_links']['qualifies'])
    def test_missing_exact_manual_does_not_downgrade_catalogue_identity(self):
        self.require(192,'1812','1954','missing exact-product PDF','3.0.9','4.1.19')
        self.require(193,'573960','573958','1814','6.0.1','5.0.9','4.1.19')
        self.require(195,'2.1.7','3.0.7','not wholesale electrical or mechanical identity')
    def test_hotel_operations_and_editor_objects_keep_their_scope(self):
        self.require(190,'DND paragraph inconsistency','MUR','10-second restart','20-second DHCP','30-second log','not be equated with local diagnostic Objects','completed actions are not undone')
    def test_phone_connections_and_historical_service_are_distinct(self):
        self.require(191,'3489GSM','PSTN','rear six-way serial','four cycles','20 seconds')
        self.require(194,'56K modem','two-wire interface','8-wire','401/402','3.0.0')
    def test_handset_currents_jumper_and_ethernet_candidate_survive(self):
        self.require(196,'3/18 mA','27/275 mA','J1','J2','physical configuration only','not proof of an Ethernet interface','0..3999','0..99')
    def test_pir_hardware_is_not_ultrasonic_reusable_metadata(self):
        self.require(197,'ultrasonic transducer','No build row','16 IR slots','5 s 59 min 59 h','2454','2466','unresolved restriction','no replacement')
    def test_app_generation_and_gateway_labels_do_not_create_aliases(self):
        self.require(198,'not guarantee','Nuvo','HMAC','five physical sockets')
        self.require(199,'13 firmware definitions','20 retained build rows','30-zones-per-room','AA','AB','not a commercial alias','not recovered unless synchronised')
        self.require(208,'third-party software','50 scenarios','150 installer','transcription discrepancy','Blank F460/F461 cells')
    def test_control_topology_feedback_and_invalid_defaults_survive(self):
        self.require(201,'26W18','five roles','no direct firmware/Object','4135','3662','outside')
        self.require(202,'25W49','3569','4136','3664','200 VA','220 VA','no unit printed')
        self.require(203,'2–10 minutes','17 mA single','25.4 mA double','3666','calibration','not proof')
    def test_external_probe_scopes_and_actuator_restrictions_survive(self):
        self.require(204,'3457','8051','3757..3765','3766','3767','outside','2.1 and over','after 2.1','future use','scaling')
    def test_motor_and_lighting_ratings_are_not_normalized(self):
        self.require(205,'2 × 4 A','16 A','3706','no replacement','dashes','K4950')
        self.require(206,'3856','pulse motor','3795','16 A','2 A','no-neutral','interlocked')

if __name__ == '__main__': unittest.main()
