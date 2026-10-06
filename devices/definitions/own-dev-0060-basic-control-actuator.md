# Basic control actuator

## Summary

This compact SCS relay actuator combines a single load output with an input for a conventional normally open pushbutton. Its Basic format fits behind controls or inside junction boxes, and the input supports cyclic, separate ON/OFF and timed lighting commands.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0060` | Project identity |
| Technical description | Basic control actuator | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `3476` | Canonical commercial records |
| Catalogue item | `55` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `105` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Lighting, Actuator, Local control, Flush-mounted | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `3476` | Established identity | canonical commercial record for item `55` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `3476` | `8012199653129` | [Archived original](https://archive.openwebnet-ha.org/sha256/2f/97/2f97fa4647a8fb658e3c02678b1cb92d9566da6dd7ba6cc9a096581a802b334b.pdf), `3476-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ST_00000915_EN` | technical sheet | `ST-00000915-EN`; 2021-04-15 | Printed/PDF pp. 1–2; exact `3476` ratings, input wires, physical/virtual modes, server-channel statement and protection diagram | [Archived original](https://archive.openwebnet-ha.org/sha256/6e/8e/6e8e29681ebb902d1a1b879706213d7057a07ffabc411f2510f53f5b896b8fb6.pdf) | [Official source](https://dar.bticino.com/asset/Documents/ST_00000915_EN.pdf) |
| `3476-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `3476` to EAN-13 relationship at printed/PDF p. 1. Exact-reference identifiers and technical export attributes examined; linked downloads and prices outside scope. | [Archived original](https://archive.openwebnet-ha.org/sha256/2f/97/2f97fa4647a8fb658e3c02678b1cb92d9566da6dd7ba6cc9a096581a802b334b.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-3476) |
| `BTicino-MyHOME-Spanish-technical-sheets.pdf` | Historical Spanish technical-sheet compilation | BT00077-c-ES; undated leaf | Printed p. 619 / PDF p. 50; complete exact `3476` sheet | [Archived original](https://archive.openwebnet-ha.org/sha256/89/4f/894f468c301ea2b7aaec22635d91961e1eedc00136a21e21b774e975c378b4eb.pdf) | [Publisher source](https://www.bticino.es/pdf/FICHA_TECNICA_DOMOTICA_MYHOME_BTICINO.pdf) |
| `ch_de_katalog_wohnbau.pdf` | Historical regional catalogue | No dated imprint established | Printed p. 165 / PDF p. 167; exact `3476` consumption and dimensions | [Archived original](https://archive.openwebnet-ha.org/sha256/9f/e5/9fe511c3ac12d861dff7d8d28ddec3b3612a27e99a804afbed89877c73a6b4ed.pdf) | Publisher URL not retained in manifest |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / current | `27 Vdc` nominal SCS; operating `18..27 Vdc`; `13 mA` | `ST_00000915_EN`, printed/PDF pp. 1–2 |
| Relay limits at 230 Vac | Incandescent/halogen: `460 W` / `2 A`; `LED`/CFL: `40 W`, maximum one lamp; ferromagnetic transformers: 460 VA / `2 A` cosφ 0.5 | `ST_00000915_EN`, printed/PDF pp. 1–2 |
| Installation | Basic module for flush, junction or shutter boxes and trunking; fits behind suitable controls | `ST_00000915_EN`, printed/PDF pp. 1–2 |
| Interface | Configurator socket, `LED`, SCS bus and 0.75 mm² load leads | `ST_00000915_EN`, printed/PDF pp. 1–2 |
| External input / wiring | Normally open conventional pushbutton; blue bus leads, grey/black input leads, two white load-contact leads | `ST_00000915_EN`, printed/PDF pp. 1–2 |
| Circuit protection shown | `10 A` thermal magnetic circuit breaker in the published wiring diagram | `ST_00000915_EN`, printed/PDF pp. 1–2 |
| Regional dimensions | `41 × 41 × 19 mm` | German catalogue, printed p. 165 / PDF p. 167 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `55` | Canonical catalogue |
| Technical item | Basic control actuator | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `105` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `105` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `55` | `3476` | `1` | `5` | `BTicino_Undefined_Basic control actuator` |

All these records are visible, non-dependent and not marked as gateways; `visibility_type` is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `194` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `194` | `1` | `6` Light actuator | Fixed/designated metadata | `690` | `6` | `479` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `194` | Physical configuration | `0` | Canonical firmware/mode association |
| `194` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `194` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `194` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `194` | `A` | `0..9` | `0` | A; Environment |
| `194` | `PL` | `0..9` | `0` | `PL`; Light Point |
| `194` | `M` | `0..8`; `11` = `SLA`; `15` = `PUL`; `9` = `O/I` | `0` | M; Mode (0-8, Pul, Sla, I/O) |
| `194` | `G1` | `0..9` | `0` | `G1`; `G1` - (0-9) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

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

### Device-specific interpretation

Firmware `194` designates one Light actuator Object `6`, with no Virgin, an empty slot condition and no conversion rule. Physical `A/PL` `1..9` excludes firmware defaults 0; virtual `A=0..10` / `PL` `0..15` is separately documented. Firmware `M=9` is labelled O/I, while historical conversion terminology elsewhere uses I/O; no conversion is stored for this item. Relation filter `1898` permits `LOCAL_BUTTON` 60 and 9: 60 has no reusable label, and default 0 is excluded without replacement. Do not silently repair 60 or discard the published cyclic/timed operation. The 2021 physical ON/OFF symbols are absent from the firmware enum. Software `M=16` slave-PUL and load subtypes are reusable/virtual scopes, not separate physical relays.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `194` | `1` | `6` | `4145` | No textual predicate stored | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `194` | `6` | `683` | `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open (entire reusable range retained) | `0` | Per energy management (State on Reset) |
| `194` | `6` | `1868` | `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing (entire reusable range retained) | `0` | Load_control_mode |
| `194` | `6` | `1898` | `LOCAL_BUTTON` | `60`; `9` = `ON` - `OFF` | `0` | Local button modality; reusable default `0` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `55` / `modobj = 105` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`6`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Relay operation | Single relay; basic automation modes exclude functions requiring two interlocked relays | `ST_00000915_EN`, printed/PDF pp. 1–2 |
| PUL / `SLA` | Monostable ON ignores room/general commands; slave receives commands from master with same address | `ST_00000915_EN`, printed/PDF pp. 1–2 |
| Local control | Cyclic ON/OFF, separate ON/OFF, top ON/bottom OFF and timed ON | `ST_00000915_EN`, printed/PDF pp. 1–2 |
| Server scope | 2021 sheet says MyHOME Server automatically configures one channel; no production-week cutoff appears on this sheet | `ST_00000915_EN`, printed/PDF pp. 1–2 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Physical configuration values and reusable Object settings are separate. The 2021 sheet explicitly distinguishes physical MyHOME configurators from MyHOME_Suite.

| Setting | Physical values | Virtual scope |
| --- | --- | --- |
| A / `PL` | `1..9` / `1..9` | Room `0..10`; light point `0..15` |
| Group | G=`0..9` | Groups `1..10` each `0..255` |
| Actuator mode | `M=0` master; `SLA` slave; PUL master monostable ON | Slave-PUL and documented load subtypes require software |
| Input command | `M=0` cyclic; ON; OFF; O/I top ON/bottom OFF | Cyclic, ON, OFF, top/bottom behavior |
| Timed ON | `M=8`: 0.5 s; 7: 30 s; 1: 1 min; 2: 2 min; 3: 3 min; 4: 4 min; 5: 5 min; 6: 15 min | `0..255` h and timed OFF through software |

The input timing belongs to `3476` and is not the delayed-slave OFF operation of `3475`. Follow the exact sheet's coloured leads and protection diagram; a generic Object `LOCAL_BUTTON` value does not substitute for input wiring.

## Source reconciliation

The historical Spanish BT00077-c-ES and exact `ST_00000915_EN` agree on load-class limits, supply/current and Basic mounting. The German catalogue supplies exact dimensions without proving a new firmware revision. The device-label diagram says cosφ 0.6, while the technical load table says cosφ 0.5; these source scopes remain separate. The Spanish sheet uses absent M for cyclic and “0/1” for ON/OFF; the 2021 sheet adds explicit ON and OFF symbols and separately lists `M=0`. Its one-channel server statement does not establish the previous uncited 12W39 cutoff, which has been removed pending verification. The Italian export agrees on 2 A/460 W/460 VA, but does not replace the exact `LED`/CFL restriction.

Catalogue-specific scope and filter irregularities are detailed under [Object configuration surfaces](#object-configuration-surfaces); those relations do not establish additional physical sensors, load interfaces or installed behavior.

## Evidence limits and open work

- The previously mentioned production-week compatibility cutoff has no retained cited supporting row in this dossier; installed/server-version compatibility remains unverified.
- Load-table versus device-label power-factor wording remains source-specific.
- MyHOME_Suite/glossary help and actual relay/input timing or diagnostics are not independently tested.
- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, software payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `3476-ean-product-sheet.pdf`, printed/PDF p. 1: exact `3476` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/2f/97/2f97fa4647a8fb658e3c02678b1cb92d9566da6dd7ba6cc9a096581a802b334b.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-3476); SHA-256 `2f97fa4647a8fb658e3c02678b1cb92d9566da6dd7ba6cc9a096581a802b334b`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0051-0060-2026-10-06.md#own-dev-0060)
