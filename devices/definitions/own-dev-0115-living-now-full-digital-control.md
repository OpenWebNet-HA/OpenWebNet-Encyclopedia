# Living Now FULL digital control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0115` | Project identity |
| Technical description | Living Now FULL digital control | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `KW8011`, `KM8011`, `KG8011` | All three catalogue commercial records; confidence scoped below |
| Catalogue item | `2273` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `119` | Main association; independent of project ID |
| Firmware definition | `804` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `5` | Firmware metadata |
| Categories | Commands, Scenarios, User interfaces, Audio video, Multifunction devices | Source-derived roles |

The exact manufacturer sheet and reference lists establish all three Living Now colour variants. This is one physical digital control mounted on an electrified frame, distinct from the catalogue’s logical Module count. One to three single-slot functions, or one three-slot dimmer/shutter/player role, share three touch areas; the fourth and fifth logical Modules handle icon/proximity settings and brightness.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Living Now | `KW8011` | Established commercial variant | Catalogue record `2630`; published family/variant scope reconciled below |
| BTicino - Living Now | `KM8011` | Established commercial variant | Catalogue record `2631`; published family/variant scope reconciled below |
| BTicino - Living Now | `KG8011` | Established commercial variant | Catalogue record `2632`; published family/variant scope reconciled below |

