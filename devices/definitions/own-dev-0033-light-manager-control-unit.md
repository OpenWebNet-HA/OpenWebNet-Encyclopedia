# Light manager control unit

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0033` | Project identity |
| Technical description | Lighting Management control unit, Ethernet interface, scenario scheduler and Open/SCS gateway | Catalogue + official documentation |
| Catalogue item / model | `35` / `modobj 35` | Implementation evidence |
| Firmware applicability | 126, version 2.0 build 1, three slots | Implementation evidence |
| Commercial identities | BMNE500 | Catalogue |
| Categories | Gateway, Lighting management, Scenario scheduler, Integration | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino / Undefined | `BMNE500` | `35` | Gateway identity | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Relevant pages | Status | Source |
| --- | --- | --- | --- | --- | --- |
| U4554C_S4_EN | TiBMNE500 software manual | publisher revision as archived | Whole manual | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-bmne500-u4554c-s4-en/U4554C_S4_EN.pdf) |
| BMNE500 catalogue record | Current product record | current | Whole product record | External official source | [Official source](https://catalogue.bticino.com/pdf/scheda-prodotto/BTI-BMNE500) |

Multi-product guides retain an explicit page-location limitation until both printed and 1-based PDF page numbers are pinned.

## Physical and electrical characteristics

Current publisher data gives 12..27 V supply, BUS maximum consumption 8 mA and a six-DIN-module enclosure.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `35` | Canonical catalogue |
| Technical item description | Light manager control unit | Canonical catalogue |
| Item family | `8` - Network device | Canonical catalogue |
| Main system | `26` - Integration functions; `modobj` `35` | AS_ITEM_SYSTEM |
| Commercial records | `1` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Declared slots | Default | Status |
| ---: | ---: | ---: | ---: | --- | --- |
| `126` | `2` | `0` | `3` | `1` | `-1` |

Firmware 126 is version 2.0 build 1 and declares three Module slots.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `126` | `467` | `127` | `127` | Lighting manager |
| `126` | `468` | `61` | `61` | Scenario scheduler |
| `126` | `469` | `150` | `150` | Gateway Open SCS |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `672` | `1` | `127` | fixed | Lighting manager |
| `673` | `2` | `61` | fixed | Scenario scheduler |
| `674` | `3` | `150` | fixed | Gateway Open SCS |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| - | - | - | - | No firmware-scoped Virgin Object | - | - |

The topology is explicit and fixed: slot 1 is Object 127 Lighting manager; slot 2 is Object 61 Scenario scheduler; slot 3 is Object 150 Gateway Open SCS.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `126` | `4` | `3` | Product Programming |

The catalogue lists configuration mode 4 only. Publisher documentation independently states that BMNE500 is configured by software.

## Firmware-scoped configuration

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `AID` | ID | user_value | `********` - AID - range `0`..`0` - step `1` | visible=1, hidden=0, read-only=0, type-id=0 |
| `IS_GATEWAY` | Gateway | Boolean | range -..- - step `1`<br>`0` - Disable - range -..- - step `1`<br>`1` - Enable - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `SYSADDRESS` | Univocal code | user_value | `######` - Univocal code - range -..- - step `1` - default marker `1` | visible=1, hidden=0, read-only=, type-id= |
| `FW_VER` | Firmware version | user_value | `######` - Firmware version - range -..- - step `1` - default marker `3.0.0` | visible=1, hidden=0, read-only=, type-id= |
| `CMD_PORT` | Commands port | user_value | `#####` - Commands port - range -..- - step `1` - default marker `20000` | visible=1, hidden=0, read-only=, type-id= |
| `LAN_IP_ADDRESS` | Local IP address | user_value | `###.###.###.###` - Local IP address - range -..- - step `1` - default marker `192.168.1.35 (catalogue default/example, not observed)` | visible=1, hidden=0, read-only=, type-id= |
| `LAN_IP_ADDR_TYPE` | Local IP dynamicity | Enum | range -..- - step `1`<br>`0` - Static IP - range -..- - step `1`<br>`1` - Dynamic IP (DHCP) - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `CONNECTION_METHOD` | Public IP dynamicity | Enum | range -..- - step `1`<br>`0` - Dynamic IP (DHCP) - range -..- - step `1`<br>`1` - Static IP - range -..- - step `1`<br>`2` - Web active connections - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |

Catalogue range rows are preserved directly; product-document physical configurator limits remain a distinct evidence layer.

Firmware fields include AID, IS_GATEWAY, SYSADDRESS, FW_VER, CMD_PORT, LAN_IP_ADDRESS, LAN_IP_ADDR_TYPE and CONNECTION_METHOD. The three Objects add their own network/gateway and scenario-scheduler configuration surfaces.

## Object configuration surfaces

