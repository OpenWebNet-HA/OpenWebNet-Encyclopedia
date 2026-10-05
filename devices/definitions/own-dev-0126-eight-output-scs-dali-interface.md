# Eight-output SCS and DALI interface

## Summary

This DIN interface brings SCS lighting control to eight independent DALI outputs. Each output supports up to 16 documented ballasts, allowing several DALI lighting groups to be controlled through one bus-connected device.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0126` | Project identity |
| Technical description | Eight-output SCS and DALI interface | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `002633`, `BMDI1100` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1171` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `175` | Main association; independent of project ID |
| Firmware definition | `211` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `8` | Firmware metadata |
| Categories | Gateways and interfaces, Actuators | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `002633` | Established catalogue identity | Manufacturer database commercial record `1171` explicitly links this SKU to item `1171` |
| BTicino | `BMDI1100` | Established catalogue identity | Manufacturer database commercial record `2516` explicitly links this SKU to item `1171` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `BT00582_b_IT.pdf` | Manufacturer legacy documentation | `BT00582_b_IT; 12/11/2013` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-3; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/a9/45/a945b86c57da65c4607849ccf577ac700cf107a065041c55fe08e59d84f70223.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/BT00582_b_IT.pdf) |
| `BMDI1100-italian-product-sheet.pdf` | Exact Italian product export | `Retrieved 04/10/2026; old compliance-template date does not establish product publication date` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-1; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/bf/47/bf47b525184a52f7c34e52604d6e5fe36e549970617ebd226a3b7629b5cab352.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMDI1100) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `1171` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mains | `100..240 Vac; 50/60 Hz` | `BT00582-b-IT` printed/PDF pp. 1-3 |
| Outputs | `8 independent DALI outputs; <=16 ballasts/output` | `BT00582-b-IT` printed/PDF pp. 1-3 |
| Mounting | `10 DIN modules; enclosed IP20; IK04` | `BT00582-b-IT` printed/PDF pp. 1-3 |
| Dimensions | `178 x 83 x 66 mm; illustrated subdimensions 50 mm and 45 mm` | `BT00582-b-IT` printed/PDF pp. 1-3 |
| Operating / storage temperature | `-5..45 °C / -20..70 °C` | `BT00582-b-IT` printed/PDF pp. 1-3 |
| Weight | `307 g` | `BT00582-b-IT` printed/PDF pp. 1-3 |
| Standby consumption | `0.8 W` | `BT00582-b-IT` printed/PDF pp. 1-3 |
| SCS wiring | `RJ45 or SCS cable adapted to RJ45; <=500 m supply-to-farthest-device` | `BT00582-b-IT` printed/PDF pp. 1-3 |
| Supply terminals | `screw terminals; 2 x 2.5 mm²` | `BT00582-b-IT` printed/PDF pp. 1-3 |
| DALI terminals | `<=1.5 mm²` | `BT00582-b-IT` printed/PDF pp. 1-3 |
| DALI cable runs | `<=100 m at 0.5 mm²; <=150 m at 0.75 mm²; <=300 m at 1.5 mm²` | `BT00582-b-IT` printed/PDF pp. 1-3 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1171` | Canonical catalogue |
| Technical item description | 8 channels DALI/SCS interface, 10DIN | Canonical catalogue |
| Item family | 0; key `4` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `175` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `211` | `-1` | `-1` | `-1` | `8` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `211` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `887` | `8` | `560` |
| `211` | `2` | `8` Dimmer actuator | Fixed/designated metadata | `888` | `8` | `560` |
| `211` | `3` | `8` Dimmer actuator | Fixed/designated metadata | `889` | `8` | `560` |
| `211` | `4` | `8` Dimmer actuator | Fixed/designated metadata | `890` | `8` | `560` |
| `211` | `5` | `8` Dimmer actuator | Fixed/designated metadata | `891` | `8` | `560` |
| `211` | `6` | `8` Dimmer actuator | Fixed/designated metadata | `892` | `8` | `560` |
| `211` | `7` | `8` Dimmer actuator | Fixed/designated metadata | `893` | `8` | `560` |
| `211` | `8` | `8` Dimmer actuator | Fixed/designated metadata | `894` | `8` | `560` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `211` | Virtual Configuration | `1` | Association key `1` |
| `211` | Advanced Configuration | `2` | Association key `2` |
| `211` | Physical configuration | `0` | Association key `3` |


No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `211` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `211` | `A` | `0..9` | `0` | A; Enviroment |
| `211` | `G` | `0..9` | `0` | G (0-9) |
| `211` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (0-4, Pul, Sla) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `8` - Dimmer actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality; mode (M,S + PULL) |
| `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled | `0` | State saving on reset |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `MIN_LEVEL` | `1..100` | `1` | Minimum level |
| `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge | `0` | Type of load; Default value depends on device. |
| `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard | `0` | Voltage standard |
| `MIN_LEVEL_ADV` | `1..100` | `0` | Minimum level advanced; Default value depends on device and Type of load value |
| `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable | `0` | Enable / Disable minimum level |
| `G1` | `0..255` | `0` | Group 1 |
| `G2` | `0..255` | `0` | Group 2 |
| `G3` | `0..255` | `0` | Group 3 |
| `G4` | `0..255` | `0` | Group 4 |
| `G5` | `0..255` | `0` | Group 5 |
| `G6` | `0..255` | `0` | Group 6 |
| `G7` | `0..255` | `0` | Group 7 |
| `G8` | `0..255` | `0` | Group 8 |
| `G9` | `0..255` | `0` | Group 9 |
| `G10` | `0..255` | `0` | Group 10 |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `211` | `1` | `8` | `4956` | No textual predicate stored | `7206` |
| `211` | `2` | `8` | `4937` | No textual predicate stored | `7207` |
| `211` | `3` | `8` | `4938` | No textual predicate stored | `7208` |
| `211` | `4` | `8` | `4957` | No textual predicate stored | `7209` |
| `211` | `5` | `8` | `4958` | No textual predicate stored | `7210` |
| `211` | `6` | `8` | `4959` | No textual predicate stored | `7211` |
| `211` | `7` | `8` | `4961` | No textual predicate stored | `7212` |
| `211` | `8` | `8` | `4962` | No textual predicate stored | `7213` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `211` | `8` | `969` | `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Funzionalità di pulsante locale ridotta (Local button mode) |
| `211` | `8` | `970` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Funzionalità di temporizzazione non presente (Hours) |
| `211` | `8` | `971` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Funzionalità di temporizzazione non presente (Minutes) |
| `211` | `8` | `972` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Funzionalità di temporizzazione non presente (Seconds) |
| `211` | `8` | `973` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge (entire reusable range retained) | `0` | Funzionalità di specifica carico pilotato ridotta (Type of load) |
| `211` | `8` | `974` | `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard (entire reusable range retained) | `0` | Funzionalità di specifica carico pilotato ridotta (Type of standard) |
| `211` | `8` | `2182` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |
| `211` | `8` | `3006` | `MIN_LEVEL_ADV` | `1..100` (entire reusable range retained) | `0` | Minimum level advanced |
| `211` | `8` | `3007` | `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable (entire reusable range retained) | `0` | Enable / Disable minimum level |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `7206` | `A=0` | `PL` = `0` | `7206` |
| `7206` | `A=1` | `PL` = `1` | `7206` |
| `7206` | `A=2` | `PL` = `1` | `7206` |
| `7206` | `A=3` | `PL` = `1` | `7206` |
| `7206` | `A=4` | `PL` = `1` | `7206` |
| `7206` | `A=5` | `PL` = `1` | `7206` |
| `7206` | `A=6` | `PL` = `1` | `7206` |
| `7206` | `A=7` | `PL` = `1` | `7206` |
| `7206` | `A=8` | `PL` = `1` | `7206` |
| `7206` | `A=9` | `PL` = `1` | `7206` |
| `7207` | `A=0` | `PL` = `0` | `7207` |
| `7207` | `A=1` | `PL` = `2` | `7207` |
| `7207` | `A=2` | `PL` = `2` | `7207` |
| `7207` | `A=3` | `PL` = `2` | `7207` |
| `7207` | `A=4` | `PL` = `2` | `7207` |
| `7207` | `A=5` | `PL` = `2` | `7207` |
| `7207` | `A=6` | `PL` = `2` | `7207` |
| `7207` | `A=7` | `PL` = `2` | `7207` |
| `7207` | `A=8` | `PL` = `2` | `7207` |
| `7207` | `A=9` | `PL` = `2` | `7207` |
| `7208` | `A=0` | `PL` = `0` | `7208` |
| `7208` | `A=1` | `PL` = `3` | `7208` |
| `7208` | `A=2` | `PL` = `3` | `7208` |
| `7208` | `A=3` | `PL` = `3` | `7208` |
| `7208` | `A=4` | `PL` = `3` | `7208` |
| `7208` | `A=5` | `PL` = `3` | `7208` |
| `7208` | `A=6` | `PL` = `3` | `7208` |
| `7208` | `A=7` | `PL` = `3` | `7208` |
| `7208` | `A=8` | `PL` = `3` | `7208` |
| `7208` | `A=9` | `PL` = `3` | `7208` |
| `7209` | `A=0` | `PL` = `0` | `7209` |
| `7209` | `A=1` | `PL` = `4` | `7209` |
| `7209` | `A=2` | `PL` = `4` | `7209` |
| `7209` | `A=3` | `PL` = `4` | `7209` |
| `7209` | `A=4` | `PL` = `4` | `7209` |
| `7209` | `A=5` | `PL` = `4` | `7209` |
| `7209` | `A=6` | `PL` = `4` | `7209` |
| `7209` | `A=7` | `PL` = `4` | `7209` |
| `7209` | `A=8` | `PL` = `4` | `7209` |
| `7209` | `A=9` | `PL` = `4` | `7209` |
| `7210` | `A=0` | `PL` = `0` | `7210` |
| `7210` | `A=1` | `PL` = `5` | `7210` |
| `7210` | `A=2` | `PL` = `5` | `7210` |
| `7210` | `A=3` | `PL` = `5` | `7210` |
| `7210` | `A=4` | `PL` = `5` | `7210` |
| `7210` | `A=5` | `PL` = `5` | `7210` |
| `7210` | `A=6` | `PL` = `5` | `7210` |
| `7210` | `A=7` | `PL` = `5` | `7210` |
| `7210` | `A=8` | `PL` = `5` | `7210` |
| `7210` | `A=9` | `PL` = `5` | `7210` |
| `7211` | `A=0` | `PL` = `0` | `7211` |
| `7211` | `A=1` | `PL` = `6` | `7211` |
| `7211` | `A=2` | `PL` = `6` | `7211` |
| `7211` | `A=3` | `PL` = `6` | `7211` |
| `7211` | `A=4` | `PL` = `6` | `7211` |
| `7211` | `A=5` | `PL` = `6` | `7211` |
| `7211` | `A=6` | `PL` = `6` | `7211` |
| `7211` | `A=7` | `PL` = `6` | `7211` |
| `7211` | `A=8` | `PL` = `6` | `7211` |
| `7211` | `A=9` | `PL` = `6` | `7211` |
| `7212` | `A=0` | `PL` = `0` | `7212` |
| `7212` | `A=1` | `PL` = `7` | `7212` |
| `7212` | `A=2` | `PL` = `7` | `7212` |
| `7212` | `A=3` | `PL` = `7` | `7212` |
| `7212` | `A=4` | `PL` = `7` | `7212` |
| `7212` | `A=5` | `PL` = `7` | `7212` |
| `7212` | `A=6` | `PL` = `7` | `7212` |
| `7212` | `A=7` | `PL` = `7` | `7212` |
| `7212` | `A=8` | `PL` = `7` | `7212` |
| `7212` | `A=9` | `PL` = `7` | `7212` |
| `7213` | `A=0` | `PL` = `0` | `7213` |
| `7213` | `A=1` | `PL` = `8` | `7213` |
| `7213` | `A=2` | `PL` = `8` | `7213` |
| `7213` | `A=3` | `PL` = `8` | `7213` |
| `7213` | `A=4` | `PL` = `8` | `7213` |
| `7213` | `A=5` | `PL` = `8` | `7213` |
| `7213` | `A=6` | `PL` = `8` | `7213` |
| `7213` | `A=7` | `PL` = `8` | `7213` |
| `7213` | `A=8` | `PL` = `8` | `7213` |
| `7213` | `A=9` | `PL` = `8` | `7213` |

