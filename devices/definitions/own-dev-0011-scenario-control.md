# Scenario control

## Summary

This two-module wall control provides four buttons for recalling or programming configured scenarios. Depending on the installation, it works with a scenario module or a scenario programmer to coordinate several actions from one button press.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0011` | Project identity |
| Technical description | Two-module four-button scenario control | Catalogue + official technical sheet |
| Catalogue item | `402` - “Scenario control” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `6` | Implementation evidence |
| Firmware definition | `1.0.0`, firmware `7` | Implementation evidence |
| Declared Modules | `2` | Implementation evidence |
| Categories | Command, Scenario, Multifunction | Capability model |

The Device is a four-button scenario control that can drive scenario modules, programmed `CEN` scenarios, and PLUS scenario representations. The canonical firmware models the four physical keys as two configurable command Modules.

## Commercial identities

The canonical catalogue contains ten Device records. Several database records combine finish variants into one code, while the official technical sheet names the printed references separately.

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC4680` | Established identity | Catalogue cluster + official technical sheet |
| BTicino - Axolute | `HS4680` | Established identity | Catalogue cluster + official technical sheet |
| BTicino - Axolute | `HD4680` | Established identity | Catalogue cluster + official technical sheet |
| BTicino - LivingLight | `L4680` | Established identity | Catalogue cluster + official technical sheet |
| BTicino - LivingLight | `N4680` | Established identity | Catalogue cluster + official technical sheet |
| BTicino - LivingLight | `NT4680` | Established identity | Catalogue cluster + official technical sheet |
| Legrand - Arteor | `573902` | Established identity | Catalogue + official technical sheet |
| Legrand - Arteor | `573903` | Established identity | Catalogue + official technical sheet |
| Legrand - Arteor | `574503` | Established identity | Catalogue + official technical sheet |
| Legrand - Arteor | `574504` | Established identity | Catalogue + official technical sheet |
| Legrand - Céliane | `067217` | Established identity | Catalogue + official technical sheet |
| Legrand - Céliane | `067218` | Established identity | Catalogue + official technical sheet |
| Legrand - Mosaic | `078478` | Established catalogue identity | Canonical catalogue; exact-product technical sheet not retained |
| Legrand - Mosaic | `079178` | Established catalogue identity | Canonical catalogue; exact-product technical sheet not retained |

The count of printed identities exceeds the ten `EN_DEVICE` rows because BTicino finish variants are collapsed into combined catalogue codes such as `HC/HS/HD4680`.

