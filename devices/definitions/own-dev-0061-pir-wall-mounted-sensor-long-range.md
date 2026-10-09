# `PIR` wall-mounted sensor - long range

## Summary

This wall or ceiling SCS sensor combines long-range passive infrared movement detection with a daylight threshold. It can switch lighting, regulate a dimmer or report to a scenario controller; its published coverage and remote-configuration behavior vary between revisions.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0061` | Project identity |
| Technical description | `PIR` wall-mounted sensor - long range | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSE2004`, `048829` | Canonical commercial records |
| Catalogue item | `56` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `39` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `17` | Canonical firmware catalogue |
| Categories | Presence sensing, Daylight sensing, Automation | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSE2004` | Established identity | canonical commercial record for item `56` |
| Legrand | `048829` | Established identity | canonical commercial record for item `56` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `BT00299_c_IT` | technical sheet | BT00299-c-IT; 2013-11-20 | Printed/PDF pp. 1–5; complete exact-product ratings, coverage matrix, remote/physical settings, route restrictions and mounting | [Archived original](https://archive.openwebnet-ha.org/sha256/78/58/7858fdb08933d8e3842b2855333bc7285225b8f1100f3a050052ff4c0650d144.pdf) | [Official source](https://dar.bticino.it/asset/Documents/BT00299_c_IT.pdf) |
| `BTicino-MyHOME-Spanish-technical-sheets.pdf` | Historical Spanish exact-product sheet within compilation | BT00299-a-ES; undated leaf | Printed pp. 658–663 / PDF pp. 89–94; complete `BMSE2004` specifications, coverage, modes and installation | [Archived original](https://archive.openwebnet-ha.org/sha256/89/4f/894f468c301ea2b7aaec22635d91961e1eedc00136a21e21b774e975c378b4eb.pdf) | [Publisher source](https://www.bticino.es/pdf/FICHA_TECNICA_DOMOTICA_MYHOME_BTICINO.pdf) |
| `ch_de_katalog_wohnbau.pdf` | Historical regional catalogue | No dated imprint established | Printed pp. 159, 165 / PDF pp. 161, 167; exact `BMSE2004` dimension and current rows, including contradictory height | [Archived original](https://archive.openwebnet-ha.org/sha256/9f/e5/9fe511c3ac12d861dff7d8d28ddec3b3612a27e99a804afbed89877c73a6b4ed.pdf) | Publisher URL not retained in manifest |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / current / environment | `27 Vdc`; `12 mA`; `−5..45 °C`; IP42; indoor use | BT00299-c-IT, printed/PDF pp. 1–5 |
| Connection / interface | RJ45 `BMAC1001` adapter; bidirectional IR; LEARN button/`LED`; wall/ceiling bracket | BT00299-c-IT, printed/PDF pp. 1–5 |
| Italian dimensions / headline | `116 × 91 × 70 mm`; `11 × 14 m` / `120 m²`; 45°/90° | BT00299-c-IT, printed/PDF pp. 1–5 |
| Italian drawing | Page 2 labels `90 m²`; vertical 12° / horizontal 70°; `27 m` reach, A approximately `10 m` at `2.4 m` | BT00299-c-IT, printed/PDF pp. 1–5 |
| Italian adjustment headline | `5..1275` lux; `30 s`..255 h 59 min `59 s` | BT00299-c-IT, printed/PDF pp. 1–5 |
| Spanish headline / dimensions | `10 × 27 m` / `210 m²`; 60°/140°; maximum mounting height `6 m`; `115.86 × 91 × 69.6 mm` | BT00299-a-ES, printed pp. 658–663 / PDF pp. 89–94 |
| Spanish adjustment headline | `1..2000` lux; `30 s`..255 h | BT00299-a-ES, printed pp. 658–663 / PDF pp. 89–94 |
| Regional dimension discrepancy | Dimension table: `H=91`, `B=115.86`, `T=69.6 mm`; consumption-table row instead gives `H=94 mm`; both list the exact `BMSE2004` reference | German catalogue, printed pp. 159, 165 / PDF pp. 161, 167 |

### Italian `PIR` coverage

Each cell retains drawing A / W in metres and the stated area; these source labels and areas are not recomputed. BT00299-c-IT, printed/PDF p. 2

| Height (m) | Low (25%) | Medium (50%) | High (75%) | Maximum (100%) |
| --- | --- | --- | --- | --- |
| `2.5` | `3 × 6 m / 54 m²` | `5 × 15 m / 109 m²` | `8 × 21 m / 156 m²` | `10 × 27 m / 210 m²` |
| `3` | `3 × 6 m / 54 m²` | `5 × 15 m / 109 m²` | `8 × 21 m / 156 m²` | `10 × 27 m / 210 m²` |
| `4` | `3 × 6 m / 54 m²` | `5 × 15 m / 109 m²` | `8 × 21 m / 156 m²` | `10 × 27 m / 210 m²` |
| `5` | `3 × 6 m / 54 m²` | `5 × 15 m / 109 m²` | `8 × 21 m / 156 m²` | `10 × 27 m / 210 m²` |
| `6` | `3 × 6 m / 54 m²` | `5 × 15 m / 109 m²` | `8 × 21 m / 156 m²` | `10 × 27 m / 210 m²` |

### Historical Spanish `PIR` coverage

Each cell retains width × reach in metres and stated area; this is a different revision-specific matrix. BT00299-a-ES, printed p. 659 / PDF p. 90

| Height (m) | Low (25%) | Medium (50%) | High (75%) | Maximum (100%) |
| --- | --- | --- | --- | --- |
| `2.5` | `8.5 × 25.5 m / 95 m²` | `9 × 26 m / 103 m²` | `9.5 × 27 m / 115 m²` | `9.5 × 27 m / 115 m²` |
| `3` | `9.5 × 26 m / 107 m²` | `9.5 × 26.5 m / 111 m²` | `9.5 × 27 m / 116 m²` | `10 × 27 m / 117 m²` |
| `4` | `9.5 × 26.5 m / 110 m²` | `9.5 × 27 m / 116 m²` | `10 × 28 m / 123 m²` | `10 × 28.5 m / 128 m²` |
| `5` | `9.5 × 26.5 m / 110 m²` | `9.5 × 27 m / 116 m²` | `10 × 28 m / 123 m²` | `10 × 28.5 m / 128 m²` |
| `6` | `9.5 × 26.5 m / 110 m²` | `9.5 × 27 m / 116 m²` | `10 × 28 m / 123 m²` | `10 × 28.5 m / 128 m²` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `56` | Canonical catalogue |
| Technical item | `PIR` wall-mounted sensor - long range | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `39` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `39` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `56` | `BMSE2004` | `1` | `5` | `BTicino_Undefined_Wall mounted detector` |
| `1797` | `048829` | `2` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `135` | `-1` | `-1` | `-1` | `17` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `135` | `1` | `119` Stand alone presence sensor | Candidate alternative | `348` | `119` | `302` |
| `135` | `1` | `128` Scenarios daylight and presence sensor | Fixed/designated metadata | `349` | `128` | `303` |
| `135` | `1` | `164` Scenarios daylight sensor | Candidate alternative | `350` | `164` | `304` |
| `135` | `1` | `165` Scenarios presence sensor | Candidate alternative | `351` | `165` | `305` |
| `135` | `1` | `166` Stand alone daylight sensor | Candidate alternative | `352` | `166` | `306` |
| `135` | `1` | `168` Stand alone daylight and presence sensor | Candidate alternative | `353` | `168` | `307` |
| `135` | `2` | `431` IR scenario control | Fixed/designated metadata | `354` | `431` | `308` |
| `135` | `3` | `431` IR scenario control | Fixed/designated metadata | `355` | `431` | `308` |
| `135` | `4` | `431` IR scenario control | Fixed/designated metadata | `356` | `431` | `308` |
| `135` | `5` | `431` IR scenario control | Fixed/designated metadata | `357` | `431` | `308` |
| `135` | `6` | `431` IR scenario control | Fixed/designated metadata | `358` | `431` | `308` |
| `135` | `7` | `431` IR scenario control | Fixed/designated metadata | `359` | `431` | `308` |
| `135` | `8` | `431` IR scenario control | Fixed/designated metadata | `360` | `431` | `308` |
| `135` | `9` | `431` IR scenario control | Fixed/designated metadata | `361` | `431` | `308` |
| `135` | `10` | `431` IR scenario control | Fixed/designated metadata | `362` | `431` | `308` |
| `135` | `11` | `431` IR scenario control | Fixed/designated metadata | `363` | `431` | `308` |
| `135` | `12` | `431` IR scenario control | Fixed/designated metadata | `364` | `431` | `308` |
| `135` | `13` | `431` IR scenario control | Fixed/designated metadata | `365` | `431` | `308` |
| `135` | `14` | `431` IR scenario control | Fixed/designated metadata | `366` | `431` | `308` |
| `135` | `15` | `431` IR scenario control | Fixed/designated metadata | `367` | `431` | `308` |
| `135` | `16` | `431` IR scenario control | Fixed/designated metadata | `368` | `431` | `308` |
| `135` | `17` | `431` IR scenario control | Fixed/designated metadata | `369` | `431` | `308` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `135` | `515` Daylight and motion sensor virgin | `1` | `119`, `128`, `164`, `165`, `166`, `168` | `515` | `8` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `135` | Physical configuration | `0` | Canonical firmware/mode association |
| `135` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `135` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `135` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `135` | `A` | `0..9` | `0` | A; Environment |
| `135` | `PL` | `0..9` | `0` | `PL`; Light Point |
| `135` | `M` | `0..4` | `0` | M; Mode 0-4 |
| `135` | `S` | `0..4` | `0` | S; Configurator S (0-4) |
| `135` | `T` | `0..9` | `0` | T; Configurator T (time) - (0-9) |
| `135` | `D` | `0..5` | `0` | D; (0-5) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `119` - Stand alone presence sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | `0` = Point to point; `2` = Group | `0` | Addressing type |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `0..255` | `0` | Group number |
| `A_R` | `0..10` | `0` | Referent area address |
| `PL_R` | `0..15` | `0` | Referent light point address |
| `MAIN_GROUP` | `0` = Disable; `1` = Enable | `0` | Enable secondary groups |
| `G1` | `0..255` | `0` | Secondary group 1 |
| `G2` | `0..255` | `0` | Secondary group 2 |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `10` | Minutes |
| `SECONDS` | `0..59` | `0` | Seconds |
| `FUNC_MODE` | `1` = Auto `ON`/`OFF`; `2` = Auto Walkthrough; `3` = Manual `ON` / Auto `OFF`; `5` = Partial `ON` / Group `OFF` | `2` | Operating mode; Functional_mode |
| `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `3` | `PIR` sensitivity |
| `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `2` | `US` sensitivity |
| `INITIAL_OCCUPANCY` | `1` = `PIR` only; `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `3` | Initial occupancy |
| `MAINTAIN_OCCUPANCY` | `1` = `PIR` only; `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Maintain detection |
| `RETRIGGER` | `0` = Disabled; `1` = `PIR` only; `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Retrigger |
| `ALERT` | `0` = Disabled; `1` = Visual; `2` = Acoustic; `3` = Visual and Acoustic | `0` | Alert |
| `ENABLE_LOAD_CONTROL` | `0` = Disabled; `1` = Enabled | `1` | Enable load control |

