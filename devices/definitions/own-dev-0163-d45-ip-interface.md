# D45 to IP interface

## Summary

323011 connects a D45 video-entry installation to an IP network and supports mixed D45 / two-wire-IP installations. It has separate D45 bus and main-entrance-panel connections, Ethernet, USB and serial configuration interfaces. Video-gain switches adapt the documented bus connection.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0163` | Project identity |
| Technical description | D45 to IP interface | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `323011` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1178` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `49` | Main association; independent of project ID |
| Firmware definition | `71` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Gateways and interfaces, Audio video | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `323011` | Established catalogue identity | Manufacturer database commercial record `1953` explicitly links this SKU to item `1178` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `BT00459-b-EN.pdf` | Exact-product manufacturer source | BT00459-b-EN; 13/05/2013 | PDF pp. 1-2: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/10/54/105452f6c19200f06548456308b4a1e025478cd7d3526181f90c6540f2643282.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/BT00459-b-EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1178`: complete extracted catalogue associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Auxiliary supply | `30 Vdc` | `BT00459-b-EN` printed/PDF pp. 1-2 |
| Standby / maximum draw | `≤130 mA / ≤230 mA at 30 V` | `BT00459-b-EN` printed/PDF pp. 1-2 |
| Operating temperature | `-10..40 °C` | `BT00459-b-EN` printed/PDF pp. 1-2 |
| Dimensions / mounting | `175 x 90 x 60 mm; DIN rail` | `BT00459-b-EN` printed/PDF pp. 1-2 |
| Interfaces | `10/100 Mbit Ethernet; USB; RS232; SYSTEM1 D45 riser bus; SYSTEM2 main entrance panel` | `BT00459-b-EN` printed/PDF pp. 1-2 |
| Local controls | `video gain DIP switch; configurator socket; unused pushbutton` | `BT00459-b-EN` printed/PDF pp. 1-2 |
| LEDs | `SYSTEM powered/working; LINK network; FULL duplex; SPEED 100 Mbit on / 10 Mbit off` | `BT00459-b-EN` printed/PDF pp. 1-2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1178` | Canonical catalogue |
| Technical item description | IP interface (D45/IP) | Canonical catalogue |
| Item family | Source placeholder description `0`; key `100` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `49` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `71` | `4` | `0` | `1` | `1` | Catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `71` | `1` | `92` IP interface (2 wires/IP and D2009/IP) | Fixed / designated metadata | `2264` | `92` | `942` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `71` | Product Programming | `3` | Association key `4` |

| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `71` | Ethernet | `2` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `71` | `2` | `0` | `TiDeviceIP_0400` | Parameter type `7`; payload not inspected |

Brand / line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

### Manufacturer configuration and operating settings

Published product selectors and software settings are separate from catalogue mode IDs. Their domains, defaults and topology limits do not replace Firmware-specific filters.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `Configuration tool` | D45/IP interface Config 2.0 | `BT00459-b-EN` printed/PDF pp. 1-2 |
| `Download routes` | Online Ethernet, serial RS232, USB | `BT00459-b-EN` printed/PDF pp. 1-2 |
| `SYSTEM1 / SYSTEM2 / DC` | D45 riser shunt / D45 main entrance panel / auxiliary 30 Vdc supply | `BT00459-b-EN` printed/PDF pp. 1-2 |
| `DIP / unused controls` | Video-gain selection shown; complete switch-value matrix not given; local pushbutton and `AUX` LED unused | `BT00459-b-EN` printed/PDF pp. 1-2 |
| `SYSTEM / LINK / FULL / SPEED` | Powered / working / network found / full duplex / 100 Mbit on or 10 Mbit off | `BT00459-b-EN` printed/PDF pp. 1-2 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `71` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `71` | `EXTERNAL_UNIT_MIN` | `0..100090` | Not specified in source | (0-100090) |
| `71` | `EXTERNAL_UNIT_MAX` | `0..100090` | Not specified in source | (0-100090) |
| `71` | `INTERNAL_UNIT_MIN` | `0..103999` | Not specified in source | (0-103999) |
| `71` | `INTERNAL_UNIT_MAX` | `0..103999` | Not specified in source | (0-103999) |
| `71` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `71` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `71` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

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
| `DIMENSION 1` | Corroborate item model `49` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The exact sheet specifies D45/IP interface Config 2.0. Download routes are online Ethernet, serial and USB; USB also supports firmware updates. SYSTEM1 connects to a D45 riser shunt, SYSTEM2 to the main entrance panel and DC to the auxiliary 30 V supply. The lower / higher handset ranges must cover the intended risers without overlaps; the sheet illustrates consecutive 80-address risers. Do not use Ethernet RJ45 pin assumptions for the D45 SYSTEM connectors simply because the connector shape is identical.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The exact 2013 sheet establishes this D45 interface independently of 346890, even though both firmware definitions reuse Object `92`. Shared Object fields do not establish interchangeable terminals, supply or commissioning tools. The database label “D2009/IP” is retained implementation terminology; the product sheet uses D45. The two-page sheet establishes three configuration-transfer routes but does not document every software field or network default.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `BT00459-b-EN.pdf` | PDF pp. 1-2: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. |

## Evidence limits and open work

The original Config 2.0 software / manual, complete video-gain settings, detailed mixed-system limits and hardware / network diagnostics remain gaps. The official historical catalogue URL attempted during discovery returned 403.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
