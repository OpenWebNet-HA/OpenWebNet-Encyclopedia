# HOMETOUCH home automation and video-entry display

## Summary

HOMETOUCH is a 7-inch touch panel combining MyHOME home controls with a connected video-entry unit. It displays system status and controls lighting, shutters, temperature, scenarios and supported music/alarm functions. Separate automation and video-entry bus connections, plus Ethernet or Wi-Fi, let it participate in both systems.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0156` | Project identity |
| Technical description | HOMETOUCH home automation and video-entry display | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `067259`, `3488` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `2214` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `128` | Main association; independent of project ID |
| Firmware definition | `752`, `810`, `820`, `828`, `830` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `2` | Firmware metadata |
| Categories | Audio video, User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `067259` | Established catalogue identity | Manufacturer database commercial record `2556` explicitly links this SKU to item `2214` |
| BTicino | `3488` | Established catalogue identity | Manufacturer database commercial record `2555` explicitly links this SKU to item `2214` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `3488` | `8005543612033` | [3488-publisher-product-sheet.pdf](https://archive.openwebnet-ha.org/sha256/df/4e/df4e3aa837d4df07e7dc9a89f19f03f46f561ff2e2d51d499334439c8b45a6ed.pdf) PDF p. 1 |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `3488` | HOME TOUCH 7 | Canonical commercial record `2555` |
| `067259` | HOME TOUCH 7 | Canonical commercial record `2556` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `RA00162AE_EN.pdf` | English counterpart of manufacturer-linked document | `RA00162AE`-11/21-PC; printed cover label | PDF pp. 32–34,47–58,68–69,152–155,177–188,232–234: setup, server/alarm/load association and controls; remaining chapters unexamined | [Archived original](https://archive.openwebnet-ha.org/sha256/61/40/61405fb7779dff0b0c87dcf2cbeb83a20725a45e552c9c4d0fa829821f552ba7.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/RA00162AE_EN.pdf) |
| `ST-00000724-EN.pdf` | Technical Sheet `ST-00000724-EN` | `ST-00000724-EN; 30/06/2020` | PDF pp. 1–3:2020 sheet printed asST-00000517-EN; identity, rating and setup examined; later diagrams unexamined | [Archived original](https://archive.openwebnet-ha.org/sha256/eb/8f/eb8f3473da6240ab2278f69cfc50598d9d0fef5d0a4f7d95464ccd2653bb347d.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00000724-EN.pdf) |
| `3488-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 05.10.2026` | Complete exact-reference commercial export and all classification attributes examined; EAN only where explicitly retained. Source-specific ratings do not replace technical-sheet scopes | [Archived original](https://archive.openwebnet-ha.org/sha256/df/4e/df4e3aa837d4df07e7dc9a89f19f03f46f561ff2e2d51d499334439c8b45a6ed.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-3488&include_technical=1) |
| `3488-italian-product-sheet.pdf` | Exact Italian product export | `Captured 05/10/2026; compliance-template date does not establish product publication date` | Complete exact-reference commercial export and all classification attributes examined; EAN only where explicitly retained. Source-specific ratings do not replace technical-sheet scopes | [Archived original](https://archive.openwebnet-ha.org/sha256/54/76/5476372510aa149035463a0567f66726baf197e05c8c15a39d442cff4d337310.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-3488) |
| `RA00162AE_IT.pdf` | Legacy manufacturer technical documentation | `RA00162AE`-11/21-PC; printed cover label | PDF pp. 48–51,177,187: Italian server/alarm/load cross-check; remaining translation chapters unexamined | [Archived original](https://archive.openwebnet-ha.org/sha256/c6/28/c628c93b5971112560cc7a48705bd60aadf9d06233e87973dc940045939554c5.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/RA00162AE_IT.pdf) |
| `ST_00001032_IT.pdf` | Legacy manufacturer technical documentation | `ST_00001032_IT; 29/04/2022` | PDF pp. 1,4: Italian rating, server and EOS-compatibility cross-check; remaining translation pages unexamined | [Archived original](https://archive.openwebnet-ha.org/sha256/a4/65/a46584f070a5ee74879f0f5741e690e32d227a13ee5602798025ccf55929df27.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/ST_00001032_IT.pdf) |
| `ST_00001032_EN.pdf` | English counterpart of manufacturer-linked document | `ST_00001032_EN; 29/04/2022` | PDF pp. 1–6: complete2022 exact HOMETOUCH sheet, with additional-supply and EOS/server exclusions | [Archived original](https://archive.openwebnet-ha.org/sha256/91/cd/91cd736a3115eb9582dbade37df35658d3381e875e4fd2916e2c01326d9446a0.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/ST_00001032_EN.pdf) |
| `ST-00002703-EN.pdf` | Technical Sheet `ST-00002703-EN` | `ST-00002703-EN; 16/06/2026` | PDF p. 9: exact actuator/server ecosystem compatibility inspected; other product functions not transferred | [Archived original](https://archive.openwebnet-ha.org/sha256/b2/f5/b2f5090b601e33cdef9ba666108848ff4d9800792ccd5b7c14385da300bf0ffa.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002703-EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2214`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |
| `door-entry-app-update-publisher-page.html` | Exact-reference manufacturer app notice | 18 June 2024; minimums effective20 June 2024 | Entire dated notice examined; names these references, app families and minimum Android/iOS releases; not evidence of present service availability | [Archived original](https://archive.openwebnet-ha.org/sha256/b1/c5/b1c57ba8d2097fbb90bdfe3b51753b625d8440d71b5b4ed1e65e80208f251ba9.pdf) | [Publisher source](https://www.bticino.com/news/door-entry-app-important-update-available-security-reliability-and-performance-app) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `27 Vdc; additional 1–2 power supply required` | `ST_00001032_EN` p. 1 |
| AV SCS maximum draw | `20 mA during conversation at 27 V` | `ST_00001032_EN` p. 1 |
| MH SCS draw | `1 mA` | `ST_00001032_EN` p. 1 |
| Maximum additional-supply draw | `300 mA during conversation` | `ST_00001032_EN` p. 1 |
| Temperature / dimensions | `5..35 °C; 196 x 147 x 25 mm` | `ST_00001032_EN` p. 1 |
| Display | `7-inch capacitive touch screen` | `ST_00001032_EN` p. 1 |
| Interfaces | `AV SCS BUS; MH SCS BUS; Ethernet; Wi-Fi; service mini-USB; floor-call terminals` | `ST_00001032_EN` p. 1 |
| Wireless | `IEEE 802.11 b/g/n, 2.4 GHz, 13 channels` | `ST_00001032_EN` p. 1 |
| Published network traffic | `5061 SIP device; 5228 SIP app; UDP 0..65000 negotiated media; HTTP/HTTPS 80/443` | `ST_00001032_EN` p. 1 |
| Mounting | `wall bracket or flush box 3487; supply 346020 related item` | `ST_00001032_EN` p. 1 |
| Network limits | `one app-connected internal unit; maximum ten HOMETOUCH connected to a MyHOMEServer1 on one LAN` | `ST_00001032_EN` p. 6 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Classification frequency values of zero are separate from explicitly documented Wi-Fi carriers; a negative connected-object classification does not exclude remote control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `ST_00001032_EN` p. 1 |
| Bus system KNX-RF (Radio Frequency) | `No` | `ST_00001032_EN` p. 1 |
| Bus system radio frequency | `No` | `ST_00001032_EN` p. 1 |
| Bus system LON | `No` | `ST_00001032_EN` p. 1 |
| Bus system Powernet | `Yes` | `ST_00001032_EN` p. 1 |
| Other bus systems | `Other` | `ST_00001032_EN` p. 1 |
| Radio frequency bidirectional | `Yes` | `ST_00001032_EN` p. 1 |
| Assembly arrangement | `Control element` | `ST_00001032_EN` p. 1 |
| Model | `Control tableau` | `ST_00001032_EN` p. 1 |
| Mounting method | `Flush-mounted` | `ST_00001032_EN` p. 1 |
| Touch function | `Yes` | `ST_00001032_EN` p. 1 |
| Additional interfaces | `Ethernet` | `ST_00001032_EN` p. 1 |
| With bus connection | `Yes` | `ST_00001032_EN` p. 1 |
| Material | `Glass` | `ST_00001032_EN` p. 1 |
| Material quality | `Other` | `ST_00001032_EN` p. 1 |
| Colour | `Black` | `ST_00001032_EN` p. 1 |
| RAL-number (similar) | `9005` | `ST_00001032_EN` p. 1 |
| Degree of protection (IP) | `Other` | `ST_00001032_EN` p. 1 |
| Width | `196 mm` | `ST_00001032_EN` p. 1 |
| Height | `147 mm` | `ST_00001032_EN` p. 1 |
| Depth | `25 mm` | `ST_00001032_EN` p. 1 |
| Built-in depth | `7 mm` | `ST_00001032_EN` p. 1 |
| degree of impact strength (IK) | `Not applicable` | `ST_00001032_EN` p. 1 |
| Operating / setting temperature (Min-Max) | `5-35 °C` | `ST_00001032_EN` p. 1 |
| Storage temperature (Min-Max) | `-10-70 °C` | `ST_00001032_EN` p. 1 |
| Hands free | `Yes` | `ST_00001032_EN` p. 1 |
| Loudness setting | `Yes` | `ST_00001032_EN` p. 1 |
| Addressable | `Yes` | `ST_00001032_EN` p. 1 |
| Remote opening of gate / Electric door opener | `Yes` | `ST_00001032_EN` p. 1 |
| Screen resolution | `852x480` | `ST_00001032_EN` p. 1 |
| Screen brightness setting | `Yes` | `ST_00001032_EN` p. 1 |
| Screen contrast setting | `Yes` | `ST_00001032_EN` p. 1 |
| Contains Batteries | `No` | `ST_00001032_EN` p. 1 |
| Connected object | `Yes` | `ST_00001032_EN` p. 1 |
| Operating method | `SCS, Wifi network 2.4G` | `ST_00001032_EN` p. 1 |
| Application store for download | `Google Play Store, Mac Apple Store` | `ST_00001032_EN` p. 1 |
| Programmable | `Yes` | `ST_00001032_EN` p. 1 |
| Connectable by Internet box | `Yes` | `ST_00001032_EN` p. 1 |
| Application name | `Door Entry` | `ST_00001032_EN` p. 1 |
| Product use function | `Control & command systems` | `ST_00001032_EN` p. 1 |
| Software Update Duration (years) | `3` | `ST_00001032_EN` p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2214` | Canonical catalogue |
| Technical item description | HOME TOUCH 7 | Canonical catalogue |
| Item family | 0; key `20` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `128` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |
| Additional system | Video door entry system; key `4`; model `24` | Separate non-main catalogue association |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Video door entry system | `24` | No | Canonical item/system relationship |
| Integration function | `128` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Multimedia | private riser | Canonical item/bus relationship |
| Multimedia | public riser | Canonical item/bus relationship |
| Video door entry system 8 wires | private riser | Canonical item/bus relationship |
| Video door entry system 8 wires | public riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `752` | `1` | `0` | `0` | `2` | Not catalogue default | Official |
| `810` | `2` | `0` | `0` | `2` | Not catalogue default | Official |
| `820` | `3` | `0` | `0` | `2` | Not catalogue default | Official |
| `828` | `2` | `4` | `0` | `2` | Not catalogue default | Official |
| `830` | `2` | `5` | `0` | `2` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `752` | `1038` | BTicino (key `1`) | `0` | Extra | `2214_1.0_BT\xml\Extra\extra.xml` |
| `752` | `1039` | BTicino (key `1`) | `0` | Protocol and other device parameters | `2214_1.0_BT\xml\Protocol\protocol.xml` |
| `752` | `1040` | Legrand (key `2`) | `0` | Extra | `2214_1.0_LG\xml\Extra\extra.xml` |
| `752` | `1041` | Legrand (key `2`) | `0` | Protocol and other device parameters | `2214_1.0_LG\xml\Protocol\protocol.xml` |
| `810` | `1048` | BTicino (key `1`) | `0` | Extra | `2214_2.0_BT\xml\Extra\extra.xml` |
| `810` | `1049` | BTicino (key `1`) | `0` | Protocol and other device parameters | `2214_2.0_BT\xml\Protocol\protocol.xml` |
| `810` | `1050` | Legrand (key `2`) | `0` | Extra | `2214_2.0_LG\xml\Extra\extra.xml` |
| `810` | `1051` | Legrand (key `2`) | `0` | Protocol and other device parameters | `2214_2.0_LG\xml\Protocol\protocol.xml` |
| `820` | `1072` | BTicino (key `1`) | `0` | Extra | `2214_3.0_BT\xml\Extra\extra.xml` |
| `820` | `1073` | BTicino (key `1`) | `0` | Protocol and other device parameters | `2214_3.0_BT\xml\Protocol\protocol.xml` |
| `820` | `1076` | Legrand (key `2`) | `0` | Extra | `2214_3.0_LG\xml\Extra\extra.xml` |
| `820` | `1077` | Legrand (key `2`) | `0` | Protocol and other device parameters | `2214_3.0_LG\xml\Protocol\protocol.xml` |
| `828` | `1086` | BTicino (key `1`) | `0` | Extra | `2214_2.4_BT\xml\Extra\extra.xml` |
| `828` | `1087` | BTicino (key `1`) | `0` | Protocol and other device parameters | `2214_2.4_BT\xml\Protocol\protocol.xml` |
| `828` | `1088` | Legrand (key `2`) | `0` | Extra | `2214_2.4_LG\xml\Extra\extra.xml` |
| `828` | `1089` | Legrand (key `2`) | `0` | Protocol and other device parameters | `2214_2.4_LG\xml\Protocol\protocol.xml` |
| `830` | `1093` | BTicino (key `1`) | `0` | Extra | `2214_2.5_BT\xml\Extra\extra.xml` |
| `830` | `1094` | BTicino (key `1`) | `0` | Protocol and other device parameters | `2214_2.5_BT\xml\Protocol\protocol.xml` |
| `830` | `1095` | Legrand (key `2`) | `0` | Extra | `2214_2.5_LG\xml\Extra\extra.xml` |
| `830` | `1096` | Legrand (key `2`) | `0` | Protocol and other device parameters | `2214_2.5_LG\xml\Protocol\protocol.xml` |

All 20 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `752` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `2681` | `32` | `1288` |
| `752` | `2` | `154` Internal Unit | Fixed/designated metadata | `2682` | `154` | `1289` |
| `810` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `3392` | `32` | `1646` |
| `810` | `2` | `154` Internal Unit | Fixed/designated metadata | `3393` | `154` | `1647` |
| `820` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `3411` | `32` | `1665` |
| `820` | `2` | `154` Internal Unit | Fixed/designated metadata | `3412` | `154` | `1666` |
| `828` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `3423` | `32` | `1677` |
| `828` | `2` | `154` Internal Unit | Fixed/designated metadata | `3424` | `154` | `1678` |
| `830` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `3427` | `32` | `1681` |
| `830` | `2` | `154` Internal Unit | Fixed/designated metadata | `3428` | `154` | `1682` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `752` | Product Programming | `3` | Canonical firmware/mode association |
| `810` | Product Programming | `3` | Canonical firmware/mode association |
| `820` | Product Programming | `3` | Canonical firmware/mode association |
| `828` | Product Programming | `3` | Canonical firmware/mode association |
| `830` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `752` | Ethernet | Canonical firmware/connection association |
| `752` | Ethernet over USB | Canonical firmware/connection association |
| `810` | Ethernet | Canonical firmware/connection association |
| `810` | Ethernet over USB | Canonical firmware/connection association |
| `820` | Ethernet | Canonical firmware/connection association |
| `820` | Ethernet over USB | Canonical firmware/connection association |
| `828` | Ethernet | Canonical firmware/connection association |
| `828` | Ethernet over USB | Canonical firmware/connection association |
| `830` | Ethernet | Canonical firmware/connection association |
| `830` | Ethernet over USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `First switch-on` | language; video N/P, app-connected unit, staircase light, teleloop; then server/network | `ST-00000724-EN` printed/PDF pp. 1-8, printed identifier `ST-00000517-EN`; `RA00162AE_EN` pp. 47-54,55-98 |
| `App-connected unit` | one per system; owns call forwarding and answering machine | `ST-00000724-EN` printed/PDF pp. 1-8, printed identifier `ST-00000517-EN`; `RA00162AE_EN` pp. 47-54,55-98 |
| `MyHOMEServer1 connection` | Ethernet or Wi-Fi; DHCP or manual IP; synchronization required | `ST-00000724-EN` printed/PDF pp. 1-8, printed identifier `ST-00000517-EN`; `RA00162AE_EN` pp. 47-54,55-98 |
| `Update routes` | device settings / Door Entry for HOMETOUCH / Suite USB | `ST-00000724-EN` printed/PDF pp. 1-8, printed identifier `ST-00000517-EN`; `RA00162AE_EN` pp. 47-54,55-98 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `752` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `810` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `820` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `828` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `830` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `32` - Colors Touch Screen

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Object `154` - Internal Unit

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `N` | `0..3999` | `0` | Address |
| `P` | `0..95` | `0` | Associated external unit |
| `HAND_FREE` | `0` = Disable; `1` = Enable | `0` | HAND_FREE |
| `PRO_STUDIO` | `0` = Disable; `1` = Enable | `0` | Professional Studio |
| `DOOR_STATE` | `0` = Disable; `1` = Enable | `0` | Door state display |
| `PEOPLE_S` | `0` = No; `1` = ?; `2` = ? | `0` | PeopleSearching |
| `MENU_PRE` | `0..99` | `0` | MenuPreset |
| `RING_T_OUT` | `1..30` | `10` | RingTimeOut |
| `CALL_T_OUT` | `10..180` | `30` | Call timeout |
| `PE_T_OUT` | `3..90` | `6` | EUConnectionTimeOut |
| `PI_T_OUT` | `3..90` | `18` | IUConnectionTimeOut |
| `TEL_T_OUT` | `3..180` | `90` | TelConnectionTimeout |
| `ASS_SWITCH` | `0..95` | `0` | AssociatedSwitchboard |
| `BEEP` | `0` = Disable; `1` = Enable | `0` | BEEP |
| `IS_SLAVE` | `0` = Not slave; `1` = Slave | Not specified in source | Slave |
| `DOSA_CALL` | `0` = Enable; `1` = Disable | `0` | Forward incoming call to ethernet |

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

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution remains in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `128` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `32` - Colors Touch Screen | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `154` - Internal Unit | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system/model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The home-automation objects are detected from the configured MyHOME_Up/MyHOMEServer1 system; this does not mean initial setup is absent. First switch-on selects language, N/P video-entry addressing, app-connected unit, staircase light and teleloop, then network connection and MyHOMEServer1 synchronisation. The first-switch-on menu allows sections to be skipped and completed later. Use DHCP or manual IP and Ethernet/Wi-Fi as documented. The video-entry app handles calls, locks, cameras and answering-machine events; the local panel adds favourites and configured home objects. Firmware updates use device settings with Internet, the Door Entry for HOMETOUCH app or Suite over USB. Check server firmware compatibility. Additional supply is mandatory in the sheet’s diagrams; in/out video wiring is allowed only with addressed calls. Parallel additional units need Master/Slave support. While the app is connected for a call/camera operation, other display operations are unavailable.

Apply the firmware-specific restrictions above. The generic session/validation method remains in [Programming](../../programming/).

### Home control prerequisites

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| MyHOMEServer1 association | DHCP is initially enabled. Select the actual server by its Device ID and enter its installer code; manual IP search is available. Imported functions rely on the already configured server. | Manual pp. 47–54 |
| Temperature and scenarios | Thermostat/towel-warmer/fan-coil controls depend on configured objects. Scenario object starts a scenario created in MyHOME_Up; it is not a scenario programming editor. | Manual pp. 152–155 |
| Alarm management | Requires BTicino4200/4201/4203 and installer association; country availability applies. Insertion scenarios/partitions and zone inclusion/exclusion may ask for the system code. Acknowledging an alarm display does not resolve its cause. | Manual pp. 177–185 |
| Load management | Installer configuration required. A shed load can be force-enabled for 4hours with higher priority only within the maximum absorption threshold; its normal priority then resumes. Consumption viewing is assigned to MyHOME_Up in this edition. | Manual pp. 186–188 |
| Topology | Additional supply required; only Master/Slave-capable additional IUs allowed in the parallel diagram. One app-connected IU per system and at most10 HOMETOUCH on the server LAN. | `ST_00001032_EN` pp. 4–6 |

### Dated app-update prerequisite

The [manufacturer notice of 18 June 2024](https://archive.openwebnet-ha.org/sha256/b1/c5/b1c57ba8d2097fbb90bdfe3b51753b625d8440d71b5b4ed1e65e80208f251ba9.pdf) names 3488/3488 W/067259 for Door Entry HOMETOUCH. From 20 June 2024 it requires at least Android 1.7.0 or iOS 1.6.0 to continue receiving calls. These are dated service prerequisites, not the latest release, installed firmware, or measured cloud availability.

## Source reconciliation

3488 and 067259 are database identities; the shared sheet also names 3488 W as a documented external variant without adding it to this cluster’s catalogue records. The downloaded filename `ST-00000724-EN` prints `ST-00000517-EN` and 30/06/2020; both identifiers are preserved. “No configuration necessary” describes discovery of existing home objects, whereas the manual explicitly requires basic video/network/server setup. The current EOS sheet says HOMETOUCH is incompatible with Classe 300EOS and compatible only with MyHOMEServer1; a newer server or gateway is not substituted on the basis of branding.

### Reviewed source boundaries

Automatic import does not remove the need to associate MyHOMEServer1 and complete basic setup. One app-connected internal unit per system and ten HOMETOUCH panels on the server LAN are different limits. The 2022 sheet requires additional supply and excludes Classe 300EOS; it does not authorise substituting a newer server. Alarm and load controls require the explicitly associated equipment and configuration, with country-dependent availability.

### Retained source accounting

| Original | Examined role / remaining scope |
| --- | --- |
| `RA00162AE_EN.pdf` | PDF pp. 32–34,47–58,68–69,152–155,177–188,232–234: setup, server/alarm/load association and controls; remaining chapters unexamined |
| `ST-00000724-EN.pdf` | PDF pp. 1–3:2020 sheet printed asST-00000517-EN; identity, rating and setup examined; later diagrams unexamined |
| `3488-publisher-product-sheet.pdf` | Complete exact-reference commercial export and all classification attributes examined; EAN only where explicitly retained. Source-specific ratings do not replace technical-sheet scopes |
| `3488-italian-product-sheet.pdf` | Complete exact-reference commercial export and all classification attributes examined; EAN only where explicitly retained. Source-specific ratings do not replace technical-sheet scopes |
| `RA00162AE_IT.pdf` | PDF pp. 48–51,177,187: Italian server/alarm/load cross-check; remaining translation chapters unexamined |
| `ST_00001032_IT.pdf` | PDF pp. 1,4: Italian rating, server and EOS-compatibility cross-check; remaining translation pages unexamined |
| `ST_00001032_EN.pdf` | PDF pp. 1–6: complete2022 exact HOMETOUCH sheet, with additional-supply and EOS/server exclusions |
| `ST-00002703-EN.pdf` | PDF p. 9: exact actuator/server ecosystem compatibility inspected; other product functions not transferred |
| `door-entry-app-update-publisher-page.html` | Entire dated notice examined; names these references, app families and minimum Android/iOS releases; not evidence of present service availability |

## Evidence limits and open work

Server/firmware compatibility, present app/cloud service, hearing-loop implementation, installed protocol/diagnostic behavior and integration with any later server require corroboration.

No installed hardware revision or microcontroller fingerprint is retained for this cluster. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Canonical catalogue extraction and reconciliation are complete within the retained evidence scope. Unexamined documentation, source conflicts and runtime corroboration remain explicit limits of this review.

### Discovered sources outside this review

These publisher-linked sources were identified but were not retained or used as evidence. Their presence is not evidence of installed firmware, a certified test result or additional capability.

| Source | Remaining scope | Publisher provenance |
| --- | --- | --- |
| `LGMDBDWSDK.PDF` | Publisher-linked document; contents and applicability unexamined | [Publisher listing](https://assets.legrand.com/pim/Certif/LGMDBDWSDK.PDF) |
| `Brochure Living_NOW 2M.pdf` | Publisher-linked document; contents and applicability unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Brochure Living_NOW 2M.pdf) |
| `Brochure Living_NOW 3M.pdf` | Publisher-linked document; contents and applicability unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Brochure Living_NOW 3M.pdf) |
| `Brochure MyHOME.pdf` | Publisher-linked document; contents and applicability unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Brochure MyHOME.pdf) |
| `Catalogue Living_NOW 2M.pdf` | Publisher-linked document; contents and applicability unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Catalogue Living_NOW 2M.pdf) |
| `Catalogue Living_NOW 3M.pdf` | Publisher-linked document; contents and applicability unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Catalogue Living_NOW 3M.pdf) |
| `MyHome_Suite_README_v2.pdf` | Publisher-linked document; contents and applicability unexamined | [Publisher listing](https://assets.legrand.com/pim/AUTRE/MyHome_Suite_README_v2.pdf) |
| `SMARTDES_030205.fwz` | Firmware binary; payload/update applicability unexamined | [Publisher listing](https://assets.legrand.com/pim/AUTRE/SMARTDES_030205.fwz) |

[`RA00162AD_U_EN.pdf`](https://dar.bticino.com/asset/Documents/RA00162AD_U_EN.pdf) is an earlier manufacturer revision found during discovery; its full content has not been compared with AE. The source’s MyHOME_Up naming is historical and does not establish present app availability.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0151-0160-2026-10-07.md#own-dev-0156)
