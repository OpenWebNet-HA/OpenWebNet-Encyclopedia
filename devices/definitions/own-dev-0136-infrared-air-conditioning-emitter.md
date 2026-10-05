# Infrared air-conditioning emitter

## Summary

This compact infrared emitter brings compatible air-conditioning units into the SCS control system. It can learn infrared commands or use the documented advanced control configuration, with a separate transmitter lead positioned to reach the air conditioner's receiver.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0136` | Project identity |
| Technical description | Infrared air-conditioning emitter | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `3456`, `088301` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1520` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Temperature control | Main system association |
| Item model / `modobj` | `26` | Main association; independent of project ID |
| Firmware definition | `128` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Thermoregulation, Gateways and interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `3456` | Established catalogue identity | Manufacturer database commercial record `1157` explicitly links this SKU to item `1520` |
| Legrand | `088301` | Established catalogue identity | Manufacturer database commercial record `1728` explicitly links this SKU to item `1520` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00357-b-UK.pdf` | Technical Sheet MQ00357-B-UK | `MQ00357-b-UK; 17/12/2012` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-2; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/85/78/85788000ca03620c64639768465e28e7a45b4d1e92892fa64ef32c27a6ff4ba5.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MQ00357-b-UK.pdf) |
| `MQ00357-c-EN.pdf` | Technical Sheet MQ00357-C-EN | `MQ00357-c-EN; 05/06/2014` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-2; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/56/5c/565c6b83a0ff7f52beb3980f5fc102e2159e45b7f363926f5ef65e9b8832336b.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MQ00357-c-EN.pdf) |
| `MyHOME Technical Guide.pdf` | English system technical guide | `AD-EXMH25GT; Versione 6/2025 printed on rear cover` | Energy/load functions and installation topology: printed/PDF pp. 74-80, 90, 96, 101. No exact 3456/F450 match; no rating transferred to those products. | [Archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MyHOME Technical Guide.pdf) |
| `U4713A_S_EN.pdf` | Technical Guide U4713A_S_EN | `U4713A_S_EN; 07/10-01 PC` | Exact-product specifications, operating/configuration material and source limitations; retained 22-page original; relevant product sections reviewed. Printed pagination and 1-based PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/8c/ab/8cab26ca1a6b06d4f0dd5a1d96a2420c2e36b4dadef41c2992863c8f52368230.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/U4713A_S_EN.pdf) |
| `U4714B.pdf` | Instruction Use U4714B | `U4714B-01PC-12W46` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-2; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/4c/2c/4c2c63a2a0a44692284f3a160dad650499fb3fd880a956f982d5eb3777aac580.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/U4714B.pdf) |
| `3456-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 04.10.2026` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-3; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/8d/1b/8d1b557543aef5e5b9c6bfc3215993e5505706a42631ba778fe322b68a226091.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-3456&include_technical=1) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `1520` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply | `18..27 Vdc` | `MQ00357-b-UK` pp. 1-2; `MQ00357-c-EN` pp. 1-2 |
| Standby / transmitting draw | `15 mA / 25 mA peak` | `MQ00357-b-UK` pp. 1-2; `MQ00357-c-EN` pp. 1-2 |
| Operating temperature | `5..40 °C` | `MQ00357-b-UK` pp. 1-2; `MQ00357-c-EN` pp. 1-2 |
| Mounting | `basic module; behind wiring devices, distribution box or inside split unit` | `MQ00357-b-UK` pp. 1-2; `MQ00357-c-EN` pp. 1-2 |
| IR transmitter lead | `2 m` | `MQ00357-b-UK` pp. 1-2; `MQ00357-c-EN` pp. 1-2 |
| Configurator sockets | `ZA/A; ZB/PL; N; M` | `MQ00357-b-UK` pp. 1-2; `MQ00357-c-EN` pp. 1-2 |
| Basic acquisition capacity | `20 IR commands` | `MQ00357-b-UK` pp. 1-2; `MQ00357-c-EN` pp. 1-2 |
| Advanced temperature selection | `16..30 °C` | `MQ00357-b-UK` pp. 1-2; `MQ00357-c-EN` pp. 1-2 |
| Advanced operating modes | `auto; heating; cooling; dry; fan` | `MQ00357-b-UK` pp. 1-2; `MQ00357-c-EN` pp. 1-2 |
| Advanced fan / swing | `auto/minimum/medium/maximum; swing ON/OFF` | `MQ00357-b-UK` pp. 1-2; `MQ00357-c-EN` pp. 1-2 |


### Publisher export attributes

