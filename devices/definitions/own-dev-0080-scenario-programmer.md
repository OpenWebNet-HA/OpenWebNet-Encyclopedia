# Scenario programmer

## Summary

The MH200 is a programmable scenario controller that coordinates MyHOME actions in response to times or events. Projects created with TiMH200 are transferred over Ethernet and can address automation devices across documented SCS/SCS-separated installations.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0080` | Project identity |
| Technical description | Scenario programmer | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `MH200` | Canonical commercial records |
| Catalogue item | `98` | Canonical catalogue |
| Main catalogue system | Integration function | Canonical catalogue |
| Item model / `modobj` | `4` | Canonical inventory |
| Firmware definition | `2.0.0` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Scenarios, Integration, Ethernet programmer | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `MH200` | Established identity | canonical commercial record for item `98` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `TiMH200_FR` | software/configuration manual | version 2.03; 06/07-01 PC | Configuration, Ethernet transfer, scenario editing and firmware update for `MH200` | [Archived original](https://archive.openwebnet-ha.org/sha256/00/64/00649f4d577863eab8a6366529468044a7fdce4d2b868cdcd09b8f4f634a01ea.pdf) | [Official source](https://www.bticino.be/sites/default/files/Service-en-support/software-en-schemas2/Audio-Video/MH200/Version%202_1_00/TiMH200_FR.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Network interface | Ethernet LAN | `TiMH200_FR`, printed p. 8 / PDF p. 8 |
| Project transfer | Ethernet crossover/direct LAN or remote IP connection | `TiMH200_FR`, printed p. 8 / PDF p. 8 |
| Automation connection context | MyHOME Automation BUS | `TiMH200_FR`, printed pp. 16-18 / PDF pp. 16-18 |
| Declared module count | `1` | Canonical firmware catalogue |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `98` | Canonical catalogue |
| Technical item | Scenario programmer | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `4` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `210` | `2` | `0` | `0` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `210` | `1` | `61` Scenario scheduler | Fixed/designated metadata | `1188` | `61` | `639` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `210` | Product Programming | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `210` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `210` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `210` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `210` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity; Local Dynamic IP |
| `210` | `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `210` | `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` (publisher catalogue documentation default) | Public IP address |
| `210` | `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity; Public Dynamic IP |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `61` - Scenario scheduler

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity |
| `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` (publisher catalogue documentation default) | Public IP address |
| `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | - | None | - | No relation-specific filters associated | - | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `98` / `modobj = 4` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`61`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Programmable scenario controller configured with TiMH200. Projects define time- or event-driven scenarios, are transferred over Ethernet, and can coordinate MyHOME Automation devices and F422-separated installations.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical catalogue identifies a single `MH200` commercial identity with firmware `2.0.0`. The retained official TiMH200 manual directly targets the MH200 Scenario Programmer and documents Ethernet programming, project transfer and firmware update without importing MH200N-specific electrical characteristics.

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