### Object `128` - Scenarios daylight and presence sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `HOURS` | `0..255` | `0` | Time delay - Hours |
| `MINUTES` | `0..59` | `15` | Time delay - Minutes |
| `SECONDS` | `0..59` | `0` | Time delay - Seconds |
| `SCHEMA` | `1` = `PIR` only; `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Detection scheme |
| `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `3` | `PIR` sensitivity |
| `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `2` | `US` sensitivity |

### Object `164` - Scenarios daylight sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |

### Object `165` - Scenarios presence sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `HOURS` | `0..255` | `0` | Time delay - Hours |
| `MINUTES` | `0..59` | `15` | Time delay - Minutes |
| `SECONDS` | `0..59` | `0` | Time delay - Seconds |
| `SCHEMA` | `1` = `PIR` only; `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Detection scheme |
| `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `3` | `PIR` sensitivity |
| `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `2` | `US` sensitivity |

### Object `166` - Stand alone daylight sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | `0` = Point to point; `2` = Group | `0` | Addressing type |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `0..255` | `0` | Group number |
| `A_R` | `0..10` | `0` | Area of reference actuator |
| `PL_R` | `0..15` | `0` | Light point of reference actuator |
| `TYPE_LOOP` | `0` = Closed loop; `1` = Open loop | `0` | Loop type |
| `GD` | `0..255` | `0` | Daylight cell group |
| `DAYLIGHT_SETPOINT` | `0`; `1..255` = `5 × stored value` lux | `100` | Daylight setpoint (Lux) |
| `PROVISION_OF_LIGHT` | `0` = Automatic; `1..255` = `5 × stored value` lux | `0` | Provision of light (Lux) |
| `FUNC_MODE` | `1` = Auto `ON`/`OFF`; `3` = Manual `ON` / Auto `OFF`; `5` = Partial `ON` / Group `OFF` | `1` | Operating mode; Functional_mode (auto/manual/partial) |
| `LIGHTING_REGULATION` | `0` = Disabled; `1` = Enabled | `0` | Lighting regulation |
| `DAYLIGHT_FACTOR` | `0..255` | `0` | Daylight factor |
| `NATURAL_LIGHT_FACTOR` | `0..255` | `0` | Natural light factor |
| `DAYLIGHT_LEVEL` | `0..255` | `0` | Daylight level |

