# `PIR` wall-mounted sensor - short range

## Summary

This wall or ceiling SCS sensor combines narrow-beam passive infrared movement detection with a daylight threshold. It can switch lighting, regulate a dimmer or report to a scenario controller; its published coverage figures vary between revisions.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0057` | Project identity |
| Technical description | `PIR` wall-mounted sensor - short range | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSE2002`, `048825` | Canonical commercial records |
| Catalogue item | `52` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `37` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `17` | Canonical firmware catalogue |
| Categories | Presence sensing, Daylight sensing, Automation | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSE2002` | Established identity | canonical commercial record for item `52` |
| Legrand | `048825` | Established identity | canonical commercial record for item `52` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MM00297_c_EN` | technical sheet | 2013-02-01 | Printed/PDF pp. 1–7; complete exact-product specifications, route restrictions, remote matrix, physical selectors/modes, coverage and assembly | [Archived original](https://archive.openwebnet-ha.org/sha256/bd/3a/bd3a2ab2b78360677424609bbd4fbeca5ca2e9f4c6692eec614a1f84f1559d66.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MM00297_c_EN.pdf) |
| `BTicino-MyHOME-Spanish-technical-sheets.pdf` | Spanish technical-sheet compilation | BT00297-a-ES; no separate dated imprint established | Exact `BMSE2002` leaf, printed pp. 646–651 / PDF pp. 77–82; all its specifications, modes, coverage and installation examined; other leaves outside stated scope | [Archived original](https://archive.openwebnet-ha.org/sha256/89/4f/894f468c301ea2b7aaec22635d91961e1eedc00136a21e21b774e975c378b4eb.pdf) | [Publisher source](https://www.bticino.es/pdf/FICHA_TECNICA_DOMOTICA_MYHOME_BTICINO.pdf) |
| `ch_de_katalog_wohnbau.pdf` | Historical residential catalogue | No dated imprint established | Printed pp. 156–159 / PDF pp. 158–161; exact sensor entries, coverage and dimensions; no `BMSE2003` dimension row | [Archived original](https://archive.openwebnet-ha.org/sha256/9f/e5/9fe511c3ac12d861dff7d8d28ddec3b3612a27e99a804afbed89877c73a6b4ed.pdf) | Publisher URL not retained in manifest |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / current | `27 Vdc` from SCS; `12 mA` | MM00297_c_EN, printed/PDF pp. 1–7 |
| Environment / installation | `−5..45 °C`; IP42; indoor wall or ceiling using supplied bracket | MM00297_c_EN, printed/PDF pp. 1–7 |
| Connections / controls | RJ45 bus; `BMAC1001` RJ45/SCS adapter; light sensor, `PIR` sensor, two-way IR receiver, parameter-enable pushbutton, `LED` and six physical configurator positions | MM00297_c_EN, printed/PDF pp. 1–7 |
| Maximum height | 6 m | MM00297_c_EN, printed/PDF pp. 1–7 |
| Dimensions | `115.86 × 91 × 69.6 mm` | MM00297_c_EN, printed/PDF pp. 1–7 |
| Headline coverage / angle | 11 × 14 m / 120 m² at 2.5 m; MM00297-c-EN says 45° / 90°, Spanish leaf says 60° / 90° | MM00297_c_EN, printed/PDF pp. 1–7 |
| Threshold / delay ranges | Technical headline: `5..1275` lux; 30 s..255 h 59 min 59 s. Remote table: `0..1275` lux; Spanish historical leaf: `1..2000` lux and 30 s..255 h | MM00297_c_EN, printed/PDF pp. 1–7 |

### `PIR` coverage in the MM c revision

Each cell is width × depth / publisher-stated area; identical rows are printed for the five heights. MM00297-c-EN, printed/PDF p. 6.

| Height (m) | Low (25%) | Medium (50%) | High (75%) | Maximum (100%) |
| --- | --- | --- | --- | --- |
| `2.5` | `3 × 3 m / 31 m²` | `6 × 8 m / 62 m²` | `9 × 11 m / 89 m²` | `11 × 14 m / 120 m²` |
| `3` | `3 × 3 m / 31 m²` | `6 × 8 m / 62 m²` | `9 × 11 m / 89 m²` | `11 × 14 m / 120 m²` |
| `4` | `3 × 3 m / 31 m²` | `6 × 8 m / 62 m²` | `9 × 11 m / 89 m²` | `11 × 14 m / 120 m²` |
| `5` | `3 × 3 m / 31 m²` | `6 × 8 m / 62 m²` | `9 × 11 m / 89 m²` | `11 × 14 m / 120 m²` |
| `6` | `3 × 3 m / 31 m²` | `6 × 8 m / 62 m²` | `9 × 11 m / 89 m²` | `11 × 14 m / 120 m²` |

### `PIR` coverage in the historical Spanish revision

Each cell is width × depth / stated area; these are distinct from the MM c matrix. BT00297-a-ES, printed p. 647 / PDF p. 78.

| Height (m) | Low (25%) | Medium (50%) | High (75%) | Maximum (100%) |
| --- | --- | --- | --- | --- |
| `2.5` | `10 × 13.5 m / 65 m²` | `10 × 14 m / 68 m²` | `10.5 × 14 m / 68 m²` | `11 × 14 m / 70 m²` |
| `3` | `10 × 13.5 m / 66 m²` | `10.5 × 14 m / 68 m²` | `10.5 × 14 m / 70 m²` | `11 × 14 m / 70 m²` |
| `4` | `10 × 14 m / 68 m²` | `10.5 × 14 m / 70 m²` | `11 × 14 m / 76 m²` | `11 × 14.5 m / 76 m²` |
| `5` | `10 × 14 m / 68 m²` | `10.5 × 14 m / 70 m²` | `11 × 14 m / 76 m²` | `11 × 14.5 m / 76 m²` |
| `6` | `10 × 14 m / 68 m²` | `10.5 × 14 m / 70 m²` | `11 × 14 m / 76 m²` | `11 × 14.5 m / 76 m²` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `52` | Canonical catalogue |
| Technical item | `PIR` wall-mounted sensor - short range | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `37` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `37` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `52` | `BMSE2002` | `1` | `5` | `BTicino_Undefined_Wall mounted detector` |
| `1558` | `048825` | `2` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; `visibility_type` is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `133` | `-1` | `-1` | `-1` | `17` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `133` | `1` | `119` Stand alone presence sensor | Candidate alternative | `304` | `119` | `288` |
| `133` | `1` | `128` Scenarios daylight and presence sensor | Fixed/designated metadata | `305` | `128` | `289` |
| `133` | `1` | `164` Scenarios daylight sensor | Candidate alternative | `306` | `164` | `290` |
| `133` | `1` | `165` Scenarios presence sensor | Candidate alternative | `307` | `165` | `291` |
| `133` | `1` | `166` Stand alone daylight sensor | Candidate alternative | `308` | `166` | `292` |
| `133` | `1` | `168` Stand alone daylight and presence sensor | Candidate alternative | `309` | `168` | `293` |
| `133` | `2` | `431` IR scenario control | Fixed/designated metadata | `310` | `431` | `294` |
| `133` | `3` | `431` IR scenario control | Fixed/designated metadata | `311` | `431` | `294` |
| `133` | `4` | `431` IR scenario control | Fixed/designated metadata | `312` | `431` | `294` |
| `133` | `5` | `431` IR scenario control | Fixed/designated metadata | `313` | `431` | `294` |
| `133` | `6` | `431` IR scenario control | Fixed/designated metadata | `314` | `431` | `294` |
| `133` | `7` | `431` IR scenario control | Fixed/designated metadata | `315` | `431` | `294` |
| `133` | `8` | `431` IR scenario control | Fixed/designated metadata | `316` | `431` | `294` |
| `133` | `9` | `431` IR scenario control | Fixed/designated metadata | `317` | `431` | `294` |
| `133` | `10` | `431` IR scenario control | Fixed/designated metadata | `318` | `431` | `294` |
| `133` | `11` | `431` IR scenario control | Fixed/designated metadata | `319` | `431` | `294` |
| `133` | `12` | `431` IR scenario control | Fixed/designated metadata | `320` | `431` | `294` |
| `133` | `13` | `431` IR scenario control | Fixed/designated metadata | `321` | `431` | `294` |
| `133` | `14` | `431` IR scenario control | Fixed/designated metadata | `322` | `431` | `294` |
| `133` | `15` | `431` IR scenario control | Fixed/designated metadata | `323` | `431` | `294` |
| `133` | `16` | `431` IR scenario control | Fixed/designated metadata | `324` | `431` | `294` |
| `133` | `17` | `431` IR scenario control | Fixed/designated metadata | `325` | `431` | `294` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `133` | `515` Daylight and motion sensor virgin | `1` | `119`, `128`, `164`, `165`, `166`, `168` | `515` | `6` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `133` | Physical configuration | `0` | Canonical firmware/mode association |
| `133` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `133` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `133` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `133` | `A` | `0..9` | `0` | A; Environment |
| `133` | `PL` | `0..9` | `0` | `PL`; Light Point |
| `133` | `M` | `0..4` | `0` | M; Mode 0-4 |
| `133` | `S` | `0..4` | `0` | S; Configurator S (0-4) |
| `133` | `T` | `0..9` | `0` | T; Configurator T (time) - (0-9) |

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

The catalogue declares 17 Modules: slot `1` offers six sensor Objects, while slots `2..17` designate IR scenario control 431. Virgin `515` applies only to slot `1` and admits the same six Objects; this is one sensing product, not seventeen physical sensors. `M=0/3` selects 168, `M=1/4` selects 166, `M=2` selects 128 where those predicates are stored. Candidate 119/164/165 membership is not proof of automatic activation. No conversion rule supplies a physical-to-Object mapping. Reusable timers default to 10 minutes in 119/168 and 15 in 128/165; these do not override the published 15-minute product setting. `DAYLIGHT_SETPOINT` and `PROVISION_OF_LIGHT` encode `1..255` as five times the stored value in lux; `DAYLIGHT_SETPOINT` default 100 therefore encodes 500 lux, not 100 lux. Zero setpoint has no stored label; provision zero is Automatic. `TYPE_OF_REGULATION` on 431 is restricted to 3 (stereo amplifiers), excluding reusable default 1 without a replacement. This does not establish a speaker or sixteen installed IR functions. Firmware `A/PL` `0..9` and `S=0..4` exceed the sheets' physical `A/PL` `1..9` and `S=0..3`. M/T/D agree as numeric domains, but reusable address domains extend to `A=10` and `PL=15`. Filters retain `US`-only and combined `PIR`/`US` schemes; they do not establish ultrasonic hardware on a `PIR`-only SKU. The referenced occupancy fields belong to their stated Object scopes; their similar names do not make distinct fields interchangeable. `ALERT` filters exclude default 0 without replacements. The empty allowed-value subset on `PROVISION_OF_LIGHT` remains unresolved, not unrestricted.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `133` | `1` | `128` | `4477` | `M=2` | None |
| `133` | `1` | `166` | `4461` | `M=1` | None |
| `133` | `1` | `166` | `4505` | `M=4` | None |
| `133` | `1` | `168` | `4439` | `M=0` | None |
| `133` | `1` | `168` | `4491` | `M=3` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `133` | `119` | `122` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | `US` sensitivity |
| `133` | `119` | `123` | `INITIAL_OCCUPANCY` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `3` | Initial occupancy |
| `133` | `119` | `124` | `MAINTAIN_OCCUPANCY` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Mantain occupancy |
| `133` | `119` | `125` | `RETRIGGER` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Re-trigger |
| `133` | `119` | `2337` | `ALERT` | `1` = Visual; `3` = Visual and Acoustic | `0` | Alert; reusable default `0` is outside this subset; filter supplies no replacement default |
| `133` | `128` | `126` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | `US` sensitivity |
| `133` | `128` | `127` | `SCHEMA` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Detection Schema |
| `133` | `165` | `128` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | `US` sensitivity |
| `133` | `165` | `129` | `SCHEMA` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Detection Schema |
| `133` | `166` | `2102` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `133` | `166` | `2117` | `NATURAL_LIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Natural light factor |
| `133` | `166` | `2132` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `133` | `168` | `130` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `1` | `US` sensitivity |
| `133` | `168` | `131` | `INITIAL_OCC` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `3` | Initial occupancy |
| `133` | `168` | `132` | `MAINTAIN_OCC` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Mantain occupancy |
| `133` | `168` | `133` | `RE-TRIGGER` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Re-trigger |
| `133` | `168` | `2148` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `133` | `168` | `2338` | `NATURAL_LIGHT_FACTOR` | `1..255` (entire reusable range retained) | `10` | Natural light factor |
| `133` | `168` | `2339` | `ALERT` | `1` = Visual; `3` = Visual and Acoustic | `0` | Alert; reusable default `0` is outside this subset; filter supplies no replacement default |
| `133` | `168` | `2363` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `133` | `168` | `2458` | `PROVISION_OF_LIGHT` | Subset flag present but no allowed values stored; unresolved restriction | `0` | Provision of light (Lux) |
| `133` | `431` | `2396` | `TYPE_OF_REGULATION` | `3` = Stereo amplifiers only | `1` | Regulation type; reusable default `1` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `52` / `modobj = 37` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`119`, `128`, `164`, `165`, `166`, `168`, `431`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Daylight priority | Presence does not request lighting when natural light meets the threshold; threshold tolerance prevents repeated switching | MM00297_c_EN, printed/PDF pp. 1–7 |
| Auto / Eco | Auto switches on/off automatically; Eco requires a bus control for manual ON and permits automatic restart within 30 s of an absence-triggered OFF | MM00297_c_EN, printed/PDF pp. 1–7 |
| Override | Manual ON/OFF remains effective while presence continues, returning to automatic behavior after absence timeout | MM00297_c_EN, printed/PDF pp. 1–7 |
| Walkthrough | Occupancy shorter than 20 s reduces a longer timeout to 3 min; shorter selected delay takes precedence | MM00297_c_EN, printed/PDF pp. 1–7 |
| Software roles | Local/central presence, daylight or combined detector; PLUS IR scenario control in the product sheet; direct reachability still depends on catalogue relations | MM00297_c_EN, printed/PDF pp. 1–7 |
| Historical audible warning | Spanish leaf reports alerts at 1 min, 30 s and 10 s before timeout; not an observed implementation | MM00297_c_EN, printed/PDF pp. 1–7 |
| Remote-only advanced functions | Partial ON/group OFF requires a learned light group; retrigger window 30 s; daylight regulation OFF after 10 min above threshold and ON after 20 s below threshold | MM00297_c_EN, printed/PDF pp. 1–7 |
| Factory reset | Brief LEARN press starts slow flashing; hold LEARN 10 s until fast flashing | MM00297_c_EN, printed/PDF pp. 1–7 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

These are product-sheet physical values, separate from the reusable Object encodings (MM00297_c_EN, printed/PDF pp. 1–7).

| Physical position | Published values | Consequence |
| --- | --- | --- |
| A / `PL` | `1..9` / `1..9` | Zero is excluded |
| M | `0..4` | Modes below |
| S | 0 absent: Low; 1 Medium; 2 High; 3 Very high | Source physical sensitivity; firmware additionally permits 4 |
| T | 0 absent: 15 min; 1: 30 s; 2: 1 min; 3: 2 min; 4: 5 min; 5: 10 min; 6: 15 min; 7: 20 min; 8: 30 min; 9: 40 min | Physical delay |
| D | 0 absent: wall 300 lux / ceiling 500 lux; 1: 20; 2: 100; 3: 300; 4: 500; 5: 1000 lux | Physical light threshold |

| M | Published behavior |
| --- | --- |
| 0 | Presence plus daylight, automatic ON/OFF; manual OFF override lasts until absence timeout |
| 1 | Twilight ON/OFF only; presence disabled; leave S/T empty; no GEN/ROOM/GR |
| 2 | Report presence/light to MH200N; unique A/`PL`; no direct load control; leave S/T empty; no GEN/ROOM/GR |
| 3 | Presence plus constant-light regulation; requires dimmer; manual dimming sets temporary setpoint until next ON |
| 4 | Daylight regulation with manual ON and automatic OFF; presence disabled; requires dimmer; no automatic restart after daylight falls |

Use `M=2` for MH200N scenarios; a scenario controller, not the sensor, manages its timing in this route. Virtual configuration is described through 3503N or a web server with Virtual Configurator. Lighting Management separately lists Plug&Go, Push&Learn and Project&Download; these commissioning workflows are not numeric catalogue mode IDs.

The Italian note on MM00297_c_EN p. 3 says physical or virtual MyHOME configuration disables configuration remotes and makes remote-only advanced functions unavailable. Do not combine those routes with the following remote matrix as if all were simultaneously enabled.

| Remote parameter | Printed default | Allowed adjustment / tool |
| --- | --- | --- |
| Delay | 15 min | `BMSO4003`: 3, 5, 10, 15, 20 min; `BMSO4001`: 30 s..255 h 59 min 59 s |
| `PIR` sensitivity | Very high | Low / Medium / High / Maximum with either tool |
| Light threshold | 300 lux | `BMSO4003`: 20, 100, 300, 500, 1000 lux; `BMSO4001`: `0..1275` lux |
| Auto / Eco / Partial ON–Group OFF | Disabled / Disabled / Disabled | Auto/Eco selectable by either; partial mode `BMSO4001` only |
| Walkthrough | Enabled | Enable/disable with either tool |
| Initial / maintaining detection | `PIR` / `PIR` | Not editable in the printed matrix |
| Retrigger | `PIR` | `PIR` or Disabled, `BMSO4001` only |
| Alarm | Disabled | Enable/disable, `BMSO4001` only |
| Calibration | No default shown | `0..99995` lux input; measure with luxmeter and send using `BMSO4001` |
| Light regulation | Disabled | Enable/disable, `BMSO4001` only |
| Provision of light | Auto | Auto or up to 1275 lux, `BMSO4001` only |

## Source reconciliation

The exact Spanish BT00297-a-ES leaf establishes `BMSE2002` specifications and procedures; Legrand SKU equivalence remains catalogue evidence rather than independent physical verification. The retained MM c revision uses `5..1275` lux (`0..1275` in its remote table), versus Spanish `1..2000`; Spanish factory Auto differs from MM Auto disabled. Spanish permits physical/remote/PC adjustments, whereas MM warns that physical/virtual setup disables remotes. No revision-to-firmware mapping resolves these differences. The MM p. 6 drawing labels 60 m² although its table/headline say 120 m²; Spanish maximum table gives 70 m² at 2.5 m despite the same 120 m² headline. MM 45°/90° differs from Spanish 60°/90°. The two coverage matrices remain revision-specific.

Catalogue-specific scope and filter irregularities are detailed under [Object configuration surfaces](#object-configuration-surfaces); those relations do not establish additional physical sensors, load interfaces or installed behavior.

## Evidence limits and open work

- Coverage, threshold and configuration-route conflicts remain unresolved by a change log or hardware revision.
- Exact Legrand-reference physical specifications and independent EAN records are not retained; its identity is established by the catalogue.
- Virtual Configurator/glossary, 3503N/web-server procedures, remote manuals and Plug&Go/Project&Download guides referenced by the sheets are not independently examined here.
- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, software payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0051-0060-2026-10-06.md#own-dev-0057)
