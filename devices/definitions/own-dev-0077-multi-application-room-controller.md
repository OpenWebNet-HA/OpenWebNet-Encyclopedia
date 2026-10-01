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

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BTicino General Catalogue product sheet | publisher product sheet | current catalogue export | `BMSW3003` multi-application Room Controller outputs and SCS interfaces; printed p. 1 / PDF p. 1 | [Archived original](https://archive.openwebnet-ha.org/sha256/d1/7c/d17c79d0a00ce5901c44991a992cb0d6fabfe9abbcb36338294eac4e433ef593.pdf) | [Official source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMSW3003) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `100..240 Vac @ 50/60 Hz` | BTicino General Catalogue product sheet |
| Outputs | `4` multi-application outputs | BTicino General Catalogue product sheet |
| Automation output class | max `2.1 A @ 230 Vac` | BTicino General Catalogue product sheet |
| ON/OFF output class | up to `16 A @ 230 Vac` | BTicino General Catalogue product sheet |
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

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `285` | `-1` | `-1` | `-1` | `5` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `285` | `2514` | `490` Automation actuator | catalogue firmware/Object relation |
| `285` | `2515` | `479` Actuator for sensors | catalogue firmware/Object relation |
| `285` | `2516, 2517` | `8` Dimmer actuator | catalogue firmware/Object relation |
| `285` | `2518` | `167` Room controller | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `285` | Advanced Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `285` | `AID` | catalogue-defined domain | catalogue-scoped | ID |

## Object configuration surfaces

### Object `8` - Dimmer actuator

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |
| `M` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `LOCAL_BUTTON` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local button modality |
| `DELAYED_OFF` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Delayed OFF for Slave (s) |
| `STATE_SAVING_ON_RESET` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | State saving on reset |
| `HOURS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Hours |
| `MINUTES` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Minutes |
| `SECONDS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Seconds |
| `MIN_LEVEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Minimum level |
| `TYPE_LOAD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type of load |
| `TYPE_STANDARD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Voltage standard |
| `MIN_LEVEL_ADV` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Minimum level advanced |
| `MIN_AUTO` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Enable / Disable minimum level |
| `G1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 1 |
| `G2` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 2 |
| `G3` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 3 |
| `G4` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 4 |
| `G5` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 5 |
| `G6` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 6 |
| `G7` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 7 |
| `G8` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 8 |
| `G9` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 9 |
| `G10` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 10 |

### Object `167` - Room controller

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `MODE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |

### Object `479` - Actuator for sensors

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |
| `M` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `STOP_TIME` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Stop time (minutes) |
| `G1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 1 |
| `G2` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 2 |
| `G3` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 3 |
| `G4` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 4 |
| `G5` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 5 |
| `G6` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 6 |
| `G7` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 7 |
| `G8` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 8 |
| `G9` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 9 |
| `G10` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 10 |

### Object `490` - Automation actuator

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |
| `M` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `LOCAL_BUTTON` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local button modality |
| `STOP_TIME` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Stop time |
| `SUBTYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type of load |
| `G1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 1 |
| `G2` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 2 |
| `G3` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 3 |
| `G4` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 4 |
| `G5` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 5 |
| `G6` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 6 |
| `G7` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 7 |
| `G8` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 8 |
| `G9` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 9 |
| `G10` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 10 |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | `2195` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | none | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `89` / `modobj = 173` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`8`, `167`, `479`, `490`) | [Modules](../../diagnostics/dim30-modules.md) |
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
