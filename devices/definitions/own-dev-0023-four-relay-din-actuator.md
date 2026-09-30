# Four-relay DIN actuator

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0023` | Project identity |
| Technical description | Four-independent-relay 2-DIN actuator for lighting and paired automation/motor loads | Catalogue + official documentation |
| Commercial identities | `F411/4`, `003844` | Catalogue |
| Catalogue item | `3` - “4 relay actuator 2 modules DIN bus” | Implementation evidence |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `130` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `142` | Implementation evidence |
| Declared Modules | `4` | Implementation evidence |
| Categories | Actuator, Lighting, Automation, Shutter | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino / Undefined | `F411/4` | `3` | Commercial identity of this Technical Device | Canonical catalogue |
| Legrand / Undefined | `003844` | `1707` | Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ST-00000896-EN` | Technical sheet | 2021-03-23 | whole document / PDF pp. 1-4 | [Archived PDF](../../sources/devices/documents/device-doc-f411-4-st00000896-en/ST-00000896-EN.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/ST-00000896-EN.pdf) |
| `AUTOMATISME.pdf` | MyHOME automation guide | historical publisher guide | F411/4 family sections; exact page locator pending | [Archived PDF](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

For the multi-product guide, exact printed and 1-based PDF page locations remain an explicit reconciliation item until pinned.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 DIN modules | `ST-00000896-EN` / current product data |
| Outputs | 4 independent relays | `ST-00000896-EN` |
| Local interface | manual operation with LED indication | `ST-00000896-EN` |
| SCS nominal supply | `27 Vdc` | Current product data |
| SCS operating range | `18..27 Vdc` | Current product data |
| Current draw | `40 mA` | Current product data |
| Rated switching current | `2 A` | Current product data |
| Motor reducers | `500 W` | Current product data |
| Ferromagnetic transformer | `2 A`, cos φ `0.5` | Current product data |
| Fluorescent load | `70 W` | Current product data |
| Paired motor/shutter use | relay pairs can be logically interlocked | `ST-00000896-EN` |

The technical sheet shows a `10 A` protective breaker in a lighting wiring example; that example is not treated as the relay switching rating.

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
| `A` | `0..9` | `0` | area / environment configurator |
| `PL1` | `0..9` | `0` | output 1 light-point configurator |
| `PL2` | `0..9` | `0` | output 2 light-point configurator |
| `PL3` | `0..9` | `0` | output 3 light-point configurator |
| `PL4` | `0..9` | `0` | output 4 light-point configurator |
| `M` | `0..4` / `SLA` / `PUL` | `0` | operating / function mode |

The shared area plus `PL1` through `PL4` fields address the four output positions. The active Light / Automation / Blind Object topology is governed by the slot conditions documented below.

## Object configuration surfaces

### Object `1` - Blind actuator

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | target, group, installation-level or network addressing |
| Mode and behavior | `M`, `LOCAL_BUTTON` | operating mode and behavior selectors |
| Timing and levels | `STOP_TIME`, `DELAY_DOORS` | timers, delays, levels and transition parameters |
| Group membership | `G1`, `G2`, `G3`, `G4`, `G5`, `G6`, `G7`, `G8`, `G9`, `G10` | reusable group memberships; `0` means no group |

**Firmware relationship.** The catalogue relation explicitly exposes `LOCAL_BUTTON`.

### Object `6` - Light actuator

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | target, group, installation-level or network addressing |
| Mode and behavior | `M`, `LOCAL_BUTTON`, `STATE_RESET`, `LOAD_CONTROL_MODE`, `SUBTYPE` | operating mode and behavior selectors |
| Timing and levels | `DELAYED_OFF`, `HOURS`, `MINUTES`, `SECONDS` | timers, delays, levels and transition parameters |
| Group membership | `G1`, `G2`, `G3`, `G4`, `G5`, `G6`, `G7`, `G8`, `G9`, `G10` | reusable group memberships; `0` means no group |

**Firmware relationship.** The catalogue relation explicitly exposes `LOCAL_BUTTON`, `HOURS`, `MINUTES`, `STATE_RESET`, `SECONDS`, `LOAD_CONTROL_MODE`.

### Object `7` - Automation actuator

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | target, group, installation-level or network addressing |
| Mode and behavior | `M`, `LOCAL_BUTTON`, `SUBTYPE` | operating mode and behavior selectors |
| Timing and levels | `STOP_TIME` | timers, delays, levels and transition parameters |
| Group membership | `G1`, `G2`, `G3`, `G4`, `G5`, `G6`, `G7`, `G8`, `G9`, `G10` | reusable group memberships; `0` means no group |

**Firmware relationship.** The catalogue relation explicitly exposes `LOCAL_BUTTON`.

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

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

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 130` and the `F411/4` / `003844` family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | record installed firmware rather than assuming wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | enumerate all four relay positions and resolve conditional Light/Automation/Blind Objects | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the four configured output addresses | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `A`, `M`, `PL1` through `PL4` and the slot conditions that select the active Objects | [Configuration](../../diagnostics/dim35-configuration.md) |

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
