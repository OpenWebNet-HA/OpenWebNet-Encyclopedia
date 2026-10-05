# Multi-application Room Controller

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0077` | Project identity |
| Technical description | Multi-application Room Controller | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSW3003`, `048847` | Canonical commercial records |
| Catalogue item | `89` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `173` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `5` | Canonical firmware catalogue |
| Categories | Lighting Management, Room Controller, Relay actuator, Blind control | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSW3003` | Established identity | canonical commercial record for item `89` |
| Legrand | `048847` | Established identity | canonical commercial record for item `89` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `048847` | `3245060488475` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/ba/24/ba2400e8829a0d7a0d52474c8f86080c33eb6833e1b4c4604e2ec12765da7b81.pdf), `048847-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BTicino General Catalogue product sheet | publisher product sheet | current catalogue export | `BMSW3003` multi-application Room Controller outputs and SCS interfaces; printed p. 1 / PDF p. 1 | [Archived original](https://archive.openwebnet-ha.org/sha256/d1/7c/d17c79d0a00ce5901c44991a992cb0d6fabfe9abbcb36338294eac4e433ef593.pdf) | [Official source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMSW3003) |
| `048847-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `048847` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/ba/24/ba2400e8829a0d7a0d52474c8f86080c33eb6833e1b4c4604e2ec12765da7b81.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue-archives/controleurs-faux-plafond-2-circuits-declairage-1-ouvrant-et-1-contact-cvc-mosaic) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `100..240 Vac @ 50/60 Hz` | BTicino General Catalogue product sheet |
| Outputs | `4` multi-application outputs | BTicino General Catalogue product sheet |
| Automation output class | max `2.1 A @ 230 Vac` | BTicino General Catalogue product sheet |
| `ON`/`OFF` output class | up to `16 A @ 230 Vac` | BTicino General Catalogue product sheet |
| 1-10 V output class | up to `4.3 A @ 230 Vac` | BTicino General Catalogue product sheet |
| Local SCS inputs | `4`; combined supply maximum `200 mA` | BTicino General Catalogue product sheet |
| Protection | `IP20` | BTicino General Catalogue product sheet |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `89` | Canonical catalogue |
| Technical item | Multi-application Room Controller | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `173` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `285` | `-1` | `-1` | `-1` | `5` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `285` | `1` | `29` Automation actuator | Fixed/designated metadata | `2514` | `490` | `1164` |
| `285` | `2` | `16` Actuator for sensors | Fixed/designated metadata | `2515` | `479` | `1165` |
| `285` | `3` | `8` Dimmer actuator | Fixed/designated metadata | `2516` | `8` | `1166` |
| `285` | `4` | `8` Dimmer actuator | Fixed/designated metadata | `2517` | `8` | `1166` |
| `285` | `5` | `167` Room controller | Fixed/designated metadata | `2518` | `167` | `1167` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `285` | Advanced Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `285` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

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


### Object `16` - Actuator for sensors

Catalogue Object key `479` maps to external Object `16`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave | `0` | Modality |
| `STOP_TIME` | `1..180`; `182..255`; `0` = Infinite; `181` = 101 | `0` | Stop time (minutes) |
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


### Object `29` - Automation actuator

Catalogue Object key `490` maps to external Object `29`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality; mode (M,S + PULL) |
| `LOCAL_BUTTON` | `12` = Bistable; `13` = Monostable | `12` | Local button modality |
| `STOP_TIME` | `0` = Infinite; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min | `60` | Stop time |
| `SUBTYPE` | `11` = Actuator; `2` = Shutter; `3` = Curtain; `4` = Gate; `5` = Garage door; `15` = Differential restart | `11` | Type of load |
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
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `285` | `8` | `2195` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `89` / `modobj = 173` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`8`, `167`, `16`, `29`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Multi-application Room Controller whose outputs can serve lighting, automation/blind and 1-10 V control roles depending on configuration. The canonical firmware exposes dedicated controller/automation Objects plus the shared dimmer and Room Controller Objects.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical database's shortened description emphasizes a `16 A` blind-capable application, while the current BTicino product sheet documents a broader four-output multi-application controller. The page preserves the canonical identity while using the publisher description for functional scope; `048847` remains catalogue-derived cross-brand identity.

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

- `048847-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `048847` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/ba/24/ba2400e8829a0d7a0d52474c8f86080c33eb6833e1b4c4604e2ec12765da7b81.pdf); [publisher source](https://www.legrand.fr/pro/catalogue-archives/controleurs-faux-plafond-2-circuits-declairage-1-ouvrant-et-1-contact-cvc-mosaic); SHA-256 `ba2400e8829a0d7a0d52474c8f86080c33eb6833e1b4c4604e2ec12765da7b81`.
