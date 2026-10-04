# Three-input electricity meter

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0120` | Project identity |
| Technical description | Three-input electricity meter | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `F520`, `003555` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1160` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | New energy saving and load control | Main system association |
| Item model / `modobj` | `4` | Main association; independent of project ID |
| Firmware definition | `235`, `736` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `3` | Firmware metadata |
| Categories | Energy management, Sensors | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F520` | Established catalogue identity | Manufacturer database commercial record `1160` explicitly links this SKU to item `1160` |
| Legrand | `003555` | Established catalogue identity | Manufacturer database commercial record `1894` explicitly links this SKU to item `1160` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MyHOME Technical Guide.pdf` | English system technical guide | `AD-EXMH25GT; Versione 6/2025 printed on rear cover` | Energy/load functions and installation topology: printed/PDF pp. 74-80, 90, 96, 101. No exact 3456/F450 match; no rating transferred to those products. | [Archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MyHOME Technical Guide.pdf) |
| `ST-00001810-EN.pdf` | Technical Sheet ST-00001810-EN | `ST-00001810-EN; 28/05/2024` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-4; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/4b/52/4b52a9d26bba3549782f9c65e41c89acaafe645b07e46054e1214a84e47ffcf1.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00001810-EN.pdf) |
| `U4724E.pdf` | Instruction Use U4724E | `U4724E; 05/24-01 PC` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-4; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/11/7e/117e45fbbbd1c684aa08b98cba3485ac14cab079e94623f82941c321e1a06000.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/U4724E.pdf) |
| `F520-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 04.10.2026` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-3; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/e4/61/e461d606f9422c0eb12a1067e74e1e6392675356acd35add4f062be073bb56f8.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-F520&include_technical=1) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `1160` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mains input | `110..240 Vac; 50/60 Hz` | `ST-00001810-EN` printed/PDF pp. 1-4 |
| SCS supply | `18..27 Vdc` | `ST-00001810-EN` printed/PDF pp. 1-4 |
| SCS draw | `35 mA max` | `ST-00001810-EN` printed/PDF pp. 1-4 |
| Operating temperature | `5..40 °C` | `ST-00001810-EN` printed/PDF pp. 1-4 |
| Mounting | `1 DIN module` | `ST-00001810-EN` printed/PDF pp. 1-4 |
| Measured / nominal current | `90 A maximum / 16 A nominal` | `ST-00001810-EN` printed/PDF pp. 1-4 |
| Functions | `3 separate toroid inputs; instantaneous W and cumulative Wh` | `ST-00001810-EN` printed/PDF pp. 1-4 |
| Historical storage | `hourly: 12 months; daily: 2 years; monthly: 12 years` | `ST-00001810-EN` printed/PDF pp. 1-4 |
| Toroid accessory | `3523; one supplied` | `ST-00001810-EN` printed/PDF pp. 1-4 |
| Mains protection | `<=16 A thermal magnetic circuit breaker` | `ST-00001810-EN` printed/PDF pp. 1-4 |


### Publisher export attributes

These are the captured publisher classification values for the named variants. They do not override a technical sheet’s ratings or prove runtime protocol support. A negative radio-bus/connected-object classification is not evidence against separately documented gateway or Wi-Fi behavior.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| EAN | `8005543402061` | `F520` export p. 1 |
| Bus system KNX | `No` | `F520` export p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `F520` export p. 2 |
| Bus system radio frequency | `No` | `F520` export p. 2 |
| Bus system LON | `No` | `F520` export p. 2 |
| Bus system Powernet | `No` | `F520` export p. 2 |
| Other bus systems | `Other` | `F520` export p. 2 |
| Model | `Direct/transformer` | `F520` export p. 2 |
| Connection type | `Direct` | `F520` export p. 2 |
| Reactive power | `No` | `F520` export p. 2 |
| Approved according to PTB | `No` | `F520` export p. 2 |
| S0 impulse interface | `None` | `F520` export p. 2 |
| Tariff switch | `No` | `F520` export p. 2 |
| Connected object | `No` | `F520` export p. 2 |

### Published status indicators



