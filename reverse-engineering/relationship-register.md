# Relationship Register

This register is the compact index of relationships whose evidence affects more than one documentation section. It records namespace, conditions, coverage, and confidence; detailed operational semantics remain on the linked reference pages.

## Status vocabulary

| Status | Meaning |
| --- | --- |
| Declared | enforced or explicitly represented by the stored schema |
| Structurally established | complete non-sentinel key coverage and compatible table/cardinality role in this revision |
| Corroborated | independent database, capture, UI, or product evidence confirms the meaning |
| Strongly inferred | one candidate best explains the complete pattern, but a discriminating observation is missing |
| Open | evidence cannot yet distinguish the remaining candidates |
| Rejected | evidence conflicts with the proposed relationship |

Counts are scoped to the canonical MyHOME Suite 3.5.38 sources.

## Within `MHCatalogue.db`

| Source | Target | Coverage/conditions | Status |
| --- | --- | --- | --- |
| `EN_DEVICE.id_item` | `EN_ITEM.id_item` | 541 rows; 0 orphans | structurally established |
| `EN_DEVICE.id_brand` | `EN_BRAND.id_brand` | 541 rows; 0 orphans | structurally established |
| `EN_DEVICE.id_line` | `EN_LINE.id_line` | 541 rows; 0 orphans | structurally established |
| `EN_FIRMWARE.id_item` | `EN_ITEM.id_item` | 311 rows; 0 orphans | structurally established |
| `EN_BUILDS.id_firmware` | `EN_FIRMWARE.id_firmware` | 308 rows; 0 orphans; zero/multiple build rows possible per firmware | structurally established |
| `AS_ITEM_SYSTEM` | item and catalogue-system parents | 223 rows; 0 orphans on either parent | structurally established |
| `AS_OBJECT_SYSTEM` | Object and catalogue-system parents | 251 rows; 0 orphans on either parent | structurally established |
| `AS_OBJECT_FIRMWARE` | firmware and Object parents | 827 rows; 0 orphans on either parent | structurally established |
| `AS_FIRMWARE_CONFIG_MODE` | firmware and configuration-mode parents | firmware capability association; `EN_CONFIG_MODE` keeps Virtual, Advanced, Physical, and Product Programming as distinct records | structurally established |
| `EN_SLOTS.id_object_firmware` | `AS_OBJECT_FIRMWARE.id_object_firmware` | 1,725 rows; several Object alternatives can share `first_slot` | structurally established |
| `EN_KEY_OBJECT.id_family` | `EN_OBJECT_ITEM_FAMILY.id_family` | 158 rows; 0 orphans; no zero sentinel used | structurally established |
| `AS_FIRMWARE_VIRGIN_OBJECT` | firmware and Virgin Object parents | 75 rows; 0 orphans | structurally established |
| `AS_OBJECT_VIRGIN_OBJECT` | Virgin Object and permitted Object parents | 102 rows; capability set, not runtime selection | structurally established |
| `EN_CONF_RANGE.id_conf` | `EN_CONF.id_conf` | 14,346 rows; 0 orphans | structurally established |
| `EN_FILTER` | Object/firmware association and configuration definition | 1,909 rows; 0 orphans on both references | structurally established |
| `AS_SLOT_CONDITION` | slot-placement row and condition | 1,000 rows; 0 orphans on both references | structurally established |
| physical condition branch | firmware `EN_CONF`/`EN_CONF_RANGE` domains plus `EN_SLOTS`/`AS_SLOT_CONDITION`/`EN_CONDITION` | stored condition must be reachable in the exact firmware domain before it can select an Object/slot candidate | catalogue-native resolver established for represented predicates |
| `EN_CONF` owner | Object or firmware | 1,420 Object-scoped; 1,463 firmware-scoped; selected by zero discriminator | established polymorphic relationship |
| `EN_FIRMWARE.slots` | distinct internal Module positions | compare with `COUNT(DISTINCT EN_SLOTS.first_slot)`, not row count | corroborated capability relationship |

See [Database Relationship Reconstruction](database-relationship-reconstruction.md) and [Device Model](../device-model/).

## Within `OPEN.db`

