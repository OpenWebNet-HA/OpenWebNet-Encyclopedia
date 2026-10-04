# Load management central unit

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0121` | Project identity |
| Technical description | Load management central unit | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `F521`, `003557` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1162` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | New energy saving and load control | Main system association |
| Item model / `modobj` | `5` | Main association; independent of project ID |
| Firmware definition | `231`, `735` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Energy management, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F521` | Established catalogue identity | Manufacturer database commercial record `1162` explicitly links this SKU to item `1162` |
| Legrand | `003557` | Established catalogue identity | Manufacturer database commercial record `1895` explicitly links this SKU to item `1162` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MyHOME Technical Guide.pdf` | English system technical guide | `AD-EXMH25GT; Versione 6/2025 printed on rear cover` | Energy/load functions and installation topology: printed/PDF pp. 74-80, 90, 96, 101. No exact 3456/F450 match; no rating transferred to those products. | [Archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MyHOME Technical Guide.pdf) |
| `ST-00001811-EN.pdf` | Technical Sheet ST-00001811-EN | `ST-00001811-EN; 28/05/2024` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-4; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/98/cd/98cd21a7039899d30aa8f309876607f44b4af3cd411144a33f2a11c86af1e0d3.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00001811-EN.pdf) |
| `U4725D.pdf` | Instruction Use U4725D | `U4725D; 05/24-01 PC` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-4; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/63/00/6300e7a27e8722dc3b2945f6c3b7e908cb3042c7193d3ab988519bab6311bfcd.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/U4725D.pdf) |
| `F521-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 04.10.2026` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-3; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/66/32/663200333ff67628f2f3cc671eaa694563ca4942344456623de1f57818fb0b3b.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-F521&include_technical=1) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `1162` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mains input | `110..240 Vac; 50/60 Hz` | `ST-00001811-EN` printed/PDF pp. 1-4 |
| SCS supply | `18..27 Vdc` | `ST-00001811-EN` printed/PDF pp. 1-4 |
| SCS draw | `28 mA max` | `ST-00001811-EN` printed/PDF pp. 1-4 |
| Operating temperature | `0..40 °C` | `ST-00001811-EN` printed/PDF pp. 1-4 |
| Mounting | `1 DIN module` | `ST-00001811-EN` printed/PDF pp. 1-4 |
| Measured / nominal current | `90 A maximum / 16 A nominal` | `ST-00001811-EN` printed/PDF pp. 1-4 |
| Functions | `load control: up to 63 actuators per phase; instantaneous W and cumulative Wh` | `ST-00001811-EN` printed/PDF pp. 1-4 |
| Historical storage | `hourly: 12 months; daily: 2 years; monthly: 12 years` | `ST-00001811-EN` printed/PDF pp. 1-4 |
| Toroid accessory | `3523; one supplied` | `ST-00001811-EN` printed/PDF pp. 1-4 |
| Mains protection | `<=16 A thermal magnetic circuit breaker` | `ST-00001811-EN` printed/PDF pp. 1-4 |


### Publisher export attributes

These are the captured publisher classification values for the named variants. They do not override a technical sheet’s ratings or prove runtime protocol support. A negative radio-bus/connected-object classification is not evidence against separately documented gateway or Wi-Fi behavior.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| EAN | `8005543402078` | `F521` export p. 1 |
| Bus system KNX | `No` | `F521` export p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `F521` export p. 2 |
| Bus system radio frequency | `No` | `F521` export p. 2 |
| Bus system LON | `No` | `F521` export p. 2 |
| Bus system Powernet | `No` | `F521` export p. 2 |
| Other bus systems | `Other` | `F521` export p. 2 |
| Model | `Energy meter` | `F521` export p. 2 |
| Connection type | `Direct` | `F521` export p. 2 |
| Reactive power | `No` | `F521` export p. 2 |
| Approved according to PTB | `No` | `F521` export p. 2 |
| S0 impulse interface | `None` | `F521` export p. 2 |
| Tariff switch | `No` | `F521` export p. 2 |
| Connected object | `No` | `F521` export p. 2 |

### Published status indicators