The exact technical sheet names `KW8011`, `KM8011` and `KG8011` together; the retained guide/catalogue lists establish white, sand and black. Individual publisher exports independently identify Living Now, with the KM colour attribute labelled Beige and the catalogue labelled sand. The canonical commercial descriptions distinguish colours even though the technical item/name contains “white”; that source label does not make all variants white. EAN and commercial identity do not establish installed firmware. All three variant exports are retained separately.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ST-00000784-EN.pdf` | English FULL technical sheet | `ST-00000784-EN; 14/10/2020` | KW/KM/KG8011: variant-dependent current, layout, icons and app/Suite setup p. 1; complete function/touch-area/slot mapping p. 2. Printed/PDF pp. 1-2 coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/18/8f/188f03e3a7030800cfafc12baa7b8250d40f25d96459736b0a5a766c44314170.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00000784-EN.pdf) |
| `KW8011-publisher-product-sheet.pdf` | English publisher product export | `DATASHEET; 03.10.2026` | KW8011 only: identity, line, colour and descriptive capability pp. 1-2; physical/technical attributes pp. 3-4; publisher document inventory p. 5. Printed/PDF pages coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/f1/65/f165fe498237036b996aa2a26a4353ff453a63700f162f966896b0e154bc3ac8.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-KW8011&include_technical=1) |
| `KM8011-publisher-product-sheet.pdf` | English publisher product export | `DATASHEET; 03.10.2026` | KM8011 only: identity, line, colour and descriptive capability pp. 1-2; physical/technical attributes pp. 3-4; publisher document inventory p. 5. Printed/PDF pages coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/5e/b9/5eb9686b608f8c10b7dac16da159c687a4fc5a94a544eb29fe06301e6de99ac3.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-KM8011&include_technical=1) |
| `KG8011-publisher-product-sheet.pdf` | English publisher product export | `DATASHEET; 03.10.2026` | KG8011 only: identity, line, colour and descriptive capability pp. 1-2; physical/technical attributes pp. 3-4; publisher document inventory p. 5. Printed/PDF pages coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/ee/25/ee25e66076affa4298dd914aeb190be60700291084bcb7662dbcab03714f1ebc.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-KG8011&include_technical=1) |
| `KW8011-italian-product-sheet.pdf` | Italian publisher product export | `Price-list validity 01/07/2026; retrieved 03/10/2026` | KW8011 only: exact name, line, supply/current/module attribute and EAN p. 1; compatible parts on following pages. Printed/PDF pages coincide. Prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/26/47/26477524059892ef8e1fc9aaba0edae34bfba6ce4e9ef9357e64a22aa8603c56.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-KW8011) |
| `MyHOME-Technical-Guide.pdf` | English system technical guide | `AD-EXMH25GT; Versione 6/2025 printed on rear cover; URL directory is older` | Digital-control customisation, construction, mounting, Home+Project, frame/box composition and exact colour/reference lists: printed pp. 22, 50-53, 84-85 / PDF pp. 22, 50-53, 84-85. Printed edition confirmed on rear cover. | [Archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) | [Publisher original](https://www.bticino.com/sites/default/files/2024-02/MyHOME%20Technical%20Guide.pdf) |
| `Living-Now-2025-3M-catalogue.pdf` | English Living Now catalogue | `AD-EXLNW25C/GB; Edition 01/2025 printed on rear cover` | KW/KG/KM8010 and 8011 exact family/colour descriptions, functions and frame/connection compatibility printed p. 103 / PDF p. 103. The original contains the complete 144-page catalogue. | [Archived original](https://archive.openwebnet-ha.org/sha256/e3/15/e3153d42a54335de37d0ca05b7f696b3345bf2743ebe2ec78e32a1cb7ee5f47e.pdf) | [Publisher original](https://www.bticino.com/sites/default/files/2024-12/GB%20Living%20NOW%20catalogue%203%20MODULES%202025.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2273`: all firmware/commercial/system/Object/Module/Virgin/field/filter/mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `18..27 Vdc`; SCS through four frame contact clips | `ST-00000784-EN` p. 1 |
| Sizing current by variant | Standby `9 mA`; maximum/sizing: KW `12 mA`, KM `15 mA`, KG `25 mA` | Exact sheet p. 1: maximum calculated for a typical system |
| Current-export standby by variant | KW `6 mA`, KM `6 mA`, KG `6.2 mA` | Each exact export p. 3; differs from sheet standby `9 mA` |
| Italian KW catalogue attribute | Supply `27 Vdc`; current `12 mA`; one module | Italian KW8011 export p. 1; current is not labelled standby |
| Local controls/indication | Three capacitive touch areas, configurable LED icon matrices and proximity sensor | Exact sheet p. 1; configured icons appear on approach even if LEDs were otherwise off |
| Physical format | One digital position, described as one-module surface mounting; supported by an electrified frame | `ST-00000784-EN` p. 1; MyHOME guide pp. 50-53 |
| Operating temperature by source | Sheet `5..40 °C`; current exports `5..45 °C` | `ST-00000784-EN` p. 1; each export p. 3; unresolved upper-bound difference |
| Current-export metric size | `40 x 86 x 6 mm`; built-in depth `2 mm`; minimum box depth `40 mm` | All three colour exports p. 3; scope is product attributes, separate from frame/box assembly |
| Current-export storage/protection | `-10..70 °C`, `IP20`; IK not applicable | All three colour exports p. 3 |
| Materials/finish | Matt untreated thermoplastic; white / Beige / black; not transparent | Exact colour exports p. 3 |
| Connection mechanism | Four clips / SCS contact points; no per-control parallel BUS wiring needed when using electrified frame | `ST-00000784-EN` p. 1; guide p. 51 |
| Publisher terminal attributes | Capacity `1..1 mm²`, flexible or rigid wire; terminal marking No | Exports p. 4; attributes do not turn frame contacts into a conventional direct wiring diagram |
| Published standards | `EN50491`; `EN60669-2-5` | `ST-00000784-EN` p. 1 |
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
| `EN_ITEM.id_item` | `2273` | Canonical catalogue |
| Technical item description | Adv - command advanced white | Canonical catalogue |
| Item family | 0; key `1` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `119` | `AS_ITEM_SYSTEM` |
| Commercial record count | `3` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `804` | `1` | `0` | No build row | `5` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `804` | `1` | `416` Scheduled scenario PLUS | Candidate alternative | `3352` | `416` | `1624` |
| `804` | `1` | `463` Load control actuator visualization | Candidate alternative | `3346` | `492` | `1622` |
| `804` | `1` | `434` Simplified Light single control basic | Fixed/designated metadata | `3361` | `652` | `1629` |
| `804` | `1` | `436` Dimmer Command 3 Keys | Candidate alternative | `3360` | `656` | `1628` |
| `804` | `1` | `437` Simplified Shutter control 3 slots | Candidate alternative | `3345` | `659` | `1621` |
| `804` | `1` | `438` Player command 3 slots | Candidate alternative | `3417` | `660` | `1671` |
| `804` | `2` | `416` Scheduled scenario PLUS | Candidate alternative | `3353` | `416` | `1624` |
| `804` | `2` | `463` Load control actuator visualization | Candidate alternative | `3347` | `492` | `1622` |
| `804` | `2` | `434` Simplified Light single control basic | Fixed/designated metadata | `3362` | `652` | `1629` |
| `804` | `3` | `416` Scheduled scenario PLUS | Candidate alternative | `3354` | `416` | `1624` |
| `804` | `3` | `463` Load control actuator visualization | Candidate alternative | `3348` | `492` | `1622` |
| `804` | `3` | `434` Simplified Light single control basic | Fixed/designated metadata | `3363` | `652` | `1629` |
| `804` | `4` | `147` User interface settings for symbol management with led matrix | Fixed/designated metadata | `3356` | `655` | `1626` |
| `804` | `5` | `148` Led Brightness Settings | Fixed/designated metadata | `3355` | `657` | `1625` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `804` | `521` Soft-Touch command virgin | `1`, `2`, `3` | `410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `418`, `419`, `421`, `426`, `427`, `462` | `521` | `141` |

Command slots `1/2/3` each permit single-slot Objects `434`, `416` and `463`. Three-slot Objects `436` (dimmer), `437` (shutter) and `438` (player) have stored starting placement `1` only; they occupy a different role configuration from three independent single-slot commands. Object `147` is in slot `4`; Object `148` in slot `5`. Virgin Object `521` covers only command slots `1/2/3` and lists generic Objects `410..419`, `421`, `426`, `427`, `462`. Those are different from this firmware’s direct membership. No conversion or slot predicate establishes when or how they become active; the generic Virgin list must not enlarge published Device capability. Multi-slot candidates do not create extra stored placements in their covered slots.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `804` | Advanced Configuration | `2` | Association key `2` |


No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

The exact 2020 sheet names MyHOME_Up and MyHOME_Suite. Its description also names Digital Controls for function/icon/brightness customisation; load-control configuration is explicitly MyHOME_Suite only in that revision. The retained `6/2025` system guide names Home+Project for function assignment, associated actuators and icon configuration. These are source/revision-specific workflows. The catalogue mode and connection associations above remain the implementation snapshot; no installed gateway/app/firmware compatibility is inferred from current app names. No published physical configurator setup is documented for this digital contact-mounted control.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `804` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `416` - Scheduled scenario PLUS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | `0..255` | `1` | Scheduled scenario PLUS number |
| `PPT_CEN_HIG` | `0..7` | `0` | Scheduled scenario PLUS number |
| `BUTTON_1` | `0..31` | `1` | Button |
| `MODE` | `0` = Press/release only; `1` = Press/hold/release | `0` | Modality; Mode (Lighting management) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |


### Object `463` - Load control actuator visualization

Catalogue Object key `492` maps to external Object `463`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PRIORITY` | `0..63` | `1` | Priority |
| `PHASE` | `0` = Single phase; `1` = Phase 1; `2` = Phase 2; `3` = Phase 3 | `0` | Phase |


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


