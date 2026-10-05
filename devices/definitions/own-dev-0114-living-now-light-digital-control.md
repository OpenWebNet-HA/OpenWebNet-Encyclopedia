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

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ST-00000542-EN.pdf` | English LIGHT technical sheet | `ST-00000542-EN; 21/02/2020` | KW/KM/KG8010: specifications, layout, light/brightness functions and MyHOME_Up/Suite setup. Printed/PDF p. 1. | [Archived original](https://archive.openwebnet-ha.org/sha256/0e/65/0e6556ab0dc6719429e7e5d5cfeb4bc715ca134cc0d3fdacae4cfa97ed11e662.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00000542-EN.pdf) |
| `KW8010-publisher-product-sheet.pdf` | English publisher product export | `DATASHEET; 03.10.2026` | KW8010 only: identity, line, colour and descriptive capability pp. 1-2; physical/technical attributes pp. 3-4; publisher document inventory p. 5. Printed/PDF pages coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/88/ca/88ca328656a25c613079ee74ad293d6ae1be4b0c06a970fb9be1f89e730c3af1.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-KW8010&include_technical=1) |
| `KM8010-publisher-product-sheet.pdf` | English publisher product export | `DATASHEET; 03.10.2026` | KM8010 only: identity, line, colour and descriptive capability pp. 1-2; physical/technical attributes pp. 3-4; publisher document inventory p. 5. Printed/PDF pages coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/da/24/da2404125a548a616b6b5f4314e5268be741b72c6e65f485c075edf18ca4d71d.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-KM8010&include_technical=1) |
| `KG8010-publisher-product-sheet.pdf` | English publisher product export | `DATASHEET; 03.10.2026` | KG8010 only: identity, line, colour and descriptive capability pp. 1-2; physical/technical attributes pp. 3-4; publisher document inventory p. 5. Printed/PDF pages coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/2f/9b/2f9b4480ea05ad1e53f34957ccf13c60771e818307ab2af87c7907b6d4d3bd2f.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-KG8010&include_technical=1) |
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

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `803` | `1` | `0` | No build row | `3` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

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

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `803` | Advanced Configuration | `2` | Association key `2` |


No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

The exact 2020 sheet names MyHOME_Up and MyHOME_Suite. The retained `6/2025` system guide names Home+Project for function assignment, associated actuators and icon configuration. These are source/revision-specific workflows. The catalogue mode and connection associations above remain the implementation snapshot; no installed gateway/app/firmware compatibility is inferred from current app names. No published physical configurator setup is documented for this digital contact-mounted control.

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

- Reconcile published functions with the exact firmware filter/default restrictions through inspected parameter payloads and accepted software/hardware configuration.
- Establish the temperature differences, revision applicability, complete reset/update/replacement procedures and app/gateway prerequisites.
- Corroborate active Modules/Objects, Virgin transitions, installed firmware/build, hardware/MCU revisions and source-defined behavior using sanitized captures.
- Confirm both command positions, point-to-point versus group/general feedback, timed-off behavior and separate brightness/power-save settings.

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
