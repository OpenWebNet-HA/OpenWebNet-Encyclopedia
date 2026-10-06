# DIN dimmer 1000 VA

## Summary

The `F416U1` / `002621` is a six-DIN-module phase-cut dimmer with one independently controlled output. It regulates incandescent and halogen lighting, including compatible transformer loads, and provides local test/dimming buttons and selectable capacitive or inductive load operation.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0073` | Project identity |
| Technical description | DIN dimmer 1000 VA | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `F416U1`, `002621` | Canonical commercial records |
| Catalogue item | `84` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `164` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Lighting, Dimmer, DIN | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F416U1` | Established identity | canonical commercial record for item `84` |
| Legrand | `002621` | Established identity | canonical commercial record for item `84` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F416U1` | `8012199968209` | [Archived original](https://archive.openwebnet-ha.org/sha256/e7/ee/e7eef1088291662598bc466139740521584065aa1f108cab400b16709302ddff.pdf), `F416U1-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00315-e-EN` | technical sheet | 2014-06-09 | Printed/PDF pp. 1–4;complete exact-product ratings,load classes,physical/software setup,local forcing and wiring | [Archived original](https://archive.openwebnet-ha.org/sha256/79/02/7902811439501a406f3d69bf8b95b22705610fe25cc0912a1fc2bc29d157d76e.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00315_e_EN.pdf) |
| `F416U1-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Printed/PDF p. 1;exact-reference EAN and complete technical export attributes examined;linked downloads/prices not incorporated | [Archived original](https://archive.openwebnet-ha.org/sha256/e7/ee/e7eef1088291662598bc466139740521584065aa1f108cab400b16709302ddff.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F416U1) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply/standby | `100..240 Vac`, `50..60 Hz`; `0.3 W` | MQ00315_e_EN.pdf, printed/PDF p. 1 |
| Outputs at 230 V | `1 × 4.3 A`; incandescent/halogen `1000 W`, ferromagnetic/electronic transformers `1000 VA` | MQ00315_e_EN.pdf, printed/PDF p. 1 |
| Loads at 110 V | Incandescent/halogen `600 W`, ferromagnetic/electronic `600 VA`; retain the printed current rating separately | MQ00315_e_EN.pdf, printed/PDF p. 1 |
| Environment/enclosure | `-5..45 °C`; IP20; IK04; six DIN modules | MQ00315_e_EN.pdf, printed/PDF p. 1 |
| Connections | RJ45 bus; input `2 × 2.5 mm²`, output `2 × 1.5 mm²` and `1 × 2.5 mm²`; cable `2.5 mm²` | MQ00315_e_EN.pdf, printed/PDF p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `84` | Canonical catalogue |
| Technical item | DIN dimmer 1000 VA | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `164` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `164` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `84` | `F416U1` | `1` | `5` | `BTicino_Undefined_DIN dimmer 1000 VA` |
| `1603` | `002621` | `2` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `178` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `178` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `609` | `8` | `423` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `178` | Physical configuration | `0` | Canonical firmware/mode association |
| `178` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `178` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `178` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `178` | `A` | `0..9` | `0` | A; Environment |
| `178` | `PL` | `0..9` | `0` | PL; Light Point |
| `178` | `M` | `0..4` | `0` | M; Mode 0-4 |
| `178` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |
| `178` | `G2` | `0..9` | `0` | G2; G2 - (0-9) |
| `178` | `G3` | `0..9` | `0` | G3; G3 - (0-9) |

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

Firmware `178` exposes numeric `M=0..4` only; stored rule `3` also contains I/O, PUL and SLA branches outside that firmware domain. The manufacturer documents SLA/PUL physical configurators, so retain the source discrepancy rather than silently widening the database domain. The empty condition retains rule `3` but does not establish runtime activation. M=`1..4` converts to 60/120/180/240 seconds and master mode; the documented delay concerns the associated slave after the master switches off. Relation filters have no subset rows and retain whole reusable domains even when their descriptions say reduced or absent. Thus TYPE_LOAD values for DALI, fluorescent and LED technology and TYPE_STANDARD do not prove those physical load types or an analogue output on this phase-cut dimmer. `MIN_LEVEL_ADV` default 0 is outside reusable `1..100`, with no replacement default. All fields, groups, filters and conversions remain source-scoped.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `178` | `1` | `8` | `4149` | No textual predicate stored | `3` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `178` | `8` | `411` | `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Funzionalità di pulsante locale ridotta (Local button mode) |
| `178` | `8` | `412` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Funzionalità di temporizzazione non presente (Hours) |
| `178` | `8` | `413` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Funzionalità di temporizzazione non presente (Minutes) |
| `178` | `8` | `414` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Funzionalità di temporizzazione non presente (Seconds) |
| `178` | `8` | `415` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge (entire reusable range retained) | `0` | Funzionalità di specifica carico pilotato ridotta (Type of load) |
| `178` | `8` | `416` | `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard (entire reusable range retained) | `0` | Definizione ramge voltaggio utile |
| `178` | `8` | `417` | `MIN_LEVEL_ADV` | `1..100` (entire reusable range retained) | `0` | Minimum level advanced |
| `178` | `8` | `418` | `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable (entire reusable range retained) | `0` | enable disable minimum level |
| `178` | `8` | `2173` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

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

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `84` / `modobj = 164` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`8`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Addressing | Physical A and PL `1..9`; virtual room `0..10`, point `0..15`; G1/G2/G3 `0..9`; ten virtual groups `0..255` | MQ00315_e_EN.pdf, p. 2 |
| Master/slave/PUL | `M=0` master, SLA same-address slave, PUL monostable ignores room/general; M `1..4` delays corresponding slave OFF by `1..4` min, master OFF immediately; Suite `0..255` s for master/master PUL | MQ00315_e_EN.pdf, p. 2 |
| Local operation and load detection | ON/+ and OFF/− buttons switch/dim; load LED off=OFF, green=`1..100`%, orange=fault; load recognition/forcing cycles capacitive, forced capacitive, inductive, forced inductive | MQ00315_e_EN.pdf, pp. 1, 3 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

MyHOME supports physical or Suite setup; slave with PUL and minimum start brightness require Suite (no numeric minimum range printed here). Lighting Management uses Plug&Go only with a Room Controller association, Push&Learn or Virtual Configurator (p. 2). Do not mix electronic and ferromagnetic transformers on one channel (p. 1). In the pictured forcing procedure, short presses cycle load modes, a 10 s RL/C press confirms, and a short press exits without saving (p. 3). Follow the exact wiring diagram on p. 4; its protective-device example is not a universally specified installation rating.

## Source reconciliation

The technical sheet directly names both `F416U1` / `002621` and is revision e, 9 June 2014. The retained Italian `F416U1` export corroborates `100..240` V, 1000 W/VA and six DIN modules. Physical manufacturer SLA/PUL modes exceed firmware `178`’s numeric M domain; that disagreement is documented rather than corrected by assumption.

Catalogue interpretation is detailed under [Object configuration surfaces](#object-configuration-surfaces); these software records do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- No installed load test, firmware capture or minimum-load rating is retained; no universal LED/CFL compatibility is inferred.
- Suite function help, Virtual Configurator guide, separate Plug&Go/Push&Learn procedures and linked DWG/usage instructions from the Italian export are unexamined. Filter descriptions and their unreduced domains disagree; symbolic conversion reachability and the out-of-domain advanced minimum default remain unresolved.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `F416U1-ean-product-sheet.pdf`, printed/PDF p. 1: exact `F416U1` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/e7/ee/e7eef1088291662598bc466139740521584065aa1f108cab400b16709302ddff.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F416U1); SHA-256 `e7eef1088291662598bc466139740521584065aa1f108cab400b16709302ddff`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0071-0080-2026-10-06.md#own-dev-0073)
