# Living Now LIGHT digital control

## Summary

This Living Now LIGHT digital control operates one or two configured lighting functions from an electrified support frame. Its central or top/bottom actuation and blue status indication provide a compact local lighting interface.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0114` | Project identity |
| Technical description | Living Now LIGHT digital control | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `KW8010`, `KM8010`, `KG8010` | All three catalogue commercial records; confidence scoped below |
| Catalogue item | `2272` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `117` | Main association; independent of project ID |
| Firmware definition | `803` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `3` | Firmware metadata |
| Categories | Commands, User interfaces | Source-derived roles |

The exact manufacturer sheet and reference lists establish all three Living Now colour variants. This is one physical digital control mounted on an electrified frame, distinct from the catalogue’s logical Module count. It manages one or two light functions; the third logical Module handles brightness. The sheet’s three front callouts illustrate selectable touch positions, not three independently published light functions.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Living Now | `KW8010` | Established commercial variant | Catalogue record `2627`; published family/variant scope reconciled below |
| BTicino - Living Now | `KM8010` | Established commercial variant | Catalogue record `2628`; published family/variant scope reconciled below |
| BTicino - Living Now | `KG8010` | Established commercial variant | Catalogue record `2629`; published family/variant scope reconciled below |

The exact technical sheet names `KW8010`, `KM8010` and `KG8010` together; the retained guide/catalogue lists establish white, sand and black. Individual publisher exports independently identify Living Now, with the KM colour attribute labelled Beige and the catalogue labelled sand. The canonical commercial descriptions distinguish colours even though the technical item/name contains “white”; that source label does not make all variants white. EAN and commercial identity do not establish installed firmware. All three variant exports are retained separately.

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `KW8010` | `8005543645994` | [Archived original](https://archive.openwebnet-ha.org/sha256/88/ca/88ca328656a25c613079ee74ad293d6ae1be4b0c06a970fb9be1f89e730c3af1.pdf), `KW8010-publisher-product-sheet.pdf`, printed/PDF p. 1 |
| `KM8010` | `8005543646014` | [Archived original](https://archive.openwebnet-ha.org/sha256/da/24/da2404125a548a616b6b5f4314e5268be741b72c6e65f485c075edf18ca4d71d.pdf), `KM8010-publisher-product-sheet.pdf`, printed/PDF p. 1 |
| `KG8010` | `8005543646038` | [Archived original](https://archive.openwebnet-ha.org/sha256/2f/9b/2f9b4480ea05ad1e53f34957ccf13c60771e818307ab2af87c7907b6d4d3bd2f.pdf), `KG8010-publisher-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

### Complete catalogue commercial metadata

| Record | Reference | Catalogue name | Brand key | Line key | Visible | Visibility type | Dependent | Gateway | Catalogue description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `2627` | `KW8010` | `Adv - command white` | `1` | `20` | `1` |  | `0` | `0` | `Adv - command white` |
| `2628` | `KM8010` | `Adv - command white` | `1` | `20` | `1` |  | `0` | `0` | `Adv - command sand` |
| `2629` | `KG8010` | `Adv - command white` | `1` | `20` | `1` |  | `0` | `0` | `Adv - command dark` |

