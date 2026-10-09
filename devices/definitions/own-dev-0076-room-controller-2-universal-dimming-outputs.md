# Room Controller - 2 universal dimming outputs

## Summary

`BMDI3301` / `048845` is a Room Controller with two independently regulated lighting outputs for incandescent and halogen loads, including compatible transformers. The Legrand technical sheet rates each output at 1000 W or 1000 VA at 230 V; local controls and load-type forcing complement sensor or bus control.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0076` | Project identity |
| Technical description | Room Controller - 2 universal dimming outputs | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMDI3301`, `048845` | Canonical commercial records |
| Catalogue item | `88` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `171` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `3` | Canonical firmware catalogue |
| Categories | Lighting Management, Room Controller, Universal dimmer | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMDI3301` | Established identity | canonical commercial record for item `88` |
| Legrand | `048845` | Established identity | canonical commercial record for item `88` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite version history | software compatibility record | 2015-03-20 | PDF p. 4: both references in version 1.0.45 first-release list dated 2013-10-10;software history,not installed state | [Archived original](https://archive.openwebnet-ha.org/sha256/cd/c4/cdc467fa6408908a98348892c78a98439826b216197f7b17b4230da9f46554c3.pdf) | [Official compatibility source](https://myhomeswupdate.bticino.com/VersionHistory/Version_History_MyHOME_Suite_20150320.pdf) |
| `F01123EN-00.pdf` | English exact technical sheet | F01123EN/00;2010-10-06 | `048845`;full 3 pages | [Archived original](https://archive.openwebnet-ha.org/sha256/50/bc/50bc9ffc078b6a0263525df7647da1ce769a82adbee3ab57a448d14c2c6a5c27.pdf) | [Publisher source](https://assets.legrand.com/pim/NP-FT-GT/F01123EN-00.pdf) |
| `F01123FR-00.pdf` | French exact technical sheet | F01123FR/00;2010-10-06 | `048845`;full 3 pages | [Archived original](https://archive.openwebnet-ha.org/sha256/fa/3f/fa3fc76aab10f9264262f742f1a549119b24f6eee5a938de297eef9e54186b82.pdf) | [Publisher source](https://assets.legrand.com/pim/NP-FT-GT/F01123FR-00.pdf) |
| `programme-mosaic-lighting-FR.pdf` | Historical regional manufacturer catalogue | June 2013 page-production labels | `048845` printed pp. 11,45,51,53 / PDF pp. 13,47,53,55;unrelated pages unexamined | [Archived original](https://archive.openwebnet-ha.org/sha256/c8/45/c8457dab35a22ae446ec3f1c759d63788a1abc956d33240831b7dda76c3a2010.pdf) | [Publisher source](https://www.legrand.fr/sites/default/files/programmemosaic_solutionspilotageeclairage_bd.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply and standby | `100..240 Vac`, `50..60 Hz`; `1.8 W` no-load | F01123EN/FR-00, p. 1 |
| Output loads | At 230 V:`2 × 1000 W` incandescent/halogen, `2 × 1000 VA` ferro/electronic transformers, `2 × 4.3 A`. At 110 V:`2 × 500 W`/VA | F01123EN/FR-00, p. 1; regional brochure printed p. 53 / PDF p. 55 |
| Bus/wiring | Two local ports, `200 mA` combined; screw power `2 × 2.5 mm²`, RJ45; `150 m` controller–sensor, `500 m` supply–furthest product | F01123EN/FR-00, pp. 1–2 |
| Environment/body | `-5..45 °C` operating, `-20..70 °C` storage; IP20, IK04; `762 g`; `147 × 240 mm` body, `275 mm` mounting extent, `50 mm` arrows | F01123EN/FR-00, pp. 1–2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `88` | Canonical catalogue |
| Technical item | Room Controller - 2 universal dimming outputs | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `171` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `171` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `88` | `BMDI3301` | `1` | `5` | Empty in source |
| `1779` | `048845` | `2` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `284` | `-1` | `-1` | `-1` | `3` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `284` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `916` | `8` | `575` |
| `284` | `2` | `8` Dimmer actuator | Fixed/designated metadata | `917` | `8` | `575` |
| `284` | `3` | `167` Room controller | Fixed/designated metadata | `918` | `167` | `576` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `284` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `284` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `8` - Dimmer actuator

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL`, `G1`, `G2` | Reusable schema; apply the Device and firmware restrictions below. |
| Operation, timing and presentation | `M`, `LOCAL_BUTTON`, `DELAYED_OFF`, `STATE_SAVING_ON_RESET`, `HOURS`, `MINUTES`, `SECONDS`, `MIN_LEVEL`, `TYPE_LOAD`, `TYPE_STANDARD`, `MIN_LEVEL_ADV`, `MIN_AUTO`, `G3`, `G4`, `G5`, `G6`, `G7`, `G8`, `G9`, `G10` | Reusable schema; apply the Device and firmware restrictions below. |

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

