# Ballast DIN dimmer 1-10 V

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0030` | Project identity |
| Technical description | DIN-rail 1-10 V ballast dimmer | Catalogue + official family documentation |
| Catalogue item / model | `31` / `modobj 7` | Implementation evidence |
| Firmware applicability | firmware `174`, `-1.-1.-1`, one slot | Implementation evidence |
| Commercial identities | `F413` | Catalogue |
| Categories | Dimmer, Lighting | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino / Undefined | `F413` | `31` | Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Relevant pages | Status | Source |
| --- | --- | --- | --- | --- | --- |
| AUTOMATISME.pdf | MyHOME automation guide | historical publisher guide | F413 ballast-dimmer sections; exact printed/PDF locator pending | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) |

Multi-product guides retain an explicit page-location limitation until both printed and 1-based PDF page numbers are pinned.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `31` | Canonical catalogue |
| Technical item description | Ballast DIN dimmer 1-10 V | Canonical catalogue |
| Item family | `4` - Dimmer | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `7` | AS_ITEM_SYSTEM |
| Commercial records | `1` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Declared slots | Default | Status |
| ---: | ---: | ---: | ---: | --- | --- |
| `174` | `-1` | `-1` | `1` | `1` | `0` |

Firmware `174` is wildcard `-1.-1.-1` and declares one Module.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `174` | `420` | `8` | `8` | Dimmer actuator |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `606` | `1` | `8` | fixed | Dimmer actuator |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| - | - | - | - | No firmware-scoped Virgin Object | - | - |

The Module resolves to Object `8`, **Dimmer actuator**. The catalogue records one Virgin-Object relationship for this technical item through the shared dimmer model.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `174` | `1` | `1` | Virtual Configuration |
| `174` | `2` | `2` | Advanced Configuration |
| `174` | `3` | `0` | Physical configuration |

Advanced Configuration, Physical Configuration and Virtual Configuration are declared.

## Firmware-scoped configuration

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `AID` | ID | user_value | `********` - AID - range `0`..`0` - step `1` | visible=1, hidden=0, read-only=0, type-id=0 |
| `A` | A | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=1 |
| `PL` | PL | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=2 |
| `M` | M | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1`<br>`1` - 1 - range -..- - step `1`<br>`2` - 2 - range -..- - step `1`<br>`3` - 3 - range -..- - step `1`<br>`4` - 4 - range -..- - step `1`<br>`11` - SLA - range -..- - step `1`<br>`15` - PUL - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `G1` | G1 | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=3 |

Catalogue range rows are preserved directly; product-document physical configurator limits remain a distinct evidence layer.

Firmware `174` exposes `A`, `PL`, `M`, `G1` and `AID`. Its `M` description uses the classic `1..4`, `PUL`, `SLA` mode family. Object `8` also provides the reusable dimmer parameter surface, but firmware applicability must be evaluated before exposing newer load-type/minimum-level fields.

## Object configuration surfaces

