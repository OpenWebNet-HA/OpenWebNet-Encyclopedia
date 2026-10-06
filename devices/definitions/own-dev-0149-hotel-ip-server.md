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

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `F458` | IP server | Canonical commercial record `2157` |
| `003599` | IP server | Canonical commercial record `2158` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `LE06433AA.pdf` | Legacy manufacturer technical documentation | `LE06433AA-01PC-13W22; printed revision label` | PDF p. 1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/74/25/742573bc3915ad251a7abf01c81e8c01dba2b390f1553993c555ae8e0f4110c1.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/LE06433AA.pdf) |
| `MM00857_a_IT.pdf` | Legacy manufacturer technical documentation | `MM00857_a_IT; 15/01/2015` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/cf/e7/cfe75feffd8b77ec861b848ef7cf8f4a5a88f8fd3ad4e91d6f58c584be6ddd6e.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/MM00857_a_IT.pdf) |
| `MM00857_a_EN.pdf` | English counterpart of manufacturer-linked document | `MM00857_a_EN; 15/01/2015` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/81/6e/816e26925d197689d4bd9fc99a770181bdea0d339d60c87b82591ab435a61ff0.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MM00857_a_EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1864`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Power supply | `18..30 Vdc; external DC supply, 346020 recommended` | `MM00857_a_EN` and `MM00857_a_IT` PDF p. 1 |
| Maximum current | `55 mA` | `MM00857_a_EN` and `MM00857_a_IT` PDF p. 1 |
| Minimum / maximum consumption | `1.3 W / 3.3 W as printed` | `MM00857_a_EN` and `MM00857_a_IT` PDF p. 1 |
| Clock retention without supply | `48 hours` | `MM00857_a_EN` and `MM00857_a_IT` PDF p. 1 |
| Temperature / size | `5..45 °C; 6 DIN modules` | `MM00857_a_EN` and `MM00857_a_IT` PDF p. 1 |
| Network | `RJ45 Ethernet 10/100 Mbit` | `MM00857_a_EN` and `MM00857_a_IT` PDF p. 1 |
| Service interface | `mini-USB for configuration and software update` | `MM00857_a_EN` and `MM00857_a_IT` PDF p. 1 |
| Default IP / mask | `192.168.1.51 / 255.255.255.0` | `MM00857_a_EN` and `MM00857_a_IT` PDF p. 1; public documentation value, not an observed installation |
| DHCP/DNS range in Suite 2.0.91 | `192.168.1.52..192.168.5.49` | `MM00857_a_EN` and `MM00857_a_IT` PDF p. 1; public documentation value, not an observed installation |
| Default OPEN password | `12345; published factory value, not an installed credential` | `MM00857_a_EN` and `MM00857_a_IT` PDF p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1864` | Canonical catalogue |
| Technical item description | IP server | Canonical catalogue |
| Item family | 0; key `8` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `105` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `105` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Network | LAN | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `545` | `1` | `0` | `0` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `545` | `341` | BTicino (key `1`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `545` | `342` | BTicino (key `1`) | `0` | SVM | `1864_1.0_BT\xml\SVM\svm.xml` |
| `545` | `343` | BTicino (key `1`) | `0` | Extra | `1864_1.0_BT\xml\Extra\extra.xml` |
| `545` | `344` | BTicino (key `1`) | `0` | Director | `1864_1.0_BT\xml\DIRECTOR\director.xml` |
| `545` | `345` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1864_1.0_BT\xml\Protocol\protocol.xml` |
| `545` | `374` | Undefined (key `5`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `545` | `375` | Undefined (key `5`) | `0` | SVM | `1864_1.0_LGG\xml\SVM\svm.xml` |
| `545` | `376` | Undefined (key `5`) | `0` | Extra | `1864_1.0_LGG\xml\Extra\extra.xml` |
| `545` | `377` | Undefined (key `5`) | `0` | Director | `1864_1.0_LGG\xml\DIRECTOR\director.xml` |
| `545` | `378` | Undefined (key `5`) | `0` | Protocol and other device parameters | `1864_1.0_LGG\xml\Protocol\protocol.xml` |

All 10 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

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
| `545` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `545` | Ethernet | Canonical firmware/connection association |
| `545` | Ethernet over USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `Configuration route` | MyHOME_Suite; Ethernet or USB as independently documented | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction |
| `System LED` | supply on, goes off, returns steadily operational | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction |
| `Speed LED` | `ON` 100 Mbit / `OFF` 10 Mbit | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction |
| `Link LED` | Ethernet network present | `MM00857_a_EN` printed/PDF pp. 1-4; `LE06433AA` installation instruction |
| `Hotel topology` | required over 100 rooms/MH201 areas; examples up to 500 areas and ten supervision PCs | `MM00857_a_EN` and `MM00857_a_IT` PDF pp. 1–4 |

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

Apply the exact firmware restrictions above. The generic session/validation method remains in [Programming](../../programming/).

## Source reconciliation

The technical sheet title says BUS-SCS server IP, but its interface legend shows Ethernet, USB and DC power terminals, without a physical SCS BUS connector. The database represents DHCP Object `99989` and DNS Object `99988` in two declared Modules; these are network-service roles rather than two room controllers or two output relays. The printed maximum 3.3 W and 55 mA are retained independently; the measurement conditions needed to reconcile their apparent arithmetic mismatch are not established. The database brand label Legrand BTicino groups both commercial records. Human-facing identities use the manufacturer’s separately established BTicino and Legrand reference families; the raw grouping is preserved here as catalogue terminology.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `LE06433AA.pdf` | PDF p. 1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `MM00857_a_IT.pdf` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `MM00857_a_EN.pdf` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |

The EN and IT manufacturer documentation specifies factory IP 192.168.1.51, while both firmware and reusable DHCP/DNS Objects store 192.168.1.35. These independent defaults are a source discrepancy; neither identifies a live network. All three originals agree on Ethernet/USB/DC and LED meanings; the one-page LE06433AA does not supply the technical sheet’s power ratings, default IP, password or hotel-size examples. The diagram labelled fewer than 100 areas nevertheless includes a Room 100 label; no additional threshold is inferred. Ethernet over USB is a catalogue connection label, not a measured USB network protocol.

### Semantic review findings

Firmware `545` is official/default 1.0.0 with two fixed service slots, DHCP 99989/key609 and DNS99988/key611, no Virgin, conditions, filters or conversions. Complete IP/FW_VER/SYSADDRESS reusable fields and firmware AID/IP/FW_VER preserved; masks do not define validation or byte encoding. Public manufacturer documentation default IP 192.168.1.35 conflicts with both EN/IT sheets factory IP 192.168.1.51, now explicitly reconciled. Ten parameter associations cover BT and LGG SDC/SVM/Extra/Director/Protocol with actual type/brand/line metadata, no package associations and unexamined XML payloads. One programming mode and Ethernet/Ethernet-over-USB connections match setup routes but do not establish USB wire protocol. BUS-SCS title does not add an SCS connector; canonical bus is LAN. EN/IT four-page topology and power facts inspected; LE06433AA one-page interface/LED scope separately attributed rather than incorrectly cited for power/IP/password. Public factory password is not a private installed credential. 55mA versus3.3W lacks measurement reconciliation; fewer-than100 diagram includes Room100, retained as illustration. No EAN is retained in these originals; current exact manufacturer listing found, no catalogue identity uncertainty.

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

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0141-0150-2026-10-06.md#own-dev-0149)
