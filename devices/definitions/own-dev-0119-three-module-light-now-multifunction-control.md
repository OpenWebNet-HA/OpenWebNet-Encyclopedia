# Three-module Light Now multifunction control

## Summary

This three-module Light Now control operates configured lights, dimmers, shutters or scenarios. Its published capacity covers six lighting functions, three shutters or six scenario activations, with selectable key covers and adjustable status LEDs for the chosen arrangement.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0119` | Project identity |
| Technical description | Three-module Light Now multifunction control | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `Y4652M3`, `MX5223`, `AA5223` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `2311` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `145` | Main association; independent of project ID |
| Firmware definition | `871` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `7` | Firmware metadata |
| Categories | Commands, Scenarios, User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Light Now | `Y4652M3` | Established catalogue identity | Manufacturer database commercial record `2667` explicitly links this SKU to item `2311` |
| Legrand - Céliane | `MX5223` | Established catalogue identity | Manufacturer database commercial record `2668` explicitly links this SKU to item `2311` |
| Legrand - Arteor | `AA5223` | Established catalogue identity | Manufacturer database commercial record `2687` explicitly links this SKU to item `2311` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `Y4652M3` | `8005543762271` | [Archived original](https://archive.openwebnet-ha.org/sha256/12/c2/12c2927c49758f9ea1b4eee966f0f137d393e839d59c6961ceddd144e810fbec.pdf), `Y4652M3-publisher-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

### Complete catalogue commercial metadata

| Record | Reference | Catalogue name | Brand key | Line key | Visible | Visibility type | Dependent | Gateway | Catalogue description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `2667` | `Y4652M3` | `Command Device 3M Light Now` | `1` | `22` | `1` |  | `0` | `0` | `Command device 3M Cube` |
| `2668` | `MX5223` | `Command Device 3M Light Now` | `2` | `23` | `1` |  | `0` | `0` | `Command device 3M Eden Park` |
| `2687` | `AA5223` | `Command Device 3M Light Now` | `2` | `11` | `1` |  | `0` | `0` | `Command Device 3M Arteor Advance Slender (Altair elite)` |

