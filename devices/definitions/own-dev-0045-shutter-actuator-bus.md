# Shutter actuator bus

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0045` | Project identity |
| Technical description | Flush-mounted bus shutter actuator with position and preset management | Canonical catalogue plus reconciled Device sources |
| Commercial identities | `H4661M2`, `LN4661M2`, `AM5861M2`, `067557` | Canonical commercial records |
| Catalogue item | `1586` | Implementation evidence |
| Main catalogue system | Automation | Implementation evidence |
| Item model / `modobj` | `48` | Implementation evidence |
| Firmware definition | `192 / -1.-1.-1` | Implementation evidence |
| Declared Modules | `1` | Firmware catalogue |
| Categories | Automation, Shutters, Actuator | Capability model |

Flush-mounted bus shutter actuator with position and preset management.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4661M2` | established catalogue identity for item `1586` | canonical commercial record |
| BTicino - LivingLight | `LN4661M2` | established catalogue identity for item `1586` | canonical commercial record |
| BTicino - Matix | `AM5861M2` | established catalogue identity for item `1586` | canonical commercial record |
| Legrand - Céliane | `067557` | established catalogue identity for item `1586` | canonical commercial record |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `H4661M2` | `8005543478288` | [Archived original](https://archive.openwebnet-ha.org/sha256/de/dd/dedd7ad5fd015532902e19745201329e4261d4b663035d931beb77fb5db4d162.pdf), `H4661M2-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `LN4661M2` | `8005543478295` | [Archived original](https://archive.openwebnet-ha.org/sha256/36/be/36be120c08d83fcf4c17b696e4ed9bd56d6a2e84a61a5f6afdc34bc73ced6dca.pdf), `LN4661M2-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `AM5861M2` | `8005543478271` | [Archived original](https://archive.openwebnet-ha.org/sha256/e3/2b/e32b59a57ebbd1b45db21c916cd2ec4808224b082ee2e05ad46f28d978c465f7.pdf), `AM5861M2-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `067557` | `3245060675578` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/13/11/13116e4a406b60cffd3ab03a97d6d0d2d92e808dbde9f923017a07971ba74997.pdf), `067557-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| AUTOMATISME | technical/system documentation | revision/date as printed | Advanced shutter actuator family and preset behavior | [Archived original](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |
| ST-00000900-EN | technical sheet | 2021-03-23 | H4661M2 / LN4661M2 / 067557 / AM5861M2; addressing, motor type, calibration and modes | - | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00000900-EN.pdf) |
| `H4661M2-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `H4661M2` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/de/dd/dedd7ad5fd015532902e19745201329e4261d4b663035d931beb77fb5db4d162.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4661M2) |
| `LN4661M2-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `LN4661M2` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/36/be/36be120c08d83fcf4c17b696e4ed9bd56d6a2e84a61a5f6afdc34bc73ced6dca.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4661M2) |
| `AM5861M2-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `AM5861M2` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/e3/2b/e32b59a57ebbd1b45db21c916cd2ec4808224b082ee2e05ad46f28d978c465f7.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5861M2) |
| `067557-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `067557` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/13/11/13116e4a406b60cffd3ab03a97d6d0d2d92e808dbde9f923017a07971ba74997.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue/actionneur-myhome-up-celiane-avec-commande-integree-pour-volets-motorises) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Controlled load | One shutter motor channel | ST-00000900-EN |
| Motor models | Standard motor with manual calibration or pulse operation | ST-00000900-EN |
| Position management | After endpoint acquisition, supports 100 positions and preset operation | ST-00000900-EN |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1586` | Implementation evidence |
| Technical item description | Shutter actuator bus | Implementation evidence |
| Main system | Automation | Implementation evidence |
| Item model / `modobj` | `48` | Implementation evidence |
| Commercial records | `4` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `192` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `192` | `1` | `218` Shutter actuator | Fixed/designated metadata | `669` | `514` | `464` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `192` | Physical configuration | supported route for this Device family |
| `192` | Virtual Configuration | supported route for this Device family |
| `192` | Advanced Configuration | supported route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `192` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `192` | `A` | `0..9` | `0` | A; Environment |
| `192` | `PL` | `0..9` | `0` | PL; Light Point |
| `192` | `M` | `0..2`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `15` = `PUL`; `11` = `SLA` | `0` | M; Mode (SU_GIU, Su_GIU_M, 1,2, `PUL`, `SLA`) |
| `192` | `TYPE` | `1..2` | `1` | TYPE; Shutter type Standard - Value : 1 Pulse - Value : 2 |
| `192` | `PRE` | `0..9` | `0` | PRE; Shutter management preset number |
| `192` | `G1` | `0..9` | `0` | G1; Group 1 |

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
| `192` | `1` | `218` | `4911` | No textual predicate stored | `115` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `192` | `218` | `597` | `SHUTTER_TYPE` | `0` = Standard automatic without slats; `3` = Standard with slats | `0` | Shutter type |
| `192` | `218` | `598` | `ROLLING` | `1..100` (entire reusable range retained) | `70` | Rolling to tilting switch pulse duration |
| `192` | `218` | `599` | `TILTING` | `1..100` (entire reusable range retained) | `70` | Tilting to rolling switch pulse duration |
| `192` | `218` | `600` | `P10` | `0..100` (entire reusable range retained) | `100` | Preset of position P10 |
| `192` | `218` | `601` | `PRESET_NUMBER` | `10` | `0` | Preset; reusable default `0` is outside this subset; filter supplies no replacement default |
| `192` | `218` | `602` | `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety (entire reusable range retained) | `1` | Priority |
| `192` | `218` | `4440` | `UP_SHUTTER_TIME_MINUTES` | `0..9` (entire reusable range retained) | `0` | UP shutter calbration time (m) |
| `192` | `218` | `4453` | `UP_SHUTTER_TIME_SECONDS` | `0..59` (entire reusable range retained) | `0` | UP shutter calbration time (s) |
| `192` | `218` | `4466` | `DOWN_SHUTTER_TIME_MINUTES` | `0..9` (entire reusable range retained) | `0` | DOWN shutter calbration time (m) |
| `192` | `218` | `4479` | `SLATS_ROTATION_TIME_DOWN_H` | `0..27` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is all the way down - HIGH BYTE (ms) |
| `192` | `218` | `4492` | `SLATS_ROTATION_TIME_DOWN_L` | `0..255` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is all the way down - LOW BYTE (ms) |
| `192` | `218` | `4505` | `SLATS_ROTATION_TIME_MIDDLE_H` | `0..27` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is in middle position - HIGH BYTE (ms) |
| `192` | `218` | `4518` | `SLATS_ROTATION_TIME_MIDDLE_L` | `0..255` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is in middle position - LOW BYTE (ms) |
| `192` | `218` | `4531` | `SLATS_ROTATION_STEP_NUMBER` | `3..100` (entire reusable range retained) | `4` | SLATS ROTATION step number |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `115` | `M=0` | `MODE` = `0`; `LOCAL_BUTTON` = `0` | `115` |
| `115` | `M=1` | `MODE` = `0`; `LOCAL_BUTTON` = `2` | `115` |
| `115` | `M=2` | `MODE` = `0`; `LOCAL_BUTTON` = `3` | `115` |
| `115` | `M=11` | `MODE` = `11`; `LOCAL_BUTTON` = `0` | `115` |
| `115` | `M=12` | `MODE` = `0`; `LOCAL_BUTTON` = `0` | `115` |
| `115` | `M=13` | `MODE` = `0`; `LOCAL_BUTTON` = `1` | `115` |
| `115` | `M=15` | `MODE` = `15`; `LOCAL_BUTTON` = `0` | `115` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve item `1586` / `modobj = 48` identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware tuple while preserving wildcard sentinels | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate item-specific Module/Object topology `218` | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after active Object/system context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration against firmware/Object filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Advanced shutter actuation with calibrated position/preset behavior; configuration selects addressing, mode and motor type.

