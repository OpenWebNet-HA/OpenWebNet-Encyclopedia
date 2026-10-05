# Two-relay temperature-control actuator

## Summary

F430/2 switches two temperature-control loads, such as valves, pumps or electric radiators. The relays can operate independently or form an interlocked opening/closing pair for one valve. Unlike the four-relay model, it explicitly supports a circulation-pump role in zone 00.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0147` | Project identity |
| Technical description | Two-relay temperature-control actuator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `003579`, `F430/2` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1852` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Temperature control | Main system association |
| Item model / `modobj` | `144` | Main association; independent of project ID |
| Firmware definition | `14`, `163` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `2` | Firmware metadata |
| Categories | Actuators, Thermoregulation | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `003579` | Established catalogue identity | Manufacturer database commercial record `1696` explicitly links this SKU to item `1852` |
| BTicino | `F430/2` | Established catalogue identity | Manufacturer database commercial record `72` explicitly links this SKU to item `1852` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F430/2` | `8012199667690` | `F430-2-publisher-product-sheet.pdf` PDF p. 1 |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `F430-2-italian-product-sheet.pdf` | Exact Italian product export | `Captured 05/10/2026; compliance-template date does not establish product publication date` | PDF pp. 1-2: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/71/b6/71b603d692b340543cfe698333da152851a50ce94751116cc8fac598350d20aa.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F430_2) |
| `ST-00000902-EN.pdf` | Technical Sheet ST-00000902-EN | `ST-00000902-EN; 23/03/2021` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/8c/6d/8c6d26613e55e300cb23b3e855c5fb6e8ad26bf15e28b0416ef5d6b2caa69565.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00000902-EN.pdf) |
| `F430-2-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 05.10.2026` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/d1/20/d12084d56d0f2bef68d00c377bbb81e98fd97a58135b171d361911d52bfeaebe.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-F430/2&include_technical=1) |
| `MQ00184_c_EN.pdf` | Earlier exact-product manufacturer original | `MQ00184_c_EN; 29/04/2014` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/44/25/44258d81a15f42fc01420337d8fcd107f121fc145c802cd7d8298d3c83bb305e.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MQ00184_c_EN.pdf) |
| `ST-00002703-EN.pdf` | Technical Sheet ST-00002703-EN | `ST-00002703-EN; 16/06/2026` | Retained 19-page original; exact-product technical, configuration and operating sections reviewed where applicable. Source-specific facts and remaining limits are scoped in the dossier; this does not claim a line-by-line review of every manual page. | [Archived original](https://archive.openwebnet-ha.org/sha256/b2/f5/b2f5090b601e33cdef9ba666108848ff4d9800792ccd5b7c14385da300bf0ffa.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002703-EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1852`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS nominal / operating supply | `27 Vdc / 18..27 Vdc` | `ST-00000902-EN` printed/PDF pp. 1-4; `MQ00184_c_EN` earlier technical sheet |
| Standby draw | `9 mA` | `ST-00000902-EN` printed/PDF pp. 1-4; `MQ00184_c_EN` earlier technical sheet |
| Maximum independent / interlocked draw | `25.5 mA / 14 mA` | `ST-00000902-EN` printed/PDF pp. 1-4; `MQ00184_c_EN` earlier technical sheet |
| Relay ratings | `6 A resistive / 2 A inductive` | `ST-00000902-EN` printed/PDF pp. 1-4; `MQ00184_c_EN` earlier technical sheet |
| Temperature / size | `5..40 °C; 2 DIN modules` | `ST-00000902-EN` printed/PDF pp. 1-4; `MQ00184_c_EN` earlier technical sheet |
| Maximum dissipation | `1.7 W` | `ST-00000902-EN` printed/PDF pp. 1-4; `MQ00184_c_EN` earlier technical sheet |
| Outputs | `two independent contacts: C1 terminals 1–2; C2 terminals 3–4` | `ST-00000902-EN` printed/PDF pp. 1-4; `MQ00184_c_EN` earlier technical sheet |


### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Classification frequency values of zero are separate from explicitly documented Wi-Fi carriers; a negative connected-object classification does not exclude remote control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system radio frequency | `No` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system LON | `No` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system Powernet | `No` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Other bus systems | `Other` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Mounting method | `DRA (DIN-rail adaptor)` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Width in number of modular spacings | `2` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Local operation/hand operation | `Yes` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| With LED indication | `Yes` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Number of digital inputs | `0` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Suitable for C-load | `No` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Max. number of switching contacts | `2` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Rated current | `6 A` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Rated operating voltage (Min- Max) | `240-240 V` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Different phases connectable | `No` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| With bus connection | `Yes` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Modular expandability | `No` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Degree of protection (IP) | `IP20` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Connected object | `No` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |
| Product use function | `Thermal comfort management` | `F430-2-publisher-product-sheet.pdf` PDF p. 2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1852` | Canonical catalogue |
| Technical item description | DIN actuator | Canonical catalogue |
| Item family | 0; key `2` | Canonical catalogue |
| Main system | Temperature control; key `2` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `144` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `14` | `7` | `0` | `0` | `2` | Not catalogue default | Official |
| `163` | `6` | `0` | `0` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `14` | `1` | `169` Temperature control on/off actuator | Fixed/designated metadata | `678` | `169` | `473` |
| `14` | `1` | `170` Temperature control open/close actuator | Candidate alternative | `680` | `170` | `474` |
| `14` | `1` | `52` Temperature control pump actuator | Candidate alternative | `1209` | `533` | `650` |
| `14` | `2` | `169` Temperature control on/off actuator | Fixed/designated metadata | `679` | `169` | `473` |
| `14` | `2` | `52` Temperature control pump actuator | Candidate alternative | `1210` | `533` | `650` |
| `163` | `1` | `169` Temperature control on/off actuator | Fixed/designated metadata | `1370` | `169` | `722` |
| `163` | `1` | `170` Temperature control open/close actuator | Candidate alternative | `1372` | `170` | `723` |
| `163` | `2` | `169` Temperature control on/off actuator | Fixed/designated metadata | `1371` | `169` | `722` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `14` | `519` Thermoregulation relay virgin | `1`, `2` | `52`, `86`, `87`, `89`, `93`, `169`, `170`, `171` | `519` | `33` |
| `163` | `519` Thermoregulation relay virgin | `1`, `2` | `52`, `86`, `87`, `89`, `93`, `169`, `170`, `171` | `519` | `43` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `14` | Virtual Configuration | `1` | Association key `1` |
| `14` | Advanced Configuration | `2` | Association key `2` |
| `14` | Physical configuration | `0` | Association key `3` |
| `163` | Virtual Configuration | `1` | Association key `1` |
| `163` | Physical configuration | `0` | Association key `3` |


No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `ZA / ZB1,N1 / ZB2,N2` | shared zone tens / relay-specific units and progressive numbers | `ST-00000902-EN` printed/PDF pp. 1-4; `MQ00184_c_EN` earlier technical sheet |
| `ZA,ZB / N` | digits `0..9` / `1..9` | `ST-00000902-EN` printed/PDF pp. 1-4; `MQ00184_c_EN` earlier technical sheet |
| `ZB1=ZB2 and N1=N2` | interlock: C1 open; C2 close | `ST-00000902-EN` printed/PDF pp. 1-4; `MQ00184_c_EN` earlier technical sheet |
| `ZB1 or ZB2=OFF` | exclude corresponding relay and local forcing button | `ST-00000902-EN` printed/PDF pp. 1-4; `MQ00184_c_EN` earlier technical sheet |
| `Zone 00` | circulation pump; interlocking excluded | `ST-00000902-EN` printed/PDF pp. 1-4; `MQ00184_c_EN` earlier technical sheet |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `14` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `14` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `14` | `ZB1` | `0..9`; `10` = `OFF` | `0` | ZB1 |
| `14` | `N1` | `1..9` | `1` | N1; Thermoregulation zone device number N1 |
| `14` | `ZB2` | `0..9`; `10` = `OFF` | `0` | ZB2; ZB2 thermo Actuator zone address |
| `14` | `N2` | `0..9` | `1` | N2; Thermoregulation zone device number N2 |
| `163` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `163` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `163` | `ZB1` | `0..9`; `10` = `OFF` | `0` | ZB1 |
| `163` | `N1` | `0..9` | `1` | N1; Thermoregulation zone device number N1 The 0 value is valid only when device is virgin |
| `163` | `ZB2` | `0..9`; `10` = `OFF` | `0` | ZB2; ZB2 thermo Actuator zone address |
| `163` | `N2` | `0..9` | `1` | N2; Thermoregulation zone device number N2 The 0 value is valid only when device is virgin |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `169` - Temperature control on/off actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `1..9` | `1` | Device number |
| `SUBTYPE` | `16` = Valve on/off; `17` = Pump | `16` | Type of load |


### Object `170` - Temperature control open/close actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `1..9` | `1` | Device number |
| `SUBTYPE` | `16` = Valve on/off; `17` = Pump | `16` | Type of load |


### Object `52` - Temperature control pump actuator

Catalogue Object key `533` maps to external Object `52`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `00` | `00` | Zone |
| `N` | `1..9` | `1` | Device number |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `14` | `1` | `169` | `4164` | No textual predicate stored | `6000` |
| `14` | `1` | `169` | `4882` | `ZB1<>OFF` | `2000` |
| `14` | `1` | `169` | `4883` | `ZB1=OFF` | `2001` |
| `14` | `1` | `170` | `4885` | `ZB1=ZB2;N1=N2` | `2000` |
| `14` | `2` | `169` | `4887` | `ZB2<>OFF` | `3000` |
| `14` | `2` | `169` | `4888` | `ZB2=OFF` | `3001` |
| `163` | `1` | `169` | `4164` | No textual predicate stored | `6000` |
| `163` | `1` | `169` | `4882` | `ZB1<>OFF` | `2000` |
| `163` | `1` | `169` | `4883` | `ZB1=OFF` | `2001` |
| `163` | `1` | `170` | `4885` | `ZB1=ZB2;N1=N2` | `2000` |
| `163` | `2` | `169` | `4887` | `ZB2<>OFF` | `3000` |
| `163` | `2` | `169` | `4888` | `ZB2=OFF` | `3001` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `14` | `169` | `670` | `SUBTYPE` | `16` = Valve on/off; `17` = Pump (entire reusable range retained) | `16` | Subtype |
| `14` | `170` | `671` | `SUBTYPE` | `16` = Valve on/off; `17` = Pump (entire reusable range retained) | `16` | Subtype |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `2000` | `ZA=0; ZB1=1` | `ZAZB` = `1` | `2000` → `2001` |
| `2000` | `ZA=0; ZB1=2` | `ZAZB` = `2` | `2000` → `2001` |
| `2000` | `ZA=0; ZB1=3` | `ZAZB` = `3` | `2000` → `2001` |
| `2000` | `ZA=0; ZB1=4` | `ZAZB` = `4` | `2000` → `2001` |
| `2000` | `ZA=0; ZB1=5` | `ZAZB` = `5` | `2000` → `2001` |
| `2000` | `ZA=0; ZB1=6` | `ZAZB` = `6` | `2000` → `2001` |
| `2000` | `ZA=0; ZB1=7` | `ZAZB` = `7` | `2000` → `2001` |
| `2000` | `ZA=0; ZB1=8` | `ZAZB` = `8` | `2000` → `2001` |
| `2000` | `ZA=0; ZB1=9` | `ZAZB` = `9` | `2000` → `2001` |
| `2000` | `ZA=0; ZB1=OFF` | `ZAZB` = `OFF` | `2000` → `2001` |
| `2000` | `ZA=1; ZB1=0` | `ZAZB` = `10` | `2000` → `2002` |
| `2000` | `ZA=1; ZB1=1` | `ZAZB` = `11` | `2000` → `2002` |
| `2000` | `ZA=1; ZB1=2` | `ZAZB` = `12` | `2000` → `2002` |
| `2000` | `ZA=1; ZB1=3` | `ZAZB` = `13` | `2000` → `2002` |
| `2000` | `ZA=1; ZB1=4` | `ZAZB` = `14` | `2000` → `2002` |
| `2000` | `ZA=1; ZB1=5` | `ZAZB` = `15` | `2000` → `2002` |
| `2000` | `ZA=1; ZB1=6` | `ZAZB` = `16` | `2000` → `2002` |
| `2000` | `ZA=1; ZB1=7` | `ZAZB` = `17` | `2000` → `2002` |
| `2000` | `ZA=1; ZB1=8` | `ZAZB` = `18` | `2000` → `2002` |
| `2000` | `ZA=1; ZB1=9` | `ZAZB` = `19` | `2000` → `2002` |
| `2000` | `ZA=1; ZB1=OFF` | `ZAZB` = `OFF` | `2000` → `2002` |
| `2000` | `ZA=2; ZB1=0` | `ZAZB` = `20` | `2000` → `2003` |
| `2000` | `ZA=2; ZB1=1` | `ZAZB` = `21` | `2000` → `2003` |
| `2000` | `ZA=2; ZB1=2` | `ZAZB` = `22` | `2000` → `2003` |
| `2000` | `ZA=2; ZB1=3` | `ZAZB` = `23` | `2000` → `2003` |
| `2000` | `ZA=2; ZB1=4` | `ZAZB` = `24` | `2000` → `2003` |
| `2000` | `ZA=2; ZB1=5` | `ZAZB` = `25` | `2000` → `2003` |
| `2000` | `ZA=2; ZB1=6` | `ZAZB` = `26` | `2000` → `2003` |
| `2000` | `ZA=2; ZB1=7` | `ZAZB` = `27` | `2000` → `2003` |
| `2000` | `ZA=2; ZB1=8` | `ZAZB` = `28` | `2000` → `2003` |
| `2000` | `ZA=2; ZB1=9` | `ZAZB` = `29` | `2000` → `2003` |
| `2000` | `ZA=2; ZB1=OFF` | `ZAZB` = `OFF` | `2000` → `2003` |
| `2000` | `ZA=3; ZB1=0` | `ZAZB` = `30` | `2000` → `2004` |
| `2000` | `ZA=3; ZB1=1` | `ZAZB` = `31` | `2000` → `2004` |
| `2000` | `ZA=3; ZB1=2` | `ZAZB` = `32` | `2000` → `2004` |
| `2000` | `ZA=3; ZB1=3` | `ZAZB` = `33` | `2000` → `2004` |
| `2000` | `ZA=3; ZB1=4` | `ZAZB` = `34` | `2000` → `2004` |
| `2000` | `ZA=3; ZB1=5` | `ZAZB` = `35` | `2000` → `2004` |
| `2000` | `ZA=3; ZB1=6` | `ZAZB` = `36` | `2000` → `2004` |
| `2000` | `ZA=3; ZB1=7` | `ZAZB` = `37` | `2000` → `2004` |
| `2000` | `ZA=3; ZB1=8` | `ZAZB` = `38` | `2000` → `2004` |
| `2000` | `ZA=3; ZB1=9` | `ZAZB` = `39` | `2000` → `2004` |
| `2000` | `ZA=3; ZB1=OFF` | `ZAZB` = `OFF` | `2000` → `2004` |
| `2000` | `ZA=4; ZB1=0` | `ZAZB` = `40` | `2000` → `2005` |
| `2000` | `ZA=4; ZB1=1` | `ZAZB` = `41` | `2000` → `2005` |
| `2000` | `ZA=4; ZB1=2` | `ZAZB` = `42` | `2000` → `2005` |
| `2000` | `ZA=4; ZB1=3` | `ZAZB` = `43` | `2000` → `2005` |
| `2000` | `ZA=4; ZB1=4` | `ZAZB` = `44` | `2000` → `2005` |
| `2000` | `ZA=4; ZB1=5` | `ZAZB` = `45` | `2000` → `2005` |
| `2000` | `ZA=4; ZB1=6` | `ZAZB` = `46` | `2000` → `2005` |
| `2000` | `ZA=4; ZB1=7` | `ZAZB` = `47` | `2000` → `2005` |
| `2000` | `ZA=4; ZB1=8` | `ZAZB` = `48` | `2000` → `2005` |
| `2000` | `ZA=4; ZB1=9` | `ZAZB` = `49` | `2000` → `2005` |
| `2000` | `ZA=4; ZB1=OFF` | `ZAZB` = `OFF` | `2000` → `2005` |
| `2000` | `ZA=5; ZB1=0` | `ZAZB` = `50` | `2000` → `2006` |
| `2000` | `ZA=5; ZB1=1` | `ZAZB` = `51` | `2000` → `2006` |
| `2000` | `ZA=5; ZB1=2` | `ZAZB` = `52` | `2000` → `2006` |
| `2000` | `ZA=5; ZB1=3` | `ZAZB` = `53` | `2000` → `2006` |
| `2000` | `ZA=5; ZB1=4` | `ZAZB` = `54` | `2000` → `2006` |
| `2000` | `ZA=5; ZB1=5` | `ZAZB` = `55` | `2000` → `2006` |
| `2000` | `ZA=5; ZB1=6` | `ZAZB` = `56` | `2000` → `2006` |
| `2000` | `ZA=5; ZB1=7` | `ZAZB` = `57` | `2000` → `2006` |
| `2000` | `ZA=5; ZB1=8` | `ZAZB` = `58` | `2000` → `2006` |
| `2000` | `ZA=5; ZB1=9` | `ZAZB` = `59` | `2000` → `2006` |
| `2000` | `ZA=5; ZB1=OFF` | `ZAZB` = `OFF` | `2000` → `2006` |
| `2000` | `ZA=6; ZB1=0` | `ZAZB` = `60` | `2000` → `2007` |
| `2000` | `ZA=6; ZB1=1` | `ZAZB` = `61` | `2000` → `2007` |
| `2000` | `ZA=6; ZB1=2` | `ZAZB` = `62` | `2000` → `2007` |
| `2000` | `ZA=6; ZB1=3` | `ZAZB` = `63` | `2000` → `2007` |
| `2000` | `ZA=6; ZB1=4` | `ZAZB` = `64` | `2000` → `2007` |
| `2000` | `ZA=6; ZB1=5` | `ZAZB` = `65` | `2000` → `2007` |
| `2000` | `ZA=6; ZB1=6` | `ZAZB` = `66` | `2000` → `2007` |
| `2000` | `ZA=6; ZB1=7` | `ZAZB` = `67` | `2000` → `2007` |
| `2000` | `ZA=6; ZB1=8` | `ZAZB` = `68` | `2000` → `2007` |
| `2000` | `ZA=6; ZB1=9` | `ZAZB` = `69` | `2000` → `2007` |
| `2000` | `ZA=6; ZB1=OFF` | `ZAZB` = `OFF` | `2000` → `2007` |
| `2000` | `ZA=7; ZB1=0` | `ZAZB` = `70` | `2000` → `2008` |
| `2000` | `ZA=7; ZB1=1` | `ZAZB` = `71` | `2000` → `2008` |
| `2000` | `ZA=7; ZB1=2` | `ZAZB` = `72` | `2000` → `2008` |
| `2000` | `ZA=7; ZB1=3` | `ZAZB` = `73` | `2000` → `2008` |
| `2000` | `ZA=7; ZB1=4` | `ZAZB` = `74` | `2000` → `2008` |
| `2000` | `ZA=7; ZB1=5` | `ZAZB` = `75` | `2000` → `2008` |
| `2000` | `ZA=7; ZB1=6` | `ZAZB` = `76` | `2000` → `2008` |
| `2000` | `ZA=7; ZB1=7` | `ZAZB` = `77` | `2000` → `2008` |
| `2000` | `ZA=7; ZB1=8` | `ZAZB` = `78` | `2000` → `2008` |
| `2000` | `ZA=7; ZB1=9` | `ZAZB` = `79` | `2000` → `2008` |
| `2000` | `ZA=7; ZB1=OFF` | `ZAZB` = `OFF` | `2000` → `2008` |
| `2000` | `ZA=8; ZB1=5` | `ZAZB` = `85` | `2000` → `2009` |
| `2000` | `ZA=8; ZB1=6` | `ZAZB` = `86` | `2000` → `2009` |
| `2000` | `ZA=8; ZB1=7` | `ZAZB` = `87` | `2000` → `2009` |
| `2000` | `ZA=8; ZB1=8` | `ZAZB` = `88` | `2000` → `2009` |
| `2000` | `ZA=8; ZB1=9` | `ZAZB` = `89` | `2000` → `2009` |
| `2000` | `ZA=8; ZB1=0` | `ZAZB` = `80` | `2000` → `2009` |
| `2000` | `ZA=8; ZB1=1` | `ZAZB` = `81` | `2000` → `2009` |
| `2000` | `ZA=8; ZB1=2` | `ZAZB` = `82` | `2000` → `2009` |
| `2000` | `ZA=8; ZB1=3` | `ZAZB` = `83` | `2000` → `2009` |
| `2000` | `ZA=8; ZB1=4` | `ZAZB` = `84` | `2000` → `2009` |
| `2000` | `ZA=8; ZB1=OFF` | `ZAZB` = `OFF` | `2000` → `2009` |
| `2000` | `ZA=9; ZB1=0` | `ZAZB` = `90` | `2000` → `2010` |
| `2000` | `ZA=9; ZB1=1` | `ZAZB` = `91` | `2000` → `2010` |
| `2000` | `ZA=9; ZB1=2` | `ZAZB` = `92` | `2000` → `2010` |
| `2000` | `ZA=9; ZB1=3` | `ZAZB` = `93` | `2000` → `2010` |
| `2000` | `ZA=9; ZB1=4` | `ZAZB` = `94` | `2000` → `2010` |
| `2000` | `ZA=9; ZB1=5` | `ZAZB` = `95` | `2000` → `2010` |
| `2000` | `ZA=9; ZB1=6` | `ZAZB` = `96` | `2000` → `2010` |
| `2000` | `ZA=9; ZB1=7` | `ZAZB` = `97` | `2000` → `2010` |
| `2000` | `ZA=9; ZB1=8` | `ZAZB` = `98` | `2000` → `2010` |
| `2000` | `ZA=9; ZB1=9` | `ZAZB` = `99` | `2000` → `2010` |
| `2000` | `ZA=9; ZB1=OFF` | `ZAZB` = `OFF` | `2000` → `2010` |
| `2001` | `ZB1=1` | `ZAZB` = `1` | `2001` |
| `2001` | `ZB1=2` | `ZAZB` = `2` | `2001` |
| `2001` | `ZB1=3` | `ZAZB` = `3` | `2001` |
| `2001` | `ZB1=4` | `ZAZB` = `4` | `2001` |
| `2001` | `ZB1=5` | `ZAZB` = `5` | `2001` |
| `2001` | `ZB1=6` | `ZAZB` = `6` | `2001` |
| `2001` | `ZB1=7` | `ZAZB` = `7` | `2001` |
| `2001` | `ZB1=8` | `ZAZB` = `8` | `2001` |
| `2001` | `ZB1=9` | `ZAZB` = `9` | `2001` |
| `2001` | `ZB1=OFF` | `ZAZB` = `OFF` | `2001` |
| `3000` | `ZA=0; ZB2=1` | `ZAZB` = `1` | `3000` → `3001` |
| `3000` | `ZA=0; ZB2=2` | `ZAZB` = `2` | `3000` → `3001` |
| `3000` | `ZA=0; ZB2=3` | `ZAZB` = `3` | `3000` → `3001` |
| `3000` | `ZA=0; ZB2=4` | `ZAZB` = `4` | `3000` → `3001` |
| `3000` | `ZA=0; ZB2=5` | `ZAZB` = `5` | `3000` → `3001` |
| `3000` | `ZA=0; ZB2=6` | `ZAZB` = `6` | `3000` → `3001` |
| `3000` | `ZA=0; ZB2=7` | `ZAZB` = `7` | `3000` → `3001` |
| `3000` | `ZA=0; ZB2=8` | `ZAZB` = `8` | `3000` → `3001` |
| `3000` | `ZA=0; ZB2=9` | `ZAZB` = `9` | `3000` → `3001` |
| `3000` | `ZA=0; ZB2=OFF` | `ZAZB` = `OFF` | `3000` → `3001` |
| `3000` | `ZA=1; ZB2=0` | `ZAZB` = `10` | `3000` → `3002` |
| `3000` | `ZA=1; ZB2=1` | `ZAZB` = `11` | `3000` → `3002` |
| `3000` | `ZA=1; ZB2=2` | `ZAZB` = `12` | `3000` → `3002` |
| `3000` | `ZA=1; ZB2=3` | `ZAZB` = `13` | `3000` → `3002` |
| `3000` | `ZA=1; ZB2=4` | `ZAZB` = `14` | `3000` → `3002` |
| `3000` | `ZA=1; ZB2=5` | `ZAZB` = `15` | `3000` → `3002` |
| `3000` | `ZA=1; ZB2=6` | `ZAZB` = `16` | `3000` → `3002` |
| `3000` | `ZA=1; ZB2=7` | `ZAZB` = `17` | `3000` → `3002` |
| `3000` | `ZA=1; ZB2=8` | `ZAZB` = `18` | `3000` → `3002` |
| `3000` | `ZA=1; ZB2=9` | `ZAZB` = `19` | `3000` → `3002` |
| `3000` | `ZA=1; ZB2=OFF` | `ZAZB` = `OFF` | `3000` → `3002` |
| `3000` | `ZA=2; ZB2=0` | `ZAZB` = `20` | `3000` → `3003` |
| `3000` | `ZA=2; ZB2=1` | `ZAZB` = `21` | `3000` → `3003` |
| `3000` | `ZA=2; ZB2=2` | `ZAZB` = `22` | `3000` → `3003` |
| `3000` | `ZA=2; ZB2=3` | `ZAZB` = `23` | `3000` → `3003` |
| `3000` | `ZA=2; ZB2=4` | `ZAZB` = `24` | `3000` → `3003` |
| `3000` | `ZA=2; ZB2=5` | `ZAZB` = `25` | `3000` → `3003` |
| `3000` | `ZA=2; ZB2=6` | `ZAZB` = `26` | `3000` → `3003` |
| `3000` | `ZA=2; ZB2=7` | `ZAZB` = `27` | `3000` → `3003` |
| `3000` | `ZA=2; ZB2=8` | `ZAZB` = `28` | `3000` → `3003` |
| `3000` | `ZA=2; ZB2=9` | `ZAZB` = `29` | `3000` → `3003` |
| `3000` | `ZA=2; ZB2=OFF` | `ZAZB` = `OFF` | `3000` → `3003` |
| `3000` | `ZA=3; ZB2=0` | `ZAZB` = `30` | `3000` → `3004` |
| `3000` | `ZA=3; ZB2=1` | `ZAZB` = `31` | `3000` → `3004` |
| `3000` | `ZA=3; ZB2=2` | `ZAZB` = `32` | `3000` → `3004` |
| `3000` | `ZA=3; ZB2=3` | `ZAZB` = `33` | `3000` → `3004` |
| `3000` | `ZA=3; ZB2=4` | `ZAZB` = `34` | `3000` → `3004` |
| `3000` | `ZA=3; ZB2=5` | `ZAZB` = `35` | `3000` → `3004` |
| `3000` | `ZA=3; ZB2=6` | `ZAZB` = `36` | `3000` → `3004` |
| `3000` | `ZA=3; ZB2=7` | `ZAZB` = `37` | `3000` → `3004` |
| `3000` | `ZA=3; ZB2=8` | `ZAZB` = `38` | `3000` → `3004` |
| `3000` | `ZA=3; ZB2=9` | `ZAZB` = `39` | `3000` → `3004` |
| `3000` | `ZA=3; ZB2=OFF` | `ZAZB` = `OFF` | `3000` → `3004` |
| `3000` | `ZA=4; ZB2=0` | `ZAZB` = `40` | `3000` → `3005` |
| `3000` | `ZA=4; ZB2=1` | `ZAZB` = `41` | `3000` → `3005` |
| `3000` | `ZA=4; ZB2=2` | `ZAZB` = `42` | `3000` → `3005` |
| `3000` | `ZA=4; ZB2=3` | `ZAZB` = `43` | `3000` → `3005` |
| `3000` | `ZA=4; ZB2=4` | `ZAZB` = `44` | `3000` → `3005` |
| `3000` | `ZA=4; ZB2=5` | `ZAZB` = `45` | `3000` → `3005` |
| `3000` | `ZA=4; ZB2=6` | `ZAZB` = `46` | `3000` → `3005` |
| `3000` | `ZA=4; ZB2=7` | `ZAZB` = `47` | `3000` → `3005` |
| `3000` | `ZA=4; ZB2=8` | `ZAZB` = `48` | `3000` → `3005` |
| `3000` | `ZA=4; ZB2=9` | `ZAZB` = `49` | `3000` → `3005` |
| `3000` | `ZA=4; ZB2=OFF` | `ZAZB` = `OFF` | `3000` → `3005` |
| `3000` | `ZA=5; ZB2=0` | `ZAZB` = `50` | `3000` → `3006` |
| `3000` | `ZA=5; ZB2=1` | `ZAZB` = `51` | `3000` → `3006` |
| `3000` | `ZA=5; ZB2=2` | `ZAZB` = `52` | `3000` → `3006` |
| `3000` | `ZA=5; ZB2=3` | `ZAZB` = `53` | `3000` → `3006` |
| `3000` | `ZA=5; ZB2=4` | `ZAZB` = `54` | `3000` → `3006` |
| `3000` | `ZA=5; ZB2=5` | `ZAZB` = `55` | `3000` → `3006` |
| `3000` | `ZA=5; ZB2=6` | `ZAZB` = `56` | `3000` → `3006` |
| `3000` | `ZA=5; ZB2=7` | `ZAZB` = `57` | `3000` → `3006` |
| `3000` | `ZA=5; ZB2=8` | `ZAZB` = `58` | `3000` → `3006` |
| `3000` | `ZA=5; ZB2=9` | `ZAZB` = `59` | `3000` → `3006` |
| `3000` | `ZA=5; ZB2=OFF` | `ZAZB` = `OFF` | `3000` → `3006` |
| `3000` | `ZA=6; ZB2=0` | `ZAZB` = `60` | `3000` → `3007` |
| `3000` | `ZA=6; ZB2=1` | `ZAZB` = `61` | `3000` → `3007` |
| `3000` | `ZA=6; ZB2=2` | `ZAZB` = `62` | `3000` → `3007` |
| `3000` | `ZA=6; ZB2=3` | `ZAZB` = `63` | `3000` → `3007` |
| `3000` | `ZA=6; ZB2=4` | `ZAZB` = `64` | `3000` → `3007` |
| `3000` | `ZA=6; ZB2=5` | `ZAZB` = `65` | `3000` → `3007` |
| `3000` | `ZA=6; ZB2=6` | `ZAZB` = `66` | `3000` → `3007` |
| `3000` | `ZA=6; ZB2=7` | `ZAZB` = `67` | `3000` → `3007` |
| `3000` | `ZA=6; ZB2=8` | `ZAZB` = `68` | `3000` → `3007` |
| `3000` | `ZA=6; ZB2=9` | `ZAZB` = `69` | `3000` → `3007` |
| `3000` | `ZA=6; ZB2=OFF` | `ZAZB` = `OFF` | `3000` → `3007` |
| `3000` | `ZA=7; ZB2=0` | `ZAZB` = `70` | `3000` → `3008` |
| `3000` | `ZA=7; ZB2=1` | `ZAZB` = `71` | `3000` → `3008` |
| `3000` | `ZA=7; ZB2=2` | `ZAZB` = `72` | `3000` → `3008` |
| `3000` | `ZA=7; ZB2=3` | `ZAZB` = `73` | `3000` → `3008` |
| `3000` | `ZA=7; ZB2=4` | `ZAZB` = `74` | `3000` → `3008` |
| `3000` | `ZA=7; ZB2=5` | `ZAZB` = `75` | `3000` → `3008` |
| `3000` | `ZA=7; ZB2=6` | `ZAZB` = `76` | `3000` → `3008` |
| `3000` | `ZA=7; ZB2=7` | `ZAZB` = `77` | `3000` → `3008` |
| `3000` | `ZA=7; ZB2=8` | `ZAZB` = `78` | `3000` → `3008` |
| `3000` | `ZA=7; ZB2=9` | `ZAZB` = `79` | `3000` → `3008` |
| `3000` | `ZA=7; ZB2=OFF` | `ZAZB` = `OFF` | `3000` → `3008` |
| `3000` | `ZA=8; ZB2=5` | `ZAZB` = `85` | `3000` → `3009` |
| `3000` | `ZA=8; ZB2=6` | `ZAZB` = `86` | `3000` → `3009` |
| `3000` | `ZA=8; ZB2=7` | `ZAZB` = `87` | `3000` → `3009` |
| `3000` | `ZA=8; ZB2=8` | `ZAZB` = `88` | `3000` → `3009` |
| `3000` | `ZA=8; ZB2=9` | `ZAZB` = `89` | `3000` → `3009` |
| `3000` | `ZA=8; ZB2=0` | `ZAZB` = `80` | `3000` → `3009` |
| `3000` | `ZA=8; ZB2=1` | `ZAZB` = `81` | `3000` → `3009` |
| `3000` | `ZA=8; ZB2=2` | `ZAZB` = `82` | `3000` → `3009` |
| `3000` | `ZA=8; ZB2=3` | `ZAZB` = `83` | `3000` → `3009` |
| `3000` | `ZA=8; ZB2=4` | `ZAZB` = `84` | `3000` → `3009` |
| `3000` | `ZA=8; ZB2=OFF` | `ZAZB` = `OFF` | `3000` → `3009` |
| `3000` | `ZA=9; ZB2=0` | `ZAZB` = `90` | `3000` → `3010` |
| `3000` | `ZA=9; ZB2=1` | `ZAZB` = `91` | `3000` → `3010` |
| `3000` | `ZA=9; ZB2=2` | `ZAZB` = `92` | `3000` → `3010` |
| `3000` | `ZA=9; ZB2=3` | `ZAZB` = `93` | `3000` → `3010` |
| `3000` | `ZA=9; ZB2=4` | `ZAZB` = `94` | `3000` → `3010` |
| `3000` | `ZA=9; ZB2=5` | `ZAZB` = `95` | `3000` → `3010` |
| `3000` | `ZA=9; ZB2=6` | `ZAZB` = `96` | `3000` → `3010` |
| `3000` | `ZA=9; ZB2=7` | `ZAZB` = `97` | `3000` → `3010` |
| `3000` | `ZA=9; ZB2=8` | `ZAZB` = `98` | `3000` → `3010` |
| `3000` | `ZA=9; ZB2=9` | `ZAZB` = `99` | `3000` → `3010` |
| `3000` | `ZA=9; ZB2=OFF` | `ZAZB` = `OFF` | `3000` → `3010` |
| `3001` | `ZB2=1` | `ZAZB` = `1` | `3001` |
| `3001` | `ZB2=2` | `ZAZB` = `2` | `3001` |
| `3001` | `ZB2=3` | `ZAZB` = `3` | `3001` |
| `3001` | `ZB2=4` | `ZAZB` = `4` | `3001` |
| `3001` | `ZB2=5` | `ZAZB` = `5` | `3001` |
| `3001` | `ZB2=6` | `ZAZB` = `6` | `3001` |
| `3001` | `ZB2=7` | `ZAZB` = `7` | `3001` |
| `3001` | `ZB2=8` | `ZAZB` = `8` | `3001` |
| `3001` | `ZB2=9` | `ZAZB` = `9` | `3001` |
| `3001` | `ZB2=OFF` | `ZAZB` = `OFF` | `3001` |
| `6000` | `ZA=0; ZB1=1` | `ZAZB` = `1` | `6000` → `6001` |
| `6000` | `ZA=0; ZB1=2` | `ZAZB` = `2` | `6000` → `6001` |
| `6000` | `ZA=0; ZB1=3` | `ZAZB` = `3` | `6000` → `6001` |
| `6000` | `ZA=0; ZB1=4` | `ZAZB` = `4` | `6000` → `6001` |
| `6000` | `ZA=0; ZB1=5` | `ZAZB` = `5` | `6000` → `6001` |
| `6000` | `ZA=0; ZB1=6` | `ZAZB` = `6` | `6000` → `6001` |
| `6000` | `ZA=0; ZB1=7` | `ZAZB` = `7` | `6000` → `6001` |
| `6000` | `ZA=0; ZB1=8` | `ZAZB` = `8` | `6000` → `6001` |
| `6000` | `ZA=0; ZB1=9` | `ZAZB` = `9` | `6000` → `6001` |
| `6000` | `ZA=0; ZB1=OFF` | `ZAZB` = `OFF` | `6000` → `6001` |
| `6000` | `ZA=0; ZB2=1` | `ZAZB` = `1` | `6000` → `6001` |
| `6000` | `ZA=0; ZB2=2` | `ZAZB` = `2` | `6000` → `6001` |
| `6000` | `ZA=0; ZB2=3` | `ZAZB` = `3` | `6000` → `6001` |
| `6000` | `ZA=0; ZB2=4` | `ZAZB` = `4` | `6000` → `6001` |
| `6000` | `ZA=0; ZB2=5` | `ZAZB` = `5` | `6000` → `6001` |
| `6000` | `ZA=0; ZB2=6` | `ZAZB` = `6` | `6000` → `6001` |
| `6000` | `ZA=0; ZB2=7` | `ZAZB` = `7` | `6000` → `6001` |
| `6000` | `ZA=0; ZB2=8` | `ZAZB` = `8` | `6000` → `6001` |
| `6000` | `ZA=0; ZB2=9` | `ZAZB` = `9` | `6000` → `6001` |
| `6000` | `ZA=0; ZB2=OFF` | `ZAZB` = `OFF` | `6000` → `6001` |
| `6000` | `ZA=1; ZB1=0` | `ZAZB` = `10` | `6000` → `6002` |
| `6000` | `ZA=1; ZB1=1` | `ZAZB` = `11` | `6000` → `6002` |
| `6000` | `ZA=1; ZB1=2` | `ZAZB` = `12` | `6000` → `6002` |
| `6000` | `ZA=1; ZB1=3` | `ZAZB` = `13` | `6000` → `6002` |
| `6000` | `ZA=1; ZB1=4` | `ZAZB` = `14` | `6000` → `6002` |
| `6000` | `ZA=1; ZB1=5` | `ZAZB` = `15` | `6000` → `6002` |
| `6000` | `ZA=1; ZB1=6` | `ZAZB` = `16` | `6000` → `6002` |
| `6000` | `ZA=1; ZB1=7` | `ZAZB` = `17` | `6000` → `6002` |
| `6000` | `ZA=1; ZB1=8` | `ZAZB` = `18` | `6000` → `6002` |
| `6000` | `ZA=1; ZB1=9` | `ZAZB` = `19` | `6000` → `6002` |
| `6000` | `ZA=1; ZB2=0` | `ZAZB` = `10` | `6000` → `6002` |
| `6000` | `ZA=1; ZB2=1` | `ZAZB` = `11` | `6000` → `6002` |
| `6000` | `ZA=1; ZB2=2` | `ZAZB` = `12` | `6000` → `6002` |
| `6000` | `ZA=1; ZB2=3` | `ZAZB` = `13` | `6000` → `6002` |
| `6000` | `ZA=1; ZB2=4` | `ZAZB` = `14` | `6000` → `6002` |
| `6000` | `ZA=1; ZB2=5` | `ZAZB` = `15` | `6000` → `6002` |
| `6000` | `ZA=1; ZB2=6` | `ZAZB` = `16` | `6000` → `6002` |
| `6000` | `ZA=1; ZB2=7` | `ZAZB` = `17` | `6000` → `6002` |
| `6000` | `ZA=1; ZB2=8` | `ZAZB` = `18` | `6000` → `6002` |
| `6000` | `ZA=1; ZB2=9` | `ZAZB` = `19` | `6000` → `6002` |
| `6000` | `ZA=2; ZB1=0` | `ZAZB` = `20` | `6000` → `6003` |
| `6000` | `ZA=2; ZB1=1` | `ZAZB` = `21` | `6000` → `6003` |
| `6000` | `ZA=2; ZB1=2` | `ZAZB` = `22` | `6000` → `6003` |
| `6000` | `ZA=2; ZB1=3` | `ZAZB` = `23` | `6000` → `6003` |
| `6000` | `ZA=2; ZB1=4` | `ZAZB` = `24` | `6000` → `6003` |
| `6000` | `ZA=2; ZB1=5` | `ZAZB` = `25` | `6000` → `6003` |
| `6000` | `ZA=2; ZB1=6` | `ZAZB` = `26` | `6000` → `6003` |
| `6000` | `ZA=2; ZB1=7` | `ZAZB` = `27` | `6000` → `6003` |
| `6000` | `ZA=2; ZB1=8` | `ZAZB` = `28` | `6000` → `6003` |
| `6000` | `ZA=2; ZB1=9` | `ZAZB` = `29` | `6000` → `6003` |
| `6000` | `ZA=2; ZB2=0` | `ZAZB` = `20` | `6000` → `6003` |
| `6000` | `ZA=2; ZB2=1` | `ZAZB` = `21` | `6000` → `6003` |
| `6000` | `ZA=2; ZB2=2` | `ZAZB` = `22` | `6000` → `6003` |
| `6000` | `ZA=2; ZB2=3` | `ZAZB` = `23` | `6000` → `6003` |
| `6000` | `ZA=2; ZB2=4` | `ZAZB` = `24` | `6000` → `6003` |
| `6000` | `ZA=2; ZB2=5` | `ZAZB` = `25` | `6000` → `6003` |
| `6000` | `ZA=2; ZB2=6` | `ZAZB` = `26` | `6000` → `6003` |
| `6000` | `ZA=2; ZB2=7` | `ZAZB` = `27` | `6000` → `6003` |
| `6000` | `ZA=2; ZB2=8` | `ZAZB` = `28` | `6000` → `6003` |
| `6000` | `ZA=2; ZB2=9` | `ZAZB` = `29` | `6000` → `6003` |
| `6000` | `ZA=3; ZB1=0` | `ZAZB` = `30` | `6000` → `6004` |
| `6000` | `ZA=3; ZB1=1` | `ZAZB` = `31` | `6000` → `6004` |
| `6000` | `ZA=3; ZB1=2` | `ZAZB` = `32` | `6000` → `6004` |
| `6000` | `ZA=3; ZB1=3` | `ZAZB` = `33` | `6000` → `6004` |
| `6000` | `ZA=3; ZB1=4` | `ZAZB` = `34` | `6000` → `6004` |
| `6000` | `ZA=3; ZB1=5` | `ZAZB` = `35` | `6000` → `6004` |
| `6000` | `ZA=3; ZB1=6` | `ZAZB` = `36` | `6000` → `6004` |
| `6000` | `ZA=3; ZB1=7` | `ZAZB` = `37` | `6000` → `6004` |
| `6000` | `ZA=3; ZB1=8` | `ZAZB` = `38` | `6000` → `6004` |
| `6000` | `ZA=3; ZB1=9` | `ZAZB` = `39` | `6000` → `6004` |
| `6000` | `ZA=3; ZB2=0` | `ZAZB` = `30` | `6000` → `6004` |
| `6000` | `ZA=3; ZB2=1` | `ZAZB` = `31` | `6000` → `6004` |
| `6000` | `ZA=3; ZB2=2` | `ZAZB` = `32` | `6000` → `6004` |
| `6000` | `ZA=3; ZB2=3` | `ZAZB` = `33` | `6000` → `6004` |
| `6000` | `ZA=3; ZB2=4` | `ZAZB` = `34` | `6000` → `6004` |
| `6000` | `ZA=3; ZB2=5` | `ZAZB` = `35` | `6000` → `6004` |
| `6000` | `ZA=3; ZB2=6` | `ZAZB` = `36` | `6000` → `6004` |
| `6000` | `ZA=3; ZB2=7` | `ZAZB` = `37` | `6000` → `6004` |
| `6000` | `ZA=3; ZB2=8` | `ZAZB` = `38` | `6000` → `6004` |
| `6000` | `ZA=3; ZB2=9` | `ZAZB` = `39` | `6000` → `6004` |
| `6000` | `ZA=4; ZB1=0` | `ZAZB` = `40` | `6000` → `6005` |
| `6000` | `ZA=4; ZB1=1` | `ZAZB` = `41` | `6000` → `6005` |
| `6000` | `ZA=4; ZB1=2` | `ZAZB` = `42` | `6000` → `6005` |
| `6000` | `ZA=4; ZB1=3` | `ZAZB` = `43` | `6000` → `6005` |
| `6000` | `ZA=4; ZB1=4` | `ZAZB` = `44` | `6000` → `6005` |
| `6000` | `ZA=4; ZB1=5` | `ZAZB` = `45` | `6000` → `6005` |
| `6000` | `ZA=4; ZB1=6` | `ZAZB` = `46` | `6000` → `6005` |
| `6000` | `ZA=4; ZB1=7` | `ZAZB` = `47` | `6000` → `6005` |
| `6000` | `ZA=4; ZB1=8` | `ZAZB` = `48` | `6000` → `6005` |
| `6000` | `ZA=4; ZB1=9` | `ZAZB` = `49` | `6000` → `6005` |
| `6000` | `ZA=4; ZB2=0` | `ZAZB` = `40` | `6000` → `6005` |
| `6000` | `ZA=4; ZB2=1` | `ZAZB` = `41` | `6000` → `6005` |
| `6000` | `ZA=4; ZB2=2` | `ZAZB` = `42` | `6000` → `6005` |
| `6000` | `ZA=4; ZB2=3` | `ZAZB` = `43` | `6000` → `6005` |
| `6000` | `ZA=4; ZB2=4` | `ZAZB` = `44` | `6000` → `6005` |
| `6000` | `ZA=4; ZB2=5` | `ZAZB` = `45` | `6000` → `6005` |
| `6000` | `ZA=4; ZB2=6` | `ZAZB` = `46` | `6000` → `6005` |
| `6000` | `ZA=4; ZB2=7` | `ZAZB` = `47` | `6000` → `6005` |
| `6000` | `ZA=4; ZB2=8` | `ZAZB` = `48` | `6000` → `6005` |
| `6000` | `ZA=4; ZB2=9` | `ZAZB` = `49` | `6000` → `6005` |
| `6000` | `ZA=5; ZB1=0` | `ZAZB` = `50` | `6000` → `6006` |
| `6000` | `ZA=5; ZB1=1` | `ZAZB` = `51` | `6000` → `6006` |
| `6000` | `ZA=5; ZB1=2` | `ZAZB` = `52` | `6000` → `6006` |
| `6000` | `ZA=5; ZB1=3` | `ZAZB` = `53` | `6000` → `6006` |
| `6000` | `ZA=5; ZB1=4` | `ZAZB` = `54` | `6000` → `6006` |
| `6000` | `ZA=5; ZB1=5` | `ZAZB` = `55` | `6000` → `6006` |
| `6000` | `ZA=5; ZB1=6` | `ZAZB` = `56` | `6000` → `6006` |
| `6000` | `ZA=5; ZB1=7` | `ZAZB` = `57` | `6000` → `6006` |
| `6000` | `ZA=5; ZB1=8` | `ZAZB` = `58` | `6000` → `6006` |
| `6000` | `ZA=5; ZB1=9` | `ZAZB` = `59` | `6000` → `6006` |
| `6000` | `ZA=5; ZB2=0` | `ZAZB` = `50` | `6000` → `6006` |
| `6000` | `ZA=5; ZB2=1` | `ZAZB` = `51` | `6000` → `6006` |
| `6000` | `ZA=5; ZB2=2` | `ZAZB` = `52` | `6000` → `6006` |
| `6000` | `ZA=5; ZB2=3` | `ZAZB` = `53` | `6000` → `6006` |
| `6000` | `ZA=5; ZB2=4` | `ZAZB` = `54` | `6000` → `6006` |
| `6000` | `ZA=5; ZB2=5` | `ZAZB` = `55` | `6000` → `6006` |
| `6000` | `ZA=5; ZB2=6` | `ZAZB` = `56` | `6000` → `6006` |
| `6000` | `ZA=5; ZB2=7` | `ZAZB` = `57` | `6000` → `6006` |
| `6000` | `ZA=5; ZB2=8` | `ZAZB` = `58` | `6000` → `6006` |
| `6000` | `ZA=5; ZB2=9` | `ZAZB` = `59` | `6000` → `6006` |
| `6000` | `ZA=6; ZB1=0` | `ZAZB` = `60` | `6000` → `6007` |
| `6000` | `ZA=6; ZB1=1` | `ZAZB` = `61` | `6000` → `6007` |
| `6000` | `ZA=6; ZB1=2` | `ZAZB` = `62` | `6000` → `6007` |
| `6000` | `ZA=6; ZB1=3` | `ZAZB` = `63` | `6000` → `6007` |
| `6000` | `ZA=6; ZB1=4` | `ZAZB` = `64` | `6000` → `6007` |
| `6000` | `ZA=6; ZB1=5` | `ZAZB` = `65` | `6000` → `6007` |
| `6000` | `ZA=6; ZB1=6` | `ZAZB` = `66` | `6000` → `6007` |
| `6000` | `ZA=6; ZB1=7` | `ZAZB` = `67` | `6000` → `6007` |
| `6000` | `ZA=6; ZB1=8` | `ZAZB` = `68` | `6000` → `6007` |
| `6000` | `ZA=6; ZB1=9` | `ZAZB` = `69` | `6000` → `6007` |
| `6000` | `ZA=6; ZB2=0` | `ZAZB` = `60` | `6000` → `6007` |
| `6000` | `ZA=6; ZB2=1` | `ZAZB` = `61` | `6000` → `6007` |
| `6000` | `ZA=6; ZB2=2` | `ZAZB` = `62` | `6000` → `6007` |
| `6000` | `ZA=6; ZB2=3` | `ZAZB` = `63` | `6000` → `6007` |
| `6000` | `ZA=6; ZB2=4` | `ZAZB` = `64` | `6000` → `6007` |
| `6000` | `ZA=6; ZB2=5` | `ZAZB` = `65` | `6000` → `6007` |
| `6000` | `ZA=6; ZB2=6` | `ZAZB` = `66` | `6000` → `6007` |
| `6000` | `ZA=6; ZB2=7` | `ZAZB` = `67` | `6000` → `6007` |
| `6000` | `ZA=6; ZB2=8` | `ZAZB` = `68` | `6000` → `6007` |
| `6000` | `ZA=6; ZB2=9` | `ZAZB` = `69` | `6000` → `6007` |
| `6000` | `ZA=7; ZB1=0` | `ZAZB` = `70` | `6000` → `6008` |
| `6000` | `ZA=7; ZB1=1` | `ZAZB` = `71` | `6000` → `6008` |
| `6000` | `ZA=7; ZB1=2` | `ZAZB` = `72` | `6000` → `6008` |
| `6000` | `ZA=7; ZB1=3` | `ZAZB` = `73` | `6000` → `6008` |
| `6000` | `ZA=7; ZB1=4` | `ZAZB` = `74` | `6000` → `6008` |
| `6000` | `ZA=7; ZB1=5` | `ZAZB` = `75` | `6000` → `6008` |
| `6000` | `ZA=7; ZB1=6` | `ZAZB` = `76` | `6000` → `6008` |
| `6000` | `ZA=7; ZB1=7` | `ZAZB` = `77` | `6000` → `6008` |
| `6000` | `ZA=7; ZB1=8` | `ZAZB` = `78` | `6000` → `6008` |
| `6000` | `ZA=7; ZB1=9` | `ZAZB` = `79` | `6000` → `6008` |
| `6000` | `ZA=7; ZB2=0` | `ZAZB` = `70` | `6000` → `6008` |
| `6000` | `ZA=7; ZB2=1` | `ZAZB` = `71` | `6000` → `6008` |
| `6000` | `ZA=7; ZB2=2` | `ZAZB` = `72` | `6000` → `6008` |
| `6000` | `ZA=7; ZB2=3` | `ZAZB` = `73` | `6000` → `6008` |
| `6000` | `ZA=7; ZB2=4` | `ZAZB` = `74` | `6000` → `6008` |
| `6000` | `ZA=7; ZB2=5` | `ZAZB` = `75` | `6000` → `6008` |
| `6000` | `ZA=7; ZB2=6` | `ZAZB` = `76` | `6000` → `6008` |
| `6000` | `ZA=7; ZB2=7` | `ZAZB` = `77` | `6000` → `6008` |
| `6000` | `ZA=7; ZB2=8` | `ZAZB` = `78` | `6000` → `6008` |
| `6000` | `ZA=7; ZB2=9` | `ZAZB` = `79` | `6000` → `6008` |
| `6000` | `ZA=8; ZB1=5` | `ZAZB` = `85` | `6000` → `6009` |
| `6000` | `ZA=8; ZB1=6` | `ZAZB` = `86` | `6000` → `6009` |
| `6000` | `ZA=8; ZB1=7` | `ZAZB` = `87` | `6000` → `6009` |
| `6000` | `ZA=8; ZB1=8` | `ZAZB` = `88` | `6000` → `6009` |
| `6000` | `ZA=8; ZB1=9` | `ZAZB` = `89` | `6000` → `6009` |
| `6000` | `ZA=8; ZB1=0` | `ZAZB` = `80` | `6000` → `6009` |
| `6000` | `ZA=8; ZB1=1` | `ZAZB` = `81` | `6000` → `6009` |
| `6000` | `ZA=8; ZB1=2` | `ZAZB` = `82` | `6000` → `6009` |
| `6000` | `ZA=8; ZB1=3` | `ZAZB` = `83` | `6000` → `6009` |
| `6000` | `ZA=8; ZB1=4` | `ZAZB` = `84` | `6000` → `6009` |
| `6000` | `ZA=8; ZB2=5` | `ZAZB` = `85` | `6000` → `6009` |
| `6000` | `ZA=8; ZB2=6` | `ZAZB` = `86` | `6000` → `6009` |
| `6000` | `ZA=8; ZB2=7` | `ZAZB` = `87` | `6000` → `6009` |
| `6000` | `ZA=8; ZB2=8` | `ZAZB` = `88` | `6000` → `6009` |
| `6000` | `ZA=8; ZB2=9` | `ZAZB` = `89` | `6000` → `6009` |
| `6000` | `ZA=8; ZB2=0` | `ZAZB` = `80` | `6000` → `6009` |
| `6000` | `ZA=8; ZB2=1` | `ZAZB` = `81` | `6000` → `6009` |
| `6000` | `ZA=8; ZB2=2` | `ZAZB` = `82` | `6000` → `6009` |
| `6000` | `ZA=8; ZB2=3` | `ZAZB` = `83` | `6000` → `6009` |
| `6000` | `ZA=8; ZB2=4` | `ZAZB` = `84` | `6000` → `6009` |
| `6000` | `ZA=9; ZB1=0` | `ZAZB` = `90` | `6000` → `6010` |
| `6000` | `ZA=9; ZB1=1` | `ZAZB` = `91` | `6000` → `6010` |
| `6000` | `ZA=9; ZB1=2` | `ZAZB` = `92` | `6000` → `6010` |
| `6000` | `ZA=9; ZB1=3` | `ZAZB` = `93` | `6000` → `6010` |
| `6000` | `ZA=9; ZB1=4` | `ZAZB` = `94` | `6000` → `6010` |
| `6000` | `ZA=9; ZB1=5` | `ZAZB` = `95` | `6000` → `6010` |
| `6000` | `ZA=9; ZB1=6` | `ZAZB` = `96` | `6000` → `6010` |
| `6000` | `ZA=9; ZB1=7` | `ZAZB` = `97` | `6000` → `6010` |
| `6000` | `ZA=9; ZB1=8` | `ZAZB` = `98` | `6000` → `6010` |
| `6000` | `ZA=9; ZB1=9` | `ZAZB` = `99` | `6000` → `6010` |
| `6000` | `ZA=9; ZB2=0` | `ZAZB` = `90` | `6000` → `6010` |
| `6000` | `ZA=9; ZB2=1` | `ZAZB` = `91` | `6000` → `6010` |
| `6000` | `ZA=9; ZB2=2` | `ZAZB` = `92` | `6000` → `6010` |
| `6000` | `ZA=9; ZB2=3` | `ZAZB` = `93` | `6000` → `6010` |
| `6000` | `ZA=9; ZB2=4` | `ZAZB` = `94` | `6000` → `6010` |
| `6000` | `ZA=9; ZB2=5` | `ZAZB` = `95` | `6000` → `6010` |
| `6000` | `ZA=9; ZB2=6` | `ZAZB` = `96` | `6000` → `6010` |
| `6000` | `ZA=9; ZB2=7` | `ZAZB` = `97` | `6000` → `6010` |
| `6000` | `ZA=9; ZB2=8` | `ZAZB` = `98` | `6000` → `6010` |
| `6000` | `ZA=9; ZB2=9` | `ZAZB` = `99` | `6000` → `6010` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `144` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `169` - Temperature control on/off actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `170` - Temperature control open/close actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `52` - Temperature control pump actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |


These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system/model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

ZA is the shared zone tens digit; ZB1/N1 and ZB2/N2 give each relay’s zone units/progressive number. ZA and ZB use `0..9`; N1/N2 use 1..9. Equal `ZB1=ZB2` and `N1=N2` interlock the pair: C1 opens and C2 closes. `OFF` in the corresponding ZB disables that relay and its forcing button. Zone 00 selects a circulation-pump role; interlocking is not allowed for that role. The sheet illustrates separate zones, two radiators in one zone with different progressive numbers, an open/close valve and circulation pump. Apply its 10 A protective breaker separately from the relay rating. EOS compatibility requires batch 13W06 or later for both F430/2 and 003579 and software configuration.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session/validation method remains in [Programming](../../programming/).

## Source reconciliation

The file ST-00000902-EN prints the placeholder code ST-00000000-EN in its footer, and its first configuration paragraphs are Italian despite the English filename. The reference F430/2 and technical table are explicit. The older sheet and newer sheet are separately retained; catalogue firmware 14 and 163 are not assumed interchangeable. The source-specific pump role is corroborated by Object `52` in the later catalogue firmware. Historical sheets are not sufficient to prove support in every physical revision.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `F430-2-italian-product-sheet.pdf` | Exact named commercial/product export; values and descriptive defects reconciled against technical documents. Compliance-template dates do not date the product. |
| `ST-00000902-EN.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `F430-2-publisher-product-sheet.pdf` | Exact named variant; complete classification attributes captured above and EAN under Commercial identities. Sheet-specific ratings remain independently scoped. |
| `MQ00184_c_EN.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `ST-00002703-EN.pdf` | Explicit compatibility/reference inventory and ecosystem restrictions for this product; EOS electrical/display specifications are not transferred. |

## Evidence limits and open work

Installed production/firmware, pump acquisition/control behavior, contact timing and exact diagnostic support remain unobserved.

No installed hardware revision or microcontroller fingerprint is retained for this cluster. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Canonical catalogue extraction and reconciliation are complete for the retained evidence; further documentation discovery, runtime corroboration and final evidence closure remain partial.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
