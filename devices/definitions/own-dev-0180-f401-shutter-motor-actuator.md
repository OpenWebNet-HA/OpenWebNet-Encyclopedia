# F401 shutter motor actuator

## Summary

F401 is a DIN-rail actuator for one shutter motor, using two interlocked relays and local up / down controls. With compatible advanced controls it can move the shutter to a stored preset position. Calibration records the opening and closing travel so remote position control can operate correctly.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0180` | Project identity |
| Technical description | F401 shutter motor actuator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `F401` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1570` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `31` | Main association; independent of project ID |
| Firmware definition | `191` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Actuators | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F401` | Established catalogue identity | Manufacturer database commercial record `1570` explicitly links this SKU to item `1570` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F401` | `8005543469699` | `F401-publisher-product-sheet.pdf` PDF p. 1; `F401-italian-product-sheet.pdf` PDF p. 1 |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `LE05557AC.pdf` | Instruction Use LE05557AC | LE05557AC-01PC-21W15; printed revision label | PDF pp. 1-4: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/f8/4f/f84f0ba7492cfb576028a0e137dc23baf30380130ad4612dec38763ce3c75fff.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/LE05557AC.pdf) |
| `MyHOME Technical Guide.pdf` | Installation Guide GUI-MHOME | GUI-MHOME; printed publication date not established; incidental older-sheet dates are not guide dates | F401 printed/PDF pp.47, 89, 93, 95, 99 and unnumbered wiring-example PDF p.58; HC/HS/HD4657M4 touch controls printed/PDF p.95. Other product sheets and their incidental dates do not date the whole guide or override exact-product limits. | [Archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MyHOME%20Technical%20Guide.pdf) |
| `ST-00001901-EN.pdf` | Technical Sheet ST-00001901-EN | ST-00001901-EN; 01/10/2024 | PDF pp. 1-3: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/7d/33/7d33b474f7951949d50023bc1e025d92450386d1857d5302a218e84e1bf9c9e3.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00001901-EN.pdf) |
| `F401-publisher-product-sheet.pdf` | Exact English product export | Publisher DATASHEET; 05.10.2026 | PDF pp. 1-3: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/8e/81/8e817a5676c4373d1793c324c9ba8a22368619a0e3242429370c0ff87eadd16d.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-F401&include_technical=1) |
| `F401-italian-product-sheet.pdf` | Exact Italian product export | Product export retrieved 05/10/2026; boilerplate compliance dates are not product publication dates | PDF pp. 1-1: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/f8/49/f8490dfd3dd79a1d5058cb0203b31a0c2b6ebee2e37d43d739c849325475fbe7.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F401) |
| `ST_00000897_IT.pdf` | Manufacturer Italian/installation document | ST_00000897_IT; 23/03/2021 | PDF pp. 1-3: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/59/91/5991446162831c57ebbeafa2ba9b509fcd85f3e27be09b016fbbeb8567b29af0.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/ST_00000897_IT.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1570`: complete extracted catalogue associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS nominal / operating supply | `27 Vdc / 18..27 Vdc` | `ST-00001901-EN` printed/PDF pp. 1-3; `ST_00000897_IT` pp. 1-3; `LE05557AC` calibration / wiring original |
| Maximum draw | `16 mA` | `ST-00001901-EN` printed/PDF pp. 1-3; `ST_00000897_IT` pp. 1-3; `LE05557AC` calibration / wiring original |
| Temperature | `0..40 °C` | `ST-00001901-EN` printed/PDF pp. 1-3; `ST_00000897_IT` pp. 1-3; `LE05557AC` calibration / wiring original |
| Load contact rating | `250 Vac, 2 A` | `ST-00001901-EN` printed/PDF pp. 1-3; `ST_00000897_IT` pp. 1-3; `LE05557AC` calibration / wiring original |
| Protection | `IP20; IK04` | `ST-00001901-EN` printed/PDF pp. 1-3; `ST_00000897_IT` pp. 1-3; `LE05557AC` calibration / wiring original |
| Mounting | `2 DIN modules` | `ST-00001901-EN` printed/PDF pp. 1-3; `ST_00000897_IT` pp. 1-3; `LE05557AC` calibration / wiring original |
| Local interface | `up/down buttons and LEDs; calibration/Push&Learn button and LED` | `ST-00001901-EN` printed/PDF pp. 1-3; `ST_00000897_IT` pp. 1-3; `LE05557AC` calibration / wiring original |
| Motor types | `standard automatic; standard manual; pulse motor` | `ST-00001901-EN` printed/PDF pp. 1-3; `ST_00000897_IT` pp. 1-3; `LE05557AC` calibration / wiring original |
| Preset requirement | `advanced shutter control; scenario module production after week 29-2012` | `ST-00001901-EN` printed/PDF pp. 1-3; `ST_00000897_IT` pp. 1-3; `LE05557AC` calibration / wiring original |
| Uncalibrated operation | `local buttons only; not manageable by control devices` | `ST-00001901-EN` printed/PDF pp. 1-3; `ST_00000897_IT` pp. 1-3; `LE05557AC` calibration / wiring original |

| Publisher rated power | `500 W; separate load-related publisher value,not SCS consumption` | `F401-publisher-product-sheet.pdf` p.1 |
| Publisher nominated advanced controls | `LN4660M2,H4660M2,AM5861M2; exact published reference list,not an exhaustive compatibility declaration` | `F401-publisher-product-sheet.pdf` p.1 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Frequency classifications and a negative connected-object classification do not establish the runtime transport or exclude control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system radio frequency | `No` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system LON | `No` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system Powernet | `No` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Other bus systems | `Other` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Radio frequency bidirectional | `No` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Mounting method | `DRA (DIN-rail adaptor)` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| With anti-theft / dismantling protection | `No` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| With bus connection | `Yes` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Number of actuation points | `1` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Number of buttons | `3` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| With LED indication | `Yes` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| With label area | `No` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| With display | `No` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Material | `Plastic` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Material quality | `Thermoplastic` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Surface protection | `Other` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Colour | `White` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| RAL-number (similar) | `9011` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Transparent | `No` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| With room temperature controller | `No` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| With IR sensor | `No` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Degree of protection (IP) | `IP20` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Min. depth of built-in installation box | `55 mm` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Width | `36 mm` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Height | `105 mm` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Depth | `31 mm` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| degree of impact strength (IK) | `IK04` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Operating / setting temperature (Min-Max) | `0-40 °C` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Storage temperature (Min-Max) | `-10-70 °C` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Frequency (Min-Max) | `0-0 Hz` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Standby consumption | `5 mA` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Terminal marking indication | `Yes` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Antimicrobial treatment | `No` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Terminals capacity (Min-Max) | `0.5-2.5 mm²` | `F401-publisher-product-sheet.pdf` PDF p. 2 |
| Cable nature for connection | `Flexible or rigid` | `F401-publisher-product-sheet.pdf` PDF p. 3 |
| Label space / information surface | `No` | `F401-publisher-product-sheet.pdf` PDF p. 3 |
| Addressable | `Yes` | `F401-publisher-product-sheet.pdf` PDF p. 3 |
| Contains Batteries | `No` | `F401-publisher-product-sheet.pdf` PDF p. 3 |
| Connected object | `No` | `F401-publisher-product-sheet.pdf` PDF p. 3 |
| Operating method | `SCS` | `F401-publisher-product-sheet.pdf` PDF p. 3 |
| With voice command | `No` | `F401-publisher-product-sheet.pdf` PDF p. 3 |
| Programmable | `Yes` | `F401-publisher-product-sheet.pdf` PDF p. 3 |
| Interoperable connection Protocol | `No` | `F401-publisher-product-sheet.pdf` PDF p. 3 |
| Connectable by Internet box | `No` | `F401-publisher-product-sheet.pdf` PDF p. 3 |
| Product use function | `Shutter management` | `F401-publisher-product-sheet.pdf` PDF p. 3 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1570` | Canonical catalogue |
| Technical item description | Shutter actuator DIN 1 motor bus | Canonical catalogue |
| Item family | Source placeholder description `0`; key `2` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `31` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `191` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `191` | `1` | `218` Shutter actuator | Fixed / designated metadata | `662` | `514` | `458` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `191` | Virtual Configuration | `1` | Association key `1` |
| `191` | Advanced Configuration | `2` | Association key `2` |
| `191` | Physical configuration | `0` | Association key `3` |

