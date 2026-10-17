# Flush mounted leading dimmer 300 VA

## Summary

H4678 / L4678 is a flush-mounted leading-edge dimmer for the resistive/incandescent and ferromagnetic-transformer loads specified in its historical guide. Short presses switch the load and long presses adjust brightness; broad reusable software load labels do not extend those published load ratings.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0099` | Project identity |
| Technical description | Flush mounted leading dimmer 300 VA | Canonical catalogue |
| Commercial identities | `L4678`, `H4678` | Canonical commercial records |
| Catalogue item | `1123` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `106` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Automation, Dimmer | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `L4678` | Established catalogue identity | canonical commercial record for item `1123` |
| BTicino - Axolute | `H4678` | Established catalogue identity | canonical commercial record for item `1123` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| `AUTOMATISME.pdf` | MyHOME automation guide | historical publisher guide | H/L4678 load table printed p. 159 / PDF p. 161; consumption/dissipation printed p. 160 / PDF p. 162; technical characteristics printed p. 163 / PDF p. 165; only cited applicable leaves examined; unrelated guide pages and linked dedicated documents unexamined | [Archived PDF](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Construction / supply | Two wiring modules; `27 Vdc`, `9 mA`; dissipation `3 W`; `5..35 °C` | AUTOMATISME printed pp. 159–160/PDF pp. 161–162 |
| Supported load ratings | Resistive/incandescent `60..300 W`, `0.25..1.35 A`; ferromagnetic `60..300 VA`, `0.25..1.35 A`; `50/60 Hz` | AUTOMATISME printed p. 159/PDF p. 161; electronic/fluorescent/shutter entries have no supported rating |
| Transformer condition | Rated loading at least 90%; efficiency-dependent apparent-power example retained as a source condition | Same page footnote; not a measured installed efficiency |
| Controls / terminals | Local switch/dim button, status LED, A/PL/M/G sockets; controlled-load/line/neutral diagram | AUTOMATISME printed p. 163/PDF p. 165 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1123` | Canonical catalogue |
| Technical item | Flush mounted leading dimmer 300 VA | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `106` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `106` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `1123` | `L4678` | `1` | `4` | Empty in source |
| `1730` | `H4678` | `1` | `2` | `BTicino_Axolute_Flush mounted leading dimmer ` |

| Record | Visible | Dependent | Gateway flag | Visibility type |
| --- | --- | --- | --- | --- |
| `1123` | `1` | `0` | `0` | Empty in source |
| `1730` | `1` | `0` | `0` | Empty in source |

These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `197` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `197` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `1338` | `8` | `697` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `197` | Physical configuration | `0` | Canonical firmware/mode association |
| `197` | Virtual Configuration | `1` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `197` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `197` | `A` | `0..9` | `0` | A; Environment |
| `197` | `PL` | `0..9` | `0` | PL; Light Point |
| `197` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL`; `9` = `O/I` | `0` | M; Mode (0-4, Pul, Sla, I/O) |
| `197` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |

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

### Device-specific interpretation

Official/default wildcard firmware `197` declares one Module with Object `8` and no Virgin Objects. Firmware M permits `0..4`, 9 O/I, 11 SLA and 15 PUL; no stored conversion establishes their mapping to all reusable fields. The broad TYPE_LOAD enum includes LED, CFL, DALI and DSI, while the exact historical H/L4678 source only supports its specified resistive/incandescent and ferromagnetic loads. MIN_LEVEL_ADV retains domain `1..100` with default 0 outside that domain: no corrected default is invented. STATE_SAVING_ON_RESET filter `2192` retains the whole boolean domain/default 0; this is software state policy, not a documented physical factory-reset sequence. Reusable ten-group and regulation fields remain software scopes rather than additional physical configurators.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `197` | `8` | `2192` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1123` / `modobj = 106` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`8`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `8` Dimmer actuator | Automation | Firmware/Object capability association; resolve the slot and configuration first |

Catalogue system identifiers are not `WHO` numbers. The source establishes the roles shown, not a complete command vocabulary or proof of every installed function. Correlate the selected role with [Functional Protocol](../../functional/) before sending functional commands. Product behavior is additionally bounded by the publisher evidence below; uncorroborated transport and firmware details remain open work.

The guide describes bus and local-button operation: a brief press switches the load, while a sustained press adjusts intensity. These documented functions do not independently establish the full OpenWebNet command or diagnostic vocabulary.

### Manufacturer-documented functions

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Local operation | Short press ON/OFF; long press brightness regulation | AUTOMATISME printed p. 163/PDF p. 165 |
| Indications | Green/blue supplied with load OFF; red load ON; flashing indication configuration error | Same source; source labels are historical device scope |
| Software settings | Load-type/minimum-level/state-recall surfaces require exact product/firmware qualification | Canonical Object `8`; LED/CFL/DALI/DSI labels are not independent hardware support evidence |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

AUTOMATISME, printed p. 163 / PDF p. 165, describes local physical addressing and operation with A/PL/M/G. The source includes a fuse-replacement illustration, but it does not establish an invented fuse rating or a button factory-reset sequence. Recorded catalogue modes and state-saving fields do not supply a universal project-transfer/update procedure. The exact supported-load table and transformer conditions apply before broader reusable load settings.

## Source reconciliation

The canonical technical title identifies leading-edge control; the exact historical H/L guide supplies the restricted load ratings. Reusable Object `8` also contains other load-type enums, so those are retained as schema rather than advertised hardware capability. The MIN_LEVEL_ADV default/domain discrepancy is not silently corrected; STATE_SAVING_ON_RESET is not a documented hardware reset method.

The catalogue-domain and conversion discrepancies are explained under [Device-specific interpretation](#device-specific-interpretation), alongside the complete reusable fields.

## Evidence limits and open work

- Clarify the out-of-domain minimum-level default and firmware-specific effective load settings with matching software/source revisions.
- Linked dedicated revisions, fuse specification, project transfer/reset/update and installed behavior remain unexamined.
- Applicable exact-product guide leaves were inspected; unrelated guide pages and linked dedicated documents remain unexamined.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0091-0100-2026-10-06.md#own-dev-0099)
