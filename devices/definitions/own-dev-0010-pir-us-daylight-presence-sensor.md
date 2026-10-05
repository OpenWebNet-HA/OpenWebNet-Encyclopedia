# PIR+US daylight and presence sensor

## Summary


| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0010` | Project identity |
| Technical description | Flush-mounted dual-technology PIR+ultrasound presence and daylight sensor with IR scenario-control projection | Catalogue + official technical sheets |
| Catalogue item | `1559` - “PIR+US flush mounted sensor” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `44` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `220` | Implementation evidence |
| Declared Modules | `17` | Implementation evidence |
| Categories | Sensor, Lighting, Scenario | Capability model |

The Device combines PIR and ultrasonic presence detection with a brightness sensor, local `ON`/`OFF` and learning controls, and an IR transmitter. The canonical firmware projects one configurable sensor Module plus sixteen fixed IR scenario-control Modules.

## Commercial identities


The current 2024 official technical sheet directly names the complete 12-record catalogue cluster:

| Brand / line | References |
| --- | --- |
| BTicino Axolute | `HC/HS/HD4658` |
| BTicino L/N/NT | `L/N/NT4658N` |
| BTicino Light Now | `YD4658`, `YG4658`, `YW4658` |
| BTicino Matix | `AM5658` |
| Legrand Arteor Advance / catalogue Eden Park line | `AC5220MB`, `AC5220MW` |
| Legrand | `067226`, `078486`, `574048`, `574098` |

The current product page markets AC5220MB/MW under Arteor Advance, while MyHOME Suite 3.5.38 assigns those records to the stored line name “Eden Park”. Preserve the source-version naming difference.

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `HC4658` | `8005543442524` | [Archived original](https://archive.openwebnet-ha.org/sha256/aa/7f/aa7fa0b3bce43693009aea9136320416afbb4fab83d3880908021b766ccf7d45.pdf), `HC4658-ean-product-sheet.pdf`, printed/PDF p. 2 |
| `HS4658` | `8005543442562` | [Archived original](https://archive.openwebnet-ha.org/sha256/0a/15/0a153990e83287b94526e36feecde775e664c5e634a9aa33d917b1571fa0f61f.pdf), `HS4658-ean-product-sheet.pdf`, printed/PDF p. 2 |
| `HD4658` | `8005543442609` | [Archived original](https://archive.openwebnet-ha.org/sha256/64/e3/64e311e2bf7371107fef4cd3c2a33afc2ab5d40ccbeb72884bc871e5e8b93b80.pdf), `HD4658-ean-product-sheet.pdf`, printed/PDF p. 2 |
| `L4658N` | `8005543441961` | [Archived original](https://archive.openwebnet-ha.org/sha256/68/2b/682b46c7c474ceaca8ff2f8899bbedf6c14be38977d30a45eac23907302cd9f7.pdf), `L4658N-ean-product-sheet.pdf`, printed/PDF p. 2 |
| `N4658N` | `8005543442005` | [Archived original](https://archive.openwebnet-ha.org/sha256/85/23/8523c991b311a636335f0974bca50973f46ae9d768761137d9ff5eeba14b7940.pdf), `N4658N-ean-product-sheet.pdf`, printed/PDF p. 2 |
| `NT4658N` | `8005543442647` | [Archived original](https://archive.openwebnet-ha.org/sha256/0e/1f/0e1f6b5065f9ed3dbc25cbf3be064ec19f966b7f070b432bbc6180c3a39a2316.pdf), `NT4658N-ean-product-sheet.pdf`, printed/PDF p. 2 |
| `YD4658` | `8005543768471` | [Archived original](https://archive.openwebnet-ha.org/sha256/96/dc/96dc33285b03b8d77ab621a315c0633d629b4fbd518725abd67b79dac88703cb.pdf), `YD4658-ean-international-sheet.pdf`, printed/PDF p. 1 |
| `YG4658` | `8005543768464` | [Archived original](https://archive.openwebnet-ha.org/sha256/c0/a8/c0a8254394799a7af11923420a41d7d2f2ab16a35ab9d140a4ace748e00b80e6.pdf), `YG4658-ean-international-sheet.pdf`, printed/PDF p. 1 |
| `YW4658` | `8005543768457` | [Archived original](https://archive.openwebnet-ha.org/sha256/73/f4/73f4eccbb21e626ef821bbd042f25f5e75fa7e7f86293f5cd14d8226a9f1919a.pdf), `YW4658-ean-international-sheet.pdf`, printed/PDF p. 1 |
| `AM5658` | `8005543479001` | [Archived original](https://archive.openwebnet-ha.org/sha256/f7/22/f722c6cc24129d14c170ee752e06083de4f453bf68cf990a29ee07d255a1bcf3.pdf), `AM5658-ean-product-sheet.pdf`, printed/PDF p. 2 |
| `067226` | `3245060672263` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/11/9b/119bcd106a380cdd76747dc36d8b7bc668e6727c0d920bb427722264e00fd9a3.pdf), `067226-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |
| `078486` | `3245060784867` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/61/51/6151ca609a993f0b555f467f923c3194f91703896a257030019784625901b5d1.pdf), `078486-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00473-f-EN` | official source | 09/06/2014 | six earlier references | [Archived PDF](https://archive.openwebnet-ha.org/sha256/9c/4f/9c4fc06a61797a3cd4f1b16ad4254b419d6e1adaf51e28c374a2bd793af4b748.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00473-f-EN.pdf) |
| `MQ00473-f-FR` | official source | 22/04/2014 | six earlier references | [Archived PDF](https://archive.openwebnet-ha.org/sha256/d2/a6/d2a68430ce079fdc114d349efc8033881ac8b6a3ab1276262ec18108afb216b2.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00473-f-FR.pdf) |
| `ST-00001844-EN` | official source | 12/08/2024 | all 12 current cluster references | [Archived PDF](https://archive.openwebnet-ha.org/sha256/ba/24/ba24bdc0f0bf1f928eb531117c566d79ef03f4f7624bc457c08a93d256375ab9.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00001844-EN.pdf) |
| `ST-00001844-FR` | official source | 12/08/2024 | all 12 current cluster references | [Archived PDF](https://archive.openwebnet-ha.org/sha256/10/57/1057c84858e3c3c6df455a9899b3a044d25b9a7f4a5406e75f6ade4abedafa6e.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00001844-FR.pdf) |
| `LE15098AA` | official source | revision to verify | current family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/8d/e1/8de1235d87a640ef54121e54709092d8a6d05e6a083c919a5b67b341dff23920.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE15098AA.pdf) |
| `HC4658-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HC4658` to EAN-13 relationship at printed/PDF p. 2. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/aa/7f/aa7fa0b3bce43693009aea9136320416afbb4fab83d3880908021b766ccf7d45.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4658) |
| `HS4658-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HS4658` to EAN-13 relationship at printed/PDF p. 2. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/0a/15/0a153990e83287b94526e36feecde775e664c5e634a9aa33d917b1571fa0f61f.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4658) |
| `HD4658-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HD4658` to EAN-13 relationship at printed/PDF p. 2. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/64/e3/64e311e2bf7371107fef4cd3c2a33afc2ab5d40ccbeb72884bc871e5e8b93b80.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HD4658) |
| `L4658N-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `L4658N` to EAN-13 relationship at printed/PDF p. 2. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/68/2b/682b46c7c474ceaca8ff2f8899bbedf6c14be38977d30a45eac23907302cd9f7.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4658N) |
| `N4658N-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `N4658N` to EAN-13 relationship at printed/PDF p. 2. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/85/23/8523c991b311a636335f0974bca50973f46ae9d768761137d9ff5eeba14b7940.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-N4658N) |
| `NT4658N-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `NT4658N` to EAN-13 relationship at printed/PDF p. 2. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/0e/1f/0e1f6b5065f9ed3dbc25cbf3be064ec19f966b7f070b432bbc6180c3a39a2316.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-NT4658N) |
| `YD4658-ean-international-sheet.pdf` | English manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `YD4658` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/96/dc/96dc33285b03b8d77ab621a315c0633d629b4fbd518725abd67b79dac88703cb.pdf) | [Publisher source](https://www.bticino.com/products/pdf?sku=BT-YD4658&include_technical=1) |
| `YG4658-ean-international-sheet.pdf` | English manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `YG4658` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/c0/a8/c0a8254394799a7af11923420a41d7d2f2ab16a35ab9d140a4ace748e00b80e6.pdf) | [Publisher source](https://www.bticino.com/products/pdf?sku=BT-YG4658&include_technical=1) |
| `YW4658-ean-international-sheet.pdf` | English manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `YW4658` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/73/f4/73f4eccbb21e626ef821bbd042f25f5e75fa7e7f86293f5cd14d8226a9f1919a.pdf) | [Publisher source](https://www.bticino.com/products/pdf?sku=BT-YW4658&include_technical=1) |
| `AM5658-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `AM5658` to EAN-13 relationship at printed/PDF p. 2. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/f7/22/f722c6cc24129d14c170ee752e06083de4f453bf68cf990a29ee07d255a1bcf3.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5658) |
| `067226-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `067226` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/11/9b/119bcd106a380cdd76747dc36d8b7bc668e6727c0d920bb427722264e00fd9a3.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue/detecteur-de-mouvements-bus-celiane-presence-et-luminosite-pour-espace-de-travail-avec-poussoir) |
| `078486-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `078486` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/61/51/6151ca609a993f0b555f467f923c3194f91703896a257030019784625901b5d1.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue/detecteur-de-mouvements-bus-mosaic-presence-et-luminosite-pour-espace-de-travail-avec-poussoir-blanc) |

