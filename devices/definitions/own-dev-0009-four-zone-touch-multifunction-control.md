# Four-zone touch multifunction control

## Summary

This compact SCS wall control has four capacitive touch zones with adjustable blue LED feedback. Its configurable and self-learning functions cover lighting, shutters, scenarios, sound and selected door-entry actions, allowing individual touch zones to serve different purposes.


| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0009` | Project identity |
| Technical description | Two-module capacitive four-zone multifunction SCS control | Catalogue + official technical sheet |
| Catalogue item | `1376` - “Touch control multifunction” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `17` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `159` | Implementation evidence |
| Declared Modules | `5` | Implementation evidence |
| Categories | Command, Multifunction, Lighting, Automation, Scenario, Audio / Video | Capability model |

The Device has four capacitive command zones plus a fifth fixed **User interface settings** Module. Its command Modules can be configured across lighting, automation, scenarios, `AUX`, sound-system, and video-door-entry-related roles.

## Commercial identities


The canonical catalogue contains 15 commercial records for item `1376`.

| Brand / line | References | Evidence status |
| --- | --- | --- |
| Legrand Arteor | `573904`, `573905`, `573906`, `573907` | directly documented by `LG00045-b-UK` and the MyHOME catalogue |
| Legrand Arteor | `574089`, `574589` | shared technical item; individual product-document review pending |
| Legrand Céliane | `067243`, `067244`, `067245` | catalogue + MyHOME Server compatibility documentation; minimum compatible production batch `13W05` |
| Legrand Céliane | `067273`, `067274`, `067275`, `067293`, `067294`, `067295` | shared technical item; individual product-document review pending |

The older technical sheet directly names only the four Arteor references. Shared item membership establishes a common implementation capability core, not perfect physical/package synonymy.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `LG00045-b-UK` | Technical sheet | not stated in retained row | `573904..573907` | [Archived PDF](https://archive.openwebnet-ha.org/sha256/9e/18/9e18cf6694d6fcb44ee1c0964175c88d7a9f1918de4e4c4ac8c2d969b401d422.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LG00045_b_UK.pdf) |
| `U3300B` | Instruction sheet | not stated in retained row | `573904..573907` family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/bf/19/bf19dc9f2f7d44ed0714fc43e734b58428aa5320cfd30c9a8822e4530f63b9cd.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/U3300B.pdf) |
| MyHOME residential automation catalogue | Product catalogue | not stated in retained row | all `573904..573907` references on printed p. 19 / PDF p. 19; `573904` / `573905` also appear in the installation principle on printed p. 31 / PDF p. 31 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/13/8e/138e7a234fe24fb044d3bfc82954e08b2887be22f3f8ceb24aecaeff6ed2f2e5.pdf) | [Official source](https://assets.legrand.com/pim/DOCUMENT/BR%20MyHOME%20HPML0714.pdf) |
| `ST-00001031-EN` | Compatibility table | not stated in retained row | `067243..067245` occur on printed p. 2 / PDF p. 2 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/14/97/14971697bfbdbb33587b5724c7b38ac2aa6977e05e404556941291cafa589ad7.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00001031-EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 flush-mounted modules | Publisher documentation cited in this section |
| User controls | 4 capacitive touch zones | Publisher documentation cited in this section |
| Feedback | two light-blue LEDs per key zone, with adjustable intensity behavior | Publisher documentation cited in this section |
| SCS supply | `18..27 Vdc` | Publisher documentation cited in this section |
| Maximum consumption | `25 mA` at maximum LED level; `20 mA` medium; `17 mA` minimum | Publisher documentation cited in this section |
| Operating temperature | `0..40 °C` | Publisher documentation cited in this section |
| Depth | `18.3 mm` | Publisher documentation cited in this section |
| Physical labels | `A`, `PL`, `M`, `SPE`; rear programming/LED-intensity button `P` | Publisher documentation cited in this section |

For `573904..573907`, `LG00045-b-UK` establishes:


The programming pushbutton `P` is a physical user/programming control, not simply another firmware configuration value.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1376` | Canonical catalogue |
| Item model / `modobj` | `17` | Canonical catalogue / retained definition |
| Main system | Lighting / Automation | Canonical catalogue / retained definition |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `159` | `-1` | `-1` | `-1` | `5` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `159` | `1` | `410` Light control | Fixed/designated metadata | `920` | `410` | `578` |
| `159` | `1` | `411` Automation control | Candidate alternative | `924` | `411` | `579` |
| `159` | `1` | `412` Lock/unlock actuator control | Candidate alternative | `928` | `412` | `580` |
| `159` | `1` | `413` Scenario module control | Candidate alternative | `932` | `413` | `581` |
| `159` | `1` | `414` Scheduled scenario | Candidate alternative | `936` | `414` | `582` |
| `159` | `1` | `415` Scenario PLUS Lighting Management | Candidate alternative | `940` | `415` | `583` |
| `159` | `1` | `416` Scheduled scenario PLUS | Candidate alternative | `944` | `416` | `584` |
| `159` | `1` | `417` `AUX` control | Candidate alternative | `948` | `417` | `585` |
| `159` | `1` | `418` Open lock control | Candidate alternative | `952` | `418` | `586` |
| `159` | `1` | `419` Sound diffusion control | Candidate alternative | `956` | `419` | `587` |
| `159` | `1` | `421` Cyclic autoswitch control | Candidate alternative | `969` | `421` | `590` |
| `159` | `1` | `426` Staircase light control | Candidate alternative | `973` | `426` | `591` |
| `159` | `1` | `427` Floor call control | Candidate alternative | `977` | `427` | `592` |
| `159` | `1` | `462` Open lock command on session | Candidate alternative | `981` | `489` | `593` |
| `159` | `2` | `410` Light control | Fixed/designated metadata | `921` | `410` | `578` |
| `159` | `2` | `411` Automation control | Candidate alternative | `925` | `411` | `579` |
| `159` | `2` | `412` Lock/unlock actuator control | Candidate alternative | `929` | `412` | `580` |
| `159` | `2` | `413` Scenario module control | Candidate alternative | `933` | `413` | `581` |
| `159` | `2` | `414` Scheduled scenario | Candidate alternative | `937` | `414` | `582` |
| `159` | `2` | `415` Scenario PLUS Lighting Management | Candidate alternative | `941` | `415` | `583` |
| `159` | `2` | `416` Scheduled scenario PLUS | Candidate alternative | `945` | `416` | `584` |
| `159` | `2` | `417` `AUX` control | Candidate alternative | `949` | `417` | `585` |
| `159` | `2` | `418` Open lock control | Candidate alternative | `953` | `418` | `586` |
| `159` | `2` | `419` Sound diffusion control | Candidate alternative | `957` | `419` | `587` |
| `159` | `2` | `421` Cyclic autoswitch control | Candidate alternative | `970` | `421` | `590` |
| `159` | `2` | `426` Staircase light control | Candidate alternative | `974` | `426` | `591` |
| `159` | `2` | `427` Floor call control | Candidate alternative | `978` | `427` | `592` |
| `159` | `2` | `462` Open lock command on session | Candidate alternative | `982` | `489` | `593` |
| `159` | `3` | `410` Light control | Fixed/designated metadata | `922` | `410` | `578` |
| `159` | `3` | `411` Automation control | Candidate alternative | `926` | `411` | `579` |
| `159` | `3` | `412` Lock/unlock actuator control | Candidate alternative | `930` | `412` | `580` |
| `159` | `3` | `413` Scenario module control | Candidate alternative | `934` | `413` | `581` |
| `159` | `3` | `414` Scheduled scenario | Candidate alternative | `938` | `414` | `582` |
| `159` | `3` | `415` Scenario PLUS Lighting Management | Candidate alternative | `942` | `415` | `583` |
| `159` | `3` | `416` Scheduled scenario PLUS | Candidate alternative | `946` | `416` | `584` |
| `159` | `3` | `417` `AUX` control | Candidate alternative | `950` | `417` | `585` |
| `159` | `3` | `418` Open lock control | Candidate alternative | `954` | `418` | `586` |
| `159` | `3` | `419` Sound diffusion control | Candidate alternative | `958` | `419` | `587` |
| `159` | `3` | `421` Cyclic autoswitch control | Candidate alternative | `971` | `421` | `590` |
| `159` | `3` | `426` Staircase light control | Candidate alternative | `975` | `426` | `591` |
| `159` | `3` | `427` Floor call control | Candidate alternative | `979` | `427` | `592` |
| `159` | `3` | `462` Open lock command on session | Candidate alternative | `983` | `489` | `593` |
| `159` | `4` | `410` Light control | Fixed/designated metadata | `923` | `410` | `578` |
| `159` | `4` | `411` Automation control | Candidate alternative | `927` | `411` | `579` |
| `159` | `4` | `412` Lock/unlock actuator control | Candidate alternative | `931` | `412` | `580` |
| `159` | `4` | `413` Scenario module control | Candidate alternative | `935` | `413` | `581` |
| `159` | `4` | `414` Scheduled scenario | Candidate alternative | `939` | `414` | `582` |
| `159` | `4` | `415` Scenario PLUS Lighting Management | Candidate alternative | `943` | `415` | `583` |
| `159` | `4` | `416` Scheduled scenario PLUS | Candidate alternative | `947` | `416` | `584` |
| `159` | `4` | `417` `AUX` control | Candidate alternative | `951` | `417` | `585` |
| `159` | `4` | `418` Open lock control | Candidate alternative | `955` | `418` | `586` |
| `159` | `4` | `419` Sound diffusion control | Candidate alternative | `959` | `419` | `587` |
| `159` | `4` | `421` Cyclic autoswitch control | Candidate alternative | `972` | `421` | `590` |
| `159` | `4` | `426` Staircase light control | Candidate alternative | `976` | `426` | `591` |
| `159` | `4` | `427` Floor call control | Candidate alternative | `980` | `427` | `592` |
| `159` | `4` | `462` Open lock command on session | Candidate alternative | `984` | `489` | `593` |
| `159` | `5` | `130` User interface settings | Fixed/designated metadata | `919` | `480` | `577` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `159` | `521` Soft-Touch command virgin | `1`, `2`, `3`, `4` | `410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `418`, `419`, `421`, `426`, `427`, `462` | `521` | `36` |

### Reconciled topology notes


### Fixed UI Module

Slot `5` is fixed to Object `130`, **User interface settings**.

| Parameter | Domain |
| --- | --- |
| `STATE_OF_UNUSED_BUTTON` | `ON` / `OFF` |
| `STATE_UPDATE` | No / Yes |
| `LED_LEVEL` | `0..10`, default `6` |
| `LED_FADE` | `0..10`, default `5` |
| `BACKLIGHT_INTENSITY_STANDBY_LEVEL` | `OFF` or levels `1..10` |
| `SINGLE_LED_INTENSITY_STANDBY_LEVEL` | `OFF` or levels `1..10` |
| `BACKLIGHT_DELAY` | `0..255 s`, default `15` |
| `PROXIMITY_ENABLE` | Disable / Enable |
| `SIGNBOARD` | Off / Fixed / Chase |

The published sheet independently documents three LED intensity pairings for active/idle states: 100%/60%, 75%/30%, and 45%/off.

### Command Modules

Slots `1..4` use Virgin Object `521`, **Soft-Touch command virgin**, and can select:

| Object | Role |
| ---: | --- |
| `410` | Light control |
| `411` | Automation control |
| `412` | Lock/unlock actuator control |
| `413` | Scenario module control |
| `414` | Scheduled scenario |
| `415` | Scenario PLUS Lighting Management |
| `416` | Scheduled scenario PLUS |
| `417` | `AUX` control |
| `418` | Open lock control |
| `419` | Sound diffusion control |
| `421` | Cyclic autoswitch control |
| `426` | Staircase light control |
| `427` | Floor call control |
| `462` | Open lock command on session |

Light control `410` is the designated Object on all four command slots. The canonical firmware has **no `AS_SLOT_CONDITION` rows** for these slots, so the Device page must not invent a physical-condition-to-Object mapping from the mere Object list.

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `159` | Catalogue configuration route(s) described in retained notes | retained Device-specific configuration modality |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `159` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `159` | `A` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB` | `0` | A; Environment (0-9 `GEN`,`GR`,`AMB`) |
| `159` | `PL` | `0..9` | `0` | PL; Light Point |
| `159` | `M` | `0..3`; `5..6`; `9` = `O/I`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `14` = `CEN` | `0` | M; Mode physical configurator (0-3,5-6,`O/I`,SU_GIU,SU_GIU_M,`CEN`) |
| `159` | `SET` | `0..7` | `0` | SET; User interface settings configurator (0-7) |




