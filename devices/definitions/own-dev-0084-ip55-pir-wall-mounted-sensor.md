# IP55 PIR wall mounted sensor

## Summary

This IP55 PIR sensor combines motion and daylight sensing for lighting control, with wall or ceiling mounting and 270° horizontal coverage. It offers automatic, walkthrough and manual-on operation, adjustable sensitivity, and calibrated daylight regulation; the exact settings depend on the configuration method.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0084` | Project identity |
| Technical description | IP55 PIR wall mounted sensor | Canonical catalogue |
| Commercial identities | `BMSE2006`, `048830` | Canonical commercial records |
| Catalogue item | `137` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `42` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `17` | Canonical firmware catalogue |
| Categories | Automation, Sensor | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSE2006` | Established catalogue identity | canonical commercial record for item `137` |
| Legrand | `048830` | Established catalogue identity | canonical commercial record for item `137` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| `BMSE2006-publisher-product-sheet.pdf` | product sheet | Publisher export retained 2026-10-03 | Whole product document, PDF pp. 1-1; printed p. 1 for one-page catalogue exports | [Archived original](https://archive.openwebnet-ha.org/sha256/72/77/7277c0ed6139c8f865f52093b825b6fb0eccdbe71e21b85427de8dc43ce819af.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMSE2006) |
| `BT00301_d_IT.pdf` | exact-product technical sheet | `BT00301-d-IT`, 20/11/2013 | All five pages: ratings/controls p. 1, coverage p. 2, mounting p. 3, remote settings/reset p. 4, MyHOME physical modes p. 5 | [Archived original](https://archive.openwebnet-ha.org/sha256/0f/23/0f23b2a75812de6b9e91eb88c55697f0fd674014b0a6ba081b1f022d2c1aed86.pdf) | [Publisher source](https://dar.bticino.it/asset/Documents/BT00301_d_IT.pdf) |
| `U4617A.pdf` | illustrated instructions | `U4617A` A01SY-09W51 | All three PDF pages, panels 1–7: ratings, coverage, wall/ceiling installation, Auto/Eco and IR/LEARN controls; no printed page numbers | [Archived original](https://archive.openwebnet-ha.org/sha256/e3/91/e391282de05e30fb081d80382cfd7494ba14dfe1918e679f23c372b258d37dfc.pdf) | [Publisher source](https://dar.bticino.it/asset/Documents/U4617A.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / current | `27 Vdc`; `12 mA` | `BT00301-d-IT` p. 1; `U4617A` PDF p. 1 panel 1; publisher export |
| Size / weight | `104 × 166 × 82 mm`; 250 g | `BT00301-d-IT` pp. 1, 3 |
| Protection / temperature | IP55, IK04; operation −`5..45 °C`; storage −`20..70 °C` | `BT00301-d-IT` p. 1 |
| Sensing / coverage | PIR plus daylight; horizontal 270°, vertical 90°; installation height up to 6 m | `BT00301-d-IT` p. 1 |
| Coverage at 2.5 m, maximum sensitivity | Diagram axes `A=30` m, `B=10` m; 263 m² | `BT00301-d-IT` p. 2; publisher export; geometry diagram inspected |
| Earlier instruction coverage | 90 m²; diagram height 2.4 m, range marks 5/10/15 m and approximate 6 m span | `U4617A` PDF p. 1 panels 1–2; conditions differ from the later sensitivity table |
| Connections / controls | RJ45 SCS, physical configurator sockets, IR reception/LED and LEARN button | `BT00301-d-IT` p. 1; `U4617A` PDF p. 3 panel 7 |
| Installation | Wall and ceiling arrangements illustrated | `BT00301-d-IT` p. 3; `U4617A` PDF pp. 1–2 panels 3–4 |

### Coverage by height and sensitivity

`BT00301-d-IT`, printed/PDF p. 2, supplies every height/sensitivity combination below. A/B refer to its diagram axes, in metres; the third value is area in m². They are rated coverage, not measured installation performance.

| Height (m) | Low 25%: A / B / area | Medium 50%: A / B / area | High 75%: A / B / area | Maximum 100%: A / B / area |
| --- | --- | --- | --- | --- |
| 2.5 | 8 / 3 / 66 | 15 / 5 / 131 | 23 / 8 / 197 | 30 / 10 / 263 |
| 3 | 8 / 3 / 66 | 15 / 5 / 131 | 23 / 8 / 197 | 30 / 10 / 263 |
| 4 | 8 / 2 / 58 | 15 / 5 / 116 | 23 / 7 / 174 | 30 / 9 / 233 |
| 5 | 8 / 2 / 53 | 15 / 4 / 105 | 23 / 6 / 158 | 30 / 8 / 210 |
| 6 | 8 / 2 / 47 | 15 / 4 / 94 | 23 / 5 / 141 | 30 / 7 / 188 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `137` | Canonical catalogue |
| Technical item | IP55 PIR wall mounted sensor | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `42` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `42` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `137` | `BMSE2006` | `1` | `5` | Empty in source |
| `1560` | `048830` | `2` | `5` | Empty in source |

| Record | Visible | Dependent | Gateway flag | Visibility type |
| --- | --- | --- | --- | --- |
| `137` | `1` | `0` | `0` | Empty in source |
| `1560` | `1` | `0` | `0` | Empty in source |

These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `137` | `-1` | `-1` | `-1` | `17` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `137` | `1` | `119` Stand alone presence sensor | Candidate alternative | `392` | `119` | `316` |
| `137` | `1` | `128` Scenarios daylight and presence sensor | Candidate alternative | `393` | `128` | `317` |
| `137` | `1` | `164` Scenarios daylight sensor | Candidate alternative | `394` | `164` | `318` |
| `137` | `1` | `165` Scenarios presence sensor | Candidate alternative | `395` | `165` | `319` |
| `137` | `1` | `166` Stand alone daylight sensor | Candidate alternative | `396` | `166` | `320` |
| `137` | `1` | `168` Stand alone daylight and presence sensor | Fixed/designated metadata | `397` | `168` | `321` |
| `137` | `2` | `431` IR scenario control | Fixed/designated metadata | `398` | `431` | `322` |
| `137` | `3` | `431` IR scenario control | Fixed/designated metadata | `399` | `431` | `322` |
| `137` | `4` | `431` IR scenario control | Fixed/designated metadata | `400` | `431` | `322` |
| `137` | `5` | `431` IR scenario control | Fixed/designated metadata | `401` | `431` | `322` |
| `137` | `6` | `431` IR scenario control | Fixed/designated metadata | `402` | `431` | `322` |
| `137` | `7` | `431` IR scenario control | Fixed/designated metadata | `403` | `431` | `322` |
| `137` | `8` | `431` IR scenario control | Fixed/designated metadata | `404` | `431` | `322` |
| `137` | `9` | `431` IR scenario control | Fixed/designated metadata | `405` | `431` | `322` |
| `137` | `10` | `431` IR scenario control | Fixed/designated metadata | `406` | `431` | `322` |
| `137` | `11` | `431` IR scenario control | Fixed/designated metadata | `407` | `431` | `322` |
| `137` | `12` | `431` IR scenario control | Fixed/designated metadata | `408` | `431` | `322` |
| `137` | `13` | `431` IR scenario control | Fixed/designated metadata | `409` | `431` | `322` |
| `137` | `14` | `431` IR scenario control | Fixed/designated metadata | `410` | `431` | `322` |
| `137` | `15` | `431` IR scenario control | Fixed/designated metadata | `411` | `431` | `322` |
| `137` | `16` | `431` IR scenario control | Fixed/designated metadata | `412` | `431` | `322` |
| `137` | `17` | `431` IR scenario control | Fixed/designated metadata | `413` | `431` | `322` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `137` | `515` Daylight and motion sensor virgin | `1` | `119`, `128`, `164`, `165`, `166`, `168` | `515` | `10` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `137` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `137` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

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
| `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `3` | PIR sensitivity |
| `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `2` | US sensitivity |
| `INITIAL_OCCUPANCY` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `3` | Initial occupancy |
| `MAINTAIN_OCCUPANCY` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Maintain detection |
| `RETRIGGER` | `0` = Disabled; `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Retrigger |
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
| `SCHEMA` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Detection scheme |
| `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `3` | PIR sensitivity |
| `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `2` | US sensitivity |

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
| `SCHEMA` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Detection scheme |
| `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `3` | PIR sensitivity |
| `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `2` | US sensitivity |

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
| `DAYLIGHT_SETPOINT` | `0`; `1..255` = 5 × stored value lux | `100` | Daylight setpoint (Lux) |
| `PROVISION_OF_LIGHT` | `0` = Automatic; `1..255` = 5 × stored value lux | `0` | Provision of light (Lux) |
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
| `DAYLIGHT_SETPOINT` | `0`; `1..255` = 5 × stored value lux | `100` | Daylight setpoint (Lux) |
| `PROVISION_OF_LIGHT` | `0` = Automatic; `1..255` = 5 × stored value lux | `0` | Provision of light (Lux) |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `10` | Minutes |
| `SECONDS` | `0..59` | `0` | Seconds |
| `FUNC_MODE` | `1` = Auto `ON`/`OFF`; `2` = Auto walkthrough; `3` = Manual `ON` / Auto `OFF`; `5` = Partial `ON` / Group `OFF` | `2` | Operating mode; Functional_mode |
| `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `3` | PIR sensitivity |
| `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `1` | US sensitivity |
| `INITIAL_OCC` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `3` | Initial detection |
| `MAINTAIN_OCC` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Maintain detection |
| `RE-TRIGGER` | `0` = Disabled; `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Re-trigger |
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
| `ID1` | `0..255` | `0` | ID1 |
| `ID2` | `0..255` | `0` | ID2 |
| `ID3` | `0..15` | `0` | ID3 |
| `UNIT_NUMBER` | `0..15` | `0` | Push button number |

### Device-specific interpretation

Firmware `137` declares 17 Modules: six alternative sensor Objects in slot `1` (fixed/designated `168`) and Object `431` in slots `2..17`. Virgin `515` permits those six alternatives only in slot `1`; these are logical contexts, not 17 physical sensors. Five conditions select Object `128` for `M=2`, `166` for `M=1/4` and `168` for `M=0/3`, but the firmware exposes only AID: M is an unresolved condition symbol in this extraction, not an invented firmware field. Only Advanced Configuration `2` is associated despite the product sheet documenting physical/virtual routes. US-related reusable/filter domains do not prove ultrasonic hardware: the exact product is PIR. Cross-Object field links INITIAL_OCC versus INITIAL_OCCUPANCY, MAINTAIN_OCC versus MAINTAIN_OCCUPANCY, and RE-TRIGGER versus RETRIGGER remain literal and separate. ALERT filters `2351`/`2352` exclude default `0`; IR regulation filter `2393` permits only stereo amplifiers `3` while the reusable default is lights `1`. No replacement defaults are supplied. Setpoint/provision filters `2450`/`2462` have subset flags but zero stored allowed values, an unresolved restriction rather than an empty proven hardware domain. Lux encodings retain sentinel `0` and `1..255` mapped to `5..1275` in steps of five; `DAYLIGHT_SETPOINT` default `100` means `500 lux`, while `PROVISION_OF_LIGHT` `0` explicitly means automatic. Object timer defaults `10` or `15 min`, regulation default disabled and occupancy defaults are distinct from the product-sheet configuration defaults. No selection predicate is stored for candidates 119/164/165 or the IR slots; catalogue membership does not establish runtime activation or selection precedence.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `137` | `1` | `128` | `4477` | `M=2` | None |
| `137` | `1` | `166` | `4461` | `M=1` | None |
| `137` | `1` | `166` | `4505` | `M=4` | None |
| `137` | `1` | `168` | `4439` | `M=0` | None |
| `137` | `1` | `168` | `4491` | `M=3` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `137` | `119` | `161` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `1` | US sensitivity; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `137` | `119` | `162` | `INITIAL_OCC` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `3` | Initial occupancy; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `137` | `119` | `163` | `MAINTAIN_OCC` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Mantain occupancy; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `137` | `119` | `164` | `RE-TRIGGER` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Re-trigger; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `137` | `119` | `2347` | `INITIAL_OCCUPANCY` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `3` | Initial occupancy |
| `137` | `119` | `2348` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | US sensitivity |
| `137` | `119` | `2349` | `MAINTAIN_OCCUPANCY` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Mantain occupancy |
| `137` | `119` | `2350` | `RETRIGGER` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Re-trigger |
| `137` | `119` | `2351` | `ALERT` | `1` = Visual; `3` = Visual and Acoustic | `0` | Alert; reusable default `0` is outside this subset; filter supplies no replacement default |
| `137` | `128` | `166` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | US sensitivity |
| `137` | `128` | `167` | `SCHEMA` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Detection Schema |
| `137` | `165` | `168` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | US sensitivity |
| `137` | `165` | `169` | `SCHEMA` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Detection Schema |
| `137` | `166` | `2106` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `137` | `166` | `2121` | `NATURAL_LIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Natural light factor |
| `137` | `166` | `2136` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `137` | `168` | `170` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `1` | US sensitivity |
| `137` | `168` | `171` | `FUNC_MODE` | `2` = Auto walkthrough | `2` | Functional mode |
| `137` | `168` | `172` | `RE-TRIGGER` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Re-trigger |
| `137` | `168` | `173` | `MAINTAIN_OCC` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Mantain occupancy |
| `137` | `168` | `174` | `INITIAL_OCC` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `3` | Initial occupancy |
| `137` | `168` | `2152` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `137` | `168` | `2352` | `ALERT` | `1` = Visual; `3` = Visual and Acoustic | `0` | Alert; reusable default `0` is outside this subset; filter supplies no replacement default |
| `137` | `168` | `2360` | `NATURAL_LIGHT_FACTOR` | `1..255` (entire reusable range retained) | `10` | Natural light factor |
| `137` | `168` | `2367` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `137` | `168` | `2450` | `DAYLIGHT_SETPOINT` | Subset flag present but no allowed values stored; unresolved restriction | `100` | Daylight setpoint (Lux) |
| `137` | `168` | `2462` | `PROVISION_OF_LIGHT` | Subset flag present but no allowed values stored; unresolved restriction | `0` | Provision of light (Lux) |
| `137` | `431` | `2393` | `TYPE_OF_REGULATION` | `3` = Stereo amplifiers only | `1` | Regulation type; reusable default `1` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `137` / `modobj = 42` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`119`, `128`, `164`, `165`, `166`, `168`, `431`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `119` Stand alone presence sensor | Automation | Firmware/Object capability association; resolve the slot and configuration first |
| `128` Scenarios daylight and presence sensor | Automation | Firmware/Object capability association; resolve the slot and configuration first |
| `164` Scenarios daylight sensor | Automation | Firmware/Object capability association; resolve the slot and configuration first |
| `165` Scenarios presence sensor | Automation | Firmware/Object capability association; resolve the slot and configuration first |
| `166` Stand alone daylight sensor | Automation | Firmware/Object capability association; resolve the slot and configuration first |
| `168` Stand alone daylight and presence sensor | Automation | Firmware/Object capability association; resolve the slot and configuration first |
| `431` IR scenario control | Automation | Firmware/Object capability association; resolve the slot and configuration first |

These are catalogue Object/system associations, not `WHO` numbers, physical connector claims or observed command acceptance. Resolve the active Module/Object and its restrictions before using the [Functional Protocol](../../functional/).

### Published product functions

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Delay | Default 15 min; `BMSO4003` choices 3/5/10/15/20 min; `BMSO4001` range 5 s..59 min 59 s | `BT00301-d-IT` p. 4 |
| Sensitivity | PIR maximum default for remote settings; four sensitivity levels | Same page; physical S defaults differ below |
| Daylight threshold | Default 300 lux; basic remote 20/100/300/500/1000 lux; advanced `5..1275` lux | Same page |
| Remote modes | Auto inactive, Walkthrough active, Eco inactive in the printed default table | Same page |
| Walkthrough | Presence shorter than 20 s reduces delay to 3 min, unless the configured delay is already shorter | Same page |
| Eco | Manual ON, automatic absence OFF; detection within 30 s after OFF retriggers, then manual ON is needed | Same page |
| Detection schemas | Initial and maintain are fixed PIR; retrigger default PIR; table lists PIR/US alternatives without proving US hardware | Same page |
| Alert | Inactive default; optional pre-off warnings at 1 min, 30 s and 10 s | Same page |
| Calibration / regulation | Calibration `0..99995` lux; regulation active default; provision of light Auto or up to 1275 lux. Calibrate artificial light at full output with shutters closed, then natural light with load OFF/shutters open | Same page |
| Daylight regulation | Switch off after 10 min plus safety interval above threshold even with presence; manual level/ON/OFF interactions depend on M | `BT00301-d-IT` pp. 4–5 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

`BT00301-d-IT` p. 5 distinguishes MyHOME physical/virtual configuration from Lighting Management Plug&Go, Push&Learn and Virtual Configurator. Plug&Go requires a Room Controller. MyHOME virtual configuration uses software with kit 3503N or a MyHOME web server. Physical/virtual configuration disables remotes and advanced functions; the historical catalogue separately associates only Advanced Configuration `2`.

### MyHOME physical configuration

`BT00301-d-IT`, printed/PDF p. 5, supplies these settings. Physical/virtual mode disables remote configuration and advanced functions.

| Socket | Permitted physical values | Default / behavior |
| --- | --- | --- |
| A, PL | `1..9` | Nonzero point addressing |
| M | `0..4` | See mode matrix |
| S | Unset, `1..3` | Unset low; 1 medium, 2 high, 3 maximum |
| T | Unset, `1..9` | Unset 15 min; 1=30 s, 2=1 min, 3=2 min, 4=5 min, 5=10 min, 6=15 min, 7=20 min, 8=30 min, 9=40 min |
| D | Unset, `1..5` | Unset 300 lux wall / 500 lux ceiling; 1=20, 2=100, 3=300, 4=500, 5=1000 lux |

| M | Function | Constraint / manual-control consequence |
| --- | --- | --- |
| `0` | Presence/daylight ON, delayed absence OFF | Manual OFF inhibits until absence for T |
| `1` | Daylight only | Point-to-point; S/T unused; no general/room/group commands |
| `2` | MH200N scenario notification | Unique point address; S/T unused |
| `3` | Closed-loop presence/daylight regulation | Manual level temporary until absence for T; manual OFF inhibits until manual ON; A/PL/M/S/T required |
| `4` | Daylight regulation without presence | Manual start; never automatic ON; high daylight can dim to OFF |

These are published physical settings, not additional firmware fields.

Factory reset: briefly press LEARN for slow blinking, then hold LEARN 10 s for rapid blinking (p. 4). The illustrated Auto/Eco procedures and receiver controls in `U4617A` PDF pp. 2–3 agree with separate automatic/manual-start roles.

## Source reconciliation

`BT00301-d-IT` (20/11/2013), the older `U4617A` (09W51) and the retained product export directly name `BMSE2006`. The export’s delay range `30 s..255 h` differs from the technical sheet’s remote and physical routes; catalogue `HOURS` `0..255` is another scope. `U4617A`’s 90 m² and 2.4 m mounting diagram differ from the later 263 m² maximum-sensitivity table. Both are preserved without silently selecting one universal coverage. The technical sheet labels `12 mA` as dissipated power; the unit, export and illustrated current symbol support current demand, not 12 mW. Its Auto paragraph says insufficient natural light causes OFF, contrary to the threshold/regulation explanation; the contradiction remains. Physical sensitivity and wall/ceiling daylight defaults differ from remote defaults. No claim of ultrasonic hardware follows from reusable US fields or the retrigger table. The Legrand 048830 identity is catalogue-established; exact-variant hardware differences are not independently resolved.

Catalogue interpretation is detailed under [Object configuration surfaces](#object-configuration-surfaces); the complete firmware, topology and restriction tables remain authoritative for software applicability.

## Evidence limits and open work

- Clarify the export/older-instruction coverage and delay scopes, inconsistent Auto wording, and the two zero-value subset filters with exact revision or software evidence.
- Obtain separately applicable 048830 documentation; correlate remote/physical/local settings with active Objects on hardware.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0081-0090-2026-10-06.md#own-dev-0084)
