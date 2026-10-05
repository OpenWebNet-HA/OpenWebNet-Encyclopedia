# Three-module Soft Touch control

## Summary

This three-module Soft Touch control uses a capacitive sensitive area to send configured SCS commands. Brief proximity switches configured lights, while sustained proximity can regulate a point-to-point dimmer; its modes also provide scenario and other documented control functions.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0137` | Project identity |
| Technical description | Three-module Soft Touch control | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `HC/HS4653/3`, `HD4653M3` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1554` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `8` | Main association; independent of project ID |
| Firmware definition | `150` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `2` | Firmware metadata |
| Categories | Commands, Scenarios, User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC/HS4653/3` | Established catalogue identity | Manufacturer database commercial record `1554` explicitly links this SKU to item `1554` |
| BTicino - Axolute | `HD4653M3` | Established catalogue identity | Manufacturer database commercial record `1555` explicitly links this SKU to item `1554` |
| BTicino - Axolute | `HC4653/3` | Established member of grouped catalogue identity | AUTOMATISME printed p. 36 / PDF p. 38 and grouped database code |
| BTicino - Axolute | `HS4653/3` | Established member of grouped catalogue identity | AUTOMATISME printed p. 36 / PDF p. 38 and grouped database code |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `AUTOMATISME.pdf` | Exact manufacturer documentation | `AUTOMATISME; original publication date not established` | HC/HS4653/3: range printed p. 36 / PDF p. 38; physical modes and LED/scenario procedures printed pp. 93-94 / PDF pp. 95-96; supply/current/size printed p. 161 / PDF p. 163. HD4653M3 is outside this original’s explicit reference list. | [Archived original](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |
| `Axolute-AD-ITAX17C.pdf` | Italian Axolute commercial catalogue | `AD-ITAX17C; Edizione 11/2017 printed on rear cover` | HD4653M3 and HC/HS4653/3: lighting/scenarios printed/PDF p. 76; sound control p. 86; depth p. 116. Publication is 2017; the URL’s 2025 directory does not date the original. | [Archived original](https://archive.openwebnet-ha.org/sha256/b9/5f/b95ff63d6989dc791a02d0da95575948d735fee3048c3aced5f4b432f98d5233.pdf) | [Publisher original](https://www.bticino.it/sites/default/files/2025-03/catalogo-Axolute_AD_ITAX17C.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `1554` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / current, HC/HS only | `27 Vdc bus; 15 mA` | `AUTOMATISME`, printed pp. 36, 93-94, 161 / PDF pp. 38, 95-96, 163 |
| Mounting, HC/HS | `3 flush-mounted wiring-device modules` | `AUTOMATISME`, printed pp. 36, 93-94, 161 / PDF pp. 38, 95-96, 163 |
| Interface | `capacitive sensitive area; adjustable status LED` | `AUTOMATISME`, printed pp. 36, 93-94, 161 / PDF pp. 38, 95-96, 163 |
| Configurator sockets | `A; PL/PF; M; M2; SPE; INT` | `AUTOMATISME`, printed pp. 36, 93-94, 161 / PDF pp. 38, 95-96, 163 |
| Timing modes, SPE absent | `M=1:1 min; 2:2 min; 3:3 min; 4:4 min; 5:5 min; 6:15 min; 7:30 s; 8:0.5 s` | `AUTOMATISME`, printed pp. 36, 93-94, 161 / PDF pp. 38, 95-96, 163 |
| Alternate timed-`ON`, `SPE=7` | `M=1:2 s; M=2:10 min` | `AUTOMATISME`, printed pp. 36, 93-94, 161 / PDF pp. 38, 95-96, 163 |
| Flashing, `SPE=2` | `M absent:0.5 s; M=1..9:1..5 s in 0.5 s increments` | `AUTOMATISME`, printed pp. 36, 93-94, 161 / PDF pp. 38, 95-96, 163 |
| Fixed dimmer level, `SPE=3` | `M=1..9:10%..90% in 10% steps` | `AUTOMATISME`, printed pp. 36, 93-94, 161 / PDF pp. 38, 95-96, 163 |
| Scenario selection, `SPE=6` | `M/M2 selects scenario 1..16 at addressed F420` | `AUTOMATISME`, printed pp. 36, 93-94, 161 / PDF pp. 38, 95-96, 163 |
| LED INT absent | `30% resting/OFF; 60% ON for point-to-point lighting` | `AUTOMATISME`, printed pp. 36, 93-94, 161 / PDF pp. 38, 95-96, 163 |
| LED `INT=1` | `45% resting/OFF; 70% ON for point-to-point lighting` | `AUTOMATISME`, printed pp. 36, 93-94, 161 / PDF pp. 38, 95-96, 163 |
| LED `INT=OFF` | `0% resting/OFF; 30% ON for point-to-point lighting` | `AUTOMATISME`, printed pp. 36, 93-94, 161 / PDF pp. 38, 95-96, 163 |

### Additional exact Axolute catalogue facts



| Property | Value | Evidence |
| --- | --- | --- |
| HD4653M3 mounting | `3 wiring-device modules` | AD-ITAX17C printed/PDF p. 76 |
| HD4653M3 depth | `20 mm` | AD-ITAX17C printed/PDF p. 116 |
| Co-listed sound role | speaker `ON`/`OFF` and volume adjustment | AD-ITAX17C printed/PDF p. 86 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1554` | Canonical catalogue |
| Technical item description | Soft touch control | Canonical catalogue |
| Item family | 0; key `1` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `8` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `150` | `-1` | `-1` | `-1` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `150` | `1` | `410` Light control | Fixed/designated metadata | `575` | `410` | `394` |
| `150` | `1` | `411` Automation control | Candidate alternative | `576` | `411` | `395` |
| `150` | `1` | `412` Lock/unlock actuator control | Candidate alternative | `577` | `412` | `396` |
| `150` | `1` | `413` Scenario module control | Candidate alternative | `578` | `413` | `397` |
| `150` | `1` | `414` Scheduled scenario | Candidate alternative | `579` | `414` | `398` |
| `150` | `1` | `415` Scenario PLUS Lighting Management | Candidate alternative | `580` | `415` | `399` |
| `150` | `1` | `416` Scheduled scenario PLUS | Candidate alternative | `581` | `416` | `400` |
| `150` | `1` | `418` Open lock control | Candidate alternative | `582` | `418` | `401` |
| `150` | `1` | `419` Sound diffusion control | Candidate alternative | `583` | `419` | `402` |
| `150` | `1` | `426` Staircase light control | Candidate alternative | `585` | `426` | `404` |
| `150` | `1` | `427` Floor call control | Candidate alternative | `584` | `427` | `403` |
| `150` | `2` | `130` User interface settings | Fixed/designated metadata | `586` | `480` | `405` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `150` | `521` Soft-Touch command virgin | `1` | `410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `418`, `419`, `421`, `426`, `427`, `462` | `521` | `24` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `150` | Virtual Configuration | `1` | Association key `1` |
| `150` | Advanced Configuration | `2` | Association key `2` |
| `150` | Physical configuration | `0` | Association key `3` |


No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `150` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `150` | `A` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB`; `15` = `AUX` | `0` | A; Enviroment (0-9 `GEN`,`GR`,`AMB`,`AUX`) |
| `150` | `PL` | `0..9` | `0` | PL; Light Point |
| `150` | `M` | `0..9`; `14` = `CEN`; `10` = `OFF`; `11` = `ON`; `15` = `PUL` | `0` | M; Mode physical configurator (0-9,`OFF`,`ON`,`CEN`,`PUL`) |
| `150` | `M2` | `0..9` | `0` | M2; Mode physical configurator (0-9) |
| `150` | `SPE` | `0..4`; `6..9` | `0` | SPE; Special function command control (0,1,2,3,4,6,7,8,9) |
| `150` | `INT` | `0..1`; `10` = `OFF` | `0` | INT; INT (0,1,`OFF`) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `410` - Light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `1` = Timed `ON`; `2` = Toggle dimmer; `4` = Toggle `ON`/`OFF`; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `20` = `ON` and point to point dimmer; `21` = `OFF` and point to point dimmer; `22` = `ON` and Dimmer; `23` = `OFF` and Dimmer; `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90%; `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `131` = Customized toggle dimmer; `133` = Customized toggle dimmer without regulation; `135` = Customized `ON` and dimmer without regulation; `136` = Customized `OFF` and dimmer without regulation; `137` = Customized `ON` and dimmer with regulation; `138` = Customized `OFF` and dimmer with regulation | `0` | Modality; Mode (MODE+`ON`/`OFF`) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `HOURS` | `0..255` | `0` | Hours; Only for `MOD=128` |
| `MINUTES` | `0..59` | `0` | Minutes; Only for `MOD=128` |
| `SECONDS` | `0..59` | `30` | Seconds; Only for `MOD=128` |
| `LEVEL` | `0..100` | `100` | Level; Only for `MOD=129`, 131, 133, 135, 136, 137, 138 |
| `START_S` | `0..255` | `255` | Soft start speed; Only for `MOD=129`, 131, 133, 135, 136, 137, 138 |
| `STOP_S` | `0..255` | `255` | Soft stop speed; Only for `MOD=129`, 131, 133, 135, 136, 137, 138 |
| `DIMMING_S` | `0..255` | `255` | Dimming speed; Only for `MOD=129`, 131 |
| `T_TIME` | `1` = 1 min; `2` = 2 min; `3` = 3 min; `4` = 4 min; `5` = 5 min; `6` = 15 min; `7` = 30 s; `8` = 0.5 s; `9` = 2 s; `10` = 10 min | `1` | Tabled time; Only for `MOD=1` |