Empty catalogue values are retained as empty metadata; none is an installed-state or market-availability observation.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `LE14822AA.pdf` | Instruction Use LE14822AA | `LE14822AA; 07/24-01 PC` | English ratings/instructions, product labels and mounting diagrams inspected on PDF pp. 1-3; other translations not comprehensively reconciled | [Archived original](https://archive.openwebnet-ha.org/sha256/f2/a6/f2a67ce4704cc4ca3ca96ea6fac9885166f363db3f70e5c68ecd21df4750b669.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/LE14822AA.pdf) |
| `ST-00002498-EN.pdf` | Technical Sheet ST-00002498-EN | `ST-00002498-EN; 30/04/2026` | Complete five-page technical sheet: ratings, status/brightness, configuration and physical-mode/address matrix; revision and translation discrepancies explicitly reconciled | [Archived original](https://archive.openwebnet-ha.org/sha256/0d/7a/0d7a5625ed5ff3e6b96a9ecf1984bc97d89fc8f4712e0a5b40e8e08822116a28.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002498-EN.pdf) |
| `Y4652M3-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 04.10.2026` | Complete exact-reference export: commercial/EAN and all classification fields; linked documents inventoried separately, not automatically incorporated | [Archived original](https://archive.openwebnet-ha.org/sha256/12/c2/12c2927c49758f9ea1b4eee966f0f137d393e839d59c6961ceddd144e810fbec.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-Y4652M3&include_technical=1) |
| `ST-00002122-EN.pdf` | System compatibility sheet | `ST-00002122-EN; 21/10/2024` | Classe 300EOS with Netatmo 344845/344885 compatibility: exact Y/MX entries printed/PDF p. 8 and cross-line control entries p. 10. Retained complete 20-page compatibility inventory; other entries do not establish this Device’s diagnostics. | [Archived original](https://archive.openwebnet-ha.org/sha256/e1/a8/e1a8da77199296d9f56ea708402f144b8614473558002c0f8db4ee16eb2f0d0d.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002122-EN.pdf) |
| `Light-Now-2026-2M-catalogue.pdf` | English Light Now commercial catalogue | `AD-EXLHTNW26C/GB/2M; 01/2026` | Y4652M2/Y4652M3 controls and Y4672M2L actuator: printed pp. 84-85, 90 / PDF pp. 86-87, 92. Catalogue inventory reconciled with the exact technical sheets. | [Archived original](https://archive.openwebnet-ha.org/sha256/06/86/06868c27aec52afc42273d4fd94d8a28efdd6c7e0cddcebd5316c45174438dd9.pdf) | [Publisher original](https://www.bticino.com/sites/default/files/2026-02/Light%20Now%20catalogue%202%20MODULES%202026.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `2311` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |
| `ST-00001841-EN.pdf` | Historical exact-family technical sheet | 12/08/2024 | Complete five-page original reconciled with 2026 ST-00002498; physical mode matrix and ratings preserved, suffix-C/group-status revision scope distinguished | [Archived original](https://archive.openwebnet-ha.org/sha256/20/18/2018cab525ab6d40efd4231017ff2d9e0d79f21ecc65b3384809891601bbad1a.pdf) | [Publisher source](https://assets.legrand.com/pim/NP-FT-GT/ST-00001841-EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `18..27 Vdc` | `ST-00002498-EN` printed/PDF pp. 1-5 |
| Standby / maximum draw | `6 mA / 7 mA` | `ST-00002498-EN` printed/PDF pp. 1-5 |
| Operating temperature | `0..40 °C` | `ST-00002498-EN` printed/PDF pp. 1-5 |
| Dimensions | `67.5 x 45 mm; depth 16.5 mm + front 7 mm` | `ST-00002498-EN` printed/PDF pp. 1-5 |
| Published function capacity | `6 lights/dimmers; 3 shutters; 6 scenario activations` | `ST-00002498-EN` printed/PDF pp. 1-5 |
| Covers | `1-module or 2-module covers; ordered separately` | `ST-00002498-EN` printed/PDF pp. 1-5 |
| Y status LEDs | `blue: ON; white: OFF; blue flashing: unconfigured` | `ST-00002498-EN` printed/PDF pp. 1-5 |
| MX status LEDs | `purple: ON; blue: OFF; purple flashing: unconfigured` | `ST-00002498-EN` printed/PDF pp. 1-5 |
| LED brightness cycle | `30%, 0%, 100%, 60% default; changes every 2 s while held` | `ST-00002498-EN` printed/PDF pp. 1-5 |
| Group-light status return | `Production batch >=26W17` | `ST-00002498-EN` printed/PDF pp. 1-5 |

### Publisher export attributes

These are the captured publisher classification values for the named variants. They do not override a technical sheet’s ratings or prove runtime protocol support. A negative radio-bus/connected-object classification is not evidence against separately documented gateway or Wi-Fi behavior.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `Y4652M3` export p. 3 |
| Bus system KNX-RF (Radio Frequency) | `No` | `Y4652M3` export p. 3 |
| Bus system KNX Secure | `No` | `Y4652M3` export p. 3 |
| Bus system KNX Secure-RF (Radio Frequency) | `No` | `Y4652M3` export p. 3 |
| Bus system radio frequency | `No` | `Y4652M3` export p. 3 |
| Bus system LON | `No` | `Y4652M3` export p. 3 |
| Bus system Powernet | `No` | `Y4652M3` export p. 3 |
| Other bus systems | `Other` | `Y4652M3` export p. 3 |
| Radio frequency bidirectional | `No` | `Y4652M3` export p. 3 |
| Mounting method | `Flush-mounted` | `Y4652M3` export p. 3 |
| With anti-theft/dismantling protection | `No` | `Y4652M3` export p. 3 |
| With bus connection | `Yes` | `Y4652M3` export p. 3 |
| Number of actuation points | `6` | `Y4652M3` export p. 3 |
| Number of buttons | `3` | `Y4652M3` export p. 3 |
| With LED indication | `Yes` | `Y4652M3` export p. 3 |
| With label area | `No` | `Y4652M3` export p. 3 |
| With display | `No` | `Y4652M3` export p. 3 |
| Material | `Plastic` | `Y4652M3` export p. 3 |
| Material quality | `Thermoplastic` | `Y4652M3` export p. 3 |
| Surface protection | `Untreated` | `Y4652M3` export p. 3 |
| Surface finishing | `Matt` | `Y4652M3` export p. 3 |
| Colour | `Black` | `Y4652M3` export p. 3 |
| RAL-number (similar) | `9011` | `Y4652M3` export p. 3 |
| Transparent | `No` | `Y4652M3` export p. 3 |
| With room temperature controller | `No` | `Y4652M3` export p. 3 |
| With IR sensor | `No` | `Y4652M3` export p. 3 |
| Degree of protection (IP) | `IP20` | `Y4652M3` export p. 3 |
| Min. depth of built-in installation box | `55 mm` | `Y4652M3` export p. 3 |
| Width | `66 mm` | `Y4652M3` export p. 3 |
| Height | `45 mm` | `Y4652M3` export p. 3 |
| Depth | `24 mm` | `Y4652M3` export p. 3 |
| Built-in depth | `45 mm` | `Y4652M3` export p. 3 |
| degree of impact strength (IK) | `IK04` | `Y4652M3` export p. 3 |
| Operating / setting temperature (Min-Max) | `-5-35 °C` | `Y4652M3` export p. 3 |
| Storage temperature (Min-Max) | `-10-70 °C` | `Y4652M3` export p. 4 |
| Frequency (Min-Max) | `50-60 Hz` | `Y4652M3` export p. 4 |
| Terminal marking indication | `Yes` | `Y4652M3` export p. 4 |
| Antimicrobial treatment | `No` | `Y4652M3` export p. 4 |
| Terminals capacity (Min-Max) | `0.34-2.5 mm²` | `Y4652M3` export p. 4 |
| Cable nature for connection | `Flexible or rigid` | `Y4652M3` export p. 4 |
| Label space/information surface | `No` | `Y4652M3` export p. 4 |
| Addressable | `Yes` | `Y4652M3` export p. 4 |
| Contains Batteries | `No` | `Y4652M3` export p. 4 |
| Connected object | `No` | `Y4652M3` export p. 4 |
| Programmable | `Yes` | `Y4652M3` export p. 4 |
| Interoperable connection Protocol | `Yes` | `Y4652M3` export p. 4 |
| Connectable by Internet box | `No` | `Y4652M3` export p. 4 |
| Product use function | `Lighting management` | `Y4652M3` export p. 4 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2311` | Canonical catalogue |
| Technical item description | Command Device 3M Light Now | Canonical catalogue |
| Item family | 0; key `1` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `145` | `AS_ITEM_SYSTEM` |
| Commercial record count | `3` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `145` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `871` | `1` | `0` | No build row | `7` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `871` | `1` | `410` Light control | Fixed/designated metadata | `4356` | `410` | `1964` |
| `871` | `1` | `411` Automation control | Candidate alternative | `3924` | `411` | `1849` |
| `871` | `1` | `412` Lock/unlock actuator control | Candidate alternative | `3930` | `412` | `1850` |
| `871` | `1` | `416` Scheduled scenario PLUS | Candidate alternative | `3936` | `416` | `1851` |
| `871` | `1` | `418` Open lock control | Candidate alternative | `3942` | `418` | `1852` |
| `871` | `1` | `426` Staircase light control | Candidate alternative | `3948` | `426` | `1853` |
| `871` | `1` | `427` Floor call control | Candidate alternative | `3954` | `427` | `1854` |
| `871` | `1` | `463` Load control actuator visualization | Candidate alternative | `3960` | `492` | `1855` |
| `871` | `2` | `410` Light control | Fixed/designated metadata | `4357` | `410` | `1964` |
| `871` | `2` | `411` Automation control | Candidate alternative | `3925` | `411` | `1849` |
| `871` | `2` | `412` Lock/unlock actuator control | Candidate alternative | `3931` | `412` | `1850` |
| `871` | `2` | `416` Scheduled scenario PLUS | Candidate alternative | `3937` | `416` | `1851` |
| `871` | `2` | `418` Open lock control | Candidate alternative | `3943` | `418` | `1852` |
| `871` | `2` | `426` Staircase light control | Candidate alternative | `3949` | `426` | `1853` |
| `871` | `2` | `427` Floor call control | Candidate alternative | `3955` | `427` | `1854` |
| `871` | `2` | `463` Load control actuator visualization | Candidate alternative | `3961` | `492` | `1855` |
| `871` | `2` | `174` Shutter control (3 slots) | Candidate alternative | `3916` | `665` | `1847` |
| `871` | `3` | `410` Light control | Fixed/designated metadata | `4358` | `410` | `1964` |
| `871` | `3` | `411` Automation control | Candidate alternative | `3926` | `411` | `1849` |
| `871` | `3` | `412` Lock/unlock actuator control | Candidate alternative | `3932` | `412` | `1850` |
| `871` | `3` | `416` Scheduled scenario PLUS | Candidate alternative | `3938` | `416` | `1851` |
| `871` | `3` | `418` Open lock control | Candidate alternative | `3944` | `418` | `1852` |
| `871` | `3` | `426` Staircase light control | Candidate alternative | `3950` | `426` | `1853` |
| `871` | `3` | `427` Floor call control | Candidate alternative | `3956` | `427` | `1854` |
| `871` | `3` | `463` Load control actuator visualization | Candidate alternative | `3962` | `492` | `1855` |
| `871` | `4` | `410` Light control | Fixed/designated metadata | `4359` | `410` | `1964` |
| `871` | `4` | `411` Automation control | Candidate alternative | `3927` | `411` | `1849` |
| `871` | `4` | `412` Lock/unlock actuator control | Candidate alternative | `3933` | `412` | `1850` |
| `871` | `4` | `416` Scheduled scenario PLUS | Candidate alternative | `3939` | `416` | `1851` |
| `871` | `4` | `418` Open lock control | Candidate alternative | `3945` | `418` | `1852` |
| `871` | `4` | `426` Staircase light control | Candidate alternative | `3951` | `426` | `1853` |
| `871` | `4` | `427` Floor call control | Candidate alternative | `3957` | `427` | `1854` |
| `871` | `4` | `463` Load control actuator visualization | Candidate alternative | `3963` | `492` | `1855` |
| `871` | `4` | `174` Shutter control (3 slots) | Candidate alternative | `3917` | `665` | `1847` |
| `871` | `5` | `410` Light control | Fixed/designated metadata | `4360` | `410` | `1964` |
| `871` | `5` | `411` Automation control | Candidate alternative | `3928` | `411` | `1849` |
| `871` | `5` | `412` Lock/unlock actuator control | Candidate alternative | `3934` | `412` | `1850` |
| `871` | `5` | `416` Scheduled scenario PLUS | Candidate alternative | `3940` | `416` | `1851` |
| `871` | `5` | `418` Open lock control | Candidate alternative | `3946` | `418` | `1852` |
| `871` | `5` | `426` Staircase light control | Candidate alternative | `3952` | `426` | `1853` |
| `871` | `5` | `427` Floor call control | Candidate alternative | `3958` | `427` | `1854` |
| `871` | `5` | `463` Load control actuator visualization | Candidate alternative | `3964` | `492` | `1855` |
| `871` | `6` | `410` Light control | Fixed/designated metadata | `4361` | `410` | `1964` |
| `871` | `6` | `411` Automation control | Candidate alternative | `3929` | `411` | `1849` |
| `871` | `6` | `412` Lock/unlock actuator control | Candidate alternative | `3935` | `412` | `1850` |
| `871` | `6` | `416` Scheduled scenario PLUS | Candidate alternative | `3941` | `416` | `1851` |
| `871` | `6` | `418` Open lock control | Candidate alternative | `3947` | `418` | `1852` |
| `871` | `6` | `426` Staircase light control | Candidate alternative | `3953` | `426` | `1853` |
| `871` | `6` | `427` Floor call control | Candidate alternative | `3959` | `427` | `1854` |
| `871` | `6` | `463` Load control actuator visualization | Candidate alternative | `3965` | `492` | `1855` |
| `871` | `7` | `143` User interface settings for command | Fixed/designated metadata | `3915` | `644` | `1846` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `871` | `521` Soft-Touch command virgin | `1`, `2`, `3`, `4`, `5`, `6` | `410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `418`, `419`, `421`, `426`, `427`, `462` | `521` | `158` |

The active firmware has six command Modules and a seventh Module for the user-interface Object; the six command slots correspond to the published three-zone control functions.

## Configuration modes

### Published three-control physical mode matrix

ST-00002498-EN printed/PDF p. 5, Table A. The common physical selector chooses this combination; independent virtual command roles use the catalogue surfaces above.

| Physical M | Left A1/PL1 | Centre A2/PL2 | Right A3/PL3 |
| --- | --- | --- | --- |
| `0` | cyclic | cyclic | cyclic |
| `1` | cyclic | cyclic | bistable shutter |
| `2` | cyclic | bistable shutter | bistable shutter |
| `3` | bistable shutter | bistable shutter | bistable shutter |
| `4` | cyclic | cyclic | monostable shutter |
| `5` | cyclic | monostable shutter | monostable shutter |
| `6` | monostable shutter | monostable shutter | monostable shutter |
| `7` | cyclic | cyclic | floor call |
| `8` | cyclic | door lock | staircase lights |
| `9` | upper `ON`/lower `OFF` | upper `ON`/lower `OFF` | upper `ON`/lower `OFF` |

### Complete catalogue mode and connection associations

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `871` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `871` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `410` - Light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `1` = Timed `ON`; `2` = Toggle dimmer; `4` = Toggle `ON/OFF`; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `20` = `ON` and point to point dimmer; `21` = `OFF` and point to point dimmer; `22` = `ON` and Dimmer; `23` = `OFF` and Dimmer; `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90%; `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `131` = Customized toggle dimmer; `133` = Customized toggle dimmer without regulation; `135` = Customized `ON` and dimmer without regulation; `136` = Customized `OFF` and dimmer without regulation; `137` = Customized `ON` and dimmer with regulation; `138` = Customized `OFF` and dimmer with regulation | `0` | Modality; Mode (MODE+`ON/OFF`) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `HOURS` | `0..255` | `0` | Hours; Only for `MOD=128` |
| `MINUTES` | `0..59` | `0` | Minutes; Only for `MOD=128` |
| `SECONDS` | `0..59` | `30` | Seconds; Only for `MOD=128` |
| `LEVEL` | `0..100` | `100` | Level; Only for `MOD=129`, 131, 133, 135, 136, 137, 138 |
| `START_S` | `0..255` | `255` | Soft start speed; Only for `MOD=129`, 131, 133, 135, 136, 137, 138 |
| `STOP_S` | `0..255` | `255` | Soft stop speed; Only for `MOD=129`, 131, 133, 135, 136, 137, 138 |
| `DIMMING_S` | `0..255` | `255` | Dimming speed; Only for `MOD=129`, 131 |
| `T_TIME` | `1` = 1 min; `2` = 2 min; `3` = 3 min; `4` = 4 min; `5` = 5 min; `6` = 15 min; `7` = 30 s; `8` = 0.5 s; `9` = 2 s; `10` = 10 min | `1` | Tabled time; Only for `MOD=1` |

### Object `411` - Automation control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = UP bistable control; `1` = DOWN bistable control; `2` = UP monostable control; `3` = DOWN monostable control; `4` = UP monostable and bistable control; `5` = DOWN monostable and bistable control | `0` | Modality; mode (`UP/DOWN`) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `412` - Lock/unlock actuator control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `1` = Disable; `2` = Enable | `1` | Modality; mode (D/E) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `416` - Scheduled scenario PLUS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | `0..255` | `1` | Scheduled scenario PLUS number |
| `PPT_CEN_HIG` | `0..7` | `0` | Scheduled scenario PLUS number |
| `BUTTON_1` | `0..31` | `1` | Button |
| `MODE` | `0` = Press/release only; `1` = Press/hold/release | `0` | Modality; Mode (Lighting management) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `418` - Open lock control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same level; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Level |

### Object `426` - Staircase light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |

### Object `427` - Floor call control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `TO_ALL` | `0` = Point to point; `1` = General | `1` | Type of call |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
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

### Object `174` - Shutter control (3 slots)

Catalogue Object key `665` maps to external Object `174`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Bistable control; `1` = Monostable control; `2` = Blades control and bistable; `3` = Bistable and blades control | `0` | Modality; Mode (0,1,2,3) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..10` | `0` | Area; See Automation System Addressing |
| `PL` | `0..15` | `0` | Light point; See Automation System Addressing |
| `G1` | `1..255` | `1` | Group 1; See Automation System Addressing |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level; See Automation System Addressing |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `15` = Local bus 15; `16` = All systems | `0` | Destination level; See Automation System Addressing |
| `A_R` | `0..10` | `0` | Area of reference actuator |
| `PL_R` | `0..15` | `0` | Light point of reference actuator |
| `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety | `1` | Priority; Shutter management command priority |
| `PRE` | `1..9`; `0` = None | `0` | Preset; Shutter management preset number |

### Virgin-only reusable capability

The following Objects are permitted by an associated Virgin Object but lack a direct Object/Firmware relationship for this Device. Their reusable definitions are inventoried for completeness; they are not a declaration of active placements or supported values on this Firmware.

### Object `413` - Scenario module control (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Scenario activation and modification; `1` = Scenario activation | `0` | Modality |
| `APL` | `0..175`; area `floor(APL/16)`, light point `APL mod 16` | `0` | Scenario module address |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15 | `0` | Destination level; Destination level (`0..15`) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `SCE_BUTT_1` | `1..16` | `1` | Scenario number |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay of scenario number |

### Object `414` - Scheduled scenario (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `CEN_BUTT_1` | `0..31` | `1` | Button |
| `MODE` | `0` = Press/release only; `1` = Press/hold/release | `0` | Modality; Mode (Lighting management) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `415` - Scenario PLUS Lighting Management (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = `ON`; `1` = `OFF`; `2` = `ON` with regulation; `3` = `OFF` with regulation | `0` | Modality; Mode (`ON/OFF` regulation) |
| `PPT_SCE_1` | `0..255` | `1` | Upper button scenario |
| `TYPE_OF_REGULATION` | `0` = Regulate all; `1` = Lights only; `2` = Shutters only; `3` = Stereo amplifiers only | `0` | Regulation type |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for upper button |

### Object `417` - `AUX` control (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Cyclical; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `17` = DOWN Shutter bistable command; `18` = UP shutter monostable command; `4` = Reset `BI`; `5` = Reset `TRI`; `6` = Reset `GEN`; `1` = Disable; `2` = Enable; `16` = UP shutter bistable command; `19` = DOWN Shutter monostable command | `0` | Modality; mode(Cyclical,off,on,pul,up,down,...) |
| `OUT_AUX_CH` | `1..15` | `1` | `AUX` channel |
| `TYPE_CONTACT` | No legal values specified in source | `0` | Contact type |

### Object `419` - Sound diffusion control (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = `ON`/volume +; `1` = `OFF`/volume -; `2` = Change track; `3` = Switch source; `4` = Toggle `ON/OFF` | `0` | Modality; Mode (VOL,ON_OFF) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..9` | `0` | Area |
| `PF` | `0..9` | `0` | Audio point |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `IS_FOLLOW_ME` | `0` = No; `1` = Yes | `1` | Follow me |
| `SOURCE` | `1..9` | `1` | Source |
| `SUB_SOURCE` | `0..255` | `0` | Sub source |
| `CHANNEL` | `0` = Base Band; `1` = Left; `2` = Right; `3` = Stereo; `8` = Base Band and Video; `9` = Left and video; `10` = Right and video; `11` = Left and video | `3` | Channel (BB-Stereo) |

### Object `421` - Cyclic autoswitch control (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |

### Object `462` - Open lock command on session (Virgin-only)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |

### Object `413` - Scenario module control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Scenario activation and modification; `1` = Scenario activation | `0` | Modality |
| `APL` | `0` = `A=0` `PL=0`; `1` = `A=0` `PL=1`; `2` = `A=0` `PL=2`; `3` = `A=0` `PL=3`; `4` = `A=0` `PL=4`; `5` = `A=0` `PL=5`; `6` = `A=0` `PL=6`; `7` = `A=0` `PL=7`; `8` = `A=0` `PL=8`; `9` = `A=0` `PL=9`; `10` = `A=0` `PL=10`; `11` = `A=0` `PL=11`; `12` = `A=0` `PL=12`; `13` = `A=0` `PL=13`; `14` = `A=0` `PL=14`; `15` = `A=0` `PL=15`; `16` = `A=1` `PL=0`; `17` = `A=1` `PL=1`; `18` = `A=1` `PL=2`; `19` = `A=1` `PL=3`; `20` = `A=1` `PL=4`; `21` = `A=1` `PL=5`; `22` = `A=1` `PL=6`; `23` = `A=1` `PL=7`; `24` = `A=1` `PL=8`; `25` = `A=1` `PL=9`; `26` = `A=1` `PL=10`; `27` = `A=1` `PL=11`; `28` = `A=1` `PL=12`; `29` = `A=1` `PL=13`; `30` = `A=1` `PL=14`; `31` = `A=1` `PL=15`; `32` = `A=2` `PL=0`; `33` = `A=2` `PL=1`; `34` = `A=2` `PL=2`; `35` = `A=2` `PL=3`; `36` = `A=2` `PL=4`; `37` = `A=2` `PL=5`; `38` = `A=2` `PL=6`; `39` = `A=2` `PL=7`; `40` = `A=2` `PL=8`; `41` = `A=2` `PL=9`; `42` = `A=2` `PL=10`; `43` = `A=2` `PL=11`; `44` = `A=2` `PL=12`; `45` = `A=2` `PL=13`; `46` = `A=2` `PL=14`; `47` = `A=2` `PL=15`; `48` = `A=3` `PL=0`; `49` = `A=3` `PL=1`; `50` = `A=3` `PL=2`; `51` = `A=3` `PL=3`; `52` = `A=3` `PL=4`; `53` = `A=3` `PL=5`; `54` = `A=3` `PL=6`; `55` = `A=3` `PL=7`; `56` = `A=3` `PL=8`; `57` = `A=3` `PL=9`; `58` = `A=3` `PL=10`; `59` = `A=3` `PL=11`; `60` = `A=3` `PL=12`; `61` = `A=3` `PL=13`; `62` = `A=3` `PL=14`; `63` = `A=3` `PL=15`; `64` = `A=4` `PL=0`; `65` = `A=4` `PL=1`; `66` = `A=4` `PL=2`; `67` = `A=4` `PL=3`; `68` = `A=4` `PL=4`; `69` = `A=4` `PL=5`; `70` = `A=4` `PL=6`; `71` = `A=4` `PL=7`; `72` = `A=4` `PL=8`; `73` = `A=4` `PL=9`; `74` = `A=4` `PL=10`; `75` = `A=4` `PL=11`; `76` = `A=4` `PL=12`; `77` = `A=4` `PL=13`; `78` = `A=4` `PL=14`; `79` = `A=4` `PL=15`; `80` = `A=5` `PL=0`; `81` = `A=5` `PL=1`; `82` = `A=5` `PL=2`; `83` = `A=5` `PL=3`; `84` = `A=5` `PL=4`; `85` = `A=5` `PL=5`; `86` = `A=5` `PL=6`; `87` = `A=5` `PL=7`; `88` = `A=5` `PL=8`; `89` = `A=5` `PL=9`; `90` = `A=5` `PL=10`; `91` = `A=5` `PL=11`; `92` = `A=5` `PL=12`; `93` = `A=5` `PL=13`; `94` = `A=5` `PL=14`; `95` = `A=5` `PL=15`; `96` = `A=6` `PL=0`; `97` = `A=6` `PL=1`; `98` = `A=6` `PL=2`; `99` = `A=6` `PL=3`; `100` = `A=6` `PL=4`; `101` = `A=6` `PL=5`; `102` = `A=6` `PL=6`; `103` = `A=6` `PL=7`; `104` = `A=6` `PL=8`; `105` = `A=6` `PL=9`; `106` = `A=6` `PL=10`; `107` = `A=6` `PL=11`; `108` = `A=6` `PL=12`; `109` = `A=6` `PL=13`; `110` = `A=6` `PL=14`; `111` = `A=6` `PL=15`; `112` = `A=7` `PL=0`; `113` = `A=7` `PL=1`; `114` = `A=7` `PL=2`; `115` = `A=7` `PL=3`; `116` = `A=7` `PL=4`; `117` = `A=7` `PL=5`; `118` = `A=7` `PL=6`; `119` = `A=7` `PL=7`; `120` = `A=7` `PL=8`; `121` = `A=7` `PL=9`; `122` = `A=7` `PL=10`; `123` = `A=7` `PL=11`; `124` = `A=7` `PL=12`; `125` = `A=7` `PL=13`; `126` = `A=7` `PL=14`; `127` = `A=7` `PL=15`; `128` = `A=8` `PL=0`; `129` = `A=8` `PL=1`; `130` = `A=8` `PL=2`; `131` = `A=8` `PL=3`; `132` = `A=8` `PL=4`; `133` = `A=8` `PL=5`; `134` = `A=8` `PL=6`; `135` = `A=8` `PL=7`; `136` = `A=8` `PL=8`; `137` = `A=8` `PL=9`; `138` = `A=8` `PL=10`; `139` = `A=8` `PL=11`; `140` = `A=8` `PL=12`; `141` = `A=8` `PL=13`; `142` = `A=8` `PL=14`; `143` = `A=8` `PL=15`; `144` = `A=9` `PL=0`; `145` = `A=9` `PL=1`; `146` = `A=9` `PL=2`; `147` = `A=9` `PL=3`; `148` = `A=9` `PL=4`; `149` = `A=9` `PL=5`; `150` = `A=9` `PL=6`; `151` = `A=9` `PL=7`; `152` = `A=9` `PL=8`; `153` = `A=9` `PL=9`; `154` = `A=9` `PL=10`; `155` = `A=9` `PL=11`; `156` = `A=9` `PL=12`; `157` = `A=9` `PL=13`; `158` = `A=9` `PL=14`; `159` = `A=9` `PL=15`; `160` = `A=10` `PL=0`; `161` = `A=10` `PL=1`; `162` = `A=10` `PL=2`; `163` = `A=10` `PL=3`; `164` = `A=10` `PL=4`; `165` = `A=10` `PL=5`; `166` = `A=10` `PL=6`; `167` = `A=10` `PL=7`; `168` = `A=10` `PL=8`; `169` = `A=10` `PL=9`; `170` = `A=10` `PL=10`; `171` = `A=10` `PL=11`; `172` = `A=10` `PL=12`; `173` = `A=10` `PL=13`; `174` = `A=10` `PL=14`; `175` = `A=10` `PL=15` | `0` | Scenario module address |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15 | `0` | Destination level; Destination level (`0..15`) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `SCE_BUTT_1` | `1..16` | `1` | Scenario number |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay of scenario number |

### Object `414` - Scheduled scenario (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `CEN_BUTT_1` | `0..31` | `1` | Button |
| `MODE` | `0` = Press/release only; `1` = Press/hold/release | `0` | Modality; Mode (Lighting management) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `415` - Scenario PLUS Lighting Management (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = `ON`; `1` = `OFF`; `2` = `ON` with regulation; `3` = `OFF` with regulation | `0` | Modality; Mode (`ON/OFF` regulation) |
| `PPT_SCE_1` | `0..255` | `1` | Upper button scenario |
| `TYPE_OF_REGULATION` | `0` = Regulate all; `1` = Lights only; `2` = Shutters only; `3` = Stereo amplifiers only | `0` | Regulation type |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for upper button |

### Object `417` - AUX control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Cyclical; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `17` = DOWN Shutter bistable command; `18` = UP shutter monostable command; `4` = Reset `BI`; `5` = Reset `TRI`; `6` = Reset `GEN`; `1` = Disable; `2` = Enable; `16` = UP shutter bistable command; `19` = DOWN Shutter monostable command | `0` | Modality; mode(Cyclical,off,on,pul,up,down,...) |
| `OUT_AUX_CH` | `1..15` | `1` | AUX channel |
| `TYPE_CONTACT` | No legal values specified in source | `0` | Contact type |

### Object `419` - Sound diffusion control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = `ON`/volume +; `1` = `OFF`/volume -; `2` = Change track; `3` = Switch source; `4` = Toggle `ON/OFF` | `0` | Modality; Mode (VOL,ON_OFF) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `3` = General | `0` | Addressing type |
| `A` | `0..9` | `0` | Area |
| `PF` | `0..9` | `0` | Audio point |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `IS_FOLLOW_ME` | `0` = No; `1` = Yes | `1` | Follow me |
| `SOURCE` | `1..9` | `1` | Source |
| `SUB_SOURCE` | `0..255` | `0` | Sub source |
| `CHANNEL` | `0` = Base Band; `1` = Left; `2` = Right; `3` = Stereo; `8` = Base Band and Video; `9` = Left and video; `10` = Right and video; `11` = Left and video | `3` | Channel (BB-Stereo) |

### Object `421` - Cyclic autoswitch control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |

### Object `462` - Open lock command on session (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |

### Semantic review findings

Six command positions plus UI Object `143` account for seven logical Modules. Three-slot Object `174` starts at slots `2` or `4` only, with no implicit placement or overlap precedence. Seven Virgin-only candidates add 32 reusable fields. The firmware stores AID only and an Advanced Configuration association; the published shared physical M selector and three address pairs are a different source scope. The full ten-row physical-mode matrix is preserved; independent physical roles cannot be freely assigned beyond that matrix.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `871` | `143` | `4087` | `ENABLE_DISABLE_LED_COMMAND` | `0` = All Led Enabled; `1` = Presence Led Enabled - State Update Led Disable; `2` = Presence Led Disable - State Update Led Enable; `3` = All Led Disable (entire reusable range retained) | `0` | Enable-Disable LED |
| `871` | `143` | `4088` | `PRESENCE_LED_INTENSITY_LEVEL_COMMAND` | `0` = Standard level; `1` = High intensity level (entire reusable range retained) | `0` | Presence LED intensity level |
| `871` | `174` | `4090` | `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety (entire reusable range retained) | `1` | Priority |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

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
| `143` - User interface settings for command | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `174` - Shutter control (3 slots) | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `411` - Automation control | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `412` - Lock/unlock actuator control | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `416` - Scheduled scenario PLUS | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `418` - Open lock control | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `426` - Staircase light control | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `427` - Floor call control | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `463` - Load control actuator visualization | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |
| `410` - Light control | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |

These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Configure the addressing and role of each command independently in Home+Project. Physical configuration remains supported. The LED button adjusts brightness after configuration; retain the rear safety/sealing cap. Physical point-to-point addressing uses room/light-point digits `1..9`; room, group and general use `AMB`, `GR`, `GEN`. Short light presses switch; long presses regulate only in point-to-point adjustment modes. Door-lock, floor-call and staircase controls use the target’s two-digit address. Runtime group status return requires the published production qualification, independently of the catalogue field domains.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

## Source reconciliation

The manufacturer database establishes Y, MX and AA identities. Current shared sheets explicitly cover Y and MX, including MX suffix-C variants outside this database cluster. Published MX products are Céliane; the database’s line label “Eden Park” is retained as conflicting source terminology, not presented as the marketed line. AA references are established Legrand - Arteor catalogue identities; exact AA physical ratings and commissioning documents were not found. Publisher exports have their own classification, dimensions and temperature entries; these are preserved below and are not silently substituted for the shared technical sheet. Physical wiring-device modules, command capacity, Firmware Modules and the separate UI Object are distinct counts.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `LE14822AA.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `ST-00002498-EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `Y4652M3-publisher-product-sheet.pdf` | Captured exact-variant identity and complete technical classification attributes tabulated above; document links are discovery provenance, not additional independently verified capability. |
| `ST-00002122-EN.pdf` | Classe 300EOS with Netatmo compatibility p. 8 excludes physically configured devices; p. 10 lists exact multifunction controls, but not Y4672M2L/MX5230 cross-line commissioning. |
| `Light-Now-2026-2M-catalogue.pdf` | Exact Y references and function/cover inventory: printed pp. 84-85, 90 / PDF pp. 86-87, 92. Commercial catalogue does not replace firmware domains. |
| `ST-00001841-EN.pdf` | Complete five-page original reconciled with 2026 ST-00002498; physical mode matrix and ratings preserved, suffix-C/group-status revision scope distinguished |

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Server and configuration boundary | The exact Y/MX references are listed on p. 8 for Classe 300EOS with Netatmo, with physically configured devices explicitly excluded. Page 10 lists Y4652M2/MX5222 and Y4652M3/MX5223 for cross-line control; this is source-scoped commissioning compatibility, not universal installed protocol support. | `ST-00002122-EN` pp. 8, 10 |

| Property | Value | Evidence |
| --- | --- | --- |
| Dimensions and temperature | Export width `66 mm`, depth `24 mm`, built-in depth `45 mm`, operating `-5..35 °C`; technical sheet width `67.5 mm`, component depths `16.5+7 mm`, operating `0..40 °C`. Different scopes are retained; no universal replacement value chosen | Y4652M3 export p. 3; `ST-00002498-EN` p. 1 |
| Production scope | 2026 sheet adds suffix-C and group status from `26W17`; 2024 English sheet does not establish that feature for earlier production | `ST-00001841-EN` and `ST-00002498-EN` pp. 1, 3-5 |

## Evidence limits and open work

Exact AA documentation, suffix-C equivalence to the historical catalogue firmware, group status behavior across production batches, and active Object/diagnostic captures remain missing.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

Publisher-linked `BRO-LHNOW2M`, `BRO-LHNOW3M`, `CAT-LHNOW3M` and `PRE-LHNOW` have not all been independently examined. The retained two-module catalogue and technical sheets support only their stated page/revision scopes. Mounting leaflets were examined for English instructions, labels and diagrams; additional translations remain unexamined.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0111-0120-2026-10-06.md#own-dev-0119)
