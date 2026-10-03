# Special-functions control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0043` | Project identity |
| Technical description | Two-module automation control exposing special-function Object alternatives | Canonical catalogue plus reconciled Device sources |
| Commercial identities | `H4651/2`, `L4651/2`, `AM5831/2`, `687376` | Canonical commercial records |
| Catalogue item | `1525` | Implementation evidence |
| Main catalogue system | Automation | Implementation evidence |
| Item model / `modobj` | `1` | Implementation evidence |
| Firmware definition | `147 / -1.-1.-1` | Implementation evidence |
| Declared Modules | `2` | Firmware catalogue |
| Categories | Automation, Control, Special functions | Capability model |

Two-module automation control exposing special-function Object alternatives.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4651/2` | established catalogue identity for item `1525` | canonical commercial record |
| BTicino - LivingLight | `L4651/2` | established catalogue identity for item `1525` | canonical commercial record |
| BTicino - Matix | `AM5831/2` | established catalogue identity for item `1525` | canonical commercial record |
| Legrand - Vela | `687376` | established catalogue identity for item `1525` | canonical commercial record |
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| AUTOMATISME | technical/system documentation | revision/date as printed | MyHOME automation control model; exact four identities still need direct-sheet reconciliation | [Archived original](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Product role | Bus automation control with selectable special-function topology | Canonical item/Object model |
| Declared logical modules | 2 | Canonical firmware catalogue |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1525` | Implementation evidence |
| Technical item description | Special-functions control | Implementation evidence |
| Main system | Automation | Implementation evidence |
| Item model / `modobj` | `1` | Implementation evidence |
| Commercial records | `4` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `147` | `-1` | `-1` | `-1` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `147` | `1` | `400` Light control | Fixed/designated metadata | `560` | `400` | `380` |
| `147` | `1` | `401` Automation control | Candidate alternative | `541` | `401` | `372` |
| `147` | `1` | `402` Lock/unlock actuator control | Candidate alternative | `543` | `402` | `373` |
| `147` | `1` | `403` Scenario module control | Candidate alternative | `545` | `403` | `374` |
| `147` | `1` | `404` Scheduled scenario | Candidate alternative | `547` | `404` | `375` |
| `147` | `1` | `408` Open lock control | Candidate alternative | `549` | `408` | `376` |
| `147` | `1` | `409` Sound diffusion control | Candidate alternative | `562` | `409` | `381` |
| `147` | `2` | `400` Light control | Fixed/designated metadata | `561` | `400` | `380` |
| `147` | `2` | `401` Automation control | Candidate alternative | `542` | `401` | `372` |
| `147` | `2` | `402` Lock/unlock actuator control | Candidate alternative | `544` | `402` | `373` |
| `147` | `2` | `403` Scenario module control | Candidate alternative | `546` | `403` | `374` |
| `147` | `2` | `404` Scheduled scenario | Candidate alternative | `548` | `404` | `375` |
| `147` | `2` | `408` Open lock control | Candidate alternative | `550` | `408` | `376` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `147` | `501` Special double command virgin | `1`, `2` | `400`, `401`, `402`, `403`, `404`, `405`, `406`, `407`, `408`, `409`, `427`, `430` | `501` | `20` |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `147` | Physical configuration | supported route for this Device family |
| `147` | Virtual Configuration | supported route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `147` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `147` | `A` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB` | `0` | A; Environment (0-9 `GEN`,`GR`,`AMB`) |
| `147` | `PL` | `0..9` | `0` | PL; Light Point |
| `147` | `M` | `0..8`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `15` = `PUL` | `0` | M; Mode physical configurator (0-8, `O/I`,`OFF`,`ON`,SU_GIU,SU_GIU_M,`PUL`) |
| `147` | `SPE` | `0..9` | `0` | SPE; Special function command control (0-9) |
| `147` | `AUX` | `0..9` | `0` | `AUX`; `AUX` channel |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `400` - Light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `1` = Timed `ON`; `2` = Toggle dimmer; `3` = `ON`/`OFF` and dimming; `4` = Toggle `ON`/`OFF`; `5` = `ON`/`OFF`; `9` = `ON`/`OFF` and point to point dimming; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90%; `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `130` = Customized `ON`/`OFF` and point to point dimmer; `131` = Customized toggle dimmer; `132` = Customized `ON`/`OFF` and dimmer; `133` = Customized toggle dimmer without regulation; `134` = Customized `ON`/`OFF` and dimmer without regulation | `0` | Modality; Standard mode means: with regulation for Point-to-point addressing, without regulation for Area, Group and General addressing |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Light point of reference actuator; 0=no referent address |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0=no referent address |
| `HOURS` | `0..255` | `0` | Hours; Only for `MOD=128` |
| `MINUTES` | `0..59` | `0` | Minutes; Only for `MOD=128` |
| `SECONDS` | `0..59` | `30` | Seconds; Only for `MOD=128` |
| `LEVEL` | `0..100` | `100` | Level; Only for `MOD=129-134` |
| `START_S` | `0..255` | `255` | Soft start speed; Only for `MOD=129-134` |
| `STOP_S` | `0..255` | `255` | Soft stop speed; Only for `MOD=129-134` |
| `DIMMING_S` | `0..255` | `255` | Dimming speed; Only for `MOD=129-132` |
| `T_TIME` | `1` = 1 min; `2` = 2 min; `3` = 3 min; `4` = 4 min; `5` = 5 min; `6` = 15 min; `7` = 30 s; `8` = 0.5 s; `9` = 2 s; `10` = 10 min | `1` | Tabled time; Only for `MOD=1` |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |


