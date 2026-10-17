# SCS and ZigBee gateway

## Summary

This gateway links the wired SCS lighting system to a manufacturer-profile ZigBee radio network. The exact Legrand 048832 leaflet documents a 27 Vdc BUS connection, false-ceiling mounting and separate network and Push&Learn commissioning; BMNE4000 shares its catalogue item, with exact hardware documentation still absent.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0125` | Project identity |
| Technical description | SCS and ZigBee gateway | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `048832`, `BMNE4000` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1169` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `202` | Main association; independent of project ID |
| Firmware definition | `376` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Gateways and interfaces | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `048832` | Established catalogue identity | Manufacturer database commercial record `1786` explicitly links this SKU to item `1169` |
| BTicino | `BMNE4000` | Established catalogue identity | Manufacturer database commercial record `1923` explicitly links this SKU to item `1169` |

### Complete catalogue commercial metadata

| Record | Reference | Catalogue name | Brand key | Line key | Visible | Visibility type | Dependent | Gateway | Catalogue description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `1786` | `048832` | `Gateway SCS / ZIGBEE` | `2` | `5` | `1` | `` | `0` | `0` | `` |
| `1923` | `BMNE4000` | `Gateway SCS / ZIGBEE` | `1` | `5` | `1` | `` | `0` | `0` | `BTicino_Undefined_Gateway SCS / ZIGBEE` |