### Material revision difference

The 2014 English sheet specifies `17 mA` current draw. The 2024 successor specifies `15 mA`.

Both originals are retained because this may represent a product revision, documentation correction, or later hardware family expansion. Do not collapse the values into one timeless specification.

The 2024 sheet also updates the software-configuration workflow from MyHOME Suite to Home + Project while explicitly retaining physical configuration.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 flush-mounted modules | Publisher documentation cited in this section |
| Supply | `27 Vdc` | Publisher documentation cited in this section |
| Current draw | `15 mA` in the 2024 sheet | Publisher documentation cited in this section |
| Detection technology | PIR + ultrasound, 180° | Publisher documentation cited in this section |
| Brightness sensor | integrated | Publisher documentation cited in this section |
| Front controls | `ON`/`OFF` button + LEARN button / LED | Publisher documentation cited in this section |
| IR | integrated transmitter | Publisher documentation cited in this section |
| Flush box depth | `40 mm` | Publisher documentation cited in this section |
| Weight | `60 g` | Publisher documentation cited in this section |
| Impact protection | `IK04` | Publisher documentation cited in this section |
| Ingress protection | `IP20` | Publisher documentation cited in this section |
| Time-delay range | `5 s .. 59 min 59 s` | Publisher documentation cited in this section |
| Brightness range | `20 .. 1275 lux` | Publisher documentation cited in this section |
| Operating temperature | `-5 .. +45 °C` | Publisher documentation cited in this section |
| Storage temperature | `-20 .. +70 °C` | Publisher documentation cited in this section |
| Physical configurator sockets | `A`, `PL`, `M`, `S`, `T`, `D` | Publisher documentation cited in this section |

