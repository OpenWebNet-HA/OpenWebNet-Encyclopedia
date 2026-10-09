# PIR flush-mounted daylight and presence sensor

## Summary

This flush-mounted sensor combines passive infrared presence detection with ambient-light measurement for configured lighting control. Local operation and adjustable sensing behaviour allow it to fit the room's occupancy and daylight requirements.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0016` | Project identity |
| Technical description | Flush-mounted PIR daylight and presence sensor with scenario-control functions | Catalogue + official documentation |
| Catalogue item | `1566` - “PIR flush mounted sensor” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `43` | Implementation evidence |
| Firmware definition | wildcard `-1.-1.-1`, firmware `222` | Implementation evidence |
| Declared Modules | `17` | Implementation evidence |
| Configuration modes | Physical, Virtual, Advanced | Implementation evidence |
| Categories | Sensor, Multifunction, Scenario | Capability model |

This family is the PIR-only counterpart to the PIR+US Green Switch family. Its catalogue topology contains one configuration-selected sensor Object at slot `1` and sixteen fixed IR scenario-control Objects at slots `2..17`.

## Commercial identities

The canonical catalogue groups eight Device records. Several BTicino database codes collapse finish variants into one row, so the printed identity list is larger.

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC4659`, `HS4659`, `HD4659` | Established identities | Catalogue cluster + archived historical sheet / compatibility table |
| BTicino - LivingLight | `L4659N`, `N4659N`, `NT4659N` | Established identities | Catalogue cluster + archived historical sheet / compatibility table |
| BTicino - Matix | `AM5659` | Established identity | Catalogue + archived historical sheet |
| BTicino - Living Now | `K4659` | Established commercial identity | Catalogue + archived current technical sheet |
| Legrand - Arteor | `574046`, `574096` | Established identities | Catalogue + archived historical sheet / compatibility table |
| Legrand - Céliane | `067225` | Established identity | Catalogue + archived historical sheet / compatibility table |
| Legrand - Mosaic | `078485` | Established identity | Catalogue + archived compatibility table |
| BTicino - Axolute | `HC/HS/HD4659` | Catalogue combined identity | Implementation evidence |
| BTicino - LivingLight | `L/N/NT4659N` | Catalogue combined identity | Implementation evidence |

These documents collectively cover every commercial record in the canonical item cluster.

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `HC4659` | `8005543442531` | [Archived original](https://archive.openwebnet-ha.org/sha256/9f/7d/9f7d840c36727261a89dd6d026f33b79acc2861d48e94f1d85d786c5c9ef1d80.pdf), `HC4659-ean-product-sheet.pdf`, printed/PDF p. 2 |
| `HS4659` | `8005543442579` | [Archived original](https://archive.openwebnet-ha.org/sha256/df/2d/df2dea652da781c312db2d963b197adc2f313f5633ec5028ba80f97a06b5deb8.pdf), `HS4659-ean-product-sheet.pdf`, printed/PDF p. 2 |
| `HD4659` | `8005543442616` | [Archived original](https://archive.openwebnet-ha.org/sha256/26/08/2608ba817cda34281dafdd102548acb329e4be97b3ecd319b3c9b1e2197a49ac.pdf), `HD4659-ean-international-sheet.pdf`, printed/PDF p. 1 |
| `L4659N` | `8005543441978` | [Archived original](https://archive.openwebnet-ha.org/sha256/b4/af/b4aff92b26cbcdb644511a58da6aea791b8f19790471fbbde4c4c72f11100aec.pdf), `L4659N-ean-product-sheet.pdf`, printed/PDF p. 2 |
| `N4659N` | `8005543442012` | [Archived original](https://archive.openwebnet-ha.org/sha256/47/e8/47e88293946a5581746597e216733aa1957ad35008f89577fa826cc44823cd56.pdf), `N4659N-ean-product-sheet.pdf`, printed/PDF p. 2 |
| `NT4659N` | `8005543442654` | [Archived original](https://archive.openwebnet-ha.org/sha256/cd/08/cd08a718bffc6184903788616984ed518e05261f7e5e09798a26887234c42c95.pdf), `NT4659N-ean-product-sheet.pdf`, printed/PDF p. 2 |
| `AM5659` | `8005543479018` | [Archived original](https://archive.openwebnet-ha.org/sha256/cc/92/cc92a40fdbb0f207d702b99520a77e212715039128b670f24c75a347a3fd09a8.pdf), `AM5659-ean-product-sheet.pdf`, printed/PDF p. 2 |
| `K4659` | `8005543615102` | [Archived original](https://archive.openwebnet-ha.org/sha256/ca/e8/cae8772d9a0897b5859445a97a12bf036ce058d31702fcbf9143dff3a2387eef.pdf), `K4659-ean-product-sheet.pdf`, printed/PDF p. 2 |
| `067225` | `3245060672256` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/b6/bc/b6bc990f93ddce1dc166caf79f8a05bd2e935943aae095964a6dd5331c46cc6d.pdf), `067225-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |
| `078485` | `3245060784850` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/16/ef/16ef087c09c291616f2a7238d97f37e360715677fcf1df59730b4d957bca6839.pdf), `078485-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00474-e-FR` | Historical technical sheet | No dated imprint established in inspected original | legacy PIR Green Switch family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/35/a9/35a9f4316e1e9d1202f6c13256f5ab87e56cb935c81674b04b3a7bf9fbcbccb4.pdf) | publisher source not currently retained |
| `ST_00000220_EN` | Current-generation technical sheet | 24 April 2019 | `K4659` and PIR flush-mounted sensor | [Archived PDF](https://archive.openwebnet-ha.org/sha256/0d/11/0d11c78827815fcb3d783259f51760ee7e49a1ae35e1c980519a89856d79ae9e.pdf) | publisher source not currently retained |
| `ST-00002122-EN` | Compatibility table | 21 October 2024 | PIR family references occur on printed pp. 8, 11 / PDF pp. 8, 11 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/e1/a8/e1a8da77199296d9f56ea708402f144b8614473558002c0f8db4ee16eb2f0d0d.pdf) | publisher source not currently retained |
| `HC4659-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HC4659` to EAN-13 relationship at printed/PDF p. 2. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/9f/7d/9f7d840c36727261a89dd6d026f33b79acc2861d48e94f1d85d786c5c9ef1d80.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4659) |
| `HS4659-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HS4659` to EAN-13 relationship at printed/PDF p. 2. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/df/2d/df2dea652da781c312db2d963b197adc2f313f5633ec5028ba80f97a06b5deb8.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4659) |
| `HD4659-ean-international-sheet.pdf` | English manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HD4659` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/26/08/2608ba817cda34281dafdd102548acb329e4be97b3ecd319b3c9b1e2197a49ac.pdf) | [Publisher source](https://www.bticino.com/products/pdf?sku=BT-HD4659&include_technical=1) |
| `L4659N-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `L4659N` to EAN-13 relationship at printed/PDF p. 2. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/b4/af/b4aff92b26cbcdb644511a58da6aea791b8f19790471fbbde4c4c72f11100aec.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4659N) |
| `N4659N-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `N4659N` to EAN-13 relationship at printed/PDF p. 2. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/47/e8/47e88293946a5581746597e216733aa1957ad35008f89577fa826cc44823cd56.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-N4659N) |
| `NT4659N-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `NT4659N` to EAN-13 relationship at printed/PDF p. 2. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/cd/08/cd08a718bffc6184903788616984ed518e05261f7e5e09798a26887234c42c95.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-NT4659N) |
| `AM5659-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `AM5659` to EAN-13 relationship at printed/PDF p. 2. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/cc/92/cc92a40fdbb0f207d702b99520a77e212715039128b670f24c75a347a3fd09a8.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5659) |
| `K4659-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `K4659` to EAN-13 relationship at printed/PDF p. 2. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/ca/e8/cae8772d9a0897b5859445a97a12bf036ce058d31702fcbf9143dff3a2387eef.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-K4659) |
| `067225-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `067225` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/b6/bc/b6bc990f93ddce1dc166caf79f8a05bd2e935943aae095964a6dd5331c46cc6d.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue/detecteur-de-mouvements-bus-celiane-presence-et-luminosite-pour-lieux-de-passage) |
| `078485-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `078485` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/16/ef/16ef087c09c291616f2a7238d97f37e360715677fcf1df59730b4d957bca6839.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue/detecteur-de-mouvements-bus-mosaic-presence-et-luminosite-pour-lieux-de-passage-blanc) |

