# Room Controller - 2 dimming outputs 0-10 V

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0079` | Project identity |
| Technical description | Room Controller - 2 dimming outputs 0-10 V | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMDI3001`, `048842` | Canonical commercial records |
| Catalogue item | `94` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `168` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `3` | Canonical firmware catalogue |
| Categories | Lighting Management, Room Controller, 0-10 V dimmer | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMDI3001` | Established identity | canonical commercial record for item `94` |
| Legrand | `048842` | Established identity | canonical commercial record for item `94` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `048842` | `3245060488420` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/9d/13/9d13d4580b63376b05737629165b360c5fa6d874d0a7e08815b210599bea706f.pdf), `048842-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BTicino General Catalogue product sheet | publisher product sheet | current catalogue export | `BMDI3001` two-output 1-10 V Room Controller; printed p. 1 / PDF p. 1 | [Archived original](https://archive.openwebnet-ha.org/sha256/47/95/47959cd888b93d2c1a5329cc1b5652eb72bbc3851b8b8b5dcec98c77734bf91d.pdf) | [Official source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMDI3001) |
| `048842-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `048842` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/9d/13/9d13d4580b63376b05737629165b360c5fa6d874d0a7e08815b210599bea706f.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue-archives/controleurs-faux-plafond-pour-2-circuits-mosaic-a-fonction-variation-ballast-1v-a-10v-avec-2-sorties-1000va-maximum) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `100..240 Vac @ 50/60 Hz` | BTicino General Catalogue product sheet |
| Dimming outputs | `2` independent 1-10 V outputs, max `4.3 A @ 230 Vac` each | BTicino General Catalogue product sheet |
| Local BUS inputs | `2`; combined supply maximum `200 mA` | BTicino General Catalogue product sheet |
| Trunk SCS input | `1` terminal/RJ45 input | BTicino General Catalogue product sheet |
| Protection | `IP20` | BTicino General Catalogue product sheet |
| Installation | Ceiling / false-ceiling | BTicino General Catalogue product sheet |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `94` | Canonical catalogue |
| Technical item | Room Controller - 2 dimming outputs 0-10 V | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `168` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `208` | `-1` | `-1` | `-1` | `3` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `208` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `895` | `8` | `561` |
| `208` | `2` | `8` Dimmer actuator | Fixed/designated metadata | `896` | `8` | `561` |
| `208` | `3` | `167` Room controller | Fixed/designated metadata | `897` | `167` | `562` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `208` | Advanced Configuration | supported configuration route for this Device family |
| `208` | Physical configuration | supported configuration route for this Device family |
| `208` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `208` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `208` | `A` | `0..9` | `0` | A; Environment |
| `208` | `PL1` | `0..9` | `0` | PL1; PL1 - (0-9) |
| `208` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |
| `208` | `PL2` | `0..9` | `0` | PL2; PL2 - (0-9) |
| `208` | `G2` | `0..9` | `0` | G2; G2 - (0-9) |
| `208` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (0-4, Pul, Sla) |

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

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `208` | `8` | `981` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `208` | `8` | `982` | `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `208` | `8` | `983` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `208` | `8` | `984` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `208` | `8` | `985` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge (entire reusable range retained) | `0` | Type of Load |
| `208` | `8` | `986` | `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard (entire reusable range retained) | `0` | Voltage standard |
| `208` | `8` | `2183` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `94` / `modobj = 168` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`8`, `167`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Two-output zero-crossing Room Controller for 1-10 V lighting loads with two local SCS sensor/control inputs and one SCS trunk connection. The canonical topology exposes two dimmer Modules plus the Room Controller context.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The current BTicino product sheet directly documents `BMDI3001`; Legrand `048842` is corroborated by the canonical catalogue and current Legrand product information, but the archived direct sheet is BTicino-branded.

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

- `048842-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `048842` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/9d/13/9d13d4580b63376b05737629165b360c5fa6d874d0a7e08815b210599bea706f.pdf); [publisher source](https://www.legrand.fr/pro/catalogue-archives/controleurs-faux-plafond-pour-2-circuits-mosaic-a-fonction-variation-ballast-1v-a-10v-avec-2-sorties-1000va-maximum); SHA-256 `9d13d4580b63376b05737629165b360c5fa6d874d0a7e08815b210599bea706f`.
