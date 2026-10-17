# Occupancy sensor + IR + ZigBee

## Summary

The catalogue identifies this as an occupancy sensor combining IR and ZigBee communication. Its software model includes sensing and IR scenario-control roles, while the exact hardware construction, radio profile and commissioning procedure remain undocumented in the retained sources.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0063` | Project identity |
| Technical description | Occupancy sensor + IR + ZigBee | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSE2007`, `048831` | Canonical commercial records |
| Catalogue item | `58` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `41` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `17` | Canonical firmware catalogue |
| Categories | Occupancy sensing, IR, ZigBee, Lighting Management | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSE2007` | Established identity | canonical commercial record for item `58` |
| Legrand | `048831` | Established identity | canonical commercial record for item `58` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite version history | software compatibility record | Document dated 2015-03-20; applicable product list under first release 1.0.45 dated 2013-10-10 | Printed/PDF p. 4; both exact references listed for virtual configuration; software compatibility only, not physical specifications or installed firmware | [Archived original](https://archive.openwebnet-ha.org/sha256/cd/c4/cdc467fa6408908a98348892c78a98439826b216197f7b17b4230da9f46554c3.pdf) | [Official compatibility source](https://myhomeswupdate.bticino.com/VersionHistory/Version_History_MyHOME_Suite_20150320.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Catalogue-established product role | occupancy sensor with IR and ZigBee communication | Canonical item 58 |
| Physical ratings | Supply, consumption, enclosure, dimensions and optical/radio limits are not established by the retained compatibility list | Canonical item 58 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `58` | Canonical catalogue |
| Technical item | Occupancy sensor + IR + ZigBee | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `41` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `41` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `58` | `BMSE2007` | `1` | `5` | Empty in source |
| `1561` | `048831` | `2` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `138` | `-1` | `-1` | `-1` | `17` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `138` | `1` | `119` Stand alone presence sensor | Candidate alternative | `414` | `119` | `323` |
| `138` | `1` | `128` Scenarios daylight and presence sensor | Candidate alternative | `415` | `128` | `324` |
| `138` | `1` | `164` Scenarios daylight sensor | Candidate alternative | `416` | `164` | `325` |
| `138` | `1` | `165` Scenarios presence sensor | Candidate alternative | `417` | `165` | `326` |
| `138` | `1` | `166` Stand alone daylight sensor | Candidate alternative | `418` | `166` | `327` |
| `138` | `1` | `168` Stand alone daylight and presence sensor | Fixed/designated metadata | `419` | `168` | `328` |
| `138` | `2` | `431` IR scenario control | Fixed/designated metadata | `420` | `431` | `329` |
| `138` | `3` | `431` IR scenario control | Fixed/designated metadata | `421` | `431` | `329` |
| `138` | `4` | `431` IR scenario control | Fixed/designated metadata | `422` | `431` | `329` |
| `138` | `5` | `431` IR scenario control | Fixed/designated metadata | `423` | `431` | `329` |
| `138` | `6` | `431` IR scenario control | Fixed/designated metadata | `424` | `431` | `329` |
| `138` | `7` | `431` IR scenario control | Fixed/designated metadata | `425` | `431` | `329` |
| `138` | `8` | `431` IR scenario control | Fixed/designated metadata | `426` | `431` | `329` |
| `138` | `9` | `431` IR scenario control | Fixed/designated metadata | `427` | `431` | `329` |
| `138` | `10` | `431` IR scenario control | Fixed/designated metadata | `428` | `431` | `329` |
| `138` | `11` | `431` IR scenario control | Fixed/designated metadata | `429` | `431` | `329` |
| `138` | `12` | `431` IR scenario control | Fixed/designated metadata | `430` | `431` | `329` |
| `138` | `13` | `431` IR scenario control | Fixed/designated metadata | `431` | `431` | `329` |
| `138` | `14` | `431` IR scenario control | Fixed/designated metadata | `432` | `431` | `329` |
| `138` | `15` | `431` IR scenario control | Fixed/designated metadata | `433` | `431` | `329` |
| `138` | `16` | `431` IR scenario control | Fixed/designated metadata | `434` | `431` | `329` |
| `138` | `17` | `431` IR scenario control | Fixed/designated metadata | `435` | `431` | `329` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `138` | `515` Daylight and motion sensor virgin | `1` | `119`, `128`, `164`, `165`, `166`, `168` | `515` | `11` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `138` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `138` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

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

Slot `1` admits six sensor Objects (119/128/164/165/166/168); slots `2..17` designate IR scenario Object `431`. Virgin `515` applies only to slot `1` and admits the same six alternatives. These are software placements, not seventeen physical sensors. Reusable timers default to 10 minutes in 119/168 and 15 minutes in 128/165; these do not override a product factory setting. `DAYLIGHT_SETPOINT` and `PROVISION_OF_LIGHT` encode `1..255` as five times the stored value in lux: setpoint default 100 means 500 lux, with zero unlabelled; provision zero means Automatic. Object `431` `TYPE_OF_REGULATION` is restricted to 3 (stereo), excluding default 1 without a replacement; this does not prove sixteen installed IR functions or speaker hardware. Firmware `138` stores only `AID` and Advanced Configuration. No slot condition or conversion is associated, so neither physical M selectors nor automatic activation of every candidate is established. Daylight restrictions retain their reusable domains; the Provision of light description on Object `166` still references `DAYLIGHT_SETPOINT`. Reusable `PIR`/`US` choices do not establish detector construction for this catalogue-described IR/ZigBee product. Catalogue private-riser/local-bus associations do not prove a wired connector on the radio-described product.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `138` | `166` | `2107` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `138` | `166` | `2122` | `NATURAL_LIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Natural light factor |
| `138` | `166` | `2137` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `138` | `166` | `2284` | `PROVISION_OF_LIGHT` | `0` = Automatic; `1..255` = `5 × stored value` lux (entire reusable range retained) | `0` | Provision of light (Lux) |
| `138` | `166` | `2313` | `DAYLIGHT_SETPOINT` | `0`; `1..255` = `5 × stored value` lux (entire reusable range retained) | `100` | Provision of light (Lux) |
| `138` | `168` | `2153` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `138` | `168` | `2267` | `PROVISION_OF_LIGHT` | `0` = Automatic; `1..255` = `5 × stored value` lux (entire reusable range retained) | `0` | Provision of light (Lux) |
| `138` | `168` | `2299` | `DAYLIGHT_SETPOINT` | `0`; `1..255` = `5 × stored value` lux (entire reusable range retained) | `100` | Daylight setpoint (Lux) |
| `138` | `168` | `2368` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `138` | `431` | `2394` | `TYPE_OF_REGULATION` | `3` = Stereo amplifiers only | `1` | Regulation type; reusable default `1` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `58` / `modobj = 41` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`119`, `128`, `164`, `165`, `166`, `168`, `431`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Software compatibility | `BMSE2007` and `048831` occur in the product list for first release 1.0.45 dated 10 October 2013 | Version_History_MyHOME_Suite_20150320, printed/PDF p. 4 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Resolve the active Module/Object and its catalogue restrictions before interpreting configuration. The only firmware-level field is `AID` and the only associated mode is Advanced Configuration; no exact retained instructions establish physical configurators or a commissioning sequence. Seventeen catalogue Modules describe alternative sensor and IR scenario roles. They do not establish seventeen physical inputs, a ZigBee profile, a pairing sequence or a wired SCS connector.

## Source reconciliation

Both references explicitly map to the same technical item. The version history corroborates both exact references in its 1.0.45 product list (p. 4), not newly added support in the document’s 20 March 2015 release and not an installed 3.5.38 firmware. Exact-reference manufacturer searches and historical retained Spanish/German catalogues did not establish a technical sheet; the Italian exact-reference product export returned HTTP 500 on 6 October 2026. That endpoint failure is not evidence that a product or document never existed. Missing physical documentation does not make either identity unresolved.

Catalogue-specific scope, selectors, defaults and filter/conversion irregularities are detailed under [Object configuration surfaces](#object-configuration-surfaces). Those software relations do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- Exact-product physical specifications, factory settings and commissioning instructions remain a documentation gap.
- Detector technology, radio frequency/profile, power source, pairing and IR remote compatibility are not established by the catalogue role.
- No verified EAN is retained for either reference; adjacent sensor specifications are not imported.
- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0061-0070-2026-10-06.md#own-dev-0063)
