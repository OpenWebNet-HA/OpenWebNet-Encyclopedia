# 4-relay DIN actuator 16 A

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0067` | Project identity |
| Technical description | 4-relay DIN actuator 16 A | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSW1003`, `002602` | Canonical commercial records |
| Catalogue item | `63` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `162` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `4` | Canonical firmware catalogue |
| Categories | Lighting, Actuator, DIN, Lighting Management | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSW1003` | Established identity | canonical commercial record for item `63` |
| Legrand | `002602` | Established identity | canonical commercial record for item `63` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00313-e-EN` | technical sheet | 2014-06-09 | `BMSW1003` / `002602` four-relay actuator characteristics and configuration | [Archived original](https://archive.openwebnet-ha.org/sha256/92/c7/92c7042e277e5f93890757663ad30837292b357744988a96fb0e864d3fd018aa.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00313_e_EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `110..240 Vac @ 50/60 Hz` | `MQ00313-e-EN` |
| Outputs | `4 x 16 A` | `MQ00313-e-EN` |
| Operating consumption | `0.8 W` | `MQ00313-e-EN` |
| Protection | `IP20` | `MQ00313-e-EN` |
| Impact resistance | `IK04` | `MQ00313-e-EN` |
| Width | `6 DIN modules` | `MQ00313-e-EN` |
| BUS connection | RJ45 | `MQ00313-e-EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `63` | Canonical catalogue |
| Technical item | 4-relay DIN actuator 16 A | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `162` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `169` | `-1` | `-1` | `-1` | `4` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `169` | `596, 597, 598, 599` | `6` Light actuator | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `169` | Advanced Configuration | supported configuration route for this Device family |
| `169` | Physical configuration | supported configuration route for this Device family |
| `169` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `169` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `169` | `A` | catalogue-defined domain | catalogue-scoped | A |
| `169` | `PL1` | catalogue-defined domain | catalogue-scoped | PL1 |
| `169` | `PL2` | catalogue-defined domain | catalogue-scoped | PL2 |
| `169` | `PL3` | catalogue-defined domain | catalogue-scoped | PL3 |
| `169` | `PL4` | catalogue-defined domain | catalogue-scoped | PL4 |
| `169` | `M` | catalogue-defined domain | catalogue-scoped | M |

## Object configuration surfaces

### Object `6` - Light actuator

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |
| `M` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `LOCAL_BUTTON` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local button modality |
| `DELAYED_OFF` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Delayed OFF for Slave (s) |
| `STATE_RESET` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Relay state on device reset |
| `LOAD_CONTROL_MODE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Load control mode |
| `HOURS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Hours |
| `MINUTES` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Minutes |
| `SECONDS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Seconds |
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
| Object filters | `371`, `1860`, `2472`, `2473`, `2474`, `2475` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | `4147` | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `63` / `modobj = 162` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`6`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Four-independent-relay DIN actuator for Lighting Management and MyHOME lighting loads. The publisher explicitly excludes relay interlocking, so it must not be modeled as a rolling-shutter motor actuator despite having four channels.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The publisher sheet directly identifies both `BMSW1003` and `002602`, giving strong commercial reconciliation as well as configuration and load data.

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
