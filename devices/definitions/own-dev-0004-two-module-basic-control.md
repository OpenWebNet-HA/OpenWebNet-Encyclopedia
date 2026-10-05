# Two-module basic control

## Summary

This two-module wall control uses four buttons to operate configured lights, dimmers, shutters or scenarios over the SCS bus. Its two-colour indicators provide feedback, with locally adjustable LED brightness.


| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0004` | Project identity |
| Technical description | Two-module, two-channel configurable SCS control | Catalogue + official technical sheet |
| Catalogue item | `281` - “Basic control” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `2` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `145` | Implementation evidence |
| Declared Modules | `2` | Implementation evidence |
| Categories | Command, Multifunction, Lighting, Automation, Scenario | Capability model |

This technical definition covers the shared catalogue capability core used by 19 commercial Device records. The official `MQ00286-d-EN` technical sheet directly covers four of those references - `067552`, `H4652/2`, `L4652/2`, and `AM5832/2`. The remaining catalogue records are retained as commercial identities associated with item `281`, but their packaging, range, and exact commercial equivalence still require product-document review.

## Commercial identities


### Directly documented references

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4652/2` | Established identity | Catalogue + `MQ00286-d-EN` |
| BTicino - LivingLight | `L4652/2` | Established identity | Catalogue + `MQ00286-d-EN` |
| BTicino - Matix | `AM5832/2` | Established identity | Catalogue + `MQ00286-d-EN` |
| Legrand - Céliane | `067552` | Established identity | Catalogue + `MQ00286-d-EN` |

### Additional commercial records sharing item 281

| Brand / line | References | Status |
| --- | --- | --- |
| Arnould Espace Evolution | `64160`, `64161`, `64360` | Shared technical item; individual product-document review pending |
| Legrand Arteor | `571848`, `573974` | Shared technical item; individual product-document review pending |
| Legrand Matix | `078473` | Shared technical item; individual product-document review pending |
| Legrand Mosaic | `078462`, `078463`, `078471`, `079171`, `079173`, `079262`, `079263` | Shared technical item; individual product-document review pending |
| Legrand, catalogue line undefined | `067241` | Shared technical item; product-line/document review pending |
| Legrand Vela | `687377` | Shared technical item; individual product-document review pending |

