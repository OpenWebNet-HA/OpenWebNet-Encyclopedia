# Three-module basic control

## Summary

This three-module SCS wall control provides six pushbuttons for three independently configured loads or functions. Status LEDs give local feedback, while configuration determines how each pair of buttons operates its assigned target.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0007` | Project identity |
| Technical description | Three-module, six-button configurable SCS control for three independent loads/functions | Catalogue + official technical sheet |
| Catalogue item | `4` - “Basic control” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `3` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `148` | Implementation evidence |
| Declared Modules | `3` | Implementation evidence |
| Categories | Command, Multifunction, Lighting, Automation, Scenario | Capability model |

This Device exposes three independently addressed command Modules under a shared physical mode selector. The official `MQ00290-c-EN` technical sheet directly covers `067554`, `H4652/3`, `L4652/3`, and `AM5832/3`. The catalogue also maps `573975` and `687378` to the same technical item.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4652/3` | Established identity | Catalogue + official technical sheet |
| BTicino - LivingLight | `L4652/3` | Established identity | Catalogue + official technical sheet |
| BTicino - Matix | `AM5832/3` | Established identity | Catalogue + official technical sheet |
| Legrand - Céliane | `067554` | Established catalogue identity | Catalogue + official technical sheet |
| Legrand - Arteor | `573975` | Shared technical-item identity | Canonical catalogue; retained exact-product sheet absent |
| Legrand - Vela | `687378` | Shared technical-item identity | Canonical catalogue; retained exact-product sheet absent |

