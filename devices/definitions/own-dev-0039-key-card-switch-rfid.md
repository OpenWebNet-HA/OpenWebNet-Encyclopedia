# Key card switch RFID

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0039` | Project identity |
| Technical description | 13.56 MHz RFID key-card presence switch with scenario, CEN and group-control roles | Catalogue + `MM00771-a-EN` |
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
| BTicino Axolute | `H4648` | established identity | catalogue + `MM00771-a-EN` |
| BTicino Living / LivingLight | `LN4648` | established identity | catalogue + `MM00771-a-EN` |
| Legrand Céliane | `067566` | established identity | catalogue + `MM00771-a-EN` |
| Legrand Mosaic | `078480` | established catalogue identity | implementation evidence; not printed in the retained core sheet |
| Legrand Arteor | `572236` | established identity; printed `5 722 36` | catalogue + `MM00771-a-EN` |
| Legrand Arteor | `572736` | publisher-documented family identity; catalogue conflict | `MM00771-a-EN`; current catalogue assigns `572736` to item `1563` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MM00771-a-EN` | Technical sheet | revision a / 2013-12-02 | `H4648`, `LN4648`, `0 675 66`, `5 727 36`, `5 722 36`; RFID and configuration behavior | [Archived original](../../sources/devices/documents/device-doc-key-card-rfid-mm00771-a-en/MM00771-a-EN.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MM00771_a_EN.pdf) |
| `MM00496-b-EN` | Technical sheet | revision b / 2013-12-02 | cross-family comparison for the non-RFID key-card switch | [Archived original](../../sources/devices/documents/device-doc-key-card-mm00496-b-en/MM00496-b-EN.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MM00496_b_EN.pdf) |

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

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `162` | `-1` | `-1` | `-1` | `1` | catalogue default | wildcard applicability |

## Module, Object, and Virgin Object model

| Module / slot | Object | Catalogue relationship | Role |
| --- | --- | --- | --- |
| `1` | `404` | candidate, non-fixed | Scheduled scenario |
| `1` | `521` | candidate, non-fixed | Scheduled scenario PLUS and group control |
| `1` | `522` | catalogue marks fixed | Enable/Disable group control |
| `1` | `523` | candidate, non-fixed | Scenario and group control |

Virgin Object `514`, **Badge command virgin**, is associated with firmware `162`. No slot-condition row selects among these candidate roles in the current catalogue.

## Configuration modes

| Mode | Meaning | Evidence |
| --- | --- | --- |
| `1` | Physical configuration | catalogue + `MM00771-a-EN` |
| `2` | Virtual Configuration | implementation evidence |
| `3` | Advanced Configuration | catalogue + MyHOME Suite workflow described by `MM00771-a-EN` |

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | Device identity | - | implementation identity field |
| `A` | `0..9` | `0` | area / environment |
| `PL` | `0..9` | `0` | point / local address |
| `M1` | `0..8` / `CEN` | `0` | operating mode |
| `M2` | `0` only | `0` | retained catalogue field |
| `DEL1` | `0..9` | `0` | activation delay for badge IN |
| `DEL2` | stored range `0..7`; catalogue description and publisher table include `8`/`9` | `0` | activation delay for badge OUT |

The delay encoding is `0` none, `8` 15 s, `9` 30 s, `1` 60 s, `2` 2 min, `3` 3 min, `4` 4 min, `5` 5 min, `6` 10 min and `7` 15 min. The firmware `DEL2` range conflicts with its own textual description as well as the publisher sheet.

## Object configuration surfaces

### Object `404` - Scheduled scenario

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | area |
| `PL` | `0..15` | `0` | light point |
| `BUTTON_1` | `0..31` | `1` | insertion role |
| `BUTTON_2` | `0..31` | `2` | removal role |
| `IN_AUX_CHANNEL` | `0..15` | `0` | input AUX channel |
| `START_DELAY` | `0..255` s | `10` | device restart delay |

### Object `521` - Scheduled scenario PLUS and group control

