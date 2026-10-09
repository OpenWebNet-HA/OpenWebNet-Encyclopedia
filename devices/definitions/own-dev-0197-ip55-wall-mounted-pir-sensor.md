# IP55 wall-mounted PIR sensor

## Summary

Legrand 048834 is a wall-mounted PIR movement and light sensor with IP55 protection for indoor or outdoor transit areas. It sends SCS control information rather than switching a mains load directly, and its detection threshold, delay and operating mode can be configured.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0197` | Project identity |
| Technical description | IP55 wall-mounted PIR sensor | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `048834` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `2147` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `81` | Main association; independent of project ID |
| Firmware definition | `683` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `17` | Firmware metadata |
| Categories | Sensors | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `048834` | Established catalogue identity | Manufacturer database commercial record `2490` explicitly links this SKU to item `2147` |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `048834` | IP55 PIR wall mounted sensor, long range | Canonical commercial record `2490` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ST-00001033-EN.pdf` | Classe300EOS external compatibility evidence | `ST-00001033-EN; 04/10/2022` | Printed/PDF p. 8 only: exact MyHOMEServer1, 048834 and K4652M2 entries in another product’s compatibility table; no electrical ratings transferred. | [Archived original](https://archive.openwebnet-ha.org/sha256/e8/54/e854cdd3edff2d77efb06d28600565bbe4c691ef760b6aca7ff16b2cfa8576eb.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00001033-EN.pdf) |
| `legrand-living-now-historical.pdf` | Historical Living Now/MyHOME catalogue | `Printed publication date not established` | Printed/PDF pp. 35, 92, 94-95, 98: exact MyHOMEServer1, F459, K4652M2 and 048834 catalogue descriptions; p. 98 PIR settings and internal threshold / timing discrepancy. | [Archived original](https://archive.openwebnet-ha.org/sha256/f7/2a/f72ab15db14eea29dd1693203fa242c32213717b596bcee9fd2ee96ce7d53e71.pdf) | [Publisher original](https://assets.legrand.com/webf/bg/bg_en_Living_NOW_catalogue.pdf) |
| `ST-00001031-EN.pdf` | Previously archived MyHOME Server technical sheet | `ST-00001031-EN; 30/05/2022` | Printed/PDF pp. 1-4: exact MyHOMEServer1 electrical / interface and system limits; p. 3 explicitly lists 048834 and K4652M2 compatibility. Original publisher URL absent from legacy archival record. | [Archived original](https://archive.openwebnet-ha.org/sha256/14/97/14971697bfbdbb33587b5724c7b38ac2aa6977e05e404556941291cafa589ad7.pdf) | [Previously archived original](https://archive.openwebnet-ha.org/sha256/14/97/14971697bfbdbb33587b5724c7b38ac2aa6977e05e404556941291cafa589ad7.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2147`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / connection | `27 Vdc from SCS BUS; SCS clamp` | `legrand-living-now-historical.pdf` printed/PDF p. 98 |
| Protection / mounting | `IP55; wall mounting; corner accessory 048971` | `legrand-living-now-historical.pdf` printed/PDF p. 98 |
| Detection at 2.5 m height | `15 × 6 m coverage; horizontal 140°, vertical 45°` | `legrand-living-now-historical.pdf` printed/PDF p. 98 |
| Modes | `AUTO / ECO / WALKTHROUGH` | `legrand-living-now-historical.pdf` printed/PDF p. 98 |
| Brightness range / factory setting | `Table: 5..1275 lux / 300 lux` | `legrand-living-now-historical.pdf` printed/PDF p. 98 |
| Published delay / factory setting | `Table prints “5 s 59 min 59 h” / 15 min; upper endpoint ambiguous` | `legrand-living-now-historical.pdf` printed/PDF p. 98 |
| Configuration tools | `BMSO4001 advanced or BMSO4003 basic IR configurator; physical or virtual configuration` | `legrand-living-now-historical.pdf` printed/PDF p. 98 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2147` | Canonical catalogue |
| Technical item description | IP55 PIR wall mounted sensor, long range | Canonical catalogue |
| Item family | Source placeholder description `0`; key `5` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `81` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `81` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `683` | `2` | `9` | No build row | `17` | Catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `683` | `1` | `119` Stand alone presence sensor | Candidate alternative | `2586` | `119` | `1205` |
| `683` | `1` | `128` Scenarios daylight and presence sensor | Candidate alternative | `2529` | `128` | `1178` |
| `683` | `1` | `164` Scenarios daylight sensor | Candidate alternative | `2528` | `164` | `1177` |
| `683` | `1` | `165` Scenarios presence sensor | Candidate alternative | `2530` | `165` | `1179` |
| `683` | `1` | `166` Stand alone daylight sensor | Candidate alternative | `2531` | `166` | `1180` |
| `683` | `1` | `168` Stand alone daylight and presence sensor | Fixed / designated metadata | `2587` | `168` | `1206` |
| `683` | `2` | `431` IR scenario control | Fixed / designated metadata | `2549` | `431` | `1183` |
| `683` | `3` | `431` IR scenario control | Fixed / designated metadata | `2550` | `431` | `1183` |
| `683` | `4` | `431` IR scenario control | Fixed / designated metadata | `2551` | `431` | `1183` |
| `683` | `5` | `431` IR scenario control | Fixed / designated metadata | `2552` | `431` | `1183` |
| `683` | `6` | `431` IR scenario control | Fixed / designated metadata | `2553` | `431` | `1183` |
| `683` | `7` | `431` IR scenario control | Fixed / designated metadata | `2554` | `431` | `1183` |
| `683` | `8` | `431` IR scenario control | Fixed / designated metadata | `2555` | `431` | `1183` |
| `683` | `9` | `431` IR scenario control | Fixed / designated metadata | `2556` | `431` | `1183` |
| `683` | `10` | `431` IR scenario control | Fixed / designated metadata | `2557` | `431` | `1183` |
| `683` | `11` | `431` IR scenario control | Fixed / designated metadata | `2558` | `431` | `1183` |
| `683` | `12` | `431` IR scenario control | Fixed / designated metadata | `2559` | `431` | `1183` |
| `683` | `13` | `431` IR scenario control | Fixed / designated metadata | `2560` | `431` | `1183` |
| `683` | `14` | `431` IR scenario control | Fixed / designated metadata | `2561` | `431` | `1183` |
| `683` | `15` | `431` IR scenario control | Fixed / designated metadata | `2562` | `431` | `1183` |
| `683` | `16` | `431` IR scenario control | Fixed / designated metadata | `2563` | `431` | `1183` |
| `683` | `17` | `431` IR scenario control | Fixed / designated metadata | `2564` | `431` | `1183` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `683` | `515` Daylight and motion sensor virgin | `1` | `119`, `128`, `164`, `165`, `166`, `168` | `515` | `53` |

Firmware `683` declares 17 logical Modules: slot `1` has six sensor candidate Objects, with designated Object `168`; slots 2–17 each reference IR scenario Object `431`. Virgin `515` permits exactly the six slot-1 sensor roles. These 16 IR slots are not physical buttons, extra PIR detectors or a load-rating count. Stored slot predicates cover `M=0/3` → 168, `M=1/4` → 166 and `M=2` → 128; Objects 119, 164 and 165 have no attached selection predicate. Their membership does not establish when they become active.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `683` | Physical configuration | `0` | Canonical firmware/mode association |
| `683` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `683` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Operating modes | AUTO/ECO/WALKTHROUGH; paragraph automatic / manual | `legrand-living-now-historical.pdf` printed/PDF p. 98 |
| Prose brightness / delay | `20..1275` lux / 5 s..59 min | `legrand-living-now-historical.pdf` printed/PDF p. 98 |
| Table brightness / delay | `5..1275` lux / malformed “5 s 59 min 59 h”; endpoint unresolved | `legrand-living-now-historical.pdf` printed/PDF p. 98 |
| Factory settings | 300 lux; 15 min | `legrand-living-now-historical.pdf` printed/PDF p. 98 |
| Configuration | Physical or virtual; BMSO4001/BMSO4003 IR remote configurators | `legrand-living-now-historical.pdf` printed/PDF p. 98 |
| Mounting geometry | 15 × 6 m at 2.5 m height; 45° vertical / 140° horizontal | `legrand-living-now-historical.pdf` printed/PDF p. 98 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `683` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `683` | `A` | `0..9` | `0` | Area |
| `683` | `PL` | `0..9` | `0` | PL (0-9 range) |
| `683` | `M` | `0..4` | `0` | Modality; Mode 0-4 |
| `683` | `S` | `0..3` | `0` | Sensitivity |
| `683` | `T` | `0..9` | `0` | Configurator T (time) - (0-9) |
| `683` | `D` | `0..5` | `0` | (0-5); Daylight setpoint |

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
| `FUNC_MODE` | `1` = Auto `ON`/`OFF`; `3` = Manual `ON` / Auto `OFF`; `5` = Partial `ON` / Group `OFF` | `1` | Operating mode; Functional_mode (auto / manual / partial) |
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
| `683` | `1` | `128` | `4477` | `M=2` | None |
| `683` | `1` | `166` | `4461` | `M=1` | None |
| `683` | `1` | `166` | `4505` | `M=4` | None |
| `683` | `1` | `168` | `4439` | `M=0` | None |
| `683` | `1` | `168` | `4491` | `M=3` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `683` | `119` | `2165` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | US sensitivity |
| `683` | `119` | `2166` | `INITIAL_OCCUPANCY` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `3` | Initial occupancy |
| `683` | `119` | `2167` | `MAINTAIN_OCCUPANCY` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Mantain occupancy |
| `683` | `119` | `2168` | `RETRIGGER` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Re-trigger |
| `683` | `119` | `2169` | `ALERT` | `1` = Visual; `3` = Visual and Acoustic | `0` | Alert; reusable default `0` is outside this subset; filter supplies no replacement default |
| `683` | `128` | `2060` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | US sensitivity |
| `683` | `128` | `2061` | `SCHEMA` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Detection scheme |
| `683` | `165` | `2042` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | US sensitivity |
| `683` | `165` | `2043` | `SCHEMA` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Detection scheme |
| `683` | `166` | `2114` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `683` | `166` | `2129` | `NATURAL_LIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Natural light factor |
| `683` | `166` | `2144` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `683` | `168` | `2145` | `NATURAL_LIGHT_FACTOR` | `1..255` (entire reusable range retained) | `10` | Natural light factor |
| `683` | `168` | `2159` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `683` | `168` | `2160` | `ALERT` | `1` = Visual; `3` = Visual and Acoustic | `0` | Alert; reusable default `0` is outside this subset; filter supplies no replacement default |
| `683` | `168` | `2161` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `1` | US sensitivity |
| `683` | `168` | `2162` | `INITIAL_OCC` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `3` | Initial occupancy |
| `683` | `168` | `2163` | `MAINTAIN_OCC` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Mantain occupancy |
| `683` | `168` | `2164` | `RE-TRIGGER` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Re-trigger |
| `683` | `168` | `2373` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `683` | `168` | `2454` | `DAYLIGHT_SETPOINT` | Subset flag present but no allowed values stored; unresolved restriction | `100` | Daylight setpoint (Lux) |
| `683` | `168` | `2466` | `PROVISION_OF_LIGHT` | Subset flag present but no allowed values stored; unresolved restriction | `0` | Provision of light (Lux) |
| `683` | `431` | `2388` | `TYPE_OF_REGULATION` | `3` = Stereo amplifiers only | `1` | Regulation type; reusable default `1` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

### Sensor-specific catalogue conflicts

The exact manufacturer catalogue identifies this hardware as PIR. The canonical firmware nevertheless retains US-related fields and filters admitting US-only/PIR-and-US/PIR-or-US while excluding PIR-only. These reusable and relation-specific records are preserved as source conflicts, not evidence of an ultrasonic transducer in 048834. ALERT defaults `0` fall outside subsets `{1,3}` for Objects 119/168, and Object `431` regulation default `1` lies outside subset `{3}`. Filters 2454/2466 mark subsets without storing allowed values for DAYLIGHT_SETPOINT/PROVISION_OF_LIGHT; they cannot supply a valid-domain/default resolution. No replacement value or precedence is inferred.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `81` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `164` - Scenarios daylight sensor | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `128` - Scenarios daylight and presence sensor | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `165` - Scenarios presence sensor | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `166` - Stand alone daylight sensor | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `431` - IR scenario control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `119` - Stand alone presence sensor | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `168` - Stand alone daylight and presence sensor | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `164` - Scenarios daylight sensor | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `128` - Scenarios daylight and presence sensor | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `165` - Scenarios presence sensor | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `166` - Stand alone daylight sensor | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `431` - IR scenario control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `119` - Stand alone presence sensor | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `168` - Stand alone daylight and presence sensor | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

### Special-function associations

| id_function | id_object |
| --- | --- |
| `1` | `164` |
| `1` | `166` |
| `1` | `168` |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The historical catalogue describes selectable automatic / manual behavior, delay and light threshold through BMSO4001/BMSO4003 or physical / virtual configuration. Its prose specifies 5 seconds to 59 minutes and `20..1275` lux, whereas its adjacent table gives different / inconsistent limits. Apply the full source-specific canonical field / filter tables below for Firmware `683`; declared count of 17 Modules is capability topology, not 17 simultaneous sensors.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The exact catalogue paragraph and table agree on PIR, IP55 and 140°/15 m coverage, but differ on minimum brightness (20 versus 5 lux), while the table’s delay endpoint has malformed units. Both statements are retained without repairing the table by inference. The Classe300EOS sheet only names 048834 in a compatibility table (printed/PDF p. 8); it does not establish this sensor’s electrical ratings.

The exact restriction table identifies reusable defaults outside a Firmware/Object subset. These are catalogue conflicts; no replacement default is inferred.

Visual inspection of historical catalogue p. 98 confirms the malformed delay table literally prints “5 s 59 min 59 h”; its paragraph instead says 5 s to 59 min. The 20/5 lux minimum discrepancy remains. Factory 300 lux/15 min is product prose, whereas reusable timing defaults include 10 min and reusable DAYLIGHT_SETPOINT defaults use encoded table values. Firmware `683` is Official `2.9` with no build row; no `.0` build is invented. No payload or connection association is stored, and the catalogue’s physical/virtual/advanced modes are separate from the IR remote-tool descriptions.

## Evidence limits and open work

Operating current, temperature, detailed lens / coverage diagram, exact revision-dependent timing domain and physical selector procedure remain documentation gaps. The 048971 accessory’s own protection does not replace the sensor IP55 rating.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0191-0200-2026-10-07.md#own-dev-0197)
