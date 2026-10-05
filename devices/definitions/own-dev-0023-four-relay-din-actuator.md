# Four-relay DIN actuator

## Summary

This two-module DIN actuator provides four independent relay outputs for configured lighting loads. Relay pairs can be logically interlocked for motor or shutter use, with local controls and indicators for manual operation.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0023` | Project identity |
| Technical description | Four-independent-relay 2-DIN actuator for lighting and paired automation/motor loads | Catalogue + official documentation |
| Commercial identities | `F411/4`, `003844` | Catalogue |
| Catalogue item | `3` - “4 relay actuator 2 modules DIN bus” | Canonical manufacturer catalogue |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Canonical manufacturer catalogue |
| Item model / `modobj` | `130` | Canonical manufacturer catalogue |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `142` | Canonical manufacturer catalogue |
| Declared Modules | `4` | Canonical manufacturer catalogue |
| Categories | Actuator, Lighting, Automation, Shutter | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F411/4` | Established identity | Canonical catalogue; canonical commercial record `3`; Commercial identity of this Technical Device |
| Legrand | `003844` | Established identity | Canonical catalogue; canonical commercial record `1707`; Commercial identity of this Technical Device |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F411/4` | `8012199425061` | [Archived original](https://archive.openwebnet-ha.org/sha256/d5/d5/d5d519a8d1715f0e8b04d20310ff7884c1b4444195e1b9a524f0c4d6fdf3bf0a.pdf), `F411_4-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ST-00000896-EN` | Technical sheet | 2021-03-23 | whole document / PDF pp. 1-4 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/f3/1c/f31ca3b29c75fc69881f4d2ed3744435c10b83bad181a5ce4fb3e55a08509def.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/ST-00000896-EN.pdf) |
| `AUTOMATISME.pdf` | MyHOME automation guide | October 2006 publisher guide | F411/4 configuration: printed p. 122 / PDF p. 124; load/specification tables: printed pp. 157-160 / PDF pp. 159-162 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |
| `F411_4-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `F411/4` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/d5/d5/d5d519a8d1715f0e8b04d20310ff7884c1b4444195e1b9a524f0c4d6fdf3bf0a.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F411_4) |
| `ST-00002122-EN.pdf` | Classe 300EOS compatibility matrix | 21 October 2024 | Only applicable production/compatibility rows, p.7 and physical-configuration exclusion, p.8 | [Archived original](https://archive.openwebnet-ha.org/sha256/e1/a8/e1a8da77199296d9f56ea708402f144b8614473558002c0f8db4ee16eb2f0d0d.pdf) | Publisher URL not retained in manifest |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting / channels | 2 DIN modules; 4 relay output(s) | ST-00000896-EN p. 1 |
| SCS nominal / operating supply | `27 Vdc` / `18..27` Vdc | ST-00000896-EN p. 1 |
| Current draw | `60 mA`; `40 mA` for products before batch 14W39 | ST-00000896-EN p. 1 |
| Operating temperature | −5..+`45 °C` | ST-00000896-EN p. 1 |
| Maximum-load dissipation | `2.4 W` | ST-00000896-EN p. 1 |
| Local controls | Load-control button(s) and status LED(s); 2018 sheets require configuration before local operation | ST-00000896-EN p. 1 |

| `230 Vac` load category | Published rating | Evidence |
| --- | --- | --- |
| Incandescent / halogen | `460 W` / `2 A` | ST-00000896-EN p. 1 |
| LED / CFL | `70 W`, max. 2 lamps | ST-00000896-EN p. 1 |
| Linear fluorescent / electronic transformer | `70 W` / `0.3 A` | ST-00000896-EN p. 1 |
| Ferromagnetic transformer | `460 VA` / `2 A`, cosφ 0.5 | ST-00000896-EN p. 1 |
| Motor | `460 W` / `2 A` | ST-00000896-EN p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `3` | Canonical catalogue |
| Technical item description | 4 relay actuator 2 modules DIN bus | Canonical catalogue |
| Item family | `2` - Actuator | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `130` | `AS_ITEM_SYSTEM` |
| Commercial records | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `130` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Canonical commercial record metadata

| Reference / record | Catalogue name / source description | Visibility / type | Dependent / gateway | Evidence |
| --- | --- | --- | --- | --- |
| `F411/4` / `3` | 4 relay actuator 2 modules DIN bus; `BTicino_Undefined_4 relays DIN actuator 6 A` | `1` / Empty | `0` / `0` | Canonical manufacturer catalogue |
| `003844` / `1707` | 4 relay actuator 2 modules DIN bus; `Legrand_Undefined_Attuatore DIN 4 relay` | `1` / Empty | `0` / `0` | Canonical manufacturer catalogue |

Visibility, dependency and gateway flags describe the catalogue record, not the installed Device state.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `142` | `-1` | `-1` | `-1` | `4` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Firmware `142` is wildcard `-1.-1.-1` and declares four Modules.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `142` | `1` | `1` Blind actuator | Candidate alternative | `500` | `1` | `349` |
| `142` | `1` | `6` Light actuator | Fixed/designated metadata | `501` | `6` | `350` |
| `142` | `1` | `7` Automation actuator | Candidate alternative | `505` | `7` | `351` |
| `142` | `2` | `6` Light actuator | Fixed/designated metadata | `502` | `6` | `350` |
| `142` | `2` | `7` Automation actuator | Candidate alternative | `506` | `7` | `351` |
| `142` | `3` | `6` Light actuator | Fixed/designated metadata | `503` | `6` | `350` |
| `142` | `3` | `7` Automation actuator | Candidate alternative | `507` | `7` | `351` |
| `142` | `4` | `6` Light actuator | Fixed/designated metadata | `504` | `6` | `350` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `142` | `510` Automation relay virgin | `1`, `2`, `3`, `4` | `1`, `6`, `7` | `510` | `15` |

All four slots can be Object `6`, Light actuator. Object `7`, Automation actuator, is a candidate on slots `1..3`; Object `1`, Blind actuator, is a candidate beginning at slot `1`. Virgin Object `510`, Automation relay virgin, applies across slots `1..4` and permits Objects `1`, `6`, and `7`.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `142` | Physical configuration | `0` | Canonical firmware/mode association |
| `142` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `142` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `142` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `142` | `A` | `0..9` | `0` | A; Environment |
| `142` | `PL1` | `0..9` | `0` | `PL1`; `PL1` - (0-9) |
| `142` | `PL2` | `0..9` | `0` | `PL2`; `PL2` - (0-9) |
| `142` | `PL3` | `0..9` | `0` | `PL3`; `PL3` - (0-9) |
| `142` | `PL4` | `0..9` | `0` | `PL4`; `PL4` - (0-9) |
| `142` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (1-4, Pul, Sla) |

The shared area plus `PL1` through `PL4` fields address the four output positions. The active Light / Automation / Blind Object topology is governed by the slot conditions documented below.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `1` - Blind actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality |
| `LOCAL_BUTTON` | `12` = Bistable control; `13` = Monostable control | `12` | Local button modality |
| `STOP_TIME` | `0` = Infinite; `1` = 1 s; `2` = 2 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `21` = 21 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min | `60` | Stop time; Only for Master modes |
| `DELAY_DOORS` | `0..60` | `3` | Delay between doors |
| `G1` | `0..255` | `0` | Group 1; Group = 0 means no group |
| `G2` | `0..255` | `0` | Group 2; Group = 0 means no group |
| `G3` | `0..255` | `0` | Group 3; Group = 0 means no group |
| `G4` | `0..255` | `0` | Group 4; Group = 0 means no group |
| `G5` | `0..255` | `0` | Group 5; Group = 0 means no group |
| `G6` | `0..255` | `0` | Group 6; Group = 0 means no group |
| `G7` | `0..255` | `0` | Group 7; Group = 0 means no group |
| `G8` | `0..255` | `0` | Group 8; Group = 0 means no group |
| `G9` | `0..255` | `0` | Group 9; Group = 0 means no group |
| `G10` | `0..255` | `0` | Group 10; Group = 0 means no group |

### Object `6` - Light actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality |
| `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open | `0` | Relay state on device reset |
| `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing | `0` | Load control mode |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `SUBTYPE` | `11` = Actuator; `1` = Lamp; `10` = Valve; `15` = Differential restart; `6` = Fan; `7` = Watering; `8` = Controlled socket; `9` = Lock | `11` | Type of load |
| `G1` | `0..255` | `0` | Group 1; Group = 0 means no group |
| `G2` | `0..255` | `0` | Group 2; Group = 0 means no group |
| `G3` | `0..255` | `0` | Group 3; Group = 0 means no group |
| `G4` | `0..255` | `0` | Group 4; Group = 0 means no group |
| `G5` | `0..255` | `0` | Group 5; Group = 0 means no group |
| `G6` | `0..255` | `0` | Group 6; Group = 0 means no group |
| `G7` | `0..255` | `0` | Group 7; Group = 0 means no group |
| `G8` | `0..255` | `0` | Group 8; Group = 0 means no group |
| `G9` | `0..255` | `0` | Group 9; Group = 0 means no group |
| `G10` | `0..255` | `0` | Group 10; Group = 0 means no group |

### Object `7` - Automation actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality |
| `LOCAL_BUTTON` | `12` = Bistable control; `13` = Monostable control; `14` = Bistable and blades control | `12` | Local button modality |
| `STOP_TIME` | `0` = Infinite; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min | `60` | Stop time |
| `SUBTYPE` | `11` = Actuator; `2` = Shutter; `3` = Curtain; `4` = Gate; `5` = Garage door; `15` = Differential restart | `11` | Type of load |
| `G1` | `0..255` | `0` | Group 1; Group = 0 means no group |
| `G2` | `0..255` | `0` | Group 2; Group = 0 means no group |
| `G3` | `0..255` | `0` | Group 3; Group = 0 means no group |
| `G4` | `0..255` | `0` | Group 4; Group = 0 means no group |
| `G5` | `0..255` | `0` | Group 5; Group = 0 means no group |
| `G6` | `0..255` | `0` | Group 6; Group = 0 means no group |
| `G7` | `0..255` | `0` | Group 7; Group = 0 means no group |
| `G8` | `0..255` | `0` | Group 8; Group = 0 means no group |
| `G9` | `0..255` | `0` | Group 9; Group = 0 means no group |
| `G10` | `0..255` | `0` | Group 10; Group = 0 means no group |

### Device-specific interpretation

All four PL values equal selects Blind Object `1` through condition `4703` / rule 9; individual adjacent equalities select Automation Object `7` through 4702/4704/4705 / rule 2. These correspond to different manufacturer shutter roles and timing tables. Rule 2 `M=5..9` lies outside stored firmware M; Object `1` filter 207 references another Object scope. Do not invent precedence for overlapping candidates.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `142` | `1` | `1` | `4703` | `PL2=`PL1`;`PL4`=`PL3`;`PL3`=PL2` | `9` |
| `142` | `1` | `6` | `4151` | No textual predicate stored | `10` |
| `142` | `1` | `7` | `4702` | `PL2=PL1` | `2` |
| `142` | `2` | `6` | `4151` | No textual predicate stored | `10` |
| `142` | `2` | `7` | `4704` | `PL3=PL2` | `2` |
| `142` | `3` | `6` | `4151` | No textual predicate stored | `10` |
| `142` | `3` | `7` | `4705` | `PL4=PL3` | `2` |
| `142` | `4` | `6` | `4151` | No textual predicate stored | `10` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `142` | `1` | `207` | `LOCAL_BUTTON` | `12` = Bistable control; `13` = Monostable control; `14` = Bistable and blades control (entire reusable range retained) | `12` | Funzionalità di pulsante locale ridotta (Local button mode); field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `142` | `1` | `208` | `LOCAL_BUTTON` | `12` = Bistable control; `13` = Monostable control (entire reusable range retained) | `12` | Local button mode shutter (bi or mono) |
| `142` | `6` | `224` | `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `142` | `6` | `225` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `142` | `6` | `226` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `142` | `6` | `227` | `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open (entire reusable range retained) | `0` | Relay state on device reset |
| `142` | `6` | `228` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `142` | `6` | `1857` | `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing (entire reusable range retained) | `0` | Load_control_mode |
| `142` | `7` | `233` | `LOCAL_BUTTON` | `12` = Bistable control; `13` = Monostable control; `14` = Bistable and blades control (entire reusable range retained) | `12` | Funzionalità di pulsante locale ridotta (Local button mode) |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `2` | `M=0` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `60` | `2` |
| `2` | `M=1` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `62` | `2` |
| `2` | `M=2` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `65` | `2` |
| `2` | `M=3` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `70` | `2` |
| `2` | `M=4` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `0` | `2` |
| `2` | `M=5` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `20` | `2` |
| `2` | `M=6` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `10` | `2` |
| `2` | `M=7` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `5` | `2` |
| `2` | `M=8` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `15` | `2` |
| `2` | `M=9` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `30` | `2` |
| `2` | `M=I/O` | `LOCAL_BUTTON` = `13`; `M` = `0`; `STOP_TIME` = `60` | `2` |
| `2` | `M=PUL` | `LOCAL_BUTTON` = `12`; `M` = `15`; `STOP_TIME` = `60` | `2` |
| `2` | `M=SLA` | `LOCAL_BUTTON` = `12`; `M` = `11` | `2` |
| `9` | `M=0` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `20` | `9` |
| `9` | `M=1` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `15` | `9` |
| `9` | `M=2` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `25` | `9` |
| `9` | `M=3` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `60` | `9` |
| `9` | `M=PUL` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `15`; `STOP_TIME` = `20` | `9` |
| `9` | `M=SLA` | `LOCAL_BUTTON` = `12`; `M` = `11` | `9` |
| `10` | `M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `10` |
| `10` | `M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `10` |
| `10` | `M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `10` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 130` and the `F411/4` / `003844` family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | record installed firmware rather than assuming wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | enumerate all four relay positions and resolve conditional Light/Automation/Blind Objects | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the four configured output addresses | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `A`, `M`, `PL1` through `PL4` and the slot conditions that select the active Objects | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The Device can expose [`WHO 1` - Lighting](../../functional/who-1-lighting/) and [`WHO 2` - Automation](../../functional/who-2-automation/).

## Observed behavior and corroboration

No sanitized hardware fingerprint is currently retained.

## Programming

Resolve slot conditions before assigning relay roles. Motor/shutter arrangements require logical interlocking; a four-light arrangement keeps four independent lighting Modules.

| Setting / property | Source-scoped value or behavior | Evidence |
| --- | --- | --- |
| Addressing | Lighting/ordinary automation: physical `A=1..9`, `PL1..PL4=1..9`; rolling-shutter §3 permits `A=0..9`; Suite room `0..10` and point `0..15`. Numeric firmware domains are stored separately. | ST-00000896-EN pp. 2–3 |
| Master / Slave / PUL | `M=0` / SLA / PUL. PUL ignores Room and General controls; this wording alone does not establish Group behavior. | ST-00000896-EN mode tables |
| Lighting OFF delay | Lighting mode lists Master/Slave/PUL; do not assign the two-relay lighting delay matrix to all four outputs. | ST-00000896-EN p. 2 |

| Setting / property | Source-scoped value or behavior | Evidence |
| --- | --- | --- |
| Adjacent motor pair | Equal adjacent PL addresses interlock that pair, including `PL2=PL3`; mixed lighting/motor loads are documented. | ST-00000896-EN pp. 2–3 |
| Rolling-shutter pair stop | `M=0..4` = 1/2/5/10 minutes / until limit stop; `M=5..9` = 20/10/5/15/30 seconds. Suite `1..60` s, `2..10` min or infinity. | ST-00000896-EN p. 3 §3 |
| Two rabbet shutters | All four PL equal; pairs 1/2 internal and 3/4 external shutter. External opens first, internal starts 3 s later; internal closes first, external starts 3 s later. `M=0/1/2/3` = 20/15/25/60 s. | ST-00000896-EN pp. 3 §2 and 4 |
| Wiring / groups | Common relay supply terminal; diagrams specify 10 A thermal-magnetic protection. Groups use Suite; MyHOME Server auto-configures four channels. | ST-00000896-EN pp. 1–4 |

## Source reconciliation

Official documentation corroborates four physical outputs, local control and paired motor use. The Virgin-Object topology explains the shared lighting/automation/blind capability. Older catalogues publish different lamp-load figures; this dossier keeps current values source-scoped.

The historical `AUTOMATISME.pdf` load tables (printed pp. 158 / PDF p. 160) and consumption table (printed p. 160 / PDF p. 162) were examined. They list resistive 6 A / 1400 W, incandescent 2 A / 500 W, fluorescent/electronic 0.3 A / 70 W, ferromagnetic 2 A / 500 VA and motor 2 A / 500 W. The retained Italian export instead labels 2 A resistive and 6 A incandescent in its description, while its structured fields give 40 mA / 460 W / 460 VA. This is a real internal/source discrepancy; the 2021 technical sheet’s 60 mA and explicit pre-14W39 qualification must not be replaced by the export. No production cutoff is inferred for load-rating differences. A specific installed revision must be matched before choosing its ratings.

The 2021 sheet distinguishes the four-contact rabbet-shutter mode from ordinary interlocked rolling-shutter pairs; their timing tables are not competing revisions of one function. Its §3 notation `PL...=PL+1` is qualified by “same configurators”; it denotes matching adjacent positions, not arithmetic address increment. The historic guide lists only `M=0..4` for interlocked motors. The complete 2021 ten-value pair table is preserved without widening the older wildcard catalogue’s M domain. The sheet p. 1 gives `P[mW]=140+400*N+10*(Ic1²+…+IcN²)`; the historical guide gives 3.2 W for single loads and 40/22 mA for single/interlocked use, versus the 2021 2.4 W / 60 mA. The latter’s before-14W39 current qualifier is explicit; other revision boundaries remain unknown.

The retained Classe 300EOS compatibility matrix lists F411/4 from 09W04; 003844 from 10W22; downstream F422 minimum batch `15W25`. Its p.8 excludes Devices using physical configurators. These are Classe 300EOS compatibility boundaries, not universal hardware revisions or guaranteed firmware versions.

## Evidence limits and open work

- All-PL-equal and adjacent-pair topology/conversions are documented above, but catalogue overlapping candidate precedence remains unstated.
- Load ratings/export wording and historical dissipation differences remain source-scoped; no universal revision boundary resolves them.
- No representative hardware trace was inspected. The export’s environmental/DWG links and additional revisions remain unexamined.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [ST-00000896-EN](https://archive.openwebnet-ha.org/sha256/f3/1c/f31ca3b29c75fc69881f4d2ed3744435c10b83bad181a5ce4fb3e55a08509def.pdf)
- [AUTOMATISME.pdf](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)

- `F411_4-ean-product-sheet.pdf`, printed/PDF p. 1: exact `F411/4` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/d5/d5/d5d519a8d1715f0e8b04d20310ff7884c1b4444195e1b9a524f0c4d6fdf3bf0a.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F411_4); SHA-256 `d5d519a8d1715f0e8b04d20310ff7884c1b4444195e1b9a524f0c4d6fdf3bf0a`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0021-0030-2026-10-06.md#own-dev-0023)