Historical and current sheets should remain separate evidence because product ranges, software requirements and presentation evolved.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Sensor / width | PIR with 180° detection and brightness sensor; 2 flush-mounted modules | MQ00474-e-FR, p. 1; ST-00000220-EN, p. 1 |
| Supply / maximum current | `27 Vdc`; `15 mA` | Same sources; named legacy variants and K4659 |
| Dimensions / box | Legacy body `45 × 45 × 51 mm`; minimum flush-box depth `40 mm` | MQ00474-e-FR, p. 1; box depth also ST-00000220-EN, p. 1 |
| Weight / enclosure | 60 g; IP20; IK04 | Both sheets, p. 1 |
| Temperatures | Operating −5..+`45 °C`; storage −20..+`70 °C` | Both sheets, p. 1 |
| Headline settings | Delay 5 s..59 min 59 s; brightness `20..1275` lux | Both sheets, p. 1; distinct from advanced remote/physical presets |
| Detection geometry | At illustrated 1.2 m height: approximately 6 m large-movement and 3 m small-movement reach | MQ00474-e-FR, p. 3; ST-00000220-EN, p. 3; diagram scope |

These electrical specifications directly name the legacy sheet references and K4659. The compatibility table supplies a relationship for 078485, but does not establish that Mosaic package’s weight or electrical equivalence.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1566` | Implementation evidence |
| Main system | Lighting / Automation | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `43` | Implementation evidence |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `43` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `222` | `-1` | `-1` | `-1` | `17` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Wildcard values are catalogue applicability sentinels, not claims about an installed firmware version.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `222` | `1` | `119` Stand alone presence sensor | Candidate alternative | `2119` | `119` | `885` |
| `222` | `1` | `128` Scenarios daylight and presence sensor | Candidate alternative | `2115` | `128` | `881` |
| `222` | `1` | `164` Scenarios daylight sensor | Candidate alternative | `2116` | `164` | `882` |
| `222` | `1` | `165` Scenarios presence sensor | Candidate alternative | `2117` | `165` | `883` |
| `222` | `1` | `166` Stand alone daylight sensor | Candidate alternative | `2118` | `166` | `884` |
| `222` | `1` | `168` Stand alone daylight and presence sensor | Fixed/designated metadata | `2120` | `168` | `886` |
| `222` | `2` | `431` IR scenario control | Fixed/designated metadata | `1139` | `431` | `618` |
| `222` | `3` | `431` IR scenario control | Fixed/designated metadata | `1140` | `431` | `618` |
| `222` | `4` | `431` IR scenario control | Fixed/designated metadata | `1141` | `431` | `618` |
| `222` | `5` | `431` IR scenario control | Fixed/designated metadata | `1142` | `431` | `618` |
| `222` | `6` | `431` IR scenario control | Fixed/designated metadata | `1143` | `431` | `618` |
| `222` | `7` | `431` IR scenario control | Fixed/designated metadata | `1144` | `431` | `618` |
| `222` | `8` | `431` IR scenario control | Fixed/designated metadata | `1145` | `431` | `618` |
| `222` | `9` | `431` IR scenario control | Fixed/designated metadata | `1146` | `431` | `618` |
| `222` | `10` | `431` IR scenario control | Fixed/designated metadata | `1147` | `431` | `618` |
| `222` | `11` | `431` IR scenario control | Fixed/designated metadata | `1148` | `431` | `618` |
| `222` | `12` | `431` IR scenario control | Fixed/designated metadata | `1149` | `431` | `618` |
| `222` | `13` | `431` IR scenario control | Fixed/designated metadata | `1150` | `431` | `618` |
| `222` | `14` | `431` IR scenario control | Fixed/designated metadata | `1151` | `431` | `618` |
| `222` | `15` | `431` IR scenario control | Fixed/designated metadata | `1152` | `431` | `618` |
| `222` | `16` | `431` IR scenario control | Fixed/designated metadata | `1153` | `431` | `618` |
| `222` | `17` | `431` IR scenario control | Fixed/designated metadata | `1154` | `431` | `618` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

Slot `1` can represent several sensor roles:
Object `168` is marked fixed/designated in the slot table, while other sensor Objects are alternatives selected by configuration. The absence of explicit condition rows on Objects `119`, `164` and `165` should not be “completed” by guessing missing branches.
Object `431`, **IR scenario control**, is fixed at each slot from `2` through `17`, giving sixteen IR scenario-control Modules in addition to the primary sensor Module.
There are no Virgin Objects.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `222` | Physical configuration | `0` | Canonical firmware/mode association |
| `222` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `222` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `222` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `222` | `A` | `0..9` | `0` | A; Environment |
| `222` | `PL` | `0..9` | `0` | PL; Light Point |
| `222` | `M` | `0..4` | `0` | M; Mode 0-4 |
| `222` | `S` | `0..4` | `0` | S; Configurator S (0-4) |
| `222` | `T` | `0..9` | `0` | T; Configurator T (time) - (0-9) |
| `222` | `D` | `0..5` | `0` | D; (0-5) |

### Published `M` modes

The product documentation describes the modes as:

| `M` | Role |
| ---: | --- |
| `0` | automatic load control from motion/presence and ambient brightness |
| `1` | daylight-only operation, movement detection disabled |
| `2` | sends movement/brightness information for scenario-management use |
| `3` | presence plus constant-brightness / dimmer regulation |
| `4` | daylight-oriented manual-`ON` / automatic-`OFF` constant-brightness operation |

### Published `T` timing presets

| `T` | Delay |
| ---: | --- |
| no configurator | 15 min |
| `1` | 30 s |
| `2` | 1 min |
| `3` | 2 min |
| `4` | 5 min |
| `5` | 10 min |
| `6` | 15 min |
| `7` | 20 min |
| `8` | 30 min |
| `9` | 40 min |

### Published sensitivity and daylight presets

The published physical sensitivity selector has no configurator = Low, `1=Medium`, `2=High`, `3=Very high`.

The daylight selector documents no configurator = 300 lux, then approximately `20`, `100`, `300`, `500`, and `1000 lux` for `D=1..5`.

### Published remote-control settings

| Setting | Published default | Adjustable scope | Evidence |
| --- | --- | --- | --- |
| Delay | 15 min | Simplified 3/5/10/15/20 min; advanced 30 s..255 h 59 min 59 s | MQ00474-e-FR, p. 2; ST-00000220-EN, p. 2 |
| PIR sensitivity | Very high | Low / medium / high / very high | Same sources |
| Brightness | 300 lux | Presets 20/100/300/500/1000; advanced `0..1275` lux | Same sources |
| Occupancy modes | Auto off, Walkthrough on, Eco off | ON/OFF | Same sources |
| Detection stages | PIR | Initial/holding fixed PIR; retrigger PIR/OFF | Same sources |
| Warning alarm | Off | ON/OFF; signals at 1 min, 30 s, 10 s before switch-off | Same sources, settings explanation |
| Calibration / adjustment | No calibration value specified; adjustment off | Lux-meter calibration `0..99995` lux; adjustment ON/OFF | Same sources |
| Contribution of light | Automatic | Automatic or up to 1275 lux | Same sources |

BMSO4001/088230 is the advanced remote; BMSO4003/088235 the simplified remote. The source’s copied “PIR and US” sensitivity footnote does not establish an ultrasonic sensor in this PIR-only product.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `119` - Stand alone presence sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | `0` = Point to point; `2` = Group | `0` | Addressing type |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `0..255` | `0` | Group number |
| `A_R` | `0..10` | `0` | Referent area address |
| `PL_R` | `0..15` | `0` | Referent light point address |
| `MAIN_GROUP` | `0` = Disable; `1` = Enable | `0` | Enable secondary groups |
| `G1` | `0..255` | `0` | Secondary group 1 |
| `G2` | `0..255` | `0` | Secondary group 2 |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `10` | Minutes |
| `SECONDS` | `0..59` | `0` | Seconds |
| `FUNC_MODE` | `1` = Auto `ON`/`OFF`; `2` = Auto Walkthrough; `3` = Manual `ON` / Auto `OFF`; `5` = Partial `ON` / Group `OFF` | `2` | Operating mode; Functional_mode |
| `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `3` | PIR sensitivity |
| `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `2` | US sensitivity |
| `INITIAL_OCCUPANCY` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `3` | Initial occupancy |
| `MAINTAIN_OCCUPANCY` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Maintain detection |
| `RETRIGGER` | `0` = Disabled; `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Retrigger |
| `ALERT` | `0` = Disabled; `1` = Visual; `2` = Acoustic; `3` = Visual and Acoustic | `0` | Alert |
| `ENABLE_LOAD_CONTROL` | `0` = Disabled; `1` = Enabled | `1` | Enable load control |

