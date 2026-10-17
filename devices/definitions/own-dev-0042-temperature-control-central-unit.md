# Temperature control central unit

## Summary

The 99-zone temperature-control central unit supervises SCS heating and cooling zones from one local keypad and display. It provides weekly schedules, room-specific temperatures, scenarios and holiday modes, with programming through the supplied TiThermo software for the documented 3550 variant.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0042` | Project identity |
| Technical description | Temperature-control central unit and supervisory programmer | Canonical catalogue plus reconciled Device sources |
| Commercial identities | `3550`, `067456`, `573918`, `573919` | Canonical commercial records |
| Catalogue item | `291` | Canonical catalogue |
| Main catalogue system | Temperature control | Canonical catalogue |
| Item model / `modobj` | `2` | Canonical catalogue |
| Firmware definition | `24 / 3.0.0`; `25 / 2.0.15`; `26 / 1.1.6` | Canonical catalogue |
| Declared Modules | `1` | Firmware catalogue |
| Categories | Temperature control, HVAC, Central unit, Programming | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `3550` | established catalogue identity for item `291` | canonical commercial record |
| Legrand - Céliane | `067456` | established catalogue identity for item `291` | canonical commercial record |
| Legrand - Arteor | `573918` | established catalogue identity for item `291` | canonical commercial record |
| Legrand - Arteor | `573919` | established catalogue identity for item `291` | canonical commercial record |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BR-MyHOME-HPML0714 | product catalogue | 2014 | 573918 / 573919 temperature-control context: printed pp. 16, 24, 32 / PDF pp. 16, 24, 32 | [Archived original](https://archive.openwebnet-ha.org/sha256/13/8e/138e7a234fe24fb044d3bfc82954e08b2887be22f3f8ceb24aecaeff6ed2f2e5.pdf) | [Official source](https://assets.legrand.com/pim/DOCUMENT/BR%20MyHOME%20HPML0714.pdf) |
| `U0256E_U_EN.pdf` | 99-zone central-unit user manual | U0256E; retained publisher copy | Printed/PDF pp. 4–39; operating modes, settings, diagnostics and schedule/scenario editing; front matter and final publisher page inspected | [Archived original](https://archive.openwebnet-ha.org/sha256/5f/46/5f465092198f5ae29498045da516789f18425acec339580c833722582ff89a12.pdf) | [Publisher source](https://dar.bticino.com/asset/Documents/U0256E_U_EN.pdf) |
| `3550-italian-product-sheet-IT.pdf` | Exact-product manufacturer export | Retrieved 2026-10-06; no printed technical revision | Printed/PDF p. 1; exact 3550 capacity, supply/current, dimensions, mounting and TiThermo packaging | [Archived original](https://archive.openwebnet-ha.org/sha256/9b/ee/9bee7de338f9fffd39fb72ba9b1800efd9da53d2036ef81d0612c9bfd51a8ecd.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-3550) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| 3550 supply / current | `27 Vdc`; nominal `0.075 A` (`75 mA`) | 3550 Italian export printed/PDF p. 1 |
| 3550 dimensions / mounting | `140 × 210 × 35 mm` (W × H × D); wall or MULTIBOX mounting | Same source p. 1 |
| Interface | Graphic display and navigation keypad; local zone and system menu | U0256E user manual pp. 4–7 |
| Variant boundary | Exact 3550 ratings do not independently establish every Legrand finish/installation package | Canonical SKU/item relationships establish their identities |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `291` | Canonical catalogue |
| Technical item description | Temperature control central unit | Canonical catalogue |
| Main system | Temperature control | Canonical catalogue |
| Item model / `modobj` | `2` | Canonical catalogue |
| Commercial records | `4` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Temperature control | `2` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `291` | `3550` | `1` | `5` | `BTicino_Undefined_Temperature central unit` |
| `1784` | `573918` | `2` | `5` | Empty in source |
| `1785` | `573919` | `2` | `5` | Empty in source |
| `1837` | `067456` | `2` | `13` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `24` | `3` | `0` | `0` | `1` | Catalogue default | Official |
| `25` | `2` | `0` | `15` | `1` | Not catalogue default | Official |
| `26` | `1` | `1` | `6` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `24` | `62` | BTicino (key `1`) | `0` | external software | `TiThermo_0200` |
| `24` | `523` | Legrand (key `2`) | `0` | external software | `UNAVAILABLE_0000` |
| `25` | `107` | BTicino (key `1`) | `0` | external software | `TiThermo_0100` |
| `25` | `121` | Legrand (key `2`) | `0` | external software | `ThermoConfig_0200` |
| `26` | `120` | Legrand (key `2`) | `0` | external software | `ThermoConfig_0101` |
| `26` | `522` | BTicino (key `1`) | `0` | external software | `UNAVAILABLE_0000` |

All 6 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `24` | `1` | `35` Temperature control 99 zones control unit | Fixed/designated metadata | `912` | `35` | `571` |
| `25` | `1` | `35` Temperature control 99 zones control unit | Fixed/designated metadata | `913` | `35` | `572` |
| `26` | `1` | `35` Temperature control 99 zones control unit | Fixed/designated metadata | `914` | `35` | `573` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `24` | Product Programming | `3` | Canonical firmware/mode association |
| `25` | Product Programming | `3` | Canonical firmware/mode association |
| `26` | Product Programming | `3` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `24` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `24` | `WARM` | `0` = Disable; `1` = Enable | `0` | WARM; Winter mode |
| `24` | `COLD` | `0` = Disable; `1` = Enable | `0` | COLD; Summer mode |
| `25` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `25` | `WARM` | `0` = Disable; `1` = Enable | `0` | WARM; Winter mode |
| `25` | `COLD` | `0` = Disable; `1` = Enable | `0` | COLD; Summer mode |
| `26` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `26` | `WARM` | `0` = Disable; `1` = Enable | `0` | WARM; Winter mode |
| `26` | `COLD` | `0` = Disable; `1` = Enable | `0` | COLD; Summer mode |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `35` - Temperature control 99 zones control unit

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `COLD` | `0` = Disable; `1` = Enable | `0` | Summer modality; Summer mode |
| `WARM` | `0` = Disable; `1` = Enable | `0` | Winter modality; Winter mode |

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
| `DIMENSION 1` | resolve item `291` / `modobj = 2` identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware tuple while preserving wildcard sentinels | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate item-specific Module/Object topology `35` | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after active Object/system context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration against firmware/Object filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Weekly schedules | Three customizable weekly programs per season, daily 24-hour zone profiles | U0256E pp. 8, 28–35 |
| Scenarios / holidays | Sixteen winter and sixteen summer scenarios; holiday profile until specified date/time then selected weekly program; holidays return to a chosen program | Same source pp. 10–12, 28, 36–39 |
| Manual / local overrides | Global or zone-specific manual temperatures, OFF, antifreeze and heat protection | Same source pp. 9, 13–16 |
| Settings / diagnostics | Date/time, season, remote control enable, user code, contrast, slave/configuration errors and program/zone display | Same source pp. 17–24 |
| Profile temperature defaults | `T1=18` °C, `T2=20` °C, `T3=22` °C; antifreeze 7 °C and heat protection 35 °C | Same source p. 20; central-unit profile defaults, not every probe’s defaults |
| Conditional integration | Temperature sensors, auxiliary window contacts and Climaveneta Idrorelax menu depend on installed system | Same source pp. 25–27 |

## Observed behavior and corroboration

No sanitized hardware fingerprint or Device-specific protocol capture is currently retained for this exact technical item.

## Programming

Set date/time and season before evaluating schedules; seasonal switching leaves the system in antifreeze/heat protection. The user manual’s programming menu edits names, copies weekly programs, assigns daily profiles by zone/day and creates/copies scenarios and holiday profiles. Scroll and edit cursors have different behavior; the profile example is illustrative, not an observed installation (U0256E pp. 21, 28–39).

The 3550 export says TiThermo is included. Six canonical parameter-file associations are fully recorded under Firmware and hardware, but their payloads, TiThermo help/software and exact installation manual are unexamined. Do not pretend the two Object `35` seasonal flags encode all UI schedules.

## Source reconciliation

The retained 3550 export confirms 99-zone capacity and the exact product’s physical data. Regional Arteor guide coverage establishes 573918/573919 marketing context; the catalogue’s internal line 5 placeholder is not a marketed line. Identity is established for all four SKUs even where an exact variant electrical sheet is absent. The user manual’s screen illustrations contain duplicated/garbled text layers; operating prose and menu context are used without inventing text from the overlays.

All three firmware records designate Object `35` in slot `1`, with no associated Virgin, slot conditions, relation filters or conversion references. WARM/COLD default 0 are catalogue defaults, not proof that a configured central unit operates in neither season. Object `35` contains only the two seasonal flags: the six linked parameter records, not these flags, are the unexamined payload surface for richer programming. The user manual documents schedules and scenarios independently of that minimal Object schema.

## Evidence limits and open work

- Exact Legrand variant electrical/package sheets, the central-unit installation/calibration manual and TiThermo parameter payloads remain unexamined.
- The discovered installer-manual endpoint returned 403; it does not establish the contents of an installation original.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Archived original](https://archive.openwebnet-ha.org/sha256/13/8e/138e7a234fe24fb044d3bfc82954e08b2887be22f3f8ceb24aecaeff6ed2f2e5.pdf)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0041-0050-2026-10-06.md#own-dev-0042)
