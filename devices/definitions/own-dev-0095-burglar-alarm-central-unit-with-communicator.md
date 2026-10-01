# Burglar alarm central unit with communicator

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0095` | Project identity |
| Technical description | Burglar alarm central unit with communicator | Canonical catalogue |
| Commercial identities | `067510`, `775795` | Canonical commercial records |
| Catalogue item | `975` | Canonical catalogue |
| Main catalogue system | Burglar alarm system | Canonical catalogue |
| Item model / `modobj` | `201` | Canonical inventory |
| Firmware definition | `6.0.20`; `7.0.17` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Burglar alarm system, Burglar alarm | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand - Celiane | `067510` | Established catalogue identity | canonical commercial record for item `975` |
| Legrand - Galea | `775795` | Established catalogue identity | canonical commercial record for item `975` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) | Bundled with MyHOME Suite `3.5.38` |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Catalogue product class | `Burglar alarm central unit with communicator` | canonical item description |
| Commercial variants represented | `2` | canonical commercial records |
| Declared Module count | `1` | canonical firmware catalogue |
| Programming / connectivity surface | Serial | canonical inventory |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `975` | Canonical catalogue |
| Technical item | Burglar alarm central unit with communicator | Canonical catalogue |
| Main system | Burglar alarm system | Canonical catalogue |
| Item model / `modobj` | `201` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `106` | `6` | `0` | `20` | `1` | non-default | concrete catalogue applicability |
| `107` | `7` | `0` | `17` | `1` | catalogue default | concrete catalogue applicability |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `106` | `2296` | `13` AI Control Unit With Communicator Pstn | catalogue firmware/Object relation |
| `107` | `2295` | `13` AI Control Unit With Communicator Pstn | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `106` | Product Programming | supported configuration route for this Device family |
| `107` | Product Programming | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `106` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `107` | `AID` | catalogue-defined domain | catalogue-scoped | ID |

## Object configuration surfaces

### Object `13` - AI Control Unit With Communicator Pstn

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `NUM_PSTN` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Telephone number PSTN |
| `FW_VER` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Firmware version |
| `IS_GATEWAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Gateway |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | none | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | none | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `975` / `modobj = 201` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`13`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The canonical catalogue describes this technical item as Burglar alarm central unit with communicator. Its firmware exposes `1` distinct Object families across the declared Module topology. This definition records those surfaces without treating reusable Object vocabulary as proof of undocumented physical capabilities.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the named configuration-mode boundary. Product-programmed Devices must not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical MyHOME Suite catalogue binds `067510`, `775795` to technical item `975`. A dedicated retained publisher product document for this exact technical item has not yet been reconciled in the Device source archive, so external documentation discovery remains partial.

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
