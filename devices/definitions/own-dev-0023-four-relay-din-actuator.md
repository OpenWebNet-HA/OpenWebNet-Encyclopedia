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

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `AID` | ID | user_value | `********` - AID - range `0`..`0` - step `1` | visible=1, hidden=0, read-only=0, type-id=0 |
| `A` | A | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=1 |
| `PL1` | PL1 | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=2 |
| `PL2` | PL2 | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=2 |
| `PL3` | PL3 | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=2 |
| `PL4` | PL4 | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id=2 |
| `M` | M | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1`<br>`1` - 1 - range -..- - step `1`<br>`2` - 2 - range -..- - step `1`<br>`3` - 3 - range -..- - step `1`<br>`4` - 4 - range -..- - step `1`<br>`11` - SLA - range -..- - step `1`<br>`15` - PUL - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |

Catalogue range rows are preserved directly; product-document physical configurator limits remain a distinct evidence layer.

`A` and `PL1..PL4` are `0..9`; `M` permits default/`0..4`/`SLA`/`PUL`; `AID` is the identity field.

## Object configuration surfaces

### Object `1` - Blind actuator

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `A` | Area | Range | range `0`..`10` - step `1` | visible=1, hidden=0, read-only=, type-id=1 |
| `PL` | Light point | Range | range `0`..`15` - step `1` | visible=1, hidden=0, read-only=, type-id=2 |
| `M` | Modality | Enum | range -..- - step `1`<br>`0` - Master - range -..- - step `1`<br>`11` - Slave - range -..- - step `1`<br>`15` - Master PUL - range -..- - step `1`<br>`16` - Slave and PUL - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `LOCAL_BUTTON` | Local button modality | Enum | range -..- - step `1` - default marker `12`<br>`12` - Bistable control - range -..- - step `1`<br>`13` - Monostable control - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `STOP_TIME` | Stop time | Enum | range -..- - step `1` - default marker `60`<br>`0` - Infinite - range -..- - step `1`<br>`1` - 1 s - range -..- - step `1`<br>`2` - 2 s - range -..- - step `1`<br>`4` - 4 s - range -..- - step `1`<br>`5` - 5 s - range -..- - step `1`<br>`6` - 6 s - range -..- - step `1`<br>`7` - 7 s - range -..- - step `1`<br>`8` - 8 s - range -..- - step `1`<br>`9` - 9 s - range -..- - step `1`<br>`10` - 10 s - range -..- - step `1`<br>`13` - 13 s - range -..- - step `1`<br>`14` - 14 s - range -..- - step `1`<br>`15` - 15 s - range -..- - step `1`<br>`16` - 16 s - range -..- - step `1`<br>`17` - 17 s - range -..- - step `1`<br>`18` - 18 s - range -..- - step `1`<br>`19` - 19 s - range -..- - step `1`<br>`21` - 21 s - range -..- - step `1`<br>`23` - 23 s - range -..- - step `1`<br>`24` - 24 s - range -..- - step `1`<br>`25` - 25 s - range -..- - step `1`<br>`26` - 26 s - range -..- - step `1`<br>`27` - 27 s - range -..- - step `1`<br>`28` - 28 s - range -..- - step `1`<br>`29` - 29 s - range -..- - step `1`<br>`30` - 30 s - range -..- - step `1`<br>`31` - 31 s - range -..- - step `1`<br>`34` - 34 s - range -..- - step `1`<br>`35` - 35 s - range -..- - step `1`<br>`36` - 36 s - range -..- - step `1`<br>`37` - 37 s - range -..- - step `1`<br>`38` - 38 s - range -..- - step `1`<br>`39` - 39 s - range -..- - step `1`<br>`40` - 40 s - range -..- - step `1`<br>`41` - 41 s - range -..- - step `1`<br>`42` - 42 s - range -..- - step `1`<br>`43` - 43 s - range -..- - step `1`<br>`44` - 44 s - range -..- - step `1`<br>`45` - 45 s - range -..- - step `1`<br>`46` - 46 s - range -..- - step `1`<br>`47` - 47 s - range -..- - step `1`<br>`48` - 48 s - range -..- - step `1`<br>`49` - 49 s - range -..- - step `1`<br>`50` - 50 s - range -..- - step `1`<br>`51` - 51 s - range -..- - step `1`<br>`52` - 52 s - range -..- - step `1`<br>`53` - 53 s - range -..- - step `1`<br>`54` - 54 s - range -..- - step `1`<br>`55` - 55 s - range -..- - step `1`<br>`56` - 56 s - range -..- - step `1`<br>`57` - 57 s - range -..- - step `1`<br>`58` - 58 s - range -..- - step `1`<br>`59` - 59 s - range -..- - step `1`<br>`60` - 60 s - range -..- - step `1`<br>`62` - 2 min - range -..- - step `1`<br>`63` - 3 min - range -..- - step `1`<br>`64` - 4 min - range -..- - step `1`<br>`65` - 5 min - range -..- - step `1`<br>`66` - 6 min - range -..- - step `1`<br>`67` - 7 min - range -..- - step `1`<br>`68` - 8 min - range -..- - step `1`<br>`69` - 9 min - range -..- - step `1`<br>`70` - 10 min - range -..- - step `1` | visible=1, hidden=1, read-only=, type-id=0 |
| `DELAY_DOORS` | Delay between doors | Range | range `0`..`60` - step `1` - default marker `3` | visible=1, hidden=0, read-only=, type-id= |
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

Selected slots reuse the Light, Automation, or Blind actuator configuration models. Pairing/interlocking must remain consistent with resolved topology.

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