### Object `61` - Scenario scheduler

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | Local IP address | user_value | `###.###.###.###` - Local IP address - range -..- - step `1` - default marker `192.168.1.35 (catalogue default/example, not observed)` | visible=1, hidden=0, read-only=, type-id= |
| `LAN_IP_ADDR_TYPE` | Local IP dynamicity | Enum | range -..- - step `1`<br>`0` - Static IP - range -..- - step `1`<br>`1` - Dynamic IP (DHCP) - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `CONNECTION_METHOD` | Public IP dynamicity | Enum | range -..- - step `1`<br>`0` - Dynamic IP (DHCP) - range -..- - step `1`<br>`1` - Static IP - range -..- - step `1`<br>`2` - Web active connections - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `IP_ADDRESS` | Public IP address | user_value | `###.###.###.###` - Public IP address - range -..- - step `1` - default marker `192.168.1.35 (catalogue default/example, not observed)` | visible=1, hidden=0, read-only=, type-id= |
| `CMD_PORT` | Commands port | user_value | `#####` - Commands port - range -..- - step `1` - default marker `20000` | visible=1, hidden=0, read-only=, type-id= |
| `IS_GATEWAY` | Gateway | Boolean | range -..- - step `1`<br>`0` - Disable - range -..- - step `1`<br>`1` - Enable - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `SYSADDRESS` | Univocal code | user_value | `######` - Univocal code - range -..- - step `1` - default marker `1` | visible=1, hidden=0, read-only=, type-id= |

### Object `127` - Lighting manager

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | Local IP address | user_value | `###.###.###.###` - Local IP address - range -..- - step `1` - default marker `192.168.1.35 (catalogue default/example, not observed)` | visible=1, hidden=0, read-only=, type-id= |
| `CONNECTION_METHOD` | Public IP dynamicity | Enum | range -..- - step `1`<br>`0` - Dynamic IP (DHCP) - range -..- - step `1`<br>`1` - Static IP - range -..- - step `1`<br>`2` - Web active connections - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `LAN_IP_ADDR_TYPE` | Local IP dynamicity | Enum | range -..- - step `1`<br>`0` - Static IP - range -..- - step `1`<br>`1` - Dynamic IP (DHCP) - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `SYSADDRESS` | Univocal code | user_value | `######` - Univocal code - range -..- - step `1` - default marker `1` | visible=1, hidden=0, read-only=, type-id= |

### Object `150` - Gateway Open SCS

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | Local IP address | user_value | `###.###.###.###` - Local IP address - range -..- - step `1` - default marker `192.168.1.35 (catalogue default/example, not observed)` | visible=1, hidden=0, read-only=, type-id=0 |
| `LAN_IP_ADDR_TYPE` | Local IP dynamicity | Enum | range -..- - step `1`<br>`0` - Static IP - range -..- - step `1`<br>`1` - Dynamic IP (DHCP) - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `IS_GATEWAY` | Gateway | Boolean | range -..- - step `1`<br>`0` - Disable - range -..- - step `1`<br>`1` - Enable - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `SYSADDRESS` | Univocal code | user_value | `######` - Univocal code - range -..- - step `1` - default marker `1` | visible=1, hidden=0, read-only=, type-id=0 |

Object 127 owns Lighting Manager network settings, Object 61 owns scheduler/network fields, and Object 150 represents the Open/SCS gateway. These are three fixed functional Modules of one Physical Device, not three separate products.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `0` | Device/Firmware topology conditions |
| Object/Firmware filters | `0` | Conditional Object configuration exposure |
| Referenced conversion rules | `0` | None |

Generic condition/conversion evaluation remains canonical in [Catalogue Resolution](../../internals/catalogue-resolution.md); these tables preserve this Device's exact applicability records.

## Diagnostic applicability

| Surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | Identify the Device model/family and compare it with catalogue identity. | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Record installed firmware instead of treating wildcard catalogue applicability as an observed version. | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve Module/Object topology, especially when candidates share a slot. | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Inspect addressing for the resolved Module/Object when exposed. | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Corroborate firmware/Object configuration and physical/software relationships. | [Configuration](../../diagnostics/dim35-configuration.md) |

Catalogue applicability is not itself an observed runtime result.

## Functional applicability

BMNE500 spans Lighting Management and integration functions: lighting supervision, scheduling/scenarios and Open/SCS gateway access.

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact technical item is currently retained.

## Programming

Keep gateway/network identity fields separate from runtime lighting objects. Preserve all three fixed Modules and do not collapse BMNE500 to a generic Ethernet gateway.

## Source reconciliation

The canonical database and current publisher material agree that BMNE500 is a software-configured Lighting Management gateway/control unit. The database adds the exact three-slot internal model: Lighting manager, Scenario scheduler and Gateway Open SCS.

## Evidence limits and open work

- Archive a stable publisher-generated BMNE500 product-sheet PDF if one becomes available; the TiBMNE500 manual is archived.
- Add a sanitized BMNE500 hardware fingerprint and gateway-session observations.
- Corroborate firmware 2.0 build 1 against observed DIM2/DIM3/DIM6 diagnostics.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [U4554C_S4_EN](../../sources/devices/documents/device-doc-bmne500-u4554c-s4-en/U4554C_S4_EN.pdf)
- [BMNE500 catalogue record](https://catalogue.bticino.com/pdf/scheda-prodotto/BTI-BMNE500)
