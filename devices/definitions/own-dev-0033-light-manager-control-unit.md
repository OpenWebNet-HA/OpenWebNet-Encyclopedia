# Light manager control unit

## Summary

The BMNE500 is a DIN-mounted Light Manager for lighting supervision, scheduling and scenarios. Its Ethernet interface and Open/SCS gateway functions connect the configured lighting system to software-based management and integration.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0033` | Project identity |
| Technical description | Lighting Management control unit, Ethernet interface, scenario scheduler and Open/SCS gateway | Catalogue + official documentation |
| Commercial identities | `BMNE500` | Catalogue |
| Catalogue item | `35` - “Light manager control unit” | Implementation evidence |
| Main catalogue system | Integration functions (`id_system = 26`) | Implementation evidence |
| Item model / `modobj` | `35` | Implementation evidence |
| Firmware definition | firmware `126`, version `2.0`, build `1` | Implementation evidence |
| Declared Modules | `3` | Implementation evidence |
| Categories | Gateway, Lighting management, Scenario scheduler, Integration | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMNE500` | Established identity | Canonical catalogue; canonical commercial record `35`; Gateway identity |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `U4554C_S4_EN` | TiBMNE500 software manual | 09/12-01 PC | printed/PDF pp. 4–62; all configuration, scheduling, scenario and transfer sections | [Archived PDF](https://archive.openwebnet-ha.org/sha256/e5/d2/e5d235a413023e1e004380ffc74c3e69c5589a474249b09f4a7892374c83a62c.pdf) | [Publisher PDF](https://dar.bticino.com/asset/Documents/U4554C_S4_EN.pdf) |
| `BMNE500-italian-product-sheet-IT.pdf` | Italian manufacturer product export | Retrieved 2026-10-06 | Exact BMNE500 supply, current, DIN size and software-configured role; printed/PDF p. 1 | [Archived original](https://archive.openwebnet-ha.org/sha256/f6/11/f6115b19a650fd2a1a105a232514dc7d07123d0127f258efad678e451c383b56.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMNE500) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / bus current | `12..27 V` / `8 mA` | `BMNE500-italian-product-sheet-IT.pdf`, printed/PDF p. 1 |
| Mounting | 6 DIN modules | `BMNE500-italian-product-sheet-IT.pdf`, printed/PDF p. 1 |
| Interfaces | SCS / Ethernet; Ethernet and serial project transfer described by the software manual | `U4554C_S4_EN.pdf`, printed/PDF pp. 55–62 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `35` | Canonical catalogue |
| Technical item description | Light manager control unit | Canonical catalogue |
| Item family | `8` - Network device | Canonical catalogue |
| Main system | `26` - Integration functions; `modobj` `35` | AS_ITEM_SYSTEM |
| Commercial records | `1` | EN_DEVICE |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `35` | Yes | Canonical item/system relationship |

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
| `126` | `2` | `0` | `1` | `3` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `126` | `948` | BTicino (key `1`) | `0` | external software | `TiBMNE500_0200` |

All 1 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No AS_FW_PACKAGE association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `126` | `1` | `127` Lighting manager | Fixed/designated metadata | `672` | `127` | `467` |
| `126` | `2` | `61` Scenario scheduler | Fixed/designated metadata | `673` | `61` | `468` |
| `126` | `3` | `150` Gateway Open SCS | Fixed/designated metadata | `674` | `150` | `469` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

The topology is explicit and fixed: slot `1` is Object `127` Lighting manager; slot `2` is Object `61` Scenario scheduler; slot `3` is Object `150` Gateway Open SCS.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `126` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `126` | Ethernet | Canonical firmware/connection association |
| `126` | USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `126` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `126` | `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `126` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `126` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `126` | `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `126` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `126` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity; Local Dynamic IP |
| `126` | `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity; Public Dynamic IP |

These are software/network fields, not physical configurators. Defaults shown here are catalogue defaults or examples; published address examples do not establish deployment settings. None of these values is an observation from a deployed BMNE500.

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

### Object `127` - Lighting manager

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Object `150` - Gateway Open SCS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Device-specific interpretation

The catalogue defaults `LAN_IP_ADDR_TYPE` to static `0`, whereas TiBMNE500 describes DHCP as the default. Firmware definition version `2.0`, build `1`, differs from the `FW_VER` field default `3.0.0`; neither is an observed installed version. All three reusable `SYSADDRESS` defaults are `1`, while the manual requires three individually unique function codes. Validate these product constraints before applying reusable defaults.

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
| `DIMENSION 1` | resolve `modobj = 35` and `BMNE500` identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | corroborate installed firmware against catalogue version `2.0` build `1` | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm the three fixed Objects: Lighting manager, Scenario scheduler and Open/SCS gateway | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect any exposed system/network addressing for the three fixed roles | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `SYSADDRESS`, gateway/network fields and software-programmed configuration without collapsing the three Objects | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

BMNE500 spans Lighting Management and integration functions: lighting supervision, scheduling/scenarios and Open/SCS gateway access.

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Lighting zones | Actuator/dimmer and sensor inventories feed logical zones; a zone must contain either actuators or dimmers, not a mixture; every zone requires scheduling. | `U4554C_S4_EN.pdf`, printed/PDF pp. 15–20 |
| Lighting regulation | Switch-on level, max/maintained illuminance, automatic ON/OFF and their delays, secondary-dimmer delta; movement delay, standby level/timer and OFF level. | `U4554C_S4_EN.pdf`, printed/PDF pp. 18–20 |
| Actuator checks | DALI-ballast fault checking defaults enabled when a DALI dimmer is used; actuator priority defaults primary. This does not give BMNE500 a direct DALI output. | `U4554C_S4_EN.pdf`, printed/PDF pp. 19–20 |
| Scheduling | Named lighting profiles feed weekly programs and annual date intervals; profiles/programs must be unlinked before deletion. | `U4554C_S4_EN.pdf`, printed/PDF pp. 21–31 |
| Scenario execution | When and Stop events use OR; Only-if conditions permit AND/OR; Execute is mandatory and ordered. Repeat and resume-at-restart are optional. | `U4554C_S4_EN.pdf`, printed/PDF pp. 37–55 |
| Scenario families | ON/OFF, motor, scenario, CEN/CEN PLUS controls, time, auxiliary/contact, lock/unlock, lighting zones and counter/Boolean variables are software editor families, not additional Device Modules. | `U4554C_S4_EN.pdf`, printed/PDF pp. 42–52 |

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact technical item is currently retained.

## Programming

Keep gateway/network identity fields separate from runtime lighting objects. Preserve all three fixed Modules and do not collapse BMNE500 to a generic Ethernet gateway.

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Network / clock | Fixed or dynamic address, mask/router/DNS; time zone/summer time, master/slave clock and geographic coordinates for astronomic clock. | `U4554C_S4_EN.pdf`, printed/PDF pp. 9–10 |
| Three function codes | Gateway, Lighting Manager and Scenario Scheduler codes must each be unique across the configured system. | `U4554C_S4_EN.pdf`, printed/PDF p. 10 |
| Authentication / remote control | Web user/admin credentials and OPEN password; optional password-free IP intervals; LAN/Internet inhibition through one of nine auxiliary channels; input OPEN-command block list. | `U4554C_S4_EN.pdf`, printed/PDF pp. 11–14 |
| Web session | Timeout choices `1/2/5/15 min`. | `U4554C_S4_EN.pdf`, printed/PDF p. 14 |
| Software address scope | Device inventory A `0..10`, PL `0..15`, with joint `0/0` rejected; use local-bus/interface context where required. | `U4554C_S4_EN.pdf`, printed/PDF pp. 14–16 |
| Scenario field restrictions | Timed light, irrigation, motor assemblies, delays, lock/unlock and zones are Execute-only. CEN events are When/Stop-only; Hour/Day is excluded from Execute; simple Hour also from Only-if; contacts excluded from Execute; Scenario PLUS excluded from Only-if. | `U4554C_S4_EN.pdf`, printed/PDF pp. 43–52 |
| Project / firmware transfer | Download sends project to Device; Upload receives it. Single-device transfer allows Ethernet or serial; multiple-device transfer uses Ethernet. Transfer requires configured OPEN password and MAC address. | `U4554C_S4_EN.pdf`, printed/PDF pp. 55–62 |
| Version migration | For firmware `1.x` to `2.x`, receive and save current configuration before updating, then send it back after the update. | `U4554C_S4_EN.pdf`, printed/PDF p. 60 |

## Source reconciliation

The canonical database and current publisher material agree that BMNE500 is a software-configured Lighting Management gateway/control unit. The database adds the exact three-slot internal model: Lighting manager, Scenario scheduler and Gateway Open SCS.

The new retained Italian export replaces the previously unarchived physical-rating evidence. The manual explicitly requires three unique function addresses, matching the three-slot model. Its DHCP default differs from the catalogue static-IP default, and catalogue `FW_VER` default `3.0.0` differs from firmware definition version `2.0` build `1`; these are source/model defaults, not observed installed settings. The manual discusses historical `1.x`/`2.x` migration without establishing every supported release/build. The catalogue associates Ethernet and USB, while this manual describes Ethernet and serial project transfer. These are source-specific software connection descriptions; no examined original establishes a physical USB connector or reconciles the serial/USB difference.

## Evidence limits and open work

- No sanitized hardware/network fingerprint establishes installed firmware or actual defaults.
- The one associated parameter payload is listed but not available in this extraction.
- Product-export links to instruction, technical sheet and software downloads were located; instruction/standalone technical-sheet payloads and software binaries were not inspected. Exact serial connector/pinout and operating-temperature ratings are not established by the examined originals.
- Validate three function codes, clock/address defaults and migration against a real device before relying on them as observed behavior.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [U4554C_S4_EN](https://archive.openwebnet-ha.org/sha256/e5/d2/e5d235a413023e1e004380ffc74c3e69c5589a474249b09f4a7892374c83a62c.pdf)
- [BMNE500 catalogue record](https://catalogue.bticino.com/pdf/scheda-prodotto/BTI-BMNE500)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0031-0040-2026-10-06.md#own-dev-0033)
