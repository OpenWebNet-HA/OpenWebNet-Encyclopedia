# Ballast DIN dimmer 0-10 V

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0052` | Project identity |
| Technical description | Ballast DIN dimmer 0-10 V | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMDI1001`, `002611` | Canonical commercial records |
| Catalogue item | `47` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `163` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Lighting, Dimmer, DIN actuator | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMDI1001` | Established identity | canonical commercial record for item `47` |
| Legrand | `002611` | Established identity | canonical commercial record for item `47` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00314-f-FR` | technical sheet | 2014-04-18 | `002611` / `BMDI1001` physical characteristics, configuration and wiring | [Archived original](https://archive.openwebnet-ha.org/sha256/8b/36/8b36e76ccaef5d1099d03f0a8fce88d37221f3d3c9c0658f2bba75d4f9fd6c4f.pdf) | [Official source](https://assets.legrand.com/general/legrand-fr/bt/np-ft-gt/mq00314-f-fr.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `100..240 Vac @ 50/60 Hz` | `MQ00314-f-FR` |
| Maximum device consumption | `165 mA` | `MQ00314-f-FR` |
| Output | `1 x 4.3 A` | `MQ00314-f-FR` |
| Maximum connected ballasts | `160` | `MQ00314-f-FR` |
| Protection | `IP20`; `IK04` | `MQ00314-f-FR` |
| Operating temperature | `-5..45 °C` | `MQ00314-f-FR` |
| Width | `6 DIN modules` | `MQ00314-f-FR` |
| Controlled load | `1000 VA @ 240 Vac`; `500 VA @ 110 Vac` | `MQ00314-f-FR` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `47` | Canonical catalogue |
| Technical item | Ballast DIN dimmer 0-10 V | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `163` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `206` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `206` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `664` | `8` | `460` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `206` | Advanced Configuration | supported configuration route for this Device family |
| `206` | Physical configuration | supported configuration route for this Device family |
| `206` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `206` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `206` | `A` | `0..9` | `0` | A; Environment |
| `206` | `PL` | `0..9` | `0` | PL; Light Point |
| `206` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (0-4, Pul, Sla) |
| `206` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |
| `206` | `G2` | `0..9` | `0` | G2; G2 - (0-9) |
| `206` | `G3` | `0..9` | `0` | G3; G3 - (0-9) |

### Published physical selectors absent from the stored firmware field list

| Selector | Physical setting | Published result | Evidence |
| --- | --- | --- | --- |
| `L` | `0` | Minimum output `1 V` | `MQ00314-f-FR`, printed p. 2 / PDF p. 2 |
| `L` | `1` | Minimum output `1.5 V` | Same source |
| `L` | `2` | Minimum output `2 V` | Same source |
| `L` | `3` | Minimum output `0 V` | Same source |
| `L` | `4` | Minimum output `0.5 V` | Same source |
| `TYPE` | `0` | Fluorescent ballast; soft-start accounts for typical `1.5 s` ignition delay | Same source, note 3 |
| `TYPE` | `1` | LED supply; immediate soft-start | Same source, note 3 |

The physical `L` selector establishes support for both 1-10 V and 0-10 V control; the apparent catalogue/product naming difference is therefore not evidence of incompatible standards. `L` and `TYPE` are printed physical positions but are absent from firmware `206`'s stored field list. Do not alias those positions to similarly named reusable Object fields without an established conversion.

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
| `206` | `1` | `8` | `4145` | No textual predicate stored | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `206` | `8` | `582` | `MIN_LEVEL_ADV` | `1..100` (entire reusable range retained) | `0` | Minimum level advanced |
| `206` | `8` | `583` | `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable (entire reusable range retained) | `0` | enable disable minimum level |
| `206` | `8` | `584` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge; `2` = Forced capacitive; `3` = Forced inductive; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI | `0` | Type of Load |
| `206` | `8` | `585` | `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `206` | `8` | `2177` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |
| `206` | `8` | `2494` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `206` | `8` | `2495` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `206` | `8` | `2496` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `47` / `modobj = 163` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`8`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Single-channel SCS DIN dimmer for 0-10 V / 1-10 V ballast-controlled lighting. It supports local actuation, physical configurators and software configuration, with catalogue dimmer Object fields for addressing, operating mode, minimum level, load type, reset state and group membership.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The publisher technical sheet directly identifies `002611` and `BMDI1001` as the same SCS 1-10 V 1 x 4.3 A DIN dimmer. It explicitly documents physical and MYHOME_Suite configuration, including `A`, `PL`, `M`, group addressing, minimum-level and load-type behavior.

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