| Source | Target | Coverage/evidence | Status |
| --- | --- | --- | --- |
| `AS_SYSTEM_ADDRESS_RULE` | system and address-rule parents | 16 rows; 0 orphans; loaded by `OpenQuery.txt` | established |
| `AS_OPEN_SYSTEM` | frame and system parents | 251 rows; 0 orphans | established |
| `AS_OPEN_PARAM` | frame and parameter parents | 91 rows; 0 orphans; queried by `OpenQuery.txt` | established |
| `AS_SCENARIO_SEQUENCE` | scenario and ordered sequence | 39 rows; 0 orphans | established |
| `AS_OPEN_SEQUENCE` | sequence and ordered frame | 147 rows; 0 orphans; carries order/repetition/status metadata | established |
| `AS_TIMEOUT_OPEN_SEQUENCE` | frame/sequence context and timeout | 62 rows; 0 orphans on all three parents | established |
| `EN_OPEN.open_string` placeholders | `EN_OPEN_PARAM.param_string` | association required; placeholder text alone is not a global key | established where associated |

## Across wire traffic and catalogue

| Source | Target | Required context | Status |
| --- | --- | --- | --- |
| `DIMENSION 1.OBJECT_MODEL` | `AS_ITEM_SYSTEM.modobj` | resolved management/catalogue system | corroborated |
| `DIMENSION 1.BRAND` | `EN_BRAND.brand_modobj` | parsed identity response | corroborated |
| `DIMENSION 1.LINE` | `EN_LINE.line_modobj` | parsed identity response | corroborated |
| ordinary addressed `DIMENSION 1.N_CONF` | physical configurator-position count | addressed Device identity; product diagrams/captures | corroborated for documented addressed Devices |
| gateway `DIMENSION 1.N_CONF` | unresolved gateway-variant field; observed value `15` on MH202 and F454 | empty-`WHERE` gateway identity captures | observed; sentinel interpretation inferred, exact semantics open |
| `DIMENSION 2` `V.R.b` | `EN_FIRMWARE` plus `EN_BUILDS` | resolved item; sentinel/default/build handling | structurally corroborated; exact selection precedence open |
| `DIMENSION 3`/`6` `V.R.b` | no canonical catalogue field found | retain as installed-state evidence | open database correlation |
| `DIMENSION 30.KEYO` | `EN_KEY_OBJECT.key_object` | `STATE = 0`, enabled Module, resolved firmware and `slot` | experimentally corroborated with UI behavior |
| `DIMENSION 30.KEYO` | `EN_VIRGIN_OBJECT.virgin_key_object` | `STATE = 1`, disabled Module, resolved firmware and `slot` | experimentally corroborated with UI behavior |
| `DIMENSION 30.SLOT` | `EN_SLOTS.first_slot` placement | resolved firmware; not `id_slot` | structurally corroborated |
| `DIMENSION 35.INDEX` | `EN_CONF.idx` | Device, firmware, Module, Object, and ownership scope | strongly corroborated |
| diagnostic outer `WHERE` | configured address of `slot` `1` | repeated `WHO 1001` observations | strongly inferred; alternate layouts open |
| `DIMENSION 32.SYS` | `MHCatalogue.db.EN_SYSTEM.sys_modobj` | resolved Object/system context | strongly inferred; needs discriminating non-Lighting capture |
| `WHO 16` `WHERE` `1ES` | environment `E` listening to source `S` | F441M installations; `E` in `1..9`; `10S` excluded as a source address | corroborated on two plants; not published in `WHO 16` |
| `WHO 16` amplifier `WHERE` `EA` | environment `E`, amplifier `A` | two-digit addresses; single-digit form untested | corroborated by `WHO 22` counterparts and F441M documentation |
| `WHO 16` sound events | `WHO 22` counterpart frames | one MH200N; area/point and source/area fields written out | established for that Device; origin and generality open |

## Across database models

