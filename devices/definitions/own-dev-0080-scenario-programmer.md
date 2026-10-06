# Scenario programmer

## Summary

`MH200` is a programmable MyHOME scenario controller that runs actions in response to bus events, times or conditions. TiMH200 lets it coordinate lighting, shutters, temperature, sound and door-entry functions, with ordered actions, delays and repeatable sequences; the retained manual limits a collection to 300 scenarios.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0080` | Project identity |
| Technical description | Scenario programmer | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `MH200` | Canonical commercial records |
| Catalogue item | `98` | Canonical catalogue |
| Main catalogue system | Integration function | Canonical catalogue |
| Item model / `modobj` | `4` | Canonical inventory |
| Firmware definition | `2.0.0` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Scenarios, Integration, Ethernet programmer | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `MH200` | Established identity | canonical commercial record for item `98` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `TiMH200_FR` | software/configuration manual | TiMH200 software Version 2.0;06/07-01 PC (June 2007) | Cover and printed/PDF pp. 3–58;complete Version 2.0 software manual;project/network/security,scenario families and limits;hardware installation sheet not included | [Archived original](https://archive.openwebnet-ha.org/sha256/00/64/00649f4d577863eab8a6366529468044a7fdce4d2b868cdcd09b8f4f634a01ea.pdf) | [Official source](https://www.bticino.be/sites/default/files/Service-en-support/software-en-schemas2/Audio-Video/MH200/Version%202_1_00/TiMH200_FR.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Network/programming interfaces | Ethernet LAN and serial setup via 335919/3559; direct crossover or remote IP/password transfer | TiMH200_FR.pdf, printed/PDF pp. 8, 21–25 |
| Hardware scope | One catalogue Module; exact enclosure, supply/current/environment ratings not established by this software manual | Canonical firmware `210`; TiMH200 software scope |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `98` | Canonical catalogue |
| Technical item | Scenario programmer | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `4` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `4` | Yes | Canonical item/system relationship |

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
| `98` | `MH200` | `1` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `210` | `2` | `0` | `0` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `210` | `513` | BTicino (key `1`) | `0` | external software | `TiMH200_0200` |

All 1 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `210` | `1` | `61` Scenario scheduler | Fixed/designated metadata | `1188` | `61` | `639` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `210` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `210` | Ethernet | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `210` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `210` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `210` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `210` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity; Local Dynamic IP |
| `210` | `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `210` | `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` (publisher catalogue documentation default) | Public IP address |
| `210` | `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity; Public Dynamic IP |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `61` - Scenario scheduler

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity |
| `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` (publisher catalogue documentation default) | Public IP address |
| `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Device-specific interpretation

