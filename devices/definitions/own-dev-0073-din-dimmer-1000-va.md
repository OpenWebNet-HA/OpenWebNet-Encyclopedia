# DIN dimmer 1000 VA

## Summary

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

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00315-e-EN` | technical sheet | 2014-06-09 | `F416U1` / `002621` 1-channel SCS dimmer characteristics and configuration | [Archived original](https://archive.openwebnet-ha.org/sha256/79/02/7902811439501a406f3d69bf8b95b22705610fe25cc0912a1fc2bc29d157d76e.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00315_e_EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `100..240 Vac @ 50/60 Hz` | `MQ00315-e-EN` |
| Outputs | `1 x 4.3 A` | `MQ00315-e-EN` |
| Standby consumption | `0.3 W` | `MQ00315-e-EN` |
| Operating temperature | `-5..45 °C` | `MQ00315-e-EN` |
| Protection | `IP20`; `IK04` | `MQ00315-e-EN` |
| Width | `6 DIN modules` | `MQ00315-e-EN` |
| Resistive / transformer load at 230 V | up to `1000 W` / `1000 VA` | `MQ00315-e-EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `84` | Canonical catalogue |
| Technical item | DIN dimmer 1000 VA | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `164` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `178` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

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

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `178` | Advanced Configuration | supported configuration route for this Device family |
| `178` | Physical configuration | supported configuration route for this Device family |
| `178` | Virtual Configuration | supported configuration route for this Device family |

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

Single-channel DIN SCS dimmer for resistive loads and ferromagnetic/electronic transformers. It supports Lighting Management procedures as well as physical or MYHOME_Suite configuration in MyHOME installations.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The publisher sheet directly identifies both `F416U1` and `002621`, so the two commercial references are strongly reconciled to the canonical technical item.

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