No conversion reference is attached to these slot rows. Resolve the active Object and apply its firmware-specific domain restrictions separately. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `175` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Read installed firmware and compare with the applicability table | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Obtain hardware revision; no source-backed installed value | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Obtain microcontroller identity; no fingerprint retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve active Modules/Objects independently of candidate metadata | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Corroborate installed addressing and distinguish physical from reusable ranges | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Compare installed configuration with the exact firmware/Object restrictions | [Configuration](../../diagnostics/dim35-configuration.md) |

These are catalogue-derived diagnostic candidates. No Device-specific response or support across all commercial variants is established by a hardware capture.

## Functional applicability

| Catalogue Object / role | Applicability | Evidence |
| --- | --- | --- |
| `8` - Dimmer actuator | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |


These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Connect compatible SCS controls/sensors and a separate SCS supply. An addressing module is required except with software configuration. Plug&Go applies through a room controller; Push&Learn creates or changes associations, and Virtual Configurator is the documented software route. Local channel buttons and LEARN/status indicators are distinct from bus commands. Ballast learning uses the illustrated DALI button sequence: a short press followed by a ten-second hold; loads fully illuminate and progressively extinguish. Do not mix DALI and DSI ballasts on one product.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

## Source reconciliation

The exact BTicino technical sheet and Italian export establish the electrical/output roles; the database separately establishes the Legrand reference. The export’s nominal SCS attribute is not the sheet’s mains input: they describe different interfaces. Eight Firmware Modules map eight dimmer Objects and agree with eight physical outputs. The published source is a Lighting Management commissioning document, while the historical Suite catalogue expresses Object/Firmware configuration; their programming routes are not interchangeable.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `BT00582_b_IT.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `BMDI1100-italian-product-sheet.pdf` | Exact named product export; identity and available commercial/physical attributes retained; compliance-template date does not date the product. |

## Evidence limits and open work

Exact Legrand-reference instructions, installed DALI/1-10 V control behavior, association persistence and firmware diagnostics remain unobserved.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
