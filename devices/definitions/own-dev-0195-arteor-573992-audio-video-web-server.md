# Arteor 573992 audio and video web server

## Summary

Arteor 573992 is the Legrand audio / video web-server reference in the catalogue. It combines an audio / video server Object with an Open SCS gateway role, enabling integration with configured MyHOME functions; manufacturer protocol documents describe some capabilities by firmware version.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0195` | Project identity |
| Technical description | Arteor 573992 audio and video web server | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `573992` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1834` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `38` | Main association; independent of project ID |
| Firmware definition | `100` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `2` | Firmware metadata |
| Categories | Gateways and interfaces, Audio video, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand - Arteor | `573992` | Established catalogue identity | Manufacturer database commercial record `1976` explicitly links this SKU to item `1834` |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `573992` | Webserver Audio/Video DIN | Canonical commercial record `1976` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `WHO_25.pdf` | `WHO 25` dry-contact / IR protocol specification | `Version 1.0.0; 01/11/2010` | Printed/PDF p. 13: explicit 573992 / F453AV firmware 2.1.7 applicability; protocol descriptions do not supply electrical ratings. | [Archived original](https://archive.openwebnet-ha.org/sha256/12/2d/122d9c1a43e1610a43eaeac3f61feefbdb1fd5ff377041e216c82a802eba4927.pdf) | [Publisher original](https://developer.legrand.com/uploads/2019/12/WHO_25.pdf) |
| `WHO_15-25.pdf` | `CEN` and `CEN`+ protocol specification | `Version 1.0.0; 01/10/2010` | Printed/PDF p. 24: 573992 / F453AV version 2.1.7 `CEN`/`CEN` pressure/`CEN`+ support table; protocol scope only. | [Archived original](https://archive.openwebnet-ha.org/sha256/8b/f0/8bf06ff1394615dbf6d46a1fc8b9c53573ed96f1c1b112b2dd8a6021faf3dd21.pdf) | [Publisher original](https://developer.legrand.com/uploads/2019/12/WHO_15-25.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1834`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

No exact 573992 electrical/mechanical sheet is retained. Dimensions, supply, draw and physical connector allocation remain unestablished; protocol support belongs under Functional applicability.

| Property | Value | Evidence |
| --- | --- | --- |
| Supply, current draw, dimensions and physical connectors | Not established | No retained exact-product electrical/mechanical sheet; the protocol documents establish version-scoped functions only |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1834` | Canonical catalogue |
| Technical item description | Webserver Audio/Video DIN | Canonical catalogue |
| Item family | Source placeholder description `0`; key `8` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `38` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `38` | Yes | Canonical item/system relationship |

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
| `100` | `3` | `0` | `7` | `2` | Catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `100` | `147` | Legrand (key `2`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `100` | `148` | Legrand (key `2`) | `0` | SVM | `1834_3.0_LG\xml\SVM\svm.xml` |
| `100` | `149` | Legrand (key `2`) | `0` | Extra | `1834_3.0_LG\xml\Extra\extra.xml` |
| `100` | `150` | Legrand (key `2`) | `0` | Director | `1834_3.0_LG\xml\DIRECTOR\director.xml` |
| `100` | `151` | Legrand (key `2`) | `0` | Protocol and other device parameters | `1834_3.0_LG\xml\Protocol\protocol.xml` |
| `100` | `173` | Legrand (key `2`) | `2` | SDC | `xml\SDC\sdc.xml` |
| `100` | `174` | Legrand (key `2`) | `2` | SVM | `1834_3.0_LG\xml\SVM\svm.xml` |
| `100` | `175` | Legrand (key `2`) | `2` | Extra | `1834_3.0_LG\xml\Extra\extra.xml` |
| `100` | `176` | Legrand (key `2`) | `2` | Director | `1834_3.0_LG\xml\DIRECTOR\director.xml` |
| `100` | `177` | Legrand (key `2`) | `2` | Protocol and other device parameters | `1834_3.0_LG\xml\Protocol\protocol.xml` |

All 10 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

Catalogue-default Official firmware `100` is `3.0.7`, with fixed/designated Object `56` in slot `1` and `150` in slot `2`. The item default `FW_VER=3.0.0` and reusable Object `56` default `1.0.0` remain distinct configuration defaults. No relation filter resolves that difference; neither value is a release record. The two `IS_GATEWAY=0` defaults do not negate the manufacturer’s version-scoped gateway role. Public documentation network and port defaults are templates, not observed deployment endpoints.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `100` | `1` | `56` Web Server Audio / Video 2 Wires (F453AV) | Fixed / designated metadata | `1336` | `56` | `695` |
| `100` | `2` | `150` Gateway Open SCS | Fixed / designated metadata | `1337` | `150` | `696` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `100` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `100` | Ethernet | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Firmware `2.1.7` applicability | 573992 explicitly named with F453AV | `WHO_25.pdf` printed/PDF p. 13; `WHO_15-25.pdf` p. 24 |
| `CEN` / `CEN` pressure / `CEN`+ | Yes / yes / yes in version-scoped protocol table | `WHO_25.pdf` printed/PDF p. 13; `WHO_15-25.pdf` p. 24 |
| Dry-contact/IR states | Gateway allowing this family at 2.1.7 | `WHO_25.pdf` printed/PDF p. 13; `WHO_15-25.pdf` p. 24 |
| Programming sequence | Exact product installation / transfer procedure unestablished by these protocol documents | `WHO_25.pdf` printed/PDF p. 13; `WHO_15-25.pdf` p. 24 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `100` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `100` | `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway; Boolean flag for Gateway device |
| `100` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `100` | `VCD_PORT` | `#####` = Video port | `10000` | Video port; VIdeo port |
| `100` | `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `100` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `100` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity; Local Dynamic IP |
| `100` | `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` | Public IP address; public documentation value, not an observed installation |
| `100` | `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity; Public Dynamic IP |
| `100` | `S_VCT` | `0` = Disable; `1` = Enable | `0` | Voice box videos; Voice Box Vds |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `56` - Web Server Audio / Video 2 Wires (F453AV)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` | Public IP address; public documentation value, not an observed installation |
| `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity |
| `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `VCD_PORT` | `#####` = Video port | `10000` | Video port |
| `FW_VER` | `######` = Firmware version | `1.0.0` | Firmware version |
| `S_VCT` | `0` = Disable; `1` = Enable | `0` | Voice box videos |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Object `150` - Gateway Open SCS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
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
| `DIMENSION 1` | Corroborate item model `38` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `56` - Web Server Audio / Video 2 Wires (F453AV) | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `150` - Gateway Open SCS | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `56` - Web Server Audio / Video 2 Wires (F453AV) | Integration function | `26` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `150` - Gateway Open SCS | Integration function | `26` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

### Related functional reference families

The correspondence below is a semantic cross-reference based on the named role and the canonical functional reference; it does not assert captured frames or support for every operation.

| Catalogue role | Related canonical reference | Evidence limit |
| --- | --- | --- |
| Video-entry-related roles | [Basic video entry](../../functional/who-6-basic-video-door-entry/);[Video entry and telephony](../../functional/who-8-video-door-entry-telephony/) | Related canonical families; which namespace and operation applies to each installed component is not established by the product manual alone |

### Published firmware-specific gateway support

| Property | Value | Evidence |
| --- | --- | --- |
| Published version-scoped protocol reference | `573992 at version 2.1.7, listed alongside F453AV` | `WHO_25.pdf` printed/PDF p. 13; `WHO_15-25.pdf` printed/PDF p. 24; canonical item `1834` |
| `CEN` / pressure / `CEN`+ table | `Version 2.1.7: yes / yes / yes, manufacturer CEN document` | `WHO_25.pdf` printed/PDF p. 13; `WHO_15-25.pdf` printed/PDF p. 24; canonical item `1834` |
| Dry-contact / IR-state family | `Version 2.1.7 shown as a gateway allowing the function` | `WHO_25.pdf` printed/PDF p. 13; `WHO_15-25.pdf` printed/PDF p. 24; canonical item `1834` |

The two protocol tables establish the named functions at `573992 v2.1.7`. They do not establish a blanket support matrix for every release or make F453AV a commercial alias of 573992.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Use the exact catalogue firmware, mode and connection associations below when locating the programming tool. The manufacturer protocol tables provide version-scoped gateway applicability; they do not provide an installation or project-transfer sequence for 573992. Do not assign a later server’s software or electrical specification merely because the gateway family is related.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The protocol documents explicitly associate 573992 with F453AV at 2.1.7 for their respective functions. This scoped equivalence supports protocol-family applicability, not wholesale electrical or mechanical identity. The retained canonical Firmware tuple must be compared independently with the protocol version; no installed response or unlisted operation is established.

Repeat manufacturer/historical/regional searches found a support-page lead for this exact server, but direct retrieval returned only a temporarily unavailable product-search component. Its indexed firmware lead was not adopted or archived as functioning product evidence. No exact electrical sheet or installation manual was recovered; the retained manufacturer protocol tables remain the bounded product evidence.

## Evidence limits and open work

Exact 573992 installation, technical and user originals, EAN, supply / draw, enclosure size and actual functional sessions remain documentation / corroboration gaps.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0191-0200-2026-10-07.md#own-dev-0195)