### Object `128` - Scenarios daylight and presence sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `HOURS` | `0..255` | `0` | Time delay - Hours |
| `MINUTES` | `0..59` | `15` | Time delay - Minutes |
| `SECONDS` | `0..59` | `0` | Time delay - Seconds |
| `SCHEMA` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Detection scheme |
| `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `3` | PIR sensitivity |
| `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `2` | US sensitivity |

### Object `164` - Scenarios daylight sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |

### Object `165` - Scenarios presence sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `HOURS` | `0..255` | `0` | Time delay - Hours |
| `MINUTES` | `0..59` | `15` | Time delay - Minutes |
| `SECONDS` | `0..59` | `0` | Time delay - Seconds |
| `SCHEMA` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Detection scheme |
| `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `3` | PIR sensitivity |
| `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `2` | US sensitivity |

### Object `166` - Stand alone daylight sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | `0` = Point to point; `2` = Group | `0` | Addressing type |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `0..255` | `0` | Group number |
| `A_R` | `0..10` | `0` | Area of reference actuator |
| `PL_R` | `0..15` | `0` | Light point of reference actuator |
| `TYPE_LOOP` | `0` = Closed loop; `1` = Open loop | `0` | Loop type |
| `GD` | `0..255` | `0` | Daylight cell group |
| `DAYLIGHT_SETPOINT` | `0`; `1` = 5; `2` = 10; `3` = 15; `4` = 20; `5` = 25; `6` = 30; `7` = 35; `8` = 40; `9` = 45; `10` = 50; `11` = 55; `12` = 60; `13` = 65; `14` = 70; `15` = 75; `16` = 80; `17` = 85; `18` = 90; `19` = 95; `20` = 100; `21` = 105; `22` = 110; `23` = 115; `24` = 120; `25` = 125; `26` = 130; `27` = 135; `28` = 140; `29` = 145; `30` = 150; `31` = 155; `32` = 160; `33` = 165; `34` = 170; `35` = 175; `36` = 180; `37` = 185; `38` = 190; `39` = 195; `40` = 200; `41` = 205; `42` = 210; `43` = 215; `44` = 220; `45` = 225; `46` = 230; `47` = 235; `48` = 240; `49` = 245; `50` = 250; `51` = 255; `52` = 260; `53` = 265; `54` = 270; `55` = 275; `56` = 280; `57` = 285; `58` = 290; `59` = 295; `60` = 300; `61` = 305; `62` = 310; `63` = 315; `64` = 320; `65` = 325; `66` = 330; `67` = 335; `68` = 340; `69` = 345; `70` = 350; `71` = 355; `72` = 360; `73` = 365; `74` = 370; `75` = 375; `76` = 380; `77` = 385; `78` = 390; `79` = 395; `80` = 400; `81` = 405; `82` = 410; `83` = 415; `84` = 420; `85` = 425; `86` = 430; `87` = 435; `88` = 440; `89` = 445; `90` = 450; `91` = 455; `92` = 460; `93` = 465; `94` = 470; `95` = 475; `96` = 480; `97` = 485; `98` = 490; `99` = 495; `100` = 500; `101` = 505; `102` = 510; `103` = 515; `104` = 520; `105` = 525; `106` = 530; `107` = 535; `108` = 540; `109` = 545; `110` = 550; `111` = 555; `112` = 560; `113` = 565; `114` = 570; `115` = 575; `116` = 580; `117` = 585; `118` = 590; `119` = 595; `120` = 600; `121` = 605; `122` = 610; `123` = 615; `124` = 620; `125` = 625; `126` = 630; `127` = 635; `128` = 640; `129` = 645; `130` = 650; `131` = 655; `132` = 660; `133` = 665; `134` = 670; `135` = 675; `136` = 680; `137` = 685; `138` = 690; `139` = 695; `140` = 700; `141` = 705; `142` = 710; `143` = 715; `144` = 720; `145` = 725; `146` = 730; `147` = 735; `148` = 740; `149` = 745; `150` = 750; `151` = 755; `152` = 760; `153` = 765; `154` = 770; `155` = 775; `156` = 780; `157` = 785; `158` = 790; `159` = 795; `160` = 800; `161` = 805; `162` = 810; `163` = 815; `164` = 820; `165` = 825; `166` = 830; `167` = 835; `168` = 840; `169` = 845; `170` = 850; `171` = 855; `172` = 860; `173` = 865; `174` = 870; `175` = 875; `176` = 880; `177` = 885; `178` = 890; `179` = 895; `180` = 900; `181` = 905; `182` = 910; `183` = 915; `184` = 920; `185` = 925; `186` = 930; `187` = 935; `188` = 940; `189` = 945; `190` = 950; `191` = 955; `192` = 960; `193` = 965; `194` = 970; `195` = 975; `196` = 980; `197` = 985; `198` = 990; `199` = 995; `200` = 1000; `201` = 1005; `202` = 1010; `203` = 1015; `204` = 1020; `205` = 1025; `206` = 1030; `207` = 1035; `208` = 1040; `209` = 1045; `210` = 1050; `211` = 1055; `212` = 1060; `213` = 1065; `214` = 1070; `215` = 1075; `216` = 1080; `217` = 1085; `218` = 1090; `219` = 1095; `220` = 1100; `221` = 1105; `222` = 1110; `223` = 1115; `224` = 1120; `225` = 1125; `226` = 1130; `227` = 1135; `228` = 1140; `229` = 1145; `230` = 1150; `231` = 1155; `232` = 1160; `233` = 1165; `234` = 1170; `235` = 1175; `236` = 1180; `237` = 1185; `238` = 1190; `239` = 1195; `240` = 1200; `241` = 1205; `242` = 1210; `243` = 1215; `244` = 1220; `245` = 1225; `246` = 1230; `247` = 1235; `248` = 1240; `249` = 1245; `250` = 1250; `251` = 1255; `252` = 1260; `253` = 1265; `254` = 1270; `255` = 1275 | `100` | Daylight setpoint (Lux) |
| `PROVISION_OF_LIGHT` | `0` = Automatic; `1` = 5; `2` = 10; `3` = 15; `4` = 20; `5` = 25; `6` = 30; `7` = 35; `8` = 40; `9` = 45; `10` = 50; `11` = 55; `12` = 60; `13` = 65; `14` = 70; `15` = 75; `16` = 80; `17` = 85; `18` = 90; `19` = 95; `20` = 100; `21` = 105; `22` = 110; `23` = 115; `24` = 120; `25` = 125; `26` = 130; `27` = 135; `28` = 140; `29` = 145; `30` = 150; `31` = 155; `32` = 160; `33` = 165; `34` = 170; `35` = 175; `36` = 180; `37` = 185; `38` = 190; `39` = 195; `40` = 200; `41` = 205; `42` = 210; `43` = 215; `44` = 220; `45` = 225; `46` = 230; `47` = 235; `48` = 240; `49` = 245; `50` = 250; `51` = 255; `52` = 260; `53` = 265; `54` = 270; `55` = 275; `56` = 280; `57` = 285; `58` = 290; `59` = 295; `60` = 300; `61` = 305; `62` = 310; `63` = 315; `64` = 320; `65` = 325; `66` = 330; `67` = 335; `68` = 340; `69` = 345; `70` = 350; `71` = 355; `72` = 360; `73` = 365; `74` = 370; `75` = 375; `76` = 380; `77` = 385; `78` = 390; `79` = 395; `80` = 400; `81` = 405; `82` = 410; `83` = 415; `84` = 420; `85` = 425; `86` = 430; `87` = 435; `88` = 440; `89` = 445; `90` = 450; `91` = 455; `92` = 460; `93` = 465; `94` = 470; `95` = 475; `96` = 480; `97` = 485; `98` = 490; `99` = 495; `100` = 500; `101` = 505; `102` = 510; `103` = 515; `104` = 520; `105` = 525; `106` = 530; `107` = 535; `108` = 540; `109` = 545; `110` = 550; `111` = 555; `112` = 560; `113` = 565; `114` = 570; `115` = 575; `116` = 580; `117` = 585; `118` = 590; `119` = 595; `120` = 600; `121` = 605; `122` = 610; `123` = 615; `124` = 620; `125` = 625; `126` = 630; `127` = 635; `128` = 640; `129` = 645; `130` = 650; `131` = 655; `132` = 660; `133` = 665; `134` = 670; `135` = 675; `136` = 680; `137` = 685; `138` = 690; `139` = 695; `140` = 700; `141` = 705; `142` = 710; `143` = 715; `144` = 720; `145` = 725; `146` = 730; `147` = 735; `148` = 740; `149` = 745; `150` = 750; `151` = 755; `152` = 760; `153` = 765; `154` = 770; `155` = 775; `156` = 780; `157` = 785; `158` = 790; `159` = 795; `160` = 800; `161` = 805; `162` = 810; `163` = 815; `164` = 820; `165` = 825; `166` = 830; `167` = 835; `168` = 840; `169` = 845; `170` = 850; `171` = 855; `172` = 860; `173` = 865; `174` = 870; `175` = 875; `176` = 880; `177` = 885; `178` = 890; `179` = 895; `180` = 900; `181` = 905; `182` = 910; `183` = 915; `184` = 920; `185` = 925; `186` = 930; `187` = 935; `188` = 940; `189` = 945; `190` = 950; `191` = 955; `192` = 960; `193` = 965; `194` = 970; `195` = 975; `196` = 980; `197` = 985; `198` = 990; `199` = 995; `200` = 1000; `201` = 1005; `202` = 1010; `203` = 1015; `204` = 1020; `205` = 1025; `206` = 1030; `207` = 1035; `208` = 1040; `209` = 1045; `210` = 1050; `211` = 1055; `212` = 1060; `213` = 1065; `214` = 1070; `215` = 1075; `216` = 1080; `217` = 1085; `218` = 1090; `219` = 1095; `220` = 1100; `221` = 1105; `222` = 1110; `223` = 1115; `224` = 1120; `225` = 1125; `226` = 1130; `227` = 1135; `228` = 1140; `229` = 1145; `230` = 1150; `231` = 1155; `232` = 1160; `233` = 1165; `234` = 1170; `235` = 1175; `236` = 1180; `237` = 1185; `238` = 1190; `239` = 1195; `240` = 1200; `241` = 1205; `242` = 1210; `243` = 1215; `244` = 1220; `245` = 1225; `246` = 1230; `247` = 1235; `248` = 1240; `249` = 1245; `250` = 1250; `251` = 1255; `252` = 1260; `253` = 1265; `254` = 1270; `255` = 1275 | `0` | Provision of light (Lux) |
| `FUNC_MODE` | `1` = Auto `ON`/`OFF`; `3` = Manual `ON` / Auto `OFF`; `5` = Partial `ON` / Group `OFF` | `1` | Operating mode; Functional_mode (auto/manual/partial) |
| `LIGHTING_REGULATION` | `0` = Disabled; `1` = Enabled | `0` | Lighting regulation |
| `DAYLIGHT_FACTOR` | `0..255` | `0` | Daylight factor |
| `NATURAL_LIGHT_FACTOR` | `0..255` | `0` | Natural light factor |
| `DAYLIGHT_LEVEL` | `0..255` | `0` | Daylight level |