The retained canonical catalogue assigns `067554` to Céliane. An attempted current manufacturer export was inaccessible during review, so no new marketed-line assignment is incorporated.

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `H4652/3` | `8012199745367` | [Archived original](https://archive.openwebnet-ha.org/sha256/63/e5/63e5b4eb1e7aaf083e4c5949b4aed30ca2d067944554caa6014d0e98fd0843a2.pdf), `H4652_3-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `L4652/3` | `8012199365619` | [Archived original](https://archive.openwebnet-ha.org/sha256/2f/07/2f0714e82b199b9d75fcb29f08d7b64ddf15a612c97f9af7f160e82c87df4fd6.pdf), `L4652_3-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `AM5832/3` | `8012199838342` | [Archived original](https://archive.openwebnet-ha.org/sha256/1c/ec/1cecf514a4b6bbae5c315d16bb1dd0f74f5203899e30cb418d22bbaf10c91e53.pdf), `AM5832_3-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00290-c-EN` | Technical sheet | 01/08/2013 | `067554`, `H4652/3`, `L4652/3`, `AM5832/3` | [Archived PDF](https://archive.openwebnet-ha.org/sha256/21/3c/213cc3f253156d5ef9c7311ff6a1a5f9ae6c48405991341ded7f7b3a94517a85.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00290_c_EN.pdf) |
| `MQ00290-c-FR` | Technical sheet | 05/05/2014 | same family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/48/79/48794f03e6d3bc4b5e200f3ebf49de93f7d85f4c29714869914e11752b8cff2e.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00290-c-FR.pdf) |
| `T9807J` | Instruction sheet | Printed revision; date not established | L4652/3 family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/3e/59/3e59e4fbc2a4cbfb4f70b85750d2d970f750e8ac81c79af99f91c332c7512cc5.pdf) | [Official source](https://dar.bticino.com/asset/Documents/T9807J.pdf) |
| `LE05420AA` | Instruction sheet | Printed `10/12-01 PC` | `067554` | [Archived PDF](https://archive.openwebnet-ha.org/sha256/c5/f9/c5f96fb6a845ad7c7b2ffc5b41c232c446ed6e1d306585e133ca56f263fdaf17.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE05420AA.pdf) |
| `H4652_3-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `H4652/3` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/63/e5/63e5b4eb1e7aaf083e4c5949b4aed30ca2d067944554caa6014d0e98fd0843a2.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4652_3) |
| `L4652_3-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `L4652/3` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/2f/07/2f0714e82b199b9d75fcb29f08d7b64ddf15a612c97f9af7f160e82c87df4fd6.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4652_3) |
| `AM5832_3-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `AM5832/3` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/1c/ec/1cecf514a4b6bbae5c315d16bb1dd0f74f5203899e30cb418d22bbaf10c91e53.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5832_3) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Width | 3 flush-mounted modules | Publisher documentation cited in this section |
| Front controls | 6 pushbuttons with status LEDs | Publisher documentation cited in this section |
| SCS nominal supply | `27 Vdc` | Publisher documentation cited in this section |
| SCS operating supply | `18..27 Vdc` | Publisher documentation cited in this section |
| Current draw | `9 mA` | Publisher documentation cited in this section |
| Physical configurator positions | `A1`, `PL1`, `A2`, `PL2`, `A3`, `PL3`, `M` | Publisher documentation cited in this section |

The seven printed configurator positions independently support the expected ordinary addressed-form configurator count. An observed `DIMENSION 1` read is still required before recording `N_CONF = 7` as hardware-corroborated.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `4` | Canonical catalogue |
| Item model / `modobj` | `3` | Canonical catalogue / retained definition |
| Main system | Lighting / Automation | Canonical catalogue / retained definition |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `3` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These are software applicability associations, not an inventory of physical ports or proof of every functional service.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `148` | `-1` | `-1` | `-1` | `3` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

### Parameter and package associations

No firmware parameter-file associations are stored for this item in the canonical snapshot.

No `AS_FW_PACKAGE` association is stored for these firmware definitions. This is a catalogue coverage statement, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `148` | `1` | `400` Light control | Fixed/designated metadata | `638` | `400` | `444` |
| `148` | `1` | `401` Automation control | Candidate alternative | `551` | `401` | `377` |
| `148` | `1` | `404` Scheduled scenario | Candidate alternative | `554` | `404` | `378` |
| `148` | `1` | `406` Scheduled scenario PLUS | Candidate alternative | `557` | `406` | `379` |
| `148` | `2` | `400` Light control | Fixed/designated metadata | `639` | `400` | `444` |
| `148` | `2` | `401` Automation control | Candidate alternative | `552` | `401` | `377` |
| `148` | `2` | `404` Scheduled scenario | Candidate alternative | `555` | `404` | `378` |
| `148` | `2` | `406` Scheduled scenario PLUS | Candidate alternative | `558` | `406` | `379` |
| `148` | `3` | `400` Light control | Fixed/designated metadata | `640` | `400` | `444` |
| `148` | `3` | `401` Automation control | Candidate alternative | `553` | `401` | `377` |
| `148` | `3` | `404` Scheduled scenario | Candidate alternative | `556` | `404` | `378` |
| `148` | `3` | `406` Scheduled scenario PLUS | Candidate alternative | `559` | `406` | `379` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `148` | `500` Automation double command virgin | `1`, `2`, `3` | `400`, `401`, `404`, `406`, `407` | `500` | `21` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Applicability |
| --- | --- | --- | --- |
| `148` | Physical configuration | `0` | Canonical catalogue association; not proof of installed state |
| `148` | Virtual Configuration | `1` | Canonical catalogue association; not proof of installed state |
| `148` | Advanced Configuration | `2` | Canonical catalogue association; not proof of installed state |

Product physical and software setup are distinct from the catalogue mode labels. A declared mode does not prove every reusable Object or programming operation is available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `148` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `148` | `A1` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB`; `15` = `AUX` | `0` | A1; Automation A addressing space (for configurator A1) |
| `148` | `PL1` | `0..9` | `0` | PL1; PL1 - (0-9) |
| `148` | `A2` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB`; `15` = `AUX` | `0` | A2; Automation A addressing space (for configurator A2) |
| `148` | `PL2` | `0..9` | `0` | PL2; PL2 - (0-9) |
| `148` | `A3` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB`; `15` = `AUX` | `0` | A3; Automation A addressing space (for configurator A3) |
| `148` | `PL3` | `0..9` | `0` | PL3; PL3 - (0-9) |
| `148` | `M` | `0..9`; `14` = `CEN` | `0` | M; Mode (0-9,`CEN`) |

### Published and reconciled details

| Field | Catalogue domain | Role |
| --- | --- | --- |
| `AID` | Device identity field | not a physical configurator |
| `A1`, `A2`, `A3` | `0..9`, `GEN`, `GR`, `AMB`, `AUX` | address scope for each Module |
| `PL1`, `PL2`, `PL3` | `0..9` | point/function value for each Module |
| `M` | `0..9`, `CEN` | shared function selector |

The published sheet documents virtual point-to-point room `0..10`, light point `0..15`, group `1..255`, room, group, and general command forms. The physical form uses the three A/PL pairs and the shared `M` position.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

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

### Virgin-only candidate Objects

The following reusable surfaces occur only through permitted Virgin Object membership; no direct association proves that they become active on this Device.

### Object `407` - AUX control (Virgin-only candidate)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `9` = ON/OFF and point to point dimming; `10` = OFF; `11` = ON; `15` = PUL; `12` = Bistable control; `13` = Monostable control; `4` = Reset BI; `5` = Reset TRI; `6` = Reset GEN; `1` = Disable (lower button); `2` = Enable (lower button); `3` = Disable (upper button) - enable (lower button) | `0` | Modality |
| `OUT_AUX_CH` | `1..15` | `1` | AUX channel |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input AUX channel |

### Applicability interpretation

Three addressed Modules share a physical mode selector. Reusable Object membership does not permit independent physical `M` values for each pair of buttons.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `148` | `1` | `400` | `4464` | `M=1;A1<>AMB;A1<>GR;A1<>GEN` | `31` |
| `148` | `1` | `400` | `4465` | `M=1;A1=AMB` | `31` |
| `148` | `1` | `400` | `4466` | `M=1;A1=GEN` | `31` |
| `148` | `1` | `400` | `4467` | `M=1;A1=GR` | `31` |
| `148` | `1` | `400` | `4479` | `M=2;A1<>AMB;A1<>GR;A1<>GEN` | `31` |
| `148` | `1` | `400` | `4480` | `M=2;A1=AMB` | `31` |
| `148` | `1` | `400` | `4481` | `M=2;A1=GEN` | `31` |
| `148` | `1` | `400` | `4482` | `M=2;A1=GR` | `31` |
| `148` | `1` | `400` | `4507` | `M=4;A1<>AMB;A1<>GR;A1<>GEN` | `31` |
| `148` | `1` | `400` | `4508` | `M=4;A1=AMB` | `31` |
| `148` | `1` | `400` | `4509` | `M=4;A1=GEN` | `31` |
| `148` | `1` | `400` | `4510` | `M=4;A1=GR` | `31` |
| `148` | `1` | `400` | `4521` | `M=5;A1<>AMB;A1<>GR;A1<>GEN` | `31` |
| `148` | `1` | `400` | `4522` | `M=5;A1=AMB` | `31` |
| `148` | `1` | `400` | `4523` | `M=5;A1=GEN` | `31` |
| `148` | `1` | `400` | `4524` | `M=5;A1=GR` | `31` |
| `148` | `1` | `400` | `4547` | `M=7;A1<>AMB;A1<>GR;A1<>GEN` | `31` |
| `148` | `1` | `400` | `4548` | `M=7;A1=AMB` | `31` |
| `148` | `1` | `400` | `4549` | `M=7;A1=GEN` | `31` |
| `148` | `1` | `400` | `4550` | `M=7;A1=GR` | `31` |
| `148` | `1` | `400` | `4560` | `M=8;A1<>AMB;A1<>GR;A1<>GEN` | `31` |
| `148` | `1` | `400` | `4561` | `M=8;A1=AMB` | `31` |
| `148` | `1` | `400` | `4562` | `M=8;A1=GEN` | `31` |
| `148` | `1` | `400` | `4563` | `M=8;A1=GR` | `31` |
| `148` | `1` | `400` | `4572` | `M=9;A1<>AMB;A1<>GR;A1<>GEN` | `31` |
| `148` | `1` | `400` | `4573` | `M=9;A1=AMB` | `31` |
| `148` | `1` | `400` | `4574` | `M=9;A1=GEN` | `31` |
| `148` | `1` | `400` | `4575` | `M=9;A1=GR` | `31` |
| `148` | `1` | `401` | `4493` | `M=3;A1<>AMB;A1<>GR;A1<>GEN` | `31` |
| `148` | `1` | `401` | `4494` | `M=3;A1=AMB` | `31` |
| `148` | `1` | `401` | `4495` | `M=3;A1=GEN` | `31` |
| `148` | `1` | `401` | `4496` | `M=3;A1=GR` | `31` |
| `148` | `1` | `401` | `4534` | `M=6;A1<>AMB;A1<>GR;A1<>GEN` | `31` |
| `148` | `1` | `401` | `4535` | `M=6;A1=AMB` | `31` |
| `148` | `1` | `401` | `4536` | `M=6;A1=GEN` | `31` |
| `148` | `1` | `401` | `4537` | `M=6;A1=GR` | `31` |
| `148` | `1` | `404` | `4587` | `M=CEN` | `31` |
| `148` | `1` | `406` | `4594` | `M=FAKE` | None |
| `148` | `2` | `400` | `4468` | `M=1;A2<>AMB;A2<>GR;A2<>GEN` | `32` |
| `148` | `2` | `400` | `4469` | `M=1;A2=AMB` | `32` |
| `148` | `2` | `400` | `4470` | `M=1;A2=GEN` | `32` |
| `148` | `2` | `400` | `4471` | `M=1;A2=GR` | `32` |
| `148` | `2` | `400` | `4511` | `M=4;A2<>AMB;A2<>GR;A2<>GEN` | `32` |
| `148` | `2` | `400` | `4512` | `M=4;A2=AMB` | `32` |
| `148` | `2` | `400` | `4513` | `M=4;A2=GEN` | `32` |
| `148` | `2` | `400` | `4514` | `M=4;A2=GR` | `32` |
| `148` | `2` | `400` | `4551` | `M=7;A2<>AMB;A2<>GR;A2<>GEN` | `32` |
| `148` | `2` | `400` | `4552` | `M=7;A2=AMB` | `32` |
| `148` | `2` | `400` | `4553` | `M=7;A2=GEN` | `32` |
| `148` | `2` | `400` | `4554` | `M=7;A2=GR` | `32` |
| `148` | `2` | `400` | `4564` | `M=8;A2<>AMB;A2<>GR;A2<>GEN` | `32` |
| `148` | `2` | `400` | `4565` | `M=8;A2=AMB` | `32` |
| `148` | `2` | `400` | `4566` | `M=8;A2=GEN` | `32` |
| `148` | `2` | `400` | `4567` | `M=8;A2=GR` | `32` |
| `148` | `2` | `400` | `4576` | `M=9;A2<>AMB;A2<>GR;A2<>GEN` | `32` |
| `148` | `2` | `400` | `4577` | `M=9;A2=AMB` | `32` |
| `148` | `2` | `400` | `4578` | `M=9;A2=GEN` | `32` |
| `148` | `2` | `400` | `4579` | `M=9;A2=GR` | `32` |
| `148` | `2` | `401` | `4483` | `M=2;A2<>AMB;A2<>GR;A2<>GEN` | `32` |
| `148` | `2` | `401` | `4484` | `M=2;A2=AMB` | `32` |
| `148` | `2` | `401` | `4485` | `M=2;A2=GEN` | `32` |
| `148` | `2` | `401` | `4486` | `M=2;A2=GR` | `32` |
| `148` | `2` | `401` | `4497` | `M=3;A2<>AMB;A2<>GR;A2<>GEN` | `32` |
| `148` | `2` | `401` | `4498` | `M=3;A2=AMB` | `32` |
| `148` | `2` | `401` | `4499` | `M=3;A2=GEN` | `32` |
| `148` | `2` | `401` | `4500` | `M=3;A2=GR` | `32` |
| `148` | `2` | `401` | `4525` | `M=5;A2<>AMB;A2<>GR;A2<>GEN` | `32` |
| `148` | `2` | `401` | `4526` | `M=5;A2=AMB` | `32` |
| `148` | `2` | `401` | `4527` | `M=5;A2=GEN` | `32` |
| `148` | `2` | `401` | `4528` | `M=5;A2=GR` | `32` |
| `148` | `2` | `401` | `4538` | `M=6;A2<>AMB;A2<>GR;A2<>GEN` | `32` |
| `148` | `2` | `401` | `4539` | `M=6;A2=AMB` | `32` |
| `148` | `2` | `401` | `4540` | `M=6;A2=GEN` | `32` |
| `148` | `2` | `401` | `4541` | `M=6;A2=GR` | `32` |
| `148` | `2` | `404` | `4588` | `M=CEN` | `32` |
| `148` | `2` | `406` | `4594` | `M=FAKE` | None |
| `148` | `3` | `400` | `4555` | `M=7;A3<>AMB;A3<>GR;A3<>GEN` | `33` |
| `148` | `3` | `400` | `4556` | `M=7;A3=AMB` | `33` |
| `148` | `3` | `400` | `4557` | `M=7;A3=GEN` | `33` |
| `148` | `3` | `400` | `4558` | `M=7;A3=GR` | `33` |
| `148` | `3` | `400` | `4568` | `M=8;A3<>AMB;A3<>GR;A3<>GEN` | `33` |
| `148` | `3` | `400` | `4569` | `M=8;A3=AMB` | `33` |
| `148` | `3` | `400` | `4570` | `M=8;A3=GEN` | `33` |
| `148` | `3` | `400` | `4571` | `M=8;A3=GR` | `33` |
| `148` | `3` | `400` | `4580` | `M=9;A3<>AMB;A3<>GR;A3<>GEN` | `33` |
| `148` | `3` | `400` | `4581` | `M=9;A3=AMB` | `33` |
| `148` | `3` | `400` | `4582` | `M=9;A3=GEN` | `33` |
| `148` | `3` | `400` | `4583` | `M=9;A3=GR` | `33` |
| `148` | `3` | `401` | `4472` | `M=1;A3<>AMB;A3<>GR;A3<>GEN` | `33` |
| `148` | `3` | `401` | `4473` | `M=1;A3=AMB` | `33` |
| `148` | `3` | `401` | `4474` | `M=1;A3=GEN` | `33` |
| `148` | `3` | `401` | `4475` | `M=1;A3=GR` | `33` |
| `148` | `3` | `401` | `4487` | `M=2;A3<>AMB;A3<>GR;A3<>GEN` | `33` |
| `148` | `3` | `401` | `4488` | `M=2;A3=AMB` | `33` |
| `148` | `3` | `401` | `4489` | `M=2;A3=GEN` | `33` |
| `148` | `3` | `401` | `4490` | `M=2;A3=GR` | `33` |
| `148` | `3` | `401` | `4501` | `M=3;A3<>AMB;A3<>GR;A3<>GEN` | `33` |
| `148` | `3` | `401` | `4502` | `M=3;A3=AMB` | `33` |
| `148` | `3` | `401` | `4503` | `M=3;A3=GEN` | `33` |
| `148` | `3` | `401` | `4504` | `M=3;A3=GR` | `33` |
| `148` | `3` | `401` | `4515` | `M=4;A3<>AMB;A3<>GR;A3<>GEN` | `33` |
| `148` | `3` | `401` | `4516` | `M=4;A3=AMB` | `33` |
| `148` | `3` | `401` | `4517` | `M=4;A3=GEN` | `33` |
| `148` | `3` | `401` | `4518` | `M=4;A3=GR` | `33` |
| `148` | `3` | `401` | `4529` | `M=5;A3<>AMB;A3<>GR;A3<>GEN` | `33` |
| `148` | `3` | `401` | `4530` | `M=5;A3=AMB` | `33` |
| `148` | `3` | `401` | `4531` | `M=5;A3=GEN` | `33` |
| `148` | `3` | `401` | `4532` | `M=5;A3=GR` | `33` |
| `148` | `3` | `401` | `4542` | `M=6;A3<>AMB;A3<>GR;A3<>GEN` | `33` |
| `148` | `3` | `401` | `4543` | `M=6;A3=AMB` | `33` |
| `148` | `3` | `401` | `4544` | `M=6;A3=GEN` | `33` |
| `148` | `3` | `401` | `4545` | `M=6;A3=GR` | `33` |
| `148` | `3` | `404` | `4589` | `M=CEN` | `33` |
| `148` | `3` | `406` | `4594` | `M=FAKE` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `148` | `400` | `562` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `148` | `400` | `563` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `148` | `400` | `564` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `148` | `400` | `565` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `148` | `400` | `566` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `148` | `400` | `567` | `LEVEL` | `0..100` (entire reusable range retained) | `100` | Level |
| `148` | `400` | `568` | `START_S` | `0..255` (entire reusable range retained) | `255` | Soft start speed |
| `148` | `400` | `569` | `STOP_S` | `0..255` (entire reusable range retained) | `255` | Soft stop speed |
| `148` | `400` | `570` | `DIMMING_S` | `0..255` (entire reusable range retained) | `255` | Dimming speed |
| `148` | `400` | `571` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `148` | `400` | `572` | `M` | `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `130` = Customized `ON`/`OFF` and point to point dimmer; `131` = Customized toggle dimmer; `132` = Customized `ON`/`OFF` and dimmer; `133` = Customized toggle dimmer without regulation; `134` = Customized `ON`/`OFF` and dimmer without regulation; `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `4` = Toggle `ON`/`OFF`; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `5` = `ON`/`OFF`; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90% | `0` | Mode; reusable default `0` is outside this subset; filter supplies no replacement default |
| `148` | `401` | `298` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `148` | `401` | `299` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `148` | `401` | `300` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `148` | `401` | `301` | `M` | `14` = Blades control and bistable | `12` | Modality; reusable default `12` is outside this subset; filter supplies no replacement default |
| `148` | `404` | `304` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `148` | `404` | `1702` | `START_DELAY` | `0..255` (entire reusable range retained) | `10` | Start delay |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `31` | `M=0` | `M` = `0` | `31` |
| `31` | `M=1` | `M` = `0` | `31` |
| `31` | `M=2` | `M` = `0` | `31` |
| `31` | `M=3` | `M` = `12` | `31` |
| `31` | `M=4` | `M` = `0` | `31` |
| `31` | `M=5` | `M` = `0` | `31` |
| `31` | `M=6` | `M` = `13` | `31` |
| `31` | `M=7` | `M` = `0` | `31` |
| `31` | `M=8` | `M` = `0` | `31` |
| `31` | `M=9` | `M` = `9` | `31` |
| `31` | `M=CEN` | `CEN_BUTT_1 ` = `2`; `CEN_BUTT_2 ` = `5` | `31` |
| `31` | `A1=AMB` | `ADDR_TYPE` = `1` | `31` |
| `31` | `A1=GR` | `ADDR_TYPE` = `2` | `31` |
| `31` | `A1=GEN` | `ADDR_TYPE` = `3` | `31` |
| `31` | `A1=AMB; PL1=1` | `A` = `1` | `31` → `201` |
| `31` | `A1=AMB; PL1=2` | `A` = `2` | `31` → `201` |
| `31` | `A1=AMB; PL1=3` | `A` = `3` | `31` → `201` |
| `31` | `A1=AMB; PL1=4` | `A` = `4` | `31` → `201` |
| `31` | `A1=AMB; PL1=5` | `A` = `5` | `31` → `201` |
| `31` | `A1=AMB; PL1=6` | `A` = `6` | `31` → `201` |
| `31` | `A1=AMB; PL1=7` | `A` = `7` | `31` → `201` |
| `31` | `A1=AMB; PL1=8` | `A` = `8` | `31` → `201` |
| `31` | `A1=AMB; PL1=9` | `A` = `9` | `31` → `201` |
| `31` | `A1=GR; PL1=1` | `G1` = `1` | `31` → `200` |
| `31` | `A1=GR; PL1=2` | `G1` = `2` | `31` → `200` |
| `31` | `A1=GR; PL1=3` | `G1` = `3` | `31` → `200` |
| `31` | `A1=GR; PL1=4` | `G1` = `4` | `31` → `200` |
| `31` | `A1=GR; PL1=5` | `G1` = `5` | `31` → `200` |
| `31` | `A1=GR; PL1=6` | `G1` = `6` | `31` → `200` |
| `31` | `A1=GR; PL1=7` | `G1` = `7` | `31` → `200` |
| `31` | `A1=GR; PL1=8` | `G1` = `8` | `31` → `200` |
| `31` | `A1=GR; PL1=9` | `G1` = `9` | `31` → `200` |
| `32` | `M=0` | `M` = `0` | `32` |
| `32` | `M=1` | `M` = `0` | `32` |
| `32` | `M=2` | `M` = `12` | `32` |
| `32` | `M=3` | `M` = `12` | `32` |
| `32` | `M=4` | `M` = `0` | `32` |
| `32` | `M=5` | `M` = `13` | `32` |
| `32` | `M=6` | `M` = `13` | `32` |
| `32` | `M=7` | `M` = `0` | `32` |
| `32` | `M=8` | `M` = `9` | `32` |
| `32` | `M=9` | `M` = `9` | `32` |
| `32` | `M=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `5` | `32` |
| `32` | `A2=AMB` | `ADDR_TYPE` = `1` | `32` |
| `32` | `A2=GR` | `ADDR_TYPE` = `2` | `32` |
| `32` | `A2=GEN` | `ADDR_TYPE` = `3` | `32` |
| `32` | `A2=AMB; PL2=1` | `A` = `1` | `32` → `203` |
| `32` | `A2=AMB; PL2=2` | `A` = `2` | `32` → `203` |
| `32` | `A2=AMB; PL2=3` | `A` = `3` | `32` → `203` |
| `32` | `A2=AMB; PL2=4` | `A` = `4` | `32` → `203` |
| `32` | `A2=AMB; PL2=5` | `A` = `5` | `32` → `203` |
| `32` | `A2=AMB; PL2=6` | `A` = `6` | `32` → `203` |
| `32` | `A2=AMB; PL2=7` | `A` = `7` | `32` → `203` |
| `32` | `A2=AMB; PL2=8` | `A` = `8` | `32` → `203` |
| `32` | `A2=AMB; PL2=9` | `A` = `9` | `32` → `203` |
| `32` | `A2=GR; PL2=1` | `G1` = `1` | `32` → `202` |
| `32` | `A2=GR; PL2=2` | `G1` = `2` | `32` → `202` |
| `32` | `A2=GR; PL2=3` | `G1` = `3` | `32` → `202` |
| `32` | `A2=GR; PL2=4` | `G1` = `4` | `32` → `202` |
| `32` | `A2=GR; PL2=5` | `G1` = `5` | `32` → `202` |
| `32` | `A2=GR; PL2=6` | `G1` = `6` | `32` → `202` |
| `32` | `A2=GR; PL2=7` | `G1` = `7` | `32` → `202` |
| `32` | `A2=GR; PL2=8` | `G1` = `8` | `32` → `202` |
| `32` | `A2=GR; PL2=9` | `G1` = `9` | `32` → `202` |
| `33` | `M=0` | `M` = `0` | `33` |
| `33` | `M=1` | `M` = `12` | `33` |
| `33` | `M=2` | `M` = `12` | `33` |
| `33` | `M=3` | `M` = `12` | `33` |
| `33` | `M=4` | `M` = `13` | `33` |
| `33` | `M=5` | `M` = `13` | `33` |
| `33` | `M=6` | `M` = `13` | `33` |
| `33` | `M=7` | `M` = `9` | `33` |
| `33` | `M=8` | `M` = `9` | `33` |
| `33` | `M=9` | `M` = `9` | `33` |
| `33` | `M=CEN` | `CEN_BUTT_1 ` = `3`; `CEN_BUTT_2 ` = `6` | `33` |
| `33` | `A3=AMB` | `ADDR_TYPE` = `1` | `33` |
| `33` | `A3=GR` | `ADDR_TYPE` = `2` | `33` |
| `33` | `A3=GEN` | `ADDR_TYPE` = `3` | `33` |
| `33` | `A3=AMB; PL3=1` | `A` = `1` | `33` → `205` |
| `33` | `A3=AMB; PL3=2` | `A` = `2` | `33` → `205` |
| `33` | `A3=AMB; PL3=3` | `A` = `3` | `33` → `205` |
| `33` | `A3=AMB; PL3=4` | `A` = `4` | `33` → `205` |
| `33` | `A3=AMB; PL3=5` | `A` = `5` | `33` → `205` |
| `33` | `A3=AMB; PL3=6` | `A` = `6` | `33` → `205` |
| `33` | `A3=AMB; PL3=7` | `A` = `7` | `33` → `205` |
| `33` | `A3=AMB; PL3=8` | `A` = `8` | `33` → `205` |
| `33` | `A3=AMB; PL3=9` | `A` = `9` | `33` → `205` |
| `33` | `A3=GR; PL3=1` | `G1` = `1` | `33` → `204` |
| `33` | `A3=GR; PL3=2` | `G1` = `2` | `33` → `204` |
| `33` | `A3=GR; PL3=3` | `G1` = `3` | `33` → `204` |
| `33` | `A3=GR; PL3=4` | `G1` = `4` | `33` → `204` |
| `33` | `A3=GR; PL3=5` | `G1` = `5` | `33` → `204` |
| `33` | `A3=GR; PL3=6` | `G1` = `6` | `33` → `204` |
| `33` | `A3=GR; PL3=7` | `G1` = `7` | `33` → `204` |
| `33` | `A3=GR; PL3=8` | `G1` = `8` | `33` → `204` |
| `33` | `A3=GR; PL3=9` | `G1` = `9` | `33` → `204` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

The stored PLUS condition `M=FAKE` uses a symbol absent from firmware `148`'s enum. The product sheet documents software PLUS activation, but does not resolve the internal `FAKE` selector or its execution precedence.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 3`, brand, line, and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | obtain actual installed firmware despite wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | determine active Object for each of the three command Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine the three Module addresses | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values | [Configuration](../../diagnostics/dim35-configuration.md) |
## Functional applicability

| Function / configuration | Documented use | Evidence |
| --- | --- | --- |
| Lighting | Three A/PL pairs; cyclic ON/OFF and cover-dependent ON/OFF/adjustment, with software reference address for group/room status | `MQ00290-c-EN`, pp. 2, 4; FR pp. 2, 4 |
| Automation | Cover-dependent bistable or monostable shutter commands under a shared `M` | Same EN/FR sheets, pp. 2–4 |
| MH200N CEN | Six scenario buttons; physical `M=CEN` uses the first A/PL pair and leaves `A2/PL2/A3/PL3` unconfigured | Same sheets, pp. 3–4 |
| PLUS scenarios | Software scenario address `1..2047`; button `0..31` | Same sheets, p. 3 |

Three independent catalogue command Modules do not imply three independently selectable physical mode values.

## Observed behavior and corroboration

No additional publishable runtime observation is asserted beyond observations explicitly retained elsewhere on this page.

## Programming

For ordinary addressed controls, the left, middle and right button pairs correspond to `A1/PL1`, `A2/PL2` and `A3/PL3`. `M` is shared and its physical effect depends on the fitted button covers. The published table mixes lighting and shutter functions for some covers; resolve the exact cover/function combination instead of assigning three unrelated `M` values.

Physical CEN is different: configure only the first address pair and leave `A2/PL2/A3/PL3` empty. Software uses button identifiers `0..31` and, for PLUS scenarios, scenario address `1..2047`. Physical A/PL values `1..9` and software room `0..10` / point `0..15` remain separate from the catalogue's underlying `0..9` fields. Check the active Object projection before writing; generic sequencing stays in [Programming Validation](../../programming/validation.md).

## Source reconciliation

The archived `MQ00290` and installation sheets add Device-specific behavior to the three independent command Modules:

- the shared physical `M` selector changes the function family of all three A/PL pairs and therefore cannot be interpreted independently per Module;
- physical and virtual configuration cover point-to-point, room, group and general lighting scopes, programmed scenarios, `CEN`/`CEN` PLUS behavior and automation control;
- software configuration can associate return-of-load status with a reference actuator address for non-point-to-point commands;
- `CEN`-only use has product-level constraints on address positions that are not used by the `CEN` function;
- the published PLUS scenario representation uses the wider software scenario domain rather than only the physical selector values;
- LED/mechanical behavior remains a commercial/package concern and should not be inferred solely from the shared item.

The current source set is reconciled for the core product family; direct documentation for `573975` and `687378` remains outstanding.

The English sheet is dated 1 August 2013; the French revision is dated 5 May 2014. Their addressing, CEN constraints and function/cover tables agree on the reviewed facts. `T9807J` is a multi-product button-assembly instruction including `L4652/3`; `LE05420AA` (`10/12-01 PC`) is an assembly sheet. Neither supplies additional firmware or load ratings. The inaccessible current manufacturer export remains a discovery lead; an earlier unretained Arteor wording report is not used to establish a competing marketed-line identity.

## Evidence limits and open work

- Locate product-specific documentation for `573975` and `687378`.
- Retrieve a retained current manufacturer record for `067554` before adjudicating any reported marketed-line wording difference.
- Add a sanitized hardware fingerprint to corroborate `modobj`, firmware, expected configurator count, Module Objects, addresses, and configuration.
- Verify whether all package/finish variants expose identical LED and mechanical behavior.
- Continue archival discovery for older technical-sheet revisions and language variants.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
- [Programming](../../programming/)

- `H4652_3-ean-product-sheet.pdf`, printed/PDF p. 1: exact `H4652/3` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/63/e5/63e5b4eb1e7aaf083e4c5949b4aed30ca2d067944554caa6014d0e98fd0843a2.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4652_3); SHA-256 `63e5b4eb1e7aaf083e4c5949b4aed30ca2d067944554caa6014d0e98fd0843a2`.
- `L4652_3-ean-product-sheet.pdf`, printed/PDF p. 1: exact `L4652/3` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/2f/07/2f0714e82b199b9d75fcb29f08d7b64ddf15a612c97f9af7f160e82c87df4fd6.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4652_3); SHA-256 `2f0714e82b199b9d75fcb29f08d7b64ddf15a612c97f9af7f160e82c87df4fd6`.
- `AM5832_3-ean-product-sheet.pdf`, printed/PDF p. 1: exact `AM5832/3` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/1c/ec/1cecf514a4b6bbae5c315d16bb1dd0f74f5203899e30cb418d22bbaf10c91e53.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5832_3); SHA-256 `1cecf514a4b6bbae5c315d16bb1dd0f74f5203899e30cb418d22bbaf10c91e53`.

- [Semantic review record, 5 October 2026](../../project/review/device-reviews-0001-0010-2026-10-05.md#own-dev-0007)