Sharing one `EN_ITEM` establishes a common catalogue capability core. It does not by itself prove that every commercial package is physically identical.

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `H4652/2` | `8012199745350` | [Archived original](https://archive.openwebnet-ha.org/sha256/ad/dd/addd32061c1c9d26cc0d020b1350da5df27703e04b47e09dc7e0c2e25ee4c443.pdf), `H4652_2-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `L4652/2` | `8012199365596` | [Archived original](https://archive.openwebnet-ha.org/sha256/d9/bb/d9bbfd3bf418467ba799b924c4c498bdfd81756e2f2d2a9ce2f4b4872e526f53.pdf), `L4652_2-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `AM5832/2` | `8012199838311` | [Archived original](https://archive.openwebnet-ha.org/sha256/55/3f/553f31cf8d9e29c0823e2d113a732ef7e1d111c44776fbfa8e6390467833ec52.pdf), `AM5832_2-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `067552` | `3245060675523` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/79/fc/79fc17156bfa9496ba91f4c31e18fc53de8b4628e2df4d0fc111386156802dfb.pdf), `067552-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |
| `079171` | `3245060791711` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/51/11/51112351ad65b37aadc0900f4183618a017781b6fd444018804f1628b98f8c30.pdf), `079171-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |
| `079173` | `3245060791735` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/79/c1/79c1d9371186159008b486b4d978ef92d6bc9c7ae3ed89d67e55b04313a66ed5.pdf), `079173-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00286-d-EN` - Basic control for 2 independent loads | Technical sheet | 20/01/2014 | `067552`, `H4652/2`, `L4652/2`, `AM5832/2` | [Archived original](https://archive.openwebnet-ha.org/sha256/36/64/366400ace218504580a0ec2a88e13e7676ace5ed97cdbe9fc34e33441bfb0ff6.pdf) | [Official PDF](https://assets.legrand.com/general/mediagrp/np-ft-gt/mq00286-d-en.pdf) |
| `H4652_2-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `H4652/2` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/ad/dd/addd32061c1c9d26cc0d020b1350da5df27703e04b47e09dc7e0c2e25ee4c443.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4652_2) |
| `L4652_2-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `L4652/2` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/d9/bb/d9bbfd3bf418467ba799b924c4c498bdfd81756e2f2d2a9ce2f4b4872e526f53.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4652_2) |
| `AM5832_2-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `AM5832/2` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/55/3f/553f31cf8d9e29c0823e2d113a732ef7e1d111c44776fbfa8e6390467833ec52.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5832_2) |
| `067552-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `067552` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/79/fc/79fc17156bfa9496ba91f4c31e18fc53de8b4628e2df4d0fc111386156802dfb.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue/commande-celiane-1-ou-2-fonctions-pour-lumiere-ou-volets-myhome-up) |
| `079171-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `079171` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/51/11/51112351ad65b37aadc0900f4183618a017781b6fd444018804f1628b98f8c30.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue-archives/commande-mosaic-pour-lumiere-ou-volets-myhome-up-1-sortie-alu) |
| `079173-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `079173` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/79/c1/79c1d9371186159008b486b4d978ef92d6bc9c7ae3ed89d67e55b04313a66ed5.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue-archives/commande-mosaic-pour-lumiere-ou-volets-myhome-up-2-sorties-alu) |

Additional language revisions and product-range-specific sheets should be collected rather than treating this one document as exhaustive.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting size | 2 flush-mounted modules | Official technical sheet |
| Controls | 4 buttons | Official technical sheet |
| Indicators | two-colour LEDs with local brightness/off adjustment | Official technical sheet |
| SCS nominal supply | `27 Vdc` | Official technical sheet |
| SCS operating supply | `18..27 Vdc` | Official technical sheet |
| Maximum LED-brightness current | `6 mA` for `H4652/2`; `8.5 mA` for `L4652/2`, `AM5832/2`, `067552` | Official technical sheet |
| Physical configurator positions | `A1`, `PL1`, `M1`, `A2`, `PL2`, `M2` | Official technical sheet |

The official technical sheet establishes the following for its four named references:


The six documented physical configurator positions are consistent with the ordinary diagnostic interpretation of `N_CONF`, but an observed `DIMENSION 1` value for known hardware is still needed before recording `N_CONF = 6` as corroborated behavior.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `281` | Canonical catalogue |
| Item model / `modobj` | `2` | Canonical catalogue / retained definition |
| Main system | Lighting / Automation | Canonical catalogue / retained definition |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `145` | `-1` | `-1` | `-1` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `145` | `1` | `400` Light control | Fixed/designated metadata | `533` | `400` | `368` |
| `145` | `1` | `401` Automation control | Candidate alternative | `535` | `401` | `369` |
| `145` | `1` | `404` Scheduled scenario | Candidate alternative | `537` | `404` | `370` |
| `145` | `1` | `406` Scheduled scenario PLUS | Candidate alternative | `539` | `406` | `371` |
| `145` | `2` | `400` Light control | Fixed/designated metadata | `534` | `400` | `368` |
| `145` | `2` | `401` Automation control | Candidate alternative | `536` | `401` | `369` |
| `145` | `2` | `404` Scheduled scenario | Candidate alternative | `538` | `404` | `370` |
| `145` | `2` | `406` Scheduled scenario PLUS | Candidate alternative | `540` | `406` | `371` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `145` | `500` Automation double command virgin | `1`, `2` | `400`, `401`, `404`, `406`, `407` | `500` | `18` |

### Reconciled topology notes


Firmware `145` exposes two configurable Modules.

| Object | Description | Slots | Relationship |
| ---: | --- | --- | --- |
| `400` | Light control | `1`, `2` | designated Object |
| `401` | Automation control | `1`, `2` | alternative |
| `404` | Scheduled scenario | `1`, `2` | alternative |
| `406` | Scheduled scenario PLUS | `1`, `2` | alternative |

Virgin Object `500`, **Automation double command virgin**, applies to slots `1` and `2` and permits Objects `400`, `401`, `404`, `406`, and `407` (`AUX` control).

Installed Object selection belongs to [`DIMENSION 30`](../../diagnostics/dim30-modules.md); generic frame syntax is not repeated here.

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `145` | Physical configuration | retained Device-specific configuration modality |
| `145` | Virtual Configuration | retained Device-specific configuration modality |
| `145` | Advanced Configuration | retained Device-specific configuration modality |


The catalogue declares all three modes:

- Physical configuration
- Virtual Configuration
- Advanced Configuration

The official sheet independently documents physical configuration and MyHOME Suite virtual configuration. It also documents Lighting Management configuration modes such as Plug&go, Push&Learn, and Project&Download for the named product variants.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `145` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `145` | `A1` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB`; `15` = `AUX` | `0` | A1; Automation A addressing space (for configurator A1) |
| `145` | `PL1` | `0..9` | `0` | PL1; PL1 - (0-9) |
| `145` | `M1` | `0..8`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `14` = `CEN`; `15` = `PUL` | `0` | M1; Mode physical configurator (0-8, `O/I`,`OFF`,`ON`,SU_GIU,SU_GIU_M,`CEN`,`PUL`) |
| `145` | `A2` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB`; `15` = `AUX` | `0` | A2; Automation A addressing space (for configurator A2) |
| `145` | `PL2` | `0..9` | `0` | PL2; PL2 - (0-9) |
| `145` | `M2` | `0..8`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `14` = `CEN`; `15` = `PUL` | `0` | M2; Mode physical configurator (0-8, `O/I`,`OFF`,`ON`,SU_GIU,SU_GIU_M,`CEN`,`PUL`) |




### Published and reconciled details


The complete firmware-scoped configuration surface is:

| Field | Domain | Meaning / document correlation |
| --- | --- | --- |
| `AID` | Device identity field | not a physical configurator |
| `A1`, `A2` | `0..9`, `GEN=12`, `GR=13`, `AMB=14`, `AUX=15` | channel address scope |
| `PL1`, `PL2` | `0..9` | physical point / function value |
| `M1`, `M2` | `0..8`, `O/I=9`, `OFF=10`, `ON=11`, `UP/DOWN=12`, `UP/DOWN monostable=13`, `CEN=14`, `PUL=15` | channel mode |

The official sheet uses physical `A=1..9` and `PL=1..9` for ordinary point-to-point addressing, while the database stores `0` in the firmware-level domains. Preserve that source-level distinction.

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


### Reconciled Object notes


The Objects reachable from the Device expose these reusable configuration families:

| Object | Principal configuration surface |
| ---: | --- |
| `400` Light control | mode; point/area/group/general address; installation/destination level; reference address; timed and dimmer parameters; `AUX` input |
| `401` Automation control | bistable/monostable/blades mode; point/area/group/general address; installation/destination level; reference address; `AUX` input |
| `404` Scheduled scenario | `A`, `PL`, upper/lower button `0..31`, `AUX` input, restart delay |
| `406` Scheduled scenario PLUS | scenario number split across low/high fields; upper/lower button `0..31` |
| `407` `AUX` control | toggle/`ON`/`OFF`/`PUL`/automation/reset/enable-disable modes; `AUX` output channel `1..15`; `AUX` input `0..15` |

These are reusable Object definitions. A value appearing in a reusable Object enum is not automatically a physically reachable configuration of this Device; firmware conditions and conversion rules remain authoritative for reachability.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `145` | `1` | `400` | `4165` | `A1=AMB` | `94` |
| `145` | `1` | `400` | `4167` | `A1=GEN` | `95` |
| `145` | `1` | `400` | `4169` | `A1=GR` | `93` |
| `145` | `1` | `400` | `4192` | `M1<>CEN;A1<>AUX;A1<>GR;A1<>AMB;A1<>GEN` | `4` |
| `145` | `1` | `400` | `4233` | `M1=0;A1<>AUX;A1<>GR;A1<>AMB;A1<>GEN` | `4` |
| `145` | `1` | `400` | `4234` | `M1=0;A1=AMB` | `94` |
| `145` | `1` | `400` | `4236` | `M1=0;A1=GEN` | `95` |
| `145` | `1` | `400` | `4237` | `M1=0;A1=GR` | `93` |
| `145` | `1` | `400` | `4274` | `M1=O/I;A1<>AUX;A1<>GR;A1<>AMB;A1<>GEN` | `4` |
| `145` | `1` | `400` | `4275` | `M1=O/I;A1=AMB` | `94` |
| `145` | `1` | `400` | `4277` | `M1=O/I;A1=GEN` | `95` |
| `145` | `1` | `400` | `4278` | `M1=O/I;A1=GR` | `93` |
| `145` | `1` | `400` | `4281` | `M1=OFF;A1<>AUX;A1<>GR;A1<>AMB;A1<>GEN` | `4` |
| `145` | `1` | `400` | `4282` | `M1=OFF;A1=AMB` | `94` |
| `145` | `1` | `400` | `4284` | `M1=OFF;A1=GEN` | `95` |
| `145` | `1` | `400` | `4285` | `M1=OFF;A1=GR` | `93` |
| `145` | `1` | `400` | `4286` | `M1=ON;A1<>AUX;A1<>GR;A1<>AMB;A1<>GEN` | `4` |
| `145` | `1` | `400` | `4287` | `M1=ON;A1=AMB` | `94` |
| `145` | `1` | `400` | `4289` | `M1=ON;A1=GEN` | `95` |
| `145` | `1` | `400` | `4290` | `M1=ON;A1=GR` | `93` |
| `145` | `1` | `400` | `4293` | `M1=PUL;A1<>AUX;A1<>GR;A1<>AMB;A1<>GEN` | `4` |
| `145` | `1` | `400` | `4294` | `M1=PUL;A1=AMB` | `94` |
| `145` | `1` | `400` | `4296` | `M1=PUL;A1=GEN` | `95` |
| `145` | `1` | `400` | `4297` | `M1=PUL;A1=GR` | `93` |
| `145` | `1` | `401` | `4300` | `M1=SU_GIU;A1<>AUX;A1<>GR;A1<>AMB;A1<>GEN` | `4` |
| `145` | `1` | `401` | `4301` | `M1=SU_GIU;A1=AMB` | `94` |
| `145` | `1` | `401` | `4303` | `M1=SU_GIU;A1=GEN` | `95` |
| `145` | `1` | `401` | `4304` | `M1=SU_GIU;A1=GR` | `93` |
| `145` | `1` | `401` | `4308` | `M1=SU_GIU_M;A1<>AUX;A1<>GR;A1<>AMB;A1<>GEN` | `4` |
| `145` | `1` | `401` | `4309` | `M1=SU_GIU_M;A1=AMB` | `94` |
| `145` | `1` | `401` | `4311` | `M1=SU_GIU_M;A1=GEN` | `95` |
| `145` | `1` | `401` | `4312` | `M1=SU_GIU_M;A1=GR` | `93` |
| `145` | `1` | `404` | `4254` | `M1=CEN` | `4` |
| `145` | `1` | `404` | `4270` | `M1=M2;M2=CEN` | `17` |
| `145` | `1` | `406` | `4269` | `M1=FAKE` | None |
| `145` | `2` | `400` | `4171` | `A2=AMB` | `97` |
| `145` | `2` | `400` | `4173` | `A2=GEN` | `95` |
| `145` | `2` | `400` | `4175` | `A2=GR` | `96` |
| `145` | `2` | `400` | `4314` | `M2<>CEN;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `145` | `2` | `400` | `4315` | `M2=0;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `145` | `2` | `400` | `4316` | `M2=0;A2=AMB` | `97` |
| `145` | `2` | `400` | `4318` | `M2=0;A2=GEN` | `95` |
| `145` | `2` | `400` | `4319` | `M2=0;A2=GR` | `96` |
| `145` | `2` | `400` | `4391` | `M2=O/I;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `145` | `2` | `400` | `4392` | `M2=O/I;A2=AMB` | `97` |
| `145` | `2` | `400` | `4394` | `M2=O/I;A2=GEN` | `95` |
| `145` | `2` | `400` | `4395` | `M2=O/I;A2=GR` | `96` |
| `145` | `2` | `400` | `4396` | `M2=OFF;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `145` | `2` | `400` | `4397` | `M2=OFF;A2=AMB` | `97` |
| `145` | `2` | `400` | `4399` | `M2=OFF;A2=GEN` | `95` |
| `145` | `2` | `400` | `4400` | `M2=OFF;A2=GR` | `96` |
| `145` | `2` | `400` | `4401` | `M2=ON;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `145` | `2` | `400` | `4402` | `M2=ON;A2=AMB` | `97` |
| `145` | `2` | `400` | `4404` | `M2=ON;A2=GEN` | `95` |
| `145` | `2` | `400` | `4405` | `M2=ON;A2=GR` | `96` |
| `145` | `2` | `400` | `4406` | `M2=PUL;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `145` | `2` | `400` | `4407` | `M2=PUL;A2=AMB` | `97` |
| `145` | `2` | `400` | `4409` | `M2=PUL;A2=GEN` | `95` |
| `145` | `2` | `400` | `4410` | `M2=PUL;A2=GR` | `96` |
| `145` | `2` | `401` | `4411` | `M2=SU_GIU;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `145` | `2` | `401` | `4412` | `M2=SU_GIU;A2=AMB` | `97` |
| `145` | `2` | `401` | `4414` | `M2=SU_GIU;A2=GEN` | `95` |
| `145` | `2` | `401` | `4415` | `M2=SU_GIU;A2=GR` | `96` |
| `145` | `2` | `401` | `4417` | `M2=SU_GIU_M;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `145` | `2` | `401` | `4418` | `M2=SU_GIU_M;A2=AMB` | `97` |
| `145` | `2` | `401` | `4420` | `M2=SU_GIU_M;A2=GEN` | `95` |
| `145` | `2` | `401` | `4421` | `M2=SU_GIU_M;A2=GR` | `96` |
| `145` | `2` | `404` | `4271` | `M1=M2;M2=CEN` | `18` |
| `145` | `2` | `404` | `4389` | `M2=CEN` | `4` |
| `145` | `2` | `406` | `4390` | `M2=FAKE` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `145` | `400` | `263` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `145` | `400` | `264` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `145` | `400` | `265` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `145` | `400` | `266` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `145` | `400` | `267` | `START_S` | `0..255` (entire reusable range retained) | `255` | Soft start speed |
| `145` | `400` | `268` | `STOP_S` | `0..255` (entire reusable range retained) | `255` | Soft stop speed |
| `145` | `400` | `269` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `145` | `400` | `270` | `LEVEL` | `0..100` (entire reusable range retained) | `100` | Level |
| `145` | `400` | `271` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `145` | `400` | `272` | `DIMMING_S` | `0..255` (entire reusable range retained) | `255` | Dimming speed |
| `145` | `400` | `273` | `M` | `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `130` = Customized `ON`/`OFF` and point to point dimmer; `131` = Customized toggle dimmer; `132` = Customized `ON`/`OFF` and dimmer; `133` = Customized toggle dimmer without regulation; `134` = Customized `ON`/`OFF` and dimmer without regulation; `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `4` = Toggle `ON`/`OFF`; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `5` = `ON`/`OFF`; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90% | `0` | Modality; reusable default `0` is outside this subset; filter supplies no replacement default |
| `145` | `401` | `277` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `145` | `401` | `278` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `145` | `401` | `279` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `145` | `404` | `281` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `145` | `404` | `1701` | `START_DELAY` | `0..255` (entire reusable range retained) | `10` | Start delay |

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
| `17` | `M1=CEN` | `IN_AUX_CHANNEL` = `0`; `CEN_BUTT_1` = `1`; `CEN_BUTT_2` = `3` | `17` |
| `18` | `M2=CEN` | `IN_AUX_CHANNEL` = `0`; `CEN_BUTT_1` = `2`; `CEN_BUTT_2` = `4` | `18` |
| `93` | `M1=0` | `M` = `0`; `ADDR_TYPE` = `2` | `93` |
| `93` | `M1=1` | `M` = `1`; `T_TIME ` = `1`; `ADDR_TYPE` = `2` | `93` |
| `93` | `M1=2` | `M` = `1`; `T_TIME ` = `2`; `ADDR_TYPE` = `2` | `93` |
| `93` | `M1=3` | `M` = `1`; `T_TIME ` = `3`; `ADDR_TYPE` = `2` | `93` |
| `93` | `M1=4` | `T_TIME ` = `4`; `M` = `1`; `ADDR_TYPE` = `2` | `93` |
| `93` | `M1=5` | `T_TIME ` = `5`; `M` = `1`; `ADDR_TYPE` = `2` | `93` |
| `93` | `M1=6` | `M` = `1`; `T_TIME ` = `6`; `ADDR_TYPE` = `2` | `93` |
| `93` | `M1=7` | `M` = `1`; `T_TIME ` = `7`; `ADDR_TYPE` = `2` | `93` |
| `93` | `M1=8` | `T_TIME ` = `8`; `M` = `1`; `ADDR_TYPE` = `2` | `93` |
| `93` | `M1=O/I` | `M` = `9`; `ADDR_TYPE` = `2` | `93` |
| `93` | `M1=OFF` | `M` = `10`; `ADDR_TYPE` = `2` | `93` |
| `93` | `M1=ON` | `M` = `11`; `ADDR_TYPE` = `2` | `93` |
| `93` | `M1=PUL` | `M` = `15`; `ADDR_TYPE` = `2` | `93` |
| `93` | `M1=SU_GIU` | `M` = `12`; `ADDR_TYPE` = `2` | `93` |
| `93` | `M1=SU_GIU_M` | `M` = `13`; `ADDR_TYPE` = `2` | `93` |
| `93` | `M1=0; PL1=1` | `G1` = `1` | `93` → `200` |
| `93` | `M1=0; PL1=2` | `G1` = `2` | `93` → `200` |
| `93` | `M1=0; PL1=3` | `G1` = `3` | `93` → `200` |
| `93` | `M1=0; PL1=4` | `G1` = `4` | `93` → `200` |
| `93` | `M1=0; PL1=5` | `G1` = `5` | `93` → `200` |
| `93` | `M1=0; PL1=6` | `G1` = `6` | `93` → `200` |
| `93` | `M1=0; PL1=7` | `G1` = `7` | `93` → `200` |
| `93` | `M1=0; PL1=8` | `G1` = `8` | `93` → `200` |
| `93` | `M1=0; PL1=9` | `G1` = `9` | `93` → `200` |
| `93` | `M1=1; PL1=1` | `G1` = `1` | `93` → `200` |
| `93` | `M1=1; PL1=2` | `G1` = `2` | `93` → `200` |
| `93` | `M1=1; PL1=3` | `G1` = `3` | `93` → `200` |
| `93` | `M1=1; PL1=4` | `G1` = `4` | `93` → `200` |
| `93` | `M1=1; PL1=5` | `G1` = `5` | `93` → `200` |
| `93` | `M1=1; PL1=6` | `G1` = `6` | `93` → `200` |
| `93` | `M1=1; PL1=7` | `G1` = `7` | `93` → `200` |
| `93` | `M1=1; PL1=8` | `G1` = `8` | `93` → `200` |
| `93` | `M1=1; PL1=9` | `G1` = `9` | `93` → `200` |
| `93` | `M1=2; PL1=1` | `G1` = `1` | `93` → `200` |
| `93` | `M1=2; PL1=2` | `G1` = `2` | `93` → `200` |
| `93` | `M1=2; PL1=3` | `G1` = `3` | `93` → `200` |
| `93` | `M1=2; PL1=4` | `G1` = `4` | `93` → `200` |
| `93` | `M1=2; PL1=5` | `G1` = `5` | `93` → `200` |
| `93` | `M1=2; PL1=6` | `G1` = `6` | `93` → `200` |
| `93` | `M1=2; PL1=7` | `G1` = `7` | `93` → `200` |
| `93` | `M1=2; PL1=8` | `G1` = `8` | `93` → `200` |
| `93` | `M1=2; PL1=9` | `G1` = `9` | `93` → `200` |
| `93` | `M1=3; PL1=1` | `G1` = `1` | `93` → `200` |
| `93` | `M1=3; PL1=2` | `G1` = `2` | `93` → `200` |
| `93` | `M1=3; PL1=3` | `G1` = `3` | `93` → `200` |
| `93` | `M1=3; PL1=4` | `G1` = `4` | `93` → `200` |
| `93` | `M1=3; PL1=5` | `G1` = `5` | `93` → `200` |
| `93` | `M1=3; PL1=6` | `G1` = `6` | `93` → `200` |
| `93` | `M1=3; PL1=7` | `G1` = `7` | `93` → `200` |
| `93` | `M1=3; PL1=8` | `G1` = `8` | `93` → `200` |
| `93` | `M1=3; PL1=9` | `G1` = `9` | `93` → `200` |
| `93` | `M1=4; PL1=1` | `G1` = `1` | `93` → `200` |
| `93` | `M1=4; PL1=2` | `G1` = `2` | `93` → `200` |
| `93` | `M1=4; PL1=3` | `G1` = `3` | `93` → `200` |
| `93` | `M1=4; PL1=4` | `G1` = `4` | `93` → `200` |
| `93` | `M1=4; PL1=5` | `G1` = `5` | `93` → `200` |
| `93` | `M1=4; PL1=6` | `G1` = `6` | `93` → `200` |
| `93` | `M1=4; PL1=7` | `G1` = `7` | `93` → `200` |
| `93` | `M1=4; PL1=8` | `G1` = `8` | `93` → `200` |
| `93` | `M1=4; PL1=9` | `G1` = `9` | `93` → `200` |
| `93` | `M1=5; PL1=1` | `G1` = `1` | `93` → `200` |
| `93` | `M1=5; PL1=2` | `G1` = `2` | `93` → `200` |
| `93` | `M1=5; PL1=3` | `G1` = `3` | `93` → `200` |
| `93` | `M1=5; PL1=4` | `G1` = `4` | `93` → `200` |
| `93` | `M1=5; PL1=5` | `G1` = `5` | `93` → `200` |
| `93` | `M1=5; PL1=6` | `G1` = `6` | `93` → `200` |
| `93` | `M1=5; PL1=7` | `G1` = `7` | `93` → `200` |
| `93` | `M1=5; PL1=8` | `G1` = `8` | `93` → `200` |
| `93` | `M1=5; PL1=9` | `G1` = `9` | `93` → `200` |
| `93` | `M1=6; PL1=1` | `G1` = `1` | `93` → `200` |
| `93` | `M1=6; PL1=2` | `G1` = `2` | `93` → `200` |
| `93` | `M1=6; PL1=3` | `G1` = `3` | `93` → `200` |
| `93` | `M1=6; PL1=4` | `G1` = `4` | `93` → `200` |
| `93` | `M1=6; PL1=5` | `G1` = `5` | `93` → `200` |
| `93` | `M1=6; PL1=6` | `G1` = `6` | `93` → `200` |
| `93` | `M1=6; PL1=7` | `G1` = `7` | `93` → `200` |
| `93` | `M1=6; PL1=8` | `G1` = `8` | `93` → `200` |
| `93` | `M1=6; PL1=9` | `G1` = `9` | `93` → `200` |
| `93` | `M1=7; PL1=1` | `G1` = `1` | `93` → `200` |
| `93` | `M1=7; PL1=2` | `G1` = `2` | `93` → `200` |
| `93` | `M1=7; PL1=3` | `G1` = `3` | `93` → `200` |
| `93` | `M1=7; PL1=4` | `G1` = `4` | `93` → `200` |
| `93` | `M1=7; PL1=5` | `G1` = `5` | `93` → `200` |
| `93` | `M1=7; PL1=6` | `G1` = `6` | `93` → `200` |
| `93` | `M1=7; PL1=7` | `G1` = `7` | `93` → `200` |
| `93` | `M1=7; PL1=8` | `G1` = `8` | `93` → `200` |
| `93` | `M1=7; PL1=9` | `G1` = `9` | `93` → `200` |
| `93` | `M1=8; PL1=1` | `G1` = `1` | `93` → `200` |
| `93` | `M1=8; PL1=2` | `G1` = `2` | `93` → `200` |
| `93` | `M1=8; PL1=3` | `G1` = `3` | `93` → `200` |
| `93` | `M1=8; PL1=4` | `G1` = `4` | `93` → `200` |
| `93` | `M1=8; PL1=5` | `G1` = `5` | `93` → `200` |
| `93` | `M1=8; PL1=6` | `G1` = `6` | `93` → `200` |
| `93` | `M1=8; PL1=7` | `G1` = `7` | `93` → `200` |
| `93` | `M1=8; PL1=8` | `G1` = `8` | `93` → `200` |
| `93` | `M1=8; PL1=9` | `G1` = `9` | `93` → `200` |
| `93` | `M1=O/I; PL1=1` | `G1` = `1` | `93` → `200` |
| `93` | `M1=O/I; PL1=2` | `G1` = `2` | `93` → `200` |
| `93` | `M1=O/I; PL1=3` | `G1` = `3` | `93` → `200` |
| `93` | `M1=O/I; PL1=4` | `G1` = `4` | `93` → `200` |
| `93` | `M1=O/I; PL1=5` | `G1` = `5` | `93` → `200` |
| `93` | `M1=O/I; PL1=6` | `G1` = `6` | `93` → `200` |
| `93` | `M1=O/I; PL1=7` | `G1` = `7` | `93` → `200` |
| `93` | `M1=O/I; PL1=8` | `G1` = `8` | `93` → `200` |
| `93` | `M1=O/I; PL1=9` | `G1` = `9` | `93` → `200` |
| `93` | `M1=OFF; PL1=1` | `G1` = `1` | `93` → `200` |
| `93` | `M1=OFF; PL1=2` | `G1` = `2` | `93` → `200` |
| `93` | `M1=OFF; PL1=3` | `G1` = `3` | `93` → `200` |
| `93` | `M1=OFF; PL1=4` | `G1` = `4` | `93` → `200` |
| `93` | `M1=OFF; PL1=5` | `G1` = `5` | `93` → `200` |
| `93` | `M1=OFF; PL1=6` | `G1` = `6` | `93` → `200` |
| `93` | `M1=OFF; PL1=7` | `G1` = `7` | `93` → `200` |
| `93` | `M1=OFF; PL1=8` | `G1` = `8` | `93` → `200` |
| `93` | `M1=OFF; PL1=9` | `G1` = `9` | `93` → `200` |
| `93` | `M1=ON; PL1=1` | `G1` = `1` | `93` → `200` |
| `93` | `M1=ON; PL1=2` | `G1` = `2` | `93` → `200` |
| `93` | `M1=ON; PL1=3` | `G1` = `3` | `93` → `200` |
| `93` | `M1=ON; PL1=4` | `G1` = `4` | `93` → `200` |
| `93` | `M1=ON; PL1=5` | `G1` = `5` | `93` → `200` |
| `93` | `M1=ON; PL1=6` | `G1` = `6` | `93` → `200` |
| `93` | `M1=ON; PL1=7` | `G1` = `7` | `93` → `200` |
| `93` | `M1=ON; PL1=8` | `G1` = `8` | `93` → `200` |
| `93` | `M1=ON; PL1=9` | `G1` = `9` | `93` → `200` |
| `93` | `M1=PUL; PL1=1` | `G1` = `1` | `93` → `200` |
| `93` | `M1=PUL; PL1=2` | `G1` = `2` | `93` → `200` |
| `93` | `M1=PUL; PL1=3` | `G1` = `3` | `93` → `200` |
| `93` | `M1=PUL; PL1=4` | `G1` = `4` | `93` → `200` |
| `93` | `M1=PUL; PL1=5` | `G1` = `5` | `93` → `200` |
| `93` | `M1=PUL; PL1=6` | `G1` = `6` | `93` → `200` |
| `93` | `M1=PUL; PL1=7` | `G1` = `7` | `93` → `200` |
| `93` | `M1=PUL; PL1=8` | `G1` = `8` | `93` → `200` |
| `93` | `M1=PUL; PL1=9` | `G1` = `9` | `93` → `200` |
| `93` | `M1=SU_GIU; PL1=1` | `G1` = `1` | `93` → `200` |
| `93` | `M1=SU_GIU; PL1=2` | `G1` = `2` | `93` → `200` |
| `93` | `M1=SU_GIU; PL1=3` | `G1` = `3` | `93` → `200` |
| `93` | `M1=SU_GIU; PL1=4` | `G1` = `4` | `93` → `200` |
| `93` | `M1=SU_GIU; PL1=5` | `G1` = `5` | `93` → `200` |
| `93` | `M1=SU_GIU; PL1=6` | `G1` = `6` | `93` → `200` |
| `93` | `M1=SU_GIU; PL1=7` | `G1` = `7` | `93` → `200` |
| `93` | `M1=SU_GIU; PL1=8` | `G1` = `8` | `93` → `200` |
| `93` | `M1=SU_GIU; PL1=9` | `G1` = `9` | `93` → `200` |
| `93` | `M1=SU_GIU_M; PL1=1` | `G1` = `1` | `93` → `200` |
| `93` | `M1=SU_GIU_M; PL1=2` | `G1` = `2` | `93` → `200` |
| `93` | `M1=SU_GIU_M; PL1=3` | `G1` = `3` | `93` → `200` |
| `93` | `M1=SU_GIU_M; PL1=4` | `G1` = `4` | `93` → `200` |
| `93` | `M1=SU_GIU_M; PL1=5` | `G1` = `5` | `93` → `200` |
| `93` | `M1=SU_GIU_M; PL1=6` | `G1` = `6` | `93` → `200` |
| `93` | `M1=SU_GIU_M; PL1=7` | `G1` = `7` | `93` → `200` |
| `93` | `M1=SU_GIU_M; PL1=8` | `G1` = `8` | `93` → `200` |
| `93` | `M1=SU_GIU_M; PL1=9` | `G1` = `9` | `93` → `200` |
| `94` | `M1=0` | `M` = `0`; `ADDR_TYPE` = `1` | `94` |
| `94` | `M1=1` | `M` = `1`; `T_TIME ` = `1`; `ADDR_TYPE` = `1` | `94` |
| `94` | `M1=2` | `M` = `1`; `T_TIME ` = `2`; `ADDR_TYPE` = `1` | `94` |
| `94` | `M1=3` | `M` = `1`; `T_TIME ` = `3`; `ADDR_TYPE` = `1` | `94` |
| `94` | `M1=4` | `T_TIME ` = `4`; `M` = `1`; `ADDR_TYPE` = `1` | `94` |
| `94` | `M1=5` | `T_TIME ` = `5`; `M` = `1`; `ADDR_TYPE` = `1` | `94` |
| `94` | `M1=6` | `M` = `1`; `T_TIME ` = `6`; `ADDR_TYPE` = `1` | `94` |
| `94` | `M1=7` | `M` = `1`; `T_TIME ` = `7`; `ADDR_TYPE` = `1` | `94` |
| `94` | `M1=8` | `T_TIME ` = `8`; `M` = `1`; `ADDR_TYPE` = `1` | `94` |
| `94` | `M1=O/I` | `M` = `9`; `ADDR_TYPE` = `1` | `94` |
| `94` | `M1=OFF` | `M` = `10`; `ADDR_TYPE` = `1` | `94` |
| `94` | `M1=ON` | `M` = `11`; `ADDR_TYPE` = `1` | `94` |
| `94` | `M1=PUL` | `M` = `15`; `ADDR_TYPE` = `1` | `94` |
| `94` | `M1=SU_GIU` | `M` = `12`; `ADDR_TYPE` = `1` | `94` |
| `94` | `M1=SU_GIU_M` | `M` = `13`; `ADDR_TYPE` = `1` | `94` |
| `94` | `M1=0; PL1=1` | `A` = `1` | `94` → `201` |
| `94` | `M1=0; PL1=2` | `A` = `2` | `94` → `201` |
| `94` | `M1=0; PL1=3` | `A` = `3` | `94` → `201` |
| `94` | `M1=0; PL1=4` | `A` = `4` | `94` → `201` |
| `94` | `M1=0; PL1=5` | `A` = `5` | `94` → `201` |
| `94` | `M1=0; PL1=6` | `A` = `6` | `94` → `201` |
| `94` | `M1=0; PL1=7` | `A` = `7` | `94` → `201` |
| `94` | `M1=0; PL1=8` | `A` = `8` | `94` → `201` |
| `94` | `M1=0; PL1=9` | `A` = `9` | `94` → `201` |
| `94` | `M1=1; PL1=1` | `A` = `1` | `94` → `201` |
| `94` | `M1=1; PL1=2` | `A` = `2` | `94` → `201` |
| `94` | `M1=1; PL1=3` | `A` = `3` | `94` → `201` |
| `94` | `M1=1; PL1=4` | `A` = `4` | `94` → `201` |
| `94` | `M1=1; PL1=5` | `A` = `5` | `94` → `201` |
| `94` | `M1=1; PL1=6` | `A` = `6` | `94` → `201` |
| `94` | `M1=1; PL1=7` | `A` = `7` | `94` → `201` |
| `94` | `M1=1; PL1=8` | `A` = `8` | `94` → `201` |
| `94` | `M1=1; PL1=9` | `A` = `9` | `94` → `201` |
| `94` | `M1=2; PL1=1` | `A` = `1` | `94` → `201` |
| `94` | `M1=2; PL1=2` | `A` = `2` | `94` → `201` |
| `94` | `M1=2; PL1=3` | `A` = `3` | `94` → `201` |
| `94` | `M1=2; PL1=4` | `A` = `4` | `94` → `201` |
| `94` | `M1=2; PL1=5` | `A` = `5` | `94` → `201` |
| `94` | `M1=2; PL1=6` | `A` = `6` | `94` → `201` |
| `94` | `M1=2; PL1=7` | `A` = `7` | `94` → `201` |
| `94` | `M1=2; PL1=8` | `A` = `8` | `94` → `201` |
| `94` | `M1=2; PL1=9` | `A` = `9` | `94` → `201` |
| `94` | `M1=3; PL1=1` | `A` = `1` | `94` → `201` |
| `94` | `M1=3; PL1=2` | `A` = `2` | `94` → `201` |
| `94` | `M1=3; PL1=3` | `A` = `3` | `94` → `201` |
| `94` | `M1=3; PL1=4` | `A` = `4` | `94` → `201` |
| `94` | `M1=3; PL1=5` | `A` = `5` | `94` → `201` |
| `94` | `M1=3; PL1=6` | `A` = `6` | `94` → `201` |
| `94` | `M1=3; PL1=7` | `A` = `7` | `94` → `201` |
| `94` | `M1=3; PL1=8` | `A` = `8` | `94` → `201` |
| `94` | `M1=3; PL1=9` | `A` = `9` | `94` → `201` |
| `94` | `M1=4; PL1=1` | `A` = `1` | `94` → `201` |
| `94` | `M1=4; PL1=2` | `A` = `2` | `94` → `201` |
| `94` | `M1=4; PL1=3` | `A` = `3` | `94` → `201` |
| `94` | `M1=4; PL1=4` | `A` = `4` | `94` → `201` |
| `94` | `M1=4; PL1=5` | `A` = `5` | `94` → `201` |
| `94` | `M1=4; PL1=6` | `A` = `6` | `94` → `201` |
| `94` | `M1=4; PL1=7` | `A` = `7` | `94` → `201` |
| `94` | `M1=4; PL1=8` | `A` = `8` | `94` → `201` |
| `94` | `M1=4; PL1=9` | `A` = `9` | `94` → `201` |
| `94` | `M1=5; PL1=1` | `A` = `1` | `94` → `201` |
| `94` | `M1=5; PL1=2` | `A` = `2` | `94` → `201` |
| `94` | `M1=5; PL1=3` | `A` = `3` | `94` → `201` |
| `94` | `M1=5; PL1=4` | `A` = `4` | `94` → `201` |
| `94` | `M1=5; PL1=5` | `A` = `5` | `94` → `201` |
| `94` | `M1=5; PL1=6` | `A` = `6` | `94` → `201` |
| `94` | `M1=5; PL1=7` | `A` = `7` | `94` → `201` |
| `94` | `M1=5; PL1=8` | `A` = `8` | `94` → `201` |
| `94` | `M1=5; PL1=9` | `A` = `9` | `94` → `201` |
| `94` | `M1=6; PL1=1` | `A` = `1` | `94` → `201` |
| `94` | `M1=6; PL1=2` | `A` = `2` | `94` → `201` |
| `94` | `M1=6; PL1=3` | `A` = `3` | `94` → `201` |
| `94` | `M1=6; PL1=4` | `A` = `4` | `94` → `201` |
| `94` | `M1=6; PL1=5` | `A` = `5` | `94` → `201` |
| `94` | `M1=6; PL1=6` | `A` = `6` | `94` → `201` |
| `94` | `M1=6; PL1=7` | `A` = `7` | `94` → `201` |
| `94` | `M1=6; PL1=8` | `A` = `8` | `94` → `201` |
| `94` | `M1=6; PL1=9` | `A` = `9` | `94` → `201` |
| `94` | `M1=7; PL1=1` | `A` = `1` | `94` → `201` |
| `94` | `M1=7; PL1=2` | `A` = `2` | `94` → `201` |
| `94` | `M1=7; PL1=3` | `A` = `3` | `94` → `201` |
| `94` | `M1=7; PL1=4` | `A` = `4` | `94` → `201` |
| `94` | `M1=7; PL1=5` | `A` = `5` | `94` → `201` |
| `94` | `M1=7; PL1=6` | `A` = `6` | `94` → `201` |
| `94` | `M1=7; PL1=7` | `A` = `7` | `94` → `201` |
| `94` | `M1=7; PL1=8` | `A` = `8` | `94` → `201` |
| `94` | `M1=7; PL1=9` | `A` = `9` | `94` → `201` |
| `94` | `M1=8; PL1=1` | `A` = `1` | `94` → `201` |
| `94` | `M1=8; PL1=2` | `A` = `2` | `94` → `201` |
| `94` | `M1=8; PL1=3` | `A` = `3` | `94` → `201` |
| `94` | `M1=8; PL1=4` | `A` = `4` | `94` → `201` |
| `94` | `M1=8; PL1=5` | `A` = `5` | `94` → `201` |
| `94` | `M1=8; PL1=6` | `A` = `6` | `94` → `201` |
| `94` | `M1=8; PL1=7` | `A` = `7` | `94` → `201` |
| `94` | `M1=8; PL1=8` | `A` = `8` | `94` → `201` |
| `94` | `M1=8; PL1=9` | `A` = `9` | `94` → `201` |
| `94` | `M1=O/I; PL1=1` | `A` = `1` | `94` → `201` |
| `94` | `M1=O/I; PL1=2` | `A` = `2` | `94` → `201` |
| `94` | `M1=O/I; PL1=3` | `A` = `3` | `94` → `201` |
| `94` | `M1=O/I; PL1=4` | `A` = `4` | `94` → `201` |
| `94` | `M1=O/I; PL1=5` | `A` = `5` | `94` → `201` |
| `94` | `M1=O/I; PL1=6` | `A` = `6` | `94` → `201` |
| `94` | `M1=O/I; PL1=7` | `A` = `7` | `94` → `201` |
| `94` | `M1=O/I; PL1=8` | `A` = `8` | `94` → `201` |
| `94` | `M1=O/I; PL1=9` | `A` = `9` | `94` → `201` |
| `94` | `M1=OFF; PL1=1` | `A` = `1` | `94` → `201` |
| `94` | `M1=OFF; PL1=2` | `A` = `2` | `94` → `201` |
| `94` | `M1=OFF; PL1=3` | `A` = `3` | `94` → `201` |
| `94` | `M1=OFF; PL1=4` | `A` = `4` | `94` → `201` |
| `94` | `M1=OFF; PL1=5` | `A` = `5` | `94` → `201` |
| `94` | `M1=OFF; PL1=6` | `A` = `6` | `94` → `201` |
| `94` | `M1=OFF; PL1=7` | `A` = `7` | `94` → `201` |
| `94` | `M1=OFF; PL1=8` | `A` = `8` | `94` → `201` |
| `94` | `M1=OFF; PL1=9` | `A` = `9` | `94` → `201` |
| `94` | `M1=ON; PL1=1` | `A` = `1` | `94` → `201` |
| `94` | `M1=ON; PL1=2` | `A` = `2` | `94` → `201` |
| `94` | `M1=ON; PL1=3` | `A` = `3` | `94` → `201` |
| `94` | `M1=ON; PL1=4` | `A` = `4` | `94` → `201` |
| `94` | `M1=ON; PL1=5` | `A` = `5` | `94` → `201` |
| `94` | `M1=ON; PL1=6` | `A` = `6` | `94` → `201` |
| `94` | `M1=ON; PL1=7` | `A` = `7` | `94` → `201` |
| `94` | `M1=ON; PL1=8` | `A` = `8` | `94` → `201` |
| `94` | `M1=ON; PL1=9` | `A` = `9` | `94` → `201` |
| `94` | `M1=PUL; PL1=1` | `A` = `1` | `94` → `201` |
| `94` | `M1=PUL; PL1=2` | `A` = `2` | `94` → `201` |
| `94` | `M1=PUL; PL1=3` | `A` = `3` | `94` → `201` |
| `94` | `M1=PUL; PL1=4` | `A` = `4` | `94` → `201` |
| `94` | `M1=PUL; PL1=5` | `A` = `5` | `94` → `201` |
| `94` | `M1=PUL; PL1=6` | `A` = `6` | `94` → `201` |
| `94` | `M1=PUL; PL1=7` | `A` = `7` | `94` → `201` |
| `94` | `M1=PUL; PL1=8` | `A` = `8` | `94` → `201` |
| `94` | `M1=PUL; PL1=9` | `A` = `9` | `94` → `201` |
| `94` | `M1=SU_GIU; PL1=1` | `A` = `1` | `94` → `201` |
| `94` | `M1=SU_GIU; PL1=2` | `A` = `2` | `94` → `201` |
| `94` | `M1=SU_GIU; PL1=3` | `A` = `3` | `94` → `201` |
| `94` | `M1=SU_GIU; PL1=4` | `A` = `4` | `94` → `201` |
| `94` | `M1=SU_GIU; PL1=5` | `A` = `5` | `94` → `201` |
| `94` | `M1=SU_GIU; PL1=6` | `A` = `6` | `94` → `201` |
| `94` | `M1=SU_GIU; PL1=7` | `A` = `7` | `94` → `201` |
| `94` | `M1=SU_GIU; PL1=8` | `A` = `8` | `94` → `201` |
| `94` | `M1=SU_GIU; PL1=9` | `A` = `9` | `94` → `201` |
| `94` | `M1=SU_GIU_M; PL1=1` | `A` = `1` | `94` → `201` |
| `94` | `M1=SU_GIU_M; PL1=2` | `A` = `2` | `94` → `201` |
| `94` | `M1=SU_GIU_M; PL1=3` | `A` = `3` | `94` → `201` |
| `94` | `M1=SU_GIU_M; PL1=4` | `A` = `4` | `94` → `201` |
| `94` | `M1=SU_GIU_M; PL1=5` | `A` = `5` | `94` → `201` |
| `94` | `M1=SU_GIU_M; PL1=6` | `A` = `6` | `94` → `201` |
| `94` | `M1=SU_GIU_M; PL1=7` | `A` = `7` | `94` → `201` |
| `94` | `M1=SU_GIU_M; PL1=8` | `A` = `8` | `94` → `201` |
| `94` | `M1=SU_GIU_M; PL1=9` | `A` = `9` | `94` → `201` |
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

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `281` and the installed model | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware without treating wildcard sentinels as literal installed values | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`400`, `401`, `404`, `406`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions, and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

### Existing Device-specific diagnostic notes


| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 2`, brand, line, and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe actual installed firmware despite wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3`, `6`, `13` | hardware, microcontroller, and physical Device ID when supported | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | determine active Objects on the two Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine Module system/address configuration | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability


For the four references named by `MQ00286-d-EN`, the sheet documents:

- point-to-point, room, group, and general lighting addressing;
- lighting cyclic, `ON`, `OFF`, pushbutton, timed-`ON`, and dimming functions;
- automation bistable, monostable, and lath/blade control;
- programmed scenario buttons `0..31`;
- PLUS scenario number `1..2047` and button number `0..31` through virtual configuration;
- Lighting Management virtual functions including dual light, `CEN`, `CEN` PLUS, and `AUX` control.

The exact generic functional frame grammar remains canonical under [`WHO 1` - Lighting](../../functional/who-1-lighting/) and [`WHO 2` - Automation](../../functional/who-2-automation/).

## Observed behavior and corroboration

No additional publishable runtime observation is asserted beyond observations explicitly retained elsewhere on this page.

## Programming


A programmer should resolve each Module independently from the physical/virtual configuration, then apply the selected Object configuration and conversion rules. Generic write/read-back mechanics remain in [Programming](../../programming/).

## Source reconciliation


`MQ00286-d-EN` has been reconciled beyond the high-level Object list:

- physical and virtual configuration both support point-to-point, room, group and general lighting control, but the published physical ranges and the reusable Object ranges are not identical;
- the Device supports timed-`ON` and dimming variants in addition to simple cyclic/`ON`/`OFF`/pushbutton behavior;
- load-status feedback for room/group/general commands is tied to a reference actuator address in software configuration rather than being implied by the command address alone;
- `CEN`-only use has a product-level configuration constraint: secondary address positions that are not part of the `CEN` function must remain unconfigured rather than being treated as independent command channels;
- local LED behavior and brightness adjustment are part of the Device user interface and remain distinct from the OpenWebNet command Modules.

The archived technical sheet has therefore been reconciled into both the physical configuration model and the reusable Object model; remaining incompleteness concerns other commercial variants and hardware corroboration.

## Evidence limits and open work


- Archive and hash `MQ00286-d-EN`, its language variants, and older/newer revisions.
- Locate authoritative product documents for the other 15 commercial records sharing item `281`.
- Capture a sanitized fingerprint from known hardware to corroborate `modobj`, `N_CONF`, firmware, Module/Object projection, addressing, and configuration.
- Establish which commercial variants differ only in finish/package and which have material hardware differences.
- Preserve any disagreement between product documentation and the catalogue rather than normalizing it away.

## Sources


- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
- [Programming](../../programming/)

- `H4652_2-ean-product-sheet.pdf`, printed/PDF p. 1: exact `H4652/2` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/ad/dd/addd32061c1c9d26cc0d020b1350da5df27703e04b47e09dc7e0c2e25ee4c443.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4652_2); SHA-256 `addd32061c1c9d26cc0d020b1350da5df27703e04b47e09dc7e0c2e25ee4c443`.
- `L4652_2-ean-product-sheet.pdf`, printed/PDF p. 1: exact `L4652/2` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/d9/bb/d9bbfd3bf418467ba799b924c4c498bdfd81756e2f2d2a9ce2f4b4872e526f53.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4652_2); SHA-256 `d9bbfd3bf418467ba799b924c4c498bdfd81756e2f2d2a9ce2f4b4872e526f53`.
- `AM5832_2-ean-product-sheet.pdf`, printed/PDF p. 1: exact `AM5832/2` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/55/3f/553f31cf8d9e29c0823e2d113a732ef7e1d111c44776fbfa8e6390467833ec52.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5832_2); SHA-256 `553f31cf8d9e29c0823e2d113a732ef7e1d111c44776fbfa8e6390467833ec52`.

- `067552-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `067552` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/79/fc/79fc17156bfa9496ba91f4c31e18fc53de8b4628e2df4d0fc111386156802dfb.pdf); [publisher source](https://www.legrand.fr/pro/catalogue/commande-celiane-1-ou-2-fonctions-pour-lumiere-ou-volets-myhome-up); SHA-256 `79fc17156bfa9496ba91f4c31e18fc53de8b4628e2df4d0fc111386156802dfb`.
- `079171-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `079171` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/51/11/51112351ad65b37aadc0900f4183618a017781b6fd444018804f1628b98f8c30.pdf); [publisher source](https://www.legrand.fr/pro/catalogue-archives/commande-mosaic-pour-lumiere-ou-volets-myhome-up-1-sortie-alu); SHA-256 `51112351ad65b37aadc0900f4183618a017781b6fd444018804f1628b98f8c30`.
- `079173-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `079173` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/79/c1/79c1d9371186159008b486b4d978ef92d6bc9c7ae3ed89d67e55b04313a66ed5.pdf); [publisher source](https://www.legrand.fr/pro/catalogue-archives/commande-mosaic-pour-lumiere-ou-volets-myhome-up-2-sorties-alu); SHA-256 `79c1d9371186159008b486b4d978ef92d6bc9c7ae3ed89d67e55b04313a66ed5`.
