# LED and CFL dimmer

## Summary

This single-channel DIN dimmer regulates documented dimmable LED, compact fluorescent and other compatible lighting loads. It provides local switching and brightness adjustment, with configurable load type and minimum level to suit the connected lamps.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0139` | Project identity |
| Technical description | LED and CFL dimmer | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `F418`, `003665` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1582` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `47` | Main association; independent of project ID |
| Firmware definition | `189` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Actuators | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F418` | Established catalogue identity | Manufacturer database commercial record `1638` explicitly links this SKU to item `1582` |
| Legrand | `003665` | Established catalogue identity | Manufacturer database commercial record `2187` explicitly links this SKU to item `1582` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `F418-italian-product-sheet.pdf` | Exact Italian product export | `Retrieved 04/10/2026; old compliance-template date does not establish product publication date` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-1; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/62/8f/628f8e289d17ee293652df5772dab21bd838b7bd06e0e4af950fde92328871c3.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F418) |
| `LE05177AE.pdf` | Manufacturer legacy documentation | `LE05177AE-01PC-17W18; diagrams include older product marking 12W19` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-2; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/41/90/41903d436019966da6cb9b08d6a2d628819513382804de476db9f44f6d1a90e8.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/LE05177AE.pdf) |
| `MQ00594_d_IT.pdf` | Manufacturer legacy documentation | `MQ00594_d_IT; 20/09/2018` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-4; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/75/88/758805e32270325d7905b9bce00e7f5997d37cb4997483c01c479c3a0577090c.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/MQ00594_d_IT.pdf) |
| `MQ00594_d_EN.pdf` | Exact historical manufacturer documentation | `MQ00594_d_EN; 20/09/2018` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-4; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/cf/0f/cf0f1ea620adca98efc2cf844ed0866021e087fbcc4e0ffb88a239adfed5b873.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MQ00594_d_EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `1582` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS nominal / operating supply | `27 Vdc / 18..27 Vdc` | `MQ00594-d-EN/IT` printed/PDF pp. 1-4 |
| Bus current | `10 mA maximum` | `MQ00594-d-EN/IT` printed/PDF pp. 1-4 |
| Output | `1 x 0.9 A; 100 adjustment levels` | `MQ00594-d-EN/IT` printed/PDF pp. 1-4 |
| Operating temperature | `-5..35 °C` | `MQ00594-d-EN/IT` printed/PDF pp. 1-4 |
| Mounting / enclosure | `4 DIN modules; IP20; IK04` | `MQ00594-d-EN/IT` printed/PDF pp. 1-4 |
| Incandescent / halogen at 230 Vac | `1..300 W` | `MQ00594-d-EN/IT` printed/PDF pp. 1-4 |
| Dimmable LED/CFL/electronic transformer at 230 Vac | `1..300 VA; LED/CFL typical correspondence about 200 W` | `MQ00594-d-EN/IT` printed/PDF pp. 1-4 |
| Dissipation at maximum load | `2.5 W at 230 Vac; 1.9 W at 127 Vac` | `MQ00594-d-EN/IT` printed/PDF pp. 1-4 |
| Fuse | `time-lag T1.6H 250V` | `MQ00594-d-EN/IT` printed/PDF pp. 1-4 |
| Lamp type TY | `0 inductive LED; 1 inductive CFL; 2 capacitive LED/electronic transformer; 3 capacitive CFL; 4 halogen` | `MQ00594-d-EN/IT` printed/PDF pp. 1-4 |
| TY-dependent default minimum | `TY0/TY2:10%; TY1/TY3:37%; TY4:1%` | `MQ00594-d-EN/IT` printed/PDF pp. 1-4 |
| Physical MIN selector | `0:TY-dependent default; 1:1%; 2:5%; 3:10%; 4:15%; 5:20%; 6:25%; 7:30%; 8:35%; 9:40%` | `MQ00594-d-EN/IT` printed/PDF pp. 1-4 |

### Instruction-specific load and installation limits



| Property | Value | Evidence |
| --- | --- | --- |
| Low-voltage mains range | `110..127 Vac:1..150 W halogen; 1..150 VA LED/CFL/electronic transformer` | LE05177AE PDF p. 1 |
| High-voltage mains range | `200..240 Vac:1..300 W halogen; 1..300 VA LED/CFL/electronic transformer` | LE05177AE PDF p. 1 |
| Installation constraints | no mixed loads; do not mount dimmers side by side or next to a power supply | LE05177AE PDF p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1582` | Canonical catalogue |
| Technical item description | Dimmer for energy saving lamps bus | Canonical catalogue |
| Item family | 0; key `4` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `47` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `189` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `189` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `915` | `8` | `574` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `189` | Virtual Configuration | `1` | Association key `1` |
| `189` | Advanced Configuration | `2` | Association key `2` |
| `189` | Physical configuration | `0` | Association key `3` |