The 2024 sheet establishes:


The six documented sockets independently support the expected ordinary addressed-form configurator count, pending hardware corroboration.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1559` | Canonical catalogue |
| Item model / `modobj` | `44` | Canonical catalogue / retained definition |
| Main system | Lighting / Automation | Canonical catalogue / retained definition |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `220` | `-1` | `-1` | `-1` | `17` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `220` | `1` | `119` Stand alone presence sensor | Candidate alternative | `2594` | `119` | `1211` |
| `220` | `1` | `128` Scenarios daylight and presence sensor | Fixed/designated metadata | `2595` | `128` | `1212` |
| `220` | `1` | `164` Scenarios daylight sensor | Candidate alternative | `2596` | `164` | `1213` |
| `220` | `1` | `165` Scenarios presence sensor | Candidate alternative | `2597` | `165` | `1214` |
| `220` | `1` | `166` Stand alone daylight sensor | Candidate alternative | `2598` | `166` | `1215` |
| `220` | `1` | `168` Stand alone daylight and presence sensor | Candidate alternative | `2599` | `168` | `1216` |
| `220` | `2` | `431` IR scenario control | Fixed/designated metadata | `1021` | `431` | `611` |
| `220` | `3` | `431` IR scenario control | Fixed/designated metadata | `1022` | `431` | `611` |
| `220` | `4` | `431` IR scenario control | Fixed/designated metadata | `1023` | `431` | `611` |
| `220` | `5` | `431` IR scenario control | Fixed/designated metadata | `1024` | `431` | `611` |
| `220` | `6` | `431` IR scenario control | Fixed/designated metadata | `1025` | `431` | `611` |
| `220` | `7` | `431` IR scenario control | Fixed/designated metadata | `1026` | `431` | `611` |
| `220` | `8` | `431` IR scenario control | Fixed/designated metadata | `1027` | `431` | `611` |
| `220` | `9` | `431` IR scenario control | Fixed/designated metadata | `1028` | `431` | `611` |
| `220` | `10` | `431` IR scenario control | Fixed/designated metadata | `1029` | `431` | `611` |
| `220` | `11` | `431` IR scenario control | Fixed/designated metadata | `1030` | `431` | `611` |
| `220` | `12` | `431` IR scenario control | Fixed/designated metadata | `1031` | `431` | `611` |
| `220` | `13` | `431` IR scenario control | Fixed/designated metadata | `1032` | `431` | `611` |
| `220` | `14` | `431` IR scenario control | Fixed/designated metadata | `1033` | `431` | `611` |
| `220` | `15` | `431` IR scenario control | Fixed/designated metadata | `1034` | `431` | `611` |
| `220` | `16` | `431` IR scenario control | Fixed/designated metadata | `1035` | `431` | `611` |
| `220` | `17` | `431` IR scenario control | Fixed/designated metadata | `1036` | `431` | `611` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

### Reconciled topology notes


### Slot 1 - sensing role

The firmware offers these sensor Objects on slot `1`:

| Object | Description | Physical-condition evidence |
| ---: | --- | --- |
| `119` | Stand alone presence sensor | no firmware condition row |
| `128` | Scenarios daylight and presence sensor | `M=2` |
| `164` | Scenarios daylight sensor | no firmware condition row |
| `165` | Scenarios presence sensor | no firmware condition row |
| `166` | Stand alone daylight sensor | `M=1` or `M=4` |
| `168` | Stand alone daylight and presence sensor | `M=0` or `M=3`; designated Object |

Objects without physical condition rows remain valid catalogue alternatives for virtual/advanced configuration; they must not be declared unreachable solely because the physical-condition table does not select them.

### Slots `2..17` - IR scenario controls

Object `431`, **IR scenario control**, is fixed on slots `2..17`, producing sixteen scenario-control Modules.

Its reusable parameters are:

- scenario number `1..255`;
- regulation type: all, lights only, shutters only, stereo amplifiers only;
- identifier fields `ID1 0..255`, `ID2 0..255`, `ID3 0..15`;
- unit/pushbutton number `0..15`.

This is why the Device has 17 catalogue Modules despite appearing physically as one sensor.

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `220` | Catalogue configuration route(s) described in retained notes | retained Device-specific configuration modality |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `220` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `220` | `A` | `0..9` | `0` | A; Environment |
| `220` | `PL` | `0..9` | `0` | PL; Light Point |
| `220` | `M` | `0..4` | `0` | M; Mode 0-4 |
| `220` | `S` | `0..4` | `0` | S; Configurator S (0-4) |
| `220` | `T` | `0..9` | `0` | T; Configurator T (time) - (0-9) |
| `220` | `D` | `0..5` | `0` | D; (0-5) |




### Published and reconciled details


| Field | Catalogue domain | Published physical meaning |
| --- | --- | --- |
| `AID` | Device identity | not a physical configurator |
| `A` | `0..9` | physical `1..9`; environment/address |
| `PL` | `0..9` | physical `1..9`; light point |
| `M` | `0..4` | operating mode |
| `S` | `0..4` | movement sensitivity; published physical values no-configurator / `1..3` |
| `T` | `0..9` | timeout preset |
| `D` | `0..5` | daylight threshold preset |

The sheets explicitly state that physical addresses `A=0` and `PL=0` do not exist even though the firmware database stores zero in the underlying ranges.

### Physical timeout and sensitivity mappings

| `T` | Timeout |
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

| `S` | PIR sensitivity |
| ---: | --- |
| no configurator | Low |
| `1` | Medium |
| `2` | High |
| `3` | Very high |

| `D` | Brightness threshold |
| ---: | ---: |
| no configurator | 300 lux |
| `1` | 20 lux |
| `2` | 100 lux |
| `3` | 300 lux |
| `4` | 500 lux |
| `5` | 1000 lux |

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


### Reconciled Object notes

The reusable sensor Objects extend substantially beyond the six physical sockets.

| Object family | Reconciled configuration surface |
| --- | --- |
| Presence-oriented `119`, `128`, `165` | point/group addressing; hours/minutes/seconds delay; PIR and ultrasound sensitivity; PIR/US detection scheme; initial/maintain/retrigger selection where applicable; automatic, walkthrough, manual-`ON`/auto-`OFF` and partial/group modes; visual/acoustic alert; optional load-control enablement |
| Daylight `166` | point/group and reference-actuator addressing; open/closed-loop regulation; daylight cell group; daylight setpoint in 5-lux increments over `0..1275 lux`; light contribution from Automatic through `5..1275 lux`; auto/manual/partial modes; lighting-regulation enablement; read-only daylight/natural-light factors and measured daylight level |
| Combined daylight/presence `168` | up to two sensor groups; time delay; auto `ON`/`OFF`, walkthrough, manual `ON`/auto `OFF` and partial/group modes; PIR/US sensitivities; initial/maintain/retrigger selection; visual/acoustic alerts; load-control and lighting-regulation settings; read-only light-factor measurements |

The published 2024 sheet independently documents remote-control adjustment of delay, PIR/US detection scheme, brightness threshold, Auto/Walkthrough/Eco modes, alarm, calibration, adjustment, and contribution-of-light behavior.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `220` | `1` | `128` | `4477` | `M=2` | None |
| `220` | `1` | `166` | `4461` | `M=1` | None |
| `220` | `1` | `166` | `4505` | `M=4` | None |
| `220` | `1` | `168` | `4439` | `M=0` | None |
| `220` | `1` | `168` | `4491` | `M=3` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `220` | `119` | `2221` | `ALERT` | `1` = Visual; `3` = Visual and Acoustic | `0` | Alert; reusable default `0` is outside this subset; filter supplies no replacement default |
| `220` | `166` | `2225` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `220` | `166` | `2226` | `NATURAL_LIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Natural light factor |
| `220` | `166` | `2227` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `220` | `168` | `2222` | `ALERT` | `1` = Visual; `3` = Visual and Acoustic | `0` | Alert; reusable default `0` is outside this subset; filter supplies no replacement default |
| `220` | `168` | `2223` | `NATURAL_LIGHT_FACTOR` | `1..255` (entire reusable range retained) | `10` | Natural light factor |
| `220` | `168` | `2224` | `DAYLIGHT_FACTOR` | `0..255` (entire reusable range retained) | `0` | Daylight factor |
| `220` | `168` | `2374` | `DAYLIGHT_LEVEL` | `0..255` (entire reusable range retained) | `0` | Daylight level |
| `220` | `168` | `2455` | `DAYLIGHT_SETPOINT` | Subset flag present but no allowed values stored; unresolved restriction | `100` | Daylight setpoint (Lux) |
| `220` | `168` | `2467` | `PROVISION_OF_LIGHT` | Subset flag present but no allowed values stored; unresolved restriction | `0` | Provision of light (Lux) |
| `220` | `431` | `2387` | `TYPE_OF_REGULATION` | `3` = Stereo amplifiers only | `1` | Regulation type; reusable default `1` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1559` and the installed model | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware without treating wildcard sentinels as literal installed values | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`119`, `128`, `164`, `165`, `166`, `168`, `431`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions, and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

### Existing Device-specific diagnostic notes


| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 44`, commercial identity fields and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | enumerate one sensor Object plus sixteen IR scenario-control Objects | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | resolve sensor/scenario addressing | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/virtual/advanced configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Functional applicability follows the resolved firmware/Object topology and the documented product roles above.

