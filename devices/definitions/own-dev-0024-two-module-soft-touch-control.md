# Two-module Soft Touch control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0024` | Project identity |
| Technical description | Two-module capacitive Soft Touch SCS command with configurable function and UI settings | Catalogue + official documentation |
| Catalogue item / model | `12` / `modobj 8` | Implementation evidence |
| Firmware applicability | firmware `149`, `-1.-1.-1`, two slots | Implementation evidence |
| Commercial identities | `HC/HS4653/2`, `HD4653M2` | Catalogue |
| Categories | Command, Lighting, Automation, Scenario, Sound, Access | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino / Axolute | `HC/HS4653/2` | `12` | Commercial identity of this Technical Device | Canonical catalogue |
| BTicino / Axolute | `HD4653M2` | `1553` | Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Relevant pages | Status | Source |
| --- | --- | --- | --- | --- | --- |
| AUTOMATISME.pdf | MyHOME automation guide | historical publisher guide | Soft Touch / 4653 family sections; exact printed/PDF locator pending | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) |

Multi-product guides retain an explicit page-location limitation until both printed and 1-based PDF page numbers are pinned.

## Physical and electrical characteristics

Published data gives SCS nominal `27 Vdc`, operating `18..27 Vdc`, maximum consumption `18 mA`, operating temperature `5..35 °C`, and a two-module flush-mounted form for HC/HS4653/2. LED intensity is adjustable.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `12` | Canonical catalogue |
| Technical item description | Soft touch control | Canonical catalogue |
| Item family | `1` - Control | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `8` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Declared slots | Default | Status |
| ---: | ---: | ---: | ---: | --- | --- |
| `149` | `-1` | `-1` | `2` | `1` | `0` |

