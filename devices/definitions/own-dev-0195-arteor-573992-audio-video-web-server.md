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

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `legrand-WHO-25.pdf` | `WHO 25` dry-contact / IR protocol specification | `Version 1.0.0; 01/11/2010` | Printed/PDF p. 13: explicit 573992 / F453AV firmware 2.1.7 applicability; protocol descriptions do not supply electrical ratings. | [Archived original](https://archive.openwebnet-ha.org/sha256/12/2d/122d9c1a43e1610a43eaeac3f61feefbdb1fd5ff377041e216c82a802eba4927.pdf) | [Publisher original](https://developer.legrand.com/uploads/2019/12/WHO_25.pdf) |
| `legrand-WHO-15-25.pdf` | `CEN` and `CEN`+ protocol specification | `Version 1.0.0; 01/10/2010` | Printed/PDF p. 24: 573992 / F453AV version 2.1.7 `CEN`/`CEN` pressure/`CEN`+ support table; protocol scope only. | [Archived original](https://archive.openwebnet-ha.org/sha256/8b/f0/8bf06ff1394615dbf6d46a1fc8b9c53573ed96f1c1b112b2dd8a6021faf3dd21.pdf) | [Publisher original](https://developer.legrand.com/uploads/2019/12/WHO_15-25.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1834`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Published version-scoped protocol reference | `573992 at version 2.1.7, listed alongside F453AV` | `legrand-WHO-25.pdf` printed/PDF p. 13; `legrand-WHO-15-25.pdf` printed/PDF p. 24; canonical item `1834` |
| `CEN` / pressure / `CEN`+ table | `Version 2.1.7: yes / yes / yes, manufacturer CEN document` | `legrand-WHO-25.pdf` printed/PDF p. 13; `legrand-WHO-15-25.pdf` printed/PDF p. 24; canonical item `1834` |
| Dry-contact / IR-state family | `Version 2.1.7 shown as a gateway allowing the function` | `legrand-WHO-25.pdf` printed/PDF p. 13; `legrand-WHO-15-25.pdf` printed/PDF p. 24; canonical item `1834` |
| Exact SKU electrical / mechanical ratings | `Not established by retained exact-product sheet` | `legrand-WHO-25.pdf` printed/PDF p. 13; `legrand-WHO-15-25.pdf` printed/PDF p. 24; canonical item `1834` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1834` | Canonical catalogue |
| Technical item description | Webserver Audio/Video DIN | Canonical catalogue |
| Item family | Source placeholder description `0`; key `8` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `38` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `100` | `3` | `0` | `7` | `2` | Catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

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
| `100` | Product Programming | `3` | Association key `4` |

| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `100` | Ethernet | `2` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `100` | `2` | `0` | `xml\SDC\sdc.xml` | Parameter type `1`; payload not inspected |
| `100` | `2` | `0` | `1834_3.0_LG\xml\SVM\svm.xml` | Parameter type `2`; payload not inspected |
| `100` | `2` | `0` | `1834_3.0_LG\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `100` | `2` | `0` | `1834_3.0_LG\xml\DIRECTOR\director.xml` | Parameter type `5`; payload not inspected |
| `100` | `2` | `0` | `1834_3.0_LG\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |
| `100` | `2` | `2` | `xml\SDC\sdc.xml` | Parameter type `1`; payload not inspected |
| `100` | `2` | `2` | `1834_3.0_LG\xml\SVM\svm.xml` | Parameter type `2`; payload not inspected |
| `100` | `2` | `2` | `1834_3.0_LG\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `100` | `2` | `2` | `1834_3.0_LG\xml\DIRECTOR\director.xml` | Parameter type `5`; payload not inspected |
| `100` | `2` | `2` | `1834_3.0_LG\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |

Brand / line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Firmware `2`.1.7 applicability | 573992 explicitly named with F453AV | `legrand-WHO-25.pdf` printed/PDF p. 13; `legrand-WHO-15-25.pdf` p. 24 |
| `CEN` / `CEN` pressure / `CEN`+ | Yes / yes / yes in version-scoped protocol table | `legrand-WHO-25.pdf` printed/PDF p. 13; `legrand-WHO-15-25.pdf` p. 24 |
| Dry-contact/IR states | Gateway allowing this family at 2.1.7 | `legrand-WHO-25.pdf` printed/PDF p. 13; `legrand-WHO-15-25.pdf` p. 24 |
| Programming sequence | Exact product installation / transfer procedure unestablished by these protocol documents | `legrand-WHO-25.pdf` printed/PDF p. 13; `legrand-WHO-15-25.pdf` p. 24 |

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

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Use the exact catalogue firmware, mode and connection associations below when locating the programming tool. The manufacturer protocol tables provide version-scoped gateway applicability; they do not provide an installation or project-transfer sequence for 573992. Do not assign a later server’s software or electrical specification merely because the gateway family is related.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The protocol documents explicitly associate 573992 with F453AV at 2.1.7 for their respective functions. This scoped equivalence supports protocol-family applicability, not wholesale electrical or mechanical identity. The retained canonical Firmware tuple must be compared independently with the protocol version; no installed response or unlisted operation is established.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `legrand-WHO-25.pdf` | Printed/PDF p. 13: explicit 573992 / F453AV firmware 2.1.7 applicability; protocol descriptions do not supply electrical ratings. |
| `legrand-WHO-15-25.pdf` | Printed/PDF p. 24: 573992 / F453AV version 2.1.7 `CEN`/`CEN` pressure/`CEN`+ support table; protocol scope only. |

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

### Retained original fingerprints

All incorporated originals were checked against the public archive by SHA-256 and byte length. Their manifest registrations were pushed on main before incorporation; previously registered originals were reused by fingerprint.

| Original | SHA-256 | Retention / size |
| --- | --- | --- |
| `legrand-WHO-25.pdf` | `122d9c1a43e1610a43eaeac3f61feefbdb1fd5ff377041e216c82a802eba4927` | 425272 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/12/2d/122d9c1a43e1610a43eaeac3f61feefbdb1fd5ff377041e216c82a802eba4927.pdf) |
| `legrand-WHO-15-25.pdf` | `8bf06ff1394615dbf6d46a1fc8b9c53573ed96f1c1b112b2dd8a6021faf3dd21` | 931576 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/8b/f0/8bf06ff1394615dbf6d46a1fc8b9c53573ed96f1c1b112b2dd8a6021faf3dd21.pdf) |
