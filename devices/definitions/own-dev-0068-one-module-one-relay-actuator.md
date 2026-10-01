# 1-module 1-relay actuator

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0068` | Project identity |
| Technical description | 1-module 1-relay actuator | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `L/N/NT4675` | Canonical commercial records |
| Catalogue item | `66` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `100` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Lighting, Actuator, Flush-mounted | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - LivingLight | `L/N/NT4675` | Established identity | canonical commercial record for item `66` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `AUTOMATISME.pdf` | technical/system guide | publisher guide | `L/N/NT4675` mini 1-relay actuator installation and operating modes | [Archived original](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Form factor | `1` Living International/Light module | `AUTOMATISME.pdf` |
| Outputs | `1` relay | `AUTOMATISME.pdf` |
| Load leads | `0.75 mm²` conductors | `AUTOMATISME.pdf` |
| Local interface | status indicator + local micro-pushbutton | `AUTOMATISME.pdf` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `66` | Canonical catalogue |
| Technical item | 1-module 1-relay actuator | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `100` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `195` | `-1` | `-1` | `-1` | `1` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `195` | `699` | `6` Light actuator | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `195` | Advanced Configuration | supported configuration route for this Device family |
| `195` | Physical configuration | supported configuration route for this Device family |
| `195` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `195` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `195` | `A` | catalogue-defined domain | catalogue-scoped | A |
| `195` | `PL` | catalogue-defined domain | catalogue-scoped | PL |
| `195` | `M` | catalogue-defined domain | catalogue-scoped | M |
| `195` | `G1` | catalogue-defined domain | catalogue-scoped | G1 |
| `195` | `G2` | catalogue-defined domain | catalogue-scoped | G2 |
| `195` | `G3` | catalogue-defined domain | catalogue-scoped | G3 |

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
| Object filters | `690`, `1869` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | `4145` | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `66` / `modobj = 100` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`6`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Compact one-relay actuator intended for installation in junction boxes, shutter boxes, trunking or modular boxes. It provides local load actuation for test/scenario definition and supports the standard single-relay actuator modes except interlocked-relay functions.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical catalogue contains the combined `L/N/NT4675` reference under the LivingLight catalogue family. The publisher automation guide uses the same combined reference and directly documents its one-module, one-relay form.

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
