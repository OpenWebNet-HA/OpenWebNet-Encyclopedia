# Flush-mounted radio receiver for batteryless control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0035` | Project identity |
| Technical description | Four-slot SCS radio receiver for batteryless flat controls | Catalogue + official documentation |
| Catalogue item / model | `40` / `modobj 19` | Implementation evidence |
| Firmware applicability | 218, wildcard -1.-1.-1, four slots | Implementation evidence |
| Commercial identities | HC/HS/HD4575SB; L/N/NT4575SB | Catalogue |
| Categories | Radio interface, Lighting control, Automation control, Scenario control | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino / Axolute | `HC/HS/HD4575SB` | `40` | Commercial identity of this Technical Device | Canonical catalogue |
| BTicino / Axolute | `L/N/NT4575SB` | `1841` | Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Relevant pages | Status | Source |
| --- | --- | --- | --- | --- | --- |
| AUTOMATISME.pdf | MyHOME automation guide | historical publisher guide | 4575SB interface sections; exact printed/PDF locator pending | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) |

Multi-product guides retain an explicit page-location limitation until both printed and 1-based PDF page numbers are pinned.

## Physical and electrical characteristics

Official automation documentation describes a 27 Vdc BUS-powered two-module receiver. Historical technical material specifies 868 MHz radio operation; exact range and current figures remain source-revision scoped.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `40` | Canonical catalogue |
| Technical item description | Flush mounted radio receiver for HA/HB4572SB | Canonical catalogue |
| Item family | `27` - Radio device | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `19` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Declared slots | Default | Status |
| ---: | ---: | ---: | ---: | --- | --- |
| `218` | `-1` | `-1` | `4` | `1` | `0` |

Firmware 218 has wildcard version/revision/build applicability and four Module slots.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `218` | `608` | `400` | `400` | Light control |
| `218` | `609` | `403` | `403` | Scenario module control |
| `218` | `610` | `401` | `401` | Automation control |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `1011` | `1` | `400` | fixed | Light control |
| `1015` | `1` | `403` | candidate / non-fixed | Scenario module control |
| `1019` | `1` | `401` | candidate / non-fixed | Automation control |
| `1012` | `2` | `400` | fixed | Light control |
| `1016` | `2` | `403` | candidate / non-fixed | Scenario module control |
| `1013` | `3` | `400` | fixed | Light control |
| `1017` | `3` | `403` | candidate / non-fixed | Scenario module control |
| `1020` | `3` | `401` | candidate / non-fixed | Automation control |
| `1014` | `4` | `400` | fixed | Light control |
| `1018` | `4` | `403` | candidate / non-fixed | Scenario module control |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| - | - | - | - | No firmware-scoped Virgin Object | - | - |

Object 400 Light control is fixed on slots 1,2,3,4. Object 403 Scenario module control is a non-fixed candidate on all four slots. Object 401 Automation control is a non-fixed candidate on slots 1 and 3. Shared Virgin Object families 500/501/502 cover the corresponding Light, Automation and Scenario control Objects.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `218` | `1` | `1` | Virtual Configuration |
| `218` | `3` | `0` | Physical configuration |

The catalogue declares configuration modes 1 and 3.