### Object `8` - Dimmer actuator

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `A` | Area | Range | range `0`..`10` - step `1` | visible=1, hidden=0, read-only=, type-id=1 |
| `PL` | Light point | Range | range `0`..`15` - step `1` | visible=1, hidden=0, read-only=, type-id=2 |
| `M` | Modality | Enum | range -..- - step `1`<br>`0` - Master - range -..- - step `1`<br>`11` - Slave - range -..- - step `1`<br>`15` - Master PUL - range -..- - step `1`<br>`16` - Slave and PUL - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `LOCAL_BUTTON` | Local button modality | Enum | range -..- - step `1`<br>`0` - Toggle - range -..- - step `1`<br>`9` - ON - OFF - range -..- - step `1`<br>`15` - Pushbutton - range -..- - step `1`<br>`18` - Timed ON - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `DELAYED_OFF` | Delayed OFF for Slave (s) | Range | range `0`..`255` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `STATE_SAVING_ON_RESET` | State saving on reset | Boolean | range -..- - step `1`<br>`0` - Disabled - range -..- - step `1`<br>`1` - Enabled - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `HOURS` | Hours | Range | range `0`..`255` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `MINUTES` | Minutes | Range | range `0`..`59` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `SECONDS` | Seconds | Range | range `0`..`59` - step `1` - default marker `30` | visible=1, hidden=1, read-only=, type-id= |
| `MIN_LEVEL` | Minimum level | Range | range `1`..`100` - step `1` - default marker `1` | visible=1, hidden=0, read-only=, type-id= |
| `TYPE_LOAD` | Type of load | Enum | range -..- - step `1`<br>`0` - Auto detect capacitive - range -..- - step `1`<br>`1` - Auto detect inductive - range -..- - step `1`<br>`2` - Forced capacitive - range -..- - step `1`<br>`3` - Forced inductive - range -..- - step `1`<br>`5` - Fluorescent lamps - range -..- - step `1`<br>`6` - Led lamps - range -..- - step `1`<br>`7` - Discharge lamps - range -..- - step `1`<br>`8` - Dali standard - range -..- - step `1`<br>`9` - DSI - range -..- - step `1`<br>`10` - Halogen lamp - range -..- - step `1`<br>`11` - LED trailing edge / electronic transformers - range -..- - step `1`<br>`12` - LED leading edge - range -..- - step `1`<br>`13` - CFL trailing edge - range -..- - step `1`<br>`14` - CFL leading edge - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `TYPE_STANDARD` | Voltage standard | Enum | range -..- - step `1`<br>`0` - 1-10V standard - range -..- - step `1`<br>`1` - 0-10V standard - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `MIN_LEVEL_ADV` | Minimum level advanced | Range | range `1`..`100` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `MIN_AUTO` | Enable / Disable minimum level | Boolean | range -..- - step `1`<br>`0` - Minimum not editable - range -..- - step `1`<br>`1` - Minimum editable - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `G1` | Group 1 | Range | range `0`..`255` - step `1` | visible=1, hidden=0, read-only=, type-id=3 |
| `G2` | Group 2 | Range | range `0`..`255` - step `1` | visible=1, hidden=0, read-only=, type-id=3 |
| `G3` | Group 3 | Range | range `0`..`255` - step `1` | visible=1, hidden=0, read-only=, type-id=3 |
| `G4` | Group 4 | Range | range `0`..`255` - step `1` | visible=1, hidden=0, read-only=, type-id=3 |
| `G5` | Group 5 | Range | range `0`..`255` - step `1` | visible=1, hidden=0, read-only=, type-id=3 |
| `G6` | Group 6 | Range | range `0`..`255` - step `1` | visible=1, hidden=0, read-only=, type-id=3 |
| `G7` | Group 7 | Range | range `0`..`255` - step `1` | visible=1, hidden=0, read-only=, type-id=3 |
| `G8` | Group 8 | Range | range `0`..`255` - step `1` | visible=1, hidden=0, read-only=, type-id=3 |
| `G9` | Group 9 | Range | range `0`..`255` - step `1` | visible=1, hidden=0, read-only=, type-id=3 |
| `G10` | Group 10 | Range | range `0`..`255` - step `1` | visible=1, hidden=0, read-only=, type-id=3 |

The Device is one addressed Dimmer actuator Module. The shared Object surface must not be mistaken for proof that every later dimmer feature exists on F413.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `1` | Device/Firmware topology conditions |
| Object/Firmware filters | `4` | Conditional Object configuration exposure |
| Referenced conversion rules | `1` | `3` |

### Slot conditions

| Slot | Object | Condition ID | Condition expression | Conversion rule |
| ---: | ---: | ---: | --- | ---: |
| `1` | `8` | `4149` | No textual predicate - conversion-driven or unconditional catalogue row | `3` |

### Object/Firmware filters

| Object | Filter ID | Field | Note | Whole range | Filter ranges |
| ---: | ---: | --- | --- | --- | --- |
| `8` | `393` | `MIN_LEVEL_ADV` | Minimum level advanced | `1` | - |
| `8` | `394` | `MIN_AUTO` | enable disable minimum level | `1` | - |
| `8` | `395` | `TYPE_LOAD` | Type of Load | `0` | `0` - Auto detect capacitive<br>`1` - Auto detect inductive<br>`10` - Alogen lamp<br>`11` - LED trailing edge / electronic transformers<br>`12` - LED leading edge<br>`13` - CFL trailing edge<br>`14` - CFL leading edge<br>`2` - Forced capacitive<br>`3` - Forced inductive<br>`7` - Discharge lamps<br>`8` - Dali standard<br>`9` - DSI |
| `8` | `2170` | `STATE_SAVING_ON_RESET` | State saving on reset | `1` | - |

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

The Device participates in [`WHO 1` - Lighting](../../functional/who-1-lighting/), with dimming applied through its 1-10 V ballast-control role.

## Observed behavior and corroboration

No sanitized F413 hardware fingerprint is currently retained.

## Programming

Preserve the classic `M` mode and group semantics. Do not substitute current F413N electrical specifications or configuration behavior unless the hardware identity has been established.

## Source reconciliation

The canonical database establishes F413 as a one-slot Dimmer actuator with physical, virtual and advanced configuration. Publisher material confirms the 1-10 V family role, while the currently published F413N material represents a later/current reference. The dossier therefore keeps historical F413 identity separate from successor specifications.

## Evidence limits and open work

- Recover and archive a publisher-original F413-specific technical sheet.
- Resolve the recorded condition and conversion rule into human-readable behavior.
- Add a sanitized hardware fingerprint and establish F413 versus F413N revision continuity.
- Pin exact printed and 1-based PDF page locations for each applicable multi-product guide citation.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf)
