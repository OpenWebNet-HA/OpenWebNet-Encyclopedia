# Basic actuator

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0059` | Project identity |
| Technical description | Basic actuator | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `3475` | Canonical commercial records |
| Catalogue item | `54` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `104` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Lighting, Actuator, Flush-mounted | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `3475` | Established identity | canonical commercial record for item `54` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00076-d-UK` | technical sheet | publisher sheet | `3475` Basic actuator electrical characteristics and configuration | [Archived original](https://archive.openwebnet-ha.org/sha256/f3/88/f3886a858806692c3850f820a4cad509ff86bd2789782539b6dbce67992d5574.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00076-d-UK.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `27 Vdc` from SCS BUS; operating `18..27 Vdc` | `MQ00076-d-UK` |
| Consumption | `13 mA` | `MQ00076-d-UK` |
| Relay/load output | `2 A` nominal; load-dependent limits apply | `MQ00076-d-UK` |
| Size | basic module | `MQ00076-d-UK` |
| Installation | Flush box, junction box, shutter box or trunking | `MQ00076-d-UK` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `54` | Canonical catalogue |
| Technical item | Basic actuator | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `104` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `193` | `-1` | `-1` | `-1` | `1` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `193` | `689` | `6` Light actuator | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `193` | Advanced Configuration | supported configuration route for this Device family |
| `193` | Physical configuration | supported configuration route for this Device family |
| `193` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `193` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `193` | `A` | catalogue-defined domain | catalogue-scoped | A |
| `193` | `PL` | catalogue-defined domain | catalogue-scoped | PL |
| `193` | `M` | catalogue-defined domain | catalogue-scoped | M |
| `193` | `G1` | catalogue-defined domain | catalogue-scoped | G1 |

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
| Object filters | `679`, `680`, `681`, `682`, `1795`, `1867` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | `4147` | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `54` / `modobj = 104` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`6`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Compact SCS relay actuator for basic lighting/load automation. The canonical item exposes one actuator Object and supports advanced, physical and virtual configuration.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The dedicated publisher sheet directly identifies `3475` as the Basic actuator. Current MyHOME Server compatibility documentation also lists it as a one-channel supported device from production batch `12W31`.

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