| State | LED indication | Source |
| --- | --- | --- |
| not configured | `orange/green 128 ms/128 ms` | Exact technical sheet, indicator table in Documentation |
| configuration error | `irregular orange on green` | Exact technical sheet, indicator table in Documentation |
| normal | `green` | Exact technical sheet, indicator table in Documentation |
| insufficient bus/drop | `green 500 ms/500 ms` | Exact technical sheet, indicator table in Documentation |
| no mains | `red 100 ms/900 ms` | Exact technical sheet, indicator table in Documentation |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1160` | Canonical catalogue |
| Technical item description | Bus meter with memory 3-inputs for toroids - 1 DIN | Canonical catalogue |
| Item family | Energy saving (control unit, meter, counter); key `12` | Canonical catalogue |
| Main system | New energy saving and load control; key `20` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `4` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `235` | `-1` | `-1` | `-1` | `3` | Catalogue default | Official |
| `736` | `3` | `0` | `0` | `3` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `235` | `1` | `198` Energy metering | Fixed/designated metadata | `1185` | `469` | `638` |
| `235` | `2` | `198` Energy metering | Fixed/designated metadata | `1186` | `469` | `638` |
| `235` | `3` | `198` Energy metering | Fixed/designated metadata | `1187` | `469` | `638` |
| `736` | `1` | `198` Energy metering | Fixed/designated metadata | `2667` | `469` | `1277` |
| `736` | `2` | `198` Energy metering | Fixed/designated metadata | `2668` | `469` | `1277` |
| `736` | `3` | `198` Energy metering | Fixed/designated metadata | `2669` | `469` | `1277` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `235` | Virtual Configuration | `1` | Association key `1` |
| `235` | Advanced Configuration | `2` | Association key `2` |
| `235` | Physical configuration | `0` | Association key `3` |
| `736` | Virtual Configuration | `1` | Association key `1` |
| `736` | Advanced Configuration | `2` | Association key `2` |
| `736` | Physical configuration | `0` | Association key `3` |


No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

### Published physical metering selectors



| Selector | Physical domain / meaning | Published software scope |
| --- | --- | --- |
| Address | `1..127` | software address `0..127`; catalogue restrictions separately tabulated |
| Toroid direction | `T=0:orientation independent; T=1:directional` | same two documented direction choices |
| Clock | system date/time required | absence prevents historical saving, not instantaneous measurement |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `235` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `235` | `A1` | `0..2` | `0` | A1; Energy Management A1 Address (0-2) |
| `235` | `A2` | `0..9` | `0` | A2; Energy Management A2 Address (0-9) |
| `235` | `A3-TA` | `0..9` | `0` | A3-Ta; Energy Management A3Ta Address (0-9) |
| `235` | `A3-TB` | `0..9` | `0` | A3-Tb; Energy Management A3Tb Address (0-9) |
| `235` | `A3-TC` | `0..9` | `0` | A3-Tc; Energy Management A3Tc Address (0-9) |
| `736` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `736` | `A1` | `0..1` | `0` | A1; Energy Management A1 Address (0-2) |
| `736` | `A2` | `0..9` | `0` | A2; Energy Management A2 Address (0-9) |
| `736` | `A3-TA` | `0..9` | `0` | A3-Ta; Energy Management A3Ta Address (0-9) |
| `736` | `A3-TB` | `0..9` | `0` | A3-Tb; Energy Management A3Tb Address (0-9) |
| `736` | `A3-TC` | `0..9` | `0` | A3-Tc; Energy Management A3Tc Address (0-9) |
| `736` | `T↑` | `0..1` | `0` | Toroid direction management |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `198` - Energy metering

Catalogue Object key `469` maps to external Object `198`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A123` | `0..127` | `0` | Address; Energy Management A123 Address (0-255) |
| `TOROID_DIRECTION` | `0` = Disabled; `1` = Enabled | `0` | Toroid direction management |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `235` | `1` | `198` | `4159` | No textual predicate stored | `700` |
| `235` | `2` | `198` | `4160` | No textual predicate stored | `730` |
| `235` | `3` | `198` | `4161` | No textual predicate stored | `760` |
| `736` | `1` | `198` | `4159` | No textual predicate stored | `700` |
| `736` | `2` | `198` | `4160` | No textual predicate stored | `730` |
| `736` | `3` | `198` | `4161` | No textual predicate stored | `760` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `235` | `198` | `3004` | `TOROID_DIRECTION` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | Toroid direction management |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `700` | `A1=0; A2=0; A3-Ta=0` | `A123` = `0` | `700` → `701` → `702` |
| `700` | `A1=0; A2=0; A3-Ta=1` | `A123` = `1` | `700` → `701` → `702` |
| `700` | `A1=0; A2=0; A3-Ta=2` | `A123` = `2` | `700` → `701` → `702` |
| `700` | `A1=0; A2=0; A3-Ta=3` | `A123` = `3` | `700` → `701` → `702` |
| `700` | `A1=0; A2=0; A3-Ta=4` | `A123` = `4` | `700` → `701` → `702` |
| `700` | `A1=0; A2=0; A3-Ta=5` | `A123` = `5` | `700` → `701` → `702` |
| `700` | `A1=0; A2=0; A3-Ta=6` | `A123` = `6` | `700` → `701` → `702` |
| `700` | `A1=0; A2=0; A3-Ta=7` | `A123` = `7` | `700` → `701` → `702` |
| `700` | `A1=0; A2=0; A3-Ta=8` | `A123` = `8` | `700` → `701` → `702` |
| `700` | `A1=0; A2=0; A3-Ta=9` | `A123` = `9` | `700` → `701` → `702` |
| `700` | `A1=0; A2=1; A3-Ta=0` | `A123` = `10` | `700` → `701` → `703` |
| `700` | `A1=0; A2=1; A3-Ta=1` | `A123` = `11` | `700` → `701` → `703` |
| `700` | `A1=0; A2=1; A3-Ta=2` | `A123` = `12` | `700` → `701` → `703` |
| `700` | `A1=0; A2=1; A3-Ta=3` | `A123` = `13` | `700` → `701` → `703` |
| `700` | `A1=0; A2=1; A3-Ta=4` | `A123` = `14` | `700` → `701` → `703` |
| `700` | `A1=0; A2=1; A3-Ta=5` | `A123` = `15` | `700` → `701` → `703` |
| `700` | `A1=0; A2=1; A3-Ta=6` | `A123` = `16` | `700` → `701` → `703` |
| `700` | `A1=0; A2=1; A3-Ta=7` | `A123` = `17` | `700` → `701` → `703` |
| `700` | `A1=0; A2=1; A3-Ta=8` | `A123` = `18` | `700` → `701` → `703` |
| `700` | `A1=0; A2=1; A3-Ta=9` | `A123` = `19` | `700` → `701` → `703` |
| `700` | `A1=0; A2=2; A3-Ta=0` | `A123` = `20` | `700` → `701` → `704` |
| `700` | `A1=0; A2=2; A3-Ta=1` | `A123` = `21` | `700` → `701` → `704` |
| `700` | `A1=0; A2=2; A3-Ta=2` | `A123` = `22` | `700` → `701` → `704` |
| `700` | `A1=0; A2=2; A3-Ta=3` | `A123` = `23` | `700` → `701` → `704` |
| `700` | `A1=0; A2=2; A3-Ta=4` | `A123` = `24` | `700` → `701` → `704` |
| `700` | `A1=0; A2=2; A3-Ta=5` | `A123` = `25` | `700` → `701` → `704` |
| `700` | `A1=0; A2=2; A3-Ta=6` | `A123` = `26` | `700` → `701` → `704` |
| `700` | `A1=0; A2=2; A3-Ta=7` | `A123` = `27` | `700` → `701` → `704` |
| `700` | `A1=0; A2=2; A3-Ta=8` | `A123` = `28` | `700` → `701` → `704` |
| `700` | `A1=0; A2=2; A3-Ta=9` | `A123` = `29` | `700` → `701` → `704` |
| `700` | `A1=0; A2=3; A3-Ta=0` | `A123` = `30` | `700` → `701` → `705` |
| `700` | `A1=0; A2=3; A3-Ta=1` | `A123` = `31` | `700` → `701` → `705` |
| `700` | `A1=0; A2=3; A3-Ta=2` | `A123` = `32` | `700` → `701` → `705` |
| `700` | `A1=0; A2=3; A3-Ta=3` | `A123` = `33` | `700` → `701` → `705` |
| `700` | `A1=0; A2=3; A3-Ta=4` | `A123` = `34` | `700` → `701` → `705` |
| `700` | `A1=0; A2=3; A3-Ta=5` | `A123` = `35` | `700` → `701` → `705` |
| `700` | `A1=0; A2=3; A3-Ta=6` | `A123` = `36` | `700` → `701` → `705` |
| `700` | `A1=0; A2=3; A3-Ta=7` | `A123` = `37` | `700` → `701` → `705` |
| `700` | `A1=0; A2=3; A3-Ta=8` | `A123` = `38` | `700` → `701` → `705` |
| `700` | `A1=0; A2=3; A3-Ta=9` | `A123` = `39` | `700` → `701` → `705` |
| `700` | `A1=0; A2=4; A3-Ta=0` | `A123` = `40` | `700` → `701` → `706` |
| `700` | `A1=0; A2=4; A3-Ta=1` | `A123` = `41` | `700` → `701` → `706` |
| `700` | `A1=0; A2=4; A3-Ta=2` | `A123` = `42` | `700` → `701` → `706` |
| `700` | `A1=0; A2=4; A3-Ta=3` | `A123` = `43` | `700` → `701` → `706` |
| `700` | `A1=0; A2=4; A3-Ta=4` | `A123` = `44` | `700` → `701` → `706` |
| `700` | `A1=0; A2=4; A3-Ta=5` | `A123` = `45` | `700` → `701` → `706` |
| `700` | `A1=0; A2=4; A3-Ta=6` | `A123` = `46` | `700` → `701` → `706` |
| `700` | `A1=0; A2=4; A3-Ta=7` | `A123` = `47` | `700` → `701` → `706` |
| `700` | `A1=0; A2=4; A3-Ta=8` | `A123` = `48` | `700` → `701` → `706` |
| `700` | `A1=0; A2=4; A3-Ta=9` | `A123` = `49` | `700` → `701` → `706` |
| `700` | `A1=0; A2=5; A3-Ta=0` | `A123` = `50` | `700` → `701` → `707` |
| `700` | `A1=0; A2=5; A3-Ta=1` | `A123` = `51` | `700` → `701` → `707` |
| `700` | `A1=0; A2=5; A3-Ta=2` | `A123` = `52` | `700` → `701` → `707` |
| `700` | `A1=0; A2=5; A3-Ta=3` | `A123` = `53` | `700` → `701` → `707` |
| `700` | `A1=0; A2=5; A3-Ta=4` | `A123` = `54` | `700` → `701` → `707` |
| `700` | `A1=0; A2=5; A3-Ta=5` | `A123` = `55` | `700` → `701` → `707` |
| `700` | `A1=0; A2=5; A3-Ta=6` | `A123` = `56` | `700` → `701` → `707` |
| `700` | `A1=0; A2=5; A3-Ta=7` | `A123` = `57` | `700` → `701` → `707` |
| `700` | `A1=0; A2=5; A3-Ta=8` | `A123` = `58` | `700` → `701` → `707` |
| `700` | `A1=0; A2=5; A3-Ta=9` | `A123` = `59` | `700` → `701` → `707` |
| `700` | `A1=0; A2=6; A3-Ta=0` | `A123` = `60` | `700` → `701` → `708` |
| `700` | `A1=0; A2=6; A3-Ta=1` | `A123` = `61` | `700` → `701` → `708` |
| `700` | `A1=0; A2=6; A3-Ta=2` | `A123` = `62` | `700` → `701` → `708` |
| `700` | `A1=0; A2=6; A3-Ta=3` | `A123` = `63` | `700` → `701` → `708` |
| `700` | `A1=0; A2=6; A3-Ta=4` | `A123` = `64` | `700` → `701` → `708` |
| `700` | `A1=0; A2=6; A3-Ta=5` | `A123` = `65` | `700` → `701` → `708` |
| `700` | `A1=0; A2=6; A3-Ta=6` | `A123` = `66` | `700` → `701` → `708` |
| `700` | `A1=0; A2=6; A3-Ta=7` | `A123` = `67` | `700` → `701` → `708` |
| `700` | `A1=0; A2=6; A3-Ta=8` | `A123` = `68` | `700` → `701` → `708` |
| `700` | `A1=0; A2=6; A3-Ta=9` | `A123` = `69` | `700` → `701` → `708` |
| `700` | `A1=0; A2=7; A3-Ta=0` | `A123` = `70` | `700` → `701` → `709` |
| `700` | `A1=0; A2=7; A3-Ta=1` | `A123` = `71` | `700` → `701` → `709` |
| `700` | `A1=0; A2=7; A3-Ta=2` | `A123` = `72` | `700` → `701` → `709` |
| `700` | `A1=0; A2=7; A3-Ta=3` | `A123` = `73` | `700` → `701` → `709` |
| `700` | `A1=0; A2=7; A3-Ta=4` | `A123` = `74` | `700` → `701` → `709` |
| `700` | `A1=0; A2=7; A3-Ta=5` | `A123` = `75` | `700` → `701` → `709` |
| `700` | `A1=0; A2=7; A3-Ta=6` | `A123` = `76` | `700` → `701` → `709` |
| `700` | `A1=0; A2=7; A3-Ta=7` | `A123` = `77` | `700` → `701` → `709` |
| `700` | `A1=0; A2=7; A3-Ta=8` | `A123` = `78` | `700` → `701` → `709` |
| `700` | `A1=0; A2=7; A3-Ta=9` | `A123` = `79` | `700` → `701` → `709` |
| `700` | `A1=0; A2=8; A3-Ta=0` | `A123` = `80` | `700` → `701` → `710` |
| `700` | `A1=0; A2=8; A3-Ta=1` | `A123` = `81` | `700` → `701` → `710` |
| `700` | `A1=0; A2=8; A3-Ta=2` | `A123` = `82` | `700` → `701` → `710` |
| `700` | `A1=0; A2=8; A3-Ta=3` | `A123` = `83` | `700` → `701` → `710` |
| `700` | `A1=0; A2=8; A3-Ta=4` | `A123` = `84` | `700` → `701` → `710` |
| `700` | `A1=0; A2=8; A3-Ta=5` | `A123` = `85` | `700` → `701` → `710` |
| `700` | `A1=0; A2=8; A3-Ta=6` | `A123` = `86` | `700` → `701` → `710` |
| `700` | `A1=0; A2=8; A3-Ta=7` | `A123` = `87` | `700` → `701` → `710` |
| `700` | `A1=0; A2=8; A3-Ta=8` | `A123` = `88` | `700` → `701` → `710` |
| `700` | `A1=0; A2=8; A3-Ta=9` | `A123` = `89` | `700` → `701` → `710` |
| `700` | `A1=0; A2=9; A3-Ta=0` | `A123` = `90` | `700` → `701` → `711` |
| `700` | `A1=0; A2=9; A3-Ta=1` | `A123` = `91` | `700` → `701` → `711` |
| `700` | `A1=0; A2=9; A3-Ta=2` | `A123` = `92` | `700` → `701` → `711` |
| `700` | `A1=0; A2=9; A3-Ta=3` | `A123` = `93` | `700` → `701` → `711` |
| `700` | `A1=0; A2=9; A3-Ta=4` | `A123` = `94` | `700` → `701` → `711` |
| `700` | `A1=0; A2=9; A3-Ta=5` | `A123` = `95` | `700` → `701` → `711` |
| `700` | `A1=0; A2=9; A3-Ta=6` | `A123` = `96` | `700` → `701` → `711` |
| `700` | `A1=0; A2=9; A3-Ta=7` | `A123` = `97` | `700` → `701` → `711` |
| `700` | `A1=0; A2=9; A3-Ta=8` | `A123` = `98` | `700` → `701` → `711` |
| `700` | `A1=0; A2=9; A3-Ta=9` | `A123` = `99` | `700` → `701` → `711` |
| `700` | `A1=1; A2=0; A3-Ta=0` | `A123` = `100` | `700` → `712` → `713` |
| `700` | `A1=1; A2=0; A3-Ta=1` | `A123` = `101` | `700` → `712` → `713` |
| `700` | `A1=1; A2=0; A3-Ta=2` | `A123` = `102` | `700` → `712` → `713` |
| `700` | `A1=1; A2=0; A3-Ta=3` | `A123` = `103` | `700` → `712` → `713` |
| `700` | `A1=1; A2=0; A3-Ta=4` | `A123` = `104` | `700` → `712` → `713` |
| `700` | `A1=1; A2=0; A3-Ta=5` | `A123` = `105` | `700` → `712` → `713` |
| `700` | `A1=1; A2=0; A3-Ta=6` | `A123` = `106` | `700` → `712` → `713` |
| `700` | `A1=1; A2=0; A3-Ta=7` | `A123` = `107` | `700` → `712` → `713` |
| `700` | `A1=1; A2=0; A3-Ta=8` | `A123` = `108` | `700` → `712` → `713` |
| `700` | `A1=1; A2=0; A3-Ta=9` | `A123` = `109` | `700` → `712` → `713` |
| `700` | `A1=1; A2=1; A3-Ta=0` | `A123` = `110` | `700` → `712` → `714` |
| `700` | `A1=1; A2=1; A3-Ta=1` | `A123` = `111` | `700` → `712` → `714` |
| `700` | `A1=1; A2=1; A3-Ta=2` | `A123` = `112` | `700` → `712` → `714` |
| `700` | `A1=1; A2=1; A3-Ta=3` | `A123` = `113` | `700` → `712` → `714` |
| `700` | `A1=1; A2=1; A3-Ta=4` | `A123` = `114` | `700` → `712` → `714` |
| `700` | `A1=1; A2=1; A3-Ta=5` | `A123` = `115` | `700` → `712` → `714` |
| `700` | `A1=1; A2=1; A3-Ta=6` | `A123` = `116` | `700` → `712` → `714` |
| `700` | `A1=1; A2=1; A3-Ta=7` | `A123` = `117` | `700` → `712` → `714` |
| `700` | `A1=1; A2=1; A3-Ta=8` | `A123` = `118` | `700` → `712` → `714` |
| `700` | `A1=1; A2=1; A3-Ta=9` | `A123` = `119` | `700` → `712` → `714` |
| `700` | `A1=1; A2=2; A3-Ta=0` | `A123` = `120` | `700` → `712` → `715` |
| `700` | `A1=1; A2=2; A3-Ta=1` | `A123` = `121` | `700` → `712` → `715` |
| `700` | `A1=1; A2=2; A3-Ta=2` | `A123` = `122` | `700` → `712` → `715` |
| `700` | `A1=1; A2=2; A3-Ta=3` | `A123` = `123` | `700` → `712` → `715` |
| `700` | `A1=1; A2=2; A3-Ta=4` | `A123` = `124` | `700` → `712` → `715` |
| `700` | `A1=1; A2=2; A3-Ta=5` | `A123` = `125` | `700` → `712` → `715` |
| `700` | `A1=1; A2=2; A3-Ta=6` | `A123` = `126` | `700` → `712` → `715` |
| `700` | `A1=1; A2=2; A3-Ta=7` | `A123` = `127` | `700` → `712` → `715` |
| `700` | `A1=1; A2=2; A3-Ta=8` | `A123` = `128` | `700` → `712` → `715` |
| `700` | `A1=1; A2=2; A3-Ta=9` | `A123` = `129` | `700` → `712` → `715` |
| `700` | `A1=1; A2=3; A3-Ta=0` | `A123` = `130` | `700` → `712` → `716` |
| `700` | `A1=1; A2=3; A3-Ta=1` | `A123` = `131` | `700` → `712` → `716` |
| `700` | `A1=1; A2=3; A3-Ta=2` | `A123` = `132` | `700` → `712` → `716` |
| `700` | `A1=1; A2=3; A3-Ta=3` | `A123` = `133` | `700` → `712` → `716` |
| `700` | `A1=1; A2=3; A3-Ta=4` | `A123` = `134` | `700` → `712` → `716` |
| `700` | `A1=1; A2=3; A3-Ta=5` | `A123` = `135` | `700` → `712` → `716` |
| `700` | `A1=1; A2=3; A3-Ta=6` | `A123` = `136` | `700` → `712` → `716` |
| `700` | `A1=1; A2=3; A3-Ta=7` | `A123` = `137` | `700` → `712` → `716` |
| `700` | `A1=1; A2=3; A3-Ta=8` | `A123` = `138` | `700` → `712` → `716` |
| `700` | `A1=1; A2=3; A3-Ta=9` | `A123` = `139` | `700` → `712` → `716` |
| `700` | `A1=1; A2=4; A3-Ta=0` | `A123` = `140` | `700` → `712` → `717` |
| `700` | `A1=1; A2=4; A3-Ta=1` | `A123` = `141` | `700` → `712` → `717` |
| `700` | `A1=1; A2=4; A3-Ta=2` | `A123` = `142` | `700` → `712` → `717` |
| `700` | `A1=1; A2=4; A3-Ta=3` | `A123` = `143` | `700` → `712` → `717` |
| `700` | `A1=1; A2=4; A3-Ta=4` | `A123` = `144` | `700` → `712` → `717` |
| `700` | `A1=1; A2=4; A3-Ta=5` | `A123` = `145` | `700` → `712` → `717` |
| `700` | `A1=1; A2=4; A3-Ta=6` | `A123` = `146` | `700` → `712` → `717` |
| `700` | `A1=1; A2=4; A3-Ta=7` | `A123` = `147` | `700` → `712` → `717` |
| `700` | `A1=1; A2=4; A3-Ta=8` | `A123` = `148` | `700` → `712` → `717` |
| `700` | `A1=1; A2=4; A3-Ta=9` | `A123` = `149` | `700` → `712` → `717` |
| `700` | `A1=1; A2=5; A3-Ta=0` | `A123` = `150` | `700` → `712` → `718` |
| `700` | `A1=1; A2=5; A3-Ta=1` | `A123` = `151` | `700` → `712` → `718` |
| `700` | `A1=1; A2=5; A3-Ta=2` | `A123` = `152` | `700` → `712` → `718` |
| `700` | `A1=1; A2=5; A3-Ta=3` | `A123` = `153` | `700` → `712` → `718` |
| `700` | `A1=1; A2=5; A3-Ta=4` | `A123` = `154` | `700` → `712` → `718` |
| `700` | `A1=1; A2=5; A3-Ta=5` | `A123` = `155` | `700` → `712` → `718` |
| `700` | `A1=1; A2=5; A3-Ta=6` | `A123` = `156` | `700` → `712` → `718` |
| `700` | `A1=1; A2=5; A3-Ta=7` | `A123` = `157` | `700` → `712` → `718` |
| `700` | `A1=1; A2=5; A3-Ta=8` | `A123` = `158` | `700` → `712` → `718` |
| `700` | `A1=1; A2=5; A3-Ta=9` | `A123` = `159` | `700` → `712` → `718` |
| `700` | `A1=1; A2=6; A3-Ta=0` | `A123` = `160` | `700` → `712` → `719` |
| `700` | `A1=1; A2=6; A3-Ta=1` | `A123` = `161` | `700` → `712` → `719` |
| `700` | `A1=1; A2=6; A3-Ta=2` | `A123` = `162` | `700` → `712` → `719` |
| `700` | `A1=1; A2=6; A3-Ta=3` | `A123` = `163` | `700` → `712` → `719` |
| `700` | `A1=1; A2=6; A3-Ta=4` | `A123` = `164` | `700` → `712` → `719` |
| `700` | `A1=1; A2=6; A3-Ta=5` | `A123` = `165` | `700` → `712` → `719` |
| `700` | `A1=1; A2=6; A3-Ta=6` | `A123` = `166` | `700` → `712` → `719` |
| `700` | `A1=1; A2=6; A3-Ta=7` | `A123` = `167` | `700` → `712` → `719` |
| `700` | `A1=1; A2=6; A3-Ta=8` | `A123` = `168` | `700` → `712` → `719` |
| `700` | `A1=1; A2=6; A3-Ta=9` | `A123` = `169` | `700` → `712` → `719` |
| `700` | `A1=1; A2=7; A3-Ta=0` | `A123` = `170` | `700` → `712` → `720` |
| `700` | `A1=1; A2=7; A3-Ta=1` | `A123` = `171` | `700` → `712` → `720` |
| `700` | `A1=1; A2=7; A3-Ta=2` | `A123` = `172` | `700` → `712` → `720` |
| `700` | `A1=1; A2=7; A3-Ta=3` | `A123` = `173` | `700` → `712` → `720` |
| `700` | `A1=1; A2=7; A3-Ta=4` | `A123` = `174` | `700` → `712` → `720` |
| `700` | `A1=1; A2=7; A3-Ta=5` | `A123` = `175` | `700` → `712` → `720` |
| `700` | `A1=1; A2=7; A3-Ta=6` | `A123` = `176` | `700` → `712` → `720` |
| `700` | `A1=1; A2=7; A3-Ta=7` | `A123` = `177` | `700` → `712` → `720` |
| `700` | `A1=1; A2=7; A3-Ta=8` | `A123` = `178` | `700` → `712` → `720` |
| `700` | `A1=1; A2=7; A3-Ta=9` | `A123` = `179` | `700` → `712` → `720` |
| `700` | `A1=1; A2=8; A3-Ta=0` | `A123` = `180` | `700` → `712` → `721` |
| `700` | `A1=1; A2=8; A3-Ta=1` | `A123` = `181` | `700` → `712` → `721` |
| `700` | `A1=1; A2=8; A3-Ta=2` | `A123` = `182` | `700` → `712` → `721` |
| `700` | `A1=1; A2=8; A3-Ta=3` | `A123` = `183` | `700` → `712` → `721` |
| `700` | `A1=1; A2=8; A3-Ta=4` | `A123` = `184` | `700` → `712` → `721` |
| `700` | `A1=1; A2=8; A3-Ta=5` | `A123` = `185` | `700` → `712` → `721` |
| `700` | `A1=1; A2=8; A3-Ta=6` | `A123` = `186` | `700` → `712` → `721` |
| `700` | `A1=1; A2=8; A3-Ta=7` | `A123` = `187` | `700` → `712` → `721` |
| `700` | `A1=1; A2=8; A3-Ta=8` | `A123` = `188` | `700` → `712` → `721` |
| `700` | `A1=1; A2=8; A3-Ta=9` | `A123` = `189` | `700` → `712` → `721` |
| `700` | `A1=1; A2=9; A3-Ta=0` | `A123` = `190` | `700` → `712` → `722` |
| `700` | `A1=1; A2=9; A3-Ta=1` | `A123` = `191` | `700` → `712` → `722` |
| `700` | `A1=1; A2=9; A3-Ta=2` | `A123` = `192` | `700` → `712` → `722` |
| `700` | `A1=1; A2=9; A3-Ta=3` | `A123` = `193` | `700` → `712` → `722` |
| `700` | `A1=1; A2=9; A3-Ta=4` | `A123` = `194` | `700` → `712` → `722` |
| `700` | `A1=1; A2=9; A3-Ta=5` | `A123` = `195` | `700` → `712` → `722` |
| `700` | `A1=1; A2=9; A3-Ta=6` | `A123` = `196` | `700` → `712` → `722` |
| `700` | `A1=1; A2=9; A3-Ta=7` | `A123` = `197` | `700` → `712` → `722` |
| `700` | `A1=1; A2=9; A3-Ta=8` | `A123` = `198` | `700` → `712` → `722` |
| `700` | `A1=1; A2=9; A3-Ta=9` | `A123` = `199` | `700` → `712` → `722` |
| `700` | `A1=2; A2=0; A3-Ta=0` | `A123` = `200` | `700` → `723` → `724` |
| `700` | `A1=2; A2=0; A3-Ta=1` | `A123` = `201` | `700` → `723` → `724` |
| `700` | `A1=2; A2=0; A3-Ta=2` | `A123` = `202` | `700` → `723` → `724` |
| `700` | `A1=2; A2=0; A3-Ta=3` | `A123` = `203` | `700` → `723` → `724` |
| `700` | `A1=2; A2=0; A3-Ta=4` | `A123` = `204` | `700` → `723` → `724` |
| `700` | `A1=2; A2=0; A3-Ta=5` | `A123` = `205` | `700` → `723` → `724` |
| `700` | `A1=2; A2=0; A3-Ta=6` | `A123` = `206` | `700` → `723` → `724` |
| `700` | `A1=2; A2=0; A3-Ta=7` | `A123` = `207` | `700` → `723` → `724` |
| `700` | `A1=2; A2=0; A3-Ta=8` | `A123` = `208` | `700` → `723` → `724` |
| `700` | `A1=2; A2=0; A3-Ta=9` | `A123` = `209` | `700` → `723` → `724` |
| `700` | `A1=2; A2=1; A3-Ta=0` | `A123` = `210` | `700` → `723` → `725` |
| `700` | `A1=2; A2=1; A3-Ta=1` | `A123` = `211` | `700` → `723` → `725` |
| `700` | `A1=2; A2=1; A3-Ta=2` | `A123` = `212` | `700` → `723` → `725` |
| `700` | `A1=2; A2=1; A3-Ta=3` | `A123` = `213` | `700` → `723` → `725` |
| `700` | `A1=2; A2=1; A3-Ta=4` | `A123` = `214` | `700` → `723` → `725` |
| `700` | `A1=2; A2=1; A3-Ta=5` | `A123` = `215` | `700` → `723` → `725` |
| `700` | `A1=2; A2=1; A3-Ta=6` | `A123` = `216` | `700` → `723` → `725` |
| `700` | `A1=2; A2=1; A3-Ta=7` | `A123` = `217` | `700` → `723` → `725` |
| `700` | `A1=2; A2=1; A3-Ta=8` | `A123` = `218` | `700` → `723` → `725` |
| `700` | `A1=2; A2=1; A3-Ta=9` | `A123` = `219` | `700` → `723` → `725` |
| `700` | `A1=2; A2=2; A3-Ta=0` | `A123` = `220` | `700` → `723` → `726` |
| `700` | `A1=2; A2=2; A3-Ta=1` | `A123` = `221` | `700` → `723` → `726` |
| `700` | `A1=2; A2=2; A3-Ta=2` | `A123` = `222` | `700` → `723` → `726` |
| `700` | `A1=2; A2=2; A3-Ta=3` | `A123` = `223` | `700` → `723` → `726` |
| `700` | `A1=2; A2=2; A3-Ta=4` | `A123` = `224` | `700` → `723` → `726` |
| `700` | `A1=2; A2=2; A3-Ta=5` | `A123` = `225` | `700` → `723` → `726` |
| `700` | `A1=2; A2=2; A3-Ta=6` | `A123` = `226` | `700` → `723` → `726` |
| `700` | `A1=2; A2=2; A3-Ta=7` | `A123` = `227` | `700` → `723` → `726` |
| `700` | `A1=2; A2=2; A3-Ta=8` | `A123` = `228` | `700` → `723` → `726` |
| `700` | `A1=2; A2=2; A3-Ta=9` | `A123` = `229` | `700` → `723` → `726` |
| `700` | `A1=2; A2=3; A3-Ta=0` | `A123` = `230` | `700` → `723` → `727` |
| `700` | `A1=2; A2=3; A3-Ta=1` | `A123` = `231` | `700` → `723` → `727` |
| `700` | `A1=2; A2=3; A3-Ta=2` | `A123` = `232` | `700` → `723` → `727` |
| `700` | `A1=2; A2=3; A3-Ta=3` | `A123` = `233` | `700` → `723` → `727` |
| `700` | `A1=2; A2=3; A3-Ta=4` | `A123` = `234` | `700` → `723` → `727` |
| `700` | `A1=2; A2=3; A3-Ta=5` | `A123` = `235` | `700` → `723` → `727` |
| `700` | `A1=2; A2=3; A3-Ta=6` | `A123` = `236` | `700` → `723` → `727` |
| `700` | `A1=2; A2=3; A3-Ta=7` | `A123` = `237` | `700` → `723` → `727` |
| `700` | `A1=2; A2=3; A3-Ta=8` | `A123` = `238` | `700` → `723` → `727` |
| `700` | `A1=2; A2=3; A3-Ta=9` | `A123` = `239` | `700` → `723` → `727` |
| `700` | `A1=2; A2=4; A3-Ta=0` | `A123` = `240` | `700` → `723` → `728` |
| `700` | `A1=2; A2=4; A3-Ta=1` | `A123` = `241` | `700` → `723` → `728` |
| `700` | `A1=2; A2=4; A3-Ta=2` | `A123` = `242` | `700` → `723` → `728` |
| `700` | `A1=2; A2=4; A3-Ta=3` | `A123` = `243` | `700` → `723` → `728` |
| `700` | `A1=2; A2=4; A3-Ta=4` | `A123` = `244` | `700` → `723` → `728` |
| `700` | `A1=2; A2=4; A3-Ta=5` | `A123` = `245` | `700` → `723` → `728` |
| `700` | `A1=2; A2=4; A3-Ta=6` | `A123` = `246` | `700` → `723` → `728` |
| `700` | `A1=2; A2=4; A3-Ta=7` | `A123` = `247` | `700` → `723` → `728` |
| `700` | `A1=2; A2=4; A3-Ta=8` | `A123` = `248` | `700` → `723` → `728` |
| `700` | `A1=2; A2=4; A3-Ta=9` | `A123` = `249` | `700` → `723` → `728` |
| `700` | `A1=2; A2=5; A3-Ta=0` | `A123` = `250` | `700` → `723` → `729` |
| `700` | `A1=2; A2=5; A3-Ta=1` | `A123` = `251` | `700` → `723` → `729` |
| `700` | `A1=2; A2=5; A3-Ta=2` | `A123` = `252` | `700` → `723` → `729` |
| `700` | `A1=2; A2=5; A3-Ta=3` | `A123` = `253` | `700` → `723` → `729` |
| `700` | `A1=2; A2=5; A3-Ta=4` | `A123` = `254` | `700` → `723` → `729` |
| `700` | `A1=2; A2=5; A3-Ta=5` | `A123` = `255` | `700` → `723` → `729` |
| `730` | `A1=0; A2=0; A3-Tb=0` | `A123` = `0` | `730` → `731` → `732` |
| `730` | `A1=0; A2=0; A3-Tb=1` | `A123` = `1` | `730` → `731` → `732` |
| `730` | `A1=0; A2=0; A3-Tb=2` | `A123` = `2` | `730` → `731` → `732` |
| `730` | `A1=0; A2=0; A3-Tb=3` | `A123` = `3` | `730` → `731` → `732` |
| `730` | `A1=0; A2=0; A3-Tb=4` | `A123` = `4` | `730` → `731` → `732` |
| `730` | `A1=0; A2=0; A3-Tb=5` | `A123` = `5` | `730` → `731` → `732` |
| `730` | `A1=0; A2=0; A3-Tb=6` | `A123` = `6` | `730` → `731` → `732` |
| `730` | `A1=0; A2=0; A3-Tb=7` | `A123` = `7` | `730` → `731` → `732` |
| `730` | `A1=0; A2=0; A3-Tb=8` | `A123` = `8` | `730` → `731` → `732` |
| `730` | `A1=0; A2=0; A3-Tb=9` | `A123` = `9` | `730` → `731` → `732` |
| `730` | `A1=0; A2=1; A3-Tb=0` | `A123` = `10` | `730` → `731` → `733` |
| `730` | `A1=0; A2=1; A3-Tb=1` | `A123` = `11` | `730` → `731` → `733` |
| `730` | `A1=0; A2=1; A3-Tb=2` | `A123` = `12` | `730` → `731` → `733` |
| `730` | `A1=0; A2=1; A3-Tb=3` | `A123` = `13` | `730` → `731` → `733` |
| `730` | `A1=0; A2=1; A3-Tb=4` | `A123` = `14` | `730` → `731` → `733` |
| `730` | `A1=0; A2=1; A3-Tb=5` | `A123` = `15` | `730` → `731` → `733` |
| `730` | `A1=0; A2=1; A3-Tb=6` | `A123` = `16` | `730` → `731` → `733` |
| `730` | `A1=0; A2=1; A3-Tb=7` | `A123` = `17` | `730` → `731` → `733` |
| `730` | `A1=0; A2=1; A3-Tb=8` | `A123` = `18` | `730` → `731` → `733` |
| `730` | `A1=0; A2=1; A3-Tb=9` | `A123` = `19` | `730` → `731` → `733` |
| `730` | `A1=0; A2=2; A3-Tb=0` | `A123` = `20` | `730` → `731` → `734` |
| `730` | `A1=0; A2=2; A3-Tb=1` | `A123` = `21` | `730` → `731` → `734` |
| `730` | `A1=0; A2=2; A3-Tb=2` | `A123` = `22` | `730` → `731` → `734` |
| `730` | `A1=0; A2=2; A3-Tb=3` | `A123` = `23` | `730` → `731` → `734` |
| `730` | `A1=0; A2=2; A3-Tb=4` | `A123` = `24` | `730` → `731` → `734` |
| `730` | `A1=0; A2=2; A3-Tb=5` | `A123` = `25` | `730` → `731` → `734` |
| `730` | `A1=0; A2=2; A3-Tb=6` | `A123` = `26` | `730` → `731` → `734` |
| `730` | `A1=0; A2=2; A3-Tb=7` | `A123` = `27` | `730` → `731` → `734` |
| `730` | `A1=0; A2=2; A3-Tb=8` | `A123` = `28` | `730` → `731` → `734` |
| `730` | `A1=0; A2=2; A3-Tb=9` | `A123` = `29` | `730` → `731` → `734` |
| `730` | `A1=0; A2=3; A3-Tb=0` | `A123` = `30` | `730` → `731` → `735` |
| `730` | `A1=0; A2=3; A3-Tb=1` | `A123` = `31` | `730` → `731` → `735` |
| `730` | `A1=0; A2=3; A3-Tb=2` | `A123` = `32` | `730` → `731` → `735` |
| `730` | `A1=0; A2=3; A3-Tb=3` | `A123` = `33` | `730` → `731` → `735` |
| `730` | `A1=0; A2=3; A3-Tb=4` | `A123` = `34` | `730` → `731` → `735` |
| `730` | `A1=0; A2=3; A3-Tb=5` | `A123` = `35` | `730` → `731` → `735` |
| `730` | `A1=0; A2=3; A3-Tb=6` | `A123` = `36` | `730` → `731` → `735` |
| `730` | `A1=0; A2=3; A3-Tb=7` | `A123` = `37` | `730` → `731` → `735` |
| `730` | `A1=0; A2=3; A3-Tb=8` | `A123` = `38` | `730` → `731` → `735` |
| `730` | `A1=0; A2=3; A3-Tb=9` | `A123` = `39` | `730` → `731` → `735` |
| `730` | `A1=0; A2=4; A3-Tb=0` | `A123` = `40` | `730` → `731` → `736` |
| `730` | `A1=0; A2=4; A3-Tb=1` | `A123` = `41` | `730` → `731` → `736` |
| `730` | `A1=0; A2=4; A3-Tb=2` | `A123` = `42` | `730` → `731` → `736` |
| `730` | `A1=0; A2=4; A3-Tb=3` | `A123` = `43` | `730` → `731` → `736` |
| `730` | `A1=0; A2=4; A3-Tb=4` | `A123` = `44` | `730` → `731` → `736` |
| `730` | `A1=0; A2=4; A3-Tb=5` | `A123` = `45` | `730` → `731` → `736` |
| `730` | `A1=0; A2=4; A3-Tb=6` | `A123` = `46` | `730` → `731` → `736` |
| `730` | `A1=0; A2=4; A3-Tb=7` | `A123` = `47` | `730` → `731` → `736` |
| `730` | `A1=0; A2=4; A3-Tb=8` | `A123` = `48` | `730` → `731` → `736` |
| `730` | `A1=0; A2=4; A3-Tb=9` | `A123` = `49` | `730` → `731` → `736` |
| `730` | `A1=0; A2=5; A3-Tb=0` | `A123` = `50` | `730` → `731` → `737` |
| `730` | `A1=0; A2=5; A3-Tb=1` | `A123` = `51` | `730` → `731` → `737` |
| `730` | `A1=0; A2=5; A3-Tb=2` | `A123` = `52` | `730` → `731` → `737` |
| `730` | `A1=0; A2=5; A3-Tb=3` | `A123` = `53` | `730` → `731` → `737` |
| `730` | `A1=0; A2=5; A3-Tb=4` | `A123` = `54` | `730` → `731` → `737` |
| `730` | `A1=0; A2=5; A3-Tb=5` | `A123` = `55` | `730` → `731` → `737` |
| `730` | `A1=0; A2=5; A3-Tb=6` | `A123` = `56` | `730` → `731` → `737` |
| `730` | `A1=0; A2=5; A3-Tb=7` | `A123` = `57` | `730` → `731` → `737` |
| `730` | `A1=0; A2=5; A3-Tb=8` | `A123` = `58` | `730` → `731` → `737` |
| `730` | `A1=0; A2=5; A3-Tb=9` | `A123` = `59` | `730` → `731` → `737` |
| `730` | `A1=0; A2=6; A3-Tb=0` | `A123` = `60` | `730` → `731` → `738` |
| `730` | `A1=0; A2=6; A3-Tb=1` | `A123` = `61` | `730` → `731` → `738` |
| `730` | `A1=0; A2=6; A3-Tb=2` | `A123` = `62` | `730` → `731` → `738` |
| `730` | `A1=0; A2=6; A3-Tb=3` | `A123` = `63` | `730` → `731` → `738` |
| `730` | `A1=0; A2=6; A3-Tb=4` | `A123` = `64` | `730` → `731` → `738` |
| `730` | `A1=0; A2=6; A3-Tb=5` | `A123` = `65` | `730` → `731` → `738` |
| `730` | `A1=0; A2=6; A3-Tb=6` | `A123` = `66` | `730` → `731` → `738` |
| `730` | `A1=0; A2=6; A3-Tb=7` | `A123` = `67` | `730` → `731` → `738` |
| `730` | `A1=0; A2=6; A3-Tb=8` | `A123` = `68` | `730` → `731` → `738` |
| `730` | `A1=0; A2=6; A3-Tb=9` | `A123` = `69` | `730` → `731` → `738` |
| `730` | `A1=0; A2=7; A3-Tb=0` | `A123` = `70` | `730` → `731` → `739` |
| `730` | `A1=0; A2=7; A3-Tb=1` | `A123` = `71` | `730` → `731` → `739` |
| `730` | `A1=0; A2=7; A3-Tb=2` | `A123` = `72` | `730` → `731` → `739` |
| `730` | `A1=0; A2=7; A3-Tb=3` | `A123` = `73` | `730` → `731` → `739` |
| `730` | `A1=0; A2=7; A3-Tb=4` | `A123` = `74` | `730` → `731` → `739` |
| `730` | `A1=0; A2=7; A3-Tb=5` | `A123` = `75` | `730` → `731` → `739` |
| `730` | `A1=0; A2=7; A3-Tb=6` | `A123` = `76` | `730` → `731` → `739` |
| `730` | `A1=0; A2=7; A3-Tb=7` | `A123` = `77` | `730` → `731` → `739` |
| `730` | `A1=0; A2=7; A3-Tb=8` | `A123` = `78` | `730` → `731` → `739` |
| `730` | `A1=0; A2=7; A3-Tb=9` | `A123` = `79` | `730` → `731` → `739` |
| `730` | `A1=0; A2=8; A3-Tb=0` | `A123` = `80` | `730` → `731` → `740` |
| `730` | `A1=0; A2=8; A3-Tb=1` | `A123` = `81` | `730` → `731` → `740` |
| `730` | `A1=0; A2=8; A3-Tb=2` | `A123` = `82` | `730` → `731` → `740` |
| `730` | `A1=0; A2=8; A3-Tb=3` | `A123` = `83` | `730` → `731` → `740` |
| `730` | `A1=0; A2=8; A3-Tb=4` | `A123` = `84` | `730` → `731` → `740` |
| `730` | `A1=0; A2=8; A3-Tb=5` | `A123` = `85` | `730` → `731` → `740` |
| `730` | `A1=0; A2=8; A3-Tb=6` | `A123` = `86` | `730` → `731` → `740` |
| `730` | `A1=0; A2=8; A3-Tb=7` | `A123` = `87` | `730` → `731` → `740` |
| `730` | `A1=0; A2=8; A3-Tb=8` | `A123` = `88` | `730` → `731` → `740` |
| `730` | `A1=0; A2=8; A3-Tb=9` | `A123` = `89` | `730` → `731` → `740` |
| `730` | `A1=0; A2=9; A3-Tb=0` | `A123` = `90` | `730` → `731` → `741` |
| `730` | `A1=0; A2=9; A3-Tb=1` | `A123` = `91` | `730` → `731` → `741` |
| `730` | `A1=0; A2=9; A3-Tb=2` | `A123` = `92` | `730` → `731` → `741` |
| `730` | `A1=0; A2=9; A3-Tb=3` | `A123` = `93` | `730` → `731` → `741` |
| `730` | `A1=0; A2=9; A3-Tb=4` | `A123` = `94` | `730` → `731` → `741` |
| `730` | `A1=0; A2=9; A3-Tb=5` | `A123` = `95` | `730` → `731` → `741` |
| `730` | `A1=0; A2=9; A3-Tb=6` | `A123` = `96` | `730` → `731` → `741` |
| `730` | `A1=0; A2=9; A3-Tb=7` | `A123` = `97` | `730` → `731` → `741` |
| `730` | `A1=0; A2=9; A3-Tb=8` | `A123` = `98` | `730` → `731` → `741` |
| `730` | `A1=0; A2=9; A3-Tb=9` | `A123` = `99` | `730` → `731` → `741` |
| `730` | `A1=1; A2=0; A3-Tb=0` | `A123` = `100` | `730` → `742` → `743` |
| `730` | `A1=1; A2=0; A3-Tb=1` | `A123` = `101` | `730` → `742` → `743` |
| `730` | `A1=1; A2=0; A3-Tb=2` | `A123` = `102` | `730` → `742` → `743` |
| `730` | `A1=1; A2=0; A3-Tb=3` | `A123` = `103` | `730` → `742` → `743` |
| `730` | `A1=1; A2=0; A3-Tb=4` | `A123` = `104` | `730` → `742` → `743` |
| `730` | `A1=1; A2=0; A3-Tb=5` | `A123` = `105` | `730` → `742` → `743` |
| `730` | `A1=1; A2=0; A3-Tb=6` | `A123` = `106` | `730` → `742` → `743` |
| `730` | `A1=1; A2=0; A3-Tb=7` | `A123` = `107` | `730` → `742` → `743` |
| `730` | `A1=1; A2=0; A3-Tb=8` | `A123` = `108` | `730` → `742` → `743` |
| `730` | `A1=1; A2=0; A3-Tb=9` | `A123` = `109` | `730` → `742` → `743` |
| `730` | `A1=1; A2=1; A3-Tb=0` | `A123` = `110` | `730` → `742` → `744` |
| `730` | `A1=1; A2=1; A3-Tb=1` | `A123` = `111` | `730` → `742` → `744` |
| `730` | `A1=1; A2=1; A3-Tb=2` | `A123` = `112` | `730` → `742` → `744` |
| `730` | `A1=1; A2=1; A3-Tb=3` | `A123` = `113` | `730` → `742` → `744` |
| `730` | `A1=1; A2=1; A3-Tb=4` | `A123` = `114` | `730` → `742` → `744` |
| `730` | `A1=1; A2=1; A3-Tb=5` | `A123` = `115` | `730` → `742` → `744` |
| `730` | `A1=1; A2=1; A3-Tb=6` | `A123` = `116` | `730` → `742` → `744` |
| `730` | `A1=1; A2=1; A3-Tb=7` | `A123` = `117` | `730` → `742` → `744` |
| `730` | `A1=1; A2=1; A3-Tb=8` | `A123` = `118` | `730` → `742` → `744` |
| `730` | `A1=1; A2=1; A3-Tb=9` | `A123` = `119` | `730` → `742` → `744` |
| `730` | `A1=1; A2=2; A3-Tb=0` | `A123` = `120` | `730` → `742` → `745` |
| `730` | `A1=1; A2=2; A3-Tb=1` | `A123` = `121` | `730` → `742` → `745` |
| `730` | `A1=1; A2=2; A3-Tb=2` | `A123` = `122` | `730` → `742` → `745` |
| `730` | `A1=1; A2=2; A3-Tb=3` | `A123` = `123` | `730` → `742` → `745` |
| `730` | `A1=1; A2=2; A3-Tb=4` | `A123` = `124` | `730` → `742` → `745` |
| `730` | `A1=1; A2=2; A3-Tb=5` | `A123` = `125` | `730` → `742` → `745` |
| `730` | `A1=1; A2=2; A3-Tb=6` | `A123` = `126` | `730` → `742` → `745` |
| `730` | `A1=1; A2=2; A3-Tb=7` | `A123` = `127` | `730` → `742` → `745` |
| `730` | `A1=1; A2=2; A3-Tb=8` | `A123` = `128` | `730` → `742` → `745` |
| `730` | `A1=1; A2=2; A3-Tb=9` | `A123` = `129` | `730` → `742` → `745` |
| `730` | `A1=1; A2=3; A3-Tb=0` | `A123` = `130` | `730` → `742` → `746` |
| `730` | `A1=1; A2=3; A3-Tb=1` | `A123` = `131` | `730` → `742` → `746` |
| `730` | `A1=1; A2=3; A3-Tb=2` | `A123` = `132` | `730` → `742` → `746` |
| `730` | `A1=1; A2=3; A3-Tb=3` | `A123` = `133` | `730` → `742` → `746` |
| `730` | `A1=1; A2=3; A3-Tb=4` | `A123` = `134` | `730` → `742` → `746` |
| `730` | `A1=1; A2=3; A3-Tb=5` | `A123` = `135` | `730` → `742` → `746` |
| `730` | `A1=1; A2=3; A3-Tb=6` | `A123` = `136` | `730` → `742` → `746` |
| `730` | `A1=1; A2=3; A3-Tb=7` | `A123` = `137` | `730` → `742` → `746` |
| `730` | `A1=1; A2=3; A3-Tb=8` | `A123` = `138` | `730` → `742` → `746` |
| `730` | `A1=1; A2=3; A3-Tb=9` | `A123` = `139` | `730` → `742` → `746` |
| `730` | `A1=1; A2=4; A3-Tb=0` | `A123` = `140` | `730` → `742` → `747` |
| `730` | `A1=1; A2=4; A3-Tb=1` | `A123` = `141` | `730` → `742` → `747` |
| `730` | `A1=1; A2=4; A3-Tb=2` | `A123` = `142` | `730` → `742` → `747` |
| `730` | `A1=1; A2=4; A3-Tb=3` | `A123` = `143` | `730` → `742` → `747` |
| `730` | `A1=1; A2=4; A3-Tb=4` | `A123` = `144` | `730` → `742` → `747` |
| `730` | `A1=1; A2=4; A3-Tb=5` | `A123` = `145` | `730` → `742` → `747` |
| `730` | `A1=1; A2=4; A3-Tb=6` | `A123` = `146` | `730` → `742` → `747` |
| `730` | `A1=1; A2=4; A3-Tb=7` | `A123` = `147` | `730` → `742` → `747` |
| `730` | `A1=1; A2=4; A3-Tb=8` | `A123` = `148` | `730` → `742` → `747` |
| `730` | `A1=1; A2=4; A3-Tb=9` | `A123` = `149` | `730` → `742` → `747` |
| `730` | `A1=1; A2=5; A3-Tb=0` | `A123` = `150` | `730` → `742` → `748` |
| `730` | `A1=1; A2=5; A3-Tb=1` | `A123` = `151` | `730` → `742` → `748` |
| `730` | `A1=1; A2=5; A3-Tb=2` | `A123` = `152` | `730` → `742` → `748` |
| `730` | `A1=1; A2=5; A3-Tb=3` | `A123` = `153` | `730` → `742` → `748` |
| `730` | `A1=1; A2=5; A3-Tb=4` | `A123` = `154` | `730` → `742` → `748` |
| `730` | `A1=1; A2=5; A3-Tb=5` | `A123` = `155` | `730` → `742` → `748` |
| `730` | `A1=1; A2=5; A3-Tb=6` | `A123` = `156` | `730` → `742` → `748` |
| `730` | `A1=1; A2=5; A3-Tb=7` | `A123` = `157` | `730` → `742` → `748` |
| `730` | `A1=1; A2=5; A3-Tb=8` | `A123` = `158` | `730` → `742` → `748` |
| `730` | `A1=1; A2=5; A3-Tb=9` | `A123` = `159` | `730` → `742` → `748` |
| `730` | `A1=1; A2=6; A3-Tb=0` | `A123` = `160` | `730` → `742` → `749` |
| `730` | `A1=1; A2=6; A3-Tb=1` | `A123` = `161` | `730` → `742` → `749` |
| `730` | `A1=1; A2=6; A3-Tb=2` | `A123` = `162` | `730` → `742` → `749` |
| `730` | `A1=1; A2=6; A3-Tb=3` | `A123` = `163` | `730` → `742` → `749` |
| `730` | `A1=1; A2=6; A3-Tb=4` | `A123` = `164` | `730` → `742` → `749` |
| `730` | `A1=1; A2=6; A3-Tb=5` | `A123` = `165` | `730` → `742` → `749` |
| `730` | `A1=1; A2=6; A3-Tb=6` | `A123` = `166` | `730` → `742` → `749` |
| `730` | `A1=1; A2=6; A3-Tb=7` | `A123` = `167` | `730` → `742` → `749` |
| `730` | `A1=1; A2=6; A3-Tb=8` | `A123` = `168` | `730` → `742` → `749` |
| `730` | `A1=1; A2=6; A3-Tb=9` | `A123` = `169` | `730` → `742` → `749` |
| `730` | `A1=1; A2=7; A3-Tb=0` | `A123` = `170` | `730` → `742` → `750` |
| `730` | `A1=1; A2=7; A3-Tb=1` | `A123` = `171` | `730` → `742` → `750` |
| `730` | `A1=1; A2=7; A3-Tb=2` | `A123` = `172` | `730` → `742` → `750` |
| `730` | `A1=1; A2=7; A3-Tb=3` | `A123` = `173` | `730` → `742` → `750` |
| `730` | `A1=1; A2=7; A3-Tb=4` | `A123` = `174` | `730` → `742` → `750` |
| `730` | `A1=1; A2=7; A3-Tb=5` | `A123` = `175` | `730` → `742` → `750` |
| `730` | `A1=1; A2=7; A3-Tb=6` | `A123` = `176` | `730` → `742` → `750` |
| `730` | `A1=1; A2=7; A3-Tb=7` | `A123` = `177` | `730` → `742` → `750` |
| `730` | `A1=1; A2=7; A3-Tb=8` | `A123` = `178` | `730` → `742` → `750` |
| `730` | `A1=1; A2=7; A3-Tb=9` | `A123` = `179` | `730` → `742` → `750` |
| `730` | `A1=1; A2=8; A3-Tb=0` | `A123` = `180` | `730` → `742` → `751` |
| `730` | `A1=1; A2=8; A3-Tb=1` | `A123` = `181` | `730` → `742` → `751` |
| `730` | `A1=1; A2=8; A3-Tb=2` | `A123` = `182` | `730` → `742` → `751` |
| `730` | `A1=1; A2=8; A3-Tb=3` | `A123` = `183` | `730` → `742` → `751` |
| `730` | `A1=1; A2=8; A3-Tb=4` | `A123` = `184` | `730` → `742` → `751` |
| `730` | `A1=1; A2=8; A3-Tb=5` | `A123` = `185` | `730` → `742` → `751` |
| `730` | `A1=1; A2=8; A3-Tb=6` | `A123` = `186` | `730` → `742` → `751` |
| `730` | `A1=1; A2=8; A3-Tb=7` | `A123` = `187` | `730` → `742` → `751` |
| `730` | `A1=1; A2=8; A3-Tb=8` | `A123` = `188` | `730` → `742` → `751` |
| `730` | `A1=1; A2=8; A3-Tb=9` | `A123` = `189` | `730` → `742` → `751` |
| `730` | `A1=1; A2=9; A3-Tb=0` | `A123` = `190` | `730` → `742` → `752` |
| `730` | `A1=1; A2=9; A3-Tb=1` | `A123` = `191` | `730` → `742` → `752` |
| `730` | `A1=1; A2=9; A3-Tb=2` | `A123` = `192` | `730` → `742` → `752` |
| `730` | `A1=1; A2=9; A3-Tb=3` | `A123` = `193` | `730` → `742` → `752` |
| `730` | `A1=1; A2=9; A3-Tb=4` | `A123` = `194` | `730` → `742` → `752` |
| `730` | `A1=1; A2=9; A3-Tb=5` | `A123` = `195` | `730` → `742` → `752` |
| `730` | `A1=1; A2=9; A3-Tb=6` | `A123` = `196` | `730` → `742` → `752` |
| `730` | `A1=1; A2=9; A3-Tb=7` | `A123` = `197` | `730` → `742` → `752` |
| `730` | `A1=1; A2=9; A3-Tb=8` | `A123` = `198` | `730` → `742` → `752` |
| `730` | `A1=1; A2=9; A3-Tb=9` | `A123` = `199` | `730` → `742` → `752` |
| `730` | `A1=2; A2=0; A3-Tb=0` | `A123` = `200` | `730` → `753` → `754` |
| `730` | `A1=2; A2=0; A3-Tb=1` | `A123` = `201` | `730` → `753` → `754` |
| `730` | `A1=2; A2=0; A3-Tb=2` | `A123` = `202` | `730` → `753` → `754` |
| `730` | `A1=2; A2=0; A3-Tb=3` | `A123` = `203` | `730` → `753` → `754` |
| `730` | `A1=2; A2=0; A3-Tb=4` | `A123` = `204` | `730` → `753` → `754` |
| `730` | `A1=2; A2=0; A3-Tb=5` | `A123` = `205` | `730` → `753` → `754` |
| `730` | `A1=2; A2=0; A3-Tb=6` | `A123` = `206` | `730` → `753` → `754` |
| `730` | `A1=2; A2=0; A3-Tb=7` | `A123` = `207` | `730` → `753` → `754` |
| `730` | `A1=2; A2=0; A3-Tb=8` | `A123` = `208` | `730` → `753` → `754` |
| `730` | `A1=2; A2=0; A3-Tb=9` | `A123` = `209` | `730` → `753` → `754` |
| `730` | `A1=2; A2=1; A3-Tb=0` | `A123` = `210` | `730` → `753` → `755` |
| `730` | `A1=2; A2=1; A3-Tb=1` | `A123` = `211` | `730` → `753` → `755` |
| `730` | `A1=2; A2=1; A3-Tb=2` | `A123` = `212` | `730` → `753` → `755` |
| `730` | `A1=2; A2=1; A3-Tb=3` | `A123` = `213` | `730` → `753` → `755` |
| `730` | `A1=2; A2=1; A3-Tb=4` | `A123` = `214` | `730` → `753` → `755` |
| `730` | `A1=2; A2=1; A3-Tb=5` | `A123` = `215` | `730` → `753` → `755` |
| `730` | `A1=2; A2=1; A3-Tb=6` | `A123` = `216` | `730` → `753` → `755` |
| `730` | `A1=2; A2=1; A3-Tb=7` | `A123` = `217` | `730` → `753` → `755` |
| `730` | `A1=2; A2=1; A3-Tb=8` | `A123` = `218` | `730` → `753` → `755` |
| `730` | `A1=2; A2=1; A3-Tb=9` | `A123` = `219` | `730` → `753` → `755` |
| `730` | `A1=2; A2=2; A3-Tb=0` | `A123` = `220` | `730` → `753` → `756` |
| `730` | `A1=2; A2=2; A3-Tb=1` | `A123` = `221` | `730` → `753` → `756` |
| `730` | `A1=2; A2=2; A3-Tb=2` | `A123` = `222` | `730` → `753` → `756` |
| `730` | `A1=2; A2=2; A3-Tb=3` | `A123` = `223` | `730` → `753` → `756` |
| `730` | `A1=2; A2=2; A3-Tb=4` | `A123` = `224` | `730` → `753` → `756` |
| `730` | `A1=2; A2=2; A3-Tb=5` | `A123` = `225` | `730` → `753` → `756` |
| `730` | `A1=2; A2=2; A3-Tb=6` | `A123` = `226` | `730` → `753` → `756` |
| `730` | `A1=2; A2=2; A3-Tb=7` | `A123` = `227` | `730` → `753` → `756` |
| `730` | `A1=2; A2=2; A3-Tb=8` | `A123` = `228` | `730` → `753` → `756` |
| `730` | `A1=2; A2=2; A3-Tb=9` | `A123` = `229` | `730` → `753` → `756` |
| `730` | `A1=2; A2=3; A3-Tb=0` | `A123` = `230` | `730` → `753` → `757` |
| `730` | `A1=2; A2=3; A3-Tb=1` | `A123` = `231` | `730` → `753` → `757` |
| `730` | `A1=2; A2=3; A3-Tb=2` | `A123` = `232` | `730` → `753` → `757` |
| `730` | `A1=2; A2=3; A3-Tb=3` | `A123` = `233` | `730` → `753` → `757` |
| `730` | `A1=2; A2=3; A3-Tb=4` | `A123` = `234` | `730` → `753` → `757` |
| `730` | `A1=2; A2=3; A3-Tb=5` | `A123` = `235` | `730` → `753` → `757` |
| `730` | `A1=2; A2=3; A3-Tb=6` | `A123` = `236` | `730` → `753` → `757` |
| `730` | `A1=2; A2=3; A3-Tb=7` | `A123` = `237` | `730` → `753` → `757` |
| `730` | `A1=2; A2=3; A3-Tb=8` | `A123` = `238` | `730` → `753` → `757` |
| `730` | `A1=2; A2=3; A3-Tb=9` | `A123` = `239` | `730` → `753` → `757` |
| `730` | `A1=2; A2=4; A3-Tb=0` | `A123` = `240` | `730` → `753` → `758` |
| `730` | `A1=2; A2=4; A3-Tb=1` | `A123` = `241` | `730` → `753` → `758` |
| `730` | `A1=2; A2=4; A3-Tb=2` | `A123` = `242` | `730` → `753` → `758` |
| `730` | `A1=2; A2=4; A3-Tb=3` | `A123` = `243` | `730` → `753` → `758` |
| `730` | `A1=2; A2=4; A3-Tb=4` | `A123` = `244` | `730` → `753` → `758` |
| `730` | `A1=2; A2=4; A3-Tb=5` | `A123` = `245` | `730` → `753` → `758` |
| `730` | `A1=2; A2=4; A3-Tb=6` | `A123` = `246` | `730` → `753` → `758` |
| `730` | `A1=2; A2=4; A3-Tb=7` | `A123` = `247` | `730` → `753` → `758` |
| `730` | `A1=2; A2=4; A3-Tb=8` | `A123` = `248` | `730` → `753` → `758` |
| `730` | `A1=2; A2=4; A3-Tb=9` | `A123` = `249` | `730` → `753` → `758` |
| `730` | `A1=2; A2=5; A3-Tb=0` | `A123` = `250` | `730` → `753` → `759` |
| `730` | `A1=2; A2=5; A3-Tb=1` | `A123` = `251` | `730` → `753` → `759` |
| `730` | `A1=2; A2=5; A3-Tb=2` | `A123` = `252` | `730` → `753` → `759` |
| `730` | `A1=2; A2=5; A3-Tb=3` | `A123` = `253` | `730` → `753` → `759` |
| `730` | `A1=2; A2=5; A3-Tb=4` | `A123` = `254` | `730` → `753` → `759` |
| `730` | `A1=2; A2=5; A3-Tb=5` | `A123` = `255` | `730` → `753` → `759` |
| `760` | `A1=0; A2=0; A3-Tc=0` | `A123` = `0` | `760` → `761` → `762` |
| `760` | `A1=0; A2=0; A3-Tc=1` | `A123` = `1` | `760` → `761` → `762` |
| `760` | `A1=0; A2=0; A3-Tc=2` | `A123` = `2` | `760` → `761` → `762` |
| `760` | `A1=0; A2=0; A3-Tc=3` | `A123` = `3` | `760` → `761` → `762` |
| `760` | `A1=0; A2=0; A3-Tc=4` | `A123` = `4` | `760` → `761` → `762` |
| `760` | `A1=0; A2=0; A3-Tc=5` | `A123` = `5` | `760` → `761` → `762` |
| `760` | `A1=0; A2=0; A3-Tc=6` | `A123` = `6` | `760` → `761` → `762` |
| `760` | `A1=0; A2=0; A3-Tc=7` | `A123` = `7` | `760` → `761` → `762` |
| `760` | `A1=0; A2=0; A3-Tc=8` | `A123` = `8` | `760` → `761` → `762` |
| `760` | `A1=0; A2=0; A3-Tc=9` | `A123` = `9` | `760` → `761` → `762` |
| `760` | `A1=0; A2=1; A3-Tc=0` | `A123` = `10` | `760` → `761` → `763` |
| `760` | `A1=0; A2=1; A3-Tc=1` | `A123` = `11` | `760` → `761` → `763` |
| `760` | `A1=0; A2=1; A3-Tc=2` | `A123` = `12` | `760` → `761` → `763` |
| `760` | `A1=0; A2=1; A3-Tc=3` | `A123` = `13` | `760` → `761` → `763` |
| `760` | `A1=0; A2=1; A3-Tc=4` | `A123` = `14` | `760` → `761` → `763` |
| `760` | `A1=0; A2=1; A3-Tc=5` | `A123` = `15` | `760` → `761` → `763` |
| `760` | `A1=0; A2=1; A3-Tc=6` | `A123` = `16` | `760` → `761` → `763` |
| `760` | `A1=0; A2=1; A3-Tc=7` | `A123` = `17` | `760` → `761` → `763` |
| `760` | `A1=0; A2=1; A3-Tc=8` | `A123` = `18` | `760` → `761` → `763` |
| `760` | `A1=0; A2=1; A3-Tc=9` | `A123` = `19` | `760` → `761` → `763` |
| `760` | `A1=0; A2=2; A3-Tc=0` | `A123` = `20` | `760` → `761` → `764` |
| `760` | `A1=0; A2=2; A3-Tc=1` | `A123` = `21` | `760` → `761` → `764` |
| `760` | `A1=0; A2=2; A3-Tc=2` | `A123` = `22` | `760` → `761` → `764` |
| `760` | `A1=0; A2=2; A3-Tc=3` | `A123` = `23` | `760` → `761` → `764` |
| `760` | `A1=0; A2=2; A3-Tc=4` | `A123` = `24` | `760` → `761` → `764` |
| `760` | `A1=0; A2=2; A3-Tc=5` | `A123` = `25` | `760` → `761` → `764` |
| `760` | `A1=0; A2=2; A3-Tc=6` | `A123` = `26` | `760` → `761` → `764` |
| `760` | `A1=0; A2=2; A3-Tc=7` | `A123` = `27` | `760` → `761` → `764` |
| `760` | `A1=0; A2=2; A3-Tc=8` | `A123` = `28` | `760` → `761` → `764` |
| `760` | `A1=0; A2=2; A3-Tc=9` | `A123` = `29` | `760` → `761` → `764` |
| `760` | `A1=0; A2=3; A3-Tc=0` | `A123` = `30` | `760` → `761` → `765` |
| `760` | `A1=0; A2=3; A3-Tc=1` | `A123` = `31` | `760` → `761` → `765` |
| `760` | `A1=0; A2=3; A3-Tc=2` | `A123` = `32` | `760` → `761` → `765` |
| `760` | `A1=0; A2=3; A3-Tc=3` | `A123` = `33` | `760` → `761` → `765` |
| `760` | `A1=0; A2=3; A3-Tc=4` | `A123` = `34` | `760` → `761` → `765` |
| `760` | `A1=0; A2=3; A3-Tc=5` | `A123` = `35` | `760` → `761` → `765` |
| `760` | `A1=0; A2=3; A3-Tc=6` | `A123` = `36` | `760` → `761` → `765` |
| `760` | `A1=0; A2=3; A3-Tc=7` | `A123` = `37` | `760` → `761` → `765` |
| `760` | `A1=0; A2=3; A3-Tc=8` | `A123` = `38` | `760` → `761` → `765` |
| `760` | `A1=0; A2=3; A3-Tc=9` | `A123` = `39` | `760` → `761` → `765` |
| `760` | `A1=0; A2=4; A3-Tc=0` | `A123` = `40` | `760` → `761` → `766` |
| `760` | `A1=0; A2=4; A3-Tc=1` | `A123` = `41` | `760` → `761` → `766` |
| `760` | `A1=0; A2=4; A3-Tc=2` | `A123` = `42` | `760` → `761` → `766` |
| `760` | `A1=0; A2=4; A3-Tc=3` | `A123` = `43` | `760` → `761` → `766` |
| `760` | `A1=0; A2=4; A3-Tc=4` | `A123` = `44` | `760` → `761` → `766` |
| `760` | `A1=0; A2=4; A3-Tc=5` | `A123` = `45` | `760` → `761` → `766` |
| `760` | `A1=0; A2=4; A3-Tc=6` | `A123` = `46` | `760` → `761` → `766` |
| `760` | `A1=0; A2=4; A3-Tc=7` | `A123` = `47` | `760` → `761` → `766` |
| `760` | `A1=0; A2=4; A3-Tc=8` | `A123` = `48` | `760` → `761` → `766` |
| `760` | `A1=0; A2=4; A3-Tc=9` | `A123` = `49` | `760` → `761` → `766` |
| `760` | `A1=0; A2=5; A3-Tc=0` | `A123` = `50` | `760` → `761` → `767` |
| `760` | `A1=0; A2=5; A3-Tc=1` | `A123` = `51` | `760` → `761` → `767` |
| `760` | `A1=0; A2=5; A3-Tc=2` | `A123` = `52` | `760` → `761` → `767` |
| `760` | `A1=0; A2=5; A3-Tc=3` | `A123` = `53` | `760` → `761` → `767` |
| `760` | `A1=0; A2=5; A3-Tc=4` | `A123` = `54` | `760` → `761` → `767` |
| `760` | `A1=0; A2=5; A3-Tc=5` | `A123` = `55` | `760` → `761` → `767` |
| `760` | `A1=0; A2=5; A3-Tc=6` | `A123` = `56` | `760` → `761` → `767` |
| `760` | `A1=0; A2=5; A3-Tc=7` | `A123` = `57` | `760` → `761` → `767` |
| `760` | `A1=0; A2=5; A3-Tc=8` | `A123` = `58` | `760` → `761` → `767` |
| `760` | `A1=0; A2=5; A3-Tc=9` | `A123` = `59` | `760` → `761` → `767` |
| `760` | `A1=0; A2=6; A3-Tc=0` | `A123` = `60` | `760` → `761` → `768` |
| `760` | `A1=0; A2=6; A3-Tc=1` | `A123` = `61` | `760` → `761` → `768` |
| `760` | `A1=0; A2=6; A3-Tc=2` | `A123` = `62` | `760` → `761` → `768` |
| `760` | `A1=0; A2=6; A3-Tc=3` | `A123` = `63` | `760` → `761` → `768` |
| `760` | `A1=0; A2=6; A3-Tc=4` | `A123` = `64` | `760` → `761` → `768` |
| `760` | `A1=0; A2=6; A3-Tc=5` | `A123` = `65` | `760` → `761` → `768` |
| `760` | `A1=0; A2=6; A3-Tc=6` | `A123` = `66` | `760` → `761` → `768` |
| `760` | `A1=0; A2=6; A3-Tc=7` | `A123` = `67` | `760` → `761` → `768` |
| `760` | `A1=0; A2=6; A3-Tc=8` | `A123` = `68` | `760` → `761` → `768` |
| `760` | `A1=0; A2=6; A3-Tc=9` | `A123` = `69` | `760` → `761` → `768` |
| `760` | `A1=0; A2=7; A3-Tc=0` | `A123` = `70` | `760` → `761` → `769` |
| `760` | `A1=0; A2=7; A3-Tc=1` | `A123` = `71` | `760` → `761` → `769` |
| `760` | `A1=0; A2=7; A3-Tc=2` | `A123` = `72` | `760` → `761` → `769` |
| `760` | `A1=0; A2=7; A3-Tc=3` | `A123` = `73` | `760` → `761` → `769` |
| `760` | `A1=0; A2=7; A3-Tc=4` | `A123` = `74` | `760` → `761` → `769` |
| `760` | `A1=0; A2=7; A3-Tc=5` | `A123` = `75` | `760` → `761` → `769` |
| `760` | `A1=0; A2=7; A3-Tc=6` | `A123` = `76` | `760` → `761` → `769` |
| `760` | `A1=0; A2=7; A3-Tc=7` | `A123` = `77` | `760` → `761` → `769` |
| `760` | `A1=0; A2=7; A3-Tc=8` | `A123` = `78` | `760` → `761` → `769` |
| `760` | `A1=0; A2=7; A3-Tc=9` | `A123` = `79` | `760` → `761` → `769` |
| `760` | `A1=0; A2=8; A3-Tc=0` | `A123` = `80` | `760` → `761` → `770` |
| `760` | `A1=0; A2=8; A3-Tc=1` | `A123` = `81` | `760` → `761` → `770` |
| `760` | `A1=0; A2=8; A3-Tc=2` | `A123` = `82` | `760` → `761` → `770` |
| `760` | `A1=0; A2=8; A3-Tc=3` | `A123` = `83` | `760` → `761` → `770` |
| `760` | `A1=0; A2=8; A3-Tc=4` | `A123` = `84` | `760` → `761` → `770` |
| `760` | `A1=0; A2=8; A3-Tc=5` | `A123` = `85` | `760` → `761` → `770` |
| `760` | `A1=0; A2=8; A3-Tc=6` | `A123` = `86` | `760` → `761` → `770` |
| `760` | `A1=0; A2=8; A3-Tc=7` | `A123` = `87` | `760` → `761` → `770` |
| `760` | `A1=0; A2=8; A3-Tc=8` | `A123` = `88` | `760` → `761` → `770` |
| `760` | `A1=0; A2=8; A3-Tc=9` | `A123` = `89` | `760` → `761` → `770` |
| `760` | `A1=0; A2=9; A3-Tc=0` | `A123` = `90` | `760` → `761` → `771` |
| `760` | `A1=0; A2=9; A3-Tc=1` | `A123` = `91` | `760` → `761` → `771` |
| `760` | `A1=0; A2=9; A3-Tc=2` | `A123` = `92` | `760` → `761` → `771` |
| `760` | `A1=0; A2=9; A3-Tc=3` | `A123` = `93` | `760` → `761` → `771` |
| `760` | `A1=0; A2=9; A3-Tc=4` | `A123` = `94` | `760` → `761` → `771` |
| `760` | `A1=0; A2=9; A3-Tc=5` | `A123` = `95` | `760` → `761` → `771` |
| `760` | `A1=0; A2=9; A3-Tc=6` | `A123` = `96` | `760` → `761` → `771` |
| `760` | `A1=0; A2=9; A3-Tc=7` | `A123` = `97` | `760` → `761` → `771` |
| `760` | `A1=0; A2=9; A3-Tc=8` | `A123` = `98` | `760` → `761` → `771` |
| `760` | `A1=0; A2=9; A3-Tc=9` | `A123` = `99` | `760` → `761` → `771` |
| `760` | `A1=1; A2=0; A3-Tc=0` | `A123` = `100` | `760` → `772` → `773` |
| `760` | `A1=1; A2=0; A3-Tc=1` | `A123` = `101` | `760` → `772` → `773` |
| `760` | `A1=1; A2=0; A3-Tc=2` | `A123` = `102` | `760` → `772` → `773` |
| `760` | `A1=1; A2=0; A3-Tc=3` | `A123` = `103` | `760` → `772` → `773` |
| `760` | `A1=1; A2=0; A3-Tc=4` | `A123` = `104` | `760` → `772` → `773` |
| `760` | `A1=1; A2=0; A3-Tc=5` | `A123` = `105` | `760` → `772` → `773` |
| `760` | `A1=1; A2=0; A3-Tc=6` | `A123` = `106` | `760` → `772` → `773` |
| `760` | `A1=1; A2=0; A3-Tc=7` | `A123` = `107` | `760` → `772` → `773` |
| `760` | `A1=1; A2=0; A3-Tc=8` | `A123` = `108` | `760` → `772` → `773` |
| `760` | `A1=1; A2=0; A3-Tc=9` | `A123` = `109` | `760` → `772` → `773` |
| `760` | `A1=1; A2=1; A3-Tc=0` | `A123` = `110` | `760` → `772` → `774` |
| `760` | `A1=1; A2=1; A3-Tc=1` | `A123` = `111` | `760` → `772` → `774` |
| `760` | `A1=1; A2=1; A3-Tc=2` | `A123` = `112` | `760` → `772` → `774` |
| `760` | `A1=1; A2=1; A3-Tc=3` | `A123` = `113` | `760` → `772` → `774` |
| `760` | `A1=1; A2=1; A3-Tc=4` | `A123` = `114` | `760` → `772` → `774` |
| `760` | `A1=1; A2=1; A3-Tc=5` | `A123` = `115` | `760` → `772` → `774` |
| `760` | `A1=1; A2=1; A3-Tc=6` | `A123` = `116` | `760` → `772` → `774` |
| `760` | `A1=1; A2=1; A3-Tc=7` | `A123` = `117` | `760` → `772` → `774` |
| `760` | `A1=1; A2=1; A3-Tc=8` | `A123` = `118` | `760` → `772` → `774` |
| `760` | `A1=1; A2=1; A3-Tc=9` | `A123` = `119` | `760` → `772` → `774` |
| `760` | `A1=1; A2=2; A3-Tc=0` | `A123` = `120` | `760` → `772` → `775` |
| `760` | `A1=1; A2=2; A3-Tc=1` | `A123` = `121` | `760` → `772` → `775` |
| `760` | `A1=1; A2=2; A3-Tc=2` | `A123` = `122` | `760` → `772` → `775` |
| `760` | `A1=1; A2=2; A3-Tc=3` | `A123` = `123` | `760` → `772` → `775` |
| `760` | `A1=1; A2=2; A3-Tc=4` | `A123` = `124` | `760` → `772` → `775` |
| `760` | `A1=1; A2=2; A3-Tc=5` | `A123` = `125` | `760` → `772` → `775` |
| `760` | `A1=1; A2=2; A3-Tc=6` | `A123` = `126` | `760` → `772` → `775` |
| `760` | `A1=1; A2=2; A3-Tc=7` | `A123` = `127` | `760` → `772` → `775` |
| `760` | `A1=1; A2=2; A3-Tc=8` | `A123` = `128` | `760` → `772` → `775` |
| `760` | `A1=1; A2=2; A3-Tc=9` | `A123` = `129` | `760` → `772` → `775` |
| `760` | `A1=1; A2=3; A3-Tc=0` | `A123` = `130` | `760` → `772` → `776` |
| `760` | `A1=1; A2=3; A3-Tc=1` | `A123` = `131` | `760` → `772` → `776` |
| `760` | `A1=1; A2=3; A3-Tc=2` | `A123` = `132` | `760` → `772` → `776` |
| `760` | `A1=1; A2=3; A3-Tc=3` | `A123` = `133` | `760` → `772` → `776` |
| `760` | `A1=1; A2=3; A3-Tc=4` | `A123` = `134` | `760` → `772` → `776` |
| `760` | `A1=1; A2=3; A3-Tc=5` | `A123` = `135` | `760` → `772` → `776` |
| `760` | `A1=1; A2=3; A3-Tc=6` | `A123` = `136` | `760` → `772` → `776` |
| `760` | `A1=1; A2=3; A3-Tc=7` | `A123` = `137` | `760` → `772` → `776` |
| `760` | `A1=1; A2=3; A3-Tc=8` | `A123` = `138` | `760` → `772` → `776` |
| `760` | `A1=1; A2=3; A3-Tc=9` | `A123` = `139` | `760` → `772` → `776` |
| `760` | `A1=1; A2=4; A3-Tc=0` | `A123` = `140` | `760` → `772` → `777` |
| `760` | `A1=1; A2=4; A3-Tc=1` | `A123` = `141` | `760` → `772` → `777` |
| `760` | `A1=1; A2=4; A3-Tc=2` | `A123` = `142` | `760` → `772` → `777` |
| `760` | `A1=1; A2=4; A3-Tc=3` | `A123` = `143` | `760` → `772` → `777` |
| `760` | `A1=1; A2=4; A3-Tc=4` | `A123` = `144` | `760` → `772` → `777` |
| `760` | `A1=1; A2=4; A3-Tc=5` | `A123` = `145` | `760` → `772` → `777` |
| `760` | `A1=1; A2=4; A3-Tc=6` | `A123` = `146` | `760` → `772` → `777` |
| `760` | `A1=1; A2=4; A3-Tc=7` | `A123` = `147` | `760` → `772` → `777` |
| `760` | `A1=1; A2=4; A3-Tc=8` | `A123` = `148` | `760` → `772` → `777` |
| `760` | `A1=1; A2=4; A3-Tc=9` | `A123` = `149` | `760` → `772` → `777` |
| `760` | `A1=1; A2=5; A3-Tc=0` | `A123` = `150` | `760` → `772` → `778` |
| `760` | `A1=1; A2=5; A3-Tc=1` | `A123` = `151` | `760` → `772` → `778` |
| `760` | `A1=1; A2=5; A3-Tc=2` | `A123` = `152` | `760` → `772` → `778` |
| `760` | `A1=1; A2=5; A3-Tc=3` | `A123` = `153` | `760` → `772` → `778` |
| `760` | `A1=1; A2=5; A3-Tc=4` | `A123` = `154` | `760` → `772` → `778` |
| `760` | `A1=1; A2=5; A3-Tc=5` | `A123` = `155` | `760` → `772` → `778` |
| `760` | `A1=1; A2=5; A3-Tc=6` | `A123` = `156` | `760` → `772` → `778` |
| `760` | `A1=1; A2=5; A3-Tc=7` | `A123` = `157` | `760` → `772` → `778` |
| `760` | `A1=1; A2=5; A3-Tc=8` | `A123` = `158` | `760` → `772` → `778` |
| `760` | `A1=1; A2=5; A3-Tc=9` | `A123` = `159` | `760` → `772` → `778` |
| `760` | `A1=1; A2=6; A3-Tc=0` | `A123` = `160` | `760` → `772` → `779` |
| `760` | `A1=1; A2=6; A3-Tc=1` | `A123` = `161` | `760` → `772` → `779` |
| `760` | `A1=1; A2=6; A3-Tc=2` | `A123` = `162` | `760` → `772` → `779` |
| `760` | `A1=1; A2=6; A3-Tc=3` | `A123` = `163` | `760` → `772` → `779` |
| `760` | `A1=1; A2=6; A3-Tc=4` | `A123` = `164` | `760` → `772` → `779` |
| `760` | `A1=1; A2=6; A3-Tc=5` | `A123` = `165` | `760` → `772` → `779` |
| `760` | `A1=1; A2=6; A3-Tc=6` | `A123` = `166` | `760` → `772` → `779` |
| `760` | `A1=1; A2=6; A3-Tc=7` | `A123` = `167` | `760` → `772` → `779` |
| `760` | `A1=1; A2=6; A3-Tc=8` | `A123` = `168` | `760` → `772` → `779` |
| `760` | `A1=1; A2=6; A3-Tc=9` | `A123` = `169` | `760` → `772` → `779` |
| `760` | `A1=1; A2=7; A3-Tc=0` | `A123` = `170` | `760` → `772` → `780` |
| `760` | `A1=1; A2=7; A3-Tc=1` | `A123` = `171` | `760` → `772` → `780` |
| `760` | `A1=1; A2=7; A3-Tc=2` | `A123` = `172` | `760` → `772` → `780` |
| `760` | `A1=1; A2=7; A3-Tc=3` | `A123` = `173` | `760` → `772` → `780` |
| `760` | `A1=1; A2=7; A3-Tc=4` | `A123` = `174` | `760` → `772` → `780` |
| `760` | `A1=1; A2=7; A3-Tc=5` | `A123` = `175` | `760` → `772` → `780` |
| `760` | `A1=1; A2=7; A3-Tc=6` | `A123` = `176` | `760` → `772` → `780` |
| `760` | `A1=1; A2=7; A3-Tc=7` | `A123` = `177` | `760` → `772` → `780` |
| `760` | `A1=1; A2=7; A3-Tc=8` | `A123` = `178` | `760` → `772` → `780` |
| `760` | `A1=1; A2=7; A3-Tc=9` | `A123` = `179` | `760` → `772` → `780` |
| `760` | `A1=1; A2=8; A3-Tc=0` | `A123` = `180` | `760` → `772` → `781` |
| `760` | `A1=1; A2=8; A3-Tc=1` | `A123` = `181` | `760` → `772` → `781` |
| `760` | `A1=1; A2=8; A3-Tc=2` | `A123` = `182` | `760` → `772` → `781` |
| `760` | `A1=1; A2=8; A3-Tc=3` | `A123` = `183` | `760` → `772` → `781` |
| `760` | `A1=1; A2=8; A3-Tc=4` | `A123` = `184` | `760` → `772` → `781` |
| `760` | `A1=1; A2=8; A3-Tc=5` | `A123` = `185` | `760` → `772` → `781` |
| `760` | `A1=1; A2=8; A3-Tc=6` | `A123` = `186` | `760` → `772` → `781` |
| `760` | `A1=1; A2=8; A3-Tc=7` | `A123` = `187` | `760` → `772` → `781` |
| `760` | `A1=1; A2=8; A3-Tc=8` | `A123` = `188` | `760` → `772` → `781` |
| `760` | `A1=1; A2=8; A3-Tc=9` | `A123` = `189` | `760` → `772` → `781` |
| `760` | `A1=1; A2=9; A3-Tc=0` | `A123` = `190` | `760` → `772` → `782` |
| `760` | `A1=1; A2=9; A3-Tc=1` | `A123` = `191` | `760` → `772` → `782` |
| `760` | `A1=1; A2=9; A3-Tc=2` | `A123` = `192` | `760` → `772` → `782` |
| `760` | `A1=1; A2=9; A3-Tc=3` | `A123` = `193` | `760` → `772` → `782` |
| `760` | `A1=1; A2=9; A3-Tc=4` | `A123` = `194` | `760` → `772` → `782` |
| `760` | `A1=1; A2=9; A3-Tc=5` | `A123` = `195` | `760` → `772` → `782` |
| `760` | `A1=1; A2=9; A3-Tc=6` | `A123` = `196` | `760` → `772` → `782` |
| `760` | `A1=1; A2=9; A3-Tc=7` | `A123` = `197` | `760` → `772` → `782` |
| `760` | `A1=1; A2=9; A3-Tc=8` | `A123` = `198` | `760` → `772` → `782` |
| `760` | `A1=1; A2=9; A3-Tc=9` | `A123` = `199` | `760` → `772` → `782` |
| `760` | `A1=2; A2=0; A3-Tc=0` | `A123` = `200` | `760` → `783` → `784` |
| `760` | `A1=2; A2=0; A3-Tc=1` | `A123` = `201` | `760` → `783` → `784` |
| `760` | `A1=2; A2=0; A3-Tc=2` | `A123` = `202` | `760` → `783` → `784` |
| `760` | `A1=2; A2=0; A3-Tc=3` | `A123` = `203` | `760` → `783` → `784` |
| `760` | `A1=2; A2=0; A3-Tc=4` | `A123` = `204` | `760` → `783` → `784` |
| `760` | `A1=2; A2=0; A3-Tc=5` | `A123` = `205` | `760` → `783` → `784` |
| `760` | `A1=2; A2=0; A3-Tc=6` | `A123` = `206` | `760` → `783` → `784` |
| `760` | `A1=2; A2=0; A3-Tc=7` | `A123` = `207` | `760` → `783` → `784` |
| `760` | `A1=2; A2=0; A3-Tc=8` | `A123` = `208` | `760` → `783` → `784` |
| `760` | `A1=2; A2=0; A3-Tc=9` | `A123` = `209` | `760` → `783` → `784` |
| `760` | `A1=2; A2=1; A3-Tc=0` | `A123` = `210` | `760` → `783` → `785` |
| `760` | `A1=2; A2=1; A3-Tc=1` | `A123` = `211` | `760` → `783` → `785` |
| `760` | `A1=2; A2=1; A3-Tc=2` | `A123` = `212` | `760` → `783` → `785` |
| `760` | `A1=2; A2=1; A3-Tc=3` | `A123` = `213` | `760` → `783` → `785` |
| `760` | `A1=2; A2=1; A3-Tc=4` | `A123` = `214` | `760` → `783` → `785` |
| `760` | `A1=2; A2=1; A3-Tc=5` | `A123` = `215` | `760` → `783` → `785` |
| `760` | `A1=2; A2=1; A3-Tc=6` | `A123` = `216` | `760` → `783` → `785` |
| `760` | `A1=2; A2=1; A3-Tc=7` | `A123` = `217` | `760` → `783` → `785` |
| `760` | `A1=2; A2=1; A3-Tc=8` | `A123` = `218` | `760` → `783` → `785` |
| `760` | `A1=2; A2=1; A3-Tc=9` | `A123` = `219` | `760` → `783` → `785` |
| `760` | `A1=2; A2=2; A3-Tc=0` | `A123` = `220` | `760` → `783` → `786` |
| `760` | `A1=2; A2=2; A3-Tc=1` | `A123` = `221` | `760` → `783` → `786` |
| `760` | `A1=2; A2=2; A3-Tc=2` | `A123` = `222` | `760` → `783` → `786` |
| `760` | `A1=2; A2=2; A3-Tc=3` | `A123` = `223` | `760` → `783` → `786` |
| `760` | `A1=2; A2=2; A3-Tc=4` | `A123` = `224` | `760` → `783` → `786` |
| `760` | `A1=2; A2=2; A3-Tc=5` | `A123` = `225` | `760` → `783` → `786` |
| `760` | `A1=2; A2=2; A3-Tc=6` | `A123` = `226` | `760` → `783` → `786` |
| `760` | `A1=2; A2=2; A3-Tc=7` | `A123` = `227` | `760` → `783` → `786` |
| `760` | `A1=2; A2=2; A3-Tc=8` | `A123` = `228` | `760` → `783` → `786` |
| `760` | `A1=2; A2=2; A3-Tc=9` | `A123` = `229` | `760` → `783` → `786` |
| `760` | `A1=2; A2=3; A3-Tc=0` | `A123` = `230` | `760` → `783` → `787` |
| `760` | `A1=2; A2=3; A3-Tc=1` | `A123` = `231` | `760` → `783` → `787` |
| `760` | `A1=2; A2=3; A3-Tc=2` | `A123` = `232` | `760` → `783` → `787` |
| `760` | `A1=2; A2=3; A3-Tc=3` | `A123` = `233` | `760` → `783` → `787` |
| `760` | `A1=2; A2=3; A3-Tc=4` | `A123` = `234` | `760` → `783` → `787` |
| `760` | `A1=2; A2=3; A3-Tc=5` | `A123` = `235` | `760` → `783` → `787` |
| `760` | `A1=2; A2=3; A3-Tc=6` | `A123` = `236` | `760` → `783` → `787` |
| `760` | `A1=2; A2=3; A3-Tc=7` | `A123` = `237` | `760` → `783` → `787` |
| `760` | `A1=2; A2=3; A3-Tc=8` | `A123` = `238` | `760` → `783` → `787` |
| `760` | `A1=2; A2=3; A3-Tc=9` | `A123` = `239` | `760` → `783` → `787` |
| `760` | `A1=2; A2=4; A3-Tc=0` | `A123` = `240` | `760` → `783` → `788` |
| `760` | `A1=2; A2=4; A3-Tc=1` | `A123` = `241` | `760` → `783` → `788` |
| `760` | `A1=2; A2=4; A3-Tc=2` | `A123` = `242` | `760` → `783` → `788` |
| `760` | `A1=2; A2=4; A3-Tc=3` | `A123` = `243` | `760` → `783` → `788` |
| `760` | `A1=2; A2=4; A3-Tc=4` | `A123` = `244` | `760` → `783` → `788` |
| `760` | `A1=2; A2=4; A3-Tc=5` | `A123` = `245` | `760` → `783` → `788` |
| `760` | `A1=2; A2=4; A3-Tc=6` | `A123` = `246` | `760` → `783` → `788` |
| `760` | `A1=2; A2=4; A3-Tc=7` | `A123` = `247` | `760` → `783` → `788` |
| `760` | `A1=2; A2=4; A3-Tc=8` | `A123` = `248` | `760` → `783` → `788` |
| `760` | `A1=2; A2=4; A3-Tc=9` | `A123` = `249` | `760` → `783` → `788` |
| `760` | `A1=2; A2=5; A3-Tc=0` | `A123` = `250` | `760` → `783` → `789` |
| `760` | `A1=2; A2=5; A3-Tc=1` | `A123` = `251` | `760` → `783` → `789` |
| `760` | `A1=2; A2=5; A3-Tc=2` | `A123` = `252` | `760` → `783` → `789` |
| `760` | `A1=2; A2=5; A3-Tc=3` | `A123` = `253` | `760` → `783` → `789` |
| `760` | `A1=2; A2=5; A3-Tc=4` | `A123` = `254` | `760` → `783` → `789` |
| `760` | `A1=2; A2=5; A3-Tc=5` | `A123` = `255` | `760` → `783` → `789` |