## Observed behavior and corroboration

No additional publishable runtime observation is asserted beyond observations explicitly retained elsewhere on this page.

## Programming

Programming must validate firmware applicability, active Module/Object topology, relation filters, and Device-specific configuration constraints.

## Source reconciliation


The archived 2014/2024 PIR+US material has been reconciled beyond the basic `M/S/T/D` configurator table.

The product-level configuration surface additionally includes:

- Auto and Walkthrough occupancy behaviors;
- Eco/manual-on behavior and switch-off warning;
- Initial, Holding and Retrigger detection-stage choices;
- brightness calibration/adjustment and natural-light contribution;
- software/remote configuration paths in addition to physical configurators;
- product reset and learning/programming workflows;
- revision-dependent software tooling, including the transition from MyHOME Suite-era configuration to Home + Project while retaining physical setup.

These settings explain why reusable sensor Objects expose more behavior than the six physical sockets alone. They remain product-level semantics and should not be collapsed into one generic presence-sensor mode.

## Evidence limits and open work


- Obtain a sanitized fingerprint from known hardware and verify the unusual 17-Module projection.
- Correlate old and new production batches with the 17 mA versus 15 mA documentation difference.
- Determine whether all 12 commercial variants share identical hardware or whether the current technical sheet intentionally spans revised electronics.
- Corroborate the six physical configurator positions and slot-1 mode selection through diagnostics.
- Record real-world IR scenario Object behavior for slots `2..17`.

