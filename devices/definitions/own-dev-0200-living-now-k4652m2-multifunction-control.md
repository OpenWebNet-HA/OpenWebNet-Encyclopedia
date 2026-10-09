# Living Now K4652M2 multifunction control

## Summary

Living Now K4652M2 is a two-module SCS pushbutton control that can manage one actuator or two separate functions. It covers lighting, dimming, shutters, scenario triggers and video-entry commands, with status LEDs and additional functions available through software configuration.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0200` | Project identity |
| Technical description | Living Now K4652M2 multifunction control | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `K4652M2` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `2205` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `88` | Main association; independent of project ID |
| Firmware definition | `743` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `3` | Firmware metadata |
| Categories | User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Living Now | `K4652M2` | Established catalogue identity | Manufacturer database commercial record `2568` explicitly links this SKU to item `2205` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `K4652M2` | `8005543615157` | [K4652M2-publisher-product-sheet.pdf](https://archive.openwebnet-ha.org/sha256/0d/a4/0da43b49b33e9398cd4f66a6913cd9a56fc30f12f7e433a4de01b54e82421783.pdf) PDF p. 1; [K4652M2-italian-product-sheet.pdf](https://archive.openwebnet-ha.org/sha256/d0/88/d0886b63b9304f5c39d85a11f47780800e80cf19a2643c4f2a0398c1eda99410.pdf) PDF p. 1 |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `K4652M2` | Comando unico Living Now 2 moduli | Canonical commercial record `2568` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MyHOME Technical Guide.pdf` | MyHOME technical guide | `GUI-MHOME; printed publication date not established` | PDF pp. 25, 60, 71-72, 82: exact F459 integration references; pp. 48, 54-58, 86-87, 99: K4652M2 configuration / application examples. Family examples are not measured behavior. | [Archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MyHOME%20Technical%20Guide.pdf) |
| `LE10514AA.pdf` | Living Now multilingual installation leaflet | `LE10514AA; printed code 02/18-01PC` | PDF pp. 1-2: K4652M2 cover / mounting and control assembly; other product references do not establish K4652M2 capabilities. | [Archived original](https://archive.openwebnet-ha.org/sha256/38/d2/38d2b5bc30b1ce4e743c38c975eb0e7d3629d03b84d27316a5a7cbaee53fc247.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/LE10514AA.pdf) |
| `ST-00002492-EN.pdf` | K4652M2 technical sheet | `ST-00002492-EN; 18/04/2026` | Printed/PDF pp. 1-4: supply / draw / temperature, controls/LEDs, physical and virtual mode / address tables; group feedback expressly limited to production from 25W49. | [Archived original](https://archive.openwebnet-ha.org/sha256/4f/32/4f325ec36ccd0550d6e42335e7f164fd37bf6e85cfe2e3a0533917184a6f8c68.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002492-EN.pdf) |
| `K4652M2-publisher-product-sheet.pdf` | Exact English publisher product export | `Export dated 05.10.2026` | Complete description, product-characteristics and classification tables; exact commercial EAN; linked document / payload inventory remains separately scoped. | [Archived original](https://archive.openwebnet-ha.org/sha256/0d/a4/0da43b49b33e9398cd4f66a6913cd9a56fc30f12f7e433a4de01b54e82421783.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-K4652M2&include_technical=1) |
| `K4652M2-italian-product-sheet.pdf` | Exact Italian publisher product export | `Export retrieved 05.10.2026; compliance dates are boilerplate` | Exact commercial description and technical attributes; EAN used only if explicitly present; European compliance boilerplate is not a publication revision. | [Archived original](https://archive.openwebnet-ha.org/sha256/d0/88/d0886b63b9304f5c39d85a11f47780800e80cf19a2643c4f2a0398c1eda99410.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-K4652M2) |
| `ST-00001033-EN.pdf` | Classe300EOS external compatibility evidence | `ST-00001033-EN; 04/10/2022` | Printed/PDF p. 8 only: exact MyHOMEServer1, 048834 and K4652M2 entries in another product’s compatibility table; no electrical ratings transferred. | [Archived original](https://archive.openwebnet-ha.org/sha256/e8/54/e854cdd3edff2d77efb06d28600565bbe4c691ef760b6aca7ff16b2cfa8576eb.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00001033-EN.pdf) |
| `legrand-living-now-historical.pdf` | Historical Living Now/MyHOME catalogue | `Printed publication date not established` | Printed/PDF pp. 35, 92, 94-95, 98: exact MyHOMEServer1, F459, K4652M2 and 048834 catalogue descriptions; p. 98 PIR settings and internal threshold / timing discrepancy. | [Archived original](https://archive.openwebnet-ha.org/sha256/f7/2a/f72ab15db14eea29dd1693203fa242c32213717b596bcee9fd2ee96ce7d53e71.pdf) | [Publisher original](https://assets.legrand.com/webf/bg/bg_en_Living_NOW_catalogue.pdf) |
| `ST_00000218_IT.pdf` | K4652M2 technical sheet | `ST-00000218-IT; 19/07/2018` | Printed/PDF pp. 1-4: earlier electrical / physical specifications, status LEDs and physical / virtual function matrices; comparison with later production-scoped sheet. | [Archived original](https://archive.openwebnet-ha.org/sha256/02/a3/02a3cc32f642c0dd835f182aabebcd3b8548bd5fa7f06c092897de887ba52c9d.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/ST_00000218_IT.pdf) |
| `ST-00001031-EN.pdf` | Previously archived MyHOME Server technical sheet | `ST-00001031-EN; 30/05/2022` | Printed/PDF pp. 1-4: exact MyHOMEServer1 electrical / interface and system limits; p. 3 explicitly lists 048834 and K4652M2 compatibility. Original publisher URL absent from legacy archival record. | [Archived original](https://archive.openwebnet-ha.org/sha256/14/97/14971697bfbdbb33587b5724c7b38ac2aa6977e05e404556941291cafa589ad7.pdf) | [Previously archived original](https://archive.openwebnet-ha.org/sha256/14/97/14971697bfbdbb33587b5724c7b38ac2aa6977e05e404556941291cafa589ad7.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2205`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply | `18..27 Vdc` | `ST-00002492-EN.pdf` printed/PDF p. 1; `LE10514AA.pdf` PDF pp. 1-2 |
| Draw at maximum LED intensity | `5 mA standby / 11 mA maximum` | `ST-00002492-EN.pdf` printed/PDF p. 1; `LE10514AA.pdf` PDF pp. 1-2 |
| Operating temperature / size | `0..40 °C; 2 flush-mounted modules` | `ST-00002492-EN.pdf` printed/PDF p. 1; `LE10514AA.pdf` PDF pp. 1-2 |
| Completion | `One or two-module covers; exact cover options shown in installation leaflet` | `ST-00002492-EN.pdf` printed/PDF p. 1; `LE10514AA.pdf` PDF pp. 1-2 |
| Local interface | `Control pushbuttons; status LEDs; LED adjustment button; SCS connector; physical selector sockets` | `ST-00002492-EN.pdf` printed/PDF p. 1; `LE10514AA.pdf` PDF pp. 1-2 |
| Status LEDs | `Steady blue: load on; steady white: load off; flashing: Object not configured` | `ST-00002492-EN.pdf` printed/PDF p. 1; `LE10514AA.pdf` PDF pp. 1-2 |
| Group feedback production limit | `From production 25W49, according to 18/04/2026 sheet` | `ST-00002492-EN.pdf` p. 1; earlier virtual-feedback wording retained separately |
| Publisher product-characteristics | One command for lighting / dimmer / shutter / scenario; configured by app; 2 flush-mounted modules; complete with one- or two-module cover | `K4652M2-publisher-product-sheet.pdf` PDF pp. 1-2 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Frequency classifications and a negative connected-object classification do not establish the runtime transport or exclude control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system KNX-RF (Radio Frequency) | `No` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system radio frequency | `Yes` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system LON | `No` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system Powernet | `No` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Other bus systems | `Other` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Radio frequency bidirectional | `No` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Mounting method | `Flush-mounted` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| With anti-theft / dismantling protection | `No` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| With bus connection | `Yes` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Number of actuation points | `2` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Number of buttons | `2` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| With LED indication | `Yes` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| With label area | `No` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| With display | `No` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Material | `Other` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Material quality | `Other` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Surface protection | `Untreated` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Surface finishing | `Matt` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Colour | `Anthracite` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| RAL-number (similar) | `9011` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Transparent | `No` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| With room temperature controller | `No` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| With IR sensor | `No` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Degree of protection (IP) | `Other` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Min. depth of built-in installation box | `30 mm` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Width | `45 mm` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Height | `45 mm` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Depth | `18 mm` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| degree of impact strength (IK) | `Not applicable` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Operating / setting temperature (Min-Max) | `0-40 °C` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Storage temperature (Min-Max) | `-10-70 °C` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Frequency (Min-Max) | `0-0 Hz` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Standby consumption | `5 mA` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Terminal marking indication | `Yes` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Antimicrobial treatment | `No` | `K4652M2-publisher-product-sheet.pdf` PDF p. 3 |
| Cable nature for connection | `Flexible or rigid` | `K4652M2-publisher-product-sheet.pdf` PDF p. 4 |
| Label space / information surface | `No` | `K4652M2-publisher-product-sheet.pdf` PDF p. 4 |
| Addressable | `Yes` | `K4652M2-publisher-product-sheet.pdf` PDF p. 4 |
| Contains Batteries | `No` | `K4652M2-publisher-product-sheet.pdf` PDF p. 4 |
| Connected object | `No` | `K4652M2-publisher-product-sheet.pdf` PDF p. 4 |
| Operating method | `SCS` | `K4652M2-publisher-product-sheet.pdf` PDF p. 4 |
| With voice command | `Yes` | `K4652M2-publisher-product-sheet.pdf` PDF p. 4 |
| Programmable | `Yes` | `K4652M2-publisher-product-sheet.pdf` PDF p. 4 |
| Interoperable connection Protocol | `Yes` | `K4652M2-publisher-product-sheet.pdf` PDF p. 4 |
| Connectable by Internet box | `Yes` | `K4652M2-publisher-product-sheet.pdf` PDF p. 4 |
| Product use function | `Control & command systems` | `K4652M2-publisher-product-sheet.pdf` PDF p. 4 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2205` | Canonical catalogue |
| Technical item description | Comando unico Living Now 2 moduli | Canonical catalogue |
| Item family | Source placeholder description `0`; key `1` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `88` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `88` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `743` | `1` | `0` | No build row | `3` | Catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `743` | `1` | `400` Light control | Fixed / designated metadata | `3033` | `400` | `1446` |
| `743` | `1` | `401` Automation control | Candidate alternative | `2846` | `401` | `1352` |
| `743` | `1` | `402` Lock / unlock actuator control | Candidate alternative | `2848` | `402` | `1353` |
| `743` | `1` | `406` Scheduled scenario PLUS | Candidate alternative | `2850` | `406` | `1354` |
| `743` | `1` | `408` Open lock control | Candidate alternative | `2856` | `408` | `1357` |
| `743` | `1` | `427` Floor call control | Candidate alternative | `2858` | `427` | `1358` |
| `743` | `1` | `430` Staircase light control | Candidate alternative | `2860` | `430` | `1359` |
| `743` | `1` | `463` Load control actuator visualization | Candidate alternative | `2852` | `492` | `1355` |
| `743` | `1` | `145` Shutter control (2 slots) | Candidate alternative | `3053` | `650` | `1458` |
| `743` | `2` | `400` Light control | Fixed / designated metadata | `3034` | `400` | `1446` |
| `743` | `2` | `401` Automation control | Candidate alternative | `2847` | `401` | `1352` |
| `743` | `2` | `402` Lock / unlock actuator control | Candidate alternative | `2849` | `402` | `1353` |
| `743` | `2` | `406` Scheduled scenario PLUS | Candidate alternative | `2851` | `406` | `1354` |
| `743` | `2` | `408` Open lock control | Candidate alternative | `2857` | `408` | `1357` |
| `743` | `2` | `427` Floor call control | Candidate alternative | `2859` | `427` | `1358` |
| `743` | `2` | `430` Staircase light control | Candidate alternative | `2861` | `430` | `1359` |
| `743` | `2` | `463` Load control actuator visualization | Candidate alternative | `2853` | `492` | `1355` |
| `743` | `3` | `143` User interface settings for command | Fixed / designated metadata | `3032` | `644` | `1445` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `743` | `501` Special double command virgin | `1`, `2` | `400`, `401`, `402`, `403`, `404`, `405`, `406`, `407`, `408`, `409`, `427`, `430` | `501` | `80` |

Firmware `743` is Official `1.0` with no build row; no `.0` build is invented. Three logical Modules describe two control positions and a UI-settings Object, separate from the two-module physical width. Virgin `501` permits 12 reusable roles in slots 1/2; Objects 403/404/405/407/409 have Virgin membership without direct firmware/Object placement and are retained as Virgin-only candidates. Shutter Object `145` is named “2 slots” but has only a slot-1 association; this label does not establish an additional slot-2 placement. No attached slot predicates or conversion rules map the physical selectors to active Objects.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `743` | Physical configuration | `0` | Canonical firmware/mode association |
| `743` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `743` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Physical A1/A2 / PL1/PL2 | `1..9` / `1..9` for point control; virtual room `0..10`, point `0..15` | `ST-00002492-EN.pdf` printed/PDF pp. 1-4; `ST_00000218_IT.pdf` pp. 1-4 |
| Room / group / general | Physical `AMB`/`GR`/`GEN`; virtual groups `1..255` | `ST-00002492-EN.pdf` printed/PDF pp. 1-4; `ST_00000218_IT.pdf` pp. 1-4 |
| M1/`M2=0` / `ON` / `OFF` / `PUL` | Cyclic / `ON` / `OFF` / pushbutton | `ST-00002492-EN.pdf` printed/PDF pp. 1-4; `ST_00000218_IT.pdf` pp. 1-4 |
| Physical timed `ON` `M=8` / 7 / 1 / 2 | 0.5 s / 30 s / 1 min / 2 min; other timings via software | `ST-00002492-EN.pdf` printed/PDF pp. 1-4; `ST_00000218_IT.pdf` pp. 1-4 |
| Physical dimmer M1/`M2=0` / 0/I | Cyclic with sustained adjustment / top `ON` and bottom `OFF` with sustained dimming | `ST-00002492-EN.pdf` printed/PDF pp. 1-4; `ST_00000218_IT.pdf` pp. 1-4 |
| Automation physical M1/M2 | Bistable arrow configurator / monostable arrow-M configurator / 6 for bistable with lath control | `ST-00002492-EN.pdf` printed/PDF pp. 1-4; `ST_00000218_IT.pdf` pp. 1-4 |
| PLUS scenario, virtual | Address `1..2047`; scenario / button number `0..31` | `ST-00002492-EN.pdf` printed/PDF pp. 1-4; `ST_00000218_IT.pdf` pp. 1-4 |
| Door release | Virtual entrance address `0..95`; physical M1/`M2=3`; right module P+1 if `A2=PL2`=`M2=0` | `ST-00002492-EN.pdf` printed/PDF pp. 1-4; `ST_00000218_IT.pdf` pp. 1-4 |
| Floor call | Virtual handset `0..99` or general; physical `M=4`; general `A=GEN` with A/`PL=0` as printed | `ST-00002492-EN.pdf` printed/PDF pp. 1-4; `ST_00000218_IT.pdf` pp. 1-4 |
| Stair light | Virtual handset `0..99`; physical `M=5` | `ST-00002492-EN.pdf` printed/PDF pp. 1-4; `ST_00000218_IT.pdf` pp. 1-4 |
| Virtual-only commands | Shutter position; actuator lock / unlock; load-control actuator display | `ST-00002492-EN.pdf` printed/PDF pp. 1-4; `ST_00000218_IT.pdf` pp. 1-4 |
| LED / group feedback | Hold >2 s to toggle always on / off; group-status return only from 25W49 in current sheet | `ST-00002492-EN.pdf` printed/PDF pp. 1-4; `ST_00000218_IT.pdf` pp. 1-4 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `743` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `743` | `A1` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB` | `0` | Automation A addressing space (for configurator A1) |
| `743` | `PL1` | `0..9` | `0` | PL1 - (0-9) |
| `743` | `M1` | `0..8`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `15` = `PUL` | `0` | Modality; Mode physical configurator (0-8, `O/I`,`OFF`,`ON`, SU_GIU, SU_GIU_M,`PUL`) |
| `743` | `A2` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB` | `0` | Automation A addressing space (for configurator A2) |
| `743` | `PL2` | `0..9` | `0` | PL2 - (0-9) |
| `743` | `M2` | `0..8`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `15` = `PUL` | `0` | Modality; Mode physical configurator (0-8, `O/I`,`OFF`,`ON`, SU_GIU, SU_GIU_M,`CEN`,`PUL`) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `400` - Light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `1` = Timed `ON`; `2` = Toggle dimmer; `3` = `ON`/`OFF` and dimming; `4` = Toggle `ON`/`OFF`; `5` = `ON`/`OFF`; `9` = `ON`/`OFF` and point to point dimming; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90%; `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `130` = Customized `ON`/`OFF` and point to point dimmer; `131` = Customized toggle dimmer; `132` = Customized `ON`/`OFF` and dimmer; `133` = Customized toggle dimmer without regulation; `134` = Customized `ON`/`OFF` and dimmer without regulation | `0` | Modality; Standard mode means: with regulation for Point-to-point addressing, without regulation for Area, Group and General addressing |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group  |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
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
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group  |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |

### Object `402` - Lock / unlock actuator control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `1` = Disable (lower button); `2` = Enable (lower button); `3` = Disable (lower button) - enable (upper button) | `1` | Modality |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group  |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |

### Object `406` - Scheduled scenario PLUS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | `0..255` | `1` | Scheduled scenario PLUS number |
| `PPT_CEN_HIG` | `0..7` | `0` | Scheduled scenario PLUS number |
| `BUTTON_1` | `0..31` | `1` | Upper button |
| `BUTTON_2` | `0..31` | `2` | Lower button |

### Object `408` - Open lock control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEGMENT` | `0` = Same level; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Level |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |

### Object `427` - Floor call control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `TO_ALL` | `0` = Point to point; `1` = General | `1` | Type of call |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |

### Object `430` - Staircase light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Associated Internal Unit address - hundreds |
| `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |

### Object `463` - Load control actuator visualization

Catalogue Object key `492` maps to external Object `463`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PRIORITY` | `0..63` | `1` | Priority |
| `PHASE` | `0` = Single phase; `1` = Phase 1; `2` = Phase 2; `3` = Phase 3 | `0` | Phase |

### Object `143` - User interface settings for command

Catalogue Object key `644` maps to external Object `143`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LED_LEVEL_COMMANDS` | `0` = `OFF`; `1` = Minimum level; `2` = Medium level; `3` = Maximum level | `2` | LED intensity level |
| `ENABLE_DISABLE_LED_COMMAND` | `0` = All Led Enabled; `1` = Presence Led Enabled - State Update Led Disable; `2` = Presence Led Disable - State Update Led Enable; `3` = All Led Disable | `0` | Enable-Disable LED |
| `PRESENCE_LED_INTENSITY_LEVEL_COMMAND` | `0` = Standard level; `1` = High intensity level | `0` | Presence LED intensity level |

### Object `145` - Shutter control (2 slots)

Catalogue Object key `650` maps to external Object `145`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Bistable control; `1` = Monostable control; `2` = Blades control and bistable; `3` = Bistable and blades control | `0` | Modality; Mode (0, 1, 2, 3) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; See Automation System Addressing |
| `A` | `0..10` | `0` | Area; See Automation System Addressing |
| `PL` | `0..15` | `0` | Light point; See Automation System Addressing |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level; See Automation System Addressing |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `15` = Local bus 15; `16` = All systems | `0` | Destination level; See Automation System Addressing |
| `A_R` | `0..10` | `0` | Area of reference actuator |
| `PL_R` | `0..15` | `0` | Light point of reference actuator |
| `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety | `1` | Priority; Shutter management command priority |
| `PRE` | `1..9`; `0` = None | `0` | Preset; Shutter management preset number |

### Object `403` - Scenario module control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Scenario activation and modification; `1` = Scenario activation | `0` | Modality |
| `APL` | `0` = `A=0` `PL=0`; `1` = `A=0` `PL=1`; `2` = `A=0` `PL=2`; `3` = `A=0` `PL=3`; `4` = `A=0` `PL=4`; `5` = `A=0` `PL=5`; `6` = `A=0` `PL=6`; `7` = `A=0` `PL=7`; `8` = `A=0` `PL=8`; `9` = `A=0` `PL=9`; `10` = `A=0` `PL=10`; `11` = `A=0` `PL=11`; `12` = `A=0` `PL=12`; `13` = `A=0` `PL=13`; `14` = `A=0` `PL=14`; `15` = `A=0` `PL=15`; `16` = `A=1` `PL=0`; `17` = `A=1` `PL=1`; `18` = `A=1` `PL=2`; `19` = `A=1` `PL=3`; `20` = `A=1` `PL=4`; `21` = `A=1` `PL=5`; `22` = `A=1` `PL=6`; `23` = `A=1` `PL=7`; `24` = `A=1` `PL=8`; `25` = `A=1` `PL=9`; `26` = `A=1` `PL=10`; `27` = `A=1` `PL=11`; `28` = `A=1` `PL=12`; `29` = `A=1` `PL=13`; `30` = `A=1` `PL=14`; `31` = `A=1` `PL=15`; `32` = `A=2` `PL=0`; `33` = `A=2` `PL=1`; `34` = `A=2` `PL=2`; `35` = `A=2` `PL=3`; `36` = `A=2` `PL=4`; `37` = `A=2` `PL=5`; `38` = `A=2` `PL=6`; `39` = `A=2` `PL=7`; `40` = `A=2` `PL=8`; `41` = `A=2` `PL=9`; `42` = `A=2` `PL=10`; `43` = `A=2` `PL=11`; `44` = `A=2` `PL=12`; `45` = `A=2` `PL=13`; `46` = `A=2` `PL=14`; `47` = `A=2` `PL=15`; `48` = `A=3` `PL=0`; `49` = `A=3` `PL=1`; `50` = `A=3` `PL=2`; `51` = `A=3` `PL=3`; `52` = `A=3` `PL=4`; `53` = `A=3` `PL=5`; `54` = `A=3` `PL=6`; `55` = `A=3` `PL=7`; `56` = `A=3` `PL=8`; `57` = `A=3` `PL=9`; `58` = `A=3` `PL=10`; `59` = `A=3` `PL=11`; `60` = `A=3` `PL=12`; `61` = `A=3` `PL=13`; `62` = `A=3` `PL=14`; `63` = `A=3` `PL=15`; `64` = `A=4` `PL=0`; `65` = `A=4` `PL=1`; `66` = `A=4` `PL=2`; `67` = `A=4` `PL=3`; `68` = `A=4` `PL=4`; `69` = `A=4` `PL=5`; `70` = `A=4` `PL=6`; `71` = `A=4` `PL=7`; `72` = `A=4` `PL=8`; `73` = `A=4` `PL=9`; `74` = `A=4` `PL=10`; `75` = `A=4` `PL=11`; `76` = `A=4` `PL=12`; `77` = `A=4` `PL=13`; `78` = `A=4` `PL=14`; `79` = `A=4` `PL=15`; `80` = `A=5` `PL=0`; `81` = `A=5` `PL=1`; `82` = `A=5` `PL=2`; `83` = `A=5` `PL=3`; `84` = `A=5` `PL=4`; `85` = `A=5` `PL=5`; `86` = `A=5` `PL=6`; `87` = `A=5` `PL=7`; `88` = `A=5` `PL=8`; `89` = `A=5` `PL=9`; `90` = `A=5` `PL=10`; `91` = `A=5` `PL=11`; `92` = `A=5` `PL=12`; `93` = `A=5` `PL=13`; `94` = `A=5` `PL=14`; `95` = `A=5` `PL=15`; `96` = `A=6` `PL=0`; `97` = `A=6` `PL=1`; `98` = `A=6` `PL=2`; `99` = `A=6` `PL=3`; `100` = `A=6` `PL=4`; `101` = `A=6` `PL=5`; `102` = `A=6` `PL=6`; `103` = `A=6` `PL=7`; `104` = `A=6` `PL=8`; `105` = `A=6` `PL=9`; `106` = `A=6` `PL=10`; `107` = `A=6` `PL=11`; `108` = `A=6` `PL=12`; `109` = `A=6` `PL=13`; `110` = `A=6` `PL=14`; `111` = `A=6` `PL=15`; `112` = `A=7` `PL=0`; `113` = `A=7` `PL=1`; `114` = `A=7` `PL=2`; `115` = `A=7` `PL=3`; `116` = `A=7` `PL=4`; `117` = `A=7` `PL=5`; `118` = `A=7` `PL=6`; `119` = `A=7` `PL=7`; `120` = `A=7` `PL=8`; `121` = `A=7` `PL=9`; `122` = `A=7` `PL=10`; `123` = `A=7` `PL=11`; `124` = `A=7` `PL=12`; `125` = `A=7` `PL=13`; `126` = `A=7` `PL=14`; `127` = `A=7` `PL=15`; `128` = `A=8` `PL=0`; `129` = `A=8` `PL=1`; `130` = `A=8` `PL=2`; `131` = `A=8` `PL=3`; `132` = `A=8` `PL=4`; `133` = `A=8` `PL=5`; `134` = `A=8` `PL=6`; `135` = `A=8` `PL=7`; `136` = `A=8` `PL=8`; `137` = `A=8` `PL=9`; `138` = `A=8` `PL=10`; `139` = `A=8` `PL=11`; `140` = `A=8` `PL=12`; `141` = `A=8` `PL=13`; `142` = `A=8` `PL=14`; `143` = `A=8` `PL=15`; `144` = `A=9` `PL=0`; `145` = `A=9` `PL=1`; `146` = `A=9` `PL=2`; `147` = `A=9` `PL=3`; `148` = `A=9` `PL=4`; `149` = `A=9` `PL=5`; `150` = `A=9` `PL=6`; `151` = `A=9` `PL=7`; `152` = `A=9` `PL=8`; `153` = `A=9` `PL=9`; `154` = `A=9` `PL=10`; `155` = `A=9` `PL=11`; `156` = `A=9` `PL=12`; `157` = `A=9` `PL=13`; `158` = `A=9` `PL=14`; `159` = `A=9` `PL=15`; `160` = `A=10` `PL=0`; `161` = `A=10` `PL=1`; `162` = `A=10` `PL=2`; `163` = `A=10` `PL=3`; `164` = `A=10` `PL=4`; `165` = `A=10` `PL=5`; `166` = `A=10` `PL=6`; `167` = `A=10` `PL=7`; `168` = `A=10` `PL=8`; `169` = `A=10` `PL=9`; `170` = `A=10` `PL=10`; `171` = `A=10` `PL=11`; `172` = `A=10` `PL=12`; `173` = `A=10` `PL=13`; `174` = `A=10` `PL=14`; `175` = `A=10` `PL=15` | `0` | Scenario module address |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15 | `0` | Destination level |
| `SCE_BUTT_1` | `1..16` | `1` | Upper button scenario |
| `SCE_BUTT_2` | `1..16` | `2` | Lower button scenario |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `43` = 43 s; `44` = 44 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for upper button |
| `DEL_BUTTON_2` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `36` = 36 s; `37` = 37 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `69` = 9 min; `70` = 10 min | `0` | Activation delay for lower button |

### Object `404` - Scheduled scenario (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `BUTTON_1` | `0..31` | `1` | Upper button |
| `BUTTON_2` | `0..31` | `2` | Lower button |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input AUX channel |
| `START_DELAY` | `0..255` | `10` | Time of restart device (s) |

### Object `405` - Scenario PLUS Lighting Management (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_SCE_1` | `1..255` | `1` | Upper button scenario; Delay (20) |
| `PPT_SCE_2` | `1..255` | `2` | Lower button scenario; Delay (21) |
| `TYPE_OF_REGULATION` | `0` = Regulate all; `1` = Lights only; `2` = Shutters only; `3` = Stereo amplifiers only | `0` | Regulation type; Only if Scenario1=Scenario2 |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for upper button; Only if Scenario1<>Scenario2 |
| `DEL_BUTTON_2` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for lower button; Only if Scenario1<>Scenario2 |

### Object `407` - AUX control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `9` = `ON`/`OFF` and point to point dimming; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `12` = Bistable control; `13` = Monostable control; `4` = Reset BI; `5` = Reset TRI; `6` = Reset `GEN`; `1` = Disable (lower button); `2` = Enable (lower button); `3` = Disable (upper button) - enable (lower button) | `0` | Modality |
| `OUT_AUX_CH` | `1..15` | `1` | AUX channel |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input AUX channel |

### Object `409` - Sound diffusion control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `3` = General | `0` | Addressing type |
| `A` | `0..9` | `0` | Area |
| `PF` | `0..9` | `0` | Audio point |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input AUX channel |
| `IS_FOLLOW_ME` | `0` = No; `1` = Yes | `1` | Follow me |
| `SOURCE` | `1..9` | `1` | Source |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `743` | `400` | `3431` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `743` | `400` | `3432` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `743` | `400` | `3433` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `743` | `401` | `3236` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `743` | `401` | `3237` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `743` | `401` | `3238` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `743` | `402` | `3242` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `743` | `402` | `3243` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `743` | `402` | `3244` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `743` | `408` | `3245` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `743` | `427` | `3246` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `743` | `427` | `3695` | `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone (entire reusable range retained) | `0` | Segment |
| `743` | `430` | `3247` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `743` | `430` | `3696` | `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone (entire reusable range retained) | `0` | Segment |
| `743` | `430` | `4121` | `N2` | `0..15` (entire reusable range retained) | `0` | Associated Internal Unit address - hundreds |
| `743` | `430` | `4134` | `N1` | `100`; `101`; `102`; `103`; `104`; `105`; `106`; `107`; `108`; `109`; `110`; `111`; `112`; `113`; `114`; `115`; `116`; `117`; `118`; `119`; `120`; `121`; `122`; `123`; `124`; `125`; `126`; `127`; `128`; `129`; `130`; `131`; `132`; `133`; `134`; `135`; `136`; `137`; `138`; `139`; `140`; `141`; `142`; `143`; `144`; `145`; `146`; `147`; `148`; `149`; `150`; `151`; `152`; `153`; `154`; `155`; `156`; `157`; `158`; `159`; `160`; `161`; `162`; `163`; `164`; `165`; `166`; `167`; `168`; `169`; `170`; `171`; `172`; `173`; `174`; `175`; `176`; `177`; `178`; `179`; `180`; `181`; `182`; `183`; `184`; `185`; `186`; `187`; `188`; `189`; `190`; `191`; `192`; `193`; `194`; `195`; `196`; `197`; `198`; `199`; `200`; `201`; `202`; `203`; `204`; `205`; `206`; `207`; `208`; `209`; `210`; `211`; `212`; `213`; `214`; `215`; `216`; `217`; `218`; `219`; `220`; `221`; `222`; `223`; `224`; `225`; `226`; `227`; `228`; `229`; `230`; `231`; `232`; `233`; `234`; `235`; `236`; `237`; `238`; `239`; `240`; `241`; `242`; `243`; `244`; `245`; `246`; `247`; `248`; `249`; `250`; `251`; `252`; `253`; `254`; `255` | `0` | Internal unit address; reusable default `0` is outside this subset; filter supplies no replacement default |
| `743` | `143` | `3412` | `LED_LEVEL_COMMANDS` | `0` = `OFF`; `1` = Minimum level; `2` = Medium level; `3` = Maximum level (entire reusable range retained) | `2` | LED intensity level |
| `743` | `143` | `3659` | `PRESENCE_LED_INTENSITY_LEVEL_COMMAND` | `0` = Standard level; `1` = High intensity level (entire reusable range retained) | `0` | Presence LED intensity level |
| `743` | `143` | `3660` | `ENABLE_DISABLE_LED_COMMAND` | `1` = Presence Led Enabled - State Update Led Disable | `0` | Enable-Disable LED; reusable default `0` is outside this subset; filter supplies no replacement default |
| `743` | `145` | `3424` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `743` | `145` | `3425` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `743` | `145` | `3426` | `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety (entire reusable range retained) | `1` | Priority |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

### Address and LED restriction conflicts

Stair-light Object `430` has filter `4134` restricting `N1` to 100–255 while its reusable default is `0`; the exact physical sheet describes two-digit 0–99 virtual handset addressing. These are different source scopes and the default is outside the attached subset. UI Object `143` filter `3660` admits only value `1` (presence LED on, state-update LED disabled) while its reusable default is `0`. Neither filter supplies a replacement default. Shutter Object `145` DEST_LEV omits value 14 even though other Objects include it; its full-domain filter retains that omission. No missing value or precedence is invented.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `88` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `401` - Automation control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `402` - Lock / unlock actuator control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `406` - Scheduled scenario PLUS | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `463` - Load control actuator visualization | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `408` - Open lock control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `427` - Floor call control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `430` - Staircase light control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `143` - User interface settings for command | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `400` - Light control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `145` - Shutter control (2 slots) | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `401` - Automation control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `402` - Lock / unlock actuator control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `406` - Scheduled scenario PLUS | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `406` - Scheduled scenario PLUS | Burglar alarm system | `3` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `406` - Scheduled scenario PLUS | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `406` - Scheduled scenario PLUS | Sound system | `5` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `463` - Load control actuator visualization | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `463` - Load control actuator visualization | New energy saving and load control | `20` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `408` - Open lock control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `408` - Open lock control | Burglar alarm system | `3` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `408` - Open lock control | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `408` - Open lock control | Sound system | `5` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `427` - Floor call control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `427` - Floor call control | Burglar alarm system | `3` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `427` - Floor call control | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `427` - Floor call control | Sound system | `5` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `430` - Staircase light control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `430` - Staircase light control | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `430` - Staircase light control | Sound system | `5` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `143` - User interface settings for command | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `143` - User interface settings for command | New energy saving and load control | `20` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `400` - Light control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `400` - Light control | Burglar alarm system | `3` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `400` - Light control | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `400` - Light control | Sound system | `5` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `145` - Shutter control (2 slots) | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

### Related functional reference families

The correspondence below is a semantic cross-reference based on the named role and the canonical functional reference; it does not assert captured frames or support for every operation.

| Catalogue role | Related canonical reference | Evidence limit |
| --- | --- | --- |
| `400` | [Lighting](../../functional/who-1-lighting/) | Related canonical semantics for the named role; exact configured operation and runtime transport remain to be corroborated |
| `145`, `401` | [Automation](../../functional/who-2-automation/) | Related canonical semantics for the named role; exact configured operation and runtime transport remain to be corroborated |
| `463` | [Energy and load management](../../functional/who-18-energy-management/) | Related canonical semantics for the named role; exact configured operation and runtime transport remain to be corroborated |
| Video-entry-related roles | [Basic video entry](../../functional/who-6-basic-video-door-entry/);[Video entry and telephony](../../functional/who-8-video-door-entry-telephony/) | Related canonical families; which namespace and operation applies to each installed component is not established by the product manual alone |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The current sheet documents physical and MyHOME Suite configuration and refers to Home+Project (printed/PDF pp. 2-4). Point addressing uses A1/`A2=1..9` and PL1/`PL2=1..9` physically, versus room `0..10` and point `0..15` virtually. Room / group / general commands use `AMB`/`GR`/`GEN`; virtual groups 1..255. Separate M1/M2 sockets select cyclic, `ON`, `OFF`, `PUL` and dimming modes. Shutter position control, actuator lock / unlock and load-control visualisation require virtual configuration. Hold the LED button more than 2 seconds to toggle always-on / off indication, releasing to confirm.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

K4652M2 is a bus command, not a mains switching actuator: load ratings on neighbouring K4672 products are excluded. The installation leaflet’s “connection without neutral” footnote does not establish a mains connection for this SCS device. LED adjustment holds the dedicated button more than two seconds and changes status every two seconds, released to confirm (both exact technical sheets p. 1). Published physical and virtual selector tables remain separate from reusable domains and unresolved selection metadata.

## Source reconciliation

The Italian ST_00000218_IT revision (19/07/2018) and 2018 multilingual installation leaflet establish the earlier physical product. The 2026 English sheet adds an explicit production condition to group feedback described in the earlier sheet; that feature is not assigned to all older hardware/Firmware. Physical width (two modules) differs from three catalogue Modules and ten candidate Object roles. Publisher attributes are classification evidence, not an exhaustive runtime support matrix.

The exact restriction table identifies reusable defaults outside a Firmware/Object subset. These are catalogue conflicts; no replacement default is inferred.

The export classifies the bus as radio frequency while stating non-bidirectional radio and SCS operation. These exporter classification fields do not establish a radio transceiver in the product; the exact technical sheet describes its SCS connector. Status / control through a system gateway is separate from an embedded voice or Internet interface.

The 2018 Italian sheet already mentions virtual room/group/general load-status return; the 2026 English sheet adds an explicit group-state production condition from `25W49`. Thus the later text adds an applicability restriction to an earlier statement, rather than proving that all earlier hardware lacked every form of feedback. The condition remains unresolved for any given physical unit and is not retroactively assigned to firmware `743`. The 2018 software prerequisite is MyHOME_Suite above `03.03.73` or MyHOME_Up firmware after `2.1` AND app after `2.2`; the server’s separate 2022 sheet uses OR in its Living Now note. These different source conditions remain literal and edition-scoped.

## Evidence limits and open work

Exact production batch and Firmware applicability of group feedback, full installed role assignment, cover / mounting completion and runtime feedback remain to be corroborated.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

### Linked sources outside reviewed evidence

These manufacturer-listed resources are visible discovery work. A listing establishes a source association; it does not establish that the payload was downloaded, verified or examined here.

| Resource | Manufacturer label | Discovery location | Review scope |
| --- | --- | --- | --- |
| `LGRP-01140-V01.01-EN.pdf` | PEP-EPD LGRP-01140-V01.01-EN  /  PDF (750 KB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/LGRP-01140-V01.01-EN.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `LGRP-01860-V01.01-EN.pdf` | PEP-EPD LGRP-01860-V01.01-EN  /  PDF (872 KB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/LGRP-01860-V01.01-EN.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Brochure Living_NOW 2M.pdf` | Brochure BRO-LNOW-2M  /  PDF (15.9 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Brochure%20Living_NOW%202M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Brochure Living_NOW 3M.pdf` | Brochure BRO-LNOW-3M  /  PDF (16.3 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Brochure%20Living_NOW%203M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Catalogue Living_NOW 2M.pdf` | Catalog Commercial Page CAT-LNOW-2M  /  PDF (23.1 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Catalogue%20Living_NOW%202M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Catalogue Living_NOW 3M.pdf` | Catalog Commercial Page CAT-LNOW-3M  /  PDF (22.5 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Catalogue%20Living_NOW%203M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0191-0200-2026-10-07.md#own-dev-0200)
