# Basic contacts interface

## Summary

The `3477` basic contact interface connects two conventional switches or pushbuttons to the SCS bus, allowing existing controls to operate lighting, shutters, scenes and audio. Its two logical inputs can work independently or pair for a motor command; the compact module fits behind conventional controls.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0072` | Project identity |
| Technical description | Basic contacts interface | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `3477`, `573996`, `049238` | Canonical commercial records |
| Catalogue item | `81` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `152` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `2` | Canonical firmware catalogue |
| Categories | Automation, Contact interface, Basic module | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `3477` | Established identity | canonical commercial record for item `81` |
| Legrand - Arteor | `573996` | Established identity | canonical commercial record for item `81` |
| Legrand | `049238` | Established identity | canonical commercial record for item `81` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `3477` | `8012199653136` | [Archived original](https://archive.openwebnet-ha.org/sha256/f0/95/f095af5e62d424ecaea74869e98ef6007dfa7b4ab9ef96a9b3a0caa95a6f2018.pdf), `3477-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00272-c-EN` | technical sheet | MQ00272-c-EN;2014-06-07 | Printed/PDF pp. 1–8;complete exact `3477` ratings,roles,settings and wiring | [Archived original](https://archive.openwebnet-ha.org/sha256/84/9f/849fecce315893cec920898f9492f474fd2e477f2d6375af65b4c50d580c641b.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00272_c_EN.pdf) |
| F460/F461 installation/configuration compatibility table | compatibility documentation | RA00224AA; retained publisher revision | PDF p. 7: `3477` / `573996` pairing, direct association from batch `10W04` | [Archived original](https://archive.openwebnet-ha.org/sha256/d2/a4/d2a45bbcd72baa0b6e5536baccca8816cce3cdf94414e7b7144763003c1b1e6d.pdf) | [Official source](https://dar.bticino.com/asset/Documents/RA00224AA_EN.pdf) |
| `3477-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Printed/PDF p. 1;exact-reference EAN and complete technical export attributes examined;linked downloads/prices not incorporated | [Archived original](https://archive.openwebnet-ha.org/sha256/f0/95/f095af5e62d424ecaea74869e98ef6007dfa7b4ab9ef96a9b3a0caa95a6f2018.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-3477) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `27 Vdc` SCS; operating `18..27 Vdc`; `3.5 mA` | MQ00272-c-EN, printed/PDF p. 1; Italian export p. 1 |
| Inputs and enclosure | Two no-voltage NO/NC inputs, three connection wires, status LED; Basic enclosure for flush/junction/shutter boxes and ducts | MQ00272-c-EN, pp. 1, 8 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `81` | Canonical catalogue |
| Technical item | Basic contacts interface | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `152` | Canonical inventory |
| Commercial records | `3` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `152` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `81` | `3477` | `1` | `5` | `BTicino_Undefined_Basic contacts interface` |
| `1742` | `573996` | `2` | `11` | Empty in source |
| `1866` | `049238` | `2` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `129` | `-1` | `-1` | `-1` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `129` | `1` | `181` Contact state | Fixed/designated metadata | `846` | `181` | `545` |
| `129` | `1` | `410` Light control | Candidate alternative | `844` | `410` | `544` |
| `129` | `1` | `411` Automation control | Candidate alternative | `830` | `411` | `537` |
| `129` | `1` | `412` Lock/unlock actuator control | Candidate alternative | `832` | `412` | `538` |
| `129` | `1` | `413` Scenario module control | Candidate alternative | `834` | `413` | `539` |
| `129` | `1` | `414` Scheduled scenario | Candidate alternative | `836` | `414` | `540` |
| `129` | `1` | `415` Scenario PLUS Lighting Management | Candidate alternative | `838` | `415` | `541` |
| `129` | `1` | `416` Scheduled scenario PLUS | Candidate alternative | `840` | `416` | `542` |
| `129` | `1` | `417` `AUX` control | Candidate alternative | `1368` | `417` | `721` |
| `129` | `1` | `419` Sound diffusion control | Candidate alternative | `842` | `419` | `543` |
| `129` | `2` | `181` Contact state | Fixed/designated metadata | `847` | `181` | `545` |
| `129` | `2` | `410` Light control | Candidate alternative | `845` | `410` | `544` |
| `129` | `2` | `411` Automation control | Candidate alternative | `831` | `411` | `537` |
| `129` | `2` | `412` Lock/unlock actuator control | Candidate alternative | `833` | `412` | `538` |
| `129` | `2` | `413` Scenario module control | Candidate alternative | `835` | `413` | `539` |
| `129` | `2` | `414` Scheduled scenario | Candidate alternative | `837` | `414` | `540` |
| `129` | `2` | `415` Scenario PLUS Lighting Management | Candidate alternative | `839` | `415` | `541` |
| `129` | `2` | `416` Scheduled scenario PLUS | Candidate alternative | `841` | `416` | `542` |
| `129` | `2` | `417` `AUX` control | Candidate alternative | `1369` | `417` | `721` |
| `129` | `2` | `419` Sound diffusion control | Candidate alternative | `843` | `419` | `543` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `129` | `512` Contact interface single virgin | `1`, `2` | `181`, `410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `419` | `512` | `1` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `129` | Physical configuration | `0` | Canonical firmware/mode association |
| `129` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `129` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `129` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `129` | `A` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB`; `15` = `AUX` | `0` | A; Environment (0-9 `GEN`,`GR`,`AMB`,`AUX`) |
| `129` | `PL1` | `0..9` | `0` | PL1; PL1 - (0-9) |
| `129` | `PL2` | `0..9` | `0` | PL2; PL2 - (0-9) |
| `129` | `M` | `0..9`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `14` = `CEN`; `15` = `PUL` | `0` | M; Mode physical configurator (0-9, `O/I`,`OFF`,`ON`,SU_GIU,SU_GIU_M,`CEN`,`PUL`) |
| `129` | `SPE` | `0..8` | `0` | SPE; Special function command control (0-8) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `181` - Contact state

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `CONTACT_NUMBER` | `1..201` | `1` | Number of contact |

### Object `410` - Light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `1` = Timed `ON`; `2` = Toggle dimmer; `4` = Toggle `ON`/`OFF`; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `20` = `ON` and point to point dimmer; `21` = `OFF` and point to point dimmer; `22` = `ON` and Dimmer; `23` = `OFF` and Dimmer; `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90%; `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `131` = Customized toggle dimmer; `133` = Customized toggle dimmer without regulation; `135` = Customized `ON` and dimmer without regulation; `136` = Customized `OFF` and dimmer without regulation; `137` = Customized `ON` and dimmer with regulation; `138` = Customized `OFF` and dimmer with regulation | `0` | Modality; Mode (MODE+`ON`/`OFF`) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `HOURS` | `0..255` | `0` | Hours; Only for `MOD=128` |
| `MINUTES` | `0..59` | `0` | Minutes; Only for `MOD=128` |
| `SECONDS` | `0..59` | `30` | Seconds; Only for `MOD=128` |
| `LEVEL` | `0..100` | `100` | Level; Only for `MOD=129`, 131, 133, 135, 136, 137, 138 |
| `START_S` | `0..255` | `255` | Soft start speed; Only for `MOD=129`, 131, 133, 135, 136, 137, 138 |
| `STOP_S` | `0..255` | `255` | Soft stop speed; Only for `MOD=129`, 131, 133, 135, 136, 137, 138 |
| `DIMMING_S` | `0..255` | `255` | Dimming speed; Only for `MOD=129`, 131 |
| `T_TIME` | `1` = 1 min; `2` = 2 min; `3` = 3 min; `4` = 4 min; `5` = 5 min; `6` = 15 min; `7` = 30 s; `8` = 0.5 s; `9` = 2 s; `10` = 10 min | `1` | Tabled time; Only for `MOD=1` |

### Object `411` - Automation control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = UP bistable control; `1` = DOWN bistable control; `2` = UP monostable control; `3` = DOWN monostable control; `4` = UP monostable and bistable control; `5` = DOWN monostable and bistable control | `0` | Modality; mode (`UP/DOWN`) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `412` - Lock/unlock actuator control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `1` = Disable; `2` = Enable | `1` | Modality; mode (D/E) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = All systems | `0` | Destination level |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `413` - Scenario module control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Scenario activation and modification; `1` = Scenario activation | `0` | Modality |
| `APL` | `0..175`; encoded by `APL=16*A+PL`, with `A=0..10` and `PL=0..15` | `0` | Scenario module address |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number | `0` | Destination level; Destination level (`0..15`) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `SCE_BUTT_1` | `1..16` | `1` | Scenario number |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay of scenario number |

### Object `414` - Scheduled scenario

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `CEN_BUTT_1` | `0..31` | `1` | Button |
| `MODE` | `0` = Press/release only; `1` = Press/hold/release | `0` | Modality; Mode (Lighting management) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `415` - Scenario PLUS Lighting Management

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = `ON`; `1` = `OFF`; `2` = `ON` with regulation; `3` = `OFF` with regulation | `0` | Modality; Mode (`ON`/`OFF` regulation) |
| `PPT_SCE_1` | `0..255` | `1` | Upper button scenario |
| `TYPE_OF_REGULATION` | `0` = Regulate all; `1` = Lights only; `2` = Shutters only; `3` = Stereo amplifiers only | `0` | Regulation type |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for upper button |

### Object `416` - Scheduled scenario PLUS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | `0..255` | `1` | Scheduled scenario PLUS number |
| `PPT_CEN_HIG` | `0..7` | `0` | Scheduled scenario PLUS number |
| `BUTTON_1` | `0..31` | `1` | Button |
| `MODE` | `0` = Press/release only; `1` = Press/hold/release | `0` | Modality; Mode (Lighting management) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `417` - `AUX` control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Cyclical; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `17` = DOWN Shutter bistable command; `18` = UP shutter monostable command; `4` = Reset BI; `5` = Reset TRI; `6` = Reset `GEN`; `1` = Disable; `2` = Enable; `16` = UP shutter bistable command; `19` = DOWN Shutter monostable command | `0` | Modality; mode(Cyclical,off,on,pul,up,down,...) |
| `OUT_AUX_CH` | `1..15` | `1` | `AUX` channel |
| `TYPE_CONTACT` | No legal values specified in source | `0` | Contact type |

### Object `419` - Sound diffusion control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = `ON`/volume +; `1` = `OFF`/volume -; `2` = Change track; `3` = Switch source; `4` = Toggle `ON`/`OFF` | `0` | Modality; Mode (VOL,ON_OFF) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `3` = General | `0` | Addressing type |
| `A` | `0..9` | `0` | Area |
| `PF` | `0..9` | `0` | Audio point |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `IS_FOLLOW_ME` | `0` = No; `1` = Yes | `1` | Follow me |
| `SOURCE` | `1..9` | `1` | Source |
| `SUB_SOURCE` | `0..255` | `0` | Sub source |
| `CHANNEL` | `0` = Base Band; `1` = Left; `2` = Right; `3` = Stereo; `8` = Base Band and Video; `9` = Left and video; `10` = Right and video; `11` = Left and video | `3` | Channel (BB-Stereo) |

### Device-specific interpretation

Firmware `129` supplies two Modules with identical candidate families and Virgin `512`; each slot is resolved independently. `M=FAKE` selects contact state and PLUS candidates in stored predicates, but FAKE is outside the firmware domain. Object `417` has direct and Virgin membership but no slot-condition row. Filter `1839` restricts light-control `M` to 135–138, excludes reusable default 0 and conflicts with outputs of the physical conversion rules; it does not replace the default or erase the manufacturer’s physical modes. Rule `67` and 69 distinguish ON/OFF and UP/DOWN by slot; rule `76`/77 maps odd/even `F420` scenes, and rule `83` repeats odd scene numbers in both slots. Rule `87` emits CEN button 2 in both slots. Preserve these branches without inventing PL1/PL2 correction. Rules emit `T_TIME ` with a trailing space, `CONTACT_TYPE`, `FOLLOW`, `IN_AUX_CHANNEL` and `OUT_AUX_CHANNEL`, whereas reusable fields include `T_TIME`, `TYPE_CONTACT`, `IS_FOLLOW_ME` and `OUT_AUX_CH`; these are unresolved aliases, not silently normalized identifiers. Sound rules can emit SOURCE 0 outside its `1..9` domain; rule `72` can emit AUX channel 0. M=`10..15` branches under `SPE=2` exceed physical numeric `0..9` and must not be treated as attainable raw configurators. Complete branch tables below retain all these source facts.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `129` | `1` | `181` | `4594` | `M=FAKE` | None |
| `129` | `1` | `410` | `4711` | `SPE=0;M=0;A<>AUX` | `67` |
| `129` | `1` | `410` | `4718` | `SPE=0;M=1;A<>AUX` | `67` |
| `129` | `1` | `410` | `4723` | `SPE=0;M=2;A<>AUX` | `67` |
| `129` | `1` | `410` | `4728` | `SPE=0;M=3;A<>AUX` | `67` |
| `129` | `1` | `410` | `4729` | `SPE=0;M=4;A<>AUX` | `67` |
| `129` | `1` | `410` | `4734` | `SPE=0;M=5;A<>AUX` | `67` |
| `129` | `1` | `410` | `4735` | `SPE=0;M=6;A<>AUX` | `67` |
| `129` | `1` | `410` | `4736` | `SPE=0;M=7;A<>AUX` | `67` |
| `129` | `1` | `410` | `4737` | `SPE=0;M=8;A<>AUX` | `67` |
| `129` | `1` | `410` | `4744` | `SPE=0;M=O/I;A<>AUX` | `67` |
| `129` | `1` | `410` | `4754` | `SPE=0;M=OFF;A<>AUX` | `67` |
| `129` | `1` | `410` | `4757` | `SPE=0;M=ON;A<>AUX` | `67` |
| `129` | `1` | `410` | `4760` | `SPE=0;M=PUL;A<>AUX` | `67` |
| `129` | `1` | `410` | `4834` | `SPE=1;M=7;A<>AUX` | `71` |
| `129` | `1` | `410` | `4838` | `SPE=1;M=8;A<>AUX` | `71` |
| `129` | `1` | `410` | `4843` | `SPE=2;` | `74` |
| `129` | `1` | `410` | `4845` | `SPE=3;` | `75` |
| `129` | `1` | `410` | `4861` | `SPE=7;M<>SU_GIU;M<>SU_GIU_M;A<>AUX` | `87` |
| `129` | `1` | `410` | `4876` | `SPE=8;` | `85` |
| `129` | `1` | `411` | `4765` | `SPE=0;M=SU_GIU;A<>AUX` | `67` |
| `129` | `1` | `411` | `4777` | `SPE=0;M=SU_GIU_M;A<>AUX` | `67` |
| `129` | `1` | `411` | `4868` | `SPE=7;M=SU_GIU;A<>AUX` | `87` |
| `129` | `1` | `411` | `4871` | `SPE=7;M=SU_GIU_M;A<>AUX` | `87` |
| `129` | `1` | `412` | `4799` | `SPE=1;M=1;A<>AUX` | `71` |
| `129` | `1` | `412` | `4807` | `SPE=1;M=2;A<>AUX` | `71` |
| `129` | `1` | `412` | `4815` | `SPE=1;M=3;A<>AUX` | `71` |
| `129` | `1` | `413` | `4847` | `SPE=4` | `76` |
| `129` | `1` | `413` | `4858` | `SPE=6` | `83` |
| `129` | `1` | `414` | `4739` | `SPE=0;M=CEN` | `67` |
| `129` | `1` | `414` | `4867` | `SPE=7;M=CEN;` | `87` |
| `129` | `1` | `415` | `4594` | `M=FAKE` | None |
| `129` | `1` | `416` | `4594` | `M=FAKE` | None |
| `129` | `1` | `419` | `4851` | `SPE=5;M=0;PL2<>0` | `78` |
| `129` | `1` | `419` | `4853` | `SPE=5;M=0;PL2=0` | `79` |
| `129` | `1` | `419` | `4855` | `SPE=5;M=1` | `79` |
| `129` | `2` | `181` | `4594` | `M=FAKE` | None |
| `129` | `2` | `410` | `4711` | `SPE=0;M=0;A<>AUX` | `67` |
| `129` | `2` | `410` | `4718` | `SPE=0;M=1;A<>AUX` | `67` |
| `129` | `2` | `410` | `4723` | `SPE=0;M=2;A<>AUX` | `67` |
| `129` | `2` | `410` | `4728` | `SPE=0;M=3;A<>AUX` | `67` |
| `129` | `2` | `410` | `4729` | `SPE=0;M=4;A<>AUX` | `67` |
| `129` | `2` | `410` | `4734` | `SPE=0;M=5;A<>AUX` | `67` |
| `129` | `2` | `410` | `4735` | `SPE=0;M=6;A<>AUX` | `67` |
| `129` | `2` | `410` | `4736` | `SPE=0;M=7;A<>AUX` | `67` |
| `129` | `2` | `410` | `4737` | `SPE=0;M=8;A<>AUX` | `67` |
| `129` | `2` | `410` | `4745` | `SPE=0;M=O/I;A<>AUX` | `69` |
| `129` | `2` | `410` | `4754` | `SPE=0;M=OFF;A<>AUX` | `67` |
| `129` | `2` | `410` | `4757` | `SPE=0;M=ON;A<>AUX` | `67` |
| `129` | `2` | `410` | `4760` | `SPE=0;M=PUL;A<>AUX` | `67` |
| `129` | `2` | `410` | `4834` | `SPE=1;M=7;A<>AUX` | `71` |
| `129` | `2` | `410` | `4839` | `SPE=1;M=8;A<>AUX` | `72` |
| `129` | `2` | `410` | `4843` | `SPE=2;` | `74` |
| `129` | `2` | `410` | `4845` | `SPE=3;` | `75` |
| `129` | `2` | `410` | `4861` | `SPE=7;M<>SU_GIU;M<>SU_GIU_M;A<>AUX` | `87` |
| `129` | `2` | `410` | `4876` | `SPE=8;` | `85` |
| `129` | `2` | `411` | `4766` | `SPE=0;M=SU_GIU;A<>AUX` | `69` |
| `129` | `2` | `411` | `4778` | `SPE=0;M=SU_GIU_M;A<>AUX` | `69` |
| `129` | `2` | `411` | `4868` | `SPE=7;M=SU_GIU;A<>AUX` | `87` |
| `129` | `2` | `411` | `4871` | `SPE=7;M=SU_GIU_M;A<>AUX` | `87` |
| `129` | `2` | `412` | `4799` | `SPE=1;M=1;A<>AUX` | `71` |
| `129` | `2` | `412` | `4807` | `SPE=1;M=2;A<>AUX` | `71` |
| `129` | `2` | `412` | `4816` | `SPE=1;M=3;A<>AUX` | `72` |
| `129` | `2` | `413` | `4848` | `SPE=4` | `77` |
| `129` | `2` | `413` | `4858` | `SPE=6` | `83` |
| `129` | `2` | `414` | `4740` | `SPE=0;M=CEN` | `69` |
| `129` | `2` | `414` | `4867` | `SPE=7;M=CEN;` | `87` |
| `129` | `2` | `415` | `4594` | `M=FAKE` | None |
| `129` | `2` | `416` | `4594` | `M=FAKE` | None |
| `129` | `2` | `419` | `4852` | `SPE=5;M=0;PL2<>0` | `91` |
| `129` | `2` | `419` | `4854` | `SPE=5;M=0;PL2=0` | `80` |
| `129` | `2` | `419` | `4856` | `SPE=5;M=1` | `82` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `129` | `410` | `1839` | `M` | `135` = Customized `ON` and dimmer without regulation; `136` = Customized `OFF` and dimmer without regulation; `137` = Customized `ON` and dimmer with regulation; `138` = Customized `OFF` and dimmer with regulation | `0` | Modality; reusable default `0` is outside this subset; filter supplies no replacement default |
| `129` | `415` | `851` | `M` | `0` = `ON`; `1` = `OFF`; `2` = `ON` with regulation; `3` = `OFF` with regulation (entire reusable range retained) | `0` | Mode (`ON`/`OFF` regulation) |
| `129` | `415` | `852` | `TYPE_OF_REGULATION` | `0` = Regulate all; `1` = Lights only; `2` = Shutters only; `3` = Stereo amplifiers only (entire reusable range retained) | `0` | REG_TYPE |
| `129` | `419` | `855` | `SUB_SOURCE` | `0..255` (entire reusable range retained) | `0` | SUB_SOURCE |
| `129` | `419` | `856` | `CHANNEL` | `0` = Base Band; `1` = Left; `2` = Right; `3` = Stereo; `8` = Base Band and Video; `9` = Left and video; `10` = Right and video; `11` = Left and video (entire reusable range retained) | `3` | Channel (BB-Stereo) |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `67` | `M=0` | `M` = `0` | `67` |
| `67` | `M=1` | `M` = `1`; `T_TIME ` = `1` | `67` |
| `67` | `M=2` | `M` = `1`; `T_TIME ` = `2` | `67` |
| `67` | `M=3` | `M` = `1`; `T_TIME ` = `3` | `67` |
| `67` | `M=4` | `M` = `1`; `T_TIME ` = `4` | `67` |
| `67` | `M=5` | `M` = `1`; `T_TIME ` = `5` | `67` |
| `67` | `M=6` | `M` = `1`; `T_TIME ` = `6` | `67` |
| `67` | `M=7` | `M` = `1`; `T_TIME ` = `7` | `67` |
| `67` | `M=8` | `M` = `1`; `T_TIME ` = `8` | `67` |
| `67` | `M=O/I` | `M` = `20` | `67` |
| `67` | `M=OFF` | `M` = `10` | `67` |
| `67` | `M=ON` | `M` = `11` | `67` |
| `67` | `M=SU_GIU` | `M` = `0` | `67` |
| `67` | `M=SU_GIU_M` | `M` = `2` | `67` |
| `67` | `M=PUL` | `M` = `15` | `67` |
| `67` | `M=CEN` | `IN_AUX_CHANNEL` = `0`; `CEN_BUTT_1` = `1` | `67` |
| `69` | `M=O/I` | `M` = `21` | `69` |
| `69` | `M=SU_GIU` | `M` = `1` | `69` |
| `69` | `M=SU_GIU_M` | `M` = `3` | `69` |
| `69` | `M=CEN` | `IN_AUX_CHANNEL` = `0`; `CEN_BUTT_1` = `2` | `69` |
| `71` | `M=1` | `M` = `1` | `71` |
| `71` | `M=2` | `M` = `2` | `71` |
| `71` | `M=3` | `M` = `2` | `71` |
| `71` | `M=7` | `M` = `4` | `71` |
| `71` | `M=8` | `M` = `11` | `71` |
| `72` | `M=3` | `M` = `1` | `72` |
| `72` | `M=8` | `M` = `10` | `72` |
| `72` | `PL2=0` | `OUT_AUX_CHANNEL` = `0` | `72` |
| `72` | `PL2=1` | `OUT_AUX_CHANNEL` = `1` | `72` |
| `72` | `PL2=2` | `OUT_AUX_CHANNEL` = `2` | `72` |
| `72` | `PL2=3` | `OUT_AUX_CHANNEL` = `3` | `72` |
| `72` | `PL2=4` | `OUT_AUX_CHANNEL` = `4` | `72` |
| `72` | `PL2=5` | `OUT_AUX_CHANNEL` = `5` | `72` |
| `72` | `PL2=6` | `OUT_AUX_CHANNEL` = `6` | `72` |
| `72` | `PL2=7` | `OUT_AUX_CHANNEL` = `7` | `72` |
| `72` | `PL2=8` | `OUT_AUX_CHANNEL` = `8` | `72` |
| `72` | `PL2=9` | `OUT_AUX_CHANNEL` = `9` | `72` |
| `74` | `M=1` | `M` = `33` | `74` |
| `74` | `M=2` | `M` = `34` | `74` |
| `74` | `M=3` | `M` = `35` | `74` |
| `74` | `M=4` | `M` = `36` | `74` |
| `74` | `M=5` | `M` = `37` | `74` |
| `74` | `M=6` | `M` = `38` | `74` |
| `74` | `M=7` | `M` = `39` | `74` |
| `74` | `M=8` | `M` = `40` | `74` |
| `74` | `M=9` | `M` = `41` | `74` |
| `74` | `M=10` | `M` = `42` | `74` |
| `74` | `M=11` | `M` = `43` | `74` |
| `74` | `M=12` | `M` = `44` | `74` |
| `74` | `M=13` | `M` = `45` | `74` |
| `74` | `M=14` | `M` = `46` | `74` |
| `74` | `M=15` | `M` = `47` | `74` |
| `75` | `M=1` | `M` = `49` | `75` |
| `75` | `M=2` | `M` = `50` | `75` |
| `75` | `M=3` | `M` = `51` | `75` |
| `75` | `M=4` | `M` = `52` | `75` |
| `75` | `M=5` | `M` = `53` | `75` |
| `75` | `M=6` | `M` = `54` | `75` |
| `75` | `M=7` | `M` = `55` | `75` |
| `75` | `M=8` | `M` = `56` | `75` |
| `75` | `M=9` | `M` = `57` | `75` |
| `76` | `M=1` | `M` = `1`; `SCE_BUTT_1` = `1` | `76` |
| `76` | `M=2` | `M` = `1`; `SCE_BUTT_1` = `3` | `76` |
| `76` | `M=3` | `M` = `1`; `SCE_BUTT_1` = `5` | `76` |
| `76` | `M=4` | `M` = `1`; `SCE_BUTT_1` = `7` | `76` |
| `76` | `M=5` | `M` = `1`; `SCE_BUTT_1` = `9` | `76` |
| `76` | `M=6` | `M` = `1`; `SCE_BUTT_1` = `11` | `76` |
| `76` | `M=7` | `M` = `1`; `SCE_BUTT_1` = `13` | `76` |
| `76` | `M=8` | `M` = `1`; `SCE_BUTT_1` = `15` | `76` |
| `77` | `M=1` | `M` = `1`; `SCE_BUTT_1` = `2` | `77` |
| `77` | `M=2` | `M` = `1`; `SCE_BUTT_1` = `4` | `77` |
| `77` | `M=3` | `M` = `1`; `SCE_BUTT_1` = `6` | `77` |
| `77` | `M=4` | `M` = `1`; `SCE_BUTT_1` = `8` | `77` |
| `77` | `M=5` | `M` = `1`; `SCE_BUTT_1` = `10` | `77` |
| `77` | `M=6` | `M` = `1`; `SCE_BUTT_1` = `12` | `77` |
| `77` | `M=7` | `M` = `1`; `SCE_BUTT_1` = `14` | `77` |
| `77` | `M=8` | `M` = `1`; `SCE_BUTT_1` = `16` | `77` |
| `78` | `PL1=0` | `PF` = `0` | `78` |
| `78` | `PL1=1` | `PF` = `1` | `78` |
| `78` | `PL1=2` | `PF` = `2` | `78` |
| `78` | `PL1=3` | `PF` = `3` | `78` |
| `78` | `PL1=4` | `PF` = `4` | `78` |
| `78` | `PL1=5` | `PF` = `5` | `78` |
| `78` | `PL1=6` | `PF` = `6` | `78` |
| `78` | `PL1=7` | `PF` = `7` | `78` |
| `78` | `PL1=8` | `PF` = `8` | `78` |
| `78` | `PL1=9` | `PF` = `9` | `78` |
| `78` | `M=0` | `FOLLOW` = `0` | `78` |
| `79` | `M=0` | `M` = `0`; `FOLLOW` = `0` | `79` |
| `79` | `M=1` | `M` = `3` | `79` |
| `79` | `PL1=0` | `SOURCE` = `0`; `PF` = `0` | `79` |
| `79` | `PL1=1` | `SOURCE` = `1`; `PF` = `1` | `79` |
| `79` | `PL1=2` | `SOURCE` = `2`; `PF` = `2` | `79` |
| `79` | `PL1=3` | `SOURCE` = `3`; `PF` = `3` | `79` |
| `79` | `PL1=4` | `SOURCE` = `4`; `PF` = `4` | `79` |
| `79` | `PL1=5` | `SOURCE` = `5`; `PF` = `5` | `79` |
| `79` | `PL1=6` | `SOURCE` = `6`; `PF` = `6` | `79` |
| `79` | `PL1=7` | `SOURCE` = `7`; `PF` = `7` | `79` |
| `79` | `PL1=8` | `SOURCE` = `8`; `PF` = `8` | `79` |
| `79` | `PL1=9` | `SOURCE` = `9`; `PF` = `9` | `79` |
| `80` | `PL1=4` | `PF` = `4`; `SOURCE` = `4` | `80` |
| `80` | `PL1=5` | `PF` = `5`; `SOURCE` = `5` | `80` |
| `80` | `PL1=6` | `PF` = `6`; `SOURCE` = `6` | `80` |
| `80` | `PL1=7` | `PF` = `7`; `SOURCE` = `7` | `80` |
| `80` | `PL1=8` | `PF` = `8`; `SOURCE` = `8` | `80` |
| `80` | `PL1=9` | `PF` = `9`; `SOURCE` = `9` | `80` |
| `80` | `M=0` | `FOLLOW` = `1`; `M` = `1` | `80` |
| `80` | `M=1` | `M` = `2` | `80` |
| `80` | `PL1=0` | `SOURCE` = `0`; `PF` = `0` | `80` |
| `80` | `PL1=1` | `SOURCE` = `1`; `PF` = `1` | `80` |
| `80` | `PL1=2` | `SOURCE` = `2`; `PF` = `2` | `80` |
| `80` | `PL1=3` | `SOURCE` = `3`; `PF` = `3` | `80` |
| `82` | `M=0` | `FOLLOW` = `1`; `M` = `1` | `82` |
| `82` | `PL1=0` | `SOURCE` = `0` | `82` |
| `82` | `PL1=1` | `SOURCE` = `1` | `82` |
| `82` | `PL1=2` | `SOURCE` = `2` | `82` |
| `82` | `PL1=3` | `SOURCE` = `3` | `82` |
| `82` | `PL1=4` | `SOURCE` = `4` | `82` |
| `82` | `PL1=5` | `SOURCE` = `5` | `82` |
| `82` | `PL1=6` | `SOURCE` = `6` | `82` |
| `82` | `PL1=7` | `SOURCE` = `7` | `82` |
| `82` | `PL1=8` | `SOURCE` = `8` | `82` |
| `82` | `PL1=9` | `SOURCE` = `9` | `82` |
| `82` | `PL2=0` | `PF` = `0` | `82` |
| `82` | `PL2=1` | `PF` = `1` | `82` |
| `82` | `PL2=2` | `PF` = `2` | `82` |
| `82` | `PL2=3` | `PF` = `3` | `82` |
| `82` | `PL2=4` | `PF` = `4` | `82` |
| `82` | `PL2=5` | `PF` = `5` | `82` |
| `82` | `PL2=6` | `PF` = `6` | `82` |
| `82` | `PL2=7` | `PF` = `7` | `82` |
| `82` | `PL2=8` | `PF` = `8` | `82` |
| `82` | `PL2=9` | `PF` = `9` | `82` |
| `82` | `M=1` | `M` = `2` | `82` |
| `83` | `M=1` | `M` = `0`; `SCE_BUTT_1` = `1` | `83` |
| `83` | `M=2` | `M` = `0`; `SCE_BUTT_1` = `3` | `83` |
| `83` | `M=3` | `M` = `0`; `SCE_BUTT_1` = `5` | `83` |
| `83` | `M=4` | `M` = `0`; `SCE_BUTT_1` = `7` | `83` |
| `83` | `M=5` | `M` = `0`; `SCE_BUTT_1` = `9` | `83` |
| `83` | `M=6` | `M` = `0`; `SCE_BUTT_1` = `11` | `83` |
| `83` | `M=7` | `M` = `0`; `SCE_BUTT_1` = `13` | `83` |
| `83` | `M=8` | `M` = `0`; `SCE_BUTT_1` = `15` | `83` |
| `85` | `M=1` | `M` = `1`; `T_TIME ` = `9` | `85` |
| `85` | `M=2` | `M` = `1`; `T_TIME ` = `10` | `85` |
| `87` | `M=0` | `M` = `0`; `CONTACT_TYPE` = `1` | `87` |
| `87` | `M=1` | `M` = `1`; `T_TIME ` = `1`; `CONTACT_TYPE` = `1` | `87` |
| `87` | `M=2` | `M` = `1`; `T_TIME ` = `2`; `CONTACT_TYPE` = `1` | `87` |
| `87` | `M=3` | `M` = `1`; `T_TIME ` = `3`; `CONTACT_TYPE` = `1` | `87` |
| `87` | `M=4` | `M` = `1`; `T_TIME ` = `4`; `CONTACT_TYPE` = `1` | `87` |
| `87` | `M=5` | `M` = `1`; `T_TIME ` = `5`; `CONTACT_TYPE` = `1` | `87` |
| `87` | `M=6` | `M` = `1`; `T_TIME ` = `6`; `CONTACT_TYPE` = `1` | `87` |
| `87` | `M=7` | `M` = `1`; `T_TIME ` = `7`; `CONTACT_TYPE` = `1` | `87` |
| `87` | `M=8` | `M` = `1`; `T_TIME ` = `8`; `CONTACT_TYPE` = `1` | `87` |
| `87` | `M=OFF` | `M` = `10`; `CONTACT_TYPE` = `1` | `87` |
| `87` | `M=ON` | `M` = `11`; `CONTACT_TYPE` = `1` | `87` |
| `87` | `M=PUL` | `M` = `15`; `CONTACT_TYPE` = `1` | `87` |
| `87` | `M=CEN` | `CONTACT_TYPE` = `1`; `IN_AUX_CHANNEL` = `0`; `CEN_BUTT_1` = `2` | `87` |
| `87` | `M=O/I` | `CONTACT_TYPE` = `1`; `M` = `21` | `87` |
| `87` | `M=SU_GIU` | `CONTACT_TYPE` = `1`; `M` = `1` | `87` |
| `87` | `M=SU_GIU_M` | `CONTACT_TYPE` = `1`; `M` = `3` | `87` |
| `91` | `M=0` | `FOLLOW` = `0` | `91` |
| `91` | `PL2=0` | `PF` = `0` | `91` |
| `91` | `PL2=1` | `PF` = `1` | `91` |
| `91` | `PL2=2` | `PF` = `2` | `91` |
| `91` | `PL2=3` | `PF` = `3` | `91` |
| `91` | `PL2=4` | `PF` = `4` | `91` |
| `91` | `PL2=5` | `PF` = `5` | `91` |
| `91` | `PL2=6` | `PF` = `6` | `91` |
| `91` | `PL2=7` | `PF` = `7` | `91` |
| `91` | `PL2=8` | `PF` = `8` | `91` |
| `91` | `PL2=9` | `PF` = `9` | `91` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `81` / `modobj = 152` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`181`, `410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `419`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Lighting and addressing | Physical room `1..9`, PL1/PL2 `0..9`; virtual room `0..10`, point `0..15`, group `1..255`, room/general. Status-return address is virtual-only for broad commands | MQ00272-c-EN, pp. 2–3 |
| Physical timers | `SPE=0` M `1..8`: 1/2/3/4/5/15 min, 30 s, 0.5 s; `SPE=8` M1/2: 2 s/10 min; custom `0..255` h, `0..59` min/s via Suite | MQ00272-c-EN, p. 2 |
| Dimming/blink/lock | Point-to-point long press dimming, `SPE=3` M `1..9` gives `10..90`%; `SPE=2` M `0..9` blinks 0.5..5 s (5.5..8 s virtual); `SPE=1` M1/2 disables/enables | MQ00272-c-EN, pp. 3–5 |
| Shutters and scenes | Equal PL1/PL2 for bistable/monostable shutters. `F420` pairs scenes `1..16` through M `1..8`; `SPE=4` recalls, `SPE=6` learns/recalls. CEN and PLUS scenes have separate procedures | MQ00272-c-EN, pp. 4–6 |
| Audio | Amplifier point/room/general, ON/volume+, OFF/volume−, track/source change, follow-me; source `1..9` and cyclic ON/OFF via Suite | MQ00272-c-EN, pp. 7–8 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Configure physical A/PL1/PL2/M/SPE or MyHOME Suite; Lighting Management uses Plug&Go or Project&Download (p. 1). NO inputs use `SPE=0` and NC `SPE=7`. Respect the per-function address table: shutter pair requires equal PL1/PL2; `F420` PL2 equals PL1 or is absent; CEN equal points activate different scenes, unequal points the same scene (p. 6). `F420` learning requires its unlock LED green, control held 3 s, desired actions and short confirmation; deletion is approximately 10 s in this 2014 sheet (p. 5). PLUS scheduled scene address `1..2047` and button `0..31` are virtual-only; auxiliary and PLUS Lighting Management setup are delegated to Suite (p. 6). The destination-level table mentions I though the device diagram has no I socket, and contains the literal “missing in XLS”; treat it as unresolved publication text, not a new physical socket. Audio p. 7’s source/track PL ordering disagrees with the examples on p. 8, so no hardware-tested precedence is claimed.

## Source reconciliation

The F460/F461 manual PDF p. 7 limits direct association of `3477`/573996 to production batch 10W04 onward.

Catalogue item 81 explicitly establishes `3477`/573996/049238. The retained compatibility table pairs `3477`/573996 (PDF p. 7); no separate `049238` physical sheet is incorporated; its catalogue identity remains established. The exact `3477` technical sheet is printed 07/06/2014 (7 June 2014), correcting the earlier August 2013 date. The Italian export corroborates 27 V, 3.5 mA and dry-contact construction. The historical `L/N/NT4688` guide is not used to override the newer `3477` scene-delete timing.

Catalogue interpretation is detailed under [Object configuration surfaces](#object-configuration-surfaces); these software records do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- No exact separate `049238` technical original or installed capture is retained.
- Audio PL ordering, the undefined physical I entry, empty AUX contact domain, conversion aliases, out-of-domain results and filter `1839` conflicts remain explicit. Suite help and Lighting Management Project&Download instructions, the export’s environmental profile and linked downloads are unexamined.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `3477-ean-product-sheet.pdf`, printed/PDF p. 1: exact `3477` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/f0/95/f095af5e62d424ecaea74869e98ef6007dfa7b4ab9ef96a9b3a0caa95a6f2018.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-3477); SHA-256 `f095af5e62d424ecaea74869e98ef6007dfa7b4ab9ef96a9b3a0caa95a6f2018`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0071-0080-2026-10-06.md#own-dev-0072)
