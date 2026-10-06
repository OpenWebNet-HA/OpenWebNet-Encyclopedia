# OPEN and BACnet gateway

## Summary

This DIN gateway connects MyHOME OPEN functions with BACnet integration for configured heating, cooling and ventilation equipment. Its Ethernet connection and dedicated project software define the network identities and equipment mappings, with exact BACnet interoperability still requiring corroboration.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0138` | Project identity |
| Technical description | OPEN and BACnet gateway | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `F450`, `003597` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1556` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `52` | Main association; independent of project ID |
| Firmware definition | `124`, `90` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Gateways and interfaces, Thermoregulation | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F450` | Established catalogue identity | Manufacturer database commercial record `1562` explicitly links this SKU to item `1556` |
| Legrand | `003597` | Established catalogue identity | Manufacturer database commercial record `1656` explicitly links this SKU to item `1556` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F450` | `8005543488430` | [Archived original](https://archive.openwebnet-ha.org/sha256/2a/4e/2a4e430f07b33fdb901541000cc66e751fe6e99097d4b42c725ca8f4bbb1673a.pdf), `F450-publisher-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

### Catalogue labels and classifications

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `F450` | Gateway OPEN-BACNET | Canonical commercial record `1562` |
| `003597` | Gateway OPEN-BACNET | Canonical commercial record `1656` |

Both commercial records are enabled for catalogue display, have no visibility-type value, and are not marked dependent or gateway in this historical commercial table. These classifications do not establish market availability, installed state or functional gateway capability. Empty or truncated internal description labels are not used to infer additional product features.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MyHOME-Technical-Guide.pdf` | English system technical guide | `AD-EXMH25GT; Versione 6/2025 printed on rear cover` | AD-EXMH25GT, Versione 6/2025 rear-cover label; exact F524 entry printed/PDF p. 101 examined. No exact 3456/F450 match; other product ratings/wiring excluded from those items. | [Archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) | [Publisher original](https://www.bticino.com/sites/default/files/2024-02/MyHOME%20Technical%20Guide.pdf) |
| `LE05271AB.pdf` | Instruction Use LE05271AB | `LE05271AB-01PC-13W02` | Exact F450 one-page multilingual instruction; English interfaces/LED/2-wire-bus labels examined; generic Web Server/video-bus wording does not expand product scope. | [Archived original](https://archive.openwebnet-ha.org/sha256/ac/e5/ace54f437f59d280d26b053eb0c54c087d65c210d7fc1fa1b4b946cbe700fa63.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/LE05271AB.pdf) |
| `MQ01008-a-EN.pdf` | Technical Sheet MQ01008-A-EN | `MQ01008-a-EN; 07/06/2014` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-1; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/fa/2f/fa2f3e244efc271c815cab4db48a75609c84ea0d054e078b3d470a712987de78.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MQ01008-a-EN.pdf) |
| `RA00058AC_S_EN.pdf` | Technical Guide RA00058AC_S_EN | `RA00058AC_S_EN; source filename revision; printed publication date not established` | Exact F450 TiOpenBacnet 16-page software manual examined in full; transfer/project/network/clock/IDs/authentication and six HVAC classes. | [Archived original](https://archive.openwebnet-ha.org/sha256/6d/5f/6d5f2aa56dd67df6fb78451b3194d577e51aa2492ef229572c0c5fc4dda74c08.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00058AC_S_EN.pdf) |
| `RA00058AD_S_EN.pdf` | Technical Guide RA00058AD_S_EN | `RA00058AD_S_EN; source filename revision; printed publication date not established` | Exact F450 Gateway OpenBacnet 16-page software manual examined in full; revised Configure workflow and eight HVAC classes; erroneous MH202/Web Server introductory wording recorded. | [Archived original](https://archive.openwebnet-ha.org/sha256/fa/c2/fac205ca4b7ced796ae40b5a2c619b33df019df11298514327d348d449cecea4.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00058AD_S_EN.pdf) |
| `F450-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 04.10.2026` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-3; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/2a/4e/2a4e430f07b33fdb901541000cc66e751fe6e99097d4b42c725ca8f4bbb1673a.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-F450&include_technical=1) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `1556` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply | `18..27 Vdc` | `MQ01008-a-EN` p. 1 |
| Maximum draw | `55 mA` | `MQ01008-a-EN` p. 1 |
| Operating temperature | `5..45 °C` | `MQ01008-a-EN` p. 1 |
| Mounting | `6 DIN modules` | `MQ01008-a-EN` p. 1 |
| LAN | `RJ45; 10/100 Mbit/s` | `MQ01008-a-EN` p. 1 |
| USB | `configuration and firmware updating` | `MQ01008-a-EN` p. 1 |
| Published HVAC classes | `AC units; fan coils; air-treatment units; VRV/VAV; underfloor heating; probes; thermostats; generic units` | `MQ01008-a-EN` p. 1 |
| Indicators | `system operation; speed ON=100 Mbit/s, OFF=10 Mbit/s; Ethernet link` | `MQ01008-a-EN` p. 1 |

### Publisher export attributes

These are the captured publisher classification values for the named variants. They do not override a technical sheet’s ratings or prove runtime protocol support. A negative radio-bus/connected-object classification is not evidence against separately documented gateway or Wi-Fi behavior.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `F450` export p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `F450` export p. 2 |
| Bus system radio frequency | `No` | `F450` export p. 2 |
| Bus system LON | `No` | `F450` export p. 2 |
| Bus system Powernet | `No` | `F450` export p. 2 |
| Other bus systems | `Other` | `F450` export p. 2 |
| Model | `Ethernet interface` | `F450` export p. 2 |
| Mounting method | `DRA (DIN-rail adaptor)` | `F450` export p. 2 |
| Width in number of modular spacings | `6` | `F450` export p. 2 |
| Demounting protection | `No` | `F450` export p. 2 |
| With LED indication | `Yes` | `F450` export p. 2 |
| Updateable | `Yes` | `F450` export p. 2 |
| Operating voltage (Min-Max) | `27-27 V` | `F450` export p. 2 |
| Protocol | `Other` | `F450` export p. 2 |
| Provider dependent | `No` | `F450` export p. 2 |
| Visualization | `No` | `F450` export p. 2 |
| Web-Server | `No` | `F450` export p. 2 |
| Radio interface | `No` | `F450` export p. 2 |
| IR interface | `No` | `F450` export p. 2 |
| Degree of protection (IP) | `IP20` | `F450` export p. 2 |
| Type of load | `Not applicable` | `F450` export p. 2 |
| Connection type | `Screwed terminal` | `F450` export p. 2 |
| Connected object | `No` | `F450` export p. 2 |
| Programming way | `Smartphone apps` | `F450` export p. 2 |
| With voice command | `Yes` | `F450` export p. 2 |
| Programmable | `Yes` | `F450` export p. 2 |
| Interoperable connection Protocol | `No` | `F450` export p. 2 |
| Connectable by Internet box | `No` | `F450` export p. 2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1556` | Canonical catalogue |
| Technical item description | Gateway OPEN-BACNET | Canonical catalogue |
| Item family | 0; key `8` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `52` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `52` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Burglar alarm | private riser | Canonical item/bus relationship |
| Multimedia | private riser | Canonical item/bus relationship |
| Multimedia | public riser | Canonical item/bus relationship |
| Network | LAN | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `90` | `1` | `0` | `1` | `1` | Not catalogue default | Official |
| `124` | `2` | `0` | `0` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `90` | `73` | BTicino (key `1`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `90` | `74` | BTicino (key `1`) | `0` | SVM | `1556_1.0_BT\xml\SVM\svm.xml` |
| `90` | `75` | BTicino (key `1`) | `0` | Extra | `1556_1.0_BT\xml\Extra\extra.xml` |
| `90` | `76` | BTicino (key `1`) | `0` | Director | `1556_1.0_BT\xml\DIRECTOR\director.xml` |
| `90` | `77` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1556_1.0_BT\xml\Protocol\protocol.xml` |
| `90` | `514` | Legrand (key `2`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `90` | `515` | Legrand (key `2`) | `0` | SVM | `1556_1.0_LG\xml\SVM\svm.xml` |
| `90` | `516` | Legrand (key `2`) | `0` | Extra | `1556_1.0_LG\xml\Extra\extra.xml` |
| `90` | `517` | Legrand (key `2`) | `0` | Director | `1556_1.0_LG\xml\DIRECTOR\director.xml` |
| `90` | `518` | Legrand (key `2`) | `0` | Protocol and other device parameters | `1556_1.0_LG\xml\Protocol\protocol.xml` |
| `124` | `243` | BTicino (key `1`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `124` | `244` | BTicino (key `1`) | `0` | Director | `1556_2.0_BT\xml\DIRECTOR\director.xml` |
| `124` | `245` | BTicino (key `1`) | `0` | Extra | `1556_2.0_BT\xml\Extra\extra.xml` |
| `124` | `246` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1556_2.0_BT\xml\Protocol\protocol.xml` |
| `124` | `247` | BTicino (key `1`) | `0` | SVM | `1556_2.0_BT\xml\SVM\svm.xml` |
| `124` | `816` | Legrand (key `2`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `124` | `817` | Legrand (key `2`) | `0` | SVM | `1556_2.0_LG\xml\SVM\svm.xml` |
| `124` | `818` | Legrand (key `2`) | `0` | Extra | `1556_2.0_LG\xml\Extra\extra.xml` |
| `124` | `819` | Legrand (key `2`) | `0` | Director | `1556_2.0_LG\xml\DIRECTOR\director.xml` |
| `124` | `820` | Legrand (key `2`) | `0` | Protocol and other device parameters | `1556_2.0_LG\xml\Protocol\protocol.xml` |

All 20 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `90` | `1` | `220` Gateway OPEN-BACNET | Fixed/designated metadata | `1307` | `531` | `667` |
| `124` | `1` | `220` Gateway OPEN-BACNET | Fixed/designated metadata | `1308` | `531` | `668` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `90` | Product Programming | `3` | Canonical firmware/mode association |
| `124` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `90` | Ethernet | Canonical firmware/connection association |
| `90` | USB | Canonical firmware/connection association |
| `124` | Ethernet | Canonical firmware/connection association |
| `124` | USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `124` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `124` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `124` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `124` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `124` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `90` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `90` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `90` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `90` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `90` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `220` - Gateway OPEN-BACNET

Catalogue Object key `531` maps to external Object `220`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |

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

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `52` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `220` - Gateway OPEN-BACNET | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |

These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Use TiOpenBacnet / Gateway OpenBacnet software to create, send or receive a project, request device information and update firmware. Connect USB-miniUSB or Ethernet with the SCS bus powered; direct Ethernet uses a crossover cable according to the sheet. Configure unique OPEN gateway and BACnet identities separately, network parameters, clock-master/time zone, authentication and up to ten authorized IP ranges. Assign the MyHOME area/address, description (<=15 characters) and available BACnet HVAC units. BACnet points and the OpenWebNet-facing gateway identity are distinct namespaces.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

AC pp. 7–10 distinguishes Send Configuration (PC to device), Receive Configuration (device to PC), `.fwz` firmware update and Device Info. AD pp. 5–9 reorganizes the same operations into the global Configure area, with firmware selection before the update button appears and date/time set when sending. AC p. 15 lists generic units, fan coils, AC units, ATU, VRV/VAV and underfloor heating; AD p. 15 additionally lists probes and thermostats. Keep the supported UI edition explicit rather than backdating these two classes to AC. Both manuals require a fixed unique network address and distinguish the OPEN password/IP-range bypass from the BACnet ID. Up to ten enabled IP ranges can connect without the OPEN password; this is an access setting, not a guarantee of authenticated operation or a complete BACnet service/point map.

## Source reconciliation

F450/003597 catalogue identity and OPEN/BACnet role agree with the exact sheet and instructions. AC and AD software manuals retain the network, clock, gateway-ID and BACnet-ID settings while reorganizing the application workflow; AD extends the published HVAC classes with probes and thermostats. AD erroneously calls this an MH202 scenario programmer/Web Server in generic introductory prose despite its F450 cover and diagrams; this is a source-editing defect, not a device identity conflict. The manufacturer-linked general guide does not name F450 and supplies no exact rating. Historical firmware definitions `90` and `124` remain distinct from document revisions AC/AD.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `MyHOME-Technical-Guide.pdf` | June 2025 shared energy guide: wiring, load control and consumption topology; no exact 3456/F450 match and no specifications transferred to those products. |
| `LE05271AB.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `MQ01008-a-EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `RA00058AC_S_EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `RA00058AD_S_EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `F450-publisher-product-sheet.pdf` | Captured exact-variant identity and complete technical classification attributes tabulated above; document links are discovery provenance, not additional independently verified capability. |

### Semantic review findings

Two official firmware definitions (`90`=`1.0.1`, nondefault; `124`=`2.0.0`, default) each place one fixed Object `220` and retain all twenty parameter associations and four USB/Ethernet connections. There are no Virgin, slot condition, filter or conversion associations. A reusable `FW_VER=3.0.0` default is not an installed or supported release claim. AC software lists six HVAC classes; AD adds probes and thermostats. Both distinguish the unique OPEN gateway identifier, BACnet identifier and screen area/address. AD's introductory MH202/Web Server references and LE05271AB's Web Server/video-bus labels are generic source defects, not evidence of a scenario programmer or a web-server feature; the exact F450 sheet controls product scope. Current export attributes `Smartphone apps`/`With voice command=Yes` are classification metadata, not proof of direct voice capture or standalone smartphone commissioning. Linked `F450_020010` and production firmware payloads are unexamined and not equated to an installed `2.0.10` tuple. The shared energy guide lacks an exact F450 match and supplies no ratings.

## Evidence limits and open work

BACnet object/property mapping and supported service details, installed gateway firmware, exact authentication/diagnostic traffic and interoperability captures remain uncorroborated.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0131-0140-2026-10-06.md#own-dev-0138)
