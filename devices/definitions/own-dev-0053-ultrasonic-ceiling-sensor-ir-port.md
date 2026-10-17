# Ultrasonic ceiling sensor with IR port

## Summary

This ceiling sensor combines ultrasonic presence detection with a daylight threshold for SCS lighting control. Unlike the `PIR` and dual-technology variants, its retained installation sheet identifies an ultrasonic detector; detailed `BMSE3002`-specific technical documentation remains incomplete.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0053` | Project identity |
| Technical description | Ultrasonic ceiling sensor with IR port | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSE3002`, `048821` | Canonical commercial records |
| Catalogue item | `48` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `33` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `17` | Canonical firmware catalogue |
| Categories | Presence sensing, Daylight sensing, Automation | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSE3002` | Established identity | canonical commercial record for item `48` |
| Legrand | `048821` | Established identity | canonical commercial record for item `48` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `LE02817AD` | instruction sheet | Revision AD; no separate date established | No consistent printed pagination; PDF pp. 1–4; exact `048820`/21/22 sensor-type, installation and adjustment diagrams | [Archived original](https://archive.openwebnet-ha.org/sha256/72/48/7248bde719c44406319ccaff2131c760858d3ec2558c6ff7c087cf1f64b8aaa4.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE02817AD.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / current | `27 Vdc`; `16 mA` | LE02817AD, PDF p. 1 |
| Environment | `−5..45 °C` | LE02817AD, PDF p. 1 |
| Sensing | ultrasonic movement detection and daylight threshold | LE02817AD, PDF p. 1 |
| Opening / housing height | `68 mm` boxed / `65 mm` spring opening; drawing height `50 mm` | LE02817AD, PDF pp. 1–2 |
| Coverage at 2.5 m | 8 m diameter floor coverage; 6 m `US` diameter at the 1.2 m plane shown in the diagram | LE02817AD, PDF pp. 1–2 |
| Published settings | 500 lux / 15 min shown in instructions; light threshold `5..1275` lux; delay 30 s..255 h 59 min 59 s; sensitivity 25%, 50%, 75%, 100% | LE02817AD, PDF pp. 1, 4 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `48` | Canonical catalogue |
| Technical item | Ultrasonic ceiling sensor with IR port | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `33` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `33` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `48` | `BMSE3002` | `1` | `5` | Empty in source |
| `1580` | `048821` | `2` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; `visibility_type` is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `140` | `-1` | `-1` | `-1` | `17` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `140` | `1` | `119` Stand alone presence sensor | Candidate alternative | `457` | `119` | `336` |
| `140` | `1` | `128` Scenarios daylight and presence sensor | Candidate alternative | `589` | `128` | `408` |
| `140` | `1` | `164` Scenarios daylight sensor | Candidate alternative | `458` | `164` | `337` |
| `140` | `1` | `165` Scenarios presence sensor | Candidate alternative | `459` | `165` | `338` |
| `140` | `1` | `166` Stand alone daylight sensor | Candidate alternative | `460` | `166` | `339` |
| `140` | `1` | `168` Stand alone daylight and presence sensor | Fixed/designated metadata | `461` | `168` | `340` |
| `140` | `2` | `431` IR scenario control | Fixed/designated metadata | `462` | `431` | `341` |
| `140` | `3` | `431` IR scenario control | Fixed/designated metadata | `463` | `431` | `341` |
| `140` | `4` | `431` IR scenario control | Fixed/designated metadata | `464` | `431` | `341` |
| `140` | `5` | `431` IR scenario control | Fixed/designated metadata | `465` | `431` | `341` |
| `140` | `6` | `431` IR scenario control | Fixed/designated metadata | `466` | `431` | `341` |
| `140` | `7` | `431` IR scenario control | Fixed/designated metadata | `467` | `431` | `341` |
| `140` | `8` | `431` IR scenario control | Fixed/designated metadata | `468` | `431` | `341` |
| `140` | `9` | `431` IR scenario control | Fixed/designated metadata | `469` | `431` | `341` |
| `140` | `10` | `431` IR scenario control | Fixed/designated metadata | `470` | `431` | `341` |
| `140` | `11` | `431` IR scenario control | Fixed/designated metadata | `471` | `431` | `341` |
| `140` | `12` | `431` IR scenario control | Fixed/designated metadata | `472` | `431` | `341` |
| `140` | `13` | `431` IR scenario control | Fixed/designated metadata | `473` | `431` | `341` |
| `140` | `14` | `431` IR scenario control | Fixed/designated metadata | `474` | `431` | `341` |
| `140` | `15` | `431` IR scenario control | Fixed/designated metadata | `475` | `431` | `341` |
| `140` | `16` | `431` IR scenario control | Fixed/designated metadata | `476` | `431` | `341` |
| `140` | `17` | `431` IR scenario control | Fixed/designated metadata | `477` | `431` | `341` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `140` | `515` Daylight and motion sensor virgin | `1` | `119`, `128`, `164`, `165`, `166`, `168` | `515` | `13` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `140` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `140` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

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

The catalogue declares 17 Modules: slot `1` offers six sensor Objects, while slots `2..17` designate IR scenario control 431. Virgin `515` applies only to slot `1` and admits the same six Objects; this is one sensing product, not seventeen physical sensors. Object `166` retains `M=1/4` predicates; 119/128/165/168 have empty predicates, so no M-based selection is established for those alternatives. Candidate 119/164/165 membership is not proof of automatic activation. No conversion rule supplies a physical-to-Object mapping. Reusable timers default to 10 minutes in 119/168 and 15 in 128/165; these do not override the published 15-minute product setting. `DAYLIGHT_SETPOINT` and `PROVISION_OF_LIGHT` encode `1..255` as five times the stored value in lux; `DAYLIGHT_SETPOINT` default 100 therefore encodes 500 lux, not 100 lux. Zero setpoint has no stored label; provision zero is Automatic. `TYPE_OF_REGULATION` on 431 is restricted to 3 (stereo amplifiers), excluding reusable default 1 without a replacement. This does not establish a speaker or sixteen installed IR functions. The firmware surface contains only `AID`: stored M predicates are not backed by a firmware M field. Physical sockets are not inferred from them. Four slot-1 conditions have empty predicates. Filters retain `PIR`-only choices on this ultrasonic product, and `INITIAL_OCC`/`RE-TRIGGER` subsets on 168 exclude their reusable defaults. `DAYLIGHT_SETPOINT` filter text says Provision of light; the referenced field identity remains `DAYLIGHT_SETPOINT`. Do not reinterpret these as a physical `PIR` detector.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `140` | `1` | `119` | `4145` | No textual predicate stored | None |
| `140` | `1` | `128` | `4145` | No textual predicate stored | None |
| `140` | `1` | `165` | `4145` | No textual predicate stored | None |
| `140` | `1` | `168` | `4145` | No textual predicate stored | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `140` | `119` | `192` | `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `3` | `PIR` sensitivity; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `140` | `119` | `193` | `INITIAL_OCC` | `1` = `PIR` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `3` | Initial occupancy; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `140` | `119` | `194` | `MAINTAIN_OCC` | `1` = `PIR` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Mantain occupancy; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `140` | `119` | `195` | `RE-TRIGGER` | `1` = `PIR` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Re-trigger; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `140` | `128` | `358` | `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `3` | `PIR` sensitivity; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `140` | `128` | `359` | `INITIAL_OCC` | `1` = `PIR` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `3` | Initial occupancy; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `140` | `128` | `360` | `MAINTAIN_OCC` | `1` = `PIR` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Mantain occupancy; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `140` | `128` | `361` | `RE-TRIGGER` | `1` = `PIR` only; `4` = `PIR` or `US` | `4` | Re-trigger; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `140` | `165` | `197` | `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `3` | `PIR` sensitivity; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `140` | `166` | `2109` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `140` | `166` | `2124` | `NATURAL_LIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Natural light factor |
| `140` | `166` | `2139` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `140` | `166` | `2286` | `PROVISION_OF_LIGHT` | `0` = Automatic; `1..255` = `5 × stored value` lux (entire reusable range retained) | `0` | Provision of light (Lux) |
| `140` | `166` | `2315` | `DAYLIGHT_SETPOINT` | `0`; `1..255` = `5 × stored value` lux (entire reusable range retained) | `100` | Provision of light (Lux) |
| `140` | `168` | `202` | `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `3` | `PIR` sensitivity |
| `140` | `168` | `203` | `INITIAL_OCC` | `1` = `PIR` only | `3` | Initial occupancy; reusable default `3` is outside this subset; filter supplies no replacement default |
| `140` | `168` | `204` | `MAINTAIN_OCC` | `4` = `PIR` or `US` | `4` | Mantain occupancy |
| `140` | `168` | `205` | `RE-TRIGGER` | `1` = `PIR` only | `4` | Re-trigger; reusable default `4` is outside this subset; filter supplies no replacement default |
| `140` | `168` | `2155` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `140` | `168` | `2269` | `PROVISION_OF_LIGHT` | `0` = Automatic; `1..255` = `5 × stored value` lux (entire reusable range retained) | `0` | Provision of light (Lux) |
| `140` | `168` | `2301` | `DAYLIGHT_SETPOINT` | `0`; `1..255` = `5 × stored value` lux (entire reusable range retained) | `100` | Daylight setpoint (Lux) |
| `140` | `168` | `2370` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `140` | `431` | `2392` | `TYPE_OF_REGULATION` | `3` = Stereo amplifiers only | `1` | Regulation type; reusable default `1` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `48` / `modobj = 33` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`119`, `128`, `164`, `165`, `166`, `168`, `431`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Automatic control | Auto ON/OFF responds to presence and illumination; manual ON / auto OFF requires a separate control | LE02817AD, PDF pp. 3–4 |
| Adjustment | `088230` / `088235` tools are named in this revision; LEARN and IR `LED` are shown | LE02817AD, PDF pp. 3–4 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Select the documented sensor role and its addressed actuator/controller before reading or writing Object configuration. The historical firmware record stores only `AID` and Advanced Configuration; its M selection predicates do not establish physical configurator sockets. LE02817AD PDF pp. 2–4 shows the installation methods, automatic/manual operation and adjustment tools. The remote models named in these older instructions differ from the current Italian export; no interchangeability or release cutoff is established.

## Source reconciliation

The manufacturer catalogue explicitly binds `BMSE3002` and `048821` to one technical item. LE02817AD identifies `048821` as ultrasonic with 16 mA, 500 lux and 15-minute settings. Its floor-level 8 m diagram and the 6 m `US` circle at the 1.2 m working plane are different measurement planes. No exact `BMSE3002` technical sheet was located; protection, independent coverage tables and physical sockets are not imported from `BMSE3001`/3003. This documentation gap does not unsettle the explicit catalogue identity.

Catalogue-specific scope and filter irregularities are detailed under [Object configuration surfaces](#object-configuration-surfaces); those relations do not establish additional physical sensors, load interfaces or installed behavior.

## Evidence limits and open work

- No exact `BMSE3002` technical sheet or regional EAN record is retained; enclosure protection, independent detailed `US` sensitivity matrix and `BMSE3002`-specific setup are not inferred from other products.
- The instructions' `048821` coverage diagram is retained, but installed behavior and actual detection boundaries are unobserved.
- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, software payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0051-0060-2026-10-06.md#own-dev-0053)
