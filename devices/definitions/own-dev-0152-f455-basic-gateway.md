# F455 basic gateway

## Summary

F455 provides local and remote access to supported MyHOME lighting, automation, temperature-control and energy functions. It also acts as a gateway for virtual configuration through MyHOME_Suite. Its supported applications and connection limits are narrower than those of a general integration gateway.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0152` | Project identity |
| Technical description | F455 basic gateway | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `003594`, `F455` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `2064` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `8` | Main association; independent of project ID |
| Firmware definition | `589` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `2` | Firmware metadata |
| Categories | Gateways and interfaces | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `003594` | Established catalogue identity | Manufacturer database commercial record `2364` explicitly links this SKU to item `2064` |
| BTicino | `F455` | Established catalogue identity | Manufacturer database commercial record `2363` explicitly links this SKU to item `2064` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ01012-c-EN.pdf` | Exact-product manufacturer original | `MQ01012-c-EN; 26/01/2016` | PDF pp. 1-1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/01/58/0158e0b1ddacf416204cfe6e05eb6ee2c21a40634073bd831a48de497ce0cd69.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MQ01012-c-EN.pdf) |
| `MQ01012-c-IT.pdf` | Exact-product manufacturer original | `MQ01012-c-IT; 26/01/2016` | PDF pp. 1-1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/68/77/68773a79cc126f204723752d83b8918be4b417349ee532d765ff01448df568a1.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MQ01012-c-IT.pdf) |
| `RA00125AB_I_EN.pdf` | Exact-product manufacturer original | `RA00125AB_I_EN; printed publication date not established` | Retained 20-page original; exact-product technical, configuration and operating sections reviewed where applicable. Source-specific facts and remaining limits are scoped in the dossier; this does not claim a line-by-line review of every manual page. | [Archived original](https://archive.openwebnet-ha.org/sha256/59/83/5983079beea9a5947ce49f2df49a2d4ff886764888dd1aa2615623dd7b6c5304.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00125AB_I_EN.pdf) |
| `LE05548AC.pdf` | Exact-product manufacturer original | `LE05548AC-01PC-15W12; printed revision label` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/b3/5b/b35b493c708d1dc1081fbaea747d7d4239f8fd99a058dd8b51625414d1d67eea.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/LE05548AC.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2064`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply / draw | `18..27 Vdc / 30 mA` | `MQ01012-c-EN` printed/PDF p. 1; `RA00125AB_I_EN` printed/PDF pp. 4,11-18; `LE05548AC` instruction |
| Temperature / size | `5..40 °C; 1 DIN module` | `MQ01012-c-EN` printed/PDF p. 1; `RA00125AB_I_EN` printed/PDF pp. 4,11-18; `LE05548AC` instruction |
| Interfaces | `RJ45 Ethernet; SCS terminals; red/green LED; reset button` | `MQ01012-c-EN` printed/PDF p. 1; `RA00125AB_I_EN` printed/PDF pp. 4,11-18; `LE05548AC` instruction |
| Socket limit | `no more than five simultaneous sockets` | `MQ01012-c-EN` printed/PDF p. 1; `RA00125AB_I_EN` printed/PDF pp. 4,11-18; `LE05548AC` instruction |
| Recovery address / mask | `192.168.1.5 / 255.255.255.0; temporary until restart` | `MQ01012-c-EN` printed/PDF p. 1; `RA00125AB_I_EN` printed/PDF pp. 4,11-18; `LE05548AC` instruction; public documentation value, not an observed installation |
| Web default password | `basic_gw` | `MQ01012-c-EN` printed/PDF p. 1; `RA00125AB_I_EN` printed/PDF pp. 4,11-18; `LE05548AC` instruction |
| OPEN default password | `12345` | `MQ01012-c-EN` printed/PDF p. 1; `RA00125AB_I_EN` printed/PDF pp. 4,11-18; `LE05548AC` instruction |
| New web password length | `8..10 characters, installer manual` | `MQ01012-c-EN` printed/PDF p. 1; `RA00125AB_I_EN` printed/PDF pp. 4,11-18; `LE05548AC` instruction |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2064` | Canonical catalogue |
| Technical item description | Basic gateway | Canonical catalogue |
| Item family | 0; key `8` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `8` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `589` | `1` | `0` | `0` | `2` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `589` | `1` | `229` Basic Gateway | Fixed/designated metadata | `2388` | `619` | `1043` |
| `589` | `2` | `150` Gateway Open SCS | Fixed/designated metadata | `2389` | `150` | `1044` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `589` | Product Programming | `3` | Association key `4` |


| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `589` | Ethernet | `2` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `589` | `5` | `0` | `2064_1.0_LGG\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `589` | `5` | `0` | `2064_1.0_LGG\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |


Brand/line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `Power-on button hold 3 s` | temporary 192.168.1.5 / 255.255.255.0 | `MQ01012-c-EN` printed/PDF p. 1; `RA00125AB_I_EN` printed/PDF pp. 4,11-18; `LE05548AC` instruction; public documentation value, not an observed installation |
| `Button hold 10 s / 20 s` | restart / restart into dynamic IP selection | `MQ01012-c-EN` printed/PDF p. 1; `RA00125AB_I_EN` printed/PDF pp. 4,11-18; `LE05548AC` instruction |
| `Web recovery` | both security questions and answers required | `MQ01012-c-EN` printed/PDF p. 1; `RA00125AB_I_EN` printed/PDF pp. 4,11-18; `LE05548AC` instruction |
| `Red 1 s on/off / green 1 s on,3 s off` | searching for network / network found | `MQ01012-c-EN` printed/PDF p. 1; `RA00125AB_I_EN` printed/PDF pp. 4,11-18; `LE05548AC` instruction |
| `Third-party integration / SDK` | explicitly excluded by manufacturer | `MQ01012-c-EN` printed/PDF p. 1; `RA00125AB_I_EN` printed/PDF pp. 4,11-18; `LE05548AC` instruction |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `589` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `589` | `IS_GATEWAY` | `0` = Disable; `1` = Enable | `1` | Gateway |
| `589` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `589` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `589` | `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` | Public IP address; public documentation value, not an observed installation |
| `589` | `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `2` | Public IP dynamicity |
| `589` | `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `589` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `150` - Gateway Open SCS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |


### Object `229` - Basic Gateway

Catalogue Object key `619` maps to external Object `229`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `1` | Gateway |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` | Public IP address; public documentation value, not an observed installation |
| `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `2` | Public IP dynamicity |
| `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
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

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution remains in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `8` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `229` - Basic Gateway | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `150` - Gateway Open SCS | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |


These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system/model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Configure through the device web pages. The sheet lists MyHomeBticino/MyHomeLegrand apps and scenario recall through MHVisual/Supervision Gadget; it excludes scenario programming. It excludes video entry, sound, anti-intrusion, advanced shutter management, Lighting Management and advanced scenarios. It explicitly prohibits use as a third-party SDK/development or integration gateway and points to F454 for that role. Configure two recovery questions and answers: both are required and this is the published password-recovery route. The installer manual documents Ethernet/DHCP, OPEN/HMAC authentication and an IP range permitted without OPEN password, plus an auxiliary channel that enables/disables remote access. Power-on while holding the button for 3 seconds selects temporary recovery IP; 10 seconds restarts; 20 seconds restarts into dynamic IP selection. Red 1 s on/off searches for Ethernet; green 1 s on/3 s off indicates network found.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session/validation method remains in [Programming](../../programming/).

## Source reconciliation

The catalogue offers Basic gateway Object `229` and OpenSCS gateway Object `150` candidates, but that metadata does not override the manufacturer’s explicit SDK/integration prohibition or guarantee third-party apps. The sheet prints a malformed netmask using colons; the installer manual corroborates 255.255.255.0. App names and remote-service instructions are historical publication evidence, not verification that those cloud services still operate. Web password recovery and OPEN authentication are distinct mechanisms. The database brand label Legrand BTicino groups both commercial records. Human-facing identities use the manufacturer’s separately established BTicino and Legrand reference families; the raw grouping is preserved here as catalogue terminology.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `MQ01012-c-EN.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `MQ01012-c-IT.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `RA00125AB_I_EN.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `LE05548AC.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |

## Evidence limits and open work

Current app/cloud-service availability, production/firmware applicability of authentication, simultaneous sockets and installed diagnostics remain unverified.

No installed hardware revision or microcontroller fingerprint is retained for this cluster. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Canonical catalogue extraction and reconciliation are complete for the retained evidence; further documentation discovery, runtime corroboration and final evidence closure remain partial.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
