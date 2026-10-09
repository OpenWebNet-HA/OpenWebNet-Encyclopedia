# Two-output 0-10 V valve actuator

## Summary

F430V10 controls two motorised heating or cooling valves through independent 0–10 V analogue outputs. Each output has its own zone addressing and manual open/close control. It is intended for proportional valve control rather than mains-load switching.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0145` | Project identity |
| Technical description | Two-output 0-10 V valve actuator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `003518`, `F430V10` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1684` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Temperature control | Main system association |
| Item model / `modobj` | `4` | Main association; independent of project ID |
| Firmware definition | `252` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `2` | Firmware metadata |
| Categories | Actuators, Thermoregulation | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `003518` | Established catalogue identity | Manufacturer database commercial record `2111` explicitly links this SKU to item `1684` |
| BTicino | `F430V10` | Established catalogue identity | Manufacturer database commercial record `1744` explicitly links this SKU to item `1684` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F430V10` | `8005543505304` | [F430V10-publisher-product-sheet.pdf](https://archive.openwebnet-ha.org/sha256/a7/cf/a7cf84342e5bbd2ef626ddb775234289e2c2b6a579d9a204c7b1aa2ce7140524.pdf) PDF p. 1 |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `F430V10` | Actuator DIN with 2 outputs 0-10V | Canonical commercial record `1744` |
| `003518` | Actuator DIN with 2 outputs 0-10V | Canonical commercial record `2111` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MM00780-a-EN.pdf` | Technical Sheet MM00780-A-EN | `MM00780-a-EN; 30/09/2013` | PDF p. 1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/86/15/8615ca26e997c90179d1bd79e02e0e94e79b96957d3ea5954f13662928fba7e1.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MM00780-a-EN.pdf) |
| `F430V10-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 05.10.2026` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/a7/cf/a7cf84342e5bbd2ef626ddb775234289e2c2b6a579d9a204c7b1aa2ce7140524.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-F430V10&include_technical=1) |
| `MM00780_a_IT.pdf` | Legacy manufacturer technical documentation | `MM00780_a_IT; 12/09/2013` | PDF p. 1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/22/8e/228edfd3cd51122863c134dd84ba368b7ca3bd098274f31a7124dc0984e4fd6e.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/MM00780_a_IT.pdf) |
| `MM00780_a_EN.pdf` | English counterpart of manufacturer-linked document | `MM00780_a_EN; 30/09/2013` | PDF p. 1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/86/15/8615ca26e997c90179d1bd79e02e0e94e79b96957d3ea5954f13662928fba7e1.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MM00780_a_EN.pdf) |
| `ST-00002703-EN.pdf` | Technical Sheet ST-00002703-EN | `ST-00002703-EN; 16/06/2026` | PDF p. 9: exact-reference ecosystem compatibility rows and minimum production batches; other EOS functions and wiring are outside this review. | [Archived original](https://archive.openwebnet-ha.org/sha256/b2/f5/b2f5090b601e33cdef9ba666108848ff4d9800792ccd5b7c14385da300bf0ffa.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002703-EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1684`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |
| `MyHOME-Suite-thermoregulation-actuator-functions-IT.html` | Italian manufacturer Suite function help | MHS_function_0304b / IT_MHS_function_0304; page date not stated | Exact F430V10 two-output 0–10 V valve role examined; publication/installed-software applicability not established | [Archived original](https://archive.openwebnet-ha.org/sha256/bc/cc/bccc3ce223a0e3536f2e76e28ed010ec664397e14ab6fc7a14a30eb7dc7f5413.pdf) | [Publisher source](https://myhomeswupdate.bticino.com/MyHOMESuite_Docs/MHS_function_0304b/IT_MHS_function_0304/attuatori_termo.html) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS operating supply | `18..27 Vdc` | MM00780-a-EN and MM00780_a_IT PDF p. 1 |
| Standby / maximum draw | `19 mA / 25 mA` | MM00780-a-EN and MM00780_a_IT PDF p. 1 |
| Temperature | `5..40 °C` | MM00780-a-EN and MM00780_a_IT PDF p. 1 |
| Outputs | `two independent 0..10 V analogue channels; maximum 1 mA per output` | MM00780-a-EN and MM00780_a_IT PDF p. 1 |
| Mounting | `2 DIN modules, publisher classification` | F430V10-publisher-product-sheet.pdf PDF p. 2 |
| Local interface | `two manual open/close controls and associated status LEDs` | MM00780-a-EN and MM00780_a_IT PDF p. 1 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. A negative connected-object classification does not exclude remote control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system radio frequency | `No` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system LON | `No` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system Powernet | `No` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Other bus systems | `Other` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Mounting method | `DRA (DIN-rail adaptor)` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Width in number of modular spacings | `2` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Local operation/hand operation | `Yes` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| With LED indication | `Yes` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Number of digital inputs | `0` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Suitable for C-load | `No` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Max. number of switching contacts | `0.001` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Rated current | `0.001 A` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Rated operating voltage (Min- Max) | `0-10 V` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Different phases connectable | `No` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| With bus connection | `Yes` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Modular expandability | `No` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Degree of protection (IP) | `IP20` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Connected object | `No` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |
| Product use function | `Thermal comfort management` | `F430V10-publisher-product-sheet.pdf` PDF p. 2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1684` | Canonical catalogue |
| Technical item description | Actuator DIN with 2 outputs 0-10V | Canonical catalogue |
| Item family | 0; key `2` | Canonical catalogue |
| Main system | Temperature control; key `2` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `4` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Temperature control | `4` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `252` | `-1` | `-1` | `-1` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `252` | `1` | `54` Temperature control 0-10V valve actuator | Fixed/designated metadata | `874` | `535` | `551` |
| `252` | `2` | `54` Temperature control 0-10V valve actuator | Fixed/designated metadata | `875` | `535` | `551` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `252` | Physical configuration | `0` | Canonical firmware/mode association |
| `252` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `252` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `ZA1 / ZB1 / N1` | first analogue output zone / progressive number | `MM00780-a-EN` printed/PDF p. 1; `F430V10-publisher-product-sheet` PDF p. 2 |
| `ZA2 / ZB2 / N2` | second analogue output zone / progressive number | `MM00780-a-EN` printed/PDF p. 1; `F430V10-publisher-product-sheet` PDF p. 2 |
| `Virtual route` | Suite >=1.3; no physical configurators fitted | `MM00780-a-EN` printed/PDF p. 1; `F430V10-publisher-product-sheet` PDF p. 2 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `252` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `252` | `ZA1` | `0..9` | `0` | ZA1; ZA thermo zone address 1 |
| `252` | `ZB1` | `0..9`; `10` = `OFF` | `0` | ZB1; ZB1 thermo Actuator zone address |
| `252` | `N1` | `0..9` | `0` | N1; Thermoregulation zone device number N1 |
| `252` | `ZA2` | `0..9` | `0` | ZA2; ZA thermo zone address 2 |
| `252` | `ZB2` | `0..9`; `10` = `OFF` | `0` | ZB2; ZB2 thermo Actuator zone address |
| `252` | `N2` | `0..9` | `0` | N2; Thermoregulation zone device number N2 |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `54` - Temperature control 0-10V valve actuator

Catalogue Object key `535` maps to external Object `54`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `0..9` | `1` | Device number |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `252` | `1` | `54` | `4919` | `ZB1<>OFF` | `7011` |
| `252` | `1` | `54` | `4920` | `ZB1=OFF` | `7012` |
| `252` | `2` | `54` | `4921` | `ZB2<>OFF` | `7022` |
| `252` | `2` | `54` | `4922` | `ZB2=OFF` | `7023` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | Not applicable | None | Not applicable | No relation-specific filters associated | Not applicable | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `7011` | `ZA1=0; ZB1=1` | `ZAZB` = `1` | `7011` → `7012` |
| `7011` | `ZA1=0; ZB1=2` | `ZAZB` = `2` | `7011` → `7012` |
| `7011` | `ZA1=0; ZB1=3` | `ZAZB` = `3` | `7011` → `7012` |
| `7011` | `ZA1=0; ZB1=4` | `ZAZB` = `4` | `7011` → `7012` |
| `7011` | `ZA1=0; ZB1=5` | `ZAZB` = `5` | `7011` → `7012` |
| `7011` | `ZA1=0; ZB1=6` | `ZAZB` = `6` | `7011` → `7012` |
| `7011` | `ZA1=0; ZB1=7` | `ZAZB` = `7` | `7011` → `7012` |
| `7011` | `ZA1=0; ZB1=8` | `ZAZB` = `8` | `7011` → `7012` |
| `7011` | `ZA1=0; ZB1=9` | `ZAZB` = `9` | `7011` → `7012` |
| `7011` | `ZA1=0; ZB1=OFF` | `ZAZB` = `OFF` | `7011` → `7012` |
| `7011` | `ZA1=1; ZB1=0` | `ZAZB` = `10` | `7011` → `7013` |
| `7011` | `ZA1=1; ZB1=1` | `ZAZB` = `11` | `7011` → `7013` |
| `7011` | `ZA1=1; ZB1=2` | `ZAZB` = `12` | `7011` → `7013` |
| `7011` | `ZA1=1; ZB1=3` | `ZAZB` = `13` | `7011` → `7013` |
| `7011` | `ZA1=1; ZB1=4` | `ZAZB` = `14` | `7011` → `7013` |
| `7011` | `ZA1=1; ZB1=5` | `ZAZB` = `15` | `7011` → `7013` |
| `7011` | `ZA1=1; ZB1=6` | `ZAZB` = `16` | `7011` → `7013` |
| `7011` | `ZA1=1; ZB1=7` | `ZAZB` = `17` | `7011` → `7013` |
| `7011` | `ZA1=1; ZB1=8` | `ZAZB` = `18` | `7011` → `7013` |
| `7011` | `ZA1=1; ZB1=9` | `ZAZB` = `19` | `7011` → `7013` |
| `7011` | `ZA1=1; ZB1=OFF` | `ZAZB` = `OFF` | `7011` → `7013` |
| `7011` | `ZA1=2; ZB1=0` | `ZAZB` = `20` | `7011` → `7014` |
| `7011` | `ZA1=2; ZB1=1` | `ZAZB` = `21` | `7011` → `7014` |
| `7011` | `ZA1=2; ZB1=2` | `ZAZB` = `22` | `7011` → `7014` |
| `7011` | `ZA1=2; ZB1=3` | `ZAZB` = `23` | `7011` → `7014` |
| `7011` | `ZA1=2; ZB1=4` | `ZAZB` = `24` | `7011` → `7014` |
| `7011` | `ZA1=2; ZB1=5` | `ZAZB` = `25` | `7011` → `7014` |
| `7011` | `ZA1=2; ZB1=6` | `ZAZB` = `26` | `7011` → `7014` |
| `7011` | `ZA1=2; ZB1=7` | `ZAZB` = `27` | `7011` → `7014` |
| `7011` | `ZA1=2; ZB1=8` | `ZAZB` = `28` | `7011` → `7014` |
| `7011` | `ZA1=2; ZB1=9` | `ZAZB` = `29` | `7011` → `7014` |
| `7011` | `ZA1=2; ZB1=OFF` | `ZAZB` = `OFF` | `7011` → `7014` |
| `7011` | `ZA1=3; ZB1=0` | `ZAZB` = `30` | `7011` → `7015` |
| `7011` | `ZA1=3; ZB1=1` | `ZAZB` = `31` | `7011` → `7015` |
| `7011` | `ZA1=3; ZB1=2` | `ZAZB` = `32` | `7011` → `7015` |
| `7011` | `ZA1=3; ZB1=3` | `ZAZB` = `33` | `7011` → `7015` |
| `7011` | `ZA1=3; ZB1=4` | `ZAZB` = `34` | `7011` → `7015` |
| `7011` | `ZA1=3; ZB1=5` | `ZAZB` = `35` | `7011` → `7015` |
| `7011` | `ZA1=3; ZB1=6` | `ZAZB` = `36` | `7011` → `7015` |
| `7011` | `ZA1=3; ZB1=7` | `ZAZB` = `37` | `7011` → `7015` |
| `7011` | `ZA1=3; ZB1=8` | `ZAZB` = `38` | `7011` → `7015` |
| `7011` | `ZA1=3; ZB1=9` | `ZAZB` = `39` | `7011` → `7015` |
| `7011` | `ZA1=3; ZB1=OFF` | `ZAZB` = `OFF` | `7011` → `7015` |
| `7011` | `ZA1=4; ZB1=0` | `ZAZB` = `40` | `7011` → `7016` |
| `7011` | `ZA1=4; ZB1=1` | `ZAZB` = `41` | `7011` → `7016` |
| `7011` | `ZA1=4; ZB1=2` | `ZAZB` = `42` | `7011` → `7016` |
| `7011` | `ZA1=4; ZB1=3` | `ZAZB` = `43` | `7011` → `7016` |
| `7011` | `ZA1=4; ZB1=4` | `ZAZB` = `44` | `7011` → `7016` |
| `7011` | `ZA1=4; ZB1=5` | `ZAZB` = `45` | `7011` → `7016` |
| `7011` | `ZA1=4; ZB1=6` | `ZAZB` = `46` | `7011` → `7016` |
| `7011` | `ZA1=4; ZB1=7` | `ZAZB` = `47` | `7011` → `7016` |
| `7011` | `ZA1=4; ZB1=8` | `ZAZB` = `48` | `7011` → `7016` |
| `7011` | `ZA1=4; ZB1=9` | `ZAZB` = `49` | `7011` → `7016` |
| `7011` | `ZA1=4; ZB1=OFF` | `ZAZB` = `OFF` | `7011` → `7016` |
| `7011` | `ZA1=5; ZB1=0` | `ZAZB` = `50` | `7011` → `7017` |
| `7011` | `ZA1=5; ZB1=1` | `ZAZB` = `51` | `7011` → `7017` |
| `7011` | `ZA1=5; ZB1=2` | `ZAZB` = `52` | `7011` → `7017` |
| `7011` | `ZA1=5; ZB1=3` | `ZAZB` = `53` | `7011` → `7017` |
| `7011` | `ZA1=5; ZB1=4` | `ZAZB` = `54` | `7011` → `7017` |
| `7011` | `ZA1=5; ZB1=5` | `ZAZB` = `55` | `7011` → `7017` |
| `7011` | `ZA1=5; ZB1=6` | `ZAZB` = `56` | `7011` → `7017` |
| `7011` | `ZA1=5; ZB1=7` | `ZAZB` = `57` | `7011` → `7017` |
| `7011` | `ZA1=5; ZB1=8` | `ZAZB` = `58` | `7011` → `7017` |
| `7011` | `ZA1=5; ZB1=9` | `ZAZB` = `59` | `7011` → `7017` |
| `7011` | `ZA1=5; ZB1=OFF` | `ZAZB` = `OFF` | `7011` → `7017` |
| `7011` | `ZA1=6; ZB1=0` | `ZAZB` = `60` | `7011` → `7018` |
| `7011` | `ZA1=6; ZB1=1` | `ZAZB` = `61` | `7011` → `7018` |
| `7011` | `ZA1=6; ZB1=2` | `ZAZB` = `62` | `7011` → `7018` |
| `7011` | `ZA1=6; ZB1=3` | `ZAZB` = `63` | `7011` → `7018` |
| `7011` | `ZA1=6; ZB1=4` | `ZAZB` = `64` | `7011` → `7018` |
| `7011` | `ZA1=6; ZB1=5` | `ZAZB` = `65` | `7011` → `7018` |
| `7011` | `ZA1=6; ZB1=6` | `ZAZB` = `66` | `7011` → `7018` |
| `7011` | `ZA1=6; ZB1=7` | `ZAZB` = `67` | `7011` → `7018` |
| `7011` | `ZA1=6; ZB1=8` | `ZAZB` = `68` | `7011` → `7018` |
| `7011` | `ZA1=6; ZB1=9` | `ZAZB` = `69` | `7011` → `7018` |
| `7011` | `ZA1=6; ZB1=OFF` | `ZAZB` = `OFF` | `7011` → `7018` |
| `7011` | `ZA1=7; ZB1=0` | `ZAZB` = `70` | `7011` → `7019` |
| `7011` | `ZA1=7; ZB1=1` | `ZAZB` = `71` | `7011` → `7019` |
| `7011` | `ZA1=7; ZB1=2` | `ZAZB` = `72` | `7011` → `7019` |
| `7011` | `ZA1=7; ZB1=3` | `ZAZB` = `73` | `7011` → `7019` |
| `7011` | `ZA1=7; ZB1=4` | `ZAZB` = `74` | `7011` → `7019` |
| `7011` | `ZA1=7; ZB1=5` | `ZAZB` = `75` | `7011` → `7019` |
| `7011` | `ZA1=7; ZB1=6` | `ZAZB` = `76` | `7011` → `7019` |
| `7011` | `ZA1=7; ZB1=7` | `ZAZB` = `77` | `7011` → `7019` |
| `7011` | `ZA1=7; ZB1=8` | `ZAZB` = `78` | `7011` → `7019` |
| `7011` | `ZA1=7; ZB1=9` | `ZAZB` = `79` | `7011` → `7019` |
| `7011` | `ZA1=7; ZB1=OFF` | `ZAZB` = `OFF` | `7011` → `7019` |
| `7011` | `ZA1=8; ZB1=0` | `ZAZB` = `80` | `7011` → `7020` |
| `7011` | `ZA1=8; ZB1=1` | `ZAZB` = `81` | `7011` → `7020` |
| `7011` | `ZA1=8; ZB1=2` | `ZAZB` = `82` | `7011` → `7020` |
| `7011` | `ZA1=8; ZB1=3` | `ZAZB` = `83` | `7011` → `7020` |
| `7011` | `ZA1=8; ZB1=4` | `ZAZB` = `84` | `7011` → `7020` |
| `7011` | `ZA1=8; ZB1=5` | `ZAZB` = `85` | `7011` → `7020` |
| `7011` | `ZA1=8; ZB1=6` | `ZAZB` = `86` | `7011` → `7020` |
| `7011` | `ZA1=8; ZB1=7` | `ZAZB` = `87` | `7011` → `7020` |
| `7011` | `ZA1=8; ZB1=8` | `ZAZB` = `88` | `7011` → `7020` |
| `7011` | `ZA1=8; ZB1=9` | `ZAZB` = `89` | `7011` → `7020` |
| `7011` | `ZA1=8; ZB1=OFF` | `ZAZB` = `OFF` | `7011` → `7020` |
| `7011` | `ZA1=9; ZB1=0` | `ZAZB` = `90` | `7011` → `7021` |
| `7011` | `ZA1=9; ZB1=1` | `ZAZB` = `91` | `7011` → `7021` |
| `7011` | `ZA1=9; ZB1=2` | `ZAZB` = `92` | `7011` → `7021` |
| `7011` | `ZA1=9; ZB1=3` | `ZAZB` = `93` | `7011` → `7021` |
| `7011` | `ZA1=9; ZB1=4` | `ZAZB` = `94` | `7011` → `7021` |
| `7011` | `ZA1=9; ZB1=5` | `ZAZB` = `95` | `7011` → `7021` |
| `7011` | `ZA1=9; ZB1=6` | `ZAZB` = `96` | `7011` → `7021` |
| `7011` | `ZA1=9; ZB1=7` | `ZAZB` = `97` | `7011` → `7021` |
| `7011` | `ZA1=9; ZB1=8` | `ZAZB` = `98` | `7011` → `7021` |
| `7011` | `ZA1=9; ZB1=9` | `ZAZB` = `99` | `7011` → `7021` |
| `7011` | `ZA1=9; ZB1=OFF` | `ZAZB` = `OFF` | `7011` → `7021` |
| `7012` | `ZB1=1` | `ZAZB` = `1` | `7012` |
| `7012` | `ZB1=2` | `ZAZB` = `2` | `7012` |
| `7012` | `ZB1=3` | `ZAZB` = `3` | `7012` |
| `7012` | `ZB1=4` | `ZAZB` = `4` | `7012` |
| `7012` | `ZB1=5` | `ZAZB` = `5` | `7012` |
| `7012` | `ZB1=6` | `ZAZB` = `6` | `7012` |
| `7012` | `ZB1=7` | `ZAZB` = `7` | `7012` |
| `7012` | `ZB1=8` | `ZAZB` = `8` | `7012` |
| `7012` | `ZB1=9` | `ZAZB` = `9` | `7012` |
| `7012` | `ZB1=OFF` | `ZAZB` = `OFF` | `7012` |
| `7022` | `ZA2=0; ZB2=1` | `ZAZB` = `1` | `7022` → `7023` |
| `7022` | `ZA2=0; ZB2=2` | `ZAZB` = `2` | `7022` → `7023` |
| `7022` | `ZA2=0; ZB2=3` | `ZAZB` = `3` | `7022` → `7023` |
| `7022` | `ZA2=0; ZB2=4` | `ZAZB` = `4` | `7022` → `7023` |
| `7022` | `ZA2=0; ZB2=5` | `ZAZB` = `5` | `7022` → `7023` |
| `7022` | `ZA2=0; ZB2=6` | `ZAZB` = `6` | `7022` → `7023` |
| `7022` | `ZA2=0; ZB2=7` | `ZAZB` = `7` | `7022` → `7023` |
| `7022` | `ZA2=0; ZB2=8` | `ZAZB` = `8` | `7022` → `7023` |
| `7022` | `ZA2=0; ZB2=9` | `ZAZB` = `9` | `7022` → `7023` |
| `7022` | `ZA2=0; ZB2=OFF` | `ZAZB` = `OFF` | `7022` → `7023` |
| `7022` | `ZA2=1; ZB2=0` | `ZAZB` = `10` | `7022` → `7024` |
| `7022` | `ZA2=1; ZB2=1` | `ZAZB` = `11` | `7022` → `7024` |
| `7022` | `ZA2=1; ZB2=2` | `ZAZB` = `12` | `7022` → `7024` |
| `7022` | `ZA2=1; ZB2=3` | `ZAZB` = `13` | `7022` → `7024` |
| `7022` | `ZA2=1; ZB2=4` | `ZAZB` = `14` | `7022` → `7024` |
| `7022` | `ZA2=1; ZB2=5` | `ZAZB` = `15` | `7022` → `7024` |
| `7022` | `ZA2=1; ZB2=6` | `ZAZB` = `16` | `7022` → `7024` |
| `7022` | `ZA2=1; ZB2=7` | `ZAZB` = `17` | `7022` → `7024` |
| `7022` | `ZA2=1; ZB2=8` | `ZAZB` = `18` | `7022` → `7024` |
| `7022` | `ZA2=1; ZB2=9` | `ZAZB` = `19` | `7022` → `7024` |
| `7022` | `ZA2=1; ZB2=OFF` | `ZAZB` = `OFF` | `7022` → `7024` |
| `7022` | `ZA2=2; ZB2=0` | `ZAZB` = `20` | `7022` → `7025` |
| `7022` | `ZA2=2; ZB2=1` | `ZAZB` = `21` | `7022` → `7025` |
| `7022` | `ZA2=2; ZB2=2` | `ZAZB` = `22` | `7022` → `7025` |
| `7022` | `ZA2=2; ZB2=3` | `ZAZB` = `23` | `7022` → `7025` |
| `7022` | `ZA2=2; ZB2=4` | `ZAZB` = `24` | `7022` → `7025` |
| `7022` | `ZA2=2; ZB2=5` | `ZAZB` = `25` | `7022` → `7025` |
| `7022` | `ZA2=2; ZB2=6` | `ZAZB` = `26` | `7022` → `7025` |
| `7022` | `ZA2=2; ZB2=7` | `ZAZB` = `27` | `7022` → `7025` |
| `7022` | `ZA2=2; ZB2=8` | `ZAZB` = `28` | `7022` → `7025` |
| `7022` | `ZA2=2; ZB2=9` | `ZAZB` = `29` | `7022` → `7025` |
| `7022` | `ZA2=2; ZB2=OFF` | `ZAZB` = `OFF` | `7022` → `7025` |
| `7022` | `ZA2=3; ZB2=0` | `ZAZB` = `30` | `7022` → `7026` |
| `7022` | `ZA2=3; ZB2=1` | `ZAZB` = `31` | `7022` → `7026` |
| `7022` | `ZA2=3; ZB2=2` | `ZAZB` = `32` | `7022` → `7026` |
| `7022` | `ZA2=3; ZB2=3` | `ZAZB` = `33` | `7022` → `7026` |
| `7022` | `ZA2=3; ZB2=4` | `ZAZB` = `34` | `7022` → `7026` |
| `7022` | `ZA2=3; ZB2=5` | `ZAZB` = `35` | `7022` → `7026` |
| `7022` | `ZA2=3; ZB2=6` | `ZAZB` = `36` | `7022` → `7026` |
| `7022` | `ZA2=3; ZB2=7` | `ZAZB` = `37` | `7022` → `7026` |
| `7022` | `ZA2=3; ZB2=8` | `ZAZB` = `38` | `7022` → `7026` |
| `7022` | `ZA2=3; ZB2=9` | `ZAZB` = `39` | `7022` → `7026` |
| `7022` | `ZA2=3; ZB2=OFF` | `ZAZB` = `OFF` | `7022` → `7026` |
| `7022` | `ZA2=4; ZB2=0` | `ZAZB` = `40` | `7022` → `7027` |
| `7022` | `ZA2=4; ZB2=1` | `ZAZB` = `41` | `7022` → `7027` |
| `7022` | `ZA2=4; ZB2=2` | `ZAZB` = `42` | `7022` → `7027` |
| `7022` | `ZA2=4; ZB2=3` | `ZAZB` = `43` | `7022` → `7027` |
| `7022` | `ZA2=4; ZB2=4` | `ZAZB` = `44` | `7022` → `7027` |
| `7022` | `ZA2=4; ZB2=5` | `ZAZB` = `45` | `7022` → `7027` |
| `7022` | `ZA2=4; ZB2=6` | `ZAZB` = `46` | `7022` → `7027` |
| `7022` | `ZA2=4; ZB2=7` | `ZAZB` = `47` | `7022` → `7027` |
| `7022` | `ZA2=4; ZB2=8` | `ZAZB` = `48` | `7022` → `7027` |
| `7022` | `ZA2=4; ZB2=9` | `ZAZB` = `49` | `7022` → `7027` |
| `7022` | `ZA2=4; ZB2=OFF` | `ZAZB` = `OFF` | `7022` → `7027` |
| `7022` | `ZA2=5; ZB2=0` | `ZAZB` = `50` | `7022` → `7028` |
| `7022` | `ZA2=5; ZB2=1` | `ZAZB` = `51` | `7022` → `7028` |
| `7022` | `ZA2=5; ZB2=2` | `ZAZB` = `52` | `7022` → `7028` |
| `7022` | `ZA2=5; ZB2=3` | `ZAZB` = `53` | `7022` → `7028` |
| `7022` | `ZA2=5; ZB2=4` | `ZAZB` = `54` | `7022` → `7028` |
| `7022` | `ZA2=5; ZB2=5` | `ZAZB` = `55` | `7022` → `7028` |
| `7022` | `ZA2=5; ZB2=6` | `ZAZB` = `56` | `7022` → `7028` |
| `7022` | `ZA2=5; ZB2=7` | `ZAZB` = `57` | `7022` → `7028` |
| `7022` | `ZA2=5; ZB2=8` | `ZAZB` = `58` | `7022` → `7028` |
| `7022` | `ZA2=5; ZB2=9` | `ZAZB` = `59` | `7022` → `7028` |
| `7022` | `ZA2=5; ZB2=OFF` | `ZAZB` = `OFF` | `7022` → `7028` |
| `7022` | `ZA2=6; ZB2=0` | `ZAZB` = `60` | `7022` → `7029` |
| `7022` | `ZA2=6; ZB2=1` | `ZAZB` = `61` | `7022` → `7029` |
| `7022` | `ZA2=6; ZB2=2` | `ZAZB` = `62` | `7022` → `7029` |
| `7022` | `ZA2=6; ZB2=3` | `ZAZB` = `63` | `7022` → `7029` |
| `7022` | `ZA2=6; ZB2=4` | `ZAZB` = `64` | `7022` → `7029` |
| `7022` | `ZA2=6; ZB2=5` | `ZAZB` = `65` | `7022` → `7029` |
| `7022` | `ZA2=6; ZB2=6` | `ZAZB` = `66` | `7022` → `7029` |
| `7022` | `ZA2=6; ZB2=7` | `ZAZB` = `67` | `7022` → `7029` |
| `7022` | `ZA2=6; ZB2=8` | `ZAZB` = `68` | `7022` → `7029` |
| `7022` | `ZA2=6; ZB2=9` | `ZAZB` = `69` | `7022` → `7029` |
| `7022` | `ZA2=6; ZB2=OFF` | `ZAZB` = `OFF` | `7022` → `7029` |
| `7022` | `ZA2=7; ZB2=0` | `ZAZB` = `70` | `7022` → `7030` |
| `7022` | `ZA2=7; ZB2=1` | `ZAZB` = `71` | `7022` → `7030` |
| `7022` | `ZA2=7; ZB2=2` | `ZAZB` = `72` | `7022` → `7030` |
| `7022` | `ZA2=7; ZB2=3` | `ZAZB` = `73` | `7022` → `7030` |
| `7022` | `ZA2=7; ZB2=4` | `ZAZB` = `74` | `7022` → `7030` |
| `7022` | `ZA2=7; ZB2=5` | `ZAZB` = `75` | `7022` → `7030` |
| `7022` | `ZA2=7; ZB2=6` | `ZAZB` = `76` | `7022` → `7030` |
| `7022` | `ZA2=7; ZB2=7` | `ZAZB` = `77` | `7022` → `7030` |
| `7022` | `ZA2=7; ZB2=8` | `ZAZB` = `78` | `7022` → `7030` |
| `7022` | `ZA2=7; ZB2=9` | `ZAZB` = `79` | `7022` → `7030` |
| `7022` | `ZA2=7; ZB2=OFF` | `ZAZB` = `OFF` | `7022` → `7030` |
| `7022` | `ZA2=8; ZB2=0` | `ZAZB` = `80` | `7022` → `7031` |
| `7022` | `ZA2=8; ZB2=1` | `ZAZB` = `81` | `7022` → `7031` |
| `7022` | `ZA2=8; ZB2=2` | `ZAZB` = `82` | `7022` → `7031` |
| `7022` | `ZA2=8; ZB2=3` | `ZAZB` = `83` | `7022` → `7031` |
| `7022` | `ZA2=8; ZB2=4` | `ZAZB` = `84` | `7022` → `7031` |
| `7022` | `ZA2=8; ZB2=5` | `ZAZB` = `85` | `7022` → `7031` |
| `7022` | `ZA2=8; ZB2=6` | `ZAZB` = `86` | `7022` → `7031` |
| `7022` | `ZA2=8; ZB2=7` | `ZAZB` = `87` | `7022` → `7031` |
| `7022` | `ZA2=8; ZB2=8` | `ZAZB` = `88` | `7022` → `7031` |
| `7022` | `ZA2=8; ZB2=9` | `ZAZB` = `89` | `7022` → `7031` |
| `7022` | `ZA2=8; ZB2=OFF` | `ZAZB` = `OFF` | `7022` → `7031` |
| `7022` | `ZA2=9; ZB2=0` | `ZAZB` = `90` | `7022` → `7032` |
| `7022` | `ZA2=9; ZB2=1` | `ZAZB` = `91` | `7022` → `7032` |
| `7022` | `ZA2=9; ZB2=2` | `ZAZB` = `92` | `7022` → `7032` |
| `7022` | `ZA2=9; ZB2=3` | `ZAZB` = `93` | `7022` → `7032` |
| `7022` | `ZA2=9; ZB2=4` | `ZAZB` = `94` | `7022` → `7032` |
| `7022` | `ZA2=9; ZB2=5` | `ZAZB` = `95` | `7022` → `7032` |
| `7022` | `ZA2=9; ZB2=6` | `ZAZB` = `96` | `7022` → `7032` |
| `7022` | `ZA2=9; ZB2=7` | `ZAZB` = `97` | `7022` → `7032` |
| `7022` | `ZA2=9; ZB2=8` | `ZAZB` = `98` | `7022` → `7032` |
| `7022` | `ZA2=9; ZB2=9` | `ZAZB` = `99` | `7022` → `7032` |
| `7022` | `ZA2=9; ZB2=OFF` | `ZAZB` = `OFF` | `7022` → `7032` |
| `7023` | `ZB2=1` | `ZAZB` = `1` | `7023` |
| `7023` | `ZB2=2` | `ZAZB` = `2` | `7023` |
| `7023` | `ZB2=3` | `ZAZB` = `3` | `7023` |
| `7023` | `ZB2=4` | `ZAZB` = `4` | `7023` |
| `7023` | `ZB2=5` | `ZAZB` = `5` | `7023` |
| `7023` | `ZB2=6` | `ZAZB` = `6` | `7023` |
| `7023` | `ZB2=7` | `ZAZB` = `7` | `7023` |
| `7023` | `ZB2=8` | `ZAZB` = `8` | `7023` |
| `7023` | `ZB2=9` | `ZAZB` = `9` | `7023` |
| `7023` | `ZB2=OFF` | `ZAZB` = `OFF` | `7023` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

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
| `54` - Temperature control 0-10V valve actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system/model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Set ZA1/ZB1/N1 for the first output and ZA2/ZB2/N2 for the second: each has its own two-digit zone and progressive number. A probe and its actuator must refer to the same zone. MyHOME_Suite 1.3 or later permits virtual configuration only when no physical configurators are fitted. The outputs supply a control signal; size and power the external valve separately. The current EOS compatibility list includes F430V10 and 003518 but requires software configuration for that ecosystem. Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement.

Apply the exact firmware restrictions above. The generic session/validation method remains in [Programming](../../programming/).

## Source reconciliation

The one-page technical sheet and export agree on two analogue channels and 1 mA output capacity. The export’s rated-current value 0.001 A concerns the analogue output, not the 25 mA maximum SCS draw. Two independent valve channels are represented by firmware-specific placements of temperature-control Object `54`, independently of their physical control buttons. The database brand label Legrand BTicino groups both commercial records. Human-facing identities use the manufacturer’s separately established BTicino and Legrand reference families; the raw grouping is preserved here as catalogue terminology.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `MM00780-a-EN.pdf` | PDF p. 1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `F430V10-publisher-product-sheet.pdf` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `MM00780_a_IT.pdf` | PDF p. 1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `MM00780_a_EN.pdf` | PDF p. 1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `ST-00002703-EN.pdf` | PDF p. 9: exact-reference ecosystem compatibility rows and minimum production batches; other EOS functions and wiring are outside this review. Source conflicts and limits are reconciled above. |

### Semantic review findings

Two fixed Object `54` placements (catalogue key 535) expose two analogue channels. Conditions 4919/4920 and 4921/4922 select normal versus OFF paths from ZB1/ZB2, with conversion roots 7011/7012/7022/7023. Decimal zone leaves preserve `01..99`, exclude 00, and retain explicit OFF assignments outside the reusable active-zone domain; OFF disables an output rather than proving a legal active zone. No filters, Virgin or parameter/package associations are stored. Firmware N defaults 0 differ from reusable `N=1`, and no replacement is inferred. EN and IT a sheets have different printed September 2013 dates but agree on 19/25 mA, two 1 mA outputs and software-only-when-not-physically-configured. Publisher switching-contact count 0.001 is a classification defect matching a current magnitude, not a fractional relay or a digital input. Two-DIN width is supported by the exact export, not an absent dimensions table in the technical sheet. The archived Suite help independently lists the exact 0-10 V valve role. EOS compatibility is a separate ecosystem scope.

## Evidence limits and open work

External valve input compatibility, analogue transfer function, actual firmware and diagnostic responses remain unmeasured.

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

Known earlier EOS system editions RA00215AC_I_EN.pdf and ST-00001816-EN.pdf were discovered but not examined in this batch; no earlier-edition capability is transferred. The reviewed EOS compatibility evidence is the 16/06/2026 edition only.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0141-0150-2026-10-06.md#own-dev-0145)
