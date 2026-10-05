# 1-10 V ballast dimmer

## Summary

F413N combines a switching relay with an analogue control output to dim fluorescent ballasts or compatible LED drivers. Although marketed as a 1–10 V dimmer, its configurable minimum output can also reach 0 V. Local short presses switch the load; long presses adjust brightness.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0142` | Project identity |
| Technical description | 1-10 V ballast dimmer | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `003656`, `F413N` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1597` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `141` | Main association; independent of project ID |
| Firmware definition | `175` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Actuators | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `003656` | Established catalogue identity | Manufacturer database commercial record `1709` explicitly links this SKU to item `1597` |
| BTicino | `F413N` | Established catalogue identity | Manufacturer database commercial record `1597` explicitly links this SKU to item `1597` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F413N` | `8012199894461` | `F413N-publisher-product-sheet.pdf` PDF p. 1 |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ST-00000901-EN.pdf` | Technical Sheet ST-00000901-EN | `ST-00000901-EN; 23/03/2021` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/b3/58/b35812017eaa42deb82245af5db63a3c68e4de87c2f3019996c9c0f360ebe2a1.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00000901-EN.pdf) |
| `U2099C.pdf` | Legacy manufacturer technical documentation | `U2099C-01PC-12W46; printed revision label` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/46/76/46760e8898ea7c091713edb862cf44c4cccbd871b1f6eb82bc3b3841dac52cbf.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/U2099C.pdf) |
| `F413N-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 05.10.2026` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/9a/f0/9af037809958dc3ed0d4d40724e61ddee5ad034ecd0fe0288d3a28c5e51bcccd.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-F413N&include_technical=1) |
| `F413N-italian-product-sheet.pdf` | Exact Italian product export | `Captured 05/10/2026; compliance-template date does not establish product publication date` | PDF pp. 1-1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/e1/e1/e1e10008f1a79c9b17613372d63c5d9b27539dc41a829568c4f195aeffbe0265.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F413N) |
| `ST_00000901_IT.pdf` | Legacy manufacturer technical documentation | `ST_00000901_IT; 23/03/2021` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/38/79/3879722f95f768c0f2c85c573eddeaa93d08a9129af53fba148396ec9a7bfb7d.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/ST_00000901_IT.pdf) |
| `ST_00000901_EN.pdf` | English counterpart of manufacturer-linked document | `ST_00000901_EN; 23/03/2021` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/b3/58/b35812017eaa42deb82245af5db63a3c68e4de87c2f3019996c9c0f360ebe2a1.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/ST_00000901_EN.pdf) |
| `ST-00002703-EN.pdf` | Technical Sheet ST-00002703-EN | `ST-00002703-EN; 16/06/2026` | Retained 19-page original; exact-product technical, configuration and operating sections reviewed where applicable. Source-specific facts and remaining limits are scoped in the dossier; this does not claim a line-by-line review of every manual page. | [Archived original](https://archive.openwebnet-ha.org/sha256/b2/f5/b2f5090b601e33cdef9ba666108848ff4d9800792ccd5b7c14385da300bf0ffa.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002703-EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1597`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS nominal / operating supply | `27 Vdc / 18..27 Vdc` | `ST-00000901-EN` printed/PDF pp. 1-3; `U2099C` PDF p. 1 |
| Current draw | `30 mA` | `ST-00000901-EN` printed/PDF pp. 1-3; `U2099C` PDF p. 1 |
| Temperature / size | `-5..45 °C; 2 DIN modules` | `ST-00000901-EN` printed/PDF pp. 1-3; `U2099C` PDF p. 1 |
| Switching capacity | `2 A; 460 W at 230 V / 220 W at 110 V` | `ST-00000901-EN` printed/PDF pp. 1-3; `U2099C` PDF p. 1 |
| Analogue output | `1..10 V nominal; minimum can be configured to 0 V; 6 mA maximum` | `ST-00000901-EN` printed/PDF pp. 1-3; `U2099C` PDF p. 1 |
| Ballasts / drivers | `maximum 10 compatible ballasts or LED drivers` | `ST-00000901-EN` printed/PDF pp. 1-3; `U2099C` PDF p. 1 |
| Dissipated power | `1 W` | `ST-00000901-EN` printed/PDF pp. 1-3; `U2099C` PDF p. 1 |
| Protection codes | `IP20 / IK04; printed property labels reversed` | `ST-00000901-EN` printed/PDF pp. 1-3; `U2099C` PDF p. 1 |
| Contactors | `U2099C recommends above 1.5 A and requires them for loads above the direct 2 A rating` | `ST-00000901-EN` printed/PDF pp. 1-3; `U2099C` PDF p. 1 |


### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Classification frequency values of zero are separate from explicitly documented Wi-Fi carriers; a negative connected-object classification does not exclude remote control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system radio frequency | `No` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system LON | `No` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system Powernet | `No` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Other bus systems | `Other` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Radio frequency bidirectional | `No` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Model | `Dimming actuator` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Mounting method | `DRA (DIN-rail adaptor)` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Width in number of modular spacings | `2` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| With bus connection | `Yes` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Bus module detachable | `No` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Substation input | `No` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Local operation/hand operation | `Yes` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| With LED indication | `Yes` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Number of outputs | `1` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Output power (Min-Max) | `0-460 W` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Power boost suitable | `Yes` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Type of load | `Capacitive` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Max. control current | `6 mA` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Parallel-service possible | `No` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Frequency (Min-Max) | `50-60 Hz` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Degree of protection (IP) | `IP20` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |
| Compatible with Casambi | `No` | `F413N-publisher-product-sheet.pdf` PDF p. 2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1597` | Canonical catalogue |
| Technical item description | Ballast DIN dimmer 1-10 V | Canonical catalogue |
| Item family | 0; key `4` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `141` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `175` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `175` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `607` | `8` | `421` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `175` | Virtual Configuration | `1` | Association key `1` |
| `175` | Advanced Configuration | `2` | Association key `2` |
| `175` | Physical configuration | `0` | Association key `3` |


No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `A / PL / G` | physical `1..9` / `1..9` / `0..9`; virtual room `0..10`, point `0..15`, ten groups `0..255` | `ST-00000901-EN` printed/PDF pp. 1-3; `U2099C` PDF p. 1 |
| `M=0 / SLA / PUL` | master / slave / monostable master | `ST-00000901-EN` printed/PDF pp. 1-3; `U2099C` PDF p. 1 |
| `M=1..4` | slave `OFF` delay `1..4` min; virtual `0..255` s | `ST-00000901-EN` printed/PDF pp. 1-3; `U2099C` PDF p. 1 |
| `L=0,1,2,3,4` | minimum voltage 1,1.5,2,0,0.5 V | `ST-00000901-EN` printed/PDF pp. 1-3; `U2099C` PDF p. 1 |
| `TYPE=0 / TYPE=1` | fluorescent soft start after 1.5 s / immediate LED soft start | `ST-00000901-EN` printed/PDF pp. 1-3; `U2099C` PDF p. 1 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `175` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `175` | `A` | `0..9` | `0` | A; Enviroment |
| `175` | `PL` | `0..9` | `0` | PL; Light Point |
| `175` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (1-4, Pul, Sla) |
| `175` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |
| `175` | `L` | `0..4` | `0` | L; Dimmer L |
| `175` | `TY` | `0..1` | `0` | TY |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `8` - Dimmer actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality; mode (M,S + PULL) |
| `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled | `0` | State saving on reset |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `MIN_LEVEL` | `1..100` | `1` | Minimum level |
| `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge | `0` | Type of load; Default value depends on device. |
| `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard | `0` | Voltage standard |
| `MIN_LEVEL_ADV` | `1..100` | `0` | Minimum level advanced; Default value depends on device and Type of load value |
| `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable | `0` | Enable / Disable minimum level |
| `G1` | `0..255` | `0` | Group 1 |
| `G2` | `0..255` | `0` | Group 2 |
| `G3` | `0..255` | `0` | Group 3 |
| `G4` | `0..255` | `0` | Group 4 |
| `G5` | `0..255` | `0` | Group 5 |
| `G6` | `0..255` | `0` | Group 6 |
| `G7` | `0..255` | `0` | Group 7 |
| `G8` | `0..255` | `0` | Group 8 |
| `G9` | `0..255` | `0` | Group 9 |
| `G10` | `0..255` | `0` | Group 10 |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `175` | `1` | `8` | `4152` | No textual predicate stored | `11` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `175` | `8` | `396` | `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Funzionalità di pulsante locale ridotta (Local button mode) |
| `175` | `8` | `397` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Funzionalità di temporizzazione non presente (Hours) |
| `175` | `8` | `398` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Funzionalità di temporizzazione non presente (Minutes) |
| `175` | `8` | `399` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Funzionalità di temporizzazione non presente (Seconds) |
| `175` | `8` | `400` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge; `2` = Forced capacitive; `3` = Forced inductive; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI | `0` | Funzionalità di specifica carico pilotato ridotta (Type of load) |
| `175` | `8` | `401` | `MIN_LEVEL_ADV` | `1..100` (entire reusable range retained) | `0` | Minimum level advanced |
| `175` | `8` | `402` | `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable (entire reusable range retained) | `0` | enable disable minimum level |
| `175` | `8` | `2171` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `11` | `L=0` | `MIN_LEVEL` = `1`; `TYPE_STANDARD` = `0` | `11` |
| `11` | `L=1` | `MIN_LEVEL` = `13`; `TYPE_STANDARD` = `0` | `11` |
| `11` | `L=2` | `MIN_LEVEL` = `25`; `TYPE_STANDARD` = `0` | `11` |
| `11` | `L=3` | `MIN_LEVEL` = `1`; `TYPE_STANDARD` = `1` | `11` |
| `11` | `L=4` | `MIN_LEVEL` = `3`; `TYPE_STANDARD` = `1` | `11` |
| `11` | `M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `11` |
| `11` | `M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `11` |
| `11` | `M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `11` |
| `11` | `M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `11` |
| `11` | `M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `11` |
| `11` | `M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `11` |
| `11` | `M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `11` |
| `11` | `TY=0` | `TYPE_LOAD` = `5` | `11` |
| `11` | `TY=1` | `TYPE_LOAD` = `6` | `11` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `141` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `8` - Dimmer actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |


These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system/model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Physical A/PL addressing uses `1..9`; Suite uses room `0..10` and lighting point 0..15. Physical group G uses `0..9`; Suite provides ten group fields 0..255. Master `M=0`, slave `M=SLA` and monostable master `M=PUL` are documented; `PUL` ignores room/general controls. Delayed slave `OFF` uses `M=1..4` minutes physically or `0..255` seconds in Suite, for point-to-point control only: the master switches off immediately, its slave after the delay. Slave `PUL` requires software. Physical minimum `L=0`/1/2/3/4 selects 1/1.5/2/0/0.5 V. The virtual minimum parameter is `1..100` in this sheet. `TYPE=0` fluorescent introduces a 1.5-second switch-on delay for soft start; `TYPE=1` LED switches on immediately with soft start. Suite exposes additional load-type labels, including DALI and DSI; these labels do not establish a DALI/DSI hardware port on this analogue product. MyHOME Server automatic configuration uses one channel. The source also describes Lighting Management Push&Learn and Virtual Configurator routes. Keep the load connection at least 3 m as shown, and apply the sheet’s 10 A protective breaker independently of its 2 A relay rating.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session/validation method remains in [Programming](../../programming/).

## Source reconciliation

The exact sheet and U2099C agree on 2 A, maximum ten ballasts and 6 mA analogue current. The older shared guide’s F413 entry is a different reference; its 2.5 A/four-ballast values are not transferred to F413N. IP and IK property labels are reversed in the sheet; the codes are preserved with their correct meanings. The database’s dimmer Object is configuration metadata, independently of the one physical output. The 2026 EOS compatibility sheet lists F413N from batch 09W14 and 003656 from 10W05, with software configuration required for that ecosystem.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `ST-00000901-EN.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `U2099C.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `F413N-publisher-product-sheet.pdf` | Exact named variant; complete classification attributes captured above and EAN under Commercial identities. Sheet-specific ratings remain independently scoped. |
| `F413N-italian-product-sheet.pdf` | Exact named commercial/product export; values and descriptive defects reconciled against technical documents. Compliance-template dates do not date the product. |
| `ST_00000901_IT.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `ST_00000901_EN.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `ST-00002703-EN.pdf` | Explicit compatibility/reference inventory and ecosystem restrictions for this product; EOS electrical/display specifications are not transferred. |

## Evidence limits and open work

Actual driver compatibility, the effect of the minimum parameter across firmware revisions, production applicability and installed diagnostics remain unmeasured.

No installed hardware revision or microcontroller fingerprint is retained for this cluster. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Canonical catalogue extraction and reconciliation are complete for the retained evidence; further documentation discovery, runtime corroboration and final evidence closure remain partial.

### Discovered sources outside this review

These publisher-linked sources were identified but were not retained or used as evidence. Their presence is not evidence of installed firmware, a certified test result or additional capability.

| Source | Remaining scope | Publisher provenance |
| --- | --- | --- |
| `U2099C.pdf` | Software licence, declaration or ancillary document; not used for product specifications here | [Publisher listing](https://assets.legrand.com/pim/NP-FT-GT/U2099C.pdf) |
| `Brochure Living_NOW 2M.pdf` | Software licence, declaration or ancillary document; not used for product specifications here | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Brochure Living_NOW 2M.pdf) |
| `Brochure Living_NOW 3M.pdf` | Software licence, declaration or ancillary document; not used for product specifications here | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Brochure Living_NOW 3M.pdf) |
| `Catalogue Living_NOW 2M.pdf` | Software licence, declaration or ancillary document; not used for product specifications here | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Catalogue Living_NOW 2M.pdf) |
| `Catalogue Living_NOW 3M.pdf` | Software licence, declaration or ancillary document; not used for product specifications here | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Catalogue Living_NOW 3M.pdf) |

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
