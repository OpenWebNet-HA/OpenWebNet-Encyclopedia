# Key card switch

## Summary

This key-card switch turns card insertion and removal into configured SCS scenario or group-control actions. Its backlit slot accepts an ISO-format card, and separate insertion/removal programming allows arrival and departure to trigger different actions.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0036` | Project identity |
| Technical description | SCS key-card presence switch with scenario, `CEN` and group-control roles | Catalogue + official documentation |
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

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `H4649` | `8005543441718` | [Archived original](https://archive.openwebnet-ha.org/sha256/23/7e/237ead515d5333a822d12f9b487add39a2f1ec69bbd4cbadfcb2e5a718f90733.pdf), `H4649-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `LN4649` | `8005543441794` | [Archived original](https://archive.openwebnet-ha.org/sha256/aa/d5/aad500b54e38cdeb86918860f1ea2efaef15efa43087ac49668beb723d610276.pdf), `LN4649-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `67565` | `3245060675653` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/c6/69/c66947d703cfc2f09be74261ea7c3758cb2c5ccc36dc7abd28d76083cd3fc686.pdf), `67565-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field; manufacturer reference `067565` (catalogue `67565`) |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MM00496-b-EN` | Technical sheet | revision b / 2013-12-02 | `H4649`, `LN4649`, `0 675 65`, `5 727 35`, `5 722 35` | [Archived original](https://archive.openwebnet-ha.org/sha256/fb/b6/fbb66b8f4b3aebc54b5159450544d393eabf559eaffe753594348dd24c34715f.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MM00496_b_EN.pdf) |
| `MM00771-a-EN` | Technical sheet | revision a / 2013-12-02 | cross-family evidence for the disputed `5 727 36` identity | [Archived original](https://archive.openwebnet-ha.org/sha256/d2/71/d271cc73c58bd7350c84c8f295751041a5ec789c415133103dafd8d4583e5449.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MM00771_a_EN.pdf) |
| `H4649-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `H4649` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/23/7e/237ead515d5333a822d12f9b487add39a2f1ec69bbd4cbadfcb2e5a718f90733.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4649) |
| `LN4649-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `LN4649` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/aa/d5/aad500b54e38cdeb86918860f1ea2efaef15efa43087ac49668beb723d610276.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4649) |
| `67565-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `67565` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field; manufacturer reference `067565` (catalogue `67565`). Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/c6/69/c66947d703cfc2f09be74261ea7c3758cb2c5ccc36dc7abd28d76083cd3fc686.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue/lecteur-de-badge-celiane-bus-pour-badge-ou-carte-format-45mm-ou-54mm) |

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

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `161` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

The `-1` triplet is catalogue applicability metadata, not an observed installed firmware version.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `161` | `1` | `404` Scheduled scenario | Candidate alternative | `1349` | `404` | `707` |
| `161` | `1` | `466` Scheduled scenario PLUS and group control | Candidate alternative | `1350` | `521` | `708` |
| `161` | `1` | `467` Enable/Disable group control | Fixed/designated metadata | `2303` | `522` | `981` |
| `161` | `1` | `468` Scenario and group control | Candidate alternative | `1352` | `523` | `710` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `161` | `514` Badge command virgin | `1` | `404`, `466`, `467`, `468` | `514` | `41` |

Virgin Object `514`, **Badge command virgin**, is associated with firmware `161` and with the badge-command Object family. The fixed/candidate flags and Virgin Object membership are preserved as catalogue topology; without runtime corroboration they are not sufficient to infer one universal active role for every configuration.

## Configuration modes

| Mode | Meaning | Evidence |
| --- | --- | --- |
| `1` | Physical configuration | catalogue + `MM00496-b-EN` |
| `2` | Virtual Configuration | implementation evidence |
| `3` | Advanced Configuration | catalogue + MyHOME Suite workflow described by `MM00496-b-EN` |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `161` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `161` | `A` | `0..9` | `0` | Area |
| `161` | `PL` | `0..9` | `0` | Light point |
| `161` | `M1` | `0..8`; `14` = `CEN` | `0` | M1; Mode physical configurator (0-8, `CEN`) |
| `161` | `DEL1` | `0..7` | `0` | DEL 1 |
| `161` | `M2` | `0` | `0` | M2 |
| `161` | `DEL2` | `0..7` | `0` | DEL 2 |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `A` | `0..9` | area / environment |
| `PL` | `0..9` | point / local address |
| `M1` | `0..8` / `CEN` | operating mode; publisher physical scenario modes use `1..8` or `CEN` |
| `DEL1` | catalogue `0..7`; publisher physical table `0..9` | insertion-action delay |
| `M2` | `0` only | retained catalogue field; no independent physical selector is documented |
| `DEL2` | catalogue `0..7`; publisher physical table `0..9` | removal-action delay |


The official delay table uses `0` none, `8` 15 s, `9` 30 s, `1` 60 s, `2` 2 min, `3` 3 min, `4` 4 min, `5` 5 min, `6` 10 min and `7` 15 min. The narrower catalogue range on firmware `161` is therefore a source discrepancy, not a reason to discard the published `8`/`9` values.

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
| `161` | `404` | `1697` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

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

`MM00496-b-EN` directly corroborates the H4649/LN4649/Céliane/Arteor key-card family, electrical data, physical configurators, scenario/`CEN` behavior and Learn IN/OUT programming. The catalogue adds the reusable four-Object badge-command topology.

Two source conflicts remain explicit. First, firmware `161` stores `DEL1`/`DEL2` as `0..7` while the publisher physical table documents `0..9`. Second, the catalogue associates `572736` with item `1563`, while `MM00771-a-EN` identifies printed `5 727 36` as an RFID key-card switch. Neither conflict is silently normalized.

## Evidence limits and open work

- Hardware-corroborate the active Object projection for representative scenario, group and `CEN` configurations.
- Resolve the `572736` catalogue association against a later/independent commercial catalogue if available.
- Determine whether firmware/runtime accepts published delay values `8` and `9` despite the narrower firmware `161` catalogue range.

## Sources

- [Device Source Index](../../sources/devices/index.md)
- [Device Database Inventory](../inventory/)
- [`MM00496-b-EN` archived original](https://archive.openwebnet-ha.org/sha256/fb/b6/fbb66b8f4b3aebc54b5159450544d393eabf559eaffe753594348dd24c34715f.pdf)
- [`MM00771-a-EN` archived original](https://archive.openwebnet-ha.org/sha256/d2/71/d271cc73c58bd7350c84c8f295751041a5ec789c415133103dafd8d4583e5449.pdf)

- `H4649-ean-product-sheet.pdf`, printed/PDF p. 1: exact `H4649` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/23/7e/237ead515d5333a822d12f9b487add39a2f1ec69bbd4cbadfcb2e5a718f90733.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4649); SHA-256 `237ead515d5333a822d12f9b487add39a2f1ec69bbd4cbadfcb2e5a718f90733`.
- `LN4649-ean-product-sheet.pdf`, printed/PDF p. 1: exact `LN4649` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/aa/d5/aad500b54e38cdeb86918860f1ea2efaef15efa43087ac49668beb723d610276.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4649); SHA-256 `aad500b54e38cdeb86918860f1ea2efaef15efa43087ac49668beb723d610276`.

- `67565-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field; manufacturer reference `067565` (catalogue `67565`): exact `67565` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/c6/69/c66947d703cfc2f09be74261ea7c3758cb2c5ccc36dc7abd28d76083cd3fc686.pdf); [publisher source](https://www.legrand.fr/pro/catalogue/lecteur-de-badge-celiane-bus-pour-badge-ou-carte-format-45mm-ou-54mm); SHA-256 `c66947d703cfc2f09be74261ea7c3758cb2c5ccc36dc7abd28d76083cd3fc686`.
