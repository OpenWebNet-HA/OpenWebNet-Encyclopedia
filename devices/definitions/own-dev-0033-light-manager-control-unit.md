# Light manager control unit

## Summary

The BMNE500 is a DIN-mounted Light Manager for lighting supervision, scheduling and scenarios. Its Ethernet interface and Open/SCS gateway functions connect the configured lighting system to software-based management and integration.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0033` | Project identity |
| Technical description | Lighting Management control unit, Ethernet interface, scenario scheduler and Open/SCS gateway | Catalogue + official documentation |
| Commercial identities | `BMNE500` | Catalogue |
| Catalogue item | `35` - “Light manager control unit” | Implementation evidence |
| Main catalogue system | Integration functions (`id_system = 26`) | Implementation evidence |
| Item model / `modobj` | `35` | Implementation evidence |
| Firmware definition | firmware `126`, version `2.0`, build `1` | Implementation evidence |
| Declared Modules | `3` | Implementation evidence |
| Categories | Gateway, Lighting management, Scenario scheduler, Integration | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino | `BMNE500` | Established identity | canonical commercial record `35`; Gateway identity | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `U4554C_S4_EN` | TiBMNE500 software manual | publisher revision as archived | whole manual | [Archived PDF](https://archive.openwebnet-ha.org/sha256/e5/d2/e5d235a413023e1e004380ffc74c3e69c5589a474249b09f4a7892374c83a62c.pdf) | [Publisher PDF](https://dar.bticino.com/asset/Documents/U4554C_S4_EN.pdf) |
| BTicino `BMNE500` catalogue record | Current product record | current | whole product record | - | [Publisher record](https://catalogue.bticino.com/pdf/scheda-prodotto/BTI-BMNE500) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply range | `12..27 V` | Current publisher product data |
| SCS BUS maximum current draw | `8 mA` | Current publisher product data |
| Mounting | 6 DIN modules | Current publisher product data |
| Network interface | Ethernet / IP interface used by the software-configured gateway functions | Publisher product data + TiBMNE500 manual |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `35` | Canonical catalogue |
| Technical item description | Light manager control unit | Canonical catalogue |
| Item family | `8` - Network device | Canonical catalogue |
| Main system | `26` - Integration functions; `modobj` `35` | AS_ITEM_SYSTEM |
| Commercial records | `1` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `126` | `2` | `0` | `1` | `3` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `126` | `1` | `127` Lighting manager | Fixed/designated metadata | `672` | `127` | `467` |
| `126` | `2` | `61` Scenario scheduler | Fixed/designated metadata | `673` | `61` | `468` |
| `126` | `3` | `150` Gateway Open SCS | Fixed/designated metadata | `674` | `150` | `469` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

The topology is explicit and fixed: slot `1` is Object `127` Lighting manager; slot `2` is Object `61` Scenario scheduler; slot `3` is Object `150` Gateway Open SCS.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `126` | `4` | `3` | Product Programming |

The catalogue lists configuration mode 4 only. Publisher documentation independently states that BMNE500 is configured by software.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `126` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `126` | `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `126` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `126` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `126` | `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `126` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `126` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity; Local Dynamic IP |
| `126` | `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity; Public Dynamic IP |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `IS_GATEWAY` | Disable / Enable | gateway enable flag |
| `SYSADDRESS` | catalogue user value | system / univocal address |
| `FW_VER` | version string | firmware-version field used by the software model |
| `CMD_PORT` | TCP port | OpenWebNet command port |
| `LAN_IP_ADDRESS` | IPv4 address | local IP address |
| `LAN_IP_ADDR_TYPE` | Static IP / Dynamic IP (DHCP) | static / DHCP selection |
| `CONNECTION_METHOD` | Dynamic IP (DHCP) / Static IP / Web active connections | network connection method |


These are software/network fields, not physical configurators. Defaults shown here are catalogue defaults or examples; private-address examples are intentionally not reproduced, and none of these values are observations from a deployed BMNE500.

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


### Object `127` - Lighting manager

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |


### Object `150` - Gateway Open SCS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |


### Product interpretation and source differences

**Object `127` - Lighting manager - product interpretation.**

**Firmware relationship.** No additional Object/Firmware range filter in the catalogue.

**Object `61` - Scenario scheduler - product interpretation.**

**Firmware relationship.** No additional Object/Firmware range filter in the catalogue.

**Object `150` - Gateway Open SCS - product interpretation.**

**Firmware relationship.** No additional Object/Firmware range filter in the catalogue.

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

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
| `DIMENSION 1` | resolve `modobj = 35` and `BMNE500` identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | corroborate installed firmware against catalogue version `2.0` build `1` | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm the three fixed Objects: Lighting manager, Scenario scheduler and Open/SCS gateway | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect any exposed system/network addressing for the three fixed roles | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `SYSADDRESS`, gateway/network fields and software-programmed configuration without collapsing the three Objects | [Configuration](../../diagnostics/dim35-configuration.md) |

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
- Corroborate firmware `2.0` build `1` against observed `DIMENSION 2` / `DIMENSION 3` / `DIMENSION 6` diagnostics.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [U4554C_S4_EN](https://archive.openwebnet-ha.org/sha256/e5/d2/e5d235a413023e1e004380ffc74c3e69c5589a474249b09f4a7892374c83a62c.pdf)
- [BMNE500 catalogue record](https://catalogue.bticino.com/pdf/scheda-prodotto/BTI-BMNE500)