Firmware `149` is wildcard `-1.-1.-1` and declares two slots.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `149` | `382` | `410` | `410` | Light control |
| `149` | `383` | `411` | `411` | Automation control |
| `149` | `384` | `412` | `412` | Lock/unlock actuator control |
| `149` | `385` | `413` | `413` | Scenario module control |
| `149` | `386` | `414` | `414` | Scheduled scenario |
| `149` | `387` | `415` | `415` | Scenario PLUS Lighting Management |
| `149` | `388` | `416` | `416` | Scheduled scenario PLUS |
| `149` | `389` | `418` | `418` | Open lock control |
| `149` | `390` | `419` | `419` | Sound diffusion control |
| `149` | `391` | `427` | `427` | Floor call control |
| `149` | `392` | `426` | `426` | Staircase light control |
| `149` | `393` | `480` | `130` | User interface settings |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `563` | `1` | `410` | fixed | Light control |
| `564` | `1` | `411` | candidate / non-fixed | Automation control |
| `565` | `1` | `412` | candidate / non-fixed | Lock/unlock actuator control |
| `566` | `1` | `413` | candidate / non-fixed | Scenario module control |
| `567` | `1` | `414` | candidate / non-fixed | Scheduled scenario |
| `568` | `1` | `415` | candidate / non-fixed | Scenario PLUS Lighting Management |
| `569` | `1` | `416` | candidate / non-fixed | Scheduled scenario PLUS |
| `570` | `1` | `418` | candidate / non-fixed | Open lock control |
| `571` | `1` | `419` | candidate / non-fixed | Sound diffusion control |
| `572` | `1` | `427` | candidate / non-fixed | Floor call control |
| `573` | `1` | `426` | candidate / non-fixed | Staircase light control |
| `574` | `2` | `480` | fixed | User interface settings |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| `149` | `23` | `521` | `521` | Soft-Touch command virgin | `410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `418`, `419`, `421`, `426`, `427`, `489` | `1` |

Slot `1` is the configurable command surface. Direct candidates are Objects `410`, `411`, `412`, `413`, `414`, `415`, `416`, `418`, `419`, `426`, and `427`. Virgin Object `521`, Soft-Touch command virgin, additionally permits AUX `417`, cyclic autoswitch `421`, and Open-lock-on-session `462`. Slot `2` is fixed Object `130`, User interface settings. It is not a second command channel.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `149` | `1` | `1` | Virtual Configuration |
| `149` | `2` | `2` | Advanced Configuration |
| `149` | `3` | `0` | Physical configuration |

Physical configuration, Virtual Configuration and Advanced Configuration.

## Firmware-scoped configuration

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `AID` | ID | user_value | `********` - AID - range `0`..`0` - step `1` | visible=1, hidden=0, read-only=0, type-id=0 |
| `A` | A | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1`<br>`1` - 1 - range -..- - step `1`<br>`2` - 2 - range -..- - step `1`<br>`3` - 3 - range -..- - step `1`<br>`4` - 4 - range -..- - step `1`<br>`5` - 5 - range -..- - step `1`<br>`6` - 6 - range -..- - step `1`<br>`7` - 7 - range -..- - step `1`<br>`8` - 8 - range -..- - step `1`<br>`9` - 9 - range -..- - step `1`<br>`12` - GEN - range -..- - step `1`<br>`13` - GR - range -..- - step `1`<br>`14` - AMB - range -..- - step `1`<br>`15` - AUX - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `PL` | PL | Range | range `0`..`9` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `M` | M | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1`<br>`1` - 1 - range -..- - step `1`<br>`2` - 2 - range -..- - step `1`<br>`3` - 3 - range -..- - step `1`<br>`4` - 4 - range -..- - step `1`<br>`5` - 5 - range -..- - step `1`<br>`6` - 6 - range -..- - step `1`<br>`7` - 7 - range -..- - step `1`<br>`8` - 8 - range -..- - step `1`<br>`9` - 9 - range -..- - step `1`<br>`14` - CEN - range -..- - step `1`<br>`10` - OFF - range -..- - step `1`<br>`11` - ON - range -..- - step `1`<br>`15` - PUL - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `M2` | M2 | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1`<br>`1` - 1 - range -..- - step `1`<br>`2` - 2 - range -..- - step `1`<br>`3` - 3 - range -..- - step `1`<br>`4` - 4 - range -..- - step `1`<br>`5` - 5 - range -..- - step `1`<br>`6` - 6 - range -..- - step `1`<br>`7` - 7 - range -..- - step `1`<br>`8` - 8 - range -..- - step `1`<br>`9` - 9 - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `SPE` | SPE | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1`<br>`1` - 1 - range -..- - step `1`<br>`2` - 2 - range -..- - step `1`<br>`3` - 3 - range -..- - step `1`<br>`4` - 4 - range -..- - step `1`<br>`6` - 6 - range -..- - step `1`<br>`7` - 7 - range -..- - step `1`<br>`8` - 8 - range -..- - step `1`<br>`9` - 9 - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `INT` | INT | Enum | range -..- - step `1`<br>`0` - 0 - range -..- - step `1`<br>`1` - 1 - range -..- - step `1`<br>`10` - OFF - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |

Catalogue range rows are preserved directly; product-document physical configurator limits remain a distinct evidence layer.

`A` supports `0..9`, `GEN`, `GR`, `AMB`, `AUX`; `PL` is `0..9`; `M` supports `0..9`, `OFF`, `ON`, `CEN`, `PUL`; `M2` is `0..9`; `SPE` supports default and `0,1,2,3,4,6,7,8,9`; `INT` supports default, `0`, `1`, `OFF`; `AID` is the identity field.

## Object configuration surfaces

### Object `410` - Light control

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `M` | Modality | Enum | range -..- - step `1`<br>`0` - Toggle - range -..- - step `1`<br>`1` - Timed ON - range -..- - step `1`<br>`2` - Toggle dimmer - range -..- - step `1`<br>`4` - Toggle ON/OFF - range -..- - step `1`<br>`10` - OFF - range -..- - step `1`<br>`11` - ON - range -..- - step `1`<br>`15` - PUL - range -..- - step `1`<br>`20` - ON and point to point dimmer - range -..- - step `1`<br>`21` - OFF and point to point dimmer - range -..- - step `1`<br>`22` - ON and Dimmer - range -..- - step `1`<br>`23` - OFF and Dimmer - range -..- - step `1`<br>`32` - Blinking 0.5 s - range -..- - step `1`<br>`33` - Blinking 1 s - range -..- - step `1`<br>`34` - Blinking 1.5 s - range -..- - step `1`<br>`35` - Blinking 2 s - range -..- - step `1`<br>`36` - Blinking 2.5 s - range -..- - step `1`<br>`37` - Blinking 3 s - range -..- - step `1`<br>`38` - Blinking 3.5 s - range -..- - step `1`<br>`39` - Blinking 4 s - range -..- - step `1`<br>`40` - Blinking 4.5 s - range -..- - step `1`<br>`41` - Blinking 5 s - range -..- - step `1`<br>`42` - Blinking 5.5 s - range -..- - step `1`<br>`43` - Blinking 6 s - range -..- - step `1`<br>`44` - Blinking 6.5 s - range -..- - step `1`<br>`45` - Blinking 7 s - range -..- - step `1`<br>`46` - Blinking 7.5 s - range -..- - step `1`<br>`47` - Blinking 8 s - range -..- - step `1`<br>`49` - ON dimmer 10% - range -..- - step `1`<br>`50` - ON dimmer 20% - range -..- - step `1`<br>`51` - ON dimmer 30% - range -..- - step `1`<br>`52` - ON dimmer 40% - range -..- - step `1`<br>`53` - ON dimmer 50% - range -..- - step `1`<br>`54` - ON dimmer 60% - range -..- - step `1`<br>`55` - ON dimmer 70% - range -..- - step `1`<br>`56` - ON dimmer 80% - range -..- - step `1`<br>`57` - ON dimmer 90% - range -..- - step `1`<br>`128` - Customized timed ON - range -..- - step `1`<br>`129` - Customized toggle and point to point dimmer - range -..- - step `1`<br>`131` - Customized toggle dimmer - range -..- - step `1`<br>`133` - Customized toggle dimmer without regulation - range -..- - step `1`<br>`135` - Customized ON and dimmer without regulation - range -..- - step `1`<br>`136` - Customized OFF and dimmer without regulation - range -..- - step `1`<br>`137` - Customized ON and dimmer with regulation - range -..- - step `1`<br>`138` - Customized OFF and dimmer with regulation - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `ADDR_TYPE` | Addressing type | Enum | range -..- - step `1`<br>`0` - Point to point - range -..- - step `1`<br>`1` - Area - range -..- - step `1`<br>`2` - Group - range -..- - step `1`<br>`3` - General - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `A` | Area | Range | range `0`..`10` - step `1` | visible=1, hidden=1, read-only=, type-id=0 |
| `PL` | Light point | Range | range `0`..`15` - step `1` | visible=1, hidden=1, read-only=, type-id=0 |
| `G` | Group | Range | range `1`..`255` - step `1` - default marker `1` | visible=1, hidden=1, read-only=, type-id=3 |
| `INST_LEV` | Installation level | Enum | range -..- - step `1` - default marker `16`<br>`0` - Private riser - range -..- - step `1`<br>`1` - Local bus 1 - range -..- - step `1`<br>`2` - Local bus 2 - range -..- - step `1`<br>`3` - Local bus 3 - range -..- - step `1`<br>`4` - Local bus 4 - range -..- - step `1`<br>`5` - Local bus 5 - range -..- - step `1`<br>`6` - Local bus 6 - range -..- - step `1`<br>`7` - Local bus 7 - range -..- - step `1`<br>`8` - Local bus 8 - range -..- - step `1`<br>`9` - Local bus 9 - range -..- - step `1`<br>`10` - Local bus 10 - range -..- - step `1`<br>`11` - Local bus 11 - range -..- - step `1`<br>`12` - Local bus 12 - range -..- - step `1`<br>`13` - Local bus 13 - range -..- - step `1`<br>`14` - Local bus 14 - range -..- - step `1`<br>`15` - Local bus 15 - range -..- - step `1`<br>`16` - Standard - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `DEST_LEV` | Destination level | Enum | range -..- - step `1`<br>`0` - Private riser - range -..- - step `1`<br>`1` - Local bus 1 - range -..- - step `1`<br>`2` - Local bus 2 - range -..- - step `1`<br>`3` - Local bus 3 - range -..- - step `1`<br>`4` - Local bus 4 - range -..- - step `1`<br>`5` - Local bus 5 - range -..- - step `1`<br>`6` - Local bus 6 - range -..- - step `1`<br>`7` - Local bus 7 - range -..- - step `1`<br>`8` - Local bus 8 - range -..- - step `1`<br>`9` - Local bus 9 - range -..- - step `1`<br>`10` - Local bus 10 - range -..- - step `1`<br>`11` - Local bus 11 - range -..- - step `1`<br>`12` - Local bus 12 - range -..- - step `1`<br>`13` - Local bus 13 - range -..- - step `1`<br>`14` - Local bus 14 - range -..- - step `1`<br>`15` - Local bus 15 - range -..- - step `1`<br>`16` - All systems - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `A_R` | Area of reference actuator | Range | range `0`..`10` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `PL_R` | Light point of reference actuator | Range | range `0`..`15` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `TYPE_CONTACT` | Contact type | Enum | range -..- - step `1`<br>`0` - Normally open - range -..- - step `1`<br>`1` - Normally closed - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `HOURS` | Hours | Range | range `0`..`255` - step `1` | visible=1, hidden=1, read-only=, type-id=0 |
| `MINUTES` | Minutes | Range | range `0`..`59` - step `1` | visible=1, hidden=1, read-only=, type-id=0 |
| `SECONDS` | Seconds | Range | range `0`..`59` - step `1` - default marker `30` | visible=1, hidden=1, read-only=, type-id=0 |
| `LEVEL` | Level | Range | range `0`..`100` - step `1` - default marker `100` | visible=1, hidden=1, read-only=, type-id= |
| `START_S` | Soft start speed | Range | range `0`..`255` - step `1` - default marker `255` | visible=1, hidden=1, read-only=, type-id=0 |
| `STOP_S` | Soft stop speed | Range | range `0`..`255` - step `1` - default marker `255` | visible=1, hidden=1, read-only=, type-id=0 |
| `DIMMING_S` | Dimming speed | Range | range `0`..`255` - step `1` - default marker `255` | visible=1, hidden=1, read-only=, type-id=0 |
| `T_TIME` | Tabled time | Enum | range -..- - step `1` - default marker `1`<br>`1` - 1 min - range -..- - step `1`<br>`2` - 2 min - range -..- - step `1`<br>`3` - 3 min - range -..- - step `1`<br>`4` - 4 min - range -..- - step `1`<br>`5` - 5 min - range -..- - step `1`<br>`6` - 15 min - range -..- - step `1`<br>`7` - 30 s - range -..- - step `1`<br>`8` - 0.5 s - range -..- - step `1`<br>`9` - 2 s - range -..- - step `1`<br>`10` - 10 min - range -..- - step `1` | visible=1, hidden=1, read-only=, type-id=0 |

### Object `411` - Automation control

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `M` | Modality | Enum | range -..- - step `1`<br>`0` - UP bistable control - range -..- - step `1`<br>`1` - DOWN bistable control - range -..- - step `1`<br>`2` - UP monostable control - range -..- - step `1`<br>`3` - DOWN monostable control - range -..- - step `1`<br>`4` - UP monostable and bistable control - range -..- - step `1`<br>`5` - DOWN monostable and bistable control - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `ADDR_TYPE` | Addressing type | Enum | range -..- - step `1`<br>`0` - Point to point - range -..- - step `1`<br>`1` - Area - range -..- - step `1`<br>`2` - Group - range -..- - step `1`<br>`3` - General - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `A` | Area | Range | range `0`..`10` - step `1` | visible=1, hidden=1, read-only=, type-id=0 |
| `PL` | Light point | Range | range `0`..`15` - step `1` | visible=1, hidden=1, read-only=, type-id=0 |
| `G` | Group | Range | range `1`..`255` - step `1` - default marker `1` | visible=1, hidden=1, read-only=, type-id=3 |
| `INST_LEV` | Installation level | Enum | range -..- - step `1` - default marker `16`<br>`0` - Private riser - range -..- - step `1`<br>`1` - Local bus 1 - range -..- - step `1`<br>`2` - Local bus 2 - range -..- - step `1`<br>`3` - Local bus 3 - range -..- - step `1`<br>`4` - Local bus 4 - range -..- - step `1`<br>`5` - Local bus 5 - range -..- - step `1`<br>`6` - Local bus 6 - range -..- - step `1`<br>`7` - Local bus 7 - range -..- - step `1`<br>`8` - Local bus 8 - range -..- - step `1`<br>`9` - Local bus 9 - range -..- - step `1`<br>`10` - Local bus 10 - range -..- - step `1`<br>`11` - Local bus 11 - range -..- - step `1`<br>`12` - Local bus 12 - range -..- - step `1`<br>`13` - Local bus 13 - range -..- - step `1`<br>`14` - Local bus 14 - range -..- - step `1`<br>`15` - Local bus 15 - range -..- - step `1`<br>`16` - Standard - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `DEST_LEV` | Destination level | Enum | range -..- - step `1`<br>`0` - Private riser - range -..- - step `1`<br>`1` - Local bus 1 - range -..- - step `1`<br>`2` - Local bus 2 - range -..- - step `1`<br>`3` - Local bus 3 - range -..- - step `1`<br>`4` - Local bus 4 - range -..- - step `1`<br>`5` - Local bus 5 - range -..- - step `1`<br>`6` - Local bus 6 - range -..- - step `1`<br>`7` - Local bus 7 - range -..- - step `1`<br>`8` - Local bus 8 - range -..- - step `1`<br>`9` - Local bus 9 - range -..- - step `1`<br>`10` - Local bus 10 - range -..- - step `1`<br>`11` - Local bus 11 - range -..- - step `1`<br>`12` - Local bus 12 - range -..- - step `1`<br>`13` - Local bus 13 - range -..- - step `1`<br>`14` - Local bus 14 - range -..- - step `1`<br>`15` - Local bus 15 - range -..- - step `1`<br>`16` - All systems - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `A_R` | Area of reference actuator | Range | range `0`..`10` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `PL_R` | Light point of reference actuator | Range | range `0`..`15` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `TYPE_CONTACT` | Contact type | Enum | range -..- - step `1`<br>`0` - Normally open - range -..- - step `1`<br>`1` - Normally closed - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |

### Object `412` - Lock/unlock actuator control

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `M` | Modality | Enum | range -..- - step `1` - default marker `1`<br>`1` - Disable - range -..- - step `1`<br>`2` - Enable - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `ADDR_TYPE` | Addressing type | Enum | range -..- - step `1`<br>`0` - Point to point - range -..- - step `1`<br>`1` - Area - range -..- - step `1`<br>`2` - Group - range -..- - step `1`<br>`3` - General - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `A` | Area | Range | range `0`..`10` - step `1` | visible=1, hidden=1, read-only=, type-id=0 |
| `PL` | Light point | Range | range `0`..`15` - step `1` | visible=1, hidden=1, read-only=, type-id=0 |
| `G` | Group | Range | range `1`..`255` - step `1` - default marker `1` | visible=1, hidden=1, read-only=, type-id=3 |
| `INST_LEV` | Installation level | Enum | range -..- - step `1` - default marker `16`<br>`0` - Private riser - range -..- - step `1`<br>`1` - Local bus 1 - range -..- - step `1`<br>`2` - Local bus 2 - range -..- - step `1`<br>`3` - Local bus 3 - range -..- - step `1`<br>`4` - Local bus 4 - range -..- - step `1`<br>`5` - Local bus 5 - range -..- - step `1`<br>`6` - Local bus 6 - range -..- - step `1`<br>`7` - Local bus 7 - range -..- - step `1`<br>`8` - Local bus 8 - range -..- - step `1`<br>`9` - Local bus 9 - range -..- - step `1`<br>`10` - Local bus 10 - range -..- - step `1`<br>`11` - Local bus 11 - range -..- - step `1`<br>`12` - Local bus 12 - range -..- - step `1`<br>`13` - Local bus 13 - range -..- - step `1`<br>`14` - Local bus 14 - range -..- - step `1`<br>`15` - Local bus 15 - range -..- - step `1`<br>`16` - Standard - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `DEST_LEV` | Destination level | Enum | range -..- - step `1`<br>`0` - Private riser - range -..- - step `1`<br>`1` - Local bus 1 - range -..- - step `1`<br>`2` - Local bus 2 - range -..- - step `1`<br>`3` - Local bus 3 - range -..- - step `1`<br>`4` - Local bus 4 - range -..- - step `1`<br>`5` - Local bus 5 - range -..- - step `1`<br>`6` - Local bus 6 - range -..- - step `1`<br>`7` - Local bus 7 - range -..- - step `1`<br>`8` - Local bus 8 - range -..- - step `1`<br>`9` - Local bus 9 - range -..- - step `1`<br>`10` - Local bus 10 - range -..- - step `1`<br>`11` - Local bus 11 - range -..- - step `1`<br>`12` - Local bus 12 - range -..- - step `1`<br>`13` - Local bus 13 - range -..- - step `1`<br>`14` - Local bus 14 - range -..- - step `1`<br>`15` - Local bus 15 - range -..- - step `1`<br>`16` - All systems - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `TYPE_CONTACT` | Contact type | Enum | range -..- - step `1`<br>`0` - Normally open - range -..- - step `1`<br>`1` - Normally closed - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |

### Object `413` - Scenario module control

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `M` | Modality | Enum | range -..- - step `1`<br>`0` - Scenario activation and modification - range -..- - step `1`<br>`1` - Scenario activation - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `APL` | Scenario module address | Enum | range -..- - step `1`<br>`0` - `A=0 PL=0` - range -..- - step `1`<br>`1` - `A=0 PL=1` - range -..- - step `1`<br>`2` - `A=0 PL=2` - range -..- - step `1`<br>`3` - `A=0 PL=3` - range -..- - step `1`<br>`4` - `A=0 PL=4` - range -..- - step `1`<br>`5` - `A=0 PL=5` - range -..- - step `1`<br>`6` - `A=0 PL=6` - range -..- - step `1`<br>`7` - `A=0 PL=7` - range -..- - step `1`<br>`8` - `A=0 PL=8` - range -..- - step `1`<br>`9` - `A=0 PL=9` - range -..- - step `1`<br>`10` - `A=0 PL=10` - range -..- - step `1`<br>`11` - `A=0 PL=11` - range -..- - step `1`<br>`12` - `A=0 PL=12` - range -..- - step `1`<br>`13` - `A=0 PL=13` - range -..- - step `1`<br>`14` - `A=0 PL=14` - range -..- - step `1`<br>`15` - `A=0 PL=15` - range -..- - step `1`<br>`16` - `A=1 PL=0` - range -..- - step `1`<br>`17` - `A=1 PL=1` - range -..- - step `1`<br>`18` - `A=1 PL=2` - range -..- - step `1`<br>`19` - `A=1 PL=3` - range -..- - step `1`<br>`20` - `A=1 PL=4` - range -..- - step `1`<br>`21` - `A=1 PL=5` - range -..- - step `1`<br>`22` - `A=1 PL=6` - range -..- - step `1`<br>`23` - `A=1 PL=7` - range -..- - step `1`<br>`24` - `A=1 PL=8` - range -..- - step `1`<br>`25` - `A=1 PL=9` - range -..- - step `1`<br>`26` - `A=1 PL=10` - range -..- - step `1`<br>`27` - `A=1 PL=11` - range -..- - step `1`<br>`28` - `A=1 PL=12` - range -..- - step `1`<br>`29` - `A=1 PL=13` - range -..- - step `1`<br>`30` - `A=1 PL=14` - range -..- - step `1`<br>`31` - `A=1 PL=15` - range -..- - step `1`<br>`32` - `A=2 PL=0` - range -..- - step `1`<br>`33` - `A=2 PL=1` - range -..- - step `1`<br>`34` - `A=2 PL=2` - range -..- - step `1`<br>`35` - `A=2 PL=3` - range -..- - step `1`<br>`36` - `A=2 PL=4` - range -..- - step `1`<br>`37` - `A=2 PL=5` - range -..- - step `1`<br>`38` - `A=2 PL=6` - range -..- - step `1`<br>`39` - `A=2 PL=7` - range -..- - step `1`<br>`40` - `A=2 PL=8` - range -..- - step `1`<br>`41` - `A=2 PL=9` - range -..- - step `1`<br>`42` - `A=2 PL=10` - range -..- - step `1`<br>`43` - `A=2 PL=11` - range -..- - step `1`<br>`44` - `A=2 PL=12` - range -..- - step `1`<br>`45` - `A=2 PL=13` - range -..- - step `1`<br>`46` - `A=2 PL=14` - range -..- - step `1`<br>`47` - `A=2 PL=15` - range -..- - step `1`<br>`48` - `A=3 PL=0` - range -..- - step `1`<br>`49` - `A=3 PL=1` - range -..- - step `1`<br>`50` - `A=3 PL=2` - range -..- - step `1`<br>`51` - `A=3 PL=3` - range -..- - step `1`<br>`52` - `A=3 PL=4` - range -..- - step `1`<br>`53` - `A=3 PL=5` - range -..- - step `1`<br>`54` - `A=3 PL=6` - range -..- - step `1`<br>`55` - `A=3 PL=7` - range -..- - step `1`<br>`56` - `A=3 PL=8` - range -..- - step `1`<br>`57` - `A=3 PL=9` - range -..- - step `1`<br>`58` - `A=3 PL=10` - range -..- - step `1`<br>`59` - `A=3 PL=11` - range -..- - step `1`<br>`60` - `A=3 PL=12` - range -..- - step `1`<br>`61` - `A=3 PL=13` - range -..- - step `1`<br>`62` - `A=3 PL=14` - range -..- - step `1`<br>`63` - `A=3 PL=15` - range -..- - step `1`<br>`64` - `A=4 PL=0` - range -..- - step `1`<br>`65` - `A=4 PL=1` - range -..- - step `1`<br>`66` - `A=4 PL=2` - range -..- - step `1`<br>`67` - `A=4 PL=3` - range -..- - step `1`<br>`68` - `A=4 PL=4` - range -..- - step `1`<br>`69` - `A=4 PL=5` - range -..- - step `1`<br>`70` - `A=4 PL=6` - range -..- - step `1`<br>`71` - `A=4 PL=7` - range -..- - step `1`<br>`72` - `A=4 PL=8` - range -..- - step `1`<br>`73` - `A=4 PL=9` - range -..- - step `1`<br>`74` - `A=4 PL=10` - range -..- - step `1`<br>`75` - `A=4 PL=11` - range -..- - step `1`<br>`76` - `A=4 PL=12` - range -..- - step `1`<br>`77` - `A=4 PL=13` - range -..- - step `1`<br>`78` - `A=4 PL=14` - range -..- - step `1`<br>`79` - `A=4 PL=15` - range -..- - step `1`<br>`80` - `A=5 PL=0` - range -..- - step `1`<br>`81` - `A=5 PL=1` - range -..- - step `1`<br>`82` - `A=5 PL=2` - range -..- - step `1`<br>`83` - `A=5 PL=3` - range -..- - step `1`<br>`84` - `A=5 PL=4` - range -..- - step `1`<br>`85` - `A=5 PL=5` - range -..- - step `1`<br>`86` - `A=5 PL=6` - range -..- - step `1`<br>`87` - `A=5 PL=7` - range -..- - step `1`<br>`88` - `A=5 PL=8` - range -..- - step `1`<br>`89` - `A=5 PL=9` - range -..- - step `1`<br>`90` - `A=5 PL=10` - range -..- - step `1`<br>`91` - `A=5 PL=11` - range -..- - step `1`<br>`92` - `A=5 PL=12` - range -..- - step `1`<br>`93` - `A=5 PL=13` - range -..- - step `1`<br>`94` - `A=5 PL=14` - range -..- - step `1`<br>`95` - `A=5 PL=15` - range -..- - step `1`<br>`96` - `A=6 PL=0` - range -..- - step `1`<br>`97` - `A=6 PL=1` - range -..- - step `1`<br>`98` - `A=6 PL=2` - range -..- - step `1`<br>`99` - `A=6 PL=3` - range -..- - step `1`<br>`100` - `A=6 PL=4` - range -..- - step `1`<br>`101` - `A=6 PL=5` - range -..- - step `1`<br>`102` - `A=6 PL=6` - range -..- - step `1`<br>`103` - `A=6 PL=7` - range -..- - step `1`<br>`104` - `A=6 PL=8` - range -..- - step `1`<br>`105` - `A=6 PL=9` - range -..- - step `1`<br>`106` - `A=6 PL=10` - range -..- - step `1`<br>`107` - `A=6 PL=11` - range -..- - step `1`<br>`108` - `A=6 PL=12` - range -..- - step `1`<br>`109` - `A=6 PL=13` - range -..- - step `1`<br>`110` - `A=6 PL=14` - range -..- - step `1`<br>`111` - `A=6 PL=15` - range -..- - step `1`<br>`112` - `A=7 PL=0` - range -..- - step `1`<br>`113` - `A=7 PL=1` - range -..- - step `1`<br>`114` - `A=7 PL=2` - range -..- - step `1`<br>`115` - `A=7 PL=3` - range -..- - step `1`<br>`116` - `A=7 PL=4` - range -..- - step `1`<br>`117` - `A=7 PL=5` - range -..- - step `1`<br>`118` - `A=7 PL=6` - range -..- - step `1`<br>`119` - `A=7 PL=7` - range -..- - step `1`<br>`120` - `A=7 PL=8` - range -..- - step `1`<br>`121` - `A=7 PL=9` - range -..- - step `1`<br>`122` - `A=7 PL=10` - range -..- - step `1`<br>`123` - `A=7 PL=11` - range -..- - step `1`<br>`124` - `A=7 PL=12` - range -..- - step `1`<br>`125` - `A=7 PL=13` - range -..- - step `1`<br>`126` - `A=7 PL=14` - range -..- - step `1`<br>`127` - `A=7 PL=15` - range -..- - step `1`<br>`128` - `A=8 PL=0` - range -..- - step `1`<br>`129` - `A=8 PL=1` - range -..- - step `1`<br>`130` - `A=8 PL=2` - range -..- - step `1`<br>`131` - `A=8 PL=3` - range -..- - step `1`<br>`132` - `A=8 PL=4` - range -..- - step `1`<br>`133` - `A=8 PL=5` - range -..- - step `1`<br>`134` - `A=8 PL=6` - range -..- - step `1`<br>`135` - `A=8 PL=7` - range -..- - step `1`<br>`136` - `A=8 PL=8` - range -..- - step `1`<br>`137` - `A=8 PL=9` - range -..- - step `1`<br>`138` - `A=8 PL=10` - range -..- - step `1`<br>`139` - `A=8 PL=11` - range -..- - step `1`<br>`140` - `A=8 PL=12` - range -..- - step `1`<br>`141` - `A=8 PL=13` - range -..- - step `1`<br>`142` - `A=8 PL=14` - range -..- - step `1`<br>`143` - `A=8 PL=15` - range -..- - step `1`<br>`144` - `A=9 PL=0` - range -..- - step `1`<br>`145` - `A=9 PL=1` - range -..- - step `1`<br>`146` - `A=9 PL=2` - range -..- - step `1`<br>`147` - `A=9 PL=3` - range -..- - step `1`<br>`148` - `A=9 PL=4` - range -..- - step `1`<br>`149` - `A=9 PL=5` - range -..- - step `1`<br>`150` - `A=9 PL=6` - range -..- - step `1`<br>`151` - `A=9 PL=7` - range -..- - step `1`<br>`152` - `A=9 PL=8` - range -..- - step `1`<br>`153` - `A=9 PL=9` - range -..- - step `1`<br>`154` - `A=9 PL=10` - range -..- - step `1`<br>`155` - `A=9 PL=11` - range -..- - step `1`<br>`156` - `A=9 PL=12` - range -..- - step `1`<br>`157` - `A=9 PL=13` - range -..- - step `1`<br>`158` - `A=9 PL=14` - range -..- - step `1`<br>`159` - `A=9 PL=15` - range -..- - step `1`<br>`160` - `A=10 PL=0` - range -..- - step `1`<br>`161` - `A=10 PL=1` - range -..- - step `1`<br>`162` - `A=10 PL=2` - range -..- - step `1`<br>`163` - `A=10 PL=3` - range -..- - step `1`<br>`164` - `A=10 PL=4` - range -..- - step `1`<br>`165` - `A=10 PL=5` - range -..- - step `1`<br>`166` - `A=10 PL=6` - range -..- - step `1`<br>`167` - `A=10 PL=7` - range -..- - step `1`<br>`168` - `A=10 PL=8` - range -..- - step `1`<br>`169` - `A=10 PL=9` - range -..- - step `1`<br>`170` - `A=10 PL=10` - range -..- - step `1`<br>`171` - `A=10 PL=11` - range -..- - step `1`<br>`172` - `A=10 PL=12` - range -..- - step `1`<br>`173` - `A=10 PL=13` - range -..- - step `1`<br>`174` - `A=10 PL=14` - range -..- - step `1`<br>`175` - `A=10 PL=15` - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `INST_LEV` | Installation level | Enum | range -..- - step `1` - default marker `16`<br>`0` - Private riser - range -..- - step `1`<br>`1` - Local bus 1 - range -..- - step `1`<br>`2` - Local bus 2 - range -..- - step `1`<br>`3` - Local bus 3 - range -..- - step `1`<br>`4` - Local bus 4 - range -..- - step `1`<br>`5` - Local bus 5 - range -..- - step `1`<br>`6` - Local bus 6 - range -..- - step `1`<br>`7` - Local bus 7 - range -..- - step `1`<br>`8` - Local bus 8 - range -..- - step `1`<br>`9` - Local bus 9 - range -..- - step `1`<br>`10` - Local bus 10 - range -..- - step `1`<br>`11` - Local bus 11 - range -..- - step `1`<br>`12` - Local bus 12 - range -..- - step `1`<br>`13` - Local bus 13 - range -..- - step `1`<br>`14` - Local bus 14 - range -..- - step `1`<br>`15` - Local bus 15 - range -..- - step `1`<br>`16` - Standard - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `DEST_LEV` | Destination level | Enum | range -..- - step `1`<br>`0` - Private riser - range -..- - step `1`<br>`1` - Local bus 1 - range -..- - step `1`<br>`2` - Local bus 2 - range -..- - step `1`<br>`3` - Local bus 3 - range -..- - step `1`<br>`4` - Local bus 4 - range -..- - step `1`<br>`5` - Local bus 5 - range -..- - step `1`<br>`6` - Local bus 6 - range -..- - step `1`<br>`7` - Local bus 7 - range -..- - step `1`<br>`8` - Local bus 8 - range -..- - step `1`<br>`9` - Local bus 9 - range -..- - step `1`<br>`10` - Local bus 10 - range -..- - step `1`<br>`11` - Local bus 11 - range -..- - step `1`<br>`12` - Local bus 12 - range -..- - step `1`<br>`13` - Local bus 13 - range -..- - step `1`<br>`14` - Local bus 14 - range -..- - step `1`<br>`15` - Local bus 15 - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `TYPE_CONTACT` | Contact type | Enum | range -..- - step `1`<br>`0` - Normally open - range -..- - step `1`<br>`1` - Normally closed - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `SCE_BUTT_1` | Scenario number | Range | range `1`..`16` - step `1` - default marker `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `DEL_BUTTON_1` | Activation delay of scenario number | Enum | range -..- - step `1`<br>`0` - None - range -..- - step `1`<br>`1` - 1 s - range -..- - step `1`<br>`2` - 2 s - range -..- - step `1`<br>`3` - 3 s - range -..- - step `1`<br>`4` - 4 s - range -..- - step `1`<br>`5` - 5 s - range -..- - step `1`<br>`6` - 6 s - range -..- - step `1`<br>`7` - 7 s - range -..- - step `1`<br>`8` - 8 s - range -..- - step `1`<br>`9` - 9 s - range -..- - step `1`<br>`10` - 10 s - range -..- - step `1`<br>`11` - 11 s - range -..- - step `1`<br>`12` - 12 s - range -..- - step `1`<br>`13` - 13 s - range -..- - step `1`<br>`14` - 14 s - range -..- - step `1`<br>`15` - 15 s - range -..- - step `1`<br>`16` - 16 s - range -..- - step `1`<br>`17` - 17 s - range -..- - step `1`<br>`18` - 18 s - range -..- - step `1`<br>`19` - 19 s - range -..- - step `1`<br>`20` - 20 s - range -..- - step `1`<br>`21` - 21 s - range -..- - step `1`<br>`22` - 22 s - range -..- - step `1`<br>`23` - 23 s - range -..- - step `1`<br>`24` - 24 s - range -..- - step `1`<br>`25` - 25 s - range -..- - step `1`<br>`26` - 26 s - range -..- - step `1`<br>`27` - 27 s - range -..- - step `1`<br>`28` - 28 s - range -..- - step `1`<br>`29` - 29 s - range -..- - step `1`<br>`30` - 30 s - range -..- - step `1`<br>`31` - 31 s - range -..- - step `1`<br>`32` - 32 s - range -..- - step `1`<br>`33` - 33 s - range -..- - step `1`<br>`34` - 34 s - range -..- - step `1`<br>`35` - 35 s - range -..- - step `1`<br>`36` - 36 s - range -..- - step `1`<br>`37` - 37 s - range -..- - step `1`<br>`38` - 38 s - range -..- - step `1`<br>`39` - 39 s - range -..- - step `1`<br>`40` - 40 s - range -..- - step `1`<br>`41` - 41 s - range -..- - step `1`<br>`42` - 42 s - range -..- - step `1`<br>`43` - 43 s - range -..- - step `1`<br>`44` - 44 s - range -..- - step `1`<br>`45` - 45 s - range -..- - step `1`<br>`46` - 46 s - range -..- - step `1`<br>`47` - 47 s - range -..- - step `1`<br>`48` - 48 s - range -..- - step `1`<br>`49` - 49 s - range -..- - step `1`<br>`50` - 50 s - range -..- - step `1`<br>`51` - 51 s - range -..- - step `1`<br>`52` - 52 s - range -..- - step `1`<br>`53` - 53 s - range -..- - step `1`<br>`54` - 54 s - range -..- - step `1`<br>`55` - 55 s - range -..- - step `1`<br>`56` - 56 s - range -..- - step `1`<br>`57` - 57 s - range -..- - step `1`<br>`58` - 58 s - range -..- - step `1`<br>`59` - 59 s - range -..- - step `1`<br>`60` - 60 s - range -..- - step `1`<br>`61` - 1 min 30 s - range -..- - step `1`<br>`62` - 2 min - range -..- - step `1`<br>`63` - 3 min - range -..- - step `1`<br>`64` - 4 min - range -..- - step `1`<br>`65` - 5 min - range -..- - step `1`<br>`66` - 6 min - range -..- - step `1`<br>`67` - 7 min - range -..- - step `1`<br>`68` - 8 min - range -..- - step `1`<br>`69` - 9 min - range -..- - step `1`<br>`70` - 10 min - range -..- - step `1`<br>`71` - 15 min - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |

### Object `414` - Scheduled scenario

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `A` | Area | Range | range `0`..`10` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `PL` | Light point | Range | range `0`..`15` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `CEN_BUTT_1` | Button | Range | range `0`..`31` - step `1` - default marker `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `MODE` | Modality | Enum | range -..- - step `1`<br>`0` - Press/release only - range -..- - step `1`<br>`1` - Press/hold/release - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `TYPE_CONTACT` | Contact type | Enum | range -..- - step `1`<br>`0` - Normally open - range -..- - step `1`<br>`1` - Normally closed - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |

### Object `415` - Scenario PLUS Lighting Management

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `M` | Modality | Enum | range -..- - step `1`<br>`0` - ON - range -..- - step `1`<br>`1` - OFF - range -..- - step `1`<br>`2` - ON with regulation - range -..- - step `1`<br>`3` - OFF with regulation - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `PPT_SCE_1` | Upper button scenario | Range | range `0`..`255` - step `1` - default marker `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `TYPE_OF_REGULATION` | Regulation type | Enum | range -..- - step `1`<br>`0` - Regulate all - range -..- - step `1`<br>`1` - Lights only - range -..- - step `1`<br>`2` - Shutters only - range -..- - step `1`<br>`3` - Stereo amplifiers only - range -..- - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `TYPE_CONTACT` | Contact type | Enum | range -..- - step `1`<br>`0` - Normally open - range -..- - step `1`<br>`1` - Normally closed - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `DEL_BUTTON_1` | Activation delay for upper button | Enum | range -..- - step `1`<br>`0` - None - range -..- - step `1`<br>`1` - 1 s - range -..- - step `1`<br>`2` - 2 s - range -..- - step `1`<br>`3` - 3 s - range -..- - step `1`<br>`4` - 4 s - range -..- - step `1`<br>`5` - 5 s - range -..- - step `1`<br>`6` - 6 s - range -..- - step `1`<br>`7` - 7 s - range -..- - step `1`<br>`8` - 8 s - range -..- - step `1`<br>`9` - 9 s - range -..- - step `1`<br>`10` - 10 s - range -..- - step `1`<br>`11` - 11 s - range -..- - step `1`<br>`12` - 12 s - range -..- - step `1`<br>`13` - 13 s - range -..- - step `1`<br>`14` - 14 s - range -..- - step `1`<br>`15` - 15 s - range -..- - step `1`<br>`16` - 16 s - range -..- - step `1`<br>`17` - 17 s - range -..- - step `1`<br>`18` - 18 s - range -..- - step `1`<br>`19` - 19 s - range -..- - step `1`<br>`20` - 20 s - range -..- - step `1`<br>`21` - 21 s - range -..- - step `1`<br>`22` - 22 s - range -..- - step `1`<br>`23` - 23 s - range -..- - step `1`<br>`24` - 24 s - range -..- - step `1`<br>`25` - 25 s - range -..- - step `1`<br>`26` - 26 s - range -..- - step `1`<br>`27` - 27 s - range -..- - step `1`<br>`28` - 28 s - range -..- - step `1`<br>`29` - 29 s - range -..- - step `1`<br>`30` - 30 s - range -..- - step `1`<br>`31` - 31 s - range -..- - step `1`<br>`32` - 32 s - range -..- - step `1`<br>`33` - 33 s - range -..- - step `1`<br>`34` - 34 s - range -..- - step `1`<br>`35` - 35 s - range -..- - step `1`<br>`36` - 36 s - range -..- - step `1`<br>`37` - 37 s - range -..- - step `1`<br>`38` - 38 s - range -..- - step `1`<br>`39` - 39 s - range -..- - step `1`<br>`40` - 40 s - range -..- - step `1`<br>`41` - 41 s - range -..- - step `1`<br>`42` - 42 s - range -..- - step `1`<br>`43` - 43 s - range -..- - step `1`<br>`44` - 44 s - range -..- - step `1`<br>`45` - 45 s - range -..- - step `1`<br>`46` - 46 s - range -..- - step `1`<br>`47` - 47 s - range -..- - step `1`<br>`48` - 48 s - range -..- - step `1`<br>`49` - 49 s - range -..- - step `1`<br>`50` - 50 s - range -..- - step `1`<br>`51` - 51 s - range -..- - step `1`<br>`52` - 52 s - range -..- - step `1`<br>`53` - 53 s - range -..- - step `1`<br>`54` - 54 s - range -..- - step `1`<br>`55` - 55 s - range -..- - step `1`<br>`56` - 56 s - range -..- - step `1`<br>`57` - 57 s - range -..- - step `1`<br>`58` - 58 s - range -..- - step `1`<br>`59` - 59 s - range -..- - step `1`<br>`60` - 60 s - range -..- - step `1`<br>`61` - 1 min 30 s - range -..- - step `1`<br>`62` - 2 min - range -..- - step `1`<br>`63` - 3 min - range -..- - step `1`<br>`64` - 4 min - range -..- - step `1`<br>`65` - 5 min - range -..- - step `1`<br>`66` - 6 min - range -..- - step `1`<br>`67` - 7 min - range -..- - step `1`<br>`68` - 8 min - range -..- - step `1`<br>`69` - 9 min - range -..- - step `1`<br>`70` - 10 min - range -..- - step `1`<br>`71` - 15 min - range -..- - step `1` | visible=1, hidden=1, read-only=, type-id=0 |