### Published and reconciled details


The firmware-level fields are:

| Field | Stored domain | Evidence |
| --- | --- | --- |
| `AID` | Device identity field | Implementation evidence |
| `A` | `0..9`, `GEN`, `GR`, `AMB` | Implementation evidence |
| `PL` | `0..9` | Implementation evidence |
| `M` | `0,1,2,3,5,6,O/I,UP/DOWN,UP/DOWN monostable,CEN` | Implementation evidence |
| `SET` | `0..7` | Implementation evidence |

### Database/document mapping boundary

The physical technical sheet labels the configurator housing `A / PL / M / SPE` and separately identifies programming button `P`. The database instead stores `A / PL / M / SET`.

No equivalence between database `SET` and physical `SPE` is asserted here without further implementation evidence. Preserve both source models.

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


### Object `417` - `AUX` control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Cyclical; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `17` = DOWN Shutter bistable command; `18` = UP shutter monostable command; `4` = Reset BI; `5` = Reset TRI; `6` = Reset `GEN`; `1` = Disable; `2` = Enable; `16` = UP shutter bistable command; `19` = DOWN Shutter monostable command | `0` | Modality; mode(Cyclical,off,on,pul,up,down,...) |
| `OUT_AUX_CH` | `1..15` | `1` | `AUX` channel |
| `TYPE_CONTACT` | No legal values specified in source | `0` | Contact type |


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


