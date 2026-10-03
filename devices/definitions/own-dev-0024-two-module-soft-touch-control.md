# Two-module Soft Touch control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0024` | Project identity |
| Technical description | Two-module capacitive Soft Touch SCS command with configurable function and UI settings | Catalogue + official documentation |
| Commercial identities | `HC/HS4653/2`, `HD4653M2` | Catalogue |
| Catalogue item | `12` - “Soft touch control” | Implementation evidence |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `8` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `149` | Implementation evidence |
| Declared Modules | `2` | Implementation evidence |
| Categories | Command, Lighting, Automation, Scenario, Sound, Access | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino - Axolute | `HC/HS4653/2` | Established identity | canonical commercial record `12`; Commercial identity of this Technical Device | Canonical catalogue |
| BTicino - Axolute | `HD4653M2` | Established identity | canonical commercial record `1553`; Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `AUTOMATISME.pdf` | MyHOME automation guide | historical publisher guide | Soft Touch HC/HS4653/2 and HC/HS4653/3: printed pp. 93-94 / PDF pp. 95-96; specification table printed p. 161 / PDF p. 163 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

The printed and 1-based PDF page locators remain unresolved and are retained explicitly as an evidence gap.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 flush-mounted modules | Publisher automation documentation |
| SCS nominal supply | `27 Vdc` | Publisher data |
| SCS operating range | `18..27 Vdc` | Publisher data |
| Maximum current draw | `18 mA` | Publisher data |
| Operating temperature | `5..35 °C` | Publisher data |
| User interface | capacitive Soft Touch surface | Publisher automation documentation |
| LED indication | intensity adjustable | Publisher automation documentation |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `12` | Canonical catalogue |
| Technical item description | Soft touch control | Canonical catalogue |
| Item family | `1` - Control | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `8` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `149` | `-1` | `-1` | `-1` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Firmware `149` is wildcard `-1.-1.-1` and declares two Modules.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `149` | `1` | `410` Light control | Fixed/designated metadata | `563` | `410` | `382` |
| `149` | `1` | `411` Automation control | Candidate alternative | `564` | `411` | `383` |
| `149` | `1` | `412` Lock/unlock actuator control | Candidate alternative | `565` | `412` | `384` |
| `149` | `1` | `413` Scenario module control | Candidate alternative | `566` | `413` | `385` |
| `149` | `1` | `414` Scheduled scenario | Candidate alternative | `567` | `414` | `386` |
| `149` | `1` | `415` Scenario PLUS Lighting Management | Candidate alternative | `568` | `415` | `387` |
| `149` | `1` | `416` Scheduled scenario PLUS | Candidate alternative | `569` | `416` | `388` |
| `149` | `1` | `418` Open lock control | Candidate alternative | `570` | `418` | `389` |
| `149` | `1` | `419` Sound diffusion control | Candidate alternative | `571` | `419` | `390` |
| `149` | `1` | `426` Staircase light control | Candidate alternative | `573` | `426` | `392` |
| `149` | `1` | `427` Floor call control | Candidate alternative | `572` | `427` | `391` |
| `149` | `2` | `130` User interface settings | Fixed/designated metadata | `574` | `480` | `393` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `149` | `521` Soft-Touch command virgin | `1` | `410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `418`, `419`, `421`, `426`, `427`, `462` | `521` | `23` |

Slot `1` is the configurable command surface. Direct candidates are Objects `410`, `411`, `412`, `413`, `414`, `415`, `416`, `418`, `419`, `426`, and `427`. Virgin Object `521`, Soft-Touch command virgin, additionally permits `AUX` `417`, cyclic autoswitch `421`, and Open-lock-on-session `462`. Slot `2` is fixed Object `130`, User interface settings. It is not a second command channel.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `149` | `1` | `1` | Virtual Configuration |
| `149` | `2` | `2` | Advanced Configuration |
| `149` | `3` | `0` | Physical configuration |

Physical configuration, Virtual Configuration and Advanced Configuration.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `149` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `149` | `A` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB`; `15` = `AUX` | `0` | A; Environment (0-9 `GEN`,`GR`,`AMB`,`AUX`) |
| `149` | `PL` | `0..9` | `0` | PL; Light Point |
| `149` | `M` | `0..9`; `14` = `CEN`; `10` = `OFF`; `11` = `ON`; `15` = `PUL` | `0` | M; Mode physical configurator (0-9,`OFF`,`ON`,`CEN`,`PUL`) |
| `149` | `M2` | `0..9` | `0` | M2; Mode physical configurator (0-9) |
| `149` | `SPE` | `0..4`; `6..9` | `0` | SPE; Special function command control (0,1,2,3,4,6,7,8,9) |
| `149` | `INT` | `0..1`; `10` = `OFF` | `0` | INT; INT (0,1,`OFF`) |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `A` | `0..9` / `GEN` / `GR` / `AMB` / `AUX` | area / environment configurator |
| `PL` | `0..9` | light-point configurator |
| `M` | `0..9` / `CEN` / `OFF` / `ON` / `PUL` | operating / function mode |
| `M2` | `0..9` | channel 2 operating mode |
| `SPE` | `0` / `1` / `2` / `3` / `4` / `6` / `7` / `8` / `9` | special-function selector |
| `INT` | `0` / `1` / `OFF` | interface-function selector |


