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

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `AID` | ID | user_value | `********` - AID - range `0`..`0` - step `1` | visible=1, hidden=0, read-only=0, type-id=0 |
| `A` | A | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=1 |
| `PL1` | PL1 | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=2 |
| `PL2` | PL2 | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=2 |
| `G1` | G1 | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=3 |
| `M` | M | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1`<br>`1` - 1 - range -..- - step `1`<br>`2` - 2 - range -..- - step `1`<br>`3` - 3 - range -..- - step `1`<br>`4` - 4 - range -..- - step `1`<br>`11` - SLA - range -..- - step `1`<br>`15` - PUL - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |

Catalogue range rows are preserved directly; product-document physical configurator limits remain a distinct evidence layer.

`A`, `PL1`, `PL2`, and `G1` are `0..9`; `M` permits default/`0..4`/`SLA`/`PUL`; `AID` is the identity field. The shared `A` plus separate `PL1/PL2` addresses the two outputs.

## Object configuration surfaces

### Object `6` - Light actuator

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `A` | Area | Range | range `0`..`10` - step `1` | visible=1, hidden=0, read-only=, type-id=1 |
| `PL` | Light point | Range | range `0`..`15` - step `1` | visible=1, hidden=0, read-only=, type-id=2 |
| `M` | Modality | Enum | range -..- - step `1`<br>`0` - Master - range -..- - step `1`<br>`11` - Slave - range -..- - step `1`<br>`15` - Master PUL - range -..- - step `1`<br>`16` - Slave and PUL - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `LOCAL_BUTTON` | Local button modality | Enum | range -..- - step `1`<br>`0` - Toggle - range -..- - step `1`<br>`1` - ON/OFF - range -..- - step `1`<br>`9` - ON - OFF - range -..- - step `1`<br>`15` - Pushbutton - range -..- - step `1`<br>`18` - Timed ON - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `DELAYED_OFF` | Delayed OFF for Slave (s) | Range | range `0`..`255` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `STATE_RESET` | Relay state on device reset | Enum | range -..- - step `1`<br>`0` - Restore last value - range -..- - step `1`<br>`1` - Closed - range -..- - step `1`<br>`2` - Open - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `LOAD_CONTROL_MODE` | Load control mode | Enum | range -..- - step `1`<br>`0` - With zero crossing - range -..- - step `1`<br>`1` - Without zero crossing - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `HOURS` | Hours | Range | range `0`..`255` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `MINUTES` | Minutes | Range | range `0`..`59` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `SECONDS` | Seconds | Range | range `0`..`59` - step `1` - default marker `30` | visible=1, hidden=1, read-only=, type-id= |
| `SUBTYPE` | Type of load | Enum | range -..- - step `1` - default marker `11`<br>`11` - Actuator - range -..- - step `1`<br>`1` - Lamp - range -..- - step `1`<br>`10` - Valve - range -..- - step `1`<br>`15` - Differential restart - range -..- - step `1`<br>`6` - Fan - range -..- - step `1`<br>`7` - Watering - range -..- - step `1`<br>`8` - Controlled socket - range -..- - step `1`<br>`9` - Lock - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
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

### Object `7` - Automation actuator

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `A` | Area | Range | range `0`..`10` - step `1` | visible=1, hidden=0, read-only=, type-id=1 |
| `PL` | Light point | Range | range `0`..`15` - step `1` | visible=1, hidden=0, read-only=, type-id=2 |
| `M` | Modality | Enum | range -..- - step `1`<br>`0` - Master - range -..- - step `1`<br>`11` - Slave - range -..- - step `1`<br>`15` - Master PUL - range -..- - step `1`<br>`16` - Slave and PUL - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `LOCAL_BUTTON` | Local button modality | Enum | range -..- - step `1` - default marker `12`<br>`12` - Bistable control - range -..- - step `1`<br>`13` - Monostable control - range -..- - step `1`<br>`14` - Bistable and blades control - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `STOP_TIME` | Stop time | Enum | range -..- - step `1` - default marker `60`<br>`0` - Infinite - range -..- - step `1`<br>`1` - 1 s - range -..- - step `1`<br>`2` - 2 s - range -..- - step `1`<br>`3` - 3 s - range -..- - step `1`<br>`4` - 4 s - range -..- - step `1`<br>`5` - 5 s - range -..- - step `1`<br>`6` - 6 s - range -..- - step `1`<br>`7` - 7 s - range -..- - step `1`<br>`8` - 8 s - range -..- - step `1`<br>`9` - 9 s - range -..- - step `1`<br>`10` - 10 s - range -..- - step `1`<br>`11` - 11 s - range -..- - step `1`<br>`12` - 12 s - range -..- - step `1`<br>`13` - 13 s - range -..- - step `1`<br>`14` - 14 s - range -..- - step `1`<br>`15` - 15 s - range -..- - step `1`<br>`16` - 16 s - range -..- - step `1`<br>`17` - 17 s - range -..- - step `1`<br>`19` - 19 s - range -..- - step `1`<br>`20` - 20 s - range -..- - step `1`<br>`21` - 21 s - range -..- - step `1`<br>`22` - 22 s - range -..- - step `1`<br>`23` - 23 s - range -..- - step `1`<br>`24` - 24 s - range -..- - step `1`<br>`25` - 25 s - range -..- - step `1`<br>`26` - 26 s - range -..- - step `1`<br>`27` - 27 s - range -..- - step `1`<br>`28` - 28 s - range -..- - step `1`<br>`29` - 29 s - range -..- - step `1`<br>`30` - 30 s - range -..- - step `1`<br>`31` - 31 s - range -..- - step `1`<br>`32` - 32 s - range -..- - step `1`<br>`33` - 33 s - range -..- - step `1`<br>`34` - 34 s - range -..- - step `1`<br>`35` - 35 s - range -..- - step `1`<br>`36` - 36 s - range -..- - step `1`<br>`37` - 37 s - range -..- - step `1`<br>`38` - 38 s - range -..- - step `1`<br>`39` - 39 s - range -..- - step `1`<br>`40` - 40 s - range -..- - step `1`<br>`41` - 41 s - range -..- - step `1`<br>`42` - 42 s - range -..- - step `1`<br>`43` - 43 s - range -..- - step `1`<br>`44` - 44 s - range -..- - step `1`<br>`45` - 45 s - range -..- - step `1`<br>`46` - 46 s - range -..- - step `1`<br>`47` - 47 s - range -..- - step `1`<br>`48` - 48 s - range -..- - step `1`<br>`49` - 49 s - range -..- - step `1`<br>`50` - 50 s - range -..- - step `1`<br>`51` - 51 s - range -..- - step `1`<br>`52` - 52 s - range -..- - step `1`<br>`53` - 53 s - range -..- - step `1`<br>`54` - 54 s - range -..- - step `1`<br>`55` - 55 s - range -..- - step `1`<br>`56` - 56 s - range -..- - step `1`<br>`57` - 57 s - range -..- - step `1`<br>`58` - 58 s - range -..- - step `1`<br>`59` - 59 s - range -..- - step `1`<br>`60` - 60 s - range -..- - step `1`<br>`62` - 2 min - range -..- - step `1`<br>`63` - 3 min - range -..- - step `1`<br>`64` - 4 min - range -..- - step `1`<br>`65` - 5 min - range -..- - step `1`<br>`66` - 6 min - range -..- - step `1`<br>`67` - 7 min - range -..- - step `1`<br>`68` - 8 min - range -..- - step `1`<br>`69` - 9 min - range -..- - step `1`<br>`70` - 10 min - range -..- - step `1` | visible=1, hidden=1, read-only=, type-id=0 |
| `SUBTYPE` | Type of load | Enum | range -..- - step `1` - default marker `11`<br>`11` - Actuator - range -..- - step `1`<br>`2` - Shutter - range -..- - step `1`<br>`3` - Curtain - range -..- - step `1`<br>`4` - Gate - range -..- - step `1`<br>`5` - Garage door - range -..- - step `1`<br>`15` - Differential restart - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
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

Objects `1`, `6`, and `7` contribute their reusable blind, lighting and automation parameter models when selected.

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