## Sources


- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
- [Programming](../../programming/)

- `HC4658-ean-product-sheet.pdf`, printed/PDF p. 2: exact `HC4658` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/aa/7f/aa7fa0b3bce43693009aea9136320416afbb4fab83d3880908021b766ccf7d45.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4658); SHA-256 `aa7fa0b3bce43693009aea9136320416afbb4fab83d3880908021b766ccf7d45`.
- `HS4658-ean-product-sheet.pdf`, printed/PDF p. 2: exact `HS4658` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/0a/15/0a153990e83287b94526e36feecde775e664c5e634a9aa33d917b1571fa0f61f.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4658); SHA-256 `0a153990e83287b94526e36feecde775e664c5e634a9aa33d917b1571fa0f61f`.
- `HD4658-ean-product-sheet.pdf`, printed/PDF p. 2: exact `HD4658` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/64/e3/64e311e2bf7371107fef4cd3c2a33afc2ab5d40ccbeb72884bc871e5e8b93b80.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HD4658); SHA-256 `64e311e2bf7371107fef4cd3c2a33afc2ab5d40ccbeb72884bc871e5e8b93b80`.
- `L4658N-ean-product-sheet.pdf`, printed/PDF p. 2: exact `L4658N` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/68/2b/682b46c7c474ceaca8ff2f8899bbedf6c14be38977d30a45eac23907302cd9f7.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4658N); SHA-256 `682b46c7c474ceaca8ff2f8899bbedf6c14be38977d30a45eac23907302cd9f7`.
- `N4658N-ean-product-sheet.pdf`, printed/PDF p. 2: exact `N4658N` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/85/23/8523c991b311a636335f0974bca50973f46ae9d768761137d9ff5eeba14b7940.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-N4658N); SHA-256 `8523c991b311a636335f0974bca50973f46ae9d768761137d9ff5eeba14b7940`.
- `NT4658N-ean-product-sheet.pdf`, printed/PDF p. 2: exact `NT4658N` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/0e/1f/0e1f6b5065f9ed3dbc25cbf3be064ec19f966b7f070b432bbc6180c3a39a2316.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-NT4658N); SHA-256 `0e1f6b5065f9ed3dbc25cbf3be064ec19f966b7f070b432bbc6180c3a39a2316`.
- `YD4658-ean-international-sheet.pdf`, printed/PDF p. 1: exact `YD4658` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/96/dc/96dc33285b03b8d77ab621a315c0633d629b4fbd518725abd67b79dac88703cb.pdf); [publisher source](https://www.bticino.com/products/pdf?sku=BT-YD4658&include_technical=1); SHA-256 `96dc33285b03b8d77ab621a315c0633d629b4fbd518725abd67b79dac88703cb`.
- `YG4658-ean-international-sheet.pdf`, printed/PDF p. 1: exact `YG4658` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/c0/a8/c0a8254394799a7af11923420a41d7d2f2ab16a35ab9d140a4ace748e00b80e6.pdf); [publisher source](https://www.bticino.com/products/pdf?sku=BT-YG4658&include_technical=1); SHA-256 `c0a8254394799a7af11923420a41d7d2f2ab16a35ab9d140a4ace748e00b80e6`.
- `YW4658-ean-international-sheet.pdf`, printed/PDF p. 1: exact `YW4658` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/73/f4/73f4eccbb21e626ef821bbd042f25f5e75fa7e7f86293f5cd14d8226a9f1919a.pdf); [publisher source](https://www.bticino.com/products/pdf?sku=BT-YW4658&include_technical=1); SHA-256 `73f4eccbb21e626ef821bbd042f25f5e75fa7e7f86293f5cd14d8226a9f1919a`.
- `AM5658-ean-product-sheet.pdf`, printed/PDF p. 2: exact `AM5658` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/f7/22/f722c6cc24129d14c170ee752e06083de4f453bf68cf990a29ee07d255a1bcf3.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5658); SHA-256 `f722c6cc24129d14c170ee752e06083de4f453bf68cf990a29ee07d255a1bcf3`.

- `067226-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `067226` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/11/9b/119bcd106a380cdd76747dc36d8b7bc668e6727c0d920bb427722264e00fd9a3.pdf); [publisher source](https://www.legrand.fr/pro/catalogue/detecteur-de-mouvements-bus-celiane-presence-et-luminosite-pour-espace-de-travail-avec-poussoir); SHA-256 `119bcd106a380cdd76747dc36d8b7bc668e6727c0d920bb427722264e00fd9a3`.
- `078486-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `078486` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/61/51/6151ca609a993f0b555f467f923c3194f91703896a257030019784625901b5d1.pdf); [publisher source](https://www.legrand.fr/pro/catalogue/detecteur-de-mouvements-bus-mosaic-presence-et-luminosite-pour-espace-de-travail-avec-poussoir-blanc); SHA-256 `6151ca609a993f0b555f467f923c3194f91703896a257030019784625901b5d1`.