### Object `411` - Automation control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = UP bistable control; `1` = DOWN bistable control; `2` = UP monostable control; `3` = DOWN monostable control; `4` = UP monostable and bistable control; `5` = DOWN monostable and bistable control | `0` | Modality; mode (`UP/DOWN`) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |


### Object `412` - Lock/unlock actuator control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `1` = Disable; `2` = Enable | `1` | Modality; mode (D/E) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |


### Object `413` - Scenario module control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Scenario activation and modification; `1` = Scenario activation | `0` | Modality |
| `APL` | `0..175`; area `floor(APL/16)`, light point `APL mod 16` | `0` | Scenario module address |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15 | `0` | Destination level; Destination level (`0..15`) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `SCE_BUTT_1` | `1..16` | `1` | Scenario number |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay of scenario number |


### Object `414` - Scheduled scenario

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `CEN_BUTT_1` | `0..31` | `1` | Button |
| `MODE` | `0` = Press/release only; `1` = Press/hold/release | `0` | Modality; Mode (Lighting management) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |


### Object `415` - Scenario PLUS Lighting Management

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = `ON`; `1` = `OFF`; `2` = `ON` with regulation; `3` = `OFF` with regulation | `0` | Modality; Mode (`ON`/`OFF` regulation) |
| `PPT_SCE_1` | `0..255` | `1` | Upper button scenario |
| `TYPE_OF_REGULATION` | `0` = Regulate all; `1` = Lights only; `2` = Shutters only; `3` = Stereo amplifiers only | `0` | Regulation type |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for upper button |


