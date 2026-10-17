# 4-relay DIN actuator 16 A

## Summary

This six-module DIN actuator switches four independent lighting loads and provides local test buttons. Its 16 A headline applies to the specified load classes at 230 V; it does not support interlocked shutter or curtain motors.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0067` | Project identity |
| Technical description | 4-relay DIN actuator 16 A | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSW1003`, `002602` | Canonical commercial records |
| Catalogue item | `63` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `162` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `4` | Canonical firmware catalogue |
| Categories | Lighting, Actuator, DIN, Lighting Management | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSW1003` | Established identity | canonical commercial record for item `63` |
| Legrand | `002602` | Established identity | canonical commercial record for item `63` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `BMSW1003` | `8012199968186` | [Archived original](https://archive.openwebnet-ha.org/sha256/a2/36/a2365832d5b40f7b9002f1b73c112b75c1a5fe9f8795d0c267437514c4992cbb.pdf), `BMSW1003-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00313-e-EN` | technical sheet | MQ00313-e-EN; 2014-06-09 | Printed/PDF pp. 1–3; exact `BMSW1003` load matrix, supply, malformed standby row, physical/software modes and wiring | [Archived original](https://archive.openwebnet-ha.org/sha256/92/c7/92c7042e277e5f93890757663ad30837292b357744988a96fb0e864d3fd018aa.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00313_e_EN.pdf) |
| `BMSW1003-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Printed/PDF p. 1; exact-reference EAN and complete technical attributes examined; linked technical/DWG downloads and prices not incorporated | [Archived original](https://archive.openwebnet-ha.org/sha256/a2/36/a2365832d5b40f7b9002f1b73c112b75c1a5fe9f8795d0c267437514c4992cbb.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMSW1003) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / operating power | `110..240 Vac`, `50/60 Hz`; `0.8 W` operating power | MQ00313-e-EN, printed/PDF pp. 1–3 |
| Protection / size | IP20; IK04; six DIN modules; terminal and RJ45 connections | MQ00313-e-EN, printed/PDF pp. 1–3 |
| Malformed standby row | Source labels (−5)..(+45) °C as standby power consumption; no numerical standby power is established by this row | MQ00313-e-EN, printed/PDF pp. 1–3 |
| Terminal capacities | Supply `2 × 2.5 mm²`; outputs `2 × 1.5 mm²` and `1 × 2.5 mm²`; `2.5 mm²` wiring | MQ00313-e-EN, printed/PDF pp. 1–3 |
| Output count / load class | Four independent relays, each `16 A` at `230 Vac` for the specified classes | MQ00313-e-EN, printed/PDF pp. 1–3 |
| Incandescent / halogen at 230 / 110 V | `3680 / 1760 W`; `16 A` | MQ00313-e-EN, printed/PDF pp. 1–3 |
| Linear fluorescent at 230 / 110 V | 10 × (`2 × 36 W`) / 5 × (`2 × 36 W`); `4.3 A` | MQ00313-e-EN, printed/PDF pp. 1–3 |
| Transformer at 230 / 110 V | `3680 / 1760 VA`; `16 A` | MQ00313-e-EN, printed/PDF pp. 1–3 |
| CFL at 230 / 110 V | `1150 / 550 VA`; `5 A` | MQ00313-e-EN, printed/PDF pp. 1–3 |
| `LED` at 230 / 110 V | `1 × 500 / 1 × 250 VA`; `2.1 A` | MQ00313-e-EN, printed/PDF pp. 1–3 |
| Current export supply / technology | `100..240 Vac`, `50/60 Hz`; Zero Crossing; four independent outputs, `16 A` at `230 Vac`; IP20 and six DIN modules | `BMSW1003`-ean-product-sheet.pdf, printed/PDF p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `63` | Canonical catalogue |
| Technical item | 4-relay DIN actuator 16 A | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `162` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `162` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `63` | `BMSW1003` | `1` | `5` | `BTicino_Undefined_4 relay DIN actuator 16 A 1` |
| `1574` | `002602` | `2` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `169` | `-1` | `-1` | `-1` | `4` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `169` | `1` | `6` Light actuator | Fixed/designated metadata | `596` | `6` | `414` |
| `169` | `2` | `6` Light actuator | Fixed/designated metadata | `597` | `6` | `414` |
| `169` | `3` | `6` Light actuator | Fixed/designated metadata | `598` | `6` | `414` |
| `169` | `4` | `6` Light actuator | Fixed/designated metadata | `599` | `6` | `414` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `169` | Physical configuration | `0` | Canonical firmware/mode association |
| `169` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `169` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `169` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `169` | `A` | `0..9` | `0` | A; Environment |
| `169` | `PL1` | `0..9` | `0` | `PL1`; `PL1` - (0-9) |
| `169` | `PL2` | `0..9` | `0` | `PL2`; `PL2` - (0-9) |
| `169` | `PL3` | `0..9` | `0` | `PL3`; `PL3` - (0-9) |
| `169` | `PL4` | `0..9` | `0` | `PL4`; `PL4` - (0-9) |
| `169` | `M` | `0..4`; `15` = `PUL` | `0` | M; Mode (0-4, Pul) |

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

Firmware `169` declares four slots of Light actuator 6, without a Virgin. Each empty condition `4147` references rule `1`. `M=1..4` converts to `DELAYED_OFF=60`/120/180/240 seconds, with `LOCAL_BUTTON=0` and Object `M=0`. `M=PUL` maps to 15, while `SLA` maps to 11 without assigning `DELAYED_OFF`. `SLA` and I/O conversion inputs are absent from this firmware M enum (`0..4`/PUL15); do not invent an encoding or infer reachability. Filter `2472` restricts `LOCAL_BUTTON` to 1/15/18/9, excluding reusable default 0 and several rule-1 outputs without a replacement: unresolved filter/conversion conflict. `STATE_RESET`, zero-crossing and timing filters retain their full reusable ranges. Software slave-PUL and wider address/group fields do not prove interlocked motor control, which the sheet excludes.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `169` | `1` | `6` | `4147` | No textual predicate stored | `1` |
| `169` | `2` | `6` | `4147` | No textual predicate stored | `1` |
| `169` | `3` | `6` | `4147` | No textual predicate stored | `1` |
| `169` | `4` | `6` | `4147` | No textual predicate stored | `1` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `169` | `6` | `371` | `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open (entire reusable range retained) | `0` | Per energy management (State on Reset) |
| `169` | `6` | `1860` | `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing (entire reusable range retained) | `0` | Load_control_mode |
| `169` | `6` | `2472` | `LOCAL_BUTTON` | `1` = `ON`/`OFF`; `15` = Pushbutton; `18` = Timed `ON`; `9` = `ON` - `OFF` | `0` | Local button modality; reusable default `0` is outside this subset; filter supplies no replacement default |
| `169` | `6` | `2473` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `169` | `6` | `2474` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `169` | `6` | `2475` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `1` | `M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `1` |
| `1` | `M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `1` |
| `1` | `M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `1` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `63` / `modobj = 162` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`6`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Load boundary | Independent single-function loads; interlocked motor/shutter/curtain operation is excluded | MQ00313-e-EN, printed/PDF pp. 1–3 |
| Delayed slave OFF | Master OFF immediate, matching slave delayed `1..4` min for point-to-point commands | MQ00313-e-EN, printed/PDF pp. 1–3 |
| Software scope | Slave-PUL, load subtypes and local-button behavior require software configuration | MQ00313-e-EN, printed/PDF pp. 1–3 |
| Local operation | Four load buttons/indicators plus learning interface for test and learned arrangements | MQ00313-e-EN, printed/PDF pp. 1–3 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Lighting Management uses Push&Learn/Virtual Configurator, with Plug&Go mentioned as a separate system route. MyHOME uses physical configurators or MyHOME_Suite.

| Setting | Physical sheet | Software scope |
| --- | --- | --- |
| A / `PL1`..`PL4` | `1..9` for each address component | Room `0..10`; light point `0..15` |
| M | 0 master; `SLA` slave; PUL; `1..4` delayed slave OFF `1..4` min | Master or master-PUL delayed OFF `0..255` s; slave-PUL and local-button/load choices |
| Groups | Software required in this sheet | Configured through MyHOME_Suite |
| Software load type | No physical type selector listed | Actuator, lamp, valve, differential reset, fan, irrigation, controlled outlet, lock |
| Software local button | Front buttons exist; software selects behavior | Cyclical, ON/OFF, ON-OFF, pushbutton, timed ON |
| Delayed-off prerequisite | `PL1`≠`PL2`≠`PL3`≠`PL4` as printed | Do not infer independent interlocked outputs |

The p. 3 wiring diagram separates mains supply and the four output contacts; front buttons test single loads. The temperature-like source row remains malformed rather than being treated as a verified standby specification.

## Source reconciliation

The exact e sheet specifies `110..240` Vac while the current export says `100..240` Vac. The sheet’s standby-power row contains temperature units instead of power; `−5..45` °C is preserved as printed but its mislabel prevents a reliable standby-power value. Zero-crossing hardware is supported by the exact current export, not inferred from the reusable Object field. Physical `SLA` is documented but absent from this firmware M enum; software filters also conflict with rule-1 local-button outputs. No release/hardware mapping resolves these differences.

Catalogue-specific scope, selectors, defaults and filter/conversion irregularities are detailed under [Object configuration surfaces](#object-configuration-surfaces). Those software relations do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- Supply lower bound and malformed temperature/standby row need manufacturer clarification; actual standby power remains unknown.
- Exact `002602` physical instructions/EAN and linked DWG/software/commissioning sources are not independently examined.
- Installed zero-crossing mode, delays and actual load compatibility are unobserved.
- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `BMSW1003-ean-product-sheet.pdf`, printed/PDF p. 1: exact `BMSW1003` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/a2/36/a2365832d5b40f7b9002f1b73c112b75c1a5fe9f8795d0c267437514c4992cbb.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMSW1003); SHA-256 `a2365832d5b40f7b9002f1b73c112b75c1a5fe9f8795d0c267437514c4992cbb`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0061-0070-2026-10-06.md#own-dev-0067)
