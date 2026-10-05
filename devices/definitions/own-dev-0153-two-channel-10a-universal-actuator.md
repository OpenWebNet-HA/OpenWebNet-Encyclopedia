# Two-channel 10 A universal actuator

## Summary

F411U2 switches two independent lighting loads or interlocks its relays to drive one shutter motor. Zero-crossing control improves switching of compatible LED and fluorescent loads. It also provides local control and configurable power-restoration behavior.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0153` | Project identity |
| Technical description | Two-channel 10 A universal actuator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `003848`, `F411U2` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `2115` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `78` | Main association; independent of project ID |
| Firmware definition | `659` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `2` | Firmware metadata |
| Categories | Actuators, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `003848` | Established catalogue identity | Manufacturer database commercial record `2518` explicitly links this SKU to item `2115` |
| BTicino | `F411U2` | Established catalogue identity | Manufacturer database commercial record `2450` explicitly links this SKU to item `2115` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F411U2` | `8005543533871` | `F411U2-publisher-product-sheet.pdf` PDF p. 1 |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ST-00000893-EN.pdf` | Technical Sheet ST-00000893-EN | `ST-00000893-EN; 23/03/2021` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/f5/9a/f59a4f84982b8d0040f7824acbe4be8125f877d93d28aa6f8bf27fe4ec6892a0.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00000893-EN.pdf) |
| `ST-00002461-EN.pdf` | Technical Sheet ST-00002461-EN | `ST-00002461-EN; 10/10/2025` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/33/f1/33f1629776d7e18399846278bf533512d66169bf3f4c417eb5a0bd3df4d7d71b.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002461-EN.pdf) |
| `F411U2-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 05.10.2026` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/cf/87/cf879e27a57038b30f3dfa99faf2e33c061218f8ad90bd1aa2aa99fb54626ac3.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-F411U2&include_technical=1) |
| `F411U2-italian-product-sheet.pdf` | Exact Italian product export | `Captured 05/10/2026; compliance-template date does not establish product publication date` | PDF pp. 1-1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/ee/58/ee58f29189bd4487b54dedb5be2eeb3dd868e196cc18b2348405e10e4543952d.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F411U2) |
| `BT-F411U2-IT.pdf` | Legacy manufacturer technical documentation | `BT-F411U2-IT; printed publication date not established` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/ca/55/ca5508aadf551c57492c7553f2cc23f23ca6b9d713580b32ec941aab6288b36e.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/BT-F411U2-IT.pdf) |
| `ST_00000893_IT.pdf` | Legacy manufacturer technical documentation | `ST_00000893_IT; 23/03/2021` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/df/74/df7470db3704d79ba75a0f7d720ccac6a59995a214a1a1a2a740f317606d5b7b.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/ST_00000893_IT.pdf) |
| `ST_00000893_EN.pdf` | English counterpart of manufacturer-linked document | `ST_00000893_EN; 23/03/2021` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/f5/9a/f59a4f84982b8d0040f7824acbe4be8125f877d93d28aa6f8bf27fe4ec6892a0.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/ST_00000893_EN.pdf) |
| `ST-00002703-EN.pdf` | Technical Sheet ST-00002703-EN | `ST-00002703-EN; 16/06/2026` | Retained 19-page original; exact-product technical, configuration and operating sections reviewed where applicable. Source-specific facts and remaining limits are scoped in the dossier; this does not claim a line-by-line review of every manual page. | [Archived original](https://archive.openwebnet-ha.org/sha256/b2/f5/b2f5090b601e33cdef9ba666108848ff4d9800792ccd5b7c14385da300bf0ffa.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002703-EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2115`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS nominal / operating supply | `27 Vdc / 22..27 Vdc` | `ST-00002461-EN` printed/PDF pp. 1-4 |
| Standby / maximum draw | `5 mA / 55 mA independent / 30 mA interlocked` | `ST-00002461-EN` printed/PDF pp. 1-4 |
| Temperature / size | `0..40 °C; 2 DIN modules` | `ST-00002461-EN` printed/PDF pp. 1-4 |
| Outputs | `2 x 10 A` | `ST-00002461-EN` printed/PDF pp. 1-4 |
| Incandescent/halogen | `2300 W / 10 A at printed 250 Vac; 1100 W / 10 A at 110 Vac` | `ST-00002461-EN` printed/PDF pp. 1-4 |
| LED / CFL | `500 W / 2 A at 250 Vac; 250 W / 2 A at 110 Vac; maximum 10 lamps with neutral connected` | `ST-00002461-EN` printed/PDF pp. 1-4 |
| Linear fluorescent / electronic transformer | `920 W / 4 A at 250 Vac; 440 W / 4 A at 110 Vac` | `ST-00002461-EN` printed/PDF pp. 1-4 |
| Ferromagnetic transformer | `920 VA / 4 A cos phi 0.5 at 250 Vac; 440 VA / 4 A at 110 Vac` | `ST-00002461-EN` printed/PDF pp. 1-4 |
| Protection codes | `IP20; IK40 printed in 2025 sheet, not silently corrected` | `ST-00002461-EN` printed/PDF pp. 1-4 |
| Shutter motor | `460 W / 2 A at 250 Vac; 250 W / 2 A at 110 Vac` | `ST-00002461-EN` printed/PDF pp. 1-4 |


### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Classification frequency values of zero are separate from explicitly documented Wi-Fi carriers; a negative connected-object classification does not exclude remote control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system radio frequency | `No` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system LON | `No` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system Powernet | `No` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |
| Other bus systems | `None` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |
| Mounting method | `Other` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |
| Width in number of modular spacings | `2` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |
| Local operation/hand operation | `Yes` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |
| With LED indication | `Yes` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |
| Number of digital inputs | `1` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |
| Max. switching power | `1000 W` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |
| Max. number of switching contacts | `4` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |
| Rated operating voltage (Min- Max) | `27-27 V` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |
| With bus connection | `No` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |
| Degree of protection (IP) | `IP20` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |
| Connected object | `No` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |
| Product use function | `Lighting management` | `F411U2-publisher-product-sheet.pdf` PDF p. 2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2115` | Canonical catalogue |
| Technical item description | 2x10A actuator, 2DIN | Canonical catalogue |
| Item family | 0; key `2` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `78` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `659` | `1` | `0` | No build row | `2` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `659` | `1` | `6` Light actuator | Fixed/designated metadata | `2487` | `6` | `1138` |
| `659` | `1` | `7` Automation actuator | Candidate alternative | `2486` | `7` | `1137` |
| `659` | `2` | `6` Light actuator | Fixed/designated metadata | `2488` | `6` | `1138` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `659` | `510` Automation relay virgin | `1`, `2` | `1`, `6`, `7` | `510` | `52` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `659` | Virtual Configuration | `1` | Association key `1` |
| `659` | Advanced Configuration | `2` | Association key `2` |
| `659` | Physical configuration | `0` | Association key `3` |


No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `A / PL1 / PL2` | lighting addresses; `PL1=PL2` interlocks motor relays | `ST-00002461-EN` printed/PDF pp. 1-4 |
| `M=0 / SLA / PUL` | master / slave / monostable master | `ST-00002461-EN` printed/PDF pp. 1-4 |
| `Lighting M=1..4` | slave `OFF` delay `1..4` min; virtual `0..255` s | `ST-00002461-EN` printed/PDF pp. 1-4 |
| `Motor M=0,1,2,3,4` | stop after 1,2,5,10 min; indefinite until next command | `ST-00002461-EN` printed/PDF pp. 1-4 |
| `Motor M=5,6,7,8,9` | stop after 20,10,5,15,30 s | `ST-00002461-EN` printed/PDF pp. 1-4 |
| `Load mode / restoration` | zero crossing and power-recovery contact state configured separately | `ST-00002461-EN` printed/PDF pp. 1-4 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `659` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `659` | `A` | `0..9` | `0` | Area |
| `659` | `PL1` | `0..9` | `0` | PL1 - (0-9) |
| `659` | `PL2` | `0..9` | `0` | PL2 - (0-9) |
| `659` | `G1` | `0..255` | `0` | Group 1 |
| `659` | `MODE` | `0..9`; `11` = `SLA`; `15` = PLU | `0` | mode(0-9, sla ,plu); Mode 5-9 only for light |
| `659` | `C` | `0..1` | `0` | Zero crossing - Dry contact; For shutter only value 0 is valid |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `6` - Light actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality |
| `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open | `0` | Relay state on device reset |
| `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing | `0` | Load control mode |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `SUBTYPE` | `11` = Actuator; `1` = Lamp; `10` = Valve; `15` = Differential restart; `6` = Fan; `7` = Watering; `8` = Controlled socket; `9` = Lock | `11` | Type of load |
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


### Object `7` - Automation actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality |
| `LOCAL_BUTTON` | `12` = Bistable control; `13` = Monostable control; `14` = Bistable and blades control | `12` | Local button modality |
| `STOP_TIME` | `0` = Infinite; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min | `60` | Stop time |
| `SUBTYPE` | `11` = Actuator; `2` = Shutter; `3` = Curtain; `4` = Gate; `5` = Garage door; `15` = Differential restart | `11` | Type of load |
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
| `659` | `1` | `6` | `4147` | No textual predicate stored | `1` |
| `659` | `1` | `7` | `4702` | `PL2=PL1` | `2` |
| `659` | `2` | `6` | `4147` | No textual predicate stored | `1` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `659` | `6` | `2380` | `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `659` | `6` | `2381` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `659` | `6` | `2382` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `659` | `6` | `2383` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `659` | `7` | `2379` | `LOCAL_BUTTON` | `12` = Bistable control; `13` = Monostable control; `14` = Bistable and blades control (entire reusable range retained) | `12` | Local button modality |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `1` | `M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `1` |
| `1` | `M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `1` |
| `1` | `M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `1` |
| `2` | `M=0` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `60` | `2` |
| `2` | `M=1` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `62` | `2` |
| `2` | `M=2` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `65` | `2` |
| `2` | `M=3` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `70` | `2` |
| `2` | `M=4` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `0` | `2` |
| `2` | `M=5` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `20` | `2` |
| `2` | `M=6` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `10` | `2` |
| `2` | `M=7` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `5` | `2` |
| `2` | `M=8` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `15` | `2` |
| `2` | `M=9` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `30` | `2` |
| `2` | `M=I/O` | `LOCAL_BUTTON` = `13`; `M` = `0`; `STOP_TIME` = `60` | `2` |
| `2` | `M=PUL` | `LOCAL_BUTTON` = `12`; `M` = `15`; `STOP_TIME` = `60` | `2` |
| `2` | `M=SLA` | `LOCAL_BUTTON` = `12`; `M` = `11` | `2` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `78` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `7` - Automation actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `6` - Light actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |


These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system/model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Physical A/PL addressing uses `1..9`; Suite uses room `0..10` and lighting point 0..15. Physical group G uses `0..9`; Suite provides ten group fields 0..255. Master `M=0`, slave `M=SLA` and monostable master `M=PUL` are documented; `PUL` ignores room/general controls. Delayed slave `OFF` uses `M=1..4` minutes physically or `0..255` seconds in Suite, for point-to-point control only: the master switches off immediately, its slave after the delay. Slave `PUL` requires software. The stated load capacities require zero crossing and neutral connected; without them relay bonding may occur. The sheet’s 250 Vac column retains 2300 W/920 W values as printed rather than recalculating power. The local press switches the load. Suite exposes contact state at power recovery and additional role/local-button options. MyHOME Server automatically configures 2 channel(s). `PL1=PL2` interlocks the relays for an AC motor with two windings. Physical motor stop `M=0`/1/2/3/4/5/6/7/8/9 gives 1 min/2 min/5 min/10 min/infinite-until-next-command/20 s/10 s/5 s/15 s/30 s; software offers `1..60` s, `2..10` min and infinite. The 2025 sheet adds a dissipated-power formula P[mW]=140+400*N+10*(Ic1+Ic2), with N the loaded-relay count; its expression differs from older squared-current formulas and is retained as printed. The source’s 10 A breaker and at least 3 m load connection are wiring qualifications, not a different relay rating.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session/validation method remains in [Programming](../../programming/).

## Source reconciliation

Exact reference and Legrand alias are established by the database and shared manufacturer heading. The 2021 and 2025 F411U2 technical sheets are retained separately. The 2025 sheet prints IK40, whereas the older sheet must be applied by its own values; no production boundary or corrected IK value is assumed. The shared guide incorrectly calls F411U2 a four-relay actuator in its descriptive text but the exact sheets and terminal diagram establish two. The database has lighting Object `6` and automation Object `7` candidates, consistent with alternate physical roles. The 2026 EOS list uses a 16 A product label for these references, while the exact sheets describe 10 A and load-specific lower capacities. That label is not authority to raise every load rating.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `ST-00000893-EN.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `ST-00002461-EN.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `F411U2-publisher-product-sheet.pdf` | Exact named variant; complete classification attributes captured above and EAN under Commercial identities. Sheet-specific ratings remain independently scoped. |
| `F411U2-italian-product-sheet.pdf` | Exact named commercial/product export; values and descriptive defects reconciled against technical documents. Compliance-template dates do not date the product. |
| `BT-F411U2-IT.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `ST_00000893_IT.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `ST_00000893_EN.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `ST-00002703-EN.pdf` | Explicit compatibility/reference inventory and ecosystem restrictions for this product; EOS electrical/display specifications are not transferred. |

