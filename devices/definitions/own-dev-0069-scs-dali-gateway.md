# SCS/DALI gateway

## Summary

This SCS-to-DALI interface controls eight independent dimming outputs, each documented for up to sixteen DALI devices. Local buttons select and test an output, and the instructions explicitly do not guarantee compatibility with DALI2 devices.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0069` | Project identity |
| Technical description | SCS/DALI gateway | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `F429`, `002631` | Canonical commercial records |
| Catalogue item | `71` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `138` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `8` | Canonical firmware catalogue |
| Categories | Lighting, DALI gateway, DIN interface | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F429` | Established identity | canonical commercial record for item `71` |
| Legrand | `002631` | Established identity | canonical commercial record for item `71` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F429` | `8012199850542` | [Archived original](https://archive.openwebnet-ha.org/sha256/55/5d/555db4a56b0514d86eea4526f805f3174407f01e016f1dfc491ca8ee98abf665.pdf), `F429-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `U2068C` | instruction sheet | U2068C; 05/21-01PC | Printed/PDF pp. 1–4; complete exact `F429` multilingual instruction, 6/16-device caption conflict, modes, supply and DALI2 limit | [Archived original](https://archive.openwebnet-ha.org/sha256/88/80/888012e06924ff327b19eb352392050f968a9c43bd25748e9c1e278c44ca0b8a.pdf) | [Official source](https://dar.bticino.com/asset/Documents/U2068C.pdf) |
| `F429-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Printed/PDF p. 1; exact-reference EAN and complete technical attributes examined; linked technical/DWG downloads and prices not incorporated | [Archived original](https://archive.openwebnet-ha.org/sha256/55/5d/555db4a56b0514d86eea4526f805f3174407f01e016f1dfc491ca8ee98abf665.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F429) |
| `BTicino-MyHOME-Spanish-technical-sheets.pdf` | Historical Spanish exact-product sheet within compilation | BT00284-a-ES; undated leaf | Printed pp. 720–722 / PDF pp. 151–153; complete `F429` supply, outputs, addressing, mode and wiring scopes | [Archived original](https://archive.openwebnet-ha.org/sha256/89/4f/894f468c301ea2b7aaec22635d91961e1eedc00136a21e21b774e975c378b4eb.pdf) | [Publisher source](https://www.bticino.es/pdf/FICHA_TECNICA_DOMOTICA_MYHOME_BTICINO.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / bus consumption | `110..240 Vac` `50/60 Hz` or `110..240 Vdc`; maximum `5 mA` from SCS bus | U2068C, printed/PDF pp. 1–3 |
| Environment / size | `+5..45 °C`; six DIN modules | U2068C, printed/PDF pp. 1–3 |
| Outputs / capacity | Eight independent DALI outputs, up to 16 devices per output in headline and non-French wiring captions | U2068C, printed/PDF pp. 1–3 |
| Compatibility limit | DALI2 compatibility is not guaranteed | U2068C, printed/PDF pp. 1–3 |
| Local controls | `P1` virtual setup; `P2` port selection/`LED` count; `P3` short ON/OFF and long dimming | U2068C, printed/PDF pp. 1–3 |
| Historical temperature / power | `−5..45 °C`; dissipated power `4 W` | BT00284-a-ES, printed pp. 720–722 / PDF pp. 151–153 |
| Current export scopes | Description: mains `230 Vac` `50/60 Hz` or `110..240 Vdc`; attribute: `27 Vdc`; `5 mA`, IP20, `−5..45 °C`, six DIN modules | `F429`-ean-product-sheet.pdf, printed/PDF p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `71` | Canonical catalogue |
| Technical item | SCS/DALI gateway | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `138` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `138` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `71` | `F429` | `1` | `5` | `BTicino_Undefined_SCS/DALI gateway` |
| `1606` | `002631` | `2` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `180` | `-1` | `-1` | `-1` | `8` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `180` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `612` | `8` | `425` |
| `180` | `2` | `8` Dimmer actuator | Fixed/designated metadata | `613` | `8` | `425` |
| `180` | `3` | `8` Dimmer actuator | Fixed/designated metadata | `614` | `8` | `425` |
| `180` | `4` | `8` Dimmer actuator | Fixed/designated metadata | `615` | `8` | `425` |
| `180` | `5` | `8` Dimmer actuator | Fixed/designated metadata | `616` | `8` | `425` |
| `180` | `6` | `8` Dimmer actuator | Fixed/designated metadata | `617` | `8` | `425` |
| `180` | `7` | `8` Dimmer actuator | Fixed/designated metadata | `618` | `8` | `425` |
| `180` | `8` | `8` Dimmer actuator | Fixed/designated metadata | `619` | `8` | `425` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `180` | Physical configuration | `0` | Canonical firmware/mode association |
| `180` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `180` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `180` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `180` | `A` | `0..9` | `0` | A; Environment |
| `180` | `G` | `0..9` | `0` | G (0-9) |
| `180` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | Mode (0-4, sla, pul) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `8` - Dimmer actuator

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL`, `G1`, `G2` | Reusable schema; apply the Device and firmware restrictions below. |
| Operation, timing and presentation | `M`, `LOCAL_BUTTON`, `DELAYED_OFF`, `STATE_SAVING_ON_RESET`, `HOURS`, `MINUTES`, `SECONDS`, `MIN_LEVEL`, `TYPE_LOAD`, `TYPE_STANDARD`, `MIN_LEVEL_ADV`, `MIN_AUTO`, `G3`, `G4`, `G5`, `G6`, `G7`, `G8`, `G9`, `G10` | Reusable schema; apply the Device and firmware restrictions below. |

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality; mode (M,S + PULL) |
| `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled | `0` | State saving on reset |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `MIN_LEVEL` | `1..100` | `1` | Minimum level |
| `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = `LED` trailing edge / electronic transformers; `12` = `LED` leading edge; `13` = CFL trailing edge; `14` = CFL leading edge | `0` | Type of load; Default value depends on device. |
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

Firmware `180` declares eight slots of Dimmer actuator 8, with no Virgin. Empty conditions reference rules `7206..7213`: `A=1..9` maps each Module to its corresponding `PL=1..8`; `A=0` maps `PL=0`. This does not authorize physical `A=0`, which the instructions exclude. Firmware `M=0..4`/SLA11/PUL15 is separate from reusable slave-PUL16. `TYPE_LOAD` filter `495` excludes value 8 (Dali standard) while retaining phase-cut and DSI labels: an unresolved catalogue/product mismatch, not evidence that `F429` lacks DALI or supports those unrelated interfaces. `LOCAL_BUTTON` filter `491` excludes default 0; `MIN_LEVEL_ADV=1..100` retains out-of-domain default 0. Timing filters say functionality absent while retaining whole ranges; neither description nor range alone proves active timed operation. No conversion resolves these filter/default conflicts.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `180` | `1` | `8` | `4956` | No textual predicate stored | `7206` |
| `180` | `2` | `8` | `4937` | No textual predicate stored | `7207` |
| `180` | `3` | `8` | `4938` | No textual predicate stored | `7208` |
| `180` | `4` | `8` | `4957` | No textual predicate stored | `7209` |
| `180` | `5` | `8` | `4958` | No textual predicate stored | `7210` |
| `180` | `6` | `8` | `4959` | No textual predicate stored | `7211` |
| `180` | `7` | `8` | `4961` | No textual predicate stored | `7212` |
| `180` | `8` | `8` | `4962` | No textual predicate stored | `7213` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `180` | `8` | `491` | `LOCAL_BUTTON` | `15` = Pushbutton; `18` = Timed `ON`; `9` = `ON` - `OFF` | `0` | Funzionalità di pulsante locale ridotta (Local button mode); reusable default `0` is outside this subset; filter supplies no replacement default |
| `180` | `8` | `492` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Funzionalità di temporizzazione non presente (Hours) |
| `180` | `8` | `493` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Funzionalità di temporizzazione non presente (Minutes) |
| `180` | `8` | `494` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Funzionalità di temporizzazione non presente (Seconds) |
| `180` | `8` | `495` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `10` = Halogen lamp; `11` = `LED` trailing edge / electronic transformers; `12` = `LED` leading edge; `13` = CFL trailing edge; `14` = CFL leading edge; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `9` = DSI | `0` | Funzionalità di specifica carico pilotato ridotta (Type of load) |
| `180` | `8` | `496` | `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard (entire reusable range retained) | `0` | `TYPE_STANDARD` |
| `180` | `8` | `497` | `MIN_LEVEL_ADV` | `1..100` (entire reusable range retained) | `0` | Minimum level advanced |
| `180` | `8` | `498` | `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable (entire reusable range retained) | `0` | enable disable minimum level |
| `180` | `8` | `2175` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `7206` | `A=0` | `PL` = `0` | `7206` |
| `7206` | `A=1` | `PL` = `1` | `7206` |
| `7206` | `A=2` | `PL` = `1` | `7206` |
| `7206` | `A=3` | `PL` = `1` | `7206` |
| `7206` | `A=4` | `PL` = `1` | `7206` |
| `7206` | `A=5` | `PL` = `1` | `7206` |
| `7206` | `A=6` | `PL` = `1` | `7206` |
| `7206` | `A=7` | `PL` = `1` | `7206` |
| `7206` | `A=8` | `PL` = `1` | `7206` |
| `7206` | `A=9` | `PL` = `1` | `7206` |
| `7207` | `A=0` | `PL` = `0` | `7207` |
| `7207` | `A=1` | `PL` = `2` | `7207` |
| `7207` | `A=2` | `PL` = `2` | `7207` |
| `7207` | `A=3` | `PL` = `2` | `7207` |
| `7207` | `A=4` | `PL` = `2` | `7207` |
| `7207` | `A=5` | `PL` = `2` | `7207` |
| `7207` | `A=6` | `PL` = `2` | `7207` |
| `7207` | `A=7` | `PL` = `2` | `7207` |
| `7207` | `A=8` | `PL` = `2` | `7207` |
| `7207` | `A=9` | `PL` = `2` | `7207` |
| `7208` | `A=0` | `PL` = `0` | `7208` |
| `7208` | `A=1` | `PL` = `3` | `7208` |
| `7208` | `A=2` | `PL` = `3` | `7208` |
| `7208` | `A=3` | `PL` = `3` | `7208` |
| `7208` | `A=4` | `PL` = `3` | `7208` |
| `7208` | `A=5` | `PL` = `3` | `7208` |
| `7208` | `A=6` | `PL` = `3` | `7208` |
| `7208` | `A=7` | `PL` = `3` | `7208` |
| `7208` | `A=8` | `PL` = `3` | `7208` |
| `7208` | `A=9` | `PL` = `3` | `7208` |
| `7209` | `A=0` | `PL` = `0` | `7209` |
| `7209` | `A=1` | `PL` = `4` | `7209` |
| `7209` | `A=2` | `PL` = `4` | `7209` |
| `7209` | `A=3` | `PL` = `4` | `7209` |
| `7209` | `A=4` | `PL` = `4` | `7209` |
| `7209` | `A=5` | `PL` = `4` | `7209` |
| `7209` | `A=6` | `PL` = `4` | `7209` |
| `7209` | `A=7` | `PL` = `4` | `7209` |
| `7209` | `A=8` | `PL` = `4` | `7209` |
| `7209` | `A=9` | `PL` = `4` | `7209` |
| `7210` | `A=0` | `PL` = `0` | `7210` |
| `7210` | `A=1` | `PL` = `5` | `7210` |
| `7210` | `A=2` | `PL` = `5` | `7210` |
| `7210` | `A=3` | `PL` = `5` | `7210` |
| `7210` | `A=4` | `PL` = `5` | `7210` |
| `7210` | `A=5` | `PL` = `5` | `7210` |
| `7210` | `A=6` | `PL` = `5` | `7210` |
| `7210` | `A=7` | `PL` = `5` | `7210` |
| `7210` | `A=8` | `PL` = `5` | `7210` |
| `7210` | `A=9` | `PL` = `5` | `7210` |
| `7211` | `A=0` | `PL` = `0` | `7211` |
| `7211` | `A=1` | `PL` = `6` | `7211` |
| `7211` | `A=2` | `PL` = `6` | `7211` |
| `7211` | `A=3` | `PL` = `6` | `7211` |
| `7211` | `A=4` | `PL` = `6` | `7211` |
| `7211` | `A=5` | `PL` = `6` | `7211` |
| `7211` | `A=6` | `PL` = `6` | `7211` |
| `7211` | `A=7` | `PL` = `6` | `7211` |
| `7211` | `A=8` | `PL` = `6` | `7211` |
| `7211` | `A=9` | `PL` = `6` | `7211` |
| `7212` | `A=0` | `PL` = `0` | `7212` |
| `7212` | `A=1` | `PL` = `7` | `7212` |
| `7212` | `A=2` | `PL` = `7` | `7212` |
| `7212` | `A=3` | `PL` = `7` | `7212` |
| `7212` | `A=4` | `PL` = `7` | `7212` |
| `7212` | `A=5` | `PL` = `7` | `7212` |
| `7212` | `A=6` | `PL` = `7` | `7212` |
| `7212` | `A=7` | `PL` = `7` | `7212` |
| `7212` | `A=8` | `PL` = `7` | `7212` |
| `7212` | `A=9` | `PL` = `7` | `7212` |
| `7213` | `A=0` | `PL` = `0` | `7213` |
| `7213` | `A=1` | `PL` = `8` | `7213` |
| `7213` | `A=2` | `PL` = `8` | `7213` |
| `7213` | `A=3` | `PL` = `8` | `7213` |
| `7213` | `A=4` | `PL` = `8` | `7213` |
| `7213` | `A=5` | `PL` = `8` | `7213` |
| `7213` | `A=6` | `PL` = `8` | `7213` |
| `7213` | `A=7` | `PL` = `8` | `7213` |
| `7213` | `A=8` | `PL` = `8` | `7213` |
| `7213` | `A=9` | `PL` = `8` | `7213` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `71` / `modobj = 138` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`8`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| DALI control | Dimming/ON-OFF per output; the group setting is shared by all eight outputs | U2068C, printed/PDF pp. 1–3 |
| Local selection | `P2` cycles channel selection; flashes indicate selected output; `P3` tests the selected output | U2068C, printed/PDF pp. 1–3 |
| M modes | `SLA` follows matching master; PUL ignores room/general; `M=1..4` delays slave OFF `1..4` min for point-to-point control | U2068C, printed/PDF pp. 1–3 |
| Interlocking exclusion | Basic modes exclude functions requiring interlocked relays | U2068C, printed/PDF pp. 1–3 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Use physical `A=1..9`; there is no `PL` socket because outputs are `PL=1..8` within the chosen area. The historical Spanish leaf specifies `G=1..9` and the same group for all outputs. Virtual configuration uses `P1`; Lighting Management dimmer setup is described through Plug&Go and Project&Download in the historical leaf, whose linked full procedures remain unexamined. Do not address all eight outputs as one light point. Catalogue `A=0` converting to `PL=0` is not a valid physical configuration authorized by the instructions. The local `P2`/`P3` test mechanism is separate from software Object defaults. The Spanish leaf also describes PL as selected with `P2`, while its address table assigns outputs `1..8` within each area; that wording does not establish reassignment of the physical output numbering.

## Source reconciliation

The exact instruction, Spanish leaf and current export establish eight DALI outputs and a 16-device-per-output headline. U2068C’s French wiring caption alone says 6 devices maximum per output, inconsistent with its headline and other language captions; this translation discrepancy remains explicit. Its `+5..45 °C` differs from Spanish/export `−5..45` °C. The export’s 27 Vdc attribute is a bus context and does not replace the separately stated mains supply; its 230 Vac headline is narrower than the instruction’s `110..240` Vac. The catalogue `TYPE_LOAD` restriction excludes Dali standard, despite exact-product DALI documentation; manufacturer capability and inconsistent software schema are kept distinct.

Catalogue-specific scope, selectors, defaults and filter/conversion irregularities are detailed under [Object configuration surfaces](#object-configuration-surfaces). Those software relations do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- Temperature and French 6/16-device caption discrepancies have no identified revision-to-hardware resolution.
- The `TYPE_LOAD` filter, local-button default and minimum-level default conflicts remain catalogue evidence gaps; installed behavior is unobserved.
- Exact `002631` independent physical documentation/EAN and linked DWG/commissioning/software sources remain unexamined.
- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `F429-ean-product-sheet.pdf`, printed/PDF p. 1: exact `F429` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/55/5d/555db4a56b0514d86eea4526f805f3174407f01e016f1dfc491ca8ee98abf665.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F429); SHA-256 `555db4a56b0514d86eea4526f805f3174407f01e016f1dfc491ca8ee98abf665`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0061-0070-2026-10-06.md#own-dev-0069)
