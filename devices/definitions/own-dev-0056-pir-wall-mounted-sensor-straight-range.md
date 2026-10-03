# PIR wall-mounted sensor - straight range

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0056` | Project identity |
| Technical description | PIR wall-mounted sensor - straight range | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSE2001`, `048824` | Canonical commercial records |
| Catalogue item | `51` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `36` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `17` | Canonical firmware catalogue |
| Categories | Presence sensing, Daylight sensing, Automation | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSE2001` | Established identity | canonical commercial record for item `51` |
| Legrand | `048824` | Established identity | canonical commercial record for item `51` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MM00296_c_EN` | technical sheet | 2013-02-04 | `BMSE2001` wide-band PIR wall/ceiling sensor characteristics and MY HOME configuration | [Archived original](https://archive.openwebnet-ha.org/sha256/2b/06/2b0656aa8623d733caa7c863b25a05bde17d3fc5d29b11cec1048907b0a33eda.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MM00296_c_EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `27 Vdc` | `MM00296_c_EN` |
| Consumption | `12 mA` | `MM00296_c_EN` |
| Detection | PIR + daylight sensing | `MM00296_c_EN` |
| Protection | `IP42` | `MM00296_c_EN` |
| Light sensitivity | `5..1275 lux` | `MM00296_c_EN` |
| Operating temperature | `-5..45 °C` | `MM00296_c_EN` |
| Maximum installation height | `6 m` | `MM00296_c_EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `51` | Canonical catalogue |
| Technical item | PIR wall-mounted sensor - straight range | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `36` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `131` | `-1` | `-1` | `-1` | `17` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `131` | `1` | `119` Stand alone presence sensor | Candidate alternative | `282` | `119` | `281` |
| `131` | `1` | `128` Scenarios daylight and presence sensor | Fixed/designated metadata | `283` | `128` | `282` |
| `131` | `1` | `164` Scenarios daylight sensor | Candidate alternative | `284` | `164` | `283` |
| `131` | `1` | `165` Scenarios presence sensor | Candidate alternative | `285` | `165` | `284` |
| `131` | `1` | `166` Stand alone daylight sensor | Candidate alternative | `286` | `166` | `285` |
| `131` | `1` | `168` Stand alone daylight and presence sensor | Candidate alternative | `287` | `168` | `286` |
| `131` | `2` | `431` IR scenario control | Fixed/designated metadata | `288` | `431` | `287` |
| `131` | `3` | `431` IR scenario control | Fixed/designated metadata | `289` | `431` | `287` |
| `131` | `4` | `431` IR scenario control | Fixed/designated metadata | `290` | `431` | `287` |
| `131` | `5` | `431` IR scenario control | Fixed/designated metadata | `291` | `431` | `287` |
| `131` | `6` | `431` IR scenario control | Fixed/designated metadata | `292` | `431` | `287` |
| `131` | `7` | `431` IR scenario control | Fixed/designated metadata | `293` | `431` | `287` |
| `131` | `8` | `431` IR scenario control | Fixed/designated metadata | `294` | `431` | `287` |
| `131` | `9` | `431` IR scenario control | Fixed/designated metadata | `295` | `431` | `287` |
| `131` | `10` | `431` IR scenario control | Fixed/designated metadata | `296` | `431` | `287` |
| `131` | `11` | `431` IR scenario control | Fixed/designated metadata | `297` | `431` | `287` |
| `131` | `12` | `431` IR scenario control | Fixed/designated metadata | `298` | `431` | `287` |
| `131` | `13` | `431` IR scenario control | Fixed/designated metadata | `299` | `431` | `287` |
| `131` | `14` | `431` IR scenario control | Fixed/designated metadata | `300` | `431` | `287` |
| `131` | `15` | `431` IR scenario control | Fixed/designated metadata | `301` | `431` | `287` |
| `131` | `16` | `431` IR scenario control | Fixed/designated metadata | `302` | `431` | `287` |
| `131` | `17` | `431` IR scenario control | Fixed/designated metadata | `303` | `431` | `287` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `131` | `515` Daylight and motion sensor virgin | `1` | `119`, `128`, `164`, `165`, `166`, `168` | `515` | `4` |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `131` | Advanced Configuration | supported configuration route for this Device family |
| `131` | Physical configuration | supported configuration route for this Device family |
| `131` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `131` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `131` | `A` | `0..9` | `0` | A; Environment |
| `131` | `PL` | `0..9` | `0` | PL; Light Point |
| `131` | `M` | `0..4` | `0` | M; Mode 0-4 |
| `131` | `S` | `0..4` | `0` | S; Configurator S (0-4) |
| `131` | `T` | `0..9` | `0` | T; Configurator T (time) - (0-9) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `119` - Stand alone presence sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | `0` = Point to point; `2` = Group | `0` | Addressing type |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `0..255` | `0` | Group number |
| `A_R` | `0..10` | `0` | Referent area address |
| `PL_R` | `0..15` | `0` | Referent light point address |
| `MAIN_GROUP` | `0` = Disable; `1` = Enable | `0` | Enable secondary groups |
| `G1` | `0..255` | `0` | Secondary group 1 |
| `G2` | `0..255` | `0` | Secondary group 2 |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `10` | Minutes |
| `SECONDS` | `0..59` | `0` | Seconds |
| `FUNC_MODE` | `1` = Auto `ON`/`OFF`; `2` = Auto Walkthrough; `3` = Manual `ON` / Auto `OFF`; `5` = Partial `ON` / Group `OFF` | `2` | Operating mode; Functional_mode |
| `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `3` | PIR sensitivity |
| `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `2` | US sensitivity |
| `INITIAL_OCCUPANCY` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `3` | Initial occupancy |
| `MAINTAIN_OCCUPANCY` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Maintain detection |
| `RETRIGGER` | `0` = Disabled; `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Retrigger |
| `ALERT` | `0` = Disabled; `1` = Visual; `2` = Acoustic; `3` = Visual and Acoustic | `0` | Alert |
| `ENABLE_LOAD_CONTROL` | `0` = Disabled; `1` = Enabled | `1` | Enable load control |


### Object `128` - Scenarios daylight and presence sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `HOURS` | `0..255` | `0` | Time delay - Hours |
| `MINUTES` | `0..59` | `15` | Time delay - Minutes |
| `SECONDS` | `0..59` | `0` | Time delay - Seconds |
| `SCHEMA` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Detection scheme |
| `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `3` | PIR sensitivity |
| `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `2` | US sensitivity |


### Object `164` - Scenarios daylight sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |


### Object `165` - Scenarios presence sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `HOURS` | `0..255` | `0` | Time delay - Hours |
| `MINUTES` | `0..59` | `15` | Time delay - Minutes |
| `SECONDS` | `0..59` | `0` | Time delay - Seconds |
| `SCHEMA` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Detection scheme |
| `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `3` | PIR sensitivity |
| `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `2` | US sensitivity |


### Object `166` - Stand alone daylight sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | `0` = Point to point; `2` = Group | `0` | Addressing type |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `0..255` | `0` | Group number |
| `A_R` | `0..10` | `0` | Area of reference actuator |
| `PL_R` | `0..15` | `0` | Light point of reference actuator |
| `TYPE_LOOP` | `0` = Closed loop; `1` = Open loop | `0` | Loop type |
| `GD` | `0..255` | `0` | Daylight cell group |
| `DAYLIGHT_SETPOINT` | `0`; `1` = 5; `2` = 10; `3` = 15; `4` = 20; `5` = 25; `6` = 30; `7` = 35; `8` = 40; `9` = 45; `10` = 50; `11` = 55; `12` = 60; `13` = 65; `14` = 70; `15` = 75; `16` = 80; `17` = 85; `18` = 90; `19` = 95; `20` = 100; `21` = 105; `22` = 110; `23` = 115; `24` = 120; `25` = 125; `26` = 130; `27` = 135; `28` = 140; `29` = 145; `30` = 150; `31` = 155; `32` = 160; `33` = 165; `34` = 170; `35` = 175; `36` = 180; `37` = 185; `38` = 190; `39` = 195; `40` = 200; `41` = 205; `42` = 210; `43` = 215; `44` = 220; `45` = 225; `46` = 230; `47` = 235; `48` = 240; `49` = 245; `50` = 250; `51` = 255; `52` = 260; `53` = 265; `54` = 270; `55` = 275; `56` = 280; `57` = 285; `58` = 290; `59` = 295; `60` = 300; `61` = 305; `62` = 310; `63` = 315; `64` = 320; `65` = 325; `66` = 330; `67` = 335; `68` = 340; `69` = 345; `70` = 350; `71` = 355; `72` = 360; `73` = 365; `74` = 370; `75` = 375; `76` = 380; `77` = 385; `78` = 390; `79` = 395; `80` = 400; `81` = 405; `82` = 410; `83` = 415; `84` = 420; `85` = 425; `86` = 430; `87` = 435; `88` = 440; `89` = 445; `90` = 450; `91` = 455; `92` = 460; `93` = 465; `94` = 470; `95` = 475; `96` = 480; `97` = 485; `98` = 490; `99` = 495; `100` = 500; `101` = 505; `102` = 510; `103` = 515; `104` = 520; `105` = 525; `106` = 530; `107` = 535; `108` = 540; `109` = 545; `110` = 550; `111` = 555; `112` = 560; `113` = 565; `114` = 570; `115` = 575; `116` = 580; `117` = 585; `118` = 590; `119` = 595; `120` = 600; `121` = 605; `122` = 610; `123` = 615; `124` = 620; `125` = 625; `126` = 630; `127` = 635; `128` = 640; `129` = 645; `130` = 650; `131` = 655; `132` = 660; `133` = 665; `134` = 670; `135` = 675; `136` = 680; `137` = 685; `138` = 690; `139` = 695; `140` = 700; `141` = 705; `142` = 710; `143` = 715; `144` = 720; `145` = 725; `146` = 730; `147` = 735; `148` = 740; `149` = 745; `150` = 750; `151` = 755; `152` = 760; `153` = 765; `154` = 770; `155` = 775; `156` = 780; `157` = 785; `158` = 790; `159` = 795; `160` = 800; `161` = 805; `162` = 810; `163` = 815; `164` = 820; `165` = 825; `166` = 830; `167` = 835; `168` = 840; `169` = 845; `170` = 850; `171` = 855; `172` = 860; `173` = 865; `174` = 870; `175` = 875; `176` = 880; `177` = 885; `178` = 890; `179` = 895; `180` = 900; `181` = 905; `182` = 910; `183` = 915; `184` = 920; `185` = 925; `186` = 930; `187` = 935; `188` = 940; `189` = 945; `190` = 950; `191` = 955; `192` = 960; `193` = 965; `194` = 970; `195` = 975; `196` = 980; `197` = 985; `198` = 990; `199` = 995; `200` = 1000; `201` = 1005; `202` = 1010; `203` = 1015; `204` = 1020; `205` = 1025; `206` = 1030; `207` = 1035; `208` = 1040; `209` = 1045; `210` = 1050; `211` = 1055; `212` = 1060; `213` = 1065; `214` = 1070; `215` = 1075; `216` = 1080; `217` = 1085; `218` = 1090; `219` = 1095; `220` = 1100; `221` = 1105; `222` = 1110; `223` = 1115; `224` = 1120; `225` = 1125; `226` = 1130; `227` = 1135; `228` = 1140; `229` = 1145; `230` = 1150; `231` = 1155; `232` = 1160; `233` = 1165; `234` = 1170; `235` = 1175; `236` = 1180; `237` = 1185; `238` = 1190; `239` = 1195; `240` = 1200; `241` = 1205; `242` = 1210; `243` = 1215; `244` = 1220; `245` = 1225; `246` = 1230; `247` = 1235; `248` = 1240; `249` = 1245; `250` = 1250; `251` = 1255; `252` = 1260; `253` = 1265; `254` = 1270; `255` = 1275 | `100` | Daylight setpoint (Lux) |
| `PROVISION_OF_LIGHT` | `0` = Automatic; `1` = 5; `2` = 10; `3` = 15; `4` = 20; `5` = 25; `6` = 30; `7` = 35; `8` = 40; `9` = 45; `10` = 50; `11` = 55; `12` = 60; `13` = 65; `14` = 70; `15` = 75; `16` = 80; `17` = 85; `18` = 90; `19` = 95; `20` = 100; `21` = 105; `22` = 110; `23` = 115; `24` = 120; `25` = 125; `26` = 130; `27` = 135; `28` = 140; `29` = 145; `30` = 150; `31` = 155; `32` = 160; `33` = 165; `34` = 170; `35` = 175; `36` = 180; `37` = 185; `38` = 190; `39` = 195; `40` = 200; `41` = 205; `42` = 210; `43` = 215; `44` = 220; `45` = 225; `46` = 230; `47` = 235; `48` = 240; `49` = 245; `50` = 250; `51` = 255; `52` = 260; `53` = 265; `54` = 270; `55` = 275; `56` = 280; `57` = 285; `58` = 290; `59` = 295; `60` = 300; `61` = 305; `62` = 310; `63` = 315; `64` = 320; `65` = 325; `66` = 330; `67` = 335; `68` = 340; `69` = 345; `70` = 350; `71` = 355; `72` = 360; `73` = 365; `74` = 370; `75` = 375; `76` = 380; `77` = 385; `78` = 390; `79` = 395; `80` = 400; `81` = 405; `82` = 410; `83` = 415; `84` = 420; `85` = 425; `86` = 430; `87` = 435; `88` = 440; `89` = 445; `90` = 450; `91` = 455; `92` = 460; `93` = 465; `94` = 470; `95` = 475; `96` = 480; `97` = 485; `98` = 490; `99` = 495; `100` = 500; `101` = 505; `102` = 510; `103` = 515; `104` = 520; `105` = 525; `106` = 530; `107` = 535; `108` = 540; `109` = 545; `110` = 550; `111` = 555; `112` = 560; `113` = 565; `114` = 570; `115` = 575; `116` = 580; `117` = 585; `118` = 590; `119` = 595; `120` = 600; `121` = 605; `122` = 610; `123` = 615; `124` = 620; `125` = 625; `126` = 630; `127` = 635; `128` = 640; `129` = 645; `130` = 650; `131` = 655; `132` = 660; `133` = 665; `134` = 670; `135` = 675; `136` = 680; `137` = 685; `138` = 690; `139` = 695; `140` = 700; `141` = 705; `142` = 710; `143` = 715; `144` = 720; `145` = 725; `146` = 730; `147` = 735; `148` = 740; `149` = 745; `150` = 750; `151` = 755; `152` = 760; `153` = 765; `154` = 770; `155` = 775; `156` = 780; `157` = 785; `158` = 790; `159` = 795; `160` = 800; `161` = 805; `162` = 810; `163` = 815; `164` = 820; `165` = 825; `166` = 830; `167` = 835; `168` = 840; `169` = 845; `170` = 850; `171` = 855; `172` = 860; `173` = 865; `174` = 870; `175` = 875; `176` = 880; `177` = 885; `178` = 890; `179` = 895; `180` = 900; `181` = 905; `182` = 910; `183` = 915; `184` = 920; `185` = 925; `186` = 930; `187` = 935; `188` = 940; `189` = 945; `190` = 950; `191` = 955; `192` = 960; `193` = 965; `194` = 970; `195` = 975; `196` = 980; `197` = 985; `198` = 990; `199` = 995; `200` = 1000; `201` = 1005; `202` = 1010; `203` = 1015; `204` = 1020; `205` = 1025; `206` = 1030; `207` = 1035; `208` = 1040; `209` = 1045; `210` = 1050; `211` = 1055; `212` = 1060; `213` = 1065; `214` = 1070; `215` = 1075; `216` = 1080; `217` = 1085; `218` = 1090; `219` = 1095; `220` = 1100; `221` = 1105; `222` = 1110; `223` = 1115; `224` = 1120; `225` = 1125; `226` = 1130; `227` = 1135; `228` = 1140; `229` = 1145; `230` = 1150; `231` = 1155; `232` = 1160; `233` = 1165; `234` = 1170; `235` = 1175; `236` = 1180; `237` = 1185; `238` = 1190; `239` = 1195; `240` = 1200; `241` = 1205; `242` = 1210; `243` = 1215; `244` = 1220; `245` = 1225; `246` = 1230; `247` = 1235; `248` = 1240; `249` = 1245; `250` = 1250; `251` = 1255; `252` = 1260; `253` = 1265; `254` = 1270; `255` = 1275 | `0` | Provision of light (Lux) |
| `FUNC_MODE` | `1` = Auto `ON`/`OFF`; `3` = Manual `ON` / Auto `OFF`; `5` = Partial `ON` / Group `OFF` | `1` | Operating mode; Functional_mode (auto/manual/partial) |
| `LIGHTING_REGULATION` | `0` = Disabled; `1` = Enabled | `0` | Lighting regulation |
| `DAYLIGHT_FACTOR` | `0..255` | `0` | Daylight factor |
| `NATURAL_LIGHT_FACTOR` | `0..255` | `0` | Natural light factor |
| `DAYLIGHT_LEVEL` | `0..255` | `0` | Daylight level |


### Object `168` - Stand alone daylight and presence sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | `0` = Point-to-point; `2` = Group | `0` | Addressing type |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `1` | Light point |
| `G` | `0..255` | `0` | Group number |
| `A_R` | `0..10` | `0` | Referent area address |
| `PL_R` | `0..15` | `0` | Referent light point address |
| `MAIN_GROUP` | `0` = Disable; `1` = Enable | `0` | Enable secondary groups |
| `G1` | `0..255` | `0` | Sensor group 1 |
| `G2` | `0..255` | `0` | Sensor group 2 |
| `TYPE_LOOP` | `0` = Closed loop; `1` = Open loop | `0` | Loop type |
| `GD` | `0..255` | `0` | Daylight cell group |
| `DAYLIGHT_SETPOINT` | `0`; `1` = 5; `2` = 10; `3` = 15; `4` = 20; `5` = 25; `6` = 30; `7` = 35; `8` = 40; `9` = 45; `10` = 50; `11` = 55; `12` = 60; `13` = 65; `14` = 70; `15` = 75; `16` = 80; `17` = 85; `18` = 90; `19` = 95; `20` = 100; `21` = 105; `22` = 110; `23` = 115; `24` = 120; `25` = 125; `26` = 130; `27` = 135; `28` = 140; `29` = 145; `30` = 150; `31` = 155; `32` = 160; `33` = 165; `34` = 170; `35` = 175; `36` = 180; `37` = 185; `38` = 190; `39` = 195; `40` = 200; `41` = 205; `42` = 210; `43` = 215; `44` = 220; `45` = 225; `46` = 230; `47` = 235; `48` = 240; `49` = 245; `50` = 250; `51` = 255; `52` = 260; `53` = 265; `54` = 270; `55` = 275; `56` = 280; `57` = 285; `58` = 290; `59` = 295; `60` = 300; `61` = 305; `62` = 310; `63` = 315; `64` = 320; `65` = 325; `66` = 330; `67` = 335; `68` = 340; `69` = 345; `70` = 350; `71` = 355; `72` = 360; `73` = 365; `74` = 370; `75` = 375; `76` = 380; `77` = 385; `78` = 390; `79` = 395; `80` = 400; `81` = 405; `82` = 410; `83` = 415; `84` = 420; `85` = 425; `86` = 430; `87` = 435; `88` = 440; `89` = 445; `90` = 450; `91` = 455; `92` = 460; `93` = 465; `94` = 470; `95` = 475; `96` = 480; `97` = 485; `98` = 490; `99` = 495; `100` = 500; `101` = 505; `102` = 510; `103` = 515; `104` = 520; `105` = 525; `106` = 530; `107` = 535; `108` = 540; `109` = 545; `110` = 550; `111` = 555; `112` = 560; `113` = 565; `114` = 570; `115` = 575; `116` = 580; `117` = 585; `118` = 590; `119` = 595; `120` = 600; `121` = 605; `122` = 610; `123` = 615; `124` = 620; `125` = 625; `126` = 630; `127` = 635; `128` = 640; `129` = 645; `130` = 650; `131` = 655; `132` = 660; `133` = 665; `134` = 670; `135` = 675; `136` = 680; `137` = 685; `138` = 690; `139` = 695; `140` = 700; `141` = 705; `142` = 710; `143` = 715; `144` = 720; `145` = 725; `146` = 730; `147` = 735; `148` = 740; `149` = 745; `150` = 750; `151` = 755; `152` = 760; `153` = 765; `154` = 770; `155` = 775; `156` = 780; `157` = 785; `158` = 790; `159` = 795; `160` = 800; `161` = 805; `162` = 810; `163` = 815; `164` = 820; `165` = 825; `166` = 830; `167` = 835; `168` = 840; `169` = 845; `170` = 850; `171` = 855; `172` = 860; `173` = 865; `174` = 870; `175` = 875; `176` = 880; `177` = 885; `178` = 890; `179` = 895; `180` = 900; `181` = 905; `182` = 910; `183` = 915; `184` = 920; `185` = 925; `186` = 930; `187` = 935; `188` = 940; `189` = 945; `190` = 950; `191` = 955; `192` = 960; `193` = 965; `194` = 970; `195` = 975; `196` = 980; `197` = 985; `198` = 990; `199` = 995; `200` = 1000; `201` = 1005; `202` = 1010; `203` = 1015; `204` = 1020; `205` = 1025; `206` = 1030; `207` = 1035; `208` = 1040; `209` = 1045; `210` = 1050; `211` = 1055; `212` = 1060; `213` = 1065; `214` = 1070; `215` = 1075; `216` = 1080; `217` = 1085; `218` = 1090; `219` = 1095; `220` = 1100; `221` = 1105; `222` = 1110; `223` = 1115; `224` = 1120; `225` = 1125; `226` = 1130; `227` = 1135; `228` = 1140; `229` = 1145; `230` = 1150; `231` = 1155; `232` = 1160; `233` = 1165; `234` = 1170; `235` = 1175; `236` = 1180; `237` = 1185; `238` = 1190; `239` = 1195; `240` = 1200; `241` = 1205; `242` = 1210; `243` = 1215; `244` = 1220; `245` = 1225; `246` = 1230; `247` = 1235; `248` = 1240; `249` = 1245; `250` = 1250; `251` = 1255; `252` = 1260; `253` = 1265; `254` = 1270; `255` = 1275 | `100` | Daylight setpoint (Lux) |
| `PROVISION_OF_LIGHT` | `0` = Automatic; `1` = 5; `2` = 10; `3` = 15; `4` = 20; `5` = 25; `6` = 30; `7` = 35; `8` = 40; `9` = 45; `10` = 50; `11` = 55; `12` = 60; `13` = 65; `14` = 70; `15` = 75; `16` = 80; `17` = 85; `18` = 90; `19` = 95; `20` = 100; `21` = 105; `22` = 110; `23` = 115; `24` = 120; `25` = 125; `26` = 130; `27` = 135; `28` = 140; `29` = 145; `30` = 150; `31` = 155; `32` = 160; `33` = 165; `34` = 170; `35` = 175; `36` = 180; `37` = 185; `38` = 190; `39` = 195; `40` = 200; `41` = 205; `42` = 210; `43` = 215; `44` = 220; `45` = 225; `46` = 230; `47` = 235; `48` = 240; `49` = 245; `50` = 250; `51` = 255; `52` = 260; `53` = 265; `54` = 270; `55` = 275; `56` = 280; `57` = 285; `58` = 290; `59` = 295; `60` = 300; `61` = 305; `62` = 310; `63` = 315; `64` = 320; `65` = 325; `66` = 330; `67` = 335; `68` = 340; `69` = 345; `70` = 350; `71` = 355; `72` = 360; `73` = 365; `74` = 370; `75` = 375; `76` = 380; `77` = 385; `78` = 390; `79` = 395; `80` = 400; `81` = 405; `82` = 410; `83` = 415; `84` = 420; `85` = 425; `86` = 430; `87` = 435; `88` = 440; `89` = 445; `90` = 450; `91` = 455; `92` = 460; `93` = 465; `94` = 470; `95` = 475; `96` = 480; `97` = 485; `98` = 490; `99` = 495; `100` = 500; `101` = 505; `102` = 510; `103` = 515; `104` = 520; `105` = 525; `106` = 530; `107` = 535; `108` = 540; `109` = 545; `110` = 550; `111` = 555; `112` = 560; `113` = 565; `114` = 570; `115` = 575; `116` = 580; `117` = 585; `118` = 590; `119` = 595; `120` = 600; `121` = 605; `122` = 610; `123` = 615; `124` = 620; `125` = 625; `126` = 630; `127` = 635; `128` = 640; `129` = 645; `130` = 650; `131` = 655; `132` = 660; `133` = 665; `134` = 670; `135` = 675; `136` = 680; `137` = 685; `138` = 690; `139` = 695; `140` = 700; `141` = 705; `142` = 710; `143` = 715; `144` = 720; `145` = 725; `146` = 730; `147` = 735; `148` = 740; `149` = 745; `150` = 750; `151` = 755; `152` = 760; `153` = 765; `154` = 770; `155` = 775; `156` = 780; `157` = 785; `158` = 790; `159` = 795; `160` = 800; `161` = 805; `162` = 810; `163` = 815; `164` = 820; `165` = 825; `166` = 830; `167` = 835; `168` = 840; `169` = 845; `170` = 850; `171` = 855; `172` = 860; `173` = 865; `174` = 870; `175` = 875; `176` = 880; `177` = 885; `178` = 890; `179` = 895; `180` = 900; `181` = 905; `182` = 910; `183` = 915; `184` = 920; `185` = 925; `186` = 930; `187` = 935; `188` = 940; `189` = 945; `190` = 950; `191` = 955; `192` = 960; `193` = 965; `194` = 970; `195` = 975; `196` = 980; `197` = 985; `198` = 990; `199` = 995; `200` = 1000; `201` = 1005; `202` = 1010; `203` = 1015; `204` = 1020; `205` = 1025; `206` = 1030; `207` = 1035; `208` = 1040; `209` = 1045; `210` = 1050; `211` = 1055; `212` = 1060; `213` = 1065; `214` = 1070; `215` = 1075; `216` = 1080; `217` = 1085; `218` = 1090; `219` = 1095; `220` = 1100; `221` = 1105; `222` = 1110; `223` = 1115; `224` = 1120; `225` = 1125; `226` = 1130; `227` = 1135; `228` = 1140; `229` = 1145; `230` = 1150; `231` = 1155; `232` = 1160; `233` = 1165; `234` = 1170; `235` = 1175; `236` = 1180; `237` = 1185; `238` = 1190; `239` = 1195; `240` = 1200; `241` = 1205; `242` = 1210; `243` = 1215; `244` = 1220; `245` = 1225; `246` = 1230; `247` = 1235; `248` = 1240; `249` = 1245; `250` = 1250; `251` = 1255; `252` = 1260; `253` = 1265; `254` = 1270; `255` = 1275 | `0` | Provision of light (Lux) |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `10` | Minutes |
| `SECONDS` | `0..59` | `0` | Seconds |
| `FUNC_MODE` | `1` = Auto `ON`/`OFF`; `2` = Auto walkthrough; `3` = Manual `ON` / Auto `OFF`; `5` = Partial `ON` / Group `OFF` | `2` | Operating mode; Functional_mode |
| `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `3` | PIR sensitivity |
| `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `1` | US sensitivity |
| `INITIAL_OCC` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `3` | Initial detection |
| `MAINTAIN_OCC` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Maintain detection |
| `RE-TRIGGER` | `0` = Disabled; `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Re-trigger |
| `ALERT` | `0` = Disabled; `1` = Visual; `2` = Acoustic; `3` = Visual and Acoustic | `0` | Alert |
| `LOAD_CONTROL` | `0` = Disabled; `1` = Enabled | `1` | Enable load control |
| `LIGHTING_REGULATION` | `0` = Disabled; `1` = Enabled | `0` | Lighting regulation |
| `NATURAL_LIGHT_FACTOR` | `1..255` | `10` | Natural light factor |
| `DAYLIGHT_FACTOR` | `0..255` | `0` | Daylight factor |
| `DAYLIGHT_LEVEL` | `0..255` | `0` | Daylight level |


### Object `431` - IR scenario control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_SCE_1` | `1..255` | `1` | Scenario number |
| `TYPE_OF_REGULATION` | `0` = Regulate all; `1` = Lights only; `2` = Shutters only; `3` = Stereo amplifiers only | `1` | Regulation type |
| `ID1` | `0..255` | `0` | ID1 |
| `ID2` | `0..255` | `0` | ID2 |
| `ID3` | `0..15` | `0` | ID3 |
| `UNIT_NUMBER` | `0..15` | `0` | Push button number |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `131` | `1` | `128` | `4477` | `M=2` | None |
| `131` | `1` | `166` | `4461` | `M=1` | None |
| `131` | `1` | `166` | `4505` | `M=4` | None |
| `131` | `1` | `168` | `4439` | `M=0` | None |
| `131` | `1` | `168` | `4491` | `M=3` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `131` | `119` | `108` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | US sensitivity |
| `131` | `119` | `109` | `INITIAL_OCCUPANCY` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `3` | Initial occupancy |
| `131` | `119` | `110` | `MAINTAIN_OCCUPANCY` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Mantain occupancy |
| `131` | `119` | `111` | `RETRIGGER` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Re-trigger |
| `131` | `119` | `2334` | `ALERT` | `1` = Visual; `3` = Visual and Acoustic | `0` | Alert; reusable default `0` is outside this subset; filter supplies no replacement default |
| `131` | `128` | `112` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | US sensitivity |
| `131` | `128` | `113` | `SCHEMA` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Detection Schema |
| `131` | `165` | `114` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | US sensitivity |
| `131` | `165` | `115` | `SCHEMA` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Detection Schema |
| `131` | `166` | `2101` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `131` | `166` | `2116` | `NATURAL_LIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Natural light factor |
| `131` | `166` | `2131` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `131` | `168` | `117` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `1` | US sensitivity |
| `131` | `168` | `118` | `INITIAL_OCC` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `3` | Initial occupancy |
| `131` | `168` | `119` | `MAINTAIN_OCC` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Mantain occupancy |
| `131` | `168` | `120` | `RE-TRIGGER` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Re-trigger |
| `131` | `168` | `2147` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `131` | `168` | `2335` | `NATURAL_LIGHT_FACTOR` | `1..255` (entire reusable range retained) | `10` | Natural light factor |
| `131` | `168` | `2336` | `ALERT` | `1` = Visual; `3` = Visual and Acoustic | `0` | Alert; reusable default `0` is outside this subset; filter supplies no replacement default |
| `131` | `168` | `2362` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `131` | `168` | `2445` | `DAYLIGHT_SETPOINT` | Subset flag present but no allowed values stored; unresolved restriction | `100` | Daylight setpoint (Lux) |
| `131` | `168` | `2457` | `PROVISION_OF_LIGHT` | Subset flag present but no allowed values stored; unresolved restriction | `0` | Provision of light (Lux) |
| `131` | `431` | `2395` | `TYPE_OF_REGULATION` | `3` = Stereo amplifiers only | `1` | Regulation type; reusable default `1` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `51` / `modobj = 36` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`119`, `128`, `164`, `165`, `166`, `168`, `431`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Wide-band wall/ceiling PIR and daylight sensor for SCS automation. It supports physical and virtual MY HOME configuration and exposes the shared presence/daylight/scenario Object topology with Device relation filters.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical catalogue binds `BMSE2001` and `048824` to one technical item. The dedicated BTicino sheet directly documents `BMSE2001`; the Legrand `048824` identity remains catalogue-derived for this technical cluster.

## Evidence limits and open work

- Archive the identified publisher documents locally where licensing and repository policy allow.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate relation filters and condition-selected topology against MyHOME Suite and controlled hardware observations.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