### Object `416` - Scheduled scenario PLUS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | `0..255` | `1` | Scheduled scenario PLUS number |
| `PPT_CEN_HIG` | `0..7` | `0` | Scheduled scenario PLUS number |
| `BUTTON_1` | `0..31` | `1` | Button |
| `MODE` | `0` = Press/release only; `1` = Press/hold/release | `0` | Modality; Mode (Lighting management) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |


### Object `418` - Open lock control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same level; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Level |


### Object `419` - Sound diffusion control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = `ON`/volume +; `1` = `OFF`/volume -; `2` = Change track; `3` = Switch source; `4` = Toggle `ON`/`OFF` | `0` | Modality; Mode (VOL,ON_OFF) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..9` | `0` | Area |
| `PF` | `0..9` | `0` | Audio point |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `IS_FOLLOW_ME` | `0` = No; `1` = Yes | `1` | Follow me |
| `SOURCE` | `1..9` | `1` | Source |
| `SUB_SOURCE` | `0..255` | `0` | Sub source |
| `CHANNEL` | `0` = Base Band; `1` = Left; `2` = Right; `3` = Stereo; `8` = Base Band and Video; `9` = Left and video; `10` = Right and video; `11` = Left and video | `3` | Channel (BB-Stereo) |


### Object `426` - Staircase light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |


### Object `427` - Floor call control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `TO_ALL` | `0` = Point to point; `1` = General | `1` | Type of call |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |


### Object `130` - User interface settings

