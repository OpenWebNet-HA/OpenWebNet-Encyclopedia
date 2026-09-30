# Four-relay DIN actuator

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0023` | Project identity |
| Technical description | Four-independent-relay 2-DIN actuator for lighting and paired automation/motor loads | Catalogue + official documentation |
| Catalogue item / model | `3` / `modobj 130` | Implementation evidence |
| Firmware applicability | firmware `142`, `-1.-1.-1`, four slots | Implementation evidence |
| Commercial identities | `F411/4`, `003844` | Catalogue |
| Categories | Actuator, Lighting, Automation, Shutter | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino / Undefined | `F411/4` | `3` | Commercial identity of this Technical Device | Canonical catalogue |
| Legrand / Undefined | `003844` | `1707` | Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Relevant pages | Status | Source |
| --- | --- | --- | --- | --- | --- |
| ST-00000896-EN | Technical sheet | 2021-03-23 | PDF pp. 1-4 | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-f411-4-st00000896-en/ST-00000896-EN.pdf) |
| AUTOMATISME.pdf | MyHOME automation guide | historical publisher guide | F411/4 family sections; exact printed/PDF locator pending | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) |

Multi-product guides retain an explicit page-location limitation until both printed and 1-based PDF page numbers are pinned.

## Physical and electrical characteristics

Current product data describes four independent relays in two DIN modules, local/manual operation, LED indication, `27 Vdc` nominal supply, `40 mA` input current and `18..27 V` operation. Current load data includes `2 A` rated switching, `500 W` motor reducers, `2 A cosφ 0.5` ferromagnetic transformers and `70 W` fluorescent loads. The technical sheet shows a `10 A` protective breaker for its lighting example and paired motor/shutter wiring. Relays can be logically interlocked.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `3` | Canonical catalogue |
| Technical item description | 4 relay actuator 2 modules DIN bus | Canonical catalogue |
| Item family | `2` - Actuator | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `130` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Declared slots | Default | Status |
| ---: | ---: | ---: | ---: | --- | --- |
| `142` | `-1` | `-1` | `4` | `1` | `0` |

Firmware `142` is wildcard `-1.-1.-1` and declares four Modules.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `142` | `349` | `1` | `1` | Blind actuator |
| `142` | `350` | `6` | `6` | Light actuator |
| `142` | `351` | `7` | `7` | Automation actuator |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `500` | `1` | `1` | candidate / non-fixed | Blind actuator |
| `501` | `1` | `6` | fixed | Light actuator |
| `505` | `1` | `7` | candidate / non-fixed | Automation actuator |
| `502` | `2` | `6` | fixed | Light actuator |
| `506` | `2` | `7` | candidate / non-fixed | Automation actuator |
| `503` | `3` | `6` | fixed | Light actuator |
| `507` | `3` | `7` | candidate / non-fixed | Automation actuator |
| `504` | `4` | `6` | fixed | Light actuator |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| `142` | `15` | `510` | `510` | Automation relay virgin | `1`, `6`, `7` | `1`, `2`, `3`, `4` |

All four slots can be Object `6`, Light actuator. Object `7`, Automation actuator, is a candidate on slots `1..3`; Object `1`, Blind actuator, is a candidate beginning at slot `1`. Virgin Object `510`, Automation relay virgin, applies across slots `1..4` and permits Objects `1`, `6`, and `7`.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `142` | `1` | `1` | Virtual Configuration |
| `142` | `2` | `2` | Advanced Configuration |
| `142` | `3` | `0` | Physical configuration |

Physical configuration, Virtual Configuration and Advanced Configuration.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | MyHOME Suite / catalogue identity field - not a physical configurator |
| `A` | 0..9 | 0 | area / environment configurator |
| `PL1` | 0..9 | 0 | output 1 light-point configurator |
| `PL2` | 0..9 | 0 | output 2 light-point configurator |
| `PL3` | 0..9 | 0 | output 3 light-point configurator |
| `PL4` | 0..9 | 0 | output 4 light-point configurator |
| `M` | 0..4 / SLA / PUL | 0 | operating / function mode |

The shared area plus PL1..PL4 fields address the four output positions. The active Light / Automation / Blind Object topology is governed by the slot conditions documented below.

## Object configuration surfaces

### Object `1` - Blind actuator

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | target, group, installation-level or network addressing |
| Mode and behavior | `M`, `LOCAL_BUTTON` | operating mode and behavior selectors |
| Timing and levels | `STOP_TIME`, `DELAY_DOORS` | timers, delays, levels and transition parameters |
| Group membership | `G1`, `G2`, `G3`, `G4`, `G5`, `G6`, `G7`, `G8`, `G9`, `G10` | reusable group memberships; 0 means no group |

**Firmware relationship.** The catalogue relation explicitly exposes `LOCAL_BUTTON`.

### Object `6` - Light actuator

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | target, group, installation-level or network addressing |
| Mode and behavior | `M`, `LOCAL_BUTTON`, `STATE_RESET`, `LOAD_CONTROL_MODE`, `SUBTYPE` | operating mode and behavior selectors |
| Timing and levels | `DELAYED_OFF`, `HOURS`, `MINUTES`, `SECONDS` | timers, delays, levels and transition parameters |
| Group membership | `G1`, `G2`, `G3`, `G4`, `G5`, `G6`, `G7`, `G8`, `G9`, `G10` | reusable group memberships; 0 means no group |

**Firmware relationship.** The catalogue relation explicitly exposes `LOCAL_BUTTON`, `HOURS`, `MINUTES`, `STATE_RESET`, `SECONDS`, `LOAD_CONTROL_MODE`.

### Object `7` - Automation actuator

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | target, group, installation-level or network addressing |
| Mode and behavior | `M`, `LOCAL_BUTTON`, `SUBTYPE` | operating mode and behavior selectors |
| Timing and levels | `STOP_TIME` | timers, delays, levels and transition parameters |
| Group membership | `G1`, `G2`, `G3`, `G4`, `G5`, `G6`, `G7`, `G8`, `G9`, `G10` | reusable group memberships; 0 means no group |

**Firmware relationship.** The catalogue relation explicitly exposes `LOCAL_BUTTON`.

The tables above account for the reusable Object fields without reproducing database serialization metadata. Generic Object capability is kept distinct from the Device/firmware relationship and from physical configurator positions.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `8` | Device/Firmware topology conditions |
| Object/Firmware filters | `9` | Conditional Object configuration exposure |
| Referenced conversion rules | `3` | `10`, `2`, `9` |

### Slot conditions

| Slot | Object | Condition ID | Condition expression | Conversion rule |
| ---: | ---: | ---: | --- | ---: |
| `1` | `1` | `4703` | `PL2=PL1;PL4=PL3;PL3=PL2` | `9` |
| `1` | `6` | `4151` | No textual predicate - conversion-driven or unconditional catalogue row | `10` |
| `1` | `7` | `4702` | `PL2=PL1` | `2` |
| `2` | `6` | `4151` | No textual predicate - conversion-driven or unconditional catalogue row | `10` |
| `2` | `7` | `4704` | `PL3=PL2` | `2` |
| `3` | `6` | `4151` | No textual predicate - conversion-driven or unconditional catalogue row | `10` |
| `3` | `7` | `4705` | `PL4=PL3` | `2` |
| `4` | `6` | `4151` | No textual predicate - conversion-driven or unconditional catalogue row | `10` |

### Object/Firmware filters

| Object | Filter ID | Field | Note | Whole range | Filter ranges |
| ---: | ---: | --- | --- | --- | --- |
| `1` | `207` | `LOCAL_BUTTON` | FunzionalitÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â di pulsante locale ridotta (Local button mode) | `1` | - |
| `1` | `208` | `LOCAL_BUTTON` | Local button mode shutter (bi or mono) | `1` | - |
| `6` | `224` | `LOCAL_BUTTON` | Local button modality | `1` | - |
| `6` | `225` | `HOURS` | Hours | `1` | - |
| `6` | `226` | `MINUTES` | Minutes | `1` | - |
| `6` | `227` | `STATE_RESET` | Relay state on device reset | `1` | - |
| `6` | `228` | `SECONDS` | Seconds | `1` | - |
| `6` | `1857` | `LOAD_CONTROL_MODE` | Load_control_mode | `1` | - |
| `7` | `233` | `LOCAL_BUTTON` | FunzionalitÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â di pulsante locale ridotta (Local button mode) | `1` | - |

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

The Device can expose [`WHO 1` - Lighting](../../functional/who-1-lighting/) and [`WHO 2` - Automation](../../functional/who-2-automation/).

## Observed behavior and corroboration

No sanitized hardware fingerprint is currently retained.

## Programming

Resolve slot conditions before assigning relay roles. Motor/shutter arrangements require logical interlocking; a four-light arrangement keeps four independent lighting Modules.

## Source reconciliation

Official documentation corroborates four physical outputs, local control and paired motor use. The Virgin-Object topology explains the shared lighting/automation/blind capability. Older catalogues publish different lamp-load figures; this dossier keeps current values source-scoped.

## Evidence limits and open work

- Hardware-corroborate representative four-light and paired-motor configurations.
- Publish an exact `M` to slot-condition topology table after conversion-rule review.
- Pin exact printed and 1-based PDF page locations for each applicable multi-product guide citation.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [ST-00000896-EN](../../sources/devices/documents/device-doc-f411-4-st00000896-en/ST-00000896-EN.pdf)
- [AUTOMATISME.pdf](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf)
