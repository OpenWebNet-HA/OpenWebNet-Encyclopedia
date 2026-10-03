# DIN dimmer 2 x 400 VA

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0074` | Project identity |
| Technical description | DIN dimmer 2 x 400 VA | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `F417U2`, `002622` | Canonical commercial records |
| Catalogue item | `85` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `165` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `2` | Canonical firmware catalogue |
| Categories | Lighting, Dimmer, DIN | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F417U2` | Established identity | canonical commercial record for item `85` |
| Legrand | `002622` | Established identity | canonical commercial record for item `85` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00316-e-EN` | technical sheet | 2014-06-09 | `F417U2` / `002622` dual-channel SCS dimmer characteristics and configuration | [Archived original](https://archive.openwebnet-ha.org/sha256/5d/86/5d86ca223ed7002c2aa078a71213c4dc8851852abc70ebebc7f50635249fdc75.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00316_e_EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `100..240 Vac @ 50/60 Hz` | `MQ00316-e-EN` |
| Outputs | `2 x 1.7 A` | `MQ00316-e-EN` |
| Standby consumption | `0.9 W` | `MQ00316-e-EN` |
| Operating temperature | `-5..45 °C` | `MQ00316-e-EN` |
| Protection | `IP20`; `IK04` | `MQ00316-e-EN` |
| Width | `6 DIN modules` | `MQ00316-e-EN` |
| Resistive / transformer load at 230 V | up to `2 x 400 W` / `2 x 400 VA` | `MQ00316-e-EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `85` | Canonical catalogue |
| Technical item | DIN dimmer 2 x 400 VA | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `165` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `179` | `-1` | `-1` | `-1` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `179` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `610` | `8` | `424` |
| `179` | `2` | `8` Dimmer actuator | Fixed/designated metadata | `611` | `8` | `424` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `179` | Advanced Configuration | supported configuration route for this Device family |
| `179` | Physical configuration | supported configuration route for this Device family |
| `179` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `179` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `179` | `A` | `0..9` | `0` | A; Environment |
| `179` | `PL1` | `0..9` | `0` | PL1; PL1 - (0-9) |
| `179` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |
| `179` | `PL2` | `0..9` | `0` | PL2; PL2 - (0-9) |
| `179` | `G2` | `0..9` | `0` | G2; G2 - (0-9) |
| `179` | `M` | `0..4` | `0` | M; Mode 0-4 |

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
| `179` | `1` | `8` | `4149` | No textual predicate stored | `3` |
| `179` | `2` | `8` | `4149` | No textual predicate stored | `3` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `179` | `8` | `427` | `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Funzionalità di pulsante locale ridotta (Local button mode) |
| `179` | `8` | `428` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Funzionalità di temporizzazione non presente (Hours) |
| `179` | `8` | `429` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Funzionalità di temporizzazione non presente (Minutes) |
| `179` | `8` | `430` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Funzionalità di temporizzazione non presente (Seconds) |
| `179` | `8` | `431` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge (entire reusable range retained) | `0` | Funzionalità di specifica carico pilotato ridotta (Type of load) |
| `179` | `8` | `432` | `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard (entire reusable range retained) | `0` | Definizione ramge voltaggio utile |
| `179` | `8` | `433` | `MIN_LEVEL_ADV` | `1..100` (entire reusable range retained) | `0` | Minimum level advanced |
| `179` | `8` | `434` | `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable (entire reusable range retained) | `0` | enable disable minimum level |
| `179` | `8` | `2174` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

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
| `DIMENSION 1` | corroborate technical identity for catalogue item `85` / `modobj = 165` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`8`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Two-channel DIN SCS dimmer for resistive loads and ferromagnetic/electronic transformers. Each channel is independently addressable; the device supports Lighting Management procedures and MyHOME physical/software configuration.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The publisher sheet directly identifies both `F417U2` and `002622`, strongly reconciling the commercial identities and the canonical two-module topology.

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