| Source | Target | Conditions/evidence | Status |
| --- | --- | --- | --- |
| `OPEN.EN_ADDRESS_RULE.object_device_family` | `MHCatalogue.EN_OBJECT_ITEM_FAMILY.id_family` | all 11 nonzero values resolve; `0` is unqualified; semantics agree | structurally and semantically corroborated |
| `rules.KOBJECTS` | `EN_KEY_OBJECT.key_object` | Objects `95`, `96`, and `184` represented in this revision | strongly corroborated |
| `rules.db3` `$N` reference | `EN_CONF.idx = N` | selected Object context and parsed rule syntax | strongly corroborated |
| ScenarioDevices `ChiOpen` | functional `WHO` parsed from literal `Frame` | all 57 literal templates in Program Files revision agree | established for literal templates |
| ScenarioDevices ProgramData semantic path | Program Files semantic path | compare full hierarchy/non-local fields, never local row IDs | established subset relationship |
| physical firmware property | advanced Object property | symbol, semantic type, filters, conversions, and controlled read-back | established only for individually corroborated mappings; generalization open |
| `OPEN.db` `DIMENSION 4/5.C1..C12` | `MHCatalogue.db` firmware `EN_CONF` definitions / `progressive` | transport fields and catalogue ordering coexist, but no explicit cross-database key or universal positional rule is present | open correlation |

## Sentinel and discriminator rules

| Location | Rule | Status |
| --- | --- | --- |
| `EN_CONF.id_key_object` / `id_firmware` | exactly one owner resolves and the other is `0` | established |
| `EN_ADDRESS_RULE.object_device_family = 0` | family-unqualified address rule | corroborated by complete rule set |
| firmware component `-1` | any or unspecified for that component | strongly corroborated by `-1.-1.-1` and concrete `V.R.-1` rows |
| missing `EN_BUILDS` row | distinct from explicit `firmware_b = -1` | structurally established |
| `DIMENSION 30.STATE` | `0` selects enabled regular Object; `1` selects disabled Virgin Object | experimentally corroborated with MyHOME_Suite UI behavior |
| gateway `DIMENSION 1.N_CONF = 15` | `15` is `0xF`; viewed in four bits, it is `1111`, an all-ones pattern consistent with a reserved-sentinel convention, but no canonical source establishes the sentinel meaning | observed value; sentinel interpretation inferred and unresolved |

Sentinel meaning is local to the field. This table does not authorize interpreting every zero or negative value the same way.

## Open relationships

| Question | Leading evidence | Decisive evidence needed |
| --- | --- | --- |
| `DIMENSION 4`/`5` catalogue correlation | `C1..C12` transport fields and `0..255` ranges are established; `ConfConfigurators` is labelled virtual configuration | controlled Device-family correlation between `C1..C12` and firmware-specific `EN_CONF` symbols/positions |
| generic `DIMENSION 310.VAL_PAR` meaning | Object-specific response without generic index metadata | Object-specific captures and decoder behavior |
| catalogue-wide addressed-form `N_CONF` field-count equivalence | diagrams, captures, and resolved firmware fields agree in tested addressed Devices | systematic conditional-field audit across firmware |
| gateway `N_CONF = 15` meaning | MH202 and F454 gateway captures both return out-of-range `15`; `15 = 0xF` is compatible with a sentinel | an applicable implementation decoder, authoritative definition, or discriminating gateway/firmware observations that establish the encoded meaning |
| firmware selection precedence | exact, wildcard, default, missing, multiple-build patterns | controlled loader/UI observation |
| `WHO 16` directed source selection provenance | `1ES` observed on two plants; specification defines cycling only | a published specification, application note, or stored frame template naming the address |
| `WHO 16` routing under the `#E` environment form and base band | all observations use point-to-point amplifiers and `WHAT 3` | a capture from a base-band plant or one whose controls use environment power commands |
| ScenarioDevices matching IDs | stable local fields and semantic hierarchy | runtime matcher trace or application code |
| ScenarioDevices source precedence | two revisions in different installation locations | file-open/update trace |
| scenario-instance persistence | capability stores lack graph structure | controlled save diff and file trace |

The full research backlog and proposed experiments are in [Open Questions](open-questions.md) and [Hypothesis Testing](hypothesis-testing.md).

## Maintenance rule

When evidence changes a relationship:

1. update the detailed reference page;
2. update this register's status, conditions, and coverage;
3. remove or narrow the corresponding open question;
4. retain rejected alternatives when they are likely to recur;
5. record the source revision and test that caused the change.
