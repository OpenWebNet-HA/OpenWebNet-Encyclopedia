# Pulse counter interface

## Summary

3522N converts pulses from a water, gas or similar consumption meter into data available on the SCS system. It calculates instantaneous flow and retains historical totals, and provides an optically isolated repeat output. The meter’s pulse scale is set using multiplication and division factors.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0150` | Project identity |
| Technical description | Pulse counter interface | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `003576`, `3522N` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1885` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | New energy saving and load control | Main system association |
| Item model / `modobj` | `12` | Main association; independent of project ID |
| Firmware definition | `406` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Energy management, Sensors, Gateways and interfaces | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `003576` | Established catalogue identity | Manufacturer database commercial record `2194` explicitly links this SKU to item `1885` |
| BTicino | `3522N` | Established catalogue identity | Manufacturer database commercial record `2192` explicitly links this SKU to item `1885` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `3522N` | `8005543520710` | [3522N-publisher-product-sheet.pdf](https://archive.openwebnet-ha.org/sha256/ae/d7/aed7724590d5350341659244b2dbe65bb5e3b63139a4c01d7e3aa3b6d3bf4934.pdf) PDF p. 1 |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `3522N` | Pulses counter interface | Canonical commercial record `2192` |
| `003576` | Pulses counter interface | Canonical commercial record `2194` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `LE06852AC.pdf` | Legacy manufacturer technical documentation | `LE06852AC-01PC-17W17; printed revision label` | PDF pp. 1-2: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/a4/f9/a4f98c1c31410329270efb139d07063673e7106c5dbbd918965bbacf7c758234.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/LE06852AC.pdf) |
| `MQ01007-a-EN.pdf` | Technical Sheet MQ01007-A-EN | `MQ01007-a-EN; 07/06/2014` | PDF pp. 1-2: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/1e/c0/1ec0e48a1512f3ec6b490ebca95979d1c2b62ad50351136217eaf8a0b283a3d3.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MQ01007-a-EN.pdf) |
| `3522N-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 05.10.2026` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/ae/d7/aed7724590d5350341659244b2dbe65bb5e3b63139a4c01d7e3aa3b6d3bf4934.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-3522N&include_technical=1) |
| `MQ01007_a_IT.pdf` | Legacy manufacturer technical documentation | `MQ01007_a_IT; 17/04/2014` | PDF pp. 1-2: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/f7/ab/f7ab14f8563f3d9248aede0907266f9b674f3ae38e27e77a7c66bca1095de084.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/MQ01007_a_IT.pdf) |
| `MQ01007_a_EN.pdf` | English counterpart of manufacturer-linked document | `MQ01007_a_EN; 07/06/2014` | PDF pp. 1-2: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/1e/c0/1ec0e48a1512f3ec6b490ebca95979d1c2b62ad50351136217eaf8a0b283a3d3.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MQ01007_a_EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1885`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply / maximum draw | `21..27 Vdc / 17 mA` | `MQ01007-a-EN` printed/PDF pp. 1-2; `LE06852 AC` PDF pp. 1-2 |
| Temperature / enclosure | `0..40 °C; basic module 40 x 40 x 23 mm` | `MQ01007-a-EN` printed/PDF pp. 1-2 |
| Input | `pulse contact or galvanically isolated output; observe open-collector/open-drain polarity` | `MQ01007-a-EN` printed/PDF pp. 1-2; `LE06852 AC` PDF pp. 1-2 |
| Repeat output | `opto-isolated input-pulse repetition` | `MQ01007-a-EN` printed/PDF pp. 1-2; `LE06852 AC` PDF pp. 1-2 |
| Minimum pulse interval | `60 ms: 30 ms signal plus 30 ms pause as specified` | `MQ01007-a-EN` printed/PDF pp. 1-2 |
| Instantaneous flow | `(3600 / interval in seconds) x (MUL / DIV); zero when interval exceeds 30 s` | `MQ01007-a-EN` printed/PDF pp. 1-2 |
| History retention | `hourly 12 months; daily 2 years; monthly 12 years` | `MQ01007-a-EN` printed/PDF pp. 1-2 |
| Hourly capacity | `65536 x (DIV / MUL) meter pulses; source example MUL=100,DIV=1 caps at 655 pulses/h` | `MQ01007-a-EN` printed/PDF pp. 1-2 |
| Time/date | `external system time/date required for historical storage` | `MQ01007-a-EN` printed/PDF pp. 1-2 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. A negative connected-object classification does not exclude remote control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `3522N-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `3522N-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system radio frequency | `No` | `3522N-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system LON | `No` | `3522N-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system Powernet | `No` | `3522N-publisher-product-sheet.pdf` PDF p. 2 |
| Other bus systems | `Other` | `3522N-publisher-product-sheet.pdf` PDF p. 2 |
| Radio frequency bidirectional | `No` | `3522N-publisher-product-sheet.pdf` PDF p. 2 |
| Model | `Energy meter` | `3522N-publisher-product-sheet.pdf` PDF p. 2 |
| Connection type | `Direct` | `3522N-publisher-product-sheet.pdf` PDF p. 2 |
| Reactive power | `No` | `3522N-publisher-product-sheet.pdf` PDF p. 2 |
| Approved according to PTB | `No` | `3522N-publisher-product-sheet.pdf` PDF p. 2 |
| S0 impulse interface | `None` | `3522N-publisher-product-sheet.pdf` PDF p. 2 |
| Tariff switch | `No` | `3522N-publisher-product-sheet.pdf` PDF p. 2 |
| Connected object | `No` | `3522N-publisher-product-sheet.pdf` PDF p. 2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1885` | Canonical catalogue |
| Technical item description | Pulses counter interface | Canonical catalogue |
| Item family | 0; key `100` | Canonical catalogue |
| Main system | New energy saving and load control; key `20` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `12` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| New energy saving and load control | `12` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `406` | `1` | `0` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `406` | `1` | `105` Pulse counter | Fixed/designated metadata | `2334` | `607` | `989` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `406` | Physical configuration | `0` | Canonical firmware/mode association |
| `406` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `406` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `A1 / A2 / A3` | hundreds / tens / units; address up to 127 | `MQ01007-a-EN` printed/PDF pp. 1-2 |
| `MUL=0,1,2,3,4,5,6` | factors 1,2,5,10,20,50,100 | `MQ01007-a-EN` printed/PDF pp. 1-2; `LE06852AC` PDF pp. 1-2 |
| `DIV=0,1,2,3,4,5,6,7` | divisors 1,10,100,1000,2,20,200,2000 | `MQ01007-a-EN` printed/PDF pp. 1-2; `LE06852AC` PDF pp. 1-2 |
| `Data reset` | hold >=20 s; release when green/red LEDs flash | `MQ01007-a-EN` printed/PDF pp. 1-2 |
| `Green steady / red toggle` | powered / pulse indication | `MQ01007-a-EN` printed/PDF pp. 1-2 |
| `Green 500 ms on/off` | insufficient supply; retention not guaranteed below 21 V | `MQ01007-a-EN` printed/PDF pp. 1-2 |
| `Irregular or 128 ms red/green` | configuration error / unconfigured | `MQ01007-a-EN` printed/PDF pp. 1-2 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `406` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `406` | `A1` | `0..1` | `0` | Energy pulse counter address - hundreds; address - hundreds (0-1) |
| `406` | `A2` | `0..9` | `0` | Energy pulse counter address - tens; address - tens (0-9) |
| `406` | `A3` | `0..9` | `0` | Energy pulse counter address - units; address - units (0-9) |
| `406` | `MUL` | `0..6` | `0` | Energy pulse counter multiplying coefficient; Multiplying coefficient (0-6) |
| `406` | `DIV` | `0..7` | `0` | Energy pulse counter dividing coefficient; Dividing coefficient (0-7) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `105` - Pulse counter

