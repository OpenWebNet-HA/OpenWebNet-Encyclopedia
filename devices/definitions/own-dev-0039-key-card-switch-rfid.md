# Key card switch RFID

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0039` | Project identity |
| Technical description | 13.56 MHz RFID key-card presence switch with scenario, `CEN` and group-control roles | Catalogue + `MM00771-a-EN` |
| Commercial identities | `H4648`, `LN4648`, `067566`, `078480`, `572236` | Catalogue + official documentation |
| Catalogue item | `1847` | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `30` | Implementation evidence |
| Firmware definition | `162` / `-1.-1.-1` | Implementation evidence |
| Declared Modules | `1` | Implementation evidence |
| Categories | RFID, Control, Scenario, Group control, Hospitality | Capability model |

The Device detects authorized RFID card insertion/removal and maps that state into scenario or group-control behavior. The publisher family list and the implementation catalogue disagree about Arteor reference `572736`, so both source scopes remain visible.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4648` | established identity | catalogue + `MM00771-a-EN` |
| BTicino - LivingLight | `LN4648` | established identity | catalogue + `MM00771-a-EN` |
| Legrand - Céliane | `067566` | established identity | catalogue + `MM00771-a-EN` |
| Legrand - Mosaic | `078480` | established catalogue identity | implementation evidence; not printed in the retained core sheet |
| Legrand - Arteor | `572236` | established identity; printed `5 722 36` | catalogue + `MM00771-a-EN` |
| Legrand - Arteor | `572736` | publisher-documented family identity; catalogue conflict | `MM00771-a-EN`; current catalogue assigns `572736` to item `1563` |
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MM00771-a-EN` | Technical sheet | revision a / 2013-12-02 | `H4648`, `LN4648`, `0 675 66`, `5 727 36`, `5 722 36`; RFID and configuration behavior | [Archived original](https://archive.openwebnet-ha.org/sha256/d2/71/d271cc73c58bd7350c84c8f295751041a5ec789c415133103dafd8d4583e5449.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MM00771_a_EN.pdf) |
| `MM00496-b-EN` | Technical sheet | revision b / 2013-12-02 | cross-family comparison for the non-RFID key-card switch | [Archived original](https://archive.openwebnet-ha.org/sha256/fb/b6/fbb66b8f4b3aebc54b5159450544d393eabf559eaffe753594348dd24c34715f.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MM00496_b_EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 flush-mounted modules | `MM00771-a-EN` |
| RFID carrier frequency | `13.56 MHz` | `MM00771-a-EN` |
| SCS supply | `18..27 Vdc` | `MM00771-a-EN` |
| Maximum current draw | `6 mA` | `MM00771-a-EN` |
| Standby current | `5 mA` | `MM00771-a-EN` |
| Operating temperature | `5..40 °C` | `MM00771-a-EN` |
| Accepted card width | `45..54 mm` ISO-format card | `MM00771-a-EN` |
| Local interface | card slot plus Learn IN / Learn OUT programming controls | `MM00771-a-EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1847` | Implementation evidence |
| Main system | Lighting / Automation | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `30` | Implementation evidence |
| Catalogue buses | `1`, `2` | Implementation evidence |
| Commercial records | `5` | Implementation evidence |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `162` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `162` | `1` | `404` Scheduled scenario | Candidate alternative | `1353` | `404` | `711` |
| `162` | `1` | `466` Scheduled scenario PLUS and group control | Candidate alternative | `2305` | `521` | `983` |
| `162` | `1` | `467` Enable/Disable group control | Fixed/designated metadata | `2304` | `522` | `982` |
| `162` | `1` | `468` Scenario and group control | Candidate alternative | `2306` | `523` | `984` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `162` | `514` Badge command virgin | `1` | `404`, `466`, `467`, `468` | `514` | `42` |

Virgin Object `514`, **Badge command virgin**, is associated with firmware `162`. No slot-condition row selects among these candidate roles in the current catalogue.

## Configuration modes

| Mode | Meaning | Evidence |
| --- | --- | --- |
| `1` | Physical configuration | catalogue + `MM00771-a-EN` |
| `2` | Virtual Configuration | implementation evidence |
| `3` | Advanced Configuration | catalogue + MyHOME Suite workflow described by `MM00771-a-EN` |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `162` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `162` | `A` | `0..9` | `0` | A |
| `162` | `PL` | `0..9` | `0` | PL |
| `162` | `M1` | `0..8`; `14` = `CEN` | `0` | Modality; Mode physical configurator (0-8, `CEN`) |
| `162` | `M2` | `0` | `0` | M2 |
| `162` | `DEL1` | `0..9` | `0` | Activation delay for badge IN; (None: 0) (15 s: 8) (30 s: 9) (60 s: 1) (2 min: 2) (3 min: 3) (4 min: 4) (5 min: 5) (10 min: 6) (15 min: 7) |
| `162` | `DEL2` | `0..7` | `0` | Activation delay for badge OUT; (None: 0) (15 s: 8) (30 s: 9) (60 s: 1) (2 min: 2) (3 min: 3) (4 min: 4) (5 min: 5) (10 min: 6) (15 min: 7) If `M1=CEN`, `DEL2=0` |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `A` | `0..9` | area / environment |
| `PL` | `0..9` | point / local address |
| `M1` | `0..8` / `CEN` | operating mode |
| `M2` | `0` only | retained catalogue field |
| `DEL1` | `0..9` | activation delay for badge IN |
| `DEL2` | stored range `0..7`; catalogue description and publisher table include `8`/`9` | activation delay for badge OUT |


The delay encoding is `0` none, `8` 15 s, `9` 30 s, `1` 60 s, `2` 2 min, `3` 3 min, `4` 4 min, `5` 5 min, `6` 10 min and `7` 15 min. The firmware `DEL2` range conflicts with its own textual description as well as the publisher sheet.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `404` - Scheduled scenario

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `BUTTON_1` | `0..31` | `1` | Upper button |
| `BUTTON_2` | `0..31` | `2` | Lower button |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |
| `START_DELAY` | `0..255` | `10` | Time of restart device (s) |


### Object `466` - Scheduled scenario PLUS and group control

Catalogue Object key `521` maps to external Object `466`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_SCE_1` | `1..255` | `1` | Scenario on insertion |
| `PPT_SCE_2` | `1..255` | `2` | Scenario on removal |
| `GROUP_BUTTON_1_ENABLE` | `0..255` | `1` | Group of actuators enabled on insertion; 0= no group |
| `GROUP_BUTTON_2_DISABLE` | `0..255` | `1` | Group of actuators disabled on removal; 0= no group |
| `ACTIVATION_DELAY_FOR_BUTTON_1` | `0..71` | `0` | Activation delay for scenario after insertion; only if scenario <> scenario 2 |
| `ACTIVATION_DELAY_FOR_BUTTON_2` | `0..71` | `30` | Activation delay for scenario after removal; only if scenario 1 <> scenario 2 |
| `START_DELAY` | `0..255` | `0` | Time of restart device (s) |


