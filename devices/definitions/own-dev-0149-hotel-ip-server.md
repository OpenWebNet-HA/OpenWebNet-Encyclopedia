# Hotel IP server

## Summary

F458 is the IP server used to organise larger BTicino/Legrand hotel installations. It supplies DHCP and DNS services for the hotel network, where MH201 room controllers communicate with supervision software. It has an Ethernet port and a separate DC power input.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0149` | Project identity |
| Technical description | Hotel IP server | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `003599`, `F458` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1864` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `105` | Main association; independent of project ID |
| Firmware definition | `545` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `2` | Firmware metadata |
| Categories | Gateways and interfaces | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `003599` | Established catalogue identity | Manufacturer database commercial record `2158` explicitly links this SKU to item `1864` |
| BTicino | `F458` | Established catalogue identity | Manufacturer database commercial record `2157` explicitly links this SKU to item `1864` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `LE06433AA.pdf` | Legacy manufacturer technical documentation | `LE06433AA-01PC-13W22; printed revision label` | PDF pp. 1-1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/74/25/742573bc3915ad251a7abf01c81e8c01dba2b390f1553993c555ae8e0f4110c1.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/LE06433AA.pdf) |
| `MM00857_a_IT.pdf` | Legacy manufacturer technical documentation | `MM00857_a_IT; 15/01/2015` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/cf/e7/cfe75feffd8b77ec861b848ef7cf8f4a5a88f8fd3ad4e91d6f58c584be6ddd6e.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/MM00857_a_IT.pdf) |
| `MM00857_a_EN.pdf` | English counterpart of manufacturer-linked document | `MM00857_a_EN; 15/01/2015` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/81/6e/816e26925d197689d4bd9fc99a770181bdea0d339d60c87b82591ab435a61ff0.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MM00857_a_EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1864`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Power supply | `18..30 Vdc; external DC supply, 346020 recommended` | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction |
| Maximum current | `55 mA` | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction |
| Minimum / maximum consumption | `1.3 W / 3.3 W as printed` | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction |
| Clock retention without supply | `48 hours` | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction |
| Temperature / size | `5..45 °C; 6 DIN modules` | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction |
| Network | `RJ45 Ethernet 10/100 Mbit` | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction |
| Service interface | `mini-USB for configuration and software update` | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction |
| Default IP / mask | `192.168.1.51 / 255.255.255.0` | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction; public documentation value, not an observed installation |
| DHCP/DNS range in Suite 2.0.91 | `192.168.1.52..192.168.5.49` | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction; public documentation value, not an observed installation |
| Default OPEN password | `12345; published factory value, not an installed credential` | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1864` | Canonical catalogue |
| Technical item description | IP server | Canonical catalogue |
| Item family | 0; key `8` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `105` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `545` | `1` | `0` | `0` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `545` | `1` | `99989` DHCP server | Fixed/designated metadata | `2373` | `609` | `1028` |
| `545` | `2` | `99988` DNS server | Fixed/designated metadata | `2374` | `611` | `1029` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `545` | Product Programming | `3` | Association key `4` |


| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `545` | Ethernet | `2` |
| `545` | Ethernet over USB | `4` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `545` | `1` | `0` | `xml\SDC\sdc.xml` | Parameter type `1`; payload not inspected |
| `545` | `1` | `0` | `1864_1.0_BT\xml\SVM\svm.xml` | Parameter type `2`; payload not inspected |
| `545` | `1` | `0` | `1864_1.0_BT\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `545` | `1` | `0` | `1864_1.0_BT\xml\DIRECTOR\director.xml` | Parameter type `5`; payload not inspected |
| `545` | `1` | `0` | `1864_1.0_BT\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |
| `545` | `5` | `0` | `xml\SDC\sdc.xml` | Parameter type `1`; payload not inspected |
| `545` | `5` | `0` | `1864_1.0_LGG\xml\SVM\svm.xml` | Parameter type `2`; payload not inspected |
| `545` | `5` | `0` | `1864_1.0_LGG\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `545` | `5` | `0` | `1864_1.0_LGG\xml\DIRECTOR\director.xml` | Parameter type `5`; payload not inspected |
| `545` | `5` | `0` | `1864_1.0_LGG\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |


Brand/line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `Configuration route` | MyHOME_Suite; Ethernet or USB as independently documented | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction |
| `System LED` | supply on, goes off, returns steadily operational | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction |
| `Speed LED` | `ON` 100 Mbit / `OFF` 10 Mbit | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction |
| `Link LED` | Ethernet network present | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction |
| `Hotel topology` | required over 100 rooms/MH201 areas; examples up to 500 areas and ten supervision PCs | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `545` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `545` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `545` | `FW_VER` | `######` = Firmware version | `1.0.0` | Firmware version |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `99989` - DHCP server

Catalogue Object key `609` maps to external Object `99989`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `FW_VER` | `######` = Firmware version | `1.0.0` | Firmware version |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |


### Object `99988` - DNS server

Catalogue Object key `611` maps to external Object `99988`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `FW_VER` | `######` = Firmware version | `1.0.0` | Firmware version |
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

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution remains in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `105` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `99989` - DHCP server | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `99988` - DNS server | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |


These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system/model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Configure with MyHOME_Suite. The sheet requires this server for installations over 100 rooms or over 100 MH201 areas and illustrates systems up to 500 areas and up to ten supervision PCs. Room controllers, layer-3 switches/router, supervision server and PMS interface are shown on a dedicated BTicino/Legrand VLAN. These are topology examples, not arbitrary Ethernet interoperability guarantees. The System LED lights at supply connection, goes off, then returns steadily when operational; Speed `ON` means 100 Mbit and `OFF` means 10 Mbit; Link indicates network presence. Use the separately documented DC input: the BUS-SCS title alone does not establish an SCS field connector.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session/validation method remains in [Programming](../../programming/).

## Source reconciliation

The technical sheet title says BUS-SCS server IP, but its interface legend shows Ethernet, USB and DC power terminals, without a physical SCS BUS connector. The database represents DHCP Object `99989` and DNS Object `99988` in two declared Modules; these are network-service roles rather than two room controllers or two output relays. The printed maximum 3.3 W and 55 mA are retained independently; the measurement conditions needed to reconcile their apparent arithmetic mismatch are not established. The database brand label Legrand BTicino groups both commercial records. Human-facing identities use the manufacturer’s separately established BTicino and Legrand reference families; the raw grouping is preserved here as catalogue terminology.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `LE06433AA.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `MM00857_a_IT.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `MM00857_a_EN.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |

## Evidence limits and open work

Network-service behavior, actual firmware, DHCP/DNS deployment limits beyond the illustrated topology, power measurement conditions and diagnostic transport remain uncorroborated.

No installed hardware revision or microcontroller fingerprint is retained for this cluster. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Canonical catalogue extraction and reconciliation are complete for the retained evidence; further documentation discovery, runtime corroboration and final evidence closure remain partial.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