No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

### Published physical actuator modes



| Function | Physical selector | Published virtual scope |
| --- | --- | --- |
| Master | `M=0` | master role |
| Slave | `M=SLA` | follows matching addressed master |
| Master pushbutton | `M=PUL` | ignores room/general controls |
| Delayed slave `OFF` | `M=1..4:1..4 min` | `0..255 s; point-to-point only` |
| Slave `PUL` | no listed physical selector | software configuration required |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `189` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `189` | `A` | `0..9` | `1` | A; Enviroment (extended) |
| `189` | `PL` | `0..9` | `1` | PL; Light Point |
| `189` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |
| `189` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (0-4, Pul, Sla) |
| `189` | `TY` | `0..4` | `0` | TY; (LED leading edge: 0) (CFL leading edge: 1) (LED trailing edge: 2) (CFL trailing edge: 3) (Alogen lamp: 4) |
| `189` | `MIN` | `0..9` | `0` | MIN; Minimum level (Auto: 0) (1%: 1) (5%: 2) (10%: 3) (15%: 4) (20%: 5) (25%: 6) (30%: 7) (35%: 8) (40%: 9) |

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
| `189` | `1` | `8` | `4149` | No textual predicate stored | `3` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `189` | `8` | `1035` | `MIN_LEVEL` | `1..100` (entire reusable range retained) | `1` | Minimum level |
| `189` | `8` | `1036` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `4`; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI | `0` | Type of Load |
| `189` | `8` | `1037` | `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard (entire reusable range retained) | `0` | Voltage standard |
| `189` | `8` | `1038` | `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button mode |
| `189` | `8` | `1039` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `189` | `8` | `1040` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `189` | `8` | `1041` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `189` | `8` | `2186` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `3` | `M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `3` |
| `3` | `M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `3` |
| `3` | `M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `3` |
| `3` | `M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `3` |
| `3` | `M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `3` |
| `3` | `M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `3` |
| `3` | `M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `3` |
| `3` | `M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `3` |

No conversion reference is attached to these slot rows. Resolve the active Object and apply its firmware-specific domain restrictions separately. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `47` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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

Choose the actual dimmable lamp/transformer type and stable minimum before operation. Local short presses switch; long presses adjust. Physical addressing uses A/PL and G; master/slave/`PUL`/delayed-slave settings are separately scoped from TY and MIN. Suite enables slave `PUL` and virtual minimum `0..100`. The exact sheet says MyHOME Server configures one channel automatically. Manufacturer-tested lamp examples on p. 4 are revision-bound and not a promise of compatibility with changed bulbs. The instruction warns about flicker from carried waves on mains and requires supply isolation when changing the fuse.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

## Source reconciliation

The exact d-revision English and Italian sheets agree on dimming capacity and configuration. The Italian export’s compressed descriptive “1300W/1300VA” is inconsistent with its own `300 W/300 VA` fields and the sheets’ explicit `1..300` ranges; it is retained as a product-export text defect, not a 1300 W rating. LE05177AE’s load/power and LED labels differ from the newer technical sheet and must be applied by its own printed production scope. The sheet swaps protection/robustness labels around IP20/IK04; the standard code meanings are clear but the printed labels remain a source defect. Reusable dimmer fields are narrowed by the exact Firmware filters.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `F418-italian-product-sheet.pdf` | Exact named product export; identity and available commercial/physical attributes retained; compliance-template date does not date the product. |
| `LE05177AE.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `MQ00594_d_IT.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `MQ00594_d_EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |

LE05177AE states LED green=load `OFF`, red=`ON`, flashing=load fault, whereas the d-sheet specifies orange=`ON` and distinguishes fast/slow orange/green flashing. Its photograph contains older `200 W/100 W` markings while its table states `300 VA/150 VA` (approximately `200 W/100 W` for typical LED/CFL). The markings describe a load-class/production distinction; no universal 300 W LED rating is inferred.

## Evidence limits and open work

Installed-production compatibility with the instruction’s older lamp/indicator values, exact load behavior, bulb-revision stability and diagnostics remain open.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
