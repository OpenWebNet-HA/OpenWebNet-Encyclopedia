# F460 MyHOME server

## Summary

F460 is the DIN-rail server that coordinates a MyHOME SCS home-automation installation. Installers configure it with Home + Project, while residents use Home + Control for local and remote control, scenarios and supported integrations. It manages humidity natively and can expand from 175 to 525 addresses with the documented supplies and interfaces.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0207` | Project identity |
| Technical description | F460 MyHOME server | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `F460` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `2288` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `132` | Main association; independent of project ID |
| Firmware definition | `840` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `2` | Firmware metadata |
| Categories | Gateways and interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F460` | Established catalogue identity | Manufacturer database commercial record `2649` explicitly links this SKU to item `2288` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F460` | `8005543718216` | `F460-publisher-product-sheet.pdf` PDF p. 1; `F460-italian-product-sheet.pdf` PDF p. 1 |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MyHOME Technical Guide.pdf` | Installation Guide GUI-MHOME | `Manufacturer system guide; URL retrieval generation, no explicit single release established; illustrative dates are not publication dates` | Printed/PDF pp. 6, 8-13, 24-26, 32, 82: exact-reference role, system context and catalogue entries; other products/chapters not transferred. | [Archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MyHOME%20Technical%20Guide.pdf) |
| `LE13692AC.pdf` | Instruction Use LE13692AC | `LE13692AC; 04/25-01 PC` | Printed/PDF pp. 1-2: exact-reference specification, connection and configuration content; shared-product content separately scoped. | [Archived original](https://archive.openwebnet-ha.org/sha256/af/f7/aff7c4bc2ebed1405feedebdea85f99f8a901e90446b07fe8a64ae704217bea4.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/LE13692AC.pdf) |
| `RA00224AA_EN.pdf` | Installation Guide RA00224AA_EN | `RA00224AA_EN-07/24-PC; F460/F461 server manual` | Printed/PDF pp. 5-13, 44-72, 211-279: limits, roles, topology, commissioning, settings and scoped functional chapters; screenshots not runtime evidence; unrelated UI steps not exhaustively reviewed. | [Archived original](https://archive.openwebnet-ha.org/sha256/d2/a4/d2a45bbcd72baa0b6e5536baccca8816cce3cdf94414e7b7144763003c1b1e6d.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00224AA_EN.pdf) |
| `ST-00002701-REV2-EN.pdf` | Technical Sheet ST-00002701-REV2-EN | `ST-00002701-REV2-EN; 16/06/2026` | Printed/PDF pp. 1-7: exact-reference specification, connection and configuration content; shared-product content separately scoped. | [Archived original](https://archive.openwebnet-ha.org/sha256/78/ae/78ae843060334dbd6d065284c0e5144469d8629633b519585b8daec14deacdc6.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002701-REV2-EN.pdf) |
| `F460-publisher-product-sheet.pdf` | Exact English product export | `Publisher export retrieved 05.10.2026; Italian compliance dates are boilerplate` | PDF pp. 1-5: exact-reference commercial record, EAN and classification values; no printed page sequence established; linked resources are separately accounted for. | [Archived original](https://archive.openwebnet-ha.org/sha256/fa/e3/fae334fdd184b1b2f851fb2e670326dea10798243a8a7d85afa1d1a036c35d45.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-F460&include_technical=1) |
| `F460-myhome-features-ean-publisher-page.html` | Original manufacturer HTML feature page | `Retrieved 05.10.2026; mutable publisher page` | Original HTML; sections “An even more flexible and powerful system” and “Creation and management of scenarios”; retrieved 05.10.2026; no pagination. | [Archived original](https://archive.openwebnet-ha.org/sha256/d8/6a/d86a3cc643cab14b2602759e9e36e3ed53ab669bc7c986339be9b3b75d845893.pdf) | [Publisher original](https://www.bticino.com/products/smart-home-and-home-automation-systems/home-automation-system-myhome-bus-solutions/features-and-benefits) |
| `Home-Project-2026-new-functions.pdf` | Home + Project new functions | `Manufacturer 2026 feature matrix; May 2026 publisher URL; no printed single release date` | Printed/PDF pp. 3-5, 21-29: exact F460/F461 version matrix and commissioning updates; earlier feature descriptions reviewed for applicability, not installed behavior. | [Archived original](https://archive.openwebnet-ha.org/sha256/c6/25/c625bf9b07905fdb71e009ba2e39578b4b42cd7b957576fac87ddc4968b41b40.pdf) | [Publisher original](https://www.bticino.com/sites/default/files/2026-05/NUOVE%20FUNZIONI%20HOME%20%2B%20PROJECT%202026%20GB.pdf) |
| `RA00224AA_IT.pdf` | Italian manufacturer technical document | `RA00224AA_IT-07/24-PC; F460/F461 server manual` | Printed/PDF pp. 5-13, 44-72, 211-279: limits, roles, topology, commissioning, settings and scoped functional chapters; screenshots not runtime evidence; unrelated UI steps not exhaustively reviewed. | [Archived original](https://archive.openwebnet-ha.org/sha256/b2/f7/b2f744a263a1b05c002031b3b3eeb6850f3576fe190759a849543d0de8181c08.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/RA00224AA_IT.pdf) |
| `ST-00002701-IT.pdf` | Italian manufacturer technical document | `ST-00002701-IT; 16/06/2026` | Printed/PDF pp. 1-7: exact-reference specification, connection and configuration content; shared-product content separately scoped. | [Archived original](https://archive.openwebnet-ha.org/sha256/89/a3/89a32f3b7bbded41d5417095d918a1b192061a4e4688c1e958abf15061898fb1.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/ST-00002701-IT.pdf) |
| `F460-italian-product-sheet.pdf` | Exact Italian product export | `Publisher export retrieved 05.10.2026; Italian compliance dates are boilerplate` | PDF pp. 1-1: exact-reference commercial record, EAN and classification values; no printed page sequence established; linked resources are separately accounted for. | [Archived original](https://archive.openwebnet-ha.org/sha256/ee/95/ee95d99f8ff3304af10591024346001ea0bb5b0e5268a3d2bf38967b1932800c.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F460) |
| `MyHOME-2025-Italian-guide.pdf` | MyHOME 2025 Italian guide | `Manufacturer system guide; URL retrieval generation, no explicit single release established; illustrative dates are not publication dates` | Printed/PDF pp. 6, 8-13, 24-28, 32, 134: exact-reference role and system context; URL generation 2025 does not establish a single printed release. | [Archived original](https://archive.openwebnet-ha.org/sha256/0d/f6/0df6729969f31f61feb275e84c7da84c665f8c93aeb1d5af9ba1ac29d4f82e4e.pdf) | [Publisher original](https://professionisti.bticino.it/sites/default/files/2025-03/MyHOME%20AD-ITMH25GT_smart_new.pdf) |
| `Brochure MyHOME.pdf` | MyHOME brochure | `Brochure MyHOME; printed publication date not established` | PDF pp. 22-24: F460 server/system role; no printed pagination established; no independent F461 operating specification. | [Archived original](https://archive.openwebnet-ha.org/sha256/08/9c/089c3f74e9a9713866f42956811fe779f1d952bb69aad27d6de5c4d689241718.pdf) | [Publisher original](https://assets.legrand.com/pim/DOCUMENT/Brochure%20MyHOME.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2288`: complete retained canonical associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS / supplementary supply | `18–27 Vdc / optional 20–27 Vdc` | `ST-00002701-REV2-EN.pdf` printed/PDF p. 1; dimensional data p. 2 |
| SCS draw without supplementary supply | `128 mA at 18 Vdc; 85 mA at 27 Vdc` | `ST-00002701-REV2-EN.pdf` printed/PDF p. 1; dimensional data p. 2 |
| SCS draw with supplementary supply | `3 mA` | `ST-00002701-REV2-EN.pdf` printed/PDF p. 1; dimensional data p. 2 |
| Supplementary supply draw | `106 mA at 20 Vdc; 87 mA at 27 Vdc` | `ST-00002701-REV2-EN.pdf` printed/PDF p. 1; dimensional data p. 2 |
| Operating temperature | `5–35 °C` | `ST-00002701-REV2-EN.pdf` printed/PDF p. 1; dimensional data p. 2 |
| Dimensions, 2026 sheet | `71.5 × 105 × 30.35 mm; 4 DIN modules` | `ST-00002701-REV2-EN.pdf` printed/PDF p. 1; dimensional data p. 2 |
| Dimensions, leaflet | `71.5 × 105 × 31.2 mm; unresolved depth difference` | `ST-00002701-REV2-EN.pdf` printed/PDF p. 1; dimensional data p. 2 |
| Connections | `RJ45 Ethernet LAN 10/100 Mbit; USB-C firmware/service port; SCS terminals; optional additional supply; unused connector` | `ST-00002701-REV2-EN.pdf` printed/PDF p. 1; dimensional data p. 2 |
| Indicators / restart | `System orange at power connection, then off, operative indication later; Speed yellow steady network connected; Link green steady connected, flashing transfer; brief restart-key press` | `ST-00002701-REV2-EN.pdf` printed/PDF p. 1; dimensional data p. 2 |
| Server coexistence | `Do not use F460 and F461 in the same installation` | `ST-00002701-REV2-EN.pdf` printed/PDF p. 1; dimensional data p. 2 |
| Power failure | `Device unavailable; personal-data collection interrupted` | `ST-00002701-REV2-EN.pdf` printed/PDF p. 1; dimensional data p. 2 |
| Product-specific user management | `Home + Control and documented burglar-alarm integration for F460` | `ST-00002701-REV2-EN.pdf` printed/PDF p. 1; dimensional data p. 2 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Frequency classifications and a negative connected-object classification do not establish the runtime transport or exclude control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system KNX-RF (Radio Frequency) | `No` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system radio frequency | `No` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system LON | `No` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system Powernet | `No` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Other bus systems | `Other` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Radio frequency bidirectional | `No` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Model | `Ethernet interface` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Mounting method | `DRA (DIN-rail adaptor)` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Width in number of modular spacings | `4` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Demounting protection | `No` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| With LED indication | `Yes` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Updateable | `Yes` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Operating voltage (Min-Max) | `18-27 V` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Voltage type | `DC` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Protocol | `TCP/IP` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Provider dependent | `No` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Visualization | `No` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Web-Server | `Yes` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Radio interface | `No` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| IR interface | `No` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Degree of protection (IP) | `IP30` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Width | `72 mm` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Height | `105 mm` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Depth | `36 mm` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| degree of impact strength (IK) | `Not applicable` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Operating / setting temperature (Min-Max) | `5-35 °C` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Storage temperature (Min-Max) | `-10-70 °C` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Supply current (Min-Max) | `0.003-0.160 A` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Terminal marking indication | `Yes` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Type of load | `Not applicable` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Connection type | `Screwed terminal` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Connection type | `Cable` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Label space / information surface | `No` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Fitted with USB plug | `Yes` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Addressable | `Yes` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Connected object | `Yes` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Application store for download | `Google Play Store, Mac Apple Store` | `F460-publisher-product-sheet.pdf` PDF p. 3 |
| Programming way | `Smartphone apps` | `F460-publisher-product-sheet.pdf` PDF p. 4 |
| With voice command | `Yes` | `F460-publisher-product-sheet.pdf` PDF p. 4 |
| Programmable | `Yes` | `F460-publisher-product-sheet.pdf` PDF p. 4 |
| Interoperable connection Protocol | `Yes` | `F460-publisher-product-sheet.pdf` PDF p. 4 |
| Connectable by Internet box | `Yes` | `F460-publisher-product-sheet.pdf` PDF p. 4 |
| Compatible voice assistants | `Amazon Alexa, Google Assistant` | `F460-publisher-product-sheet.pdf` PDF p. 4 |
| Application name | `Home + Control` | `F460-publisher-product-sheet.pdf` PDF p. 4 |
| Product use function | `Control & command systems` | `F460-publisher-product-sheet.pdf` PDF p. 4 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2288` | Canonical catalogue |
| Technical item description | F460 | Canonical catalogue |
| Item family | Source placeholder description `0`; key `8` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `132` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `840` | `1` | `0` | `1` | `2` | Catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `840` | `1` | `150` Gateway Open SCS | Candidate alternative | `3966` | `150` | `1856` |
| `840` | `2` | `216` Enhanced Web Server Audio/Video 2 Wires (F454) | Candidate alternative | `3967` | `512` | `1857` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `840` | Product Programming | `3` | Association key `4` |

| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `840` | Ethernet | `2` |
| `840` | Ethernet over USB | `4` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `840` | `5` | `0` | `2288_1.0_LGG\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `840` | `5` | `0` | `2288_1.0_LGG\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |

Brand / line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Capacity, 1 supply | 175 managed addresses | `RA00224AA_EN.pdf` printed/PDF p. 6 |
| Capacity, 2 supplies and 1 F422A | 350 managed addresses | `RA00224AA_EN.pdf` printed/PDF p. 6 |
| Capacity, 3 supplies and 2 F422A | 525 managed addresses | `RA00224AA_EN.pdf` printed/PDF p. 6 |
| Rooms / graphic objects | 30 rooms; 50 objects per room | `RA00224AA_EN.pdf` printed/PDF p. 6 |
| Commands / scenarios, July 2024 manual | 50 commands per actuator; 50 scenarios | `RA00224AA_EN.pdf` printed/PDF p. 6 |
| Scenario actions / start conditions | 150 actions per scenario; 50 start conditions per scenario | `RA00224AA_EN.pdf` printed/PDF p. 6 |
| Installers / concurrent installers | 15 installer accounts; 1 simultaneously connected installer | `RA00224AA_EN.pdf` printed/PDF p. 6 |
| Temperature zones | 30 maximum zones per house | `RA00224AA_EN.pdf` printed/PDF p. 6 |
| Later guide scenario figure | Up to 150 installer-created custom scenarios, unlike the manual’s 50. Four default scenarios Day/Night/Entry/Exit; custom scenario users can enable / disable rather than edit in Home + Control (F460 user role). No release mapping established. | `MyHOME-2025-Italian-guide.pdf` printed/PDF p. 13 |
| Setup / update / object association | Local plant creation; update centre; object scanning and association to rooms. Preserve project accounts and server role before transferring configuration. | `RA00224AA_EN.pdf` printed/PDF pp. 44-72 |
| Functional commissioning chapters | Scenarios 211–242; temperature 243–255; F460-only alarm 256–260; load control 261–271; system settings 272–278; desktop tool 279. These are source navigation scopes, not claims that every configured plant or F461 supports every chapter. | `RA00224AA_EN.pdf` printed/PDF pp. 211-279 |
| Physical-configuration exclusion | Not compatible with devices configured using physical configurators. Compatibility depends on exact product, production, branch and software configuration. | `ST-00002701-REV2-EN.pdf` pp. 4-5 |
| Topology requirement | Private automation riser, level 3; 175 native addresses expandable with up to two F422A interfaces as documented. | `ST-00002701-REV2-EN.pdf` p. 1; `MyHOME Technical Guide.pdf` printed/PDF pp. 6, 8, 32 |

### Published server/app revision applicability

`Home-Project-2026-new-functions.pdf` printed/PDF pp. 4-5 provides the following release pairs. These are manufacturer stack requirements, separate from catalogue version/revision/build. Installed applicability remains uncorroborated.

| Feature scope | Server release | Home + Project app | Source qualification |
| --- | --- | --- | --- |
| Older features 1–13 | Not specified | Not specified | Blank F460/F461 cells; no version inferred |
| App assessment / quick device selection | No stated server bound | `1.0.45` | Features 14–15 |
| Advanced MyHOME functions | `1.0.18` | `1.0.42` | Feature 16 |
| Configuration acquisition | `1.1.10` | `1.1.12` | Feature 17 |
| Control/actuator replacement | `1.1.19` | `1.1.16` | Feature 18 |
| DALI2 colour setup | No stated server bound | `1.1.16` | Feature 19 |
| Scan / scenario removal / DALI-channel reset | `1.4.7` | `1.2.30` | Features 20–22 |
| Classe300EOS QR retention | Not applicable to F460/F461 | Not applicable to F460/F461 | Feature 23 belongs to another server |
| Home + Control disable | `1.4.7` in grouped table | `1.2.30` | Feature 24 body specifies F460/Classe300EOS; do not transfer to F461 |

The update describes local configuration acquisition and command/actuator reassociation; dehumidification and season-change actuators are excluded from reassociation because they are functions rather than logical objects (`Home-Project-2026-new-functions.pdf` pp. 22-23).

### Published network services

These are public documentation values, not observed installation endpoints. `RA00224AA_EN.pdf` printed/PDF p. 6 lists:

| Service | Published endpoint | Port | Protocol |
| --- | --- | --- | --- |
| Main server | `nv2-bncx.netatmo.net` | `25050` | `tcp` |
| Time service | `pool.ntp.org (editable default)` | `123` | `ntp` |
| Log service | `log.bs.iotleg.com` | `5001` | `syslog` |
| Firmware download | `n3tfw.blob.core.windows.net` | `443` | `https` |
| Email | `User configuration` | `Not specified` | `Not specified` |

### Current user feature limits

| Feature | Publisher value | Scope |
| --- | --- | --- |
| Home + Control scenarios | `100` | Current retained feature HTML; user app, not installer scenario count |
| Notifications | `40` | Current retained feature HTML; installed release not specified |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `840` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `150` - Gateway Open SCS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Object `216` - Enhanced Web Server Audio/Video 2 Wires (F454)

Catalogue Object key `512` maps to external Object `216`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` | Public IP address; public documentation value, not an observed installation |
| `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity |
| `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `VCD_PORT` | `#####` = Video port | `10000` | Video port |
| `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `S_VCT` | `0` = Disable; `1` = Enable | `0` | Voice box videos |
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
| `DIMENSION 1` | Corroborate item model `132` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `150` - Gateway Open SCS | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `216` - Enhanced Web Server Audio/Video 2 Wires (F454) | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `150` - Gateway Open SCS | Integration function | `26` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `216` - Enhanced Web Server Audio/Video 2 Wires (F454) | Integration function | `26` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

### Documented functional scope and canonical references

| Role | Canonical reference | Applicability limit |
| --- | --- | --- |
| Lighting / automation / temperature / energy | [Lighting](../../functional/who-1-lighting/); [Automation](../../functional/who-2-automation/); [Temperature](../../functional/who-4-temperature-control/); [Energy](../../functional/who-18-energy-management/) | Documented system-management families; active installed objects and third-party operations remain scoped separately |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Place the server in the documented SCS automation topology and use Home + Project for commissioning, device association and configuration. The sheet requires the private automation riser at level 3. Devices configured with physical configurators are excluded by the compatibility notes; source-scoped production and F422-interface exceptions must be checked before association. Internet-connected automatic updates and USB-C PC firmware service are documented; neither establishes the installed release. The shared manual separates F460-only Home + Control and burglar-alarm pages from the common commissioning procedures.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

Catalogue Objects 150 and 216 are reusable gateway / web-server definitions. The parenthetical F454 label of Object `216` is not an additional commercial identity and does not make this server an F454. Catalogue V1/R0 is independent of publisher downloadable firmware labels and current server releases. The 2026 English sheets and retained Italian generations differ in compatibility inventory coverage, and both have 30.35 mm depth versus 31.2 mm in the leaflet. The shared July 2024 manual prints 50 scenarios, while the later Italian MyHOME guide says up to 150 installer custom scenarios; limits remain generation-scoped, without an invented firmware boundary. The global product guide and brochure establish the Home + Control role, with integration availability dependent on market and installed system.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `MyHOME Technical Guide.pdf` | Printed/PDF pp. 6, 8-13, 24-26, 32, 82: exact-reference role, system context and catalogue entries; other products/chapters not transferred. |
| `LE13692AC.pdf` | Printed/PDF pp. 1-2: exact-reference specification, connection and configuration content; shared-product content separately scoped. |
| `RA00224AA_EN.pdf` | Printed/PDF pp. 5-13, 44-72, 211-279: limits, roles, topology, commissioning, settings and scoped functional chapters; screenshots not runtime evidence; unrelated UI steps not exhaustively reviewed. |
| `ST-00002701-REV2-EN.pdf` | Printed/PDF pp. 1-7: exact-reference specification, connection and configuration content; shared-product content separately scoped. |
| `F460-publisher-product-sheet.pdf` | PDF pp. 1-5: exact-reference commercial record, EAN and classification values; no printed page sequence established; linked resources are separately accounted for. |
| `F460-myhome-features-ean-publisher-page.html` | Original HTML; sections “An even more flexible and powerful system” and “Creation and management of scenarios”; retrieved 05.10.2026; no pagination. |
| `Home-Project-2026-new-functions.pdf` | Printed/PDF pp. 3-5, 21-29: exact F460/F461 version matrix and commissioning updates; earlier feature descriptions reviewed for applicability, not installed behavior. |
| `RA00224AA_IT.pdf` | Printed/PDF pp. 5-13, 44-72, 211-279: limits, roles, topology, commissioning, settings and scoped functional chapters; screenshots not runtime evidence; unrelated UI steps not exhaustively reviewed. |
| `ST-00002701-IT.pdf` | Printed/PDF pp. 1-7: exact-reference specification, connection and configuration content; shared-product content separately scoped. |
| `F460-italian-product-sheet.pdf` | PDF pp. 1-1: exact-reference commercial record, EAN and classification values; no printed page sequence established; linked resources are separately accounted for. |
| `MyHOME-2025-Italian-guide.pdf` | Printed/PDF pp. 6, 8-13, 24-28, 32, 134: exact-reference role and system context; URL generation 2025 does not establish a single printed release. |
| `Brochure MyHOME.pdf` | PDF pp. 22-24: F460 server/system role; no printed pagination established; no independent F461 operating specification. |

The export dimensions 72 × 105 × 36 mm differ from the sheet 71.5 × 105 × 30.35 mm and leaflet 71.5 × 105 × 31.2 mm. Its supply-current class 3–160 mA is broader than the exact source-specific draw at stated supply voltages. Dimensional measurement basis and revision equivalence remain unresolved.

### Byte-identical publisher aliases

| Discovery filename | Retained original | Reconciliation | Publisher alias |
| --- | --- | --- | --- |
| `F460-F461-historical-RA00211AA-EN.pdf` | `RA00224AA_EN.pdf` | Byte-identical SHA-256; alternate source URL, not another revision | [Alternate publisher response](https://www.bticino.com/sites/default/files/2024-06/RA00211AA_I_EN.pdf) |

The 2026 feature matrix identifies server/app pairs independently of the MyHOME Suite catalogue V/R tuples. Blank F460/F461 cells for older features are unspecified, not zero or proof of absence. Its grouped F460/461 table includes Home + Control deactivation, but the feature description names F460/Classe300EOS only; that user-app operation is not transferred to F461. The group table alone does not override the exact F461 sheet’s third-party-user role.

The retained current manufacturer feature page gives 100 Home + Control user scenarios and 40 notifications. The guide gives 150 installer custom scenarios, while the July 2024 manual gives 50 scenarios without this later role split. The differing counts and generations are retained; no undocumented firmware boundary or universal combined capacity is inferred.

## Evidence limits and open work

Installed release / build, production-specific compatibility, actual capacity under the installed version, third-party payload behavior and endpoints remain uncorroborated. Linked firmware packages and external developer-protocol payloads are explicitly pending inspection; a manufacturer link alone does not establish exact runtime operation.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

### Linked sources outside reviewed evidence

These manufacturer-listed resources are visible discovery work. A listing establishes a source association; it does not establish that the payload was downloaded, verified or examined here.

| Resource | Manufacturer label | Discovery location | Review scope |
| --- | --- | --- | --- |
| `Brochure Living_NOW 2M.pdf` | Brochure BRO-LNOW-2M  /  PDF (15.9 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Brochure%20Living_NOW%202M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Brochure Living_NOW 3M.pdf` | Brochure BRO-LNOW-3M  /  PDF (16.3 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Brochure%20Living_NOW%203M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Catalogue Living_NOW 2M.pdf` | Catalog Commercial Page CAT-LNOW-2M  /  PDF (23.1 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Catalogue%20Living_NOW%202M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Catalogue Living_NOW 3M.pdf` | Catalog Commercial Page CAT-LNOW-3M  /  PDF (22.5 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Catalogue%20Living_NOW%203M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `F460_020012.fwz` | Firmware F460_020012  /  FWZ (151.2 MB) | [Manufacturer link](https://assets.legrand.com/pim/AUTRE/F460_020012.fwz) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `MyHOME_Suite_030538.exe` | Software MYHOME_SUITE_030538  /  EXE (571.7 MB) | [Manufacturer link](https://assets.legrand.com/pim/AUTRE/MyHOME_Suite_030538.exe) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `MyHome_Suite_README_v2.pdf` | Software MYHOME_SUITE_README_V2  /  PDF (551 KB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/AUTRE/MyHome_Suite_README_v2.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |

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
| `MyHOME Technical Guide.pdf` | `a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9` | 23769059 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) |
| `LE13692AC.pdf` | `aff7c4bc2ebed1405feedebdea85f99f8a901e90446b07fe8a64ae704217bea4` | 1701155 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/af/f7/aff7c4bc2ebed1405feedebdea85f99f8a901e90446b07fe8a64ae704217bea4.pdf) |
| `RA00224AA_EN.pdf` | `d2a45bbcd72baa0b6e5536baccca8816cce3cdf94414e7b7144763003c1b1e6d` | 44324781 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/d2/a4/d2a45bbcd72baa0b6e5536baccca8816cce3cdf94414e7b7144763003c1b1e6d.pdf) |
| `ST-00002701-REV2-EN.pdf` | `78ae843060334dbd6d065284c0e5144469d8629633b519585b8daec14deacdc6` | 218474 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/78/ae/78ae843060334dbd6d065284c0e5144469d8629633b519585b8daec14deacdc6.pdf) |
| `F460-publisher-product-sheet.pdf` | `fae334fdd184b1b2f851fb2e670326dea10798243a8a7d85afa1d1a036c35d45` | 717359 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/fa/e3/fae334fdd184b1b2f851fb2e670326dea10798243a8a7d85afa1d1a036c35d45.pdf) |
| `F460-myhome-features-ean-publisher-page.html` | `d86a3cc643cab14b2602759e9e36e3ed53ab669bc7c986339be9b3b75d845893` | 297122 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/d8/6a/d86a3cc643cab14b2602759e9e36e3ed53ab669bc7c986339be9b3b75d845893.pdf) |
| `Home-Project-2026-new-functions.pdf` | `c625bf9b07905fdb71e009ba2e39578b4b42cd7b957576fac87ddc4968b41b40` | 4309300 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/c6/25/c625bf9b07905fdb71e009ba2e39578b4b42cd7b957576fac87ddc4968b41b40.pdf) |
| `RA00224AA_IT.pdf` | `b2f744a263a1b05c002031b3b3eeb6850f3576fe190759a849543d0de8181c08` | 44525957 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/b2/f7/b2f744a263a1b05c002031b3b3eeb6850f3576fe190759a849543d0de8181c08.pdf) |
| `ST-00002701-IT.pdf` | `89a32f3b7bbded41d5417095d918a1b192061a4e4688c1e958abf15061898fb1` | 219150 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/89/a3/89a32f3b7bbded41d5417095d918a1b192061a4e4688c1e958abf15061898fb1.pdf) |
| `F460-italian-product-sheet.pdf` | `ee95d99f8ff3304af10591024346001ea0bb5b0e5268a3d2bf38967b1932800c` | 16576 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/ee/95/ee95d99f8ff3304af10591024346001ea0bb5b0e5268a3d2bf38967b1932800c.pdf) |
| `MyHOME-2025-Italian-guide.pdf` | `0df6729969f31f61feb275e84c7da84c665f8c93aeb1d5af9ba1ac29d4f82e4e` | 32362939 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/0d/f6/0df6729969f31f61feb275e84c7da84c665f8c93aeb1d5af9ba1ac29d4f82e4e.pdf) |
| `Brochure MyHOME.pdf` | `089c3f74e9a9713866f42956811fe779f1d952bb69aad27d6de5c4d689241718` | 2869220 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/08/9c/089c3f74e9a9713866f42956811fe779f1d952bb69aad27d6de5c4d689241718.pdf) |
