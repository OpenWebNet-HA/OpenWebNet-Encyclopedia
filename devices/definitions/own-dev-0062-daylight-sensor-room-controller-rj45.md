# Daylight sensor for Room Controller + RJ45

## Summary

The catalogue identifies this as a daylight sensor for a Room Controller, connected through RJ45. Its software model provides daylight reporting and regulation settings; exact physical specifications and setup instructions remain undocumented in the retained sources.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0062` | Project identity |
| Technical description | Daylight sensor for Room Controller + RJ45 | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSE3005`, `048828` | Canonical commercial records |
| Catalogue item | `57` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `40` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Daylight sensing, Lighting Management, Room Controller accessory | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSE3005` | Established identity | canonical commercial record for item `57` |
| Legrand | `048828` | Established identity | canonical commercial record for item `57` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite version history | software compatibility record | Document dated 2015-03-20; applicable product list under first release 1.0.45 dated 2013-10-10 | Printed/PDF p. 4; both exact references listed for virtual configuration; software compatibility only, not physical specifications or installed firmware | [Archived original](https://archive.openwebnet-ha.org/sha256/cd/c4/cdc467fa6408908a98348892c78a98439826b216197f7b17b4230da9f46554c3.pdf) | [Official compatibility source](https://myhomeswupdate.bticino.com/VersionHistory/Version_History_MyHOME_Suite_20150320.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Catalogue-established product role | daylight sensor for a Room Controller with RJ45 connection | Canonical item 57 |
| Physical ratings | Supply, consumption, enclosure, dimensions and optical/radio limits are not established by the retained compatibility list | Canonical item 57 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `57` | Canonical catalogue |
| Technical item | Daylight sensor for Room Controller + RJ45 | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `40` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `40` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `57` | `BMSE3005` | `1` | `5` | `BTicino_Undefined_Daylight sensor for Room Co` |
| `1582` | `048828` | `2` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `151` | `-1` | `-1` | `-1` | `1` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `151` | `1` | `164` Scenarios daylight sensor | Candidate alternative | `592` | `164` | `411` |
| `151` | `1` | `166` Stand alone daylight sensor | Candidate alternative | `591` | `166` | `410` |
| `151` | `1` | `194` Daylight cell | Fixed/designated metadata | `590` | `467` | `409` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `151` | `516` Daylight sensor virgin | `1` | `164`, `166`, `194` | `516` | `25` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `151` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `151` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `164` - Scenarios daylight sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |

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

### Object `194` - Daylight cell

Catalogue Object key `467` maps to external Object `194`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `GD` | `0..255` | `0` | Daylight sensor group |
| `DAYLIGHT_FACTOR` | `1..255` | `10` | Daylight factor |
| `DAYLIGHT_LEVEL` | `0..255` | `0` | Daylight level; Read only, just for IR commissionning |
| `SEND_CONDITION` | `0` = Sending cyclical or on request; `1` = Sending on request or on changing; `2` = Sending on request only; `3` = Sending cyclical or on request or on changing | `3` | Sending condition |
| `DEAD_BAND` | `1..100` | `10` | Deadband (between 1 and 100%); To define the on change sending |
| `TIME_BASE` | `1..59` | `5` | Time between two messages (minutes); Time_base_for_Cyclical_sending_(Minutes) |
| `LIMIT_NUMBER` | `0..255` | `60` | Number of messages per minute |

### Device-specific interpretation

Firmware `151` declares one Module with Objects 164, 166 and external 194 (catalogue key 467). Virgin `516` admits all three at slot `1`. Object `194` has empty condition `4145`; there are no M selectors or conversions. Firmware stores only `AID` and Advanced Configuration, so physical sockets and installed role are not inferred. Object `194` `DAYLIGHT_LEVEL=0..255` default 0 differs from `DAYLIGHT_FACTOR=1..255` default 10; `SEND_CONDITION=0` cyclic/request, 1 request/change, 2 request only, 3 all (default 3); `DEAD_BAND=1..100` default 10; `TIME_BASE=1..59` minutes default 5; `LIMIT_NUMBER=0..255` default 60. Object `166` has broader reusable regulation fields; setpoint default 100 encodes 500 lux. The filter description Provision of light references `DAYLIGHT_SETPOINT` and does not rename that field. Reusable schemas do not establish occupancy sensing.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `151` | `1` | `194` | `4145` | No textual predicate stored | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `151` | `166` | `2111` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `151` | `166` | `2126` | `NATURAL_LIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Natural light factor |
| `151` | `166` | `2141` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `151` | `166` | `2288` | `PROVISION_OF_LIGHT` | `0` = Automatic; `1..255` = `5 × stored value` lux (entire reusable range retained) | `0` | Provision of light (Lux) |
| `151` | `166` | `2317` | `DAYLIGHT_SETPOINT` | `0`; `1..255` = `5 × stored value` lux (entire reusable range retained) | `100` | Provision of light (Lux) |
| `151` | `194` | `363` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | `DAYLIGHT_LEVEL` |
| `151` | `194` | `364` | `DAYLIGHT_FACTOR` | `1..255` (entire reusable range retained) | `10` | `DAYLIGHT_FACTOR` |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `57` / `modobj = 40` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`164`, `166`, `194`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Software compatibility | `BMSE3005` and `048828` occur in the product list for first release 1.0.45 dated 10 October 2013 | Version_History_MyHOME_Suite_20150320, printed/PDF p. 4 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Resolve the active Module/Object and its catalogue restrictions before interpreting configuration. The only firmware-level field is `AID` and the only associated mode is Advanced Configuration; no exact retained instructions establish physical configurators or a commissioning sequence. Daylight cell 194 has reporting cadence, dead-band and sample-limit fields; their complete domains/defaults appear in Object configuration surfaces. These software settings do not establish calibrated lux accuracy or an occupancy detector.

## Source reconciliation

Both references explicitly map to the same technical item. The version history corroborates both exact references in its 1.0.45 product list (p. 4), not newly added support in the document’s 20 March 2015 release and not an installed 3.5.38 firmware. Exact-reference manufacturer searches and historical retained Spanish/German catalogues did not establish a technical sheet; the Italian exact-reference product export returned HTTP 500 on 6 October 2026. That endpoint failure is not evidence that a product or document never existed. Missing physical documentation does not make either identity unresolved.

Catalogue-specific scope, selectors, defaults and filter/conversion irregularities are detailed under [Object configuration surfaces](#object-configuration-surfaces). Those software relations do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- Exact-product physical specifications, factory settings and commissioning instructions remain a documentation gap.
- Optical range, accuracy, connector pinout and Room Controller compatibility are not independently established.
- No verified EAN is retained for either reference; adjacent sensor specifications are not imported.
- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0061-0070-2026-10-06.md#own-dev-0062)
