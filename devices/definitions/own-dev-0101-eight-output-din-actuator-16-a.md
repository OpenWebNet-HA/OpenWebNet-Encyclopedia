# Eight-output DIN `ON`/`OFF` actuator 16 A

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0101` | Project identity |
| Technical description | Eight-output DIN `ON`/`OFF` lighting actuator with zero-current switching | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSW1005`, `002604` | Canonical commercial records and publisher guides |
| Catalogue item | `1156` | Canonical catalogue |
| Main catalogue system | Automation (`lighting_automation`) | Canonical catalogue |
| Item model / `modobj` | `159` | Canonical catalogue |
| Firmware definition | `-1.-1.-1` | Canonical catalogue wildcard applicability |
| Declared Modules | `8` | Canonical firmware catalogue |
| Categories | Lighting, Actuator, DIN, Lighting Management | Catalogue and publisher capability evidence |

This Device is the shared technical definition behind Legrand `0 026 04 / 002604` and BTicino `BMSW1005`. It provides eight independently controlled `ON`/`OFF` lighting outputs, local output controls, BUS/SCS integration, zero-current switching, physical/virtual configuration, and - in the earlier Lighting Management documentation - Push'n Learn association.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSW1005` | Established identity | canonical item `1156`; 2025 MyHOME guide and BUS/SCS guides |
| Legrand | `0 026 04` / `002604` | Established identity | canonical item `1156`; dedicated technical sheets, PEP and BUS/SCS guides |

