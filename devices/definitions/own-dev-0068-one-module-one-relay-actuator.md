# 1-module 1-relay actuator

## Summary

This compact SCS actuator switches one load through a single relay in a wiring-device module. It fits modular, junction or shutter boxes and includes a local micro-pushbutton; same-address slave operation and delayed slave switch-off are documented in the historical guide.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0068` | Project identity |
| Technical description | 1-module 1-relay actuator | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `L/N/NT4675` | Canonical commercial records |
| Catalogue item | `66` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `100` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Lighting, Actuator, Flush-mounted | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - LivingLight | `L/N/NT4675` | Established identity | canonical commercial record for item `66` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `AUTOMATISME.pdf` | technical/system guide | Historical guide; no dated imprint established | Printed pp. 116, 159, 161 / PDF pp. 118, 161, 163; exact family configuration, load classes, supply/current and installation | [Archived original](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Form / mounting | One Living International/Light module; 503E/504E, junction/shutter boxes or trunking | AUTOMATISME.pdf, printed pp. 116, 159, 161 / PDF pp. 118, 161, 163 |
| Supply / consumption | `27 Vdc`; `13 mA` | AUTOMATISME.pdf, printed pp. 116, 159, 161 / PDF pp. 118, 161, 163 |
| Connection / local interface | `0.75 mm²` load leads; micro-pushbutton and indicator | AUTOMATISME.pdf, printed pp. 116, 159, 161 / PDF pp. 118, 161, 163 |
| Load classes at 50/60 Hz | Incandescent: `2 A` / `500 W`; resistive: `2 A` / `500 W`; ferromagnetic: `2 A` cosφ 0.5 / `500 W` as printed | AUTOMATISME.pdf, printed pp. 116, 159, 161 / PDF pp. 118, 161, 163 |
| Unrated load columns | Fluorescent, electronic transformer and motor columns show dashes; `LED`/CFL limits are not established | AUTOMATISME.pdf, printed pp. 116, 159, 161 / PDF pp. 118, 161, 163 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `66` | Canonical catalogue |
| Technical item | 1-module 1-relay actuator | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `100` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `100` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `66` | `L/N/NT4675` | `1` | `4` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `195` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `195` | `1` | `6` Light actuator | Fixed/designated metadata | `699` | `6` | `484` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `195` | Physical configuration | `0` | Canonical firmware/mode association |
| `195` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `195` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `195` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `195` | `A` | `0..9` | `0` | A; Environment |
| `195` | `PL` | `0..9` | `0` | `PL`; Light Point |
| `195` | `M` | `0..4`; `15` = `PUL` | `0` | M; Mode (0-4, Pul) |
| `195` | `G1` | `0..9` | `0` | `G1`; `G1` - (0-9) |
| `195` | `G2` | `0..9` | `0` | `G2`; `G2` - (0-9) |
| `195` | `G3` | `0..9` | `0` | `G3`; `G3` - (0-9) |

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

### Device-specific interpretation

Firmware `195` declares one Light actuator Object `6`, with no Virgin, empty condition `4145` and no conversion. Firmware A/`PL`/`G1`..`G3=0..9` and `M=0..4`/PUL15 are distinct from broader reusable Object addresses, ten groups and slave-PUL. The historical guide documents `SLA`, but this firmware M enum omits it; the guide does not independently specify complete physical A/`PL`/G domains. `STATE_RESET` and `LOAD_CONTROL_MODE` are software fields; no exact retained source establishes zero-crossing hardware for this reference. Load limits are those of the exact guide row, not later Basic-module 3475 specifications.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `195` | `1` | `6` | `4145` | No textual predicate stored | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `195` | `6` | `690` | `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open (entire reusable range retained) | `0` | Per energy management (State on Reset) |
| `195` | `6` | `1869` | `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing (entire reusable range retained) | `0` | Load_control_mode |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `66` / `modobj = 100` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`6`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Single-relay operation | Basic command modes except those requiring two interlocked relays | AUTOMATISME.pdf, printed pp. 116, 159, 161 / PDF pp. 118, 161, 163 |
| `SLA` / PUL | Follow same-address master / ignore room and general commands | AUTOMATISME.pdf, printed pp. 116, 159, 161 / PDF pp. 118, 161, 163 |
| Delayed OFF | `M=1..4` delays matching slave OFF `1..4` min, point-to-point only; master switches off immediately | AUTOMATISME.pdf, printed pp. 116, 159, 161 / PDF pp. 118, 161, 163 |
| Local button | Local operation/checking and scenario-definition use in the guide | AUTOMATISME.pdf, printed pp. 116, 159, 161 / PDF pp. 118, 161, 163 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

The guide’s exact `L/N/NT4675` entry establishes a single relay and same-address slave behavior.

| Physical M | Guide behavior |
| --- | --- |
| `SLA` | Slave to a matching-address master |
| PUL | Ignore room/general commands |
| 1 / 2 / 3 / 4 | Delay slave OFF 1 / 2 / 3 / 4 min; point-to-point only |

The guide does not establish complete physical A/`PL`/G value sets; their catalogue domains are shown separately. Do not replace the exact guide load row with later 3475/3476 ratings or treat a reusable zero-crossing enum as documented hardware.

## Source reconciliation

The combined manufacturer catalogue record `L/N/NT4675` is retained as one commercial relationship, while commercial lookup expands `L4675`/`N4675`/`NT4675`. The exact historical guide names that family and documents its own load row. Fluorescent/electronic-transformer/motor dashes are unprovided ratings, not a measured prohibition or modern `LED` limit. Catalogue M omits the guide’s `SLA`; no conversion or release mapping resolves the difference.

Catalogue-specific scope, selectors, defaults and filter/conversion irregularities are detailed under [Object configuration surfaces](#object-configuration-surfaces). Those software relations do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- No exact standalone technical sheet, verified EAN, operating-temperature/protection rating or installed revision is retained for these finishes.
- Other guide occurrences at PDF pp. 4, 43, 65, 67 and 158 are selection/system overviews not independently reconciled; no additional exact-device claims are drawn from them.
- Software help and actual relay/diagnostic behavior remain unexamined.
- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0061-0070-2026-10-06.md#own-dev-0068)