## Evidence limits and open work

Production-specific rating/IK discrepancies, zero-crossing and restoration behavior, load compatibility and diagnostic responses remain uncorroborated.

No installed hardware revision or microcontroller fingerprint is retained for this cluster. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Canonical catalogue extraction and reconciliation are complete for the retained evidence; further documentation discovery, runtime corroboration and final evidence closure remain partial.

### Discovered sources outside this review

These publisher-linked sources were identified but were not retained or used as evidence. Their presence is not evidence of installed firmware, a certified test result or additional capability.

| Source | Remaining scope | Publisher provenance |
| --- | --- | --- |
| `Brochure Living_NOW 2M.pdf` | Software licence, declaration or ancillary document; not used for product specifications here | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Brochure Living_NOW 2M.pdf) |
| `Brochure Living_NOW 3M.pdf` | Software licence, declaration or ancillary document; not used for product specifications here | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Brochure Living_NOW 3M.pdf) |
| `Brochure MyHOME.pdf` | Software licence, declaration or ancillary document; not used for product specifications here | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Brochure MyHOME.pdf) |
| `Catalogue Living_NOW 2M.pdf` | Software licence, declaration or ancillary document; not used for product specifications here | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Catalogue Living_NOW 2M.pdf) |
| `Catalogue Living_NOW 3M.pdf` | Software licence, declaration or ancillary document; not used for product specifications here | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Catalogue Living_NOW 3M.pdf) |

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
