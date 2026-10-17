"""Complete public package data must not open an arbitrary inventory import route."""
import copy
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'knowledge/tools'))
from device_supplements import APPENDIX, LINK, supplement_text
from prepare_sources import sanitize

DEVICE = 'devices/definitions/own-dev-0102-multimedia-touch-screen.md'


class DeviceSupplementTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.data = json.loads((ROOT / APPENDIX).read_text())
        self.pins = json.loads((ROOT / 'knowledge/inputs/device-supplements.json').read_text())
        self.write()

    def write(self, pin=True):
        path = self.root / APPENDIX
        path.parent.mkdir(parents=True, exist_ok=True)
        raw = json.dumps(self.data).encode()
        path.write_bytes(raw)
        if pin:
            self.pins['documents'][DEVICE]['sha256'] = hashlib.sha256(raw).hexdigest()
        pins = self.root / 'knowledge/inputs/device-supplements.json'
        pins.parent.mkdir(parents=True, exist_ok=True)
        pins.write_text(json.dumps(self.pins))

    def render(self, text=None):
        return supplement_text(self.root, DEVICE, text or f'# Device\n[Complete ranges]({LINK})\n')

    def test_complete_rows_have_named_provenance_and_no_private_values(self):
        result = self.render()
        self.assertIn('their row provenance is the named appendix', result)
        self.assertIn('not establish firmware identity/network field character domains', result)
        for row in self.data['ranges']:
            self.assertIn(f'| `{row["id_unicode_set"]}` | `{row["id_unicode_range"]}` | `{row["Min"]}` | `{row["Max"]}` |', result)
        self.assertEqual(4534, sum(line.startswith('| `') for line in result.splitlines()))
        self.assertEqual([], sanitize(result)[1])
        self.assertEqual(result, self.render())

    def test_changed_bytes_require_explicit_review_even_when_valid_json(self):
        self.data['ranges'][0]['Max'] = '00FE'
        self.write(pin=False)
        with self.assertRaisesRegex(ValueError, 'fingerprint changed'):
            self.render()

    def test_repin_does_not_bypass_complete_numeric_and_provenance_checks(self):
        original = copy.deepcopy(self.data)
        mutations = [lambda d: d['ranges'].pop(),
                     lambda d: d['ranges'].__setitem__(1, d['ranges'][0]),
                     lambda d: d['ranges'][0].__setitem__('Min', '0100'),
                     lambda d: d['ranges'][0].__setitem__('Max', '110000'),
                     lambda d: d['ranges'][0].__setitem__('id_unicode_set', True),
                     lambda d: d.__setitem__('scope', 'Installation-specific inventory'),
                     lambda d: d['sets'][0].__setitem__('notes', 'private token'),
                     lambda d: d.__setitem__('source_sha256', '0' * 64)]
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                self.data = copy.deepcopy(original)
                mutate(self.data)
                self.write()
                with self.assertRaises(ValueError):
                    self.render()

    def test_unlinked_or_arbitrary_inventory_path_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'exact accepted public appendix link'):
            self.render('# Device\nNo appendix link\n')
        self.pins['documents'][DEVICE]['path'] = 'devices/inventory/private.json'
        self.write()
        with self.assertRaisesRegex(ValueError, 'exact accepted public appendix link'):
            self.render()

    def test_unselected_device_is_unchanged(self):
        self.assertEqual('unchanged', supplement_text(self.root, 'devices/definitions/own-dev-0001-control.md', 'unchanged'))


if __name__ == '__main__':
    unittest.main()