### Object `401` - Automation control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `12` = Bistable control; `13` = Monostable control; `14` = Blades control and bistable | `12` | Modality |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |


### Object `402` - Lock/unlock actuator control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `1` = Disable (lower button); `2` = Enable (lower button); `3` = Disable (lower button) - enable (upper button) | `1` | Modality |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = All systems | `0` | Destination level |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |


### Object `403` - Scenario module control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Scenario activation and modification; `1` = Scenario activation | `0` | Modality |
| `APL` | `0..175`; encoded by `APL=16*A+PL`, with `A=0..10` and `PL=0..15` | `0` | Scenario module address |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number | `0` | Destination level |
| `SCE_BUTT_1` | `1..16` | `1` | Upper button scenario |
| `SCE_BUTT_2` | `1..16` | `2` | Lower button scenario |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `43` = 43 s; `44` = 44 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for upper button |
| `DEL_BUTTON_2` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `36` = 36 s; `37` = 37 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `69` = 9 min; `70` = 10 min | `0` | Activation delay for lower button |


### Object `404` - Scheduled scenario

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `BUTTON_1` | `0..31` | `1` | Upper button |
| `BUTTON_2` | `0..31` | `2` | Lower button |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |
| `START_DELAY` | `0..255` | `10` | Time of restart device (s) |


### Object `408` - Open lock control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEGMENT` | `0` = Same level; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Level |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |


### Object `409` - Sound diffusion control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `3` = General | `0` | Addressing type |
| `A` | `0..9` | `0` | Area |
| `PF` | `0..9` | `0` | Audio point |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |
| `IS_FOLLOW_ME` | `0` = No; `1` = Yes | `1` | Follow me |
| `SOURCE` | `1..9` | `1` | Source |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `147` | `1` | `400` | `4145` | No textual predicate stored | None |
| `147` | `1` | `400` | `4178` | `A=AMB` | `108` |
| `147` | `1` | `400` | `4182` | `A=GEN` | `109` |
| `147` | `1` | `400` | `4185` | `A=GR` | `107` |
| `147` | `1` | `401` | `4669` | `M=SU_GIU;SPE=0` | None |
| `147` | `1` | `401` | `4670` | `M=SU_GIU;SPE=0;A=AMB` | `108` |
| `147` | `1` | `401` | `4671` | `M=SU_GIU;SPE=0;A=GEN` | `109` |
| `147` | `1` | `401` | `4672` | `M=SU_GIU;SPE=0;A=GR` | `107` |
| `147` | `1` | `401` | `4690` | `M=SU_GIU_M;SPE=0` | None |
| `147` | `1` | `401` | `4691` | `M=SU_GIU_M;SPE=0;A=AMB` | `108` |
| `147` | `1` | `401` | `4692` | `M=SU_GIU_M;SPE=0;A=GEN` | `109` |
| `147` | `1` | `401` | `4693` | `M=SU_GIU_M;SPE=0;A=GR` | `107` |
| `147` | `1` | `402` | `4423` | `M<>0;SPE=1` | None |
| `147` | `1` | `402` | `4424` | `M<>0;SPE=1;A=AMB` | `108` |
| `147` | `1` | `402` | `4425` | `M<>0;SPE=1;A=GEN` | `109` |
| `147` | `1` | `402` | `4426` | `M<>0;SPE=1;A=GR` | `107` |
| `147` | `1` | `403` | `4428` | `M<>0;SPE=4` | None |
| `147` | `1` | `403` | `4430` | `M<>0;SPE=6` | None |
| `147` | `1` | `404` | `4593` | `M=CEN;SPE=0` | None |
| `147` | `1` | `408` | `4877` | `SPE=9` | None |
| `147` | `1` | `409` | `4874` | `SPE=8` | None |
| `147` | `2` | `400` | `4145` | No textual predicate stored | None |
| `147` | `2` | `400` | `4178` | `A=AMB` | `108` |
| `147` | `2` | `400` | `4182` | `A=GEN` | `109` |
| `147` | `2` | `400` | `4185` | `A=GR` | `107` |
| `147` | `2` | `401` | `4669` | `M=SU_GIU;SPE=0` | None |
| `147` | `2` | `401` | `4670` | `M=SU_GIU;SPE=0;A=AMB` | `108` |
| `147` | `2` | `401` | `4671` | `M=SU_GIU;SPE=0;A=GEN` | `109` |
| `147` | `2` | `401` | `4672` | `M=SU_GIU;SPE=0;A=GR` | `107` |
| `147` | `2` | `401` | `4690` | `M=SU_GIU_M;SPE=0` | None |
| `147` | `2` | `401` | `4691` | `M=SU_GIU_M;SPE=0;A=AMB` | `108` |
| `147` | `2` | `401` | `4692` | `M=SU_GIU_M;SPE=0;A=GEN` | `109` |
| `147` | `2` | `401` | `4693` | `M=SU_GIU_M;SPE=0;A=GR` | `107` |
| `147` | `2` | `402` | `4423` | `M<>0;SPE=1` | None |
| `147` | `2` | `402` | `4424` | `M<>0;SPE=1;A=AMB` | `108` |
| `147` | `2` | `402` | `4425` | `M<>0;SPE=1;A=GEN` | `109` |
| `147` | `2` | `402` | `4426` | `M<>0;SPE=1;A=GR` | `107` |
| `147` | `2` | `403` | `4428` | `M<>0;SPE=4` | None |
| `147` | `2` | `403` | `4430` | `M<>0;SPE=6` | None |
| `147` | `2` | `404` | `4593` | `M=CEN;SPE=0` | None |
| `147` | `2` | `408` | `4877` | `SPE=9` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `147` | `402` | `287` | `INST_LEV` | `8` = Local bus 8 | `16` | Installation level; reusable default `16` is outside this subset; filter supplies no replacement default |
| `147` | `403` | `289` | `INST_LEV` | `8` = Local bus 8 | `16` | Installation level; reusable default `16` is outside this subset; filter supplies no replacement default |
| `147` | `404` | `1709` | `START_DELAY` | `0..255` (entire reusable range retained) | `10` | Start delay |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `107` | `M=0` | `ADDR_TYPE` = `2` | `107` |
| `107` | `M=1` | `ADDR_TYPE` = `2` | `107` |
| `107` | `M=2` | `ADDR_TYPE` = `2` | `107` |
| `107` | `M=3` | `ADDR_TYPE` = `2` | `107` |
| `107` | `M=4` | `ADDR_TYPE` = `2` | `107` |
| `107` | `M=5` | `ADDR_TYPE` = `2` | `107` |
| `107` | `M=6` | `ADDR_TYPE` = `2` | `107` |
| `107` | `M=7` | `ADDR_TYPE` = `2` | `107` |
| `107` | `M=8` | `ADDR_TYPE` = `2` | `107` |
| `107` | `M=O/I` | `ADDR_TYPE` = `2` | `107` |
| `107` | `M=OFF` | `ADDR_TYPE` = `2` | `107` |
| `107` | `M=ON` | `ADDR_TYPE` = `2` | `107` |
| `107` | `M=PUL` | `ADDR_TYPE` = `2` | `107` |
| `107` | `M=SU_GIU` | `ADDR_TYPE` = `2` | `107` |
| `107` | `M=SU_GIU_M` | `ADDR_TYPE` = `2` | `107` |
| `107` | `M=0; PL=1` | `G1` = `1` | `107` → `300` |
| `107` | `M=0; PL=2` | `G1` = `2` | `107` → `300` |
| `107` | `M=0; PL=3` | `G1` = `3` | `107` → `300` |
| `107` | `M=0; PL=4` | `G1` = `4` | `107` → `300` |
| `107` | `M=0; PL=5` | `G1` = `5` | `107` → `300` |
| `107` | `M=0; PL=6` | `G1` = `6` | `107` → `300` |
| `107` | `M=0; PL=7` | `G1` = `7` | `107` → `300` |
| `107` | `M=0; PL=8` | `G1` = `8` | `107` → `300` |
| `107` | `M=0; PL=9` | `G1` = `9` | `107` → `300` |
| `107` | `M=1; PL=1` | `G1` = `1` | `107` → `300` |
| `107` | `M=1; PL=2` | `G1` = `2` | `107` → `300` |
| `107` | `M=1; PL=3` | `G1` = `3` | `107` → `300` |
| `107` | `M=1; PL=4` | `G1` = `4` | `107` → `300` |
| `107` | `M=1; PL=5` | `G1` = `5` | `107` → `300` |
| `107` | `M=1; PL=6` | `G1` = `6` | `107` → `300` |
| `107` | `M=1; PL=7` | `G1` = `7` | `107` → `300` |
| `107` | `M=1; PL=8` | `G1` = `8` | `107` → `300` |
| `107` | `M=1; PL=9` | `G1` = `9` | `107` → `300` |
| `107` | `M=2; PL=1` | `G1` = `1` | `107` → `300` |
| `107` | `M=2; PL=2` | `G1` = `2` | `107` → `300` |
| `107` | `M=2; PL=3` | `G1` = `3` | `107` → `300` |
| `107` | `M=2; PL=4` | `G1` = `4` | `107` → `300` |
| `107` | `M=2; PL=5` | `G1` = `5` | `107` → `300` |
| `107` | `M=2; PL=6` | `G1` = `6` | `107` → `300` |
| `107` | `M=2; PL=7` | `G1` = `7` | `107` → `300` |
| `107` | `M=2; PL=8` | `G1` = `8` | `107` → `300` |
| `107` | `M=2; PL=9` | `G1` = `9` | `107` → `300` |
| `107` | `M=3; PL=1` | `G1` = `1` | `107` → `300` |
| `107` | `M=3; PL=2` | `G1` = `2` | `107` → `300` |
| `107` | `M=3; PL=3` | `G1` = `3` | `107` → `300` |
| `107` | `M=3; PL=4` | `G1` = `4` | `107` → `300` |
| `107` | `M=3; PL=5` | `G1` = `5` | `107` → `300` |
| `107` | `M=3; PL=6` | `G1` = `6` | `107` → `300` |
| `107` | `M=3; PL=7` | `G1` = `7` | `107` → `300` |
| `107` | `M=3; PL=8` | `G1` = `8` | `107` → `300` |
| `107` | `M=3; PL=9` | `G1` = `9` | `107` → `300` |
| `107` | `M=4; PL=1` | `G1` = `1` | `107` → `300` |
| `107` | `M=4; PL=2` | `G1` = `2` | `107` → `300` |
| `107` | `M=4; PL=3` | `G1` = `3` | `107` → `300` |
| `107` | `M=4; PL=4` | `G1` = `4` | `107` → `300` |
| `107` | `M=4; PL=5` | `G1` = `5` | `107` → `300` |
| `107` | `M=4; PL=6` | `G1` = `6` | `107` → `300` |
| `107` | `M=4; PL=7` | `G1` = `7` | `107` → `300` |
| `107` | `M=4; PL=8` | `G1` = `8` | `107` → `300` |
| `107` | `M=4; PL=9` | `G1` = `9` | `107` → `300` |
| `107` | `M=5; PL=1` | `G1` = `1` | `107` → `300` |
| `107` | `M=5; PL=2` | `G1` = `2` | `107` → `300` |
| `107` | `M=5; PL=3` | `G1` = `3` | `107` → `300` |
| `107` | `M=5; PL=4` | `G1` = `4` | `107` → `300` |
| `107` | `M=5; PL=5` | `G1` = `5` | `107` → `300` |
| `107` | `M=5; PL=6` | `G1` = `6` | `107` → `300` |
| `107` | `M=5; PL=7` | `G1` = `7` | `107` → `300` |
| `107` | `M=5; PL=8` | `G1` = `8` | `107` → `300` |
| `107` | `M=5; PL=9` | `G1` = `9` | `107` → `300` |
| `107` | `M=6; PL=1` | `G1` = `1` | `107` → `300` |
| `107` | `M=6; PL=2` | `G1` = `2` | `107` → `300` |
| `107` | `M=6; PL=3` | `G1` = `3` | `107` → `300` |
| `107` | `M=6; PL=4` | `G1` = `4` | `107` → `300` |
| `107` | `M=6; PL=5` | `G1` = `5` | `107` → `300` |
| `107` | `M=6; PL=6` | `G1` = `6` | `107` → `300` |
| `107` | `M=6; PL=7` | `G1` = `7` | `107` → `300` |
| `107` | `M=6; PL=8` | `G1` = `8` | `107` → `300` |
| `107` | `M=6; PL=9` | `G1` = `9` | `107` → `300` |
| `107` | `M=7; PL=1` | `G1` = `1` | `107` → `300` |
| `107` | `M=7; PL=2` | `G1` = `2` | `107` → `300` |
| `107` | `M=7; PL=3` | `G1` = `3` | `107` → `300` |
| `107` | `M=7; PL=4` | `G1` = `4` | `107` → `300` |
| `107` | `M=7; PL=5` | `G1` = `5` | `107` → `300` |
| `107` | `M=7; PL=6` | `G1` = `6` | `107` → `300` |
| `107` | `M=7; PL=7` | `G1` = `7` | `107` → `300` |
| `107` | `M=7; PL=8` | `G1` = `8` | `107` → `300` |
| `107` | `M=7; PL=9` | `G1` = `9` | `107` → `300` |
| `107` | `M=8; PL=1` | `G1` = `1` | `107` → `300` |
| `107` | `M=8; PL=2` | `G1` = `2` | `107` → `300` |
| `107` | `M=8; PL=3` | `G1` = `3` | `107` → `300` |
| `107` | `M=8; PL=4` | `G1` = `4` | `107` → `300` |
| `107` | `M=8; PL=5` | `G1` = `5` | `107` → `300` |
| `107` | `M=8; PL=6` | `G1` = `6` | `107` → `300` |
| `107` | `M=8; PL=7` | `G1` = `7` | `107` → `300` |
| `107` | `M=8; PL=8` | `G1` = `8` | `107` → `300` |
| `107` | `M=8; PL=9` | `G1` = `9` | `107` → `300` |
| `107` | `M=O/I; PL=1` | `G1` = `1` | `107` → `300` |
| `107` | `M=O/I; PL=2` | `G1` = `2` | `107` → `300` |
| `107` | `M=O/I; PL=3` | `G1` = `3` | `107` → `300` |
| `107` | `M=O/I; PL=4` | `G1` = `4` | `107` → `300` |
| `107` | `M=O/I; PL=5` | `G1` = `5` | `107` → `300` |
| `107` | `M=O/I; PL=6` | `G1` = `6` | `107` → `300` |
| `107` | `M=O/I; PL=7` | `G1` = `7` | `107` → `300` |
| `107` | `M=O/I; PL=8` | `G1` = `8` | `107` → `300` |
| `107` | `M=O/I; PL=9` | `G1` = `9` | `107` → `300` |
| `107` | `M=OFF; PL=1` | `G1` = `1` | `107` → `300` |
| `107` | `M=OFF; PL=2` | `G1` = `2` | `107` → `300` |
| `107` | `M=OFF; PL=3` | `G1` = `3` | `107` → `300` |
| `107` | `M=OFF; PL=4` | `G1` = `4` | `107` → `300` |
| `107` | `M=OFF; PL=5` | `G1` = `5` | `107` → `300` |
| `107` | `M=OFF; PL=6` | `G1` = `6` | `107` → `300` |
| `107` | `M=OFF; PL=7` | `G1` = `7` | `107` → `300` |
| `107` | `M=OFF; PL=8` | `G1` = `8` | `107` → `300` |
| `107` | `M=OFF; PL=9` | `G1` = `9` | `107` → `300` |
| `107` | `M=ON; PL=1` | `G1` = `1` | `107` → `300` |
| `107` | `M=ON; PL=2` | `G1` = `2` | `107` → `300` |
| `107` | `M=ON; PL=3` | `G1` = `3` | `107` → `300` |
| `107` | `M=ON; PL=4` | `G1` = `4` | `107` → `300` |
| `107` | `M=ON; PL=5` | `G1` = `5` | `107` → `300` |
| `107` | `M=ON; PL=6` | `G1` = `6` | `107` → `300` |
| `107` | `M=ON; PL=7` | `G1` = `7` | `107` → `300` |
| `107` | `M=ON; PL=8` | `G1` = `8` | `107` → `300` |
| `107` | `M=ON; PL=9` | `G1` = `9` | `107` → `300` |
| `107` | `M=PUL; PL=1` | `G1` = `1` | `107` → `300` |
| `107` | `M=PUL; PL=2` | `G1` = `2` | `107` → `300` |
| `107` | `M=PUL; PL=3` | `G1` = `3` | `107` → `300` |
| `107` | `M=PUL; PL=4` | `G1` = `4` | `107` → `300` |
| `107` | `M=PUL; PL=5` | `G1` = `5` | `107` → `300` |
| `107` | `M=PUL; PL=6` | `G1` = `6` | `107` → `300` |
| `107` | `M=PUL; PL=7` | `G1` = `7` | `107` → `300` |
| `107` | `M=PUL; PL=8` | `G1` = `8` | `107` → `300` |
| `107` | `M=PUL; PL=9` | `G1` = `9` | `107` → `300` |
| `107` | `M=SU_GIU; PL=1` | `G1` = `1` | `107` → `300` |
| `107` | `M=SU_GIU; PL=2` | `G1` = `2` | `107` → `300` |
| `107` | `M=SU_GIU; PL=3` | `G1` = `3` | `107` → `300` |
| `107` | `M=SU_GIU; PL=4` | `G1` = `4` | `107` → `300` |
| `107` | `M=SU_GIU; PL=5` | `G1` = `5` | `107` → `300` |
| `107` | `M=SU_GIU; PL=6` | `G1` = `6` | `107` → `300` |
| `107` | `M=SU_GIU; PL=7` | `G1` = `7` | `107` → `300` |
| `107` | `M=SU_GIU; PL=8` | `G1` = `8` | `107` → `300` |
| `107` | `M=SU_GIU; PL=9` | `G1` = `9` | `107` → `300` |
| `107` | `M=SU_GIU_M; PL=1` | `G1` = `1` | `107` → `300` |
| `107` | `M=SU_GIU_M; PL=2` | `G1` = `2` | `107` → `300` |
| `107` | `M=SU_GIU_M; PL=3` | `G1` = `3` | `107` → `300` |
| `107` | `M=SU_GIU_M; PL=4` | `G1` = `4` | `107` → `300` |
| `107` | `M=SU_GIU_M; PL=5` | `G1` = `5` | `107` → `300` |
| `107` | `M=SU_GIU_M; PL=6` | `G1` = `6` | `107` → `300` |
| `107` | `M=SU_GIU_M; PL=7` | `G1` = `7` | `107` → `300` |
| `107` | `M=SU_GIU_M; PL=8` | `G1` = `8` | `107` → `300` |
| `107` | `M=SU_GIU_M; PL=9` | `G1` = `9` | `107` → `300` |
| `108` | `M=0` | `ADDR_TYPE` = `1` | `108` |
| `108` | `M=1` | `ADDR_TYPE` = `1` | `108` |
| `108` | `M=2` | `ADDR_TYPE` = `1` | `108` |
| `108` | `M=3` | `ADDR_TYPE` = `1` | `108` |
| `108` | `M=4` | `ADDR_TYPE` = `1` | `108` |
| `108` | `M=5` | `ADDR_TYPE` = `1` | `108` |
| `108` | `M=6` | `ADDR_TYPE` = `1` | `108` |
| `108` | `M=7` | `ADDR_TYPE` = `1` | `108` |
| `108` | `M=8` | `ADDR_TYPE` = `1` | `108` |
| `108` | `M=O/I` | `ADDR_TYPE` = `1` | `108` |
| `108` | `M=OFF` | `ADDR_TYPE` = `1` | `108` |
| `108` | `M=ON` | `ADDR_TYPE` = `1` | `108` |
| `108` | `M=PUL` | `ADDR_TYPE` = `1` | `108` |
| `108` | `M=SU_GIU` | `ADDR_TYPE` = `1` | `108` |
| `108` | `M=SU_GIU_M` | `ADDR_TYPE` = `1` | `108` |
| `108` | `M=0; PL=1` | `A` = `1` | `108` → `301` |
| `108` | `M=0; PL=2` | `A` = `2` | `108` → `301` |
| `108` | `M=0; PL=3` | `A` = `3` | `108` → `301` |
| `108` | `M=0; PL=4` | `A` = `4` | `108` → `301` |
| `108` | `M=0; PL=5` | `A` = `5` | `108` → `301` |
| `108` | `M=0; PL=6` | `A` = `6` | `108` → `301` |
| `108` | `M=0; PL=7` | `A` = `7` | `108` → `301` |
| `108` | `M=0; PL=8` | `A` = `8` | `108` → `301` |
| `108` | `M=0; PL=9` | `A` = `9` | `108` → `301` |
| `108` | `M=1; PL=1` | `A` = `1` | `108` → `301` |
| `108` | `M=1; PL=2` | `A` = `2` | `108` → `301` |
| `108` | `M=1; PL=3` | `A` = `3` | `108` → `301` |
| `108` | `M=1; PL=4` | `A` = `4` | `108` → `301` |
| `108` | `M=1; PL=5` | `A` = `5` | `108` → `301` |
| `108` | `M=1; PL=6` | `A` = `6` | `108` → `301` |
| `108` | `M=1; PL=7` | `A` = `7` | `108` → `301` |
| `108` | `M=1; PL=8` | `A` = `8` | `108` → `301` |
| `108` | `M=1; PL=9` | `A` = `9` | `108` → `301` |
| `108` | `M=2; PL=1` | `A` = `1` | `108` → `301` |
| `108` | `M=2; PL=2` | `A` = `2` | `108` → `301` |
| `108` | `M=2; PL=3` | `A` = `3` | `108` → `301` |
| `108` | `M=2; PL=4` | `A` = `4` | `108` → `301` |
| `108` | `M=2; PL=5` | `A` = `5` | `108` → `301` |
| `108` | `M=2; PL=6` | `A` = `6` | `108` → `301` |
| `108` | `M=2; PL=7` | `A` = `7` | `108` → `301` |
| `108` | `M=2; PL=8` | `A` = `8` | `108` → `301` |
| `108` | `M=2; PL=9` | `A` = `9` | `108` → `301` |
| `108` | `M=3; PL=1` | `A` = `1` | `108` → `301` |
| `108` | `M=3; PL=2` | `A` = `2` | `108` → `301` |
| `108` | `M=3; PL=3` | `A` = `3` | `108` → `301` |
| `108` | `M=3; PL=4` | `A` = `4` | `108` → `301` |
| `108` | `M=3; PL=5` | `A` = `5` | `108` → `301` |
| `108` | `M=3; PL=6` | `A` = `6` | `108` → `301` |
| `108` | `M=3; PL=7` | `A` = `7` | `108` → `301` |
| `108` | `M=3; PL=8` | `A` = `8` | `108` → `301` |
| `108` | `M=3; PL=9` | `A` = `9` | `108` → `301` |
| `108` | `M=4; PL=1` | `A` = `1` | `108` → `301` |
| `108` | `M=4; PL=2` | `A` = `2` | `108` → `301` |
| `108` | `M=4; PL=3` | `A` = `3` | `108` → `301` |
| `108` | `M=4; PL=4` | `A` = `4` | `108` → `301` |
| `108` | `M=4; PL=5` | `A` = `5` | `108` → `301` |
| `108` | `M=4; PL=6` | `A` = `6` | `108` → `301` |
| `108` | `M=4; PL=7` | `A` = `7` | `108` → `301` |
| `108` | `M=4; PL=8` | `A` = `8` | `108` → `301` |
| `108` | `M=4; PL=9` | `A` = `9` | `108` → `301` |
| `108` | `M=5; PL=1` | `A` = `1` | `108` → `301` |
| `108` | `M=5; PL=2` | `A` = `2` | `108` → `301` |
| `108` | `M=5; PL=3` | `A` = `3` | `108` → `301` |
| `108` | `M=5; PL=4` | `A` = `4` | `108` → `301` |
| `108` | `M=5; PL=5` | `A` = `5` | `108` → `301` |
| `108` | `M=5; PL=6` | `A` = `6` | `108` → `301` |
| `108` | `M=5; PL=7` | `A` = `7` | `108` → `301` |
| `108` | `M=5; PL=8` | `A` = `8` | `108` → `301` |
| `108` | `M=5; PL=9` | `A` = `9` | `108` → `301` |
| `108` | `M=6; PL=1` | `A` = `1` | `108` → `301` |
| `108` | `M=6; PL=2` | `A` = `2` | `108` → `301` |
| `108` | `M=6; PL=3` | `A` = `3` | `108` → `301` |
| `108` | `M=6; PL=4` | `A` = `4` | `108` → `301` |
| `108` | `M=6; PL=5` | `A` = `5` | `108` → `301` |
| `108` | `M=6; PL=6` | `A` = `6` | `108` → `301` |
| `108` | `M=6; PL=7` | `A` = `7` | `108` → `301` |
| `108` | `M=6; PL=8` | `A` = `8` | `108` → `301` |
| `108` | `M=6; PL=9` | `A` = `9` | `108` → `301` |
| `108` | `M=7; PL=1` | `A` = `1` | `108` → `301` |
| `108` | `M=7; PL=2` | `A` = `2` | `108` → `301` |
| `108` | `M=7; PL=3` | `A` = `3` | `108` → `301` |
| `108` | `M=7; PL=4` | `A` = `4` | `108` → `301` |
| `108` | `M=7; PL=5` | `A` = `5` | `108` → `301` |
| `108` | `M=7; PL=6` | `A` = `6` | `108` → `301` |
| `108` | `M=7; PL=7` | `A` = `7` | `108` → `301` |
| `108` | `M=7; PL=8` | `A` = `8` | `108` → `301` |
| `108` | `M=7; PL=9` | `A` = `9` | `108` → `301` |
| `108` | `M=8; PL=1` | `A` = `1` | `108` → `301` |
| `108` | `M=8; PL=2` | `A` = `2` | `108` → `301` |
| `108` | `M=8; PL=3` | `A` = `3` | `108` → `301` |
| `108` | `M=8; PL=4` | `A` = `4` | `108` → `301` |
| `108` | `M=8; PL=5` | `A` = `5` | `108` → `301` |
| `108` | `M=8; PL=6` | `A` = `6` | `108` → `301` |
| `108` | `M=8; PL=7` | `A` = `7` | `108` → `301` |
| `108` | `M=8; PL=8` | `A` = `8` | `108` → `301` |
| `108` | `M=8; PL=9` | `A` = `9` | `108` → `301` |
| `108` | `M=O/I; PL=1` | `A` = `1` | `108` → `301` |
| `108` | `M=O/I; PL=2` | `A` = `2` | `108` → `301` |
| `108` | `M=O/I; PL=3` | `A` = `3` | `108` → `301` |
| `108` | `M=O/I; PL=4` | `A` = `4` | `108` → `301` |
| `108` | `M=O/I; PL=5` | `A` = `5` | `108` → `301` |
| `108` | `M=O/I; PL=6` | `A` = `6` | `108` → `301` |
| `108` | `M=O/I; PL=7` | `A` = `7` | `108` → `301` |
| `108` | `M=O/I; PL=8` | `A` = `8` | `108` → `301` |
| `108` | `M=O/I; PL=9` | `A` = `9` | `108` → `301` |
| `108` | `M=OFF; PL=1` | `A` = `1` | `108` → `301` |
| `108` | `M=OFF; PL=2` | `A` = `2` | `108` → `301` |
| `108` | `M=OFF; PL=3` | `A` = `3` | `108` → `301` |
| `108` | `M=OFF; PL=4` | `A` = `4` | `108` → `301` |
| `108` | `M=OFF; PL=5` | `A` = `5` | `108` → `301` |
| `108` | `M=OFF; PL=6` | `A` = `6` | `108` → `301` |
| `108` | `M=OFF; PL=7` | `A` = `7` | `108` → `301` |
| `108` | `M=OFF; PL=8` | `A` = `8` | `108` → `301` |
| `108` | `M=OFF; PL=9` | `A` = `9` | `108` → `301` |
| `108` | `M=ON; PL=1` | `A` = `1` | `108` → `301` |
| `108` | `M=ON; PL=2` | `A` = `2` | `108` → `301` |
| `108` | `M=ON; PL=3` | `A` = `3` | `108` → `301` |
| `108` | `M=ON; PL=4` | `A` = `4` | `108` → `301` |
| `108` | `M=ON; PL=5` | `A` = `5` | `108` → `301` |
| `108` | `M=ON; PL=6` | `A` = `6` | `108` → `301` |
| `108` | `M=ON; PL=7` | `A` = `7` | `108` → `301` |
| `108` | `M=ON; PL=8` | `A` = `8` | `108` → `301` |
| `108` | `M=ON; PL=9` | `A` = `9` | `108` → `301` |
| `108` | `M=PUL; PL=1` | `A` = `1` | `108` → `301` |
| `108` | `M=PUL; PL=2` | `A` = `2` | `108` → `301` |
| `108` | `M=PUL; PL=3` | `A` = `3` | `108` → `301` |
| `108` | `M=PUL; PL=4` | `A` = `4` | `108` → `301` |
| `108` | `M=PUL; PL=5` | `A` = `5` | `108` → `301` |
| `108` | `M=PUL; PL=6` | `A` = `6` | `108` → `301` |
| `108` | `M=PUL; PL=7` | `A` = `7` | `108` → `301` |
| `108` | `M=PUL; PL=8` | `A` = `8` | `108` → `301` |
| `108` | `M=PUL; PL=9` | `A` = `9` | `108` → `301` |
| `108` | `M=SU_GIU; PL=1` | `A` = `1` | `108` → `301` |
| `108` | `M=SU_GIU; PL=2` | `A` = `2` | `108` → `301` |
| `108` | `M=SU_GIU; PL=3` | `A` = `3` | `108` → `301` |
| `108` | `M=SU_GIU; PL=4` | `A` = `4` | `108` → `301` |
| `108` | `M=SU_GIU; PL=5` | `A` = `5` | `108` → `301` |
| `108` | `M=SU_GIU; PL=6` | `A` = `6` | `108` → `301` |
| `108` | `M=SU_GIU; PL=7` | `A` = `7` | `108` → `301` |
| `108` | `M=SU_GIU; PL=8` | `A` = `8` | `108` → `301` |
| `108` | `M=SU_GIU; PL=9` | `A` = `9` | `108` → `301` |
| `108` | `M=SU_GIU_M; PL=1` | `A` = `1` | `108` → `301` |
| `108` | `M=SU_GIU_M; PL=2` | `A` = `2` | `108` → `301` |
| `108` | `M=SU_GIU_M; PL=3` | `A` = `3` | `108` → `301` |
| `108` | `M=SU_GIU_M; PL=4` | `A` = `4` | `108` → `301` |
| `108` | `M=SU_GIU_M; PL=5` | `A` = `5` | `108` → `301` |
| `108` | `M=SU_GIU_M; PL=6` | `A` = `6` | `108` → `301` |
| `108` | `M=SU_GIU_M; PL=7` | `A` = `7` | `108` → `301` |
| `108` | `M=SU_GIU_M; PL=8` | `A` = `8` | `108` → `301` |
| `108` | `M=SU_GIU_M; PL=9` | `A` = `9` | `108` → `301` |
| `109` | `M=0` | `ADDR_TYPE` = `3` | `109` |
| `109` | `M=1` | `ADDR_TYPE` = `3` | `109` |
| `109` | `M=2` | `ADDR_TYPE` = `3` | `109` |
| `109` | `M=3` | `ADDR_TYPE` = `3` | `109` |
| `109` | `M=4` | `ADDR_TYPE` = `3` | `109` |
| `109` | `M=5` | `ADDR_TYPE` = `3` | `109` |
| `109` | `M=6` | `ADDR_TYPE` = `3` | `109` |
| `109` | `M=7` | `ADDR_TYPE` = `3` | `109` |
| `109` | `M=8` | `ADDR_TYPE` = `3` | `109` |
| `109` | `M=O/I` | `ADDR_TYPE` = `3` | `109` |
| `109` | `M=OFF` | `ADDR_TYPE` = `3` | `109` |
| `109` | `M=ON` | `ADDR_TYPE` = `3` | `109` |
| `109` | `M=PUL` | `ADDR_TYPE` = `3` | `109` |
| `109` | `M=SU_GIU` | `ADDR_TYPE` = `3` | `109` |
| `109` | `M=SU_GIU_M` | `ADDR_TYPE` = `3` | `109` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve item `1525` / `modobj = 1` identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware tuple while preserving wildcard sentinels | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate item-specific Module/Object topology `400`, `401`, `402`, `403`, `404`, `408`, `409` | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after active Object/system context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration against firmware/Object filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Automation control functions selected through catalogue Object alternatives and physical/virtual conditions.

## Observed behavior and corroboration

No sanitized hardware fingerprint or Device-specific protocol capture is currently retained for this exact technical item.

## Programming

Programming must select installed firmware applicability, resolve slot/Object alternatives through catalogue conditions, apply relation filters, and preserve configuration-mode boundaries.

## Source reconciliation

The canonical catalogue establishes the commercial records, firmware applicability, topology, configuration fields, filters and conditions. Publisher sources above are used only for behaviors they directly document; missing dedicated sheets remain explicit gaps.

## Evidence limits and open work

- Recover any missing dedicated publisher sheets for the exact identities.
- Capture a sanitized hardware fingerprint covering identity, firmware, modules, addressing and configuration.
- Corroborate condition/filter behavior through MyHOME Suite and controlled configuration changes.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Archived original](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)
