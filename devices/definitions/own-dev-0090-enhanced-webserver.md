# Enhanced Webserver

## Summary

The `F453` is the catalogue’s Enhanced Webserver for MyHOME network integration, with a separate Open SCS gateway Module. The retained sound-system guide places it alongside `F453AV` for MHVISUAL version-6 multichannel supervision; a complete exact `F453` hardware and programming specification is still absent.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0090` | Project identity |
| Technical description | Enhanced Webserver | Canonical catalogue |
| Commercial identities | `F453` | Canonical commercial records |
| Catalogue item | `912` | Canonical catalogue |
| Main catalogue system | Integration function | Canonical catalogue |
| Item model / `modobj` | `42` | Canonical inventory |
| Firmware definition | `2.0.8` | Canonical firmware catalogue |
| Declared Modules | `2` | Canonical firmware catalogue |
| Categories | Integration function, Integration gateway | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F453` | Established catalogue identity | canonical commercial record for item `912` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| `mh_diff-sonore2008.pdf` | Two-wire sound-system technical guide | historical publisher guide | `F453` supervision compatibility: printed p. 38 / PDF p. 38; not a complete `F453` installation manual | [Archived PDF](https://archive.openwebnet-ha.org/sha256/f4/96/f496f0943750657477c03e43eae6708271a8e798101831991ebc02904673dccd.pdf) | [Publisher PDF](https://assets.legrand.com/general/cession/bt/np-ft-gt/mh_diff-sonore2008.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Product role | Enhanced Webserver, one webserver and one Open SCS Module | Canonical item 912 / firmware `5`; not a connector count |
| Supply / dimensions / ports | Not established by an exact retained `F453` hardware specification | Do not borrow `F453AV` or successor `F454` ratings |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `912` | Canonical catalogue |
| Technical item | Enhanced Webserver | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `42` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `42` | Yes | Canonical item/system relationship |

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
| `912` | `F453` | `1` | `5` | Empty in source |

| Record | Visible | Dependent | Gateway flag | Visibility type |
| --- | --- | --- | --- | --- |
| `912` | `1` | `0` | `1` | `EDC` |

These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `5` | `2` | `0` | `8` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `5` | `5` | BTicino (key `1`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `5` | `6` | BTicino (key `1`) | `0` | SVM | `912_2.0_BT\xml\SVM\svm.xml` |
| `5` | `7` | BTicino (key `1`) | `0` | Extra | `912_2.0_BT\xml\Extra\extra.xml` |
| `5` | `8` | BTicino (key `1`) | `0` | Director | `912_2.0_BT\xml\DIRECTOR\director.xml` |
| `5` | `9` | BTicino (key `1`) | `0` | Protocol and other device parameters | `912_2.0_BT\xml\Protocol\protocol.xml` |

All 5 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `5` | `1` | `178` Enhanced Webserver | Fixed/designated metadata | `624` | `178` | `430` |
| `5` | `2` | `150` Gateway Open SCS | Fixed/designated metadata | `623` | `150` | `429` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `5` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `5` | Ethernet | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `5` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `5` | `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway; Boolean flag for Gateway device |
| `5` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `5` | `VCD_PORT` | `#####` = Video port | `10000` | Video port; VIdeo port |
| `5` | `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `5` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `5` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity; Local Dynamic IP |
| `5` | `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` (publisher catalogue documentation default) | Public IP address |
| `5` | `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity; Public Dynamic IP |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `150` - Gateway Open SCS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Object `178` - Enhanced Webserver

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` (publisher catalogue documentation default) | Public IP address |
| `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity |
| `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `VCD_PORT` | `#####` = Video port | `10000` | Video port |
| `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `S_VCT` | `0` = Disable; `1` = Enable | `0` | Voice box videos |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Device-specific interpretation

Firmware `5`=2.0.8 is Official/default with two Modules: `178` in slot `1` and Open SCS Object `150` in slot `2`. No Virgin, condition, filter or conversion is stored. Product Programming `3`, one Ethernet connection and five parameter associations `5..9` (brand `1`, line `0`) are explicit; no package association is stored. Commercial metadata marks this reference as a gateway with visibility_type `EDC`, while reusable `IS_GATEWAY` defaults to `0`: these are different scopes. Reusable `FW_VER` default `3.0.0` differs from the firmware tuple 2.0.8; preserve both without choosing an installed value. VCD_TYPE `10000` and CMD_TYPE `20000` have no protocol-unit mapping here. Firmware identity and Object AID fields are not alias proof. LAN connection `0` denotes static IP, public connection `0` DHCP; their enums/defaults are not interchangeable. Static network defaults and video-answering/SMTP fields are reusable software data, not observed network settings, a physical modem connector or proof of every source-era service.

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
| `DIMENSION 1` | corroborate technical identity for catalogue item `912` / `modobj = 42` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`150`, `178`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `150` Gateway Open SCS | Integration function | Firmware/Object capability association; resolve the slot and configuration first |
| `178` Enhanced Webserver | Integration function | Firmware/Object capability association; resolve the slot and configuration first |

These are catalogue Object/system associations, not `WHO` numbers, physical connector claims or observed command acceptance. Resolve the active Module/Object and its restrictions before using the [Functional Protocol](../../functional/).

### Published product functions

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Sound supervision compatibility | MHVISUAL version 6 with `F453AV` or `F453` for multichannel installations | French sound guide printed/PDF p. 38, MHVISUAL row |
| Software applicability | Enhanced Webserver Object `178` and Open SCS Object `150`; Ethernet catalogue connection | Canonical record only; reusable video/network fields do not establish every physical service |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Product Programming `3` and one Ethernet connection are catalogue-associated. No retained exact `F453` manual establishes a complete commissioning, project-transfer, reset or update sequence. Manufacturer legacy download listings identify TiF453 software/manual candidates, but attempted publisher downloads did not supply usable originals. No `F453AV` workflow is adopted here.

## Source reconciliation

The French sound-system table’s version 6 applies to the MHVISUAL software row, which names `F453AV` or `F453`. The separate H/L4684 touchscreen row instead says first-half 2007; it is not the version-6 statement. Correct the former touchscreen attribution without upgrading the source into a complete hardware specification. `F453` is distinct from `F453AV` and `F454`, and its reusable webserver/answering fields do not establish AV hardware. Candidate exact software/manual listings and unavailable endpoints remain discovery evidence only; their payloads and hardware claims are not incorporated.

Catalogue interpretation is detailed under [Object configuration surfaces](#object-configuration-surfaces); the complete firmware, topology and restriction tables remain authoritative for software applicability.

## Evidence limits and open work

- Obtain exact `F453` technical/user/software originals, including revision applicability, electrical ratings, ports and commissioning.
- Inspect parameter payloads `5..9` and corroborate active webserver/gateway fields; missing PDFs are documentation gaps, not an identity ambiguity.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0081-0090-2026-10-06.md#own-dev-0090)