These are the captured publisher classification values for the named variants. They do not override a technical sheet’s ratings or prove runtime protocol support. A negative radio-bus/connected-object classification is not evidence against separately documented gateway or Wi-Fi behavior.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| EAN | `8005543400944` | `3456` export p. 1 |
| Bus system KNX | `No` | `3456` export p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `3456` export p. 2 |
| Bus system radio frequency | `No` | `3456` export p. 2 |
| Bus system LON | `No` | `3456` export p. 2 |
| Bus system Powernet | `No` | `3456` export p. 2 |
| Other bus systems | `Other` | `3456` export p. 2 |
| Model | `IR-interface` | `3456` export p. 2 |
| Mounting method | `Surface mounted` | `3456` export p. 2 |
| Demounting protection | `No` | `3456` export p. 2 |
| With LED indication | `No` | `3456` export p. 2 |
| Updateable | `No` | `3456` export p. 2 |
| Operating voltage (Min-Max) | `27-27 V` | `3456` export p. 2 |
| Protocol | `Other` | `3456` export p. 2 |
| Provider dependent | `No` | `3456` export p. 2 |
| Visualization | `No` | `3456` export p. 2 |
| Web-Server | `No` | `3456` export p. 2 |
| Radio interface | `Yes` | `3456` export p. 2 |
| IR interface | `Yes` | `3456` export p. 2 |
| Degree of protection (IP) | `IP21` | `3456` export p. 2 |
| Type of load | `Not applicable` | `3456` export p. 2 |
| Connection type | `Screwed terminal` | `3456` export p. 2 |
| Product use function | `Thermal comfort management` | `3456` export p. 2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1520` | Canonical catalogue |
| Technical item description | IR emitter | Canonical catalogue |
| Item family | 0; key `100` | Canonical catalogue |
| Main system | Temperature control; key `2` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `26` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |
| Additional system | Automation; key `1`; model `26` | Separate non-main catalogue association |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `128` | `1` | `0` | `0` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `128` | `1` | `195` IR self-learning split control | Candidate alternative | `735` | `471` | `504` |
| `128` | `1` | `196` IR complete split control | Fixed/designated metadata | `736` | `472` | `505` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `128` | `522` IR split control virgin | `1` | `195`, `196` | `522` | `2` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `128` | Virtual Configuration | `1` | Association key `1` |
| `128` | Advanced Configuration | `2` | Association key `2` |
| `128` | Physical configuration | `0` | Association key `3` |
| `128` | Product Programming | `3` | Association key `4` |


| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `128` | USB | `3` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `128` | `1` | `0` | `IRSplit_0100` | Parameter type `7`; payload not inspected |
| `128` | `2` | `0` | `IRSplit_0100` | Parameter type `7`; payload not inspected |


Brand/line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `128` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `128` | `ZA/A` | `0..9` | `0` | ZA/A |
| `128` | `ZB/PL` | `0..9` | `0` | ZB/PL |
| `128` | `N` | `0..9` | `1` | N; Device Number (1-9) 0=virgin or when m=1(autom) |
| `128` | `M` | `0..1` | `0` | M; mode (0/1) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `195` - IR self-learning split control

Catalogue Object key `471` maps to external Object `195`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |


### Object `196` - IR complete split control

Catalogue Object key `472` maps to external Object `196`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `1..9` | `1` | Device number |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `128` | `1` | `195` | `4955` | `M=1` | `7204` |
| `128` | `1` | `196` | `4914` | `M=0` | `7000` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | Not applicable | None | Not applicable | No relation-specific filters associated | Not applicable | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `7000` | `ZA/A=0; ZB/PL=1` | `ZAZB` = `1` | `7000` → `7001` |
| `7000` | `ZA/A=0; ZB/PL=2` | `ZAZB` = `2` | `7000` → `7001` |
| `7000` | `ZA/A=0; ZB/PL=3` | `ZAZB` = `3` | `7000` → `7001` |
| `7000` | `ZA/A=0; ZB/PL=4` | `ZAZB` = `4` | `7000` → `7001` |
| `7000` | `ZA/A=0; ZB/PL=5` | `ZAZB` = `5` | `7000` → `7001` |
| `7000` | `ZA/A=0; ZB/PL=6` | `ZAZB` = `6` | `7000` → `7001` |
| `7000` | `ZA/A=0; ZB/PL=7` | `ZAZB` = `7` | `7000` → `7001` |
| `7000` | `ZA/A=0; ZB/PL=8` | `ZAZB` = `8` | `7000` → `7001` |
| `7000` | `ZA/A=0; ZB/PL=9` | `ZAZB` = `9` | `7000` → `7001` |
| `7000` | `ZA/A=1; ZB/PL=0` | `ZAZB` = `10` | `7000` → `7002` |
| `7000` | `ZA/A=1; ZB/PL=1` | `ZAZB` = `11` | `7000` → `7002` |
| `7000` | `ZA/A=1; ZB/PL=2` | `ZAZB` = `12` | `7000` → `7002` |
| `7000` | `ZA/A=1; ZB/PL=3` | `ZAZB` = `13` | `7000` → `7002` |
| `7000` | `ZA/A=1; ZB/PL=4` | `ZAZB` = `14` | `7000` → `7002` |
| `7000` | `ZA/A=1; ZB/PL=5` | `ZAZB` = `15` | `7000` → `7002` |
| `7000` | `ZA/A=1; ZB/PL=6` | `ZAZB` = `16` | `7000` → `7002` |
| `7000` | `ZA/A=1; ZB/PL=7` | `ZAZB` = `17` | `7000` → `7002` |
| `7000` | `ZA/A=1; ZB/PL=8` | `ZAZB` = `18` | `7000` → `7002` |
| `7000` | `ZA/A=1; ZB/PL=9` | `ZAZB` = `19` | `7000` → `7002` |
| `7000` | `ZA/A=2; ZB/PL=0` | `ZAZB` = `20` | `7000` → `7003` |
| `7000` | `ZA/A=2; ZB/PL=1` | `ZAZB` = `21` | `7000` → `7003` |
| `7000` | `ZA/A=2; ZB/PL=2` | `ZAZB` = `22` | `7000` → `7003` |
| `7000` | `ZA/A=2; ZB/PL=3` | `ZAZB` = `23` | `7000` → `7003` |
| `7000` | `ZA/A=2; ZB/PL=4` | `ZAZB` = `24` | `7000` → `7003` |
| `7000` | `ZA/A=2; ZB/PL=5` | `ZAZB` = `25` | `7000` → `7003` |
| `7000` | `ZA/A=2; ZB/PL=6` | `ZAZB` = `26` | `7000` → `7003` |
| `7000` | `ZA/A=2; ZB/PL=7` | `ZAZB` = `27` | `7000` → `7003` |
| `7000` | `ZA/A=2; ZB/PL=8` | `ZAZB` = `28` | `7000` → `7003` |
| `7000` | `ZA/A=2; ZB/PL=9` | `ZAZB` = `29` | `7000` → `7003` |
| `7000` | `ZA/A=3; ZB/PL=0` | `ZAZB` = `30` | `7000` → `7004` |
| `7000` | `ZA/A=3; ZB/PL=1` | `ZAZB` = `31` | `7000` → `7004` |
| `7000` | `ZA/A=3; ZB/PL=2` | `ZAZB` = `32` | `7000` → `7004` |
| `7000` | `ZA/A=3; ZB/PL=3` | `ZAZB` = `33` | `7000` → `7004` |
| `7000` | `ZA/A=3; ZB/PL=4` | `ZAZB` = `34` | `7000` → `7004` |
| `7000` | `ZA/A=3; ZB/PL=5` | `ZAZB` = `35` | `7000` → `7004` |
| `7000` | `ZA/A=3; ZB/PL=6` | `ZAZB` = `36` | `7000` → `7004` |
| `7000` | `ZA/A=3; ZB/PL=7` | `ZAZB` = `37` | `7000` → `7004` |
| `7000` | `ZA/A=3; ZB/PL=8` | `ZAZB` = `38` | `7000` → `7004` |
| `7000` | `ZA/A=3; ZB/PL=9` | `ZAZB` = `39` | `7000` → `7004` |
| `7000` | `ZA/A=4; ZB/PL=0` | `ZAZB` = `40` | `7000` → `7005` |
| `7000` | `ZA/A=4; ZB/PL=1` | `ZAZB` = `41` | `7000` → `7005` |
| `7000` | `ZA/A=4; ZB/PL=2` | `ZAZB` = `42` | `7000` → `7005` |
| `7000` | `ZA/A=4; ZB/PL=3` | `ZAZB` = `43` | `7000` → `7005` |
| `7000` | `ZA/A=4; ZB/PL=4` | `ZAZB` = `44` | `7000` → `7005` |
| `7000` | `ZA/A=4; ZB/PL=5` | `ZAZB` = `45` | `7000` → `7005` |
| `7000` | `ZA/A=4; ZB/PL=6` | `ZAZB` = `46` | `7000` → `7005` |
| `7000` | `ZA/A=4; ZB/PL=7` | `ZAZB` = `47` | `7000` → `7005` |
| `7000` | `ZA/A=4; ZB/PL=8` | `ZAZB` = `48` | `7000` → `7005` |
| `7000` | `ZA/A=4; ZB/PL=9` | `ZAZB` = `49` | `7000` → `7005` |
| `7000` | `ZA/A=5; ZB/PL=0` | `ZAZB` = `50` | `7000` → `7006` |
| `7000` | `ZA/A=5; ZB/PL=1` | `ZAZB` = `51` | `7000` → `7006` |
| `7000` | `ZA/A=5; ZB/PL=2` | `ZAZB` = `52` | `7000` → `7006` |
| `7000` | `ZA/A=5; ZB/PL=3` | `ZAZB` = `53` | `7000` → `7006` |
| `7000` | `ZA/A=5; ZB/PL=4` | `ZAZB` = `54` | `7000` → `7006` |
| `7000` | `ZA/A=5; ZB/PL=5` | `ZAZB` = `55` | `7000` → `7006` |
| `7000` | `ZA/A=5; ZB/PL=6` | `ZAZB` = `56` | `7000` → `7006` |
| `7000` | `ZA/A=5; ZB/PL=7` | `ZAZB` = `57` | `7000` → `7006` |
| `7000` | `ZA/A=5; ZB/PL=8` | `ZAZB` = `58` | `7000` → `7006` |
| `7000` | `ZA/A=5; ZB/PL=9` | `ZAZB` = `59` | `7000` → `7006` |
| `7000` | `ZA/A=6; ZB/PL=0` | `ZAZB` = `60` | `7000` → `7007` |
| `7000` | `ZA/A=6; ZB/PL=1` | `ZAZB` = `61` | `7000` → `7007` |
| `7000` | `ZA/A=6; ZB/PL=2` | `ZAZB` = `62` | `7000` → `7007` |
| `7000` | `ZA/A=6; ZB/PL=3` | `ZAZB` = `63` | `7000` → `7007` |
| `7000` | `ZA/A=6; ZB/PL=4` | `ZAZB` = `64` | `7000` → `7007` |
| `7000` | `ZA/A=6; ZB/PL=5` | `ZAZB` = `65` | `7000` → `7007` |
| `7000` | `ZA/A=6; ZB/PL=6` | `ZAZB` = `66` | `7000` → `7007` |
| `7000` | `ZA/A=6; ZB/PL=7` | `ZAZB` = `67` | `7000` → `7007` |
| `7000` | `ZA/A=6; ZB/PL=8` | `ZAZB` = `68` | `7000` → `7007` |
| `7000` | `ZA/A=6; ZB/PL=9` | `ZAZB` = `69` | `7000` → `7007` |
| `7000` | `ZA/A=7; ZB/PL=0` | `ZAZB` = `70` | `7000` → `7008` |
| `7000` | `ZA/A=7; ZB/PL=1` | `ZAZB` = `71` | `7000` → `7008` |
| `7000` | `ZA/A=7; ZB/PL=2` | `ZAZB` = `72` | `7000` → `7008` |
| `7000` | `ZA/A=7; ZB/PL=3` | `ZAZB` = `73` | `7000` → `7008` |
| `7000` | `ZA/A=7; ZB/PL=4` | `ZAZB` = `74` | `7000` → `7008` |
| `7000` | `ZA/A=7; ZB/PL=5` | `ZAZB` = `75` | `7000` → `7008` |
| `7000` | `ZA/A=7; ZB/PL=6` | `ZAZB` = `76` | `7000` → `7008` |
| `7000` | `ZA/A=7; ZB/PL=7` | `ZAZB` = `77` | `7000` → `7008` |
| `7000` | `ZA/A=7; ZB/PL=8` | `ZAZB` = `78` | `7000` → `7008` |
| `7000` | `ZA/A=7; ZB/PL=9` | `ZAZB` = `79` | `7000` → `7008` |
| `7000` | `ZA/A=8; ZB/PL=5` | `ZAZB` = `85` | `7000` → `7009` |
| `7000` | `ZA/A=8; ZB/PL=6` | `ZAZB` = `86` | `7000` → `7009` |
| `7000` | `ZA/A=8; ZB/PL=7` | `ZAZB` = `87` | `7000` → `7009` |
| `7000` | `ZA/A=8; ZB/PL=8` | `ZAZB` = `88` | `7000` → `7009` |
| `7000` | `ZA/A=8; ZB/PL=9` | `ZAZB` = `89` | `7000` → `7009` |
| `7000` | `ZA/A=8; ZB/PL=0` | `ZAZB` = `80` | `7000` → `7009` |
| `7000` | `ZA/A=8; ZB/PL=1` | `ZAZB` = `81` | `7000` → `7009` |
| `7000` | `ZA/A=8; ZB/PL=2` | `ZAZB` = `82` | `7000` → `7009` |
| `7000` | `ZA/A=8; ZB/PL=3` | `ZAZB` = `83` | `7000` → `7009` |
| `7000` | `ZA/A=8; ZB/PL=4` | `ZAZB` = `84` | `7000` → `7009` |
| `7000` | `ZA/A=9; ZB/PL=0` | `ZAZB` = `90` | `7000` → `7010` |
| `7000` | `ZA/A=9; ZB/PL=1` | `ZAZB` = `91` | `7000` → `7010` |
| `7000` | `ZA/A=9; ZB/PL=2` | `ZAZB` = `92` | `7000` → `7010` |
| `7000` | `ZA/A=9; ZB/PL=3` | `ZAZB` = `93` | `7000` → `7010` |
| `7000` | `ZA/A=9; ZB/PL=4` | `ZAZB` = `94` | `7000` → `7010` |
| `7000` | `ZA/A=9; ZB/PL=5` | `ZAZB` = `95` | `7000` → `7010` |
| `7000` | `ZA/A=9; ZB/PL=6` | `ZAZB` = `96` | `7000` → `7010` |
| `7000` | `ZA/A=9; ZB/PL=7` | `ZAZB` = `97` | `7000` → `7010` |
| `7000` | `ZA/A=9; ZB/PL=8` | `ZAZB` = `98` | `7000` → `7010` |
| `7000` | `ZA/A=9; ZB/PL=9` | `ZAZB` = `99` | `7000` → `7010` |
| `7204` | `ZA/A=0` | `A` = `0` | `7204` |
| `7204` | `ZA/A=0; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=1` | `A` = `1` | `7204` |
| `7204` | `ZA/A=1; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=2` | `A` = `2` | `7204` |
| `7204` | `ZA/A=2; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=3` | `A` = `3` | `7204` |
| `7204` | `ZA/A=3; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=4` | `A` = `4` | `7204` |
| `7204` | `ZA/A=4; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=5` | `A` = `5` | `7204` |
| `7204` | `ZA/A=5; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=6` | `A` = `6` | `7204` |
| `7204` | `ZA/A=6; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=7` | `A` = `7` | `7204` |
| `7204` | `ZA/A=7; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=8` | `A` = `8` | `7204` |
| `7204` | `ZA/A=8; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=9` | `A` = `9` | `7204` |
| `7204` | `ZA/A=9; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |

No conversion reference is attached to these slot rows. Resolve the active Object and apply its firmware-specific domain restrictions separately. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `26` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `195` - IR self-learning split control | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `196` - IR complete split control | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |


These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Use `M=1` for self-learned commands with automation A/PL and `N=0`; acquire a compatible remote’s commands in IRSplit, assign command numbers `1..20`, save the custom database and download to the emitter. Use `M=0` for complete split control with a supported manufacturer/model from the software database. IRSplit has different basic/advanced project surfaces; USB connects acquisition/download and firmware/device-information workflows. The technical sheet calls remote virtual configuration and its local identification button future use, so do not infer current support from their presence in the catalogue.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

## Source reconciliation

3456/088301 are established database identities. Revisions b (2012) and c (2014) agree on the two modes and supply/current; c retains a b-style UK code in one footer despite its EN filename and explicit c revision. U4714B and IRSplit supplement wiring/acquisition procedures. The publisher-linked shared system guide does not name 3456 and contributes no exact-product rating. Object `195` (learning) and `196` (complete split) are mode alternatives; a single Module does not expose both unconditionally. IR transmission provides no captured proof that the air conditioner accepted a command.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `MQ00357-b-UK.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `MQ00357-c-EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `MyHOME Technical Guide.pdf` | June 2025 shared energy guide: wiring, load control and consumption topology; no exact 3456/F450 match and no specifications transferred to those products. |
| `U4713A_S_EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `U4714B.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `3456-publisher-product-sheet.pdf` | Captured exact-variant identity and complete technical classification attributes tabulated above; document links are discovery provenance, not additional independently verified capability. |

## Evidence limits and open work

Exact supported-brand/model database payload, physical remote compatibility and runtime acknowledgment/state feedback remain unresolved. A catalogue association alone does not prove future-use virtual commissioning is implemented.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