### Object `168` - Stand alone daylight and presence sensor

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | `0` = Point-to-point; `2` = Group | `0` | Addressing type |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `1` | Light point |
| `G` | `0..255` | `0` | Group number |
| `A_R` | `0..10` | `0` | Referent area address |
| `PL_R` | `0..15` | `0` | Referent light point address |
| `MAIN_GROUP` | `0` = Disable; `1` = Enable | `0` | Enable secondary groups |
| `G1` | `0..255` | `0` | Sensor group 1 |
| `G2` | `0..255` | `0` | Sensor group 2 |
| `TYPE_LOOP` | `0` = Closed loop; `1` = Open loop | `0` | Loop type |
| `GD` | `0..255` | `0` | Daylight cell group |
| `DAYLIGHT_SETPOINT` | `0`; `1` = 5; `2` = 10; `3` = 15; `4` = 20; `5` = 25; `6` = 30; `7` = 35; `8` = 40; `9` = 45; `10` = 50; `11` = 55; `12` = 60; `13` = 65; `14` = 70; `15` = 75; `16` = 80; `17` = 85; `18` = 90; `19` = 95; `20` = 100; `21` = 105; `22` = 110; `23` = 115; `24` = 120; `25` = 125; `26` = 130; `27` = 135; `28` = 140; `29` = 145; `30` = 150; `31` = 155; `32` = 160; `33` = 165; `34` = 170; `35` = 175; `36` = 180; `37` = 185; `38` = 190; `39` = 195; `40` = 200; `41` = 205; `42` = 210; `43` = 215; `44` = 220; `45` = 225; `46` = 230; `47` = 235; `48` = 240; `49` = 245; `50` = 250; `51` = 255; `52` = 260; `53` = 265; `54` = 270; `55` = 275; `56` = 280; `57` = 285; `58` = 290; `59` = 295; `60` = 300; `61` = 305; `62` = 310; `63` = 315; `64` = 320; `65` = 325; `66` = 330; `67` = 335; `68` = 340; `69` = 345; `70` = 350; `71` = 355; `72` = 360; `73` = 365; `74` = 370; `75` = 375; `76` = 380; `77` = 385; `78` = 390; `79` = 395; `80` = 400; `81` = 405; `82` = 410; `83` = 415; `84` = 420; `85` = 425; `86` = 430; `87` = 435; `88` = 440; `89` = 445; `90` = 450; `91` = 455; `92` = 460; `93` = 465; `94` = 470; `95` = 475; `96` = 480; `97` = 485; `98` = 490; `99` = 495; `100` = 500; `101` = 505; `102` = 510; `103` = 515; `104` = 520; `105` = 525; `106` = 530; `107` = 535; `108` = 540; `109` = 545; `110` = 550; `111` = 555; `112` = 560; `113` = 565; `114` = 570; `115` = 575; `116` = 580; `117` = 585; `118` = 590; `119` = 595; `120` = 600; `121` = 605; `122` = 610; `123` = 615; `124` = 620; `125` = 625; `126` = 630; `127` = 635; `128` = 640; `129` = 645; `130` = 650; `131` = 655; `132` = 660; `133` = 665; `134` = 670; `135` = 675; `136` = 680; `137` = 685; `138` = 690; `139` = 695; `140` = 700; `141` = 705; `142` = 710; `143` = 715; `144` = 720; `145` = 725; `146` = 730; `147` = 735; `148` = 740; `149` = 745; `150` = 750; `151` = 755; `152` = 760; `153` = 765; `154` = 770; `155` = 775; `156` = 780; `157` = 785; `158` = 790; `159` = 795; `160` = 800; `161` = 805; `162` = 810; `163` = 815; `164` = 820; `165` = 825; `166` = 830; `167` = 835; `168` = 840; `169` = 845; `170` = 850; `171` = 855; `172` = 860; `173` = 865; `174` = 870; `175` = 875; `176` = 880; `177` = 885; `178` = 890; `179` = 895; `180` = 900; `181` = 905; `182` = 910; `183` = 915; `184` = 920; `185` = 925; `186` = 930; `187` = 935; `188` = 940; `189` = 945; `190` = 950; `191` = 955; `192` = 960; `193` = 965; `194` = 970; `195` = 975; `196` = 980; `197` = 985; `198` = 990; `199` = 995; `200` = 1000; `201` = 1005; `202` = 1010; `203` = 1015; `204` = 1020; `205` = 1025; `206` = 1030; `207` = 1035; `208` = 1040; `209` = 1045; `210` = 1050; `211` = 1055; `212` = 1060; `213` = 1065; `214` = 1070; `215` = 1075; `216` = 1080; `217` = 1085; `218` = 1090; `219` = 1095; `220` = 1100; `221` = 1105; `222` = 1110; `223` = 1115; `224` = 1120; `225` = 1125; `226` = 1130; `227` = 1135; `228` = 1140; `229` = 1145; `230` = 1150; `231` = 1155; `232` = 1160; `233` = 1165; `234` = 1170; `235` = 1175; `236` = 1180; `237` = 1185; `238` = 1190; `239` = 1195; `240` = 1200; `241` = 1205; `242` = 1210; `243` = 1215; `244` = 1220; `245` = 1225; `246` = 1230; `247` = 1235; `248` = 1240; `249` = 1245; `250` = 1250; `251` = 1255; `252` = 1260; `253` = 1265; `254` = 1270; `255` = 1275 | `100` | Daylight setpoint (Lux) |
| `PROVISION_OF_LIGHT` | `0` = Automatic; `1` = 5; `2` = 10; `3` = 15; `4` = 20; `5` = 25; `6` = 30; `7` = 35; `8` = 40; `9` = 45; `10` = 50; `11` = 55; `12` = 60; `13` = 65; `14` = 70; `15` = 75; `16` = 80; `17` = 85; `18` = 90; `19` = 95; `20` = 100; `21` = 105; `22` = 110; `23` = 115; `24` = 120; `25` = 125; `26` = 130; `27` = 135; `28` = 140; `29` = 145; `30` = 150; `31` = 155; `32` = 160; `33` = 165; `34` = 170; `35` = 175; `36` = 180; `37` = 185; `38` = 190; `39` = 195; `40` = 200; `41` = 205; `42` = 210; `43` = 215; `44` = 220; `45` = 225; `46` = 230; `47` = 235; `48` = 240; `49` = 245; `50` = 250; `51` = 255; `52` = 260; `53` = 265; `54` = 270; `55` = 275; `56` = 280; `57` = 285; `58` = 290; `59` = 295; `60` = 300; `61` = 305; `62` = 310; `63` = 315; `64` = 320; `65` = 325; `66` = 330; `67` = 335; `68` = 340; `69` = 345; `70` = 350; `71` = 355; `72` = 360; `73` = 365; `74` = 370; `75` = 375; `76` = 380; `77` = 385; `78` = 390; `79` = 395; `80` = 400; `81` = 405; `82` = 410; `83` = 415; `84` = 420; `85` = 425; `86` = 430; `87` = 435; `88` = 440; `89` = 445; `90` = 450; `91` = 455; `92` = 460; `93` = 465; `94` = 470; `95` = 475; `96` = 480; `97` = 485; `98` = 490; `99` = 495; `100` = 500; `101` = 505; `102` = 510; `103` = 515; `104` = 520; `105` = 525; `106` = 530; `107` = 535; `108` = 540; `109` = 545; `110` = 550; `111` = 555; `112` = 560; `113` = 565; `114` = 570; `115` = 575; `116` = 580; `117` = 585; `118` = 590; `119` = 595; `120` = 600; `121` = 605; `122` = 610; `123` = 615; `124` = 620; `125` = 625; `126` = 630; `127` = 635; `128` = 640; `129` = 645; `130` = 650; `131` = 655; `132` = 660; `133` = 665; `134` = 670; `135` = 675; `136` = 680; `137` = 685; `138` = 690; `139` = 695; `140` = 700; `141` = 705; `142` = 710; `143` = 715; `144` = 720; `145` = 725; `146` = 730; `147` = 735; `148` = 740; `149` = 745; `150` = 750; `151` = 755; `152` = 760; `153` = 765; `154` = 770; `155` = 775; `156` = 780; `157` = 785; `158` = 790; `159` = 795; `160` = 800; `161` = 805; `162` = 810; `163` = 815; `164` = 820; `165` = 825; `166` = 830; `167` = 835; `168` = 840; `169` = 845; `170` = 850; `171` = 855; `172` = 860; `173` = 865; `174` = 870; `175` = 875; `176` = 880; `177` = 885; `178` = 890; `179` = 895; `180` = 900; `181` = 905; `182` = 910; `183` = 915; `184` = 920; `185` = 925; `186` = 930; `187` = 935; `188` = 940; `189` = 945; `190` = 950; `191` = 955; `192` = 960; `193` = 965; `194` = 970; `195` = 975; `196` = 980; `197` = 985; `198` = 990; `199` = 995; `200` = 1000; `201` = 1005; `202` = 1010; `203` = 1015; `204` = 1020; `205` = 1025; `206` = 1030; `207` = 1035; `208` = 1040; `209` = 1045; `210` = 1050; `211` = 1055; `212` = 1060; `213` = 1065; `214` = 1070; `215` = 1075; `216` = 1080; `217` = 1085; `218` = 1090; `219` = 1095; `220` = 1100; `221` = 1105; `222` = 1110; `223` = 1115; `224` = 1120; `225` = 1125; `226` = 1130; `227` = 1135; `228` = 1140; `229` = 1145; `230` = 1150; `231` = 1155; `232` = 1160; `233` = 1165; `234` = 1170; `235` = 1175; `236` = 1180; `237` = 1185; `238` = 1190; `239` = 1195; `240` = 1200; `241` = 1205; `242` = 1210; `243` = 1215; `244` = 1220; `245` = 1225; `246` = 1230; `247` = 1235; `248` = 1240; `249` = 1245; `250` = 1250; `251` = 1255; `252` = 1260; `253` = 1265; `254` = 1270; `255` = 1275 | `0` | Provision of light (Lux) |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `10` | Minutes |
| `SECONDS` | `0..59` | `0` | Seconds |
| `FUNC_MODE` | `1` = Auto `ON`/`OFF`; `2` = Auto walkthrough; `3` = Manual `ON` / Auto `OFF`; `5` = Partial `ON` / Group `OFF` | `2` | Operating mode; Functional_mode |
| `PIR` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `3` | PIR sensitivity |
| `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum | `1` | US sensitivity |
| `INITIAL_OCC` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `3` | Initial detection |
| `MAINTAIN_OCC` | `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Maintain detection |
| `RE-TRIGGER` | `0` = Disabled; `1` = PIR only; `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Re-trigger |
| `ALERT` | `0` = Disabled; `1` = Visual; `2` = Acoustic; `3` = Visual and Acoustic | `0` | Alert |
| `LOAD_CONTROL` | `0` = Disabled; `1` = Enabled | `1` | Enable load control |
| `LIGHTING_REGULATION` | `0` = Disabled; `1` = Enabled | `0` | Lighting regulation |
| `NATURAL_LIGHT_FACTOR` | `1..255` | `10` | Natural light factor |
| `DAYLIGHT_FACTOR` | `0..255` | `0` | Daylight factor |
| `DAYLIGHT_LEVEL` | `0..255` | `0` | Daylight level |

### Object `431` - IR scenario control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_SCE_1` | `1..255` | `1` | Scenario number |
| `TYPE_OF_REGULATION` | `0` = Regulate all; `1` = Lights only; `2` = Shutters only; `3` = Stereo amplifiers only | `1` | Regulation type |
| `ID1` | `0..255` | `0` | ID1 |
| `ID2` | `0..255` | `0` | ID2 |
| `ID3` | `0..15` | `0` | ID3 |
| `UNIT_NUMBER` | `0..15` | `0` | Push button number |

