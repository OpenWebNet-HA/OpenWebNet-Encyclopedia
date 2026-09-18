# Relationship Register

This register summarizes relationships whose evidence affects more than one documentation section. Detailed semantics remain on the linked reference pages.

## Within `MHCatalogue.db`

| Source | Target | Conditions | Status |
| --- | --- | --- | --- |
| `EN_DEVICE.id_item` | `EN_ITEM.id_item` | none | structurally established |
| `EN_DEVICE.id_brand` | `EN_BRAND.id_brand` | none | structurally established |
| `EN_DEVICE.id_line` | `EN_LINE.id_line` | none | structurally established |
| `EN_FIRMWARE.id_item` | `EN_ITEM.id_item` | none | structurally established |
| `AS_OBJECT_FIRMWARE` | firmware and Object parents | both keys resolved | structurally established |
| `EN_SLOTS.id_object_firmware` | `AS_OBJECT_FIRMWARE.id_object_firmware` | none | structurally established |
| `EN_KEY_OBJECT.id_family` | `EN_OBJECT_ITEM_FAMILY.id_family` | none; zero is not used | structurally established |
| firmware/Virgin-Object associations | firmware and Virgin Object | through association identities | structurally established |
| `AS_OBJECT_VIRGIN_OBJECT` | Virgin Object and permitted Object | capability, not runtime selection | structurally established |
| `EN_CONF_RANGE.id_conf` | `EN_CONF.id_conf` | none | structurally established |
| `EN_FILTER` | Object/firmware association and configuration definition | context-specific | structurally established |
| `EN_CONF` owner | Object or firmware | selected by zero-sentinel discriminator | established polymorphic relationship |

## Within `OPEN.db`

| Source | Target | Evidence | Status |
| --- | --- | --- | --- |
| `AS_SYSTEM_ADDRESS_RULE` | system and address rule | `OpenQuery.txt` and complete joins | established |
| `AS_OPEN_SYSTEM` | frame and system | schema/data | established |
| `AS_OPEN_PARAM` | frame and parameter | schema/data and `OpenQuery.txt` | established |
| `AS_SCENARIO_SEQUENCE` | scenario and ordered sequence | `OpenQuery.txt` | established |
| `AS_OPEN_SEQUENCE` | sequence and ordered frame | `OpenQuery.txt` | established |
| `AS_TIMEOUT_OPEN_SEQUENCE` | sequence/frame context and timeout | `OpenQuery.txt` | established |

## Across implementation models

| Source | Target | Conditions | Status |
| --- | --- | --- | --- |
| `DIMENSION 1.OBJECT_MODEL` | `AS_ITEM_SYSTEM.modobj` | resolved management family | corroborated |
| `DIMENSION 1.BRAND` | `EN_BRAND.brand_modobj` | none after identity parsing | corroborated |
| `DIMENSION 1.LINE` | `EN_LINE.line_modobj` | none after identity parsing | corroborated |
| `DIMENSION 1.N_CONF` | number of physical configurator positions | product documentation available | corroborated for documented Devices |
| `DIMENSION 30.KEYO` | `EN_KEY_OBJECT.key_object` | `STATE = 1` | corroborated |
| `DIMENSION 30.KEYO` | `EN_VIRGIN_OBJECT.virgin_key_object` | `STATE = 0` | corroborated |
| `DIMENSION 30.SLOT` | `EN_SLOTS.first_slot` placement | resolved firmware | structurally corroborated |
| `DIMENSION 35.INDEX` | `EN_CONF.idx` | resolved Device, firmware, Module, Object, and scope | strongly corroborated |
| `rules.KOBJECTS` | `EN_KEY_OBJECT.key_object` | Objects `95`, `96`, and `184` in this revision | strongly corroborated |
| `rules.db3` `$N` reference | `EN_CONF.idx = N` | selected Object context | strongly corroborated |
| `EN_ADDRESS_RULE.object_device_family` | `EN_OBJECT_ITEM_FAMILY.id_family` | nonzero value; `0` is unqualified | structurally and semantically corroborated |
| ScenarioDevices `ChiOpen` | parsed literal-frame `WHO` | literal frame present | established for all 57 literal templates |
| ScenarioDevices ProgramData semantic path | Program Files semantic path | compare full hierarchy, not local IDs | established subset relationship |

## Strong hypotheses

| Source | Candidate target | Evidence | Missing proof |
| --- | --- | --- | --- |
| `DIMENSION 32.SYS` | `MHCatalogue.db.EN_SYSTEM.sys_modobj` | field role, domain, Object/system graph, and non-primary-key design | discriminating non-Lighting capture |
| diagnostic outer `WHERE` | internal slot `1` configured address | repeated `WHO 1001` observations | cross-family and alternate-layout coverage |
| physical firmware property | advanced Object property | symbol, semantic type, filters, and conversions | complete mapping for most firmware |
| `N_CONF` | count of applicable physical fields | matching product diagrams and firmware metadata | systematic catalogue-wide test |

## Explicit unknowns

- generic meaning of `DIMENSION 310.VAL_PAR`;
- exact `DIMENSION 4` and `5` configurator encoding;
- runtime purpose of ScenarioDevices matching identifiers;
- ScenarioDevices source-file precedence;
- application persistence format for user-authored scenario graphs.
