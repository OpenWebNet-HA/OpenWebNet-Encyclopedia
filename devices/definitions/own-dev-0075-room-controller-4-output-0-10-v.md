# Room Controller - 4 dimming outputs 0-10 V

## Summary

This Room Controller provides four independent 1-10 V dimming outputs for compatible lighting loads. Four local SCS inputs connect room sensors and controls, while a separate trunk connection links the controller to the wider installation.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0075` | Project identity |
| Technical description | Room Controller - 4 dimming outputs 0-10 V | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMDI3002`, `048843` | Canonical commercial records |
| Catalogue item | `86` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `169` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `5` | Canonical firmware catalogue |
| Categories | Lighting Management, Room Controller, 0-10 V dimmer | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMDI3002` | Established identity | canonical commercial record for item `86` |
| Legrand | `048843` | Established identity | canonical commercial record for item `86` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `048843` | `3245060488437` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/0e/6a/0e6ac88b94c5057fabab84f9f4d5fd816a075cb76afa669aef633367f3077ca0.pdf), `048843-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BTicino General Catalogue product sheet | publisher product sheet | current catalogue export | `BMDI3002` four-output 1-10 V Room Controller; printed p. 1 / PDF p. 1 | [Archived original](https://archive.openwebnet-ha.org/sha256/36/26/3626218267f680903b46d190610c3a83879eb18b773d6e54a2ac4c0523a48e64.pdf) | [Official source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMDI3002) |
| `048843-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `048843` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/0e/6a/0e6ac88b94c5057fabab84f9f4d5fd816a075cb76afa669aef633367f3077ca0.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue-archives/controleurs-faux-plafond-pour-4-circuits-mosaic-a-fonction-variation-ballast-1v-a-10v-ou-on-et-off-avec-4-sorties-1000va) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `100..240 Vac @ 50/60 Hz` | BTicino General Catalogue product sheet |
| Dimming outputs | `4` independent 1-10 V outputs, max `4.3 A @ 230 Vac` each | BTicino General Catalogue product sheet |
| Local BUS inputs | `4`; combined supply maximum `200 mA` | BTicino General Catalogue product sheet |
| Trunk SCS input | `1` terminal/RJ45 input | BTicino General Catalogue product sheet |
| Protection | `IP20` | BTicino General Catalogue product sheet |
| Installation | Ceiling / false-ceiling | BTicino General Catalogue product sheet |
| Direct local controls | Load-control buttons and Push&Learn button | Retained `BMDI3002` product sheet, printed p. 1 / PDF p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `86` | Canonical catalogue |
| Technical item | Room Controller - 4 dimming outputs 0-10 V | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `169` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `209` | `-1` | `-1` | `-1` | `5` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `209` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `901` | `8` | `566` |
| `209` | `2` | `8` Dimmer actuator | Fixed/designated metadata | `902` | `8` | `566` |
| `209` | `3` | `8` Dimmer actuator | Fixed/designated metadata | `903` | `8` | `566` |
| `209` | `4` | `8` Dimmer actuator | Fixed/designated metadata | `904` | `8` | `566` |
| `209` | `5` | `167` Room controller | Fixed/designated metadata | `900` | `167` | `565` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `209` | Advanced Configuration | supported configuration route for this Device family |
| `209` | Physical configuration | supported configuration route for this Device family |
| `209` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `209` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `209` | `A` | `0..9` | `0` | A; Environment |
| `209` | `PL1` | `0..9` | `0` | PL1; PL1 - (0-9) |
| `209` | `PL2` | `0..9` | `0` | PL2; PL2 - (0-9) |
| `209` | `PL3` | `0..9` | `0` | PL3; PL3 - (0-9) |
| `209` | `PL4` | `0..9` | `0` | PL4; PL4 - (0-9) |
| `209` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (0-4, Pul, Sla) |

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
| `209` | `8` | `1005` | `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `209` | `8` | `1006` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `209` | `8` | `1007` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `209` | `8` | `1008` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `209` | `8` | `1009` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge (entire reusable range retained) | `0` | Type of Load |
| `209` | `8` | `1010` | `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard (entire reusable range retained) | `0` | Voltage standard |
| `209` | `8` | `2184` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `86` / `modobj = 169` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`8`, `167`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Four-output zero-crossing Room Controller for 1-10 V lighting loads, with four local SCS sensor/control inputs and one SCS trunk connection. The catalogue models four dimmer Modules plus the Room Controller context.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

The retained `BMDI3002` sheet explicitly documents automatic Plug&Go configuration, a Push&Learn button and direct-load buttons. These product procedures supplement the catalogue configuration-mode rows; they are not additional firmware mode identifiers.

## Source reconciliation

The current BTicino product sheet directly documents `BMDI3002`; Legrand `048843` is retained from the canonical commercial catalogue, so cross-brand reconciliation remains partial.

The catalogue names this item “0-10 V”, while the retained publisher sheet specifies four 1-10 V outputs. Preserve both labels with their evidence scope; do not infer 0 V output capability solely from the catalogue title. The same sheet establishes automatic Plug&Go, Push&Learn and direct local controls.

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

- `048843-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `048843` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/0e/6a/0e6ac88b94c5057fabab84f9f4d5fd816a075cb76afa669aef633367f3077ca0.pdf); [publisher source](https://www.legrand.fr/pro/catalogue-archives/controleurs-faux-plafond-pour-4-circuits-mosaic-a-fonction-variation-ballast-1v-a-10v-ou-on-et-off-avec-4-sorties-1000va); SHA-256 `0e6ac88b94c5057fabab84f9f4d5fd816a075cb76afa669aef633367f3077ca0`.