### Object `421` - Cyclic autoswitch control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |


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


### Object `462` - Open lock command on session

Catalogue Object key `489` maps to external Object `462`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |


### Reconciled Object notes


The command Objects preserve their complete reusable parameter models in the canonical database. Principal surfaces include:

| Object family | Configuration surface |
| --- | --- |
| Light control `410` | 45 command-mode values; point/area/group/general address; installation/destination level; reference address; timed/dimming values |
| Automation control `411` | six `UP/DOWN` bistable/monostable variants; point/area/group/general addressing; installation/destination level |
| Lock/unlock `412` | enable/disable plus addressed target |
| Scenario module `413` | activation/edit mode, encoded A/PL, installation/destination level, scenario button `1..16`, delay table |
| Scheduled scenario `414` | A/PL, `CEN` button `0..31`, press/release mode |
| PLUS scenario `415/416` | scenario identifiers, regulation type, delays and button fields |
| `AUX` `417` | command mode plus `AUX` output channel `1..15` |
| Door-entry-related `418/421/426/427/462` | entrance/internal-unit identifiers, segment level, point/general selection as applicable |
| Sound diffusion `419` | `ON`/`OFF`/volume/track/source modes, audio addressing, follow-me/source/channel |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `159` | `410` | `1057` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `159` | `411` | `1061` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `159` | `412` | `1065` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `159` | `413` | `1069` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `159` | `414` | `1076` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `159` | `414` | `1077` | `MODE` | `0` = Press/release only; `1` = Press/hold/release (entire reusable range retained) | `0` | Mode for `CEN` command |
| `159` | `415` | `1081` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `159` | `416` | `1088` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `159` | `416` | `1089` | `MODE` | `0` = Press/release only; `1` = Press/hold/release (entire reusable range retained) | `0` | Mode for `CEN` command |
| `159` | `417` | `1093` | `TYPE_CONTACT` | No legal values specified in source (entire reusable range retained) | `0` | Contact type |
| `159` | `419` | `1097` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `159` | `426` | `4107` | `N1` | `100`; `101`; `102`; `103`; `104`; `105`; `106`; `107`; `108`; `109`; `110`; `111`; `112`; `113`; `114`; `115`; `116`; `117`; `118`; `119`; `120`; `121`; `122`; `123`; `124`; `125`; `126`; `127`; `128`; `129`; `130`; `131`; `132`; `133`; `134`; `135`; `136`; `137`; `138`; `139`; `140`; `141`; `142`; `143`; `144`; `145`; `146`; `147`; `148`; `149`; `150`; `151`; `152`; `153`; `154`; `155`; `156`; `157`; `158`; `159`; `160`; `161`; `162`; `163`; `164`; `165`; `166`; `167`; `168`; `169`; `170`; `171`; `172`; `173`; `174`; `175`; `176`; `177`; `178`; `179`; `180`; `181`; `182`; `183`; `184`; `185`; `186`; `187`; `188`; `189`; `190`; `191`; `192`; `193`; `194`; `195`; `196`; `197`; `198`; `199`; `200`; `201`; `202`; `203`; `204`; `205`; `206`; `207`; `208`; `209`; `210`; `211`; `212`; `213`; `214`; `215`; `216`; `217`; `218`; `219`; `220`; `221`; `222`; `223`; `224`; `225`; `226`; `227`; `228`; `229`; `230`; `231`; `232`; `233`; `234`; `235`; `236`; `237`; `238`; `239`; `240`; `241`; `242`; `243`; `244`; `245`; `246`; `247`; `248`; `249`; `250`; `251`; `252`; `253`; `254`; `255` | `0` | Internal unit address; reusable default `0` is outside this subset; filter supplies no replacement default |
| `159` | `427` | `1101` | `TO_ALL` | `1` = General | `1` | Type of call |
| `159` | `427` | `1904` | `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone (entire reusable range retained) | `0` | Segment |
| `159` | `130` | `3114` | `BACKLIGHT_INTENSITY_STANDBY_LEVEL` | `0` = `OFF`; `1` = Level1; `2` = Level2; `3` = Level3; `4` = Level4; `5` = Level5; `6` = Level6; `7` = Level7; `8` = Level8; `9` = Level9; `10` = Level10 (entire reusable range retained) | `1` | Backlight intensity stand by level |
| `159` | `130` | `3121` | `PROXIMITY_ENABLE` | `0` = Disable; `1` = Enable (entire reusable range retained) | `1` | Proximity Activation |
| `159` | `130` | `3128` | `SIGNBOARD` | `0` = Off; `1` = Fixe; `2` = Chase (entire reusable range retained) | `2` | Signboard activation type |
| `159` | `130` | `3136` | `SINGLE_LED_INTENSITY_STANDBY_LEVEL` | `0` = `OFF`; `1` = Level1; `2` = Level2; `3` = Level3; `4` = Level4; `5` = Level5; `6` = Level6; `7` = Level7; `8` = Level8; `9` = Level9; `10` = Level10 (entire reusable range retained) | `1` | when BACKLIGHT_INTENSITY_STANDBY_LEVEL is `OFF`, only one led can be used for the standby. |
| `159` | `130` | `3159` | `BACKLIGHT_DELAY` | `0..255` (entire reusable range retained) | `15` | Delay time (seconds) |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1376` and the installed model | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware without treating wildcard sentinels as literal installed values | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `418`, `419`, `421`, `426`, `427`, `130`, `462`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions, and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

