# Stereo control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0100` | Project identity |
| Technical description | Stereo control | Canonical catalogue |
| Commercial identities | `L4561N`, `003586` | Canonical commercial records |
| Catalogue item | `1130` | Canonical catalogue |
| Main catalogue system | Sound system | Canonical catalogue |
| Item model / `modobj` | `6` | Canonical inventory |
| Firmware definition | `4.0.6` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Sound system | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `L4561N` | Established catalogue identity | canonical commercial record for item `1130` |
| Legrand | `003586` | Established catalogue identity | canonical commercial record for item `1130` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) | Bundled with MyHOME Suite `3.5.38` |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Catalogue product class | `Stereo control` | canonical item description |
| Commercial variants represented | `2` | canonical commercial records |
| Declared Module count | `1` | canonical firmware catalogue |
| Programming / connectivity surface | Serial | canonical inventory |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1130` | Canonical catalogue |
| Technical item | Stereo control | Canonical catalogue |
| Main system | Sound system | Canonical catalogue |
| Item model / `modobj` | `6` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `65` | `4` | `0` | `6` | `1` | catalogue default | concrete catalogue applicability |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `65` | `2298` | `161` Phonic source | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `65` | Product Programming | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `65` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `65` | `S1` | catalogue-defined domain | catalogue-scoped | S1 |
| `65` | `M1` | catalogue-defined domain | catalogue-scoped | M1 |
| `65` | `M2` | catalogue-defined domain | catalogue-scoped | M2 |

## Object configuration surfaces

### Object `161` - Phonic source

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `RECEIVE_MODE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Set the reception mode of the radio signal |
| `NUM_STATION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Set the number of station presets. 0 or 1for 5 station, 2 for 10 station and 3 for 15 station |
| `S` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `SUB_SOURCE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Max subsource |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | none | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | none | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1130` / `modobj = 6` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`161`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The canonical catalogue describes this technical item as Stereo control. Its firmware exposes `1` distinct Object families across the declared Module topology. This definition records those surfaces without treating reusable Object vocabulary as proof of undocumented physical capabilities.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the named configuration-mode boundary. Product-programmed Devices must not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical MyHOME Suite catalogue binds `L4561N`, `003586` to technical item `1130`. A dedicated retained publisher product document for this exact technical item has not yet been reconciled in the Device source archive, so external documentation discovery remains partial.

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
