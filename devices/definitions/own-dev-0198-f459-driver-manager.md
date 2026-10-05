# F459 Driver Manager

## Summary

F459 Driver Manager connects MyHOME equipment to third-party systems through installed integration drivers. Its web interface configures the platform and drivers; the manufacturer sheet describes a preinstalled MyHOME–Nuvo driver and separately acquired drivers for other integrations.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0198` | Project identity |
| Technical description | F459 Driver Manager | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `F459` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `2193` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `65` | Main association; independent of project ID |
| Firmware definition | `721`, `811` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Gateways and interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F459` | Established catalogue identity | Manufacturer database commercial record `2546` explicitly links this SKU to item `2193` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F459` | `8005543547861` | `F459-publisher-product-sheet.pdf` PDF p. 1 |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MM00883-a-EN.pdf` | F459 Driver Manager technical sheet | `MM00883-a; 10/03/2016` | Printed/PDF p. 1: exact F459 interfaces, supply / draw / temperature / mounting, driver scope and published web configuration endpoint. | [Archived original](https://archive.openwebnet-ha.org/sha256/5c/f5/5cf5493496f59ca1c8529f2309703c7b66d7a07d44b57d2db3fb9a36ab5b9676.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MM00883-a-EN.pdf) |
| `MyHOME Technical Guide.pdf` | MyHOME technical guide | `GUI-MHOME; printed publication date not established` | PDF pp. 25, 60, 71-72, 82: exact F459 integration references; pp. 48, 54-58, 86-87, 99: K4652M2 configuration / application examples. Family examples are not measured behavior. | [Archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MyHOME%20Technical%20Guide.pdf) |
| `RA00147AA_I_EN.pdf` | F459 / 003549 installation manual | `RA00147AA_I; printed publication date not established` | Printed/PDF pp. 6-19: authentication / driver lifecycle / platform configuration; pp. 20-47: Nuvo zones, sources, scenarios and diagnostics. Driver scope remains conditional. | [Archived original](https://archive.openwebnet-ha.org/sha256/e9/c6/e9c6759990488cbc2c5923bded48f71ea196657a87b358b17e8d080964abfa9b.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00147AA_I_EN.pdf) |
| `F459-publisher-product-sheet.pdf` | Exact English publisher product export | `Export dated 05.10.2026` | Complete description, product-characteristics and classification tables; exact commercial EAN; linked document / payload inventory remains separately scoped. | [Archived original](https://archive.openwebnet-ha.org/sha256/56/25/56250d59925cbc58fb2f2c36a2cdea569755c58c76d9b5b3994081761cafd70a.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-F459&include_technical=1) |
| `legrand-living-now-historical.pdf` | Historical Living Now/MyHOME catalogue | `Printed publication date not established` | Printed/PDF pp. 35, 92, 94-95, 98: exact MyHOMEServer1, F459, K4652M2 and 048834 catalogue descriptions; p. 98 PIR settings and internal threshold / timing discrepancy. | [Archived original](https://archive.openwebnet-ha.org/sha256/f7/2a/f72ab15db14eea29dd1693203fa242c32213717b596bcee9fd2ee96ce7d53e71.pdf) | [Publisher original](https://assets.legrand.com/webf/bg/bg_en_Living_NOW_catalogue.pdf) |
| `MM00883_a_IT.pdf` | F459 Driver Manager technical sheet | `MM00883-a; 10/03/2016` | Printed/PDF p. 1: exact F459 interfaces, supply / draw / temperature / mounting, driver scope and published web configuration endpoint. | [Archived original](https://archive.openwebnet-ha.org/sha256/13/8c/138c8523735e23dc2ac6fd877ec0af2542a2861cf7aa3073285ed13bfe11622f.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/MM00883_a_IT.pdf) |
| `RA00147AA_I_IT.pdf` | F459 / 003549 installation manual | `RA00147AA_I; printed publication date not established` | Printed/PDF pp. 6-19: authentication / driver lifecycle / platform configuration; pp. 20-47: Nuvo zones, sources, scenarios and diagnostics. Driver scope remains conditional. | [Archived original](https://archive.openwebnet-ha.org/sha256/7a/76/7a767d2e4a8cea7490a71cb8d70a0acd8f9f1103dee3570e4cd11f670e3b687d.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/RA00147AA_I_IT.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2193`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / maximum draw | `18..27 Vdc from SCS; 125 mA with active video interface` | `MM00883-a-EN.pdf` printed/PDF p. 1 |
| Operating temperature / mounting | `5..35 °C; 6 DIN modules` | `MM00883-a-EN.pdf` printed/PDF p. 1 |
| Connections | `Ethernet 10/100 Mbit; USB for PC firmware update; reset; RS232; video-entry SCS; burglar-alarm SCS` | `MM00883-a-EN.pdf` printed/PDF p. 1 |
| Indicators | `SPEED, LINK, SYSTEM` | `MM00883-a-EN.pdf` printed/PDF p. 1 |
| Driver scope | `MyHOME–Nuvo preinstalled according to 2016 sheet; other integrations require the specific installed driver` | `MM00883-a-EN.pdf` printed/PDF p. 1 |

| Publisher rated voltage / current | `27 Vdc` / `0.125 A` in product-characteristics paragraph; agrees with nominal SCS sheet values | `F459-publisher-product-sheet.pdf` PDF p. 1 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Frequency classifications and a negative connected-object classification do not establish the runtime transport or exclude control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system radio frequency | `No` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system LON | `No` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system Powernet | `No` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Other bus systems | `Other` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Model | `Other` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Mounting method | `Other` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Demounting protection | `No` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| With LED indication | `No` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Updateable | `No` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Operating voltage (Min-Max) | `230-230 V` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Provider dependent | `No` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Visualization | `No` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Web-Server | `No` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Radio interface | `No` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| IR interface | `No` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Degree of protection (IP) | `IP21` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Type of load | `Not applicable` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Connection type | `Screwed terminal` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Connected object | `Yes` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Programming way | `Smartphone apps` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| With voice command | `Yes` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Programmable | `Yes` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Interoperable connection Protocol | `Yes` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Connectable by Internet box | `Yes` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Compatible voice assistants | `Amazon Alexa, Google Assistant` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Application name | `Home + Control` | `F459-publisher-product-sheet.pdf` PDF p. 2 |
| Product use function | `Automation/Programming` | `F459-publisher-product-sheet.pdf` PDF p. 2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2193` | Canonical catalogue |
| Technical item description | Driver Manager | Canonical catalogue |
| Item family | Source placeholder description `0`; key `8` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `65` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `721` | `2` | `0` | `0` | `1` | Not catalogue default | Official |
| `811` | `2` | `1` | `0` | `1` | Not catalogue default | Official |
| `811` | `2` | `1` | `1` | `1` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `721` | `1` | `142` Driver Manager | Fixed / designated metadata | `2636` | `642` | `1246` |
| `811` | `1` | `142` Driver Manager | Fixed / designated metadata | `3394` | `642` | `1648` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `721` | Product Programming | `3` | Association key `4` |
| `811` | Product Programming | `3` | Association key `4` |

| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `721` | Ethernet | `2` |
| `721` | Ethernet over USB | `4` |
| `811` | Ethernet | `2` |
| `811` | Ethernet over USB | `4` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `721` | `5` | `0` | `2193_2.0_LGG\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `721` | `5` | `0` | `2193_2.0_LGG\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |
| `811` | `5` | `0` | `2193_2.1_LGG\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `811` | `5` | `0` | `2193_2.1_LGG\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |

Brand / line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Web configuration | https://192.168.1.45; public documentation value, not an observed installation | `RA00147AA_I_EN.pdf` printed/PDF pp. 6-47; `MM00883-a-EN.pdf` p. 1 |
| Driver lifecycle | Install / update specific driver; licensing / applicability driver-dependent | `RA00147AA_I_EN.pdf` printed/PDF pp. 6-47; `MM00883-a-EN.pdf` p. 1 |
| Platform settings | Network, OWN / range IP, password, date / language, restart / logout | `RA00147AA_I_EN.pdf` printed/PDF pp. 6-47; `MM00883-a-EN.pdf` p. 1 |
| Nuvo configuration | Zones, controls, direct-access, source order, scenarios and diagnostics | `RA00147AA_I_EN.pdf` printed/PDF pp. 6-47; `MM00883-a-EN.pdf` p. 1 |
| PC firmware update | USB route; RS232 connector also identified, without inferred driver protocol | `RA00147AA_I_EN.pdf` printed/PDF pp. 6-47; `MM00883-a-EN.pdf` p. 1 |
| Network | Name, static or DHCP, IP / network mask and primary / secondary DNS | `RA00147AA_I_EN.pdf` p. 14 |
| OPEN security | OPEN password; HMAC authentication selection; IP-range access without OPEN password | `RA00147AA_I_EN.pdf` p. 15 |
| Web password | Public default Admin123; replacement `8..10` characters; not an observed credential | `RA00147AA_I_EN.pdf` p. 16 |
| Date / time / languages | Manual or NTP automatic time; clock always slave on SCS; timezone; driver / web language options | `RA00147AA_I_EN.pdf` pp. 17-18 |
| Driver update / reinstall | Update retains configuration; reinstall loses configuration; separate actions | `RA00147AA_I_EN.pdf` p. 13 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `721` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `811` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `142` - Driver Manager

Catalogue Object key `642` maps to external Object `142`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.45` | Local IP address; public documentation value, not an observed installation |
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
| `DIMENSION 1` | Corroborate item model `65` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `142` - Driver Manager | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `142` - Driver Manager | Integration function | `26` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Use the web interface for platform / driver setup. `RA00147AA_I_EN.pdf` covers authentication, driver install / update, network, OWN / range-IP, password, date / language and restart / logout (printed/PDF pp. 6-19), then Nuvo zones, controls, direct access, scenarios and diagnostics (pp. 20-47). The sheet gives `https://192.168.1.45` as the configuration endpoint: public documentation value, not an observed installation. Driver purchase / availability and transport details are integration-specific.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The technical sheet and English/Italian installation manuals identify F459/003549 as the Driver Manager family. Only F459 is an explicit commercial member of this catalogue item. Examples such as VRV/VRF, Hue-type lighting and Nuvo illustrate driver use; they do not guarantee that an uninstalled driver or any current third-party version is supported. The publisher export lists `230..230` V and says no LED, no update capability and no web server; its product-characteristics paragraph instead specifies 27 Vdc/0.125 A, while the 2016 technical sheet documents SCS `18..27` Vdc, LEDs, USB firmware update and web setup. These classification contradictions remain unresolved; the export is not treated as a mains wiring instruction.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `MM00883-a-EN.pdf` | Printed/PDF p. 1: exact F459 interfaces, supply / draw / temperature / mounting, driver scope and published web configuration endpoint. |
| `MyHOME Technical Guide.pdf` | PDF pp. 25, 60, 71-72, 82: exact F459 integration references; pp. 48, 54-58, 86-87, 99: K4652M2 configuration / application examples. Family examples are not measured behavior. |
| `RA00147AA_I_EN.pdf` | Printed/PDF pp. 6-19: authentication / driver lifecycle / platform configuration; pp. 20-47: Nuvo zones, sources, scenarios and diagnostics. Driver scope remains conditional. |
| `F459-publisher-product-sheet.pdf` | Complete description, product-characteristics and classification tables; exact commercial EAN; linked document / payload inventory remains separately scoped. |
| `legrand-living-now-historical.pdf` | Printed/PDF pp. 35, 92, 94-95, 98: exact MyHOMEServer1, F459, K4652M2 and 048834 catalogue descriptions; p. 98 PIR settings and internal threshold / timing discrepancy. |
| `MM00883_a_IT.pdf` | Printed/PDF p. 1: exact F459 interfaces, supply / draw / temperature / mounting, driver scope and published web configuration endpoint. |
| `RA00147AA_I_IT.pdf` | Printed/PDF pp. 6-19: authentication / driver lifecycle / platform configuration; pp. 20-47: Nuvo zones, sources, scenarios and diagnostics. Driver scope remains conditional. |

## Evidence limits and open work

Exact installed driver / version, current driver availability, license requirements, third-party compatibility and live operation remain uncorroborated.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

### Linked sources outside reviewed evidence

These manufacturer-listed resources are visible discovery work. A listing establishes a source association; it does not establish that the payload was downloaded, verified or examined here.

| Resource | Manufacturer label | Discovery location | Review scope |
| --- | --- | --- | --- |
| `Brochure Living_NOW 2M.pdf` | Brochure BRO-LNOW-2M  /  PDF (15.9 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Brochure%20Living_NOW%202M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Brochure Living_NOW 3M.pdf` | Brochure BRO-LNOW-3M  /  PDF (16.3 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Brochure%20Living_NOW%203M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Brochure MyHOME.pdf` | Brochure BRO-MHOME  /  PDF (2.7 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Brochure%20MyHOME.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Catalogue Living_NOW 2M.pdf` | Catalog Commercial Page CAT-LNOW-2M  /  PDF (23.1 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Catalogue%20Living_NOW%202M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Catalogue Living_NOW 3M.pdf` | Catalog Commercial Page CAT-LNOW-3M  /  PDF (22.5 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Catalogue%20Living_NOW%203M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `F459_020105.fwz` | Firmware F459_020105  /  FWZ (109.5 MB) | [Manufacturer link](https://assets.legrand.com/pim/AUTRE/F459_020105.fwz) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
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
| `MM00883-a-EN.pdf` | `5cf5493496f59ca1c8529f2309703c7b66d7a07d44b57d2db3fb9a36ab5b9676` | 168950 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/5c/f5/5cf5493496f59ca1c8529f2309703c7b66d7a07d44b57d2db3fb9a36ab5b9676.pdf) |
| `MyHOME Technical Guide.pdf` | `a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9` | 23769059 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) |
| `RA00147AA_I_EN.pdf` | `e9c6759990488cbc2c5923bded48f71ea196657a87b358b17e8d080964abfa9b` | 12180499 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/e9/c6/e9c6759990488cbc2c5923bded48f71ea196657a87b358b17e8d080964abfa9b.pdf) |
| `F459-publisher-product-sheet.pdf` | `56250d59925cbc58fb2f2c36a2cdea569755c58c76d9b5b3994081761cafd70a` | 404304 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/56/25/56250d59925cbc58fb2f2c36a2cdea569755c58c76d9b5b3994081761cafd70a.pdf) |
| `legrand-living-now-historical.pdf` | `f72ab15db14eea29dd1693203fa242c32213717b596bcee9fd2ee96ce7d53e71` | 43227320 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/f7/2a/f72ab15db14eea29dd1693203fa242c32213717b596bcee9fd2ee96ce7d53e71.pdf) |
| `MM00883_a_IT.pdf` | `138c8523735e23dc2ac6fd877ec0af2542a2861cf7aa3073285ed13bfe11622f` | 169252 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/13/8c/138c8523735e23dc2ac6fd877ec0af2542a2861cf7aa3073285ed13bfe11622f.pdf) |
| `RA00147AA_I_IT.pdf` | `7a767d2e4a8cea7490a71cb8d70a0acd8f9f1103dee3570e4cd11f670e3b687d` | 12182263 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/7a/76/7a767d2e4a8cea7490a71cb8d70a0acd8f9f1103dee3570e4cd11f670e3b687d.pdf) |
