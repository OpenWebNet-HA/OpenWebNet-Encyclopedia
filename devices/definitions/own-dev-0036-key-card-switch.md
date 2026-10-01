# Key card switch

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0036` | Project identity |
| Technical description | SCS key-card presence switch with scenario, CEN and group-control roles | Catalogue + official documentation |
| Commercial identities | `H4649`, `LN4649`, `572735`, `572736`, `67565`, `572235` | Implementation evidence; publisher conflict retained below |
| Catalogue item | `1563` | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `29` | Implementation evidence |
| Firmware definition | `161` / `-1.-1.-1` | Implementation evidence |
| Declared Modules | `1` | Implementation evidence |
| Categories | Control, Scenario, Group control, Hospitality | Capability model |

The Device detects card insertion/removal and maps that state to configured scenario or group-control behavior. The current catalogue and the publisher key-card sheets disagree over one Arteor identity; the disagreement is preserved rather than normalized.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4649` | established identity | catalogue + `MM00496-b-EN` |
| BTicino - LivingLight | `LN4649` | established identity | catalogue + `MM00496-b-EN` |
| Legrand - Arteor | `572735` | established identity; printed `5 727 35` | catalogue + `MM00496-b-EN` |
| Legrand - Arteor | `572235` | established identity; printed `5 722 35` | catalogue + `MM00496-b-EN` |
| Legrand - Céliane | `67565` | established identity; printed `0 675 65` | catalogue + `MM00496-b-EN` |
| Legrand - Arteor | `572736` | catalogue-associated identity with source conflict | catalogue; `MM00771-a-EN` assigns printed `5 727 36` to the RFID family |

No commercial identity is treated as canonical. The `572736` conflict is material because the official RFID sheet associates the same printed reference with the RFID product family documented by the [RFID key-card switch](own-dev-0039-key-card-switch-rfid.md).
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MM00496-b-EN` | Technical sheet | revision b / 2013-12-02 | `H4649`, `LN4649`, `0 675 65`, `5 727 35`, `5 722 35` | [Archived original](../../sources/devices/documents/device-doc-key-card-mm00496-b-en/MM00496-b-EN.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MM00496_b_EN.pdf) |
| `MM00771-a-EN` | Technical sheet | revision a / 2013-12-02 | cross-family evidence for the disputed `5 727 36` identity | [Archived original](../../sources/devices/documents/device-doc-key-card-rfid-mm00771-a-en/MM00771-a-EN.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MM00771_a_EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 flush-mounted modules | `MM00496-b-EN` |
| SCS supply | `18..27 Vdc` | `MM00496-b-EN` |
| Maximum current draw | `6 mA` | `MM00496-b-EN` |
| Standby current | `5 mA` | `MM00496-b-EN` |
| Operating temperature | `-10..45 °C` | `MM00496-b-EN` |
| Accepted card width | `45..54 mm` ISO-format card | `MM00496-b-EN` |
| Local interface | backlit card slot plus Learn IN / Learn OUT programming keys | `MM00496-b-EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1563` | Implementation evidence |
| Main system | Lighting / Automation | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `29` | Implementation evidence |
| Catalogue buses | `1`, `2` | Implementation evidence |
| Commercial records | `6` | Implementation evidence |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `161` | `-1` | `-1` | `-1` | `1` | catalogue default | wildcard applicability |

The `-1` triplet is catalogue applicability metadata, not an observed installed firmware version.

## Module, Object, and Virgin Object model

| Module / slot | Object | Catalogue relationship | Role |
| --- | --- | --- | --- |
| `1` | `404` | candidate, non-fixed | Scheduled scenario |
| `1` | `521` | candidate, non-fixed | Scheduled scenario PLUS and group control |
| `1` | `522` | catalogue marks fixed | Enable/Disable group control |
| `1` | `523` | candidate, non-fixed | Scenario and group control |

Virgin Object `514`, **Badge command virgin**, is associated with firmware `161` and with the badge-command Object family. The fixed/candidate flags and Virgin Object membership are preserved as catalogue topology; without runtime corroboration they are not sufficient to infer one universal active role for every configuration.

## Configuration modes

| Mode | Meaning | Evidence |
| --- | --- | --- |
| `1` | Physical configuration | catalogue + `MM00496-b-EN` |
| `2` | Virtual Configuration | implementation evidence |
| `3` | Advanced Configuration | catalogue + MyHOME Suite workflow described by `MM00496-b-EN` |

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | Device identity | - | implementation identity field |
| `A` | `0..9` | `0` | area / environment |
| `PL` | `0..9` | `0` | point / local address |
| `M1` | `0..8` / `CEN` | `0` | operating mode; publisher physical scenario modes use `1..8` or `CEN` |
| `DEL1` | catalogue `0..7`; publisher physical table `0..9` | `0` | insertion-action delay |
| `M2` | `0` only | `0` | retained catalogue field; no independent physical selector is documented |
| `DEL2` | catalogue `0..7`; publisher physical table `0..9` | `0` | removal-action delay |

The official delay table uses `0` none, `8` 15 s, `9` 30 s, `1` 60 s, `2` 2 min, `3` 3 min, `4` 4 min, `5` 5 min, `6` 10 min and `7` 15 min. The narrower catalogue range on firmware `161` is therefore a source discrepancy, not a reason to discard the published `8`/`9` values.

## Object configuration surfaces

### Object `404` - Scheduled scenario

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | area |
| `PL` | `0..15` | `0` | light point |
| `BUTTON_1` | `0..31` | `1` | insertion / upper-button role |
| `BUTTON_2` | `0..31` | `2` | removal / lower-button role |
| `IN_AUX_CHANNEL` | `0..15` | `0` | input AUX channel |
| `START_DELAY` | `0..255` s | `10` | device restart delay |

### Object `521` - Scheduled scenario PLUS and group control

| Surface | Fields | Meaning |
| --- | --- | --- |
| Scenario | `PPT_SCE_1`, `PPT_SCE_2` | insertion/removal PLUS scenario numbers, each `1..255` |
| Group control | `GROUP_BUTTON_1_ENABLE`, `GROUP_BUTTON_2_DISABLE` | insertion/removal group addresses, `0..255` with `0` meaning no group |
| Timing | `ACTIVATION_DELAY_FOR_BUTTON_1`, `ACTIVATION_DELAY_FOR_BUTTON_2`, `START_DELAY` | per-action enumerated delay tables plus restart delay |

### Object `522` - Enable/Disable group control

| Surface | Fields | Meaning |
| --- | --- | --- |
| Group control | `GROUP_BUTTON_1_ENABLE`, `GROUP_BUTTON_2_DISABLE`, `GROUP_BUTTON_1_ON`, `GROUP_BUTTON_2_OFF` | group enable/disable and ON/OFF addresses, `0..255` |
| Timing | `ACTIVATION_DELAY_FOR_BUTTON_1`, `ACTIVATION_DELAY_FOR_BUTTON_2`, `START_DELAY` | per-action enumerated delay tables plus restart delay |

### Object `523` - Scenario and group control

| Surface | Fields | Meaning |
| --- | --- | --- |
| Scenario addressing | `APL` | encoded scenario-module A/PL address |
| Group control | `GROUP_BUTTON_1_ENABLE`, `GROUP_BUTTON_2_DISABLE`, `GROUP_BUTTON_2_OFF` | group actions associated with insertion/removal |
| Scenario selection | `SCE_BUT_1`, `SCE_BUT_2` | scenario numbers `1..16` |
| Timing | `ACTIVATION_DELAY_FOR_BUTTON_1`, `ACTIVATION_DELAY_FOR_BUTTON_2`, `START_DELAY` | per-action enumerated delay tables plus restart delay |

## Conditions, filters, and conversions

The current catalogue has no slot-condition row selecting among the badge-command candidates. The relationship must therefore be resolved using the catalogue/Device programming model rather than by inventing a missing predicate.

| Filter ID | Object | Field | Meaning |
| --- | --- | --- | --- |
| `1697` | `404` | `IN_AUX_CHANNEL` | Input AUX channel |

| Topology reference | Value | Meaning |
| --- | --- | --- |
| Virgin Object | `514` | Badge command virgin shared by the candidate Object family |
| Slot | `1` | all four Object/Firmware relations begin at the first Module |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 29` and installed configurator count | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware instead of treating wildcard applicability as runtime firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | determine the active badge-command Object for the single Module | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | resolve the configured address/context used by the selected Object | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration and corroborate the firmware fields above | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The Device can participate in scenario and group-control functions. Physical scenario mode maps insertion/removal to scenario actions with optional delays; centralised mode uses `M1=CEN`. PLUS and group-control behavior is represented by Objects `521`, `522` and `523` rather than by treating every card event as one generic lighting command.

