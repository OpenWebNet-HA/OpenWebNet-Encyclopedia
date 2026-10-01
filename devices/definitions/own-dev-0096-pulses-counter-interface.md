# Pulses counter interface

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0096` | Project identity |
| Technical description | Pulses counter interface | Canonical catalogue |
| Commercial identities | `3522`, `003554` | Canonical commercial records |
| Catalogue item | `1031` | Canonical catalogue |
| Main catalogue system | New energy saving and load control | Canonical catalogue |
| Item model / `modobj` | `3` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | New energy saving and load control, Energy metering, Interface | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `3522` | Established catalogue identity | canonical commercial record for item `1031` |
| Legrand | `003554` | Established catalogue identity | canonical commercial record for item `1031` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Catalogue product class | `Pulses counter interface` | canonical item description |
| Commercial variants represented | `2` | canonical commercial records |
| Declared Module count | `1` | canonical firmware catalogue |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1031` | Canonical catalogue |
| Technical item | Pulses counter interface | Canonical catalogue |
| Main system | New energy saving and load control | Canonical catalogue |
| Item model / `modobj` | `3` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `200` | `-1` | `-1` | `-1` | `1` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `200` | `758` | `481` Pulse output sensor interface | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `200` | Physical configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `200` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `200` | `A1` | catalogue-defined domain | catalogue-scoped | A1 |
| `200` | `A2` | catalogue-defined domain | catalogue-scoped | A2 |
| `200` | `A3` | catalogue-defined domain | catalogue-scoped | A3 |
| `200` | `G` | catalogue-defined domain | catalogue-scoped | G |
| `200` | `M` | catalogue-defined domain | catalogue-scoped | M |
| `200` | `SM` | catalogue-defined domain | catalogue-scoped | SM |

## Object configuration surfaces

### Object `481` - Pulse output sensor interface

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A123` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Address |
| `G` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | G |
| `M` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `SM` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Divider |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | `732` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | `4158` | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1031` / `modobj = 3` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`481`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The canonical catalogue describes this technical item as Pulses counter interface. Its firmware exposes `1` distinct Object families across the declared Module topology. This definition records those surfaces without treating reusable Object vocabulary as proof of undocumented physical capabilities.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the named configuration-mode boundary. Product-programmed Devices must not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical MyHOME Suite catalogue binds `3522`, `003554` to technical item `1031`. A dedicated retained publisher product document for this exact technical item has not yet been reconciled in the Device source archive, so external documentation discovery remains partial.

## Evidence limits and open work

- Locate and archive dedicated publisher documentation for the exact commercial references where available.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate relation filters and condition-selected topology against MyHOME Suite and controlled hardware observations.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
