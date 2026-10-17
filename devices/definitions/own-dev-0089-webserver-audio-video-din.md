# Webserver Audio/Video DIN

## Summary

The `F453AV` web server provides browser-based supervision of MyHOME installations, including lighting, shutters, alarms, temperature control and audio/video services. It adds CCTV viewing and a video-door-entry answering service, with documented differences between PC and handheld interfaces and a single simultaneous web session.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0089` | Project identity |
| Technical description | Webserver Audio/Video DIN | Canonical catalogue |
| Commercial identities | `F453AV` | Canonical commercial records |
| Catalogue item | `207` | Canonical catalogue |
| Main catalogue system | Integration function | Canonical catalogue |
| Item model / `modobj` | `12` | Canonical inventory |
| Firmware definition | `3.0.8`; `3.0.10` | Canonical firmware catalogue |
| Declared Modules | `2` | Canonical firmware catalogue |
| Categories | Integration function, Integration gateway | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F453AV` | Established catalogue identity | canonical commercial record for item `207` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| `mh_diff-sonore2008.pdf` | Two-wire sound-system technical guide | historical publisher guide | `F453AV` multi-channel support: printed p. 28 / PDF p. 28; system role table printed p. 38 / PDF p. 38 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/f4/96/f496f0943750657477c03e43eae6708271a8e798101831991ebc02904673dccd.pdf) | [Publisher PDF](https://assets.legrand.com/general/cession/bt/np-ft-gt/mh_diff-sonore2008.pdf) |
| `BT00383-a-EN.pdf` | exact-product technical sheet | Printed `BT00383-a-UK`; filename -EN | Both pages: technical ratings, controls/connector/LED legend, power/network/bus diagrams | [Archived original](https://archive.openwebnet-ha.org/sha256/32/de/32de6b7809c112f6dce610302780e43a33a5a500497abff6d704002624e45f0d.pdf) | [Publisher source](https://www.homesystems-legrandgroup.com/MatrixENG/liferay/bt_mxLiferayCheckout.jsp?fileFormat=generic&fileName=BT00383-a-EN.pdf&fileId=58107.23188.48006.45026) |
| `U0990C_S_UK.pdf` | TiF453AV software manual | U0990C, 01PC-10W06 | Complete substantive software manual PDF/printed pp. 4–35: all settings, services, .wwz transfer, .fwz update and Device info | [Archived original](https://archive.openwebnet-ha.org/sha256/ac/23/ac238e48e634cbf0fe83f685ad4b2f4011b173452693a8777b9786a31374e443.pdf) | [Publisher source](https://www.homesystems-legrandgroup.com/MatrixENG/liferay/bt_mxLiferayCheckout.jsp?fileFormat=generic&fileName=U0990C_S_UK.pdf&fileId=58107.23188.51017.55872) |
| `U0990C_U_UK.pdf` | `F453AV` user guide | U0990C, 01PC-10W06 | Complete substantive manual PDF/printed pp. 4–46: web PC/handheld functions, admin settings, deployment and troubleshooting | [Archived original](https://archive.openwebnet-ha.org/sha256/45/23/452374d5de9776539a27aa834b29438f0bfeaa2b482a17943df26ebe4b65afa5.pdf) | [Publisher source](https://www.homesystems-legrandgroup.com/MatrixENG/liferay/bt_mxLiferayCheckout.jsp?fileFormat=generic&fileName=U0990C_U_UK.pdf&fileId=58107.23188.51017.55872) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Power / temperature / mounting | `18..27 Vdc` DC supply and `18..27` V SCS bus; `5..35 °C`; 10 DIN modules | `BT00383-a-UK` p. 1 |
| Ethernet | RJ45, 10/100 Mb/s; direct PC crossover or network hub/switch connection | `BT00383-a-UK` pp. 1–2 |
| Power connection | Separate DC supply; diagrams show 346000 and 346020 supply arrangements | `BT00383-a-UK` pp. 1–2; not direct mains into `F453AV` |
| Bus interfaces | Automation/SCS, alarm and two-wire AV IN shown; separate AV connector is future application | `BT00383-a-UK` p. 1 legend and p. 2 diagrams |
| USB / Aux | USB configuration/update with 3559 shown; other USB labels technical support only; front Aux future application | `BT00383-a-UK` pp. 1–2 |
| LED indications | Speed ON 100/OFF 10 Mb/s; Full ON full/OFF half duplex; Link Ethernet presence; System startup ON/OFF/ON | `BT00383-a-UK` p. 1; `U0990C_U` p. 46 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `207` | Canonical catalogue |
| Technical item | Webserver Audio/Video DIN | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `12` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `12` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Burglar alarm | private riser | Canonical item/bus relationship |
| Multimedia | private riser | Canonical item/bus relationship |
| Multimedia | public riser | Canonical item/bus relationship |
| Network | LAN | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `207` | `F453AV` | `1` | `5` | `BTicino_Undefined_Webserver Audio/Video DIN` |

| Record | Visible | Dependent | Gateway flag | Visibility type |
| --- | --- | --- | --- | --- |
| `207` | `1` | `0` | `1` | `EDC` |

These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | `0` | `8` | `2` | Catalogue default | Official |
| `2` | `3` | `0` | `10` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `2` | `168` | BTicino (key `1`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `2` | `169` | BTicino (key `1`) | `0` | SVM | `207_3.0_BT\xml\SVM\svm.xml` |
| `2` | `170` | BTicino (key `1`) | `0` | Extra | `207_3.0_BT\xml\Extra\extra.xml` |
| `2` | `171` | BTicino (key `1`) | `0` | Director | `207_3.0_BT\xml\DIRECTOR\director.xml` |
| `2` | `172` | BTicino (key `1`) | `0` | Protocol and other device parameters | `207_3.0_BT\xml\Protocol\protocol.xml` |

All 5 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `2` | `1` | `56` Web Server Audio / Video 2 Wires (`F453AV`) | Fixed/designated metadata | `621` | `56` | `427` |
| `2` | `2` | `150` Gateway Open SCS | Fixed/designated metadata | `622` | `150` | `428` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `2` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `2` | Ethernet | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `2` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `2` | `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway; Boolean flag for Gateway device |
| `2` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `2` | `VCD_PORT` | `#####` = Video port | `10000` | Video port; VIdeo port |
| `2` | `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `2` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `2` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity; Local Dynamic IP |
| `2` | `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` (publisher catalogue documentation default) | Public IP address |
| `2` | `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity; Public Dynamic IP |
| `2` | `S_VCT` | `0` = Disable; `1` = Enable | `0` | Voice box videos; Voice Box Vds |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `56` - Web Server Audio / Video 2 Wires (`F453AV`)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` (publisher catalogue documentation default) | Public IP address |
| `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity |
| `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `VCD_PORT` | `#####` = Video port | `10000` | Video port |
| `FW_VER` | `######` = Firmware version | `1.0.0` | Firmware version |
| `S_VCT` | `0` = Disable; `1` = Enable | `0` | Voice box videos |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Object `150` - Gateway Open SCS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Device-specific interpretation

Firmware `2` has builds `3.0.8` and `3.0.10`, both under the Official/default firmware definition with two Modules: `56` in slot `1` and Open SCS Object `150` in slot `2`. No Virgin, condition, filter or conversion is stored. Product Programming `3`, one Ethernet connection and five parameter associations `168..172` (brand `1`, line `0`) are explicit; no package association is stored. Commercial metadata marks this reference as a gateway with visibility_type `EDC`, while reusable `IS_GATEWAY` defaults to `0`: these are different scopes. Reusable `FW_VER` default `1.0.0` differs from both firmware build tuples 3.0.8/3.0.10; preserve both without choosing an installed value. VCD_TYPE `10000` and CMD_TYPE `20000` have no protocol-unit mapping here. Firmware identity and Object AID fields are not alias proof. LAN connection `0` denotes static IP, public connection `0` DHCP; their enums/defaults are not interchangeable. Static network defaults and video-answering/SMTP fields are reusable software data, not observed network settings, a physical modem connector or proof of every source-era service.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | - | None | - | No relation-specific filters associated | - | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `207` / `modobj = 12` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`56`, `150`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `56` Web Server Audio / Video 2 Wires (F453AV) | Integration function | Firmware/Object capability association; resolve the slot and configuration first |
| `150` Gateway Open SCS | Integration function | Firmware/Object capability association; resolve the slot and configuration first |

These are catalogue Object/system associations, not `WHO` numbers, physical connector claims or observed command acceptance. Resolve the active Module/Object and its restrictions before using the [Functional Protocol](../../functional/).

### Published product functions

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Web controls | Scenarios; lights ON/OFF/dimmer/timing/flashing; shutters UP/DOWN/STOP; restore shed loads; alarms/status; thermal settings/diagnosis | `U0990C_U` pp. 10–24, 30–44 |
| Configured web-page limits | Scenarios and lights: 9 pages × 8 keys; automation: 10 × 8; descriptions max 15 characters; scene-module key `1..16` | `U0990C_S` pp. 17–20 |
| CCTV / answering | Software: up to 20 cameras and 10 entrance panels, `1..16` photos/call; camera-linked intrusion email; handheld page displays 4 cameras in monochrome | `U0990C_S` pp. 24–27; `U0990C_U` pp. 13–15, 28, 34 |
| Audio / resource sharing | Real-time camera audio/video documented for PC; CCTV unavailable while answering service records | `U0990C_U` pp. 4, 13 |
| Temperature controls | 4/99-zone units, 3 winter and 3 summer programs, 16 scenarios per season; manual 5..39.5 °C in 0.5 °C steps, antifrost 7 °C/protection 35 °C; season cannot change remotely | `U0990C_S` pp. 22–23; `U0990C_U` pp. 19–23, 40–43 |
| Sessions / authentication | One simultaneous web access; user/admin roles; inactivity 1/2/5/15 min; configured IP ranges may bypass authentication | `U0990C_U` pp. 8, 26, 29; `U0990C_S` pp. 13–14 |
| Remote command restrictions | AUX `1..9` ON disables / OFF enables remote access; signaling actuator; up to 20 forbidden OPEN command patterns | `U0990C_S` pp. 15–16 |
| Email / diagnosis | SMTP authentication/user/password/port/TLS/StartTLS/trust file in software; fault/alarm/photo notifications | `U0990C_S` pp. 28–29; service compatibility untested |
| Sound supervision | `F453AV` supports multichannel as well as single-channel sound systems; MHVISUAL version 6 compatibility | French sound guide printed/PDF pp. 28, 38 |
| Confirmation boundary | Command sent reports sending; user must request/check changed control-unit or zone state to confirm acceptance | `U0990C_U` pp. 20–21, 40–42 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

TiF453AV creates/edits .wwz projects, downloads them to the server and uploads its configuration for inspection/editing. Ethernet requires compatible addresses; the software calls for a static unique server address, netmask, router and DNS (`U0990C_S` pp. 5–12, 30–33). Transfer selection offers Ethernet with IP/OPEN password, Serial with COM selection/search, or USB auto-recognition (p. 32). The catalogue independently stores one Ethernet connection. Do not infer extra physical connectors solely from the generic connection selector.

Firmware update selects a manufacturer .fwz and connection mode; Device info request retrieves technical firmware/hardware information (pp. 34–35). No complete factory-reset procedure is established. Local browser access and remote router/modem examples are documented in `U0990C_U` pp. 5–8, 25–29, 45–46; these are historical deployment examples, not proof of a modem socket or present portal availability. User guide p. 6 describes source-era SSL 128-bit protection; its security assurances and certificate-warning bypass are not represented as current security recommendations.

## Source reconciliation

BT00383-a-EN.pdf is the retained publisher filename; its printed document code is `BT00383-a-UK`. Both U0990C manuals carry 01PC-10W06 and explicitly cover `F453AV`. Software upload is consistently device-to-PC in overview pp. 5/31, although p. 33 incorrectly says the project is loaded onto the device; the direction is preserved with that discrepancy. User manual headings retain MH2/TIMSERVER2 names and modem references; they do not rename the exact cover device or establish extra physical ports. Software 20-camera capacity and handheld 4-camera display are separate surfaces. Functional controls/settings exceed the small canonical schemas; the whole retained software menu is described with its source limits rather than forced into Object fields. `F453` and `F454` remain separate items; the technical-sheet future/support ports are not promoted to active services. Exact-manual revision coverage does not establish installed catalogue firmware `3.0.8` or `3.0.10` or the contents of unexamined later firmware packages.

Catalogue interpretation is detailed under [Object configuration surfaces](#object-configuration-surfaces); the complete firmware, topology and restriction tables remain authoritative for software applicability.

## Evidence limits and open work

- Examine newer manufacturer firmware/revision downloads and their applicability before assigning version-specific changes.
- Corroborate installed network settings, active Objects, command execution, email/TLS and video resources on controlled hardware; source-era services remain unverified.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0081-0090-2026-10-06.md#own-dev-0089)