The canonical `EN_DEVICE.code` uses combined `L/N/NT4680`; the named L4680, N4680 and NT4680 rows above expand that catalogue code, rather than establish additional technical items.

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `HC4680` | `8012199774312` | [Archived original](https://archive.openwebnet-ha.org/sha256/1b/60/1b60e34dc0234147d2f62e333f060b8167e9dedf305470d3716d8fd6f46e9575.pdf), `HC4680-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `HS4680` | `8012199774329` | [Archived original](https://archive.openwebnet-ha.org/sha256/e9/72/e9723de6521d8114a9c55b3f77e81fcd8544faa579fc238ceb4eee54f069dfb2.pdf), `HS4680-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `HD4680` | `8012199986241` | [Archived original](https://archive.openwebnet-ha.org/sha256/ba/c9/bac9d769b4b3542ae4d0397813019e0738e1db59a3f599d2c7441cdbac1cd378.pdf), `HD4680-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `L4680` | `8012199812908` | [Archived original](https://archive.openwebnet-ha.org/sha256/dc/fc/dcfc6f8a05a59d667101942c0b31e0e07d46cfac28f45a71fc56b61a0b354530.pdf), `L4680-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `N4680` | `8012199812922` | [Archived original](https://archive.openwebnet-ha.org/sha256/c9/bb/c9bbb720085c750ca7d148866fab49a66f1d0562fd955a8ad46402d151ecd594.pdf), `N4680-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `NT4680` | `8012199812939` | [Archived original](https://archive.openwebnet-ha.org/sha256/48/31/48312b9c56eb9cf1c1c0754cfc561cb9f004f5958c1470b3a553e1f408111840.pdf), `NT4680-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `067217` | `3245060672171` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/83/1a/831a9a80beee59800374c22807f3ed406b18c615a0de23f0a626c3b8ea7f39c7.pdf), `067217-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |
| `067218` | `3245060672188` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/3a/d1/3ad1912f0868fdf963c0a0f7eb8b53960d5fcee3b66abc26ab6599e746f91c0a.pdf), `067218-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00288-c-EN` | Technical sheet | 09/06/2014; PDF pp. 1–4 | Exact named references and all Device-specific configuration/programming pages inspected | [Archived PDF](https://archive.openwebnet-ha.org/sha256/30/34/303432cca6900f183b69227c4c203c211aaeb063b47238f70aeb244b731dc751.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00288-c-EN.pdf) |
| `MQ00288-c-FR` | Technical sheet | 05/05/2014; PDF pp. 1–4 | Exact named references and all Device-specific configuration/programming pages inspected | [Archived PDF](https://archive.openwebnet-ha.org/sha256/6d/f7/6df709af3becb5131015cf62433d7cab1c758dbb9239e1b80125e95b93ea0ee0.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00288-c-FR.pdf) |
| `U3327B` | Installation/use instructions | U3327B01PC-11W36; English PDF pp. 3–6 | 573902/573903; English operation/LED/program/delete instructions inspected; other translations not independently reconciled | [Archived PDF](https://archive.openwebnet-ha.org/sha256/3c/cd/3ccd34b5b6adf4955a0a3dc0532a3cff9bf69387efc3a07710602db26db9bfbc.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/U3327B.pdf) |
| `HC4680-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HC4680` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/1b/60/1b60e34dc0234147d2f62e333f060b8167e9dedf305470d3716d8fd6f46e9575.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4680) |
| `HS4680-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HS4680` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/e9/72/e9723de6521d8114a9c55b3f77e81fcd8544faa579fc238ceb4eee54f069dfb2.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4680) |
| `HD4680-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HD4680` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/ba/c9/bac9d769b4b3542ae4d0397813019e0738e1db59a3f599d2c7441cdbac1cd378.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HD4680) |
| `L4680-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `L4680` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/dc/fc/dcfc6f8a05a59d667101942c0b31e0e07d46cfac28f45a71fc56b61a0b354530.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4680) |
| `N4680-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `N4680` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/c9/bb/c9bbb720085c750ca7d148866fab49a66f1d0562fd955a8ad46402d151ecd594.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-N4680) |
| `NT4680-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `NT4680` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/48/31/48312b9c56eb9cf1c1c0754cfc561cb9f004f5958c1470b3a553e1f408111840.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-NT4680) |
| `067217-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `067217` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/83/1a/831a9a80beee59800374c22807f3ed406b18c615a0de23f0a626c3b8ea7f39c7.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue/commande-4-scenarios-myhome-up-celiane-blanc) |
| `067218-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `067218` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/3a/d1/3ad1912f0868fdf963c0a0f7eb8b53960d5fcee3b66abc26ab6599e746f91c0a.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue/commande-4-scenarios-myhome-up-celiane-titane) |
| `ST-00002122-EN.pdf` | Classe300EOS technical sheet / compatibility matrix | 21 October 2024 | Scenario controls, printed/PDF p. 7; only applicable compatibility rows incorporated | [Archived original](https://archive.openwebnet-ha.org/sha256/e1/a8/e1a8da77199296d9f56ea708402f144b8614473558002c0f8db4ee16eb2f0d0d.pdf) | Publisher URL not retained in manifest |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 flush-mounted modules | `MQ00288-c-EN` |
| User controls | 4 scenario buttons | `MQ00288-c-EN` |
| SCS nominal supply | `27 Vdc` | `MQ00288-c-EN` |
| SCS operating supply | `18..27 Vdc` | `MQ00288-c-EN` |
| Current draw | `9 mA` | `MQ00288-c-EN` |
| Primary physical configurators | `A`, `PL`, `M`, `N`, `DEL` | `MQ00288-c-EN` |

The sheet also describes a destination-level configurator `I` when the control operates across an SCS/SCS interface. Firmware-scoped configuration does not contain an `I` field; reusable Object configuration carries installation and destination level fields. Preserve this as a source-model boundary rather than inventing a firmware field.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `402` | Implementation evidence |
| Main system | Lighting / Automation | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `6` | Implementation evidence |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `6` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `7` | `1` | `0` | `0` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `7` | `1` | `403` Scenario module control | Fixed/designated metadata | `691` | `403` | `480` |
| `7` | `1` | `404` Scheduled scenario | Candidate alternative | `693` | `404` | `481` |
| `7` | `1` | `405` Scenario PLUS Lighting Management | Candidate alternative | `695` | `405` | `482` |
| `7` | `1` | `406` Scheduled scenario PLUS | Candidate alternative | `697` | `406` | `483` |
| `7` | `2` | `403` Scenario module control | Fixed/designated metadata | `692` | `403` | `480` |
| `7` | `2` | `404` Scheduled scenario | Candidate alternative | `694` | `404` | `481` |
| `7` | `2` | `405` Scenario PLUS Lighting Management | Candidate alternative | `696` | `405` | `482` |
| `7` | `2` | `406` Scheduled scenario PLUS | Candidate alternative | `698` | `406` | `483` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `7` | `502` Scene double command virgin | `1`, `2` | `403`, `404`, `405`, `406` | `502` | `22` |

Firmware `7` exposes two configurable Modules.
Virgin Object `502`, **Scene double command virgin**, applies to both slots and permits Objects `403..406`.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `7` | Physical configuration | `0` | Canonical firmware/mode association |
| `7` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `7` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `7` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `7` | `A` | `0..9` | `0` | A; Environment |
| `7` | `PL` | `0..9` | `0` | PL; Light Point |
| `7` | `M` | `0..4`; `14` = `CEN` | `0` | M; Mode (0-4,`CEN`) |
| `7` | `N` | `0..5` | `0` | N; N (0-5) |
| `7` | `DEL` | `0..9` | `0` | DEL; Configurator DEL |

### Published `M` mapping

The technical sheet documents:

| `M` | Physical keys activate |
| ---: | --- |
| `1` | scenarios `1..4` |
| `2` | scenarios `5..8` |
| `3` | scenarios `9..12` |
| `4` | scenarios `13..16` |
| `CEN` | `CEN`/programmed scenario mode |

With no `CEN` selector, the catalogue selects Scenario module Object `403`; with `M=CEN`, it selects Scheduled scenario Object `404`.

Implementation-only `M=FAKE` conditions expose PLUS Objects `405` and `406`; `FAKE` is not part of the physical `M` enum.

### Published delay mapping

| `N` | Delayed key(s) |
| ---: | --- |
| `0` | none |
| `1` | key 1 |
| `2` | key 2 |
| `3` | key 3 |
| `4` | key 4 |
| `5` | all four |

| `DEL` | Delay |
| ---: | --- |
| `0` | none |
| `1` | 1 min |
| `2` | 2 min |
| `3` | 3 min |
| `4` | 4 min |
| `5` | 5 min |
| `6` | 10 min |
| `7` | 15 min |
| `8` | 15 s |
| `9` | 30 s |

### Published address and bus-level scopes

F420 targeting uses physical `A=0..9, PL=1..9`, versus software room `0..10`, point `0..15`. For CEN the sheet gives physical `A/PL=1..9`. Physical destination `I=1..9` selects another local bus, `I=CEN` the riser and `I=0` the whole system; software local-bus destinations extend to `1..15`, and installation level is software-configured. These are the destination semantics in `MQ00288-c-EN/FR`, p. 2; they are not interchangeable with another product’s installation-level I socket.

The CEN table on p. 4 prints `SPE=0, M=CEN`, although neither the principal configurator list nor firmware `7` has an SPE field. This is a source irregularity, not authority to invent another socket. Software PLUS address `1..2047` and button `0..31` are published separately from the unresolved `M=FAKE` catalogue conditions.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `403` - Scenario module control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Scenario activation and modification; `1` = Scenario activation | `0` | Modality |
| `APL` | `0..175`; encoded by `APL=16*A+PL`, with `A=0..10` and `PL=0..15` | `0` | Scenario module address |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number | `0` | Destination level |
| `SCE_BUTT_1` | `1..16` | `1` | Upper button scenario |
| `SCE_BUTT_2` | `1..16` | `2` | Lower button scenario |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `43` = 43 s; `44` = 44 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for upper button |
| `DEL_BUTTON_2` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `36` = 36 s; `37` = 37 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `69` = 9 min; `70` = 10 min | `0` | Activation delay for lower button |

### Object `404` - Scheduled scenario

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `BUTTON_1` | `0..31` | `1` | Upper button |
| `BUTTON_2` | `0..31` | `2` | Lower button |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |
| `START_DELAY` | `0..255` | `10` | Time of restart device (s) |

### Object `405` - Scenario PLUS Lighting Management

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_SCE_1` | `1..255` | `1` | Upper button scenario; Delay (20) |
| `PPT_SCE_2` | `1..255` | `2` | Lower button scenario; Delay (21) |
| `TYPE_OF_REGULATION` | `0` = Regulate all; `1` = Lights only; `2` = Shutters only; `3` = Stereo amplifiers only | `0` | Regulation type; Only if Scenario1=Scenario2 |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for upper button; Only if Scenario1<>Scenario2 |
| `DEL_BUTTON_2` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for lower button; Only if Scenario1<>Scenario2 |