Catalogue Object key `480` maps to external Object `130`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `STATE_OF_UNUSED_BUTTON` | `0` = `ON`; `1` = `OFF` | `1` | State of unused button; Default depends on device |
| `STATE_UPDATE` | `0` = No; `1` = Yes | `1` | Feedback update; Default depends on device |
| `LED_LEVEL` | `0..10` | `6` | LED intensity level; Default, minimum level (0), maximum level (10) and distribution of intermediate levels depend on device |
| `LED_FADE` | `0..10` | `5` | LED fading; Default, minimum level (0), maximum level (10) and distribution of intermediate levels depend on device |
| `BACKLIGHT_INTENSITY_STANDBY_LEVEL` | `0` = `OFF`; `1` = Level1; `2` = Level2; `3` = Level3; `4` = Level4; `5` = Level5; `6` = Level6; `7` = Level7; `8` = Level8; `9` = Level9; `10` = Level10 | `1` | Backlight intensity stand by level |
| `SINGLE_LED_INTENSITY_STANDBY_LEVEL` | `0` = `OFF`; `1` = Level1; `2` = Level2; `3` = Level3; `4` = Level4; `5` = Level5; `6` = Level6; `7` = Level7; `8` = Level8; `9` = Level9; `10` = Level10 | `1` | when BACKLIGHT_INTENSITY_STANDBY_LEVEL is `OFF`, only one led can be used for the standby. |
| `BACKLIGHT_DELAY` | `0..255` | `15` | Delay time (seconds); Time en second to light off the backlight |
| `PROXIMITY_ENABLE` | `0` = Disable; `1` = Enable | `1` | Proximity Activation |
| `SIGNBOARD` | `0` = Off; `1` = Fixe; `2` = Chase | `2` | Signboard activation type |

### Virgin-only reusable capability

The following Objects are permitted by an associated Virgin Object but lack a direct Object/Firmware relationship for this Device. Their reusable definitions are inventoried for completeness; they are not a declaration of active placements or supported values on this Firmware.

### Object `417` - `AUX` control (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Cyclical; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `17` = DOWN Shutter bistable command; `18` = UP shutter monostable command; `4` = Reset BI; `5` = Reset TRI; `6` = Reset `GEN`; `1` = Disable; `2` = Enable; `16` = UP shutter bistable command; `19` = DOWN Shutter monostable command | `0` | Modality; mode(Cyclical,off,on,pul,up,down,...) |
| `OUT_AUX_CH` | `1..15` | `1` | `AUX` channel |
| `TYPE_CONTACT` | No legal values specified in source | `0` | Contact type |

### Object `421` - Cyclic autoswitch control (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |

### Object `462` - Open lock command on session (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `150` | `410` | `331` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `150` | `411` | `332` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `150` | `411` | `333` | `M` | `4` = UP monostable and bistable control; `5` = DOWN monostable and bistable control | `0` | Modality; reusable default `0` is outside this subset; filter supplies no replacement default |
| `150` | `412` | `334` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `150` | `413` | `335` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `150` | `414` | `336` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `150` | `414` | `337` | `MODE` | `0` = Press/release only; `1` = Press/hold/release (entire reusable range retained) | `0` | Mode for `CEN` command |
| `150` | `415` | `338` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `150` | `415` | `339` | `M` | `0` = `ON`; `1` = `OFF`; `2` = `ON` with regulation; `3` = `OFF` with regulation (entire reusable range retained) | `0` | Mode (`ON`/`OFF` regulation) |
| `150` | `415` | `340` | `TYPE_OF_REGULATION` | `0` = Regulate all; `1` = Lights only; `2` = Shutters only; `3` = Stereo amplifiers only (entire reusable range retained) | `0` | REG_TYPE |
| `150` | `416` | `341` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `150` | `416` | `342` | `MODE` | `0` = Press/release only; `1` = Press/hold/release (entire reusable range retained) | `0` | Mode for `CEN` command |
| `150` | `419` | `343` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `150` | `419` | `344` | `SUB_SOURCE` | `0..255` (entire reusable range retained) | `0` | SUB_SOURCE |
| `150` | `419` | `345` | `CHANNEL` | `0` = Base Band; `1` = Left; `2` = Right; `3` = Stereo; `8` = Base Band and Video; `9` = Left and video; `10` = Right and video; `11` = Left and video (entire reusable range retained) | `3` | Channel (BB-Stereo) |
| `150` | `426` | `349` | `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone (entire reusable range retained) | `0` | Segment |
| `150` | `426` | `4102` | `N1` | `100..255` | `0` | Internal unit address; reusable default `0` is outside this subset; filter supplies no replacement default |
| `150` | `427` | `346` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `150` | `427` | `347` | `TO_ALL` | `1` = General | `1` | Type of call |
| `150` | `427` | `1901` | `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone (entire reusable range retained) | `0` | Segment |
| `150` | `130` | `350` | `STATE_OF_UNUSED_BUTTON` | `0` = `ON`; `1` = `OFF` (entire reusable range retained) | `1` | State of unused button |
| `150` | `130` | `3111` | `BACKLIGHT_INTENSITY_STANDBY_LEVEL` | `0` = `OFF`; `1` = Level1; `2` = Level2; `3` = Level3; `4` = Level4; `5` = Level5; `6` = Level6; `7` = Level7; `8` = Level8; `9` = Level9; `10` = Level10 (entire reusable range retained) | `1` | Backlight intensity stand by level |
| `150` | `130` | `3118` | `PROXIMITY_ENABLE` | `0` = Disable; `1` = Enable (entire reusable range retained) | `1` | Proximity Activation |
| `150` | `130` | `3125` | `SIGNBOARD` | `0` = Off; `1` = Fixe; `2` = Chase (entire reusable range retained) | `2` | Signboard activation type |
| `150` | `130` | `3133` | `SINGLE_LED_INTENSITY_STANDBY_LEVEL` | `0` = `OFF`; `1` = Level1; `2` = Level2; `3` = Level3; `4` = Level4; `5` = Level5; `6` = Level6; `7` = Level7; `8` = Level8; `9` = Level9; `10` = Level10 (entire reusable range retained) | `1` | when BACKLIGHT_INTENSITY_STANDBY_LEVEL is `OFF`, only one led can be used for the standby. |
| `150` | `130` | `3156` | `BACKLIGHT_DELAY` | `0..255` (entire reusable range retained) | `15` | Delay time (seconds) |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `8` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Read installed firmware and compare with the applicability table | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Obtain hardware revision; no source-backed installed value | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Obtain microcontroller identity; no fingerprint retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve active Modules/Objects independently of candidate metadata | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Corroborate installed addressing and distinguish physical from reusable ranges | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Compare installed configuration with the exact firmware/Object restrictions | [Configuration](../../diagnostics/dim35-configuration.md) |