No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

### Manufacturer configuration and operating settings

Published product selectors and software settings are separate from catalogue mode IDs. Their domains, defaults and topology limits do not replace Firmware-specific filters.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `Physical A / PL / G` | `1..9` /`1..9` /`0..9` | `ST-00001901-EN` printed/PDF pp. 1-3; `LE05557AC` PDF pp. 1-4 |
| `Virtual A / PL / groups` | Room `0..10`; point `0..15`; groups `1..10` each `0..255` | `ST-00001901-EN` printed/PDF pp. 1-3; `LE05557AC` PDF pp. 1-4 |
| `M=0 / SLA / PUL` | Master / slave following same-address master / monostable master ignoring room / general commands | `ST-00001901-EN` printed/PDF pp. 1-3; `LE05557AC` PDF pp. 1-4 |
| `Slave PUL / preset / pulse durations` | Software configuration required | `ST-00001901-EN` printed/PDF pp. 1-3; `LE05557AC` PDF pp. 1-4 |
| `Type absent / Type=1 / Type=2` | Standard automatic calibration / standard manual calibration / pulse motor | `ST-00001901-EN` printed/PDF pp. 1-3; `LE05557AC` PDF pp. 1-4 |
| `Type=2 with Pre=9` | STOP when idle moves to third limit switch | `ST-00001901-EN` printed/PDF pp. 1-3; `LE05557AC` PDF pp. 1-4 |
| `Calibration / local controls` | Uncalibrated device responds to local buttons only; hold setup≥3 s then UP to begin; automatic up / down / up travel or manually marked endpoints | `ST-00001901-EN` printed/PDF pp. 1-3; `LE05557AC` PDF pp. 1-4 |
| `Preset applicability` | Compatible advanced control; F420 production after week 29-2012; blade adjustment guarantee requires pulse motor | `ST-00001901-EN` printed/PDF pp. 1-3; `LE05557AC` PDF pp. 1-4 |
| `Channel / positions` | Current sheet says MyHOME Server configures one channel; calibrated standard role allows 100 positions; public documentation capability; installed position resolution uncorroborated | `ST-00001901-EN` printed/PDF pp. 1-3; `LE05557AC` PDF pp. 1-4 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `191` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `191` | `A` | `0..9` | `0` | A; Enviroment |
| `191` | `PL` | `0..9` | `0` | PL; Light Point |
| `191` | `M` | `0`; `11` = `SLA`; `15` = `PUL` | `0` | M; MODE |
| `191` | `TYPE` | `0..2` | `0` | SHUTTER_TYPE; Shutter type |
| `191` | `G1` | `0..9` | `0` | G1; Group 1 |
| `191` | `G2` | `0..9` | `0` | G2; Group 2 |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `218` - Shutter actuator

