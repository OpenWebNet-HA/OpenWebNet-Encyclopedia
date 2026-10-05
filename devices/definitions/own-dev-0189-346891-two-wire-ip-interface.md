# 346891 two-wire to IP interface

## Summary

346891 joins two-wire video-entry risers to an IP backbone for large installations. It supports IP concierge services and advanced address translation, while maintaining separate connections for entrance panels, internal units, SCS power and local power.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0189` | Project identity |
| Technical description | 346891 two-wire to IP interface | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `346891` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1698` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `19` | Main association; independent of project ID |
| Firmware definition | `96` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Gateways and interfaces, Audio video | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `346891` | Established catalogue identity | Manufacturer database commercial record `1762` explicitly links this SKU to item `1698` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `346891` | `8005543502792` | `346891-publisher-product-sheet.pdf` PDF p. 1; `346891-italian-product-sheet.pdf` PDF p. 1 |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `346891-publisher-product-sheet.pdf` | Exact English publisher product export | `Export dated 05.10.2026` | Complete description, product-characteristics and classification tables; exact commercial EAN; linked document / payload inventory remains separately scoped. | [Archived original](https://archive.openwebnet-ha.org/sha256/93/ed/93ed9799d93e4b0879b53c880239a202b596aac3982a82c12e42752c09f2f640.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-346891&include_technical=1) |
| `346891-italian-product-sheet.pdf` | Exact Italian publisher product export | `Export retrieved 05.10.2026; compliance dates are boilerplate` | Exact commercial description and technical attributes; EAN used only if explicitly present; European compliance boilerplate is not a publication revision. | [Archived original](https://archive.openwebnet-ha.org/sha256/3c/fc/3cfcb76b340160131ead91138775d5042c764a287f9f561db1d59e4bd6a076a3.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-346891) |
| `LE05302AA.pdf` | 346891 multilingual installation leaflet | `LE05302AA-01PC-13W29` | PDF pp. 1-3: labelled interfaces, supply / connection drawings and mounting; English blocks reviewed; 346000 accessory drawing separately scoped. | [Archived original](https://archive.openwebnet-ha.org/sha256/3d/31/3d31d8d854febc7d676e51182b3bb1dfe0cb1a12e4ddbe8b29fa70633d70a4b5.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/LE05302AA.pdf) |
| `RA00060AA_S_IT.pdf` | 346891 software manual | `RA00060AA_S_IT; printed publication date not established` | Printed/PDF pp. 4-6, 9-19: configuration transfer / update, general / network / security parameters, base offsets, handset / entrance ranges, switchboards and alarm polling. | [Archived original](https://archive.openwebnet-ha.org/sha256/0c/6f/0c6f1e3cb8b98e85bc6ad7bf7482ec478655247c137fa2973323a6d1a8f114d2.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/RA00060AA_S_IT.pdf) |
| `ST_00000937IT.pdf` | 346891 technical sheet | `ST-00000937-IT; 21/05/2021` | Printed/PDF pp. 1-6: electrical / interface specifications, compatibility, quick / advanced modes, capacities, address translation and topology examples. | [Archived original](https://archive.openwebnet-ha.org/sha256/08/59/085968ebe183ef296d38ae591c73e03938fa3ede57094f982e30dd4d5fc3edaf.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/ST_00000937IT.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1698`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply | `18..27 Vdc` | `ST_00000937IT.pdf` printed/PDF p. 1 |
| SCS standby / operating draw | `35 / 35 mA` | `ST_00000937IT.pdf` printed/PDF p. 1 |
| Local DC standby / maximum draw | `90 / 115 mA` | `ST_00000937IT.pdf` printed/PDF p. 1 |
| Operating temperature | `5..40 °C` | `ST_00000937IT.pdf` printed/PDF p. 1 |
| Mounting | `10 DIN modules` | `ST_00000937IT.pdf` printed/PDF p. 1 |
| Interfaces | `Ethernet 10/100 Mbit; SCS AV IN/AV/AV OUT; local 1-2 supply; micro-USB` | `ST_00000937IT.pdf` printed/PDF p. 1 |
| Indicators / controls | `LINK, SPEED, POWER; reset; physical configurator sockets` | `ST_00000937IT.pdf` printed/PDF p. 1 |
| Software minimum | `Switchboard Suite 4.0.23` | `ST_00000937IT.pdf` printed/PDF p. 1 |
| Excluded combinations | `346890 predecessor; Classe300, Classe300X, Hometouch and Classe300EOS with Netatmo` | `ST_00000937IT.pdf` printed/PDF p. 1 |

| Current export compatibility wording | ONLY Class 100 internal units; not compatible with Classe300EOS or Hometouch | `346891-publisher-product-sheet.pdf` PDF p. 1 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Frequency classifications and a negative connected-object classification do not establish the runtime transport or exclude control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `346891-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `346891-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system radio frequency | `No` | `346891-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system LON | `No` | `346891-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system Powernet | `No` | `346891-publisher-product-sheet.pdf` PDF p. 2 |
| Other bus systems | `Other` | `346891-publisher-product-sheet.pdf` PDF p. 2 |
| Mounting method | `Other` | `346891-publisher-product-sheet.pdf` PDF p. 2 |
| Width in number of modular spacings | `10` | `346891-publisher-product-sheet.pdf` PDF p. 2 |
| With bus connection | `Yes` | `346891-publisher-product-sheet.pdf` PDF p. 2 |
| Logic object | `Yes` | `346891-publisher-product-sheet.pdf` PDF p. 2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1698` | Canonical catalogue |
| Technical item description | IP interface (2Wire/IP) | Canonical catalogue |
| Item family | Source placeholder description `0`; key `20` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `19` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `96` | `1` | `0` | `1` | `1` | Catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `96` | `1` | `92` IP interface (2 wires/IP and D2009/IP) | Fixed / designated metadata | `1304` | `92` | `664` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `96` | Product Programming | `3` | Association key `4` |

| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `96` | USB | `3` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `96` | `1` | `0` | `xml\SDC\sdc.xml` | Parameter type `1`; payload not inspected |
| `96` | `1` | `0` | `1698_1.0_BT\xml\SVM\svm.xml` | Parameter type `2`; payload not inspected |
| `96` | `1` | `0` | `1698_1.0_BT\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `96` | `1` | `0` | `1698_1.0_BT\xml\DIRECTOR\director.xml` | Parameter type `5`; payload not inspected |
| `96` | `1` | `0` | `1698_1.0_BT\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |

Brand / line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| M1 / N1 / M2 / N2 / C | Lower / upper internal-unit address parts `00..99`; M1 also `OFF`; `C=1..9` IP switchboard | `ST_00000937IT.pdf` printed/PDF pp. 2-6 |
| Quick mode 1 | `M1=OFF`; N1/M2/N2 empty; entrance panels / cameras only | `ST_00000937IT.pdf` printed/PDF pp. 2-6 |
| Quick mode 2 | Specified lower / upper internal-unit interval; entrance panels / cameras detected; strict inequalities conflict with inclusive example | `ST_00000937IT.pdf` printed/PDF pp. 2-6 |
| Quick mode 3 | M1 hundreds interval; N1/M2/N2 empty; capacity note wording is ambiguous | `ST_00000937IT.pdf` printed/PDF pp. 2-6 |
| System capacity quick / advanced | Internal units 3900 / 10000; entrance panels 95 / 1000; maximum called address 4000 / 10000 | `ST_00000937IT.pdf` printed/PDF pp. 2-6 |
| IP device / switchboard limits | 100 total IP devices; quick 9 switchboards; advanced subject to total, each PC accounts for `2..4` services | `ST_00000937IT.pdf` printed/PDF pp. 2-6 |
| Advanced address translation | System address = physical address + configured local base; independent handset / entrance-panel / lock offsets | `ST_00000937IT.pdf` printed/PDF pp. 2-6 |
| Advanced functions | Direct entrance-to-handset call; activation redirection; camera cycling | `ST_00000937IT.pdf` printed/PDF pp. 2-6 |
| Cross-hundred example `190..210` | Physical uses two 346851 interfaces; advanced uses physical `1..21` + base 189 | `ST_00000937IT.pdf` printed/PDF pp. 2-6 |
| Software clock / interface ID | Master / slave clock; timezone / date format; unique interface address `1..100000` | `RA00060AA_S_IT.pdf` p. 9 |
| Software authentication | Public password default 12345, `5..9` digits, not an observed credential | `RA00060AA_S_IT.pdf` p. 10 |
| Older software capacity wording | Basic 3999 internal units / 95 entrance panels; “practically unlimited” via base offsets; differs from bounded 2021 technical-sheet capacity table | `RA00060AA_S_IT.pdf` p. 11 |
| Range endpoints / PABX delay | Lower and upper units must physically exist; intermediate addresses may be absent; DOSA forwarding disabled or 10/15/20 seconds; force concierge call optional | `RA00060AA_S_IT.pdf` pp. 12-13 |
| Switchboards / polling | Ordered fallback; handset-specific single address / interval mapping; optional polling frequency and interruption command on non-response | `RA00060AA_S_IT.pdf` pp. 18-19 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `96` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `96` | `M1_1` | `0..3` | `0` | M1_1; Internal Unit Range |
| `96` | `M1_2` | `0..9`; `10` = `OFF` | `0` | M1_2; Internal Unit Range |
| `96` | `N1_1` | `0..9` | `0` | N1_1; Internal Unit Range |
| `96` | `N1_2` | `0..9` | `0` | N1_2; Internal Unit Range |
| `96` | `M2_1` | `0..3` | `0` | M2_1; Internal Unit Range |
| `96` | `M2_2` | `0..9` | `0` | M2_2; Internal Unit Range |
| `96` | `N2_1` | `0..9` | `0` | N2_1; Internal Unit Range |
| `96` | `N2_2` | `0..9` | `0` | N2_2; Internal Unit Range |
| `96` | `C` | `0..9` | `0` | C; Interf2wires Associated SwitchBoard |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `92` - IP interface (2 wires/IP and D2009/IP)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `EXTERNAL_UNIT_MIN` | `0..100090` | Not specified in source | (0-100090) |
| `EXTERNAL_UNIT_MAX` | `0..100090` | Not specified in source | (0-100090) |
| `INTERNAL_UNIT_MIN` | `0..103999` | Not specified in source | (0-103999) |
| `INTERNAL_UNIT_MAX` | `0..103999` | Not specified in source | (0-103999) |

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
| `DIMENSION 1` | Corroborate item model `19` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `92` - IP interface (2 wires/IP and D2009/IP) | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `92` - IP interface (2 wires/IP and D2009/IP) | Integration function | `26` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

### Related functional reference families

The correspondence below is a semantic cross-reference based on the named role and the canonical functional reference; it does not assert captured frames or support for every operation.

| Catalogue role | Related canonical reference | Evidence limit |
| --- | --- | --- |
| Video-entry-related roles | [Basic video entry](../../functional/who-6-basic-video-door-entry/);[Video entry and telephony](../../functional/who-8-video-door-entry-telephony/) | Related canonical families; which namespace and operation applies to each installed component is not established by the product manual alone |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Use the quick or advanced configuration described in `ST_00000937IT.pdf`, printed/PDF pp. 2-6, and the retained MyHOME Suite software manual. Address ranges and base offsets translate physical handset / entrance-panel addresses into system addresses. Physical and software configuration are separate routes; advanced functions include direct calls, activation redirection and camera cycling. The installation leaflet `LE05302AA.pdf` provides connections; firmware transfer uses the documented PC connection.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

This is catalogue item 1698 with its own IP-interface Object and Firmware; it is not the earlier 346890 cluster. Current exact-product technical restrictions override a family-level assumption of compatibility. The product exports corroborate the exact commercial reference and EAN but do not establish the installed release.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `346891-publisher-product-sheet.pdf` | Complete description, product-characteristics and classification tables; exact commercial EAN; linked document / payload inventory remains separately scoped. |
| `346891-italian-product-sheet.pdf` | Exact commercial description and technical attributes; EAN used only if explicitly present; European compliance boilerplate is not a publication revision. |
| `LE05302AA.pdf` | PDF pp. 1-3: labelled interfaces, supply / connection drawings and mounting; English blocks reviewed; 346000 accessory drawing separately scoped. |
| `RA00060AA_S_IT.pdf` | Printed/PDF pp. 4-6, 9-19: configuration transfer / update, general / network / security parameters, base offsets, handset / entrance ranges, switchboards and alarm polling. |
| `ST_00000937IT.pdf` | Printed/PDF pp. 1-6: electrical / interface specifications, compatibility, quick / advanced modes, capacities, address translation and topology examples. |

The older software manual says 3999 basic internal units and describes growth by base offsets as practically unlimited; the 2021 sheet gives explicit quick / advanced capacities of 3900/10000. The wording and publication scopes remain separate. The 2013 leaflet draws a 346000 power supply, while the 2021 sheet uses 346050; accessory revisions are not silently substituted. The current product export further limits internal units to Class 100.

## Evidence limits and open work

Installed Switchboard Suite/Firmware compatibility, IP-service allocation, commissioning topology and electrical terminal capacity require corroboration; public installation examples are not hardware captures.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

### Linked sources outside reviewed evidence

These manufacturer-listed resources are visible discovery work. A listing establishes a source association; it does not establish that the payload was downloaded, verified or examined here.

| Resource | Manufacturer label | Discovery location | Review scope |
| --- | --- | --- | --- |
| `INTERF2FIP_010617.fwz` | Firmware INTERF2FIP_010617  /  FWZ (60.8 MB) | [Manufacturer link](https://assets.legrand.com/pim/AUTRE/INTERF2FIP_010617.fwz) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
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
| `346891-publisher-product-sheet.pdf` | `93ed9799d93e4b0879b53c880239a202b596aac3982a82c12e42752c09f2f640` | 404075 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/93/ed/93ed9799d93e4b0879b53c880239a202b596aac3982a82c12e42752c09f2f640.pdf) |
| `346891-italian-product-sheet.pdf` | `3cfcb76b340160131ead91138775d5042c764a287f9f561db1d59e4bd6a076a3` | 18542 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/3c/fc/3cfcb76b340160131ead91138775d5042c764a287f9f561db1d59e4bd6a076a3.pdf) |
| `LE05302AA.pdf` | `3d31d8d854febc7d676e51182b3bb1dfe0cb1a12e4ddbe8b29fa70633d70a4b5` | 504289 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/3d/31/3d31d8d854febc7d676e51182b3bb1dfe0cb1a12e4ddbe8b29fa70633d70a4b5.pdf) |
| `RA00060AA_S_IT.pdf` | `0c6f1e3cb8b98e85bc6ad7bf7482ec478655247c137fa2973323a6d1a8f114d2` | 6324454 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/0c/6f/0c6f1e3cb8b98e85bc6ad7bf7482ec478655247c137fa2973323a6d1a8f114d2.pdf) |
| `ST_00000937IT.pdf` | `085968ebe183ef296d38ae591c73e03938fa3ede57094f982e30dd4d5fc3edaf` | 1387570 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/08/59/085968ebe183ef296d38ae591c73e03938fa3ede57094f982e30dd4d5fc3edaf.pdf) |
