# PIR surface ceiling-mounted sensor

## Summary

This surface-mounted ceiling sensor uses passive infrared detection and ambient-light information for configured lighting automation. Its published coverage is approximately a six-metre diameter at the reference installation height, making mounting position part of the sensing design.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0031` | Project identity |
| Technical description | Ceiling-mounted PIR / daylight sensor with stand-alone and scenario-oriented roles | Catalogue + official documentation |
| Commercial identities | `BMSE1001`, `048833` | Catalogue |
| Catalogue item | `33` - “PIR surface ceiling mounted sensor” | Implementation evidence |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `18` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `130` | Implementation evidence |
| Declared Modules | `1` | Implementation evidence |
| Categories | Sensor, Presence, Daylight, Lighting | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSE1001` | Established identity | Canonical catalogue; canonical commercial record `33`; Commercial identity of this Technical Device |
| Legrand | `048833` | Established identity | Canonical catalogue; canonical commercial record `1556`; Commercial identity of this Technical Device |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `fiche technique 048833` | Technical sheet | `LG00295-a-FR` | printed pp. 464-467 / PDF pp. 1-4 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/96/b2/96b2d164e69405d1c7f3a1b52e3eea061ad02c1fee528c16f35971255406232f.pdf) | [Publisher PDF](https://assets.legrand.com/general/legrand-fr/pfat/gm/fiche%20technique%20048833.pdf) |
| `BTicino-MyHOME-Spanish-technical-sheets.pdf` | Spanish manufacturer technical catalogue | BT00295-a-ES | BMSE1001: printed pp. 635–639 / PDF pp. 66–70; exact-product hardware and all modes/timing; unrelated product pages not examined | [Archived original](https://archive.openwebnet-ha.org/sha256/89/4f/894f468c301ea2b7aaec22635d91961e1eedc00136a21e21b774e975c378b4eb.pdf) | [Publisher source](https://www.bticino.es/pdf/FICHA_TECNICA_DOMOTICA_MYHOME_BTICINO.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Technology / connection | PIR and daylight sensor, screw terminals for SCS BUS | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |
| Supply / current | `27 Vdc` / `10 mA` | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |
| Operating temperature / protection | `-5..45 °C` / `IP20` | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |
| Illuminance / configurable delay | `1..2000 lux` / `0..255 h` in this French sheet | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |
| Ceiling installation | Reference `2.5 m`; maximum `4 m`; avoid heat sources and air-conditioning outlets | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |
| Coverage at maximum sensitivity | Diameter `6 m`, area `28 m²` at `2.5 m`; `90°/360°` vertical/horizontal | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |
| Coverage at other heights | At `3 m`: diameter `7 m`, area `38 m²`; at `4 m`: diameter `8 m`, area `50 m²` | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |
| Controls / indicators | Multifunction button and state/configuration/setpoint LEDs | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |

| Property | Value | Evidence |
| --- | --- | --- |
| Dimensions | `75 × 40 × 20 mm`; base body height `15 mm` | `LG00295-a-FR`, printed p. 465 / PDF p. 2; diagram visually inspected |
| Delay range in Spanish technical sheet | `30 s..255 h`; differs from French `0..255 h` | `BT00295-a-ES`, printed p. 635 / PDF p. 66 |

| Height | Low sensitivity: diameter / area | Medium: diameter / area | High: diameter / area | Maximum: diameter / area |
| --- | --- | --- | --- | --- |
| `2.5 m` | `2 m` / `3 m²` | `3 m` / `7 m²` | `5 m` / `20 m²` | `6 m` / `28 m²` |
| `3 m` | `3 m` / `7 m²` | `4 m` / `13 m²` | `6 m` / `28 m²` | `7 m` / `38 m²` |
| `4 m` | `3 m` / `7 m²` | `5 m` / `20 m²` | `7 m` / `38 m²` | `8 m` / `50 m²` |

Coverage tables agree in French printed p. 465 / PDF p. 2 and Spanish printed p. 636 / PDF p. 67; the Spanish illustration labels a larger diameter at the reference height, so the illustration is not used to override the tabulated coverage.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `33` | Canonical catalogue |
| Technical item description | PIR surface ceiling mounted sensor | Canonical catalogue |
| Item family | `5` - Light / Motion detector | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `18` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `18` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `130` | `-1` | `-1` | `-1` | `1` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No AS_FW_PACKAGE association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `130` | `1` | `119` Stand alone presence sensor | Candidate alternative | `277` | `119` | `276` |
| `130` | `1` | `128` Scenarios daylight and presence sensor | Fixed/designated metadata | `587` | `128` | `406` |
| `130` | `1` | `164` Scenarios daylight sensor | Candidate alternative | `278` | `164` | `277` |
| `130` | `1` | `165` Scenarios presence sensor | Candidate alternative | `279` | `165` | `278` |
| `130` | `1` | `166` Stand alone daylight sensor | Candidate alternative | `280` | `166` | `279` |
| `130` | `1` | `168` Stand alone daylight and presence sensor | Candidate alternative | `281` | `168` | `280` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `130` | `515` Daylight and motion sensor virgin | `1` | `119`, `128`, `164`, `165`, `166`, `168` | `515` | `3` |

Slot `1` has six firmware candidate Objects: `119` Stand alone presence sensor, `164` Scenarios daylight sensor, `165` Scenarios presence sensor, `166` Stand alone daylight sensor, `168` Stand alone daylight and presence sensor, and `128` Scenarios daylight and presence sensor. Catalogue slot metadata marks Object `128` fixed and the other five non-fixed candidates. Firmware `130` associates Virgin Object `515`; other shared-family memberships do not establish another Virgin Object on this firmware. Candidate ordering is not an active-role selection rule.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `130` | Physical configuration | `0` | Canonical firmware/mode association |
| `130` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `130` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `130` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `130` | `A` | `0..9` | `0` | A; Environment |
| `130` | `PL` | `0..9` | `0` | PL; Light Point |
| `130` | `M` | `0..8` | `0` | M; Mode 0-8 |
| `130` | `S` | `0..4` | `0` | S; Configurator S (0-4) |
| `130` | `T` | `0..9` | `0` | T; Configurator T (time) - (0-9) |

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

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing and membership | `ADDR_TYPE`, `A`, `PL`, `G`, `A_R`, `PL_R`, `MAIN_GROUP`, `G1`, `G2`, `GD` | Reusable addressing and group/zone scope; apply Device firmware restrictions. |
| Sensing and operation | `TYPE_LOOP`, `DAYLIGHT_SETPOINT`, `PROVISION_OF_LIGHT`, `FUNC_MODE`, `PIR`, `US`, `INITIAL_OCC`, `MAINTAIN_OCC`, `RE-TRIGGER`, `ALERT`, `LOAD_CONTROL`, `LIGHTING_REGULATION`, `NATURAL_LIGHT_FACTOR`, `DAYLIGHT_FACTOR`, `DAYLIGHT_LEVEL` | Reusable sensing, mode and presentation settings; presence in this schema is not proof of physical capability. |
| Timing | `HOURS`, `MINUTES`, `SECONDS` | Stored timing/transition values; their encodings differ by field. |

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

### Device-specific interpretation

The French introduction says physical `M=0..4`, but its following table describes `M=0..8`, matching the firmware enum and Spanish sheet. Physical `S=0..3` is narrower than the firmware range: conversion rule `6` has no PIR branch for `S=4`. Rule `6` gives `T=0` zero duration, whereas the physical absent configurator gives `15 min`. Reusable ultrasonic values do not establish ultrasonic hardware in this PIR sensor. Foreign-scope filters and the conversion names `FUNCTIONAL_MODE` and `REG` must not be silently aliased to `FUNC_MODE` and `LIGHTING_REGULATION`. Empty daylight subsets `2444` and `2456` provide no known legal values.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `130` | `1` | `128` | `4478` | `M=2` | `6` |
| `130` | `1` | `166` | `4462` | `M=1` | `6` |
| `130` | `1` | `166` | `4506` | `M=4` | `6` |
| `130` | `1` | `166` | `4546` | `M=7` | `6` |
| `130` | `1` | `166` | `4559` | `M=8` | `6` |
| `130` | `1` | `168` | `4441` | `M=0` | `6` |
| `130` | `1` | `168` | `4492` | `M=3` | `6` |
| `130` | `1` | `168` | `4520` | `M=5` | `6` |
| `130` | `1` | `168` | `4533` | `M=6` | `6` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `130` | `119` | `78` | `GD` | `0..255` (entire reusable range retained) | `0` | Daylight Sensor group; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `130` | `119` | `79` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `1` | US sensitivity; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `130` | `119` | `81` | `TYPE_LOOP` | `0` = Closed loop; `1` = Open loop (entire reusable range retained) | `0` | Type loop; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `130` | `119` | `83` | `FUNC_MODE` | `2` = Auto walkthrough | `2` | Functional mode; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `130` | `119` | `84` | `INITIAL_OCC` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US (entire reusable range retained) | `3` | Initial occupancy; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `130` | `119` | `85` | `MAINTAIN_OCC` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US (entire reusable range retained) | `4` | Mantain occupancy; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `130` | `119` | `86` | `RE-TRIGGER` | `0` = Disabled; `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US (entire reusable range retained) | `4` | Re-trigger; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `130` | `119` | `87` | `ALERT` | `0` = Disabled; `1` = Visual; `2` = Acoustic; `3` = Visual and Acoustic (entire reusable range retained) | `0` | Alert; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `130` | `119` | `2353` | `INITIAL_OCCUPANCY` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US (entire reusable range retained) | `3` | Initial occupancy |
| `130` | `119` | `2354` | `MAINTAIN_OCCUPANCY` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US (entire reusable range retained) | `4` | Mantain occupancy |
| `130` | `119` | `2355` | `RETRIGGER` | `0` = Disabled; `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US (entire reusable range retained) | `4` | Re-trigger |
| `130` | `119` | `2356` | `ALERT` | `0` = Disabled; `1` = Visual; `2` = Acoustic; `3` = Visual and Acoustic (entire reusable range retained) | `0` | Alert |
| `130` | `119` | `2357` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | US sensitivity |
| `130` | `128` | `351` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | US sensitivity |
| `130` | `128` | `352` | `SCHEMA` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Detection Schema |
| `130` | `165` | `88` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | US sensitivity |
| `130` | `165` | `89` | `SCHEMA` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Detection Schema |
| `130` | `166` | `92` | `TYPE_LOOP` | `0` = Closed loop; `1` = Open loop (entire reusable range retained) | `0` | Type loop |
| `130` | `166` | `2100` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `130` | `166` | `2115` | `NATURAL_LIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Natural light factor |
| `130` | `166` | `2130` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `130` | `166` | `2358` | `GD` | `0..255` (entire reusable range retained) | `0` | Daylight sensor group |
| `130` | `168` | `96` | `GD` | `0..255` (entire reusable range retained) | `0` | Daylight Sensor group |
| `130` | `168` | `97` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `1` | US sensitivity |
| `130` | `168` | `99` | `TYPE_LOOP` | `0` = Closed loop; `1` = Open loop (entire reusable range retained) | `0` | Type loop |
| `130` | `168` | `100` | `NATURAL_LIGHT_FACTOR` | `1..255` (entire reusable range retained) | `10` | natula light |
| `130` | `168` | `103` | `FUNC_MODE` | `2` = Auto walkthrough | `2` | Functional mode |
| `130` | `168` | `104` | `INITIAL_OCC` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US (entire reusable range retained) | `3` | Initial occupancy |
| `130` | `168` | `105` | `MAINTAIN_OCC` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US (entire reusable range retained) | `4` | Mantain occupancy |
| `130` | `168` | `106` | `RE-TRIGGER` | `0` = Disabled; `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US (entire reusable range retained) | `4` | Re-trigger |
| `130` | `168` | `107` | `ALERT` | `0` = Disabled; `1` = Visual; `2` = Acoustic; `3` = Visual and Acoustic (entire reusable range retained) | `0` | Alert |
| `130` | `168` | `2146` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `130` | `168` | `2361` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `130` | `168` | `2444` | `DAYLIGHT_SETPOINT` | Subset flag present but no allowed values stored; unresolved restriction | `100` | Daylight setpoint (Lux) |
| `130` | `168` | `2456` | `PROVISION_OF_LIGHT` | Subset flag present but no allowed values stored; unresolved restriction | `0` | Provision of light (Lux) |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `6` | `M=3` | `ADDR_TYPE` = `0`; `MAIN_GROUP` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1`; `REG` = `1` | `6` |
| `6` | `M=4` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `1` | `6` |
| `6` | `M=5` | `ADDR_TYPE` = `0`; `MAIN_GROUP` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `0` | `6` |
| `6` | `M=6` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `1` | `6` |
| `6` | `M=7` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `0` | `6` |
| `6` | `M=8` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1`; `REG` = `1` | `6` |
| `6` | `S=0` | `PIR` = `0` | `6` |
| `6` | `S=1` | `PIR` = `1` | `6` |
| `6` | `S=2` | `PIR` = `2` | `6` |
| `6` | `S=3` | `PIR` = `3` | `6` |
| `6` | `T=0` | `HOURS` = `0`; `MINUTES` = `0`; `SECONDS` = `0` | `6` |
| `6` | `T=1` | `HOURS` = `0`; `MINUTES` = `0`; `SECONDS` = `30` | `6` |
| `6` | `T=2` | `HOURS` = `0`; `MINUTES` = `1`; `SECONDS` = `0` | `6` |
| `6` | `T=3` | `HOURS` = `0`; `MINUTES` = `2`; `SECONDS` = `0` | `6` |
| `6` | `T=4` | `HOURS` = `0`; `MINUTES` = `5`; `SECONDS` = `0` | `6` |
| `6` | `T=5` | `HOURS` = `0`; `MINUTES` = `10`; `SECONDS` = `0` | `6` |
| `6` | `T=6` | `HOURS` = `0`; `MINUTES` = `15`; `SECONDS` = `0` | `6` |
| `6` | `T=7` | `HOURS` = `0`; `MINUTES` = `20`; `SECONDS` = `0` | `6` |
| `6` | `T=8` | `HOURS` = `0`; `MINUTES` = `30`; `SECONDS` = `0` | `6` |
| `6` | `T=9` | `HOURS` = `0`; `MINUTES` = `40`; `SECONDS` = `0` | `6` |
| `6` | `M=0` | `ADDR_TYPE` = `0`; `MAIN_GROUP` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1` | `6` |
| `6` | `M=1` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1`; `REG` = `0` | `6` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 18`, `BMSE1001` / `048833` and installed identity fields | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware rather than assuming wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | identify which of the six candidate sensor Objects is active in the single Module position | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the address appropriate to the resolved sensor/scenario role | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | correlate physical `A` / `PL` / `M` / `S` / `T` with role-specific presence/daylight configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Depending on resolved Object/configuration, the Device participates in lighting automation as a presence sensor, daylight sensor, combined sensor or scenario-oriented sensor.

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| `M=0` | Automatic presence/daylight ON and timed OFF; manual OFF inhibits until the absence interval expires. | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |
| `M=1` | Twilight ON/OFF control with PIR disabled; no group/general addressing. | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |
| `M=2` | Reports motion and illuminance to a scenario controller; unique address; S and T absent. | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |
| `M=3` | Automatic constant-illuminance regulation with presence and timed OFF; temporary manual level resets after absence. | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |
| `M=4` | Constant-illuminance regulation, PIR disabled, manual initial ON; no automatic restart after extinguishing. | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |
| `M=5/6/7` | Manual ON variants of presence/daylight, constant-light regulation and twilight control respectively. | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |
| `M=8` | Manual ON twilight/regulation mode; printed text says OFF below setpoint at minimum dimmer level. Do not silently invert this wording. | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |

In presence/daylight modes the Spanish sheet states that sufficient natural light suppresses a load-control signal even when PIR detects presence (printed p. 635 / PDF p. 66). The product has PIR and a light sensor; no examined original establishes ultrasonic hardware.

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact technical item is currently retained.

## Programming

Resolve the active slot Object before exposing configuration. Keep the official physical `A` / `PL` / `M` / `S` / `T` limits distinct from the wider software/database domains.

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Physical address / sensitivity | `A=1..9`, `PL=1..9`; `S=0/1/2/3` means low/medium/high/maximum. | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |
| Physical OFF delay | Absent `T`: `15 min`; `T=1`: `30 s`; `2/3/4/5/6/7/8/9`: `1/2/5/10/15/20/30/40 min` respectively. | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |
| Setpoint acquisition | Hold button `2 s`; red LED flashes; pass under sensor; acquisition ends after about `20 s`. Repeat after moving sensor or room furniture. | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |
| Configuration actions | Short press selects during virtual configuration; two short presses enter Push & Learn; short press then `10 s` press resets. | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |
| Lighting Management | Plug & Go, Push & Learn, Project & Download are documented product workflows, separate from catalogue numeric modes. | `LG00295-a-FR`, printed pp. 464–467 / PDF pp. 1–4 |

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| LED steady green | BUS present | `LG00295-a-FR`, printed p. 464 / PDF p. 1 |
| LED orange flash | Presence detected | `LG00295-a-FR`, printed p. 464 / PDF p. 1 |
| LED rapid orange/green | Missing/incorrect configuration | French p. 464 / PDF p. 1; Spanish p. 635 / PDF p. 66 |
| LED orange/green each `1 s` | Configuration active | French p. 464 / PDF p. 1; Spanish p. 635 / PDF p. 66 |
| LED rapid red / red-green | Setpoint acquisition / sensor calibration respectively | French p. 464 / PDF p. 1; Spanish p. 635 / PDF p. 66 |

## Source reconciliation

The retained French sheet directly describes `048833` and names `BMSE1001` in its coverage section. Its physical introduction says `M=0..4`, yet the following function table explicitly describes `M=0..8`, agreeing with the firmware enum. That is an internal document discrepancy, not evidence that modes `5..8` exist only in software. Physical `S=0..3` remains narrower than the stored `0..4`, with no conversion branch for `S=4`.

Rule `6` maps `T=0` to zero time; the physical sheet gives an absent configurator a `15 min` default. Reusable Object defaults vary again. The PIR/daylight hardware description does not substantiate the ultrasonic detection values retained by several reusable schemas and filters. Stored conversion output names and foreign-scope filters remain visible without inferred aliases.

The already-retained Spanish `BT00295-a-ES` directly corroborates `BMSE1001`, lists physical `M=0..8`, and agrees on electrical/environmental ratings, sensitivity and timing table. It adds daylight priority over PIR when natural light is sufficient. Its headline delay lower bound is `30 s` instead of the French `0`; both still give absent T a `15 min` default.

Mode `M=8` differs materially: Spanish printed p. 637 / PDF p. 68 describes automatic ON below threshold and OFF above, while French printed p. 466 / PDF p. 3 describes manual initial ON and OFF below setpoint at minimum dimming. Spanish mode `M=3/4` text also references configurator D, absent from both printed A/PL/M/S/T lists and this firmware surface. For setpoint acquisition, Spanish printed p. 638 / PDF p. 69 says leave the area beneath the sensor, whereas the French text says pass beneath it. The common two-second acquisition hold and approximately twenty-second completion are retained; incompatible procedural wording is not merged. No hardware/revision observation resolves these differences.

## Evidence limits and open work

- Hardware-corroborate the resolved Object for representative physical and virtual configurations.
- Resolve firmware `S=4` and the French/Spanish `M=8` behavior difference without treating published physical modes `5..8` as software-only.

- Linked programming software/help, other product-download revisions and unrelated multi-product guide pages were not inspected; the Documentation table gives the examined scope. Catalogue mode associations and reusable schemas are not observed installed behavior.

- French/Spanish `M=8`, setpoint movement instructions, delay lower bound and the Spanish unexplained D reference remain source-revision conflicts. The Lighting Management glossary/software help linked by these sheets was not inspected.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [fiche technique 048833](https://archive.openwebnet-ha.org/sha256/96/b2/96b2d164e69405d1c7f3a1b52e3eea061ad02c1fee528c16f35971255406232f.pdf)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0031-0040-2026-10-06.md#own-dev-0031)
