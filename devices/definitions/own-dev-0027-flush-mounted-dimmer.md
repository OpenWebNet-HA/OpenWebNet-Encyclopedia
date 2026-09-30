# Flush-mounted dimmer

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0027` | Project identity |
| Technical description | Flush-mounted SCS dimmer actuator | Catalogue + official automation documentation |
| Catalogue item / model | `23` / `modobj 5` | Implementation evidence |
| Firmware applicability | firmware `198`, `-1.-1.-1`, one slot | Implementation evidence |
| Commercial identities | `H4674`, `L/N/NT4674` | Catalogue |
| Categories | Dimmer, Lighting | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino / L/N/NT | `L/N/NT4674` | `23` | Commercial identity of this Technical Device | Canonical catalogue |
| BTicino / Axolute | `H4674` | `1731` | Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Relevant pages | Status | Source |
| --- | --- | --- | --- | --- | --- |
| AUTOMATISME.pdf | MyHOME automation guide | historical publisher guide | 4674 dimmer-family sections; exact printed/PDF locator pending | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) |

Multi-product guides retain an explicit page-location limitation until both printed and 1-based PDF page numbers are pinned.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `23` | Canonical catalogue |
| Technical item description | Flush mounted dimmer | Canonical catalogue |
| Item family | `4` - Dimmer | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `5` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Declared slots | Default | Status |
| ---: | ---: | ---: | ---: | --- | --- |
| `198` | `-1` | `-1` | `1` | `1` | `0` |

Firmware `198` is wildcard `-1.-1.-1` and declares one Module. Installed hardware remains to be corroborated.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `198` | `463` | `8` | `8` | Dimmer actuator |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `668` | `1` | `8` | fixed | Dimmer actuator |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| - | - | - | - | No firmware-scoped Virgin Object | - | - |

The single Module resolves to Object `8`, **Dimmer actuator**. Object `8` is also associated with Virgin Object `532` elsewhere in the catalogue; this firmware itself has no Device-specific Virgin Object row.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `198` | `1` | `1` | Virtual Configuration |
| `198` | `3` | `0` | Physical configuration |

Physical Configuration and Virtual Configuration are declared.

## Firmware-scoped configuration

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `AID` | ID | user_value | `********` - AID - range `0`..`0` - step `1` | visible=1, hidden=0, read-only=0, type-id=0 |
| `A` | A | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=1 |
| `PL` | PL | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=2 |
| `M` | M | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1`<br>`9` - O/I - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `G1` | G1 | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=3 |

Catalogue range rows are preserved directly; product-document physical configurator limits remain a distinct evidence layer.

Firmware `198` exposes `A`, `PL`, `M`, `G1` and `AID`. Its firmware description constrains `M` to the documented dimmer mode family `0` / `I/O`. The reusable Dimmer actuator Object also contains local-button, delayed-off, state-saving, minimum-level, load-type and group fields; those generic fields must only be applied when permitted by this Device's firmware/configuration path.

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

Object `8` is the reusable dimmer surface. The database records one condition for this technical item, so configuration consumers must evaluate the catalogue condition rather than assuming every generic Object field is active.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `1` | Device/Firmware topology conditions |
| Object/Firmware filters | `4` | Conditional Object configuration exposure |
| Referenced conversion rules | `0` | None |

### Slot conditions

| Slot | Object | Condition ID | Condition expression | Conversion rule |
| ---: | ---: | ---: | --- | ---: |
| `1` | `8` | `4145` | No textual predicate - conversion-driven or unconditional catalogue row | - |

### Object/Firmware filters

| Object | Filter ID | Field | Note | Whole range | Filter ranges |
| ---: | ---: | --- | --- | --- | --- |
| `8` | `594` | `MIN_LEVEL_ADV` | Minimum level advanced | `1` | - |
| `8` | `595` | `MIN_AUTO` | enable disable minimum level | `1` | - |
| `8` | `596` | `TYPE_LOAD` | Type of Load | `0` | `1` - Auto detect inductive<br>`11` - LED trailing edge / electronic transformers<br>`12` - LED leading edge<br>`2` - Forced capacitive<br>`3` - Forced inductive<br>`7` - Discharge lamps<br>`8` - Dali standard<br>`9` - DSI |
| `8` | `2180` | `STATE_SAVING_ON_RESET` | State saving on reset | `1` | - |

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

The Device participates in [`WHO 1` - Lighting](../../functional/who-1-lighting/).

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact item is currently retained.

## Programming

Treat the product as one addressed dimmer Module. Do not infer modern universal-dimmer load-selection semantics merely because they exist on the shared Object `8` surface.

## Source reconciliation

The catalogue establishes one Dimmer actuator Module and the two commercial identities. The archived automation documentation corroborates the 4674 family role. Shared Object `8` contains fields used by newer dimmers as well, so this dossier deliberately distinguishes Object capability from firmware-applicable configuration.

## Evidence limits and open work

- Recover and archive a dedicated H4674/L4674 technical-sheet revision if a publisher original is located.
- Add a sanitized hardware fingerprint.
- Resolve the single catalogue condition into a human-readable Device-specific rule.
- Pin exact printed and 1-based PDF page locations for each applicable multi-product guide citation.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf)
