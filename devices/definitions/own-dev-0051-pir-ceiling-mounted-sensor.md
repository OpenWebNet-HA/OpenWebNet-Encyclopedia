# `PIR` ceiling-mounted sensor

## Summary

This recessed ceiling sensor combines passive infrared movement detection with a daylight threshold to control SCS lighting or a controller scenario. Its circular coverage suits open rooms, while sensitivity, switch-off delay and automatic/manual operation must be set for the installation.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0051` | Project identity |
| Technical description | `PIR` ceiling-mounted sensor | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSE3001`, `048820` | Canonical commercial records |
| Catalogue item | `45` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `32` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `17` | Canonical firmware catalogue |
| Categories | Presence sensing, Daylight sensing, Automation | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSE3001` | Established identity | canonical commercial record for item `45` |
| Legrand | `048820` | Established identity | canonical commercial record for item `45` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `BMSE3001` | `8012199969244` | [Archived original](https://archive.openwebnet-ha.org/sha256/da/5b/da5be9f0e28958201f20b4cd2fc10bc644a8b8fe1dbc5d2cdb68fae911f8bdc2.pdf), `BMSE3001-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `048820` | `3245060488208` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/51/e4/51e4428663389a4b107f15200e367fd26475c079998c8b1d7eff721267d8f18c.pdf), `048820-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `LE10699AA-FR` | technical/system guide | LE10699AA-FR; no dated imprint established | Printed/PDF p. 60; exact paired identities, physical ratings and full sensitivity/height coverage; unrelated guide pages and hotel-controller programming not examined | [Archived original](https://archive.openwebnet-ha.org/sha256/48/54/4854112b1d66d371515e11e1759d3a88d68cd2dad465a25c8799d55a74298d30.pdf) | [Official source](https://assets.legrand.com/general/mediagrp/np-ft-gt/le10699aa-fr.pdf) |
| `BMSE3001-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `BMSE3001` to EAN-13 relationship at printed/PDF p. 1. Exact-reference identifiers and technical export attributes examined; linked downloads and prices outside scope. | [Archived original](https://archive.openwebnet-ha.org/sha256/da/5b/da5be9f0e28958201f20b4cd2fc10bc644a8b8fe1dbc5d2cdb68fae911f8bdc2.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMSE3001) |
| `048820-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact SKU/GTIN metadata and EAN/Gencode field; other technical attributes, linked documents and prices not incorporated | [Archived HTML](https://archive.openwebnet-ha.org/sha256/51/e4/51e4428663389a4b107f15200e367fd26475c079998c8b1d7eff721267d8f18c.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue-archives/detecteur-de-mouvements-bus-fixation-plafond-special-couloir) |
| `ch_de_katalog_wohnbau.pdf` | Historical residential catalogue | No dated imprint established | Printed pp. 156–157, 159 / PDF pp. 158–159, 161; exact sensor entries, complete coverage and mounting-specific dimension drawing | [Archived original](https://archive.openwebnet-ha.org/sha256/9f/e5/9fe511c3ac12d861dff7d8d28ddec3b3612a27e99a804afbed89877c73a6b4ed.pdf) | Publisher URL not retained in manifest |
| `U4615A.pdf` | Pictographic installation instructions | U4615A01SY-09W51 | No printed page numbering; PDF pp. 1–3, `BMSE3001`/`BMSE3003` ratings, mounting, cover release and mode selection | [Archived original](https://archive.openwebnet-ha.org/sha256/da/d7/dad7569e38b9cf2f7d8dca0f6eaa9022624a6067b8aff90e00527fd530f2982c.pdf) | [Publisher source](https://dar.bticino.com/asset/Documents/U4615A.pdf) |
| `LE02817AD.pdf` | Pictographic installation instructions | Revision AD; no separate date established | No consistent printed pagination; PDF pp. 1–4; exact `048820`/21/22 sensor-type, installation and adjustment diagrams | [Archived original](https://archive.openwebnet-ha.org/sha256/72/48/7248bde719c44406319ccaff2131c760858d3ec2558c6ff7c087cf1f64b8aaa4.pdf) | Publisher URL not retained in manifest |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / current | `27 Vdc`; `12 mA` | LE02817AD, PDF p. 1 |
| Environment | `−5..45 °C` | LE02817AD, PDF p. 1 |
| Sensing | `PIR` movement detection and daylight threshold | LE02817AD, PDF p. 1 |
| Protection / storage | IP20; IK04; −`20..70 °C` | LE10699AA-FR, printed/PDF p. 60 |
| Ceiling opening | `65 mm` without installation box; `68 mm` with box | LE10699AA-FR, printed/PDF p. 60 |
| Connection | SCS bus through RJ45/BUS adapter `048872` | LE10699AA-FR, printed/PDF p. 60 |
| Detection angle | 360° | LE10699AA-FR, printed/PDF p. 60 |
| Current commercial dimensions | `100 mm` diameter × `52 mm` depth | `BMSE3001`-ean-product-sheet.pdf, printed p. 1 / PDF p. 1 |
| Maximum installation height | 6 m | `BMSE3001`-ean-product-sheet.pdf, printed p. 1 / PDF p. 1 |
| Current commercial coverage at 2.5 m | `PIR`: 8 m diameter / 50 m² | `BMSE3001`-ean-product-sheet.pdf, printed p. 1 / PDF p. 1 |
| Surface installation accessory | LG-`048874` | `BMSE3001`-ean-product-sheet.pdf, printed p. 1 / PDF p. 1 |
| Earlier coverage headline | 45 m² | U4615A, no printed page numbers / PDF p. 1 |
| Published settings | 500 lux / 15 min shown in instructions; light threshold `5..1275` lux; delay 30 s..255 h 59 min 59 s; sensitivity 25%, 50%, 75%, 100% | LE02817AD, PDF pp. 1, 4 |

### `PIR` coverage

Each cell gives diameter and publisher-stated area; areas are not recalculated. LE10699AA-FR, printed/PDF p. 60.

| Height (m) | Low (25%) | Medium (50%) | High (75%) | Maximum (100%) |
| --- | --- | --- | --- | --- |
| `2.5` | `4 m Ø / 15 m²` | `6 m Ø / 25 m²` | `6.5 m Ø / 30 m²` | `8 m Ø / 50 m²` |
| `3` | `5.5 m Ø / 25 m²` | `6.5 m Ø / 35 m²` | `8.5 m Ø / 60 m²` | `11.5 m Ø / 100 m²` |
| `4` | `6.5 m Ø / 35 m²` | `7.5 m Ø / 45 m²` | `12.5 m Ø / 125 m²` | `14 m Ø / 155 m²` |
| `5` | `6 m Ø / 30 m²` | `10.5 m Ø / 90 m²` | `12 m Ø / 115 m²` | `16.5 m Ø / 215 m²` |
| `6` | `4 m Ø / 15 m²` | `5.5 m Ø / 25 m²` | `8.5 m Ø / 60 m²` | `12.5 m Ø / 125 m²` |

### Mounting-specific dimension drawing

The German catalogue printed p. 159 / PDF p. 161 uses drawing letters, not interchangeable whole-product dimensions. Values below retain those labels; the two mounting outlines must be read in the original.

| Drawing | A | B | C | D | E | F | G | H | I | L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BMSE3001` | `102 mm` | `R:51 mm` | `50 mm` | `52.3 mm` | `51.5 mm` | `37 mm` | `102 mm` | `53.74 mm` | `55.6 mm` | `47 mm` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `45` | Canonical catalogue |
| Technical item | `PIR` ceiling-mounted sensor | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `32` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `32` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `45` | `BMSE3001` | `1` | `4` | Empty in source |
| `1575` | `048820` | `2` | `4` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; `visibility_type` is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `139` | `-1` | `-1` | `-1` | `17` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `139` | `1` | `119` Stand alone presence sensor | Candidate alternative | `436` | `119` | `330` |
| `139` | `1` | `128` Scenarios daylight and presence sensor | Candidate alternative | `588` | `128` | `407` |
| `139` | `1` | `164` Scenarios daylight sensor | Candidate alternative | `437` | `164` | `331` |
| `139` | `1` | `165` Scenarios presence sensor | Candidate alternative | `438` | `165` | `332` |
| `139` | `1` | `166` Stand alone daylight sensor | Candidate alternative | `439` | `166` | `333` |
| `139` | `1` | `168` Stand alone daylight and presence sensor | Fixed/designated metadata | `440` | `168` | `334` |
| `139` | `2` | `431` IR scenario control | Fixed/designated metadata | `441` | `431` | `335` |
| `139` | `3` | `431` IR scenario control | Fixed/designated metadata | `442` | `431` | `335` |
| `139` | `4` | `431` IR scenario control | Fixed/designated metadata | `443` | `431` | `335` |
| `139` | `5` | `431` IR scenario control | Fixed/designated metadata | `444` | `431` | `335` |
| `139` | `6` | `431` IR scenario control | Fixed/designated metadata | `445` | `431` | `335` |
| `139` | `7` | `431` IR scenario control | Fixed/designated metadata | `446` | `431` | `335` |
| `139` | `8` | `431` IR scenario control | Fixed/designated metadata | `447` | `431` | `335` |
| `139` | `9` | `431` IR scenario control | Fixed/designated metadata | `448` | `431` | `335` |
| `139` | `10` | `431` IR scenario control | Fixed/designated metadata | `449` | `431` | `335` |
| `139` | `11` | `431` IR scenario control | Fixed/designated metadata | `450` | `431` | `335` |
| `139` | `12` | `431` IR scenario control | Fixed/designated metadata | `451` | `431` | `335` |
| `139` | `13` | `431` IR scenario control | Fixed/designated metadata | `452` | `431` | `335` |
| `139` | `14` | `431` IR scenario control | Fixed/designated metadata | `453` | `431` | `335` |
| `139` | `15` | `431` IR scenario control | Fixed/designated metadata | `454` | `431` | `335` |
| `139` | `16` | `431` IR scenario control | Fixed/designated metadata | `455` | `431` | `335` |
| `139` | `17` | `431` IR scenario control | Fixed/designated metadata | `456` | `431` | `335` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `139` | `515` Daylight and motion sensor virgin | `1` | `119`, `128`, `164`, `165`, `166`, `168` | `515` | `12` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `139` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `139` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

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

The catalogue declares 17 Modules: slot `1` offers six sensor Objects, while slots `2..17` designate IR scenario control 431. Virgin `515` applies only to slot `1` and admits the same six Objects; this is one sensing product, not seventeen physical sensors. `M=0/3` selects 168, `M=1/4` selects 166, `M=2` selects 128 where those predicates are stored. Candidate 119/164/165 membership is not proof of automatic activation. No conversion rule supplies a physical-to-Object mapping. Reusable timers default to 10 minutes in 119/168 and 15 in 128/165; these do not override the published 15-minute product setting. `DAYLIGHT_SETPOINT` and `PROVISION_OF_LIGHT` encode `1..255` as five times the stored value in lux; `DAYLIGHT_SETPOINT` default 100 therefore encodes 500 lux, not 100 lux. Zero setpoint has no stored label; provision zero is Automatic. `TYPE_OF_REGULATION` on 431 is restricted to 3 (stereo amplifiers), excluding reusable default 1 without a replacement. This does not establish a speaker or sixteen installed IR functions. The firmware surface contains only `AID`: stored M predicates are not backed by a firmware M field. Physical sockets are not inferred from them. Filters retain `US`-only and combined `PIR`/`US` schemes; they do not establish ultrasonic hardware on a `PIR`-only SKU. Older cross-Object `US`/`INITIAL_OCC`/`MAINTAIN_OCC`/`RE-TRIGGER` references are distinct from newer same-Object fields and must not be aliased. `ALERT` filters exclude default 0 without replacements. Empty allowed-value subsets on daylight/provision fields remain unresolved, not unrestricted.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `139` | `1` | `128` | `4477` | `M=2` | None |
| `139` | `1` | `166` | `4461` | `M=1` | None |
| `139` | `1` | `166` | `4505` | `M=4` | None |
| `139` | `1` | `168` | `4439` | `M=0` | None |
| `139` | `1` | `168` | `4491` | `M=3` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `139` | `119` | `175` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `1` | `US` sensitivity; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `139` | `119` | `176` | `INITIAL_OCC` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `3` | Initial occupancy; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `139` | `119` | `177` | `MAINTAIN_OCC` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Mantain occupancy; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `139` | `119` | `178` | `RE-TRIGGER` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Re-trigger; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `139` | `119` | `2322` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | `US` sensitivity |
| `139` | `119` | `2323` | `INITIAL_OCCUPANCY` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `3` | Initial occupancy |
| `139` | `119` | `2324` | `MAINTAIN_OCCUPANCY` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Mantain occupancy |
| `139` | `119` | `2325` | `RETRIGGER` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Re-trigger |
| `139` | `119` | `2326` | `ALERT` | `1` = Visual; `3` = Visual and Acoustic | `0` | Alert; reusable default `0` is outside this subset; filter supplies no replacement default |
| `139` | `128` | `353` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `1` | `US` sensitivity; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `139` | `128` | `354` | `INITIAL_OCC` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `3` | Initial occupancy; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `139` | `128` | `355` | `MAINTAIN_OCC` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Mantain occupancy; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `139` | `128` | `356` | `RE-TRIGGER` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Re-trigger; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `139` | `128` | `2329` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | `US` sensitivity |
| `139` | `128` | `2330` | `SCHEMA` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Detection scheme |
| `139` | `165` | `180` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `1` | `US` sensitivity; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `139` | `165` | `181` | `INITIAL_OCC` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `3` | Initial occupancy; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `139` | `165` | `182` | `MAINTAIN_OCC` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Mantain occupancy; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `139` | `165` | `183` | `RE-TRIGGER` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Re-trigger; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `139` | `165` | `2327` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | `US` sensitivity |
| `139` | `165` | `2328` | `SCHEMA` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Detection scheme |
| `139` | `166` | `2108` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `139` | `166` | `2123` | `NATURAL_LIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Natural light factor |
| `139` | `166` | `2138` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `139` | `168` | `187` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `1` | `US` sensitivity |
| `139` | `168` | `188` | `INITIAL_OCC` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `3` | Initial occupancy |
| `139` | `168` | `189` | `MAINTAIN_OCC` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Mantain occupancy |
| `139` | `168` | `190` | `RE-TRIGGER` | `2` = `US` only; `3` = `PIR` and `US`; `4` = `PIR` or `US` | `4` | Re-trigger |
| `139` | `168` | `2154` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `139` | `168` | `2212` | `NATURAL_LIGHT_FACTOR` | `1..255` (entire reusable range retained) | `10` | Natural light factor |
| `139` | `168` | `2213` | `ALERT` | `1` = Visual; `3` = Visual and Acoustic | `0` | Alert; reusable default `0` is outside this subset; filter supplies no replacement default |
| `139` | `168` | `2369` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `139` | `168` | `2451` | `DAYLIGHT_SETPOINT` | Subset flag present but no allowed values stored; unresolved restriction | `100` | Daylight setpoint (Lux) |
| `139` | `168` | `2463` | `PROVISION_OF_LIGHT` | Subset flag present but no allowed values stored; unresolved restriction | `0` | Provision of light (Lux) |
| `139` | `431` | `2390` | `TYPE_OF_REGULATION` | `3` = Stereo amplifiers only | `1` | Regulation type; reusable default `1` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `45` / `modobj = 32` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`119`, `128`, `164`, `165`, `166`, `168`, `431`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Automatic control | Auto ON/OFF responds to presence and illumination; manual ON / auto OFF requires a separate control | LE02817AD, PDF pp. 3–4 |
| Adjustment | `088230` / `088235` tools are named in this revision; LEARN and IR `LED` are shown | LE02817AD, PDF pp. 3–4 |
| Current setup tools | `088240` and `BMSO4001`, or configuration software; connection by terminal and RJ45 | Italian exact-product export, printed/PDF p. 1 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Select the documented sensor role and its addressed actuator/controller before reading or writing Object configuration. The historical firmware record stores only `AID` and Advanced Configuration; its M selection predicates do not establish physical configurator sockets. U4615A PDF p. 2 shows spring/boxed ceiling mounting and different front-cover release methods for `BMSE3001` and `BMSE3003`; PDF p. 3 shows Auto/Eco selection and LEARN/IR indicators. LE02817AD PDF pp. 2–4 shows the installation methods, automatic/manual operation and adjustment tools. The remote models named in these older instructions differ from the current Italian export; no interchangeability or release cutoff is established.

## Source reconciliation

Catalogue SKU relationships establish both commercial identities. The guide explicitly pairs the two references and agrees with the Italian export on current and supply. U4615A gives 500 lux/15 min and 45 m², whereas the guide/export provides sensitivity- and height-specific coverage. These headlines are source-specific, not one guaranteed effective area. The retained German catalogue PDF p. 158 / printed p. 156 gives 10 mA for `BMSE3001`/3003, conflicting with the exact instructions/export (12/17 mA), and 300 lux/15 min instead of the instructions' 500 lux. Its 256-hour ceiling conflicts with the exact delay limits. No hardware revision or correction notice resolves these differences.

The historical dimension drawing distinguishes boxed and ceiling mounting outlines. Its more precise drawing labels differ from the rounded current-export overall dimensions; they are retained with their mounting context rather than silently substituted.

Catalogue-specific scope and filter irregularities are detailed under [Object configuration surfaces](#object-configuration-surfaces); those relations do not establish additional physical sensors, load interfaces or installed behavior.

## Evidence limits and open work

- Installed thresholds, remote compatibility, active sensor Object and diagnostic results remain unobserved.
- Applicable manufacturer export links to technical sheets, use instructions and drawings were identified but their unexamined responses are not used as evidence.
- Coverage and factory-setting differences are not mapped to a production revision.
- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, software payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `BMSE3001-ean-product-sheet.pdf`, printed/PDF p. 1: exact `BMSE3001` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/da/5b/da5be9f0e28958201f20b4cd2fc10bc644a8b8fe1dbc5d2cdb68fae911f8bdc2.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMSE3001); SHA-256 `da5be9f0e28958201f20b4cd2fc10bc644a8b8fe1dbc5d2cdb68fae911f8bdc2`.

- `048820-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `048820` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/51/e4/51e4428663389a4b107f15200e367fd26475c079998c8b1d7eff721267d8f18c.pdf); [publisher source](https://www.legrand.fr/pro/catalogue-archives/detecteur-de-mouvements-bus-fixation-plafond-special-couloir); SHA-256 `51e4428663389a4b107f15200e367fd26475c079998c8b1d7eff721267d8f18c`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0051-0060-2026-10-06.md#own-dev-0051)