The later BUS/SCS guides explicitly write the pair as “`0 026 04` or `BMSW1005`”, providing direct publisher evidence that the two commercial references describe the same technical actuator.

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `BMSW1005` | `8005543485484` | [Archived original](https://archive.openwebnet-ha.org/sha256/06/66/0666a5adbe30c536820735ffd0dca78f6725b0aa251fbc65248f288ff63a0e51.pdf), `BMSW1005-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `F01132EN-04.pdf` | technical sheet | `/04`, updated `2017-11-06` | Full document, PDF pp. 1-3; `0 026 04` | [Archived original](https://archive.openwebnet-ha.org/sha256/f0/c6/f0c6c1e4cf149269079d9b0a542d29c05fa790c9b3afe5e438697d51b456b3a2.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/F01132EN-04.pdf) |
| `F01132FR-03.pdf` | technical sheet | `/03`, updated `2013-03-01` | Full document, PDF pp. 1-3; `0 026 04` | [Archived original](https://archive.openwebnet-ha.org/sha256/44/c2/44c2f82aa9be266ec385f9219b996f343fac7b5c261d38fbf95287866121e667.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/F01132FR-03.pdf) |
| `LE03171AC.pdf` | installation / wiring sheet | revision `AC` | Full document, PDF pp. 1-2; `0 026 04` | [Archived original](https://archive.openwebnet-ha.org/sha256/67/a0/67a04907f1904828ce69f3599014c3a72aaeffc6a6259e9f0a158a3986567cb1.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE03171AC.pdf) |
| `LE04385AB_EN.pdf` | Push'n Learn technical guide | revision `AB`, 2014-07 | Full 10-page guide; programming workflow referenced by the `/03` sheet | [Archived original](https://archive.openwebnet-ha.org/sha256/1a/6d/1a6dc1f2007ad55b85f50fdede27c0fe3024dbcb1b45773254189e9aff6d8c78.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE04385AB_EN.pdf) |
| `LE04385AB_FR.pdf` | Push'n Learn technical guide | revision `AB`, 2014-07 | Full 10-page guide; French revision of the same workflow | [Archived original](https://archive.openwebnet-ha.org/sha256/fb/fb/fbfbd3e8d941aa3dd17f73097e4c4dbffbd29b8e9eb34b913ad5dffa05cb6fe9.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE04385AB_FR.pdf) |
| `LGRP-2013-015-V1-FR.pdf` | Product Environmental Profile | `V1-FR`, 2013-01 | Full document, PDF pp. 1-4; `0 026 04` | [Archived original](https://archive.openwebnet-ha.org/sha256/36/55/36558f262322d9a75109b71193fc3f0c7a7d7addb9e24bf75045057390a6e48d.pdf) | [Official source](https://assets.legrand.com/pim/DOCUMENT/LGRP-2013-015-V1-FR.pdf) |
| `MyHOME-Technical-Guide.pdf` | system / product guide | current archived revision, metadata 2025-06 | Printed p. 99 / PDF p. 99; `BMSW1005` identity, description and load table | [Archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) | [Official source](https://www.bticino.com/sites/default/files/2024-02/MyHOME%20Technical%20Guide.pdf) |
| `le10699ad-en.pdf` | BUS/SCS hotel / device guide | revision `AD`, 2019 | Printed/PDF p. 36; programming example printed p. 157 / PDF p. 157 | [Archived original](https://archive.openwebnet-ha.org/sha256/02/bd/02bde8a8120d34ca8921a8ffeb82c725880b5e09b42888548561c18001d35607.pdf) | [Official source](https://assets.legrand.com/general/mediagrp/np-ft-gt/le10699ad-en.pdf) |
| `le10699aa-fr.pdf` | BUS/SCS hotel / device guide | revision `AA`, 2018 | Printed/PDF p. 24; programming example printed p. 103 / PDF p. 103 | [Archived original](https://archive.openwebnet-ha.org/sha256/48/54/4854112b1d66d371515e11e1759d3a88d68cd2dad465a25c8799d55a74298d30.pdf) | [Official source](https://assets.legrand.com/general/mediagrp/np-ft-gt/le10699aa-fr.pdf) |
| `LE04280AA.pdf` | publisher-linked wiring sheet | revision `AA` | Publisher-linked from the `002604` product page, but the PDF itself depicts `0 026 02` / 4 x 16 A; excluded from Device-specific facts | [Archived original](https://archive.openwebnet-ha.org/sha256/94/7c/947c7c7db73629689e1858107d83ceea972e69af85d4066fbf22e7bd664ffb36.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE04280AA.pdf) |
| `BMSW1005-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `BMSW1005` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/06/66/0666a5adbe30c536820735ffd0dca78f6725b0aa251fbc65248f288ff63a0e51.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMSW1005) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Outputs | `8` independent `ON`/`OFF` channels | dedicated sheets; MyHOME guide |
| Mains supply | `100..240 Vac`, `50/60 Hz` | `F01132EN-04`, `F01132FR-03`, `LE03171AC` |
| Output technology | relay switching with zero-current synchronisation / zero-crossing | dedicated sheets; later BUS/SCS guides |
| Per-output local control | one local control button per output; usable before configuration | dedicated sheets; BUS/SCS guides |
| BUS connection | `1 x RJ45` BUS/SCS connection | dedicated sheets |
| Supply terminals | `1` supply terminal block; screw terminals; input capacity `2 x 2.5 mm²` | `F01132EN-04` |
| Load terminals | `8` load terminal blocks; output capacity `2 x 1.5 mm²` or `1 x 2.5 mm²` | `F01132EN-04` |
| DIN width | `10` modules | dedicated sheets; MyHOME guide |
| Envelope / impact protection | `IP20` when installed in an enclosure; `IK04` | dedicated sheets |
| Operating temperature | `-5..+45 °C` | dedicated sheets |
| Storage temperature | `-20..+70 °C` | dedicated sheets |
| No-load consumption | `0.9 W` | dedicated sheets; BUS/SCS guides |
| Product weight | `310 g` | dedicated sheets |
| Packaged mass | `457 g` including unit packaging | `LGRP-2013-015-V1-FR` |
| Resistive / tungsten-halogen load at `230 V` | `3680 W / 16 A` per output | dedicated sheets; MyHOME guide |
| Linear fluorescent load at `230 V` | `10 x (2 x 36 W) / 4.3 A` per output | dedicated sheets; MyHOME guide |
| Separate transformer load at `230 V` | `3680 VA / 16 A` per output | dedicated sheets; MyHOME guide |
| Compact fluorescent load at `230 V` | `1150 VA / 5 A` per output | dedicated sheets; MyHOME guide |
| LED load at `230 V` | `1 x 500 VA / 2.1 A` per output | dedicated sheets; MyHOME guide |
| Single-phase requirement | all output contacts use the same supply phase; required for zero-current switching | `F01132EN-04`, `F01132FR-03`, `LE03171AC` |
| Overall dimensions | `178 x 83 x 66 mm` | `F01132EN-04`, printed p. 2 / PDF p. 2; overall envelope |
| BUS distance limit | `500 m` maximum between power supply and furthest device | Same sheet, BUS wiring, p. 2 |
| Resistive / tungsten-halogen at `110 V` | `1760 W / 16 A` per output | Same sheet, load matrix, p. 1 |
| Linear fluorescent at `110 V` | `5 x (2 x 36 W) / 4.3 A` per output | Same sheet, load matrix, p. 1 |
| Separate transformer at `110 V` | `1760 VA / 16 A` per output | Same sheet, load matrix, p. 1 |
| Compact fluorescent at `110 V` | `550 VA / 5 A` per output | Same sheet, load matrix, p. 1 |
| LED at `110 V` | `1 x 250 VA / 2.1 A` per output | Same sheet, load matrix, p. 1 |

The older dedicated sheets describe the contact as a bistable relay. The later BUS/SCS guides instead describe a normally-open monostable relay while also documenting status memory. This conflict is retained under Source reconciliation rather than normalized.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1156` | canonical catalogue |
| Technical item description | `DIN - Switch 8 x 16 A - 230V` | canonical catalogue |
| Main system | `lighting_automation` / Automation | canonical catalogue |
| Item model / `modobj` | `159` | canonical catalogue |
| Commercial records | `2` | canonical catalogue |
| Commercial codes | `002604`, `BMSW1005` | canonical catalogue and publisher sources |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `199` | `-1` | `-1` | `-1` | `8` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `199` | `1` | `6` Light actuator | Fixed/designated metadata | `737` | `6` | `506` |
| `199` | `2` | `6` Light actuator | Fixed/designated metadata | `738` | `6` | `506` |
| `199` | `3` | `6` Light actuator | Fixed/designated metadata | `739` | `6` | `506` |
| `199` | `4` | `6` Light actuator | Fixed/designated metadata | `740` | `6` | `506` |
| `199` | `5` | `6` Light actuator | Fixed/designated metadata | `741` | `6` | `506` |
| `199` | `6` | `6` Light actuator | Fixed/designated metadata | `742` | `6` | `506` |
| `199` | `7` | `6` Light actuator | Fixed/designated metadata | `743` | `6` | `506` |
| `199` | `8` | `6` Light actuator | Fixed/designated metadata | `744` | `6` | `506` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

All eight slots are fixed to the same Light actuator Object. The distinct conversion rules preserve the channel-specific mapping; the empty condition expressions do not make the conversion rules interchangeable.

## Configuration modes

| Firmware | Mode | Catalogue mode | Description |
| --- | --- | --- | --- |
| `199` | Virtual Configuration | `1` | software configuration route |
| `199` | Advanced Configuration | `2` | catalogue-declared advanced route |
| `199` | Physical configuration | `0` | physical configurator route |

The 2013 French sheet also documents Push'n Learn as a Lighting Management association procedure. That procedure is not represented as a separate firmware configuration-mode row in the canonical catalogue and disappears from the parameter-setting list of the 2017 English sheet.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `199` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `199` | `A` | `0..9` | `0` | A; Environment |
| `199` | `G` | `0..9` | `0` | G (0-9) |
| `199` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (0-4, Pul, Sla) |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `A` (configuration `2018`) | physical documentation: `1..9`; software uses Area `0..10` | area / zone base |
| `G` (configuration `4065`) | physical documentation: `1..9` | physical group number |
| `M` (configuration `2027`) | codes `0..4` select the documented standard/timed modes; `PUL` selects pushbutton behavior and `SLA` selects slave operation | operating modality |


Physical configuration has no `PL` configurator for this product. The published rule is that the eight actuator addresses are derived by incrementing the base address across outputs 1 through 8.

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


### Product interpretation and source differences

**Object `6` - Light actuator - product interpretation.**

Reusable Object `6` exposes a broader surface than the dedicated product sheets explain. Device relation filters `725`, `1870`, `1894`, `1895`, `1896`, and `1897` must be applied before presenting the reusable Object values as Device capability.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `199` | `1` | `6` | `4956` | No textual predicate stored | `7206` |
| `199` | `2` | `6` | `4937` | No textual predicate stored | `7207` |
| `199` | `3` | `6` | `4938` | No textual predicate stored | `7208` |
| `199` | `4` | `6` | `4957` | No textual predicate stored | `7209` |
| `199` | `5` | `6` | `4958` | No textual predicate stored | `7210` |
| `199` | `6` | `6` | `4959` | No textual predicate stored | `7211` |
| `199` | `7` | `6` | `4961` | No textual predicate stored | `7212` |
| `199` | `8` | `6` | `4962` | No textual predicate stored | `7213` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `199` | `6` | `725` | `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open (entire reusable range retained) | `0` | Per energy management (State on Reset) |
| `199` | `6` | `1870` | `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing (entire reusable range retained) | `0` | Load_control_mode |
| `199` | `6` | `1894` | `LOCAL_BUTTON` | `1` = `ON`/`OFF`; `15` = Pushbutton; `18` = Timed `ON`; `9` = `ON` - `OFF` | `0` | Local button modality; reusable default `0` is outside this subset; filter supplies no replacement default |
| `199` | `6` | `1895` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `199` | `6` | `1896` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `199` | `6` | `1897` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `7206` | `A=0` | `PL` = `0` | `7206` |
| `7206` | `A=1` | `PL` = `1` | `7206` |
| `7206` | `A=2` | `PL` = `1` | `7206` |
| `7206` | `A=3` | `PL` = `1` | `7206` |
| `7206` | `A=4` | `PL` = `1` | `7206` |
| `7206` | `A=5` | `PL` = `1` | `7206` |
| `7206` | `A=6` | `PL` = `1` | `7206` |
| `7206` | `A=7` | `PL` = `1` | `7206` |
| `7206` | `A=8` | `PL` = `1` | `7206` |
| `7206` | `A=9` | `PL` = `1` | `7206` |
| `7207` | `A=0` | `PL` = `0` | `7207` |
| `7207` | `A=1` | `PL` = `2` | `7207` |
| `7207` | `A=2` | `PL` = `2` | `7207` |
| `7207` | `A=3` | `PL` = `2` | `7207` |
| `7207` | `A=4` | `PL` = `2` | `7207` |
| `7207` | `A=5` | `PL` = `2` | `7207` |
| `7207` | `A=6` | `PL` = `2` | `7207` |
| `7207` | `A=7` | `PL` = `2` | `7207` |
| `7207` | `A=8` | `PL` = `2` | `7207` |
| `7207` | `A=9` | `PL` = `2` | `7207` |
| `7208` | `A=0` | `PL` = `0` | `7208` |
| `7208` | `A=1` | `PL` = `3` | `7208` |
| `7208` | `A=2` | `PL` = `3` | `7208` |
| `7208` | `A=3` | `PL` = `3` | `7208` |
| `7208` | `A=4` | `PL` = `3` | `7208` |
| `7208` | `A=5` | `PL` = `3` | `7208` |
| `7208` | `A=6` | `PL` = `3` | `7208` |
| `7208` | `A=7` | `PL` = `3` | `7208` |
| `7208` | `A=8` | `PL` = `3` | `7208` |
| `7208` | `A=9` | `PL` = `3` | `7208` |
| `7209` | `A=0` | `PL` = `0` | `7209` |
| `7209` | `A=1` | `PL` = `4` | `7209` |
| `7209` | `A=2` | `PL` = `4` | `7209` |
| `7209` | `A=3` | `PL` = `4` | `7209` |
| `7209` | `A=4` | `PL` = `4` | `7209` |
| `7209` | `A=5` | `PL` = `4` | `7209` |
| `7209` | `A=6` | `PL` = `4` | `7209` |
| `7209` | `A=7` | `PL` = `4` | `7209` |
| `7209` | `A=8` | `PL` = `4` | `7209` |
| `7209` | `A=9` | `PL` = `4` | `7209` |
| `7210` | `A=0` | `PL` = `0` | `7210` |
| `7210` | `A=1` | `PL` = `5` | `7210` |
| `7210` | `A=2` | `PL` = `5` | `7210` |
| `7210` | `A=3` | `PL` = `5` | `7210` |
| `7210` | `A=4` | `PL` = `5` | `7210` |
| `7210` | `A=5` | `PL` = `5` | `7210` |
| `7210` | `A=6` | `PL` = `5` | `7210` |
| `7210` | `A=7` | `PL` = `5` | `7210` |
| `7210` | `A=8` | `PL` = `5` | `7210` |
| `7210` | `A=9` | `PL` = `5` | `7210` |
| `7211` | `A=0` | `PL` = `0` | `7211` |
| `7211` | `A=1` | `PL` = `6` | `7211` |
| `7211` | `A=2` | `PL` = `6` | `7211` |
| `7211` | `A=3` | `PL` = `6` | `7211` |
| `7211` | `A=4` | `PL` = `6` | `7211` |
| `7211` | `A=5` | `PL` = `6` | `7211` |
| `7211` | `A=6` | `PL` = `6` | `7211` |
| `7211` | `A=7` | `PL` = `6` | `7211` |
| `7211` | `A=8` | `PL` = `6` | `7211` |
| `7211` | `A=9` | `PL` = `6` | `7211` |
| `7212` | `A=0` | `PL` = `0` | `7212` |
| `7212` | `A=1` | `PL` = `7` | `7212` |
| `7212` | `A=2` | `PL` = `7` | `7212` |
| `7212` | `A=3` | `PL` = `7` | `7212` |
| `7212` | `A=4` | `PL` = `7` | `7212` |
| `7212` | `A=5` | `PL` = `7` | `7212` |
| `7212` | `A=6` | `PL` = `7` | `7212` |
| `7212` | `A=7` | `PL` = `7` | `7212` |
| `7212` | `A=8` | `PL` = `7` | `7212` |
| `7212` | `A=9` | `PL` = `7` | `7212` |
| `7213` | `A=0` | `PL` = `0` | `7213` |
| `7213` | `A=1` | `PL` = `8` | `7213` |
| `7213` | `A=2` | `PL` = `8` | `7213` |
| `7213` | `A=3` | `PL` = `8` | `7213` |
| `7213` | `A=4` | `PL` = `8` | `7213` |
| `7213` | `A=5` | `PL` = `8` | `7213` |
| `7213` | `A=6` | `PL` = `8` | `7213` |
| `7213` | `A=7` | `PL` = `8` | `7213` |
| `7213` | `A=8` | `PL` = `8` | `7213` |
| `7213` | `A=9` | `PL` = `8` | `7213` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate catalogue item `1156` / `modobj = 159` identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | resolve the applicable firmware tuple while preserving wildcard `-1.-1.-1` semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate the eight fixed Light actuator Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect the eight incremented lighting addresses only after slot/Object context is known | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | compare runtime configuration with the `A/G/M/AID` firmware surface and Object restrictions | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The Device is an eight-channel lighting actuator in the Automation system and exposes Light actuator Object `6` on all eight fixed slots. Its primary functional surface is [Lighting](../../functional/who-1-lighting/README.md). Publisher material also positions it in Lighting Management and hotel-room BUS/SCS installations.

## Observed behavior and corroboration

No publishable Device-specific hardware capture is currently retained for this exact technical item. Publisher documentation does establish that local output buttons remain usable before configuration and that the zero-current-switching function requires the product supply and output contacts to use the same phase.

## Programming

Programming must preserve the eight fixed Light actuator channels and the distinction between physical, virtual, and advanced configuration. Physical configuration uses `A`, `G`, and `M`, derives the eight output addresses from the configured base, and does not use a separate `PL` configurator per channel. Software programming should resolve each output through its catalogue slot/Object relationship and Device-specific filters rather than treating reusable Object `6` as an unconstrained Light actuator surface.

Push'n Learn is documented by the earlier Lighting Management material but is omitted from the parameter-setting section of the 2017 English technical sheet, so it should be treated as revision-dependent rather than universally available.

## Source reconciliation

The canonical catalogue, dedicated technical sheets, later BUS/SCS guides, and current MyHOME guide agree that `002604 / 0 026 04` and `BMSW1005` are the same eight-output actuator and agree on the principal supply, form factor, BUS connection, zero-current switching, local controls, and load ratings. The `310 g` product mass in the technical sheets and the `457 g` packaged mass in the PEP have different scopes and are not contradictory.

The main revision difference concerns programming: the 2013 French sheet and 2014 EN/FR Push'n Learn guides document the manual association workflow, while the 2017 English sheet omits Push'n Learn from parameter setting. A separate publisher conflict remains unresolved: the dedicated `F01132` sheets describe a bistable relay, while the later `le10699AA/AD` guides describe a normally-open monostable relay and also document status memory. The catalogue's `STATE_RESET` surface supports configurable reset-state behavior but does not resolve the mechanical relay terminology.

`LE04280AA.pdf` is linked from the current `002604` product page but its content is for `0 026 02` / four outputs. It is retained in the archive for provenance and excluded from this Device's electrical and topology facts.

## Evidence limits and open work

- Capture a sanitized hardware fingerprint covering identity, firmware, all eight Modules, addresses and configuration.
- Resolve the publisher conflict between “bistable relay” in the dedicated sheets and “normally-open monostable relay” in the later BUS/SCS guides.
- The current BTicino generated product-sheet endpoint for `BMSW1005` was access-controlled/non-PDF during this run, so its binary was not archived; the current publisher catalogue page remains useful corroborating web evidence.
- `AID` is retained from the canonical implementation model, but the reviewed product PDFs do not give a Device-specific semantic explanation beyond the implementation label “ID”.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Lighting](../../functional/who-1-lighting/README.md)

- `BMSW1005-ean-product-sheet.pdf`, printed/PDF p. 1: exact `BMSW1005` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/06/66/0666a5adbe30c536820735ffd0dca78f6725b0aa251fbc65248f288ff63a0e51.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMSW1005); SHA-256 `0666a5adbe30c536820735ffd0dca78f6725b0aa251fbc65248f288ff63a0e51`.
