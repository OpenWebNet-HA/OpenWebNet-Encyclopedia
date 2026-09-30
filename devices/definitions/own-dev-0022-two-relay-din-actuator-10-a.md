# Two-relay DIN actuator 10 A

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0022` | Project identity |
| Technical description | Two-independent-relay DIN actuator for lighting, automation and paired motor loads | Catalogue + official documentation |
| Catalogue item / model | `2` / `modobj 129` | Implementation evidence |
| Firmware applicability | firmware `132`, `-1.-1.-1`, two slots | Implementation evidence |
| Commercial identities | `F411/2`, `003842` | Catalogue |
| Categories | Actuator, Lighting, Automation, Shutter | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino / Undefined | `F411/2` | `2` | Commercial identity of this Technical Device | Canonical catalogue |
| Legrand / Undefined | `003842` | `1708` | Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Relevant pages | Status | Source |
| --- | --- | --- | --- | --- | --- |
| AUTOMATISME.pdf | MyHOME automation guide | historical publisher guide | F411/2 family sections; exact printed/PDF locator pending | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) |
| BTicino F411/2 | Current product record | current | Whole product page | External official source | [Official source](https://www.bticino.com/products/bt-f411-2) |

Multi-product guides retain an explicit page-location limitation until both printed and 1-based PDF page numbers are pinned.

## Physical and electrical characteristics

F411/2 is a 2-DIN, two-relay actuator with local/manual control and LED indication. Current BTicino data gives `27 Vdc`, `28 mA`, `1380 W` maximum switching power, two contacts and `18..27 V` operating voltage. Current product text gives `10 A` resistive, `6 A` filament, `500 W` motor reducers, `2 A cosφ 0.5` ferromagnetic transformers and `250 W` fluorescent loads. Older guides contain lower values for some load classes and remain revision-scoped. The relays can be logically interlocked for motor/shutter use.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2` | Canonical catalogue |
| Technical item description | 2 relays DIN actuator 10 A | Canonical catalogue |
| Item family | `2` - Actuator | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `129` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Declared slots | Default | Status |
| ---: | ---: | ---: | ---: | --- | --- |
| `132` | `-1` | `-1` | `2` | `1` | `0` |

Firmware `132` is wildcard `-1.-1.-1` and declares two Module slots.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `132` | `274` | `7` | `7` | Automation actuator |
| `132` | `275` | `6` | `6` | Light actuator |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `274` | `1` | `7` | candidate / non-fixed | Automation actuator |
| `275` | `1` | `6` | fixed | Light actuator |
| `276` | `2` | `6` | fixed | Light actuator |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| `132` | `5` | `510` | `510` | Automation relay virgin | `1`, `6`, `7` | `1`, `2` |

Slots `1` and `2` default to Object `6`, Light actuator. Slot `1` also has Object `7`, Automation actuator, as a candidate. Virgin Object `510`, Automation relay virgin, applies to both slots and permits Object `1` Blind actuator, Object `6` Light actuator and Object `7` Automation actuator.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `132` | `1` | `1` | Virtual Configuration |
| `132` | `2` | `2` | Advanced Configuration |
| `132` | `3` | `0` | Physical configuration |

Physical configuration, Virtual Configuration and Advanced Configuration.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | MyHOME Suite / catalogue identity field - not a physical configurator |
| `A` | `0..9` | `0` | area / environment configurator |
| `PL1` | `0..9` | `0` | output 1 light-point configurator |
| `PL2` | `0..9` | `0` | output 2 light-point configurator |
| `G1` | `0..9` | `0` | group configurator 1 |
| `M` | `0..4` / `SLA` / `PUL` | `0` | operating / function mode |

The shared area plus separate `PL1` / `PL2` fields address the two outputs. Object selection and interlock topology are resolved separately from these firmware configurators.

## Object configuration surfaces

