# Living Now K4672M2S shutter actuator and control

## Summary

K4672M2S is a Living Now shutter actuator with a local command pair and a second pair available for remote functions. It supports shutter-position calibration and a stored preset, while the remote pair can control lighting, automation or scenarios. The choice of standard or pulse motor changes its physical mode mapping and timing behavior.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0203` | Project identity |
| Technical description | Living Now K4672M2S shutter actuator and control | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `K4672M2S` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `2237` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `98` | Main association; independent of project ID |
| Firmware definition | `767` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `4` | Firmware metadata |
| Categories | Actuators, User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Living Now | `K4672M2S` | Established catalogue identity | Manufacturer database commercial record `2581` explicitly links this SKU to item `2237` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `K4672M2S` | `8005543615126` | [K4672M2S-publisher-product-sheet.pdf](https://archive.openwebnet-ha.org/sha256/a8/1c/a81c2d6aefffc59281fab82635c55ca91feb24fd125a4cb2083a1e61048a1b03.pdf) PDF p. 1; `K4672M2S-italian-product-sheet.pdf` PDF p. 1 |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `K4672M2S` | Comando-Attuatore Living Now Tapparelle | Canonical commercial record `2581` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ST-00002701-REV2-EN.pdf` | Technical Sheet ST-00002701-REV2-EN | `ST-00002701-REV2-EN; 16/06/2026` | Printed/PDF pp. 4, 6: exact-reference F460 compatibility only; electrical ratings belong to F460, not this Device. | [Archived original](https://archive.openwebnet-ha.org/sha256/78/ae/78ae843060334dbd6d065284c0e5144469d8629633b519585b8daec14deacdc6.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002701-REV2-EN.pdf) |
| `ST-00002702-REV2-EN.pdf` | Technical Sheet ST-00002702-REV2-EN | `ST-00002702-REV2-EN; 16/06/2026` | Printed/PDF pp. 3, 5: exact-reference F461 compatibility only; electrical ratings belong to F461, not this Device. | [Archived original](https://archive.openwebnet-ha.org/sha256/26/c4/26c407274fdd72d4c0269d84f045ca21cc1beb9e8f26ca64d4de005c0026a662.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002702-REV2-EN.pdf) |
| `LE10316AC.pdf` | Instruction Use LE10316AC | `LE10316AC; 10/18-01 PC` | Printed/PDF pp. 1-4: exact-reference specification, connection and configuration content; shared-product content separately scoped. | [Archived original](https://archive.openwebnet-ha.org/sha256/82/0c/820cf13af3ef3b239f5f121e3067efd69196a8e7966f627d3bfadef2334b79ef.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/LE10316AC.pdf) |
| `ST-00002495-EN.pdf` | Technical Sheet ST-00002495-EN | `ST-00002495-EN; 19/04/2026` | Printed/PDF pp. 1-5: exact-reference specification, connection and configuration content; shared-product content separately scoped. | [Archived original](https://archive.openwebnet-ha.org/sha256/bb/78/bb787df4ca5818a83b0ea86c6af21c9a3669ca2e68f6d18c2c781bee953c520e.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002495-EN.pdf) |
| `K4672M2S-publisher-product-sheet.pdf` | Exact English product export | `Publisher export retrieved 05.10.2026; Italian compliance dates are boilerplate` | PDF pp. 1-5: exact-reference commercial record, EAN and classification values; no printed page sequence established; linked resources are separately accounted for. | [Archived original](https://archive.openwebnet-ha.org/sha256/a8/1c/a81c2d6aefffc59281fab82635c55ca91feb24fd125a4cb2083a1e61048a1b03.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-K4672M2S&include_technical=1) |
| `K4672M2S-italian-product-sheet.pdf` | Exact Italian product export | `Publisher export retrieved 05.10.2026; Italian compliance dates are boilerplate` | PDF pp. 1-2: exact-reference commercial record, EAN and classification values; no printed page sequence established; linked resources are separately accounted for. | [Archived original](https://archive.openwebnet-ha.org/sha256/a9/45/a945ec2b9653e352e34c322c8e2e6eb2115df120020411f0ad6020c2aa37b158.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-K4672M2S) |
| `ST-00001881-IT.pdf` | Italian manufacturer technical document | `ST-00001881-IT; 20/09/2024` | Printed/PDF pp. 1-5: exact-reference specification, connection and configuration content; shared-product content separately scoped. | [Archived original](https://archive.openwebnet-ha.org/sha256/0f/2f/0f2f703607aded17cb48ed43fe6f771e088c71c4f197b83539c5023d4a3aaec0.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/ST-00001881-IT.pdf) |
| `ST_00000465_IT.pdf` | Italian manufacturer technical document | `ST_00000465_IT; 19/11/2018` | Printed/PDF pp. 1-5: exact-reference specification, connection and configuration content; shared-product content separately scoped. | [Archived original](https://archive.openwebnet-ha.org/sha256/78/63/7863dde7879d55897d0df203c2873dfd93c47e8a1c9dafddd2719d038ece8e31.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/ST_00000465_IT.pdf) |
| `MyHOME-2025-Italian-guide.pdf` | MyHOME 2025 Italian guide | `AD-ITMH25GT; Edizione 04/2025, printed cover` | Printed/PDF pp. 140-141: exact-reference role and system context; Edizione 04/2025 established from the printed cover. | [Archived original](https://archive.openwebnet-ha.org/sha256/0d/f6/0df6729969f31f61feb275e84c7da84c665f8c93aeb1d5af9ba1ac29d4f82e4e.pdf) | [Publisher original](https://professionisti.bticino.it/sites/default/files/2025-03/MyHOME%20AD-ITMH25GT_smart_new.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2237`: complete retained canonical associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mains / SCS supply | `110–230 Vac / 22–27 Vdc` | `ST-00002495-EN.pdf` printed/PDF pp. 1-5 |
| Current, 2026 sheet | `8.7 mA standby; 17 mA maximum single load; 25.4 mA maximum double load` | `ST-00002495-EN.pdf` printed/PDF pp. 1-5 |
| Current, 2018/2024 Italian sheets | `8.7 mA standby; 25.4 mA maximum single load; unresolved revision difference` | `ST_00000465_IT.pdf` p. 1; `ST-00001881-IT.pdf` p. 1 |
| Operating temperature | `5–45 °C` | `ST-00002495-EN.pdf` printed/PDF pp. 1-5 |
| Size / terminals | `2 flush-mounted modules; 2 × 2.5 mm² load terminals` | `ST-00002495-EN.pdf` printed/PDF pp. 1-5 |
| Motor load, 230 Vac | `460 W / 2 A` | `ST-00002495-EN.pdf` printed/PDF pp. 1-5 |
| Motor load, 110 Vac | `250 W / 2 A as printed; not recalculated to 220 W` | `ST-00002495-EN.pdf` printed/PDF pp. 1-5 |
| Lighting-group return status | `Remote lighting control, from production 25W49` | `ST-00002495-EN.pdf` printed/PDF pp. 1-5 |
| Shutter preset limitation | `Blade-adjustment PRESET guaranteed only with a pulse motor` | `ST-00002495-EN.pdf` printed/PDF pp. 1-5 |
| Protection in published wiring | `10 A thermal-magnetic breaker, p. 5` | `ST-00002495-EN.pdf` printed/PDF pp. 1-5 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Frequency classifications and a negative connected-object classification do not establish the runtime transport or exclude control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system KNX-RF (Radio Frequency) | `No` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system radio frequency | `No` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system LON | `No` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system Powernet | `No` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Other bus systems | `Other` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Radio frequency bidirectional | `No` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Mounting method | `Flush-mounted` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| With anti-theft / dismantling protection | `No` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| With bus connection | `Yes` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Number of actuation points | `2` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Number of buttons | `2` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| With LED indication | `Yes` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| With label area | `No` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| With display | `No` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Material | `Plastic` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Material quality | `Thermoplastic` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Surface protection | `Untreated` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Surface finishing | `Matt` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Colour | `Anthracite` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| RAL-number (similar) | `9011` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Transparent | `No` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| With room temperature controller | `No` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| With IR sensor | `No` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Degree of protection (IP) | `Other` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Min. depth of built-in installation box | `55 mm` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Width | `45 mm` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Height | `45 mm` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Depth | `36 mm` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Built-in depth | `2 mm` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| degree of impact strength (IK) | `Not applicable` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Operating / setting temperature (Min-Max) | `5-45 °C` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Storage temperature (Min-Max) | `-10-70 °C` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Frequency (Min-Max) | `0-0 Hz` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Standby consumption | `10 mA` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Terminal marking indication | `Yes` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Antimicrobial treatment | `No` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Terminals capacity (Min-Max) | `1-1 mm²` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Cable nature for connection | `Flexible or rigid` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Label space / information surface | `No` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Addressable | `Yes` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Connected object | `No` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Operating method | `SCS` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| With voice command | `Yes` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Programmable | `Yes` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Interoperable connection Protocol | `Yes` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Connectable by Internet box | `Yes` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Product use function | `Shutter management` | `K4672M2S-publisher-product-sheet.pdf` PDF p. 4 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2237` | Canonical catalogue |
| Technical item description | Comando-Attuatore Living Now Tapparelle | Canonical catalogue |
| Item family | Source placeholder description `0`; key `2` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `98` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `98` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `767` | `1` | `0` | No build row | `4` | Catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `767` | `1` | `218` Shutter actuator | Fixed / designated metadata | `3009` | `514` | `1431` |
| `767` | `2` | `400` Light control | Fixed / designated metadata | `3059` | `400` | `1462` |
| `767` | `2` | `401` Automation control | Candidate alternative | `3061` | `401` | `1463` |
| `767` | `2` | `402` Lock / unlock actuator control | Candidate alternative | `3063` | `402` | `1464` |
| `767` | `2` | `406` Scheduled scenario PLUS | Candidate alternative | `3065` | `406` | `1465` |
| `767` | `2` | `408` Open lock control | Candidate alternative | `3076` | `408` | `1471` |
| `767` | `2` | `427` Floor call control | Candidate alternative | `3067` | `427` | `1466` |
| `767` | `2` | `430` Staircase light control | Candidate alternative | `3069` | `430` | `1467` |
| `767` | `2` | `463` Load control actuator visualization | Candidate alternative | `3071` | `492` | `1468` |
| `767` | `2` | `145` Shutter control (2 slots) | Candidate alternative | `3121` | `650` | `1501` |
| `767` | `3` | `400` Light control | Fixed / designated metadata | `3060` | `400` | `1462` |
| `767` | `3` | `401` Automation control | Candidate alternative | `3062` | `401` | `1463` |
| `767` | `3` | `402` Lock / unlock actuator control | Candidate alternative | `3064` | `402` | `1464` |
| `767` | `3` | `406` Scheduled scenario PLUS | Candidate alternative | `3066` | `406` | `1465` |
| `767` | `3` | `408` Open lock control | Candidate alternative | `3077` | `408` | `1471` |
| `767` | `3` | `427` Floor call control | Candidate alternative | `3068` | `427` | `1466` |
| `767` | `3` | `430` Staircase light control | Candidate alternative | `3070` | `430` | `1467` |
| `767` | `3` | `463` Load control actuator visualization | Candidate alternative | `3072` | `492` | `1468` |
| `767` | `4` | `143` User interface settings for command | Fixed / designated metadata | `3073` | `644` | `1469` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `767` | `500` Automation double command virgin | `2`, `3` | `400`, `401`, `404`, `406`, `407` | `500` | `107` |

Firmware `767` is Official `1.0` with four logical Modules and no build row: the local motor is external Object `218` (catalogue key `514`) in slot `1`; slots `2/3` provide remote command alternatives and slot `4` holds UI Object `143`. Two-slot shutter-control Object `145` starts only at slot `2`. Virgin `500` admits five remote roles, including Virgin-only `404/407`; membership does not establish direct placement.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `767` | Physical configuration | `0` | Canonical firmware/mode association |
| `767` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `767` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Current commissioning application | Home + Project; MyHOME Suite or physical configurators also described. Physical configurator operation is excluded when using F460/F461 association, by the separate server compatibility notes. | `ST-00002495-EN.pdf` printed/PDF p. 2 |
| Historical application prerequisites | MyHOME_Up firmware after 2.1 and app after 2.2; MyHOME Suite version higher than 03.03.73. These are historical commissioning-stack requirements, not this item’s canonical V/R tuple. | `ST_00000465_IT.pdf` PDF p. 1 |
| Software / physical addressing | Virtual room 0–10, lighting point 0–15; physical address digits 1–9. Room / global and group commands are function-scoped; the group command domain is 1–255, separately from actuator group-membership values. | `ST-00002495-EN.pdf` printed/PDF p. 2 |
| PLUS scenarios | Virtual scenario address 1–2047; scenario number 0–31. | `ST-00002495-EN.pdf` printed/PDF p. 4 |
| Local motor addressing | A1/PL1/M1; virtual room 0–10, point 0–15, up to ten virtual group values 0–255; physical A1/`PL1=1–9`. | `ST-00002495-EN.pdf` printed/PDF p. 2 |
| Motor mode: `PUL` | Standard motor selector `PUL`; pulse motor selector 6. `PUL` ignores room / general; standard STOP after 2 min. Slave operates to the defined time. Resolve motor type virtually first. | `ST-00002495-EN.pdf` printed/PDF p. 2 |
| Motor mode: Slave | Standard motor selector `SLA`; pulse motor selector 7. `PUL` ignores room / general; standard STOP after 2 min. Slave operates to the defined time. Resolve motor type virtually first. | `ST-00002495-EN.pdf` printed/PDF p. 2 |
| Motor mode: Monostable | Standard motor selector arrow-M; pulse motor selector 4. `PUL` ignores room / general; standard STOP after 2 min. Slave operates to the defined time. Resolve motor type virtually first. | `ST-00002495-EN.pdf` printed/PDF p. 2 |
| Motor mode: Bistable | Standard motor selector arrow or 0; pulse motor selector 3. `PUL` ignores room / general; standard STOP after 2 min. Slave operates to the defined time. Resolve motor type virtually first. | `ST-00002495-EN.pdf` printed/PDF p. 2 |
| Motor mode: Short monostable / long bistable | Standard motor selector 1; pulse motor selector 5. `PUL` ignores room / general; standard STOP after 2 min. Slave operates to the defined time. Resolve motor type virtually first. | `ST-00002495-EN.pdf` printed/PDF p. 2 |
| Slave-`PUL` timing | Select load type Actuator for blinds, curtains, gate or garage shutters; virtual STOP time 1–60 seconds. | `ST-00002495-EN.pdf` printed/PDF p. 2 |
| Remote right command | A2/PL2/M2 remote address; room 0–10, point 0–15; room / group / general routing as applicable. Remote lighting `M2=0` `ON`/`OFF` or `PUL`, timed `ON` 0.5 s/30 s/1 min/2 min via printed `M=8/7/1/2`. Remote point-to-point dimming short / long press 0 or 0/I. | `ST-00002495-EN.pdf` printed/PDF p. 3 |
| Remote automation | Bistable `UP/DOWN` arrow; monostable arrow-M; bistable plus lath M1/`M2=6` as printed. These are remote-control mappings, separate from local motor-type mappings. | `ST-00002495-EN.pdf` printed/PDF p. 4 |
| Preset storage | Move to desired position and hold STOP ≥10 s; left LED blue 2 s confirms. Source refers to nine Pre-socket selections without a corresponding Pre label in its rear socket legend. | `ST-00002495-EN.pdf` printed/PDF p. 4 |
| LED state adjustment | Hold configuration key ≥5 s: blue after 3 s, white after 5 s; thereafter switch every 2 s until release. Default white+blue enabled; alternatives white disabled / blue enabled, or both disabled. | `ST-00002495-EN.pdf` printed/PDF p. 4 |

### Exact-reference server compatibility

| Server | Published compatibility | Condition / scope | Evidence |
| --- | --- | --- | --- |
| `F460` | Direct association: all production in published table | Software-configured installation; physical configurator exclusion | `ST-00002701-REV2-EN.pdf` printed/PDF p. 4 |
| `F460` | Cross-line association `≥24W07`; own-line association YES | Separate association modes; not the device’s newer group-feedback boundary | `ST-00002701-REV2-EN.pdf` printed/PDF p. 6 |
| `F461` | Direct association: all production in published table | Software-configured installation; physical configurator exclusion | `ST-00002702-REV2-EN.pdf` printed/PDF p. 3 |
| `F461` | Cross-line association `≥24W07`; own-line association YES | Separate association modes; not the device’s newer group-feedback boundary | `ST-00002702-REV2-EN.pdf` printed/PDF p. 5 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `767` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `767` | `A1` | `0..9` | `0` | Configurator A1 (0-9) |
| `767` | `PL1` | `0..9` | `0` | PL1 - (0-9) |
| `767` | `M1` | `0..1`; `3..7`; `10` = `OFF`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `15` = `PUL` | `0` | Modality; Mode physical configurator (0-8, `O/I`,`OFF`,`ON`, SU_GIU, SU_GIU_M,`CEN`,`PUL`) |
| `767` | `A2` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB` | `0` | Automation A addressing space (for configurator A2) |
| `767` | `PL2` | `0..9` | `0` | PL2 - (0-9) |
| `767` | `M2` | `0..8`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `15` = `PUL` | `0` | Modality; Mode physical configurator (0-8, `O/I`,`OFF`,`ON`, SU_GIU, SU_GIU_M,`CEN`,`PUL`) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `400` - Light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `1` = Timed `ON`; `2` = Toggle dimmer; `3` = `ON`/`OFF` and dimming; `4` = Toggle `ON`/`OFF`; `5` = `ON`/`OFF`; `9` = `ON`/`OFF` and point to point dimming; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90%; `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `130` = Customized `ON`/`OFF` and point to point dimmer; `131` = Customized toggle dimmer; `132` = Customized `ON`/`OFF` and dimmer; `133` = Customized toggle dimmer without regulation; `134` = Customized `ON`/`OFF` and dimmer without regulation | `0` | Modality; Standard mode means: with regulation for Point-to-point addressing, without regulation for Area, Group and General addressing |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group  |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Light point of reference actuator; 0=no referent address |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0=no referent address |
| `HOURS` | `0..255` | `0` | Hours; Only for `MOD=128` |
| `MINUTES` | `0..59` | `0` | Minutes; Only for `MOD=128` |
| `SECONDS` | `0..59` | `30` | Seconds; Only for `MOD=128` |
| `LEVEL` | `0..100` | `100` | Level; Only for `MOD=129-134` |
| `START_S` | `0..255` | `255` | Soft start speed; Only for `MOD=129-134` |
| `STOP_S` | `0..255` | `255` | Soft stop speed; Only for `MOD=129-134` |
| `DIMMING_S` | `0..255` | `255` | Dimming speed; Only for `MOD=129-132` |
| `T_TIME` | `1` = 1 min; `2` = 2 min; `3` = 3 min; `4` = 4 min; `5` = 5 min; `6` = 15 min; `7` = 30 s; `8` = 0.5 s; `9` = 2 s; `10` = 10 min | `1` | Tabled time; Only for `MOD=1` |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |

### Object `401` - Automation control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `12` = Bistable control; `13` = Monostable control; `14` = Blades control and bistable | `12` | Modality |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group  |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |

### Object `402` - Lock / unlock actuator control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `1` = Disable (lower button); `2` = Enable (lower button); `3` = Disable (lower button) - enable (upper button) | `1` | Modality |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group  |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |

### Object `406` - Scheduled scenario PLUS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | `0..255` | `1` | Scheduled scenario PLUS number |
| `PPT_CEN_HIG` | `0..7` | `0` | Scheduled scenario PLUS number |
| `BUTTON_1` | `0..31` | `1` | Upper button |
| `BUTTON_2` | `0..31` | `2` | Lower button |

### Object `408` - Open lock control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEGMENT` | `0` = Same level; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Level |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |

### Object `427` - Floor call control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `TO_ALL` | `0` = Point to point; `1` = General | `1` | Type of call |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |

### Object `430` - Staircase light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Associated Internal Unit address - hundreds |
| `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |

### Object `463` - Load control actuator visualization

Catalogue Object key `492` maps to external Object `463`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PRIORITY` | `0..63` | `1` | Priority |
| `PHASE` | `0` = Single phase; `1` = Phase 1; `2` = Phase 2; `3` = Phase 3 | `0` | Phase |

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

### Object `143` - User interface settings for command

Catalogue Object key `644` maps to external Object `143`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LED_LEVEL_COMMANDS` | `0` = `OFF`; `1` = Minimum level; `2` = Medium level; `3` = Maximum level | `2` | LED intensity level |
| `ENABLE_DISABLE_LED_COMMAND` | `0` = All Led Enabled; `1` = Presence Led Enabled - State Update Led Disable; `2` = Presence Led Disable - State Update Led Enable; `3` = All Led Disable | `0` | Enable-Disable LED |
| `PRESENCE_LED_INTENSITY_LEVEL_COMMAND` | `0` = Standard level; `1` = High intensity level | `0` | Presence LED intensity level |

### Object `145` - Shutter control (2 slots)

Catalogue Object key `650` maps to external Object `145`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Bistable control; `1` = Monostable control; `2` = Blades control and bistable; `3` = Bistable and blades control | `0` | Modality; Mode (0, 1, 2, 3) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; See Automation System Addressing |
| `A` | `0..10` | `0` | Area; See Automation System Addressing |
| `PL` | `0..15` | `0` | Light point; See Automation System Addressing |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level; See Automation System Addressing |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `15` = Local bus 15; `16` = All systems | `0` | Destination level; See Automation System Addressing |
| `A_R` | `0..10` | `0` | Area of reference actuator |
| `PL_R` | `0..15` | `0` | Light point of reference actuator |
| `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety | `1` | Priority; Shutter management command priority |
| `PRE` | `1..9`; `0` = None | `0` | Preset; Shutter management preset number |

### Object `404` - Scheduled scenario (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `BUTTON_1` | `0..31` | `1` | Upper button |
| `BUTTON_2` | `0..31` | `2` | Lower button |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input AUX channel |
| `START_DELAY` | `0..255` | `10` | Time of restart device (s) |

### Object `407` - AUX control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `9` = `ON`/`OFF` and point to point dimming; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `12` = Bistable control; `13` = Monostable control; `4` = Reset BI; `5` = Reset TRI; `6` = Reset `GEN`; `1` = Disable (lower button); `2` = Enable (lower button); `3` = Disable (upper button) - enable (lower button) | `0` | Modality |
| `OUT_AUX_CH` | `1..15` | `1` | AUX channel |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input AUX channel |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `767` | `400` | `3492` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `767` | `400` | `3493` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `767` | `400` | `3494` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `767` | `401` | `3495` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `767` | `401` | `3496` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `767` | `401` | `3497` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `767` | `402` | `3498` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `767` | `402` | `3499` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `767` | `402` | `3500` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `767` | `408` | `3503` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `767` | `427` | `3501` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `767` | `427` | `3701` | `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone (entire reusable range retained) | `0` | Segment |
| `767` | `430` | `3502` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `767` | `430` | `3702` | `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone (entire reusable range retained) | `0` | Segment |
| `767` | `430` | `4127` | `N2` | `0..15` (entire reusable range retained) | `0` | Associated Internal Unit address - hundreds |
| `767` | `430` | `4140` | `N1` | `100`; `101`; `102`; `103`; `104`; `105`; `106`; `107`; `108`; `109`; `110`; `111`; `112`; `113`; `114`; `115`; `116`; `117`; `118`; `119`; `120`; `121`; `122`; `123`; `124`; `125`; `126`; `127`; `128`; `129`; `130`; `131`; `132`; `133`; `134`; `135`; `136`; `137`; `138`; `139`; `140`; `141`; `142`; `143`; `144`; `145`; `146`; `147`; `148`; `149`; `150`; `151`; `152`; `153`; `154`; `155`; `156`; `157`; `158`; `159`; `160`; `161`; `162`; `163`; `164`; `165`; `166`; `167`; `168`; `169`; `170`; `171`; `172`; `173`; `174`; `175`; `176`; `177`; `178`; `179`; `180`; `181`; `182`; `183`; `184`; `185`; `186`; `187`; `188`; `189`; `190`; `191`; `192`; `193`; `194`; `195`; `196`; `197`; `198`; `199`; `200`; `201`; `202`; `203`; `204`; `205`; `206`; `207`; `208`; `209`; `210`; `211`; `212`; `213`; `214`; `215`; `216`; `217`; `218`; `219`; `220`; `221`; `222`; `223`; `224`; `225`; `226`; `227`; `228`; `229`; `230`; `231`; `232`; `233`; `234`; `235`; `236`; `237`; `238`; `239`; `240`; `241`; `242`; `243`; `244`; `245`; `246`; `247`; `248`; `249`; `250`; `251`; `252`; `253`; `254`; `255` | `0` | Internal unit address; reusable default `0` is outside this subset; filter supplies no replacement default |
| `767` | `218` | `3482` | `TILTING` | `1..100` (entire reusable range retained) | `70` | Tilting to rolling switch pulse duration |
| `767` | `218` | `3483` | `ROLLING` | `1..100` (entire reusable range retained) | `70` | Rolling to tilting switch pulse duration |
| `767` | `218` | `3484` | `LOCAL_BUTTON` | `0` = Bistable control; `1` = Monostable control; `2` = Blades control and Bistable; `3` = Bistable and blades control (entire reusable range retained) | `0` | Modality |
| `767` | `218` | `3485` | `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety (entire reusable range retained) | `1` | Priority |
| `767` | `218` | `3486` | `PRESET_NUMBER` | `1..10`; `0` = None (entire reusable range retained) | `0` | Preset |
| `767` | `218` | `3542` | `SHUTTER_TYPE` | `0` = Standard automatic without slats; `3` = Standard with slats | `0` | Motor type |
| `767` | `218` | `4444` | `UP_SHUTTER_TIME_MINUTES` | `0..9` (entire reusable range retained) | `0` | UP shutter calbration time (m) |
| `767` | `218` | `4457` | `UP_SHUTTER_TIME_SECONDS` | `0..59` (entire reusable range retained) | `0` | UP shutter calbration time (s) |
| `767` | `218` | `4470` | `DOWN_SHUTTER_TIME_MINUTES` | `0..9` (entire reusable range retained) | `0` | DOWN shutter calbration time (m) |
| `767` | `218` | `4483` | `SLATS_ROTATION_TIME_DOWN_H` | `0..27` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is all the way down - HIGH BYTE (ms) |
| `767` | `218` | `4496` | `SLATS_ROTATION_TIME_DOWN_L` | `0..255` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is all the way down - LOW BYTE (ms) |
| `767` | `218` | `4509` | `SLATS_ROTATION_TIME_MIDDLE_H` | `0..27` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is in middle position - HIGH BYTE (ms) |
| `767` | `218` | `4522` | `SLATS_ROTATION_TIME_MIDDLE_L` | `0..255` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is in middle position - LOW BYTE (ms) |
| `767` | `218` | `4535` | `SLATS_ROTATION_STEP_NUMBER` | `3..100` (entire reusable range retained) | `4` | SLATS ROTATION step number |
| `767` | `143` | `3487` | `LED_LEVEL_COMMANDS` | `0` = `OFF`; `1` = Minimum level; `2` = Medium level; `3` = Maximum level (entire reusable range retained) | `2` | LED intensity level |
| `767` | `143` | `3665` | `PRESENCE_LED_INTENSITY_LEVEL_COMMAND` | `0` = Standard level; `1` = High intensity level (entire reusable range retained) | `0` | Presence LED intensity level |
| `767` | `143` | `3666` | `ENABLE_DISABLE_LED_COMMAND` | `1` = Presence Led Enabled - State Update Led Disable | `0` | Enable-Disable LED; reusable default `0` is outside this subset; filter supplies no replacement default |
| `767` | `145` | `3488` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `767` | `145` | `3489` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `767` | `145` | `3490` | `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety (entire reusable range retained) | `1` | Priority |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

UI filter `3666` admits only `1` for `ENABLE_DISABLE_LED_COMMAND` but defaults to `0`. Shutter-control destination level `14` is omitted from its enum while retained by its full-range filter. No slot predicate or conversion resolves physical selector precedence. Motor calibration fields retain separate up/down minutes and seconds, high/low slat timing bytes and step count; they do not prove factory calibration.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `98` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `400` - Light control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `401` - Automation control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `402` - Lock / unlock actuator control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `406` - Scheduled scenario PLUS | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `427` - Floor call control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `430` - Staircase light control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `463` - Load control actuator visualization | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `143` - User interface settings for command | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `408` - Open lock control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `145` - Shutter control (2 slots) | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `218` - Shutter actuator | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `400` - Light control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `400` - Light control | Burglar alarm system | `3` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `400` - Light control | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `400` - Light control | Sound system | `5` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `401` - Automation control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `402` - Lock / unlock actuator control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `406` - Scheduled scenario PLUS | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `406` - Scheduled scenario PLUS | Burglar alarm system | `3` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `406` - Scheduled scenario PLUS | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `406` - Scheduled scenario PLUS | Sound system | `5` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `427` - Floor call control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `427` - Floor call control | Burglar alarm system | `3` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `427` - Floor call control | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `427` - Floor call control | Sound system | `5` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `430` - Staircase light control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `430` - Staircase light control | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `430` - Staircase light control | Sound system | `5` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `463` - Load control actuator visualization | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `463` - Load control actuator visualization | New energy saving and load control | `20` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `143` - User interface settings for command | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `143` - User interface settings for command | New energy saving and load control | `20` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `408` - Open lock control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `408` - Open lock control | Burglar alarm system | `3` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `408` - Open lock control | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `408` - Open lock control | Sound system | `5` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `145` - Shutter control (2 slots) | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

### Related functional reference families

The correspondence below is a semantic cross-reference based on the named role and the canonical functional reference; it does not assert captured frames or support for every operation.

| Catalogue role | Related canonical reference | Evidence limit |
| --- | --- | --- |
| `400` | [Lighting](../../functional/who-1-lighting/) | Related canonical semantics for the named role; exact configured operation and runtime transport remain to be corroborated |
| `145`, `218`, `401` | [Automation](../../functional/who-2-automation/) | Related canonical semantics for the named role; exact configured operation and runtime transport remain to be corroborated |
| `463` | [Energy and load management](../../functional/who-18-energy-management/) | Related canonical semantics for the named role; exact configured operation and runtime transport remain to be corroborated |
| Video-entry-related roles | [Basic video entry](../../functional/who-6-basic-video-door-entry/);[Video entry and telephony](../../functional/who-8-video-door-entry-telephony/) | Related canonical families; which namespace and operation applies to each installed component is not established by the product manual alone |

### Documented functional scope and canonical references

| Role | Canonical reference | Applicability limit |
| --- | --- | --- |
| Actuator lock/unlock | [Special commands](../../functional/who-14-special-commands/) | Semantic reference for Object `402`; exact target and runtime operation require corroboration |
| PLUS scenario trigger | [CEN+ events](../../functional/who-25-transversal/cen-plus.md) | Related event semantics: address/button ranges correspond, but exact emissions remain uncorroborated |

### Virgin-only reusable system associations

| External Object | Reusable system | Catalogue system key | Applicability limit |
| --- | --- | --- | --- |
| `404` Scheduled scenario | Automation | `1` | Virgin membership only; no direct firmware/Object placement |
| `404` Scheduled scenario | Burglar alarm system | `3` | Virgin membership only; no direct firmware/Object placement |
| `404` Scheduled scenario | Video door entry system | `4` | Virgin membership only; no direct firmware/Object placement |
| `404` Scheduled scenario | Sound system | `5` | Virgin membership only; no direct firmware/Object placement |
| `407` AUX control | Automation | `1` | Virgin membership only; no direct firmware/Object placement |
| `407` AUX control | Burglar alarm system | `3` | Virgin membership only; no direct firmware/Object placement |
| `407` AUX control | Video door entry system | `4` | Virgin membership only; no direct firmware/Object placement |
| `407` AUX control | Sound system | `5` | Virgin membership only; no direct firmware/Object placement |

No special-function association is stored for these Virgin-only Objects.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Resolve the motor type and local A1/PL1/M1 role before configuring the A2/PL2/M2 remote pair. The physical standard / pulse mappings are tabulated below. Manual calibration records both limit positions and travel times; the procedure is reproduced in order below. STOP held at least ten seconds stores a user-selected preset. Accurate manual limit detection determines position accuracy; pulse-motor limitations remain applicable.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

### Manual shutter calibration

`ST-00002495-EN.pdf` printed/PDF p. 4 gives this ordered procedure:

1. Hold the configuration key at least three seconds until all LEDs are blue.
2. Release it; the left LED flashes quickly.
3. Press and release the left UP key; the shutter rises and the left LED flashes slowly.
4. At full opening, press left DOWN; the shutter closes while closing time is recorded.
5. At full closure, press/release left UP; it rises while opening time is recorded.
6. At full opening, press left DOWN again to finish; the left LEDs become steady white.

Accuracy depends on the manual detection of both limit positions. The separate STOP ≥10 s action stores a preset; it is not the calibration start key.

## Source reconciliation

The 2018 ST_00000465_IT and 2024 ST-00001881-IT sheets agree on 25.4 mA maximum single-load draw, whereas the 2026 sheet prints 17 mA single and 25.4 mA double. No hardware or firmware revision mapping resolves this difference. The 460 W/250 W motor matrix remains consistent. The calibration text mentions nine Pre-socket positions, although the rear configurator legend names A1/PL1/M1/A2/PL2/M2; this unresolved selector cross-reference is retained. Lighting-group feedback is a remote lighting function, not general proof of shutter-position feedback.

The exact restriction table identifies reusable defaults outside a Firmware/Object subset. These are catalogue conflicts; no replacement default is inferred.

The export temperature 5–45 °C agrees with the exact sheet. Its radio-frequency BUS classification does not establish a transceiver; the SCS connection remains separately documented.

The technical sheet labels the PLUS values as scenario address/number, while Object `406` stores `PPT_CEN_LOW`/`PPT_CEN_HIG` and separate `BUTTON_1`/`BUTTON_2` fields. Their address/button ranges correspond to the canonical CEN+ event model; this is a semantic inference, not a captured frame or proof of stored-scene execution under another namespace.

Both Italian sheets (2018 p. 2 and 2024 p. 2) give slave `PUL` STOP timing 1–60 seconds and 2–10 minutes; the 2026 English sheet p. 2 lists only 1–60 seconds. This is a revision-specific documentation difference, not proof that the longer settings were removed from hardware. The 2024 sheet p. 4 adds the blade-adjustment PRESET restriction to pulse motors; it is absent from the 2018 wording and retained in 2026. Earlier p. 3 virtual feedback wording does not establish the later lighting-group production threshold `25W49`. The export’s standby 10 mA differs from the technical sheets’ 8.7 mA; its 1 mm² terminal classification differs from the 2 × 2.5 mm² load-terminal specification. LE10316AC p. 4 prints 110–240 Vac versus 110–230 Vac in the exact sheets; all retain the literal 250 W motor rating at 110 Vac. Remote lighting capability is separate from the local shutter motor.

## Evidence limits and open work

Installed motor behavior, calibration precision, selector interpretation, current-revision applicability and the actual production boundary remain uncorroborated. The generic current labels single / double are retained from the sheet without implying simultaneous shutter-direction activation.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

### Linked sources outside reviewed evidence

These manufacturer-listed resources are visible discovery work. A listing establishes a source association; it does not establish that the payload was downloaded, verified or examined here.

| Resource | Manufacturer label | Discovery location | Review scope |
| --- | --- | --- | --- |
| `LGRP-00401-V01.01-EN.pdf` | PEP-EPD LGRP-00401-V01.01-EN  /  PDF (1013 KB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/LGRP-00401-V01.01-EN.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `LGRP-01975-V01.01-EN.pdf` | PEP-EPD LGRP-01975-V01.01-EN  /  PDF (795 KB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/LGRP-01975-V01.01-EN.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Brochure Living_NOW 2M.pdf` | Brochure BRO-LNOW-2M  /  PDF (15.9 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Brochure%20Living_NOW%202M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Brochure Living_NOW 3M.pdf` | Brochure BRO-LNOW-3M  /  PDF (16.3 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Brochure%20Living_NOW%203M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Catalogue Living_NOW 2M.pdf` | Catalog Commercial Page CAT-LNOW-2M  /  PDF (23.1 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Catalogue%20Living_NOW%202M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |
| `Catalogue Living_NOW 3M.pdf` | Catalog Commercial Page CAT-LNOW-3M  /  PDF (22.5 MB)  /  EN | [Manufacturer link](https://assets.legrand.com/pim/DOCUMENT/Catalogue%20Living_NOW%203M.pdf) | Linked payload not examined in this dossier; inventory evidence from retained product export / catalogue page |

Manufacturer discovery located the French ST-00002495-FR language variant; it was not incorporated or examined. The retained 2018 Italian, 2024 Italian and 2026 English revisions were compared; no installed production code, motor type or firmware pairing is corroborated.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0201-0210-2026-10-07.md#own-dev-0203)
