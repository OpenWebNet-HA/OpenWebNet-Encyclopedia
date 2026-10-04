# MH200N scenario programmer

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0131` | Project identity |
| Technical description | MH200N scenario programmer | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `MH200N`, `003565` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1331` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `44` | Main association; independent of project ID |
| Firmware definition | `73` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `2` | Firmware metadata |
| Categories | Scenarios, Gateways and interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `MH200N` | Established catalogue identity | Manufacturer database commercial record `1331` explicitly links this SKU to item `1331` |
| Legrand | `003565` | Established catalogue identity | Manufacturer database commercial record `1790` explicitly links this SKU to item `1331` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `u4613b_u_en.pdf` | Exact historical manufacturer documentation | `u4613b_u_en; original publication date not established` | Exact-product specifications, operating/configuration material and source limitations; retained 12-page original; relevant product sections reviewed. Printed pagination and 1-based PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/c6/0e/c60eecb3f5bff48d669037942f52c68dbbde21288e424cc5970390caae19c0ca.pdf) | [Publisher original](https://assets.legrand.com/general/legrand-exp/np-ft-gt/u4613b_u_en.pdf) |
| `MQ00319-b-UK.pdf` | Exact manufacturer documentation | `MQ00319-b-UK; 14/01/2013` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-3; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/93/af/93af891c3438d3e5e19643a741f4b9516af82e9598d0719769b56fbe3144d47a.pdf) | [Publisher original](https://assets.legrand.com/general/legrand-exp/np-ft-gt/mq00319-b-uk.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `1331` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `27 Vdc auxiliary; SCS operating range 18..27 Vdc` | `MQ00319-b-UK` printed/PDF pp. 1-3 |
| Maximum draw | `200 mA` | `MQ00319-b-UK` printed/PDF pp. 1-3 |
| Operating temperature | `5..40 °C` | `MQ00319-b-UK` printed/PDF pp. 1-3 |
| Mounting | `6 DIN modules` | `MQ00319-b-UK` printed/PDF pp. 1-3 |
| Scenario capacity | `300 simple/advanced scenarios` | `MQ00319-b-UK` printed/PDF pp. 1-3 |
| Interfaces | `SCS bus; Ethernet RJ45; serial/PC connection; reset and status LEDs` | `MQ00319-b-UK` printed/PDF pp. 1-3 |
| Supply accessory | `346020` | `MQ00319-b-UK` printed/PDF pp. 1-3 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1331` | Canonical catalogue |
| Technical item description | Scenario programmer | Canonical catalogue |
| Item family | 0; key `19` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `44` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `73` | `1` | `0` | `5` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Associated firmware packages

| Firmware | Package key | Package label | Package tuple |
| --- | --- | --- | --- |
| `73` | `46` | GL1 | `1.2.0` |
| `73` | `48` | GL31 | `1.3.0` |
| `73` | `49` | GL21 | `1.1.0` |
| `73` | `50` | GL42 | `1.1.0` |
| `73` | `51` | GL51 | `1.1.0` |


Package labels are source metadata; package applicability does not establish the installed tuple.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `73` | `1` | `61` Scenario scheduler | Fixed/designated metadata | `898` | `61` | `563` |
| `73` | `2` | `150` Gateway Open SCS | Fixed/designated metadata | `899` | `150` | `564` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `73` | Product Programming | `3` | Association key `4` |


| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `73` | Ethernet | `2` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `73` | `1` | `0` | `xml\SDC\sdc.xml` | Parameter type `1`; payload not inspected |
| `73` | `1` | `0` | `1331_1.0_BT\xml\SVM\svm.xml` | Parameter type `2`; payload not inspected |
| `73` | `1` | `0` | `1331_1.0_BT\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `73` | `1` | `0` | `1331_1.0_BT\xml\DIRECTOR\director.xml` | Parameter type `5`; payload not inspected |
| `73` | `1` | `0` | `1331_1.0_BT\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |
| `73` | `2` | `0` | `xml\SDC\sdc.xml` | Parameter type `1`; payload not inspected |
| `73` | `2` | `0` | `1331_1.0_LG\xml\SVM\svm.xml` | Parameter type `2`; payload not inspected |
| `73` | `2` | `0` | `1331_1.0_LG\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `73` | `2` | `0` | `1331_1.0_LG\xml\DIRECTOR\director.xml` | Parameter type `5`; payload not inspected |
| `73` | `2` | `0` | `1331_1.0_LG\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |


Brand/line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `73` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `73` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `73` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (manufacturer catalogue default/example) | Local IP address |
| `73` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity; Local Dynamic IP |
| `73` | `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `73` | `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` (manufacturer catalogue default/example) | Public IP address |
| `73` | `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity; Public Dynamic IP |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `61` - Scenario scheduler

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (manufacturer catalogue default/example) | Local IP address |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity |
| `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` (manufacturer catalogue default/example) | Public IP address |
| `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |


### Object `150` - Gateway Open SCS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (manufacturer catalogue default/example) | Local IP address |
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

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `44` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `61` - Scenario scheduler | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `150` - Gateway Open SCS | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |


These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Create and transfer scenario collections with TiMH200N. Associate `CEN` keys using addresses distinct from actuator addresses; date/time, sensor, alarm and manual events can condition a scenario. USB/serial and crossover Ethernet examples are source-specific routes; a remote transfer needs known device addressing/authentication. The user guide permits one browser session at a time; normal-user scenario/diagnostic pages are separate from administrator time, network, language and authorization configuration. Its diagnostic page is not evidence of support for every OpenWebNet DIMENSION. Power the scenario programmer supply and automation supply through a common bipolar switch as shown in the exact sheet.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

## Source reconciliation

MH200N/003565 catalogue identity and scenario/gateway roles agree with the exact MH200N sheet and user guide. The sheet contains TiMH200/MH200 and MiMH200N naming remnants plus a likely H/L4864 touch-screen reference typo; those do not establish compatibility with the different MH200 firmware. Existing MH200 captures elsewhere in the repository are not evidence for MH200N. Two Firmware Modules, scheduler and OpenSCS gateway, do not mean two physical products.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `u4613b_u_en.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `MQ00319-b-UK.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |

## Evidence limits and open work

Exact installation/software manual revisions, behavior of the retained catalogue scheduler fields and device-specific diagnostics need corroboration. MH200 captures cannot close MH200N evidence gaps.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
