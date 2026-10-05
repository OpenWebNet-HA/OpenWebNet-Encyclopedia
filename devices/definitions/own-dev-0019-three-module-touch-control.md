# Three-module touch control

## Summary

This three-module SCS wall control has six capacitive buttons for configured lighting, automation, scenarios, sound or door-entry functions. Adjustable LED feedback and a temporary cleaning inhibit make its touch interface easier to use and maintain.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0019` | Project identity |
| Technical description | Six-button capacitive multifunction command with configurable button roles | Catalogue + official technical sheet |
| Catalogue item | `1190` - Touch control | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `27` | Implementation evidence |
| Firmware definition | wildcard `-1.-1` | Implementation evidence |
| Declared Modules | `7` | Implementation evidence |
| Configuration modes | Advanced, Physical, Virtual | Implementation evidence |
| Direct / candidate Objects | `12` / `15` | Implementation evidence |
| Virgin Object | Soft-Touch command virgin (`521`) | Implementation evidence |
| Categories | Commands, Multifunction, User Interface, Scenarios | Product and capability model |

This definition covers the three-module touch-control cluster, not the four-module sibling. The product has six capacitive command zones plus a separate user-interface-settings slot. Each command zone can take one of a broad set of command roles; the catalogue models that flexibility through direct reusable Objects plus a Soft-Touch Virgin Object candidate set.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC/HS4657M3` | Documented commercial identity | Catalogue + `MQ00110` technical sheet |
| BTicino - Axolute | `HD4657M3` | Documented commercial identity | Catalogue + `MQ00110` technical sheet |
| Legrand - Arteor | `573912` | Documented commercial identity | Catalogue + `MQ00110` technical sheet |
| Legrand - Arteor | `573913` | Documented commercial identity | Catalogue + `MQ00110` technical sheet |
| Legrand - Arteor | `574091` | Shared technical item | Implementation evidence; direct sheet correlation pending |
| Legrand - Arteor | `574591` | Shared technical item | Implementation evidence; direct sheet correlation pending |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `HC4657M3` | `8012199942254` | [Archived original](https://archive.openwebnet-ha.org/sha256/6d/59/6d59225e5abac225ba376dca4a52d38edf27d541035224f7a85f9dca41c37014.pdf), `HC4657M3-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `HS4657M3` | `8012199942339` | [Archived original](https://archive.openwebnet-ha.org/sha256/c9/74/c97496ef3b0afd3e926574645da61c45875eacfb89113d535feee09662e2b591.pdf), `HS4657M3-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `HD4657M3` | `8005543412862` | [Archived original](https://archive.openwebnet-ha.org/sha256/53/b0/53b0341867a2a829f1586cd0bf5330bb65aa540dec301ac312c9f8373db82929.pdf), `HD4657M3-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00110_f_EN` | Technical sheet | revision/date not yet pinned | 4657M3/M4 and Arteor touch-control family | [Archived original](https://archive.openwebnet-ha.org/sha256/fb/98/fb9888607c897255780d423bd2a27a1104be3a7b7c908c811c93d2f34d99b1ea.pdf) | publisher source not currently retained |
| MyHOME catalogue `HPML0714` | Product catalogue | revision/date not yet pinned | `573912` / `573913` occur on printed pp. 16, 19 / PDF pp. 16, 19 | [Archived MyHOME catalogue](https://archive.openwebnet-ha.org/sha256/13/8e/138e7a234fe24fb044d3bfc82954e08b2887be22f3f8ceb24aecaeff6ed2f2e5.pdf) | publisher source not currently retained |
| `HC4657M3-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HC4657M3` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/6d/59/6d59225e5abac225ba376dca4a52d38edf27d541035224f7a85f9dca41c37014.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4657M3) |
| `HS4657M3-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HS4657M3` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/c9/74/c97496ef3b0afd3e926574645da61c45875eacfb89113d535feee09662e2b591.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4657M3) |
| `HD4657M3-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HD4657M3` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/53/b0/53b0341867a2a829f1586cd0bf5330bb65aa540dec301ac312c9f8373db82929.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HD4657M3) |

