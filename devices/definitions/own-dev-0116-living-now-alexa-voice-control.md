# Living Now Alexa voice control

## Summary

This Living Now wall device combines an Alexa voice interface with two capacitive lighting keys. Microphones, a speaker and Wi-Fi support the configured voice service, while separate setup defines the local SCS touch functions and account connection.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0116` | Project identity |
| Technical description | Living Now Alexa voice control | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `KW8013`, `KM8013`, `KG8013` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `2276` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `121` | Main association; independent of project ID |
| Firmware definition | `806` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `5` | Firmware metadata |
| Categories | Commands, User interfaces, Audio video, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Living Now | `KW8013` | Established catalogue identity | Manufacturer database commercial record `2635` explicitly links this SKU to item `2276` |
| BTicino - Living Now | `KM8013` | Established catalogue identity | Manufacturer database commercial record `2636` explicitly links this SKU to item `2276` |
| BTicino - Living Now | `KG8013` | Established catalogue identity | Manufacturer database commercial record `2637` explicitly links this SKU to item `2276` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `KG8013` | `8005543650820` | [Archived original](https://archive.openwebnet-ha.org/sha256/50/9f/509f6e105dfea157c23144e080d69b7a508d7ad32be99c3f92fb3ccd331e0630.pdf), `KG8013-publisher-product-sheet.pdf`, printed/PDF p. 1 |
| `KM8013` | `8005543650813` | [Archived original](https://archive.openwebnet-ha.org/sha256/95/79/9579ce2582249a182a7da0669b58dbe30929ddd3f1aff65e2c59620472cd527e.pdf), `KM8013-publisher-product-sheet.pdf`, printed/PDF p. 1 |
| `KW8013` | `8005543650806` | [Archived original](https://archive.openwebnet-ha.org/sha256/01/7b/017b1e0408da356d890909d6bccdeae92db34c139fe652afeda3f15b048cb9ca.pdf), `KW8013-publisher-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

### Complete catalogue commercial metadata

| Record | Reference | Catalogue name | Brand key | Line key | Visible | Visibility type | Dependent | Gateway | Catalogue description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `2635` | `KW8013` | `Adv - voice assistant Amazon` | `1` | `20` | `1` |  | `0` | `0` | `Adv - voice assistant Amazon white` |
| `2636` | `KM8013` | `Adv - voice assistant Amazon` | `1` | `20` | `1` |  | `0` | `0` | `Adv - voice assistant Amazon sand` |
| `2637` | `KG8013` | `Adv - voice assistant Amazon` | `1` | `20` | `1` |  | `0` | `0` | `Adv - voice assistant Amazon dark` |