### Object `147` - User interface settings for symbol management with led matrix

Catalogue Object key `655` maps to external Object `147`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `FIRST_LINE_SYMBOL_1_ICON_1` | `0..63` | `0` | First line (5 leds) of symbol 1 for led matrix 1 |
| `SECOND_LINE_SYMBOL_1_ICON_1` | `0..31` | `0` | Second line (5 leds) of symbol 1 for led matrix 1 |
| `THIRD_LINE_SYMBOL_1_ICON_1` | `0..31` | `0` | Third line (5 leds) of symbol 1 for led matrix 1 |
| `FOURTH_LINE_SYMBOL_1_ICON_1` | `0..31` | `0` | Fourth line (5 leds) of symbol 1 for led matrix 1 |
| `FIFTH_LINE_SYMBOL_1_ICON_1` | `0..31` | `0` | Fifth line (5 leds) of symbol 1 for led matrix 1 |
| `FIRST_LINE_SYMBOL_2_ICON_1` | `0..31` | `0` | First line (5 leds) of symbol 2 for led matrix 1 |
| `SECOND_LINE_SYMBOL_2_ICON_1` | `0..31` | `0` | Second line (5 leds) of symbol 2 for led matrix 1 |
| `THIRD_LINE_SYMBOL_2_ICON_1` | `0..31` | `0` | Third line (5 leds) of symbol 2 for led matrix 1 |
| `FOURTH_LINE_SYMBOL_2_ICON_1` | `0..31` | `0` | Fourth line (5 leds) of symbol 2 for led matrix 1 |
| `FIFTH_LINE_SYMBOL_2_ICON_1` | `0..31` | `0` | Fifth line (5 leds) of symbol 2 for led matrix 1 |
| `FIRST_LINE_SYMBOL_3_ICON_1` | `0..31` | `0` | First line (5 leds) of symbol 3 for led matrix 1 |
| `SECOND_LINE_SYMBOL_3_ICON_1` | `0..31` | `0` | Second line (5 leds) of symbol 3 for led matrix 1 |
| `THIRD_LINE_SYMBOL_3_ICON_1` | `0..31` | `0` | Third line (5 leds) of symbol 3 for led matrix 1 |
| `FOURTH_LINE_SYMBOL_3_ICON_1` | `0..31` | `0` | Fourth line (5 leds) of symbol 3 for led matrix 1 |
| `FIFTH_LINE_SYMBOL_3_ICON_1` | `0..31` | `0` | Fifth line (5 leds) of symbol 3 for led matrix 1 |
| `FIRST_LINE_SYMBOL_4_ICON_1` | `0..31` | `0` | First line (5 leds) of symbol 4 for led matrix 1 |
| `SECOND_LINE_SYMBOL_4_ICON_1` | `0..31` | `0` | Second line (5 leds) of symbol 4 for led matrix 1 |
| `THIRD_LINE_SYMBOL_4_ICON_1` | `0..31` | `0` | Third line (5 leds) of symbol 4 for led matrix 1 |
| `FOURTH_LINE_SYMBOL_4_ICON_1` | `0..31` | `0` | Fourth line (5 leds) of symbol 4 for led matrix 1 |
| `FIFTH_LINE_SYMBOL_4_ICON_1` | `0..31` | `0` | Fifth line (5 leds) of symbol 4 for led matrix 1 |
| `FIRST_LINE_SYMBOL_5_ICON_1` | `0..31` | `0` | First line (5 leds) of symbol 5 for led matrix 1 |
| `SECOND_LINE_SYMBOL_5_ICON_1` | `0..31` | `0` | Second line (5 leds) of symbol 5 for led matrix 1 |
| `THIRD_LINE_SYMBOL_5_ICON_1` | `0..31` | `0` | Third line (5 leds) of symbol 5 for led matrix 1 |
| `FOURTH_LINE_SYMBOL_5_ICON_1` | `0..31` | `0` | Fourth line (5 leds) of symbol 5 for led matrix 1 |
| `FIFTH_LINE_SYMBOL_5_ICON_1` | `0..31` | `0` | Fifth line (5 leds) of symbol 5 for led matrix 1 |
| `NUM_SYMBOLS_ANIMATION_ICON_1` | `1..5` | `1` | Number of symbol to use for animated Led Matrix 1 |
| `INTERSYMBOL_TIME_ANIMATION_ICON_1` | `0` = Very Fast; `1` = Fast; `2` = Normal; `3` = Slow; `4` = Very Slow | `2` | Intersymbol time for animated Led Matrix1 |
| `FIRST_LINE_SYMBOL_1_ICON_2` | `0..63` | `0` | First line (5 leds) of symbol 1 for led matrix 2 |
| `SECOND_LINE_SYMBOL_1_ICON_2` | `0..31` | `0` | Second line (5 leds) of symbol 1 for led matrix 2 |
| `THIRD_LINE_SYMBOL_1_ICON_2` | `0..31` | `0` | Third line (5 leds) of symbol 1 for led matrix 2 |
| `FOURTH_LINE_SYMBOL_1_ICON_2` | `0..31` | `0` | Fourth line (5 leds) of symbol 1 for led matrix 2 |
| `FIFTH_LINE_SYMBOL_1_ICON_2` | `0..31` | `0` | Fifth line (5 leds) of symbol 1 for led matrix 2 |
| `FIRST_LINE_SYMBOL_2_ICON_2` | `0..31` | `0` | First line (5 leds) of symbol 2 for led matrix 2 |
| `SECOND_LINE_SYMBOL_2_ICON_2` | `0..31` | `0` | Second line (5 leds) of symbol 2 for led matrix 2 |
| `THIRD_LINE_SYMBOL_2_ICON_2` | `0..31` | `0` | Third line (5 leds) of symbol 2 for led matrix 2 |
| `FOURTH_LINE_SYMBOL_2_ICON_2` | `0..31` | `0` | Fourth line (5 leds) of symbol 2 for led matrix 2 |
| `FIFTH_LINE_SYMBOL_2_ICON_2` | `0..31` | `0` | Fifth line (5 leds) of symbol 2 for led matrix 2 |
| `FIRST_LINE_SYMBOL_3_ICON_2` | `0..31` | `0` | First line (5 leds) of symbol 3 for led matrix 2 |
| `SECOND_LINE_SYMBOL_3_ICON_2` | `0..31` | `0` | Second line (5 leds) of symbol 3 for led matrix 2 |
| `THIRD_LINE_SYMBOL_3_ICON_2` | `0..31` | `0` | Third line (5 leds) of symbol 3 for led matrix 2 |
| `FOURTH_LINE_SYMBOL_3_ICON_2` | `0..31` | `0` | Fourth line (5 leds) of symbol 3 for led matrix 2 |
| `FIFTH_LINE_SYMBOL_3_ICON_2` | `0..31` | `0` | Fifth line (5 leds) of symbol 3 for led matrix 2 |
| `FIRST_LINE_SYMBOL_4_ICON_2` | `0..31` | `0` | First line (5 leds) of symbol 4 for led matrix 2 |
| `SECOND_LINE_SYMBOL_4_ICON_2` | `0..31` | `0` | Second line (5 leds) of symbol 4 for led matrix 2 |
| `THIRD_LINE_SYMBOL_4_ICON_2` | `0..31` | `0` | Third line (5 leds) of symbol 4 for led matrix 2 |
| `FOURTH_LINE_SYMBOL_4_ICON_2` | `0..31` | `0` | Fourth line (5 leds) of symbol 4 for led matrix 2 |
| `FIFTH_LINE_SYMBOL_4_ICON_2` | `0..31` | `0` | Fifth line (5 leds) of symbol 4 for led matrix 2 |
| `FIRST_LINE_SYMBOL_5_ICON_2` | `0..31` | `0` | First line (5 leds) of symbol 5 for led matrix 2 |
| `SECOND_LINE_SYMBOL_5_ICON_2` | `0..31` | `0` | Second line (5 leds) of symbol 5 for led matrix 2 |
| `THIRD_LINE_SYMBOL_5_ICON_2` | `0..31` | `0` | Third line (5 leds) of symbol 5 for led matrix 2 |
| `FOURTH_LINE_SYMBOL_5_ICON_2` | `0..31` | `0` | Fourth line (5 leds) of symbol 5 for led matrix 2 |
| `FIFTH_LINE_SYMBOL_5_ICON_2` | `0..31` | `0` | Fifth line (5 leds) of symbol 5 for led matrix 2 |
| `NUM_SYMBOLS_ANIMATION_ICON_2` | `1..5` | `1` | Number of symbol to use for animated Led Matrix 2 |
| `INTERSYMBOL_TIME_ANIMATION_ICON_2` | `0` = Very Fast; `1` = Fast; `2` = Normal; `3` = Slow; `4` = Very Slow | `2` | Intersymbol time for animated Led Matrix 2 |
| `FIRST_LINE_SYMBOL_1_ICON_3` | `0..63` | `0` | First line (5 leds) of symbol 1 for led matrix 3 |
| `SECOND_LINE_SYMBOL_1_ICON_3` | `0..31` | `0` | Second line (5 leds) of symbol 1 for led matrix 3 |
| `THIRD_LINE_SYMBOL_1_ICON_3` | `0..31` | `0` | Third line (5 leds) of symbol 1 for led matrix 3 |
| `FOURTH_LINE_SYMBOL_1_ICON_3` | `0..31` | `0` | Fourth line (5 leds) of symbol 1 for led matrix 3 |
| `FIFTH_LINE_SYMBOL_1_ICON_3` | `0..31` | `0` | Fifth line (5 leds) of symbol 1 for led matrix 3 |
| `FIRST_LINE_SYMBOL_2_ICON_3` | `0..31` | `0` | First line (5 leds) of symbol 2 for led matrix 3 |
| `SECOND_LINE_SYMBOL_2_ICON_3` | `0..31` | `0` | Second line (5 leds) of symbol 2 for led matrix 3 |
| `THIRD_LINE_SYMBOL_2_ICON_3` | `0..31` | `0` | Third line (5 leds) of symbol 2 for led matrix 3 |
| `FOURTH_LINE_SYMBOL_2_ICON_3` | `0..31` | `0` | Fourth line (5 leds) of symbol 2 for led matrix 3 |
| `FIFTH_LINE_SYMBOL_2_ICON_3` | `0..31` | `0` | Fifth line (5 leds) of symbol 2 for led matrix 3 |
| `FIRST_LINE_SYMBOL_3_ICON_3` | `0..31` | `0` | First line (5 leds) of symbol 3 for led matrix 3 |
| `SECOND_LINE_SYMBOL_3_ICON_3` | `0..31` | `0` | Second line (5 leds) of symbol 3 for led matrix 3 |
| `THIRD_LINE_SYMBOL_3_ICON_3` | `0..31` | `0` | Third line (5 leds) of symbol 3 for led matrix 3 |
| `FOURTH_LINE_SYMBOL_3_ICON_3` | `0..31` | `0` | Fourth line (5 leds) of symbol 3 for led matrix 3 |
| `FIFTH_LINE_SYMBOL_3_ICON_3` | `0..31` | `0` | Fifth line (5 leds) of symbol 3 for led matrix 3 |
| `FIRST_LINE_SYMBOL_4_ICON_3` | `0..31` | `0` | First line (5 leds) of symbol 4 for led matrix 3 |
| `SECOND_LINE_SYMBOL_4_ICON_3` | `0..31` | `0` | Second line (5 leds) of symbol 4 for led matrix 3 |
| `THIRD_LINE_SYMBOL_4_ICON_3` | `0..31` | `0` | Third line (5 leds) of symbol 4 for led matrix 3 |
| `FOURTH_LINE_SYMBOL_4_ICON_3` | `0..31` | `0` | Fourth line (5 leds) of symbol 4 for led matrix 3 |
| `FIFTH_LINE_SYMBOL_4_ICON_3` | `0..31` | `0` | Fifth line (5 leds) of symbol 4 for led matrix 3 |
| `FIRST_LINE_SYMBOL_5_ICON_3` | `0..31` | `0` | First line (5 leds) of symbol 5 for led matrix 3 |
| `SECOND_LINE_SYMBOL_5_ICON_3` | `0..31` | `0` | Second line (5 leds) of symbol 5 for led matrix 3 |
| `THIRD_LINE_SYMBOL_5_ICON_3` | `0..31` | `0` | Third line (5 leds) of symbol 5 for led matrix 3 |
| `FOURTH_LINE_SYMBOL_5_ICON_3` | `0..31` | `0` | Fourth line (5 leds) of symbol 5 for led matrix 3 |
| `FIFTH_LINE_SYMBOL_5_ICON_3` | `0..31` | `0` | Fifth line (5 leds) of symbol 5 for led matrix 3 |
| `NUM_SYMBOLS_ANIMATION_ICON_3` | `1..5` | `1` | Number of symbol to use for animated Led Matrix 3 |
| `INTERSYMBOL_TIME_ANIMATION_ICON_3` | `0` = Very Fast; `1` = Fast; `2` = Normal; `3` = Slow; `4` = Very Slow | `2` | Intersymbol time for animated Led Matrix 3 |
| `PROXIMITY_DISTANCE` | `0` = Proximity disabled; `1` = Minimum distance; `2` = Medium distance; `3` = Maximum distance | `3` | Proximity distance |
| `BEHAVIOUR_WITH_PROXY_DISABLED` | `0` = Icons `ON` only on touch; `1` = Icons always `ON` | `0` | Behaviour with proximity disabled |
| `LED_IN_STANDBY_OFF` | `0` = NO; `1` = YES | `0` | Led in Stand-by `OFF` |