Firmware `210` is the catalogue-default Official 2.0.0 applicability record, with one Module/Object `61`, Ethernet connection and Product Programming mode 3. The TiMH200 manual cover says software Version 2.0; its publisher download folder says Version 2_1_00. Neither folder name nor software version changes the retained catalogue firmware tuple or establishes installed 2.1.0. Firmware/Object network masks are formatting templates, not complete numeric domains. Static-LAN flag 0 and public CONNECTION_METHOD 0=DHCP use different enumerations; do not swap them. Reusable IS_GATEWAY 0/1 defaults to disabled despite `EN_DEVICE.is_gateway`=0; these are separate scopes. The manual requires static LAN addressing, whereas the reusable catalogue also lists DHCP; retain the discrepancy. The manufacturer documentation gives special predefined configuration IP `192.168.10.1`, separate from its catalogue default `192.168.1.35`; these are published settings. No Virgin/condition/filter/conversion/package is associated. One BTicino parameter-file record 513 is retained with type/path/line scope; its payload is unexamined.

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
| `DIMENSION 1` | corroborate technical identity for catalogue item `98` / `modobj = 4` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`61`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Collection limits | 300 scenarios; at most 20 with Repeat Actions enabled and/or accumulated delays over 1 min; at most 5 sharing a start event | TiMH200_FR, p. 54 |
| Scenario limits | Up to 20 objects each in If, Stop if, Only if; up to 40 actions | TiMH200_FR, p. 54 |
| Execution | If/Stop if multiple events use OR; Only if uses configurable AND/OR; Execute is required and actions run in insertion order; delays and random delays occur only in Execute | TiMH200_FR, pp. 33–34, 39, 45–47 |
| Scenario controls | CEN controls enable/disable individual scenes; collection control can stop all active scenes; repeat and Execute at device restart are per-scenario options | TiMH200_FR, pp. 27, 30, 47 |
| Function families | ON/OFF, 10/100-level dimmers, motors, `F420`/N4681 scenes, CEN, time, AUX9 channels, alarms, temperature zones `1..99`, sound, door entry and actuator lock/unlock | TiMH200_FR, pp. 35–44 |
| Placement restrictions | Temperature central/scenario/program only Execute; zone state trigger/stop or Execute but not Only if, probe Only if. Sound except amplifier only Execute; multichannel sources need matrix. Door-entry interphone in If/Stop if; camera in If/Stop if/Execute; neither in Only if. Staircase, lock and answering-machine controls only Execute | TiMH200_FR, pp. 41–44 |
| Network/security settings | Static LAN required by manual; clock/time-zone/master synchronization; OPEN password `5..9` numeric characters, trusted-IP ranges, AUX channel remote access: ON disables, OFF enables, max 20 blocked OPEN commands | TiMH200_FR, pp. 13–17 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Use Product Programming with the exact TiMH200 software scope. Save .wwz project, configure network/clock/security and installation contexts, create/activate the scenario collection, then download to `MH200`; upload retrieves its stored project (pp. 12–25). Firmware update uses publisher .fwz; collections export/import .osj and individual scenes .osx (pp. 24, 28). For version 1 projects with time/day objects, the manual recommends reopening and reactivating all scenes before transfer (p. 20). Manufacturer documentation gives predefined configuration IP `192.168.10.1` (p. 22), distinct from its catalogue default `192.168.1.35`. The editor permits 11 installation contexts/10 `F422` interfaces with 81 local addresses and actuator `11..99` excluding multiples of 10 (pp. 18–19); do not promote this 2007 software limit over later `F422` limits. Repeat needs a stop condition or bounded time; resume-at-restart is an explicit option, not guaranteed for every scene. Sound volume/source actions also require amplifier ON; staircase ON needs corresponding OFF with delay if actuator lacks one (pp. 43, 47).

## Source reconciliation

The exact `MH200` manual cover states TiMH200 Version 2.0 and 06/07-01 PC, correcting the previous 2.03 label. Its publisher directory `Version2_1_00` is provenance, not proof that the device is installed on firmware `2.1.0`. Catalogue firmware `210` remains 2.0.0. Software scenario icons are editor objects, not additional diagnostic Modules or catalogue Object numbers. The manual static-LAN requirement conflicts with reusable DHCP capability, and its special predefined-IP mode has a different address from the historical catalogue defaults. Online discovery identified a T9014B (06/06-01 PC) instruction mirror, whose manufacturer endpoints returned 403/404; its hardware claims are not incorporated, and `MH200N` electrical specifications are excluded.

Catalogue interpretation is detailed under [Object configuration surfaces](#object-configuration-surfaces); these software records do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- Exact `MH200` hardware installation original T9014B was not retained from a manufacturer endpoint; its enclosure, supply/current and temperature values remain unasserted. The retained software manual is complete and reviewed through printed p. 58; no later `MH200N` data is imported.
- The firmware parameter 513 payload, the CD installation/user manual and actual firmware .fwz are unexamined. The source’s network templates, manual/static-vs-DHCP discrepancy and installed execution behavior remain bounded.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0071-0080-2026-10-06.md#own-dev-0080)