Empty catalogue values are retained as empty metadata; none is an installed-state or market-availability observation.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `LE11578AB.pdf` | Instruction Use LE11578AB | `LE11578AB; 02/20-01 PC` | English ratings/instructions, product labels and mounting diagrams inspected on PDF pp. 1-3; other translations not comprehensively reconciled | [Archived original](https://archive.openwebnet-ha.org/sha256/c6/76/c676e4a74e5f8b2da0b53bd0b47b88392f1329f2a39640a6ac45bf6635c1504c.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/LE11578AB.pdf) |
| `RA00168AA_EN.pdf` | Technical Guide RA00168AA_EN | `RA00168AA_EN; printed production example 19W48 does not date publication` | Complete English manual pp. 1-58: setup, voice/status, account/reset/update, touch functions and Suite configuration; mounting and reused-wording contradictions reconciled explicitly. Printed pagination and 1-based PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/3b/44/3b447ddb79af394b6cbcb6e31b480ee7780284ec535957cca8c4b668666e4623.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00168AA_EN.pdf) |
| `ST-00002621-EN.pdf` | Technical Sheet ST-00002621-EN | `ST-00002621-EN; 21/05/2026` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-1; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/ad/bd/adbd010d9a5c5a677433da7bd07800a8e6a8ce40b0a559888d4b1dab273d5528.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002621-EN.pdf) |
| `KG8013-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 04.10.2026` | Complete exact-reference export: commercial/EAN and all classification fields; linked documents inventoried separately, not automatically incorporated | [Archived original](https://archive.openwebnet-ha.org/sha256/50/9f/509f6e105dfea157c23144e080d69b7a508d7ad32be99c3f92fb3ccd331e0630.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-KG8013&include_technical=1) |
| `KM8013-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 04.10.2026` | Complete exact-reference export: commercial/EAN and all classification fields; linked documents inventoried separately, not automatically incorporated | [Archived original](https://archive.openwebnet-ha.org/sha256/95/79/9579ce2582249a182a7da0669b58dbe30929ddd3f1aff65e2c59620472cd527e.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-KM8013&include_technical=1) |
| `KW8013-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 04.10.2026` | Complete exact-reference export: commercial/EAN and all classification fields; linked documents inventoried separately, not automatically incorporated | [Archived original](https://archive.openwebnet-ha.org/sha256/01/7b/017b1e0408da356d890909d6bccdeae92db34c139fe652afeda3f15b048cb9ca.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-KW8013&include_technical=1) |
| `ST_00001003_EN.pdf` | Earlier English voice technical sheet | `ST_00001003_EN; 30/09/2021` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-3; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/c0/a4/c0a47e2b7d5baafcecb8ebd8073fa6e162ee85b7f1553216af1c30d2ce5a8c71.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/ST_00001003_EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `2276` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `27 Vdc; minimum 25 Vdc` | `ST-00002621-EN` p. 1; `ST-00001003-EN` pp. 1-3; `RA00168AA_EN` pp. 4-14 |
| Standby / maximum draw | `130 mA / 350 mA` | `ST-00002621-EN` p. 1; `ST-00001003-EN` pp. 1-3; `RA00168AA_EN` pp. 4-14 |
| Mounting | `3 wiring-device modules`; leaflet prescribes horizontal mounting; manual prose prescribes vertical mounting | `LE11578AB` p. 2 versus `RA00168AA_EN` p. 10; contradictory orientation instructions require clarification |
| Operating temperature | `5..45 °C` | `ST-00002621-EN` p. 1; `ST-00001003-EN` pp. 1-3; `RA00168AA_EN` pp. 4-14 |
| Wi-Fi | `IEEE 802.11 b/g/n; 2.4..2.4835 GHz; <20 dBm; WPA/WPA2` | `ST-00002621-EN` p. 1; `ST-00001003-EN` pp. 1-3; `RA00168AA_EN` pp. 4-14 |
| Recommended voice distance | `5 m` | `ST-00002621-EN` p. 1; `ST-00001003-EN` pp. 1-3; `RA00168AA_EN` pp. 4-14 |
| Physical interface | `microphones; speaker; Alexa status LED; multifunction, mute and volume keys; two capacitive light keys` | `ST-00002621-EN` p. 1; `ST-00001003-EN` pp. 1-3; `RA00168AA_EN` pp. 4-14 |
| Additional supply | `K8003; required for additional voice controls beyond the one supported by a system power supply` | `ST-00002621-EN` p. 1; `ST-00001003-EN` pp. 1-3; `RA00168AA_EN` pp. 4-14 |

### Publisher export attributes

These are the captured publisher classification values for the named variants. They do not override a technical sheet’s ratings or prove runtime protocol support. A negative radio-bus/connected-object classification is not evidence against separately documented gateway or Wi-Fi behavior.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Bus system KNX-RF (Radio Frequency) | `No` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Bus system radio frequency | `No` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Bus system LON | `No` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Bus system Powernet | `No` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Other bus systems | `Other` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Radio frequency bidirectional | `No` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Mounting method | `Flush-mounted` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| With anti-theft/dismantling protection | `No` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| With bus connection | `Yes` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Number of actuation points | `2` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Number of buttons | `2` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| With LED indication | `Yes` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| With label area | `No` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| With display | `No` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Material | `Plastic` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Material quality | `Thermoplastic` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Surface protection | `Untreated` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Surface finishing | `Matt` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Colour | `Black` | `KG8013` export p. 3 |
| RAL-number (similar) | `9011` | `KG8013` export p. 3 |
| Transparent | `No` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| With room temperature controller | `No` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| With IR sensor | `No` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Degree of protection (IP) | `IP20` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Min. depth of built-in installation box | `40 mm` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Width | `124.5 mm` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Height | `86 mm` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Depth | `10 mm` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Built-in depth | `2 mm` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Operating / setting temperature (Min-Max) | `5-45 °C` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Storage temperature (Min-Max) | `-20-70 °C` | `KG8013` export p. 3; `KW8013` export p. 3 |
| Frequency (Min-Max) | `0-0 Hz` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Standby consumption | `130 mA` | `KG8013` export p. 3; `KM8013` export p. 3; `KW8013` export p. 3 |
| Terminal marking indication | `Yes` | `KG8013` export p. 3; `KW8013` export p. 3 |
| Antimicrobial treatment | `No` | `KG8013` export p. 3; `KM8013` export p. 4; `KW8013` export p. 3 |
| Terminals capacity (Min-Max) | `1-1 mm²` | `KG8013` export p. 4; `KM8013` export p. 4; `KW8013` export p. 4 |
| Cable nature for connection | `Flexible or rigid` | `KG8013` export p. 4; `KM8013` export p. 4; `KW8013` export p. 4 |
| Label space/information surface | `No` | `KG8013` export p. 4; `KM8013` export p. 4; `KW8013` export p. 4 |
| Addressable | `Yes` | `KG8013` export p. 4; `KM8013` export p. 4; `KW8013` export p. 4 |
| Contains Batteries | `No` | `KG8013` export p. 4; `KW8013` export p. 4 |
| Connected object | `Yes` | `KG8013` export p. 4; `KM8013` export p. 4; `KW8013` export p. 4 |
| Operating method | `SCS` | `KG8013` export p. 4; `KM8013` export p. 4; `KW8013` export p. 4 |
| With voice command | `Yes` | `KG8013` export p. 4; `KM8013` export p. 4; `KW8013` export p. 4 |
| Programmable | `Yes` | `KG8013` export p. 4; `KM8013` export p. 4; `KW8013` export p. 4 |
| Interoperable connection Protocol | `Yes` | `KG8013` export p. 4; `KM8013` export p. 4; `KW8013` export p. 4 |
| Connectable by Internet box | `Yes` | `KG8013` export p. 4; `KM8013` export p. 4; `KW8013` export p. 4 |
| Product use function | `Control & command systems` | `KG8013` export p. 4; `KM8013` export p. 4; `KW8013` export p. 4 |
| Software Update Duration (years) | `3` | `KG8013` export p. 4; `KM8013` export p. 4; `KW8013` export p. 4 |
| Colour | `Beige` | `KM8013` export p. 3 |
| RAL-number (similar) | `7044` | `KM8013` export p. 3 |
| degree of impact strength (IK) | `Not applicable` | `KM8013` export p. 3 |
| Storage temperature (Min-Max) | `-10-70 °C` | `KM8013` export p. 3 |
| Terminal marking indication | `No` | `KM8013` export p. 3 |
| Colour | `White` | `KW8013` export p. 3 |
| RAL-number (similar) | `9016` | `KW8013` export p. 3 |

### Published Alexa status indications

| Indication | Documented meaning | Source |
| --- | --- | --- |
| light blue / blue | listening, processing and verbal response; alarms/timers/memos | RA00168AA_EN p. 9 |
| blue | startup or received voice notification | RA00168AA_EN p. 9 |
| red | microphone disabled or requested service/system/Wi-Fi error | RA00168AA_EN p. 9 |
| yellow flashing | pending message/notification | RA00168AA_EN p. 9 |
| white | changed device status such as volume | RA00168AA_EN p. 9 |
| orange | ready for configuration | RA00168AA_EN p. 9 |
| purple | Do Not Disturb active | RA00168AA_EN p. 9 |

| Property | Value | Evidence |
| --- | --- | --- |
| Installation position | Recommended height `80..100 cm`, away from obstacles; `K8001` and `K8003` cannot share the same box | `RA00168AA_EN` pp. 10, 14 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2276` | Canonical catalogue |
| Technical item description | Adv - voice assistant Amazon | Canonical catalogue |
| Item family | 0; key `1` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `121` | `AS_ITEM_SYSTEM` |
| Commercial record count | `3` | `EN_DEVICE` |
| Additional system | Integration function; key `26`; model `129` | Separate non-main catalogue association |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `121` | Yes | Canonical item/system relationship |
| Integration function | `129` | No | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `806` | `1` | `0` | No build row | `5` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `806` | `1` | `434` Simplified Light single control basic | Fixed/designated metadata | `3334` | `652` | `1616` |
| `806` | `2` | `434` Simplified Light single control basic | Fixed/designated metadata | `3335` | `652` | `1616` |
| `806` | `3` | `434` Simplified Light single control basic | Fixed/designated metadata | `3336` | `652` | `1616` |
| `806` | `4` | `434` Simplified Light single control basic | Fixed/designated metadata | `3337` | `652` | `1616` |
| `806` | `5` | `148` Led Brightness Settings | Fixed/designated metadata | `3333` | `657` | `1615` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `806` | `521` Soft-Touch command virgin | `1`, `2`, `3`, `4` | `410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `418`, `419`, `421`, `426`, `427`, `462` | `521` | `142` |

## Configuration modes

### Complete catalogue mode and connection associations

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `806` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `806` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

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

### Virgin-only reusable capability

The following Objects are permitted by an associated Virgin Object but lack a direct Object/Firmware relationship for this Device. Their reusable definitions are inventoried for completeness; they are not a declaration of active placements or supported values on this Firmware.

### Object `410` - Light control (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `1` = Timed `ON`; `2` = Toggle dimmer; `4` = Toggle `ON/OFF`; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `20` = `ON` and point to point dimmer; `21` = `OFF` and point to point dimmer; `22` = `ON` and Dimmer; `23` = `OFF` and Dimmer; `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90%; `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `131` = Customized toggle dimmer; `133` = Customized toggle dimmer without regulation; `135` = Customized `ON` and dimmer without regulation; `136` = Customized `OFF` and dimmer without regulation; `137` = Customized `ON` and dimmer with regulation; `138` = Customized `OFF` and dimmer with regulation | `0` | Modality; Mode (MODE+`ON/OFF`) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
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

### Object `411` - Automation control (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = UP bistable control; `1` = DOWN bistable control; `2` = UP monostable control; `3` = DOWN monostable control; `4` = UP monostable and bistable control; `5` = DOWN monostable and bistable control | `0` | Modality; mode (`UP/DOWN`) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `412` - Lock/unlock actuator control (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `1` = Disable; `2` = Enable | `1` | Modality; mode (D/E) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `413` - Scenario module control (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Scenario activation and modification; `1` = Scenario activation | `0` | Modality |
| `APL` | `0..175`; area `floor(APL/16)`, light point `APL mod 16` | `0` | Scenario module address |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15 | `0` | Destination level; Destination level (`0..15`) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `SCE_BUTT_1` | `1..16` | `1` | Scenario number |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay of scenario number |

### Object `414` - Scheduled scenario (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `CEN_BUTT_1` | `0..31` | `1` | Button |
| `MODE` | `0` = Press/release only; `1` = Press/hold/release | `0` | Modality; Mode (Lighting management) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `415` - Scenario PLUS Lighting Management (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = `ON`; `1` = `OFF`; `2` = `ON` with regulation; `3` = `OFF` with regulation | `0` | Modality; Mode (`ON/OFF` regulation) |
| `PPT_SCE_1` | `0..255` | `1` | Upper button scenario |
| `TYPE_OF_REGULATION` | `0` = Regulate all; `1` = Lights only; `2` = Shutters only; `3` = Stereo amplifiers only | `0` | Regulation type |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for upper button |

### Object `416` - Scheduled scenario PLUS (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | `0..255` | `1` | Scheduled scenario PLUS number |
| `PPT_CEN_HIG` | `0..7` | `0` | Scheduled scenario PLUS number |
| `BUTTON_1` | `0..31` | `1` | Button |
| `MODE` | `0` = Press/release only; `1` = Press/hold/release | `0` | Modality; Mode (Lighting management) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `417` - `AUX` control (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Cyclical; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `17` = DOWN Shutter bistable command; `18` = UP shutter monostable command; `4` = Reset `BI`; `5` = Reset `TRI`; `6` = Reset `GEN`; `1` = Disable; `2` = Enable; `16` = UP shutter bistable command; `19` = DOWN Shutter monostable command | `0` | Modality; mode(Cyclical,off,on,pul,up,down,...) |
| `OUT_AUX_CH` | `1..15` | `1` | `AUX` channel |
| `TYPE_CONTACT` | No legal values specified in source | `0` | Contact type |

### Object `418` - Open lock control (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same level; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Level |

### Object `419` - Sound diffusion control (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = `ON`/volume +; `1` = `OFF`/volume -; `2` = Change track; `3` = Switch source; `4` = Toggle `ON/OFF` | `0` | Modality; Mode (VOL,ON_OFF) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..9` | `0` | Area |
| `PF` | `0..9` | `0` | Audio point |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `IS_FOLLOW_ME` | `0` = No; `1` = Yes | `1` | Follow me |
| `SOURCE` | `1..9` | `1` | Source |
| `SUB_SOURCE` | `0..255` | `0` | Sub source |
| `CHANNEL` | `0` = Base Band; `1` = Left; `2` = Right; `3` = Stereo; `8` = Base Band and Video; `9` = Left and video; `10` = Right and video; `11` = Left and video | `3` | Channel (BB-Stereo) |

### Object `421` - Cyclic autoswitch control (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |

### Object `426` - Staircase light control (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |

### Object `427` - Floor call control (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `TO_ALL` | `0` = Point to point; `1` = General | `1` | Type of call |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |

### Object `462` - Open lock command on session (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |

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

Four lighting placements and separate brightness metadata account for five catalogue Modules; voice/account functions are documented services, not an Alexa Object in this topology. MODE filter `3851` admits only `2` while the retained manual describes cyclical, `OFF`, `PUL` and timed modes. Fourteen Virgin-only candidates add 83 reusable fields. The older manual contains vertical/horizontal mounting and reused thermostat/Smarther wording conflicts; these remain visible beside the exact leaflet and later sheet, rather than silently copied as hardware specifications.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `806` | `434` | `3851` | `MODE` | `2` = `ON` without regulation | `0` | Modality; reusable default `0` is outside this subset; filter supplies no replacement default |
| `806` | `434` | `3859` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `806` | `434` | `3862` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `121` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `148` - Led Brightness Settings | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `434` - Simplified Light single control basic | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |

These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Configure the voice service and Wi-Fi association through Digital Controls and the Legrand/Amazon account workflow. Configure the SCS touch functions separately through Home+Project or MyHOME_Suite, with historical MyHOME_Up procedures retained in the 2021 sheet and manual. One voice control per system supply is the published sizing rule; additional controls need K8003. The manual documents an app reset and simultaneous multifunction/volume-plus reset that disconnect the accounts (printed/PDF pp. 29, 34). The two capacitive zones can each be assigned one cyclic control or two separate controls. Microphone mute, voice association and touch-light configuration are distinct operations.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

### Published account, update and touch-control procedures

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Initial service association | Historical manual requires Legrand and Amazon accounts, Internet-connected home Wi-Fi, smartphone Bluetooth `4.2` and smartphone/device on the same Wi-Fi network; historical OS minima do not establish current app eligibility | `RA00168AA_EN` pp. 4, 15-25 |
| Firmware update | Update over local Wi-Fi only; keep supply and connection available throughout | `RA00168AA_EN` pp. 26-27 |
| Wi-Fi or password change | Reset and repeat association; the account/device unlinking procedure uses multifunction and volume-plus keys. No SCS address/configuration wipe is established by that account reset | `RA00168AA_EN` pp. 29-34 |
| Touch function setup | Historical MyHOME_Up installer/local-PIN route or MyHOME_Suite assigns function, address and point/room/group/general scope; fifth logical Module governs brightness/off for power saving | `RA00168AA_EN` pp. 36-53 |
| Touch modes | Cyclic mode is available through the app; other modes are physically operated. Published external-actuator commissioning interlocks do not imply built-in power relays | `RA00168AA_EN` pp. 40, 50 |
| Current system prerequisite | 2026 sheet requires a MyHOME system; 2021 wiring references MyHOMEServer1. Current commissioning-tool names do not prove every older server/firmware combination | `ST-00002621-EN` p. 1; `ST_00001003_EN` pp. 1-3 |

## Source reconciliation

The 2021 sheet and user manual expose cyclic, `OFF`, `PUL` and timed touch-light behavior, while the 2026 sheet updates commissioning names to Home+Project/Digital Controls. The database exposes four lighting placements plus separate brightness metadata, not five physical touch keys and not an Alexa protocol Object. Its Object `434` restriction is only `MODE=2` (`ON`), excluding reusable default `0` and the published cyclic/`OFF`/`PUL`/timed choices. No replacement default or reconciliation with an installed firmware is established. The Virgin Object association names broader reusable commands that are not unconditional active Objects. The publisher exports describe Wi-Fi voice capability while classification fields say no radio bus and frequency `0-0 Hz`; those classification values do not specify the Wi-Fi carrier.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `LE11578AB.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `RA00168AA_EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `ST-00002621-EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `KG8013-publisher-product-sheet.pdf` | Captured exact-variant identity and complete technical classification attributes tabulated above; document links are discovery provenance, not additional independently verified capability. |
| `KM8013-publisher-product-sheet.pdf` | Captured exact-variant identity and complete technical classification attributes tabulated above; document links are discovery provenance, not additional independently verified capability. |
| `KW8013-publisher-product-sheet.pdf` | Captured exact-variant identity and complete technical classification attributes tabulated above; document links are discovery provenance, not additional independently verified capability. |
| `ST_00001003_EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |

The relation-specific restriction table explicitly identifies reusable defaults outside the permitted subset. These are catalogue inconsistencies; no replacement default is inferred. Runtime Configuration and manufacturer modes must be corroborated before selecting a substitute.

The older user manual additionally lists WEP/WPS authentication and smartphone Bluetooth requirements; the 2026 sheet lists WPA/WPA2 and Wi-Fi 2.4 GHz. Those historical setup descriptions do not establish current service/network eligibility. Documented UI status is separate from protocol readback.

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting contradiction | Leaflet says horizontal only; manual p. 10 says vertical only. Do not silently choose a direction from these conflicting instructions | `LE11578AB` p. 2; `RA00168AA_EN` p. 10 |
| Reused manual wording | The firmware-update heading says Smarther; pp. 47 and 51 refer to a thermostat. These editing errors do not change the exact voice-control identity | `RA00168AA_EN` pp. 26, 47, 51 |
| Translation unit | Dutch leaflet prints voice distance `5 mm`; English prints `5 m`. English technical sheets support `5 m`; translation discrepancy remains recorded | `LE11578AB` p. 3; technical sheets |

## Evidence limits and open work

A firmware capture is needed to resolve the touch-mode/filter discrepancy, Virgin Object applicability, and actual diagnostics. Current account-service behavior and every variant’s installed hardware remain unobserved.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

Publisher-linked `BRO-LNOW2M`, `BRO-LNOW3M`, `CAT-LNOW2M` and other Living Now catalogue/brochure editions have not all been independently examined. Only the retained revisions and page scopes listed in Documentation support claims here; linked inventory is not evidence of every edition’s contents.

Mounting orientation requires manufacturer clarification. The English manual was reviewed across pp. 1-58; mounting-leaflet scope is English instructions, specifications and diagrams, with the noted Dutch unit discrepancy. Additional translations have not all been independently reconciled.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0111-0120-2026-10-06.md#own-dev-0116)