### Object `436` - Dimmer Command 3 Keys

Catalogue Object key `656` maps to external Object `436`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `COLOR_SET` | `0` = NO; `1` = YES | `0` | Color set; If value = YES, the `ON`/`OFF` key also set the colour of colored lamp |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `G` | `0..255` | `1` | Main Group (`GR`/GS) |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `1` | Light point |
| `LEVEL` | `0..100` | `100` | Level |
| `START_S` | `0..255` | `255` | Soft start speed |
| `STOP_S` | `0..255` | `255` | Soft stop speed |
| `DIMMING_S` | `0..255` | `255` | Dimming speed |
| `HUE_COLOR_LOW_8_BITS_FIRST` | `0..255` | `0` | Hue (low 8 bits) first colour; Hue (high 1 bit) first colour = 1, range 01…67 |
| `HUE_HIGH_1_BIT_FIRST` | `0..1` | `0` | Hue (high 1 bit) first colour |
| `SATURATION_FIRST` | `0..100` | `0` | Saturation first colour |
| `VALUE_FIRST` | `0..100` | `100` | Value first colour |
| `HUE_COLOR_LOW_8_BITS_SECOND` | `0..255` | `0` | Hue (low 8 bits) second colour; Hue (high 1 bit) second colour = 1, range 01…67 |
| `HUE_HIGH_1_BIT_SECOND` | `0..1` | `0` | Hue (high 1 bit) second colour |
| `SATURATION_SECOND` | `0..100` | `100` | Saturation second colour |
| `VALUE_SECOND` | `0..100` | `100` | Value second colour |
| `HUE_COLOR_LOW_8_BITS_THIRD` | `0..255` | `60` | Hue (low 8 bits) third colour; Hue (high 1 bit) third colour = 1, range 01…67 |
| `HUE_HIGH_1_BIT_THIRD` | `0..1` | `0` | Hue (high 1 bit) third colour |
| `SATURATION_THIRD` | `0..100` | `100` | Saturation third colour |
| `VALUE_THIRD` | `0..100` | `100` | Value third colour |
| `HUE_COLOR_LOW_8_BITS_FOURTH` | `0..255` | `120` | Hue (low 8 bits) fourth colour; Hue (high 1 bit) fourth colour = 1, range 01…67 |
| `HUE_HIGH_1_BIT_FOURTH` | `0..1` | `0` | Hue (high 1 bit) fourth colour |
| `SATURATION_FOURTH` | `0..100` | `100` | Saturation fourth colour |
| `VALUE_FOURTH` | `0..100` | `100` | Value fourth colour |
| `HUE_COLOR_LOW_8_BITS_FIFTH` | `0..255` | `240` | Hue (low 8 bits) fifth colour; Hue (high 1 bit) fourth colour = 1, range 01…67 |
| `HUE_HIGH_1_BIT_FIFTH` | `0..1` | `0` | Hue (high 1 bit) fifth colour |
| `SATURATION_FIFTH` | `0..100` | `100` | Saturation fifth colour |
| `VALUE_FIFTH` | `0..100` | `100` | Value fifth colour |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |


### Object `148` - Led Brightness Settings

Catalogue Object key `657` maps to external Object `148`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LED_BRIGHTNESS_LEVEL` | `0` = Min; `1` = Max | `0` | Led brightness level |
| `LED_OFF_FOR_POWER_SAVE` | `0` = NO; `1` = YES | `0` | Led `OFF` for power save |
| `G` | `0..255` | `0` | Main Group (`GR`/GS) |


### Object `437` - Simplified Shutter control 3 slots

Catalogue Object key `659` maps to external Object `437`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Bistable control; `1` = Monostable control; `2` = Blades control and bistable; `3` = Bistable and blades control | `1` | Modality |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `1` | Light point |
| `G` | `0..255` | `0` | Main Group (`GR`/GS) |
| `POSITION_CONTROL` | `0` = NO; `1` = YES | `0` | Position control |
| `PRESET_NUMBER` | `1..10`; `0` = None | `0` | Preset; Shutter management preset number |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |


### Object `438` - Player command 3 slots

Catalogue Object key `660` maps to external Object `438`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | `0` = Point to point; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..14` | `0` | Area |
| `PF` | `0..255` | `0` | Audio point |
| `CHANNEL` | `0` = Base Band; `1` = Left; `2` = Right; `3` = Stereo; `8` = Base Band and Video; `9` = Left and video; `10` = Right and video; `11` = Stereo and Video | `3` | Channel (BB-Stereo) |