The technical sheet distinguishes the three-module version by its six capacitive buttons. It documents physical and MyHOME_Suite configuration and a multifunction command set spanning lighting, automation, locking, scenarios, video-door-entry and sound functions.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 3-module family | `MQ00110_f_EN` |
| User controls | 6 capacitive buttons | `MQ00110_f_EN` |
| Indication | blue indication | `MQ00110_f_EN` |
| SCS current by commercial variant | BTicino variants are specified below the Arteor `573912`/`573913` variants; retain revision/variant scope | `MQ00110_f_EN` |

The current source set establishes a commercial-variant electrical difference without a single shared current figure. Preserve that distinction rather than inventing a universal value.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1190` | Implementation evidence |
| Main system | lighting_automation / Automation | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `27` | Implementation evidence |
| Family | `1` | Implementation evidence |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `154` | `-1` | `-1` | `-1` | `7` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Wildcard values are catalogue applicability sentinels, not claims about an installed firmware version.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `154` | `1` | `410` Light control | Fixed/designated metadata | `764` | `410` | `526` |
| `154` | `1` | `411` Automation control | Candidate alternative | `770` | `411` | `527` |
| `154` | `1` | `412` Lock/unlock actuator control | Candidate alternative | `776` | `412` | `528` |
| `154` | `1` | `413` Scenario module control | Candidate alternative | `782` | `413` | `529` |
| `154` | `1` | `414` Scheduled scenario | Candidate alternative | `788` | `414` | `530` |
| `154` | `1` | `415` Scenario PLUS Lighting Management | Candidate alternative | `794` | `415` | `531` |
| `154` | `1` | `416` Scheduled scenario PLUS | Candidate alternative | `800` | `416` | `532` |
| `154` | `1` | `418` Open lock control | Candidate alternative | `806` | `418` | `533` |
| `154` | `1` | `419` Sound diffusion control | Candidate alternative | `812` | `419` | `534` |
| `154` | `1` | `426` Staircase light control | Candidate alternative | `818` | `426` | `535` |
| `154` | `1` | `427` Floor call control | Candidate alternative | `824` | `427` | `536` |
| `154` | `2` | `410` Light control | Fixed/designated metadata | `765` | `410` | `526` |
| `154` | `2` | `411` Automation control | Candidate alternative | `771` | `411` | `527` |
| `154` | `2` | `412` Lock/unlock actuator control | Candidate alternative | `777` | `412` | `528` |
| `154` | `2` | `413` Scenario module control | Candidate alternative | `783` | `413` | `529` |
| `154` | `2` | `414` Scheduled scenario | Candidate alternative | `789` | `414` | `530` |
| `154` | `2` | `415` Scenario PLUS Lighting Management | Candidate alternative | `795` | `415` | `531` |
| `154` | `2` | `416` Scheduled scenario PLUS | Candidate alternative | `801` | `416` | `532` |
| `154` | `2` | `418` Open lock control | Candidate alternative | `807` | `418` | `533` |
| `154` | `2` | `419` Sound diffusion control | Candidate alternative | `813` | `419` | `534` |
| `154` | `2` | `426` Staircase light control | Candidate alternative | `819` | `426` | `535` |
| `154` | `2` | `427` Floor call control | Candidate alternative | `825` | `427` | `536` |
| `154` | `3` | `410` Light control | Fixed/designated metadata | `766` | `410` | `526` |
| `154` | `3` | `411` Automation control | Candidate alternative | `772` | `411` | `527` |
| `154` | `3` | `412` Lock/unlock actuator control | Candidate alternative | `778` | `412` | `528` |
| `154` | `3` | `413` Scenario module control | Candidate alternative | `784` | `413` | `529` |
| `154` | `3` | `414` Scheduled scenario | Candidate alternative | `790` | `414` | `530` |
| `154` | `3` | `415` Scenario PLUS Lighting Management | Candidate alternative | `796` | `415` | `531` |
| `154` | `3` | `416` Scheduled scenario PLUS | Candidate alternative | `802` | `416` | `532` |
| `154` | `3` | `418` Open lock control | Candidate alternative | `808` | `418` | `533` |
| `154` | `3` | `419` Sound diffusion control | Candidate alternative | `814` | `419` | `534` |
| `154` | `3` | `426` Staircase light control | Candidate alternative | `820` | `426` | `535` |
| `154` | `3` | `427` Floor call control | Candidate alternative | `826` | `427` | `536` |
| `154` | `4` | `410` Light control | Fixed/designated metadata | `767` | `410` | `526` |
| `154` | `4` | `411` Automation control | Candidate alternative | `773` | `411` | `527` |
| `154` | `4` | `412` Lock/unlock actuator control | Candidate alternative | `779` | `412` | `528` |
| `154` | `4` | `413` Scenario module control | Candidate alternative | `785` | `413` | `529` |
| `154` | `4` | `414` Scheduled scenario | Candidate alternative | `791` | `414` | `530` |
| `154` | `4` | `415` Scenario PLUS Lighting Management | Candidate alternative | `797` | `415` | `531` |
| `154` | `4` | `416` Scheduled scenario PLUS | Candidate alternative | `803` | `416` | `532` |
| `154` | `4` | `418` Open lock control | Candidate alternative | `809` | `418` | `533` |
| `154` | `4` | `419` Sound diffusion control | Candidate alternative | `815` | `419` | `534` |
| `154` | `4` | `426` Staircase light control | Candidate alternative | `821` | `426` | `535` |
| `154` | `4` | `427` Floor call control | Candidate alternative | `827` | `427` | `536` |
| `154` | `5` | `410` Light control | Fixed/designated metadata | `768` | `410` | `526` |
| `154` | `5` | `411` Automation control | Candidate alternative | `774` | `411` | `527` |
| `154` | `5` | `412` Lock/unlock actuator control | Candidate alternative | `780` | `412` | `528` |
| `154` | `5` | `413` Scenario module control | Candidate alternative | `786` | `413` | `529` |
| `154` | `5` | `414` Scheduled scenario | Candidate alternative | `792` | `414` | `530` |
| `154` | `5` | `415` Scenario PLUS Lighting Management | Candidate alternative | `798` | `415` | `531` |
| `154` | `5` | `416` Scheduled scenario PLUS | Candidate alternative | `804` | `416` | `532` |
| `154` | `5` | `418` Open lock control | Candidate alternative | `810` | `418` | `533` |
| `154` | `5` | `419` Sound diffusion control | Candidate alternative | `816` | `419` | `534` |
| `154` | `5` | `426` Staircase light control | Candidate alternative | `822` | `426` | `535` |
| `154` | `5` | `427` Floor call control | Candidate alternative | `828` | `427` | `536` |
| `154` | `6` | `410` Light control | Fixed/designated metadata | `769` | `410` | `526` |
| `154` | `6` | `411` Automation control | Candidate alternative | `775` | `411` | `527` |
| `154` | `6` | `412` Lock/unlock actuator control | Candidate alternative | `781` | `412` | `528` |
| `154` | `6` | `413` Scenario module control | Candidate alternative | `787` | `413` | `529` |
| `154` | `6` | `414` Scheduled scenario | Candidate alternative | `793` | `414` | `530` |
| `154` | `6` | `415` Scenario PLUS Lighting Management | Candidate alternative | `799` | `415` | `531` |
| `154` | `6` | `416` Scheduled scenario PLUS | Candidate alternative | `805` | `416` | `532` |
| `154` | `6` | `418` Open lock control | Candidate alternative | `811` | `418` | `533` |
| `154` | `6` | `419` Sound diffusion control | Candidate alternative | `817` | `419` | `534` |
| `154` | `6` | `426` Staircase light control | Candidate alternative | `823` | `426` | `535` |
| `154` | `6` | `427` Floor call control | Candidate alternative | `829` | `427` | `536` |
| `154` | `7` | `130` User interface settings | Fixed/designated metadata | `763` | `480` | `525` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `154` | `521` Soft-Touch command virgin | `1`, `2`, `3`, `4`, `5`, `6` | `410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `418`, `419`, `421`, `426`, `427`, `462` | `521` | `28` |

