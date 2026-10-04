# Four-channel DALI room controller

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0128` | Project identity |
| Technical description | Four-channel DALI room controller | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `BMDI3101`, `048844` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1180` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `170` | Main association; independent of project ID |
| Firmware definition | `377` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `5` | Firmware metadata |
| Categories | Gateways and interfaces, Actuators, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMDI3101` | Established catalogue identity | Manufacturer database commercial record `1180` explicitly links this SKU to item `1180` |
| Legrand | `048844` | Established catalogue identity | Manufacturer database commercial record `1776` explicitly links this SKU to item `1180` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `BT00310_c_IT.pdf` | Manufacturer legacy documentation | `BT00310_c_IT; 12/11/2013` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-3; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/c1/0b/c10b873bffd13fce1223fe9307318d3cebcb0bb773d6187c449674eb6e9bc988.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/BT00310_c_IT.pdf) |
| `BMDI3101-italian-product-sheet.pdf` | Exact Italian product export | `Retrieved 04/10/2026; old compliance-template date does not establish product publication date` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-1; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/2c/3d/2c3df3fabd44cb1db0fc77fb979062132475653720bb6f106a5a51f5df97a1f8.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMDI3101) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `1180` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mains | `100..240 Vac; 50/60 Hz` | `BT00310-c-IT` printed/PDF pp. 1-3 |
| Standby consumption | `2.4 W` | `BT00310-c-IT` printed/PDF pp. 1-3 |
| DALI outputs, technical sheet | `4 channels; <=32 ballasts/channel` | `BT00310-c-IT` printed/PDF pp. 1-3 |
| DALI outputs, Italian export | `4 independent channels; <=16 ballasts/channel` | `BT00310-c-IT` printed/PDF pp. 1-3 |
| Peripheral SCS supply budget | `combined four peripheral branches <=200 mA` | `BT00310-c-IT` printed/PDF pp. 1-3 |
| SCS cable lengths | `<=150 m controller-to-farthest peripheral; <=500 m supply-to-farthest bus device` | `BT00310-c-IT` printed/PDF pp. 1-3 |
| DALI cable lengths | `100 m/0.5 mm²; 150 m/0.75 mm²; 300 m/1.5 mm²` | `BT00310-c-IT` printed/PDF pp. 1-3 |
| Terminals | `mains: 2 x 2.5 mm²; DALI <=1.5 mm²; SCS RJ45` | `BT00310-c-IT` printed/PDF pp. 1-3 |
| Dimensions | `147 x 275 x 50 mm; secondary illustrated length 240 mm` | `BT00310-c-IT` printed/PDF pp. 1-3 |
| Mounting | `false ceiling or suitable cable tray` | `BT00310-c-IT` printed/PDF pp. 1-3 |
| Operating / storage temperature | `-5..45 °C / -20..70 °C` | `BT00310-c-IT` printed/PDF pp. 1-3 |
| Weight / enclosure | `525 g; IP20; IK04` | `BT00310-c-IT` printed/PDF pp. 1-3 |
| Documented bus-fault response | `peripheral branch fault: lights relight after 10 min; backbone link fault: after 50 s` | `BT00310-c-IT` printed/PDF pp. 1-3 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1180` | Canonical catalogue |
| Technical item description | Room controller - Dimmer 4 Outputs Dali | Canonical catalogue |
| Item family | 0; key `23` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `170` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `377` | `-1` | `-1` | `-1` | `5` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `377` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `905` | `8` | `567` |
| `377` | `2` | `8` Dimmer actuator | Fixed/designated metadata | `906` | `8` | `567` |
| `377` | `3` | `8` Dimmer actuator | Fixed/designated metadata | `907` | `8` | `567` |
| `377` | `4` | `8` Dimmer actuator | Fixed/designated metadata | `908` | `8` | `567` |
| `377` | `5` | `167` Room controller | Fixed/designated metadata | `909` | `167` | `568` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `377` | Advanced Configuration | `2` | Association key `2` |


No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `377` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

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


### Object `167` - Room controller

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `MODE` | `0` = Stand-alone mode; `1` = Supervision mode | `0` | Modality; Mode |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `377` | `8` | `1029` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `377` | `8` | `1030` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `377` | `8` | `1031` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `377` | `8` | `1032` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge (entire reusable range retained) | `0` | Type of Load |
| `377` | `8` | `1033` | `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard (entire reusable range retained) | `0` | Voltage standard |
| `377` | `8` | `1034` | `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `377` | `8` | `2185` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `170` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `167` - Room controller | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |


These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The standalone topology powers SCS controls/sensors from the mains-powered room controller; the integrated topology links base systems over the SCS backbone. Plug&Go, Push&Learn and software commissioning depend on that topology. Learn DALI ballasts through the local short/ten-second sequence. Do not mix DALI and DSI on one channel. The red indicator reports an exceeded SCS branch/bus capacity. The source’s fail-on timings describe documented operation rather than a measured capture.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

## Source reconciliation

BMDI3101 and 048844 are explicit database identities. The exact 2013 sheet states 32 ballasts per channel repeatedly, whereas the retrieved Italian product export states 16. This is an unresolved capacity/revision discrepancy; no manufacturer change notice establishes which installed units support which capacity. Four dimmer placements plus room-controller Object `167` explain five Firmware Modules without implying five DALI outputs.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `BT00310_c_IT.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `BMDI3101-italian-product-sheet.pdf` | Exact named product export; identity and available commercial/physical attributes retained; compliance-template date does not date the product. |

## Evidence limits and open work

Manufacturer clarification of 16 versus 32 ballasts, exact 048844 documentation, physical hardware revision and fail-on/runtime captures remain missing.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