### Object `7` - Automation actuator

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | target, group, installation-level or network addressing |
| Mode and behavior | `M`, `LOCAL_BUTTON`, `SUBTYPE` | operating mode and behavior selectors |
| Timing and levels | `STOP_TIME` | timers, delays, levels and transition parameters |
| Group membership | `G1`, `G2`, `G3`, `G4`, `G5`, `G6`, `G7`, `G8`, `G9`, `G10` | reusable group memberships; `0` means no group |

**Firmware relationship.** The catalogue relation explicitly exposes `LOCAL_BUTTON`. The catalogue relation restricts `SUBTYPE`: Differential restart (`15`).

### Object `6` - Light actuator

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | target, group, installation-level or network addressing |
| Mode and behavior | `M`, `LOCAL_BUTTON`, `STATE_RESET`, `LOAD_CONTROL_MODE`, `SUBTYPE` | operating mode and behavior selectors |
| Timing and levels | `DELAYED_OFF`, `HOURS`, `MINUTES`, `SECONDS` | timers, delays, levels and transition parameters |
| Group membership | `G1`, `G2`, `G3`, `G4`, `G5`, `G6`, `G7`, `G8`, `G9`, `G10` | reusable group memberships; `0` means no group |

**Firmware relationship.** The catalogue relation explicitly exposes `LOCAL_BUTTON`, `MINUTES`, `HOURS`, `STATE_RESET`, `SECONDS`, `LOAD_CONTROL_MODE`.

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `3` | Device/Firmware topology conditions |
| Object/Firmware filters | `8` | Conditional Object configuration exposure |
| Referenced conversion rules | `2` | `1`, `2` |

### Slot conditions

| Slot | Object | Condition ID | Condition expression | Conversion rule |
| ---: | ---: | ---: | --- | ---: |
| `1` | `6` | `4147` | No textual predicate - conversion-driven or unconditional catalogue row | `1` |
| `1` | `7` | `4702` | `PL2=PL1` | `2` |
| `2` | `6` | `4147` | No textual predicate - conversion-driven or unconditional catalogue row | `1` |

### Object/Firmware filters

| Object | Filter ID | Field | Note | Whole range | Filter ranges |
| ---: | ---: | --- | --- | --- | --- |
| `6` | `73` | `LOCAL_BUTTON` | Local button modality | `1` | - |
| `6` | `74` | `MINUTES` | Minutes | `1` | - |
| `6` | `75` | `HOURS` | Hours | `1` | - |
| `6` | `76` | `STATE_RESET` | Relay state on device reset | `1` | - |
| `6` | `77` | `SECONDS` | Seconds | `1` | - |
| `6` | `1856` | `LOAD_CONTROL_MODE` | Load_control_mode | `1` | - |
| `7` | `66` | `LOCAL_BUTTON` | FunzionalitÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â di pulsante locale ridotta (Local button mode) | `1` | - |
| `7` | `67` | `SUBTYPE` | subtype(ASTCBR) | `0` | `15` - Differential restart |

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

The selected topology can expose [`WHO 1` - Lighting](../../functional/who-1-lighting/) and [`WHO 2` - Automation](../../functional/who-2-automation/).

## Observed behavior and corroboration

No sanitized hardware fingerprint is currently retained.

## Programming

Preserve both slots independently. Motor/shutter configurations require the documented logical interlock.

## Source reconciliation

The database Virgin-Object topology explains the documented single, double and combined-load behavior: the relay slots can remain lighting channels or resolve to automation/blind roles. Current and historical load tables differ, so current ratings are stated with source scope rather than overwriting older revisions.

## Evidence limits and open work

- Archive a dedicated current F411/2 technical sheet if exposed by the publisher.
- Hardware-corroborate Object selection and interlock configurations.
- Establish the exact physical configurator-position count from dedicated documentation or hardware.
- Pin exact printed and 1-based PDF page locations for each applicable multi-product guide citation.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf)
- [BTicino F411/2](https://www.bticino.com/products/bt-f411-2)
