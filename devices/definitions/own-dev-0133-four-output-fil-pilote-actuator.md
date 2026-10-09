# Four-output Fil Pilote actuator

## Summary

This four-output Fil Pilote actuator sends pilot-wire operating signals to compatible heating devices. Each output can serve up to ten documented receivers within its signal-current limit, with local buttons toggling between comfort operation and off.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0133` | Project identity |
| Technical description | Four-output Fil Pilote actuator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `003577`, `F430FP` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1463` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Temperature control | Main system association |
| Item model / `modobj` | `1` | Main association; independent of project ID |
| Firmware definition | `221` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `4` | Firmware metadata |
| Categories | Actuators, Thermoregulation | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `003577` | Established catalogue identity | Manufacturer database commercial record `1463` explicitly links this SKU to item `1463` |
| BTicino | `F430FP` | Established catalogue identity | Manufacturer database commercial record `2007` explicitly links this SKU to item `1463` |

### Catalogue labels and classifications

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `003577` | Actuator DIN with 4 fil pilote outputs bus | Canonical commercial record `1463` |
| `F430FP` | Actuator DIN with 4 fil pilote outputs bus | Canonical commercial record `2007` |

Both commercial records are enabled for catalogue display, have no visibility-type value, and are not marked dependent or gateway in this historical commercial table. These classifications do not establish market availability, installed state or functional gateway capability. Empty or truncated internal description labels are not used to infer additional product features.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `O1866B.pdf` | Fil pilote instructions | `O1866B-01PC-12W48` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-1; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/f1/02/f10259b0ed57f94f32afec0d2bde00ba022c5f3808868de7f12eab8ed2ff1e1f.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/O1866B.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `1463` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mains | `230 Vac; 50 Hz` | `O1866B-01PC-12W48`, PDF p. 1; no printed page number |
| SCS supply | `18..27 Vdc` | `O1866B-01PC-12W48`, PDF p. 1; no printed page number |
| Maximum bus draw | `20 mA` | `O1866B-01PC-12W48`, PDF p. 1; no printed page number |
| Outputs | `4 Fil Pilote outputs; <=25 mA each` | `O1866B-01PC-12W48`, PDF p. 1; no printed page number |
| Per-output capacity | `maximum 10 Fil Pilote devices` | `O1866B-01PC-12W48`, PDF p. 1; no printed page number |
| Operating temperature | `5..45 °C` | `O1866B-01PC-12W48`, PDF p. 1; no printed page number |
| Local control | `OFF toggles to Comfort; any other state toggles to OFF` | `O1866B-01PC-12W48`, PDF p. 1; no printed page number |
| Indicators | `output LED off: OFF; on: other states` | `O1866B-01PC-12W48`, PDF p. 1; no printed page number |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1463` | Canonical catalogue |
| Technical item description | Actuator DIN with 4 fil pilote outputs bus | Canonical catalogue |
| Item family | 0; key `2` | Canonical catalogue |
| Main system | Temperature control; key `2` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `1` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Temperature control | `1` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `221` | `-1` | `-1` | `-1` | `4` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `221` | `1` | `214` Fil-Pilote actuator | Fixed/designated metadata | `1005` | `498` | `605` |
| `221` | `2` | `214` Fil-Pilote actuator | Fixed/designated metadata | `1006` | `498` | `605` |
| `221` | `3` | `214` Fil-Pilote actuator | Fixed/designated metadata | `1007` | `498` | `605` |
| `221` | `4` | `214` Fil-Pilote actuator | Fixed/designated metadata | `1008` | `498` | `605` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `221` | Physical configuration | `0` | Canonical firmware/mode association |
| `221` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `221` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `221` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `221` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `221` | `ZB1` | `0..9`; `10` = `OFF` | `0` | ZB1; ZB1 thermo Actuator zone address |
| `221` | `ZB2` | `0..9`; `10` = `OFF` | `0` | ZB2; ZB2 thermo Actuator zone address |
| `221` | `ZB3` | `0..9`; `10` = `OFF` | `0` | ZB3; ZB3 thermo Actuator zone address |
| `221` | `ZB4` | `0..9`; `10` = `OFF` | `0` | ZB4; ZB4 thermo Actuator zone address |
| `221` | `N` | `0..9` | `0` | N; Thermoregulation zone device number N |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `214` - Fil-Pilote actuator

Catalogue Object key `498` maps to external Object `214`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `1..9` | `1` | Zone device number; Zone device number N |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | Not applicable | None | Not applicable | No relation-specific filters associated | Not applicable | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `1` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `214` - Fil-Pilote actuator | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |

These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Assign the zone address for each Fil Pilote output separately from the common actuator address/selectors. Any output button can identify the unit for virtual configuration. Local buttons toggle Comfort/`OFF` as described in the exact instruction; they do not select every reusable Object mode. The pilot wires are signaling outputs, not four switched heater-power relays. Validate the per-output 25 mA/ten-device limit and preserve the separate 230 V line/SCS connections.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

O1866B PDF p. 1 defines each local button precisely: OFF becomes Comfort; any other operating state becomes OFF. The corresponding LED is unlit in OFF and lit in the other states. Any button can identify the device during virtual configuration. Its wiring diagram separates the 230 Vac L/N supply, four pilot outputs and SCS bus; the pilot output is not the heater's power feed.

## Source reconciliation

003577 and F430FP are explicit catalogue identities. The exact French instruction supplies electrical limits and local behavior. Four Object `214` placements agree with four output zones, but the instruction does not supply every Suite field’s encoding, physical selector domain or Fil Pilote waveform. A technical-item model number must not be used as the functional system WHO.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `O1866B.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |

### Semantic review findings

Four fixed FilPilote Object `214` placements describe four pilot-wire signal outputs; they are not four mains power relays. The leaflet supplies `25 mA` per output and a maximum of ten FilPilote devices per output. It states that pressing a local button selects Comfort only from OFF, and selects OFF from every other state; a simple Comfort/OFF toggle omits that distinction. Firmware `ZA=0..9`, `ZB=1..4`, `N=0..9` with default `0` is distinct from each reusable Object's `ZA/ZB=01..99` and `N=1..9`, default `1`. No Virgin, condition, conversion or filter explains the mapping. Neither zone `00` nor firmware `N=0` is silently transferred into the reusable Object domain. Exact `003577` instructions, pilot-waveform details and the physical selector interpretation remain documentation gaps within established identity.

## Evidence limits and open work

Complete physical selector/commissioning tables, exact 003577 manual, Fil Pilote waveform mapping and installed thermostat/diagnostic behavior remain documentation or capture gaps.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0131-0140-2026-10-06.md#own-dev-0133)