Catalogue Object key `514` maps to external Object `218`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master standard mode; `11` = Slave standard mode; `15` = `PUL` mode master; `16` = `PUL` mode slave | `0` | Modality; Mode shutter actuator |
| `SHUTTER_TYPE` | `0` = Standard automatic without slats; `1` = Standard without slats; `2` = Pulse without slats; `3` = Standard with slats | `0` | Motor type; Shutter type |
| `STOP_PULSE_DURATION` | `1` = 0.1 s; `2` = 0.2 s; `3` = 0.3 s; `4` = 0.4 s; `5` = 0.5 s; `6` = 0.6 s; `7` = 0.7 s; `8` = 0.8 s; `9` = 0.9 s; `10` = 1 s; `11` = 1.1 s; `12` = 1.2 s; `13` = 1.3 s; `14` = 1.4 s; `15` = 1.5 s; `16` = 1.6 s; `17` = 1.7 s; `18` = 1.8 s; `19` = 1.9 s; `20` = 2 s; `21` = 2.1 s; `22` = 2.2 s; `23` = 2.3 s; `24` = 2.4 s; `25` = 2.5 s; `26` = 2.6 s; `27` = 2.7 s; `28` = 2.8 s; `29` = 2.9 s; `30` = 3 s; `31` = 3.1 s; `32` = 3.2 s; `33` = 3.3 s; `34` = 3.4 s; `35` = 3.5 s; `36` = 3.6 s; `37` = 3.7 s; `38` = 3.8 s; `39` = 3.9 s; `40` = 4 s; `41` = 4.1 s; `42` = 4.2 s; `43` = 4.3 s; `44` = 4.4 s; `45` = 4.5 s; `46` = 4.6 s; `47` = 4.7 s; `48` = 4.8 s; `49` = 4.9 s; `50` = 5 s; `51` = 5.1 s; `52` = 5.2 s; `53` = 5.3 s; `54` = 5.4 s; `55` = 5.5 s; `56` = 5.6 s; `57` = 5.7 s; `58` = 5.8 s; `59` = 5.9 s; `60` = 6 s; `61` = 6.1 s; `62` = 6.2 s; `63` = 6.3 s; `64` = 6.4 s; `65` = 6.5 s; `66` = 6.6 s; `67` = 6.7 s; `68` = 6.8 s; `69` = 6.9 s; `70` = 7 s; `71` = 7.1 s; `72` = 7.2 s; `73` = 7.3 s; `74` = 7.4 s; `75` = 7.5 s; `76` = 7.6 s; `77` = 7.7 s; `78` = 7.8 s; `79` = 7.9 s; `80` = 8 s; `81` = 8.1 s; `82` = 8.2 s; `83` = 8.3 s; `84` = 8.4 s; `85` = 8.5 s; `86` = 8.6 s; `87` = 8.7 s; `88` = 8.8 s; `89` = 8.9 s; `90` = 9 s; `91` = 9.1 s; `92` = 9.2 s; `93` = 9.3 s; `94` = 9.4 s; `95` = 9.5 s; `96` = 9.6 s; `97` = 9.7 s; `98` = 9.8 s; `99` = 9.9 s; `100` = 10 s | `1` | Stop pulse duration; Duration pulse of stop |
| `UP_OR_DOWN_PULSE_DURATION` | `1` = 0.1 s; `2` = 0.2 s; `3` = 0.3 s; `4` = 0.4 s; `5` = 0.5 s; `6` = 0.6 s; `7` = 0.7 s; `8` = 0.8 s; `9` = 0.9 s; `10` = 1 s; `11` = 1.1 s; `12` = 1.2 s; `13` = 1.3 s; `14` = 1.4 s; `15` = 1.5 s; `16` = 1.6 s; `17` = 1.7 s; `18` = 1.8 s; `19` = 1.9 s; `20` = 2 s; `21` = 2.1 s; `22` = 2.2 s; `23` = 2.3 s; `24` = 2.4 s; `25` = 2.5 s; `26` = 2.6 s; `27` = 2.7 s; `28` = 2.8 s; `29` = 2.9 s; `30` = 3 s; `31` = 3.1 s; `32` = 3.2 s; `33` = 3.3 s; `34` = 3.4 s; `35` = 3.5 s; `36` = 3.6 s; `37` = 3.7 s; `38` = 3.8 s; `39` = 3.9 s; `40` = 4 s; `41` = 4.1 s; `42` = 4.2 s; `43` = 4.3 s; `44` = 4.4 s; `45` = 4.5 s; `46` = 4.6 s; `47` = 4.7 s; `48` = 4.8 s; `49` = 4.9 s; `50` = 5 s; `51` = 5.1 s; `52` = 5.2 s; `53` = 5.3 s; `54` = 5.4 s; `55` = 5.5 s; `56` = 5.6 s; `57` = 5.7 s; `58` = 5.8 s; `59` = 5.9 s; `60` = 6 s; `61` = 6.1 s; `62` = 6.2 s; `63` = 6.3 s; `64` = 6.4 s; `65` = 6.5 s; `66` = 6.6 s; `67` = 6.7 s; `68` = 6.8 s; `69` = 6.9 s; `70` = 7 s; `71` = 7.1 s; `72` = 7.2 s; `73` = 7.3 s; `74` = 7.4 s; `75` = 7.5 s; `76` = 7.6 s; `77` = 7.7 s; `78` = 7.8 s; `79` = 7.9 s; `80` = 8 s; `81` = 8.1 s; `82` = 8.2 s; `83` = 8.3 s; `84` = 8.4 s; `85` = 8.5 s; `86` = 8.6 s; `87` = 8.7 s; `88` = 8.8 s; `89` = 8.9 s; `90` = 9 s; `91` = 9.1 s; `92` = 9.2 s; `93` = 9.3 s; `94` = 9.4 s; `95` = 9.5 s; `96` = 9.6 s; `97` = 9.7 s; `98` = 9.8 s; `99` = 9.9 s; `100` = 10 s | `1` | UP or DOWN pulse duration; Pulse duration of UP or Down |
| `TILTING` | `1..100` | `70` | Tilting to rolling switch pulse duration; Only for pulse mode. |
| `ROLLING` | `1..100` | `70` | Rolling to tilting switch pulse duration; Only for pulse mode. |
| `LOCAL_BUTTON` | `0` = Bistable control; `1` = Monostable control; `2` = Blades control and Bistable; `3` = Bistable and blades control | `0` | Modality; Local button mode for Shutter managemant 4661M2 |
| `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety | `1` | Priority; Shutter management command priority |
| `PRESET_NUMBER` | `1..10`; `0` = None | `0` | Preset; Shutter management preset number |
| `P1` | `0..100` | `10` | Preset of position P1 |
| `P2` | `0..100` | `20` | Preset of position P2 |
| `P3` | `0..100` | `30` | Preset of position P3 |
| `P4` | `0..100` | `40` | Preset of position P4 |
| `P5` | `0..100` | `50` | Preset of position P5 |
| `P6` | `0..100` | `60` | Preset of position P6 |
| `P7` | `0..100` | `70` | Preset of position P7 |
| `P8` | `0..100` | `80` | Preset of position P8 |
| `P9` | `0..100` | `90` | Preset of position P9 |
| `P10` | `0..100` | `100` | Preset of position P10 |
| `UP_SHUTTER_TIME_MINUTES` | `0..9` | `0` | UP shutter calbration time (m) |
| `UP_SHUTTER_TIME_SECONDS` | `0..59` | `0` | UP shutter calbration time (s) |
| `DOWN_SHUTTER_TIME_MINUTES` | `0..9` | `0` | DOWN shutter calbration time (m) |
| `DOWN_SHUTTER_TIME_SECONDS` | `0..59` | `0` | DOWN shutter calbration time (s) |
| `SLATS_ROTATION_TIME_DOWN_H` | `0..27` | `0` | SLATS ROTATION calibration time when shutter is all the way down - HIGH BYTE (ms) |
| `SLATS_ROTATION_TIME_DOWN_L` | `0..255` | `0` | SLATS ROTATION calibration time when shutter is all the way down - LOW BYTE (ms) |
| `SLATS_ROTATION_TIME_MIDDLE_H` | `0..27` | `0` | SLATS ROTATION calibration time when shutter is in middle position - HIGH BYTE (ms); If not intentionally modified, par 0x20 = par 30 |
| `SLATS_ROTATION_TIME_MIDDLE_L` | `0..255` | `0` | SLATS ROTATION calibration time when shutter is in middle position - LOW BYTE (ms); If not intentionally modified, par 0x21 = par 31 |
| `SLATS_ROTATION_STEP_NUMBER` | `3..100` | `4` | SLATS ROTATION step number |
| `G1` | `0..255` | `0` | Group 1; Group = 0 means no group |
| `G2` | `0..255` | `0` | Group 2; Group = 0 means no group |
| `G3` | `0..255` | `0` | Group 3; Group = 0 means no group |
| `G4` | `0..255` | `0` | Group 4; Group = 0 means no group |
| `G5` | `0..255` | `0` | Group 5; Group = 0 means no group |
| `G6` | `0..255` | `0` | Group 6; Group = 0 means no group |
| `G7` | `0..255` | `0` | Group 7; Group = 0 means no group |
| `G8` | `0..255` | `0` | Group 8; Group = 0 means no group |
| `G9` | `0..255` | `0` | Group 9; Group = 0 means no group |
| `G10` | `0..255` | `0` | Group 10; Group = 0 means no group |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `191` | `1` | `218` | `4911` | No textual predicate stored | `115` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `191` | `218` | `574` | `G` | `0..255` (entire reusable range retained) | `0` | local button; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `191` | `218` | `575` | `LOCAL_BUTTON` | `0` = Bistable control; `1` = Monostable control; `2` = Blades control and Bistable; `3` = Bistable and blades control (entire reusable range retained) | `0` | Local button mode for Shutter managemant 4661M2 |
| `191` | `218` | `576` | `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety (entire reusable range retained) | `1` | Shutter management command priority |
| `191` | `218` | `577` | `PRESET_NUMBER` | `1..10`; `0` = None (entire reusable range retained) | `0` | Shutter management preset number |
| `191` | `218` | `578` | `ROLLING` | `1..100` (entire reusable range retained) | `70` | Rolling to tilting switch pulse duration |
| `191` | `218` | `579` | `TILTING` | `1..100` (entire reusable range retained) | `70` | Tilting to rolling switch pulse duration |
| `191` | `218` | `580` | `P10` | `0..100` (entire reusable range retained) | `100` | Preset of position P10 |
| `191` | `218` | `4439` | `UP_SHUTTER_TIME_MINUTES` | `0..9` (entire reusable range retained) | `0` | UP shutter calbration time (m) |
| `191` | `218` | `4452` | `UP_SHUTTER_TIME_SECONDS` | `0..59` (entire reusable range retained) | `0` | UP shutter calbration time (s) |
| `191` | `218` | `4465` | `DOWN_SHUTTER_TIME_MINUTES` | `0..9` (entire reusable range retained) | `0` | DOWN shutter calbration time (m) |
| `191` | `218` | `4478` | `SLATS_ROTATION_TIME_DOWN_H` | `0..27` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is all the way down - HIGH BYTE (ms) |
| `191` | `218` | `4491` | `SLATS_ROTATION_TIME_DOWN_L` | `0..255` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is all the way down - LOW BYTE (ms) |
| `191` | `218` | `4504` | `SLATS_ROTATION_TIME_MIDDLE_H` | `0..27` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is in middle position - HIGH BYTE (ms) |
| `191` | `218` | `4517` | `SLATS_ROTATION_TIME_MIDDLE_L` | `0..255` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is in middle position - LOW BYTE (ms) |
| `191` | `218` | `4530` | `SLATS_ROTATION_STEP_NUMBER` | `3..100` (entire reusable range retained) | `4` | SLATS ROTATION step number |
| `191` | `218` | `4614` | `SHUTTER_TYPE` | `3` = Standard with slats | `0` | Motor type; reusable default `0` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `115` | `M=0` | `MODE` = `0`; `LOCAL_BUTTON` = `0` | `115` |
| `115` | `M=1` | `MODE` = `0`; `LOCAL_BUTTON` = `2` | `115` |
| `115` | `M=2` | `MODE` = `0`; `LOCAL_BUTTON` = `3` | `115` |
| `115` | `M=11` | `MODE` = `11`; `LOCAL_BUTTON` = `0` | `115` |
| `115` | `M=12` | `MODE` = `0`; `LOCAL_BUTTON` = `0` | `115` |
| `115` | `M=13` | `MODE` = `0`; `LOCAL_BUTTON` = `1` | `115` |
| `115` | `M=15` | `MODE` = `15`; `LOCAL_BUTTON` = `0` | `115` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `31` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `218` - Shutter actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `218` - Shutter actuator | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