## Firmware-scoped configuration

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `AID` | ID | user_value | `********` - AID - range `0`..`0` - step `1` | visible=1, hidden=0, read-only=0, type-id=0 |
| `A` | A | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `PL1` | PL1 | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `M1` | M1 | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1`<br>`1` - 1 - range -..- - step `1`<br>`2` - 2 - range -..- - step `1`<br>`3` - 3 - range -..- - step `1`<br>`4` - 4 - range -..- - step `1`<br>`5` - 5 - range -..- - step `1`<br>`6` - 6 - range -..- - step `1`<br>`7` - 7 - range -..- - step `1`<br>`8` - 8 - range -..- - step `1`<br>`9` - O/I - range -..- - step `1`<br>`10` - OFF - range -..- - step `1`<br>`11` - ON - range -..- - step `1`<br>`12` - UP/DOWN - range -..- - step `1`<br>`13` - UP/DOWN monostable - range -..- - step `1`<br>`14` - CEN - range -..- - step `1`<br>`15` - PUL - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `PL2` | PL2 | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `M2` | M2 | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1`<br>`1` - 1 - range -..- - step `1`<br>`2` - 2 - range -..- - step `1`<br>`3` - 3 - range -..- - step `1`<br>`4` - 4 - range -..- - step `1`<br>`5` - 5 - range -..- - step `1`<br>`6` - 6 - range -..- - step `1`<br>`7` - 7 - range -..- - step `1`<br>`8` - 8 - range -..- - step `1`<br>`9` - O/I - range -..- - step `1`<br>`10` - OFF - range -..- - step `1`<br>`11` - ON - range -..- - step `1`<br>`12` - UP/DOWN - range -..- - step `1`<br>`13` - UP/DOWN monostable - range -..- - step `1`<br>`14` - CEN - range -..- - step `1`<br>`15` - PUL - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `SPE` | SPE | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1`<br>`1` - 1 - range -..- - step `1`<br>`6` - 6 - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |

Catalogue range rows are preserved directly; product-document physical configurator limits remain a distinct evidence layer.

Firmware fields are A, PL1, M1, PL2, M2, SPE and AID. M1/M2 accept 0..8 plus O/I, OFF, ON, SU_GIU, SU_GIU_M, CEN and PUL; SPE accepts 0,1,6.

## Object configuration surfaces

### Object `400` - Light control

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `M` | Modality | Enum | range -..- - step `1`<br>`0` - Toggle - range -..- - step `1`<br>`1` - Timed ON - range -..- - step `1`<br>`2` - Toggle dimmer - range -..- - step `1`<br>`3` - ON/OFF and dimming - range -..- - step `1`<br>`4` - Toggle ON/OFF - range -..- - step `1`<br>`5` - ON/OFF - range -..- - step `1`<br>`9` - ON/OFF and point to point dimming - range -..- - step `1`<br>`10` - OFF - range -..- - step `1`<br>`11` - ON - range -..- - step `1`<br>`15` - PUL - range -..- - step `1`<br>`32` - Blinking 0.5 s - range -..- - step `1`<br>`33` - Blinking 1 s - range -..- - step `1`<br>`34` - Blinking 1.5 s - range -..- - step `1`<br>`35` - Blinking 2 s - range -..- - step `1`<br>`36` - Blinking 2.5 s - range -..- - step `1`<br>`37` - Blinking 3 s - range -..- - step `1`<br>`38` - Blinking 3.5 s - range -..- - step `1`<br>`39` - Blinking 4 s - range -..- - step `1`<br>`40` - Blinking 4.5 s - range -..- - step `1`<br>`41` - Blinking 5 s - range -..- - step `1`<br>`42` - Blinking 5.5 s - range -..- - step `1`<br>`43` - Blinking 6 s - range -..- - step `1`<br>`44` - Blinking 6.5 s - range -..- - step `1`<br>`45` - Blinking 7 s - range -..- - step `1`<br>`46` - Blinking 7.5 s - range -..- - step `1`<br>`47` - Blinking 8 s - range -..- - step `1`<br>`49` - ON dimmer 10% - range -..- - step `1`<br>`50` - ON dimmer 20% - range -..- - step `1`<br>`51` - ON dimmer 30% - range -..- - step `1`<br>`52` - ON dimmer 40% - range -..- - step `1`<br>`53` - ON dimmer 50% - range -..- - step `1`<br>`54` - ON dimmer 60% - range -..- - step `1`<br>`55` - ON dimmer 70% - range -..- - step `1`<br>`56` - ON dimmer 80% - range -..- - step `1`<br>`57` - ON dimmer 90% - range -..- - step `1`<br>`128` - Customized timed ON - range -..- - step `1`<br>`129` - Customized toggle and point to point dimmer - range -..- - step `1`<br>`130` - Customized ON/OFF and point to point dimmer - range -..- - step `1`<br>`131` - Customized toggle dimmer - range -..- - step `1`<br>`132` - Customized ON/OFF and dimmer - range -..- - step `1`<br>`133` - Customized toggle dimmer without regulation - range -..- - step `1`<br>`134` - Customized ON/OFF and dimmer without regulation - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `ADDR_TYPE` | Addressing type | Enum | range -..- - step `1`<br>`0` - Point to point - range -..- - step `1`<br>`1` - Area - range -..- - step `1`<br>`2` - Group - range -..- - step `1`<br>`3` - General - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `A` | Area | Range | range `0`..`10` - step `1` | visible=1, hidden=1, read-only=, type-id=0 |
| `PL` | Light point | Range | range `0`..`15` - step `1` | visible=1, hidden=1, read-only=, type-id=0 |
| `G` | Group | Range | range `1`..`255` - step `1` - default marker `1` | visible=1, hidden=1, read-only=, type-id=3 |
| `INST_LEV` | Installation level | Enum | range -..- - step `1` - default marker `16`<br>`0` - Private riser - range -..- - step `1`<br>`1` - Local bus 1 - range -..- - step `1`<br>`2` - Local bus 2 - range -..- - step `1`<br>`3` - Local bus 3 - range -..- - step `1`<br>`4` - Local bus 4 - range -..- - step `1`<br>`5` - Local bus 5 - range -..- - step `1`<br>`6` - Local bus 6 - range -..- - step `1`<br>`7` - Local bus 7 - range -..- - step `1`<br>`8` - Local bus 8 - range -..- - step `1`<br>`9` - Local bus 9 - range -..- - step `1`<br>`10` - Local bus 10 - range -..- - step `1`<br>`11` - Local bus 11 - range -..- - step `1`<br>`12` - Local bus 12 - range -..- - step `1`<br>`13` - Local bus 13 - range -..- - step `1`<br>`14` - Local bus 14 - range -..- - step `1`<br>`15` - Local bus 15 - range -..- - step `1`<br>`16` - Standard - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `DEST_LEV` | Destination level | Enum | range -..- - step `1`<br>`0` - Private riser - range -..- - step `1`<br>`1` - Local bus 1 - range -..- - step `1`<br>`2` - Local bus 2 - range -..- - step `1`<br>`3` - Local bus 3 - range -..- - step `1`<br>`4` - Local bus 4 - range -..- - step `1`<br>`5` - Local bus 5 - range -..- - step `1`<br>`6` - Local bus 6 - range -..- - step `1`<br>`7` - Local bus 7 - range -..- - step `1`<br>`8` - Local bus 8 - range -..- - step `1`<br>`9` - Local bus 9 - range -..- - step `1`<br>`10` - Local bus 10 - range -..- - step `1`<br>`11` - Local bus 11 - range -..- - step `1`<br>`12` - Local bus 12 - range -..- - step `1`<br>`13` - Local bus 13 - range -..- - step `1`<br>`14` - Local bus 14 - range -..- - step `1`<br>`15` - Local bus 15 - range -..- - step `1`<br>`16` - All systems - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `A_R` | Light point of reference actuator | Range | range `0`..`10` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `PL_R` | Light point of reference actuator | Range | range `0`..`15` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `HOURS` | Hours | Range | range `0`..`255` - step `1` | visible=1, hidden=1, read-only=, type-id=0 |
| `MINUTES` | Minutes | Range | range `0`..`59` - step `1` | visible=1, hidden=1, read-only=, type-id=0 |
| `SECONDS` | Seconds | Range | range `0`..`59` - step `1` - default marker `30` | visible=1, hidden=1, read-only=, type-id=0 |
| `LEVEL` | Level | Range | range `0`..`100` - step `1` - default marker `100` | visible=1, hidden=1, read-only=, type-id=0 |
| `START_S` | Soft start speed | Range | range `0`..`255` - step `1` - default marker `255` | visible=1, hidden=1, read-only=, type-id=0 |
| `STOP_S` | Soft stop speed | Range | range `0`..`255` - step `1` - default marker `255` | visible=1, hidden=1, read-only=, type-id=0 |
| `DIMMING_S` | Dimming speed | Range | range `0`..`255` - step `1` - default marker `255` | visible=1, hidden=1, read-only=, type-id=0 |
| `T_TIME` | Tabled time | Enum | range -..- - step `1` - default marker `1`<br>`1` - 1 min - range -..- - step `1`<br>`2` - 2 min - range -..- - step `1`<br>`3` - 3 min - range -..- - step `1`<br>`4` - 4 min - range -..- - step `1`<br>`5` - 5 min - range -..- - step `1`<br>`6` - 15 min - range -..- - step `1`<br>`7` - 30 s - range -..- - step `1`<br>`8` - 0.5 s - range -..- - step `1`<br>`9` - 2 s - range -..- - step `1`<br>`10` - 10 min - range -..- - step `1` | visible=1, hidden=1, read-only=, type-id=0 |
| `IN_AUX_CHANNEL` | Input AUX channel | Range | range `0`..`15` - step `1` | visible=1, hidden=0, read-only=, type-id=0 |

### Object `401` - Automation control

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `M` | Modality | Enum | range -..- - step `1` - default marker `12`<br>`12` - Bistable control - range -..- - step `1`<br>`13` - Monostable control - range -..- - step `1`<br>`14` - Blades control and bistable - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `ADDR_TYPE` | Addressing type | Enum | range -..- - step `1`<br>`0` - Point to point - range -..- - step `1`<br>`1` - Area - range -..- - step `1`<br>`2` - Group - range -..- - step `1`<br>`3` - General - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `A` | Area | Range | range `0`..`10` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `PL` | Light point | Range | range `0`..`15` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `G` | Group | Range | range `1`..`255` - step `1` - default marker `1` | visible=1, hidden=1, read-only=, type-id=3 |
| `INST_LEV` | Installation level | Enum | range -..- - step `1` - default marker `16`<br>`0` - Private riser - range -..- - step `1`<br>`1` - Local bus 1 - range -..- - step `1`<br>`2` - Local bus 2 - range -..- - step `1`<br>`3` - Local bus 3 - range -..- - step `1`<br>`4` - Local bus 4 - range -..- - step `1`<br>`5` - Local bus 5 - range -..- - step `1`<br>`6` - Local bus 6 - range -..- - step `1`<br>`7` - Local bus 7 - range -..- - step `1`<br>`8` - Local bus 8 - range -..- - step `1`<br>`9` - Local bus 9 - range -..- - step `1`<br>`10` - Local bus 10 - range -..- - step `1`<br>`11` - Local bus 11 - range -..- - step `1`<br>`12` - Local bus 12 - range -..- - step `1`<br>`13` - Local bus 13 - range -..- - step `1`<br>`14` - Local bus 14 - range -..- - step `1`<br>`15` - Local bus 15 - range -..- - step `1`<br>`16` - Standard - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `DEST_LEV` | Destination level | Enum | range -..- - step `1`<br>`0` - Private riser - range -..- - step `1`<br>`1` - Local bus 1 - range -..- - step `1`<br>`2` - Local bus 2 - range -..- - step `1`<br>`3` - Local bus 3 - range -..- - step `1`<br>`4` - Local bus 4 - range -..- - step `1`<br>`5` - Local bus 5 - range -..- - step `1`<br>`6` - Local bus 6 - range -..- - step `1`<br>`7` - Local bus 7 - range -..- - step `1`<br>`8` - Local bus 8 - range -..- - step `1`<br>`9` - Local bus 9 - range -..- - step `1`<br>`10` - Local bus 10 - range -..- - step `1`<br>`11` - Local bus 11 - range -..- - step `1`<br>`12` - Local bus 12 - range -..- - step `1`<br>`13` - Local bus 13 - range -..- - step `1`<br>`14` - Local bus 14 - range -..- - step `1`<br>`15` - Local bus 15 - range -..- - step `1`<br>`16` - All systems - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `A_R` | Area of reference actuator | Range | range `0`..`10` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `PL_R` | Light point of reference actuator | Range | range `0`..`15` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `IN_AUX_CHANNEL` | Input AUX channel | Range | range `0`..`15` - step `1` | visible=1, hidden=0, read-only=, type-id=0 |

### Object `403` - Scenario module control

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `M` | Modality | Enum | range -..- - step `1`<br>`0` - Scenario activation and modification - range -..- - step `1`<br>`1` - Scenario activation - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `APL` | Scenario module address | Enum | range -..- - step `1`<br>`0` - `A=0 PL=0` - range -..- - step `1`<br>`1` - `A=0 PL=1` - range -..- - step `1`<br>`2` - `A=0 PL=2` - range -..- - step `1`<br>`3` - `A=0 PL=3` - range -..- - step `1`<br>`4` - `A=0 PL=4` - range -..- - step `1`<br>`5` - `A=0 PL=5` - range -..- - step `1`<br>`6` - `A=0 PL=6` - range -..- - step `1`<br>`7` - `A=0 PL=7` - range -..- - step `1`<br>`8` - `A=0 PL=8` - range -..- - step `1`<br>`9` - `A=0 PL=9` - range -..- - step `1`<br>`10` - `A=0 PL=10` - range -..- - step `1`<br>`11` - `A=0 PL=11` - range -..- - step `1`<br>`12` - `A=0 PL=12` - range -..- - step `1`<br>`13` - `A=0 PL=13` - range -..- - step `1`<br>`14` - `A=0 PL=14` - range -..- - step `1`<br>`15` - `A=0 PL=15` - range -..- - step `1`<br>`16` - `A=1 PL=0` - range -..- - step `1`<br>`17` - `A=1 PL=1` - range -..- - step `1`<br>`18` - `A=1 PL=2` - range -..- - step `1`<br>`19` - `A=1 PL=3` - range -..- - step `1`<br>`20` - `A=1 PL=4` - range -..- - step `1`<br>`21` - `A=1 PL=5` - range -..- - step `1`<br>`22` - `A=1 PL=6` - range -..- - step `1`<br>`23` - `A=1 PL=7` - range -..- - step `1`<br>`24` - `A=1 PL=8` - range -..- - step `1`<br>`25` - `A=1 PL=9` - range -..- - step `1`<br>`26` - `A=1 PL=10` - range -..- - step `1`<br>`27` - `A=1 PL=11` - range -..- - step `1`<br>`28` - `A=1 PL=12` - range -..- - step `1`<br>`29` - `A=1 PL=13` - range -..- - step `1`<br>`30` - `A=1 PL=14` - range -..- - step `1`<br>`31` - `A=1 PL=15` - range -..- - step `1`<br>`32` - `A=2 PL=0` - range -..- - step `1`<br>`33` - `A=2 PL=1` - range -..- - step `1`<br>`34` - `A=2 PL=2` - range -..- - step `1`<br>`35` - `A=2 PL=3` - range -..- - step `1`<br>`36` - `A=2 PL=4` - range -..- - step `1`<br>`37` - `A=2 PL=5` - range -..- - step `1`<br>`38` - `A=2 PL=6` - range -..- - step `1`<br>`39` - `A=2 PL=7` - range -..- - step `1`<br>`40` - `A=2 PL=8` - range -..- - step `1`<br>`41` - `A=2 PL=9` - range -..- - step `1`<br>`42` - `A=2 PL=10` - range -..- - step `1`<br>`43` - `A=2 PL=11` - range -..- - step `1`<br>`44` - `A=2 PL=12` - range -..- - step `1`<br>`45` - `A=2 PL=13` - range -..- - step `1`<br>`46` - `A=2 PL=14` - range -..- - step `1`<br>`47` - `A=2 PL=15` - range -..- - step `1`<br>`48` - `A=3 PL=0` - range -..- - step `1`<br>`49` - `A=3 PL=1` - range -..- - step `1`<br>`50` - `A=3 PL=2` - range -..- - step `1`<br>`51` - `A=3 PL=3` - range -..- - step `1`<br>`52` - `A=3 PL=4` - range -..- - step `1`<br>`53` - `A=3 PL=5` - range -..- - step `1`<br>`54` - `A=3 PL=6` - range -..- - step `1`<br>`55` - `A=3 PL=7` - range -..- - step `1`<br>`56` - `A=3 PL=8` - range -..- - step `1`<br>`57` - `A=3 PL=9` - range -..- - step `1`<br>`58` - `A=3 PL=10` - range -..- - step `1`<br>`59` - `A=3 PL=11` - range -..- - step `1`<br>`60` - `A=3 PL=12` - range -..- - step `1`<br>`61` - `A=3 PL=13` - range -..- - step `1`<br>`62` - `A=3 PL=14` - range -..- - step `1`<br>`63` - `A=3 PL=15` - range -..- - step `1`<br>`64` - `A=4 PL=0` - range -..- - step `1`<br>`65` - `A=4 PL=1` - range -..- - step `1`<br>`66` - `A=4 PL=2` - range -..- - step `1`<br>`67` - `A=4 PL=3` - range -..- - step `1`<br>`68` - `A=4 PL=4` - range -..- - step `1`<br>`69` - `A=4 PL=5` - range -..- - step `1`<br>`70` - `A=4 PL=6` - range -..- - step `1`<br>`71` - `A=4 PL=7` - range -..- - step `1`<br>`72` - `A=4 PL=8` - range -..- - step `1`<br>`73` - `A=4 PL=9` - range -..- - step `1`<br>`74` - `A=4 PL=10` - range -..- - step `1`<br>`75` - `A=4 PL=11` - range -..- - step `1`<br>`76` - `A=4 PL=12` - range -..- - step `1`<br>`77` - `A=4 PL=13` - range -..- - step `1`<br>`78` - `A=4 PL=14` - range -..- - step `1`<br>`79` - `A=4 PL=15` - range -..- - step `1`<br>`80` - `A=5 PL=0` - range -..- - step `1`<br>`81` - `A=5 PL=1` - range -..- - step `1`<br>`82` - `A=5 PL=2` - range -..- - step `1`<br>`83` - `A=5 PL=3` - range -..- - step `1`<br>`84` - `A=5 PL=4` - range -..- - step `1`<br>`85` - `A=5 PL=5` - range -..- - step `1`<br>`86` - `A=5 PL=6` - range -..- - step `1`<br>`87` - `A=5 PL=7` - range -..- - step `1`<br>`88` - `A=5 PL=8` - range -..- - step `1`<br>`89` - `A=5 PL=9` - range -..- - step `1`<br>`90` - `A=5 PL=10` - range -..- - step `1`<br>`91` - `A=5 PL=11` - range -..- - step `1`<br>`92` - `A=5 PL=12` - range -..- - step `1`<br>`93` - `A=5 PL=13` - range -..- - step `1`<br>`94` - `A=5 PL=14` - range -..- - step `1`<br>`95` - `A=5 PL=15` - range -..- - step `1`<br>`96` - `A=6 PL=0` - range -..- - step `1`<br>`97` - `A=6 PL=1` - range -..- - step `1`<br>`98` - `A=6 PL=2` - range -..- - step `1`<br>`99` - `A=6 PL=3` - range -..- - step `1`<br>`100` - `A=6 PL=4` - range -..- - step `1`<br>`101` - `A=6 PL=5` - range -..- - step `1`<br>`102` - `A=6 PL=6` - range -..- - step `1`<br>`103` - `A=6 PL=7` - range -..- - step `1`<br>`104` - `A=6 PL=8` - range -..- - step `1`<br>`105` - `A=6 PL=9` - range -..- - step `1`<br>`106` - `A=6 PL=10` - range -..- - step `1`<br>`107` - `A=6 PL=11` - range -..- - step `1`<br>`108` - `A=6 PL=12` - range -..- - step `1`<br>`109` - `A=6 PL=13` - range -..- - step `1`<br>`110` - `A=6 PL=14` - range -..- - step `1`<br>`111` - `A=6 PL=15` - range -..- - step `1`<br>`112` - `A=7 PL=0` - range -..- - step `1`<br>`113` - `A=7 PL=1` - range -..- - step `1`<br>`114` - `A=7 PL=2` - range -..- - step `1`<br>`115` - `A=7 PL=3` - range -..- - step `1`<br>`116` - `A=7 PL=4` - range -..- - step `1`<br>`117` - `A=7 PL=5` - range -..- - step `1`<br>`118` - `A=7 PL=6` - range -..- - step `1`<br>`119` - `A=7 PL=7` - range -..- - step `1`<br>`120` - `A=7 PL=8` - range -..- - step `1`<br>`121` - `A=7 PL=9` - range -..- - step `1`<br>`122` - `A=7 PL=10` - range -..- - step `1`<br>`123` - `A=7 PL=11` - range -..- - step `1`<br>`124` - `A=7 PL=12` - range -..- - step `1`<br>`125` - `A=7 PL=13` - range -..- - step `1`<br>`126` - `A=7 PL=14` - range -..- - step `1`<br>`127` - `A=7 PL=15` - range -..- - step `1`<br>`128` - `A=8 PL=0` - range -..- - step `1`<br>`129` - `A=8 PL=1` - range -..- - step `1`<br>`130` - `A=8 PL=2` - range -..- - step `1`<br>`131` - `A=8 PL=3` - range -..- - step `1`<br>`132` - `A=8 PL=4` - range -..- - step `1`<br>`133` - `A=8 PL=5` - range -..- - step `1`<br>`134` - `A=8 PL=6` - range -..- - step `1`<br>`135` - `A=8 PL=7` - range -..- - step `1`<br>`136` - `A=8 PL=8` - range -..- - step `1`<br>`137` - `A=8 PL=9` - range -..- - step `1`<br>`138` - `A=8 PL=10` - range -..- - step `1`<br>`139` - `A=8 PL=11` - range -..- - step `1`<br>`140` - `A=8 PL=12` - range -..- - step `1`<br>`141` - `A=8 PL=13` - range -..- - step `1`<br>`142` - `A=8 PL=14` - range -..- - step `1`<br>`143` - `A=8 PL=15` - range -..- - step `1`<br>`144` - `A=9 PL=0` - range -..- - step `1`<br>`145` - `A=9 PL=1` - range -..- - step `1`<br>`146` - `A=9 PL=2` - range -..- - step `1`<br>`147` - `A=9 PL=3` - range -..- - step `1`<br>`148` - `A=9 PL=4` - range -..- - step `1`<br>`149` - `A=9 PL=5` - range -..- - step `1`<br>`150` - `A=9 PL=6` - range -..- - step `1`<br>`151` - `A=9 PL=7` - range -..- - step `1`<br>`152` - `A=9 PL=8` - range -..- - step `1`<br>`153` - `A=9 PL=9` - range -..- - step `1`<br>`154` - `A=9 PL=10` - range -..- - step `1`<br>`155` - `A=9 PL=11` - range -..- - step `1`<br>`156` - `A=9 PL=12` - range -..- - step `1`<br>`157` - `A=9 PL=13` - range -..- - step `1`<br>`158` - `A=9 PL=14` - range -..- - step `1`<br>`159` - `A=9 PL=15` - range -..- - step `1`<br>`160` - `A=10 PL=0` - range -..- - step `1`<br>`161` - `A=10 PL=1` - range -..- - step `1`<br>`162` - `A=10 PL=2` - range -..- - step `1`<br>`163` - `A=10 PL=3` - range -..- - step `1`<br>`164` - `A=10 PL=4` - range -..- - step `1`<br>`165` - `A=10 PL=5` - range -..- - step `1`<br>`166` - `A=10 PL=6` - range -..- - step `1`<br>`167` - `A=10 PL=7` - range -..- - step `1`<br>`168` - `A=10 PL=8` - range -..- - step `1`<br>`169` - `A=10 PL=9` - range -..- - step `1`<br>`170` - `A=10 PL=10` - range -..- - step `1`<br>`171` - `A=10 PL=11` - range -..- - step `1`<br>`172` - `A=10 PL=12` - range -..- - step `1`<br>`173` - `A=10 PL=13` - range -..- - step `1`<br>`174` - `A=10 PL=14` - range -..- - step `1`<br>`175` - `A=10 PL=15` - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `INST_LEV` | Installation level | Enum | range -..- - step `1` - default marker `16`<br>`0` - Private riser - range -..- - step `1`<br>`1` - Local bus 1 - range -..- - step `1`<br>`2` - Local bus 2 - range -..- - step `1`<br>`3` - Local bus 3 - range -..- - step `1`<br>`4` - Local bus 4 - range -..- - step `1`<br>`5` - Local bus 5 - range -..- - step `1`<br>`6` - Local bus 6 - range -..- - step `1`<br>`7` - Local bus 7 - range -..- - step `1`<br>`8` - Local bus 8 - range -..- - step `1`<br>`9` - Local bus 9 - range -..- - step `1`<br>`10` - Local bus 10 - range -..- - step `1`<br>`11` - Local bus 11 - range -..- - step `1`<br>`12` - Local bus 12 - range -..- - step `1`<br>`13` - Local bus 13 - range -..- - step `1`<br>`14` - Local bus 14 - range -..- - step `1`<br>`15` - Local bus 15 - range -..- - step `1`<br>`16` - Standard - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `DEST_LEV` | Destination level | Enum | range -..- - step `1`<br>`0` - Private riser - range -..- - step `1`<br>`1` - Local bus 1 - range -..- - step `1`<br>`2` - Local bus 2 - range -..- - step `1`<br>`3` - Local bus 3 - range -..- - step `1`<br>`4` - Local bus 4 - range -..- - step `1`<br>`5` - Local bus 5 - range -..- - step `1`<br>`6` - Local bus 6 - range -..- - step `1`<br>`7` - Local bus 7 - range -..- - step `1`<br>`8` - Local bus 8 - range -..- - step `1`<br>`9` - Local bus 9 - range -..- - step `1`<br>`10` - Local bus 10 - range -..- - step `1`<br>`11` - Local bus 11 - range -..- - step `1`<br>`12` - Local bus 12 - range -..- - step `1`<br>`13` - Local bus 13 - range -..- - step `1`<br>`14` - Local bus 14 - range -..- - step `1`<br>`15` - Local bus 15 - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `SCE_BUTT_1` | Upper button scenario | Range | range `1`..`16` - step `1` - default marker `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `SCE_BUTT_2` | Lower button scenario | Range | range `1`..`16` - step `1` - default marker `2` | visible=1, hidden=0, read-only=, type-id=0 |
| `DEL_BUTTON_1` | Activation delay for upper button | Enum | range -..- - step `1`<br>`0` - None - range -..- - step `1`<br>`1` - 1 s - range -..- - step `1`<br>`2` - 2 s - range -..- - step `1`<br>`3` - 3 s - range -..- - step `1`<br>`4` - 4 s - range -..- - step `1`<br>`5` - 5 s - range -..- - step `1`<br>`6` - 6 s - range -..- - step `1`<br>`7` - 7 s - range -..- - step `1`<br>`8` - 8 s - range -..- - step `1`<br>`9` - 9 s - range -..- - step `1`<br>`10` - 10 s - range -..- - step `1`<br>`11` - 11 s - range -..- - step `1`<br>`12` - 12 s - range -..- - step `1`<br>`13` - 13 s - range -..- - step `1`<br>`14` - 14 s - range -..- - step `1`<br>`15` - 15 s - range -..- - step `1`<br>`16` - 16 s - range -..- - step `1`<br>`17` - 17 s - range -..- - step `1`<br>`19` - 19 s - range -..- - step `1`<br>`20` - 20 s - range -..- - step `1`<br>`21` - 21 s - range -..- - step `1`<br>`22` - 22 s - range -..- - step `1`<br>`23` - 23 s - range -..- - step `1`<br>`24` - 24 s - range -..- - step `1`<br>`26` - 26 s - range -..- - step `1`<br>`27` - 27 s - range -..- - step `1`<br>`28` - 28 s - range -..- - step `1`<br>`29` - 29 s - range -..- - step `1`<br>`30` - 30 s - range -..- - step `1`<br>`31` - 31 s - range -..- - step `1`<br>`32` - 32 s - range -..- - step `1`<br>`33` - 33 s - range -..- - step `1`<br>`34` - 34 s - range -..- - step `1`<br>`35` - 35 s - range -..- - step `1`<br>`36` - 36 s - range -..- - step `1`<br>`37` - 37 s - range -..- - step `1`<br>`38` - 38 s - range -..- - step `1`<br>`39` - 39 s - range -..- - step `1`<br>`40` - 40 s - range -..- - step `1`<br>`43` - 43 s - range -..- - step `1`<br>`44` - 44 s - range -..- - step `1`<br>`47` - 47 s - range -..- - step `1`<br>`48` - 48 s - range -..- - step `1`<br>`49` - 49 s - range -..- - step `1`<br>`50` - 50 s - range -..- - step `1`<br>`51` - 51 s - range -..- - step `1`<br>`54` - 54 s - range -..- - step `1`<br>`55` - 55 s - range -..- - step `1`<br>`56` - 56 s - range -..- - step `1`<br>`57` - 57 s - range -..- - step `1`<br>`59` - 59 s - range -..- - step `1`<br>`60` - 60 s - range -..- - step `1`<br>`61` - 1 min 30 s - range -..- - step `1`<br>`62` - 2 min - range -..- - step `1`<br>`63` - 3 min - range -..- - step `1`<br>`64` - 4 min - range -..- - step `1`<br>`65` - 5 min - range -..- - step `1`<br>`66` - 6 min - range -..- - step `1`<br>`67` - 7 min - range -..- - step `1`<br>`68` - 8 min - range -..- - step `1`<br>`69` - 9 min - range -..- - step `1`<br>`70` - 10 min - range -..- - step `1`<br>`71` - 15 min - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `DEL_BUTTON_2` | Activation delay for lower button | Enum | range -..- - step `1`<br>`0` - None - range -..- - step `1`<br>`1` - 1 s - range -..- - step `1`<br>`2` - 2 s - range -..- - step `1`<br>`3` - 3 s - range -..- - step `1`<br>`5` - 5 s - range -..- - step `1`<br>`6` - 6 s - range -..- - step `1`<br>`7` - 7 s - range -..- - step `1`<br>`10` - 10 s - range -..- - step `1`<br>`11` - 11 s - range -..- - step `1`<br>`12` - 12 s - range -..- - step `1`<br>`14` - 14 s - range -..- - step `1`<br>`15` - 15 s - range -..- - step `1`<br>`16` - 16 s - range -..- - step `1`<br>`17` - 17 s - range -..- - step `1`<br>`19` - 19 s - range -..- - step `1`<br>`20` - 20 s - range -..- - step `1`<br>`21` - 21 s - range -..- - step `1`<br>`24` - 24 s - range -..- - step `1`<br>`25` - 25 s - range -..- - step `1`<br>`26` - 26 s - range -..- - step `1`<br>`29` - 29 s - range -..- - step `1`<br>`30` - 30 s - range -..- - step `1`<br>`31` - 31 s - range -..- - step `1`<br>`32` - 32 s - range -..- - step `1`<br>`33` - 33 s - range -..- - step `1`<br>`34` - 34 s - range -..- - step `1`<br>`36` - 36 s - range -..- - step `1`<br>`37` - 37 s - range -..- - step `1`<br>`39` - 39 s - range -..- - step `1`<br>`40` - 40 s - range -..- - step `1`<br>`41` - 41 s - range -..- - step `1`<br>`42` - 42 s - range -..- - step `1`<br>`43` - 43 s - range -..- - step `1`<br>`44` - 44 s - range -..- - step `1`<br>`45` - 45 s - range -..- - step `1`<br>`46` - 46 s - range -..- - step `1`<br>`47` - 47 s - range -..- - step `1`<br>`48` - 48 s - range -..- - step `1`<br>`49` - 49 s - range -..- - step `1`<br>`50` - 50 s - range -..- - step `1`<br>`51` - 51 s - range -..- - step `1`<br>`52` - 52 s - range -..- - step `1`<br>`53` - 53 s - range -..- - step `1`<br>`54` - 54 s - range -..- - step `1`<br>`55` - 55 s - range -..- - step `1`<br>`56` - 56 s - range -..- - step `1`<br>`60` - 60 s - range -..- - step `1`<br>`61` - 1 min 30 s - range -..- - step `1`<br>`62` - 2 min - range -..- - step `1`<br>`63` - 3 min - range -..- - step `1`<br>`64` - 4 min - range -..- - step `1`<br>`65` - 5 min - range -..- - step `1`<br>`66` - 6 min - range -..- - step `1`<br>`67` - 7 min - range -..- - step `1`<br>`69` - 9 min - range -..- - step `1`<br>`70` - 10 min - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |

