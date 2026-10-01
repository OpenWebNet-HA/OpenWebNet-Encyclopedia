# Room Controller - 4 dimming outputs 0-10 V

## Summary

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

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BTicino General Catalogue product sheet | publisher product sheet | current catalogue export | `BMDI3002` four-output 1-10 V Room Controller; printed p. 1 / PDF p. 1 | [Archived original](https://archive.openwebnet-ha.org/sha256/36/26/3626218267f680903b46d190610c3a83879eb18b773d6e54a2ac4c0523a48e64.pdf) | [Official source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMDI3002) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `100..240 Vac @ 50/60 Hz` | BTicino General Catalogue product sheet |
| Dimming outputs | `4` independent 1-10 V outputs, max `4.3 A @ 230 Vac` each | BTicino General Catalogue product sheet |
| Local BUS inputs | `4`; combined supply maximum `200 mA` | BTicino General Catalogue product sheet |
| Trunk SCS input | `1` terminal/RJ45 input | BTicino General Catalogue product sheet |
| Protection | `IP20` | BTicino General Catalogue product sheet |
| Installation | Ceiling / false-ceiling | BTicino General Catalogue product sheet |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `86` | Canonical catalogue |
| Technical item | Room Controller - 4 dimming outputs 0-10 V | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `169` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `209` | `-1` | `-1` | `-1` | `5` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `209` | `900` | `167` Room controller | catalogue firmware/Object relation |
| `209` | `901, 902, 903, 904` | `8` Dimmer actuator | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `209` | Advanced Configuration | supported configuration route for this Device family |
| `209` | Physical configuration | supported configuration route for this Device family |
| `209` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `209` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `209` | `A` | catalogue-defined domain | catalogue-scoped | A |
| `209` | `PL1` | catalogue-defined domain | catalogue-scoped | PL1 |
| `209` | `PL2` | catalogue-defined domain | catalogue-scoped | PL2 |
| `209` | `PL3` | catalogue-defined domain | catalogue-scoped | PL3 |
| `209` | `PL4` | catalogue-defined domain | catalogue-scoped | PL4 |
| `209` | `M` | catalogue-defined domain | catalogue-scoped | M |

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

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | `1005`, `1006`, `1007`, `1008`, `1009`, `1010`, `2184` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | none | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

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

## Source reconciliation

The current BTicino product sheet directly documents `BMDI3002`; Legrand `048843` is retained from the canonical commercial catalogue, so cross-brand reconciliation remains partial.

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