### Object `168` - Stand alone daylight and presence sensor

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `ADDR_TYPE`, `A`, `PL`, `G`, `A_R`, `PL_R`, `G1`, `G2` | Reusable schema; apply the Device and firmware restrictions below. |
| Operation, timing and presentation | `MAIN_GROUP`, `TYPE_LOOP`, `GD`, `DAYLIGHT_SETPOINT`, `PROVISION_OF_LIGHT`, `HOURS`, `MINUTES`, `SECONDS`, `FUNC_MODE`, `PIR`, `US`, `INITIAL_OCC`, `MAINTAIN_OCC`, `RE-TRIGGER`, `ALERT`, `LOAD_CONTROL`, `LIGHTING_REGULATION`, `NATURAL_LIGHT_FACTOR`, `DAYLIGHT_FACTOR`, `DAYLIGHT_LEVEL` | Reusable schema; apply the Device and firmware restrictions below. |

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | `0` = Point-to-point; `2` = Group | `0` | Addressing type |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `1` | Light point |
| `G` | `0..255` | `0` | Group number |
| `A_R` | `0..10` | `0` | Referent area address |
| `PL_R` | `0..15` | `0` | Referent light point address |
| `MAIN_GROUP` | `0` = Disable; `1` = Enable | `0` | Enable secondary groups |
| `G1` | `0..255` | `0` | Sensor group 1 |
| `G2` | `0..255` | `0` | Sensor group 2 |
| `TYPE_LOOP` | `0` = Closed loop; `1` = Open loop | `0` | Loop type |
| `GD` | `0..255` | `0` | Daylight cell group |
| `DAYLIGHT_SETPOINT` | `0`; `1..255` = `5 × stored value` lux | `100` | Daylight setpoint (Lux) |
| `PROVISION_OF_LIGHT` | `0` = Automatic; `1..255` = `5 × stored value` lux | `0` | Provision of light (Lux) |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `10` | Minutes |
| `SECONDS` | `0..59` | `0` | Seconds |
| `FUNC_MODE` | `1` = Auto `ON`/`OFF`; `2` = Auto walkthrough; `3` = Manual `ON` / Auto `OFF`; `5` = Partial `ON` / Group `OFF` | `2` | Operating mode; Functional_mode |
| `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `3` | `PIR` sensitivity |
| `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `1` | `US` sensitivity |
| `INITIAL_OCC` | `1` = `PIR` only; `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `3` | Initial detection |
| `MAINTAIN_OCC` | `1` = `PIR` only; `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Maintain detection |
| `RE-TRIGGER` | `0` = Disabled; `1` = `PIR` only; `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Re-trigger |
| `ALERT` | `0` = Disabled; `1` = Visual; `2` = Acoustic; `3` = Visual and Acoustic | `0` | Alert |
| `LOAD_CONTROL` | `0` = Disabled; `1` = Enabled | `1` | Enable load control |
| `LIGHTING_REGULATION` | `0` = Disabled; `1` = Enabled | `0` | Lighting regulation |
| `NATURAL_LIGHT_FACTOR` | `1..255` | `10` | Natural light factor |
| `DAYLIGHT_FACTOR` | `0..255` | `0` | Daylight factor |
| `DAYLIGHT_LEVEL` | `0..255` | `0` | Daylight level |

### Object `431` - IR scenario control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_SCE_1` | `1..255` | `1` | Scenario number |
| `TYPE_OF_REGULATION` | `0` = Regulate all; `1` = Lights only; `2` = Shutters only; `3` = Stereo amplifiers only | `1` | Regulation type |
| `ID1` | `0..255` | `0` | `ID1` |
| `ID2` | `0..255` | `0` | `ID2` |
| `ID3` | `0..15` | `0` | `ID3` |
| `UNIT_NUMBER` | `0..15` | `0` | Push button number |