## Observed behavior and corroboration

No sanitized hardware fingerprint or Device-specific protocol capture is currently retained for this exact technical item.

## Programming

Programming must select installed firmware applicability, resolve slot/Object alternatives through catalogue conditions, apply relation filters, and preserve configuration-mode boundaries.

## Source reconciliation

The canonical catalogue establishes the commercial records, firmware applicability, topology, configuration fields, filters and conditions. Publisher sources above are used only for behaviors they directly document; missing dedicated sheets remain explicit gaps.

## Evidence limits and open work

- Recover any missing dedicated publisher sheets for the exact identities.
- Capture a sanitized hardware fingerprint covering identity, firmware, modules, addressing and configuration.
- Corroborate condition/filter behavior through MyHOME Suite and controlled configuration changes.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Archived original](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)

- `H4661M2-ean-product-sheet.pdf`, printed/PDF p. 1: exact `H4661M2` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/de/dd/dedd7ad5fd015532902e19745201329e4261d4b663035d931beb77fb5db4d162.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4661M2); SHA-256 `dedd7ad5fd015532902e19745201329e4261d4b663035d931beb77fb5db4d162`.
- `LN4661M2-ean-product-sheet.pdf`, printed/PDF p. 1: exact `LN4661M2` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/36/be/36be120c08d83fcf4c17b696e4ed9bd56d6a2e84a61a5f6afdc34bc73ced6dca.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4661M2); SHA-256 `36be120c08d83fcf4c17b696e4ed9bd56d6a2e84a61a5f6afdc34bc73ced6dca`.
- `AM5861M2-ean-product-sheet.pdf`, printed/PDF p. 1: exact `AM5861M2` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/e3/2b/e32b59a57ebbd1b45db21c916cd2ec4808224b082ee2e05ad46f28d978c465f7.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5861M2); SHA-256 `e32b59a57ebbd1b45db21c916cd2ec4808224b082ee2e05ad46f28d978c465f7`.

- `067557-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `067557` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/13/11/13116e4a406b60cffd3ab03a97d6d0d2d92e808dbde9f923017a07971ba74997.pdf); [publisher source](https://www.legrand.fr/pro/catalogue/actionneur-myhome-up-celiane-avec-commande-integree-pour-volets-motorises); SHA-256 `13116e4a406b60cffd3ab03a97d6d0d2d92e808dbde9f923017a07971ba74997`.