Empty catalogue values are retained as empty metadata; none is an installed-state or market-availability observation.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ST-00000542-EN.pdf` | English LIGHT technical sheet | `ST-00000542-EN; 21/02/2020` | KW/KM/KG8010: specifications, layout, light/brightness functions and MyHOME_Up/Suite setup. Printed/PDF p. 1. | [Archived original](https://archive.openwebnet-ha.org/sha256/0e/65/0e6556ab0dc6719429e7e5d5cfeb4bc715ca134cc0d3fdacae4cfa97ed11e662.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00000542-EN.pdf) |
| `KW8010-publisher-product-sheet.pdf` | English publisher product export | `DATASHEET; 03.10.2026` | Complete exact-reference export: commercial/EAN and all classification fields; linked documents inventoried separately, not automatically incorporated | [Archived original](https://archive.openwebnet-ha.org/sha256/88/ca/88ca328656a25c613079ee74ad293d6ae1be4b0c06a970fb9be1f89e730c3af1.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-KW8010&include_technical=1) |
| `KM8010-publisher-product-sheet.pdf` | English publisher product export | `DATASHEET; 03.10.2026` | Complete exact-reference export: commercial/EAN and all classification fields; linked documents inventoried separately, not automatically incorporated | [Archived original](https://archive.openwebnet-ha.org/sha256/da/24/da2404125a548a616b6b5f4314e5268be741b72c6e65f485c075edf18ca4d71d.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-KM8010&include_technical=1) |
| `KG8010-publisher-product-sheet.pdf` | English publisher product export | `DATASHEET; 03.10.2026` | Complete exact-reference export: commercial/EAN and all classification fields; linked documents inventoried separately, not automatically incorporated | [Archived original](https://archive.openwebnet-ha.org/sha256/2f/9b/2f9b4480ea05ad1e53f34957ccf13c60771e818307ab2af87c7907b6d4d3bd2f.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-KG8010&include_technical=1) |
| `KW8010-italian-product-sheet.pdf` | Italian publisher product export | `Price-list validity 01/07/2026; retrieved 03/10/2026` | KW8010 only: exact name, line, supply/current/module attribute and EAN p. 1; compatible parts on following pages. Printed/PDF pages coincide. Prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/0d/b0/0db0a0ec30b49ade3e2b7ee44e7d00499c777c7209c6815228e417766594c117.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-KW8010) |
| `MyHOME-Technical-Guide.pdf` | English system technical guide | `AD-EXMH25GT; Versione 6/2025 printed on rear cover; URL directory is older` | Digital-control customisation, construction, mounting, Home+Project, frame/box composition and exact colour/reference lists: printed pp. 22, 50-53, 84-85 / PDF pp. 22, 50-53, 84-85. Printed edition confirmed on rear cover. | [Archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) | [Publisher original](https://www.bticino.com/sites/default/files/2024-02/MyHOME%20Technical%20Guide.pdf) |
| `Living-Now-2025-3M-catalogue.pdf` | English Living Now catalogue | `AD-EXLNW25C/GB; Edition 01/2025 printed on rear cover` | KW/KG/KM8010 and 8011 exact family/colour descriptions, functions and frame/connection compatibility printed p. 103 / PDF p. 103. The original contains the complete 144-page catalogue. | [Archived original](https://archive.openwebnet-ha.org/sha256/e3/15/e3153d42a54335de37d0ca05b7f696b3345bf2743ebe2ec78e32a1cb7ee5f47e.pdf) | [Publisher original](https://www.bticino.com/sites/default/files/2024-12/GB%20Living%20NOW%20catalogue%203%20MODULES%202025.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2272`: all firmware/commercial/system/Object/Module/Virgin/field/filter/mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `18..27 Vdc`; SCS through four frame contact clips | `ST-00000542-EN` p. 1 |
| Maximum current | `6 mA` | Exact sheet p. 1; family rating |
| Current-export standby by variant | KW `3.5 mA`, KM `3.5 mA`, KG `3.8 mA` | Each exact export p. 3; separate from sheet maximum |
| Italian KW catalogue attribute | Supply `27 Vdc`; current `6 mA`; one module | Italian KW8010 export p. 1; current is not labelled standby |
| Local controls/indication | One central or two top/bottom light controls; blue LED indicates lighting on | Exact sheet p. 1; two actuation points/buttons in each export |
| Physical format | One digital position, described as one-module surface mounting; supported by an electrified frame | `ST-00000542-EN` p. 1; MyHOME guide pp. 50-53 |
| Operating temperature by source | Sheet `5..40 °C`; current exports `5..45 °C` | `ST-00000542-EN` p. 1; each export p. 3; unresolved upper-bound difference |
| Current-export metric size | `40 x 86 x 6 mm`; built-in depth `2 mm`; minimum box depth `40 mm` | All three colour exports p. 3; scope is product attributes, separate from frame/box assembly |
| Current-export storage/protection | `-10..70 °C`, `IP20`; IK not applicable | All three colour exports p. 3 |
| Materials/finish | Matt untreated thermoplastic; white / Beige / black; not transparent | Exact colour exports p. 3 |
| Connection mechanism | Four clips / SCS contact points; no per-control parallel BUS wiring needed when using electrified frame | `ST-00000542-EN` p. 1; guide p. 51 |
| Publisher terminal attributes | Capacity `1..1 mm²`, flexible or rigid wire; terminal marking No | Exports p. 4; attributes do not turn frame contacts into a conventional direct wiring diagram |
| Published standards | `EN50491`; `EN60669-2-5` | `ST-00000542-EN` p. 1 |
| Current-export classifications | SCS operating method; bus connection Yes; radio/KNX/LON/Powernet and bidirectional radio No; no display, thermostat, IR-sensor attribute or label area | All three exports pp. 3-4; not an OpenWebNet transport declaration |

