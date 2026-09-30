# Light manager control unit

## Summary

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
| BTicino / Undefined | `BMNE500` | `35` | Gateway identity | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `U4554C_S4_EN` | TiBMNE500 software manual | publisher revision as archived | whole manual | [Archived PDF](../../sources/devices/documents/device-doc-bmne500-u4554c-s4-en/U4554C_S4_EN.pdf) | [Publisher PDF](https://dar.bticino.com/asset/Documents/U4554C_S4_EN.pdf) |
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

The topology is explicit and fixed: slot `1` is Object `127` Lighting manager; slot `2` is Object `61` Scenario scheduler; slot `3` is Object `150` Gateway Open SCS.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `126` | `4` | `3` | Product Programming |

The catalogue lists configuration mode 4 only. Publisher documentation independently states that BMNE500 is configured by software.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | MyHOME Suite / catalogue identity field - not a physical configurator |
| `IS_GATEWAY` | Disable / Enable | `0` | gateway enable flag |
| `SYSADDRESS` | catalogue user value | `1` | system / univocal address |
| `FW_VER` | version string | `3.0.0` | firmware-version field used by the software model |
| `CMD_PORT` | TCP port | `20000` | OpenWebNet command port |
| `LAN_IP_ADDRESS` | IPv4 address | catalogue example | local IP address |
| `LAN_IP_ADDR_TYPE` | Static IP / Dynamic IP (DHCP) | `0` | static / DHCP selection |
| `CONNECTION_METHOD` | Dynamic IP (DHCP) / Static IP / Web active connections | `0` | network connection method |

These are software/network fields, not physical configurators. Defaults shown here are catalogue defaults or examples; private-address examples are intentionally not reproduced, and none of these values are observations from a deployed BMNE500.

## Object configuration surfaces

### Object `127` - Lighting manager

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | IPv4 address | catalogue example | Local IP address |
| `CONNECTION_METHOD` | Dynamic IP (DHCP) / Static IP / Web active connections | `0` | Public IP dynamicity |
| `LAN_IP_ADDR_TYPE` | Static IP / Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `SYSADDRESS` | catalogue user value | `1` | Univocal code |

**Firmware relationship.** No additional Object/Firmware range filter in the catalogue.

### Object `61` - Scenario scheduler

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | IPv4 address | catalogue example | Local IP address |
| `LAN_IP_ADDR_TYPE` | Static IP / Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `CONNECTION_METHOD` | Dynamic IP (DHCP) / Static IP / Web active connections | `0` | Public IP dynamicity |
| `IP_ADDRESS` | IPv4 address | catalogue example | Public IP address |
| `CMD_PORT` | TCP port | `20000` | Commands port |
| `IS_GATEWAY` | Disable / Enable | `0` | Gateway |
| `SYSADDRESS` | catalogue user value | `1` | Univocal code |

**Firmware relationship.** No additional Object/Firmware range filter in the catalogue.

### Object `150` - Gateway Open SCS

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | IPv4 address | catalogue example | Local IP address |
| `LAN_IP_ADDR_TYPE` | Static IP / Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IS_GATEWAY` | Disable / Enable | `0` | Gateway |
| `SYSADDRESS` | catalogue user value | `1` | Univocal code |

**Firmware relationship.** No additional Object/Firmware range filter in the catalogue.

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `0` | Device/Firmware topology conditions |
| Object/Firmware filters | `0` | Conditional Object configuration exposure |
| Referenced conversion rules | `0` | None |

Generic condition/conversion evaluation remains canonical in [Catalogue Resolution](../../internals/catalogue-resolution.md); these tables preserve this Device's exact applicability records.

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
- [U4554C_S4_EN](../../sources/devices/documents/device-doc-bmne500-u4554c-s4-en/U4554C_S4_EN.pdf)
- [BMNE500 catalogue record](https://catalogue.bticino.com/pdf/scheda-prodotto/BTI-BMNE500)