These are the Soft Touch device configurators. Their values select among the candidate control Objects; the much larger reusable Object schemas are summarized separately rather than flattened into this table.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `410` - Light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `1` = Timed `ON`; `2` = Toggle dimmer; `4` = Toggle `ON`/`OFF`; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `20` = `ON` and point to point dimmer; `21` = `OFF` and point to point dimmer; `22` = `ON` and Dimmer; `23` = `OFF` and Dimmer; `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90%; `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `131` = Customized toggle dimmer; `133` = Customized toggle dimmer without regulation; `135` = Customized `ON` and dimmer without regulation; `136` = Customized `OFF` and dimmer without regulation; `137` = Customized `ON` and dimmer with regulation; `138` = Customized `OFF` and dimmer with regulation | `0` | Modality; Mode (MODE+`ON`/`OFF`) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = All systems | `0` | Destination level |
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
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |


### Object `412` - Lock/unlock actuator control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `1` = Disable; `2` = Enable | `1` | Modality; mode (D/E) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = All systems | `0` | Destination level |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |


### Object `413` - Scenario module control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Scenario activation and modification; `1` = Scenario activation | `0` | Modality |
| `APL` | `0..175`; encoded by `APL=16*A+PL`, with `A=0..10` and `PL=0..15` | `0` | Scenario module address |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number | `0` | Destination level; Destination level (`0..15`) |
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
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `3` = General | `0` | Addressing type |
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


### Product interpretation and source differences

**Object `410` - Light control - product interpretation.**

**Firmware relationship.** The catalogue relation explicitly exposes `TYPE_CONTACT`.

**Object `411` - Automation control - product interpretation.**

**Firmware relationship.** The catalogue relation explicitly exposes `TYPE_CONTACT`. The catalogue relation restricts `M`: UP mono+bistable control (`4`), DOWN mono+bistable control (`5`).

**Object `412` - Lock/unlock actuator control - product interpretation.**

**Firmware relationship.** The catalogue relation explicitly exposes `TYPE_CONTACT`.

**Object `413` - Scenario module control - product interpretation.**

**Firmware relationship.** The catalogue relation explicitly exposes `TYPE_CONTACT`.

**Object `414` - Scheduled scenario - product interpretation.**

**Firmware relationship.** The catalogue relation explicitly exposes `MODE`, `TYPE_CONTACT`.

**Object `415` - Scenario PLUS Lighting Management - product interpretation.**

**Firmware relationship.** The catalogue relation explicitly exposes `TYPE_CONTACT`, `M`, `TYPE_OF_REGULATION`.

