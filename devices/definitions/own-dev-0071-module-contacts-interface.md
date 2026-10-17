# Module contacts interface

## Summary

This one-module Living/Light/Light Tech contact interface connects two traditional dry-contact controls to the SCS bus. It can send independent lighting commands or pair the contacts for a shutter command; the retained catalogue represents the device with one diagnostic Module.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0071` | Project identity |
| Technical description | Module contacts interface | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `L/N/NT4688` | Canonical commercial records |
| Catalogue item | `80` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `150` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Automation, Contact interface, Flush-mounted | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - LivingLight | `L/N/NT4688` | Established identity | canonical commercial record for item `80` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MH_Guide_Automatisme.pdf` | technical/system guide | historical publisher guide | `L/N/NT4688` contact-interface construction and traditional-device integration; printed pp. 125–128, 161, 168 / PDF pp. 127–130, 163, 170 | [Archived original](https://archive.openwebnet-ha.org/sha256/80/6a/806a55bffb924f5ef7b25398432c0a86ab210722adc30b81f33558c6ec36f561.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MH_Guide_Automatisme.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Form factor | 1 flush-mounted Living International / Light / Light Tech module | MH_Guide_Automatisme.pdf, printed p. 168 / PDF p. 170 |
| Supply/current | `27 Vdc` bus context; `3.5 mA` | Same guide, printed p. 161 / PDF p. 163 |
| Inputs and wiring | Two dry-contact inputs; black COM, white PL1, grey PL2; LED and bus connector | Same guide, printed pp. 125–126 / PDF pp. 127–128 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `80` | Canonical catalogue |
| Technical item | Module contacts interface | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `150` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `150` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `80` | `L/N/NT4688` | `1` | `4` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `202` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `202` | `1` | `33` Interface contacts automation | Fixed/designated metadata | `1507` | `33` | `755` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `202` | Physical configuration | `0` | Canonical firmware/mode association |
| `202` | Virtual Configuration | `1` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `202` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `202` | `A` | `0..9` | `0` | A; Environment |
| `202` | `PL` | `0..9` | `0` | PL; Light Point |
| `202` | `M` | `0..9`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `15` = `PUL` | `0` | M; Mode physical configurator (0-9, `O/I`,`OFF`,`ON`,`PUL`) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `33` - Interface contacts automation

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..9` | `0` | Area |
| `PL` | `0..9` | `0` | Light point |

### Device-specific interpretation

Firmware `202` declares one Module with Object `33`, although the manufacturer describes two contact inputs. Do not turn the physical inputs into two invented diagnostic Modules. Object `33` has only `A` and `PL`; filter `1632` refers to `TYPE_CONTACT` defined in another Object scope, with no legal-value rows. This is an unresolved scope link, not evidence for adding a contact-type field to Object `33`. No Virgin, condition or conversion is associated. Firmware `M` stores numeric 9 alongside the O/I label, plus OFF/ON/PUL labels, but no shutter or SPE selector. The historical guide documents PL1/PL2, SPE and shutter commands; those product procedures are not a fuller firmware schema for this retained record.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `202` | `33` | `1632` | `TYPE_CONTACT` | No legal values specified in source (entire reusable range retained) | `0` | Contact type; field definition belongs to a different Object scope; do not alias it to a similarly named field |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `80` / `modobj = 150` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`33`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Independent/paired inputs | Separate PL1/PL2 controls two loads; equal PL1/PL2 pairs a double-function load | Guide, printed pp. 125–127 / PDF pp. 127–129 |
| Basic modes | Cyclic short press and long dimming; ON/OFF/PUL; O/I uses PL1 OFF and PL2 ON; grey raises and white lowers in shutter mode | Guide, printed p. 127 / PDF p. 129 |
| Timers and special modes | M `1..8`: 1, 2, 3, 4, 5, 15 minutes, 30 s, 0.5 s. SPE 1 lock/unlock and cyclic without dimming; 2 blink 0.5..5 s; 3 fixed dimming `10..90`%; 4 legacy central scenes; 6 `F420` scenes; 7 NC input; 8 timers 2 s/10 min | Guide, printed pp. 127–128 / PDF pp. 129–130 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Use the exact historical guide’s PL1/PL2 and SPE/M tables for product wiring and command roles. For switches it specifies PUL; other listed modes use normally open pushbuttons, with `SPE=7` for normally closed inputs. Paired loads require equal PL1/PL2. For `F420`, M=`1..8` chooses scene pairs 1/2 through 15/16, PL2 equal to PL1 or absent; contact closures under 3 s recall, `3..8` s enter learning and over 8 s delete. These procedures exceed the fields retained in firmware `202` and must not be turned into invented Objects. Evidence: guide printed pp. 125–128 / PDF pp. 127–130.

## Source reconciliation

The combined catalogue record `L/N/NT4688` and the historical guide establish the same one-module family. This is one commercial database row; `L4688`, `N4688` and `NT4688` are its named faceplate variants. The guide documents two physical inputs but the catalogue one Module, and documents a broader physical configuration surface than firmware `202`. Both scopes are preserved.

Catalogue interpretation is detailed under [Object configuration surfaces](#object-configuration-surfaces); these software records do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- The retained historical guide does not supply an exact current standalone sheet, operating-voltage range or environmental rating for every variant. No ratings are copied from `3477`.
- The two inputs have no independently retained runtime Module observation; the cross-Object TYPE_CONTACT filter link remains unresolved.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0071-0080-2026-10-06.md#own-dev-0071)