### Object `406` - Scheduled scenario PLUS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | `0..255` | `1` | Scheduled scenario PLUS number |
| `PPT_CEN_HIG` | `0..7` | `0` | Scheduled scenario PLUS number |
| `BUTTON_1` | `0..31` | `1` | Upper button |
| `BUTTON_2` | `0..31` | `2` | Lower button |

### Device-specific interpretation

The two activation-delay enums contain different stored row counts (63 and 56); the complete reusable domains are preserved separately. PLUS predicates use `FAKE`, which is absent from the firmware enum. Physical address and software address limits differ.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `7` | `1` | `403` | `4145` | No textual predicate stored | None |
| `7` | `1` | `403` | `4435` | `M<>CEN` | `14` |
| `7` | `1` | `404` | `4590` | `M=CEN` | `65` |
| `7` | `1` | `405` | `4594` | `M=FAKE` | None |
| `7` | `1` | `406` | `4594` | `M=FAKE` | None |
| `7` | `2` | `403` | `4434` | `M<>CEN` | `13` |
| `7` | `2` | `404` | `4591` | `M=CEN` | `66` |
| `7` | `2` | `405` | `4594` | `M=FAKE` | None |
| `7` | `2` | `406` | `4594` | `M=FAKE` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `7` | `404` | `1707` | `START_DELAY` | `0..255` (entire reusable range retained) | `10` | Start delay |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `13` | `M=1` | `DEST_LEV` = `0`; `INST_LEVEL` = `0`; `M` = `0`; `SCENARIO_BUTTON_1` = `2`; `SCENARIO_BUTTON_2` = `4` | `13` |
| `13` | `M=2` | `DEST_LEV` = `0`; `INST_LEVEL` = `0`; `M` = `0`; `SCENARIO_BUTTON_1` = `6`; `SCENARIO_BUTTON_2` = `8` | `13` |
| `13` | `M=3` | `DEST_LEV` = `0`; `INST_LEVEL` = `0`; `M` = `0`; `SCENARIO_BUTTON_1` = `10`; `SCENARIO_BUTTON_2` = `12` | `13` |
| `13` | `M=4` | `DEST_LEV` = `0`; `INST_LEVEL` = `0`; `M` = `0`; `SCENARIO_BUTTON_1` = `14`; `SCENARIO_BUTTON_2` = `16` | `13` |
| `13` | `N=0` | `DELAY_BUTTON_1` = `0`; `DELAY_BUTTON_2` = `0` | `13` |
| `13` | `N=1` | `DELAY_BUTTON_1` = `0`; `DELAY_BUTTON_2` = `0` | `13` |
| `13` | `N=2; DEL=0` | `DELAY_BUTTON_1` = `0` | `13` → `16` |
| `13` | `N=2; DEL=1` | `DELAY_BUTTON_1` = `60` | `13` → `16` |
| `13` | `N=2; DEL=2` | `DELAY_BUTTON_1` = `62` | `13` → `16` |
| `13` | `N=2; DEL=3` | `DELAY_BUTTON_1` = `63` | `13` → `16` |
| `13` | `N=2; DEL=4` | `DELAY_BUTTON_1` = `64` | `13` → `16` |
| `13` | `N=2; DEL=5` | `DELAY_BUTTON_1` = `65` | `13` → `16` |
| `13` | `N=2; DEL=6` | `DELAY_BUTTON_1` = `70` | `13` → `16` |
| `13` | `N=2; DEL=7` | `DELAY_BUTTON_1` = `71` | `13` → `16` |
| `13` | `N=2; DEL=8` | `DELAY_BUTTON_1` = `15` | `13` → `16` |
| `13` | `N=2; DEL=9` | `DELAY_BUTTON_1` = `30` | `13` → `16` |
| `13` | `N=2` | `DELAY_BUTTON_2` = `0` | `13` |
| `13` | `N=3` | `DELAY_BUTTON_1` = `0`; `DELAY_BUTTON_2` = `0` | `13` |
| `13` | `N=4` | `DELAY_BUTTON_1` = `0` | `13` |
| `13` | `N=4; DEL=0` | `DELAY_BUTTON_2` = `0` | `13` → `19` |
| `13` | `N=4; DEL=1` | `DELAY_BUTTON_2` = `60` | `13` → `19` |
| `13` | `N=4; DEL=2` | `DELAY_BUTTON_2` = `62` | `13` → `19` |
| `13` | `N=4; DEL=3` | `DELAY_BUTTON_2` = `63` | `13` → `19` |
| `13` | `N=4; DEL=4` | `DELAY_BUTTON_2` = `64` | `13` → `19` |
| `13` | `N=4; DEL=5` | `DELAY_BUTTON_2` = `65` | `13` → `19` |
| `13` | `N=4; DEL=6` | `DELAY_BUTTON_2` = `70` | `13` → `19` |
| `13` | `N=4; DEL=7` | `DELAY_BUTTON_2` = `71` | `13` → `19` |
| `13` | `N=4; DEL=8` | `DELAY_BUTTON_2` = `15` | `13` → `19` |
| `13` | `N=4; DEL=9` | `DELAY_BUTTON_2` = `30` | `13` → `19` |
| `13` | `N=5; DEL=0` | `DELAY_BUTTON_1` = `0` | `13` → `16` |
| `13` | `N=5; DEL=1` | `DELAY_BUTTON_1` = `60` | `13` → `16` |
| `13` | `N=5; DEL=2` | `DELAY_BUTTON_1` = `62` | `13` → `16` |
| `13` | `N=5; DEL=3` | `DELAY_BUTTON_1` = `63` | `13` → `16` |
| `13` | `N=5; DEL=4` | `DELAY_BUTTON_1` = `64` | `13` → `16` |
| `13` | `N=5; DEL=5` | `DELAY_BUTTON_1` = `65` | `13` → `16` |
| `13` | `N=5; DEL=6` | `DELAY_BUTTON_1` = `70` | `13` → `16` |
| `13` | `N=5; DEL=7` | `DELAY_BUTTON_1` = `71` | `13` → `16` |
| `13` | `N=5; DEL=8` | `DELAY_BUTTON_1` = `15` | `13` → `16` |
| `13` | `N=5; DEL=9` | `DELAY_BUTTON_1` = `30` | `13` → `16` |
| `13` | `N=5; DEL=0` | `DELAY_BUTTON_2` = `0` | `13` → `19` |
| `13` | `N=5; DEL=1` | `DELAY_BUTTON_2` = `60` | `13` → `19` |
| `13` | `N=5; DEL=2` | `DELAY_BUTTON_2` = `62` | `13` → `19` |
| `13` | `N=5; DEL=3` | `DELAY_BUTTON_2` = `63` | `13` → `19` |
| `13` | `N=5; DEL=4` | `DELAY_BUTTON_2` = `64` | `13` → `19` |
| `13` | `N=5; DEL=5` | `DELAY_BUTTON_2` = `65` | `13` → `19` |
| `13` | `N=5; DEL=6` | `DELAY_BUTTON_2` = `70` | `13` → `19` |
| `13` | `N=5; DEL=7` | `DELAY_BUTTON_2` = `71` | `13` → `19` |
| `13` | `N=5; DEL=8` | `DELAY_BUTTON_2` = `15` | `13` → `19` |
| `13` | `N=5; DEL=9` | `DELAY_BUTTON_2` = `30` | `13` → `19` |
| `14` | No item-side predicate on this branch | Referenced conversion rule absent from source | `14` |
| `65` | `M=CEN` | `IN_AUX_CHANNEL` = `0`; `CEN_BUTT_1` = `1`; `CEN_BUTT_2` = `3` | `65` |
| `66` | `M=CEN` | `IN_AUX_CHANNEL` = `0`; `CEN_BUTT_1` = `2`; `CEN_BUTT_2` = `4` | `66` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 6`, brand/line and installed configurator count | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | resolve the two active scenario Objects | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | obtain configured addresses | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The Device participates in scenario control. Depending on the selected Object, its Modules represent scenario-module, programmed/`CEN`, or PLUS scenario functions. Generic scenario protocol semantics remain canonical under Functional Protocol.

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

For the F420 procedure in `MQ00288-c-EN/FR`, p. 4, unlock the scenario module with a hold of at least 0.5 seconds (green status LED). Hold the chosen control key for four seconds, carry out the system actions, then briefly press the same key to save/exit. Repeat for other scenarios and lock the module again (red LED). Recall uses a brief key press.

The 2014 technical sheets delete one scenario with a control-key hold of at least ten seconds, confirmed by rapid LED flashing for about two seconds. Entire-memory erasure uses DEL on the scenario module for ten seconds, not the control’s DEL configurator. The older exact `573902/573903` user guide `U3327B`, PDF pp. 5–6, instead says at least eight seconds for individual deletion (LED on after three seconds, off after five more) and names module `003551`. Keep these procedures scoped to their sources; no hardware revision cutoff is established.

Resolve each Module’s active Object before applying M/N/DEL conversions. PLUS catalogue branches do not establish a physical FAKE configurator.

## Source reconciliation

The scenario-control documentation has been reconciled with the two-Module catalogue model:

- the four physical buttons map to scenario groups selected by `M`, while the two catalogue Modules represent paired command positions rather than four independent Modules;
- F420-style scenario operation includes explicit scenario programming and deletion workflows with product feedback states;
- `CEN`/programmed-scenario use is distinct from local scenario-module use and must preserve the installation/destination-level context;
- Lighting Management software configuration can represent double-scenario, double-`CEN` and PLUS forms beyond the physical `M` selector;
- `N` and `DEL` are product delay selectors and are already mapped above, but their effect is tied to selected physical buttons rather than to a generic timer Object.

The remaining source gaps concern Mosaic variants and hardware corroboration.

The English technical sheet is dated 9 June 2014 and French 5 May 2014; their four-key scenario groups, N/DEL presets and address/level scopes agree. `U3327B01PC-11W36` is specifically a 573902/573903 user guide, not installation evidence for every variant. Its eight-second deletion threshold differs from the ten-second technical-sheet instruction. Its LED brightness control (hold over two seconds; 0/30/60/100%, 60% marked default) is scoped to those named references. No equivalent LED feature is inferred for all finishes.

The 63-row versus 56-row reusable delay domains, absent SPE field, physical/software address differences and out-of-domain FAKE branches remain explicit. Mosaic SKU identities are established by the catalogue; their missing exact technical sheets are documentation gaps.

The Classe300EOS compatibility table lists 573902/573903 from production `08W51`, L/N/NT/HC/HD/HS4680 from `09W08`, and its named Mosaic/Céliane/574503/574504 codes as all batches. This is compatibility with Classe300EOS, not a general firmware equivalence. The sheet p. 8 excludes physically configured Devices from Classe300EOS compatibility.

## Evidence limits and open work

- Locate direct product documentation for Mosaic `078478` and `079178`.
- Add a sanitized hardware fingerprint and corroborate firmware, configurator count, two-Module projection, addresses and configuration.
- Corroborate the product’s destination-level I mapping against installed Object values; the published level role is now explicit. Resolve the source-specific eight/ten-second deletion threshold and absent SPE socket without assuming a hardware cutoff.
- Preserve any package/finish differences between the several printed BTicino references.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
- [Programming](../../programming/)

- `HC4680-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HC4680` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/1b/60/1b60e34dc0234147d2f62e333f060b8167e9dedf305470d3716d8fd6f46e9575.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4680); SHA-256 `1b60e34dc0234147d2f62e333f060b8167e9dedf305470d3716d8fd6f46e9575`.
- `HS4680-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HS4680` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/e9/72/e9723de6521d8114a9c55b3f77e81fcd8544faa579fc238ceb4eee54f069dfb2.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4680); SHA-256 `e9723de6521d8114a9c55b3f77e81fcd8544faa579fc238ceb4eee54f069dfb2`.
- `HD4680-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HD4680` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/ba/c9/bac9d769b4b3542ae4d0397813019e0738e1db59a3f599d2c7441cdbac1cd378.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HD4680); SHA-256 `bac9d769b4b3542ae4d0397813019e0738e1db59a3f599d2c7441cdbac1cd378`.
- `L4680-ean-product-sheet.pdf`, printed/PDF p. 1: exact `L4680` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/dc/fc/dcfc6f8a05a59d667101942c0b31e0e07d46cfac28f45a71fc56b61a0b354530.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4680); SHA-256 `dcfc6f8a05a59d667101942c0b31e0e07d46cfac28f45a71fc56b61a0b354530`.
- `N4680-ean-product-sheet.pdf`, printed/PDF p. 1: exact `N4680` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/c9/bb/c9bbb720085c750ca7d148866fab49a66f1d0562fd955a8ad46402d151ecd594.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-N4680); SHA-256 `c9bbb720085c750ca7d148866fab49a66f1d0562fd955a8ad46402d151ecd594`.
- `NT4680-ean-product-sheet.pdf`, printed/PDF p. 1: exact `NT4680` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/48/31/48312b9c56eb9cf1c1c0754cfc561cb9f004f5958c1470b3a553e1f408111840.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-NT4680); SHA-256 `48312b9c56eb9cf1c1c0754cfc561cb9f004f5958c1470b3a553e1f408111840`.

- `067217-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `067217` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/83/1a/831a9a80beee59800374c22807f3ed406b18c615a0de23f0a626c3b8ea7f39c7.pdf); [publisher source](https://www.legrand.fr/pro/catalogue/commande-4-scenarios-myhome-up-celiane-blanc); SHA-256 `831a9a80beee59800374c22807f3ed406b18c615a0de23f0a626c3b8ea7f39c7`.
- `067218-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `067218` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/3a/d1/3ad1912f0868fdf963c0a0f7eb8b53960d5fcee3b66abc26ab6599e746f91c0a.pdf); [publisher source](https://www.legrand.fr/pro/catalogue/commande-4-scenarios-myhome-up-celiane-titane); SHA-256 `3ad1912f0868fdf963c0a0f7eb8b53960d5fcee3b66abc26ab6599e746f91c0a`.

- [Semantic review record, 5 October 2026](../../project/review/device-reviews-0011-0020-2026-10-05.md#own-dev-0011)