### Related functional reference families

The correspondence below is a semantic cross-reference based on the named role and the canonical functional reference; it does not assert captured frames or support for every operation.

| Catalogue role | Related canonical reference | Evidence limit |
| --- | --- | --- |
| `218` | [Automation](../../functional/who-2-automation/) | Related canonical semantics for the named role; exact configured operation and runtime transport remain to be corroborated |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Physical A/PL addressing differs from software room / light-point domains. Standard motors default to automatic calibration, `Type=1` uses manual calibration and `Type=2` selects pulse motors. `Type=2` with `Pre=9` enables a third-limit-switch position when STOP is pressed at rest. Pulse duration and preset positions require software settings; slave `PUL` also requires software. Automatic calibration starts by holding configuration for at least 3 s then UP and traverses up / down / up to learn travel. If it cannot reverse automatically, use the documented manual `Type=1` procedure. Manual calibration marks fully open / closed transitions with DOWN/UP buttons; accuracy depends on correct endpoint detection. Connect neutral for a standard motor with mechanical limits; electronic-limit and pulse arrangements follow their own diagrams. Preset blade-position behavior is guaranteed only with the specified pulse motor. The 10 A protective breaker is separate from the 2 A relay rating.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The exact English/Italian sheets and LE05557AC retain the one-motor, two-interlocked-relay model. The current English product page / export says “flush mounted” while the F401 technical sheet and installation drawing establish a 2-DIN enclosure: preserve the conflicting classification without reinterpreting the physical mounting. The export’s 27 Vdc and 0.016 A rated supply / draw agree with the sheet’s 27 Vdc and16 mA maximum. Its 500 W value is a separate load-related publisher rating; it is not SCS consumption. The same export’s characteristic list and mounting attribute say DIN, contradicting its own flush-mounted title / description. One catalogue shutter Object is not two independent motor channels; interlocking is intrinsic to the documented one-motor role.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `LE05557AC.pdf` | PDF pp. 1-4: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. |
| `MyHOME Technical Guide.pdf` | F401 printed/PDF pp.47, 89, 93, 95, 99 and unnumbered wiring-example PDF p.58; HC/HS/HD4657M4 touch controls printed/PDF p.95. Other product sheets and their incidental dates do not date the whole guide or override exact-product limits. |
| `ST-00001901-EN.pdf` | PDF pp. 1-3: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. |
| `F401-publisher-product-sheet.pdf` | PDF pp. 1-3: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. |
| `F401-italian-product-sheet.pdf` | PDF pp. 1-1: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. |
| `ST_00000897_IT.pdf` | PDF pp. 1-3: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. |