### Device-specific interpretation

Slot `1` admits six sensor Objects (119/128/164/165/166/168); slots `2..17` designate IR scenario Object `431`. Virgin `515` applies only to slot `1` and admits the same six alternatives. These are software placements, not seventeen physical sensors. Reusable timers default to 10 minutes in 119/168 and 15 minutes in 128/165; these do not override a product factory setting. `DAYLIGHT_SETPOINT` and `PROVISION_OF_LIGHT` encode `1..255` as five times the stored value in lux: setpoint default 100 means 500 lux, with zero unlabelled; provision zero means Automatic. Object `431` `TYPE_OF_REGULATION` is restricted to 3 (stereo), excluding default 1 without a replacement; this does not prove sixteen installed IR functions or speaker hardware. Firmware `135` stores M predicates selecting 128 for `M=2`, 166 for `M=1/4` and 168 for `M=0/3`; alternatives 119/164/165 lack a stored M selection. Firmware A/`PL=0..9` default 0 and `S=0..4` differ from physical A/`PL=1..9` and `S=0..3`. No conversion is associated. Occupancy restrictions retain `US`-only and combined `PIR`/`US` choices on this `PIR`-only product; they are software evidence, not ultrasonic construction. `ALERT` subsets exclude default 0; `DAYLIGHT_SETPOINT` and `PROVISION_OF_LIGHT` on 168 have subset flags with no allowed values. These remain unresolved restrictions, not unrestricted fields.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `135` | `1` | `128` | `4477` | `M=2` | None |
| `135` | `1` | `166` | `4461` | `M=1` | None |
| `135` | `1` | `166` | `4505` | `M=4` | None |
| `135` | `1` | `168` | `4439` | `M=0` | None |
| `135` | `1` | `168` | `4491` | `M=3` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `135` | `119` | `148` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | `US` sensitivity |
| `135` | `119` | `149` | `INITIAL_OCCUPANCY` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `3` | Initial occupancy |
| `135` | `119` | `150` | `MAINTAIN_OCCUPANCY` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Mantain occupancy |
| `135` | `119` | `151` | `RETRIGGER` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Re-trigger |
| `135` | `119` | `2342` | `ALERT` | `1` = Visual; `3` = Visual and Acoustic | `0` | Alert; reusable default `0` is outside this subset; filter supplies no replacement default |
| `135` | `128` | `152` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | `US` sensitivity |
| `135` | `128` | `153` | `SCHEMA` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Detection Schema |
| `135` | `165` | `154` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | `US` sensitivity |
| `135` | `165` | `155` | `SCHEMA` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Detection Schema |
| `135` | `166` | `2104` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `135` | `166` | `2119` | `NATURAL_LIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Natural light factor |
| `135` | `166` | `2134` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `135` | `168` | `156` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `1` | `US` sensitivity |
| `135` | `168` | `157` | `INITIAL_OCC` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `3` | Initial occupancy |
| `135` | `168` | `158` | `MAINTAIN_OCC` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Mantain occupancy |
| `135` | `168` | `159` | `RE-TRIGGER` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Re-trigger |
| `135` | `168` | `2150` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `135` | `168` | `2343` | `ALERT` | `1` = Visual; `3` = Visual and Acoustic | `0` | Alert; reusable default `0` is outside this subset; filter supplies no replacement default |
| `135` | `168` | `2365` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `135` | `168` | `2448` | `DAYLIGHT_SETPOINT` | Subset flag present but no allowed values stored; unresolved restriction | `100` | Daylight setpoint (Lux) |
| `135` | `168` | `2460` | `PROVISION_OF_LIGHT` | Subset flag present but no allowed values stored; unresolved restriction | `0` | Provision of light (Lux) |
| `135` | `431` | `2398` | `TYPE_OF_REGULATION` | `3` = Stereo amplifiers only | `1` | Regulation type; reusable default `1` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `56` / `modobj = 39` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`119`, `128`, `164`, `165`, `166`, `168`, `431`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| `M=0` presence | Switch on with presence below threshold; off after T; manual OFF inhibits restart until the absence interval | BT00299-c-IT, printed/PDF pp. 1–5 |
| `M=1` twilight | Daylight-only switching, no `PIR`; S/T absent; GEN/AMB/GR not supported | BT00299-c-IT, printed/PDF pp. 1–5 |
| `M=2` controller | MH200N scenario sensing with unique address; controller determines timing; S/T absent | BT00299-c-IT, printed/PDF pp. 1–5 |
| `M=3` regulated presence | Presence and constant daylight dimming; manual adjustment becomes setpoint until absence; manual OFF inhibits automation until manual ON | BT00299-c-IT, printed/PDF pp. 1–5 |
| `M=4` daylight regulation | No `PIR`; manual ON and automatic OFF; does not automatically restart | BT00299-c-IT, printed/PDF pp. 1–5 |
| Walkthrough | Presence shorter than 20 s reduces delay to 3 min; an already shorter delay wins | BT00299-c-IT, printed/PDF pp. 1–5 |
| Eco / retrigger | Manual ON, automatic OFF; 30 s retrigger after OFF | BT00299-c-IT, printed/PDF pp. 1–5 |
| Alarm / regulation | Warning intervals: 1 min, 30 s and 10 s before OFF; regulation OFF after 10 min above threshold plus stated margin | BT00299-c-IT, printed/PDF pp. 1–5 |
| Calibration | Separate artificial/natural-light phases using lux meter; calibration input `0..99995` lux | BT00299-c-IT, printed/PDF pp. 1–5 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Lighting Management supports Plug&Go through the Room Controller, Push&Learn and Virtual Configurator. MyHOME physical configurators or 3503N/web-server virtual configuration disable configuration remotes and remote-only advanced parameters in the Italian sheet; the Spanish leaf permits IR, physical and PC parameter setup. These routes cannot be assumed simultaneously available.

| Physical selector | Italian values / consequence |
| --- | --- |
| A / `PL` | `1..9` / `1..9`; absent zero is not a valid physical address |
| M | 0 presence; 1 twilight; 2 MH200N; 3 regulated presence; 4 twilight regulation |
| S | 0 or absent low; 1 medium; 2 high; 3 maximum |
| T | 0 or absent 15 min; 1=30 s; 2=1 min; 3=2 min; 4=5 min; 5=10 min; 6=15 min; 7=20 min; 8=30 min; 9=40 min |
| D | 0 or absent wall 300 / ceiling 500 lux; 1=20; 2=100; 3=300; 4=500; 5=1000 lux |

### Italian remote settings

BT00299-c-IT p. 3 governs this table; factory values are not installed readings.

| Parameter | Printed factory setting | Adjustment / scope |
| --- | --- | --- |
| Delay | 15 min | `BMSO4003`: 3/5/10/15/20 min; `BMSO4001`: 5 s..59 min 59 s |
| `PIR` sensitivity | Maximum | `BMSO4001`/`BMSO4003`: low 25%, medium 50%, high 75%, maximum 100% |
| Daylight threshold | 300 lux | 4003: 20/100/300/500/1000 lux; 4001: `5..1275` lux |
| Auto / Eco / walkthrough | Disabled / disabled / enabled | BMSO4001/BMSO4003: enable or disable, subject to the documented control route |
| Initial / maintain scheme | `PIR` / `PIR` | Not editable using 4001 |
| Retrigger scheme | `PIR` | `BMSO4001`: `PIR` and/or `US`, `PIR`, `US`, disabled as printed; this is a source irregularity on a `PIR`-only product |
| Alarm / regulation | Disabled / enabled | BMSO4001: enable or disable |
| Light provision | Automatic | BMSO4001: Automatic..1275 lux |
| Calibration | No factory value specified | BMSO4001: `0..99995` lux; two-phase procedure |

The Italian p. 3 says an audible beep confirms receipt of a configuration-remote IR command. The Italian p. 3 says an audible beep confirms receipt of a configuration-remote IR command. For reset, briefly press LEARN until the slow indication, then hold about 10 s for fast flashing (Italian p. 3). The Spanish BT00299-a-ES instead names `BMSO4001`/`BMSO4002`, with Auto enabled, 15 min delay, `PIR` sensitivity 100%, 300 lux ±15% and walkthrough enabled; its sensitivity/timeout table contains incomplete unit labels. Its virtual role list includes IR scenario operation. Remote interchangeability and firmware cutoffs have not been established.

## Source reconciliation

The exact Italian c revision and historical Spanish a leaf agree on 27 V/12 mA/IP42 but disagree on coverage, optical angles, threshold range, remote models and whether physical/virtual setup disables remote adjustment. Italian factory Auto disabled differs from Spanish Auto enabled. Italian p. 1 headline 120 m², p. 2 drawing 90 m² and sensitivity table maximum 210 m² are retained separately, alongside the different Spanish matrix. Italian remote delay 5 s..59 min 59 s conflicts with the p. 1 30 s..255 h 59 min 59 s headline. Its Auto paragraph says OFF when light is insufficient, contrary to the described threshold/regulation logic; this unresolved wording is not silently corrected. German dimension entries disagree internally on height (91/94 mm). No release or hardware mapping resolves these source differences.

Catalogue-specific scope, selectors, defaults and filter/conversion irregularities are detailed under [Object configuration surfaces](#object-configuration-surfaces). Those software relations do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- Installed detection coverage, remote compatibility and route restrictions remain unobserved; no revision-to-firmware mapping resolves the published discrepancies.
- The Legrand identity is explicit catalogue evidence; independent exact-`048829` physical and EAN records are not retained.
- Remote manuals, Virtual Configurator/glossary, 3503N/web-server and controller setup guides linked by the sheets are not independently examined.
- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0061-0070-2026-10-06.md#own-dev-0061)