Catalogue Object key `607` maps to external Object `105`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A123` | `0..127` | `0` | Address; Energy Management A123 Address (0-127) |
| `MULTIPLIER_L` | `0..255` | `1` | Multiplier; Multiplier (Low byte). The combination of parameters 1 and 2 defines a range from 1 (0x0001) to 1000 (0x03E8) for Multiplier: if Multiplier_H = 0 (0x00), Multiplier_L must be in the range: 1-255 (0x01-0xFF); if Multiplier_H = 3 (0x03), Multiplier_L must be in the range: 0-232 (0x00-0xE8). |
| `MULTIPLIER_H` | `0..3` | `0` | Multiplier; Multiplier (High byte). The combination of parameters 1 and 2 defines a range from 1 (0x0001) to 1000 (0x03E8) for Multiplier: if Multiplier_H = 0 (0x00), Multiplier_L must be in the range: 1-255 (0x01-0xFF); if Multiplier_H = 3 (0x03), Multiplier_L must be in the range: 0-232 (0x00-0xE8). |
| `DIVIDER_L` | `0..255` | `1` | Divider; Divider (Low byte). The combination of parameters 3 and 4 defines a range from 1 (0x0001) to 10000 (0x2710) for Divider: if Divider_H = 0 (0x00), Divider_L must be in the range: 1-255 (0x01-0xFF); if Divider_H = 39 (0x27), Divider_L must be in the range: 0-16 (0x00-0x10). |
| `DIVIDER_H` | `0..39` | `0` | Divider; Divider (High byte). The combination of parameters 3 and 4 defines a range from 1 (0x0001) to 10000 (0x2710) for Divider: if Divider_H = 0 (0x00), Divider_L must be in the range: 1-255 (0x01-0xFF); if Divider_H = 39 (0x27), Divider_L must be in the range: 0-16 (0x00-0x10). |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `406` | `1` | `105` | `4158` | No textual predicate stored | `520` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | Not applicable | None | Not applicable | No relation-specific filters associated | Not applicable | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `520` | `A1=0; A2=0; A3=0` | `A123` = `0` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=1` | `A123` = `1` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=2` | `A123` = `2` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=3` | `A123` = `3` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=4` | `A123` = `4` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=5` | `A123` = `5` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=6` | `A123` = `6` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=7` | `A123` = `7` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=8` | `A123` = `8` | `520` → `521` → `522` |
| `520` | `A1=0; A2=0; A3=9` | `A123` = `9` | `520` → `521` → `522` |
| `520` | `A1=0; A2=1; A3=0` | `A123` = `10` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=1` | `A123` = `11` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=2` | `A123` = `12` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=3` | `A123` = `13` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=4` | `A123` = `14` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=5` | `A123` = `15` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=6` | `A123` = `16` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=7` | `A123` = `17` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=8` | `A123` = `18` | `520` → `521` → `523` |
| `520` | `A1=0; A2=1; A3=9` | `A123` = `19` | `520` → `521` → `523` |
| `520` | `A1=0; A2=2; A3=0` | `A123` = `20` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=1` | `A123` = `21` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=2` | `A123` = `22` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=3` | `A123` = `23` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=4` | `A123` = `24` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=5` | `A123` = `25` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=6` | `A123` = `26` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=7` | `A123` = `27` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=8` | `A123` = `28` | `520` → `521` → `524` |
| `520` | `A1=0; A2=2; A3=9` | `A123` = `29` | `520` → `521` → `524` |
| `520` | `A1=0; A2=3; A3=0` | `A123` = `30` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=1` | `A123` = `31` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=2` | `A123` = `32` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=3` | `A123` = `33` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=4` | `A123` = `34` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=5` | `A123` = `35` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=6` | `A123` = `36` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=7` | `A123` = `37` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=8` | `A123` = `38` | `520` → `521` → `525` |
| `520` | `A1=0; A2=3; A3=9` | `A123` = `39` | `520` → `521` → `525` |
| `520` | `A1=0; A2=4; A3=0` | `A123` = `40` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=1` | `A123` = `41` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=2` | `A123` = `42` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=3` | `A123` = `43` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=4` | `A123` = `44` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=5` | `A123` = `45` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=6` | `A123` = `46` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=7` | `A123` = `47` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=8` | `A123` = `48` | `520` → `521` → `526` |
| `520` | `A1=0; A2=4; A3=9` | `A123` = `49` | `520` → `521` → `526` |
| `520` | `A1=0; A2=5; A3=0` | `A123` = `50` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=1` | `A123` = `51` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=2` | `A123` = `52` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=3` | `A123` = `53` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=4` | `A123` = `54` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=5` | `A123` = `55` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=6` | `A123` = `56` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=7` | `A123` = `57` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=8` | `A123` = `58` | `520` → `521` → `527` |
| `520` | `A1=0; A2=5; A3=9` | `A123` = `59` | `520` → `521` → `527` |
| `520` | `A1=0; A2=6; A3=0` | `A123` = `60` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=1` | `A123` = `61` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=2` | `A123` = `62` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=3` | `A123` = `63` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=4` | `A123` = `64` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=5` | `A123` = `65` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=6` | `A123` = `66` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=7` | `A123` = `67` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=8` | `A123` = `68` | `520` → `521` → `528` |
| `520` | `A1=0; A2=6; A3=9` | `A123` = `69` | `520` → `521` → `528` |
| `520` | `A1=0; A2=7; A3=0` | `A123` = `70` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=1` | `A123` = `71` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=2` | `A123` = `72` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=3` | `A123` = `73` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=4` | `A123` = `74` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=5` | `A123` = `75` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=6` | `A123` = `76` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=7` | `A123` = `77` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=8` | `A123` = `78` | `520` → `521` → `529` |
| `520` | `A1=0; A2=7; A3=9` | `A123` = `79` | `520` → `521` → `529` |
| `520` | `A1=0; A2=8; A3=0` | `A123` = `80` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=1` | `A123` = `81` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=2` | `A123` = `82` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=3` | `A123` = `83` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=4` | `A123` = `84` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=5` | `A123` = `85` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=6` | `A123` = `86` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=7` | `A123` = `87` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=8` | `A123` = `88` | `520` → `521` → `530` |
| `520` | `A1=0; A2=8; A3=9` | `A123` = `89` | `520` → `521` → `530` |
| `520` | `A1=0; A2=9; A3=0` | `A123` = `90` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=1` | `A123` = `91` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=2` | `A123` = `92` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=3` | `A123` = `93` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=4` | `A123` = `94` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=5` | `A123` = `95` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=6` | `A123` = `96` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=7` | `A123` = `97` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=8` | `A123` = `98` | `520` → `521` → `531` |
| `520` | `A1=0; A2=9; A3=9` | `A123` = `99` | `520` → `521` → `531` |
| `520` | `A1=1; A2=0; A3=0` | `A123` = `100` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=1` | `A123` = `101` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=2` | `A123` = `102` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=3` | `A123` = `103` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=4` | `A123` = `104` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=5` | `A123` = `105` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=6` | `A123` = `106` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=7` | `A123` = `107` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=8` | `A123` = `108` | `520` → `532` → `533` |
| `520` | `A1=1; A2=0; A3=9` | `A123` = `109` | `520` → `532` → `533` |
| `520` | `A1=1; A2=1; A3=0` | `A123` = `110` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=1` | `A123` = `111` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=2` | `A123` = `112` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=3` | `A123` = `113` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=4` | `A123` = `114` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=5` | `A123` = `115` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=6` | `A123` = `116` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=7` | `A123` = `117` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=8` | `A123` = `118` | `520` → `532` → `534` |
| `520` | `A1=1; A2=1; A3=9` | `A123` = `119` | `520` → `532` → `534` |
| `520` | `A1=1; A2=2; A3=0` | `A123` = `120` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=1` | `A123` = `121` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=2` | `A123` = `122` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=3` | `A123` = `123` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=4` | `A123` = `124` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=5` | `A123` = `125` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=6` | `A123` = `126` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=7` | `A123` = `127` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=8` | `A123` = `128` | `520` → `532` → `535` |
| `520` | `A1=1; A2=2; A3=9` | `A123` = `129` | `520` → `532` → `535` |
| `520` | `A1=1; A2=3; A3=0` | `A123` = `130` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=1` | `A123` = `131` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=2` | `A123` = `132` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=3` | `A123` = `133` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=4` | `A123` = `134` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=5` | `A123` = `135` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=6` | `A123` = `136` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=7` | `A123` = `137` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=8` | `A123` = `138` | `520` → `532` → `536` |
| `520` | `A1=1; A2=3; A3=9` | `A123` = `139` | `520` → `532` → `536` |
| `520` | `A1=1; A2=4; A3=0` | `A123` = `140` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=1` | `A123` = `141` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=2` | `A123` = `142` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=3` | `A123` = `143` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=4` | `A123` = `144` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=5` | `A123` = `145` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=6` | `A123` = `146` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=7` | `A123` = `147` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=8` | `A123` = `148` | `520` → `532` → `537` |
| `520` | `A1=1; A2=4; A3=9` | `A123` = `149` | `520` → `532` → `537` |
| `520` | `A1=1; A2=5; A3=0` | `A123` = `150` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=1` | `A123` = `151` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=2` | `A123` = `152` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=3` | `A123` = `153` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=4` | `A123` = `154` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=5` | `A123` = `155` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=6` | `A123` = `156` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=7` | `A123` = `157` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=8` | `A123` = `158` | `520` → `532` → `538` |
| `520` | `A1=1; A2=5; A3=9` | `A123` = `159` | `520` → `532` → `538` |
| `520` | `A1=1; A2=6; A3=0` | `A123` = `160` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=1` | `A123` = `161` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=2` | `A123` = `162` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=3` | `A123` = `163` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=4` | `A123` = `164` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=5` | `A123` = `165` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=6` | `A123` = `166` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=7` | `A123` = `167` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=8` | `A123` = `168` | `520` → `532` → `539` |
| `520` | `A1=1; A2=6; A3=9` | `A123` = `169` | `520` → `532` → `539` |
| `520` | `A1=1; A2=7; A3=0` | `A123` = `170` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=1` | `A123` = `171` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=2` | `A123` = `172` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=3` | `A123` = `173` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=4` | `A123` = `174` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=5` | `A123` = `175` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=6` | `A123` = `176` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=7` | `A123` = `177` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=8` | `A123` = `178` | `520` → `532` → `540` |
| `520` | `A1=1; A2=7; A3=9` | `A123` = `179` | `520` → `532` → `540` |
| `520` | `A1=1; A2=8; A3=0` | `A123` = `180` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=1` | `A123` = `181` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=2` | `A123` = `182` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=3` | `A123` = `183` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=4` | `A123` = `184` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=5` | `A123` = `185` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=6` | `A123` = `186` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=7` | `A123` = `187` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=8` | `A123` = `188` | `520` → `532` → `541` |
| `520` | `A1=1; A2=8; A3=9` | `A123` = `189` | `520` → `532` → `541` |
| `520` | `A1=1; A2=9; A3=0` | `A123` = `190` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=1` | `A123` = `191` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=2` | `A123` = `192` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=3` | `A123` = `193` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=4` | `A123` = `194` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=5` | `A123` = `195` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=6` | `A123` = `196` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=7` | `A123` = `197` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=8` | `A123` = `198` | `520` → `532` → `542` |
| `520` | `A1=1; A2=9; A3=9` | `A123` = `199` | `520` → `532` → `542` |
| `520` | `A1=2; A2=0; A3=0` | `A123` = `200` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=1` | `A123` = `201` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=2` | `A123` = `202` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=3` | `A123` = `203` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=4` | `A123` = `204` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=5` | `A123` = `205` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=6` | `A123` = `206` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=7` | `A123` = `207` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=8` | `A123` = `208` | `520` → `543` → `544` |
| `520` | `A1=2; A2=0; A3=9` | `A123` = `209` | `520` → `543` → `544` |
| `520` | `A1=2; A2=1; A3=0` | `A123` = `210` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=1` | `A123` = `211` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=2` | `A123` = `212` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=3` | `A123` = `213` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=4` | `A123` = `214` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=5` | `A123` = `215` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=6` | `A123` = `216` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=7` | `A123` = `217` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=8` | `A123` = `218` | `520` → `543` → `545` |
| `520` | `A1=2; A2=1; A3=9` | `A123` = `219` | `520` → `543` → `545` |
| `520` | `A1=2; A2=2; A3=0` | `A123` = `220` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=1` | `A123` = `221` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=2` | `A123` = `222` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=3` | `A123` = `223` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=4` | `A123` = `224` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=5` | `A123` = `225` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=6` | `A123` = `226` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=7` | `A123` = `227` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=8` | `A123` = `228` | `520` → `543` → `546` |
| `520` | `A1=2; A2=2; A3=9` | `A123` = `229` | `520` → `543` → `546` |
| `520` | `A1=2; A2=3; A3=0` | `A123` = `230` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=1` | `A123` = `231` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=2` | `A123` = `232` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=3` | `A123` = `233` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=4` | `A123` = `234` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=5` | `A123` = `235` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=6` | `A123` = `236` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=7` | `A123` = `237` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=8` | `A123` = `238` | `520` → `543` → `547` |
| `520` | `A1=2; A2=3; A3=9` | `A123` = `239` | `520` → `543` → `547` |
| `520` | `A1=2; A2=4; A3=0` | `A123` = `240` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=1` | `A123` = `241` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=2` | `A123` = `242` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=3` | `A123` = `243` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=4` | `A123` = `244` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=5` | `A123` = `245` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=6` | `A123` = `246` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=7` | `A123` = `247` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=8` | `A123` = `248` | `520` → `543` → `548` |
| `520` | `A1=2; A2=4; A3=9` | `A123` = `249` | `520` → `543` → `548` |
| `520` | `A1=2; A2=5; A3=0` | `A123` = `250` | `520` → `543` → `549` |
| `520` | `A1=2; A2=5; A3=1` | `A123` = `251` | `520` → `543` → `549` |
| `520` | `A1=2; A2=5; A3=2` | `A123` = `252` | `520` → `543` → `549` |
| `520` | `A1=2; A2=5; A3=3` | `A123` = `253` | `520` → `543` → `549` |
| `520` | `A1=2; A2=5; A3=4` | `A123` = `254` | `520` → `543` → `549` |
| `520` | `A1=2; A2=5; A3=5` | `A123` = `255` | `520` → `543` → `549` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `12` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `105` - Pulse counter | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system/model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Physical A1/A2/A3 forms the meter address up to 127. MUL configurators `0..6` select factors 1,2,5,10,20,50,100; DIV `0..7` selects divisors 1,10,100,1000,2,20,200,2000. They can be combined. Suite is a separately documented virtual configuration route. Hold the button for at least 20 seconds and release when both LEDs flash to erase stored readings. Install close to the bus supply: below 21 V the green LED flashes and normal operation may continue, but storage/recovery after bus loss is not guaranteed. Steady green indicates power; red toggles with pulses; green 500 ms on/off indicates insufficient supply; irregular red/green indicates configuration error and 128 ms alternating red/green indicates unconfigured state. Without date/time, instantaneous flow remains available but history is not stored.

Apply the exact firmware restrictions above. The generic session/validation method remains in [Programming](../../programming/).

## Source reconciliation

The exact sheet and instruction distinguish pulse input, isolated repeat output, flow computation and storage. The 60 ms figure is explicitly composed of 30 ms signal and 30 ms pause; it must not be confused with a required 60 ms high pulse. The source’s 65536 hourly formula and rounded 655 example are preserved, without guessing saturation/overflow encoding. The export’s 27 V product description is nominal, while the sheet defines the operating range and low-voltage storage qualification. The database Object `105` is the pulse-counter role, not evidence of a particular meter’s units or calibration. The database brand label Legrand BTicino groups both commercial records. Human-facing identities use the manufacturer’s separately established BTicino and Legrand reference families; the raw grouping is preserved here as catalogue terminology.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `LE06852AC.pdf` | PDF pp. 1-2: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `MQ01007-a-EN.pdf` | PDF pp. 1-2: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `3522N-publisher-product-sheet.pdf` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `MQ01007_a_IT.pdf` | PDF pp. 1-2: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `MQ01007_a_EN.pdf` | PDF pp. 1-2: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |

English MQ01007-a is dated 07/06/2014 and Italian a is dated 17/04/2014; they agree on flow, retention, multiplier/divisor mappings and the reset procedure. LE06852AC (17W17) corroborates supply, input isolation/polarity and physical scaling, but does not publish the flow/history/reset details. The sheet labels 17 mA as maximum standby consumption, while the instruction says maximum absorption. The catalogue stores byte-pair limits allowing software multiplier `1..1000` and divisor `1..10000`; these exceed the physical selector factors and do not prove an inspected software implementation. Root 520 also stores `A1=2` and addresses `128..255` outside the exact firmware A1 `0..1` and Object A123 `0..127` domains; those branches cannot be treated as valid addresses. No attached conversion in this extraction maps physical MUL/DIV selectors into those byte pairs.

### Semantic review findings

Firmware406 official/default1.0/wildcard build has one fixed Object105/key607, no Virgin/filter/parameter/package and three configuration modes. Full A123 and four scaling-byte domains/defaults retained. Byte combination constraints require multiplier`1..1000`/divisor`1..10000`; zero low/high invalid at zero high despite individual byte domains, and high-end low-byte caps are explicit. Empty predicate4158 references address root520 with all256decimal leaves; `A1=2` is outside firmware`0..1`, and addresses`128..255` outside reusable`0..127`, so stored conversion does not legalize them. No MUL/DIV conversion is attached; physical scaling maps and software byte fields remain independent. EN/IT a dates differ but two-page technical contents agree, including30s flow-zero threshold, 30ms high+30ms pause, hourly12month/daily2year/monthly12year retention and external date/time requirement. LE06852AC two-page17W17 instruction adds dry/isolated input requirement and mirrors physical maps, without providing history/flow/reset procedure. Removed false unretained-source row for this already archived instruction and corrected overbroad citations. 17mA standby-versusmaximum labels are source scoped. 65536formula/rounded655example retains unknown overflow encoding. Verified current-export EAN8005543520710; broad GUI/brochures remain unexamined.

## Evidence limits and open work

Meter electrical compatibility, flow/totals wire representation, exact overflow behavior, time distribution and persistence on hardware remain unmeasured.

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

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0141-0150-2026-10-06.md#own-dev-0150)