### Published frame and box composition

| Installation format | Box options / dimensions | Support | Electrified frame / digital positions |
| --- | --- | --- | --- |
| 2-module box | `502E` (`70 x 70 x 50 mm`) or `PB502N` (`Ø71 x 50.5 mm`) | `K8102` | `..8102P1`, three digital positions |
| 3-module box | `503E` (`108 x 74 x 53.5 mm`) or `PB503N` (`110 x 71 x 52 mm`) | `K4703` | `..8103` three positions or `..8103P1` four |
| 4-module box | `504E` (`133 x 74 x 53.5 mm`) or `PB504N` (`132.5 x 71 x 52 mm`) | `K4704` | `..8104` four positions or `..8104P1` five |

MyHOME guide p. 53 and Living Now catalogue p. 103 distinguish box size from digital position count. Normal connection uses `K8001`, whose position inside the box is free. When a shared installation uses additional power supply `K8003` for the separate voice control, the guide says not to install `K8001`; that exception is system-level, not a power-supply module built into this control. Frames/supports, load actuators and blanking parts are separate products.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2272` | Canonical catalogue |
| Technical item description | Adv - command white | Canonical catalogue |
| Item family | 0; key `1` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `117` | `AS_ITEM_SYSTEM` |
| Commercial record count | `3` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `117` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `803` | `1` | `0` | No build row | `3` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `803` | `1` | `434` Simplified Light single control basic | Fixed/designated metadata | `3339` | `652` | `1618` |
| `803` | `2` | `434` Simplified Light single control basic | Fixed/designated metadata | `3340` | `652` | `1618` |
| `803` | `3` | `148` Led Brightness Settings | Fixed/designated metadata | `3338` | `657` | `1617` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `803` | `521` Soft-Touch command virgin | `1`, `2` | `410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `418`, `419`, `421`, `426`, `427`, `462` | `521` | `139` |

Slots `1/2` designate two instances of Object `434`; slot `3` designates brightness Object `148`. This is two lighting function positions plus UI metadata, not three lighting channels. Virgin Object `521` covers only command slots `1/2` and lists generic Objects `410..419`, `421`, `426`, `427`, `462`. Those are different from this firmware’s direct membership. No conversion or slot predicate establishes when or how they become active; the generic Virgin list must not enlarge published Device capability. Multi-slot candidates do not create extra stored placements in their covered slots.

## Configuration modes

The exact 2020 sheet names MyHOME_Up and MyHOME_Suite. The retained `6/2025` system guide names Home+Project for function assignment, associated actuators and icon configuration. These are source/revision-specific workflows. The catalogue mode and connection associations above remain the implementation snapshot; no installed gateway/app/firmware compatibility is inferred from current app names. No published physical configurator setup is documented for this digital contact-mounted control.

### Complete catalogue mode and connection associations

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `803` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `803` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `434` - Simplified Light single control basic

Catalogue Object key `652` maps to external Object `434`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `MODE` | `0` = Cyclical without regulation; `1` = `OFF` without regulation; `2` = `ON` without regulation; `3` = `PUL`; `4` = Extended timed-`ON` command | `0` | Modality |
| `ADDR_TYPE` | `0` = Point to point; `2` = Group; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `0..255` | `1` | Main Group (`GR`/GS) |
| `HOURS` | `0..255` | `0` | Hours; Only for `MOD=4` |
| `MINUTES` | `0..59` | `0` | Minutes; Only for `MOD=4` |
| `SECONDS` | `0..59` | `30` | TimeSec; Only for `MOD=4` |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |

