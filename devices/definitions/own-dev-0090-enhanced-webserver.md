# Enhanced Webserver

## Summary

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
| `mh_diff-sonore2008.pdf` | Two-wire sound-system technical guide | historical publisher guide | F453 supervision compatibility: printed p. 38 / PDF p. 38; not a complete F453 installation manual | [Archived PDF](https://archive.openwebnet-ha.org/sha256/f4/96/f496f0943750657477c03e43eae6708271a8e798101831991ebc02904673dccd.pdf) | [Publisher PDF](https://assets.legrand.com/general/cession/bt/np-ft-gt/mh_diff-sonore2008.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Programming / connectivity surface | Ethernet | canonical inventory |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `912` | Canonical catalogue |
| Technical item | Enhanced Webserver | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `42` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `5` | `2` | `0` | `8` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

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

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `5` | Product Programming | supported configuration route for this Device family |

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

Catalogue system identifiers are not `WHO` numbers. The source establishes the roles shown, not a complete command vocabulary or proof of every installed function. Correlate the selected role with [Functional Protocol](../../functional/) before sending functional commands. Product-specific behavior and transport constraints remain unestablished where no direct source is retained.

The sound-system guide, printed p. 38, / PDF p. 38, explicitly includes F453 in the supervision compatibility table, with version-6 applicability for the HC/HS4684 touchscreen. This establishes that documented compatibility context, not a complete gateway command inventory.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

The catalogue registers Product Programming for this technical item. Use the firmware-specific fields, selected Module/Object and effective restrictions on this page as the configuration boundary. This item has 2 declared Modules; retain the individual Module placements when preparing a project.

No retained product manual establishes the complete commissioning, reset, transfer or update procedure for these commercial identities. Obtain that evidence before prescribing a Device-specific sequence. The catalogue mode registration alone does not establish a universal physical-button or gateway-session workflow.

## Source reconciliation

The canonical MyHOME Suite `3.5.38` catalogue establishes the commercial-to-item association, firmware definitions, Module placements, reusable configuration values and relationship-specific conditions/filters recorded above. Retained publisher evidence is listed in Documentation; its exact Device coverage is stated there. Catalogue descriptions and Object names therefore remain implementation evidence; electrical limits, commissioning procedures and runtime behavior cannot be borrowed from sibling products.

The corrected tables distinguish external Object/Virgin Object numbers from database keys, firmware status from wildcard applicability and actual Module slots from slot row IDs. Remaining source acquisition and runtime checks are listed below.

## Evidence limits and open work

- Locate and archive dedicated publisher documentation for the exact commercial references where available.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate relation filters and condition-selected topology against MyHOME Suite and controlled hardware observations.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
