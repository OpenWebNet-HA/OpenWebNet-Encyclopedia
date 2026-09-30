# Four-scenario control unit

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0026` | Project identity |
| Technical description | Flush-mounted four-scenario control and storage unit | Catalogue + official automation guide |
| Catalogue item / model | `20` / `modobj 4` | Implementation evidence |
| Firmware applicability | firmware `223`, `-1.-1.-1`, one slot | Implementation evidence |
| Commercial identities | `N4681` | Catalogue |
| Categories | Scenario control, Automation | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino / L/N/NT | `N4681` | `20` | Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Relevant pages | Status | Source |
| --- | --- | --- | --- | --- | --- |
| AUTOMATISME.pdf | MyHOME automation guide | historical publisher guide | N4681 scenario-unit sections; exact printed/PDF locator pending | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) |

Multi-product guides retain an explicit page-location limitation until both printed and 1-based PDF page numbers are pinned.

## Physical and functional characteristics

N4681 exposes four scenario keys with indicator LEDs. The official guide states that previously stored command sequences are activated from those keys and may address actuators outside the unit's own room. Stored scenarios can be modified or deleted.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `20` | Canonical catalogue |
| Technical item description | Scenario control unit | Canonical catalogue |
| Item family | `19` - Scenarios controller and scheduler | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `4` | AS_ITEM_SYSTEM |
| Commercial records | `1` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Declared slots | Default | Status |
| ---: | ---: | ---: | ---: | --- | --- |
| `223` | `-1` | `-1` | `1` | `1` | `0` |

Firmware `223` has wildcard applicability `-1.-1.-1` and one Module slot. A sanitized hardware fingerprint remains pending.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `223` | `753` | `2` | `2` | 4 scenarios control unit |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `1505` | `1` | `2` | fixed | 4 scenarios control unit |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| - | - | - | - | No firmware-scoped Virgin Object | - | - |

The firmware resolves to Object `2`, **4 scenarios control unit**, with one slot. No Virgin Object is declared for this firmware.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `223` | `1` | `1` | Virtual Configuration |
| `223` | `3` | `0` | Physical configuration |

The catalogue declares Physical Configuration and Virtual Configuration.

## Firmware-scoped configuration

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `AID` | ID | user_value | `********` - AID - range `0`..`0` - step `1` | visible=1, hidden=0, read-only=0, type-id=0 |
| `A` | A | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=1 |
| `PL` | PL | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=2 |

Catalogue range rows are preserved directly; product-document physical configurator limits remain a distinct evidence layer.

The firmware exposes `A`, `PL` and `AID`. The Object surface adds `SCE1` through `SCE4` for the four scenario definitions.

The official guide documents two physical addressing modes. With only `PL = 1..9`, the number identifies the scenario unit and activation does not first send OFF commands. With `A` and `PL` populated, they form the unit address; scenario activation first resets actuators in the configured room before applying the scenario.

## Object configuration surfaces

### Object `2` - 4 scenarios control unit

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `A` | Area | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=1 |
| `PL` | Light point | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=2 |
| `SCE1` | Scenario 1 | Fixed_Value | `_` - SCE1 - range -..- - step `1` - default marker `_` | visible=1, hidden=0, read-only=, type-id= |
| `SCE2` | Scenario 2 | Fixed_Value | `_` - SCE2 - range -..- - step `1` - default marker `_` | visible=1, hidden=0, read-only=, type-id= |
| `SCE3` | Scenario 3 | Fixed_Value | `_` - SCE3 - range -..- - step `1` - default marker `_` | visible=1, hidden=0, read-only=, type-id= |
| `SCE4` | Scenario 4 | Fixed_Value | `_` - SCE4 - range -..- - step `1` - default marker `_` | visible=1, hidden=0, read-only=, type-id= |

Object `2` owns the four scenario fields. The scenario payload semantics belong to the reusable scenario-control Object rather than four independent Modules.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `0` | Device/Firmware topology conditions |
| Object/Firmware filters | `1` | Conditional Object configuration exposure |
| Referenced conversion rules | `0` | None |

### Object/Firmware filters

| Object | Filter ID | Field | Note | Whole range | Filter ranges |
| ---: | ---: | --- | --- | --- | --- |
| `2` | `1630` | `TYPE_CONTACT` | Contact type | `1` | - |

Generic condition/conversion evaluation remains canonical in [Catalogue Resolution](../../internals/catalogue-resolution.md); these tables preserve this Device's exact applicability records.

## Diagnostic applicability

| Surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | Identify the Device model/family and compare it with catalogue identity. | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Record installed firmware instead of treating wildcard catalogue applicability as an observed version. | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve Module/Object topology, especially when candidates share a slot. | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Inspect addressing for the resolved Module/Object when exposed. | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Corroborate firmware/Object configuration and physical/software relationships. | [Configuration](../../diagnostics/dim35-configuration.md) |

Catalogue applicability is not itself an observed runtime result.

## Functional applicability

The Device is a scenario-control endpoint. Scenario actions can target multiple functional domains; they must not be reduced to the Device's own `A/PL` address.

## Observed behavior and corroboration

No sanitized hardware capture for this exact Device is currently retained.

## Programming

Preserve the distinction between the `PL`-only mode and the `A + PL` room-reset mode. The official guide explicitly notes that the latter cannot manage scenarios by activating L4674 dimmer actuators.

## Source reconciliation

The canonical database and archived official automation guide agree on the one-slot four-scenario topology and physical addressing. The guide supplies the behavior that the database alone cannot express: four stored scenarios and the two activation/reset modes.

## Evidence limits and open work

- Add a sanitized N4681 hardware fingerprint.
- Corroborate scenario programming frames from first-hand traffic.
- Preserve the documented L4674 limitation as revision-scoped behavior.
- Pin exact printed and 1-based PDF page locations for each applicable multi-product guide citation.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf)
