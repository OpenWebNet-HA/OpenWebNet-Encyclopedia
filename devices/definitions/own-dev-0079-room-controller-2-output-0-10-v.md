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

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BTicino General Catalogue product sheet | publisher product sheet | current catalogue export | `BMDI3001` two-output 1-10 V Room Controller; printed p. 1 / PDF p. 1 | [Archived original](https://archive.openwebnet-ha.org/sha256/47/95/47959cd888b93d2c1a5329cc1b5652eb72bbc3851b8b8b5dcec98c77734bf91d.pdf) | [Official source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMDI3001) |

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

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `208` | `-1` | `-1` | `-1` | `3` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `208` | `895, 896` | `8` Dimmer actuator | catalogue firmware/Object relation |
| `208` | `897` | `167` Room controller | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `208` | Advanced Configuration | supported configuration route for this Device family |
| `208` | Physical configuration | supported configuration route for this Device family |
| `208` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `208` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `208` | `A` | catalogue-defined domain | catalogue-scoped | A |
| `208` | `PL1` | catalogue-defined domain | catalogue-scoped | PL1 |
| `208` | `G1` | catalogue-defined domain | catalogue-scoped | G1 |
| `208` | `PL2` | catalogue-defined domain | catalogue-scoped | PL2 |
| `208` | `G2` | catalogue-defined domain | catalogue-scoped | G2 |
| `208` | `M` | catalogue-defined domain | catalogue-scoped | M |

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
| Object filters | `981`, `982`, `983`, `984`, `985`, `986`, `2183` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | none | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

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
