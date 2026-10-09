# Multi-application Room Controller

## Summary

`BMSW3003` / `048847` combines a shutter motor channel, a 16 A switched-lighting or ventilation channel and two analogue dimming channels in one Room Controller. It supports manual or sensor-driven operation and bus pairing; the catalogue represents its four load channels plus a fifth controller Module.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0077` | Project identity |
| Technical description | Multi-application Room Controller | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSW3003`, `048847` | Canonical commercial records |
| Catalogue item | `89` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `173` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `5` | Canonical firmware catalogue |
| Categories | Lighting Management, Room Controller, Relay actuator, Blind control | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSW3003` | Established identity | canonical commercial record for item `89` |
| Legrand | `048847` | Established identity | canonical commercial record for item `89` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `048847` | `3245060488475` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/ba/24/ba2400e8829a0d7a0d52474c8f86080c33eb6833e1b4c4604e2ec12765da7b81.pdf), `048847-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BTicino General Catalogue product sheet | publisher product sheet | current catalogue export | `BMSW3003` multi-application Room Controller outputs and SCS interfaces; printed p. 1 / PDF p. 1 | [Archived original](https://archive.openwebnet-ha.org/sha256/d1/7c/d17c79d0a00ce5901c44991a992cb0d6fabfe9abbcb36338294eac4e433ef593.pdf) | [Official source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMSW3003) |
| `048847-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact SKU/GTIN metadata retained;technical/installation downloads examined separately below;generic ETIM attributes not adopted | [Archived HTML](https://archive.openwebnet-ha.org/sha256/ba/24/ba2400e8829a0d7a0d52474c8f86080c33eb6833e1b4c4604e2ec12765da7b81.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue-archives/controleurs-faux-plafond-2-circuits-declairage-1-ouvrant-et-1-contact-cvc-mosaic) |
| `BT00587_b_IT.pdf` | Italian exact technical sheet | BT00587-b-IT;2013-11-12 | `BMSW3003`;full 4 pages | [Archived original](https://archive.openwebnet-ha.org/sha256/d7/20/d720eaf75c918746408f18ed4df24cb7a8bac5d1646cf8e1d73c1285f2ed95a5.pdf) | [Publisher source](https://dar.bticino.it/asset/Documents/BT00587_b_IT.pdf) |
| `F01124EN-01.pdf` | English exact technical sheet | F01124EN/01;created 2010-10-28,updated 2013-02-12 | `048847`;full 4 pages | [Archived original](https://archive.openwebnet-ha.org/sha256/da/82/da82d0918419341b465844effec732d45bf732fc70587c0a48a75cd1f78a6191.pdf) | [Publisher source](https://assets.legrand.com/pim/NP-FT-GT/F01124EN-01.pdf) |
| `F01124FR-01.pdf` | French exact technical sheet | F01124FR/01;created 2010-10-28,updated 2013-02-12 | `048847`;full 4 pages | [Archived original](https://archive.openwebnet-ha.org/sha256/e2/c6/e2c69a12461a618efe3eb2c0a5553cd783286a3eb0d98df80374af125bf2c7d8.pdf) | [Publisher source](https://assets.legrand.com/pim/NP-FT-GT/F01124FR-01.pdf) |
| `LE03166AB.pdf` | Illustrated installation instructions | LE03166AB;date not printed | `048847`;full 4 pages | [Archived original](https://archive.openwebnet-ha.org/sha256/5a/ae/5aae2d51c212eba403c645e3ec1e47cbf6c991eda89f03e6a34c3ed74945416a.pdf) | [Publisher source](https://assets.legrand.com/pim/NP-FT-GT/LE03166AB.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply/environment | `100..240 Vac`, `50..60 Hz`; `3 W` standby/no-load; `-5..45 °C` operating, `-20..70 °C` storage; IP20, IK04; `595 g` | BT00587-b-IT pp. 1–2; F01124EN/FR-01 pp. 1–2 |
| Motor channel 1 | `500 VA` at 230 V /`250 VA` at 110 V; `2.1 A` | BT00587-b-IT and F01124EN/FR-01, p. 1 |
| Switched channel 2 | Incandescent/halogen `3680 W`/`1760 W`, `16 A`; transformers `3680 VA`/`1760 VA`, `16 A`; fluorescent 10×(`2× 36 W`)/5×(`2× 36 W`), `4.3 A`; CFL `1150/550 VA`, `5 A` | BT00587-b-IT and F01124EN/FR-01, p. 1 |
| LED channel 2 limit discrepancy | F01124 EN/FR:`1150/550 VA`, `5 A`; LE03166AB:`1000/500 VA`, `4.3 A`. Neither adopted as a universal rating | F01124EN/FR-01, p. 1; LE03166AB, p. 1 |
| Dimming channels 3/4 | Each `4.3 A`; `1000 VA` at 230 V and `500 VA` at 110 V per channel for linear/halogen ballast loads. CFL: technical W, instruction VA. LED column `500/250 VA`, `2.1 A`; diagram labels `50 mA` /0-10 V | BT00587-b-IT, p. 1; F01124EN/FR-01, p. 1; LE03166AB, p. 1 |
| Bus ports | Local 1, 3, 4 share `200 mA`; port 2 marked Do not use in wiring. Export says four local bus inputs: discrepancy retained; upstream bus separate | BT00587-b-IT, p. 3; F01124EN/FR-01, pp. 2–3; LE03166AB, pp. 1, 3 |
| Dimensions/terminals | `147 × 240 mm` body, `275 mm` mounting extent, `50 mm` arrows; screw `2 × 2.5 mm²`, analogue ≤ `1.5 mm²`; `150 m` sensor link, `500 m` upstream reach | BT00587-b-IT/F01124EN/FR-01, pp. 2–3 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `89` | Canonical catalogue |
| Technical item | Multi-application Room Controller | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `173` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `173` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `89` | `BMSW3003` | `1` | `5` | Empty in source |
| `1788` | `048847` | `2` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `285` | `-1` | `-1` | `-1` | `5` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `285` | `1` | `29` Automation actuator | Fixed/designated metadata | `2514` | `490` | `1164` |
| `285` | `2` | `16` Actuator for sensors | Fixed/designated metadata | `2515` | `479` | `1165` |
| `285` | `3` | `8` Dimmer actuator | Fixed/designated metadata | `2516` | `8` | `1166` |
| `285` | `4` | `8` Dimmer actuator | Fixed/designated metadata | `2517` | `8` | `1166` |
| `285` | `5` | `167` Room controller | Fixed/designated metadata | `2518` | `167` | `1167` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `285` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `285` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `8` - Dimmer actuator

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL`, `G1`, `G2` | Reusable schema; apply the Device and firmware restrictions below. |
| Operation, timing and presentation | `M`, `LOCAL_BUTTON`, `DELAYED_OFF`, `STATE_SAVING_ON_RESET`, `HOURS`, `MINUTES`, `SECONDS`, `MIN_LEVEL`, `TYPE_LOAD`, `TYPE_STANDARD`, `MIN_LEVEL_ADV`, `MIN_AUTO`, `G3`, `G4`, `G5`, `G6`, `G7`, `G8`, `G9`, `G10` | Reusable schema; apply the Device and firmware restrictions below. |

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

### Object `167` - Room controller

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `MODE` | `0` = Stand-alone mode; `1` = Supervision mode | `0` | Modality; Mode |

### Object `16` - Actuator for sensors

Catalogue Object key `479` maps to external Object `16`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave | `0` | Modality |
| `STOP_TIME` | `1..180`; `182..255`; `0` = Infinite; `181` = 101 | `0` | Stop time (minutes) |
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

### Object `29` - Automation actuator

Catalogue Object key `490` maps to external Object `29`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality; mode (M,S + PULL) |
| `LOCAL_BUTTON` | `12` = Bistable; `13` = Monostable | `12` | Local button modality |
| `STOP_TIME` | `0` = Infinite; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min | `60` | Stop time |
| `SUBTYPE` | `11` = Actuator; `2` = Shutter; `3` = Curtain; `4` = Gate; `5` = Garage door; `15` = Differential restart | `11` | Type of load |
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

### Device-specific interpretation

Firmware `285` declares five Modules for four electrical load channels: slot `1` external Object `29` uses catalogue key `490`, slot `2` external Object `16` uses key `479`, slots 3/4 Object `8`, and slot `5` Object `167`. Preserve those external/internal identifiers and field scopes. Only AID and Advanced Configuration are firmware-associated; no physical configurator schema, Virgin or slot condition/conversion is stored. Object `29` STOP_TIME uses seconds for `1..60` and minute labels `62..65`/`67..70`, omits 61/66, and defaults to 60; Object `16` STOP_TIME is a different minute-domain field with zero Infinite and unusual 181=101 label. Do not merge them. The TYPE_LOAD/TYPE_STANDARD and group domains are reusable definitions; the single state-saving filter has no subset. The MIN_LEVEL_ADV default 0 is out of domain. Deprecated metadata does not establish current discontinuation or an installed software version.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `285` | `8` | `2195` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `89` / `modobj = 173` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`8`, `167`, `16`, `29`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Local controls | UP/STOP/DOWN for motor; ON/OFF for channel 2; short switch/long dim channels 3/4 | LE03166AB, p. 4 |
| Commissioning | Automatic recognition at power-on, Learn and software/remote configuration; manual/sensor operation | BT00587-b-IT, p. 4; F01124EN/FR-01, p. 4 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Wire with mains disconnected. Automatic pairing begins at power-on; BTicino distinguishes standalone and integrated bus installations and documents Plug&Go, Push&Learn and Virtual Configurator. The Legrand sheets specify remote configuration tools 88235/88230; those tool manuals and detailed sensor sheets are not incorporated. Local test buttons switch loads; holding the relevant dimming button adjusts level. The software catalogue mode associations remain distinct from these product commissioning procedures. Use the exact load-specific channel table; the 16 A channel ceiling is not the motor rating. Follow the marked unused local bus port and shared 200 mA budget. Conflicting LED/load-unit ratings are not resolved by selecting the larger value.

## Source reconciliation

The canonical short name is misleading about which channel has 16 A; external Object `29`/key 490 is the motor and Object `16`/key 479 the switched channel. BT00587-b-IT (12 November 2013) and F01124EN/FR-01 (created 28 October 2010, updated 12 February 2013) show 1 motor+1 switched+2 analogue channels, contradicting the Italian export’s four-output headline followed by five role counts (1+2+2). These exact diagrams govern the role description. The export’s four local bus inputs also differs from the wiring’s 1/3/4 shared 200 mA and unused 2; that is unresolved rather than treated as four usable inputs. LE03166AB’s LED switched rating is 1000/500 VA, 4.3 A versus 1150/550 VA, 5 A in regional technical sheets; CFL analogue limits use VA in instructions but W in technical sheets. The switched-channel transformer limits are printed in VA in F01124EN/FR-01 but W in LE03166AB. The motor wiring labels also differ: BT00587-b-IT p. 2 prints +/N and −/L, whereas LE03166AB p. 2 prints +/L and −/N. These unresolved source differences do not establish interchangeable DC polarity; use the applicable manufacturer instruction for the exact installed revision. Regional FR product standard NF EN 50428 differs from EN IEC 60669-2-1; declarations are historical and source-scoped. The retained HTML is used only for exact `048847`/GTIN provenance, not its generic two-output attribute.

Catalogue interpretation is detailed under [Object configuration surfaces](#object-configuration-surfaces); these software records do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- No installed hardware observation is retained. Exact tool manuals, detailed sensor setup, Suite help, referenced drawings and broader current installation guides are unexamined; no commissioning-completion claim is made.
- Catalogue 0-10 V wording, wiring labels and reusable voltage/load settings do not by themselves establish every ballast or LED compatibility. Regional standards and load units are kept source-specific.
- Conflicting bus-port descriptions, motor polarity labels, LED ratings and transformer/CFL units remain unresolved; no installed revision or tested interpretation chooses between them.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `048847-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `048847` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/ba/24/ba2400e8829a0d7a0d52474c8f86080c33eb6833e1b4c4604e2ec12765da7b81.pdf); [publisher source](https://www.legrand.fr/pro/catalogue-archives/controleurs-faux-plafond-2-circuits-declairage-1-ouvrant-et-1-contact-cvc-mosaic); SHA-256 `ba2400e8829a0d7a0d52474c8f86080c33eb6833e1b4c4604e2ec12765da7b81`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0071-0080-2026-10-06.md#own-dev-0077)