The exact restriction table identifies reusable defaults outside a Firmware/Object subset. These are catalogue conflicts; no replacement default is inferred.

The shared MyHOME guide’s unnumbered PDF p.58 separately draws F401 AC-motor wiring and F411U2 DC-motor wiring. The latter’s `12..48 Vdc` motor allowance and zero-crossing instruction are not assigned to F401. Printed/PDF p.99 names K4652M2 as a current control pairing, extending the export’s named LN/H/AM control list without implying all generations are equivalent.

## Evidence limits and open work

Calibration precision, production-specific preset compatibility, mechanical / electronic / pulse motor behavior and observed diagnostics remain uncorroborated.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

### Discovered sources outside this review

These publisher-linked files were identified but are not used as retained evidence in this dossier. Firmware / installers and declarations remain separate evidence families. A listed URL does not establish payload identity, installed release or tested compatibility.

| Source | Remaining scope | Publisher provenance |
| --- | --- | --- |
| `Brochure Living_NOW 2M.pdf` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Brochure%20Living_NOW%202M.pdf) |
| `Brochure Living_NOW 3M.pdf` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Brochure%20Living_NOW%203M.pdf) |
| `Brochure MyHOME.pdf` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Brochure%20MyHOME.pdf) |
| `Catalogue Living_NOW 2M.pdf` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Catalogue%20Living_NOW%202M.pdf) |
| `Catalogue Living_NOW 3M.pdf` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Catalogue%20Living_NOW%203M.pdf) |

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
