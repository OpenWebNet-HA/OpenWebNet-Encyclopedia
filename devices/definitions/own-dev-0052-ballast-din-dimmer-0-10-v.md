# Ballast DIN dimmer 0-10 V

## Summary

This six-module DIN actuator switches and dims lighting through an analog ballast-control interface. It supports nominal 1–10 V control and selectable lower output levels for 0–10 V use, with one switched channel and local test controls.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0052` | Project identity |
| Technical description | Ballast DIN dimmer 0-10 V | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMDI1001`, `002611` | Canonical commercial records |
| Catalogue item | `47` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `163` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Lighting, Dimmer, DIN actuator | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMDI1001` | Established identity | canonical commercial record for item `47` |
| Legrand | `002611` | Established identity | canonical commercial record for item `47` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00314-f-FR` | technical sheet | 2014-04-18 | Printed/PDF pp. 1–4; exact `002611` / `BMDI1001` physical characteristics, configuration and wiring | [Archived original](https://archive.openwebnet-ha.org/sha256/8b/36/8b36e76ccaef5d1099d03f0a8fce88d37221f3d3c9c0658f2bba75d4f9fd6c4f.pdf) | [Official source](https://assets.legrand.com/general/legrand-fr/bt/np-ft-gt/mq00314-f-fr.pdf) |
| `ch_de_katalog_wohnbau.pdf` | Historical regional catalogue | No dated imprint established | Printed pp. 158, 161 / PDF pp. 160, 163; exact `BMDI1001` dimensions, analog output and configuration entry | [Archived original](https://archive.openwebnet-ha.org/sha256/9f/e5/9fe511c3ac12d861dff7d8d28ddec3b3612a27e99a804afbed89877c73a6b4ed.pdf) | Publisher URL not retained in manifest |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / maximum consumption | `100..240 Vac`, 50/`60 Hz`; `165 mA` | MQ00314-f-FR, printed/PDF pp. 1–4 |
| Output | One `4.3 A` switched channel; 1000 VA at `240 Vac` / 500 VA at `110 Vac`; maximum 160 ballasts | MQ00314-f-FR, printed/PDF pp. 1–4 |
| Analog control | Nominal 1–10 V ballast control; minimum-output choices also permit 0–10 V | MQ00314-f-FR, printed/PDF pp. 1–4 |
| Environment / size | `−5..45 °C`; IP20; IK04; six DIN modules | MQ00314-f-FR, printed/PDF pp. 1–4 |
| Connections | RJ45 SCS bus; supply terminal 2 × 2.5 mm²; outputs 2 × 1.5 mm² and 1 × 2.5 mm² | MQ00314-f-FR, printed/PDF pp. 1–4 |
| Local interface | Load `LED` and pushbutton; learning `LED` and button; physical configuration area only for MyHOME | MQ00314-f-FR, printed/PDF pp. 1–4 |
| Regional control-output rating / dimensions | Maximum `50 mA` control output; 105 × 90 × 60/`61 mm`; `1000 W` headline is distinct from French voltage-dependent VA ratings | German catalogue, printed pp. 158, 161 / PDF pp. 160, 163 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `47` | Canonical catalogue |
| Technical item | Ballast DIN dimmer 0-10 V | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `163` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `163` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `656` | `002611` | `2` | `5` | `Legrand_Undefined_Ballast DIN dimmer 0-10 V` |
| `1769` | `BMDI1001` | `1` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; `visibility_type` is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `206` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `206` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `664` | `8` | `460` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `206` | Physical configuration | `0` | Canonical firmware/mode association |
| `206` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `206` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `206` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `206` | `A` | `0..9` | `0` | A; Environment |
| `206` | `PL` | `0..9` | `0` | `PL`; Light Point |
| `206` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (0-4, Pul, Sla) |
| `206` | `G1` | `0..9` | `0` | `G1`; `G1` - (0-9) |
| `206` | `G2` | `0..9` | `0` | `G2`; `G2` - (0-9) |
| `206` | `G3` | `0..9` | `0` | `G3`; `G3` - (0-9) |

### Published physical selectors absent from the stored firmware field list

| Selector | Physical setting | Published result | Evidence |
| --- | --- | --- | --- |
| `L` | `0` | Minimum output `1 V` | `MQ00314-f-FR`, printed p. 2 / PDF p. 2 |
| `L` | `1` | Minimum output `1.5 V` | Same source |
| `L` | `2` | Minimum output `2 V` | Same source |
| `L` | `3` | Minimum output `0 V` | Same source |
| `L` | `4` | Minimum output `0.5 V` | Same source |
| `TYPE` | `0` | Fluorescent ballast; soft-start accounts for typical `1.5 s` ignition delay | Same source, note 3 |
| `TYPE` | `1` | `LED` supply; immediate soft-start | Same source, note 3 |

The physical `L` selector establishes support for both 1-10 V and 0-10 V control; the apparent catalogue/product naming difference is therefore not evidence of incompatible standards. `L` and `TYPE` are printed physical positions but are absent from firmware `206`'s stored field list. Do not alias those positions to similarly named reusable Object fields without an established conversion.

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
| `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = `LED` trailing edge / electronic transformers; `12` = `LED` leading edge; `13` = CFL trailing edge; `14` = CFL leading edge | `0` | Type of load; Default value depends on device. |
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

Firmware `206` designates one Dimmer actuator Object `8`, with no Virgin and an empty slot predicate. No conversion is associated. Firmware A/`PL`/`G1`..`G3`=`0..9` is narrower than reusable address/group domains and the sheet's virtual ten-group scope. The physical sheet has L and `TYPE` sockets absent from firmware fields. Physical `TYPE=0/1` (fluorescent/`LED`) is distinct from reusable `TYPE_LOAD`, whose relation filter excludes fluorescent 5 and `LED` 6 while retaining unrelated phase-cut/DALI/DSI labels. This does not establish those load interfaces on this ballast product. `MIN_LEVEL_ADV` domain `1..100` retains default 0: this is a source irregularity, not a legal selected level. `TYPE_STANDARD=0/1` models 1–10/0–10 V, but no stored conversion maps L to `TYPE_STANDARD` or `MIN_LEVEL`. Software slave-PUL `M=16` is reusable, beyond the physical firmware M enum.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `206` | `1` | `8` | `4145` | No textual predicate stored | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `206` | `8` | `582` | `MIN_LEVEL_ADV` | `1..100` (entire reusable range retained) | `0` | Minimum level advanced |
| `206` | `8` | `583` | `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable (entire reusable range retained) | `0` | enable disable minimum level |
| `206` | `8` | `584` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `10` = Halogen lamp; `11` = `LED` trailing edge / electronic transformers; `12` = `LED` leading edge; `13` = CFL trailing edge; `14` = CFL leading edge; `2` = Forced capacitive; `3` = Forced inductive; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI | `0` | Type of Load |
| `206` | `8` | `585` | `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `206` | `8` | `2177` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |
| `206` | `8` | `2494` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `206` | `8` | `2495` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `206` | `8` | `2496` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `47` / `modobj = 163` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`8`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Loads | Incandescent, halogen, compact fluorescent and `LED` lighting through suitable 1–10 V ballast interface | MQ00314-f-FR, printed/PDF pp. 1–4 |
| Control | Configured bus control/sensor or integrated test/control button; local ON/OFF and dimming | MQ00314-f-FR, printed/PDF pp. 1–4 |
| `TYPE` setting | 0 fluorescent with typical 1.5 s start delay; 1 `LED` with immediate soft start | MQ00314-f-FR, printed/PDF pp. 1–4 |
| Delayed slave OFF | Point-to-point only: master OFF is immediate; matching slave stays on for the selected delay | MQ00314-f-FR, printed/PDF pp. 1–4 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Use Virtual Configurator for Lighting Management; MyHOME supports physical configurators or MyHOME_Suite (MQ00314-f-FR p. 2). The software enables slave-PUL and preset position beyond the physical table.

| Setting | Physical values | Virtual scope |
| --- | --- | --- |
| A / `PL` | A=`0..9`; `PL`=`1..9` | Room `0..10`; light point `0..15` |
| Groups | G=`0..9` | Groups `1..10`, each `0..255` |
| M | 0 master; `SLA` slave; PUL monostable ON; 1/2/3/4 delayed OFF 1/2/3/4 min | Delayed OFF `0..255` s; master/master-PUL and point-to-point applicability |
| L | 0: 1 V; 1: 1.5 V; 2: 2 V; 3: 0 V; 4: 0.5 V | Minimum light level `1..100` |
| `TYPE` | 0 fluorescent; 1 `LED` | Fluorescent / `LED` load selection |

L selects the minimum output voltage while ON: `L=3/4` extends the nominal 1–10 V interface into 0–10 V use. This does not authorize an arbitrary phase-cut or DALI load from a reusable `TYPE_LOAD` label. The French wiring sheet p. 3 separates load/mains switching and low-voltage ballast terminals; p. 4 shows EASYWAY arrangements, not an additional catalogue connection mode. Maintenance chemicals are sheet-specific; use the original p. 3 for those instructions.

## Source reconciliation

The French exact-product sheet names both `002611` and `BMDI1001`. Its 1–10 V title and the catalogue's 0–10 V name describe configurable output ranges rather than conflicting identities. The German 50 mA control-output figure supplements the French sheet; its 1000 W headline does not replace the French 1000/500 VA voltage-scoped limits. Physical L/`TYPE` settings, software load labels and reusable Object enums must remain separate.

Catalogue-specific scope and filter irregularities are detailed under [Object configuration surfaces](#object-configuration-surfaces); those relations do not establish additional physical sensors, load interfaces or installed behavior.

## Evidence limits and open work

- No release note maps the historical wildcard firmware to a hardware revision or resolves the `TYPE_LOAD` filter mismatch.
- Virtual Configurator/MYHOME_Suite help and EASYWAY controller procedures are linked by the sheet but not independently examined.
- Installed ballast compatibility, minimum dim level, startup behavior and diagnostics are unobserved.
- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, software payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0051-0060-2026-10-06.md#own-dev-0052)