| State | LED indication | Source |
| --- | --- | --- |
| not configured | `orange/green 128 ms/128 ms` | Exact technical sheet, indicator table in Documentation |
| configuration error | `irregular orange on green` | Exact technical sheet, indicator table in Documentation |
| normal | `green` | Exact technical sheet, indicator table in Documentation |
| insufficient bus/drop | `green 500 ms/500 ms` | Exact technical sheet, indicator table in Documentation |
| no mains | `red 100 ms/900 ms` | Exact technical sheet, indicator table in Documentation |
| above threshold | `red` | Exact technical sheet, indicator table in Documentation |
| actuators not acquired | `steady orange` | Exact technical sheet, indicator table in Documentation |
| acquiring | `red 100 ms/100 ms` | Exact technical sheet, indicator table in Documentation |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1162` | Canonical catalogue |
| Technical item description | Load management central unit | Canonical catalogue |
| Item family | Energy saving (control unit, meter, counter); key `12` | Canonical catalogue |
| Main system | New energy saving and load control; key `20` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `5` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `231` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |
| `735` | `3` | `0` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `231` | `1` | `199` Energy metering and load control | Fixed/designated metadata | `1178` | `470` | `634` |
| `735` | `1` | `199` Energy metering and load control | Fixed/designated metadata | `2666` | `470` | `1276` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `231` | Virtual Configuration | `1` | Association key `1` |
| `231` | Advanced Configuration | `2` | Association key `2` |
| `231` | Physical configuration | `0` | Association key `3` |
| `735` | Virtual Configuration | `1` | Association key `1` |
| `735` | Advanced Configuration | `2` | Association key `2` |
| `735` | Physical configuration | `0` | Association key `3` |


No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

### Published physical metering selectors



| Selector | Physical domain / meaning | Published software scope |
| --- | --- | --- |
| Address | `1..127` | software address `0..127`; catalogue restrictions separately tabulated |
| Toroid direction | `T=0:orientation independent; T=1:directional` | same two documented direction choices |
| Clock | system date/time required | absence prevents historical saving, not instantaneous measurement |

### Published power and tolerance selectors

ST-00001811-EN printed/PDF pp. 2-3. Approximate current values in the source are guidance; contractual power is the control threshold reference.

| Selector | Physical mapping | Published virtual domain |
| --- | --- | --- |
| P | `0:3; 1:1.5; 2:4.5; 3:6; 4:9; 5:10.5; 6:12; 7:14; 8:15; 9:18 kW` | `100..25500 W; step 100 W` |
| TOL | `0:0%; 1:-5%; 2:-10%; 3:-15%; 4:-20%; 5:+5%; 6:+10%; 7:+15%; 8:+20%` | `-20..+20%; step 1%` |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `231` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `231` | `A1` | `0..2` | `0` | A1; Energy Management A1 Address (0-2) |
| `231` | `A2` | `0..9` | `0` | A2; Energy Management A2 Address (0-9) |
| `231` | `A3` | `0..9` | `0` | A3; Energy Management A3 Address (0-9) |
| `231` | `P` | `0..9` | `0` | Rated Power |
| `231` | `TOL` | `0..8` | `0` | Tolerance on rated power |
| `735` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `735` | `A1` | `0..1` | `0` | A1; Energy Management A1 Address (0-2) |
| `735` | `A2` | `0..9` | `0` | A2; Energy Management A2 Address (0-9) |
| `735` | `A3` | `0..9` | `0` | A3; Energy Management A3 Address (0-9) |
| `735` | `P` | `0..9` | `0` | Rated Power |
| `735` | `TOL` | `0..8` | `0` | Tolerance on rated power |
| `735` | `T↑` | `0..1` | `0` | Toroid direction management |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `199` - Energy metering and load control

Catalogue Object key `470` maps to external Object `199`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A123` | `0..127` | `0` | Address; Energy Management A123 Address (0-255) |
| `PHASE` | `0` = Single phase; `1` = Phase R; `2` = Phase S; `3` = Phase T | `0` | Phase |
| `RATED_POWER` | `1` = 100 W; `2` = 200 W; `3` = 300 W; `4` = 400 W; `5` = 500 W; `6` = 600 W; `7` = 700 W; `8` = 800 W; `9` = 900 W; `10` = 1000 W; `11` = 1100 W; `12` = 1200 W; `13` = 1300 W; `14` = 1400 W; `15` = 1500 W; `16` = 1600 W; `17` = 1700 W; `18` = 1800 W; `19` = 1900 W; `20` = 2000 W; `21` = 2100 W; `22` = 2200 W; `23` = 2300 W; `24` = 2400 W; `25` = 2500 W; `26` = 2600 W; `27` = 2700 W; `28` = 2800 W; `29` = 2900 W; `30` = 3000 W; `31` = 3100 W; `32` = 3200 W; `33` = 3300 W; `34` = 3400 W; `35` = 3500 W; `36` = 3600 W; `37` = 3700 W; `38` = 3800 W; `39` = 3900 W; `40` = 4000 W; `41` = 4100 W; `42` = 4200 W; `43` = 4300 W; `44` = 4400 W; `45` = 4500 W; `46` = 4600 W; `47` = 4700 W; `48` = 4800 W; `49` = 4900 W; `50` = 5000 W; `51` = 5100 W; `52` = 5200 W; `53` = 5300 W; `54` = 5400 W; `55` = 5500 W; `56` = 5600 W; `57` = 5700 W; `58` = 5800 W; `59` = 5900 W; `60` = 6000 W; `61` = 6100 W; `62` = 6200 W; `63` = 6300 W; `64` = 6400 W; `65` = 6500 W; `66` = 6600 W; `67` = 6700 W; `68` = 6800 W; `69` = 6900 W; `70` = 7000 W; `71` = 7100 W; `72` = 7200 W; `73` = 7300 W; `74` = 7400 W; `75` = 7500 W; `76` = 7600 W; `77` = 7700 W; `78` = 7800 W; `79` = 7900 W; `80` = 8000 W; `81` = 8100 W; `82` = 8200 W; `83` = 8300 W; `84` = 8400 W; `85` = 8500 W; `86` = 8600 W; `87` = 8700 W; `88` = 8800 W; `89` = 8900 W; `90` = 9000 W; `91` = 9100 W; `92` = 9200 W; `93` = 9300 W; `94` = 9400 W; `95` = 9500 W; `96` = 9600 W; `97` = 9700 W; `98` = 9800 W; `99` = 9900 W; `100` = 10000 W; `101` = 10100 W; `102` = 10200 W; `103` = 10300 W; `104` = 10400 W; `105` = 10500 W; `106` = 10600 W; `107` = 10700 W; `108` = 10800 W; `109` = 10900 W; `110` = 11000 W; `111` = 11100 W; `112` = 11200 W; `113` = 11300 W; `114` = 11400 W; `115` = 11500 W; `116` = 11600 W; `117` = 11700 W; `118` = 11800 W; `119` = 11900 W; `120` = 12000 W; `121` = 12100 W; `122` = 12200 W; `123` = 12300 W; `124` = 12400 W; `125` = 12500 W; `126` = 12600 W; `127` = 12700 W; `128` = 12800 W; `129` = 12900 W; `130` = 13000 W; `131` = 13100 W; `132` = 13200 W; `133` = 13300 W; `134` = 13400 W; `135` = 13500 W; `136` = 13600 W; `137` = 13700 W; `138` = 13800 W; `139` = 13900 W; `140` = 14000 W; `141` = 14100 W; `142` = 14200 W; `143` = 14300 W; `144` = 14400 W; `145` = 14500 W; `146` = 14600 W; `147` = 14700 W; `148` = 14800 W; `149` = 14900 W; `150` = 15000 W; `151` = 15100 W; `152` = 15200 W; `153` = 15300 W; `154` = 15400 W; `155` = 15500 W; `156` = 15600 W; `157` = 15700 W; `158` = 15800 W; `159` = 15900 W; `160` = 16000 W; `161` = 16100 W; `162` = 16200 W; `163` = 16300 W; `164` = 16400 W; `165` = 16500 W; `166` = 16600 W; `167` = 16700 W; `168` = 16800 W; `169` = 16900 W; `170` = 17000 W; `171` = 17100 W; `172` = 17200 W; `173` = 17300 W; `174` = 17400 W; `175` = 17500 W; `176` = 17600 W; `177` = 17700 W; `178` = 17800 W; `179` = 17900 W; `180` = 18000 W; `181` = 18100 W; `182` = 18200 W; `183` = 18300 W; `184` = 18400 W; `185` = 18500 W; `186` = 18600 W; `187` = 18700 W; `188` = 18800 W; `189` = 18900 W; `190` = 19000 W; `191` = 19100 W; `192` = 19200 W; `193` = 19300 W; `194` = 19400 W; `195` = 19500 W; `196` = 19600 W; `197` = 19700 W; `198` = 19800 W; `199` = 19900 W; `200` = 20000 W; `201` = 20100 W; `202` = 20200 W; `203` = 20300 W; `204` = 20400 W; `205` = 20500 W; `206` = 20600 W; `207` = 20700 W; `208` = 20800 W; `209` = 20900 W; `210` = 21000 W; `211` = 21100 W; `212` = 21200 W; `213` = 21300 W; `214` = 21400 W; `215` = 21500 W; `216` = 21600 W; `217` = 21700 W; `218` = 21800 W; `219` = 21900 W; `220` = 22000 W; `221` = 22100 W; `222` = 22200 W; `223` = 22300 W; `224` = 22400 W; `225` = 22500 W; `226` = 22600 W; `227` = 22700 W; `228` = 22800 W; `229` = 22900 W; `230` = 23000 W; `231` = 23100 W; `232` = 23200 W; `233` = 23300 W; `234` = 23400 W; `235` = 23500 W; `236` = 23600 W; `237` = 23700 W; `238` = 23800 W; `239` = 23900 W; `240` = 24000 W; `241` = 24100 W; `242` = 24200 W; `243` = 24300 W; `244` = 24400 W; `245` = 24500 W; `246` = 24600 W; `247` = 24700 W; `248` = 24800 W; `249` = 24900 W; `250` = 25000 W; `251` = 25100 W; `252` = 25200 W; `253` = 25300 W; `254` = 25400 W; `255` = 25500 W | `30` | Rated power; Rated power to be used for load control (100W steps) |
| `POWER_TOLERANCE` | `0` = 0 %; `1` = +1 %; `2` = +2 %; `3` = +3 %; `4` = +4 %; `5` = +5 %; `6` = +6 %; `7` = +7 %; `8` = +8 %; `9` = +9 %; `10` = +10 %; `11` = +11 %; `12` = +12 %; `13` = +13 %; `14` = +14 %; `15` = +15 %; `16` = +16 %; `17` = +17 %; `18` = +18 %; `19` = +19 %; `20` = +20 %; `129` = -1 %; `130` = -2 %; `131` = -3 %; `132` = -4 %; `133` = -5 %; `134` = -6 %; `135` = -7 %; `136` = -8 %; `137` = -9 %; `138` = -10 %; `139` = -11 %; `140` = -12 %; `141` = -13 %; `142` = -14 %; `143` = -15 %; `144` = -16 %; `145` = -17 %; `146` = -18 %; `147` = -19 %; `148` = -20 % | `0` | Tolerance on rated power; 1 bit sign - 7 bits value -20 = 0x94 -19 = 0x93 ... -1 = 0x81 0 = 0x00 +1 = 0x01 ... +20 = 0x14 |
| `TOROID_DIRECTION` | `0` = Disabled; `1` = Enabled | `0` | Toroid direction management |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `231` | `1` | `199` | `4162` | No textual predicate stored | `800` |
| `735` | `1` | `199` | `4162` | No textual predicate stored | `800` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `231` | `199` | `3000` | `TOROID_DIRECTION` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | Toroid direction management |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `800` | `P=0` | `POWER` = `30` | `800` |
| `800` | `P=1` | `POWER` = `15` | `800` |
| `800` | `P=2` | `POWER` = `45` | `800` |
| `800` | `P=3` | `POWER` = `60` | `800` |
| `800` | `P=4` | `POWER` = `90` | `800` |
| `800` | `P=5` | `POWER` = `105` | `800` |
| `800` | `P=6` | `POWER` = `120` | `800` |
| `800` | `P=7` | `POWER` = `140` | `800` |
| `800` | `P=8` | `POWER` = `150` | `800` |
| `800` | `P=9` | `POWER` = `180` | `800` |
| `800` | `TOL=0` | `TOLLERANCE` = `0` | `800` |
| `800` | `TOL=1` | `TOLLERANCE` = `133` | `800` |
| `800` | `TOL=2` | `TOLLERANCE` = `138` | `800` |
| `800` | `TOL=3` | `TOLLERANCE` = `143` | `800` |
| `800` | `TOL=4` | `TOLLERANCE` = `148` | `800` |
| `800` | `TOL=5` | `TOLLERANCE` = `5` | `800` |
| `800` | `TOL=6` | `TOLLERANCE` = `10` | `800` |
| `800` | `TOL=7` | `TOLLERANCE` = `15` | `800` |
| `800` | `TOL=8` | `TOLLERANCE` = `20` | `800` |
| `800` | `A1=0; A2=0; A3=8` | `A123` = `8` | `800` → `801` → `802` |
| `800` | `A1=0; A2=0; A3=9` | `A123` = `9` | `800` → `801` → `802` |
| `800` | `A1=0; A2=0; A3=0` | `A123` = `0` | `800` → `801` → `802` |
| `800` | `A1=0; A2=0; A3=1` | `A123` = `1` | `800` → `801` → `802` |
| `800` | `A1=0; A2=0; A3=2` | `A123` = `2` | `800` → `801` → `802` |
| `800` | `A1=0; A2=0; A3=3` | `A123` = `3` | `800` → `801` → `802` |
| `800` | `A1=0; A2=0; A3=4` | `A123` = `4` | `800` → `801` → `802` |
| `800` | `A1=0; A2=0; A3=5` | `A123` = `5` | `800` → `801` → `802` |
| `800` | `A1=0; A2=0; A3=6` | `A123` = `6` | `800` → `801` → `802` |
| `800` | `A1=0; A2=0; A3=7` | `A123` = `7` | `800` → `801` → `802` |
| `800` | `A1=0; A2=1; A3=0` | `A123` = `10` | `800` → `801` → `803` |
| `800` | `A1=0; A2=1; A3=1` | `A123` = `11` | `800` → `801` → `803` |
| `800` | `A1=0; A2=1; A3=2` | `A123` = `12` | `800` → `801` → `803` |
| `800` | `A1=0; A2=1; A3=3` | `A123` = `13` | `800` → `801` → `803` |
| `800` | `A1=0; A2=1; A3=4` | `A123` = `14` | `800` → `801` → `803` |
| `800` | `A1=0; A2=1; A3=5` | `A123` = `15` | `800` → `801` → `803` |
| `800` | `A1=0; A2=1; A3=6` | `A123` = `16` | `800` → `801` → `803` |
| `800` | `A1=0; A2=1; A3=7` | `A123` = `17` | `800` → `801` → `803` |
| `800` | `A1=0; A2=1; A3=8` | `A123` = `18` | `800` → `801` → `803` |
| `800` | `A1=0; A2=1; A3=9` | `A123` = `19` | `800` → `801` → `803` |
| `800` | `A1=0; A2=2; A3=0` | `A123` = `20` | `800` → `801` → `804` |
| `800` | `A1=0; A2=2; A3=1` | `A123` = `21` | `800` → `801` → `804` |
| `800` | `A1=0; A2=2; A3=2` | `A123` = `22` | `800` → `801` → `804` |
| `800` | `A1=0; A2=2; A3=3` | `A123` = `23` | `800` → `801` → `804` |
| `800` | `A1=0; A2=2; A3=4` | `A123` = `24` | `800` → `801` → `804` |
| `800` | `A1=0; A2=2; A3=5` | `A123` = `25` | `800` → `801` → `804` |
| `800` | `A1=0; A2=2; A3=6` | `A123` = `26` | `800` → `801` → `804` |
| `800` | `A1=0; A2=2; A3=7` | `A123` = `27` | `800` → `801` → `804` |
| `800` | `A1=0; A2=2; A3=8` | `A123` = `28` | `800` → `801` → `804` |
| `800` | `A1=0; A2=2; A3=9` | `A123` = `29` | `800` → `801` → `804` |
| `800` | `A1=0; A2=3; A3=0` | `A123` = `30` | `800` → `801` → `805` |
| `800` | `A1=0; A2=3; A3=1` | `A123` = `31` | `800` → `801` → `805` |
| `800` | `A1=0; A2=3; A3=2` | `A123` = `32` | `800` → `801` → `805` |
| `800` | `A1=0; A2=3; A3=3` | `A123` = `33` | `800` → `801` → `805` |
| `800` | `A1=0; A2=3; A3=4` | `A123` = `34` | `800` → `801` → `805` |
| `800` | `A1=0; A2=3; A3=5` | `A123` = `35` | `800` → `801` → `805` |
| `800` | `A1=0; A2=3; A3=6` | `A123` = `36` | `800` → `801` → `805` |
| `800` | `A1=0; A2=3; A3=7` | `A123` = `37` | `800` → `801` → `805` |
| `800` | `A1=0; A2=3; A3=8` | `A123` = `38` | `800` → `801` → `805` |
| `800` | `A1=0; A2=3; A3=9` | `A123` = `39` | `800` → `801` → `805` |
| `800` | `A1=0; A2=4; A3=0` | `A123` = `40` | `800` → `801` → `806` |
| `800` | `A1=0; A2=4; A3=1` | `A123` = `41` | `800` → `801` → `806` |
| `800` | `A1=0; A2=4; A3=2` | `A123` = `42` | `800` → `801` → `806` |
| `800` | `A1=0; A2=4; A3=3` | `A123` = `43` | `800` → `801` → `806` |
| `800` | `A1=0; A2=4; A3=4` | `A123` = `44` | `800` → `801` → `806` |
| `800` | `A1=0; A2=4; A3=5` | `A123` = `45` | `800` → `801` → `806` |
| `800` | `A1=0; A2=4; A3=6` | `A123` = `46` | `800` → `801` → `806` |
| `800` | `A1=0; A2=4; A3=7` | `A123` = `47` | `800` → `801` → `806` |
| `800` | `A1=0; A2=4; A3=8` | `A123` = `48` | `800` → `801` → `806` |
| `800` | `A1=0; A2=4; A3=9` | `A123` = `49` | `800` → `801` → `806` |
| `800` | `A1=0; A2=5; A3=0` | `A123` = `50` | `800` → `801` → `807` |
| `800` | `A1=0; A2=5; A3=1` | `A123` = `51` | `800` → `801` → `807` |
| `800` | `A1=0; A2=5; A3=2` | `A123` = `52` | `800` → `801` → `807` |
| `800` | `A1=0; A2=5; A3=3` | `A123` = `53` | `800` → `801` → `807` |
| `800` | `A1=0; A2=5; A3=4` | `A123` = `54` | `800` → `801` → `807` |
| `800` | `A1=0; A2=5; A3=5` | `A123` = `55` | `800` → `801` → `807` |
| `800` | `A1=0; A2=5; A3=6` | `A123` = `56` | `800` → `801` → `807` |
| `800` | `A1=0; A2=5; A3=7` | `A123` = `57` | `800` → `801` → `807` |
| `800` | `A1=0; A2=5; A3=8` | `A123` = `58` | `800` → `801` → `807` |
| `800` | `A1=0; A2=5; A3=9` | `A123` = `59` | `800` → `801` → `807` |
| `800` | `A1=0; A2=6; A3=0` | `A123` = `60` | `800` → `801` → `808` |
| `800` | `A1=0; A2=6; A3=1` | `A123` = `61` | `800` → `801` → `808` |
| `800` | `A1=0; A2=6; A3=2` | `A123` = `62` | `800` → `801` → `808` |
| `800` | `A1=0; A2=6; A3=3` | `A123` = `63` | `800` → `801` → `808` |
| `800` | `A1=0; A2=6; A3=4` | `A123` = `64` | `800` → `801` → `808` |
| `800` | `A1=0; A2=6; A3=5` | `A123` = `65` | `800` → `801` → `808` |
| `800` | `A1=0; A2=6; A3=6` | `A123` = `66` | `800` → `801` → `808` |
| `800` | `A1=0; A2=6; A3=7` | `A123` = `67` | `800` → `801` → `808` |
| `800` | `A1=0; A2=6; A3=8` | `A123` = `68` | `800` → `801` → `808` |
| `800` | `A1=0; A2=6; A3=9` | `A123` = `69` | `800` → `801` → `808` |
| `800` | `A1=0; A2=7; A3=0` | `A123` = `70` | `800` → `801` → `809` |
| `800` | `A1=0; A2=7; A3=1` | `A123` = `71` | `800` → `801` → `809` |
| `800` | `A1=0; A2=7; A3=2` | `A123` = `72` | `800` → `801` → `809` |
| `800` | `A1=0; A2=7; A3=3` | `A123` = `73` | `800` → `801` → `809` |
| `800` | `A1=0; A2=7; A3=4` | `A123` = `74` | `800` → `801` → `809` |
| `800` | `A1=0; A2=7; A3=5` | `A123` = `75` | `800` → `801` → `809` |
| `800` | `A1=0; A2=7; A3=6` | `A123` = `76` | `800` → `801` → `809` |
| `800` | `A1=0; A2=7; A3=7` | `A123` = `77` | `800` → `801` → `809` |
| `800` | `A1=0; A2=7; A3=8` | `A123` = `78` | `800` → `801` → `809` |
| `800` | `A1=0; A2=7; A3=9` | `A123` = `79` | `800` → `801` → `809` |
| `800` | `A1=0; A2=8; A3=0` | `A123` = `80` | `800` → `801` → `810` |
| `800` | `A1=0; A2=8; A3=1` | `A123` = `81` | `800` → `801` → `810` |
| `800` | `A1=0; A2=8; A3=2` | `A123` = `82` | `800` → `801` → `810` |
| `800` | `A1=0; A2=8; A3=3` | `A123` = `83` | `800` → `801` → `810` |
| `800` | `A1=0; A2=8; A3=4` | `A123` = `84` | `800` → `801` → `810` |
| `800` | `A1=0; A2=8; A3=5` | `A123` = `85` | `800` → `801` → `810` |
| `800` | `A1=0; A2=8; A3=6` | `A123` = `86` | `800` → `801` → `810` |
| `800` | `A1=0; A2=8; A3=7` | `A123` = `87` | `800` → `801` → `810` |
| `800` | `A1=0; A2=8; A3=8` | `A123` = `88` | `800` → `801` → `810` |
| `800` | `A1=0; A2=8; A3=9` | `A123` = `89` | `800` → `801` → `810` |
| `800` | `A1=0; A2=9; A3=0` | `A123` = `90` | `800` → `801` → `811` |
| `800` | `A1=0; A2=9; A3=1` | `A123` = `91` | `800` → `801` → `811` |
| `800` | `A1=0; A2=9; A3=2` | `A123` = `92` | `800` → `801` → `811` |
| `800` | `A1=0; A2=9; A3=3` | `A123` = `93` | `800` → `801` → `811` |
| `800` | `A1=0; A2=9; A3=4` | `A123` = `94` | `800` → `801` → `811` |
| `800` | `A1=0; A2=9; A3=5` | `A123` = `95` | `800` → `801` → `811` |
| `800` | `A1=0; A2=9; A3=6` | `A123` = `96` | `800` → `801` → `811` |
| `800` | `A1=0; A2=9; A3=7` | `A123` = `97` | `800` → `801` → `811` |
| `800` | `A1=0; A2=9; A3=8` | `A123` = `98` | `800` → `801` → `811` |
| `800` | `A1=0; A2=9; A3=9` | `A123` = `99` | `800` → `801` → `811` |
| `800` | `A1=1; A2=0; A3=0` | `A123` = `100` | `800` → `812` → `813` |
| `800` | `A1=1; A2=0; A3=1` | `A123` = `101` | `800` → `812` → `813` |
| `800` | `A1=1; A2=0; A3=2` | `A123` = `102` | `800` → `812` → `813` |
| `800` | `A1=1; A2=0; A3=3` | `A123` = `103` | `800` → `812` → `813` |
| `800` | `A1=1; A2=0; A3=4` | `A123` = `104` | `800` → `812` → `813` |
| `800` | `A1=1; A2=0; A3=5` | `A123` = `105` | `800` → `812` → `813` |
| `800` | `A1=1; A2=0; A3=6` | `A123` = `106` | `800` → `812` → `813` |
| `800` | `A1=1; A2=0; A3=7` | `A123` = `107` | `800` → `812` → `813` |
| `800` | `A1=1; A2=0; A3=8` | `A123` = `108` | `800` → `812` → `813` |
| `800` | `A1=1; A2=0; A3=9` | `A123` = `109` | `800` → `812` → `813` |
| `800` | `A1=1; A2=1; A3=0` | `A123` = `110` | `800` → `812` → `814` |
| `800` | `A1=1; A2=1; A3=1` | `A123` = `111` | `800` → `812` → `814` |
| `800` | `A1=1; A2=1; A3=2` | `A123` = `112` | `800` → `812` → `814` |
| `800` | `A1=1; A2=1; A3=3` | `A123` = `113` | `800` → `812` → `814` |
| `800` | `A1=1; A2=1; A3=4` | `A123` = `114` | `800` → `812` → `814` |
| `800` | `A1=1; A2=1; A3=5` | `A123` = `115` | `800` → `812` → `814` |
| `800` | `A1=1; A2=1; A3=6` | `A123` = `116` | `800` → `812` → `814` |
| `800` | `A1=1; A2=1; A3=7` | `A123` = `117` | `800` → `812` → `814` |
| `800` | `A1=1; A2=1; A3=8` | `A123` = `118` | `800` → `812` → `814` |
| `800` | `A1=1; A2=1; A3=9` | `A123` = `119` | `800` → `812` → `814` |
| `800` | `A1=1; A2=2; A3=0` | `A123` = `120` | `800` → `812` → `815` |
| `800` | `A1=1; A2=2; A3=1` | `A123` = `121` | `800` → `812` → `815` |
| `800` | `A1=1; A2=2; A3=2` | `A123` = `122` | `800` → `812` → `815` |
| `800` | `A1=1; A2=2; A3=3` | `A123` = `123` | `800` → `812` → `815` |
| `800` | `A1=1; A2=2; A3=4` | `A123` = `124` | `800` → `812` → `815` |
| `800` | `A1=1; A2=2; A3=5` | `A123` = `125` | `800` → `812` → `815` |
| `800` | `A1=1; A2=2; A3=6` | `A123` = `126` | `800` → `812` → `815` |
| `800` | `A1=1; A2=2; A3=7` | `A123` = `127` | `800` → `812` → `815` |
| `800` | `A1=1; A2=2; A3=8` | `A123` = `128` | `800` → `812` → `815` |
| `800` | `A1=1; A2=2; A3=9` | `A123` = `129` | `800` → `812` → `815` |
| `800` | `A1=1; A2=3; A3=0` | `A123` = `130` | `800` → `812` → `816` |
| `800` | `A1=1; A2=3; A3=1` | `A123` = `131` | `800` → `812` → `816` |
| `800` | `A1=1; A2=3; A3=2` | `A123` = `132` | `800` → `812` → `816` |
| `800` | `A1=1; A2=3; A3=3` | `A123` = `133` | `800` → `812` → `816` |
| `800` | `A1=1; A2=3; A3=4` | `A123` = `134` | `800` → `812` → `816` |
| `800` | `A1=1; A2=3; A3=5` | `A123` = `135` | `800` → `812` → `816` |
| `800` | `A1=1; A2=3; A3=6` | `A123` = `136` | `800` → `812` → `816` |
| `800` | `A1=1; A2=3; A3=7` | `A123` = `137` | `800` → `812` → `816` |
| `800` | `A1=1; A2=3; A3=8` | `A123` = `138` | `800` → `812` → `816` |
| `800` | `A1=1; A2=3; A3=9` | `A123` = `139` | `800` → `812` → `816` |
| `800` | `A1=1; A2=4; A3=0` | `A123` = `140` | `800` → `812` → `817` |
| `800` | `A1=1; A2=4; A3=1` | `A123` = `141` | `800` → `812` → `817` |
| `800` | `A1=1; A2=4; A3=2` | `A123` = `142` | `800` → `812` → `817` |
| `800` | `A1=1; A2=4; A3=3` | `A123` = `143` | `800` → `812` → `817` |
| `800` | `A1=1; A2=4; A3=4` | `A123` = `144` | `800` → `812` → `817` |
| `800` | `A1=1; A2=4; A3=5` | `A123` = `145` | `800` → `812` → `817` |
| `800` | `A1=1; A2=4; A3=6` | `A123` = `146` | `800` → `812` → `817` |
| `800` | `A1=1; A2=4; A3=7` | `A123` = `147` | `800` → `812` → `817` |
| `800` | `A1=1; A2=4; A3=8` | `A123` = `148` | `800` → `812` → `817` |
| `800` | `A1=1; A2=4; A3=9` | `A123` = `149` | `800` → `812` → `817` |
| `800` | `A1=1; A2=5; A3=0` | `A123` = `150` | `800` → `812` → `818` |
| `800` | `A1=1; A2=5; A3=1` | `A123` = `151` | `800` → `812` → `818` |
| `800` | `A1=1; A2=5; A3=2` | `A123` = `152` | `800` → `812` → `818` |
| `800` | `A1=1; A2=5; A3=3` | `A123` = `153` | `800` → `812` → `818` |
| `800` | `A1=1; A2=5; A3=4` | `A123` = `154` | `800` → `812` → `818` |
| `800` | `A1=1; A2=5; A3=5` | `A123` = `155` | `800` → `812` → `818` |
| `800` | `A1=1; A2=5; A3=6` | `A123` = `156` | `800` → `812` → `818` |
| `800` | `A1=1; A2=5; A3=7` | `A123` = `157` | `800` → `812` → `818` |
| `800` | `A1=1; A2=5; A3=8` | `A123` = `158` | `800` → `812` → `818` |
| `800` | `A1=1; A2=5; A3=9` | `A123` = `159` | `800` → `812` → `818` |
| `800` | `A1=1; A2=6; A3=0` | `A123` = `160` | `800` → `812` → `819` |
| `800` | `A1=1; A2=6; A3=1` | `A123` = `161` | `800` → `812` → `819` |
| `800` | `A1=1; A2=6; A3=2` | `A123` = `162` | `800` → `812` → `819` |
| `800` | `A1=1; A2=6; A3=3` | `A123` = `163` | `800` → `812` → `819` |
| `800` | `A1=1; A2=6; A3=4` | `A123` = `164` | `800` → `812` → `819` |
| `800` | `A1=1; A2=6; A3=5` | `A123` = `165` | `800` → `812` → `819` |
| `800` | `A1=1; A2=6; A3=6` | `A123` = `166` | `800` → `812` → `819` |
| `800` | `A1=1; A2=6; A3=7` | `A123` = `167` | `800` → `812` → `819` |
| `800` | `A1=1; A2=6; A3=8` | `A123` = `168` | `800` → `812` → `819` |
| `800` | `A1=1; A2=6; A3=9` | `A123` = `169` | `800` → `812` → `819` |
| `800` | `A1=1; A2=7; A3=0` | `A123` = `170` | `800` → `812` → `820` |
| `800` | `A1=1; A2=7; A3=1` | `A123` = `171` | `800` → `812` → `820` |
| `800` | `A1=1; A2=7; A3=2` | `A123` = `172` | `800` → `812` → `820` |
| `800` | `A1=1; A2=7; A3=3` | `A123` = `173` | `800` → `812` → `820` |
| `800` | `A1=1; A2=7; A3=4` | `A123` = `174` | `800` → `812` → `820` |
| `800` | `A1=1; A2=7; A3=5` | `A123` = `175` | `800` → `812` → `820` |
| `800` | `A1=1; A2=7; A3=6` | `A123` = `176` | `800` → `812` → `820` |
| `800` | `A1=1; A2=7; A3=7` | `A123` = `177` | `800` → `812` → `820` |
| `800` | `A1=1; A2=7; A3=8` | `A123` = `178` | `800` → `812` → `820` |
| `800` | `A1=1; A2=7; A3=9` | `A123` = `179` | `800` → `812` → `820` |
| `800` | `A1=1; A2=8; A3=0` | `A123` = `180` | `800` → `812` → `821` |
| `800` | `A1=1; A2=8; A3=1` | `A123` = `181` | `800` → `812` → `821` |
| `800` | `A1=1; A2=8; A3=2` | `A123` = `182` | `800` → `812` → `821` |
| `800` | `A1=1; A2=8; A3=3` | `A123` = `183` | `800` → `812` → `821` |
| `800` | `A1=1; A2=8; A3=4` | `A123` = `184` | `800` → `812` → `821` |
| `800` | `A1=1; A2=8; A3=5` | `A123` = `185` | `800` → `812` → `821` |
| `800` | `A1=1; A2=8; A3=6` | `A123` = `186` | `800` → `812` → `821` |
| `800` | `A1=1; A2=8; A3=7` | `A123` = `187` | `800` → `812` → `821` |
| `800` | `A1=1; A2=8; A3=8` | `A123` = `188` | `800` → `812` → `821` |
| `800` | `A1=1; A2=8; A3=9` | `A123` = `189` | `800` → `812` → `821` |
| `800` | `A1=1; A2=9; A3=0` | `A123` = `190` | `800` → `812` → `822` |
| `800` | `A1=1; A2=9; A3=1` | `A123` = `191` | `800` → `812` → `822` |
| `800` | `A1=1; A2=9; A3=2` | `A123` = `192` | `800` → `812` → `822` |
| `800` | `A1=1; A2=9; A3=3` | `A123` = `193` | `800` → `812` → `822` |
| `800` | `A1=1; A2=9; A3=4` | `A123` = `194` | `800` → `812` → `822` |
| `800` | `A1=1; A2=9; A3=5` | `A123` = `195` | `800` → `812` → `822` |
| `800` | `A1=1; A2=9; A3=6` | `A123` = `196` | `800` → `812` → `822` |
| `800` | `A1=1; A2=9; A3=7` | `A123` = `197` | `800` → `812` → `822` |
| `800` | `A1=1; A2=9; A3=8` | `A123` = `198` | `800` → `812` → `822` |
| `800` | `A1=1; A2=9; A3=9` | `A123` = `199` | `800` → `812` → `822` |
| `800` | `A1=2; A2=0; A3=0` | `A123` = `200` | `800` → `823` → `824` |
| `800` | `A1=2; A2=0; A3=1` | `A123` = `201` | `800` → `823` → `824` |
| `800` | `A1=2; A2=0; A3=2` | `A123` = `202` | `800` → `823` → `824` |
| `800` | `A1=2; A2=0; A3=3` | `A123` = `203` | `800` → `823` → `824` |
| `800` | `A1=2; A2=0; A3=4` | `A123` = `204` | `800` → `823` → `824` |
| `800` | `A1=2; A2=0; A3=5` | `A123` = `205` | `800` → `823` → `824` |
| `800` | `A1=2; A2=0; A3=6` | `A123` = `206` | `800` → `823` → `824` |
| `800` | `A1=2; A2=0; A3=7` | `A123` = `207` | `800` → `823` → `824` |
| `800` | `A1=2; A2=0; A3=8` | `A123` = `208` | `800` → `823` → `824` |
| `800` | `A1=2; A2=0; A3=9` | `A123` = `209` | `800` → `823` → `824` |
| `800` | `A1=2; A2=1; A3=0` | `A123` = `210` | `800` → `823` → `825` |
| `800` | `A1=2; A2=1; A3=1` | `A123` = `211` | `800` → `823` → `825` |
| `800` | `A1=2; A2=1; A3=2` | `A123` = `212` | `800` → `823` → `825` |
| `800` | `A1=2; A2=1; A3=3` | `A123` = `213` | `800` → `823` → `825` |
| `800` | `A1=2; A2=1; A3=4` | `A123` = `214` | `800` → `823` → `825` |
| `800` | `A1=2; A2=1; A3=5` | `A123` = `215` | `800` → `823` → `825` |
| `800` | `A1=2; A2=1; A3=6` | `A123` = `216` | `800` → `823` → `825` |
| `800` | `A1=2; A2=1; A3=7` | `A123` = `217` | `800` → `823` → `825` |
| `800` | `A1=2; A2=1; A3=8` | `A123` = `218` | `800` → `823` → `825` |
| `800` | `A1=2; A2=1; A3=9` | `A123` = `219` | `800` → `823` → `825` |
| `800` | `A1=2; A2=2; A3=0` | `A123` = `220` | `800` → `823` → `826` |
| `800` | `A1=2; A2=2; A3=1` | `A123` = `221` | `800` → `823` → `826` |
| `800` | `A1=2; A2=2; A3=2` | `A123` = `222` | `800` → `823` → `826` |
| `800` | `A1=2; A2=2; A3=3` | `A123` = `223` | `800` → `823` → `826` |
| `800` | `A1=2; A2=2; A3=4` | `A123` = `224` | `800` → `823` → `826` |
| `800` | `A1=2; A2=2; A3=5` | `A123` = `225` | `800` → `823` → `826` |
| `800` | `A1=2; A2=2; A3=6` | `A123` = `226` | `800` → `823` → `826` |
| `800` | `A1=2; A2=2; A3=7` | `A123` = `227` | `800` → `823` → `826` |
| `800` | `A1=2; A2=2; A3=8` | `A123` = `228` | `800` → `823` → `826` |
| `800` | `A1=2; A2=2; A3=9` | `A123` = `229` | `800` → `823` → `826` |
| `800` | `A1=2; A2=3; A3=0` | `A123` = `230` | `800` → `823` → `827` |
| `800` | `A1=2; A2=3; A3=1` | `A123` = `231` | `800` → `823` → `827` |
| `800` | `A1=2; A2=3; A3=2` | `A123` = `232` | `800` → `823` → `827` |
| `800` | `A1=2; A2=3; A3=3` | `A123` = `233` | `800` → `823` → `827` |
| `800` | `A1=2; A2=3; A3=4` | `A123` = `234` | `800` → `823` → `827` |
| `800` | `A1=2; A2=3; A3=5` | `A123` = `235` | `800` → `823` → `827` |
| `800` | `A1=2; A2=3; A3=6` | `A123` = `236` | `800` → `823` → `827` |
| `800` | `A1=2; A2=3; A3=7` | `A123` = `237` | `800` → `823` → `827` |
| `800` | `A1=2; A2=3; A3=8` | `A123` = `238` | `800` → `823` → `827` |
| `800` | `A1=2; A2=3; A3=9` | `A123` = `239` | `800` → `823` → `827` |
| `800` | `A1=2; A2=4; A3=0` | `A123` = `240` | `800` → `823` → `828` |
| `800` | `A1=2; A2=4; A3=1` | `A123` = `241` | `800` → `823` → `828` |
| `800` | `A1=2; A2=4; A3=2` | `A123` = `242` | `800` → `823` → `828` |
| `800` | `A1=2; A2=4; A3=3` | `A123` = `243` | `800` → `823` → `828` |
| `800` | `A1=2; A2=4; A3=4` | `A123` = `244` | `800` → `823` → `828` |
| `800` | `A1=2; A2=4; A3=5` | `A123` = `245` | `800` → `823` → `828` |
| `800` | `A1=2; A2=4; A3=6` | `A123` = `246` | `800` → `823` → `828` |
| `800` | `A1=2; A2=4; A3=7` | `A123` = `247` | `800` → `823` → `828` |
| `800` | `A1=2; A2=4; A3=8` | `A123` = `248` | `800` → `823` → `828` |
| `800` | `A1=2; A2=4; A3=9` | `A123` = `249` | `800` → `823` → `828` |
| `800` | `A1=2; A2=5; A3=0` | `A123` = `250` | `800` → `823` → `829` |
| `800` | `A1=2; A2=5; A3=1` | `A123` = `251` | `800` → `823` → `829` |
| `800` | `A1=2; A2=5; A3=2` | `A123` = `252` | `800` → `823` → `829` |
| `800` | `A1=2; A2=5; A3=3` | `A123` = `253` | `800` → `823` → `829` |
| `800` | `A1=2; A2=5; A3=4` | `A123` = `254` | `800` → `823` → `829` |
| `800` | `A1=2; A2=5; A3=5` | `A123` = `255` | `800` → `823` → `829` |