Empty catalogue values are retained as empty metadata; none is an installed-state or market-availability observation.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `1169` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |
| `LE05133AA.pdf` | Exact Legrand 048832 installation/commissioning leaflet | LE05133AA; no explicit publication date established | All eight PDF pages examined: exact 048832 cover, 27 Vdc, radio/profile/range and temperature; p. 2 mounting/BUS topology/LEDs; p. 3 network; pp. 4–7 direction-specific Push&Learn and peripheral deletion; p. 8 safety. Other commercial reference BMNE4000 not named. | [Archived original](https://archive.openwebnet-ha.org/sha256/6e/e1/6ee11e2bd386a9b3506ef1e48a5846874dec6f0109f70971bb3d7caa6e4130c8.pdf) | [Publisher source](https://assets.legrand.com/general/mediagrp/np-ft-gt/le05133aa.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Documented hardware scope | Legrand 048832 only | LE05133AA PDF p. 1 |
| Supply | `27 Vdc` | LE05133AA PDF pp. 1–2; BUS/SCS RJ45, not Ethernet |
| Operating temperature | `5..45 °C` | LE05133AA PDF p. 1 |
| Radio | `2.4 GHz` | LE05133AA PDF p. 1; ZigBee certified mesh, manufacturer-specific profile stated in French |
| Open-field range | English/most cover languages: approximately `150 m`; Chinese: `100 m` | LE05133AA PDF p. 1 translation discrepancy; no universal installed range inferred |
| Mounting | False ceiling, screw fixing and connector cover | LE05133AA PDF p. 2 |
| SCS run | A≤`250 m` (branch to gateway); A+B≤`500 m` (complete illustrated run) | LE05133AA PDF p. 2 diagram |
| Gateway count | One 048832 on the illustrated SCS topology; second crossed out | LE05133AA PDF p. 2; not extrapolated to every isolated bus segment |
| Current / dimensions / learning capacity | Not numerically specified in the examined leaflet | Full-table indication is documented without a number of entries |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1169` | Canonical catalogue |
| Technical item description | Gateway SCS / ZIGBEE | Canonical catalogue |
| Item family | 0; key `100` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `202` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `202` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `376` | `-1` | `-1` | `-1` | `1` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `376` | `1` | `193` Gateway SCS-ZigBee | Fixed/designated metadata | `990` | `465` | `596` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `376` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.


### Manufacturer commissioning scope

LE05133AA p. 3 requires radio-network creation/joining before Push&Learn and a five-second wait after closing the network. The illustrated NETWORK creation hold is three seconds; the ten-second network-removal hold belongs to the illustrated radio peripheral, not a documented gateway factory reset. Multiple open networks produce the illustrated three-second flash/retry indication. These procedures do not change the catalogue’s sole Advanced Configuration association.

Push&Learn pp. 4–5 pairs a ZigBee control to SCS recipients; pp. 6–7 pairs SCS group/scenario controls to ZigBee loads. The first ZigBee learn indication takes four seconds, with subsequent selection within ten seconds; the illustrated recipient-selection phase allows up to ten minutes. The completion/recipient interaction differs by direction, so follow the appropriate original sequence. Ten-second deletion drawings concern the depicted peripheral/control associations and are not a universal gateway reset. Traffic means SCS/radio exchanges, Identify means identification active, and Full table is a five-second notification. No generic ZigBee-brand interoperability or unlimited association count is established.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `376` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `193` - Gateway SCS-ZigBee

Catalogue Object key `465` maps to external Object `193`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `MODE` | `0` = SCS2; `1` = SCS1 | `0` | Mode for SCS-Zigbee |

### Semantic review findings

Firmware `376` is wildcard/default and Deprecated in this retained historical catalogue, with one placement of Object `193` (database key `465`) and no Virgin association. AID is its sole firmware field. Object A `0..10`/PL `0..15` are reusable software addresses, not an inferred physical configurator bay. MODE has reusable `0` (SCS2, default) and `1` (SCS1); relation filter `1102` allows only `1`, excluding default `0` without supplying a replacement. Preserve that inconsistency; SCS1/SCS2 labels alone do not identify protocol versions. No slot conditions, conversions, connections, parameters or packages are stored. The exact 048832 leaflet establishes BUS/SCS over RJ45 and a manufacturer-profile ZigBee radio; RJ45 does not mean Ethernet, and catalogue equivalence does not automatically transfer the leaflet’s physical properties to unexamined BMNE4000 hardware.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `376` | `193` | `1102` | `MODE` | `1` = SCS1 | `0` | Mode for SCS-Zigbee; reusable default `0` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `202` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Read installed firmware and compare with the applicability table | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Obtain hardware revision; no source-backed installed value | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Obtain microcontroller identity; no fingerprint retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve active Modules/Objects independently of candidate metadata | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Corroborate installed addressing and distinguish physical from reusable ranges | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Compare installed configuration with the exact firmware/Object restrictions | [Configuration](../../diagnostics/dim35-configuration.md) |

These are catalogue-derived diagnostic candidates. No Device-specific response or support across all commercial variants is established by a hardware capture.

## Functional applicability

| Catalogue Object / role | Applicability | Evidence |
| --- | --- | --- |
| `193` - Gateway SCS-ZigBee | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |

These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The database places gateway Object `193` in slot `1`. Validate its addressing and apply the attached restriction `MODE=1` (SCS1); reusable `MODE=0` (SCS2) is outside that subset and no replacement default is supplied. Resolve actual SCS/ZigBee topology before treating a downstream radio device as this gateway’s own Physical Device identity.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

## Source reconciliation

The manufacturer catalogue explicitly links 048832 and BMNE4000 to item 1169. The exact 048832 LE05133AA leaflet now establishes mounting, wired/radio interfaces and commissioning within that SKU scope; no applicable BMNE4000 hardware original was obtained. The cover’s approximately 150 m English range differs from the Chinese 100 m statement; installation-dependent radio range is not resolved by choosing one translation. The French cover specifies a manufacturer profile, so ZigBee certification alone is not generic interoperability evidence. LED flashing legends differ between the pp. 4/5 examples (60/200 ms versus 60/60 ms); no unified timing is inferred. Historical catalogue MODE default 0 versus filter-only 1 remains a separate unresolved metadata inconsistency.

A discovered MQ00410-c-EN document concerns flush-mounted L/N/NT4578N, 067250 and HD/HC/HS4578, not these SKUs; its 20 mA, two-module and 32-device specifications are excluded. The French Céliane radio guide likewise did not establish an applicable 048832/BMNE4000 specification. Deprecated status and wildcard firmware do not establish present-day availability or installed state.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `LE05133AA.pdf` | Exact 048832 installation, radio/BUS topology and commissioning; language/range/timing discrepancies retained. BMNE4000 hardware applicability remains uncorroborated. |

## Evidence limits and open work

Exact BMNE4000 hardware documentation, a stated gateway current/dimension/association-capacity specification, manufacturer clarification of language/timing discrepancies, gateway-specific factory reset and installed diagnostic/radio captures remain gaps. Exact 048832 identity, supply, mounting and commissioning are now documented.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0121-0130-2026-10-06.md#own-dev-0125)
