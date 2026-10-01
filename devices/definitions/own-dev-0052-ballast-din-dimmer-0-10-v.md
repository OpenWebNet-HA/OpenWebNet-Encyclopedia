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
| `MQ00314-f-FR` | technical sheet | 2014-04-18 | `002611` / `BMDI1001` physical characteristics, configuration and wiring | [Archived original](../../sources/devices/documents/device-doc-ballast-dimmer-mq00314-f-fr/MQ00314-f-FR.pdf) | [Official source](https://assets.legrand.com/general/legrand-fr/bt/np-ft-gt/mq00314-f-fr.pdf) |

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

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `206` | `-1` | `-1` | `-1` | `1` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `206` | `664` | `8` Dimmer actuator | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `206` | Advanced Configuration | supported configuration route for this Device family |
| `206` | Physical configuration | supported configuration route for this Device family |
| `206` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `206` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `206` | `A` | catalogue-defined domain | catalogue-scoped | A |
| `206` | `PL` | catalogue-defined domain | catalogue-scoped | PL |
| `206` | `M` | catalogue-defined domain | catalogue-scoped | M |
| `206` | `G1` | catalogue-defined domain | catalogue-scoped | G1 |
| `206` | `G2` | catalogue-defined domain | catalogue-scoped | G2 |
| `206` | `G3` | catalogue-defined domain | catalogue-scoped | G3 |

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

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | `582`, `583`, `584`, `585`, `2177`, `2494`, `2495`, `2496` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | `4145` | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

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
