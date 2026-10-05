# Two-module zero-crossing actuator and control

## Summary


| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0006` | Project identity |
| Technical description | Two-module two-relay actuator with integrated command functions and zero-crossing switching | Catalogue + official technical sheet |
| Catalogue item | `2180` - “Flush mounted actuator and free control with zero crossing” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `82` | Implementation evidence |
| Firmware definition | `1.0.-1` wildcard-build applicability, firmware `707` | Implementation evidence |
| Declared Modules | `4` | Implementation evidence |
| Categories | Actuator, Command, Multifunction, Lighting, Automation, Scenario | Capability model |

Item `2180` is the zero-crossing counterpart of the multifunction actuator/control family. It contains two independent relays and front controls, and can expose actuator functions on slots `1..2` plus command/scenario functions on slots `3..4`.

The official 2021 technical sheet directly documents all seven commercial references in the current catalogue cluster.

## Commercial identities


| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Arnould - Espace Evolution | `64195` | Documented commercial reference | Catalogue + official technical sheet |
| Arnould - Espace Evolution | `64196` | Documented commercial reference | Catalogue + official technical sheet |
| Arnould - Espace Evolution | `64393` | Documented commercial reference | Catalogue + official technical sheet |
| BTicino - Axolute | `H4672M2` | Documented commercial reference | Catalogue + official technical sheet |
| BTicino - LivingLight | `LN4672M2` | Documented commercial reference | Catalogue + official technical sheet |
| BTicino - Matix | `AM5852M2` | Documented commercial reference | Catalogue + official technical sheet |
| Legrand - Céliane | `067561` / printed `0 675 61` | Documented commercial reference | Catalogue + official technical sheet |

Shared item membership and the common technical sheet jointly establish this commercial-identity set. Range-specific dimensions and packaging remain commercial metadata.

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `H4672M2` | `8005543560860` | [Archived original](https://archive.openwebnet-ha.org/sha256/57/52/575284f0fb0bde456e0e5122bbf632c2e03739d15658ba7533e3a93b83ba94f7.pdf), `H4672M2-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `LN4672M2` | `8005543560532` | [Archived original](https://archive.openwebnet-ha.org/sha256/6b/19/6b19c5a1e1d740e4fd4168bccb23f77109a45c4d988d1b444e313ccb64c1a4a5.pdf), `LN4672M2-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `AM5852M2` | `8005543560525` | [Archived original](https://archive.openwebnet-ha.org/sha256/c3/f4/c3f44f472988b7718fe4ad50aa3ae512aa004e2f532391ea983bf2775bc23315.pdf), `AM5852M2-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ST-00000898-EN` | Technical sheet | 23/03/2021 | all seven references | [Archived PDF](https://archive.openwebnet-ha.org/sha256/4e/7b/4e7b78e4a7051d0e1c634dd8a412e4f429be925de5801a40b7781fdc441f3896.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00000898-EN.pdf) |
| `ST-00000898-FR` | Technical sheet | 23/03/2021 | all seven references | [Archived PDF](https://archive.openwebnet-ha.org/sha256/9f/b9/9fb9cdac69b9bf9763961763a55ea357d8dd8340f6063d053273f5fcc477e7e9.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00000898-FR.pdf) |
| `LE09285AB` | Instruction sheet | 03/21 | `AM5852M2`, `H4672M2`, `LN4672M2` | [Archived PDF](https://archive.openwebnet-ha.org/sha256/a3/ac/a3ac229039a7d503d6f1dde6ea067ae95477d36005c45ec94c89348d1ab4ca7a.pdf) | [Official source](https://dar.bticino.com/asset/Documents/LE09285AB.pdf) |
| `LE09287AB` | Instruction sheet | revision not yet decoded | `067561` | [Archived PDF](https://archive.openwebnet-ha.org/sha256/fd/d9/fdd9607fac4470e3c1d97d25041f9f840ee116f02525c8e7fba9bcfceb5e7b04.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE09287AB.pdf) |
| `H4672M2-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `H4672M2` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/57/52/575284f0fb0bde456e0e5122bbf632c2e03739d15658ba7533e3a93b83ba94f7.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4672M2) |
| `LN4672M2-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `LN4672M2` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/6b/19/6b19c5a1e1d740e4fd4168bccb23f77109a45c4d988d1b444e313ccb64c1a4a5.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4672M2) |
| `AM5852M2-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `AM5852M2` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/c3/f4/c3f44f472988b7718fe4ad50aa3ae512aa004e2f532391ea983bf2775bc23315.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5852M2) |

The English and French technical sheets are distinct archived byte streams and therefore remain separate source revisions/language variants.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting size | 2 flush-mounted modules | Official technical sheet |
| Front controls | 4 buttons and 4 two-colour LEDs | Official technical sheet |
| Local outputs | 2 independent relays | Official technical sheet |
| SCS supply | `18..27 Vdc` | Official technical sheet |
| Current draw | `7 mA` standby; `16 mA` max with one shutter/light; `24 mA` max with two lights | Official technical sheet |
| Operating temperature | `0..40 °C` | Official technical sheet |
| Storage temperature | `-5..45 °C` | Official technical sheet |
| Mains side | `110..230 Vac`, `50..60 Hz` | Official technical sheet |
| Maximum resistive/incandescent class at 230 Vac with neutral | `1380 W / 6 A` | Official technical sheet |
| Motor/LED-CFL class at 230 Vac with neutral | `460 W / 2 A`; `250 W / 1 A` respectively | Official technical sheet |
| Fluorescent/electronic-transformer class at 230 Vac with neutral | `460 W / 2 A` | Official technical sheet |
| Ferromagnetic-transformer class at 230 Vac with neutral | `460 VA / 2 A`, cos φ 0.5 | Official technical sheet |
| Physical configurator positions | `A1`, `PL1`, `M1`, `A2`, `PL2`, `M2` | Official technical sheet |

The 2021 technical sheet establishes:


The sheet also documents reduced load limits when used without a connected neutral. Keep neutral-dependent load tables revision-scoped rather than collapsing them into one rating.

The control and contact parts are physically separable and can be wired separately.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2180` | Canonical catalogue |
| Item model / `modobj` | `82` | Canonical catalogue / retained definition |
| Main system | Lighting / Automation | Canonical catalogue / retained definition |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `707` | `1` | `0` | `-1` | `4` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `707` | `1` | `6` Light actuator | Fixed/designated metadata | `2615` | `6` | `1227` |
| `707` | `1` | `7` Automation actuator | Candidate alternative | `2608` | `7` | `1223` |
| `707` | `2` | `6` Light actuator | Fixed/designated metadata | `2616` | `6` | `1227` |
| `707` | `3` | `400` Light control | Fixed/designated metadata | `2606` | `400` | `1222` |
| `707` | `3` | `401` Automation control | Candidate alternative | `2609` | `401` | `1224` |
| `707` | `3` | `404` Scheduled scenario | Candidate alternative | `2612` | `404` | `1225` |
| `707` | `3` | `406` Scheduled scenario PLUS | Candidate alternative | `2614` | `406` | `1226` |
| `707` | `4` | `400` Light control | Fixed/designated metadata | `2607` | `400` | `1222` |
| `707` | `4` | `401` Automation control | Candidate alternative | `2610` | `401` | `1224` |
| `707` | `4` | `404` Scheduled scenario | Candidate alternative | `2611` | `404` | `1225` |
| `707` | `4` | `406` Scheduled scenario PLUS | Candidate alternative | `2613` | `406` | `1226` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `707` | `500` Automation double command virgin | `3`, `4` | `400`, `401`, `404`, `406`, `407` | `500` | `58` |
| `707` | `510` Automation relay virgin | `1`, `2` | `1`, `6`, `7` | `510` | `59` |

### Reconciled topology notes


Firmware `707` declares the same four-role structural pattern as the non-zero-crossing actuator/control family, but it is a distinct technical item and firmware definition.

| Object | Description | Slots | Relationship |
| ---: | --- | --- | --- |
| `6` | Light actuator | `1`, `2` | designated actuator Object |
| `7` | Automation actuator | `1` | alternative |
| `400` | Light control | `3`, `4` | designated command Object |
| `401` | Automation control | `3`, `4` | alternative |
| `404` | Scheduled scenario | `3`, `4` | alternative |
| `406` | Scheduled scenario PLUS | `3`, `4` | alternative |

Virgin Object `510`, **Automation relay virgin**, applies to slots `1..2` and permits Blind actuator `1`, Light actuator `6`, and Automation actuator `7`.

Virgin Object `500`, **Automation double command virgin**, applies to slots `3..4` and permits Light control `400`, Automation control `401`, Scheduled scenario `404`, Scheduled scenario PLUS `406`, and `AUX` control `407`.

Installed Object selection belongs to [`DIMENSION 30`](../../diagnostics/dim30-modules.md).

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `707` | Physical configuration | retained Device-specific configuration modality |
| `707` | Virtual Configuration | retained Device-specific configuration modality |
| `707` | Advanced Configuration | retained Device-specific configuration modality |


The catalogue declares:

- Physical configuration
- Virtual Configuration
- Advanced Configuration

The official sheet independently documents physical configuration and MyHOME Suite configuration. In virtual configuration, front-button functions can be independent from local actuator functions, and the software exposes four independent addresses: two actuator addresses and two front-control addresses.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `707` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `707` | `A1` | `0..9` | `0` | A1; Configurator A1 (0-9) |
| `707` | `PL1` | `0..9` | `0` | PL1; PL1 - (0-9) |
| `707` | `M1` | `0..8`; `9` = `O/I`; `14` = `CEN`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `10` = `OFF`; `15` = `PUL` | `0` | M1; Mode physical configurator (0-8, `O/I`,SU_GIU,SU_GIU_M,`CEN`,`OFF`,`PUL`) |
| `707` | `A2` | `0..9` | `0` | A2; Configurator A2 (0-9) |
| `707` | `PL2` | `0..9` | `0` | PL2; PL2 - (0-9) |
| `707` | `M2` | `0..8`; `9` = `O/I`; `14` = `CEN`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `10` = `OFF`; `15` = `PUL` | `0` | M2; Mode physical configurator (0-8, `O/I`,SU_GIU,SU_GIU_M,`CEN`,`OFF`,`PUL`) |




### Published and reconciled details


| Field | Catalogue domain | Role |
| --- | --- | --- |
| `AID` | Device identity field | not a physical configurator |
| `A1` | `0..9` | local actuator address |
| `PL1` | `0..9` | local actuator point |
| `M1` | `0..8`, `O/I`, `OFF`, `UP/DOWN`, `UP/DOWN monostable`, `CEN`, `PUL` | first/local mode |
| `A2` | `0..9` | second actuator or remote-control address |
| `PL2` | `0..9` | second actuator or remote-control point |
| `M2` | same stored enum as `M1` | second/remote mode |

The 2021 technical sheet uses physical `A1/A2 = 1..9` and `PL1/PL2 = 1..9` for ordinary point-to-point addressing, while virtual configuration supports room `0..10`, lighting point `0..15`, and group `0..255` ranges.

### Source irregularities

The catalogue condition matrix contains selectors that are absent from the firmware-level enum, including `M2=ON`, scope values such as `A2=GEN/GR/AMB`, and malformed/truncated condition strings. The official technical sheet independently documents `ON`, room, group, and general remote-control modes.

Preserve this as a source-model difference: the stored firmware field domain is not sufficient by itself to enumerate every condition token used by the converter.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `6` - Light actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality |
| `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open | `0` | Relay state on device reset |
| `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing | `0` | Load control mode |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `SUBTYPE` | `11` = Actuator; `1` = Lamp; `10` = Valve; `15` = Differential restart; `6` = Fan; `7` = Watering; `8` = Controlled socket; `9` = Lock | `11` | Type of load |
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


### Object `7` - Automation actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality |
| `LOCAL_BUTTON` | `12` = Bistable control; `13` = Monostable control; `14` = Bistable and blades control | `12` | Local button modality |
| `STOP_TIME` | `0` = Infinite; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min | `60` | Stop time |
| `SUBTYPE` | `11` = Actuator; `2` = Shutter; `3` = Curtain; `4` = Gate; `5` = Garage door; `15` = Differential restart | `11` | Type of load |
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


### Object `400` - Light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `1` = Timed `ON`; `2` = Toggle dimmer; `3` = `ON`/`OFF` and dimming; `4` = Toggle `ON`/`OFF`; `5` = `ON`/`OFF`; `9` = `ON`/`OFF` and point to point dimming; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90%; `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `130` = Customized `ON`/`OFF` and point to point dimmer; `131` = Customized toggle dimmer; `132` = Customized `ON`/`OFF` and dimmer; `133` = Customized toggle dimmer without regulation; `134` = Customized `ON`/`OFF` and dimmer without regulation | `0` | Modality; Standard mode means: with regulation for Point-to-point addressing, without regulation for Area, Group and General addressing |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = All systems | `0` | Destination level |
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
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |


### Object `404` - Scheduled scenario

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `BUTTON_1` | `0..31` | `1` | Upper button |
| `BUTTON_2` | `0..31` | `2` | Lower button |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |
| `START_DELAY` | `0..255` | `10` | Time of restart device (s) |


### Object `406` - Scheduled scenario PLUS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | `0..255` | `1` | Scheduled scenario PLUS number |
| `PPT_CEN_HIG` | `0..7` | `0` | Scheduled scenario PLUS number |
| `BUTTON_1` | `0..31` | `1` | Upper button |
| `BUTTON_2` | `0..31` | `2` | Lower button |


### Reconciled Object notes

The Device references reusable actuator/control Object families. Their principal structured surfaces are:

| Object | Principal configuration surface |
| --- | --- |
| `6` Light actuator | address; master/slave/`PUL` mode; local-button mode; delayed off; reset state; load-control behavior; subtype; group membership |
| `7` Automation actuator | address; actuator mode; shutter-control mode; stop time; subtype; group membership |
| `400` Light control | point/area/group/general addressing; command mode; installation/destination level; reference address; timing/dimming fields |
| `401` Automation control | point/area/group/general addressing; bistable/monostable/blades mode; installation/destination level |
| `404` Scheduled scenario | address; button numbers; `AUX` input; restart delay |
| `406` Scheduled scenario PLUS | scenario-number fields; button fields |
| `407` `AUX` control | `AUX` channel; command mode; reachable through Virgin Object `500` when conditions permit |

A reusable Object parameter is a candidate capability until the firmware condition/filter model makes it reachable for this Device.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `707` | `1` | `6` | `4145` | No textual predicate stored | None |
| `707` | `1` | `6` | `4232` | `M1=0` | `20` |
| `707` | `1` | `6` | `4239` | `M1=1` | `20` |
| `707` | `1` | `6` | `4241` | `M1=2` | `20` |
| `707` | `1` | `6` | `4243` | `M1=3` | `20` |
| `707` | `1` | `6` | `4245` | `M1=4` | `20` |
| `707` | `1` | `6` | `4256` | `M1=CEN;M2=0` | `25` |
| `707` | `1` | `6` | `4258` | `M1=CEN;M2=1` | `25` |
| `707` | `1` | `6` | `4260` | `M1=CEN;M2=2` | `25` |
| `707` | `1` | `6` | `4262` | `M1=CEN;M2=3` | `25` |
| `707` | `1` | `6` | `4264` | `M1=CEN;M2=4` | `25` |
| `707` | `1` | `6` | `4266` | `M1=CEN;M2=O/I` | `25` |
| `707` | `1` | `6` | `4268` | `M1=CEN;M2=PUL` | `25` |
| `707` | `1` | `6` | `4273` | `M1=O/I` | `20` |
| `707` | `1` | `6` | `4292` | `M1=PUL` | `20` |
| `707` | `1` | `7` | `4247` | `M1=5` | `26` |
| `707` | `1` | `7` | `4249` | `M1=6` | `26` |
| `707` | `1` | `7` | `4251` | `M1=7` | `26` |
| `707` | `1` | `7` | `4253` | `M1=8` | `26` |
| `707` | `1` | `7` | `4280` | `M1=OFF` | `26` |
| `707` | `1` | `7` | `4298` | `M1=SU_GIU` | `26` |
| `707` | `1` | `7` | `4306` | `M1=SU_GIU_M` | `26` |
| `707` | `2` | `6` | `4145` | No textual predicate stored | None |
| `707` | `2` | `6` | `4256` | `M1=CEN;M2=0` | `25` |
| `707` | `2` | `6` | `4258` | `M1=CEN;M2=1` | `25` |
| `707` | `2` | `6` | `4260` | `M1=CEN;M2=2` | `25` |
| `707` | `2` | `6` | `4262` | `M1=CEN;M2=3` | `25` |
| `707` | `2` | `6` | `4264` | `M1=CEN;M2=4` | `25` |
| `707` | `2` | `6` | `4266` | `M1=CEN;M2=O/I` | `25` |
| `707` | `2` | `6` | `4268` | `M1=CEN;M2=PUL` | `25` |
| `707` | `3` | `400` | `4145` | No textual predicate stored | None |
| `707` | `3` | `400` | `4231` | `M1=0` | `4` |
| `707` | `3` | `400` | `4238` | `M1=1` | `4` |
| `707` | `3` | `400` | `4240` | `M1=2` | `4` |
| `707` | `3` | `400` | `4242` | `M1=3` | `4` |
| `707` | `3` | `400` | `4244` | `M1=4` | `4` |
| `707` | `3` | `400` | `4255` | `M1=CEN;M2=0` | `4` |
| `707` | `3` | `400` | `4257` | `M1=CEN;M2=1` | `4` |
| `707` | `3` | `400` | `4259` | `M1=CEN;M2=2` | `4` |
| `707` | `3` | `400` | `4261` | `M1=CEN;M2=3` | `4` |
| `707` | `3` | `400` | `4263` | `M1=CEN;M2=4` | `4` |
| `707` | `3` | `400` | `4265` | `M1=CEN;M2=O/I` | `4` |
| `707` | `3` | `400` | `4267` | `M1=CEN;M2=PUL` | `4` |
| `707` | `3` | `400` | `4272` | `M1=O/I` | `4` |
| `707` | `3` | `400` | `4291` | `M1=PUL` | `4` |
| `707` | `3` | `401` | `4246` | `M1=5` | `4` |
| `707` | `3` | `401` | `4248` | `M1=6` | `4` |
| `707` | `3` | `401` | `4250` | `M1=7` | `4` |
| `707` | `3` | `401` | `4252` | `M1=8` | `4` |
| `707` | `3` | `401` | `4279` | `M1=OFF` | `4` |
| `707` | `3` | `401` | `4299` | `M1=SU_GIU` | `550` |
| `707` | `3` | `401` | `4307` | `M1=SU_GIU_M` | `550` |
| `707` | `4` | `400` | `4145` | No textual predicate stored | None |
| `707` | `4` | `400` | `4194` | `M1<>CEN;M2=0;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `707` | `4` | `400` | `4195` | `M1<>CEN;M2=0;A2=AMB` | `97` |
| `707` | `4` | `400` | `4197` | `M1<>CEN;M2=0;A2=GEN` | `95` |
| `707` | `4` | `400` | `4198` | `M1<>CEN;M2=0;A2=GR` | `96` |
| `707` | `4` | `400` | `4201` | `M1<>CEN;M2=O/I;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `707` | `4` | `400` | `4202` | `M1<>CEN;M2=O/I;A2=AMB` | `97` |
| `707` | `4` | `400` | `4204` | `M1<>CEN;M2=O/I;A2=GEN` | `95` |
| `707` | `4` | `400` | `4205` | `M1<>CEN;M2=O/I;A2=GR` | `96` |
| `707` | `4` | `400` | `4206` | `M1<>CEN;M2=OFF;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `707` | `4` | `400` | `4207` | `M1<>CEN;M2=OFF;A2=AMB` | `97` |
| `707` | `4` | `400` | `4209` | `M1<>CEN;M2=OFF;A2=GEN` | `95` |
| `707` | `4` | `400` | `4210` | `M1<>CEN;M2=OFF;A2=GR` | `96` |
| `707` | `4` | `400` | `4211` | `M1<>CEN;M2=ON;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `707` | `4` | `400` | `4212` | `M1<>CEN;M2=ON;A2=AMB` | `97` |
| `707` | `4` | `400` | `4214` | `M1<>CEN;M2=ON;A2=GEN` | `95` |
| `707` | `4` | `400` | `4215` | `M1<>CEN;M2=ON;A2=GR` | `96` |
| `707` | `4` | `400` | `4216` | `M1<>CEN;M2=PUL;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `707` | `4` | `400` | `4217` | `M1<>CEN;M2=PUL;A2=AMB` | `97` |
| `707` | `4` | `400` | `4219` | `M1<>CEN;M2=PUL;A2=GEN` | `95` |
| `707` | `4` | `400` | `4220` | `M1<>CEN;M2=PUL;A2=GR` | `96` |
| `707` | `4` | `400` | `4255` | `M1=CEN;M2=0` | `4` |
| `707` | `4` | `400` | `4257` | `M1=CEN;M2=1` | `4` |
| `707` | `4` | `400` | `4259` | `M1=CEN;M2=2` | `4` |
| `707` | `4` | `400` | `4261` | `M1=CEN;M2=3` | `4` |
| `707` | `4` | `400` | `4263` | `M1=CEN;M2=4` | `4` |
| `707` | `4` | `400` | `4265` | `M1=CEN;M2=O/I` | `4` |
| `707` | `4` | `400` | `4267` | `M1=CEN;M2=PUL` | `4` |
| `707` | `4` | `400` | `4908` | `M1<>CEN;M2<>CEN;A2<>AUX;A2<>GR;A2<>AMB;A2<>GE` | `4` |
| `707` | `4` | `401` | `4222` | `M1<>CEN;M2=SU_GIU;A2=AMB` | `97` |
| `707` | `4` | `401` | `4224` | `M1<>CEN;M2=SU_GIU;A2=GEN` | `95` |
| `707` | `4` | `401` | `4225` | `M1<>CEN;M2=SU_GIU;A2=GR` | `96` |
| `707` | `4` | `401` | `4227` | `M1<>CEN;M2=SU_GIU_M;A2=AMB` | `97` |
| `707` | `4` | `401` | `4229` | `M1<>CEN;M2=SU_GIU_M;A2=GEN` | `95` |
| `707` | `4` | `401` | `4230` | `M1<>CEN;M2=SU_GIU_M;A2=GR` | `96` |
| `707` | `4` | `401` | `4909` | `M1<>CEN;M2=SU_GIU_M;A2<>AUX;A2<>GR;A2<>AMB;A2` | `4` |
| `707` | `4` | `401` | `4910` | `M1<>CEN;M2=SU_GIU;A2<>AUX;A2<>GR;A2<>AMB;A2<>` | `4` |
| `707` | `4` | `404` | `4199` | `M1<>CEN;M2=CEN` | `4` |
| `707` | `4` | `406` | `4200` | `M1<>CEN;M2=FAKE` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `707` | `6` | `2428` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `707` | `6` | `2429` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `707` | `6` | `2430` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `707` | `6` | `2994` | `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `707` | `7` | `2419` | `SUBTYPE` | `15` = Differential restart | `11` | subtype(ASTCBR); reusable default `11` is outside this subset; filter supplies no replacement default |
| `707` | `7` | `2993` | `LOCAL_BUTTON` | `12` = Bistable control; `13` = Monostable control; `14` = Bistable and blades control (entire reusable range retained) | `12` | Local button modality |
| `707` | `400` | `2407` | `M` | `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `4` = Toggle `ON`/`OFF`; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `5` = `ON`/`OFF`; `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `130` = Customized `ON`/`OFF` and point to point dimmer; `131` = Customized toggle dimmer; `132` = Customized `ON`/`OFF` and dimmer; `133` = Customized toggle dimmer without regulation; `134` = Customized `ON`/`OFF` and dimmer without regulation; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90% | `0` | Mode; reusable default `0` is outside this subset; filter supplies no replacement default |
| `707` | `400` | `2408` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `707` | `400` | `2409` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `707` | `400` | `2410` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `707` | `400` | `2411` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `707` | `400` | `2412` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `707` | `400` | `2413` | `LEVEL` | `0..100` (entire reusable range retained) | `100` | Level |
| `707` | `400` | `2414` | `START_S` | `0..255` (entire reusable range retained) | `255` | Soft start speed |
| `707` | `400` | `2415` | `STOP_S` | `0..255` (entire reusable range retained) | `255` | Soft stop speed |
| `707` | `400` | `2416` | `DIMMING_S` | `0..255` (entire reusable range retained) | `255` | Dimming speed |
| `707` | `400` | `2417` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `707` | `401` | `2420` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `707` | `401` | `2421` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `707` | `401` | `2422` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `707` | `404` | `2423` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `707` | `404` | `2424` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `707` | `404` | `2425` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `707` | `404` | `2426` | `START_DELAY` | `0..255` (entire reusable range retained) | `10` | Start delay |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `4` | `M1=0` | `M` = `0` | `4` |
| `4` | `M1=1` | `M` = `1`; `T_TIME ` = `1` | `4` |
| `4` | `M1=2` | `M` = `1`; `T_TIME ` = `2` | `4` |
| `4` | `M1=3` | `M` = `1`; `T_TIME ` = `3` | `4` |
| `4` | `M1=4` | `M` = `1`; `T_TIME ` = `4` | `4` |
| `4` | `M1=5` | `M` = `1`; `T_TIME ` = `5` | `4` |
| `4` | `M1=6` | `M` = `1`; `T_TIME ` = `6` | `4` |
| `4` | `M1=7` | `M` = `1`; `T_TIME ` = `7` | `4` |
| `4` | `M1=8` | `M` = `1`; `T_TIME ` = `8` | `4` |
| `4` | `M1=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `2` | `4` |
| `4` | `M1=O/I` | `M` = `9` | `4` |
| `4` | `M1=OFF` | `M` = `10` | `4` |
| `4` | `M1=ON` | `M` = `11` | `4` |
| `4` | `M1=PUL` | `M` = `15` | `4` |
| `4` | `M1=SU_GIU` | `M` = `12` | `4` |
| `4` | `M1=SU_GIU_M` | `M` = `13` | `4` |
| `4` | `M2=0` | `M` = `0` | `4` |
| `4` | `M2=1` | `M` = `1`; `T_TIME ` = `1` | `4` |
| `4` | `M2=2` | `M` = `1`; `T_TIME ` = `2` | `4` |
| `4` | `M2=3` | `M` = `1`; `T_TIME ` = `3` | `4` |
| `4` | `M2=4` | `M` = `1`; `T_TIME ` = `4` | `4` |
| `4` | `M2=5` | `M` = `1`; `T_TIME ` = `5` | `4` |
| `4` | `M2=6` | `M` = `1`; `T_TIME ` = `6` | `4` |
| `4` | `M2=7` | `M` = `1`; `T_TIME ` = `7` | `4` |
| `4` | `M2=8` | `M` = `1`; `T_TIME ` = `8` | `4` |
| `4` | `M2=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `2` | `4` |
| `4` | `M2=O/I` | `M` = `9` | `4` |
| `4` | `M2=OFF` | `M` = `10` | `4` |
| `4` | `M2=ON` | `M` = `11` | `4` |
| `4` | `M2=PUL` | `M` = `15` | `4` |
| `4` | `M2=SU_GIU` | `M` = `12` | `4` |
| `4` | `M2=SU_GIU_M` | `M` = `13` | `4` |
| `20` | `M1=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `20` |
| `20` | `M1=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `20` |
| `20` | `M1=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `20` |
| `20` | `M1=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `20` |
| `20` | `M1=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `20` |
| `20` | `M1=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `20` |
| `20` | `M1=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `20` |
| `20` | `M1=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `20` |
| `25` | `M2=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `25` |
| `25` | `M2=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `25` |
| `25` | `M2=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `25` |
| `25` | `M2=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `25` |
| `25` | `M2=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `25` |
| `25` | `M2=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `25` |
| `25` | `M2=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `25` |
| `25` | `M2=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `25` |
| `26` | `M2=0` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `60` | `26` |
| `26` | `M2=1` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `62` | `26` |
| `26` | `M2=2` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `65` | `26` |
| `26` | `M2=3` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `70` | `26` |
| `26` | `M2=4` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `0` | `26` |
| `26` | `M2=5` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `20` | `26` |
| `26` | `M2=6` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `10` | `26` |
| `26` | `M2=7` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `5` | `26` |
| `26` | `M2=8` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `15` | `26` |
| `26` | `M2=9` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `30` | `26` |
| `26` | `M2=I/O` | `LOCAL_BUTTON` = `13`; `M` = `0`; `STOP_TIME` = `60` | `26` |
| `26` | `M2=PUL` | `LOCAL_BUTTON` = `12`; `M` = `15`; `STOP_TIME` = `60` | `26` |
| `26` | `M2=SLA` | `LOCAL_BUTTON` = `12`; `M` = `11` | `26` |
| `95` | `M1=0` | `M` = `0`; `ADDR_TYPE` = `3` | `95` |
| `95` | `M1=1` | `M` = `1`; `T_TIME ` = `1`; `ADDR_TYPE` = `3` | `95` |
| `95` | `M1=2` | `M` = `1`; `T_TIME ` = `2`; `ADDR_TYPE` = `3` | `95` |
| `95` | `M1=3` | `M` = `1`; `T_TIME ` = `3`; `ADDR_TYPE` = `3` | `95` |
| `95` | `M1=4` | `T_TIME ` = `4`; `M` = `1`; `ADDR_TYPE` = `3` | `95` |
| `95` | `M1=5` | `T_TIME ` = `5`; `M` = `1`; `ADDR_TYPE` = `3` | `95` |
| `95` | `M1=6` | `M` = `1`; `T_TIME ` = `6`; `ADDR_TYPE` = `3` | `95` |
| `95` | `M1=7` | `M` = `1`; `T_TIME ` = `7`; `ADDR_TYPE` = `3` | `95` |
| `95` | `M1=8` | `T_TIME ` = `8`; `M` = `1`; `ADDR_TYPE` = `3` | `95` |
| `95` | `M1=O/I` | `M` = `9`; `ADDR_TYPE` = `3` | `95` |
| `95` | `M1=OFF` | `M` = `10`; `ADDR_TYPE` = `3` | `95` |
| `95` | `M1=ON` | `M` = `11`; `ADDR_TYPE` = `3` | `95` |
| `95` | `M1=PUL` | `M` = `15`; `ADDR_TYPE` = `3` | `95` |
| `95` | `M1=SU_GIU` | `M` = `12`; `ADDR_TYPE` = `3` | `95` |
| `95` | `M1=SU_GIU_M` | `M` = `13`; `ADDR_TYPE` = `3` | `95` |
| `96` | `M2=0` | `M` = `0`; `ADDR_TYPE` = `2` | `96` |
| `96` | `M2=1` | `M` = `1`; `T_TIME ` = `1`; `ADDR_TYPE` = `2` | `96` |
| `96` | `M2=2` | `M` = `1`; `T_TIME ` = `2`; `ADDR_TYPE` = `2` | `96` |
| `96` | `M2=3` | `M` = `1`; `T_TIME ` = `3`; `ADDR_TYPE` = `2` | `96` |
| `96` | `M2=4` | `T_TIME ` = `4`; `M` = `1`; `ADDR_TYPE` = `2` | `96` |
| `96` | `M2=5` | `T_TIME ` = `5`; `M` = `1`; `ADDR_TYPE` = `2` | `96` |
| `96` | `M2=6` | `M` = `1`; `T_TIME ` = `6`; `ADDR_TYPE` = `2` | `96` |
| `96` | `M2=7` | `M` = `1`; `T_TIME ` = `7`; `ADDR_TYPE` = `2` | `96` |
| `96` | `M2=8` | `T_TIME ` = `8`; `M` = `1`; `ADDR_TYPE` = `2` | `96` |
| `96` | `M2=O/I` | `M` = `9`; `ADDR_TYPE` = `2` | `96` |
| `96` | `M2=OFF` | `M` = `10`; `ADDR_TYPE` = `2` | `96` |
| `96` | `M2=ON` | `M` = `11`; `ADDR_TYPE` = `2` | `96` |
| `96` | `M2=PUL` | `M` = `15`; `ADDR_TYPE` = `2` | `96` |
| `96` | `M2=SU_GIU` | `M` = `12`; `ADDR_TYPE` = `2` | `96` |
| `96` | `M2=SU_GIU_M` | `M` = `13`; `ADDR_TYPE` = `2` | `96` |
| `96` | `M2=0; PL2=1` | `G1` = `1` | `96` → `202` |
| `96` | `M2=0; PL2=2` | `G1` = `2` | `96` → `202` |
| `96` | `M2=0; PL2=3` | `G1` = `3` | `96` → `202` |
| `96` | `M2=0; PL2=4` | `G1` = `4` | `96` → `202` |
| `96` | `M2=0; PL2=5` | `G1` = `5` | `96` → `202` |
| `96` | `M2=0; PL2=6` | `G1` = `6` | `96` → `202` |
| `96` | `M2=0; PL2=7` | `G1` = `7` | `96` → `202` |
| `96` | `M2=0; PL2=8` | `G1` = `8` | `96` → `202` |
| `96` | `M2=0; PL2=9` | `G1` = `9` | `96` → `202` |
| `96` | `M2=1; PL2=1` | `G1` = `1` | `96` → `202` |
| `96` | `M2=1; PL2=2` | `G1` = `2` | `96` → `202` |
| `96` | `M2=1; PL2=3` | `G1` = `3` | `96` → `202` |
| `96` | `M2=1; PL2=4` | `G1` = `4` | `96` → `202` |
| `96` | `M2=1; PL2=5` | `G1` = `5` | `96` → `202` |
| `96` | `M2=1; PL2=6` | `G1` = `6` | `96` → `202` |
| `96` | `M2=1; PL2=7` | `G1` = `7` | `96` → `202` |
| `96` | `M2=1; PL2=8` | `G1` = `8` | `96` → `202` |
| `96` | `M2=1; PL2=9` | `G1` = `9` | `96` → `202` |
| `96` | `M2=2; PL2=1` | `G1` = `1` | `96` → `202` |
| `96` | `M2=2; PL2=2` | `G1` = `2` | `96` → `202` |
| `96` | `M2=2; PL2=3` | `G1` = `3` | `96` → `202` |
| `96` | `M2=2; PL2=4` | `G1` = `4` | `96` → `202` |
| `96` | `M2=2; PL2=5` | `G1` = `5` | `96` → `202` |
| `96` | `M2=2; PL2=6` | `G1` = `6` | `96` → `202` |
| `96` | `M2=2; PL2=7` | `G1` = `7` | `96` → `202` |
| `96` | `M2=2; PL2=8` | `G1` = `8` | `96` → `202` |
| `96` | `M2=2; PL2=9` | `G1` = `9` | `96` → `202` |
| `96` | `M2=3; PL2=1` | `G1` = `1` | `96` → `202` |
| `96` | `M2=3; PL2=2` | `G1` = `2` | `96` → `202` |
| `96` | `M2=3; PL2=3` | `G1` = `3` | `96` → `202` |
| `96` | `M2=3; PL2=4` | `G1` = `4` | `96` → `202` |
| `96` | `M2=3; PL2=5` | `G1` = `5` | `96` → `202` |
| `96` | `M2=3; PL2=6` | `G1` = `6` | `96` → `202` |
| `96` | `M2=3; PL2=7` | `G1` = `7` | `96` → `202` |
| `96` | `M2=3; PL2=8` | `G1` = `8` | `96` → `202` |
| `96` | `M2=3; PL2=9` | `G1` = `9` | `96` → `202` |
| `96` | `M2=4; PL2=1` | `G1` = `1` | `96` → `202` |
| `96` | `M2=4; PL2=2` | `G1` = `2` | `96` → `202` |
| `96` | `M2=4; PL2=3` | `G1` = `3` | `96` → `202` |
| `96` | `M2=4; PL2=4` | `G1` = `4` | `96` → `202` |
| `96` | `M2=4; PL2=5` | `G1` = `5` | `96` → `202` |
| `96` | `M2=4; PL2=6` | `G1` = `6` | `96` → `202` |
| `96` | `M2=4; PL2=7` | `G1` = `7` | `96` → `202` |
| `96` | `M2=4; PL2=8` | `G1` = `8` | `96` → `202` |
| `96` | `M2=4; PL2=9` | `G1` = `9` | `96` → `202` |
| `96` | `M2=5; PL2=1` | `G1` = `1` | `96` → `202` |
| `96` | `M2=5; PL2=2` | `G1` = `2` | `96` → `202` |
| `96` | `M2=5; PL2=3` | `G1` = `3` | `96` → `202` |
| `96` | `M2=5; PL2=4` | `G1` = `4` | `96` → `202` |
| `96` | `M2=5; PL2=5` | `G1` = `5` | `96` → `202` |
| `96` | `M2=5; PL2=6` | `G1` = `6` | `96` → `202` |
| `96` | `M2=5; PL2=7` | `G1` = `7` | `96` → `202` |
| `96` | `M2=5; PL2=8` | `G1` = `8` | `96` → `202` |
| `96` | `M2=5; PL2=9` | `G1` = `9` | `96` → `202` |
| `96` | `M2=6; PL2=1` | `G1` = `1` | `96` → `202` |
| `96` | `M2=6; PL2=2` | `G1` = `2` | `96` → `202` |
| `96` | `M2=6; PL2=3` | `G1` = `3` | `96` → `202` |
| `96` | `M2=6; PL2=4` | `G1` = `4` | `96` → `202` |
| `96` | `M2=6; PL2=5` | `G1` = `5` | `96` → `202` |
| `96` | `M2=6; PL2=6` | `G1` = `6` | `96` → `202` |
| `96` | `M2=6; PL2=7` | `G1` = `7` | `96` → `202` |
| `96` | `M2=6; PL2=8` | `G1` = `8` | `96` → `202` |
| `96` | `M2=6; PL2=9` | `G1` = `9` | `96` → `202` |
| `96` | `M2=7; PL2=1` | `G1` = `1` | `96` → `202` |
| `96` | `M2=7; PL2=2` | `G1` = `2` | `96` → `202` |
| `96` | `M2=7; PL2=3` | `G1` = `3` | `96` → `202` |
| `96` | `M2=7; PL2=4` | `G1` = `4` | `96` → `202` |
| `96` | `M2=7; PL2=5` | `G1` = `5` | `96` → `202` |
| `96` | `M2=7; PL2=6` | `G1` = `6` | `96` → `202` |
| `96` | `M2=7; PL2=7` | `G1` = `7` | `96` → `202` |
| `96` | `M2=7; PL2=8` | `G1` = `8` | `96` → `202` |
| `96` | `M2=7; PL2=9` | `G1` = `9` | `96` → `202` |
| `96` | `M2=8; PL2=1` | `G1` = `1` | `96` → `202` |
| `96` | `M2=8; PL2=2` | `G1` = `2` | `96` → `202` |
| `96` | `M2=8; PL2=3` | `G1` = `3` | `96` → `202` |
| `96` | `M2=8; PL2=4` | `G1` = `4` | `96` → `202` |
| `96` | `M2=8; PL2=5` | `G1` = `5` | `96` → `202` |
| `96` | `M2=8; PL2=6` | `G1` = `6` | `96` → `202` |
| `96` | `M2=8; PL2=7` | `G1` = `7` | `96` → `202` |
| `96` | `M2=8; PL2=8` | `G1` = `8` | `96` → `202` |
| `96` | `M2=8; PL2=9` | `G1` = `9` | `96` → `202` |
| `96` | `M2=O/I; PL2=1` | `G1` = `1` | `96` → `202` |
| `96` | `M2=O/I; PL2=2` | `G1` = `2` | `96` → `202` |
| `96` | `M2=O/I; PL2=3` | `G1` = `3` | `96` → `202` |
| `96` | `M2=O/I; PL2=4` | `G1` = `4` | `96` → `202` |
| `96` | `M2=O/I; PL2=5` | `G1` = `5` | `96` → `202` |
| `96` | `M2=O/I; PL2=6` | `G1` = `6` | `96` → `202` |
| `96` | `M2=O/I; PL2=7` | `G1` = `7` | `96` → `202` |
| `96` | `M2=O/I; PL2=8` | `G1` = `8` | `96` → `202` |
| `96` | `M2=O/I; PL2=9` | `G1` = `9` | `96` → `202` |
| `96` | `M2=OFF; PL2=1` | `G1` = `1` | `96` → `202` |
| `96` | `M2=OFF; PL2=2` | `G1` = `2` | `96` → `202` |
| `96` | `M2=OFF; PL2=3` | `G1` = `3` | `96` → `202` |
| `96` | `M2=OFF; PL2=4` | `G1` = `4` | `96` → `202` |
| `96` | `M2=OFF; PL2=5` | `G1` = `5` | `96` → `202` |
| `96` | `M2=OFF; PL2=6` | `G1` = `6` | `96` → `202` |
| `96` | `M2=OFF; PL2=7` | `G1` = `7` | `96` → `202` |
| `96` | `M2=OFF; PL2=8` | `G1` = `8` | `96` → `202` |
| `96` | `M2=OFF; PL2=9` | `G1` = `9` | `96` → `202` |
| `96` | `M2=ON; PL2=1` | `G1` = `1` | `96` → `202` |
| `96` | `M2=ON; PL2=2` | `G1` = `2` | `96` → `202` |
| `96` | `M2=ON; PL2=3` | `G1` = `3` | `96` → `202` |
| `96` | `M2=ON; PL2=4` | `G1` = `4` | `96` → `202` |
| `96` | `M2=ON; PL2=5` | `G1` = `5` | `96` → `202` |
| `96` | `M2=ON; PL2=6` | `G1` = `6` | `96` → `202` |
| `96` | `M2=ON; PL2=7` | `G1` = `7` | `96` → `202` |
| `96` | `M2=ON; PL2=8` | `G1` = `8` | `96` → `202` |
| `96` | `M2=ON; PL2=9` | `G1` = `9` | `96` → `202` |
| `96` | `M2=PUL; PL2=1` | `G1` = `1` | `96` → `202` |
| `96` | `M2=PUL; PL2=2` | `G1` = `2` | `96` → `202` |
| `96` | `M2=PUL; PL2=3` | `G1` = `3` | `96` → `202` |
| `96` | `M2=PUL; PL2=4` | `G1` = `4` | `96` → `202` |
| `96` | `M2=PUL; PL2=5` | `G1` = `5` | `96` → `202` |
| `96` | `M2=PUL; PL2=6` | `G1` = `6` | `96` → `202` |
| `96` | `M2=PUL; PL2=7` | `G1` = `7` | `96` → `202` |
| `96` | `M2=PUL; PL2=8` | `G1` = `8` | `96` → `202` |
| `96` | `M2=PUL; PL2=9` | `G1` = `9` | `96` → `202` |
| `96` | `M2=SU_GIU; PL2=1` | `G1` = `1` | `96` → `202` |
| `96` | `M2=SU_GIU; PL2=2` | `G1` = `2` | `96` → `202` |
| `96` | `M2=SU_GIU; PL2=3` | `G1` = `3` | `96` → `202` |
| `96` | `M2=SU_GIU; PL2=4` | `G1` = `4` | `96` → `202` |
| `96` | `M2=SU_GIU; PL2=5` | `G1` = `5` | `96` → `202` |
| `96` | `M2=SU_GIU; PL2=6` | `G1` = `6` | `96` → `202` |
| `96` | `M2=SU_GIU; PL2=7` | `G1` = `7` | `96` → `202` |
| `96` | `M2=SU_GIU; PL2=8` | `G1` = `8` | `96` → `202` |
| `96` | `M2=SU_GIU; PL2=9` | `G1` = `9` | `96` → `202` |
| `96` | `M2=SU_GIU_M; PL2=1` | `G1` = `1` | `96` → `202` |
| `96` | `M2=SU_GIU_M; PL2=2` | `G1` = `2` | `96` → `202` |
| `96` | `M2=SU_GIU_M; PL2=3` | `G1` = `3` | `96` → `202` |
| `96` | `M2=SU_GIU_M; PL2=4` | `G1` = `4` | `96` → `202` |
| `96` | `M2=SU_GIU_M; PL2=5` | `G1` = `5` | `96` → `202` |
| `96` | `M2=SU_GIU_M; PL2=6` | `G1` = `6` | `96` → `202` |
| `96` | `M2=SU_GIU_M; PL2=7` | `G1` = `7` | `96` → `202` |
| `96` | `M2=SU_GIU_M; PL2=8` | `G1` = `8` | `96` → `202` |
| `96` | `M2=SU_GIU_M; PL2=9` | `G1` = `9` | `96` → `202` |
| `97` | `M2=0` | `M` = `0`; `ADDR_TYPE` = `1` | `97` |
| `97` | `M2=1` | `M` = `1`; `T_TIME ` = `1`; `ADDR_TYPE` = `1` | `97` |
| `97` | `M2=2` | `M` = `1`; `T_TIME ` = `2`; `ADDR_TYPE` = `1` | `97` |
| `97` | `M2=3` | `M` = `1`; `T_TIME ` = `3`; `ADDR_TYPE` = `1` | `97` |
| `97` | `M2=4` | `T_TIME ` = `4`; `M` = `1`; `ADDR_TYPE` = `1` | `97` |
| `97` | `M2=5` | `T_TIME ` = `5`; `M` = `1`; `ADDR_TYPE` = `1` | `97` |
| `97` | `M2=6` | `M` = `1`; `T_TIME ` = `6`; `ADDR_TYPE` = `1` | `97` |
| `97` | `M2=7` | `M` = `1`; `T_TIME ` = `7`; `ADDR_TYPE` = `1` | `97` |
| `97` | `M2=8` | `T_TIME ` = `8`; `M` = `1`; `ADDR_TYPE` = `1` | `97` |
| `97` | `M2=O/I` | `M` = `9`; `ADDR_TYPE` = `1` | `97` |
| `97` | `M2=OFF` | `M` = `10`; `ADDR_TYPE` = `1` | `97` |
| `97` | `M2=ON` | `M` = `11`; `ADDR_TYPE` = `1` | `97` |
| `97` | `M2=PUL` | `M` = `15`; `ADDR_TYPE` = `1` | `97` |
| `97` | `M2=SU_GIU` | `M` = `12`; `ADDR_TYPE` = `1` | `97` |
| `97` | `M2=SU_GIU_M` | `M` = `13`; `ADDR_TYPE` = `1` | `97` |
| `97` | `M2=0; PL2=1` | `A` = `1` | `97` → `203` |
| `97` | `M2=0; PL2=2` | `A` = `2` | `97` → `203` |
| `97` | `M2=0; PL2=3` | `A` = `3` | `97` → `203` |
| `97` | `M2=0; PL2=4` | `A` = `4` | `97` → `203` |
| `97` | `M2=0; PL2=5` | `A` = `5` | `97` → `203` |
| `97` | `M2=0; PL2=6` | `A` = `6` | `97` → `203` |
| `97` | `M2=0; PL2=7` | `A` = `7` | `97` → `203` |
| `97` | `M2=0; PL2=8` | `A` = `8` | `97` → `203` |
| `97` | `M2=0; PL2=9` | `A` = `9` | `97` → `203` |
| `97` | `M2=1; PL2=1` | `A` = `1` | `97` → `203` |
| `97` | `M2=1; PL2=2` | `A` = `2` | `97` → `203` |
| `97` | `M2=1; PL2=3` | `A` = `3` | `97` → `203` |
| `97` | `M2=1; PL2=4` | `A` = `4` | `97` → `203` |
| `97` | `M2=1; PL2=5` | `A` = `5` | `97` → `203` |
| `97` | `M2=1; PL2=6` | `A` = `6` | `97` → `203` |
| `97` | `M2=1; PL2=7` | `A` = `7` | `97` → `203` |
| `97` | `M2=1; PL2=8` | `A` = `8` | `97` → `203` |
| `97` | `M2=1; PL2=9` | `A` = `9` | `97` → `203` |
| `97` | `M2=2; PL2=1` | `A` = `1` | `97` → `203` |
| `97` | `M2=2; PL2=2` | `A` = `2` | `97` → `203` |
| `97` | `M2=2; PL2=3` | `A` = `3` | `97` → `203` |
| `97` | `M2=2; PL2=4` | `A` = `4` | `97` → `203` |
| `97` | `M2=2; PL2=5` | `A` = `5` | `97` → `203` |
| `97` | `M2=2; PL2=6` | `A` = `6` | `97` → `203` |
| `97` | `M2=2; PL2=7` | `A` = `7` | `97` → `203` |
| `97` | `M2=2; PL2=8` | `A` = `8` | `97` → `203` |
| `97` | `M2=2; PL2=9` | `A` = `9` | `97` → `203` |
| `97` | `M2=3; PL2=1` | `A` = `1` | `97` → `203` |
| `97` | `M2=3; PL2=2` | `A` = `2` | `97` → `203` |
| `97` | `M2=3; PL2=3` | `A` = `3` | `97` → `203` |
| `97` | `M2=3; PL2=4` | `A` = `4` | `97` → `203` |
| `97` | `M2=3; PL2=5` | `A` = `5` | `97` → `203` |
| `97` | `M2=3; PL2=6` | `A` = `6` | `97` → `203` |
| `97` | `M2=3; PL2=7` | `A` = `7` | `97` → `203` |
| `97` | `M2=3; PL2=8` | `A` = `8` | `97` → `203` |
| `97` | `M2=3; PL2=9` | `A` = `9` | `97` → `203` |
| `97` | `M2=4; PL2=1` | `A` = `1` | `97` → `203` |
| `97` | `M2=4; PL2=2` | `A` = `2` | `97` → `203` |
| `97` | `M2=4; PL2=3` | `A` = `3` | `97` → `203` |
| `97` | `M2=4; PL2=4` | `A` = `4` | `97` → `203` |
| `97` | `M2=4; PL2=5` | `A` = `5` | `97` → `203` |
| `97` | `M2=4; PL2=6` | `A` = `6` | `97` → `203` |
| `97` | `M2=4; PL2=7` | `A` = `7` | `97` → `203` |
| `97` | `M2=4; PL2=8` | `A` = `8` | `97` → `203` |
| `97` | `M2=4; PL2=9` | `A` = `9` | `97` → `203` |
| `97` | `M2=5; PL2=1` | `A` = `1` | `97` → `203` |
| `97` | `M2=5; PL2=2` | `A` = `2` | `97` → `203` |
| `97` | `M2=5; PL2=3` | `A` = `3` | `97` → `203` |
| `97` | `M2=5; PL2=4` | `A` = `4` | `97` → `203` |
| `97` | `M2=5; PL2=5` | `A` = `5` | `97` → `203` |
| `97` | `M2=5; PL2=6` | `A` = `6` | `97` → `203` |
| `97` | `M2=5; PL2=7` | `A` = `7` | `97` → `203` |
| `97` | `M2=5; PL2=8` | `A` = `8` | `97` → `203` |
| `97` | `M2=5; PL2=9` | `A` = `9` | `97` → `203` |
| `97` | `M2=6; PL2=1` | `A` = `1` | `97` → `203` |
| `97` | `M2=6; PL2=2` | `A` = `2` | `97` → `203` |
| `97` | `M2=6; PL2=3` | `A` = `3` | `97` → `203` |
| `97` | `M2=6; PL2=4` | `A` = `4` | `97` → `203` |
| `97` | `M2=6; PL2=5` | `A` = `5` | `97` → `203` |
| `97` | `M2=6; PL2=6` | `A` = `6` | `97` → `203` |
| `97` | `M2=6; PL2=7` | `A` = `7` | `97` → `203` |
| `97` | `M2=6; PL2=8` | `A` = `8` | `97` → `203` |
| `97` | `M2=6; PL2=9` | `A` = `9` | `97` → `203` |
| `97` | `M2=7; PL2=1` | `A` = `1` | `97` → `203` |
| `97` | `M2=7; PL2=2` | `A` = `2` | `97` → `203` |
| `97` | `M2=7; PL2=3` | `A` = `3` | `97` → `203` |
| `97` | `M2=7; PL2=4` | `A` = `4` | `97` → `203` |
| `97` | `M2=7; PL2=5` | `A` = `5` | `97` → `203` |
| `97` | `M2=7; PL2=6` | `A` = `6` | `97` → `203` |
| `97` | `M2=7; PL2=7` | `A` = `7` | `97` → `203` |
| `97` | `M2=7; PL2=8` | `A` = `8` | `97` → `203` |
| `97` | `M2=7; PL2=9` | `A` = `9` | `97` → `203` |
| `97` | `M2=8; PL2=1` | `A` = `1` | `97` → `203` |
| `97` | `M2=8; PL2=2` | `A` = `2` | `97` → `203` |
| `97` | `M2=8; PL2=3` | `A` = `3` | `97` → `203` |
| `97` | `M2=8; PL2=4` | `A` = `4` | `97` → `203` |
| `97` | `M2=8; PL2=5` | `A` = `5` | `97` → `203` |
| `97` | `M2=8; PL2=6` | `A` = `6` | `97` → `203` |
| `97` | `M2=8; PL2=7` | `A` = `7` | `97` → `203` |
| `97` | `M2=8; PL2=8` | `A` = `8` | `97` → `203` |
| `97` | `M2=8; PL2=9` | `A` = `9` | `97` → `203` |
| `97` | `M2=O/I; PL2=1` | `A` = `1` | `97` → `203` |
| `97` | `M2=O/I; PL2=2` | `A` = `2` | `97` → `203` |
| `97` | `M2=O/I; PL2=3` | `A` = `3` | `97` → `203` |
| `97` | `M2=O/I; PL2=4` | `A` = `4` | `97` → `203` |
| `97` | `M2=O/I; PL2=5` | `A` = `5` | `97` → `203` |
| `97` | `M2=O/I; PL2=6` | `A` = `6` | `97` → `203` |
| `97` | `M2=O/I; PL2=7` | `A` = `7` | `97` → `203` |
| `97` | `M2=O/I; PL2=8` | `A` = `8` | `97` → `203` |
| `97` | `M2=O/I; PL2=9` | `A` = `9` | `97` → `203` |
| `97` | `M2=OFF; PL2=1` | `A` = `1` | `97` → `203` |
| `97` | `M2=OFF; PL2=2` | `A` = `2` | `97` → `203` |
| `97` | `M2=OFF; PL2=3` | `A` = `3` | `97` → `203` |
| `97` | `M2=OFF; PL2=4` | `A` = `4` | `97` → `203` |
| `97` | `M2=OFF; PL2=5` | `A` = `5` | `97` → `203` |
| `97` | `M2=OFF; PL2=6` | `A` = `6` | `97` → `203` |
| `97` | `M2=OFF; PL2=7` | `A` = `7` | `97` → `203` |
| `97` | `M2=OFF; PL2=8` | `A` = `8` | `97` → `203` |
| `97` | `M2=OFF; PL2=9` | `A` = `9` | `97` → `203` |
| `97` | `M2=ON; PL2=1` | `A` = `1` | `97` → `203` |
| `97` | `M2=ON; PL2=2` | `A` = `2` | `97` → `203` |
| `97` | `M2=ON; PL2=3` | `A` = `3` | `97` → `203` |
| `97` | `M2=ON; PL2=4` | `A` = `4` | `97` → `203` |
| `97` | `M2=ON; PL2=5` | `A` = `5` | `97` → `203` |
| `97` | `M2=ON; PL2=6` | `A` = `6` | `97` → `203` |
| `97` | `M2=ON; PL2=7` | `A` = `7` | `97` → `203` |
| `97` | `M2=ON; PL2=8` | `A` = `8` | `97` → `203` |
| `97` | `M2=ON; PL2=9` | `A` = `9` | `97` → `203` |
| `97` | `M2=PUL; PL2=1` | `A` = `1` | `97` → `203` |
| `97` | `M2=PUL; PL2=2` | `A` = `2` | `97` → `203` |
| `97` | `M2=PUL; PL2=3` | `A` = `3` | `97` → `203` |
| `97` | `M2=PUL; PL2=4` | `A` = `4` | `97` → `203` |
| `97` | `M2=PUL; PL2=5` | `A` = `5` | `97` → `203` |
| `97` | `M2=PUL; PL2=6` | `A` = `6` | `97` → `203` |
| `97` | `M2=PUL; PL2=7` | `A` = `7` | `97` → `203` |
| `97` | `M2=PUL; PL2=8` | `A` = `8` | `97` → `203` |
| `97` | `M2=PUL; PL2=9` | `A` = `9` | `97` → `203` |
| `97` | `M2=SU_GIU; PL2=1` | `A` = `1` | `97` → `203` |
| `97` | `M2=SU_GIU; PL2=2` | `A` = `2` | `97` → `203` |
| `97` | `M2=SU_GIU; PL2=3` | `A` = `3` | `97` → `203` |
| `97` | `M2=SU_GIU; PL2=4` | `A` = `4` | `97` → `203` |
| `97` | `M2=SU_GIU; PL2=5` | `A` = `5` | `97` → `203` |
| `97` | `M2=SU_GIU; PL2=6` | `A` = `6` | `97` → `203` |
| `97` | `M2=SU_GIU; PL2=7` | `A` = `7` | `97` → `203` |
| `97` | `M2=SU_GIU; PL2=8` | `A` = `8` | `97` → `203` |
| `97` | `M2=SU_GIU; PL2=9` | `A` = `9` | `97` → `203` |
| `97` | `M2=SU_GIU_M; PL2=1` | `A` = `1` | `97` → `203` |
| `97` | `M2=SU_GIU_M; PL2=2` | `A` = `2` | `97` → `203` |
| `97` | `M2=SU_GIU_M; PL2=3` | `A` = `3` | `97` → `203` |
| `97` | `M2=SU_GIU_M; PL2=4` | `A` = `4` | `97` → `203` |
| `97` | `M2=SU_GIU_M; PL2=5` | `A` = `5` | `97` → `203` |
| `97` | `M2=SU_GIU_M; PL2=6` | `A` = `6` | `97` → `203` |
| `97` | `M2=SU_GIU_M; PL2=7` | `A` = `7` | `97` → `203` |
| `97` | `M2=SU_GIU_M; PL2=8` | `A` = `8` | `97` → `203` |
| `97` | `M2=SU_GIU_M; PL2=9` | `A` = `9` | `97` → `203` |
| `550` | `M1=0` | `M` = `0` | `550` |
| `550` | `M1=1` | `M` = `1`; `T_TIME ` = `1` | `550` |
| `550` | `M1=2` | `M` = `1`; `T_TIME ` = `2` | `550` |
| `550` | `M1=3` | `M` = `1`; `T_TIME ` = `3` | `550` |
| `550` | `M1=4` | `M` = `1`; `T_TIME ` = `4` | `550` |
| `550` | `M1=5` | `M` = `1`; `T_TIME ` = `5` | `550` |
| `550` | `M1=6` | `M` = `1`; `T_TIME ` = `6` | `550` |
| `550` | `M1=7` | `M` = `1`; `T_TIME ` = `7` | `550` |
| `550` | `M1=8` | `M` = `1`; `T_TIME ` = `8` | `550` |
| `550` | `M1=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `2` | `550` |
| `550` | `M1=O/I` | `M` = `9` | `550` |
| `550` | `M1=OFF` | `M` = `10` | `550` |
| `550` | `M1=ON` | `M` = `11` | `550` |
| `550` | `M1=PUL` | `M` = `15` | `550` |
| `550` | `M1=SU_GIU` | `M` = `12` | `550` |
| `550` | `M1=SU_GIU_M` | `M` = `13` | `550` |
| `550` | `A1=1` | `A` = `1` | `550` |
| `550` | `A1=2` | `A` = `2` | `550` |
| `550` | `A1=3` | `A` = `3` | `550` |
| `550` | `A1=4` | `A` = `4` | `550` |
| `550` | `A1=5` | `A` = `5` | `550` |
| `550` | `A1=6` | `A` = `6` | `550` |
| `550` | `A1=7` | `A` = `7` | `550` |
| `550` | `A1=8` | `A` = `8` | `550` |
| `550` | `A1=9` | `A` = `9` | `550` |
| `550` | `PL1=1` | `PL` = `1` | `550` |
| `550` | `PL1=1; M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `550` → `1` |
| `550` | `PL1=1; M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `550` → `1` |
| `550` | `PL1=2` | `PL` = `2` | `550` |
| `550` | `PL1=2; M=0` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `60` | `550` → `2` |
| `550` | `PL1=2; M=1` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `62` | `550` → `2` |
| `550` | `PL1=2; M=2` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `65` | `550` → `2` |
| `550` | `PL1=2; M=3` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `70` | `550` → `2` |
| `550` | `PL1=2; M=4` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `0` | `550` → `2` |
| `550` | `PL1=2; M=5` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `20` | `550` → `2` |
| `550` | `PL1=2; M=6` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `10` | `550` → `2` |
| `550` | `PL1=2; M=7` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `5` | `550` → `2` |
| `550` | `PL1=2; M=8` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `15` | `550` → `2` |
| `550` | `PL1=2; M=9` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `30` | `550` → `2` |
| `550` | `PL1=2; M=I/O` | `LOCAL_BUTTON` = `13`; `M` = `0`; `STOP_TIME` = `60` | `550` → `2` |
| `550` | `PL1=2; M=PUL` | `LOCAL_BUTTON` = `12`; `M` = `15`; `STOP_TIME` = `60` | `550` → `2` |
| `550` | `PL1=2; M=SLA` | `LOCAL_BUTTON` = `12`; `M` = `11` | `550` → `2` |
| `550` | `PL1=3` | `PL` = `3` | `550` |
| `550` | `PL1=3; M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `550` → `3` |
| `550` | `PL1=3; M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `550` → `3` |
| `550` | `PL1=4` | `PL` = `4` | `550` |
| `550` | `PL1=4; M1=0` | `M` = `0` | `550` → `4` |
| `550` | `PL1=4; M1=1` | `M` = `1`; `T_TIME ` = `1` | `550` → `4` |
| `550` | `PL1=4; M1=2` | `M` = `1`; `T_TIME ` = `2` | `550` → `4` |
| `550` | `PL1=4; M1=3` | `M` = `1`; `T_TIME ` = `3` | `550` → `4` |
| `550` | `PL1=4; M1=4` | `M` = `1`; `T_TIME ` = `4` | `550` → `4` |
| `550` | `PL1=4; M1=5` | `M` = `1`; `T_TIME ` = `5` | `550` → `4` |
| `550` | `PL1=4; M1=6` | `M` = `1`; `T_TIME ` = `6` | `550` → `4` |
| `550` | `PL1=4; M1=7` | `M` = `1`; `T_TIME ` = `7` | `550` → `4` |
| `550` | `PL1=4; M1=8` | `M` = `1`; `T_TIME ` = `8` | `550` → `4` |
| `550` | `PL1=4; M1=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `2` | `550` → `4` |
| `550` | `PL1=4; M1=O/I` | `M` = `9` | `550` → `4` |
| `550` | `PL1=4; M1=OFF` | `M` = `10` | `550` → `4` |
| `550` | `PL1=4; M1=ON` | `M` = `11` | `550` → `4` |
| `550` | `PL1=4; M1=PUL` | `M` = `15` | `550` → `4` |
| `550` | `PL1=4; M1=SU_GIU` | `M` = `12` | `550` → `4` |
| `550` | `PL1=4; M1=SU_GIU_M` | `M` = `13` | `550` → `4` |
| `550` | `PL1=4; M2=0` | `M` = `0` | `550` → `4` |
| `550` | `PL1=4; M2=1` | `M` = `1`; `T_TIME ` = `1` | `550` → `4` |
| `550` | `PL1=4; M2=2` | `M` = `1`; `T_TIME ` = `2` | `550` → `4` |
| `550` | `PL1=4; M2=3` | `M` = `1`; `T_TIME ` = `3` | `550` → `4` |
| `550` | `PL1=4; M2=4` | `M` = `1`; `T_TIME ` = `4` | `550` → `4` |
| `550` | `PL1=4; M2=5` | `M` = `1`; `T_TIME ` = `5` | `550` → `4` |
| `550` | `PL1=4; M2=6` | `M` = `1`; `T_TIME ` = `6` | `550` → `4` |
| `550` | `PL1=4; M2=7` | `M` = `1`; `T_TIME ` = `7` | `550` → `4` |
| `550` | `PL1=4; M2=8` | `M` = `1`; `T_TIME ` = `8` | `550` → `4` |
| `550` | `PL1=4; M2=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `2` | `550` → `4` |
| `550` | `PL1=4; M2=O/I` | `M` = `9` | `550` → `4` |
| `550` | `PL1=4; M2=OFF` | `M` = `10` | `550` → `4` |
| `550` | `PL1=4; M2=ON` | `M` = `11` | `550` → `4` |
| `550` | `PL1=4; M2=PUL` | `M` = `15` | `550` → `4` |
| `550` | `PL1=4; M2=SU_GIU` | `M` = `12` | `550` → `4` |
| `550` | `PL1=4; M2=SU_GIU_M` | `M` = `13` | `550` → `4` |
| `550` | `PL1=5` | `PL` = `5` | `550` |
| `550` | `PL1=5; M1=0` | `M` = `0` | `550` → `5` |
| `550` | `PL1=5; M1=O/I` | `M` = `9` | `550` → `5` |
| `550` | `PL1=5; M1=OFF` | `M` = `10` | `550` → `5` |
| `550` | `PL1=5; M1=ON` | `M` = `11` | `550` → `5` |
| `550` | `PL1=5; M1=PUL` | `M` = `15` | `550` → `5` |
| `550` | `PL1=5; M1=SU_GIU` | `M` = `12` | `550` → `5` |
| `550` | `PL1=5; M1=SU_GIU_M` | `M` = `13` | `550` → `5` |
| `550` | `PL1=5; M2=0` | `M` = `0` | `550` → `5` |
| `550` | `PL1=5; M2=O/I` | `M` = `9` | `550` → `5` |
| `550` | `PL1=5; M2=OFF` | `M` = `10` | `550` → `5` |
| `550` | `PL1=5; M2=ON` | `M` = `11` | `550` → `5` |
| `550` | `PL1=5; M2=PUL` | `M` = `15` | `550` → `5` |
| `550` | `PL1=5; M2=SU_GIU` | `M` = `12` | `550` → `5` |
| `550` | `PL1=5; M2=SU_GIU_M` | `M` = `13` | `550` → `5` |
| `550` | `PL1=5; PL1=0` | `OUT_AUX_CHANNEL` = `0` | `550` → `5` |
| `550` | `PL1=5; PL1=1` | `OUT_AUX_CHANNEL` = `1` | `550` → `5` |
| `550` | `PL1=5; PL1=2` | `OUT_AUX_CHANNEL` = `2` | `550` → `5` |
| `550` | `PL1=5; PL1=3` | `OUT_AUX_CHANNEL` = `3` | `550` → `5` |
| `550` | `PL1=5; PL1=4` | `OUT_AUX_CHANNEL` = `4` | `550` → `5` |
| `550` | `PL1=5; PL1=5` | `OUT_AUX_CHANNEL` = `5` | `550` → `5` |
| `550` | `PL1=5; PL1=6` | `OUT_AUX_CHANNEL` = `6` | `550` → `5` |
| `550` | `PL1=5; PL1=7` | `OUT_AUX_CHANNEL` = `7` | `550` → `5` |
| `550` | `PL1=5; PL1=8` | `OUT_AUX_CHANNEL` = `8` | `550` → `5` |
| `550` | `PL1=5; PL1=9` | `OUT_AUX_CHANNEL` = `9` | `550` → `5` |
| `550` | `PL1=5; PL2=0` | `OUT_AUX_CHANNEL` = `0` | `550` → `5` |
| `550` | `PL1=5; PL2=1` | `OUT_AUX_CHANNEL` = `1` | `550` → `5` |
| `550` | `PL1=5; PL2=2` | `OUT_AUX_CHANNEL` = `2` | `550` → `5` |
| `550` | `PL1=5; PL2=3` | `OUT_AUX_CHANNEL` = `3` | `550` → `5` |
| `550` | `PL1=5; PL2=4` | `OUT_AUX_CHANNEL` = `4` | `550` → `5` |
| `550` | `PL1=5; PL2=5` | `OUT_AUX_CHANNEL` = `5` | `550` → `5` |
| `550` | `PL1=5; PL2=6` | `OUT_AUX_CHANNEL` = `6` | `550` → `5` |
| `550` | `PL1=5; PL2=7` | `OUT_AUX_CHANNEL` = `7` | `550` → `5` |
| `550` | `PL1=5; PL2=8` | `OUT_AUX_CHANNEL` = `8` | `550` → `5` |
| `550` | `PL1=5; PL2=9` | `OUT_AUX_CHANNEL` = `9` | `550` → `5` |
| `550` | `PL1=6` | `PL` = `6` | `550` |
| `550` | `PL1=6; M=3` | `ADDR_TYPE` = `0`; `MAIN_GROUP` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1`; `REG` = `1` | `550` → `6` |
| `550` | `PL1=6; M=4` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `1` | `550` → `6` |
| `550` | `PL1=6; M=5` | `ADDR_TYPE` = `0`; `MAIN_GROUP` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `0` | `550` → `6` |
| `550` | `PL1=6; M=6` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `1` | `550` → `6` |
| `550` | `PL1=6; M=7` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `0` | `550` → `6` |
| `550` | `PL1=6; M=8` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1`; `REG` = `1` | `550` → `6` |
| `550` | `PL1=6; S=0` | `PIR` = `0` | `550` → `6` |
| `550` | `PL1=6; S=1` | `PIR` = `1` | `550` → `6` |
| `550` | `PL1=6; S=2` | `PIR` = `2` | `550` → `6` |
| `550` | `PL1=6; S=3` | `PIR` = `3` | `550` → `6` |
| `550` | `PL1=6; T=0` | `HOURS` = `0`; `MINUTES` = `0`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=1` | `HOURS` = `0`; `MINUTES` = `0`; `SECONDS` = `30` | `550` → `6` |
| `550` | `PL1=6; T=2` | `HOURS` = `0`; `MINUTES` = `1`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=3` | `HOURS` = `0`; `MINUTES` = `2`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=4` | `HOURS` = `0`; `MINUTES` = `5`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=5` | `HOURS` = `0`; `MINUTES` = `10`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=6` | `HOURS` = `0`; `MINUTES` = `15`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=7` | `HOURS` = `0`; `MINUTES` = `20`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=8` | `HOURS` = `0`; `MINUTES` = `30`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=9` | `HOURS` = `0`; `MINUTES` = `40`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; M=0` | `ADDR_TYPE` = `0`; `MAIN_GROUP` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1` | `550` → `6` |
| `550` | `PL1=6; M=1` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1`; `REG` = `0` | `550` → `6` |
| `550` | `PL1=7` | `PL` = `7` | `550` |
| `550` | `PL1=7` | Referenced conversion rule absent from source | `550` → `7` |
| `550` | `PL1=8` | `PL` = `8` | `550` |
| `550` | `PL1=8` | Referenced conversion rule absent from source | `550` → `8` |
| `550` | `PL1=9` | `PL` = `9` | `550` |
| `550` | `PL1=9; M=0` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `20` | `550` → `9` |
| `550` | `PL1=9; M=1` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `15` | `550` → `9` |
| `550` | `PL1=9; M=2` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `25` | `550` → `9` |
| `550` | `PL1=9; M=3` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `60` | `550` → `9` |
| `550` | `PL1=9; M=PUL` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `15`; `STOP_TIME` = `20` | `550` → `9` |
| `550` | `PL1=9; M=SLA` | `LOCAL_BUTTON` = `12`; `M` = `11` | `550` → `9` |
| `550` | `M2=0` | `M` = `0` | `550` |
| `550` | `M2=1` | `M` = `1`; `T_TIME ` = `1` | `550` |
| `550` | `M2=2` | `M` = `1`; `T_TIME ` = `2` | `550` |
| `550` | `M2=3` | `M` = `1`; `T_TIME ` = `3` | `550` |
| `550` | `M2=4` | `M` = `1`; `T_TIME ` = `4` | `550` |
| `550` | `M2=5` | `M` = `1`; `T_TIME ` = `5` | `550` |
| `550` | `M2=6` | `M` = `1`; `T_TIME ` = `6` | `550` |
| `550` | `M2=7` | `M` = `1`; `T_TIME ` = `7` | `550` |
| `550` | `M2=8` | `M` = `1`; `T_TIME ` = `8` | `550` |
| `550` | `M2=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `2` | `550` |
| `550` | `M2=O/I` | `M` = `9` | `550` |
| `550` | `M2=OFF` | `M` = `10` | `550` |
| `550` | `M2=ON` | `M` = `11` | `550` |
| `550` | `M2=PUL` | `M` = `15` | `550` |
| `550` | `M2=SU_GIU` | `M` = `12` | `550` |
| `550` | `M2=SU_GIU_M` | `M` = `13` | `550` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `2180` and the installed model | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware without treating wildcard sentinels as literal installed values | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`6`, `7`, `400`, `401`, `404`, `406`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions, and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

### Existing Device-specific diagnostic notes


| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 82`, brand, line, and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware/build | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3`, `6`, `13` | hardware, microcontroller, and Device ID when supported | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | determine the four installed Module/Object roles | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine Module system/address configuration | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values | [Configuration](../../diagnostics/dim35-configuration.md) |

The six physical configurator positions documented by the official sheet provide independent evidence for the expected ordinary addressed-form configurator count, but an observed `DIMENSION 1` read is still required for hardware corroboration.

## Functional applicability


The official sheet documents four major product arrangements:

1. one lighting or shutter load with local control;
2. two independent lighting loads with two local controls;
3. one lighting load with local control plus remote-actuator/scenario control;
4. one shutter load with local control plus remote-actuator/scenario control.

For lighting, physical modes include cyclic `ON`/`OFF`, separate `ON`/`OFF`, slave operation, `PUL`, and delayed-`OFF` presets. For automation, physical modes include timed `UP/DOWN`, bistable and monostable shutter control.

The remote-control side supports point-to-point, room, group, and general addressing plus lighting, automation, and programmed-scenario functions. Virtual configuration exposes a broader parameter surface than physical configurators.

Generic WHO frame grammar remains canonical under [`WHO 1` - Lighting](../../functional/who-1-lighting/) and [`WHO 2` - Automation](../../functional/who-2-automation/).

## Observed behavior and corroboration

No additional publishable runtime observation is asserted beyond observations explicitly retained elsewhere on this page.

## Programming


A programmer must resolve local actuator topology and front/remote command topology separately. It must evaluate the Device-specific condition/conversion graph rather than treating this as one fixed actuator Object.

See [Configuration Programming](../../programming/configuration-programming.md), [Object Programming](../../programming/object-programming.md), and [Programming Validation](../../programming/validation.md).

## Source reconciliation


The archived zero-crossing technical and instruction sheets establish additional product constraints:

- the Device has four documented operating arrangements: one local lighting/shutter load, two local lighting loads, one local lighting load plus remote/scenario control, and one local shutter load plus remote/scenario control;
- software configuration can expose four independent logical addresses - two actuator addresses and two front-control addresses - even though the physical configurator surface is shared;
- delayed-`OFF` lighting behavior is explicitly suitable for linked loads such as light/fan arrangements and must remain tied to the selected mode;
- operation without a connected neutral is supported only under documented load and production constraints, with reduced load limits and an explicit product procedure for that operating arrangement;
- the front control and contact portions are separable, and range-specific LED/current behavior is product hardware metadata rather than OpenWebNet topology.

These facts supplement the four-Module catalogue topology and are constraints on a future configurator/validator.

## Evidence limits and open work


- Add sanitized hardware fingerprints for at least one commercial variant.
- Corroborate installed `modobj`, firmware/build, configurator count, Module/Object topology, addresses, and configuration.
- Continue document discovery for older revisions and range-specific sheets.
- Compare zero-crossing item `2180` experimentally with non-zero-crossing item `1184`, keeping hardware and load-control differences explicit.
- Resolve catalogue conditions that use values outside the firmware-level physical enum.

## Sources


- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
- [Programming](../../programming/)

- `H4672M2-ean-product-sheet.pdf`, printed/PDF p. 1: exact `H4672M2` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/57/52/575284f0fb0bde456e0e5122bbf632c2e03739d15658ba7533e3a93b83ba94f7.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4672M2); SHA-256 `575284f0fb0bde456e0e5122bbf632c2e03739d15658ba7533e3a93b83ba94f7`.
- `LN4672M2-ean-product-sheet.pdf`, printed/PDF p. 1: exact `LN4672M2` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/6b/19/6b19c5a1e1d740e4fd4168bccb23f77109a45c4d988d1b444e313ccb64c1a4a5.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4672M2); SHA-256 `6b19c5a1e1d740e4fd4168bccb23f77109a45c4d988d1b444e313ccb64c1a4a5`.
- `AM5852M2-ean-product-sheet.pdf`, printed/PDF p. 1: exact `AM5852M2` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/c3/f4/c3f44f472988b7718fe4ad50aa3ae512aa004e2f532391ea983bf2775bc23315.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5852M2); SHA-256 `c3f44f472988b7718fe4ad50aa3ae512aa004e2f532391ea983bf2775bc23315`.
