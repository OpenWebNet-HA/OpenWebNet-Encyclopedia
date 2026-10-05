# Two-wire to IP interface

## Summary

346890 joins two-wire video-entry risers to an Ethernet backbone, allowing much larger installations than a single local bus. It separates physical two-wire addresses from system addresses through configurable base offsets. Quick physical configuration and advanced TiDeviceIP configuration offer different system capacities.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0162` | Project identity |
| Technical description | Two-wire to IP interface | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `346890` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1177` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `17` | Main association; independent of project ID |
| Firmware definition | `70` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Gateways and interfaces, Audio video | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `346890` | Established catalogue identity | Manufacturer database commercial record `1689` explicitly links this SKU to item `1177` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `346890-italian-product-sheet.pdf` | Exact Italian product export | Product export retrieved 05/10/2026; boilerplate compliance dates are not product publication dates | PDF pp. 1-1: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/4c/ba/4cbab45d25900ff10a4ab5496727dee464db2263320e47e67c3fbd8511945fa6.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-346890) |
| `BT00676_a_IT.pdf` | Manufacturer Italian / installation document | BT00676_a_IT; printed publication date not established | Printed/PDF pp. 1-4 supply, interfaces, physical / software address and capacity matrix; pp.5-6 contrasting physical / advanced range examples. Ambiguous boundary and capacity labels retained. | [Archived original](https://archive.openwebnet-ha.org/sha256/a0/39/a039e94eaff871a9f70c97f0c05f1157cc3af9c3da592ce62c5d8de22b1f0a18.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/BT00676_a_IT.pdf) |
| `BT00676_a_EN.pdf` | Historical exact-product manufacturer source | BT00676_a_EN; printed publication date not established | Printed/PDF pp. 1-4 supply, interfaces, physical / software address and capacity matrix; pp.5-6 contrasting physical / advanced range examples. Ambiguous boundary and capacity labels retained. | [Archived original](https://archive.openwebnet-ha.org/sha256/ca/7e/ca7e4910b7840645e96782fbf8e5d1d84deb72de73e69f7a51a530163726dfc0.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/BT00676_a_EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1177`: complete extracted catalogue associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS operating supply | `18..27 Vdc` | `BT00676_a_EN` printed/PDF pp. 1-6; Italian revision `BT00676_a_IT` pp. 1-6 |
| SCS standby / maximum draw | `5 mA / 70 mA` | `BT00676_a_EN` printed/PDF pp. 1-6; Italian revision `BT00676_a_IT` pp. 1-6 |
| DC standby / maximum draw | `150 mA / 300 mA` | `BT00676_a_EN` printed/PDF pp. 1-6; Italian revision `BT00676_a_IT` pp. 1-6 |
| Operating temperature | `5..40 °C` | `BT00676_a_EN` printed/PDF pp. 1-6; Italian revision `BT00676_a_IT` pp. 1-6 |
| Mounting | `10 DIN modules` | `BT00676_a_EN` printed/PDF pp. 1-6; Italian revision `BT00676_a_IT` pp. 1-6 |
| Interfaces | `10/100 Mbit Ethernet; USB; separate entrance-panel/handset SCS and supply terminals` | `BT00676_a_EN` printed/PDF pp. 1-6; Italian revision `BT00676_a_IT` pp. 1-6 |
| Quick configuration capacity | `3900 handsets; 95 entrance panels; 100 IP devices; 9 IP switchboards` | `BT00676_a_EN` printed/PDF pp. 1-6; Italian revision `BT00676_a_IT` pp. 1-6 |
| Advanced configuration capacity | `10000 handsets; 1000 entrance panels; 100 IP devices; switchboards constrained by total IP-device count` | `BT00676_a_EN` printed/PDF pp. 1-6; Italian revision `BT00676_a_IT` pp. 1-6 |
| System addressing | `system address = physical address + local handset/entrance-panel base` | `BT00676_a_EN` printed/PDF pp. 1-6; Italian revision `BT00676_a_IT` pp. 1-6 |
| IP switchboard service count | `2..4 IP devices per switchboard PC according to enabled services` | `BT00676_a_EN` printed/PDF pp. 1-6; Italian revision `BT00676_a_IT` pp. 1-6 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1177` | Canonical catalogue |
| Technical item description | IP interface (2Wire/IP) | Canonical catalogue |
| Item family | Source placeholder description `0`; key `100` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `17` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `70` | `4` | `0` | `8` | `1` | Catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `70` | `1` | `92` IP interface (2 wires/IP and D2009/IP) | Fixed / designated metadata | `2271` | `92` | `949` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `70` | Product Programming | `3` | Association key `4` |

| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `70` | Ethernet | `2` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `70` | `1` | `0` | `TiDeviceIP_0400` | Parameter type `7`; payload not inspected |

Brand / line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

### Manufacturer configuration and operating settings

Published product selectors and software settings are separate from catalogue mode IDs. Their domains, defaults and topology limits do not replace Firmware-specific filters.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `M1 / N1 / M2 / N2 / C` | Lower first / second address component / upper first / second component, each `00..99`; M1 also `OFF`; `C=1..9` switchboard | `BT00676_a_EN` printed/PDF pp. 1-6 |
| `Quick mode 1` | `M1=OFF`; N1/M2/N2 empty; automatically detected entrance panels / cameras only | `BT00676_a_EN` printed/PDF pp. 1-6 |
| `Quick mode 2` | Range delimited by configured lower and upper handset addresses; entrance panels / cameras automatically detected | `BT00676_a_EN` printed/PDF pp. 1-6 |
| `Quick mode 3` | M1 hundreds prefix; N1/M2/N2 empty; stated hundred-address interval; boundary inequalities conflict with example labels | `BT00676_a_EN` printed/PDF pp. 1-6 |
| `Advanced local bases` | Independent handset and entrance-panel / lock offsets; system address = physical address + base | `BT00676_a_EN` printed/PDF pp. 1-6 |
| `Capacity, quick / advanced` | System handsets 3900 /10000; entrance panels 95 /1000; highest called address 4000 /10000; total IP devices 100 in either mode | `BT00676_a_EN` printed/PDF pp. 1-6 |
| `IP switchboards / services` | Quick 9 switchboards; advanced subject to 100 IP-device total; each switchboard PC consumes `2..4` service-device entries | `BT00676_a_EN` printed/PDF pp. 1-6 |
| `Advanced functions` | Direct entrance-panel call; activation redirection; camera cycling; customizable text and system addressing | `BT00676_a_EN` printed/PDF pp. 1-6 |
| `Range example 190..210` | Physical example uses two 346851 interfaces for two hundreds ranges; advanced example uses handset addresses `1..21` plus base 189 without those interfaces | `BT00676_a_EN` printed/PDF pp. 1-6 |
| `SPEED / FULL / LINK / SYSTEM / AUX` | 100/10 Mbit; full / half duplex; Ethernet present / absent; powered / operating; `AUX` unused | `BT00676_a_EN` printed/PDF pp. 1-6 |
| `PC transfer / firmware update` | Powered interface, no physical configurators; USB-miniUSB; TiDeviceIP also verifies quick-mode consistency | `BT00676_a_EN` printed/PDF pp. 1-6 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `70` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `70` | `M1_1` | `0..3` | `0` | M1_1; Internal Unit Range |
| `70` | `M1_2` | `0..9`; `10` = `OFF` | `0` | M1_2; Internal Unit Range |
| `70` | `N1_1` | `0..9` | `0` | N1_1; Internal Unit Range |
| `70` | `N1_2` | `0..9` | `0` | N1_2; Internal Unit Range |
| `70` | `M2_1` | `0..3` | `0` | M2_1; Internal Unit Range |
| `70` | `M2_2` | `0..9` | `0` | M2_2; Internal Unit Range |
| `70` | `N2_1` | `0..9` | `0` | N2_1; Internal Unit Range |
| `70` | `N2_2` | `0..9` | `0` | N2_2; Internal Unit Range |
| `70` | `C` | `0..9` | `0` | C; Interf2wires Associated SwitchBoard |
| `70` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `70` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `70` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

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
| `DIMENSION 1` | Corroborate item model `17` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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

Quick configuration uses M1/N1 for the lower handset boundary, M2/N2 for the upper boundary and `C=1..9` for the IP switchboard. `M1=OFF` with N1/M2/N2 empty is entrance-panel-only. A hundred-address riser mode uses M1 as the hundreds prefix and leaves the other handset sockets empty. Advanced configuration introduces local bases for handsets and entrance panels / locks, direct entrance-panel calls, activation redirection and camera cycling. For USB transfer / update, power the interface and remove physical configurators. TiDeviceIP provides the quick-mode consistency check. Count switchboard communication framework, logger and alarm-manager services within the 100-IP-device ceiling. These capacity figures describe the documented system, not unrestricted per-interface fan-out.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The exact English and Italian technical sheets and Italian export agree on the two-wire/IP role and 10-DIN housing. The technical sheet distinguishes 3900 quick-mode system handsets from a basic physical address range `1..3999`; those numbers are not silently equated. Its page 2 also assigns 95 entrance panels and 3900 handsets to one interface in the stated quick configuration, whereas the page 4 table labels these as system totals; the physical wiring limits still require independent topology validation. Several example inequalities omit or vary inclusive boundaries even though diagrams show endpoints; preserve configured domains and validate boundary behavior on hardware. 346891 is a different reference and is not substituted for this discontinued item. The 346310 switchboard sheet explicitly excludes installations using 346890.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `346890-italian-product-sheet.pdf` | PDF pp. 1-1: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. |
| `BT00676_a_IT.pdf` | Printed/PDF pp. 1-4 supply, interfaces, physical / software address and capacity matrix; pp.5-6 contrasting physical / advanced range examples. Ambiguous boundary and capacity labels retained. |
| `BT00676_a_EN.pdf` | Printed/PDF pp. 1-4 supply, interfaces, physical / software address and capacity matrix; pp.5-6 contrasting physical / advanced range examples. Ambiguous boundary and capacity labels retained. |

## Evidence limits and open work

The boundary semantics in quick-mode examples, currently usable TiDeviceIP software, per-interface topology limits and installed diagnostic support remain uncorroborated.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
