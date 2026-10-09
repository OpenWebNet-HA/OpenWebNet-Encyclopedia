# Four-relay temperature-control actuator

## Summary

F430/4 uses four relays with a common contact to control temperature loads. It can operate four on/off loads, two open/close valves or a three-speed fan-coil with one valve. Its shared common terminal and application-specific relay grouping matter when choosing and wiring the loads.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0148` | Project identity |
| Technical description | Four-relay temperature-control actuator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `003580`, `F430/4` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1859` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Temperature control | Main system association |
| Item model / `modobj` | `145` | Main association; independent of project ID |
| Firmware definition | `13`, `164` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `4` | Firmware metadata |
| Categories | Actuators, Thermoregulation | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `003580` | Established catalogue identity | Manufacturer database commercial record `1697` explicitly links this SKU to item `1859` |
| BTicino | `F430/4` | Established catalogue identity | Manufacturer database commercial record `73` explicitly links this SKU to item `1859` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F430/4` | `8012199667706` | [F430-4-publisher-product-sheet.pdf](https://archive.openwebnet-ha.org/sha256/ba/98/ba98639f09572fe0b80d9cc602a5a381388f29aeb894473f5e4ffbbc42a6bbad.pdf) PDF p. 1 |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `F430/4` | DIN actuator/4 | Canonical commercial record `73` |
| `003580` | DIN actuator/4 | Canonical commercial record `1697` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MyHOME Technical Guide.pdf` | Installation Guide GUI-MHOME | `MyHOME Technical Guide; 27/04/2015` | Shared guide: F411U2 PDF pp. 47, 99; F413N pp. 56,100; HVAC pp. 63-68,101; HOMETOUCH pp. 18-20,82; pulse meter p.101. Printed page is PDF page minus 2. Model-name and output-count defects reconciled locally. | [Archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MyHOME Technical Guide.pdf) |
| `F430-4-italian-product-sheet.pdf` | Exact Italian product export | `Captured 05/10/2026; compliance-template date does not establish product publication date` | PDF pp. 1-2: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/4a/3f/4a3fdd0242299f2dd6a394f87fb949cb8771a99668d4d842cc2c2b6de559d6ef.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F430_4) |
| `ST-00000903-EN.pdf` | Technical Sheet ST-00000903-EN | `ST-00000903-EN; 23/03/2021` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/7b/cc/7bccd79e80c2436c8e11af36a3e0ea63dfe23d301cfdc84777259cbec6535d23.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00000903-EN.pdf) |
| `F430-4-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 05.10.2026` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/ba/98/ba98639f09572fe0b80d9cc602a5a381388f29aeb894473f5e4ffbbc42a6bbad.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-F430/4&include_technical=1) |
| `ST-00002703-EN.pdf` | Technical Sheet ST-00002703-EN | `ST-00002703-EN; 16/06/2026` | PDF p. 9: exact-reference ecosystem compatibility rows and minimum production batches; other EOS functions and wiring are outside this review. | [Archived original](https://archive.openwebnet-ha.org/sha256/b2/f5/b2f5090b601e33cdef9ba666108848ff4d9800792ccd5b7c14385da300bf0ffa.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002703-EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1859`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |
| `MyHOME-Suite-thermoregulation-actuator-functions-IT.html` | Manufacturer Suite function help | Publication date unstated | Exact F430/4 on/off, open/close and pump function inventory | [Archived original](https://archive.openwebnet-ha.org/sha256/bc/cc/bccc3ce223a0e3536f2e76e28ed010ec664397e14ab6fc7a14a30eb7dc7f5413.pdf) | [Publisher source](https://myhomeswupdate.bticino.com/MyHOMESuite_Docs/MHS_function_0304b/IT_MHS_function_0304/attuatori_termo.html) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS nominal / operating supply | `27 Vdc / 18..27 Vdc` | `ST-00000903-EN` printed/PDF pp. 1-4 |
| Standby draw | `9 mA` | `ST-00000903-EN` printed/PDF pp. 1-4 |
| Maximum independent / interlocked or fan-coil draw | `37.5 mA / 20.5 mA` | `ST-00000903-EN` printed/PDF pp. 1-4 |
| Relay ratings | `4 A resistive / 1 A inductive` | `ST-00000903-EN` printed/PDF pp. 1-4 |
| Temperature / size | `5..40 °C; 2 DIN modules` | `ST-00000903-EN` printed/PDF pp. 1-4 |
| Maximum dissipation | `3.2 W` | `ST-00000903-EN` printed/PDF pp. 1-4 |
| Contacts | `terminal 1 common; outputs C1/C2/C3/C4 terminals 2/3/4/5` | `ST-00000903-EN` printed/PDF pp. 1-4 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. A negative connected-object classification does not exclude remote control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system radio frequency | `No` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system LON | `No` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system Powernet | `No` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Other bus systems | `Other` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Mounting method | `DRA (DIN-rail adaptor)` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Width in number of modular spacings | `2` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Local operation/hand operation | `Yes` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| With LED indication | `Yes` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Number of digital inputs | `0` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Output power | `3.2 W` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Suitable for C-load | `No` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Max. number of switching contacts | `4` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Max. switching current | `4 A` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Rated current | `4 A` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Rated operating voltage (Min- Max) | `18-240 V` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Different phases connectable | `No` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| With bus connection | `Yes` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Modular expandability | `No` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Degree of protection (IP) | `IP20` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Width | `36 mm` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Height | `105 mm` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Depth | `31 mm` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| degree of impact strength (IK) | `IK07` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Operating / setting temperature (Min-Max) | `5-40 °C` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Storage temperature (Min-Max) | `-25-75 °C` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Voltage type | `AC/DC` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Supply current (Min-Max) | `0.009-4 A` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Terminal marking indication | `Yes` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Type of load | `Other` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Connection type | `Screwed terminal` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Number of distribution blocks | `4` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Label space/information surface | `No` | `F430-4-publisher-product-sheet.pdf` PDF p. 2 |
| Fitted with USB plug | `No` | `F430-4-publisher-product-sheet.pdf` PDF p. 3 |
| Addressable | `Yes` | `F430-4-publisher-product-sheet.pdf` PDF p. 3 |
| Connected object | `No` | `F430-4-publisher-product-sheet.pdf` PDF p. 3 |
| Product use function | `Thermal comfort management` | `F430-4-publisher-product-sheet.pdf` PDF p. 3 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1859` | Canonical catalogue |
| Technical item description | DIN actuator/4 | Canonical catalogue |
| Item family | 0; key `2` | Canonical catalogue |
| Main system | Temperature control; key `2` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `145` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Temperature control | `145` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `13` | `6` | `0` | `0` | `4` | Not catalogue default | Official |
| `164` | `5` | `0` | `0` | `4` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `13` | `1` | `169` Temperature control on/off actuator | Fixed/designated metadata | `681` | `169` | `475` |
| `13` | `1` | `170` Temperature control open/close actuator | Candidate alternative | `686` | `170` | `477` |
| `13` | `1` | `171` 2 pipes fan coil actuator with `ON`-`OFF` valve | Candidate alternative | `685` | `171` | `476` |
| `13` | `1` | `52` Temperature control pump actuator | Candidate alternative | `1211` | `533` | `651` |
| `13` | `2` | `169` Temperature control on/off actuator | Fixed/designated metadata | `682` | `169` | `475` |
| `13` | `2` | `170` Temperature control open/close actuator | Candidate alternative | `687` | `170` | `477` |
| `13` | `2` | `52` Temperature control pump actuator | Candidate alternative | `1212` | `533` | `651` |
| `13` | `3` | `169` Temperature control on/off actuator | Fixed/designated metadata | `683` | `169` | `475` |
| `13` | `3` | `170` Temperature control open/close actuator | Candidate alternative | `688` | `170` | `477` |
| `13` | `3` | `52` Temperature control pump actuator | Candidate alternative | `1213` | `533` | `651` |
| `13` | `4` | `169` Temperature control on/off actuator | Fixed/designated metadata | `684` | `169` | `475` |
| `13` | `4` | `52` Temperature control pump actuator | Candidate alternative | `1214` | `533` | `651` |
| `164` | `1` | `169` Temperature control on/off actuator | Fixed/designated metadata | `1375` | `169` | `726` |
| `164` | `1` | `170` Temperature control open/close actuator | Candidate alternative | `1380` | `170` | `728` |
| `164` | `1` | `171` 2 pipes fan coil actuator with `ON`-`OFF` valve | Candidate alternative | `1379` | `171` | `727` |
| `164` | `2` | `169` Temperature control on/off actuator | Fixed/designated metadata | `1376` | `169` | `726` |
| `164` | `2` | `170` Temperature control open/close actuator | Candidate alternative | `1381` | `170` | `728` |
| `164` | `3` | `169` Temperature control on/off actuator | Fixed/designated metadata | `1377` | `169` | `726` |
| `164` | `3` | `170` Temperature control open/close actuator | Candidate alternative | `1382` | `170` | `728` |
| `164` | `4` | `169` Temperature control on/off actuator | Fixed/designated metadata | `1378` | `169` | `726` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `13` | `519` Thermoregulation relay virgin | `1`, `2`, `3`, `4` | `52`, `86`, `87`, `89`, `93`, `169`, `170`, `171` | `519` | `34` |
| `164` | `519` Thermoregulation relay virgin | `1`, `2`, `3`, `4` | `52`, `86`, `87`, `89`, `93`, `169`, `170`, `171` | `519` | `44` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `13` | Physical configuration | `0` | Canonical firmware/mode association |
| `13` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `13` | Advanced Configuration | `2` | Canonical firmware/mode association |
| `164` | Physical configuration | `0` | Canonical firmware/mode association |
| `164` | Virtual Configuration | `1` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `ZA / ZB1..4 / N` | zone tens / relay-specific zone units / shared progressive number | `ST-00000903-EN` printed/PDF pp. 1-4 |
| `Different ZB1..4` | four separate-zone on/off loads | `ST-00000903-EN` printed/PDF pp. 1-4 |
| `ZB1=ZB2; ZB3=ZB4` | two open/close pairs: C1/C2 and C3/C4 | `ST-00000903-EN` printed/PDF pp. 1-4 |
| `ZB1=ZB2=ZB3=ZB4` | fan-coil: C1 valve; C2/C3/C4 low/medium/high fan | `ST-00000903-EN` printed/PDF pp. 1-4 |
| `OFF exclusions` | RL`2..4` can be excluded; RL1 cannot | `ST-00000903-EN` printed/PDF pp. 1-4 |
| `Physical zone 00 / separate loads same zone` | prohibited in retained sheet; later catalogue pump candidate separately unresolved | `ST-00000903-EN` printed/PDF pp. 1-4 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `13` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `13` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `13` | `ZB1` | `0..9`; `10` = `OFF` | `0` | ZB1 |
| `13` | `ZB2` | `0..9`; `10` = `OFF` | `0` | ZB2; ZB2 thermo Actuator zone address |
| `13` | `ZB3` | `0..9`; `10` = `OFF` | `0` | ZB3; ZB3 thermo Actuator zone address |
| `13` | `ZB4` | `0..9`; `10` = `OFF` | `0` | ZB4; ZB4 thermo Actuator zone address |
| `13` | `N` | `0..9` | `1` | N; Thermoregulation zone device number N |
| `164` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `164` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `164` | `ZB1` | `0..9`; `10` = `OFF` | `0` | ZB1 |
| `164` | `ZB2` | `0..9`; `10` = `OFF` | `0` | ZB2; ZB2 thermo Actuator zone address |
| `164` | `ZB3` | `0..9`; `10` = `OFF` | `0` | ZB3; ZB3 thermo Actuator zone address |
| `164` | `ZB4` | `0..9`; `10` = `OFF` | `0` | ZB4; ZB4 thermo Actuator zone address |
| `164` | `N` | `0..9` | `1` | N; Thermoregulation zone device number N The 0 value is valid only when device is virgin |

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

### Object `171` - 2 pipes fan coil actuator with `ON`-`OFF` valve

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `1..9` | `1` | Device number |

### Object `52` - Temperature control pump actuator

Catalogue Object key `533` maps to external Object `52`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `00` | `00` | Zone |
| `N` | `1..9` | `1` | Device number |

### Object `86` - Temperature control 3 points valve actuator (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `0..9` | `1` | Device number |
| `VALVE_TIME_LOW` | `0..255` | `60` | Valve time low; Valve_time_low (Valve time in seconds, over 2 bytes (0...767s)) |
| `VALVE_TIME_HIGH` | `0..2` | `0` | Valve time high; Valve_time_high (Valve time in seconds, over 2 bytes (0...767s)) |

### Object `87` - Temperature control 2 pipes fan coil actuator with 3 points valve (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `0..9` | `1` | Device number |
| `VALVE_TIME_LOW` | `0..255` | `60` | Valve time low; Valve_time_low (Valve time in seconds, over 2 bytes (0...767s)) |
| `VALVE_TIME_HIGH` | `0..2` | `0` | Valve time high; Valve_time_high (Valve time in seconds, over 2 bytes (0...767s)) |

### Object `89` - Temperature control 4 pipes fan coil actuator with ON/OFF valves (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `0..9` | `1` | Device number |

### Object `93` - Temperature control 4 pipes fan coil actuator with 3 points valve (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `0..9` | `1` | Device number |
| `HEATING_VALVE_TIME_LOW` | `0..255` | `60` | Heating valve time low; (Valve time in seconds, over 2 bytes (0...767s)) |
| `HEATING_VALVE_TIME_HIGH` | `0..2` | `0` | Heating valve time high; (Valve time in seconds, over 2 bytes (0...767s)) |
| `COOLING_VALVE_TIME_LOW` | `0..255` | `60` | Cooling valve time low; (Valve time in seconds, over 2 bytes (0...767s)) |
| `COOLING_VALVE_TIME_HIGH` | `0..2` | `0` | Cooling valve time high; (Valve time in seconds, over 2 bytes (0...767s)) |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `13` | `1` | `169` | `4164` | No textual predicate stored | `6000` |
| `13` | `1` | `169` | `4882` | `ZB1<>OFF` | `2000` |
| `13` | `1` | `169` | `4883` | `ZB1=OFF` | `2001` |
| `13` | `1` | `170` | `4884` | `ZB1=ZB2` | `2000` |
| `13` | `1` | `171` | `4886` | `ZB1=ZB2;ZB2=ZB3;ZB3=ZB4` | `2001` |
| `13` | `2` | `169` | `4887` | `ZB2<>OFF` | `3000` |
| `13` | `2` | `169` | `4888` | `ZB2=OFF` | `3001` |
| `13` | `2` | `170` | `4889` | `ZB2=ZB3` | `3000` |
| `13` | `3` | `169` | `4890` | `ZB3<>OFF` | `4000` |
| `13` | `3` | `169` | `4891` | `ZB3=OFF` | `4001` |
| `13` | `3` | `170` | `4892` | `ZB3=ZB4` | `4000` |
| `13` | `4` | `169` | `4893` | `ZB4<>OFF` | `5000` |
| `13` | `4` | `169` | `4894` | `ZB4=OFF` | `5001` |
| `164` | `1` | `169` | `4164` | No textual predicate stored | `6000` |
| `164` | `1` | `169` | `4882` | `ZB1<>OFF` | `2000` |
| `164` | `1` | `169` | `4883` | `ZB1=OFF` | `2001` |
| `164` | `1` | `170` | `4884` | `ZB1=ZB2` | `2000` |
| `164` | `1` | `171` | `4886` | `ZB1=ZB2;ZB2=ZB3;ZB3=ZB4` | `2001` |
| `164` | `2` | `169` | `4887` | `ZB2<>OFF` | `3000` |
| `164` | `2` | `169` | `4888` | `ZB2=OFF` | `3001` |
| `164` | `2` | `170` | `4889` | `ZB2=ZB3` | `3000` |
| `164` | `3` | `169` | `4890` | `ZB3<>OFF` | `4000` |
| `164` | `3` | `169` | `4891` | `ZB3=OFF` | `4001` |
| `164` | `3` | `170` | `4892` | `ZB3=ZB4` | `4000` |
| `164` | `4` | `169` | `4893` | `ZB4<>OFF` | `5000` |
| `164` | `4` | `169` | `4894` | `ZB4=OFF` | `5001` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `13` | `169` | `675` | `SUBTYPE` | `16` = Valve on/off; `17` = Pump (entire reusable range retained) | `16` | Subtype |
| `13` | `170` | `678` | `SUBTYPE` | `16` = Valve on/off; `17` = Pump (entire reusable range retained) | `16` | Subtype |

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
| `4000` | `ZA=0; ZB3=1` | `ZAZB` = `1` | `4000` → `4001` |
| `4000` | `ZA=0; ZB3=2` | `ZAZB` = `2` | `4000` → `4001` |
| `4000` | `ZA=0; ZB3=3` | `ZAZB` = `3` | `4000` → `4001` |
| `4000` | `ZA=0; ZB3=4` | `ZAZB` = `4` | `4000` → `4001` |
| `4000` | `ZA=0; ZB3=5` | `ZAZB` = `5` | `4000` → `4001` |
| `4000` | `ZA=0; ZB3=6` | `ZAZB` = `6` | `4000` → `4001` |
| `4000` | `ZA=0; ZB3=7` | `ZAZB` = `7` | `4000` → `4001` |
| `4000` | `ZA=0; ZB3=8` | `ZAZB` = `8` | `4000` → `4001` |
| `4000` | `ZA=0; ZB3=9` | `ZAZB` = `9` | `4000` → `4001` |
| `4000` | `ZA=0; ZB3=OFF` | `ZAZB` = `OFF` | `4000` → `4001` |
| `4000` | `ZA=1; ZB3=0` | `ZAZB` = `10` | `4000` → `4002` |
| `4000` | `ZA=1; ZB3=1` | `ZAZB` = `11` | `4000` → `4002` |
| `4000` | `ZA=1; ZB3=2` | `ZAZB` = `12` | `4000` → `4002` |
| `4000` | `ZA=1; ZB3=3` | `ZAZB` = `13` | `4000` → `4002` |
| `4000` | `ZA=1; ZB3=4` | `ZAZB` = `14` | `4000` → `4002` |
| `4000` | `ZA=1; ZB3=5` | `ZAZB` = `15` | `4000` → `4002` |
| `4000` | `ZA=1; ZB3=6` | `ZAZB` = `16` | `4000` → `4002` |
| `4000` | `ZA=1; ZB3=7` | `ZAZB` = `17` | `4000` → `4002` |
| `4000` | `ZA=1; ZB3=8` | `ZAZB` = `18` | `4000` → `4002` |
| `4000` | `ZA=1; ZB3=9` | `ZAZB` = `19` | `4000` → `4002` |
| `4000` | `ZA=1; ZB3=OFF` | `ZAZB` = `OFF` | `4000` → `4002` |
| `4000` | `ZA=2; ZB3=0` | `ZAZB` = `20` | `4000` → `4003` |
| `4000` | `ZA=2; ZB3=1` | `ZAZB` = `21` | `4000` → `4003` |
| `4000` | `ZA=2; ZB3=2` | `ZAZB` = `22` | `4000` → `4003` |
| `4000` | `ZA=2; ZB3=3` | `ZAZB` = `23` | `4000` → `4003` |
| `4000` | `ZA=2; ZB3=4` | `ZAZB` = `24` | `4000` → `4003` |
| `4000` | `ZA=2; ZB3=5` | `ZAZB` = `25` | `4000` → `4003` |
| `4000` | `ZA=2; ZB3=6` | `ZAZB` = `26` | `4000` → `4003` |
| `4000` | `ZA=2; ZB3=7` | `ZAZB` = `27` | `4000` → `4003` |
| `4000` | `ZA=2; ZB3=8` | `ZAZB` = `28` | `4000` → `4003` |
| `4000` | `ZA=2; ZB3=9` | `ZAZB` = `29` | `4000` → `4003` |
| `4000` | `ZA=2; ZB3=OFF` | `ZAZB` = `OFF` | `4000` → `4003` |
| `4000` | `ZA=3; ZB3=0` | `ZAZB` = `30` | `4000` → `4004` |
| `4000` | `ZA=3; ZB3=1` | `ZAZB` = `31` | `4000` → `4004` |
| `4000` | `ZA=3; ZB3=2` | `ZAZB` = `32` | `4000` → `4004` |
| `4000` | `ZA=3; ZB3=3` | `ZAZB` = `33` | `4000` → `4004` |
| `4000` | `ZA=3; ZB3=4` | `ZAZB` = `34` | `4000` → `4004` |
| `4000` | `ZA=3; ZB3=5` | `ZAZB` = `35` | `4000` → `4004` |
| `4000` | `ZA=3; ZB3=6` | `ZAZB` = `36` | `4000` → `4004` |
| `4000` | `ZA=3; ZB3=7` | `ZAZB` = `37` | `4000` → `4004` |
| `4000` | `ZA=3; ZB3=8` | `ZAZB` = `38` | `4000` → `4004` |
| `4000` | `ZA=3; ZB3=9` | `ZAZB` = `39` | `4000` → `4004` |
| `4000` | `ZA=3; ZB3=OFF` | `ZAZB` = `OFF` | `4000` → `4004` |
| `4000` | `ZA=4; ZB3=0` | `ZAZB` = `40` | `4000` → `4005` |
| `4000` | `ZA=4; ZB3=1` | `ZAZB` = `41` | `4000` → `4005` |
| `4000` | `ZA=4; ZB3=2` | `ZAZB` = `42` | `4000` → `4005` |
| `4000` | `ZA=4; ZB3=3` | `ZAZB` = `43` | `4000` → `4005` |
| `4000` | `ZA=4; ZB3=4` | `ZAZB` = `44` | `4000` → `4005` |
| `4000` | `ZA=4; ZB3=5` | `ZAZB` = `45` | `4000` → `4005` |
| `4000` | `ZA=4; ZB3=6` | `ZAZB` = `46` | `4000` → `4005` |
| `4000` | `ZA=4; ZB3=7` | `ZAZB` = `47` | `4000` → `4005` |
| `4000` | `ZA=4; ZB3=8` | `ZAZB` = `48` | `4000` → `4005` |
| `4000` | `ZA=4; ZB3=9` | `ZAZB` = `49` | `4000` → `4005` |
| `4000` | `ZA=4; ZB3=OFF` | `ZAZB` = `OFF` | `4000` → `4005` |
| `4000` | `ZA=5; ZB3=0` | `ZAZB` = `50` | `4000` → `4006` |
| `4000` | `ZA=5; ZB3=1` | `ZAZB` = `51` | `4000` → `4006` |
| `4000` | `ZA=5; ZB3=2` | `ZAZB` = `52` | `4000` → `4006` |
| `4000` | `ZA=5; ZB3=3` | `ZAZB` = `53` | `4000` → `4006` |
| `4000` | `ZA=5; ZB3=4` | `ZAZB` = `54` | `4000` → `4006` |
| `4000` | `ZA=5; ZB3=5` | `ZAZB` = `55` | `4000` → `4006` |
| `4000` | `ZA=5; ZB3=6` | `ZAZB` = `56` | `4000` → `4006` |
| `4000` | `ZA=5; ZB3=7` | `ZAZB` = `57` | `4000` → `4006` |
| `4000` | `ZA=5; ZB3=8` | `ZAZB` = `58` | `4000` → `4006` |
| `4000` | `ZA=5; ZB3=9` | `ZAZB` = `59` | `4000` → `4006` |
| `4000` | `ZA=5; ZB3=OFF` | `ZAZB` = `OFF` | `4000` → `4006` |
| `4000` | `ZA=6; ZB3=0` | `ZAZB` = `60` | `4000` → `4007` |
| `4000` | `ZA=6; ZB3=1` | `ZAZB` = `61` | `4000` → `4007` |
| `4000` | `ZA=6; ZB3=2` | `ZAZB` = `62` | `4000` → `4007` |
| `4000` | `ZA=6; ZB3=3` | `ZAZB` = `63` | `4000` → `4007` |
| `4000` | `ZA=6; ZB3=4` | `ZAZB` = `64` | `4000` → `4007` |
| `4000` | `ZA=6; ZB3=5` | `ZAZB` = `65` | `4000` → `4007` |
| `4000` | `ZA=6; ZB3=6` | `ZAZB` = `66` | `4000` → `4007` |
| `4000` | `ZA=6; ZB3=7` | `ZAZB` = `67` | `4000` → `4007` |
| `4000` | `ZA=6; ZB3=8` | `ZAZB` = `68` | `4000` → `4007` |
| `4000` | `ZA=6; ZB3=9` | `ZAZB` = `69` | `4000` → `4007` |
| `4000` | `ZA=6; ZB3=OFF` | `ZAZB` = `OFF` | `4000` → `4007` |
| `4000` | `ZA=7; ZB3=0` | `ZAZB` = `70` | `4000` → `4008` |
| `4000` | `ZA=7; ZB3=1` | `ZAZB` = `71` | `4000` → `4008` |
| `4000` | `ZA=7; ZB3=2` | `ZAZB` = `72` | `4000` → `4008` |
| `4000` | `ZA=7; ZB3=3` | `ZAZB` = `73` | `4000` → `4008` |
| `4000` | `ZA=7; ZB3=4` | `ZAZB` = `74` | `4000` → `4008` |
| `4000` | `ZA=7; ZB3=5` | `ZAZB` = `75` | `4000` → `4008` |
| `4000` | `ZA=7; ZB3=6` | `ZAZB` = `76` | `4000` → `4008` |
| `4000` | `ZA=7; ZB3=7` | `ZAZB` = `77` | `4000` → `4008` |
| `4000` | `ZA=7; ZB3=8` | `ZAZB` = `78` | `4000` → `4008` |
| `4000` | `ZA=7; ZB3=9` | `ZAZB` = `79` | `4000` → `4008` |
| `4000` | `ZA=7; ZB3=OFF` | `ZAZB` = `OFF` | `4000` → `4008` |
| `4000` | `ZA=8; ZB3=5` | `ZAZB` = `85` | `4000` → `4009` |
| `4000` | `ZA=8; ZB3=6` | `ZAZB` = `86` | `4000` → `4009` |
| `4000` | `ZA=8; ZB3=7` | `ZAZB` = `87` | `4000` → `4009` |
| `4000` | `ZA=8; ZB3=8` | `ZAZB` = `88` | `4000` → `4009` |
| `4000` | `ZA=8; ZB3=9` | `ZAZB` = `89` | `4000` → `4009` |
| `4000` | `ZA=8; ZB3=0` | `ZAZB` = `80` | `4000` → `4009` |
| `4000` | `ZA=8; ZB3=1` | `ZAZB` = `81` | `4000` → `4009` |
| `4000` | `ZA=8; ZB3=2` | `ZAZB` = `82` | `4000` → `4009` |
| `4000` | `ZA=8; ZB3=3` | `ZAZB` = `83` | `4000` → `4009` |
| `4000` | `ZA=8; ZB3=4` | `ZAZB` = `84` | `4000` → `4009` |
| `4000` | `ZA=8; ZB3=OFF` | `ZAZB` = `OFF` | `4000` → `4009` |
| `4000` | `ZA=9; ZB3=0` | `ZAZB` = `90` | `4000` → `4010` |
| `4000` | `ZA=9; ZB3=1` | `ZAZB` = `91` | `4000` → `4010` |
| `4000` | `ZA=9; ZB3=2` | `ZAZB` = `92` | `4000` → `4010` |
| `4000` | `ZA=9; ZB3=3` | `ZAZB` = `93` | `4000` → `4010` |
| `4000` | `ZA=9; ZB3=4` | `ZAZB` = `94` | `4000` → `4010` |
| `4000` | `ZA=9; ZB3=5` | `ZAZB` = `95` | `4000` → `4010` |
| `4000` | `ZA=9; ZB3=6` | `ZAZB` = `96` | `4000` → `4010` |
| `4000` | `ZA=9; ZB3=7` | `ZAZB` = `97` | `4000` → `4010` |
| `4000` | `ZA=9; ZB3=8` | `ZAZB` = `98` | `4000` → `4010` |
| `4000` | `ZA=9; ZB3=9` | `ZAZB` = `99` | `4000` → `4010` |
| `4000` | `ZA=9; ZB3=OFF` | `ZAZB` = `OFF` | `4000` → `4010` |
| `4001` | `ZB3=1` | `ZAZB` = `1` | `4001` |
| `4001` | `ZB3=2` | `ZAZB` = `2` | `4001` |
| `4001` | `ZB3=3` | `ZAZB` = `3` | `4001` |
| `4001` | `ZB3=4` | `ZAZB` = `4` | `4001` |
| `4001` | `ZB3=5` | `ZAZB` = `5` | `4001` |
| `4001` | `ZB3=6` | `ZAZB` = `6` | `4001` |
| `4001` | `ZB3=7` | `ZAZB` = `7` | `4001` |
| `4001` | `ZB3=8` | `ZAZB` = `8` | `4001` |
| `4001` | `ZB3=9` | `ZAZB` = `9` | `4001` |
| `4001` | `ZB3=OFF` | `ZAZB` = `OFF` | `4001` |
| `5000` | `ZA=0; ZB4=1` | `ZAZB` = `1` | `5000` → `5001` |
| `5000` | `ZA=0; ZB4=2` | `ZAZB` = `2` | `5000` → `5001` |
| `5000` | `ZA=0; ZB4=3` | `ZAZB` = `3` | `5000` → `5001` |
| `5000` | `ZA=0; ZB4=4` | `ZAZB` = `4` | `5000` → `5001` |
| `5000` | `ZA=0; ZB4=5` | `ZAZB` = `5` | `5000` → `5001` |
| `5000` | `ZA=0; ZB4=6` | `ZAZB` = `6` | `5000` → `5001` |
| `5000` | `ZA=0; ZB4=7` | `ZAZB` = `7` | `5000` → `5001` |
| `5000` | `ZA=0; ZB4=8` | `ZAZB` = `8` | `5000` → `5001` |
| `5000` | `ZA=0; ZB4=9` | `ZAZB` = `9` | `5000` → `5001` |
| `5000` | `ZA=0; ZB4=OFF` | `ZAZB` = `OFF` | `5000` → `5001` |
| `5000` | `ZA=1; ZB4=0` | `ZAZB` = `10` | `5000` → `5002` |
| `5000` | `ZA=1; ZB4=1` | `ZAZB` = `11` | `5000` → `5002` |
| `5000` | `ZA=1; ZB4=2` | `ZAZB` = `12` | `5000` → `5002` |
| `5000` | `ZA=1; ZB4=3` | `ZAZB` = `13` | `5000` → `5002` |
| `5000` | `ZA=1; ZB4=4` | `ZAZB` = `14` | `5000` → `5002` |
| `5000` | `ZA=1; ZB4=5` | `ZAZB` = `15` | `5000` → `5002` |
| `5000` | `ZA=1; ZB4=6` | `ZAZB` = `16` | `5000` → `5002` |
| `5000` | `ZA=1; ZB4=7` | `ZAZB` = `17` | `5000` → `5002` |
| `5000` | `ZA=1; ZB4=8` | `ZAZB` = `18` | `5000` → `5002` |
| `5000` | `ZA=1; ZB4=9` | `ZAZB` = `19` | `5000` → `5002` |
| `5000` | `ZA=1; ZB4=OFF` | `ZAZB` = `OFF` | `5000` → `5002` |
| `5000` | `ZA=2; ZB4=0` | `ZAZB` = `20` | `5000` → `5003` |
| `5000` | `ZA=2; ZB4=1` | `ZAZB` = `21` | `5000` → `5003` |
| `5000` | `ZA=2; ZB4=2` | `ZAZB` = `22` | `5000` → `5003` |
| `5000` | `ZA=2; ZB4=3` | `ZAZB` = `23` | `5000` → `5003` |
| `5000` | `ZA=2; ZB4=4` | `ZAZB` = `24` | `5000` → `5003` |
| `5000` | `ZA=2; ZB4=5` | `ZAZB` = `25` | `5000` → `5003` |
| `5000` | `ZA=2; ZB4=6` | `ZAZB` = `26` | `5000` → `5003` |
| `5000` | `ZA=2; ZB4=7` | `ZAZB` = `27` | `5000` → `5003` |
| `5000` | `ZA=2; ZB4=8` | `ZAZB` = `28` | `5000` → `5003` |
| `5000` | `ZA=2; ZB4=9` | `ZAZB` = `29` | `5000` → `5003` |
| `5000` | `ZA=2; ZB4=OFF` | `ZAZB` = `OFF` | `5000` → `5003` |
| `5000` | `ZA=3; ZB4=0` | `ZAZB` = `30` | `5000` → `5004` |
| `5000` | `ZA=3; ZB4=1` | `ZAZB` = `31` | `5000` → `5004` |
| `5000` | `ZA=3; ZB4=2` | `ZAZB` = `32` | `5000` → `5004` |
| `5000` | `ZA=3; ZB4=3` | `ZAZB` = `33` | `5000` → `5004` |
| `5000` | `ZA=3; ZB4=4` | `ZAZB` = `34` | `5000` → `5004` |
| `5000` | `ZA=3; ZB4=5` | `ZAZB` = `35` | `5000` → `5004` |
| `5000` | `ZA=3; ZB4=6` | `ZAZB` = `36` | `5000` → `5004` |
| `5000` | `ZA=3; ZB4=7` | `ZAZB` = `37` | `5000` → `5004` |
| `5000` | `ZA=3; ZB4=8` | `ZAZB` = `38` | `5000` → `5004` |
| `5000` | `ZA=3; ZB4=9` | `ZAZB` = `39` | `5000` → `5004` |
| `5000` | `ZA=3; ZB4=OFF` | `ZAZB` = `OFF` | `5000` → `5004` |
| `5000` | `ZA=4; ZB4=0` | `ZAZB` = `40` | `5000` → `5005` |
| `5000` | `ZA=4; ZB4=1` | `ZAZB` = `41` | `5000` → `5005` |
| `5000` | `ZA=4; ZB4=2` | `ZAZB` = `42` | `5000` → `5005` |
| `5000` | `ZA=4; ZB4=3` | `ZAZB` = `43` | `5000` → `5005` |
| `5000` | `ZA=4; ZB4=4` | `ZAZB` = `44` | `5000` → `5005` |
| `5000` | `ZA=4; ZB4=5` | `ZAZB` = `45` | `5000` → `5005` |
| `5000` | `ZA=4; ZB4=6` | `ZAZB` = `46` | `5000` → `5005` |
| `5000` | `ZA=4; ZB4=7` | `ZAZB` = `47` | `5000` → `5005` |
| `5000` | `ZA=4; ZB4=8` | `ZAZB` = `48` | `5000` → `5005` |
| `5000` | `ZA=4; ZB4=9` | `ZAZB` = `49` | `5000` → `5005` |
| `5000` | `ZA=4; ZB4=OFF` | `ZAZB` = `OFF` | `5000` → `5005` |
| `5000` | `ZA=5; ZB4=0` | `ZAZB` = `50` | `5000` → `5006` |
| `5000` | `ZA=5; ZB4=1` | `ZAZB` = `51` | `5000` → `5006` |
| `5000` | `ZA=5; ZB4=2` | `ZAZB` = `52` | `5000` → `5006` |
| `5000` | `ZA=5; ZB4=3` | `ZAZB` = `53` | `5000` → `5006` |
| `5000` | `ZA=5; ZB4=4` | `ZAZB` = `54` | `5000` → `5006` |
| `5000` | `ZA=5; ZB4=5` | `ZAZB` = `55` | `5000` → `5006` |
| `5000` | `ZA=5; ZB4=6` | `ZAZB` = `56` | `5000` → `5006` |
| `5000` | `ZA=5; ZB4=7` | `ZAZB` = `57` | `5000` → `5006` |
| `5000` | `ZA=5; ZB4=8` | `ZAZB` = `58` | `5000` → `5006` |
| `5000` | `ZA=5; ZB4=9` | `ZAZB` = `59` | `5000` → `5006` |
| `5000` | `ZA=5; ZB4=OFF` | `ZAZB` = `OFF` | `5000` → `5006` |
| `5000` | `ZA=6; ZB4=0` | `ZAZB` = `60` | `5000` → `5007` |
| `5000` | `ZA=6; ZB4=1` | `ZAZB` = `61` | `5000` → `5007` |
| `5000` | `ZA=6; ZB4=2` | `ZAZB` = `62` | `5000` → `5007` |
| `5000` | `ZA=6; ZB4=3` | `ZAZB` = `63` | `5000` → `5007` |
| `5000` | `ZA=6; ZB4=4` | `ZAZB` = `64` | `5000` → `5007` |
| `5000` | `ZA=6; ZB4=5` | `ZAZB` = `65` | `5000` → `5007` |
| `5000` | `ZA=6; ZB4=6` | `ZAZB` = `66` | `5000` → `5007` |
| `5000` | `ZA=6; ZB4=7` | `ZAZB` = `67` | `5000` → `5007` |
| `5000` | `ZA=6; ZB4=8` | `ZAZB` = `68` | `5000` → `5007` |
| `5000` | `ZA=6; ZB4=9` | `ZAZB` = `69` | `5000` → `5007` |
| `5000` | `ZA=6; ZB4=OFF` | `ZAZB` = `OFF` | `5000` → `5007` |
| `5000` | `ZA=7; ZB4=0` | `ZAZB` = `70` | `5000` → `5008` |
| `5000` | `ZA=7; ZB4=1` | `ZAZB` = `71` | `5000` → `5008` |
| `5000` | `ZA=7; ZB4=2` | `ZAZB` = `72` | `5000` → `5008` |
| `5000` | `ZA=7; ZB4=3` | `ZAZB` = `73` | `5000` → `5008` |
| `5000` | `ZA=7; ZB4=4` | `ZAZB` = `74` | `5000` → `5008` |
| `5000` | `ZA=7; ZB4=5` | `ZAZB` = `75` | `5000` → `5008` |
| `5000` | `ZA=7; ZB4=6` | `ZAZB` = `76` | `5000` → `5008` |
| `5000` | `ZA=7; ZB4=7` | `ZAZB` = `77` | `5000` → `5008` |
| `5000` | `ZA=7; ZB4=8` | `ZAZB` = `78` | `5000` → `5008` |
| `5000` | `ZA=7; ZB4=9` | `ZAZB` = `79` | `5000` → `5008` |
| `5000` | `ZA=7; ZB4=OFF` | `ZAZB` = `OFF` | `5000` → `5008` |
| `5000` | `ZA=8; ZB4=5` | `ZAZB` = `85` | `5000` → `5009` |
| `5000` | `ZA=8; ZB4=6` | `ZAZB` = `86` | `5000` → `5009` |
| `5000` | `ZA=8; ZB4=7` | `ZAZB` = `87` | `5000` → `5009` |
| `5000` | `ZA=8; ZB4=8` | `ZAZB` = `88` | `5000` → `5009` |
| `5000` | `ZA=8; ZB4=9` | `ZAZB` = `89` | `5000` → `5009` |
| `5000` | `ZA=8; ZB4=0` | `ZAZB` = `80` | `5000` → `5009` |
| `5000` | `ZA=8; ZB4=1` | `ZAZB` = `81` | `5000` → `5009` |
| `5000` | `ZA=8; ZB4=2` | `ZAZB` = `82` | `5000` → `5009` |
| `5000` | `ZA=8; ZB4=3` | `ZAZB` = `83` | `5000` → `5009` |
| `5000` | `ZA=8; ZB4=4` | `ZAZB` = `84` | `5000` → `5009` |
| `5000` | `ZA=8; ZB4=OFF` | `ZAZB` = `OFF` | `5000` → `5009` |
| `5000` | `ZA=9; ZB4=0` | `ZAZB` = `90` | `5000` → `5010` |
| `5000` | `ZA=9; ZB4=1` | `ZAZB` = `91` | `5000` → `5010` |
| `5000` | `ZA=9; ZB4=2` | `ZAZB` = `92` | `5000` → `5010` |
| `5000` | `ZA=9; ZB4=3` | `ZAZB` = `93` | `5000` → `5010` |
| `5000` | `ZA=9; ZB4=4` | `ZAZB` = `94` | `5000` → `5010` |
| `5000` | `ZA=9; ZB4=5` | `ZAZB` = `95` | `5000` → `5010` |
| `5000` | `ZA=9; ZB4=6` | `ZAZB` = `96` | `5000` → `5010` |
| `5000` | `ZA=9; ZB4=7` | `ZAZB` = `97` | `5000` → `5010` |
| `5000` | `ZA=9; ZB4=8` | `ZAZB` = `98` | `5000` → `5010` |
| `5000` | `ZA=9; ZB4=9` | `ZAZB` = `99` | `5000` → `5010` |
| `5000` | `ZA=9; ZB4=OFF` | `ZAZB` = `OFF` | `5000` → `5010` |
| `5001` | `ZB4=1` | `ZAZB` = `1` | `5001` |
| `5001` | `ZB4=2` | `ZAZB` = `2` | `5001` |
| `5001` | `ZB4=3` | `ZAZB` = `3` | `5001` |
| `5001` | `ZB4=4` | `ZAZB` = `4` | `5001` |
| `5001` | `ZB4=5` | `ZAZB` = `5` | `5001` |
| `5001` | `ZB4=6` | `ZAZB` = `6` | `5001` |
| `5001` | `ZB4=7` | `ZAZB` = `7` | `5001` |
| `5001` | `ZB4=8` | `ZAZB` = `8` | `5001` |
| `5001` | `ZB4=9` | `ZAZB` = `9` | `5001` |
| `5001` | `ZB4=OFF` | `ZAZB` = `OFF` | `5001` |
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
| `DIMENSION 1` | Corroborate item model `145` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `171` - 2 pipes fan coil actuator with `ON`-`OFF` valve | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `170` - Temperature control open/close actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `52` - Temperature control pump actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system/model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Use ZA, ZB1..ZB4 and shared N. Four different ZB digits select four separate zones; identical consecutive ZB1/ZB2 and ZB3/ZB4 interlock valve pairs, with C1/C3 opening and C2/C4 closing. All four ZB digits equal selects fan-coil control: C1 valve, C2/C3/C4 low/medium/high fan speed. The sheet says RL1 cannot be excluded, although unused other relays can use `OFF`. It prohibits circulation-pump zone 00 and separate loads in the same zone in physical configuration. A four-pipe fan-coil uses two actuators with separate progressive numbers, their fan-speed contacts paralleled as drawn. Prevent the fan from blowing cold water during heating using a water probe or an immersion thermostat/remote switch as prescribed. Apply the illustrated 10 A breaker. EOS compatibility requires batch 13W06 or later and software configuration.

Apply the exact firmware restrictions above. The generic session/validation method remains in [Programming](../../programming/).

## Source reconciliation

The retained English and Italian exact-product exports both specify four relays; no five-relay rating is supported by these exports. The sheet’s introduction also says two on/off loads, whereas its configuration section and Example 1 explicitly describe four; the detailed mapping is retained with that discrepancy. The physical prohibition on zone 00 contrasts with the database’s version 6.0.0 firmware `13` pump Object `52` candidate (firmware `164` is version 5.0.0 and lacks that direct candidate). That is a source/firmware-scope issue, not permission to configure a physical F430/4 as a pump. Firmware `13` and 164 remain separate applicability rows.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `MyHOME Technical Guide.pdf` | Shared guide: F411U2 PDF pp. 47, 99; F413N pp. 56,100; HVAC pp. 63-68,101; HOMETOUCH pp. 18-20,82; pulse meter p.101. Printed page is PDF page minus 2. Model-name and output-count defects reconciled locally. Source conflicts and limits are reconciled above. |
| `F430-4-italian-product-sheet.pdf` | PDF pp. 1-2: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `ST-00000903-EN.pdf` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `F430-4-publisher-product-sheet.pdf` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `ST-00002703-EN.pdf` | PDF p. 9: exact-reference ecosystem compatibility rows and minimum production batches; other EOS functions and wiring are outside this review. Source conflicts and limits are reconciled above. |

The English export classifies height as 105 mm, while the Italian exact export gives 90 mm; no dimensional revision boundary is established. Its 3.2 W “Output power” classification agrees numerically with the technical sheet’s maximum dissipation, not delivered load power. The Suite function inventory lists a pump role despite the technical sheet’s physical zone-00 prohibition; software family membership does not override that wiring limitation. Broader GUI-MHOME, environmental declaration LGRP-00434-V01.01-EN, linked DWG and listed brochures/catalogues remain unexamined.

### Semantic review findings

Firmware `13` is version 6.0.0/nondefault, 164 is 5.0.0/default: corrected former inverted pump attribution. Both declare four slots and Virgin `519`; direct pump 52 appears only under 13. Added all omitted Virgin-only field surfaces, with admission distinct from physical reachability. Two SUBTYPE filters 675/678 retain the full 16/17 domain. All equal ZB selects fan-coil, overlapping pair equalities select open/close, OFF predicates and empty 4164 have no precedence; firmware slot-2 equality `ZB2=ZB3` differs from the sheet’s illustrated pair `ZB1=ZB2` and `ZB3=ZB4`. Root 6000 retains both ZB1/ZB2 assignments; fan-coil conversion `2001` is a units-only branch even for nonzero ZA, preserved as a discrepancy. No runtime arbitration is inferred. Source prohibits RL1 exclusion and physical zone 00 despite stored OFF/pump candidates and Suite pump listing. Common terminal 1, individual outputs `2..5`, one valve plus three fan speeds, and two-actuator four-pipe drawing are retained. Exact exports both say four relays, correcting the false five-relay export attribution. English height 105 mm versus Italian 90 mm remains unresolved. 3.2 W classification is dissipation-sized, not load power; 10 A protection is not contact rating. Advanced mode is linked only to firmware `13`; no parameter/package associations. All linked broader documents/DWG remain explicit unexamined scopes.

## Evidence limits and open work

Installed firmware support for the version 6 pump candidate, physical/software role boundaries and contact/diagnostic behavior need corroboration.

No installed hardware revision or microcontroller fingerprint is retained for this cluster. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Canonical catalogue extraction and reconciliation are complete for the retained evidence; further documentation discovery, runtime corroboration and final evidence closure remain partial.

Known earlier EOS system editions RA00215AC_I_EN.pdf and ST-00001816-EN.pdf were discovered but not examined in this batch; no earlier-edition capability is transferred. The reviewed EOS compatibility evidence is the 16/06/2026 edition only.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0141-0150-2026-10-06.md#own-dev-0148)
