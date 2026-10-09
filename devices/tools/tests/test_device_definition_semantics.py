"""Regression cases for namespace, source status and configuration-value mistakes."""
import importlib.util
import sqlite3
import sys
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
spec = importlib.util.spec_from_file_location('device_checker', TOOLS / 'check-device-definitions.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class DeviceIndexCoverage(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        self.db.executescript('''
            create table EN_DEVICE(id_device integer,id_item integer,code text);
            insert into EN_DEVICE values(1,100,'HC/HS/HD1234');
            insert into EN_DEVICE values(2,100,'003001');
        ''')
        self.items = {'100': {'state': 'reviewed', 'outcome': {'device_ids': ['OWN-DEV-0001']}}}

    def tearDown(self):
        self.db.close()

    def check(self, references, did='OWN-DEV-0001'):
        text = '## Devices\n\n| Brand / line | SKU / reference | Relationship | Device definition | Notes |\n| --- | --- | --- | --- | --- |\n'
        for reference in references:
            text += f'| Example | `{reference}` | Established identity | [{did}](example.md) | Synthetic fixture |\n'
        return checker.index_coverage_errors(text, self.items, self.db)

    def test_literal_catalogue_code_and_printed_spacing(self):
        self.assertEqual(self.check(['HC/HS/HD1234', '0 030 01']), [])

    def test_complete_finish_expansion(self):
        self.assertEqual(self.check(['HC1234', 'HS1234', 'HD1234', '003001']), [])

    def test_incomplete_finish_expansion_is_rejected(self):
        self.assertTrue(any('HC/HS/HD1234' in error for error in self.check(['HC1234', 'HS1234', '003001'])))

    def test_missing_commercial_record_is_rejected(self):
        self.assertTrue(any('003001' in error for error in self.check(['HC/HS/HD1234'])))

    def test_wrong_device_and_missing_definition_are_rejected(self):
        errors = self.check(['HC/HS/HD1234', '003001'], did='OWN-DEV-0002')
        self.assertTrue(any('accepted Device OWN-DEV-0001 is missing' in error for error in errors))
        self.assertTrue(any('linked to another Device' in error for error in errors))


class DeviceDefinitionSemantics(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        self.db.row_factory = sqlite3.Row
        self.db.executescript('''
            create table EN_SLOTS(id_slot integer,first_slot integer,id_object_firmware integer);
            create table AS_OBJECT_FIRMWARE(id_object_firmware integer,id_firmware integer,id_key_object integer);
            create table EN_KEY_OBJECT(id_key_object integer,key_object integer);
            create table EN_CONF(id_conf integer,id_firmware integer,id_key_object integer,conf_name text);
            create table EN_CONF_RANGE(id_conf integer,value text,min_value integer,max_value integer,"default" text);
            insert into EN_SLOTS values(593,1,10);
            insert into AS_OBJECT_FIRMWARE values(10,2,480);
            insert into EN_KEY_OBJECT values(480,130);
            insert into EN_CONF values(1,2,0,'A');
            insert into EN_CONF values(2,0,480,'PL');
            insert into EN_CONF_RANGE values(1,null,0,9,'0');
            insert into EN_CONF_RANGE values(2,'1',null,null,'1');
            insert into EN_CONF_RANGE values(2,'3',null,null,'1');
        ''')
        self.text = '''## Firmware and hardware

| Firmware ID | Catalogue status | Default |
| --- | --- | --- |
| `2` | Official | Catalogue default |

## Module, Object, and Virgin Object model

| Module slot | External Object | Catalogue slot row ID | Catalogue Object key |
| --- | --- | --- | --- |
| `1` | `130` User interface | `593` | `480` |

## Firmware-scoped configuration

| Firmware | Field | Catalogue domain | Catalogue default |
| --- | --- | --- | --- |
| `2` | `A` | `0..9` | `0` |

## Object configuration surfaces

### Object `130` - User interface

| Field | Reusable domain | Reusable default |
| --- | --- | --- |
| `PL` | `1`; `3` | `1` |

## Diagnostic applicability

| Diagnostic surface | Device-specific use |
| --- | --- |
| `DIMENSION 30` | Resolve external KEYO `130` |
'''

    def tearDown(self):
        self.db.close()

    def semantic(self, text):
        return checker.catalogue_semantic_errors(text, self.db, [2])

    def values(self, text):
        return checker.configuration_value_errors(text, self.db, [2])

    def test_correctly_labelled_database_keys_are_allowed(self):
        self.assertEqual(self.semantic(self.text), [])
        self.assertEqual(self.values(self.text), [])

    def test_cross_reference_does_not_change_page_identity(self):
        text = """## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0088` | Project identity |

## Source reconciliation

A source inconsistency does not establish equivalence to `OWN-DEV-0086`.
"""
        self.assertEqual(checker.definition_device_ids(text), {"OWN-DEV-0088"})

    def test_database_row_is_not_a_module_slot(self):
        errors = self.semantic(self.text.replace('| `1` | `130` User', '| `593` | `130` User'))
        self.assertTrue(any('Module slot 1' in e for e in errors))

    def test_database_key_is_not_external_keyo(self):
        errors = self.semantic(self.text.replace('external KEYO `130`', 'external KEYO `480`'))
        self.assertTrue(any('external KEYO 130' in e for e in errors))

    def test_wildcard_is_not_firmware_status(self):
        errors = self.semantic(self.text.replace('Official', 'wildcard / unspecified applicability retained'))
        self.assertTrue(any('Status' in e for e in errors))

    def test_raw_status_and_default_are_not_presentation(self):
        errors = self.semantic(self.text.replace('Official', '`0`').replace('Catalogue default', '`1`'))
        self.assertEqual(len(errors), 2)

    def test_placeholder_cannot_hide_a_known_domain(self):
        text = self.text.replace('`0..9`', 'catalogue-defined')
        self.assertTrue(self.semantic(text))
        self.assertTrue(self.values(text))

    def test_correct_field_name_cannot_mask_wrong_domain(self):
        self.assertTrue(any('legal domain' in e for e in self.values(self.text.replace('`0..9`', '`0..10`'))))

    def test_missing_enum_member_is_detected(self):
        self.assertTrue(any('legal domain' in e for e in self.values(self.text.replace('`1`; `3`', '`1`'))))

    def test_wrong_default_is_detected(self):
        self.assertTrue(any('default differs' in e for e in self.values(self.text.replace('`0..9` | `0`', '`0..9` | `1`'))))

    def test_large_numeric_ranges_do_not_require_expansion(self):
        self.assertEqual(checker.numeric_intervals(['0..16777215', '16777216']), [(0, 16777216)])


if __name__ == '__main__':
    unittest.main()