### Object `148` - Led Brightness Settings

Catalogue Object key `657` maps to external Object `148`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LED_BRIGHTNESS_LEVEL` | `0` = Min; `1` = Max | `0` | Led brightness level |
| `LED_OFF_FOR_POWER_SAVE` | `0` = NO; `1` = YES | `0` | Led `OFF` for power save |
| `G` | `0..255` | `0` | Main Group (`GR`/GS) |

### Published function and touch-area mapping

| Function | Published occupancy | Control behavior | Evidence |
| --- | --- | --- | --- |
| Cyclical light | One function position | Touch alternates `ON/OFF`; non-point-to-point configuration has no state return and alternates transmitted commands | `ST-00000542-EN` p. 1 |
| `OFF`-only | One function position | Only `OFF` transmitted | `ST-00000542-EN` p. 1 |
| Pushbutton | One function position | Published `PUL` mode | `ST-00000542-EN` p. 1 |
| Timed `ON` | One function position | Published sheet says the switch-off command follows the configured interval; exact parameters determine duration | `ST-00000542-EN` p. 1 |
| Brightness | UI settings | Configured LEDs can use default or maximum level; default level is not numerically specified | `ST-00000542-EN` p. 1 |

### Object `410` - Light control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `1` = Timed `ON`; `2` = Toggle dimmer; `4` = Toggle `ON/OFF`; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `20` = `ON` and point to point dimmer; `21` = `OFF` and point to point dimmer; `22` = `ON` and Dimmer; `23` = `OFF` and Dimmer; `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90%; `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `131` = Customized toggle dimmer; `133` = Customized toggle dimmer without regulation; `135` = Customized `ON` and dimmer without regulation; `136` = Customized `OFF` and dimmer without regulation; `137` = Customized `ON` and dimmer with regulation; `138` = Customized `OFF` and dimmer with regulation | `0` | Modality; Mode (MODE+`ON/OFF`) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group  |
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

### Object `411` - Automation control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = UP bistable control; `1` = DOWN bistable control; `2` = UP monostable control; `3` = DOWN monostable control; `4` = UP monostable and bistable control; `5` = DOWN monostable and bistable control | `0` | Modality; mode (UP/DOWN) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group  |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `412` - Lock/unlock actuator control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `1` = Disable; `2` = Enable | `1` | Modality; mode (D/E) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group  |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `413` - Scenario module control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Scenario activation and modification; `1` = Scenario activation | `0` | Modality |
| `APL` | `0` = `A=0` `PL=0`; `1` = `A=0` `PL=1`; `2` = `A=0` `PL=2`; `3` = `A=0` `PL=3`; `4` = `A=0` `PL=4`; `5` = `A=0` `PL=5`; `6` = `A=0` `PL=6`; `7` = `A=0` `PL=7`; `8` = `A=0` `PL=8`; `9` = `A=0` `PL=9`; `10` = `A=0` `PL=10`; `11` = `A=0` `PL=11`; `12` = `A=0` `PL=12`; `13` = `A=0` `PL=13`; `14` = `A=0` `PL=14`; `15` = `A=0` `PL=15`; `16` = `A=1` `PL=0`; `17` = `A=1` `PL=1`; `18` = `A=1` `PL=2`; `19` = `A=1` `PL=3`; `20` = `A=1` `PL=4`; `21` = `A=1` `PL=5`; `22` = `A=1` `PL=6`; `23` = `A=1` `PL=7`; `24` = `A=1` `PL=8`; `25` = `A=1` `PL=9`; `26` = `A=1` `PL=10`; `27` = `A=1` `PL=11`; `28` = `A=1` `PL=12`; `29` = `A=1` `PL=13`; `30` = `A=1` `PL=14`; `31` = `A=1` `PL=15`; `32` = `A=2` `PL=0`; `33` = `A=2` `PL=1`; `34` = `A=2` `PL=2`; `35` = `A=2` `PL=3`; `36` = `A=2` `PL=4`; `37` = `A=2` `PL=5`; `38` = `A=2` `PL=6`; `39` = `A=2` `PL=7`; `40` = `A=2` `PL=8`; `41` = `A=2` `PL=9`; `42` = `A=2` `PL=10`; `43` = `A=2` `PL=11`; `44` = `A=2` `PL=12`; `45` = `A=2` `PL=13`; `46` = `A=2` `PL=14`; `47` = `A=2` `PL=15`; `48` = `A=3` `PL=0`; `49` = `A=3` `PL=1`; `50` = `A=3` `PL=2`; `51` = `A=3` `PL=3`; `52` = `A=3` `PL=4`; `53` = `A=3` `PL=5`; `54` = `A=3` `PL=6`; `55` = `A=3` `PL=7`; `56` = `A=3` `PL=8`; `57` = `A=3` `PL=9`; `58` = `A=3` `PL=10`; `59` = `A=3` `PL=11`; `60` = `A=3` `PL=12`; `61` = `A=3` `PL=13`; `62` = `A=3` `PL=14`; `63` = `A=3` `PL=15`; `64` = `A=4` `PL=0`; `65` = `A=4` `PL=1`; `66` = `A=4` `PL=2`; `67` = `A=4` `PL=3`; `68` = `A=4` `PL=4`; `69` = `A=4` `PL=5`; `70` = `A=4` `PL=6`; `71` = `A=4` `PL=7`; `72` = `A=4` `PL=8`; `73` = `A=4` `PL=9`; `74` = `A=4` `PL=10`; `75` = `A=4` `PL=11`; `76` = `A=4` `PL=12`; `77` = `A=4` `PL=13`; `78` = `A=4` `PL=14`; `79` = `A=4` `PL=15`; `80` = `A=5` `PL=0`; `81` = `A=5` `PL=1`; `82` = `A=5` `PL=2`; `83` = `A=5` `PL=3`; `84` = `A=5` `PL=4`; `85` = `A=5` `PL=5`; `86` = `A=5` `PL=6`; `87` = `A=5` `PL=7`; `88` = `A=5` `PL=8`; `89` = `A=5` `PL=9`; `90` = `A=5` `PL=10`; `91` = `A=5` `PL=11`; `92` = `A=5` `PL=12`; `93` = `A=5` `PL=13`; `94` = `A=5` `PL=14`; `95` = `A=5` `PL=15`; `96` = `A=6` `PL=0`; `97` = `A=6` `PL=1`; `98` = `A=6` `PL=2`; `99` = `A=6` `PL=3`; `100` = `A=6` `PL=4`; `101` = `A=6` `PL=5`; `102` = `A=6` `PL=6`; `103` = `A=6` `PL=7`; `104` = `A=6` `PL=8`; `105` = `A=6` `PL=9`; `106` = `A=6` `PL=10`; `107` = `A=6` `PL=11`; `108` = `A=6` `PL=12`; `109` = `A=6` `PL=13`; `110` = `A=6` `PL=14`; `111` = `A=6` `PL=15`; `112` = `A=7` `PL=0`; `113` = `A=7` `PL=1`; `114` = `A=7` `PL=2`; `115` = `A=7` `PL=3`; `116` = `A=7` `PL=4`; `117` = `A=7` `PL=5`; `118` = `A=7` `PL=6`; `119` = `A=7` `PL=7`; `120` = `A=7` `PL=8`; `121` = `A=7` `PL=9`; `122` = `A=7` `PL=10`; `123` = `A=7` `PL=11`; `124` = `A=7` `PL=12`; `125` = `A=7` `PL=13`; `126` = `A=7` `PL=14`; `127` = `A=7` `PL=15`; `128` = `A=8` `PL=0`; `129` = `A=8` `PL=1`; `130` = `A=8` `PL=2`; `131` = `A=8` `PL=3`; `132` = `A=8` `PL=4`; `133` = `A=8` `PL=5`; `134` = `A=8` `PL=6`; `135` = `A=8` `PL=7`; `136` = `A=8` `PL=8`; `137` = `A=8` `PL=9`; `138` = `A=8` `PL=10`; `139` = `A=8` `PL=11`; `140` = `A=8` `PL=12`; `141` = `A=8` `PL=13`; `142` = `A=8` `PL=14`; `143` = `A=8` `PL=15`; `144` = `A=9` `PL=0`; `145` = `A=9` `PL=1`; `146` = `A=9` `PL=2`; `147` = `A=9` `PL=3`; `148` = `A=9` `PL=4`; `149` = `A=9` `PL=5`; `150` = `A=9` `PL=6`; `151` = `A=9` `PL=7`; `152` = `A=9` `PL=8`; `153` = `A=9` `PL=9`; `154` = `A=9` `PL=10`; `155` = `A=9` `PL=11`; `156` = `A=9` `PL=12`; `157` = `A=9` `PL=13`; `158` = `A=9` `PL=14`; `159` = `A=9` `PL=15`; `160` = `A=10` `PL=0`; `161` = `A=10` `PL=1`; `162` = `A=10` `PL=2`; `163` = `A=10` `PL=3`; `164` = `A=10` `PL=4`; `165` = `A=10` `PL=5`; `166` = `A=10` `PL=6`; `167` = `A=10` `PL=7`; `168` = `A=10` `PL=8`; `169` = `A=10` `PL=9`; `170` = `A=10` `PL=10`; `171` = `A=10` `PL=11`; `172` = `A=10` `PL=12`; `173` = `A=10` `PL=13`; `174` = `A=10` `PL=14`; `175` = `A=10` `PL=15` | `0` | Scenario module address |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15 | `0` | Destination level; Destination level (`0..15`) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `SCE_BUTT_1` | `1..16` | `1` | Scenario number |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay of scenario number |

### Object `414` - Scheduled scenario (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `CEN_BUTT_1` | `0..31` | `1` | Button |
| `MODE` | `0` = Press/release only; `1` = Press/hold/release | `0` | Modality; Mode (Lighting management) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `415` - Scenario PLUS Lighting Management (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = `ON`; `1` = `OFF`; `2` = `ON` with regulation; `3` = `OFF` with regulation | `0` | Modality; Mode (`ON/OFF` regulation) |
| `PPT_SCE_1` | `0..255` | `1` | Upper button scenario |
| `TYPE_OF_REGULATION` | `0` = Regulate all; `1` = Lights only; `2` = Shutters only; `3` = Stereo amplifiers only | `0` | Regulation type |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for upper button |

### Object `416` - Scheduled scenario PLUS (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | `0..255` | `1` | Scheduled scenario PLUS number |
| `PPT_CEN_HIG` | `0..7` | `0` | Scheduled scenario PLUS number |
| `BUTTON_1` | `0..31` | `1` | Button |
| `MODE` | `0` = Press/release only; `1` = Press/hold/release | `0` | Modality; Mode (Lighting management) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `417` - AUX control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Cyclical; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `17` = DOWN Shutter bistable command; `18` = UP shutter monostable command; `4` = Reset `BI`; `5` = Reset `TRI`; `6` = Reset `GEN`; `1` = Disable; `2` = Enable; `16` = UP shutter bistable command; `19` = DOWN Shutter monostable command | `0` | Modality; mode(Cyclical,off,on,pul,up,down,...) |
| `OUT_AUX_CH` | `1..15` | `1` | AUX channel |
| `TYPE_CONTACT` | No legal values specified in source | `0` | Contact type |

### Object `418` - Open lock control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same level; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Level |

### Object `419` - Sound diffusion control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = `ON`/volume +; `1` = `OFF`/volume -; `2` = Change track; `3` = Switch source; `4` = Toggle `ON/OFF` | `0` | Modality; Mode (VOL,ON_OFF) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `3` = General | `0` | Addressing type |
| `A` | `0..9` | `0` | Area |
| `PF` | `0..9` | `0` | Audio point |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `IS_FOLLOW_ME` | `0` = No; `1` = Yes | `1` | Follow me |
| `SOURCE` | `1..9` | `1` | Source |
| `SUB_SOURCE` | `0..255` | `0` | Sub source |
| `CHANNEL` | `0` = Base Band; `1` = Left; `2` = Right; `3` = Stereo; `8` = Base Band and Video; `9` = Left and video; `10` = Right and video; `11` = Left and video | `3` | Channel (BB-Stereo) |

### Object `421` - Cyclic autoswitch control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |

### Object `426` - Staircase light control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |

### Object `427` - Floor call control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `TO_ALL` | `0` = Point to point; `1` = General | `1` | Type of call |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input AUX channel |

### Object `462` - Open lock command on session (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |

### Semantic review findings

Firmware `803` designates two Object `434` lighting positions and separate brightness Object `148`; its only MODE filter allows `2`, excluding generic default `0` and broader published modes. Virgin `521` admits 14 different reusable Objects with 83 fields, none directly associated with this firmware. Their schemas are now explicit, without importing their roles into the physical LIGHT control. The one physical digital position and three logical Modules remain distinct.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `803` | `434` | `3835` | `MODE` | `2` = `ON` without regulation | `0` | Modality; reusable default `0` is outside this subset; filter supplies no replacement default |
| `803` | `434` | `3860` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `803` | `434` | `3863` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion reference is attached to these slot rows. Resolve the active Object and apply its firmware-specific domain restrictions separately. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `117` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Read installed firmware and compare with the applicability table | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Obtain hardware revision; no source-backed installed value | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Obtain microcontroller identity; no fingerprint retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve active Modules/Objects independently of candidate metadata | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Corroborate installed addressing and distinguish physical from reusable ranges | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Compare installed configuration with the exact firmware/Object restrictions | [Configuration](../../diagnostics/dim35-configuration.md) |

These are catalogue-derived diagnostic candidates. No Device-specific response or support across all commercial variants is established by a hardware capture.

## Functional applicability

| Role | Source-scoped applicability | Canonical evidence / reference |
| --- | --- | --- |
| Lighting | Published one/two functions; exact catalogue Object `434` with firmware restrictions | [`WHO 1`](../../functional/who-1-lighting/) |
| LED brightness | Object `148`; configurable default/max level and retained power-save setting | Exact sheet; catalogue domains |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Plan the frame, box/support and normal `K8001` connection before fitting the control. Follow the published mounting sequence: support and connection/actuator devices, electrified frame, then digital controls or blanking modules. The source shows how to remove/reposition a control from the frame and says its configured function is retained on moving. The complete dismantling/reset/update procedure and replacement behavior are not established by these source pages. Do not infer a factory reset from physical removal.

Use the configuration method appropriate to the source/system revision: MyHOME_Up or MyHOME_Suite in the exact sheets; Home+Project in the `6/2025` guide. Associate each actual function with its external actuator and required address scope; symbols do not identify a built-in power output. Published group/general control differs from point-to-point feedback. Compare the actual installed firmware/Object with the catalogue tables before prescribing writes.

Configure one central function or two separate top/bottom functions as published. Reusable Object `434` lists cyclical, `OFF`, `ON`, `PUL` and extended timed-`ON` modes. However, firmware `803` filter `3835` permits only `2` `ON` without regulation, excluding reusable default `0`. This directly conflicts with broader published functions and has no replacement default or selection rule; do not silently loosen the filter to match the sheet. Object `148` brightness is its own Module and does not create a third light function.

## Source reconciliation

All exact colour variants and the retained sheet/export revisions are accounted for separately. Device-specific physical/function facts, touch mappings, source-defined configuration methods and mounting composition are incorporated above; unrelated gateway/actuator chapters of the system guide do not become specifications of this control. The DAR underscore filename for the sheet returns byte-identical data to the assets hyphen filename and supplies no additional revision. The catalogue/guide identity lists corroborate marketed Living Now and colour scope, while the original catalogue implementation remains a separate historical capability source.

| Issue | Reconciliation / unresolved limit | Evidence |
| --- | --- | --- |
| Physical/logical count | One physical digital position; three logical Modules: two commands and brightness | Exact sheet vs firmware topology |
| Source chronology | The technical guide’s URL directory says 2024-02 but the retained original rear cover says `AD-EXMH25GT`, version `6/2025`; catalogue rear cover is `01/2025` | Printed original labels; no date inferred from URL |
| Temperature | Sheet operating upper bound `40 °C`, current export operating/setting upper bound `45 °C`; no hardware-revision explanation | Sheet p. 1; exact exports p. 3 |
| Power scope | Sheet maximum `6 mA` differs in scope from export standby KW/KM/KG `3.5/3.5/3.8 mA`; no contradiction inferred between maximum and standby | Sheet p. 1; exact colour exports p. 3 |
| Colour naming | KM = sand in guide/catalogue and Beige in exact export; catalogue item’s white label does not describe all variants | Exact reference/colour lists and individual exports |
| Configuration tools | 2020 sheet Up/Suite ; 2025 guide Home+Project. No universal app/gateway support inferred | Exact source revisions |
| Frame mounting terminology | Sheet says surface-mounted one-module control, export says flush-mounted; guide shows digital control on front of electrified frame over a flush box | Sheet p. 1; export p. 3; guide pp. 50-53 |
| Digital transport | SCS contact supply/connection is established; exported voice/internet/interoperability attributes describe a system capability, not a native microphone, radio or direct IP socket | Exports pp. 3-4; guide distinguishes separate voice control |
| Virgin membership | Virgin `521` generic allowed list is different from direct Objects of firmware `803`; no automatic conversion is established | Exact catalogue relations |
| Mode restriction conflict | Firmware `803` MODE subset only `2` `ON`, while generic default `0` and published cyclical/`OFF`/`PUL`/timed functions lie outside it | Filter `3835`; exact sheet p. 1 |
| Front-position illustration | Sheet labels three possible touch locations but publishes at most two functions; current export lists two actuation points/buttons | Sheet illustration/function legend; export p. 3 |

## Evidence limits and open work

- Reconcile published functions with the exact firmware filter/default restrictions through accepted software/hardware configuration; no firmware parameter-file association is stored.
- Establish the temperature differences, revision applicability, complete reset/update/replacement procedures and app/gateway prerequisites.
- Corroborate active Modules/Objects, Virgin transitions, installed firmware/build, hardware/MCU revisions and source-defined behavior using sanitized captures.
- Confirm both command positions, point-to-point versus group/general feedback, timed-off behavior and separate brightness/power-save settings.

Publisher-linked `BRO-LNOW2M`, `BRO-LNOW3M`, `CAT-LNOW2M` and other Living Now catalogue/brochure editions have not all been independently examined. Only the retained revisions and page scopes listed in Documentation support claims here; linked inventory is not evidence of every edition’s contents.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- `KW8010-publisher-product-sheet.pdf`, printed/PDF p. 1: exact `KW8010` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/88/ca/88ca328656a25c613079ee74ad293d6ae1be4b0c06a970fb9be1f89e730c3af1.pdf); [publisher source](https://www.bticino.com/products/pdf?sku=BT-KW8010&include_technical=1); SHA-256 `88ca328656a25c613079ee74ad293d6ae1be4b0c06a970fb9be1f89e730c3af1`.
- `KM8010-publisher-product-sheet.pdf`, printed/PDF p. 1: exact `KM8010` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/da/24/da2404125a548a616b6b5f4314e5268be741b72c6e65f485c075edf18ca4d71d.pdf); [publisher source](https://www.bticino.com/products/pdf?sku=BT-KM8010&include_technical=1); SHA-256 `da2404125a548a616b6b5f4314e5268be741b72c6e65f485c075edf18ca4d71d`.
- `KG8010-publisher-product-sheet.pdf`, printed/PDF p. 1: exact `KG8010` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/2f/9b/2f9b4480ea05ad1e53f34957ccf13c60771e818307ab2af87c7907b6d4d3bd2f.pdf); [publisher source](https://www.bticino.com/products/pdf?sku=BT-KG8010&include_technical=1); SHA-256 `2f9b4480ea05ad1e53f34957ccf13c60771e818307ab2af87c7907b6d4d3bd2f`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0111-0120-2026-10-06.md#own-dev-0114)