These are catalogue-derived diagnostic candidates. No Device-specific response or support across all commercial variants is established by a hardware capture.

## Functional applicability

| Catalogue Object / role | Applicability | Evidence |
| --- | --- | --- |
| `410` - Light control | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `411` - Automation control | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `412` - Lock/unlock actuator control | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `413` - Scenario module control | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `414` - Scheduled scenario | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `415` - Scenario PLUS Lighting Management | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `416` - Scheduled scenario PLUS | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `418` - Open lock control | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `419` - Sound diffusion control | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `427` - Floor call control | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `426` - Staircase light control | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `130` - User interface settings | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |


These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The guide explicitly states that its two- and three-module HC/HS versions differ mechanically while configuration/modes agree. Short proximity controls cyclic lights, long proximity regulates point-to-point dimmers; `ON`/`OFF`/`PUL`, timed, flashing and fixed-level modes depend on M/SPE. In F420 scenario programming, hold proximity about three seconds then withdraw to start programming, set the scenario on the system, and approach briefly to finish. Continue holding about five additional seconds after the first three to erase the selected scenario. All-scenario deletion belongs to F420’s reset procedure. `SPE=8` changes PL/PF to a sound point, but the automation guide delegates detailed sound/video behavior to separate documents.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

## Source reconciliation

HC/HS4653/3 and HD4653M3 are explicit manufacturer database identities. AUTOMATISME directly establishes the HC/HS members and physical modes. The 2017 Axolute catalogue independently co-lists HD4653M3/HC4653/3/HS4653/3 for lighting, scenarios and sound, and establishes HD4653M3 mounting/depth. It does not supply HD electrical ratings, so AUTOMATISME’s current is not automatically transferred to HD. Its physical scenario and light roles are narrower than the historical Suite reusable Object inventory, which additionally contains `CEN`+, Plus, door-entry, sound and UI roles. Two Firmware Modules do not mean two touch areas or a two-module physical housing. The guide’s 15 mA is retained without borrowing current/temperature values from another Device dossier.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `AUTOMATISME.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `Axolute-AD-ITAX17C.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |


The relation-specific restriction table explicitly identifies reusable defaults outside the permitted subset. These are catalogue inconsistencies; no replacement default is inferred. Runtime Configuration and manufacturer modes must be corroborated before selecting a substitute.

The Object `426` restriction permits target `N1=100..255`, excluding its reusable default `0`; the physical guide delegates detailed video-door-entry settings elsewhere. The automation Object restricts M to combined monostable/bistable directions and excludes the reusable default. These catalogue constraints are not repaired by borrowing physical modes from another control.

## Evidence limits and open work

Exact HD4653M3 technical/installation instructions and electrical ratings, operating-temperature range, sound/video mode instructions, Suite-specific physical equivalence and captures of the broader Object/filter surface remain incomplete.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
