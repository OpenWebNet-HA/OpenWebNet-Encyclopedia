# MH201 hotel room scenario manager

## Summary

MH201 is a hotel room manager that connects a room’s SCS devices to an Ethernet supervision network. It coordinates room status and scenarios, provides a configuration gateway and records room events, within a compact one-DIN-module enclosure.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0190` | Project identity |
| Technical description | MH201 hotel room scenario manager | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `MH201` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1771` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Access control | Main system association |
| Item model / `modobj` | `10` | Main association; independent of project ID |
| Firmware definition | `119`, `562`, `599`, `694`, `724` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `3` | Firmware metadata |
| Categories | Gateways and interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `MH201` | Established catalogue identity | Manufacturer database commercial record `1814` explicitly links this SKU to item `1771` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `MH201` | `8005543498033` | `MH201-publisher-product-sheet.pdf` PDF p. 1 |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `LE06187AB.pdf` | MH201 multilingual installation leaflet | `LE06187AB-01PC-13W46` | PDF pp. 1-3: restart/DHCP timings, LED phase table and direct / switch Ethernet wiring; English blocks reviewed; differs from technical sheet actions. | [Archived original](https://archive.openwebnet-ha.org/sha256/51/d9/51d96097d2085e3648b56f74e44143a07e69b5da8b0e1802a0837d6a3fa80f5b.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/LE06187AB.pdf) |
| `MM00777-b-EN.pdf` | MH201 technical sheet | `MM00777-b; 15/01/2015` | Printed/PDF pp. 1-4: electrical ratings, scenario capacities, password / name, fixed-IP startup and log deletion; pp. 3-4 topology / wiring examples. | [Archived original](https://archive.openwebnet-ha.org/sha256/92/e9/92e93b6f6499c1457b4e2f9f6add55a7aef2499ef3c4631fc83aef2d8d558806.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MM00777-b-EN.pdf) |
| `RA00122AB_S_EN.pdf` | MH201 software manual | `RA00122AB_S; printed publication date not established` | Printed/PDF pp. 4-10, 13-21, 22-38: send / receive / update, network / security / memory, room access / contacts / thermostat, scenarios and object configuration. Examples are not observed installations. | [Archived original](https://archive.openwebnet-ha.org/sha256/34/57/3457250e4c5fcce9b9fe43fc6ad5e73c31df9f69023933935c61557c3d328a79.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00122AB_S_EN.pdf) |
| `MH201-publisher-product-sheet.pdf` | Exact English publisher product export | `Export dated 05.10.2026` | Complete description, product-characteristics and classification tables; exact commercial EAN; linked document / payload inventory remains separately scoped. | [Archived original](https://archive.openwebnet-ha.org/sha256/f8/91/f8915cd76aff8dab551f9f8e774ed44db38dcb6fc80e8ed1d1e45f5b7f4ec3c5.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-MH201&include_technical=1) |
| `MM00777_b_IT.pdf` | MH201 technical sheet | `MM00777-b; 15/01/2015` | Printed/PDF pp. 1-4: electrical ratings, scenario capacities, password / name, fixed-IP startup and log deletion; pp. 3-4 topology / wiring examples. | [Archived original](https://archive.openwebnet-ha.org/sha256/b2/79/b27919dbe63fb723c14e955c6a8dc2968a0e392cee382ed7fac9e3723b64f36a.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/MM00777_b_IT.pdf) |
| `RA00122AB_S_IT.pdf` | MH201 software manual | `RA00122AB_S; printed publication date not established` | Printed/PDF pp. 4-10, 13-21, 22-38: send / receive / update, network / security / memory, room access / contacts / thermostat, scenarios and object configuration. Examples are not observed installations. | [Archived original](https://archive.openwebnet-ha.org/sha256/d8/e3/d8e3245ba86f79409657ebd715c41254e34f7605cac10e2af663431e741b215e.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/RA00122AB_S_IT.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1771`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / absorption | `18..27 Vdc / 30 mA` | `MM00777-b-EN.pdf` printed/PDF pp. 1-2 |
| Operating temperature | `5..40 °C` | `MM00777-b-EN.pdf` printed/PDF pp. 1-2 |
| Mounting | `1 DIN module` | `MM00777-b-EN.pdf` printed/PDF pp. 1-2 |
| Interfaces | `RJ45 Ethernet; SCS terminals; pushbutton; red/green LED` | `MM00777-b-EN.pdf` printed/PDF pp. 1-2 |
| Scenario limit | `50 scenarios; each up to 5 start triggers, 1 stop trigger, 1 IF condition and 10 actions` | `MM00777-b-EN.pdf` printed/PDF pp. 1-2 |
| Room roles | `DND, make-up-room, access requests, generic notifications, thermostat contact and presence` | `MM00777-b-EN.pdf` printed/PDF pp. 1-2 |
| Published conformance references | `EN60669-2-1; EN50491-5-1; EN50428` | `MM00777-b-EN.pdf` printed/PDF pp. 1-2 |

| Room wiring example | LivingLight references E49, LN4651, 348210, LN4648, LN4653, LN4652, LN4691, MH201, F430R8, F411/1N; installation-specific quantities / ratings not transferred | `MM00777-b-EN.pdf` printed/PDF p. 4 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Frequency classifications and a negative connected-object classification do not establish the runtime transport or exclude control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `MH201-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `MH201-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system radio frequency | `No` | `MH201-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system LON | `No` | `MH201-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system Powernet | `No` | `MH201-publisher-product-sheet.pdf` PDF p. 2 |
| Other bus systems | `Other` | `MH201-publisher-product-sheet.pdf` PDF p. 2 |
| Mounting method | `DRA (DIN-rail adaptor)` | `MH201-publisher-product-sheet.pdf` PDF p. 2 |
| Width in number of modular spacings | `1` | `MH201-publisher-product-sheet.pdf` PDF p. 2 |
| With bus connection | `Yes` | `MH201-publisher-product-sheet.pdf` PDF p. 2 |
| Logic object | `Yes` | `MH201-publisher-product-sheet.pdf` PDF p. 2 |
| Antimicrobial treatment | `No` | `MH201-publisher-product-sheet.pdf` PDF p. 2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1771` | Canonical catalogue |
| Technical item description | IP scenario module | Canonical catalogue |
| Item family | Source placeholder description `0`; key `8` | Canonical catalogue |
| Main system | Access control; key `8` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `10` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `119` | `1` | `0` | `0` | `3` | Catalogue default | Official |
| `562` | `1` | `1` | `0` | `3` | Not catalogue default | Official |
| `599` | `2` | `0` | `0` | `3` | Not catalogue default | Official |
| `694` | `2` | `1` | `0` | `3` | Not catalogue default | Official |
| `724` | `3` | `0` | `0` | `3` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `119` | `1` | `98` Hotel room manager | Fixed / designated metadata | `2337` | `556` | `992` |
| `119` | `2` | `150` Gateway Open SCS | Fixed / designated metadata | `2339` | `150` | `994` |
| `119` | `3` | `250` Gateway XOpen SCS | Fixed / designated metadata | `2340` | `551` | `995` |
| `562` | `1` | `98` Hotel room manager | Fixed / designated metadata | `2351` | `556` | `1006` |
| `562` | `2` | `150` Gateway Open SCS | Fixed / designated metadata | `2352` | `150` | `1007` |
| `562` | `3` | `250` Gateway XOpen SCS | Fixed / designated metadata | `2353` | `551` | `1008` |
| `599` | `1` | `98` Hotel room manager | Fixed / designated metadata | `2406` | `556` | `1058` |
| `599` | `2` | `150` Gateway Open SCS | Fixed / designated metadata | `2407` | `150` | `1059` |
| `599` | `3` | `250` Gateway XOpen SCS | Fixed / designated metadata | `2408` | `551` | `1060` |
| `694` | `1` | `98` Hotel room manager | Fixed / designated metadata | `2577` | `556` | `1196` |
| `694` | `2` | `150` Gateway Open SCS | Fixed / designated metadata | `2578` | `150` | `1197` |
| `694` | `3` | `250` Gateway XOpen SCS | Fixed / designated metadata | `2579` | `551` | `1198` |
| `724` | `1` | `98` Hotel room manager | Fixed / designated metadata | `2648` | `556` | `1258` |
| `724` | `2` | `150` Gateway Open SCS | Fixed / designated metadata | `2649` | `150` | `1259` |
| `724` | `3` | `250` Gateway XOpen SCS | Fixed / designated metadata | `2650` | `551` | `1260` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `119` | Product Programming | `3` | Association key `4` |
| `562` | Product Programming | `3` | Association key `4` |
| `599` | Product Programming | `3` | Association key `4` |
| `694` | Product Programming | `3` | Association key `4` |
| `724` | Product Programming | `3` | Association key `4` |

| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `119` | Ethernet | `2` |
| `562` | Ethernet | `2` |
| `599` | Ethernet | `2` |
| `694` | Ethernet | `2` |
| `724` | Ethernet | `2` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `119` | `5` | `0` | `xml\SDC\sdc.xml` | Parameter type `1`; payload not inspected |
| `119` | `5` | `0` | `1771_1.0_LGG\xml\SVM\svm.xml` | Parameter type `2`; payload not inspected |
| `119` | `5` | `0` | `1771_1.0_LGG\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `119` | `5` | `0` | `1771_1.0_LGG\xml\DIRECTOR\director.xml` | Parameter type `5`; payload not inspected |
| `119` | `5` | `0` | `1771_1.0_LGG\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |
| `562` | `5` | `0` | `xml\SDC\sdc.xml` | Parameter type `1`; payload not inspected |
| `562` | `5` | `0` | `1771_1.1_LGG\xml\SVM\svm.xml` | Parameter type `2`; payload not inspected |
| `562` | `5` | `0` | `1771_1.1_LGG\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `562` | `5` | `0` | `1771_1.1_LGG\xml\DIRECTOR\director.xml` | Parameter type `5`; payload not inspected |
| `562` | `5` | `0` | `1771_1.1_LGG\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |
| `599` | `5` | `0` | `xml\SDC\sdc.xml` | Parameter type `1`; payload not inspected |
| `599` | `5` | `0` | `1771_2.0_LGG\xml\SVM\svm.xml` | Parameter type `2`; payload not inspected |
| `599` | `5` | `0` | `1771_2.0_LGG\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `599` | `5` | `0` | `1771_2.0_LGG\xml\DIRECTOR\director.xml` | Parameter type `5`; payload not inspected |
| `599` | `5` | `0` | `1771_2.0_LGG\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |
| `694` | `5` | `0` | `xml\SDC\sdc.xml` | Parameter type `1`; payload not inspected |
| `694` | `5` | `0` | `1771_2.1_LGG\xml\SVM\svm.xml` | Parameter type `2`; payload not inspected |
| `694` | `5` | `0` | `1771_2.1_LGG\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `694` | `5` | `0` | `1771_2.1_LGG\xml\DIRECTOR\director.xml` | Parameter type `5`; payload not inspected |
| `694` | `5` | `0` | `1771_2.1_LGG\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |
| `724` | `5` | `0` | `xml\SDC\sdc.xml` | Parameter type `1`; payload not inspected |
| `724` | `5` | `0` | `1771_3.0_LGG\xml\SVM\svm.xml` | Parameter type `2`; payload not inspected |
| `724` | `5` | `0` | `1771_3.0_LGG\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `724` | `5` | `0` | `1771_3.0_LGG\xml\DIRECTOR\director.xml` | Parameter type `5`; payload not inspected |
| `724` | `5` | `0` | `1771_3.0_LGG\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |

Brand / line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Scenario capacity | 50 scenarios; each 5 start triggers, 1 stop, 1 IF, 10 actions | `MM00777-b-EN.pdf` printed/PDF pp. 1-2; `RA00122AB_S_EN.pdf` pp. 4-38 |
| Device name / password | 16 characters / public documentation default 12345, maximum 9 characters, not an observed credential | `MM00777-b-EN.pdf` printed/PDF pp. 1-2; `RA00122AB_S_EN.pdf` pp. 4-38 |
| Startup pushbutton | Hold until green flashing: fixed IP 192.168.1.5, mask 255.255.255.0; public documentation values, not an observed installation | `MM00777-b-EN.pdf` printed/PDF pp. 1-2; `RA00122AB_S_EN.pdf` pp. 4-38 |
| Pushbutton 30 s | Erase event log | `MM00777-b-EN.pdf` printed/PDF pp. 1-2; `RA00122AB_S_EN.pdf` pp. 4-38 |
| LED red / green flashing | Acquiring Ethernet address configuration / configuration acquired; 1 s on, 1 s off | `MM00777-b-EN.pdf` printed/PDF pp. 1-2; `RA00122AB_S_EN.pdf` pp. 4-38 |
| Room settings | DND, make-up-room, access, notifications, thermostat and presence | `MM00777-b-EN.pdf` printed/PDF pp. 1-2; `RA00122AB_S_EN.pdf` pp. 4-38 |
| Transfer / update | Send, receive, firmware update and device-info requests separately documented; manual pp. 8-10 | `MM00777-b-EN.pdf` printed/PDF pp. 1-2; `RA00122AB_S_EN.pdf` pp. 4-38 |
| Leaflet reset key | 10 s restarts; 20 s restarts and selects DHCP; distinct from sheet startup / log-deletion actions | `LE06187AB.pdf` PDF p. 1 |
| Leaflet LEDs | Red slow regular: no network / address pending; green fast regular: memory-module acquisition; green slow irregular: network found (English block); Dutch text says fast irregular for network found | `LE06187AB.pdf` PDF p. 2 |
| Software network / authentication | Fixed IP or DHCP; IP / subnet / router; public default OPEN password 12345, not an observed credential; unique gateway code | `RA00122AB_S_EN.pdf` pp. 13-14 |
| Memory / IP ranges | Optional restore of saved device states after power loss; up to four IP intervals allowed without OPEN-password authentication | `RA00122AB_S_EN.pdf` p. 15 |
| Room access / SOS | Up to eight entries; external reader R1/`R2=1..99`; door actuator A/PL; keycard switch A/PL matches reader R1/R2; up to three SOS actuators | `RA00122AB_S_EN.pdf` pp. 16-17 |
| Window / strongbox / fridge | Up to three window contacts; window / fridge notifications auto-reset on closure; strongbox reset by software; strongbox / fridge notification applies after three minutes from departure | `RA00122AB_S_EN.pdf` pp. 18-19 |
| Generic contacts | NO/NC; Info/Warning/Alarm; always / presence / no-presence condition; delay; local `CEN` / software / automatic reset; keycard-switch additional flashing; Info not logged, Warning/Alarm logged | `RA00122AB_S_EN.pdf` p. 20 |
| Thermostat / Master Badge | Enable local thermostat contact / address / type; optional master-badge serial number for guest-key programming without management software | `RA00122AB_S_EN.pdf` p. 21 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `119` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `119` | `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `119` | `FW_VER` | `######` = Firmware version | `1.0.0` | Firmware version |
| `119` | `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `119` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `119` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `119` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `562` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `562` | `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `562` | `FW_VER` | `######` = Firmware version | `1.0.0` | Firmware version |
| `562` | `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `562` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `562` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `562` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `599` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `599` | `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `599` | `FW_VER` | `######` = Firmware version | `1.0.0` | Firmware version |
| `599` | `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `599` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `599` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `599` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `694` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `694` | `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `694` | `FW_VER` | `######` = Firmware version | `1.0.0` | Firmware version |
| `694` | `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `694` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `694` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `694` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `724` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `724` | `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `724` | `FW_VER` | `######` = Firmware version | `1.0.0` | Firmware version |
| `724` | `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `724` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `724` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `724` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `150` - Gateway Open SCS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Object `250` - Gateway XOpen SCS

Catalogue Object key `551` maps to external Object `250`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Object `98` - Hotel room manager

Catalogue Object key `556` maps to external Object `98`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | Not applicable | None | Not applicable | No relation-specific filters associated | Not applicable | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `10` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Read installed firmware and compare with the applicability table | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Obtain hardware revision; no source-backed installed value | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Obtain microcontroller identity; no fingerprint retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve active Modules/Objects independently of candidate metadata | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Corroborate installed addressing and distinguish physical from reusable ranges | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Compare installed configuration with the exact firmware/Object restrictions | [Configuration](../../diagnostics/dim35-configuration.md) |

These are catalogue-derived diagnostic candidates. No Device-specific response or support across all commercial variants is established by a hardware capture.

## Functional applicability

| Catalogue Object / role | Applicability | Evidence |
| --- | --- | --- |
| `98` - Hotel room manager | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `150` - Gateway Open SCS | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `250` - Gateway XOpen SCS | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `98` - Hotel room manager | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `98` - Hotel room manager | Access control | `8` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `150` - Gateway Open SCS | Integration function | `26` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `250` - Gateway XOpen SCS | Access control | `8` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Scenarios are configured with MyHOME Suite. The sheet specifies a device name of at most 16 characters and an Open Password default of `12345` (maximum 9 characters): this is a public documentation default, not an observed installation credential. Hold the pushbutton at startup until green flashing for fixed address setup; hold 30 seconds to erase the event log. Use `RA00122AB_S_EN.pdf` for software identity / network / security, room and scenario settings; retained Italian revision corroborates the workflow.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The technical sheet specifies fixed `192.168.1.5` and mask `255.255.255.0`; public documentation values, not an observed installation. These sheet facts remain separate from Firmware-specific catalogue defaults. The three candidate roles (hotel manager, Open SCS and XOpen gateway) are distinct Objects. The one-DIN physical width is independent of three catalogue Modules. The LE06187AB leaflet describes 10-second restart and 20-second DHCP selection, and red / green LED phases that differ from the technical sheet’s startup fixed-IP and 30-second log-erasure actions. These source-specific sequences are retained without assigning the difference to an unverified firmware revision.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `LE06187AB.pdf` | PDF pp. 1-3: restart/DHCP timings, LED phase table and direct / switch Ethernet wiring; English blocks reviewed; differs from technical sheet actions. |
| `MM00777-b-EN.pdf` | Printed/PDF pp. 1-4: electrical ratings, scenario capacities, password / name, fixed-IP startup and log deletion; pp. 3-4 topology / wiring examples. |
| `RA00122AB_S_EN.pdf` | Printed/PDF pp. 4-10, 13-21, 22-38: send / receive / update, network / security / memory, room access / contacts / thermostat, scenarios and object configuration. Examples are not observed installations. |
| `MH201-publisher-product-sheet.pdf` | Complete description, product-characteristics and classification tables; exact commercial EAN; linked document / payload inventory remains separately scoped. |
| `MM00777_b_IT.pdf` | Printed/PDF pp. 1-4: electrical ratings, scenario capacities, password / name, fixed-IP startup and log deletion; pp. 3-4 topology / wiring examples. |
| `RA00122AB_S_IT.pdf` | Printed/PDF pp. 4-10, 13-21, 22-38: send / receive / update, network / security / memory, room access / contacts / thermostat, scenarios and object configuration. Examples are not observed installations. |

## Evidence limits and open work

Firmware-specific scenario limits, exact supervision implementation and installed gateway responses remain uncorroborated. Current network requirements and legacy software compatibility require source / release matching.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

### Linked sources outside reviewed evidence

These manufacturer-listed resources are visible discovery work. A listing establishes a source association; it does not establish that the payload was downloaded, verified or examined here.

| Resource | Manufacturer label | Discovery location | Review scope |
| --- | --- | --- | --- |
| `MyHOME Technical Guide.pdf` | Installation Guide GUI-MHOME  /  PDF (22.7 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/NP-FT-GT/MyHOME%20Technical%20Guide.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Brochure MyHOME.pdf` | Brochure BRO-MHOME  /  PDF (2.7 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Brochure%20MyHOME.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Catalogue Livinglight_2M.pdf` | Catalog Commercial Page CAT-LL-2M  /  PDF (39.5 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Catalogue%20Livinglight_2M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Catalogue Livinglight_3M.pdf` | Catalog Commercial Page CAT-LL-3M  /  PDF (38.7 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Catalogue%20Livinglight_3M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `MH201_3_6_44.fwz` | Firmware MH201_3_6_44  /  FWZ (207 KB) | [Manufacturer link](https://assets.legrand.com/pim/AUTRE/MH201_3_6_44.fwz) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `MyHotelSuite_050130.exe` | Software MYHOTELSUITE_050130  /  EXE (487.5 MB) | [Manufacturer link](https://assets.legrand.com/pim/AUTRE/MyHotelSuite_050130.exe) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

### Retained original fingerprints

All incorporated originals were checked against the public archive by SHA-256 and byte length. Their manifest registrations were pushed on main before incorporation; previously registered originals were reused by fingerprint.

| Original | SHA-256 | Retention / size |
| --- | --- | --- |
| `LE06187AB.pdf` | `51d96097d2085e3648b56f74e44143a07e69b5da8b0e1802a0837d6a3fa80f5b` | 663256 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/51/d9/51d96097d2085e3648b56f74e44143a07e69b5da8b0e1802a0837d6a3fa80f5b.pdf) |
| `MM00777-b-EN.pdf` | `92e93b6f6499c1457b4e2f9f6add55a7aef2499ef3c4631fc83aef2d8d558806` | 392821 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/92/e9/92e93b6f6499c1457b4e2f9f6add55a7aef2499ef3c4631fc83aef2d8d558806.pdf) |
| `RA00122AB_S_EN.pdf` | `3457250e4c5fcce9b9fe43fc6ad5e73c31df9f69023933935c61557c3d328a79` | 13180278 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/34/57/3457250e4c5fcce9b9fe43fc6ad5e73c31df9f69023933935c61557c3d328a79.pdf) |
| `MH201-publisher-product-sheet.pdf` | `f8915cd76aff8dab551f9f8e774ed44db38dcb6fc80e8ed1d1e45f5b7f4ec3c5` | 207945 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/f8/91/f8915cd76aff8dab551f9f8e774ed44db38dcb6fc80e8ed1d1e45f5b7f4ec3c5.pdf) |
| `MM00777_b_IT.pdf` | `b27919dbe63fb723c14e955c6a8dc2968a0e392cee382ed7fac9e3723b64f36a` | 393896 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/b2/79/b27919dbe63fb723c14e955c6a8dc2968a0e392cee382ed7fac9e3723b64f36a.pdf) |
| `RA00122AB_S_IT.pdf` | `d8e3245ba86f79409657ebd715c41254e34f7605cac10e2af663431e741b215e` | 13891573 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/d8/e3/d8e3245ba86f79409657ebd715c41254e34f7605cac10e2af663431e741b215e.pdf) |
