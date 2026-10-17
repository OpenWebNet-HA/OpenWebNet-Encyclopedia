# Living Now K8002S shutter actuator

## Summary

K8002S is a one-module Living Now shutter actuator with two interlocked relay outputs. It supports a calibrated shutter position and, with a separate Full digital control, a stored preset in addition to up / down operation. The preset’s blade-adjustment behavior is guaranteed only with a pulse motor.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0206` | Project identity |
| Technical description | Living Now K8002S shutter actuator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `K8002S` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `2275` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `120` | Main association; independent of project ID |
| Firmware definition | `805` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Actuators | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Living Now | `K8002S` | Established catalogue identity | Manufacturer database commercial record `2634` explicitly links this SKU to item `2275` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `K8002S` | `8005543640142` | [K8002S-publisher-product-sheet.pdf](https://archive.openwebnet-ha.org/sha256/14/79/1479e87008eabea95c7929012df4668a4dc2314d731461257349767c670e6a1e.pdf) PDF p. 1; `K8002S-italian-product-sheet.pdf` PDF p. 1 |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `K8002S` | Shutter Actuator Living Now advanced | Canonical commercial record `2634` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MyHOME Technical Guide.pdf` | Installation Guide GUI-MHOME | `AD-EXMH25GT; printed version 6/2025, rear cover` | Printed/PDF pp. 50, 53, 84: exact K8002 role, shared actuator context and catalogue entry; other product specifications excluded. | [Archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MyHOME%20Technical%20Guide.pdf) |
| `ST-00002701-REV2-EN.pdf` | Technical Sheet ST-00002701-REV2-EN | `ST-00002701-REV2-EN; 16/06/2026` | Printed/PDF pp. 3: exact-reference F460 compatibility only; electrical ratings belong to F460, not this Device. | [Archived original](https://archive.openwebnet-ha.org/sha256/78/ae/78ae843060334dbd6d065284c0e5144469d8629633b519585b8daec14deacdc6.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002701-REV2-EN.pdf) |
| `ST-00002702-REV2-EN.pdf` | Technical Sheet ST-00002702-REV2-EN | `ST-00002702-REV2-EN; 16/06/2026` | Printed/PDF pp. 2: exact-reference F461 compatibility only; electrical ratings belong to F461, not this Device. | [Archived original](https://archive.openwebnet-ha.org/sha256/26/c4/26c407274fdd72d4c0269d84f045ca21cc1beb9e8f26ca64d4de005c0026a662.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002702-REV2-EN.pdf) |
| `LE11286AC.pdf` | Instruction Use LE11286AC | `LE11286AC; 10/20-01 PC` | Printed/PDF pp. 1-4: exact-reference specification, connection and configuration content; shared-product content separately scoped. | [Archived original](https://archive.openwebnet-ha.org/sha256/7b/40/7b40940e721db538467ca4717cbd396b1e24bb33b2d318d2f838312f1f7be27c.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/LE11286AC.pdf) |
| `ST-00001900-EN.pdf` | Technical Sheet ST-00001900-EN | `ST-00001900-EN; 01/10/2024` | Printed/PDF pp. 1-2: exact-reference specification, connection and configuration content; shared-product content separately scoped. | [Archived original](https://archive.openwebnet-ha.org/sha256/b0/2a/b02a369f119d2f320282bf8754194efe669dd53c2c0d3dadaa3d3cdf3c4d80d2.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00001900-EN.pdf) |
| `K8002S-publisher-product-sheet.pdf` | Exact English product export | `Publisher export retrieved 05.10.2026; Italian compliance dates are boilerplate` | PDF pp. 1-3: exact-reference commercial record, EAN and classification values; no printed page sequence established; linked resources are separately accounted for. | [Archived original](https://archive.openwebnet-ha.org/sha256/14/79/1479e87008eabea95c7929012df4668a4dc2314d731461257349767c670e6a1e.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-K8002S&include_technical=1) |
| `K8002S-italian-product-sheet.pdf` | Exact Italian product export | `Publisher export retrieved 05.10.2026; Italian compliance dates are boilerplate` | PDF pp. 1-1: exact-reference commercial record, EAN and classification values; no printed page sequence established; linked resources are separately accounted for. | [Archived original](https://archive.openwebnet-ha.org/sha256/49/75/4975ffd659e2354c7aaaade3fb595baf8ad3687b7c359d43f1f02b05f1f687f7.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-K8002S) |
| `ST_00000540_IT.pdf` | Italian manufacturer technical document | `ST_00000540_IT; 26/02/2020` | Printed/PDF pp. 1-2: exact-reference specification, connection and configuration content; shared-product content separately scoped. | [Archived original](https://archive.openwebnet-ha.org/sha256/bd/db/bddb8e898125b27b671456b0c2b10af76e5b4b7b288e24f44a412f11efd85a45.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/ST_00000540_IT.pdf) |
| `MyHOME-2025-Italian-guide.pdf` | MyHOME 2025 Italian guide | `AD-ITMH25GT; Edizione 04/2025, printed cover` | Printed/PDF pp. 52, 56, 136: exact K8002 role, shared actuator context and catalogue entry; Edizione 04/2025 established from the printed cover. | [Archived original](https://archive.openwebnet-ha.org/sha256/0d/f6/0df6729969f31f61feb275e84c7da84c665f8c93aeb1d5af9ba1ac29d4f82e4e.pdf) | [Publisher original](https://professionisti.bticino.it/sites/default/files/2025-03/MyHOME%20AD-ITMH25GT_smart_new.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2275`: complete retained canonical associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply / draw | `18–27 Vdc; 5 mA standby; 17 mA maximum with interlock` | `ST-00001900-EN.pdf` printed/PDF pp. 1-2; `ST_00000540_IT.pdf` pp. 1-2; `LE11286AC.pdf` pp. 1-4 |
| Outputs / load-part voltage | `2 × 2 A maximum; maximum applicable voltage 250 V` | `ST-00001900-EN.pdf` printed/PDF pp. 1-2; `ST_00000540_IT.pdf` pp. 1-2; `LE11286AC.pdf` pp. 1-4 |
| Operating temperature / size | `0–40 °C / 1 flush-mounted module` | `ST-00001900-EN.pdf` printed/PDF pp. 1-2; `ST_00000540_IT.pdf` pp. 1-2; `LE11286AC.pdf` pp. 1-4 |
| Motor loads | `460 W at 230 Vac; 250 W at 110 Vac, as printed` | `ST-00001900-EN.pdf` printed/PDF pp. 1-2; `ST_00000540_IT.pdf` pp. 1-2; `LE11286AC.pdf` pp. 1-4 |
| Connections | `Clips to connection module for SCS; 2 × 2.5 mm² phase, neutral and load terminals` | `ST-00001900-EN.pdf` printed/PDF pp. 1-2; `ST_00000540_IT.pdf` pp. 1-2; `LE11286AC.pdf` pp. 1-4 |
| Local buttons | `Actuator test only; not a substitute for the digital user control` | `ST-00001900-EN.pdf` printed/PDF pp. 1-2; `ST_00000540_IT.pdf` pp. 1-2; `LE11286AC.pdf` pp. 1-4 |
| Status LEDs, technical sheet | `ON active; OFF inactive; flashing unconfigured` | `ST-00001900-EN.pdf` printed/PDF pp. 1-2; `ST_00000540_IT.pdf` pp. 1-2; `LE11286AC.pdf` pp. 1-4 |
| Related Full control | `KW/KM/KG8011 for PRESET; publisher also lists the Light family, without establishing PRESET through that control` | `ST-00001900-EN.pdf` printed/PDF pp. 1-2; `ST_00000540_IT.pdf` pp. 1-2; `LE11286AC.pdf` pp. 1-4 |
| Protection in published wiring | `10 A thermal-magnetic breaker, p. 2` | `ST-00001900-EN.pdf` printed/PDF pp. 1-2; `ST_00000540_IT.pdf` pp. 1-2; `LE11286AC.pdf` pp. 1-4 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Frequency classifications and a negative connected-object classification do not establish the runtime transport or exclude control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system radio frequency | `No` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system LON | `No` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system Powernet | `No` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Other bus systems | `Other` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Radio frequency bidirectional | `No` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Mounting method | `Flush-mounted` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Width in number of modular spacings | `1` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Local operation / hand operation | `Yes` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| With LED indication | `Yes` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Number of digital inputs | `0` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Suitable for C-load | `Yes` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Max. number of switching contacts | `1` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Max. switching current | `2 A` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Rated current | `2 A` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Rated operating voltage (Min- Max) | `25-27 V` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Different phases connectable | `No` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| With bus connection | `No` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Bus module detachable | `Yes` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Min. depth of built-in installation box | `40 mm` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Modular expandability | `Yes` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Degree of protection (IP) | `IP20` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Width | `22 mm` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Height | `45 mm` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Depth | `38 mm` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| degree of impact strength (IK) | `Not applicable` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Operating / setting temperature (Min-Max) | `5-40 °C` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Storage temperature (Min-Max) | `-10-70 °C` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Voltage type | `DC` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Supply current (Min-Max) | `0.02-0.04 A` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Terminal marking indication | `Yes` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Type of load | `Universal` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Connection type | `Screwed terminal` | `K8002S-publisher-product-sheet.pdf` PDF p. 2 |
| Number of distribution blocks | `2` | `K8002S-publisher-product-sheet.pdf` PDF p. 3 |
| Terminals capacity (Min-Max) | `2-2.5 mm²` | `K8002S-publisher-product-sheet.pdf` PDF p. 3 |
| Connection type | `Cable` | `K8002S-publisher-product-sheet.pdf` PDF p. 3 |
| Label space / information surface | `No` | `K8002S-publisher-product-sheet.pdf` PDF p. 3 |
| Fitted with USB plug | `No` | `K8002S-publisher-product-sheet.pdf` PDF p. 3 |
| Addressable | `Yes` | `K8002S-publisher-product-sheet.pdf` PDF p. 3 |
| Connected object | `No` | `K8002S-publisher-product-sheet.pdf` PDF p. 3 |
| Product use function | `Shutter management` | `K8002S-publisher-product-sheet.pdf` PDF p. 3 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2275` | Canonical catalogue |
| Technical item description | Shutter Actuator Living Now advanced | Canonical catalogue |
| Item family | Source placeholder description `0`; key `2` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `120` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `120` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `805` | `1` | `0` | No build row | `1` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `805` | `1` | `218` Shutter actuator | Fixed / designated metadata | `3327` | `514` | `1612` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `805` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Configuration route | MyHOME_Up or MyHOME Suite; exact sheet establishes no physical configurator sockets. External server compatibility requires software configuration. | `ST-00001900-EN.pdf` printed/PDF p. 1 |
| Related completion | Connection module / electrified frame supplies SCS contacts; digital control is a separate product. Full 8011 supplies the shutter PRESET interface. | `ST-00001900-EN.pdf` printed/PDF p. 1 |

### Exact-reference server compatibility

| Server | Published compatibility | Condition / scope | Evidence |
| --- | --- | --- | --- |
| `F460` | Direct association: all production in published table | Software-configured installation; physical configurator exclusion | `ST-00002701-REV2-EN.pdf` printed/PDF p. 3 |
| `F461` | Direct association: all production in published table | Software-configured installation; physical configurator exclusion | `ST-00002702-REV2-EN.pdf` printed/PDF p. 2 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `805` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

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
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `805` | `218` | `3795` | `LOCAL_BUTTON` | `0` = Bistable control; `2` = Blades control and Bistable; `3` = Bistable and blades control | `0` | Modality |
| `805` | `218` | `3807` | `TILTING` | `1..100` (entire reusable range retained) | `70` | Tilting to rolling switch pulse duration |
| `805` | `218` | `3808` | `ROLLING` | `1..100` (entire reusable range retained) | `70` | Rolling to tilting switch pulse duration |
| `805` | `218` | `3809` | `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety (entire reusable range retained) | `1` | Priority |
| `805` | `218` | `3811` | `PRESET_NUMBER` | `1..10`; `0` = None (entire reusable range retained) | `0` | Preset |
| `805` | `218` | `3856` | `SHUTTER_TYPE` | `0` = Standard automatic without slats; `3` = Standard with slats | `0` | Motor type |
| `805` | `218` | `4446` | `UP_SHUTTER_TIME_MINUTES` | `0..9` (entire reusable range retained) | `0` | UP shutter calbration time (m) |
| `805` | `218` | `4459` | `UP_SHUTTER_TIME_SECONDS` | `0..59` (entire reusable range retained) | `0` | UP shutter calbration time (s) |
| `805` | `218` | `4472` | `DOWN_SHUTTER_TIME_MINUTES` | `0..9` (entire reusable range retained) | `0` | DOWN shutter calbration time (m) |
| `805` | `218` | `4485` | `SLATS_ROTATION_TIME_DOWN_H` | `0..27` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is all the way down - HIGH BYTE (ms) |
| `805` | `218` | `4498` | `SLATS_ROTATION_TIME_DOWN_L` | `0..255` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is all the way down - LOW BYTE (ms) |
| `805` | `218` | `4511` | `SLATS_ROTATION_TIME_MIDDLE_H` | `0..27` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is in middle position - HIGH BYTE (ms) |
| `805` | `218` | `4524` | `SLATS_ROTATION_TIME_MIDDLE_L` | `0..255` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is in middle position - LOW BYTE (ms) |
| `805` | `218` | `4537` | `SLATS_ROTATION_STEP_NUMBER` | `3..100` (entire reusable range retained) | `4` | SLATS ROTATION step number |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

Firmware `805` is Official `1.0`, not marked default, with no build row and one logical shutter-actuator Object `218` (catalogue key `514`). Its two interlocked motor relays are one shutter function, not two independent lighting channels. Filter `3795` excludes monostable local-button value `1` and `3856` admits only standard-automatic/no-slats `0` and standard/slats `3`; pulse type `2` and standard/nonautomatic/no-slats `1` are excluded. Other filters retain their full ranges; no replacement default, slot predicate, conversion, Virgin, parameter or package is stored.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `120` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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

Configure through MyHOME_Up or MyHOME Suite as documented. Use the separate Full control for the published PRESET function; the actuator test buttons serve commissioning. Preserve the pulse-motor blade-adjustment limitation. LE11286AC p. 2 supplies this actuator’s calibration sequence below.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

### Published actuator calibration

LE11286AC p. 2 describes the actuator test-button procedure: hold `UP` at least 5 seconds until the upper LED flashes slowly; then press and immediately release `UP` to start the upward travel. At full opening press/release `DOWN`; the closing travel is measured. At full closure press/release `UP`; the opening travel is measured. At full opening press/release `DOWN` to finish. This differs from K4672M2S’s separate configuration-button sequence. The leaflet requires K4950 blanks in empty module positions and shows the K8001 connection-module arrangement.

## Source reconciliation

The 2020 Italian sheet and 2024 English sheet agree on supply, interlock draw and 460/250 W motor ratings. LE11286AC also identifies flashing as unconfigured or missing neutral, whereas the technical-sheet legend mentions only unconfigured; the extra leaflet condition is preserved without implying that no-neutral shutter operation is supported. The technical sheet identifies Full controls for PRESET; a broader exporter compatibility list does not establish identical functions for every listed control. F460/F461 list K8002S for all production in their source scope.

The export operating/setting temperature 5–40 °C differs from the sheet 0–40 °C. Its 25–27 V operating classification differs from the sheet 18–27 V supply range, and its 20–40 mA supply-current class differs from 5/17 mA standby/interlocked draw. A classification of one switching contact is not a replacement for the sheet’s two interlocked relay outputs.

The newer 2024 English sheet adds the pulse-motor PRESET/blade guarantee that is absent from the 2020 Italian sheet. This product-documentation claim does not override catalogue firmware `805` filter `3856`, which excludes pulse motor `2`; no supported installed firmware mapping resolves that discrepancy. The Italian export p. 1 prints Corrente In 16 A while its prose and both technical sheets specify 2 A relays. English export p. 2 gives 25–27 V, 20–40 mA and 5–40 °C, versus 18–27 V, 5 mA standby/17 mA interlock maximum and 0–40 °C in the sheets. With bus connection: No is a classification, while the sheets explicitly describe SCS side contacts.

## Evidence limits and open work

The calibration sequence is documented in LE11286AC; its observed accuracy, preset persistence, installation motor type and runtime status frames remain uncorroborated. No no-neutral shutter operating mode is established by the retained sources.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

### Linked sources outside reviewed evidence

These manufacturer-listed resources are visible discovery work. A listing establishes a source association; it does not establish that the payload was downloaded, verified or examined here.

| Resource | Manufacturer label | Discovery location | Review scope |
| --- | --- | --- | --- |
| `Brochure Living_NOW 2M.pdf` | Brochure BRO-LNOW-2M  /  PDF (15.9 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Brochure%20Living_NOW%202M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Brochure Living_NOW 3M.pdf` | Brochure BRO-LNOW-3M  /  PDF (16.3 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Brochure%20Living_NOW%203M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Catalogue Living_NOW 2M.pdf` | Catalog Commercial Page CAT-LNOW-2M  /  PDF (23.1 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Catalogue%20Living_NOW%202M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Catalogue Living_NOW 3M.pdf` | Catalog Commercial Page CAT-LNOW-3M  /  PDF (22.5 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Catalogue%20Living_NOW%203M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |

Historical English ST_00000540_EN (17 March 2020) and the 2021 MyHOME_Up guide were found online but not separately incorporated. The retained Italian 2020 sheet, English 2024 sheet and October 2020 leaflet supply the examined revision evidence. Manufacturer resolution of the Italian export current and pulse-motor/catalogue filter conflict remains open.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0201-0210-2026-10-07.md#own-dev-0206)