No conversion reference is attached to these slot rows. Resolve the active Object and apply its firmware-specific domain restrictions separately. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `4` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `198` - Energy metering | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |


These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The three meter addresses share hundreds/tens selectors `A1/A2` and have separate units selectors `A3-Ta/Tb/Tc`. Input A cannot be physically zero; B/C may be zero when unused. Place near the supply: below `21 Vdc`, instantaneous operation continues but storage/restore on bus failure is not guaranteed. Time/date must be supplied by a system device to store history; without it only instantaneous variables continue. Direction `T=0` ignores orientation; `T=1` is directional. In consumption wiring the toroid’s printed side faces the meter; production wiring reverses toward the inverter. Hold about twenty seconds to erase cumulative data. Home+Project, physical selectors and Suite are separately documented configuration routes. Current published server support is F460, F461 and Classe 300EOS; the MHS1 upgrade path uses backup/restore.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

## Source reconciliation

The retained current sheet, multilingual instructions, publisher export and June 2025 system guide agree on the central metering/load roles. The sheet distinguishes primary-input range `110..240 Vac` from diagram markings `110..230 V`; do not broaden a diagram marking into a different load rating. The source’s software address domain `0..127` differs from physical `1..127`; the database’s reusable domains and firmware filters remain independently authoritative for catalogue validation. Physical circuit count is not an Object or Module count.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `MyHOME Technical Guide.pdf` | June 2025 shared energy guide: wiring, load control and consumption topology; no exact 3456/F450 match and no specifications transferred to those products. |
| `ST-00001810-EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `U4724E.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `F520-publisher-product-sheet.pdf` | Captured exact-variant identity and complete technical classification attributes tabulated above; document links are discovery provenance, not additional independently verified capability. |

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