**Object `416` - Scheduled scenario PLUS - product interpretation.**

**Firmware relationship.** The catalogue relation explicitly exposes `MODE`, `TYPE_CONTACT`.

**Object `418` - Open lock control - product interpretation.**

**Firmware relationship.** No additional Object/Firmware range filter in the catalogue.

**Object `419` - Sound diffusion control - product interpretation.**

**Firmware relationship.** The catalogue relation explicitly exposes `TYPE_CONTACT`, `SUB_SOURCE`, `CHANNEL`.

**Object `427` - Floor call control - product interpretation.**

**Firmware relationship.** The catalogue relation explicitly exposes `IN_AUX_CHANNEL`, `SEGMENT`. The catalogue relation restricts `TO_ALL`: General (`1`).

**Object `426` - Staircase light control - product interpretation.**

**Firmware relationship.** The catalogue relation explicitly exposes `SEG_LEV`. The catalogue relation restricts `N1` to `100..255`.

**Object `130` - User interface settings - product interpretation.**

**Firmware relationship.** The catalogue relation explicitly exposes `STATE_OF_UNUSED_BUTTON`, `BACKLIGHT_INTENSITY_STANDBY_LEVEL`, `PROXIMITY_ENABLE`, `SIGNBOARD`, `SINGLE_LED_INTENSITY_STANDBY_LEVEL`, `BACKLIGHT_DELAY`.

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `149` | `410` | `311` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `149` | `411` | `312` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `149` | `411` | `313` | `M` | `4` = UP monostable and bistable control; `5` = DOWN monostable and bistable control | `0` | Modality; reusable default `0` is outside this subset; filter supplies no replacement default |
| `149` | `412` | `314` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `149` | `413` | `315` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `149` | `414` | `316` | `MODE` | `0` = Press/release only; `1` = Press/hold/release (entire reusable range retained) | `0` | Mode for `CEN` command |
| `149` | `414` | `317` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `149` | `415` | `318` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `149` | `415` | `319` | `M` | `0` = `ON`; `1` = `OFF`; `2` = `ON` with regulation; `3` = `OFF` with regulation (entire reusable range retained) | `0` | Mode (`ON`/`OFF` regulation) |
| `149` | `415` | `320` | `TYPE_OF_REGULATION` | `0` = Regulate all; `1` = Lights only; `2` = Shutters only; `3` = Stereo amplifiers only (entire reusable range retained) | `0` | REG_TYPE |
| `149` | `416` | `321` | `MODE` | `0` = Press/release only; `1` = Press/hold/release (entire reusable range retained) | `0` | Mode for `CEN` command |
| `149` | `416` | `322` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `149` | `419` | `323` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `149` | `419` | `324` | `SUB_SOURCE` | `0..255` (entire reusable range retained) | `0` | SUB_SOURCE |
| `149` | `419` | `325` | `CHANNEL` | `0` = Base Band; `1` = Left; `2` = Right; `3` = Stereo; `8` = Base Band and Video; `9` = Left and video; `10` = Right and video; `11` = Left and video (entire reusable range retained) | `3` | Channel (BB-Stereo) |
| `149` | `426` | `329` | `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone (entire reusable range retained) | `0` | Segment |
| `149` | `426` | `4101` | `N1` | `100`; `101`; `102`; `103`; `104`; `105`; `106`; `107`; `108`; `109`; `110`; `111`; `112`; `113`; `114`; `115`; `116`; `117`; `118`; `119`; `120`; `121`; `122`; `123`; `124`; `125`; `126`; `127`; `128`; `129`; `130`; `131`; `132`; `133`; `134`; `135`; `136`; `137`; `138`; `139`; `140`; `141`; `142`; `143`; `144`; `145`; `146`; `147`; `148`; `149`; `150`; `151`; `152`; `153`; `154`; `155`; `156`; `157`; `158`; `159`; `160`; `161`; `162`; `163`; `164`; `165`; `166`; `167`; `168`; `169`; `170`; `171`; `172`; `173`; `174`; `175`; `176`; `177`; `178`; `179`; `180`; `181`; `182`; `183`; `184`; `185`; `186`; `187`; `188`; `189`; `190`; `191`; `192`; `193`; `194`; `195`; `196`; `197`; `198`; `199`; `200`; `201`; `202`; `203`; `204`; `205`; `206`; `207`; `208`; `209`; `210`; `211`; `212`; `213`; `214`; `215`; `216`; `217`; `218`; `219`; `220`; `221`; `222`; `223`; `224`; `225`; `226`; `227`; `228`; `229`; `230`; `231`; `232`; `233`; `234`; `235`; `236`; `237`; `238`; `239`; `240`; `241`; `242`; `243`; `244`; `245`; `246`; `247`; `248`; `249`; `250`; `251`; `252`; `253`; `254`; `255` | `0` | Internal unit address; reusable default `0` is outside this subset; filter supplies no replacement default |
| `149` | `427` | `326` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `149` | `427` | `327` | `TO_ALL` | `1` = General | `1` | Type of call |
| `149` | `427` | `1900` | `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone (entire reusable range retained) | `0` | Segment |
| `149` | `130` | `330` | `STATE_OF_UNUSED_BUTTON` | `0` = `ON`; `1` = `OFF` (entire reusable range retained) | `1` | State of unused button |
| `149` | `130` | `3110` | `BACKLIGHT_INTENSITY_STANDBY_LEVEL` | `0` = `OFF`; `1` = Level1; `2` = Level2; `3` = Level3; `4` = Level4; `5` = Level5; `6` = Level6; `7` = Level7; `8` = Level8; `9` = Level9; `10` = Level10 (entire reusable range retained) | `1` | Backlight intensity stand by level |
| `149` | `130` | `3117` | `PROXIMITY_ENABLE` | `0` = Disable; `1` = Enable (entire reusable range retained) | `1` | Proximity Activation |
| `149` | `130` | `3124` | `SIGNBOARD` | `0` = Off; `1` = Fixe; `2` = Chase (entire reusable range retained) | `2` | Signboard activation type |
| `149` | `130` | `3132` | `SINGLE_LED_INTENSITY_STANDBY_LEVEL` | `0` = `OFF`; `1` = Level1; `2` = Level2; `3` = Level3; `4` = Level4; `5` = Level5; `6` = Level6; `7` = Level7; `8` = Level8; `9` = Level9; `10` = Level10 (entire reusable range retained) | `1` | when BACKLIGHT_INTENSITY_STANDBY_LEVEL is `OFF`, only one led can be used for the standby. |
| `149` | `130` | `3155` | `BACKLIGHT_DELAY` | `0..255` (entire reusable range retained) | `15` | Delay time (seconds) |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 8` and the Soft Touch commercial family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | record installed firmware rather than assuming wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | resolve the configurable command Object plus the separate UI-settings Module | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the address of the resolved command role | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `A`, `PL`, `M`, `M2`, `SPE`, `INT` plus Device-specific UI/backlight settings | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Depending on configuration, the control participates in lighting, automation, scenarios, sound diffusion and access/door-entry command functions.

## Observed behavior and corroboration

No sanitized hardware fingerprint is currently retained.

## Programming

Treat the Device as one configurable command surface plus one UI-settings Module, not two independent commands.

## Source reconciliation

Official documentation establishes touch operation, adjustable LED intensity, actuator/scenario use and sound-system `ON`/`OFF`/volume use. The database expands the same command surface to the full Virgin-Object candidate set and explicitly separates UI settings into slot `2`.

## Evidence limits and open work

- Archive a dedicated Soft Touch technical sheet with explicit `HD4653M2` coverage.
- Publish the exact physical `M/M2/SPE/INT` function matrix.
- Hardware-corroborate active Object and UI-settings behavior.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)
