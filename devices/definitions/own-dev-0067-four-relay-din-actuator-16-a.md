# 4-relay DIN actuator 16 A

## Summary

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
| `MQ00313-e-EN` | technical sheet | 2014-06-09 | `BMSW1003` / `002602` four-relay actuator characteristics and configuration | [Archived original](https://archive.openwebnet-ha.org/sha256/92/c7/92c7042e277e5f93890757663ad30837292b357744988a96fb0e864d3fd018aa.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00313_e_EN.pdf) |
| `BMSW1003-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `BMSW1003` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/a2/36/a2365832d5b40f7b9002f1b73c112b75c1a5fe9f8795d0c267437514c4992cbb.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMSW1003) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `110..240 Vac @ 50/60 Hz` | `MQ00313-e-EN` |
| Outputs | `4 x 16 A` | `MQ00313-e-EN` |
| Operating consumption | `0.8 W` | `MQ00313-e-EN` |
| Protection | `IP20` | `MQ00313-e-EN` |
| Impact resistance | `IK04` | `MQ00313-e-EN` |
| Width | `6 DIN modules` | `MQ00313-e-EN` |
| BUS connection | RJ45 | `MQ00313-e-EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `63` | Canonical catalogue |
| Technical item | 4-relay DIN actuator 16 A | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `162` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `169` | `-1` | `-1` | `-1` | `4` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

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

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `169` | Advanced Configuration | supported configuration route for this Device family |
| `169` | Physical configuration | supported configuration route for this Device family |
| `169` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `169` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `169` | `A` | `0..9` | `0` | A; Environment |
| `169` | `PL1` | `0..9` | `0` | PL1; PL1 - (0-9) |
| `169` | `PL2` | `0..9` | `0` | PL2; PL2 - (0-9) |
| `169` | `PL3` | `0..9` | `0` | PL3; PL3 - (0-9) |
| `169` | `PL4` | `0..9` | `0` | PL4; PL4 - (0-9) |
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

Four-independent-relay DIN actuator for Lighting Management and MyHOME lighting loads. The publisher explicitly excludes relay interlocking, so it must not be modeled as a rolling-shutter motor actuator despite having four channels.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The publisher sheet directly identifies both `BMSW1003` and `002602`, giving strong commercial reconciliation as well as configuration and load data.

## Evidence limits and open work

- Archive the identified publisher documents locally where licensing and repository policy allow.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate relation filters and condition-selected topology against MyHOME Suite and controlled hardware observations.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `BMSW1003-ean-product-sheet.pdf`, printed/PDF p. 1: exact `BMSW1003` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/a2/36/a2365832d5b40f7b9002f1b73c112b75c1a5fe9f8795d0c267437514c4992cbb.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMSW1003); SHA-256 `a2365832d5b40f7b9002f1b73c112b75c1a5fe9f8795d0c267437514c4992cbb`.