### Object `416` - Scheduled scenario PLUS

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `PPT_CEN_LOW` | Scheduled scenario PLUS number | Range | range `0`..`255` - step `1` - default marker `1` | visible=1, hidden=0, read-only=, type-id= |
| `PPT_CEN_HIG` | Scheduled scenario PLUS number | Range | range `0`..`7` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `BUTTON_1` | Button | Range | range `0`..`31` - step `1` - default marker `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `MODE` | Modality | Enum | range -..- - step `1`<br>`0` - Press/release only - range -..- - step `1`<br>`1` - Press/hold/release - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `TYPE_CONTACT` | Contact type | Enum | range -..- - step `1`<br>`0` - Normally open - range -..- - step `1`<br>`1` - Normally closed - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |

### Object `418` - Open lock control

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `P` | External unit address | Range | range `0`..`95` - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `SEG_LEV` | Level | Enum | range -..- - step `1`<br>`0` - Same level - range -..- - step `1`<br>`1` - Riser - range -..- - step `1`<br>`2` - Building - range -..- - step `1`<br>`3` - Backbone - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |

### Object `419` - Sound diffusion control

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `M` | Modality | Enum | range -..- - step `1`<br>`0` - ON/volume + - range -..- - step `1`<br>`1` - OFF/volume - - range -..- - step `1`<br>`2` - Change track - range -..- - step `1`<br>`3` - Switch source - range -..- - step `1`<br>`4` - Toggle ON/OFF - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=4 |
| `ADDR_TYPE` | Addressing type | Enum | range -..- - step `1`<br>`0` - Point to point - range -..- - step `1`<br>`1` - Area - range -..- - step `1`<br>`3` - General - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `A` | Area | Range | range `0`..`9` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `PF` | Audio point | Range | range `0`..`9` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `TYPE_CONTACT` | Contact type | Enum | range -..- - step `1`<br>`0` - Normally open - range -..- - step `1`<br>`1` - Normally closed - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `IS_FOLLOW_ME` | Follow me | Enum | range -..- - step `1` - default marker `1`<br>`0` - No - range -..- - step `1`<br>`1` - Yes - range -..- - step `1` | visible=1, hidden=1, read-only=, type-id=0 |
| `SOURCE` | Source | Range | range `1`..`9` - step `1` - default marker `1` | visible=1, hidden=1, read-only=, type-id=0 |
| `SUB_SOURCE` | Sub source | Range | range `0`..`255` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `CHANNEL` | Channel (BB-Stereo) | Enum | range -..- - step `1` - default marker `3`<br>`0` - Base Band - range -..- - step `1`<br>`1` - Left - range -..- - step `1`<br>`2` - Right - range -..- - step `1`<br>`3` - Stereo - range -..- - step `1`<br>`8` - Base Band and Video - range -..- - step `1`<br>`9` - Left and video - range -..- - step `1`<br>`10` - Right and video - range -..- - step `1`<br>`11` - Left and video - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |

### Object `426` - Staircase light control

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `N1` | Internal unit address | Range | range `0`..`255` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `N2` | Internal unit address | Range | range `0`..`15` - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `SEG_LEV` | Segment | Enum | range -..- - step `1`<br>`0` - Same - range -..- - step `1`<br>`1` - Riser - range -..- - step `1`<br>`2` - Building - range -..- - step `1`<br>`3` - Backbone - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |

### Object `427` - Floor call control

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `TO_ALL` | Type of call | Enum | range -..- - step `1` - default marker `1`<br>`0` - Point to point - range -..- - step `1`<br>`1` - General - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `N1` | Internal unit address | Range | range `0`..`255` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `N2` | Internal unit address | Range | range `0`..`15` - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `SEGMENT` | Segment | Enum | range -..- - step `1`<br>`0` - The same - range -..- - step `1`<br>`1` - Riser - range -..- - step `1`<br>`2` - Building - range -..- - step `1`<br>`3` - Backbone - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `IN_AUX_CHANNEL` | Input AUX channel | Range | range `0`..`15` - step `1` | visible=1, hidden=0, read-only=, type-id=0 |

### Object `480` - User interface settings

| Field | Description | Data type | Catalogue range rows | Flags |
| --- | --- | --- | --- | --- |
| `STATE_OF_UNUSED_BUTTON` | State of unused button | Enum | range -..- - step `1` - default marker `1`<br>`0` - ON - range -..- - step `1`<br>`1` - OFF - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `STATE_UPDATE` | Feedback update | Enum | range -..- - step `1` - default marker `1`<br>`0` - No - range -..- - step `1`<br>`1` - Yes - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id=0 |
| `LED_LEVEL` | LED intensity level | Range | range `0`..`10` - step `1` - default marker `6` | visible=1, hidden=0, read-only=, type-id=0 |
| `LED_FADE` | LED fading | Range | range `0`..`10` - step `1` - default marker `5` | visible=1, hidden=0, read-only=, type-id=0 |
| `BACKLIGHT_INTENSITY_STANDBY_LEVEL` | Backlight intensity stand by level | Enum | range -..- - step `1` - default marker `1`<br>`0` - OFF - range -..- - step `1`<br>`1` - Level1 - range -..- - step `1`<br>`2` - Level2 - range -..- - step `1`<br>`3` - Level3 - range -..- - step `1`<br>`4` - Level4 - range -..- - step `1`<br>`5` - Level5 - range -..- - step `1`<br>`6` - Level6 - range -..- - step `1`<br>`7` - Level7 - range -..- - step `1`<br>`8` - Level8 - range -..- - step `1`<br>`9` - Level9 - range -..- - step `1`<br>`10` - Level10 - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `SINGLE_LED_INTENSITY_STANDBY_LEVEL` | when BACKLIGHT_INTENSITY_STANDBY_LEVEL is OFF, only one led can be used for the standby. | Enum | range -..- - step `1` - default marker `1`<br>`0` - OFF - range -..- - step `1`<br>`1` - Level1 - range -..- - step `1`<br>`2` - Level2 - range -..- - step `1`<br>`3` - Level3 - range -..- - step `1`<br>`4` - Level4 - range -..- - step `1`<br>`5` - Level5 - range -..- - step `1`<br>`6` - Level6 - range -..- - step `1`<br>`7` - Level7 - range -..- - step `1`<br>`8` - Level8 - range -..- - step `1`<br>`9` - Level9 - range -..- - step `1`<br>`10` - Level10 - range -..- - step `1` | visible=1, hidden=1, read-only=, type-id= |
| `BACKLIGHT_DELAY` | Delay time (seconds) | Range | range `0`..`255` - step `1` - default marker `15` | visible=1, hidden=0, read-only=, type-id= |
| `PROXIMITY_ENABLE` | Proximity Activation | Boolean | range -..- - step `1` - default marker `1`<br>`0` - Disable - range -..- - step `1`<br>`1` - Enable - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |
| `SIGNBOARD` | Signboard activation type | Enum | range -..- - step `1` - default marker `2`<br>`0` - Off - range -..- - step `1`<br>`1` - Fixe - range -..- - step `1`<br>`2` - Chase - range -..- - step `1` | visible=1, hidden=0, read-only=, type-id= |

The active slot-1 Object determines the functional configuration surface. Object `130` carries UI settings and must remain separate from the command Object.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `0` | Device/Firmware topology conditions |
| Object/Firmware filters | `26` | Conditional Object configuration exposure |
| Referenced conversion rules | `0` | None |

### Object/Firmware filters

| Object | Filter ID | Field | Note | Whole range | Filter ranges |
| ---: | ---: | --- | --- | --- | --- |
| `410` | `311` | `TYPE_CONTACT` | Contact type | `1` | - |
| `411` | `312` | `TYPE_CONTACT` | Contact type | `1` | - |
| `411` | `313` | `M` | Modality | `0` | `4` - UP mono+bistable control<br>`5` - DOWN mono+bistable control |
| `412` | `314` | `TYPE_CONTACT` | Contact type | `1` | - |
| `413` | `315` | `TYPE_CONTACT` | Contact type | `1` | - |
| `414` | `316` | `MODE` | Mode for CEN command | `1` | - |
| `414` | `317` | `TYPE_CONTACT` | Contact type | `1` | - |
| `415` | `318` | `TYPE_CONTACT` | Contact type | `1` | - |
| `415` | `319` | `M` | Mode (ON/OFF regulation) | `1` | - |
| `415` | `320` | `TYPE_OF_REGULATION` | REG_TYPE | `1` | - |
| `416` | `321` | `MODE` | Mode for CEN command | `1` | - |
| `416` | `322` | `TYPE_CONTACT` | Contact type | `1` | - |
| `419` | `323` | `TYPE_CONTACT` | Contact type | `1` | - |
| `419` | `324` | `SUB_SOURCE` | SUB_SOURCE | `1` | - |
| `419` | `325` | `CHANNEL` | Channel (BB-Stereo) | `1` | - |
| `426` | `329` | `SEG_LEV` | Segment | `1` | - |
| `426` | `4101` | `N1` | Internal unit address | `0` | `100`<br>`101`<br>`102`<br>`103`<br>`104`<br>`105`<br>`106`<br>`107`<br>`108`<br>`109`<br>`110`<br>`111`<br>`112`<br>`113`<br>`114`<br>`115`<br>`116`<br>`117`<br>`118`<br>`119`<br>`120`<br>`121`<br>`122`<br>`123`<br>`124`<br>`125`<br>`126`<br>`127`<br>`128`<br>`129`<br>`130`<br>`131`<br>`132`<br>`133`<br>`134`<br>`135`<br>`136`<br>`137`<br>`138`<br>`139`<br>`140`<br>`141`<br>`142`<br>`143`<br>`144`<br>`145`<br>`146`<br>`147`<br>`148`<br>`149`<br>`150`<br>`151`<br>`152`<br>`153`<br>`154`<br>`155`<br>`156`<br>`157`<br>`158`<br>`159`<br>`160`<br>`161`<br>`162`<br>`163`<br>`164`<br>`165`<br>`166`<br>`167`<br>`168`<br>`169`<br>`170`<br>`171`<br>`172`<br>`173`<br>`174`<br>`175`<br>`176`<br>`177`<br>`178`<br>`179`<br>`180`<br>`181`<br>`182`<br>`183`<br>`184`<br>`185`<br>`186`<br>`187`<br>`188`<br>`189`<br>`190`<br>`191`<br>`192`<br>`193`<br>`194`<br>`195`<br>`196`<br>`197`<br>`198`<br>`199`<br>`200`<br>`201`<br>`202`<br>`203`<br>`204`<br>`205`<br>`206`<br>`207`<br>`208`<br>`209`<br>`210`<br>`211`<br>`212`<br>`213`<br>`214`<br>`215`<br>`216`<br>`217`<br>`218`<br>`219`<br>`220`<br>`221`<br>`222`<br>`223`<br>`224`<br>`225`<br>`226`<br>`227`<br>`228`<br>`229`<br>`230`<br>`231`<br>`232`<br>`233`<br>`234`<br>`235`<br>`236`<br>`237`<br>`238`<br>`239`<br>`240`<br>`241`<br>`242`<br>`243`<br>`244`<br>`245`<br>`246`<br>`247`<br>`248`<br>`249`<br>`250`<br>`251`<br>`252`<br>`253`<br>`254`<br>`255` |
| `427` | `326` | `IN_AUX_CHANNEL` | Input AUX channel | `1` | - |
| `427` | `327` | `TO_ALL` | Type of call | `0` | `1` - General |
| `427` | `1900` | `SEGMENT` | Segment | `1` | - |
| `480` | `330` | `STATE_OF_UNUSED_BUTTON` | State of unused button | `1` | - |
| `480` | `3110` | `BACKLIGHT_INTENSITY_STANDBY_LEVEL` | Backlight intensity stand by level | `1` | - |
| `480` | `3117` | `PROXIMITY_ENABLE` | Proximity Activation | `1` | - |
| `480` | `3124` | `SIGNBOARD` | Signboard activation type | `1` | - |
| `480` | `3132` | `SINGLE_LED_INTENSITY_STANDBY_LEVEL` | when BACKLIGHT_INTENSITY_STANDBY_LEVEL is OFF, only one led can be used for the standby. | `1` | - |
| `480` | `3155` | `BACKLIGHT_DELAY` | Delay time (seconds) | `1` | - |

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

Depending on configuration, the control participates in lighting, automation, scenarios, sound diffusion and access/door-entry command functions.

## Observed behavior and corroboration

No sanitized hardware fingerprint is currently retained.

## Programming

Treat the Device as one configurable command surface plus one UI-settings Module, not two independent commands.

## Source reconciliation

Official documentation establishes touch operation, adjustable LED intensity, actuator/scenario use and sound-system ON/OFF/volume use. The database expands the same command surface to the full Virgin-Object candidate set and explicitly separates UI settings into slot `2`.

## Evidence limits and open work

- Archive a dedicated Soft Touch technical sheet with explicit `HD4653M2` coverage.
- Publish the exact physical `M/M2/SPE/INT` function matrix.
- Hardware-corroborate active Object and UI-settings behavior.
- Pin exact printed and 1-based PDF page locations for each applicable multi-product guide citation.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf)