Direct catalogue Objects include:
Virgin Object `521`, Soft-Touch command virgin, allows these command roles:
Combining the direct set with Virgin-only roles yields 15 distinct candidate Objects. The catalogue contains empty slot-condition records on some direct Light-control and Floor-call rows; because the condition text is empty, this definition treats them as source artifacts rather than as hidden semantic predicates.

## Configuration modes

| Mode / modality | Evidence |
| --- | --- |
| Physical configuration | `MQ00110_f_EN` + implementation evidence |
| Virtual Configuration | `MQ00110_f_EN` + implementation evidence |
| Advanced Configuration | implementation evidence |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `154` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `154` | `A` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB` | `0` | Area (0-9 `GEN`,`GR`,`AMB`); Environment (0-9 `GEN`,`GR`,`AMB`) |
| `154` | `PL` | `0..9` | `0` | PL; Light Point |
| `154` | `M` | `0..1`; `3..4`; `6`; `9` = `O/I`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `14` = `CEN` | `0` | M; Mode physical configurator (0-1,3-4,6,`O/I`,SU_GIU,SU_GIU_M,`CEN`) |
| `154` | `SET` | `0..7` | `0` | SET; User interface settings configurator (0-7) |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `A` | `0..9` plus `GEN` / `GR` / `AMB` forms | environment / area selector |
| `PL` | physical light-point domain | light point |
| `M` | `0`, `1`, `3`, `4`, `6`, `O/I`, `SU_GIU`, `SU_GIU_M`, `CEN` | physical mode selector |
| `SET` | `0..7` | user-interface settings configurator |


The physical sheet and catalogue agree that the Device can be configured physically or through software. Software configuration should preserve the richer reusable Object model rather than reducing every button to the physical `A` / `PL` / `M` shorthand.

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


### Additional Device-specific interpretation

The candidate roles expose different schemas:

| Role | Principal configuration fields |
| --- | --- |
| Light control | modality; addressing type; `A` / `PL` / `G`; installation/destination levels; reference actuator; contact type; optional timing, level and dimming parameters |
| Automation control | `UP/DOWN` modality; addressing; `A` / `PL` / `G`; installation/destination levels; reference actuator; contact type |
| Lock/unlock control | D/E modality; addressing; `A` / `PL` / `G`; installation/destination levels; contact type |
| Scenario module control | modality; scenario-module address; installation/destination levels; contact type; scenario number; activation delay |
| Scheduled scenario | `A` / `PL`; `CEN` button; Lighting Management mode; contact type |
| Scenario PLUS | `ON`/`OFF` regulation mode; scenario number; regulation type; contact type; delay |
| Scheduled scenario PLUS | low/high scenario number; button; Lighting Management mode; contact type |
| `AUX` control | cyclic/off/on/pulse/up/down family of modes; `AUX` channel; contact type |
| Open lock control | external-unit P; segment level |
| Sound diffusion control | VOL/ON_OFF; addressing type; `A` / `PF`; follow-me; source/sub-source; channel; contact type |
| Cyclic autoswitch | external-unit P; segment |
| Staircase light | internal-unit `N1` / `N2`; segment |
| Floor call | call type; `N1` / `N2`; segment; input `AUX` channel |
| Open lock on session | external-unit P |
| User interface settings | unused-button state; feedback update; LED level/fade; standby backlight; backlight delay; proximity enable; signboard behavior |

The Light-control address type explicitly supports address `01..175`, area `00..10` and group `01..255` in the reusable catalogue Object. Other role-specific ranges remain those of their canonical reusable Objects.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `154` | `1` | `410` | `4145` | No textual predicate stored | None |
| `154` | `1` | `427` | `4145` | No textual predicate stored | None |
| `154` | `2` | `410` | `4145` | No textual predicate stored | None |
| `154` | `2` | `427` | `4145` | No textual predicate stored | None |
| `154` | `3` | `410` | `4145` | No textual predicate stored | None |
| `154` | `3` | `427` | `4145` | No textual predicate stored | None |
| `154` | `4` | `410` | `4145` | No textual predicate stored | None |
| `154` | `4` | `427` | `4145` | No textual predicate stored | None |
| `154` | `5` | `410` | `4145` | No textual predicate stored | None |
| `154` | `5` | `427` | `4145` | No textual predicate stored | None |
| `154` | `6` | `410` | `4145` | No textual predicate stored | None |
| `154` | `6` | `427` | `4145` | No textual predicate stored | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `154` | `410` | `738` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Canonical catalogue relation |
| `154` | `411` | `749` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `154` | `412` | `756` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `154` | `413` | `762` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `154` | `414` | `773` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `154` | `414` | `774` | `MODE` | `0` = Press/release only; `1` = Press/hold/release (entire reusable range retained) | `0` | Mode for `CEN` command |
| `154` | `415` | `780` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `154` | `416` | `791` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `154` | `416` | `792` | `MODE` | `0` = Press/release only; `1` = Press/hold/release (entire reusable range retained) | `0` | Mode for `CEN` command |
| `154` | `419` | `808` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `154` | `419` | `809` | `CHANNEL` | `0` = Base Band; `1` = Left; `2` = Right; `3` = Stereo; `8` = Base Band and Video; `9` = Left and video; `10` = Right and video; `11` = Left and video (entire reusable range retained) | `3` | Channel (BB-Stereo) |
| `154` | `419` | `810` | `SUB_SOURCE` | `0..255` (entire reusable range retained) | `0` | SUB_SOURCE |
| `154` | `426` | `822` | `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone (entire reusable range retained) | `0` | Segment |
| `154` | `426` | `4106` | `N1` | `100`; `101`; `102`; `103`; `104`; `105`; `106`; `107`; `108`; `109`; `110`; `111`; `112`; `113`; `114`; `115`; `116`; `117`; `118`; `119`; `120`; `121`; `122`; `123`; `124`; `125`; `126`; `127`; `128`; `129`; `130`; `131`; `132`; `133`; `134`; `135`; `136`; `137`; `138`; `139`; `140`; `141`; `142`; `143`; `144`; `145`; `146`; `147`; `148`; `149`; `150`; `151`; `152`; `153`; `154`; `155`; `156`; `157`; `158`; `159`; `160`; `161`; `162`; `163`; `164`; `165`; `166`; `167`; `168`; `169`; `170`; `171`; `172`; `173`; `174`; `175`; `176`; `177`; `178`; `179`; `180`; `181`; `182`; `183`; `184`; `185`; `186`; `187`; `188`; `189`; `190`; `191`; `192`; `193`; `194`; `195`; `196`; `197`; `198`; `199`; `200`; `201`; `202`; `203`; `204`; `205`; `206`; `207`; `208`; `209`; `210`; `211`; `212`; `213`; `214`; `215`; `216`; `217`; `218`; `219`; `220`; `221`; `222`; `223`; `224`; `225`; `226`; `227`; `228`; `229`; `230`; `231`; `232`; `233`; `234`; `235`; `236`; `237`; `238`; `239`; `240`; `241`; `242`; `243`; `244`; `245`; `246`; `247`; `248`; `249`; `250`; `251`; `252`; `253`; `254`; `255` | `0` | Internal unit address; reusable default `0` is outside this subset; filter supplies no replacement default |
| `154` | `427` | `843` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `154` | `427` | `844` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `154` | `427` | `845` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `154` | `427` | `846` | `TO_ALL` | `1` = General | `1` | Type of call |
| `154` | `427` | `1903` | `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone (entire reusable range retained) | `0` | Segment |
| `154` | `130` | `3113` | `BACKLIGHT_INTENSITY_STANDBY_LEVEL` | `0` = `OFF`; `1` = Level1; `2` = Level2; `3` = Level3; `4` = Level4; `5` = Level5; `6` = Level6; `7` = Level7; `8` = Level8; `9` = Level9; `10` = Level10 (entire reusable range retained) | `1` | Backlight intensity stand by level |
| `154` | `130` | `3120` | `PROXIMITY_ENABLE` | `0` = Disable; `1` = Enable (entire reusable range retained) | `1` | Proximity Activation |
| `154` | `130` | `3127` | `SIGNBOARD` | `0` = Off; `1` = Fixe; `2` = Chase (entire reusable range retained) | `2` | Signboard activation type |
| `154` | `130` | `3135` | `SINGLE_LED_INTENSITY_STANDBY_LEVEL` | `0` = `OFF`; `1` = Level1; `2` = Level2; `3` = Level3; `4` = Level4; `5` = Level5; `6` = Level6; `7` = Level7; `8` = Level8; `9` = Level9; `10` = Level10 (entire reusable range retained) | `1` | when BACKLIGHT_INTENSITY_STANDBY_LEVEL is `OFF`, only one led can be used for the standby. |
| `154` | `130` | `3158` | `BACKLIGHT_DELAY` | `0..255` (entire reusable range retained) | `15` | Delay time (seconds) |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

### Product interpretation and source differences

| Surface | Source state | Interpretation |
| --- | --- | --- |
| Direct Light-control rows | empty condition records occur | treat as source artifacts, not hidden predicates |
| Direct Floor-call rows | empty condition records occur | treat as source artifacts, not hidden predicates |
| Virgin Object `521` | permits additional candidate roles | candidate capability does not establish runtime selection |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | identify `modobj` 27 and product family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe concrete installed firmware despite wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | enumerate six command Modules plus UI settings where exposed | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect each configured command address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | identify selected candidate Object and its configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Depending on selected Object, individual buttons can participate in lighting, automation, scenario, `AUX`, sound and video-door-entry functions. The official sheet corroborates this multifunction character. Generic `WHO` frame semantics remain canonical in Functional Protocol.

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

Programming must preserve six independently configurable command positions plus the fixed UI-settings slot. Physical `A`/`PL`/`M` configuration and software-selected reusable Object roles are separate layers; self-learning/scenario workflows remain product behavior.

## Source reconciliation

`MQ00110_f_EN` has been reconciled into the six-command-slot plus UI-settings model:

- self-learning and cyclic self-learning have explicit product programming/deletion procedures and are not merely generic Object alternatives;
- F420/scenario and `CEN`/MH200N-style functions have product-specific button/address mappings;
- the touch UI supports Device-level LED/status behavior selected by `SET=0..7`, including different feedback/fade/standby arrangements;
- the product provides a temporary cleaning/command-inhibit behavior for the touch surface;
- after installation/power-up the Device performs an automatic calibration interval of roughly two minutes, during which commands/feedback must not be interpreted as normal steady-state behavior;
- installation/destination-level semantics remain part of the selected function family when the Device works across interfaces.

The empty catalogue condition rows remain source artifacts requiring runtime clarification, but the principal published touch-control behavior is now explicit on the Device page.

## Evidence limits and open work

- Obtain a sanitized fingerprint showing all six button slots plus UI slot `7`.
- Correlate `DIMENSION 30` Virgin-Object identifiers with software-selected roles on real hardware.
- Locate direct official documentation for `574091` and `574591`.
- Determine whether the empty condition 4145 rows have any runtime significance.
- Correlate wildcard catalogue applicability with observed firmware versions.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)

- `HC4657M3-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HC4657M3` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/6d/59/6d59225e5abac225ba376dca4a52d38edf27d541035224f7a85f9dca41c37014.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4657M3); SHA-256 `6d59225e5abac225ba376dca4a52d38edf27d541035224f7a85f9dca41c37014`.
- `HS4657M3-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HS4657M3` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/c9/74/c97496ef3b0afd3e926574645da61c45875eacfb89113d535feee09662e2b591.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4657M3); SHA-256 `c97496ef3b0afd3e926574645da61c45875eacfb89113d535feee09662e2b591`.
- `HD4657M3-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HD4657M3` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/53/b0/53b0341867a2a829f1586cd0bf5330bb65aa540dec301ac312c9f8373db82929.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HD4657M3); SHA-256 `53b0341867a2a829f1586cd0bf5330bb65aa540dec301ac312c9f8373db82929`.