No conversion reference is attached to these slot rows. Resolve the active Object and apply its firmware-specific domain restrictions separately. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `5` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `199` - Energy metering and load control | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |


These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Set address, contractual power, tolerance, phase and toroid direction. Acquire actuators after installation: hold about ten seconds until red, release, and wait for interrogation; no load control occurs until acquisition succeeds. Time/date must be supplied by a system device to store history; without it only instantaneous variables continue. Direction `T=0` ignores orientation; `T=1` is directional. In consumption wiring the toroid’s printed side faces the meter; production wiring reverses toward the inverter. Hold about twenty seconds to erase cumulative data. Home+Project, physical selectors and Suite are separately documented configuration routes. Current published server support is F460, F461 and Classe 300EOS; the MHS1 upgrade path uses backup/restore.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

## Source reconciliation

The retained current sheet, multilingual instructions, publisher export and June 2025 system guide agree on the central metering/load roles. The sheet distinguishes primary-input range `110..240 Vac` from diagram markings `110..230 V`; do not broaden a diagram marking into a different load rating. The source’s software address domain `0..127` differs from physical `1..127`; the database’s reusable domains and firmware filters remain independently authoritative for catalogue validation. Physical circuit count is not an Object or Module count.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `MyHOME Technical Guide.pdf` | June 2025 shared energy guide: wiring, load control and consumption topology; no exact 3456/F450 match and no specifications transferred to those products. |
| `ST-00001811-EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `U4725D.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `F521-publisher-product-sheet.pdf` | Captured exact-variant identity and complete technical classification attributes tabulated above; document links are discovery provenance, not additional independently verified capability. |

## Evidence limits and open work

Installed firmware, time distribution, retention under bus loss, and diagnostic/energy behavior are not yet captured; publisher-specific Legrand instructions and current historical-guide compatibility are incomplete.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