### Published function and touch-area mapping

| Function | Published occupancy | Control behavior | Evidence |
| --- | --- | --- | --- |
| Cyclical light | One function position | Touch alternates `ON/OFF`; non-point-to-point configuration has no state return and alternates transmitted commands | `ST-00000784-EN` p. 2 |
| `OFF`-only | One function position | Only `OFF` transmitted | `ST-00000784-EN` p. 2 |
| Pushbutton | One function position | Published `PUL` mode | `ST-00000784-EN` p. 2 |
| Timed `ON` | One function position | Published sheet says the switch-off command follows the configured interval; exact parameters determine duration | `ST-00000784-EN` p. 2 |
| Dimmer | All three command slots | Top brightens; bottom dims; centre toggles. Configured long centre press cycles RGB colour | Exact sheet p. 2; Object `436` |
| Shutter | All three command slots | Top up, bottom down, centre stop; configured position management also allows centre preset | Exact sheet p. 2; Object `437` |
| NUVO Player | All three command slots | Top volume up, bottom down; short centre play/pause; long centre track forward | Exact sheet p. 2; Object `438` |
| `CEN` PLUS | One command slot per assigned scenario | Each touch area activates its corresponding scenario number | Exact sheet p. 2; Object `416` |
| Load control | One command slot per assigned role | Display enabled/disabled/overridden state; force or remove forcing; requires external load-control system | Exact sheet pp. 1-2; Object `463` |
| Brightness | UI settings | Configured LEDs can use default or maximum level; default level is not numerically specified | `ST-00000784-EN` p. 2 |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `804` | `416` | `3842` | `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed (entire reusable range retained) | `0` | Contact type |
| `804` | `434` | `3861` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `804` | `434` | `3864` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `804` | `147` | `3852` | `FIRST_LINE_SYMBOL_1_ICON_3` | `32..63` | `0` | First line (5 leds) of symbol 1 for led matrix 3; reusable default `0` is outside this subset; filter supplies no replacement default |
| `804` | `147` | `3853` | `FIRST_LINE_SYMBOL_1_ICON_2` | `32..63` | `0` | First line (5 leds) of symbol 1 for led matrix 2; reusable default `0` is outside this subset; filter supplies no replacement default |
| `804` | `147` | `3854` | `FIRST_LINE_SYMBOL_1_ICON_1` | `32..63` | `0` | First line (5 leds) of symbol 1 for led matrix 1; reusable default `0` is outside this subset; filter supplies no replacement default |
| `804` | `436` | `3858` | `COLOR_SET` | `1` = YES | `0` | Color set; reusable default `0` is outside this subset; filter supplies no replacement default |
| `804` | `436` | `3865` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `804` | `436` | `3866` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `804` | `148` | `3857` | `LED_OFF_FOR_POWER_SAVE` | `0` = NO; `1` = YES (entire reusable range retained) | `0` | Led `OFF` for power save |
| `804` | `437` | `3843` | `ADDR_TYPE` | `1` = Area | `0` | Addressing type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `804` | `437` | `3867` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `804` | `437` | `3868` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion reference is attached to these slot rows. Resolve the active Object and apply its firmware-specific domain restrictions separately. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `119` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| Lighting/dimming/colour | Single-slot Object `434` or three-slot Object `436`; configured RGB long-press and exact COLOR_SET restriction | [`WHO 1`](../../functional/who-1-lighting/) |
| Shutter | Three-slot Object `437`; external actuator; up/down/stop/preset only as configured | [`WHO 2`](../../functional/who-2-automation/) |
| Scenarios | Single-slot Object `416`; scenario number/button and contact mode domains | [CEN+ in `WHO 25`](../../functional/who-25-transversal/cen-plus.md) |
| Load control | Single-slot Object `463`; status/override requires external load control | [`WHO 18`](../../functional/who-18-energy-management/) |
| NUVO Player | Three-slot Object `438`; playback/volume/track controls require compatible player/system | [Functional Protocol](../../functional/); exact NUVO transport/WHO applicability uncorroborated |
| Icon/proximity/brightness | Separate Objects `147/148`; physical proximity is established by exact sheet; installed encoding remains unobserved | Exact sheet pp. 1-2; complete catalogue matrix fields above |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Plan the frame, box/support and normal `K8001` connection before fitting the control. Follow the published mounting sequence: support and connection/actuator devices, electrified frame, then digital controls or blanking modules. The source shows how to remove/reposition a control from the frame and says its configured function is retained on moving. The complete dismantling/reset/update procedure and replacement behavior are not established by these source pages. Do not infer a factory reset from physical removal.

Use the configuration method appropriate to the source/system revision: MyHOME_Up or MyHOME_Suite in the exact sheets; Home+Project in the `6/2025` guide. Associate each actual function with its external actuator and required address scope; symbols do not identify a built-in power output. Published group/general control differs from point-to-point feedback. Compare the actual installed firmware/Object with the catalogue tables before prescribing writes.

Select independent single-slot functions or one three-slot dimmer/shutter/player configuration; their occupancy cannot be added together. The 2020 sheet limits load-control setup to MyHOME_Suite. Proximity shows the configured icons; symbol animation and LED brightness fields retain separate legal domains. Object `147` has five possible animation symbols per icon; all rows/defaults are preserved above. The first row of the first symbol allows six-bit values in the generic domain and is restricted to `32..63` for all three icons by firmware filters; no meaning for the additional bit or replacement default is inferred.

Object `436` COLOR_SET is restricted to `1` despite reusable default `0`; Object `437` ADDR_TYPE to `1` Area despite default `0`. The publisher describes broader role/address capability, but no installed firmware or software evaluation reconciles these subsets. Preserve them rather than selecting a new default or treating the generic domains as effective.

## Source reconciliation

All exact colour variants and the retained sheet/export revisions are accounted for separately. Device-specific physical/function facts, touch mappings, source-defined configuration methods and mounting composition are incorporated above; unrelated gateway/actuator chapters of the system guide do not become specifications of this control. The DAR underscore filename for the sheet returns byte-identical data to the assets hyphen filename and supplies no additional revision. The catalogue/guide identity lists corroborate marketed Living Now and colour scope, while the original catalogue implementation remains a separate historical capability source.

| Issue | Reconciliation / unresolved limit | Evidence |
| --- | --- | --- |
| Physical/logical count | One physical digital position; five logical Modules: three command slots, icon/proximity and brightness | Exact sheet vs firmware topology |
| Source chronology | The technical guide’s URL directory says 2024-02 but the retained original rear cover says `AD-EXMH25GT`, version `6/2025`; catalogue rear cover is `01/2025` | Printed original labels; no date inferred from URL |
| Temperature | Sheet operating upper bound `40 °C`, current export operating/setting upper bound `45 °C`; no hardware-revision explanation | Sheet p. 1; exact exports p. 3 |
| Power scope | Standby `9 mA` in sheet versus current exports `6/6/6.2 mA`; sizing currents KW/KM/KG `12/15/25 mA` remain distinct | Sheet p. 1; exact colour exports p. 3 |
| Colour naming | KM = sand in guide/catalogue and Beige in exact export; catalogue item’s white label does not describe all variants | Exact reference/colour lists and individual exports |
| Configuration tools | 2020 sheet Up/Suite plus Digital Controls; load control Suite-only; 2025 guide Home+Project. No universal app/gateway support inferred | Exact source revisions |
| Frame mounting terminology | Sheet says surface-mounted one-module control, export says flush-mounted; guide shows digital control on front of electrified frame over a flush box | Sheet p. 1; export p. 3; guide pp. 50-53 |
| Digital transport | SCS contact supply/connection is established; exported voice/internet/interoperability attributes describe a system capability, not a native microphone, radio or direct IP socket | Exports pp. 3-4; guide distinguishes separate voice control |
| Virgin membership | Virgin `521` generic allowed list is different from direct Objects of firmware `804`; no automatic conversion is established | Exact catalogue relations |
| Preset/NUVO wording | Current English description says shutter without preset and omits NUVO, but its capability list includes NUVO/coloured lights; 2020 exact sheet and 2025 catalogue explicitly include preset/NUVO. No removal inferred | Export p. 1; exact sheet pp. 1-2; catalogue p. 103 |
| Restricted defaults | First icon rows `32..63`, COLOR_SET `1`, shutter ADDR_TYPE `1` exclude their generic defaults `0`; no replacement defaults or runtime resolution | Filters `3852/3853/3854/3858/3843` |
| Proximity versus IR attribute | Exact sheet establishes a proximity sensor; export IR-sensor No is a separate classification and does not negate it | Sheet p. 1; exact exports p. 3 |
| Hue prose inconsistency | Fifth hue-low field prose names fourth high bit; range/default and separate fifth high-bit field remain literal. No guessed fix | Object `436` field definitions |

## Evidence limits and open work

- Reconcile published functions with the exact firmware filter/default restrictions through inspected parameter payloads and accepted software/hardware configuration.
- Establish the temperature and standby-current differences, revision applicability, complete reset/update/replacement procedures and app/gateway prerequisites.
- Corroborate active Modules/Objects, Virgin transitions, installed firmware/build, hardware/MCU revisions and source-defined behavior using sanitized captures.
- Confirm the icon-row extra-bit semantics, accepted RGB/NUVO transport and three-slot occupancy without treating shared reusable Objects as universal support.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
