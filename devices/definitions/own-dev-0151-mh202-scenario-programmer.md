# MH202 scenario programmer

## Summary

MH202 runs up to 300 simple or advanced MyHOME scenarios. Scenarios can respond to buttons, time/date and system events, enabling sequences such as presence simulation. It observes burglar-alarm status as a trigger but cannot arm or disarm that alarm itself.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0151` | Project identity |
| Technical description | MH202 scenario programmer | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `003535`, `MH202` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1902` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `5` | Main association; independent of project ID |
| Firmware definition | `561` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Scenarios, Gateways and interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `003535` | Established catalogue identity | Manufacturer database commercial record `2362` explicitly links this SKU to item `1902` |
| BTicino | `MH202` | Established catalogue identity | Manufacturer database commercial record `2222` explicitly links this SKU to item `1902` |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `MH202` | Scenario programmer | Canonical commercial record `2222` |
| `003535` | Scenario programmer | Canonical commercial record `2362` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ01013-b-IT.pdf` | Legacy manufacturer technical documentation | `MQ01013-b-IT; 06/05/2015` | PDF pp. 1–3 inspected: exact MH202/003535 ratings, controls, configuration and topology | [Archived original](https://archive.openwebnet-ha.org/sha256/43/e2/43e2e7bb8a63bc871fd8a8935c53e9fbf8f6a4a87932f4334e7896cd4671d4db.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/MQ01013-b-IT.pdf) |
| `MQ01013-b-EN.pdf` | English counterpart of manufacturer-linked document | `MQ01013-b-EN; 06/05/2015` | PDF pp. 1–3 inspected: exact MH202/003535 ratings, controls, configuration and topology | [Archived original](https://archive.openwebnet-ha.org/sha256/70/a1/70a196b30eb53de2f4a9a0cc00a82d4ee6d0f2ee61b91eae38aef9be30d268e8.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MQ01013-b-EN.pdf) |
| `RA00127AB_S_IT.pdf` | Legacy manufacturer technical documentation | `RA00127AB_S_IT; printed publication date not established` | PDF pp. 8,12–14: Italian terminology/configuration cross-check; remaining translation sections unexamined | [Archived original](https://archive.openwebnet-ha.org/sha256/5f/21/5f21364beb2e8f4e21729f6fb65d7e474862dc01141e55a44885bf1dbd462c20.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/RA00127AB_S_IT.pdf) |
| `RA00127AB_S_EN.pdf` | English counterpart of manufacturer-linked document | `RA00127AB_S_EN; printed publication date not established` | PDF pp. 4–46: complete scenario function families, trigger/condition/action limits and configuration; worked examples pp. 47–55 unexamined | [Archived original](https://archive.openwebnet-ha.org/sha256/da/b0/dab01650cb9227aa85ae8a2569cda582ac7f6b8bdf7621e5059f67adbc9cf128.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/RA00127AB_S_EN.pdf) |
| `RA00127AB_U_IT.pdf` | Legacy manufacturer technical documentation | `RA00127AB_U_IT; printed publication date not established` | PDF pp. 4–9: Italian setup/control cross-check | [Archived original](https://archive.openwebnet-ha.org/sha256/a2/e4/a2e421e619988f7e50a8e8f8d50c61e9a2d2d3b366e0e66fb563106a43e4eb46.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/RA00127AB_U_IT.pdf) |
| `RA00127AB_U_EN.pdf` | English counterpart of manufacturer-linked document | `RA00127AB_U_EN; printed publication date not established` | PDF pp. 4–9: setup, controls, network, scenario control and limits | [Archived original](https://archive.openwebnet-ha.org/sha256/31/b4/31b4ec525e26e17a1532e9c2ea9f240c84ec31c51d8d4287af04b03810f5b7e2.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/RA00127AB_U_EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1902`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply / maximum draw | `18..27 Vdc / 55 mA` | `MQ01013-b-EN` p. 1 |
| Temperature / size | `5..45 °C; 6 DIN modules` | `MQ01013-b-EN` p. 1 |
| Scenario capacity | `up to 300` | `MQ01013-b-EN` p. 1; `RA00127AB_U_EN` p. 4 |
| Interfaces | `SCS BUS; RJ45 Ethernet 10/100 Mbit; USB for PC configuration/update` | `MQ01013-b-EN` p. 1 |
| Installation limit | `one MH202 per system` | `MQ01013-b-EN` p. 3 |
| `CEN` triggers | `button-to-scenario association through MyHOME_Suite` | `RA00127AB_S_EN` pp. 14,16–19 |
| Browser sessions | `user manual says several simultaneous users cannot connect` | `RA00127AB_U_EN` p. 5; web access only |
| Factory OPEN password | `12345, documented default` | `RA00127AB_S_EN` p. 12; documented public default |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1902` | Canonical catalogue |
| Technical item description | Scenario programmer | Canonical catalogue |
| Item family | 0; key `19` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `5` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `5` | Yes | Canonical item/system relationship |

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
| `561` | `1` | `0` | `0` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `561` | `314` | BTicino (key `1`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `561` | `315` | BTicino (key `1`) | `0` | SVM | `1902_1.0_BT\xml\SVM\svm.xml` |
| `561` | `316` | BTicino (key `1`) | `0` | Extra | `1902_1.0_BT\xml\Extra\extra.xml` |
| `561` | `317` | BTicino (key `1`) | `0` | Director | `1902_1.0_BT\xml\DIRECTOR\director.xml` |
| `561` | `318` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1902_1.0_BT\xml\Protocol\protocol.xml` |
| `561` | `319` | Undefined (key `5`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `561` | `320` | Undefined (key `5`) | `0` | SVM | `1902_1.0_LGG\xml\SVM\svm.xml` |
| `561` | `321` | Undefined (key `5`) | `0` | Extra | `1902_1.0_LGG\xml\Extra\extra.xml` |
| `561` | `322` | Undefined (key `5`) | `0` | Director | `1902_1.0_LGG\xml\DIRECTOR\director.xml` |
| `561` | `323` | Undefined (key `5`) | `0` | Protocol and other device parameters | `1902_1.0_LGG\xml\Protocol\protocol.xml` |
| `561` | `360` | Legrand (key `2`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `561` | `361` | Legrand (key `2`) | `0` | SVM | `1902_1.0_LG\xml\SVM\svm.xml` |
| `561` | `362` | Legrand (key `2`) | `0` | Extra | `1902_1.0_LG\xml\Extra\extra.xml` |
| `561` | `363` | Legrand (key `2`) | `0` | Director | `1902_1.0_LG\xml\DIRECTOR\director.xml` |
| `561` | `364` | Legrand (key `2`) | `0` | Protocol and other device parameters | `1902_1.0_LG\xml\Protocol\protocol.xml` |

All 15 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `561` | `1` | `61` Scenario scheduler | Fixed/designated metadata | `2350` | `61` | `1005` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `561` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `561` | Ethernet | Canonical firmware/connection association |
| `561` | USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `CEN trigger` | unique control address distinct from actuators; key-to-scenario mapping in Suite | `MQ01013-b-EN` printed/PDF pp. 1-3; `RA00127AB_S_EN` pp. 10-20,21-46; `RA00127AB_U_EN` pp. 4-9 |
| `Start / Only if / Stop / Action` | trigger / AND-OR conditions / stop event / sequence | `MQ01013-b-EN` printed/PDF pp. 1-3; `RA00127AB_S_EN` pp. 10-20,21-46; `RA00127AB_U_EN` pp. 4-9 |
| `Repeat / restart after power loss` | explicit scenario options, not unconditional defaults | `MQ01013-b-EN` printed/PDF pp. 1-3; `RA00127AB_S_EN` pp. 10-20,21-46; `RA00127AB_U_EN` pp. 4-9 |
| `Panic key` | stops all sequences; blocks new ones until power cycle; completed actions not undone | `MQ01013-b-EN` printed/PDF pp. 1-3; `RA00127AB_S_EN` pp. 10-20,21-46; `RA00127AB_U_EN` pp. 4-9 |
| `Clock` | time zone; summer time; master; optional astronomical coordinates | `MQ01013-b-EN` printed/PDF pp. 1-3; `RA00127AB_S_EN` pp. 10-20,21-46; `RA00127AB_U_EN` pp. 4-9 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `561` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `561` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.40` | Local IP address; public documentation value, not an observed installation |
| `561` | `FW_VER` | `######` = Firmware version | `1.0.0` | Firmware version |
| `561` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `61` - Scenario scheduler

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity |
| `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` | Public IP address; public documentation value, not an observed installation |
| `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
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

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution remains in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `5` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `61` - Scenario scheduler | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system/model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Create, send and retrieve configuration and update firmware using MyHOME_Suite. `CEN` controls may be anywhere on the system but their A/PL addresses must differ from actuator addresses; upper/lower keys are individually mapped to scenarios. In logical expansion, place MH202 on the private riser. Configure fixed/DHCP addressing, DNS, unique scheduler ID, time zone, summer time, clock-master mode and optional astronomical coordinates. Web user/admin credentials and OPEN authentication are separate. Build Start events, Only if conditions, Stop events and Action sequences; multiple conditions use AND/OR operators, and repeat/restart-after-power-loss are explicit options. Stopping does not undo completed actions; already-started delayed commands complete their cycle. The global panic key halts all scenario sequences and blocks new ones until power is removed and restored. The web interface enables/disables or runs configured scenarios; administrator pages expose time/network/access parameters.

Apply the firmware-specific restrictions above. The generic session/validation method remains in [Programming](../../programming/).

### Scenario composition and limits

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Lighting and motors | General/room/group or point addressing; Dimmer100 level and step1–100%. Start/Stop events and Actions differ from OnlyIf state tests. | Software EN pp. 21–25 |
| Scenario and CEN controls | Scenario module/Plus triggers and scenario controls; CEN Plus Start/Stop; CEN addresses must not duplicate actuator addresses. | Software EN pp. 26–28; MQ p. 3 |
| Time | Delay and random delay are Action-only; astronomical sunrise/sunset/day/night supply Start/Stop/OnlyIf events. Dates permit ** wildcards. | Software EN pp. 29–31 |
| Auxiliary/alarm | AUX1–9 states; intrusion events/zone triggers are reactions, not alarm arm/disarm commands. | Software EN pp. 32–33 |
| Temperature | 99/4-zone central programs/scenarios are Action-only; probe/external probe states are OnlyIf tests. Zone commands and triggers have their own placement. | Software EN pp. 34–37 |
| Sound | Amplifier controls require it to be on before volume/source changes. The text broadly limits other sound objects to Start, but the power-amplifier subsection expressly also defines OnlyIf/Action uses; preserve that exception. | Software EN pp. 38–40 |
| Video entry | Staircase-light/entrance-panel/door-lock controls are Action-only; camera events cannot be OnlyIf tests. Internal-unit events are Start/Stop. Pair stair-light ON with delayed OFF. | Software EN pp. 41–42 |
| Special/supervision | Lock/Unlock is Action-only and needs an unlock path. StopAndGo has distinct open/close/reactivation controls. | Software EN pp. 43–44 |
| Sensors/variables | Presence, motion, light, twilight, rain and wind tests; counter in OnlyIf/Action and Boolean variables. These are scenario objects, not local Device Module instances. | Software EN pp. 45–46 |

Web inactivity timeouts are1,2,5 or15 minutes (software p. 13). Ethernet access disabling uses both an AUX channel and its specified actuator: reserve both for this function. The user guide p. 7 confirms “Command sent”; that acknowledgement is not a measurement that every downstream action completed. Save/send and receive configuration through Suite; updates use .fwz (software pp. 5–8).

## Source reconciliation

The exact sheet’s alarm example means reacting to alarm state, not engaging/disengaging the alarm; its explicit prohibition is preserved. The software manual documents lights, automation, scenarios, time, anti-intrusion events, temperature, contacts, audio, video-entry, special controls, Stop&Go, sensors and variables as scenario families. These are remote actions/triggers, not additional physical Modules. Catalogue Object `61` is the scheduler role; it does not imply MH200N interchangeability or a general-purpose integration gateway. The panic stop and ordinary scenario stop have different restart implications. The database brand label Legrand BTicino groups both commercial records. Human-facing identities use the manufacturer’s separately established BTicino and Legrand reference families; the raw grouping is preserved here as catalogue terminology.

### Reviewed source boundaries

The catalogue firmware IP default is `192.168.1.40`; the reusable LAN and public-IP fields default to `192.168.1.35`. These are manufacturer documentation values, not an installed address. The reusable `IS_GATEWAY=0` field and the commercial gateway flag describe different records. The scenario software limits alarm events to trigger/condition use; it does not make MH202 an alarm arming panel.

### Retained source accounting

| Original | Examined role / remaining scope |
| --- | --- |
| `MQ01013-b-IT.pdf` | PDF pp. 1–3 inspected: exact MH202/003535 ratings, controls, configuration and topology |
| `MQ01013-b-EN.pdf` | PDF pp. 1–3 inspected: exact MH202/003535 ratings, controls, configuration and topology |
| `RA00127AB_S_IT.pdf` | PDF pp. 8,12–14: Italian terminology/configuration cross-check; remaining translation sections unexamined |
| `RA00127AB_S_EN.pdf` | PDF pp. 4–46: complete scenario function families, trigger/condition/action limits and configuration; worked examples pp. 47–55 unexamined |
| `RA00127AB_U_IT.pdf` | PDF pp. 4–9: Italian setup/control cross-check |
| `RA00127AB_U_EN.pdf` | PDF pp. 4–9: setup, controls, network, scenario control and limits |

## Evidence limits and open work

Installed firmware, scheduler/time recovery, simultaneous-session behavior and actual execution/diagnostic responses remain uncorroborated.

No installed hardware revision or microcontroller fingerprint is retained for this cluster. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Canonical catalogue extraction and reconciliation are complete within the retained evidence scope. Unexamined documentation, source conflicts and runtime corroboration remain explicit limits of this review.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0151-0160-2026-10-07.md#own-dev-0151)