### Existing Device-specific diagnostic notes


| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 17`, brand/line and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | enumerate four command Objects plus the UI-settings Module | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine configured functional addresses | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability


The technical sheet documents several physical behavior families:

- self-learning mode, cyclic or non-cyclic, where individual key functions can be learnt;
- scenario-module mode for recalling/programming scenarios;
- direct/swivelling lighting or shutter control of consecutive targets;
- `CEN` mode for use with a scenario programmer;
- sound-system mode when `SPE=1`;
- learned functions spanning lighting, automation, locking, staircase light, door release, floor call, camera cycling, sound diffusion, and `AUX` control.

It also specifies a two-minute self-calibration period after installation.

These published functions strongly corroborate the breadth of the catalogue Object set, but do not establish a one-to-one mapping between every physical mode and every database Object.

## Observed behavior and corroboration

No additional publishable runtime observation is asserted beyond observations explicitly retained elsewhere on this page.

## Programming

Programming must validate firmware applicability, active Module/Object topology, relation filters, and Device-specific configuration constraints.

## Source reconciliation


The archived touch-control sources establish user/programming behavior in addition to the catalogue Object set:

- the four capacitive zones can be temporarily disabled for cleaning, with the product restoring normal touch operation after the documented cleaning interval;
- self-learning can operate in cyclic and non-cyclic forms and includes explicit learn/delete procedures rather than being a generic “scenario” capability;
- scenario-module and `CEN`/programmed-scenario operation have distinct product programming workflows and button/address interpretations;
- sound-system operation assigns the touch zones to product-specific audio controls rather than treating them as ordinary lighting keys;
- front LED behavior, standby/active intensity and programming feedback are product functions of the fixed UI settings Module;
- after installation the Device performs an automatic calibration interval during which touch behavior must not be treated as normal steady-state operation.

These behaviors do not resolve the implementation `SPE` versus `SET` mapping; that source-model boundary remains explicit.

## Evidence limits and open work


- Locate direct product sheets for the Céliane `067273..067295` variants and Arteor `574089/574589`.
- Determine the exact relationship between physical `SPE`, database `SET`, and Object selection.
- Add sanitized hardware fingerprints from at least one Arteor and one Céliane variant.
- Corroborate the fifth UI-settings Module and four command Modules through `DIMENSION 30`.
- Preserve production-batch constraints such as the documented `13W05` minimum for `067243..067245`.

## Sources


- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
- [Programming](../../programming/)