### Device-specific interpretation

Firmware `284` is the wildcard catalogue default with Deprecated status, not a proven installed version or current availability. Slots `1..2` are Object `8` load contexts; slot `3` is Object `167` controller MODE (stand-alone 0 / supervision 1, default 0), not another electrical output. No Virgin, slot condition or conversion is stored. Relation filters without subset rows retain the complete reusable domains rather than proving physical support for every load enum, local-button mode or timer. The reusable MIN_LEVEL_ADV default 0 lies outside 1..100. Only AID is firmware-scoped and only Advanced Configuration is associated; do not copy A/PL/M physical fields or other mode associations from `BMDI3001`/3002.The all-load catalogue name is bounded by the manufacturer’s exact incandescent/halogen/transformer load tables; do not infer universal LED/CFL compatibility.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `284` | `8` | `1048` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `284` | `8` | `1049` | `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `284` | `8` | `1050` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `284` | `8` | `1051` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `284` | `8` | `1052` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge (entire reusable range retained) | `0` | Type of Load |
| `284` | `8` | `1053` | `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard (entire reusable range retained) | `0` | Voltage standard |
| `284` | `8` | `2187` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `88` / `modobj = 171` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`8`, `167`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Lighting/load selection | Automatic capacitive/inductive recognition when channel activated; manual forcing available; no ferro/electronic transformer mix on same channel | F01123EN/FR-00, pp. 1, 3 |
| Fault response | Local peripheral failure: lights relight after 10 min; upstream connection failure: after 50 s; bus-capacity LED | F01123EN/FR-00, p. 1 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Power-on pairs compatible controls/detectors automatically. Legrand specifies tools 88235/88230 for parameters (p. 3); the regional brochure also documents custom Learn-button associations (printed p. 51 / PDF p. 53). The load-recognition diagram cycles capacitive, forced capacitive, inductive, forced inductive with short presses and confirms using 10 s (technical p. 3). Only Advanced Configuration is associated with firmware `284`; do not add a physical or virtual catalogue mode simply because the 2013 Suite release list calls its entire device list virtual. Only transformers suitable for electronic switching are permitted; no general LED compatibility follows from the marketing term “All loads”.

## Source reconciliation

Catalogue SKU relationships establish `BMDI3301`/048845. Dedicated retained F01123 EN/FR revision 00 dated 6 October 2010 directly identifies `048845` and resolves the former physical-sheet gap. The June 2013 regional brochure confirms 1000 W per output; the previous aggregate 1000 W wording was unsupported and is removed. The Suite history’s March 2015 publication includes an October 2013 first-release list naming both references, not proof of installed firmware or a 2015 introduction. FR/EN sheets agree on ratings but cite different historical product standards (NF EN 50428 versus IEC 60669-2-1). Technical facts specifically documented for `048845` are not independently hardware-tested on a `BMDI3301` unit.

Catalogue interpretation is detailed under [Object configuration surfaces](#object-configuration-surfaces); these software records do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- The exact `048845` technical sheets are retained; no separate BTicino-labelled `BMDI3301` technical original was recovered from the current product page. Cross-brand identity is nevertheless established by the canonical SKU mapping.
- No installed load or software test is retained. Referenced 88235/88230 and sensor technical instructions remain unexamined; all-load wording does not authorize every LED/CFL load.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0071-0080-2026-10-06.md#own-dev-0076)
