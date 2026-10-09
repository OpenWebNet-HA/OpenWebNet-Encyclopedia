# Flush-mounted dimmer

## Summary

The 4674 is a flush-mounted SCS controller for a slave-dimmer arrangement. Its local buttons switch and regulate lighting through up to three compatible slave dimmers, which provide the associated load-handling stage.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0027` | Project identity |
| Technical description | Flush-mounted SCS dimmer actuator | Catalogue + official documentation |
| Commercial identities | `H4674`, `L/N/NT4674` | Catalogue |
| Catalogue item | `23` - “Flush mounted dimmer” | Canonical manufacturer catalogue |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Canonical manufacturer catalogue |
| Item model / `modobj` | `5` | Canonical manufacturer catalogue |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `198` | Canonical manufacturer catalogue |
| Declared Modules | `1` | Canonical manufacturer catalogue |
| Categories | Dimmer, Lighting | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - LivingLight | `L/N/NT4674` | Established identity | Canonical catalogue; canonical commercial record `23`; Commercial identity of this Technical Device |
| BTicino - Axolute | `H4674` | Established identity | Canonical catalogue; canonical commercial record `1731`; Commercial identity of this Technical Device |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `AUTOMATISME.pdf` | MyHOME automation guide | October 2006 publisher guide | 4674 family identity/catalogue: printed p. 41 / PDF p. 43; wiring printed p.61 /PDF p.63; configuration p.114 /PDF p.116; load/current tables pp.159–160 /PDF pp.161–162 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 wiring-device modules | Publisher `AUTOMATISME.pdf` |
| SCS supply | `27 Vdc` | Publisher `AUTOMATISME.pdf` |
| Maximum current draw | `8 mA` | Publisher `AUTOMATISME.pdf` |
| Local interface | upper/lower pushbuttons with indicator LED | Publisher `AUTOMATISME.pdf` |
| Supported slave dimmers | up to 3 `L/N/NT4416` units | Publisher `AUTOMATISME.pdf` |
| Associated published load range | `60..500 W` through the slave-dimmer arrangement | Publisher `AUTOMATISME.pdf` |
| Physical configurator positions | `A`, `PL`, `M`, `G` | Publisher `AUTOMATISME.pdf` |

The 4674 is the BUS actuator/controller for the slave-dimmer arrangement; the published load is handled through the associated slave dimmer rather than as a stand-alone internal power stage.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `23` | Canonical catalogue |
| Technical item description | Flush mounted dimmer | Canonical catalogue |
| Item family | `4` - Dimmer | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `5` | `AS_ITEM_SYSTEM` |
| Commercial records | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `5` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Canonical commercial record metadata

| Reference / record | Catalogue name / source description | Visibility / type | Dependent / gateway | Evidence |
| --- | --- | --- | --- | --- |
| `L/N/NT4674` / `23` | Flush mounted dimmer; `BTicino_L/N/NT_Flush mounted dimmer` | `1` / Empty | `0` / `0` | Canonical manufacturer catalogue |
| `H4674` / `1731` | Flush mounted dimmer; no source description | `1` / Empty | `0` / `0` | Canonical manufacturer catalogue |

Visibility, dependency and gateway flags describe the catalogue record, not the installed Device state.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `198` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Firmware `198` is wildcard `-1.-1.-1` and declares one Module. Installed hardware remains to be corroborated.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `198` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `668` | `8` | `463` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

The single Module resolves to Object `8`, **Dimmer actuator**. Object `8` is also associated with Virgin Object `532` elsewhere in the catalogue; this firmware itself has no Device-specific Virgin Object row.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `198` | Physical configuration | `0` | Canonical firmware/mode association |
| `198` | Virtual Configuration | `1` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `198` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `198` | `A` | `0..9` | `0` | A; Environment |
| `198` | `PL` | `0..9` | `0` | PL; Light Point |
| `198` | `M` | `0`; `9` = `O/I` | `0` | M; mode (0, I/O) |
| `198` | `G1` | `0..9` | `0` | `G1`; `G1` - (0-9) |

Firmware `198` exposes the physical addressing/mode fields. Advanced dimmer settings are reusable Object parameters and must not be confused with physical configurators.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `8` - Dimmer actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality; mode (M, S + PULL) |
| `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled | `0` | State saving on reset |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `MIN_LEVEL` | `1..100` | `1` | Minimum level |
| `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge | `0` | Type of load; Default value depends on device. |
| `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard | `0` | Voltage standard |
| `MIN_LEVEL_ADV` | `1..100` | `0` | Minimum level advanced; Default value depends on device and Type of load value |
| `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable | `0` | Enable / Disable minimum level |
| `G1` | `0..255` | `0` | Group 1 |
| `G2` | `0..255` | `0` | Group 2 |
| `G3` | `0..255` | `0` | Group 3 |
| `G4` | `0..255` | `0` | Group 4 |
| `G5` | `0..255` | `0` | Group 5 |
| `G6` | `0..255` | `0` | Group 6 |
| `G7` | `0..255` | `0` | Group 7 |
| `G8` | `0..255` | `0` | Group 8 |
| `G9` | `0..255` | `0` | Group 9 |
| `G10` | `0..255` | `0` | Group 10 |

### Device-specific interpretation

Condition `4145` has no textual predicate and no conversion reference; it cannot be resolved into an invented selector. Filter 596 admits DALI/DSI and LED load labels but excludes reusable default 0; those software labels do not prove compatible physical load stages on the 4674/4416 arrangement.

The reusable `MIN_LEVEL_ADV` domain is `1..100` but its stored default is `0`. No corrected default is supplied; retain this source inconsistency without treating `0` as a permitted configured value.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `198` | `1` | `8` | `4145` | No textual predicate stored | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `198` | `8` | `594` | `MIN_LEVEL_ADV` | `1..100` (entire reusable range retained) | `0` | Minimum level advanced |
| `198` | `8` | `595` | `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable (entire reusable range retained) | `0` | enable disable minimum level |
| `198` | `8` | `596` | `TYPE_LOAD` | `1` = Auto detect inductive; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `2` = Forced capacitive; `3` = Forced inductive; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI | `0` | Type of Load; reusable default `0` is outside this subset; filter supplies no replacement default |
| `198` | `8` | `2180` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 5` and the 4674 dimmer-actuator family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | record installed firmware rather than assuming wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm the single dimmer Object | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the configured dimmer address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `A`, `PL`, `M`, `G1` and reusable dimmer parameters without confusing them with the slave power stage | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The Device participates in [`WHO 1` - Lighting](../../functional/who-1-lighting/).

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact item is currently retained.

## Programming

Treat the product as one addressed dimmer Module. Do not infer modern universal-dimmer load-selection semantics merely because they exist on the shared Object `8` surface.

| Setting / property | Source-scoped value or behavior | Evidence |
| --- | --- | --- |
| Physical M | Absent: short cyclic ON/OFF, long regulation; O/I: upper ON/increase, lower OFF/decrease. Wait at least 3 s between ON and OFF. | AUTOMATISME.pdf printed p.114 /PDF p.116 |
| Slave arrangement | Up to 3 compatible 4416 slave dimmers; guide wiring labels 400 W max each with 10 m / 50 m spacing annotations. Do not reinterpret these as the 4674’s internal relay rating. | AUTOMATISME.pdf printed p.61 /PDF p.63 |

## Source reconciliation

The catalogue establishes one Dimmer actuator Module and the two commercial identities. The archived automation documentation corroborates the 4674 family role. Shared Object `8` contains fields used by newer dimmers as well, so this dossier deliberately distinguishes Object capability from firmware-applicable configuration.

The consumption table establishes 8 mA at 27 Vdc (printed p.160 /PDF p.162), correcting the prior 5 mA. The load table (printed p.159 /PDF p.161) describes H/L4674 with L/N/NT4416 at 230 Vac 50 Hz, `0.25..2 A` and `60..500` W/VA for incandescent/resistive/ferromagnetic loads. The separate multi-slave diagram labels 400 W per slave; its relation to the 500 W table is not explained and remains source-specific. No dedicated 4674 sheet was recovered in targeted manufacturer searches. The guide’s named H/L and compatible slave forms do not independently certify every regional electrical variant.

## Evidence limits and open work

- Dedicated H/L4674 technical-sheet revisions and the 400 W wiring versus 500 W table difference remain documentary gaps.
- Empty condition `4145` and filter 596’s out-of-subset default are retained; no Device-specific activation predicate or replacement default is established.
- Actual load stage, installed firmware and behavior remain unobserved; DALI/DSI catalogue labels are not physical capability evidence.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0021-0030-2026-10-06.md#own-dev-0027)