## Observed behavior and corroboration

No publishable hardware fingerprint for this exact technical item is currently retained. The physical behavior described here is publisher-documented; runtime Object selection and diagnostics remain to be corroborated on hardware.

## Programming

Physical programming uses `A`, `PL`, `M1` and delay configurators together with Learn IN / Learn OUT procedures. MyHOME Suite can configure the Device through supported software workflows. A programmer must resolve the active Object before exposing Object-specific fields and must preserve the catalogue/publisher delay-domain discrepancy.

## Source reconciliation

`MM00496-b-EN` directly corroborates the H4649/LN4649/Céliane/Arteor key-card family, electrical data, physical configurators, scenario/CEN behavior and Learn IN/OUT programming. The catalogue adds the reusable four-Object badge-command topology.

Two source conflicts remain explicit. First, firmware `161` stores `DEL1`/`DEL2` as `0..7` while the publisher physical table documents `0..9`. Second, the catalogue associates `572736` with item `1563`, while `MM00771-a-EN` identifies printed `5 727 36` as an RFID key-card switch. Neither conflict is silently normalized.

## Evidence limits and open work

- Hardware-corroborate the active Object projection for representative scenario, group and CEN configurations.
- Resolve the `572736` catalogue association against a later/independent commercial catalogue if available.
- Determine whether firmware/runtime accepts published delay values `8` and `9` despite the narrower firmware `161` catalogue range.

## Sources

- [Device Source Index](../../sources/devices/index.md)
- [Device Database Inventory](../inventory/)
- [`MM00496-b-EN` archived original](../../sources/devices/documents/device-doc-key-card-mm00496-b-en/MM00496-b-EN.pdf)
- [`MM00771-a-EN` archived original](../../sources/devices/documents/device-doc-key-card-rfid-mm00771-a-en/MM00771-a-EN.pdf)