### Object `467` - Enable/Disable group control

Catalogue Object key `522` maps to external Object `467`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `GROUP_BUTTON_1_ENABLE` | `0..255` | `1` | Group address enabled on insertion |
| `GROUP_BUTTON_2_DISABLE` | `0..255` | `1` | Group address disabled on removal |
| `GROUP_BUTTON_1_ON` | `0..255` | `2` | Group address turned on after insertion |
| `GROUP_BUTTON_2_OFF` | `0..255` | `1` | Group address turned off after removal |
| `ACTIVATION_DELAY_FOR_BUTTON_1` | `0..71` | `0` | Activation delay for scenario after insertion |
| `ACTIVATION_DELAY_FOR_BUTTON_2` | `0..71` | `30` | Activation delay for scenario after removal |
| `START_DELAY` | `0..255` | `10` | Time of restart device (s); sec |


### Object `468` - Scenario and group control

Catalogue Object key `523` maps to external Object `468`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `APL` | `0..175`; encoded by `APL=16*A+PL`, with `A=0..10` and `PL=0..15` | `0` | Scenario module address |
| `GROUP_BUTTON_1_ENABLE` | `0..255` | `1` | Group address enabled on insertion |
| `GROUP_BUTTON_2_DISABLE` | `0..255` | `1` | Group address disabled on removal |
| `GROUP_BUTTON_2_OFF` | `0..255` | `1` | Group address turned off after removal |
| `SCE_BUT_1` | `1..16` | `1` | Scenario on insertion |
| `SCE_BUT_2` | `1..16` | `2` | Scenario on removal |
| `ACTIVATION_DELAY_FOR_BUTTON_1` | `0..71` | `0` | Activation delay for scenario after insertion |
| `ACTIVATION_DELAY_FOR_BUTTON_2` | `0..71` | `30` | Activation delay for scenario after removal |
| `START_DELAY` | `0..255` | `0` | Time of restart device (s) |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `162` | `404` | `1698` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 30` and distinguish the RFID technical item | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware rather than treating wildcard applicability as an installed value | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | resolve the active badge-command Object | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect the selected Object's configured addressing | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | corroborate physical/software configuration and delay values | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The RFID switch participates in access-triggered scenario and group-control behavior. RFID recognition is a product-level input mechanism; the OpenWebNet-facing role is determined by the resolved scenario/group Object and configuration.

## Observed behavior and corroboration

No sanitized hardware fingerprint is currently retained. RFID frequency, physical configuration and Learn IN/OUT behavior are publisher-documented; runtime Object selection remains to be observed.

## Programming

Physical programming uses the scenario/`CEN` mode and insertion/removal delay model documented by `MM00771-a-EN`. Software must preserve the `DEL2` range discrepancy and must not merge RFID identity semantics with the non-RFID key-card Device solely because their Object topology is similar.

## Source reconciliation

The catalogue and `MM00771-a-EN` agree on the RFID role, H4648/LN4648/Céliane/Arteor family, one-Module badge-command topology and scenario/`CEN` programming model. The retained sheet does not directly print Mosaic `078480`, so that identity remains implementation-correlated.

The major commercial conflict is `572736`: `MM00771-a-EN` assigns printed `5 727 36` to this RFID family, while the current canonical catalogue associates code `572736` with item `1563`, the non-RFID key-card Device. The dossier records both source claims without choosing one silently. Firmware `162` also stores `DEL2=0..7` while its own description and the publisher delay table include `8` and `9`.

## Evidence limits and open work

- Recover a direct publisher document for Mosaic `078480`.
- Hardware-corroborate RFID identity, firmware and active Object selection.
- Resolve the `572736` cross-item catalogue discrepancy with an independent catalogue revision.
- Test `DEL2` values `8` and `9` against firmware/runtime behavior.

## Sources

- [Device Source Index](../../sources/devices/index.md)
- [Device Database Inventory](../inventory/)
- [`MM00771-a-EN` archived original](https://archive.openwebnet-ha.org/sha256/d2/71/d271cc73c58bd7350c84c8f295751041a5ec789c415133103dafd8d4583e5449.pdf)
- [`MM00496-b-EN` archived original](https://archive.openwebnet-ha.org/sha256/fb/b6/fbb66b8f4b3aebc54b5159450544d393eabf559eaffe753594348dd24c34715f.pdf)
