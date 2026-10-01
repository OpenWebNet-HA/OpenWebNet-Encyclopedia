# Webserver Audio/Video DIN

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0089` | Project identity |
| Technical description | Webserver Audio/Video DIN | Canonical catalogue |
| Commercial identities | `F453AV` | Canonical commercial records |
| Catalogue item | `207` | Canonical catalogue |
| Main catalogue system | Integration function | Canonical catalogue |
| Item model / `modobj` | `12` | Canonical inventory |
| Firmware definition | `3.0.8`; `3.0.10` | Canonical firmware catalogue |
| Declared Modules | `2` | Canonical firmware catalogue |
| Categories | Integration function, Integration gateway | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F453AV` | Established catalogue identity | canonical commercial record for item `207` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) | Bundled with MyHOME Suite `3.5.38` |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Catalogue product class | `Webserver Audio/Video DIN` | canonical item description |
| Commercial variants represented | `1` | canonical commercial records |
| Declared Module count | `2` | canonical firmware catalogue |
| Programming / connectivity surface | Ethernet | canonical inventory |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `207` | Canonical catalogue |
| Technical item | Webserver Audio/Video DIN | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `12` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | `0` | `8` | `2` | catalogue default | concrete catalogue applicability |
| `2` | `3` | `0` | `10` | `2` | catalogue default | concrete catalogue applicability |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `2` | `621` | `56` Web Server Audio / Video 2 Wires (F453AV) | catalogue firmware/Object relation |
| `2` | `622` | `150` Gateway Open SCS | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `2` | Product Programming | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `2` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `2` | `IS_GATEWAY` | catalogue-defined domain | catalogue-scoped | Gateway |
| `2` | `FW_VER` | catalogue-defined domain | catalogue-scoped | Firmware version |
| `2` | `VCD_PORT` | catalogue-defined domain | catalogue-scoped | Video port |
| `2` | `CMD_PORT` | catalogue-defined domain | catalogue-scoped | Commands port |
| `2` | `LAN_IP_ADDRESS` | catalogue-defined domain | catalogue-scoped | Local IP address |
| `2` | `LAN_IP_ADDR_TYPE` | catalogue-defined domain | catalogue-scoped | Local IP dynamicity |
| `2` | `IP_ADDRESS` | catalogue-defined domain | catalogue-scoped | Public IP address |
| `2` | `CONNECTION_METHOD` | catalogue-defined domain | catalogue-scoped | Public IP dynamicity |
| `2` | `S_VCT` | catalogue-defined domain | catalogue-scoped | Voice box videos |

## Object configuration surfaces

### Object `56` - Web Server Audio / Video 2 Wires (F453AV)

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `IS_GATEWAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Gateway |
| `LAN_IP_ADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local IP address |
| `LAN_IP_ADDR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local IP dynamicity |
| `IP_ADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Public IP address |
| `CONNECTION_METHOD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Public IP dynamicity |
| `CMD_PORT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Commands port |
| `VCD_PORT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Video port |
| `FW_VER` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Firmware version |
| `S_VCT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Voice box videos |
| `SYSADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Univocal code |

### Object `150` - Gateway Open SCS

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local IP address |
| `LAN_IP_ADDR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local IP dynamicity |
| `IS_GATEWAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Gateway |
| `SYSADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Univocal code |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | none | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | none | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `207` / `modobj = 12` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`56`, `150`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The canonical catalogue describes this technical item as Webserver Audio/Video DIN. Its firmware exposes `2` distinct Object families across the declared Module topology. This definition records those surfaces without treating reusable Object vocabulary as proof of undocumented physical capabilities.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the named configuration-mode boundary. Product-programmed Devices must not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical MyHOME Suite catalogue binds `F453AV` to technical item `207`. A dedicated retained publisher product document for this exact technical item has not yet been reconciled in the Device source archive, so external documentation discovery remains partial.

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