### Device-specific interpretation

Physical sensitivity allows no configurator or `1..3`; firmware S includes 4. The 16 catalogue IR scenario Modules have not been corroborated as runtime topology. Remote defaults and physical presets are separate scopes.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `222` | `1` | `128` | `4477` | `M=2` | None |
| `222` | `1` | `166` | `4461` | `M=1` | None |
| `222` | `1` | `166` | `4505` | `M=4` | None |
| `222` | `1` | `168` | `4439` | `M=0` | None |
| `222` | `1` | `168` | `4491` | `M=3` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `222` | `119` | `2232` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | US sensitivity |
| `222` | `119` | `2233` | `INITIAL_OCCUPANCY` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `3` | Initial occupancy |
| `222` | `119` | `2234` | `MAINTAIN_OCCUPANCY` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Mantain occupancy |
| `222` | `119` | `2235` | `RETRIGGER` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Re-trigger |
| `222` | `119` | `2236` | `ALERT` | `1` = Visual; `3` = Visual and Acoustic | `0` | Alert; reusable default `0` is outside this subset; filter supplies no replacement default |
| `222` | `128` | `2228` | `SCHEMA` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Detection scheme |
| `222` | `128` | `2229` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | US sensitivity |
| `222` | `165` | `2230` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `2` | US sensitivity |
| `222` | `165` | `2231` | `SCHEMA` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Detection scheme |
| `222` | `166` | `2113` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `222` | `166` | `2128` | `NATURAL_LIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Natural light factor |
| `222` | `166` | `2143` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `222` | `168` | `2158` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `222` | `168` | `2237` | `NATURAL_LIGHT_FACTOR` | `1..255` (entire reusable range retained) | `10` | Natural light factor |
| `222` | `168` | `2238` | `ALERT` | `1` = Visual; `3` = Visual and Acoustic | `0` | Alert; reusable default `0` is outside this subset; filter supplies no replacement default |
| `222` | `168` | `2239` | `INITIAL_OCC` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `3` | Initial occupancy |
| `222` | `168` | `2240` | `MAINTAIN_OCC` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Mantain occupancy |
| `222` | `168` | `2241` | `RE-TRIGGER` | `2` = US only; `3` = PIR and US; `4` = PIR or US | `4` | Re-trigger |
| `222` | `168` | `2321` | `US` | `0` = Low; `1` = Medium; `2` = High; `3` = Maximum (entire reusable range retained) | `1` | US sensitivity |
| `222` | `168` | `2372` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `222` | `168` | `2453` | `DAYLIGHT_SETPOINT` | Subset flag present but no allowed values stored; unresolved restriction | `100` | Daylight setpoint (Lux) |
| `222` | `168` | `2465` | `PROVISION_OF_LIGHT` | Subset flag present but no allowed values stored; unresolved restriction | `0` | Provision of light (Lux) |
| `222` | `431` | `2389` | `TYPE_OF_REGULATION` | `3` = Stereo amplifiers only | `1` | Regulation type; reusable default `1` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

### Product interpretation and source differences

| Surface | Catalogue / implementation | Published product source | Interpretation |
| --- | --- | --- | --- |
| `A`/`PL` | domain includes `0..9` | physical values documented as `1..9` | preserve scope difference |
| `S` | domain `0..4` | physical selector `0..3` | preserve source discrepancy |
| Candidate Objects | `119`/`164`/`165` lack explicit condition rows | no complete printed branch mapping | reachability remains to be corroborated |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 43`, brand/line and installed configurator count | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 30` | corroborate the selected slot-1 sensor Object and sixteen fixed IR Objects | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect Module address/context | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration and compare physical/virtual domains | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The selected slot-1 sensor role participates in lighting presence/daylight control or scenario-oriented sensing. Slots `2..17` are fixed IR scenario-control Modules. Generic lighting/scenario semantics remain canonical under Functional Protocol.

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

Choose the installation context before commissioning: Lighting Management Plug & Go/Push & Learn/Virtual Configurator and MyHOME physical/software setup are distinct procedures. The K4659 2019 sheet gives MyHOME_Up firmware after 2.1/app after 2.2 and MyHOME_Suite after 03.03.73; these requirements are source-scoped and do not supply firmware-222 applicability values.

Physical A/`PL=0` are excluded by both sheets despite their presence in the catalogue. Published S ends at 3 while the firmware domain includes 4. `M=1/2` excludes S/T configurators and GEN/AMB/GR addressing; use `M=2` for MH200N sensor signals. `M=3/4` needs a dimmer for constant-brightness regulation, and `M=4` does not automatically switch on after daylight falls.

Factory reset is a brief LEARN press followed by a ten-second LEARN hold until rapid flashing. Configuration-remote IR commands are acknowledged by a beep. Lux calibration needs a meter and separate artificial/natural-light stages. Walkthrough shortens detection under twenty seconds to three minutes (leaving an already shorter delay unchanged); Eco has a thirty-second retrigger interval. See the settings/configuration pages cited above. Confirm runtime Object selection before using the stored seventeen-Module model as a write target.

## Source reconciliation

The PIR-only sensor documentation has been reconciled beyond the physical `M/S/T/D` selectors.

Product-level settings include Walkthrough and Eco/manual-on behavior, detection-stage choices, switch-off warning, brightness calibration/adjustment, natural-light contribution, software/remote configuration and reset/learning workflows. These settings explain behavior available through the sensor Object configuration surface that is not representable by the six physical sockets alone.

The known source discrepancy in the physical sensitivity domain remains visible, and Objects without explicit physical condition rows remain alternatives requiring configuration/hardware corroboration rather than guessed mappings.

The legacy French sheet is dated 22 April 2014 and the K4659 English sheet 24 April 2019. Both specify 15 mA and the same temperature/settings ranges; the latter adds app/software requirements in its own scope. Both contain a PIR/US sensitivity footnote despite naming only PIR hardware. Their Auto paragraph says switch-off when natural light is insufficient, whereas their Adjustment explanation says switch-off after the threshold is exceeded; that internal wording conflict is not turned into a universal algorithm. Physical no-configurator sensitivity Low and remote default Very high are different setup scopes.

ST-00002122-EN is a Classe 300EOS compatibility source dated 21 October 2024, not a PIR technical sheet. Its p. 8 names the legacy PIR references (including 078485) with all-production-batch entries; p. 11’s configuration-tool matrix names only L/N/NT4659N. Neither matrix establishes universal variant hardware equivalence or new firmware topology.

## Evidence limits and open work

- Obtain a sanitized fingerprint from at least one legacy reference and one K4659.
- Verify the observed 17-Module `DIMENSION 30` projection.
- Corroborate the actual physical-configurator count and the `S` domain.
- Establish the precise reachability of Objects `119`, `164` and `165`, which have no explicit slot-condition rows.
- Archive further language and historical revisions of the PIR sheet.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)

- `HC4659-ean-product-sheet.pdf`, printed/PDF p. 2: exact `HC4659` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/9f/7d/9f7d840c36727261a89dd6d026f33b79acc2861d48e94f1d85d786c5c9ef1d80.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4659); SHA-256 `9f7d840c36727261a89dd6d026f33b79acc2861d48e94f1d85d786c5c9ef1d80`.
- `HS4659-ean-product-sheet.pdf`, printed/PDF p. 2: exact `HS4659` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/df/2d/df2dea652da781c312db2d963b197adc2f313f5633ec5028ba80f97a06b5deb8.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4659); SHA-256 `df2dea652da781c312db2d963b197adc2f313f5633ec5028ba80f97a06b5deb8`.
- `HD4659-ean-international-sheet.pdf`, printed/PDF p. 1: exact `HD4659` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/26/08/2608ba817cda34281dafdd102548acb329e4be97b3ecd319b3c9b1e2197a49ac.pdf); [publisher source](https://www.bticino.com/products/pdf?sku=BT-HD4659&include_technical=1); SHA-256 `2608ba817cda34281dafdd102548acb329e4be97b3ecd319b3c9b1e2197a49ac`.
- `L4659N-ean-product-sheet.pdf`, printed/PDF p. 2: exact `L4659N` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/b4/af/b4aff92b26cbcdb644511a58da6aea791b8f19790471fbbde4c4c72f11100aec.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4659N); SHA-256 `b4aff92b26cbcdb644511a58da6aea791b8f19790471fbbde4c4c72f11100aec`.
- `N4659N-ean-product-sheet.pdf`, printed/PDF p. 2: exact `N4659N` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/47/e8/47e88293946a5581746597e216733aa1957ad35008f89577fa826cc44823cd56.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-N4659N); SHA-256 `47e88293946a5581746597e216733aa1957ad35008f89577fa826cc44823cd56`.
- `NT4659N-ean-product-sheet.pdf`, printed/PDF p. 2: exact `NT4659N` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/cd/08/cd08a718bffc6184903788616984ed518e05261f7e5e09798a26887234c42c95.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-NT4659N); SHA-256 `cd08a718bffc6184903788616984ed518e05261f7e5e09798a26887234c42c95`.
- `AM5659-ean-product-sheet.pdf`, printed/PDF p. 2: exact `AM5659` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/cc/92/cc92a40fdbb0f207d702b99520a77e212715039128b670f24c75a347a3fd09a8.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5659); SHA-256 `cc92a40fdbb0f207d702b99520a77e212715039128b670f24c75a347a3fd09a8`.
- `K4659-ean-product-sheet.pdf`, printed/PDF p. 2: exact `K4659` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/ca/e8/cae8772d9a0897b5859445a97a12bf036ce058d31702fcbf9143dff3a2387eef.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-K4659); SHA-256 `cae8772d9a0897b5859445a97a12bf036ce058d31702fcbf9143dff3a2387eef`.

- `067225-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `067225` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/b6/bc/b6bc990f93ddce1dc166caf79f8a05bd2e935943aae095964a6dd5331c46cc6d.pdf); [publisher source](https://www.legrand.fr/pro/catalogue/detecteur-de-mouvements-bus-celiane-presence-et-luminosite-pour-lieux-de-passage); SHA-256 `b6bc990f93ddce1dc166caf79f8a05bd2e935943aae095964a6dd5331c46cc6d`.
- `078485-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `078485` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/16/ef/16ef087c09c291616f2a7238d97f37e360715677fcf1df59730b4d957bca6839.pdf); [publisher source](https://www.legrand.fr/pro/catalogue/detecteur-de-mouvements-bus-mosaic-presence-et-luminosite-pour-lieux-de-passage-blanc); SHA-256 `16ef087c09c291616f2a7238d97f37e360715677fcf1df59730b4d957bca6839`.

- [Semantic review record, 5 October 2026](../../project/review/device-reviews-0011-0020-2026-10-05.md#own-dev-0016)
