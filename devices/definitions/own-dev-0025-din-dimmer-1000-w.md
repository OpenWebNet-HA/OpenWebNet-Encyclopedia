# DIN dimmer 1000 W

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0025` | Project identity |
| Technical description | One-channel DIN SCS dimmer for resistive and ferromagnetic-transformer loads | Catalogue + official technical sheet |
| Catalogue item / model | `17` / `modobj 133` | Implementation evidence |
| Firmware applicability | firmware `176`, `-1.-1.-1`, one slot | Implementation evidence |
| Commercial identities | `F414`, `003652` | Catalogue |
| Categories | Actuator, Dimmer, Lighting | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino / Undefined | `F414` | `17` | Commercial identity of this Technical Device | Canonical catalogue |
| Legrand / Undefined | `003652` | `1601` | Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Relevant pages | Status | Source |
| --- | --- | --- | --- | --- | --- |
| MQ00278_e_EN | Technical sheet | revision/date as printed | Whole document | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-f414-mq00278-e-en/MQ00278_e_EN.pdf) |
| AUTOMATISME.pdf | MyHOME automation guide | historical publisher guide | F414 family sections; exact printed/PDF locator pending | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) |

Multi-product guides retain an explicit page-location limitation until both printed and 1-based PDF page numbers are pinned.

## Physical and electrical characteristics

The official sheet establishes a one-output, 4-DIN dimmer for resistive loads and ferromagnetic transformers. Short control presses switch the load; long presses adjust brightness. The actuator can report load faults such as lamp failure and has a replaceable fuse. SCS nominal supply is `27 Vdc`, operating supply `18..27 Vdc`, current draw `9 mA`, and published F414 load range `0.25..4.3 A`, `60..1000 VA`.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `17` | Canonical catalogue |
| Technical item description | DIN dimmer 1000 W | Canonical catalogue |
| Item family | `4` - Dimmer | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `133` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Declared slots | Default | Status |
| ---: | ---: | ---: | ---: | --- | --- |
| `176` | `-1` | `-1` | `1` | `1` | `0` |

Firmware `176` is wildcard `-1.-1.-1` and declares one Module. Current F460/F461 compatibility documentation maps Legrand `003652` from production batch `09W50` and BTicino `F414` from `09W29`; MyHOME_Up documentation independently gives F414 `09W29`.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `176` | `422` | `8` | `8` | Dimmer actuator |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `608` | `1` | `8` | fixed | Dimmer actuator |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| - | - | - | - | No firmware-scoped Virgin Object | - | - |

One fixed Object `8`, Dimmer actuator, occupies slot `1`. There is no Virgin Object.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `176` | `1` | `1` | Virtual Configuration |
| `176` | `2` | `2` | Advanced Configuration |
| `176` | `3` | `0` | Physical configuration |

Physical configuration, Virtual Configuration and Advanced Configuration.

## Firmware-scoped configuration

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `AID` | ID | user_value | `********` - AID - range `0`..`0` - step `1` | visible=1, hidden=0, read-only=0, type-id=0 |
| `A` | A | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=1 |
| `PL` | PL | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=2 |
| `M` | M | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1`<br>`1` - 1 - range -..- - step `1`<br>`2` - 2 - range -..- - step `1`<br>`3` - 3 - range -..- - step `1`<br>`4` - 4 - range -..- - step `1`<br>`11` - SLA - range -..- - step `1`<br>`15` - PUL - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `G1` | G1 | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=3 |

Catalogue range rows are preserved directly; product-document physical configurator limits remain a distinct evidence layer.

`A`, `PL`, and `G1` are `0..9`; `M` permits default/`0..4`/`SLA`/`PUL`; `AID` is the identity field. MyHOME Suite identifies F414 as an inductive/halogen-capable dimmer with Master, delayed Slave, Master PUL and Slave PUL modes.

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

Object `8` supplies the reusable Dimmer-actuator model. Device-specific applicability is restricted by the documented load technology; F414 is not a generic modern multi-load dimmer.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `1` | Device/Firmware topology conditions |
| Object/Firmware filters | `9` | Conditional Object configuration exposure |
| Referenced conversion rules | `1` | `3` |

### Slot conditions

| Slot | Object | Condition ID | Condition expression | Conversion rule |
| ---: | ---: | ---: | --- | ---: |
| `1` | `8` | `4149` | No textual predicate - conversion-driven or unconditional catalogue row | `3` |

### Object/Firmware filters

| Object | Filter ID | Field | Note | Whole range | Filter ranges |
| ---: | ---: | --- | --- | --- | --- |
| `8` | `403` | `LOCAL_BUTTON` | FunzionalitÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â di pulsante locale ridotta (Local button mode) | `1` | - |
| `8` | `404` | `HOURS` | FunzionalitÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â di temporizzazione non presente (Hours) | `1` | - |
| `8` | `405` | `MINUTES` | FunzionalitÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â di temporizzazione non presente (Minutes) | `1` | - |
| `8` | `406` | `SECONDS` | FunzionalitÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â di temporizzazione non presente (Seconds) | `1` | - |
| `8` | `407` | `TYPE_LOAD` | TYPE_LOAD | `1` | - |
| `8` | `408` | `TYPE_STANDARD` | Definizione range voltaggio utile | `1` | - |
| `8` | `409` | `MIN_LEVEL_ADV` | Minimum level advanced | `1` | - |
| `8` | `410` | `MIN_AUTO` | enable disable minimum level | `1` | - |
| `8` | `2172` | `STATE_SAVING_ON_RESET` | State saving on reset | `1` | - |

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

The Device participates in [`WHO 1` - Lighting](../../functional/who-1-lighting/) as a dimmer actuator.

## Observed behavior and corroboration

No raw F414/MH200 DIM4 trace is retained; the tester report remains unresolved evidence.

## Programming

Preserve inductive/resistive load constraints and distinguish F414 from capacitive/electronic-transformer variants such as F415.

## Source reconciliation

The dedicated sheet establishes load type, electrical range, local button behavior, dimming interaction, fault indication and fuse behavior. The SCS guide corroborates `60..1000 VA`. MyHOME Suite confirms mode/load applicability. F460/F461 and MyHOME_Up documentation add production-batch boundaries. The remaining issue is runtime DIM4 behavior through MH200, not basic Device definition.

## Evidence limits and open work

- Preserve a raw F414/MH200 DIM4 request/timeout/`NACK` exchange.
- Hardware-corroborate `modobj`, firmware, address and configurator count.
- Archive historical sheet revisions when they materially change load/fuse data.
- Pin exact printed and 1-based PDF page locations for each applicable multi-product guide citation.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [MQ00278_e_EN](../../sources/devices/documents/device-doc-f414-mq00278-e-en/MQ00278_e_EN.pdf)
- [AUTOMATISME.pdf](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf)
