# Shutter flush mounted actuator

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0098` | Project identity |
| Technical description | Shutter flush mounted actuator | Canonical catalogue |
| Commercial identities | `H4671/2`, `L4671/2`, `AM5851/2` | Canonical commercial records |
| Catalogue item | `1122` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `102` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `2` | Canonical firmware catalogue |
| Categories | Automation, Actuator, Shutter control | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4671/2` | Established catalogue identity | canonical commercial record for item `1122` |
| BTicino | `L4671/2` | Established catalogue identity | canonical commercial record for item `1122` |
| BTicino - Matix | `AM5851/2` | Established catalogue identity | canonical commercial record for item `1122` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Catalogue product class | `Shutter flush mounted actuator` | canonical item description |
| Commercial variants represented | `3` | canonical commercial records |
| Declared Module count | `2` | canonical firmware catalogue |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1122` | Canonical catalogue |
| Technical item | Shutter flush mounted actuator | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `102` | Canonical inventory |
| Commercial records | `3` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `188` | `-1` | `-1` | `-1` | `2` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `188` | `643` | `7` Automation actuator | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `188` | Physical configuration | supported configuration route for this Device family |
| `188` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `188` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `188` | `A` | catalogue-defined domain | catalogue-scoped | A |
| `188` | `PL` | catalogue-defined domain | catalogue-scoped | PL |
| `188` | `M` | catalogue-defined domain | catalogue-scoped | M |
| `188` | `G1` | catalogue-defined domain | catalogue-scoped | G1 |

## Object configuration surfaces

### Object `7` - Automation actuator

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
| Object filters | none | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | `4148` | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1122` / `modobj = 102` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`7`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The canonical catalogue describes this technical item as Shutter flush mounted actuator. Its firmware exposes `1` distinct Object families across the declared Module topology. This definition records those surfaces without treating reusable Object vocabulary as proof of undocumented physical capabilities.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the named configuration-mode boundary. Product-programmed Devices must not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical MyHOME Suite catalogue binds `H4671/2`, `L4671/2`, `AM5851/2` to technical item `1122`. A dedicated retained publisher product document for this exact technical item has not yet been reconciled in the Device source archive, so external documentation discovery remains partial.

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