The resolved Object determines whether a radio control surface acts as Lighting control, Automation control or Scenario module control. The four firmware slots do not imply four identical user controls without Object resolution.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `12` | Device/Firmware topology conditions |
| Object/Firmware filters | `1` | Conditional Object configuration exposure |
| Referenced conversion rules | `0` | None |

### Slot conditions

| Slot | Object | Condition ID | Condition expression | Conversion rule |
| ---: | ---: | ---: | --- | ---: |
| `1` | `400` | `4145` | No textual predicate - conversion-driven or unconditional catalogue row | - |
| `1` | `401` | `4305` | `M1=SU_GIU;SPE<>6` | - |
| `1` | `401` | `4313` | `M1=SU_GIU_M;SPE<>6` | - |
| `1` | `403` | `4857` | `SPE=6` | - |
| `2` | `400` | `4145` | No textual predicate - conversion-driven or unconditional catalogue row | - |
| `2` | `403` | `4899` | `SPE=7` | - |
| `3` | `400` | `4145` | No textual predicate - conversion-driven or unconditional catalogue row | - |
| `3` | `401` | `4416` | `M2=SU_GIU;SPE<>6` | - |
| `3` | `401` | `4422` | `M2=SU_GIU_M;SPE<>6` | - |
| `3` | `403` | `4874` | `SPE=8` | - |
| `4` | `400` | `4145` | No textual predicate - conversion-driven or unconditional catalogue row | - |
| `4` | `403` | `4877` | `SPE=9` | - |

### Object/Firmware filters

| Object | Filter ID | Field | Note | Whole range | Filter ranges |
| ---: | ---: | --- | --- | --- | --- |
| `403` | `1109` | `INST_LEV` | Installation level | `0` | `8` - Level 4 #8 |

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

Depending on Object and mode, the receiver can expose lighting, automation and scenario-control functions from paired batteryless radio controls.

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact technical item is currently retained.

## Programming

Preserve slot-by-slot Object selection and the complete M/SPE mode set. Do not model the receiver as a single generic pushbutton or as four unconditional Light controls.

## Source reconciliation

Publisher documentation establishes the 4575SB batteryless-radio receiver family and SCS BUS role. The canonical database explains its richer software topology: four fixed Light-control slot positions with optional Automation and Scenario Objects, plus the firmware-level PL/M/SPE configuration.

## Evidence limits and open work

- Add sanitized pairing and button-action captures for representative 4572SB controls.
- Corroborate optional Automation/Scenario Object resolution by DIM30 on hardware.
- Document the Installation level filter for Scenario module control in human-readable form.
- Pin exact printed and 1-based PDF page locations for each applicable multi-product guide citation.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf)