| Surface | Fields | Meaning |
| --- | --- | --- |
| Scenario | `PPT_SCE_1`, `PPT_SCE_2` | insertion/removal PLUS scenarios `1..255` |
| Group control | `GROUP_BUTTON_1_ENABLE`, `GROUP_BUTTON_2_DISABLE` | group enable/disable addresses `0..255` |
| Timing | `ACTIVATION_DELAY_FOR_BUTTON_1`, `ACTIVATION_DELAY_FOR_BUTTON_2`, `START_DELAY` | per-action enumerated delays and restart delay |

### Object `522` - Enable/Disable group control

| Surface | Fields | Meaning |
| --- | --- | --- |
| Group control | `GROUP_BUTTON_1_ENABLE`, `GROUP_BUTTON_2_DISABLE`, `GROUP_BUTTON_1_ON`, `GROUP_BUTTON_2_OFF` | insertion/removal group enable/disable and ON/OFF addresses |
| Timing | `ACTIVATION_DELAY_FOR_BUTTON_1`, `ACTIVATION_DELAY_FOR_BUTTON_2`, `START_DELAY` | per-action enumerated delays and restart delay |

### Object `523` - Scenario and group control

| Surface | Fields | Meaning |
| --- | --- | --- |
| Scenario addressing | `APL` | encoded scenario-module A/PL address |
| Group control | `GROUP_BUTTON_1_ENABLE`, `GROUP_BUTTON_2_DISABLE`, `GROUP_BUTTON_2_OFF` | group actions |
| Scenario selection | `SCE_BUT_1`, `SCE_BUT_2` | scenario numbers `1..16` |
| Timing | `ACTIVATION_DELAY_FOR_BUTTON_1`, `ACTIVATION_DELAY_FOR_BUTTON_2`, `START_DELAY` | per-action delays and restart delay |

## Conditions, filters, and conversions

The current catalogue contains no slot-condition row selecting the badge-command Object.

| Filter ID | Object | Field | Meaning |
| --- | --- | --- | --- |
| `1698` | `404` | `IN_AUX_CHANNEL` | Input AUX channel |

| Topology reference | Value | Meaning |
| --- | --- | --- |
| Virgin Object | `514` | Badge command virgin shared by the candidate Object family |
| Slot | `1` | all four Object/Firmware relations begin at the first Module |

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

Physical programming uses the scenario/CEN mode and insertion/removal delay model documented by `MM00771-a-EN`. Software must preserve the `DEL2` range discrepancy and must not merge RFID identity semantics with the non-RFID key-card Device solely because their Object topology is similar.

## Source reconciliation

The catalogue and `MM00771-a-EN` agree on the RFID role, H4648/LN4648/Céliane/Arteor family, one-Module badge-command topology and scenario/CEN programming model. The retained sheet does not directly print Mosaic `078480`, so that identity remains implementation-correlated.

The major commercial conflict is `572736`: `MM00771-a-EN` assigns printed `5 727 36` to this RFID family, while the current canonical catalogue associates code `572736` with item `1563`, the non-RFID key-card Device. The dossier records both source claims without choosing one silently. Firmware `162` also stores `DEL2=0..7` while its own description and the publisher delay table include `8` and `9`.

## Evidence limits and open work

- Recover a direct publisher document for Mosaic `078480`.
- Hardware-corroborate RFID identity, firmware and active Object selection.
- Resolve the `572736` cross-item catalogue discrepancy with an independent catalogue revision.
- Test `DEL2` values `8` and `9` against firmware/runtime behavior.

## Sources

- [Device Source Index](../../sources/devices/index.md)
- [Device Database Inventory](../inventory/)
- [`MM00771-a-EN` archived original](../../sources/devices/documents/device-doc-key-card-rfid-mm00771-a-en/MM00771-a-EN.pdf)
- [`MM00496-b-EN` archived original](../../sources/devices/documents/device-doc-key-card-mm00496-b-en/MM00496-b-EN.pdf)
