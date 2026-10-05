# 1 relay DIN actuator 16 A 100/240 V

## Summary

This DIN-mounted SCS actuator switches one lighting load through a relay. It occupies four DIN modules in the retained publisher documentation; its catalogue load class is complemented by source-specific limits rather than a universal rating for every load type.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0081` | Project identity |
| Technical description | 1 relay DIN actuator 16 A 100/240 V | Canonical catalogue |
| Commercial identities | `BMSW1001`, `002600` | Canonical commercial records |
| Catalogue item | `128` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `160` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Automation, Actuator | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSW1001` | Established catalogue identity | canonical commercial record for item `128` |
| Legrand | `002600` | Established catalogue identity | canonical commercial record for item `128` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| BTicino/Legrand residential catalogue | product catalogue | historical publisher catalogue | Current/size/dissipation reference table: printed p. 165 / PDF p. 167 | [Archived original](https://archive.openwebnet-ha.org/sha256/9f/e5/9fe511c3ac12d861dff7d8d28ddec3b3612a27e99a804afbed89877c73a6b4ed.pdf) | [Official source](https://assets.legrand.com/webf/ch/ch_de_katalog_wohnbau.pdf) |
| `LE10699AA-FR` | technical/system guide | publisher guide | Product-specific output-state programming: printed p. 102 / PDF p. 102 | [Archived original](https://archive.openwebnet-ha.org/sha256/48/54/4854112b1d66d371515e11e1759d3a88d68cd2dad465a25c8799d55a74298d30.pdf) | [Official source](https://assets.legrand.com/general/mediagrp/np-ft-gt/le10699aa-fr.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Product description | `1 relay DIN actuator 16 A 100/240 V` | Catalogue item description; not a complete product specification |
| Additional electrical/mechanical characteristics | Properties not established beyond the source-scoped facts on this page | Direct product-source reconciliation remains open |
| SCS current | `5 mA` | Retained residential catalogue, printed p. 165 / PDF p. 167 |
| DIN width | 4 modules | Same source |
| Power dissipation | `1.2 W` | Same source |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `128` | Canonical catalogue |
| Technical item | 1 relay DIN actuator 16 A 100/240 V | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `160` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `167` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `167` | `1` | `6` Light actuator | Fixed/designated metadata | `593` | `6` | `412` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `167` | Advanced Configuration | supported configuration route for this Device family |
| `167` | Physical configuration | supported configuration route for this Device family |
| `167` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `167` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `167` | `A` | `0..9` | `0` | A; Environment |
| `167` | `PL` | `0..9` | `0` | PL; Light Point |
| `167` | `M` | `0..4` | `0` | M; Mode 0-4 |
| `167` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |
| `167` | `G2` | `0..9` | `0` | G2; G2 - (0-9) |
| `167` | `G3` | `0..9` | `0` | G3; G3 - (0-9) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `6` - Light actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality |
| `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open | `0` | Relay state on device reset |
| `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing | `0` | Load control mode |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `SUBTYPE` | `11` = Actuator; `1` = Lamp; `10` = Valve; `15` = Differential restart; `6` = Fan; `7` = Watering; `8` = Controlled socket; `9` = Lock | `11` | Type of load |
| `G1` | `0..255` | `0` | Group 1; Group = 0 means no group |
| `G2` | `0..255` | `0` | Group 2; Group = 0 means no group |
| `G3` | `0..255` | `0` | Group 3; Group = 0 means no group |
| `G4` | `0..255` | `0` | Group 4; Group = 0 means no group |
| `G5` | `0..255` | `0` | Group 5; Group = 0 means no group |
| `G6` | `0..255` | `0` | Group 6; Group = 0 means no group |
| `G7` | `0..255` | `0` | Group 7; Group = 0 means no group |
| `G8` | `0..255` | `0` | Group 8; Group = 0 means no group |
| `G9` | `0..255` | `0` | Group 9; Group = 0 means no group |
| `G10` | `0..255` | `0` | Group 10; Group = 0 means no group |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `167` | `1` | `6` | `4147` | No textual predicate stored | `1` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `167` | `6` | `365` | `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open (entire reusable range retained) | `0` | Per energy management (State on Reset) |
| `167` | `6` | `1858` | `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing (entire reusable range retained) | `0` | Load_control_mode |
| `167` | `6` | `2468` | `LOCAL_BUTTON` | `1` = `ON`/`OFF`; `15` = Pushbutton; `18` = Timed `ON`; `9` = `ON` - `OFF` | `0` | Local button modality; reusable default `0` is outside this subset; filter supplies no replacement default |
| `167` | `6` | `2469` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `167` | `6` | `2470` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `167` | `6` | `2471` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `1` | `M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `1` |
| `1` | `M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `1` |
| `1` | `M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `1` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `128` / `modobj = 160` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`6`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `6` Light actuator | Automation | Firmware/Object capability association; resolve the slot and configuration first |

Catalogue system identifiers are not `WHO` numbers. The source establishes the roles shown, not a complete command vocabulary or proof of every installed function. Correlate the selected role with [Functional Protocol](../../functional/) before sending functional commands. Product behavior is additionally bounded by the publisher evidence below; uncorroborated transport and firmware details remain open work.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

The catalogue registers Virtual Configuration, Advanced Configuration, Physical configuration for this technical item. Use the firmware-specific fields, selected Module/Object and effective restrictions on this page as the configuration boundary. This item has one declared Module; do not treat candidate Object rows as additional channels.

The retained sources establish only the Device-specific procedures described below; reset, transfer or update details not covered by those sources remain open work. The catalogue mode registration alone does not establish a universal physical-button or gateway-session workflow.

The retained hotel guide, printed p. 102, / PDF p. 102, gives product-specific per-output naming and enable/disable controls; the two-output product has a corresponding panel for each channel. This is project-tool behavior, not a new OpenWebNet command grammar.

## Source reconciliation

The retained residential catalogue supplies the SCS current, DIN width and dissipation rows now incorporated above. The retained hotel guide also explicitly names this commercial pair in its output-state programming example. These publisher facts supplement the complete catalogue configuration model; dedicated load-family limits and hardware behavior still require further evidence.

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
