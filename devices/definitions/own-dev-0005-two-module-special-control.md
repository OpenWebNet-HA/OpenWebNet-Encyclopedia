# Two-module special control

## Summary


| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0005` | Project identity |
| Technical description | Two-module configurable special-function SCS control | Catalogue + official technical sheet |
| Catalogue item | `1524` - “Special control” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `16` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `146` | Implementation evidence |
| Declared Modules | `2` | Implementation evidence |
| Categories | Command, Multifunction, Lighting, Automation, Scenario, Audio / Video | Capability model |

This technical definition covers the shared catalogue capability core used by 13 commercial Device records. The official `MQ00285-d-EN` technical sheet directly covers `067553`, `H4651M2`, `L4651M2`, and `AM5831M2`. The other records remain catalogue-correlated commercial identities pending individual document review.

## Commercial identities


### Directly documented references

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4651M2` | Established identity | Catalogue + `MQ00285-d-EN` |
| BTicino - LivingLight | `L4651M2` | Established identity | Catalogue + `MQ00285-d-EN` |
| BTicino - Matix | `AM5831M2` | Established identity | Catalogue + `MQ00285-d-EN` |
| Legrand - Céliane | `067553` | Established identity | Catalogue + `MQ00285-d-EN` |

### Additional commercial records sharing item 1524

| Brand / line | References | Status |
| --- | --- | --- |
| Arnould Espace Evolution | `64162`, `64362` | Shared technical item; individual product-document review pending |
| Legrand Arteor | `571849`, `573987` | Shared technical item; individual product-document review pending |
| Legrand Céliane | `067242` | Shared technical item; individual product-document review pending |
| Legrand Mosaic | `078472`, `078475`, `079172`, `079175` | Shared technical item; individual product-document review pending |
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00285-d-EN` - Special control | Technical sheet | 09/06/2014 | `067553`, `H4651M2`, `L4651M2`, `AM5831M2` | [Archived original](https://archive.openwebnet-ha.org/sha256/03/f5/03f5093d833c675ac3fdf10c2e3b21e38e494bc3b3637d2838454e9a85b81cab.pdf) | [Official PDF](https://assets.legrand.com/pim/NP-FT-GT/MQ00285-d-EN.pdf) |

The nine-page sheet is unusually valuable because it documents several otherwise unrelated functional systems exposed by the same configurable control.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting size | 2 flush-mounted modules | Official technical sheet |
| Controls | 4 buttons | Official technical sheet |
| Indicators | two-colour LEDs with local brightness/off adjustment | Official technical sheet |
| SCS nominal supply | `27 Vdc` | Official technical sheet |
| SCS operating supply | `18..27 Vdc` | Official technical sheet |
| Maximum LED-brightness current | `6 mA` H4651M2; `7.5 mA` 067553; `8.5 mA` L4651M2 and AM5831M2 | Official technical sheet |
| Operating temperature | `5..35 °C` | Official technical sheet |
| Physical configurator positions | `A`, `PL/PF`, `M`, `LIV1/AUX`, `LIV2`, `SPE`, `I` | Official technical sheet |

For the four named references, the official sheet establishes:


The seven documented configurator positions strongly support the ordinary diagnostic interpretation `N_CONF = 7`, but a known-hardware observation is still required before marking that value as corroborated.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1524` | Canonical catalogue |
| Item model / `modobj` | `16` | Canonical catalogue / retained definition |
| Main system | Lighting / Automation | Canonical catalogue / retained definition |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `146` | `-1` | `-1` | `-1` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `146` | `1` | `400` Light control | Fixed/designated metadata | `716` | `400` | `494` |
| `146` | `1` | `401` Automation control | Candidate alternative | `718` | `401` | `495` |
| `146` | `1` | `402` Lock/unlock actuator control | Candidate alternative | `720` | `402` | `496` |
| `146` | `1` | `403` Scenario module control | Candidate alternative | `722` | `403` | `497` |
| `146` | `1` | `404` Scheduled scenario | Candidate alternative | `724` | `404` | `498` |
| `146` | `1` | `405` Scenario PLUS Lighting Management | Candidate alternative | `726` | `405` | `499` |
| `146` | `1` | `406` Scheduled scenario PLUS | Candidate alternative | `1207` | `406` | `649` |
| `146` | `1` | `408` Open lock control | Candidate alternative | `728` | `408` | `500` |
| `146` | `1` | `409` Sound diffusion control | Candidate alternative | `730` | `409` | `501` |
| `146` | `1` | `427` Floor call control | Candidate alternative | `731` | `427` | `502` |
| `146` | `1` | `430` Staircase light control | Candidate alternative | `733` | `430` | `503` |
| `146` | `2` | `400` Light control | Fixed/designated metadata | `717` | `400` | `494` |
| `146` | `2` | `401` Automation control | Candidate alternative | `719` | `401` | `495` |
| `146` | `2` | `402` Lock/unlock actuator control | Candidate alternative | `721` | `402` | `496` |
| `146` | `2` | `403` Scenario module control | Candidate alternative | `723` | `403` | `497` |
| `146` | `2` | `404` Scheduled scenario | Candidate alternative | `725` | `404` | `498` |
| `146` | `2` | `405` Scenario PLUS Lighting Management | Candidate alternative | `727` | `405` | `499` |
| `146` | `2` | `406` Scheduled scenario PLUS | Candidate alternative | `1208` | `406` | `649` |
| `146` | `2` | `408` Open lock control | Candidate alternative | `729` | `408` | `500` |
| `146` | `2` | `427` Floor call control | Candidate alternative | `732` | `427` | `502` |
| `146` | `2` | `430` Staircase light control | Candidate alternative | `734` | `430` | `503` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `146` | `501` Special double command virgin | `1`, `2` | `400`, `401`, `402`, `403`, `404`, `405`, `406`, `407`, `408`, `409`, `427`, `430` | `501` | `19` |

### Reconciled topology notes


Firmware `146` exposes two configurable Modules and a broad set of Object alternatives.

| Object | Description | Slots |
| ---: | --- | --- |
| `400` | Light control | `1`, `2` |
| `401` | Automation control | `1`, `2` |
| `402` | Lock/unlock actuator control | `1`, `2` |
| `403` | Scenario module control | `1`, `2` |
| `404` | Scheduled scenario | `1`, `2` |
| `405` | Scenario PLUS Lighting Management | `1`, `2` |
| `406` | Scheduled scenario PLUS | `1`, `2` |
| `408` | Open lock control | `1`, `2` |
| `409` | Sound diffusion control | `1` |
| `427` | Floor call control | `1`, `2` |
| `430` | Staircase light control | `1`, `2` |

Virgin Object `501`, **Special double command virgin**, applies to both slots and permits all Objects above plus Object `407` `AUX` control.

The broad Object set explains why this Device belongs to several functional categories despite being one Physical Device.

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `146` | Physical configuration | retained Device-specific configuration modality |
| `146` | Virtual Configuration | retained Device-specific configuration modality |
| `146` | Advanced Configuration | retained Device-specific configuration modality |


The catalogue declares:

- Physical configuration
- Virtual Configuration
- Advanced Configuration

The official sheet independently documents physical configuration and MyHOME Suite virtual configuration.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `146` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `146` | `A` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB`; `15` = `AUX` | `0` | A; Environment (0-9 `GEN`,`GR`,`AMB`,`AUX`) |
| `146` | `PL/PF` | `0..9` | `0` | PL/PF; Light Point |
| `146` | `M` | `0..9`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `14` = `CEN`; `15` = `PUL` | `0` | M; Mode physical configurator (0-9, `O/I`,`OFF`,`ON`,SU_GIU,SU_GIU_M,`CEN`,`PUL`) |
| `146` | `LIV1/AUX` | `0..9` | `0` | LIV1/`AUX`; Configurator LIV1 |
| `146` | `LIV2` | `0..9` | `0` | LIV2; Configurator LIV2 |
| `146` | `SPE` | `0..3`; `6`; `8..9`; `11` = `ON` | `0` | SPE; Special function command control (0,1,2,3,6,8,9,`ON`) |
| `146` | `I` | `0..9` | `0` | I; Automation interface address |




### Published and reconciled details


| Field | Catalogue domain | Purpose |
| --- | --- | --- |
| `AID` | Device identity field | not a physical configurator |
| `A` | `0..9`, `GEN=12`, `GR=13`, `AMB=14`, `AUX=15` | environment/address scope |
| `PL/PF` | `0..9` | lighting/audio point |
| `M` | `0..8`, `O/I=9`, `OFF=10`, `ON=11`, `UP/DOWN=12`, `UP/DOWN monostable=13`, `CEN=14`, `PUL=15`, plus a second stored literal `9` entry | base mode |
| `LIV1/AUX` | `0..9` | level / `AUX` physical field |
| `LIV2` | `0..9` | second level field |
| `SPE` | `0,1,2,3,6,8,9,ON(11)` | special-function selector |
| `I` | `0..9` | automation interface address |

The duplicate stored `M` value `9` - one row labelled `O/I` and another labelled `9` - is retained as a canonical database irregularity. It must not be silently deduplicated without context.

The official sheet uses `A=1..9` and `PL=1..9` for ordinary physical point-to-point addressing while virtual configuration extends the logical ranges.

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


### Object `402` - Lock/unlock actuator control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `1` = Disable (lower button); `2` = Enable (lower button); `3` = Disable (lower button) - enable (upper button) | `1` | Modality |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = All systems | `0` | Destination level |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |


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


### Object `408` - Open lock control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEGMENT` | `0` = Same level; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Level |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |


### Object `409` - Sound diffusion control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `3` = General | `0` | Addressing type |
| `A` | `0..9` | `0` | Area |
| `PF` | `0..9` | `0` | Audio point |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |
| `IS_FOLLOW_ME` | `0` = No; `1` = Yes | `1` | Follow me |
| `SOURCE` | `1..9` | `1` | Source |


### Object `427` - Floor call control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `TO_ALL` | `0` = Point to point; `1` = General | `1` | Type of call |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |


### Object `430` - Staircase light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Associated Internal Unit address - hundreds |
| `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |


### Reconciled Object notes


The reachable Objects expose the following major reusable parameter groups:

| Object | Principal configuration surface |
| ---: | --- |
| `400` Light control | mode; point/area/group/general address; installation/destination level; reference address; timed/dimmer parameters; `AUX` input |
| `401` Automation control | bistable/monostable/blades mode; address scope; installation/destination level; reference address; `AUX` input |
| `402` Lock/unlock actuator control | disable/enable mode; address scope; installation/destination level; `AUX` input |
| `403` Scenario module control | activation/edit mode and encoded scenario-module address |
| `404` Scheduled scenario | `A`, `PL`, button `0..31`, `AUX` input, restart delay |
| `405` Scenario PLUS Lighting Management | two scenario/delay fields, regulation type, per-button delay values |
| `406` Scheduled scenario PLUS | scenario number low/high fields and two button numbers |
| `407` `AUX` control | command mode, `AUX` output `1..15`, `AUX` input `0..15` |
| `408` Open lock control | external-unit address `0..95`, segment, `AUX` input |
| `409` Sound diffusion control | point/area/general address, audio point, follow-me, source, `AUX` input |
| `427` Floor call control | point/general call type, internal-unit address, segment, `AUX` input |
| `430` Staircase light control | internal-unit address, segment, `AUX` input |

Large enumerations such as encoded scenario addresses and delay tables remain machine-extractable from the canonical database. The Device page records their complete semantic domains without duplicating hundreds of mechanically repetitive rows.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `146` | `1` | `400` | `4145` | No textual predicate stored | None |
| `146` | `1` | `400` | `4177` | `A=AMB` | `101` |
| `146` | `1` | `400` | `4181` | `A=GEN` | `104` |
| `146` | `1` | `400` | `4184` | `A=GR` | `98` |
| `146` | `1` | `400` | `4606` | `M=O/I;A=AMB` | `101` |
| `146` | `1` | `400` | `4608` | `M=O/I;A=GEN` | `104` |
| `146` | `1` | `400` | `4609` | `M=O/I;A=GR` | `98` |
| `146` | `1` | `400` | `4620` | `M=OFF;A=AMB` | `101` |
| `146` | `1` | `400` | `4622` | `M=OFF;A=GEN` | `104` |
| `146` | `1` | `400` | `4623` | `M=OFF;A=GR` | `98` |
| `146` | `1` | `400` | `4634` | `M=ON;A=AMB` | `101` |
| `146` | `1` | `400` | `4636` | `M=ON;A=GEN` | `104` |
| `146` | `1` | `400` | `4637` | `M=ON;A=GR` | `98` |
| `146` | `1` | `400` | `4648` | `M=PUL;A<>AUX;A<>GR;A<>AMB;A<>GEN` | `36` |
| `146` | `1` | `400` | `4649` | `M=PUL;A=AMB` | `101` |
| `146` | `1` | `400` | `4651` | `M=PUL;A=GEN` | `104` |
| `146` | `1` | `400` | `4652` | `M=PUL;A=GR` | `98` |
| `146` | `1` | `400` | `4833` | `SPE=1;M=7` | `38` |
| `146` | `1` | `400` | `4837` | `SPE=1;M=8` | `38` |
| `146` | `1` | `400` | `4842` | `SPE=2` | `39` |
| `146` | `1` | `400` | `4844` | `SPE=3` | `40` |
| `146` | `1` | `400` | `4849` | `SPE=5;LIV2<>0` | `21` |
| `146` | `1` | `400` | `4850` | `SPE=5;LIV2=0` | `22` |
| `146` | `1` | `400` | `4878` | `SPE=9;LIV2<>0` | `21` |
| `146` | `1` | `400` | `4879` | `SPE=9;LIV2=0` | `22` |
| `146` | `1` | `400` | `4880` | `SPE=ON` | `42` |
| `146` | `1` | `401` | `4664` | `M=SU_GIU;A<>AUX;A<>GR;A<>AMB;A<>GEN` | `30` |
| `146` | `1` | `401` | `4665` | `M=SU_GIU;A=AMB` | `102` |
| `146` | `1` | `401` | `4667` | `M=SU_GIU;A=GEN` | `105` |
| `146` | `1` | `401` | `4668` | `M=SU_GIU;A=GR` | `99` |
| `146` | `1` | `401` | `4685` | `M=SU_GIU_M;A<>AUX;A<>GR;A<>AMB;A<>GEN` | `30` |
| `146` | `1` | `401` | `4686` | `M=SU_GIU_M;A=AMB` | `102` |
| `146` | `1` | `401` | `4688` | `M=SU_GIU_M;A=GEN` | `105` |
| `146` | `1` | `401` | `4689` | `M=SU_GIU_M;A=GR` | `99` |
| `146` | `1` | `402` | `4800` | `SPE=1;M=1;A<>AUX;A<>GR;A<>AMB;A<>GEN` | `37` |
| `146` | `1` | `402` | `4801` | `SPE=1;M=1;A=AMB` | `103` |
| `146` | `1` | `402` | `4805` | `SPE=1;M=1;A=GEN` | `106` |
| `146` | `1` | `402` | `4806` | `SPE=1;M=1;A=GR` | `100` |
| `146` | `1` | `402` | `4808` | `SPE=1;M=2;A<>AUX;A<>GR;A<>AMB;A<>GEN` | `37` |
| `146` | `1` | `402` | `4809` | `SPE=1;M=2;A=AMB` | `103` |
| `146` | `1` | `402` | `4813` | `SPE=1;M=2;A=GEN` | `106` |
| `146` | `1` | `402` | `4814` | `SPE=1;M=2;A=GR` | `100` |
| `146` | `1` | `402` | `4817` | `SPE=1;M=3;A<>AUX;A<>GR;A<>AMB;A<>GEN` | `37` |
| `146` | `1` | `402` | `4818` | `SPE=1;M=3;A=AMB` | `103` |
| `146` | `1` | `402` | `4822` | `SPE=1;M=3;A=GEN` | `106` |
| `146` | `1` | `402` | `4823` | `SPE=1;M=3;A=GR` | `100` |
| `146` | `1` | `403` | `4846` | `SPE=4` | `41` |
| `146` | `1` | `403` | `4859` | `SPE=6;` | `34` |
| `146` | `1` | `404` | `4585` | `M=CEN` | `7` |
| `146` | `1` | `405` | `4594` | `M=FAKE` | None |
| `146` | `1` | `408` | `4864` | `SPE=7;M=1` | `23` |
| `146` | `1` | `409` | `4875` | `SPE=8` | `24` |
| `146` | `1` | `427` | `4865` | `SPE=7;M=2` | `23` |
| `146` | `1` | `430` | `4866` | `SPE=7;M=3` | `23` |
| `146` | `2` | `400` | `4177` | `A=AMB` | `101` |
| `146` | `2` | `400` | `4181` | `A=GEN` | `104` |
| `146` | `2` | `400` | `4184` | `A=GR` | `98` |
| `146` | `2` | `400` | `4606` | `M=O/I;A=AMB` | `101` |
| `146` | `2` | `400` | `4608` | `M=O/I;A=GEN` | `104` |
| `146` | `2` | `400` | `4609` | `M=O/I;A=GR` | `98` |
| `146` | `2` | `400` | `4620` | `M=OFF;A=AMB` | `101` |
| `146` | `2` | `400` | `4622` | `M=OFF;A=GEN` | `104` |
| `146` | `2` | `400` | `4623` | `M=OFF;A=GR` | `98` |
| `146` | `2` | `400` | `4634` | `M=ON;A=AMB` | `101` |
| `146` | `2` | `400` | `4636` | `M=ON;A=GEN` | `104` |
| `146` | `2` | `400` | `4637` | `M=ON;A=GR` | `98` |
| `146` | `2` | `400` | `4648` | `M=PUL;A<>AUX;A<>GR;A<>AMB;A<>GEN` | `36` |
| `146` | `2` | `400` | `4649` | `M=PUL;A=AMB` | `101` |
| `146` | `2` | `400` | `4651` | `M=PUL;A=GEN` | `104` |
| `146` | `2` | `400` | `4652` | `M=PUL;A=GR` | `98` |
| `146` | `2` | `400` | `4833` | `SPE=1;M=7` | `38` |
| `146` | `2` | `400` | `4837` | `SPE=1;M=8` | `38` |
| `146` | `2` | `400` | `4842` | `SPE=2` | `39` |
| `146` | `2` | `400` | `4844` | `SPE=3` | `40` |
| `146` | `2` | `400` | `4849` | `SPE=5;LIV2<>0` | `21` |
| `146` | `2` | `400` | `4850` | `SPE=5;LIV2=0` | `22` |
| `146` | `2` | `400` | `4878` | `SPE=9;LIV2<>0` | `21` |
| `146` | `2` | `400` | `4879` | `SPE=9;LIV2=0` | `22` |
| `146` | `2` | `400` | `4881` | `SPE=ON` | `43` |
| `146` | `2` | `401` | `4664` | `M=SU_GIU;A<>AUX;A<>GR;A<>AMB;A<>GEN` | `30` |
| `146` | `2` | `401` | `4665` | `M=SU_GIU;A=AMB` | `102` |
| `146` | `2` | `401` | `4667` | `M=SU_GIU;A=GEN` | `105` |
| `146` | `2` | `401` | `4668` | `M=SU_GIU;A=GR` | `99` |
| `146` | `2` | `401` | `4685` | `M=SU_GIU_M;A<>AUX;A<>GR;A<>AMB;A<>GEN` | `30` |
| `146` | `2` | `401` | `4686` | `M=SU_GIU_M;A=AMB` | `102` |
| `146` | `2` | `401` | `4688` | `M=SU_GIU_M;A=GEN` | `105` |
| `146` | `2` | `401` | `4689` | `M=SU_GIU_M;A=GR` | `99` |
| `146` | `2` | `402` | `4800` | `SPE=1;M=1;A<>AUX;A<>GR;A<>AMB;A<>GEN` | `37` |
| `146` | `2` | `402` | `4801` | `SPE=1;M=1;A=AMB` | `103` |
| `146` | `2` | `402` | `4805` | `SPE=1;M=1;A=GEN` | `106` |
| `146` | `2` | `402` | `4806` | `SPE=1;M=1;A=GR` | `100` |
| `146` | `2` | `402` | `4808` | `SPE=1;M=2;A<>AUX;A<>GR;A<>AMB;A<>GEN` | `37` |
| `146` | `2` | `402` | `4809` | `SPE=1;M=2;A=AMB` | `103` |
| `146` | `2` | `402` | `4813` | `SPE=1;M=2;A=GEN` | `106` |
| `146` | `2` | `402` | `4814` | `SPE=1;M=2;A=GR` | `100` |
| `146` | `2` | `402` | `4817` | `SPE=1;M=3;A<>AUX;A<>GR;A<>AMB;A<>GEN` | `37` |
| `146` | `2` | `402` | `4818` | `SPE=1;M=3;A=AMB` | `103` |
| `146` | `2` | `402` | `4822` | `SPE=1;M=3;A=GEN` | `106` |
| `146` | `2` | `402` | `4823` | `SPE=1;M=3;A=GR` | `100` |
| `146` | `2` | `403` | `4846` | `SPE=4` | `41` |
| `146` | `2` | `403` | `4860` | `SPE=6;` | `35` |
| `146` | `2` | `404` | `4586` | `M=CEN` | `8` |
| `146` | `2` | `405` | `4594` | `M=FAKE` | None |
| `146` | `2` | `408` | `4864` | `SPE=7;M=1` | `23` |
| `146` | `2` | `427` | `4865` | `SPE=7;M=2` | `23` |
| `146` | `2` | `430` | `4866` | `SPE=7;M=3` | `23` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `146` | `400` | `697` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `146` | `400` | `698` | `DIMMING_S` | `0..255` (entire reusable range retained) | `255` | Dimming speed |
| `146` | `401` | `701` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `146` | `401` | `1797` | `M` | `14` = Blades control and bistable | `12` | Modality; reusable default `12` is outside this subset; filter supplies no replacement default |
| `146` | `402` | `704` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `146` | `404` | `706` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `146` | `404` | `1708` | `START_DELAY` | `0..255` (entire reusable range retained) | `10` | Start delay |
| `146` | `408` | `708` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `146` | `409` | `709` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `146` | `427` | `712` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `146` | `427` | `1902` | `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone (entire reusable range retained) | `0` | Segment |
| `146` | `430` | `716` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `146` | `430` | `717` | `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone (entire reusable range retained) | `0` | Segment |
| `146` | `430` | `4120` | `N2` | `0..15` (entire reusable range retained) | `0` | Associated Internal Unit address - hundreds |
| `146` | `430` | `4133` | `N1` | `100`; `101`; `102`; `103`; `104`; `105`; `106`; `107`; `108`; `109`; `110`; `111`; `112`; `113`; `114`; `115`; `116`; `117`; `118`; `119`; `120`; `121`; `122`; `123`; `124`; `125`; `126`; `127`; `128`; `129`; `130`; `131`; `132`; `133`; `134`; `135`; `136`; `137`; `138`; `139`; `140`; `141`; `142`; `143`; `144`; `145`; `146`; `147`; `148`; `149`; `150`; `151`; `152`; `153`; `154`; `155`; `156`; `157`; `158`; `159`; `160`; `161`; `162`; `163`; `164`; `165`; `166`; `167`; `168`; `169`; `170`; `171`; `172`; `173`; `174`; `175`; `176`; `177`; `178`; `179`; `180`; `181`; `182`; `183`; `184`; `185`; `186`; `187`; `188`; `189`; `190`; `191`; `192`; `193`; `194`; `195`; `196`; `197`; `198`; `199`; `200`; `201`; `202`; `203`; `204`; `205`; `206`; `207`; `208`; `209`; `210`; `211`; `212`; `213`; `214`; `215`; `216`; `217`; `218`; `219`; `220`; `221`; `222`; `223`; `224`; `225`; `226`; `227`; `228`; `229`; `230`; `231`; `232`; `233`; `234`; `235`; `236`; `237`; `238`; `239`; `240`; `241`; `242`; `243`; `244`; `245`; `246`; `247`; `248`; `249`; `250`; `251`; `252`; `253`; `254`; `255` | `0` | Internal unit address; reusable default `0` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `7` | No item-side predicate on this branch | Referenced conversion rule absent from source | `7` |
| `8` | No item-side predicate on this branch | Referenced conversion rule absent from source | `8` |
| `21` | `I=0` | `INST_LEV` = `1`; `DEST_LEV` = `1` | `21` |
| `21` | `I=1` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `21` |
| `21` | `I=2` | `INST_LEV` = `3`; `DEST_LEV` = `2` | `21` |
| `21` | `I=3` | `INST_LEV` = `4`; `DEST_LEV` = `3` | `21` |
| `21` | `I=4` | `INST_LEV` = `5`; `DEST_LEV` = `4` | `21` |
| `21` | `I=5` | `INST_LEV` = `6`; `DEST_LEV` = `5` | `21` |
| `21` | `I=6` | `INST_LEV` = `7`; `DEST_LEV` = `6` | `21` |
| `21` | `I=7` | `INST_LEV` = `8`; `DEST_LEV` = `7` | `21` |
| `21` | `I=8` | `INST_LEV` = `9`; `DEST_LEV` = `8` | `21` |
| `21` | `I=9` | `INST_LEV` = `10`; `DEST_LEV` = `10` | `21` |
| `21` | `I=CEN` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `21` |
| `21` | `SPE=5` | `M` = `133` | `21` |
| `21` | `SPE=9` | `M` = `134` | `21` |
| `21` | `M=0` | `START_S` = `0`; `STOP_S` = `0` | `21` |
| `21` | `M=1` | `START_S` = `1`; `STOP_S` = `1` | `21` |
| `21` | `M=2` | `START_S` = `2`; `STOP_S` = `2` | `21` |
| `21` | `M=3` | `START_S` = `3`; `STOP_S` = `3` | `21` |
| `21` | `M=4` | `START_S` = `4`; `STOP_S` = `4` | `21` |
| `21` | `M=5` | `START_S` = `5`; `STOP_S` = `5` | `21` |
| `21` | `M=6` | `START_S` = `6`; `STOP_S` = `6` | `21` |
| `21` | `M=7` | `START_S` = `7`; `STOP_S` = `7` | `21` |
| `21` | `M=8` | `START_S` = `8`; `STOP_S` = `8` | `21` |
| `21` | `M=9` | `START_S` = `9`; `STOP_S` = `9` | `21` |
| `21` | `LIV1=0; LIV2=0` | `LEVEL` = `0` | `21` → `45` |
| `21` | `LIV1=0; LIV2=1` | `LEVEL` = `1` | `21` → `45` |
| `21` | `LIV1=0; LIV2=2` | `LEVEL` = `2` | `21` → `45` |
| `21` | `LIV1=0; LIV2=3` | `LEVEL` = `3` | `21` → `45` |
| `21` | `LIV1=0; LIV2=4` | `LEVEL` = `4` | `21` → `45` |
| `21` | `LIV1=0; LIV2=5` | `LEVEL` = `5` | `21` → `45` |
| `21` | `LIV1=0; LIV2=6` | `LEVEL` = `6` | `21` → `45` |
| `21` | `LIV1=0; LIV2=7` | `LEVEL` = `7` | `21` → `45` |
| `21` | `LIV1=0; LIV2=8` | `LEVEL` = `8` | `21` → `45` |
| `21` | `LIV1=0; LIV2=9` | `LEVEL` = `9` | `21` → `45` |
| `21` | `LIV1=1; LIV2=0` | `LEVEL` = `10` | `21` → `46` |
| `21` | `LIV1=1; LIV2=1` | `LEVEL` = `11` | `21` → `46` |
| `21` | `LIV1=1; LIV2=2` | `LEVEL` = `12` | `21` → `46` |
| `21` | `LIV1=1; LIV2=3` | `LEVEL` = `13` | `21` → `46` |
| `21` | `LIV1=1; LIV2=4` | `LEVEL` = `14` | `21` → `46` |
| `21` | `LIV1=1; LIV2=5` | `LEVEL` = `15` | `21` → `46` |
| `21` | `LIV1=1; LIV2=6` | `LEVEL` = `16` | `21` → `46` |
| `21` | `LIV1=1; LIV2=7` | `LEVEL` = `17` | `21` → `46` |
| `21` | `LIV1=1; LIV2=8` | `LEVEL` = `18` | `21` → `46` |
| `21` | `LIV1=1; LIV2=9` | `LEVEL` = `19` | `21` → `46` |
| `21` | `LIV1=2; LIV2=0` | `LEVEL` = `20` | `21` → `47` |
| `21` | `LIV1=2; LIV2=1` | `LEVEL` = `21` | `21` → `47` |
| `21` | `LIV1=2; LIV2=2` | `LEVEL` = `22` | `21` → `47` |
| `21` | `LIV1=2; LIV2=3` | `LEVEL` = `23` | `21` → `47` |
| `21` | `LIV1=2; LIV2=4` | `LEVEL` = `24` | `21` → `47` |
| `21` | `LIV1=2; LIV2=5` | `LEVEL` = `25` | `21` → `47` |
| `21` | `LIV1=2; LIV2=6` | `LEVEL` = `26` | `21` → `47` |
| `21` | `LIV1=2; LIV2=7` | `LEVEL` = `27` | `21` → `47` |
| `21` | `LIV1=2; LIV2=8` | `LEVEL` = `28` | `21` → `47` |
| `21` | `LIV1=2; LIV2=9` | `LEVEL` = `29` | `21` → `47` |
| `21` | `LIV1=3; LIV2=0` | `LEVEL` = `30` | `21` → `48` |
| `21` | `LIV1=3; LIV2=1` | `LEVEL` = `31` | `21` → `48` |
| `21` | `LIV1=3; LIV2=2` | `LEVEL` = `32` | `21` → `48` |
| `21` | `LIV1=3; LIV2=3` | `LEVEL` = `33` | `21` → `48` |
| `21` | `LIV1=3; LIV2=4` | `LEVEL` = `34` | `21` → `48` |
| `21` | `LIV1=3; LIV2=5` | `LEVEL` = `35` | `21` → `48` |
| `21` | `LIV1=3; LIV2=6` | `LEVEL` = `36` | `21` → `48` |
| `21` | `LIV1=3; LIV2=7` | `LEVEL` = `37` | `21` → `48` |
| `21` | `LIV1=3; LIV2=8` | `LEVEL` = `38` | `21` → `48` |
| `21` | `LIV1=3; LIV2=9` | `LEVEL` = `39` | `21` → `48` |
| `21` | `LIV1=4; LIV2=0` | `LEVEL` = `40` | `21` → `49` |
| `21` | `LIV1=4; LIV2=1` | `LEVEL` = `41` | `21` → `49` |
| `21` | `LIV1=4; LIV2=2` | `LEVEL` = `42` | `21` → `49` |
| `21` | `LIV1=4; LIV2=3` | `LEVEL` = `43` | `21` → `49` |
| `21` | `LIV1=4; LIV2=4` | `LEVEL` = `44` | `21` → `49` |
| `21` | `LIV1=4; LIV2=5` | `LEVEL` = `45` | `21` → `49` |
| `21` | `LIV1=4; LIV2=6` | `LEVEL` = `46` | `21` → `49` |
| `21` | `LIV1=4; LIV2=7` | `LEVEL` = `47` | `21` → `49` |
| `21` | `LIV1=4; LIV2=8` | `LEVEL` = `48` | `21` → `49` |
| `21` | `LIV1=4; LIV2=9` | `LEVEL` = `49` | `21` → `49` |
| `21` | `LIV1=5; LIV2=0` | `LEVEL` = `50` | `21` → `50` |
| `21` | `LIV1=5; LIV2=1` | `LEVEL` = `51` | `21` → `50` |
| `21` | `LIV1=5; LIV2=2` | `LEVEL` = `52` | `21` → `50` |
| `21` | `LIV1=5; LIV2=3` | `LEVEL` = `53` | `21` → `50` |
| `21` | `LIV1=5; LIV2=4` | `LEVEL` = `54` | `21` → `50` |
| `21` | `LIV1=5; LIV2=5` | `LEVEL` = `55` | `21` → `50` |
| `21` | `LIV1=5; LIV2=6` | `LEVEL` = `56` | `21` → `50` |
| `21` | `LIV1=5; LIV2=7` | `LEVEL` = `57` | `21` → `50` |
| `21` | `LIV1=5; LIV2=8` | `LEVEL` = `58` | `21` → `50` |
| `21` | `LIV1=5; LIV2=9` | `LEVEL` = `59` | `21` → `50` |
| `21` | `LIV1=6; LIV2=0` | `LEVEL` = `60` | `21` → `51` |
| `21` | `LIV1=6; LIV2=1` | `LEVEL` = `61` | `21` → `51` |
| `21` | `LIV1=6; LIV2=2` | `LEVEL` = `62` | `21` → `51` |
| `21` | `LIV1=6; LIV2=3` | `LEVEL` = `63` | `21` → `51` |
| `21` | `LIV1=6; LIV2=4` | `LEVEL` = `64` | `21` → `51` |
| `21` | `LIV1=6; LIV2=5` | `LEVEL` = `65` | `21` → `51` |
| `21` | `LIV1=6; LIV2=6` | `LEVEL` = `66` | `21` → `51` |
| `21` | `LIV1=6; LIV2=7` | `LEVEL` = `67` | `21` → `51` |
| `21` | `LIV1=6; LIV2=8` | `LEVEL` = `68` | `21` → `51` |
| `21` | `LIV1=6; LIV2=9` | `LEVEL` = `69` | `21` → `51` |
| `21` | `LIV1=7; LIV2=0` | `LEVEL` = `70` | `21` → `52` |
| `21` | `LIV1=7; LIV2=1` | `LEVEL` = `71` | `21` → `52` |
| `21` | `LIV1=7; LIV2=2` | `LEVEL` = `72` | `21` → `52` |
| `21` | `LIV1=7; LIV2=3` | `LEVEL` = `73` | `21` → `52` |
| `21` | `LIV1=7; LIV2=4` | `LEVEL` = `74` | `21` → `52` |
| `21` | `LIV1=7; LIV2=5` | `LEVEL` = `75` | `21` → `52` |
| `21` | `LIV1=7; LIV2=6` | `LEVEL` = `76` | `21` → `52` |
| `21` | `LIV1=7; LIV2=7` | `LEVEL` = `77` | `21` → `52` |
| `21` | `LIV1=7; LIV2=8` | `LEVEL` = `78` | `21` → `52` |
| `21` | `LIV1=7; LIV2=9` | `LEVEL` = `79` | `21` → `52` |
| `21` | `LIV1=8; LIV2=0` | `LEVEL` = `80` | `21` → `53` |
| `21` | `LIV1=8; LIV2=1` | `LEVEL` = `81` | `21` → `53` |
| `21` | `LIV1=8; LIV2=2` | `LEVEL` = `82` | `21` → `53` |
| `21` | `LIV1=8; LIV2=3` | `LEVEL` = `83` | `21` → `53` |
| `21` | `LIV1=8; LIV2=4` | `LEVEL` = `84` | `21` → `53` |
| `21` | `LIV1=8; LIV2=5` | `LEVEL` = `85` | `21` → `53` |
| `21` | `LIV1=8; LIV2=6` | `LEVEL` = `86` | `21` → `53` |
| `21` | `LIV1=8; LIV2=7` | `LEVEL` = `87` | `21` → `53` |
| `21` | `LIV1=8; LIV2=8` | `LEVEL` = `88` | `21` → `53` |
| `21` | `LIV1=8; LIV2=9` | `LEVEL` = `89` | `21` → `53` |
| `21` | `LIV1=9; LIV2=0` | `LEVEL` = `90` | `21` → `54` |
| `21` | `LIV1=9; LIV2=1` | `LEVEL` = `91` | `21` → `54` |
| `21` | `LIV1=9; LIV2=2` | `LEVEL` = `92` | `21` → `54` |
| `21` | `LIV1=9; LIV2=3` | `LEVEL` = `93` | `21` → `54` |
| `21` | `LIV1=9; LIV2=4` | `LEVEL` = `94` | `21` → `54` |
| `21` | `LIV1=9; LIV2=5` | `LEVEL` = `95` | `21` → `54` |
| `21` | `LIV1=9; LIV2=6` | `LEVEL` = `96` | `21` → `54` |
| `21` | `LIV1=9; LIV2=7` | `LEVEL` = `97` | `21` → `54` |
| `21` | `LIV1=9; LIV2=8` | `LEVEL` = `98` | `21` → `54` |
| `21` | `LIV1=9; LIV2=9` | `LEVEL` = `99` | `21` → `54` |
| `22` | `I=0` | `INST_LEV` = `1`; `DEST_LEV` = `1` | `22` |
| `22` | `I=1` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `22` |
| `22` | `I=2` | `INST_LEV` = `3`; `DEST_LEV` = `2` | `22` |
| `22` | `I=3` | `INST_LEV` = `4`; `DEST_LEV` = `3` | `22` |
| `22` | `I=4` | `INST_LEV` = `5`; `DEST_LEV` = `4` | `22` |
| `22` | `I=5` | `INST_LEV` = `6`; `DEST_LEV` = `5` | `22` |
| `22` | `I=6` | `INST_LEV` = `7`; `DEST_LEV` = `6` | `22` |
| `22` | `I=7` | `INST_LEV` = `8`; `DEST_LEV` = `7` | `22` |
| `22` | `I=8` | `INST_LEV` = `9`; `DEST_LEV` = `8` | `22` |
| `22` | `I=9` | `INST_LEV` = `10`; `DEST_LEV` = `9` | `22` |
| `22` | `I=CEN` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `22` |
| `22` | `SPE=5` | `M` = `129` | `22` |
| `22` | `SPE=9` | `M` = `130` | `22` |
| `22` | `M=0` | `START_S` = `0`; `STOP_S` = `0` | `22` |
| `22` | `M=1` | `START_S` = `1`; `STOP_S` = `1` | `22` |
| `22` | `M=2` | `START_S` = `2`; `STOP_S` = `2` | `22` |
| `22` | `M=3` | `START_S` = `3`; `STOP_S` = `3` | `22` |
| `22` | `M=4` | `START_S` = `4`; `STOP_S` = `4` | `22` |
| `22` | `M=5` | `START_S` = `5`; `STOP_S` = `5` | `22` |
| `22` | `M=6` | `START_S` = `6`; `STOP_S` = `6` | `22` |
| `22` | `M=7` | `START_S` = `7`; `STOP_S` = `7` | `22` |
| `22` | `M=8` | `START_S` = `8`; `STOP_S` = `8` | `22` |
| `22` | `M=9` | `START_S` = `9`; `STOP_S` = `9` | `22` |
| `23` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `23` |
| `23` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `23` |
| `23` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `23` |
| `23` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `23` |
| `23` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `23` |
| `23` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `23` |
| `23` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `23` |
| `23` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `23` |
| `23` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `23` |
| `23` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `23` |
| `23` | `M=1` | `M` = `1` | `23` |
| `23` | `M=2` | `M` = `2` | `23` |
| `23` | `M=3` | `M` = `3` | `23` |
| `24` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `24` |
| `24` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `24` |
| `24` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `24` |
| `24` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `24` |
| `24` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `24` |
| `24` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `24` |
| `24` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `24` |
| `24` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `24` |
| `24` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `24` |
| `24` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `24` |
| `24` | `M=0` | `FOLLOW` = `1` | `24` |
| `24` | `M=0; M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `24` → `1` |
| `24` | `M=0; M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `24` → `1` |
| `24` | `M=0; M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `24` → `1` |
| `24` | `M=0; M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `24` → `1` |
| `24` | `M=0; M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `24` → `1` |
| `24` | `M=0; M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `24` → `1` |
| `24` | `M=0; M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `24` → `1` |
| `24` | `M=0; M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `24` → `1` |
| `24` | `M=1` | `FOLLOW` = `0`; `SOURCE` = `1` | `24` |
| `24` | `M=1; M=0` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `60` | `24` → `2` |
| `24` | `M=1; M=1` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `62` | `24` → `2` |
| `24` | `M=1; M=2` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `65` | `24` → `2` |
| `24` | `M=1; M=3` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `70` | `24` → `2` |
| `24` | `M=1; M=4` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `0` | `24` → `2` |
| `24` | `M=1; M=5` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `20` | `24` → `2` |
| `24` | `M=1; M=6` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `10` | `24` → `2` |
| `24` | `M=1; M=7` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `5` | `24` → `2` |
| `24` | `M=1; M=8` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `15` | `24` → `2` |
| `24` | `M=1; M=9` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `30` | `24` → `2` |
| `24` | `M=1; M=I/O` | `LOCAL_BUTTON` = `13`; `M` = `0`; `STOP_TIME` = `60` | `24` → `2` |
| `24` | `M=1; M=PUL` | `LOCAL_BUTTON` = `12`; `M` = `15`; `STOP_TIME` = `60` | `24` → `2` |
| `24` | `M=1; M=SLA` | `LOCAL_BUTTON` = `12`; `M` = `11` | `24` → `2` |
| `24` | `M=2` | `FOLLOW` = `0`; `SOURCE` = `2` | `24` |
| `24` | `M=2; M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `24` → `3` |
| `24` | `M=2; M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `24` → `3` |
| `24` | `M=2; M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `24` → `3` |
| `24` | `M=2; M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `24` → `3` |
| `24` | `M=2; M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `24` → `3` |
| `24` | `M=2; M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `24` → `3` |
| `24` | `M=2; M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `24` → `3` |
| `24` | `M=2; M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `24` → `3` |
| `24` | `M=3` | `FOLLOW` = `0`; `SOURCE` = `3` | `24` |
| `24` | `M=3; M1=0` | `M` = `0` | `24` → `4` |
| `24` | `M=3; M1=1` | `M` = `1`; `T_TIME ` = `1` | `24` → `4` |
| `24` | `M=3; M1=2` | `M` = `1`; `T_TIME ` = `2` | `24` → `4` |
| `24` | `M=3; M1=3` | `M` = `1`; `T_TIME ` = `3` | `24` → `4` |
| `24` | `M=3; M1=4` | `M` = `1`; `T_TIME ` = `4` | `24` → `4` |
| `24` | `M=3; M1=5` | `M` = `1`; `T_TIME ` = `5` | `24` → `4` |
| `24` | `M=3; M1=6` | `M` = `1`; `T_TIME ` = `6` | `24` → `4` |
| `24` | `M=3; M1=7` | `M` = `1`; `T_TIME ` = `7` | `24` → `4` |
| `24` | `M=3; M1=8` | `M` = `1`; `T_TIME ` = `8` | `24` → `4` |
| `24` | `M=3; M1=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `2` | `24` → `4` |
| `24` | `M=3; M1=O/I` | `M` = `9` | `24` → `4` |
| `24` | `M=3; M1=OFF` | `M` = `10` | `24` → `4` |
| `24` | `M=3; M1=ON` | `M` = `11` | `24` → `4` |
| `24` | `M=3; M1=PUL` | `M` = `15` | `24` → `4` |
| `24` | `M=3; M1=SU_GIU` | `M` = `12` | `24` → `4` |
| `24` | `M=3; M1=SU_GIU_M` | `M` = `13` | `24` → `4` |
| `24` | `M=3; M2=0` | `M` = `0` | `24` → `4` |
| `24` | `M=3; M2=1` | `M` = `1`; `T_TIME ` = `1` | `24` → `4` |
| `24` | `M=3; M2=2` | `M` = `1`; `T_TIME ` = `2` | `24` → `4` |
| `24` | `M=3; M2=3` | `M` = `1`; `T_TIME ` = `3` | `24` → `4` |
| `24` | `M=3; M2=4` | `M` = `1`; `T_TIME ` = `4` | `24` → `4` |
| `24` | `M=3; M2=5` | `M` = `1`; `T_TIME ` = `5` | `24` → `4` |
| `24` | `M=3; M2=6` | `M` = `1`; `T_TIME ` = `6` | `24` → `4` |
| `24` | `M=3; M2=7` | `M` = `1`; `T_TIME ` = `7` | `24` → `4` |
| `24` | `M=3; M2=8` | `M` = `1`; `T_TIME ` = `8` | `24` → `4` |
| `24` | `M=3; M2=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `2` | `24` → `4` |
| `24` | `M=3; M2=O/I` | `M` = `9` | `24` → `4` |
| `24` | `M=3; M2=OFF` | `M` = `10` | `24` → `4` |
| `24` | `M=3; M2=ON` | `M` = `11` | `24` → `4` |
| `24` | `M=3; M2=PUL` | `M` = `15` | `24` → `4` |
| `24` | `M=3; M2=SU_GIU` | `M` = `12` | `24` → `4` |
| `24` | `M=3; M2=SU_GIU_M` | `M` = `13` | `24` → `4` |
| `24` | `M=4` | `FOLLOW` = `0`; `SOURCE` = `4` | `24` |
| `24` | `M=4; M1=0` | `M` = `0` | `24` → `5` |
| `24` | `M=4; M1=O/I` | `M` = `9` | `24` → `5` |
| `24` | `M=4; M1=OFF` | `M` = `10` | `24` → `5` |
| `24` | `M=4; M1=ON` | `M` = `11` | `24` → `5` |
| `24` | `M=4; M1=PUL` | `M` = `15` | `24` → `5` |
| `24` | `M=4; M1=SU_GIU` | `M` = `12` | `24` → `5` |
| `24` | `M=4; M1=SU_GIU_M` | `M` = `13` | `24` → `5` |
| `24` | `M=4; M2=0` | `M` = `0` | `24` → `5` |
| `24` | `M=4; M2=O/I` | `M` = `9` | `24` → `5` |
| `24` | `M=4; M2=OFF` | `M` = `10` | `24` → `5` |
| `24` | `M=4; M2=ON` | `M` = `11` | `24` → `5` |
| `24` | `M=4; M2=PUL` | `M` = `15` | `24` → `5` |
| `24` | `M=4; M2=SU_GIU` | `M` = `12` | `24` → `5` |
| `24` | `M=4; M2=SU_GIU_M` | `M` = `13` | `24` → `5` |
| `24` | `M=4; PL1=0` | `OUT_AUX_CHANNEL` = `0` | `24` → `5` |
| `24` | `M=4; PL1=1` | `OUT_AUX_CHANNEL` = `1` | `24` → `5` |
| `24` | `M=4; PL1=2` | `OUT_AUX_CHANNEL` = `2` | `24` → `5` |
| `24` | `M=4; PL1=3` | `OUT_AUX_CHANNEL` = `3` | `24` → `5` |
| `24` | `M=4; PL1=4` | `OUT_AUX_CHANNEL` = `4` | `24` → `5` |
| `24` | `M=4; PL1=5` | `OUT_AUX_CHANNEL` = `5` | `24` → `5` |
| `24` | `M=4; PL1=6` | `OUT_AUX_CHANNEL` = `6` | `24` → `5` |
| `24` | `M=4; PL1=7` | `OUT_AUX_CHANNEL` = `7` | `24` → `5` |
| `24` | `M=4; PL1=8` | `OUT_AUX_CHANNEL` = `8` | `24` → `5` |
| `24` | `M=4; PL1=9` | `OUT_AUX_CHANNEL` = `9` | `24` → `5` |
| `24` | `M=4; PL2=0` | `OUT_AUX_CHANNEL` = `0` | `24` → `5` |
| `24` | `M=4; PL2=1` | `OUT_AUX_CHANNEL` = `1` | `24` → `5` |
| `24` | `M=4; PL2=2` | `OUT_AUX_CHANNEL` = `2` | `24` → `5` |
| `24` | `M=4; PL2=3` | `OUT_AUX_CHANNEL` = `3` | `24` → `5` |
| `24` | `M=4; PL2=4` | `OUT_AUX_CHANNEL` = `4` | `24` → `5` |
| `24` | `M=4; PL2=5` | `OUT_AUX_CHANNEL` = `5` | `24` → `5` |
| `24` | `M=4; PL2=6` | `OUT_AUX_CHANNEL` = `6` | `24` → `5` |
| `24` | `M=4; PL2=7` | `OUT_AUX_CHANNEL` = `7` | `24` → `5` |
| `24` | `M=4; PL2=8` | `OUT_AUX_CHANNEL` = `8` | `24` → `5` |
| `24` | `M=4; PL2=9` | `OUT_AUX_CHANNEL` = `9` | `24` → `5` |
| `24` | `M=5` | `FOLLOW` = `0`; `SOURCE` = `5` | `24` |
| `24` | `M=5; M=3` | `ADDR_TYPE` = `0`; `MAIN_GROUP` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1`; `REG` = `1` | `24` → `6` |
| `24` | `M=5; M=4` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `1` | `24` → `6` |
| `24` | `M=5; M=5` | `ADDR_TYPE` = `0`; `MAIN_GROUP` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `0` | `24` → `6` |
| `24` | `M=5; M=6` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `1` | `24` → `6` |
| `24` | `M=5; M=7` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `0` | `24` → `6` |
| `24` | `M=5; M=8` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1`; `REG` = `1` | `24` → `6` |
| `24` | `M=5; S=0` | `PIR` = `0` | `24` → `6` |
| `24` | `M=5; S=1` | `PIR` = `1` | `24` → `6` |
| `24` | `M=5; S=2` | `PIR` = `2` | `24` → `6` |
| `24` | `M=5; S=3` | `PIR` = `3` | `24` → `6` |
| `24` | `M=5; T=0` | `HOURS` = `0`; `MINUTES` = `0`; `SECONDS` = `0` | `24` → `6` |
| `24` | `M=5; T=1` | `HOURS` = `0`; `MINUTES` = `0`; `SECONDS` = `30` | `24` → `6` |
| `24` | `M=5; T=2` | `HOURS` = `0`; `MINUTES` = `1`; `SECONDS` = `0` | `24` → `6` |
| `24` | `M=5; T=3` | `HOURS` = `0`; `MINUTES` = `2`; `SECONDS` = `0` | `24` → `6` |
| `24` | `M=5; T=4` | `HOURS` = `0`; `MINUTES` = `5`; `SECONDS` = `0` | `24` → `6` |
| `24` | `M=5; T=5` | `HOURS` = `0`; `MINUTES` = `10`; `SECONDS` = `0` | `24` → `6` |
| `24` | `M=5; T=6` | `HOURS` = `0`; `MINUTES` = `15`; `SECONDS` = `0` | `24` → `6` |
| `24` | `M=5; T=7` | `HOURS` = `0`; `MINUTES` = `20`; `SECONDS` = `0` | `24` → `6` |
| `24` | `M=5; T=8` | `HOURS` = `0`; `MINUTES` = `30`; `SECONDS` = `0` | `24` → `6` |
| `24` | `M=5; T=9` | `HOURS` = `0`; `MINUTES` = `40`; `SECONDS` = `0` | `24` → `6` |
| `24` | `M=5; M=0` | `ADDR_TYPE` = `0`; `MAIN_GROUP` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1` | `24` → `6` |
| `24` | `M=5; M=1` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1`; `REG` = `0` | `24` → `6` |
| `24` | `M=6` | `FOLLOW` = `0`; `SOURCE` = `6` | `24` |
| `24` | `M=6` | Referenced conversion rule absent from source | `24` → `7` |
| `24` | `M=7` | `FOLLOW` = `0`; `SOURCE` = `7` | `24` |
| `24` | `M=7` | Referenced conversion rule absent from source | `24` → `8` |
| `24` | `M=8` | `FOLLOW` = `0`; `SOURCE` = `8` | `24` |
| `24` | `M=8; M=0` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `20` | `24` → `9` |
| `24` | `M=8; M=1` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `15` | `24` → `9` |
| `24` | `M=8; M=2` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `25` | `24` → `9` |
| `24` | `M=8; M=3` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `60` | `24` → `9` |
| `24` | `M=8; M=PUL` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `15`; `STOP_TIME` = `20` | `24` → `9` |
| `24` | `M=8; M=SLA` | `LOCAL_BUTTON` = `12`; `M` = `11` | `24` → `9` |
| `24` | `M=9` | `FOLLOW` = `0`; `SOURCE` = `9` | `24` |
| `24` | `M=9; M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `24` → `10` |
| `24` | `M=9; M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `24` → `10` |
| `24` | `M=9; M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `24` → `10` |
| `24` | `M=1; L=0` | `MIN_LEVEL` = `1`; `TYPE_STANDARD` = `0` | `24` → `11` |
| `24` | `M=1; L=1` | `MIN_LEVEL` = `13`; `TYPE_STANDARD` = `0` | `24` → `11` |
| `24` | `M=1; L=2` | `MIN_LEVEL` = `25`; `TYPE_STANDARD` = `0` | `24` → `11` |
| `24` | `M=1; L=3` | `MIN_LEVEL` = `1`; `TYPE_STANDARD` = `1` | `24` → `11` |
| `24` | `M=1; L=4` | `MIN_LEVEL` = `3`; `TYPE_STANDARD` = `1` | `24` → `11` |
| `24` | `M=1; M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `24` → `11` |
| `24` | `M=1; M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `24` → `11` |
| `24` | `M=1; M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `24` → `11` |
| `24` | `M=1; M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `24` → `11` |
| `24` | `M=1; M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `24` → `11` |
| `24` | `M=1; M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `24` → `11` |
| `24` | `M=1; M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `24` → `11` |
| `24` | `M=1; TY=0` | `TYPE_LOAD` = `5` | `24` → `11` |
| `24` | `M=1; TY=1` | `TYPE_LOAD` = `6` | `24` → `11` |
| `24` | `M=2; M=1` | `DEST_LEV` = `0`; `INST_LEVEL` = `0`; `M` = `0`; `SCENARIO_BUTTON_1` = `1`; `SCENARIO_BUTTON_2` = `3` | `24` → `12` |
| `24` | `M=2; M=2` | `DEST_LEV` = `0`; `INST_LEVEL` = `0`; `M` = `0`; `SCENARIO_BUTTON_1` = `5`; `SCENARIO_BUTTON_2` = `7` | `24` → `12` |
| `24` | `M=2; M=3` | `DEST_LEV` = `0`; `INST_LEVEL` = `0`; `M` = `0`; `SCENARIO_BUTTON_1` = `9`; `SCENARIO_BUTTON_2` = `11` | `24` → `12` |
| `24` | `M=2; M=4` | `DEST_LEV` = `0`; `INST_LEVEL` = `0`; `M` = `0`; `SCENARIO_BUTTON_1` = `13`; `SCENARIO_BUTTON_2` = `15` | `24` → `12` |
| `24` | `M=2; N=0` | `DELAY_BUTTON_1` = `0`; `DELAY_BUTTON_2` = `0` | `24` → `12` |
| `24` | `M=2; N=1; DEL=0` | `DELAY_BUTTON_1` = `0` | `24` → `12` → `16` |
| `24` | `M=2; N=1; DEL=1` | `DELAY_BUTTON_1` = `60` | `24` → `12` → `16` |
| `24` | `M=2; N=1; DEL=2` | `DELAY_BUTTON_1` = `62` | `24` → `12` → `16` |
| `24` | `M=2; N=1; DEL=3` | `DELAY_BUTTON_1` = `63` | `24` → `12` → `16` |
| `24` | `M=2; N=1; DEL=4` | `DELAY_BUTTON_1` = `64` | `24` → `12` → `16` |
| `24` | `M=2; N=1; DEL=5` | `DELAY_BUTTON_1` = `65` | `24` → `12` → `16` |
| `24` | `M=2; N=1; DEL=6` | `DELAY_BUTTON_1` = `70` | `24` → `12` → `16` |
| `24` | `M=2; N=1; DEL=7` | `DELAY_BUTTON_1` = `71` | `24` → `12` → `16` |
| `24` | `M=2; N=1; DEL=8` | `DELAY_BUTTON_1` = `15` | `24` → `12` → `16` |
| `24` | `M=2; N=1; DEL=9` | `DELAY_BUTTON_1` = `30` | `24` → `12` → `16` |
| `24` | `M=2; N=1` | `DELAY_BUTTON_2` = `0` | `24` → `12` |
| `24` | `M=2; N=2` | `DELAY_BUTTON_1` = `0`; `DELAY_BUTTON_2` = `0` | `24` → `12` |
| `24` | `M=2; N=3` | `DELAY_BUTTON_1` = `0` | `24` → `12` |
| `24` | `M=2; N=3; DEL=0` | `DELAY_BUTTON_2` = `0` | `24` → `12` → `19` |
| `24` | `M=2; N=3; DEL=1` | `DELAY_BUTTON_2` = `60` | `24` → `12` → `19` |
| `24` | `M=2; N=3; DEL=2` | `DELAY_BUTTON_2` = `62` | `24` → `12` → `19` |
| `24` | `M=2; N=3; DEL=3` | `DELAY_BUTTON_2` = `63` | `24` → `12` → `19` |
| `24` | `M=2; N=3; DEL=4` | `DELAY_BUTTON_2` = `64` | `24` → `12` → `19` |
| `24` | `M=2; N=3; DEL=5` | `DELAY_BUTTON_2` = `65` | `24` → `12` → `19` |
| `24` | `M=2; N=3; DEL=6` | `DELAY_BUTTON_2` = `70` | `24` → `12` → `19` |
| `24` | `M=2; N=3; DEL=7` | `DELAY_BUTTON_2` = `71` | `24` → `12` → `19` |
| `24` | `M=2; N=3; DEL=8` | `DELAY_BUTTON_2` = `15` | `24` → `12` → `19` |
| `24` | `M=2; N=3; DEL=9` | `DELAY_BUTTON_2` = `30` | `24` → `12` → `19` |
| `24` | `M=2; N=4` | `DELAY_BUTTON_1` = `0`; `DELAY_BUTTON_2` = `0` | `24` → `12` |
| `24` | `M=2; N=5; DEL=0` | `DELAY_BUTTON_1` = `0` | `24` → `12` → `16` |
| `24` | `M=2; N=5; DEL=1` | `DELAY_BUTTON_1` = `60` | `24` → `12` → `16` |
| `24` | `M=2; N=5; DEL=2` | `DELAY_BUTTON_1` = `62` | `24` → `12` → `16` |
| `24` | `M=2; N=5; DEL=3` | `DELAY_BUTTON_1` = `63` | `24` → `12` → `16` |
| `24` | `M=2; N=5; DEL=4` | `DELAY_BUTTON_1` = `64` | `24` → `12` → `16` |
| `24` | `M=2; N=5; DEL=5` | `DELAY_BUTTON_1` = `65` | `24` → `12` → `16` |
| `24` | `M=2; N=5; DEL=6` | `DELAY_BUTTON_1` = `70` | `24` → `12` → `16` |
| `24` | `M=2; N=5; DEL=7` | `DELAY_BUTTON_1` = `71` | `24` → `12` → `16` |
| `24` | `M=2; N=5; DEL=8` | `DELAY_BUTTON_1` = `15` | `24` → `12` → `16` |
| `24` | `M=2; N=5; DEL=9` | `DELAY_BUTTON_1` = `30` | `24` → `12` → `16` |
| `24` | `M=2; N=5; DEL=0` | `DELAY_BUTTON_2` = `0` | `24` → `12` → `19` |
| `24` | `M=2; N=5; DEL=1` | `DELAY_BUTTON_2` = `60` | `24` → `12` → `19` |
| `24` | `M=2; N=5; DEL=2` | `DELAY_BUTTON_2` = `62` | `24` → `12` → `19` |
| `24` | `M=2; N=5; DEL=3` | `DELAY_BUTTON_2` = `63` | `24` → `12` → `19` |
| `24` | `M=2; N=5; DEL=4` | `DELAY_BUTTON_2` = `64` | `24` → `12` → `19` |
| `24` | `M=2; N=5; DEL=5` | `DELAY_BUTTON_2` = `65` | `24` → `12` → `19` |
| `24` | `M=2; N=5; DEL=6` | `DELAY_BUTTON_2` = `70` | `24` → `12` → `19` |
| `24` | `M=2; N=5; DEL=7` | `DELAY_BUTTON_2` = `71` | `24` → `12` → `19` |
| `24` | `M=2; N=5; DEL=8` | `DELAY_BUTTON_2` = `15` | `24` → `12` → `19` |
| `24` | `M=2; N=5; DEL=9` | `DELAY_BUTTON_2` = `30` | `24` → `12` → `19` |
| `24` | `M=3; M=1` | `DEST_LEV` = `0`; `INST_LEVEL` = `0`; `M` = `0`; `SCENARIO_BUTTON_1` = `2`; `SCENARIO_BUTTON_2` = `4` | `24` → `13` |
| `24` | `M=3; M=2` | `DEST_LEV` = `0`; `INST_LEVEL` = `0`; `M` = `0`; `SCENARIO_BUTTON_1` = `6`; `SCENARIO_BUTTON_2` = `8` | `24` → `13` |
| `24` | `M=3; M=3` | `DEST_LEV` = `0`; `INST_LEVEL` = `0`; `M` = `0`; `SCENARIO_BUTTON_1` = `10`; `SCENARIO_BUTTON_2` = `12` | `24` → `13` |
| `24` | `M=3; M=4` | `DEST_LEV` = `0`; `INST_LEVEL` = `0`; `M` = `0`; `SCENARIO_BUTTON_1` = `14`; `SCENARIO_BUTTON_2` = `16` | `24` → `13` |
| `24` | `M=3; N=0` | `DELAY_BUTTON_1` = `0`; `DELAY_BUTTON_2` = `0` | `24` → `13` |
| `24` | `M=3; N=1` | `DELAY_BUTTON_1` = `0`; `DELAY_BUTTON_2` = `0` | `24` → `13` |
| `24` | `M=3; N=2; DEL=0` | `DELAY_BUTTON_1` = `0` | `24` → `13` → `16` |
| `24` | `M=3; N=2; DEL=1` | `DELAY_BUTTON_1` = `60` | `24` → `13` → `16` |
| `24` | `M=3; N=2; DEL=2` | `DELAY_BUTTON_1` = `62` | `24` → `13` → `16` |
| `24` | `M=3; N=2; DEL=3` | `DELAY_BUTTON_1` = `63` | `24` → `13` → `16` |
| `24` | `M=3; N=2; DEL=4` | `DELAY_BUTTON_1` = `64` | `24` → `13` → `16` |
| `24` | `M=3; N=2; DEL=5` | `DELAY_BUTTON_1` = `65` | `24` → `13` → `16` |
| `24` | `M=3; N=2; DEL=6` | `DELAY_BUTTON_1` = `70` | `24` → `13` → `16` |
| `24` | `M=3; N=2; DEL=7` | `DELAY_BUTTON_1` = `71` | `24` → `13` → `16` |
| `24` | `M=3; N=2; DEL=8` | `DELAY_BUTTON_1` = `15` | `24` → `13` → `16` |
| `24` | `M=3; N=2; DEL=9` | `DELAY_BUTTON_1` = `30` | `24` → `13` → `16` |
| `24` | `M=3; N=2` | `DELAY_BUTTON_2` = `0` | `24` → `13` |
| `24` | `M=3; N=3` | `DELAY_BUTTON_1` = `0`; `DELAY_BUTTON_2` = `0` | `24` → `13` |
| `24` | `M=3; N=4` | `DELAY_BUTTON_1` = `0` | `24` → `13` |
| `24` | `M=3; N=4; DEL=0` | `DELAY_BUTTON_2` = `0` | `24` → `13` → `19` |
| `24` | `M=3; N=4; DEL=1` | `DELAY_BUTTON_2` = `60` | `24` → `13` → `19` |
| `24` | `M=3; N=4; DEL=2` | `DELAY_BUTTON_2` = `62` | `24` → `13` → `19` |
| `24` | `M=3; N=4; DEL=3` | `DELAY_BUTTON_2` = `63` | `24` → `13` → `19` |
| `24` | `M=3; N=4; DEL=4` | `DELAY_BUTTON_2` = `64` | `24` → `13` → `19` |
| `24` | `M=3; N=4; DEL=5` | `DELAY_BUTTON_2` = `65` | `24` → `13` → `19` |
| `24` | `M=3; N=4; DEL=6` | `DELAY_BUTTON_2` = `70` | `24` → `13` → `19` |
| `24` | `M=3; N=4; DEL=7` | `DELAY_BUTTON_2` = `71` | `24` → `13` → `19` |
| `24` | `M=3; N=4; DEL=8` | `DELAY_BUTTON_2` = `15` | `24` → `13` → `19` |
| `24` | `M=3; N=4; DEL=9` | `DELAY_BUTTON_2` = `30` | `24` → `13` → `19` |
| `24` | `M=3; N=5; DEL=0` | `DELAY_BUTTON_1` = `0` | `24` → `13` → `16` |
| `24` | `M=3; N=5; DEL=1` | `DELAY_BUTTON_1` = `60` | `24` → `13` → `16` |
| `24` | `M=3; N=5; DEL=2` | `DELAY_BUTTON_1` = `62` | `24` → `13` → `16` |
| `24` | `M=3; N=5; DEL=3` | `DELAY_BUTTON_1` = `63` | `24` → `13` → `16` |
| `24` | `M=3; N=5; DEL=4` | `DELAY_BUTTON_1` = `64` | `24` → `13` → `16` |
| `24` | `M=3; N=5; DEL=5` | `DELAY_BUTTON_1` = `65` | `24` → `13` → `16` |
| `24` | `M=3; N=5; DEL=6` | `DELAY_BUTTON_1` = `70` | `24` → `13` → `16` |
| `24` | `M=3; N=5; DEL=7` | `DELAY_BUTTON_1` = `71` | `24` → `13` → `16` |
| `24` | `M=3; N=5; DEL=8` | `DELAY_BUTTON_1` = `15` | `24` → `13` → `16` |
| `24` | `M=3; N=5; DEL=9` | `DELAY_BUTTON_1` = `30` | `24` → `13` → `16` |
| `24` | `M=3; N=5; DEL=0` | `DELAY_BUTTON_2` = `0` | `24` → `13` → `19` |
| `24` | `M=3; N=5; DEL=1` | `DELAY_BUTTON_2` = `60` | `24` → `13` → `19` |
| `24` | `M=3; N=5; DEL=2` | `DELAY_BUTTON_2` = `62` | `24` → `13` → `19` |
| `24` | `M=3; N=5; DEL=3` | `DELAY_BUTTON_2` = `63` | `24` → `13` → `19` |
| `24` | `M=3; N=5; DEL=4` | `DELAY_BUTTON_2` = `64` | `24` → `13` → `19` |
| `24` | `M=3; N=5; DEL=5` | `DELAY_BUTTON_2` = `65` | `24` → `13` → `19` |
| `24` | `M=3; N=5; DEL=6` | `DELAY_BUTTON_2` = `70` | `24` → `13` → `19` |
| `24` | `M=3; N=5; DEL=7` | `DELAY_BUTTON_2` = `71` | `24` → `13` → `19` |
| `24` | `M=3; N=5; DEL=8` | `DELAY_BUTTON_2` = `15` | `24` → `13` → `19` |
| `24` | `M=3; N=5; DEL=9` | `DELAY_BUTTON_2` = `30` | `24` → `13` → `19` |
| `24` | `M=4` | Referenced conversion rule absent from source | `24` → `14` |
| `24` | `M=5` | Referenced conversion rule absent from source | `24` → `15` |
| `24` | `M=6; DEL=0` | `DELAY_BUTTON_1` = `0` | `24` → `16` |
| `24` | `M=6; DEL=1` | `DELAY_BUTTON_1` = `60` | `24` → `16` |
| `24` | `M=6; DEL=2` | `DELAY_BUTTON_1` = `62` | `24` → `16` |
| `24` | `M=6; DEL=3` | `DELAY_BUTTON_1` = `63` | `24` → `16` |
| `24` | `M=6; DEL=4` | `DELAY_BUTTON_1` = `64` | `24` → `16` |
| `24` | `M=6; DEL=5` | `DELAY_BUTTON_1` = `65` | `24` → `16` |
| `24` | `M=6; DEL=6` | `DELAY_BUTTON_1` = `70` | `24` → `16` |
| `24` | `M=6; DEL=7` | `DELAY_BUTTON_1` = `71` | `24` → `16` |
| `24` | `M=6; DEL=8` | `DELAY_BUTTON_1` = `15` | `24` → `16` |
| `24` | `M=6; DEL=9` | `DELAY_BUTTON_1` = `30` | `24` → `16` |
| `24` | `M=7; M1=CEN` | `IN_AUX_CHANNEL` = `0`; `CEN_BUTT_1` = `1`; `CEN_BUTT_2` = `3` | `24` → `17` |
| `24` | `M=8; M2=CEN` | `IN_AUX_CHANNEL` = `0`; `CEN_BUTT_1` = `2`; `CEN_BUTT_2` = `4` | `24` → `18` |
| `24` | `M=9; DEL=0` | `DELAY_BUTTON_2` = `0` | `24` → `19` |
| `24` | `M=9; DEL=1` | `DELAY_BUTTON_2` = `60` | `24` → `19` |
| `24` | `M=9; DEL=2` | `DELAY_BUTTON_2` = `62` | `24` → `19` |
| `24` | `M=9; DEL=3` | `DELAY_BUTTON_2` = `63` | `24` → `19` |
| `24` | `M=9; DEL=4` | `DELAY_BUTTON_2` = `64` | `24` → `19` |
| `24` | `M=9; DEL=5` | `DELAY_BUTTON_2` = `65` | `24` → `19` |
| `24` | `M=9; DEL=6` | `DELAY_BUTTON_2` = `70` | `24` → `19` |
| `24` | `M=9; DEL=7` | `DELAY_BUTTON_2` = `71` | `24` → `19` |
| `24` | `M=9; DEL=8` | `DELAY_BUTTON_2` = `15` | `24` → `19` |
| `24` | `M=9; DEL=9` | `DELAY_BUTTON_2` = `30` | `24` → `19` |
| `30` | `I=0` | `INST_LEV` = `1`; `DEST_LEV` = `1` | `30` |
| `30` | `I=1` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `30` |
| `30` | `I=2` | `INST_LEV` = `3`; `DEST_LEV` = `2` | `30` |
| `30` | `I=3` | `INST_LEV` = `4`; `DEST_LEV` = `3` | `30` |
| `30` | `I=4` | `INST_LEV` = `5`; `DEST_LEV` = `4` | `30` |
| `30` | `I=5` | `INST_LEV` = `6`; `DEST_LEV` = `5` | `30` |
| `30` | `I=6` | `INST_LEV` = `7`; `DEST_LEV` = `6` | `30` |
| `30` | `I=7` | `INST_LEV` = `8`; `DEST_LEV` = `7` | `30` |
| `30` | `I=8` | `INST_LEV` = `9`; `DEST_LEV` = `8` | `30` |
| `30` | `I=9` | `INST_LEV` = `10`; `DEST_LEV` = `9` | `30` |
| `30` | `I=CEN` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `30` |
| `30` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `30` |
| `30` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `30` |
| `30` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `30` |
| `30` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `30` |
| `30` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `30` |
| `30` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `30` |
| `30` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `30` |
| `30` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `30` |
| `30` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `30` |
| `30` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `30` |
| `30` | `M=0` | `M` = `0` | `30` |
| `30` | `M=1` | `M` = `1`; `T_TIME ` = `1` | `30` |
| `30` | `M=2` | `M` = `1`; `T_TIME ` = `2` | `30` |
| `30` | `M=3` | `M` = `1`; `T_TIME ` = `3` | `30` |
| `30` | `M=4` | `M` = `1`; `T_TIME ` = `4` | `30` |
| `30` | `M=5` | `M` = `1`; `T_TIME ` = `5` | `30` |
| `30` | `M=6` | `M` = `1`; `T_TIME ` = `6` | `30` |
| `30` | `M=7` | `M` = `1`; `T_TIME ` = `7` | `30` |
| `30` | `M=8` | `M` = `1`; `T_TIME ` = `8` | `30` |
| `30` | `M=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `2` | `30` |
| `30` | `M=O/I` | `M` = `9` | `30` |
| `30` | `M=OFF` | `M` = `10` | `30` |
| `30` | `M=ON` | `M` = `11` | `30` |
| `30` | `M=PUL` | `M` = `15` | `30` |
| `30` | `M=SU_GIU` | `M` = `12` | `30` |
| `30` | `M=SU_GIU_M` | `M` = `13` | `30` |
| `34` | `I=0` | `INST_LEV` = `1`; `DEST_LEV` = `1` | `34` |
| `34` | `I=1` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `34` |
| `34` | `I=2` | `INST_LEV` = `3`; `DEST_LEV` = `2` | `34` |
| `34` | `I=3` | `INST_LEV` = `4`; `DEST_LEV` = `3` | `34` |
| `34` | `I=4` | `INST_LEV` = `5`; `DEST_LEV` = `4` | `34` |
| `34` | `I=5` | `INST_LEV` = `6`; `DEST_LEV` = `5` | `34` |
| `34` | `I=6` | `INST_LEV` = `7`; `DEST_LEV` = `6` | `34` |
| `34` | `I=7` | `INST_LEV` = `8`; `DEST_LEV` = `7` | `34` |
| `34` | `I=8` | `INST_LEV` = `9`; `DEST_LEV` = `8` | `34` |
| `34` | `I=9` | `INST_LEV` = `10`; `DEST_LEV` = `9` | `34` |
| `34` | `I=CEN` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `34` |
| `34` | `M=1` | `M` = `0`; `SCENARIO_BUTTON_1` = `1`; `SCENARIO_BUTTON_2` = `3` | `34` |
| `34` | `M=2` | `M` = `0`; `SCENARIO_BUTTON_1` = `5`; `SCENARIO_BUTTON_2` = `7` | `34` |
| `34` | `M=3` | `M` = `0`; `SCENARIO_BUTTON_1` = `9`; `SCENARIO_BUTTON_2` = `11` | `34` |
| `34` | `M=4` | `M` = `0`; `SCENARIO_BUTTON_1` = `13`; `SCENARIO_BUTTON_2` = `15` | `34` |
| `35` | `I=0` | `INST_LEV` = `1`; `DEST_LEV` = `1` | `35` |
| `35` | `I=1` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `35` |
| `35` | `I=2` | `INST_LEV` = `3`; `DEST_LEV` = `2` | `35` |
| `35` | `I=3` | `INST_LEV` = `4`; `DEST_LEV` = `3` | `35` |
| `35` | `I=4` | `INST_LEV` = `5`; `DEST_LEV` = `4` | `35` |
| `35` | `I=5` | `INST_LEV` = `6`; `DEST_LEV` = `5` | `35` |
| `35` | `I=6` | `INST_LEV` = `7`; `DEST_LEV` = `6` | `35` |
| `35` | `I=7` | `INST_LEV` = `8`; `DEST_LEV` = `7` | `35` |
| `35` | `I=8` | `INST_LEV` = `9`; `DEST_LEV` = `8` | `35` |
| `35` | `I=9` | `INST_LEV` = `10`; `DEST_LEV` = `9` | `35` |
| `35` | `I=CEN` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `35` |
| `35` | `M=1` | `M` = `0`; `SCENARIO_BUTTON_1` = `2`; `SCENARIO_BUTTON_2` = `4` | `35` |
| `35` | `M=2` | `M` = `0`; `SCENARIO_BUTTON_1` = `6`; `SCENARIO_BUTTON_2` = `8` | `35` |
| `35` | `M=3` | `M` = `0`; `SCENARIO_BUTTON_1` = `10`; `SCENARIO_BUTTON_2` = `12` | `35` |
| `35` | `M=4` | `M` = `0`; `SCENARIO_BUTTON_1` = `14`; `SCENARIO_BUTTON_2` = `16` | `35` |
| `36` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `36` |
| `36` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `36` |
| `36` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `36` |
| `36` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `36` |
| `36` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `36` |
| `36` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `36` |
| `36` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `36` |
| `36` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `36` |
| `36` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `36` |
| `36` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `36` |
| `36` | `M=0` | `M` = `0` | `36` |
| `36` | `M=O/I` | `M` = `9` | `36` |
| `36` | `M=OFF` | `M` = `10` | `36` |
| `36` | `M=ON` | `M` = `11` | `36` |
| `36` | `M=PUL` | `M` = `15` | `36` |
| `36` | `M=SU_GIU` | `M` = `12` | `36` |
| `36` | `M=SU_GIU_M` | `M` = `13` | `36` |
| `37` | `I=0` | `INST_LEV` = `1`; `DEST_LEV` = `1` | `37` |
| `37` | `I=1` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `37` |
| `37` | `I=2` | `INST_LEV` = `3`; `DEST_LEV` = `2` | `37` |
| `37` | `I=3` | `INST_LEV` = `4`; `DEST_LEV` = `3` | `37` |
| `37` | `I=4` | `INST_LEV` = `5`; `DEST_LEV` = `4` | `37` |
| `37` | `I=5` | `INST_LEV` = `6`; `DEST_LEV` = `5` | `37` |
| `37` | `I=6` | `INST_LEV` = `7`; `DEST_LEV` = `6` | `37` |
| `37` | `I=7` | `INST_LEV` = `8`; `DEST_LEV` = `7` | `37` |
| `37` | `I=8` | `INST_LEV` = `9`; `DEST_LEV` = `8` | `37` |
| `37` | `I=9` | `INST_LEV` = `10`; `DEST_LEV` = `9` | `37` |
| `37` | `I=CEN` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `37` |
| `37` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `37` |
| `37` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `37` |
| `37` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `37` |
| `37` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `37` |
| `37` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `37` |
| `37` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `37` |
| `37` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `37` |
| `37` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `37` |
| `37` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `37` |
| `37` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `37` |
| `37` | `M=1` | `M` = `1` | `37` |
| `37` | `M=2` | `M` = `2` | `37` |
| `37` | `M=3` | `M` = `3` | `37` |
| `38` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `38` |
| `38` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `38` |
| `38` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `38` |
| `38` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `38` |
| `38` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `38` |
| `38` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `38` |
| `38` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `38` |
| `38` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `38` |
| `38` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `38` |
| `38` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `38` |
| `38` | `M=1` | `M` = `1` | `38` |
| `38` | `M=2` | `M` = `2` | `38` |
| `38` | `M=3` | `M` = `3` | `38` |
| `38` | `M=4` | `M` = `4` | `38` |
| `38` | `M=5` | `M` = `5` | `38` |
| `38` | `M=6` | `M` = `6` | `38` |
| `38` | `M=7` | `M` = `1`; `T_TIME ` = `9` | `38` |
| `38` | `M=8` | `M` = `1`; `T_TIME ` = `10` | `38` |
| `39` | `I=0` | `INST_LEV` = `1`; `DEST_LEV` = `1` | `39` |
| `39` | `I=1` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `39` |
| `39` | `I=2` | `INST_LEV` = `3`; `DEST_LEV` = `2` | `39` |
| `39` | `I=3` | `INST_LEV` = `4`; `DEST_LEV` = `3` | `39` |
| `39` | `I=4` | `INST_LEV` = `5`; `DEST_LEV` = `4` | `39` |
| `39` | `I=5` | `INST_LEV` = `6`; `DEST_LEV` = `5` | `39` |
| `39` | `I=6` | `INST_LEV` = `7`; `DEST_LEV` = `6` | `39` |
| `39` | `I=7` | `INST_LEV` = `8`; `DEST_LEV` = `7` | `39` |
| `39` | `I=8` | `INST_LEV` = `9`; `DEST_LEV` = `8` | `39` |
| `39` | `I=9` | `INST_LEV` = `10`; `DEST_LEV` = `9` | `39` |
| `39` | `I=CEN` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `39` |
| `39` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `39` |
| `39` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `39` |
| `39` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `39` |
| `39` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `39` |
| `39` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `39` |
| `39` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `39` |
| `39` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `39` |
| `39` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `39` |
| `39` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `39` |
| `39` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `39` |
| `39` | `M=0` | `M` = `32` | `39` |
| `39` | `M=1` | `M` = `33` | `39` |
| `39` | `M=2` | `M` = `34` | `39` |
| `39` | `M=3` | `M` = `35` | `39` |
| `39` | `M=4` | `M` = `36` | `39` |
| `39` | `M=5` | `M` = `37` | `39` |
| `39` | `M=6` | `M` = `38` | `39` |
| `39` | `M=7` | `M` = `39` | `39` |
| `39` | `M=8` | `M` = `40` | `39` |
| `39` | `M=9` | `M` = `41` | `39` |
| `39` | `M=10` | `M` = `42` | `39` |
| `39` | `M=11` | `M` = `43` | `39` |
| `39` | `M=12` | `M` = `44` | `39` |
| `39` | `M=13` | `M` = `45` | `39` |
| `39` | `M=14` | `M` = `46` | `39` |
| `39` | `M=15` | `M` = `47` | `39` |
| `40` | `I=0` | `INST_LEV` = `1`; `DEST_LEV` = `1` | `40` |
| `40` | `I=1` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `40` |
| `40` | `I=2` | `INST_LEV` = `3`; `DEST_LEV` = `2` | `40` |
| `40` | `I=3` | `INST_LEV` = `4`; `DEST_LEV` = `3` | `40` |
| `40` | `I=4` | `INST_LEV` = `5`; `DEST_LEV` = `5` | `40` |
| `40` | `I=5` | `INST_LEV` = `6`; `DEST_LEV` = `5` | `40` |
| `40` | `I=6` | `INST_LEV` = `7`; `DEST_LEV` = `6` | `40` |
| `40` | `I=7` | `INST_LEV` = `8`; `DEST_LEV` = `7` | `40` |
| `40` | `I=8` | `INST_LEV` = `9`; `DEST_LEV` = `8` | `40` |
| `40` | `I=9` | `INST_LEV` = `10`; `DEST_LEV` = `9` | `40` |
| `40` | `I=CEN` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `40` |
| `40` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `40` |
| `40` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `40` |
| `40` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `40` |
| `40` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `40` |
| `40` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `40` |
| `40` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `40` |
| `40` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `40` |
| `40` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `40` |
| `40` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `40` |
| `40` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `40` |
| `40` | `M=0` | `M` = `49` | `40` |
| `40` | `M=1` | `M` = `50` | `40` |
| `40` | `M=2` | `M` = `51` | `40` |
| `40` | `M=3` | `M` = `52` | `40` |
| `40` | `M=4` | `M` = `53` | `40` |
| `40` | `M=5` | `M` = `54` | `40` |
| `40` | `M=6` | `M` = `55` | `40` |
| `40` | `M=7` | `M` = `56` | `40` |
| `40` | `M=8` | `M` = `57` | `40` |
| `40` | `M=9` | `M` = `58` | `40` |
| `41` | `M=1` | `M` = `1`; `SCENARIO_BUTTON_1` = `1`; `SCENARIO_BUTTON_2` = `1` | `41` |
| `41` | `M=2` | `M` = `1`; `SCENARIO_BUTTON_1` = `2`; `SCENARIO_BUTTON_2` = `2` | `41` |
| `41` | `M=3` | `M` = `1`; `SCENARIO_BUTTON_1` = `3`; `SCENARIO_BUTTON_2` = `3` | `41` |
| `41` | `M=4` | `M` = `1`; `SCENARIO_BUTTON_1` = `4`; `SCENARIO_BUTTON_2` = `4` | `41` |
| `41` | `M=5` | `M` = `1`; `SCENARIO_BUTTON_1` = `5`; `SCENARIO_BUTTON_2` = `5` | `41` |
| `41` | `M=6` | `M` = `1`; `SCENARIO_BUTTON_1` = `6`; `SCENARIO_BUTTON_2` = `6` | `41` |
| `41` | `M=7` | `M` = `1`; `SCENARIO_BUTTON_1` = `7`; `SCENARIO_BUTTON_2` = `7` | `41` |
| `41` | `M=8` | `M` = `1`; `SCENARIO_BUTTON_1` = `8`; `SCENARIO_BUTTON_2` = `8` | `41` |
| `41` | `M=9` | `M` = `1`; `SCENARIO_BUTTON_1` = `9`; `SCENARIO_BUTTON_2` = `9` | `41` |
| `41` | `I=0` | `INST_LEV` = `1`; `DEST_LEV` = `1` | `41` |
| `41` | `I=1` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `41` |
| `41` | `I=2` | `INST_LEV` = `3`; `DEST_LEV` = `2` | `41` |
| `41` | `I=3` | `INST_LEV` = `4`; `DEST_LEV` = `3` | `41` |
| `41` | `I=4` | `INST_LEV` = `5`; `DEST_LEV` = `4` | `41` |
| `41` | `I=5` | `INST_LEV` = `6`; `DEST_LEV` = `5` | `41` |
| `41` | `I=6` | `INST_LEV` = `7`; `DEST_LEV` = `6` | `41` |
| `41` | `I=7` | `INST_LEV` = `8`; `DEST_LEV` = `7` | `41` |
| `41` | `I=8` | `INST_LEV` = `9`; `DEST_LEV` = `8` | `41` |
| `41` | `I=9` | `INST_LEV` = `10`; `DEST_LEV` = `9` | `41` |
| `41` | `I=CEN` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `41` |
| `42` | `I=0` | `INST_LEV` = `1`; `DEST_LEV` = `1` | `42` |
| `42` | `I=1` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `42` |
| `42` | `I=2` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `42` |
| `42` | `I=3` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `42` |
| `42` | `I=4` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `42` |
| `42` | `I=5` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `42` |
| `42` | `I=6` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `42` |
| `42` | `I=7` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `42` |
| `42` | `I=8` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `42` |
| `42` | `I=9` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `42` |
| `42` | `I=CEN` | `INST_LEV` = `0`; `DEST_LEV` = `1` | `42` |
| `42` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `42` |
| `42` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `42` |
| `42` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `42` |
| `42` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `42` |
| `42` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `42` |
| `42` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `42` |
| `42` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `42` |
| `42` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `42` |
| `42` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `42` |
| `42` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `42` |
| `42` | `SPE=ON` | `M` = `128`; `HOURS` = `0` | `42` |
| `42` | `LIV2=0` | `SECONDS` = `0` | `42` |
| `42` | `LIV2=1` | `SECONDS` = `5` | `42` |
| `42` | `LIV2=2` | `SECONDS` = `10` | `42` |
| `42` | `LIV2=3` | `SECONDS` = `15` | `42` |
| `42` | `LIV2=4` | `SECONDS` = `20` | `42` |
| `42` | `LIV2=5` | `SECONDS` = `25` | `42` |
| `42` | `LIV2=6` | `SECONDS` = `30` | `42` |
| `42` | `LIV2=7` | `SECONDS` = `35` | `42` |
| `42` | `LIV2=8` | `SECONDS` = `40` | `42` |
| `42` | `LIV2=9` | `SECONDS` = `45` | `42` |
| `42` | `M=0; LIV1=0` | `LEVEL` = `0` | `42` → `55` |
| `42` | `M=0; LIV1=1` | `LEVEL` = `1` | `42` → `55` |
| `42` | `M=0; LIV1=2` | `LEVEL` = `2` | `42` → `55` |
| `42` | `M=0; LIV1=3` | `LEVEL` = `3` | `42` → `55` |
| `42` | `M=0; LIV1=4` | `LEVEL` = `4` | `42` → `55` |
| `42` | `M=0; LIV1=5` | `LEVEL` = `5` | `42` → `55` |
| `42` | `M=0; LIV1=6` | `LEVEL` = `6` | `42` → `55` |
| `42` | `M=0; LIV1=7` | `LEVEL` = `7` | `42` → `55` |
| `42` | `M=0; LIV1=8` | `LEVEL` = `8` | `42` → `55` |
| `42` | `M=0; LIV1=9` | `LEVEL` = `9` | `42` → `55` |
| `42` | `M=1; LIV1=7` | `LEVEL` = `17` | `42` → `56` |
| `42` | `M=1; LIV1=8` | `LEVEL` = `18` | `42` → `56` |
| `42` | `M=1; LIV1=9` | `LEVEL` = `19` | `42` → `56` |
| `42` | `M=1; LIV1=0` | `LEVEL` = `10` | `42` → `56` |
| `42` | `M=1; LIV1=1` | `LEVEL` = `11` | `42` → `56` |
| `42` | `M=1; LIV1=2` | `LEVEL` = `12` | `42` → `56` |
| `42` | `M=1; LIV1=3` | `LEVEL` = `13` | `42` → `56` |
| `42` | `M=1; LIV1=4` | `LEVEL` = `14` | `42` → `56` |
| `42` | `M=1; LIV1=5` | `LEVEL` = `15` | `42` → `56` |
| `42` | `M=1; LIV1=6` | `LEVEL` = `16` | `42` → `56` |
| `42` | `M=2; LIV1=0` | `LEVEL` = `20` | `42` → `57` |
| `42` | `M=2; LIV1=1` | `LEVEL` = `21` | `42` → `57` |
| `42` | `M=2; LIV1=2` | `LEVEL` = `22` | `42` → `57` |
| `42` | `M=2; LIV1=3` | `LEVEL` = `23` | `42` → `57` |
| `42` | `M=2; LIV1=4` | `LEVEL` = `24` | `42` → `57` |
| `42` | `M=2; LIV1=5` | `LEVEL` = `25` | `42` → `57` |
| `42` | `M=2; LIV1=6` | `LEVEL` = `26` | `42` → `57` |
| `42` | `M=2; LIV1=7` | `LEVEL` = `27` | `42` → `57` |
| `42` | `M=2; LIV1=8` | `LEVEL` = `28` | `42` → `57` |
| `42` | `M=2; LIV1=9` | `LEVEL` = `29` | `42` → `57` |
| `42` | `M=3; LIV1=0` | `LEVEL` = `30` | `42` → `58` |
| `42` | `M=3; LIV1=1` | `LEVEL` = `31` | `42` → `58` |
| `42` | `M=3; LIV1=2` | `LEVEL` = `32` | `42` → `58` |
| `42` | `M=3; LIV1=3` | `LEVEL` = `33` | `42` → `58` |
| `42` | `M=3; LIV1=4` | `LEVEL` = `34` | `42` → `58` |
| `42` | `M=3; LIV1=5` | `LEVEL` = `35` | `42` → `58` |
| `42` | `M=3; LIV1=6` | `LEVEL` = `36` | `42` → `58` |
| `42` | `M=3; LIV1=7` | `LEVEL` = `37` | `42` → `58` |
| `42` | `M=3; LIV1=8` | `LEVEL` = `38` | `42` → `58` |
| `42` | `M=3; LIV1=9` | `LEVEL` = `39` | `42` → `58` |
| `42` | `M=4; LIV1=0` | `LEVEL` = `40` | `42` → `59` |
| `42` | `M=4; LIV1=1` | `LEVEL` = `41` | `42` → `59` |
| `42` | `M=4; LIV1=2` | `LEVEL` = `42` | `42` → `59` |
| `42` | `M=4; LIV1=3` | `LEVEL` = `43` | `42` → `59` |
| `42` | `M=4; LIV1=4` | `LEVEL` = `44` | `42` → `59` |
| `42` | `M=4; LIV1=5` | `LEVEL` = `45` | `42` → `59` |
| `42` | `M=4; LIV1=6` | `LEVEL` = `46` | `42` → `59` |
| `42` | `M=4; LIV1=7` | `LEVEL` = `47` | `42` → `59` |
| `42` | `M=4; LIV1=8` | `LEVEL` = `48` | `42` → `59` |
| `42` | `M=4; LIV1=9` | `LEVEL` = `49` | `42` → `59` |
| `42` | `M=5; LIV1=0` | `LEVEL` = `50` | `42` → `60` |
| `42` | `M=5; LIV1=1` | `LEVEL` = `51` | `42` → `60` |
| `42` | `M=5; LIV1=2` | `LEVEL` = `52` | `42` → `60` |
| `42` | `M=5; LIV1=3` | `LEVEL` = `53` | `42` → `60` |
| `42` | `M=5; LIV1=4` | `LEVEL` = `54` | `42` → `60` |
| `42` | `M=5; LIV1=5` | `LEVEL` = `55` | `42` → `60` |
| `42` | `M=5; LIV1=6` | `LEVEL` = `56` | `42` → `60` |
| `42` | `M=5; LIV1=7` | `LEVEL` = `57` | `42` → `60` |
| `42` | `M=5; LIV1=8` | `LEVEL` = `58` | `42` → `60` |
| `42` | `M=5; LIV1=9` | `LEVEL` = `59` | `42` → `60` |
| `42` | `M=6; LIV1=0` | `LEVEL` = `60` | `42` → `61` |
| `42` | `M=6; LIV1=1` | `LEVEL` = `61` | `42` → `61` |
| `42` | `M=6; LIV1=2` | `LEVEL` = `62` | `42` → `61` |
| `42` | `M=6; LIV1=3` | `LEVEL` = `63` | `42` → `61` |
| `42` | `M=6; LIV1=4` | `LEVEL` = `64` | `42` → `61` |
| `42` | `M=6; LIV1=5` | `LEVEL` = `65` | `42` → `61` |
| `42` | `M=6; LIV1=6` | `LEVEL` = `66` | `42` → `61` |
| `42` | `M=6; LIV1=7` | `LEVEL` = `67` | `42` → `61` |
| `42` | `M=6; LIV1=8` | `LEVEL` = `68` | `42` → `61` |
| `42` | `M=6; LIV1=9` | `LEVEL` = `69` | `42` → `61` |
| `42` | `M=7; LIV1=0` | `LEVEL` = `70` | `42` → `62` |
| `42` | `M=7; LIV1=1` | `LEVEL` = `71` | `42` → `62` |
| `42` | `M=7; LIV1=2` | `LEVEL` = `72` | `42` → `62` |
| `42` | `M=7; LIV1=3` | `LEVEL` = `73` | `42` → `62` |
| `42` | `M=7; LIV1=4` | `LEVEL` = `74` | `42` → `62` |
| `42` | `M=7; LIV1=5` | `LEVEL` = `75` | `42` → `62` |
| `42` | `M=7; LIV1=6` | `LEVEL` = `76` | `42` → `62` |
| `42` | `M=7; LIV1=7` | `LEVEL` = `77` | `42` → `62` |
| `42` | `M=7; LIV1=8` | `LEVEL` = `78` | `42` → `62` |
| `42` | `M=7; LIV1=9` | `LEVEL` = `79` | `42` → `62` |
| `42` | `M=8; LIV1=0` | `LEVEL` = `80` | `42` → `63` |
| `42` | `M=8; LIV1=1` | `LEVEL` = `81` | `42` → `63` |
| `42` | `M=8; LIV1=2` | `LEVEL` = `82` | `42` → `63` |
| `42` | `M=8; LIV1=3` | `LEVEL` = `83` | `42` → `63` |
| `42` | `M=8; LIV1=4` | `LEVEL` = `84` | `42` → `63` |
| `42` | `M=8; LIV1=5` | `LEVEL` = `85` | `42` → `63` |
| `42` | `M=8; LIV1=6` | `LEVEL` = `86` | `42` → `63` |
| `42` | `M=8; LIV1=7` | `LEVEL` = `87` | `42` → `63` |
| `42` | `M=8; LIV1=8` | `LEVEL` = `88` | `42` → `63` |
| `42` | `M=8; LIV1=9` | `LEVEL` = `89` | `42` → `63` |
| `42` | `M=9; LIV1=0` | `LEVEL` = `90` | `42` → `64` |
| `42` | `M=9; LIV1=1` | `LEVEL` = `91` | `42` → `64` |
| `42` | `M=9; LIV1=2` | `LEVEL` = `92` | `42` → `64` |
| `42` | `M=9; LIV1=3` | `LEVEL` = `93` | `42` → `64` |
| `42` | `M=9; LIV1=4` | `LEVEL` = `94` | `42` → `64` |
| `42` | `M=9; LIV1=5` | `LEVEL` = `95` | `42` → `64` |
| `42` | `M=9; LIV1=6` | `LEVEL` = `96` | `42` → `64` |
| `42` | `M=9; LIV1=7` | `LEVEL` = `97` | `42` → `64` |
| `42` | `M=9; LIV1=8` | `LEVEL` = `98` | `42` → `64` |
| `42` | `M=9; LIV1=9` | `LEVEL` = `99` | `42` → `64` |
| `43` | `I=3` | `INST_LEV` = `4`; `DEST_LEV` = `3` | `43` |
| `43` | `I=4` | `INST_LEV` = `5`; `DEST_LEV` = `4` | `43` |
| `43` | `I=5` | `INST_LEV` = `6`; `DEST_LEV` = `5` | `43` |
| `43` | `I=6` | `INST_LEV` = `7`; `DEST_LEV` = `6` | `43` |
| `43` | `I=7` | `INST_LEV` = `8`; `DEST_LEV` = `7` | `43` |
| `43` | `I=8` | `INST_LEV` = `9`; `DEST_LEV` = `8` | `43` |
| `43` | `I=9` | `INST_LEV` = `10`; `DEST_LEV` = `9` | `43` |
| `43` | `I=CEN` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `43` |
| `43` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `43` |
| `43` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `43` |
| `43` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `43` |
| `43` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `43` |
| `43` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `43` |
| `43` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `43` |
| `43` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `43` |
| `43` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `43` |
| `43` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `43` |
| `43` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `43` |
| `43` | `SPE=ON` | `M` = `9` | `43` |
| `43` | `I=0` | `INST_LEV` = `1`; `DEST_LEV` = `1` | `43` |
| `43` | `I=1` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `43` |
| `43` | `I=2` | `INST_LEV` = `3`; `DEST_LEV` = `2` | `43` |
| `98` | `M=0` | `ADDR_TYPE` = `2`; `M` = `0` | `98` |
| `98` | `M=0; PL=1` | `G1` = `1` | `98` → `300` |
| `98` | `M=0; PL=2` | `G1` = `2` | `98` → `300` |
| `98` | `M=0; PL=3` | `G1` = `3` | `98` → `300` |
| `98` | `M=0; PL=4` | `G1` = `4` | `98` → `300` |
| `98` | `M=0; PL=5` | `G1` = `5` | `98` → `300` |
| `98` | `M=0; PL=6` | `G1` = `6` | `98` → `300` |
| `98` | `M=0; PL=7` | `G1` = `7` | `98` → `300` |
| `98` | `M=0; PL=8` | `G1` = `8` | `98` → `300` |
| `98` | `M=0; PL=9` | `G1` = `9` | `98` → `300` |
| `98` | `M=1` | `ADDR_TYPE` = `2` | `98` |
| `98` | `M=1; PL=1` | `G1` = `1` | `98` → `300` |
| `98` | `M=1; PL=2` | `G1` = `2` | `98` → `300` |
| `98` | `M=1; PL=3` | `G1` = `3` | `98` → `300` |
| `98` | `M=1; PL=4` | `G1` = `4` | `98` → `300` |
| `98` | `M=1; PL=5` | `G1` = `5` | `98` → `300` |
| `98` | `M=1; PL=6` | `G1` = `6` | `98` → `300` |
| `98` | `M=1; PL=7` | `G1` = `7` | `98` → `300` |
| `98` | `M=1; PL=8` | `G1` = `8` | `98` → `300` |
| `98` | `M=1; PL=9` | `G1` = `9` | `98` → `300` |
| `98` | `M=2` | `ADDR_TYPE` = `2` | `98` |
| `98` | `M=2; PL=1` | `G1` = `1` | `98` → `300` |
| `98` | `M=2; PL=2` | `G1` = `2` | `98` → `300` |
| `98` | `M=2; PL=3` | `G1` = `3` | `98` → `300` |
| `98` | `M=2; PL=4` | `G1` = `4` | `98` → `300` |
| `98` | `M=2; PL=5` | `G1` = `5` | `98` → `300` |
| `98` | `M=2; PL=6` | `G1` = `6` | `98` → `300` |
| `98` | `M=2; PL=7` | `G1` = `7` | `98` → `300` |
| `98` | `M=2; PL=8` | `G1` = `8` | `98` → `300` |
| `98` | `M=2; PL=9` | `G1` = `9` | `98` → `300` |
| `98` | `M=3` | `ADDR_TYPE` = `2` | `98` |
| `98` | `M=3; PL=1` | `G1` = `1` | `98` → `300` |
| `98` | `M=3; PL=2` | `G1` = `2` | `98` → `300` |
| `98` | `M=3; PL=3` | `G1` = `3` | `98` → `300` |
| `98` | `M=3; PL=4` | `G1` = `4` | `98` → `300` |
| `98` | `M=3; PL=5` | `G1` = `5` | `98` → `300` |
| `98` | `M=3; PL=6` | `G1` = `6` | `98` → `300` |
| `98` | `M=3; PL=7` | `G1` = `7` | `98` → `300` |
| `98` | `M=3; PL=8` | `G1` = `8` | `98` → `300` |
| `98` | `M=3; PL=9` | `G1` = `9` | `98` → `300` |
| `98` | `M=4` | `ADDR_TYPE` = `2` | `98` |
| `98` | `M=4; PL=1` | `G1` = `1` | `98` → `300` |
| `98` | `M=4; PL=2` | `G1` = `2` | `98` → `300` |
| `98` | `M=4; PL=3` | `G1` = `3` | `98` → `300` |
| `98` | `M=4; PL=4` | `G1` = `4` | `98` → `300` |
| `98` | `M=4; PL=5` | `G1` = `5` | `98` → `300` |
| `98` | `M=4; PL=6` | `G1` = `6` | `98` → `300` |
| `98` | `M=4; PL=7` | `G1` = `7` | `98` → `300` |
| `98` | `M=4; PL=8` | `G1` = `8` | `98` → `300` |
| `98` | `M=4; PL=9` | `G1` = `9` | `98` → `300` |
| `98` | `M=5` | `ADDR_TYPE` = `2` | `98` |
| `98` | `M=5; PL=1` | `G1` = `1` | `98` → `300` |
| `98` | `M=5; PL=2` | `G1` = `2` | `98` → `300` |
| `98` | `M=5; PL=3` | `G1` = `3` | `98` → `300` |
| `98` | `M=5; PL=4` | `G1` = `4` | `98` → `300` |
| `98` | `M=5; PL=5` | `G1` = `5` | `98` → `300` |
| `98` | `M=5; PL=6` | `G1` = `6` | `98` → `300` |
| `98` | `M=5; PL=7` | `G1` = `7` | `98` → `300` |
| `98` | `M=5; PL=8` | `G1` = `8` | `98` → `300` |
| `98` | `M=5; PL=9` | `G1` = `9` | `98` → `300` |
| `98` | `M=6` | `ADDR_TYPE` = `2` | `98` |
| `98` | `M=6; PL=1` | `G1` = `1` | `98` → `300` |
| `98` | `M=6; PL=2` | `G1` = `2` | `98` → `300` |
| `98` | `M=6; PL=3` | `G1` = `3` | `98` → `300` |
| `98` | `M=6; PL=4` | `G1` = `4` | `98` → `300` |
| `98` | `M=6; PL=5` | `G1` = `5` | `98` → `300` |
| `98` | `M=6; PL=6` | `G1` = `6` | `98` → `300` |
| `98` | `M=6; PL=7` | `G1` = `7` | `98` → `300` |
| `98` | `M=6; PL=8` | `G1` = `8` | `98` → `300` |
| `98` | `M=6; PL=9` | `G1` = `9` | `98` → `300` |
| `98` | `M=7` | `ADDR_TYPE` = `2` | `98` |
| `98` | `M=7; PL=1` | `G1` = `1` | `98` → `300` |
| `98` | `M=7; PL=2` | `G1` = `2` | `98` → `300` |
| `98` | `M=7; PL=3` | `G1` = `3` | `98` → `300` |
| `98` | `M=7; PL=4` | `G1` = `4` | `98` → `300` |
| `98` | `M=7; PL=5` | `G1` = `5` | `98` → `300` |
| `98` | `M=7; PL=6` | `G1` = `6` | `98` → `300` |
| `98` | `M=7; PL=7` | `G1` = `7` | `98` → `300` |
| `98` | `M=7; PL=8` | `G1` = `8` | `98` → `300` |
| `98` | `M=7; PL=9` | `G1` = `9` | `98` → `300` |
| `98` | `M=8` | `ADDR_TYPE` = `2` | `98` |
| `98` | `M=8; PL=1` | `G1` = `1` | `98` → `300` |
| `98` | `M=8; PL=2` | `G1` = `2` | `98` → `300` |
| `98` | `M=8; PL=3` | `G1` = `3` | `98` → `300` |
| `98` | `M=8; PL=4` | `G1` = `4` | `98` → `300` |
| `98` | `M=8; PL=5` | `G1` = `5` | `98` → `300` |
| `98` | `M=8; PL=6` | `G1` = `6` | `98` → `300` |
| `98` | `M=8; PL=7` | `G1` = `7` | `98` → `300` |
| `98` | `M=8; PL=8` | `G1` = `8` | `98` → `300` |
| `98` | `M=8; PL=9` | `G1` = `9` | `98` → `300` |
| `98` | `M=O/I` | `ADDR_TYPE` = `2`; `M` = `9` | `98` |
| `98` | `M=OFF` | `ADDR_TYPE` = `2`; `M` = `10` | `98` |
| `98` | `M=ON` | `ADDR_TYPE` = `2`; `M` = `11` | `98` |
| `98` | `M=PUL` | `ADDR_TYPE` = `2`; `M` = `15` | `98` |
| `98` | `M=SU_GIU` | `ADDR_TYPE` = `2`; `M` = `12` | `98` |
| `98` | `M=SU_GIU_M` | `ADDR_TYPE` = `2`; `M` = `13` | `98` |
| `98` | `M=O/I; PL=1` | `G1` = `1` | `98` → `300` |
| `98` | `M=O/I; PL=2` | `G1` = `2` | `98` → `300` |
| `98` | `M=O/I; PL=3` | `G1` = `3` | `98` → `300` |
| `98` | `M=O/I; PL=4` | `G1` = `4` | `98` → `300` |
| `98` | `M=O/I; PL=5` | `G1` = `5` | `98` → `300` |
| `98` | `M=O/I; PL=6` | `G1` = `6` | `98` → `300` |
| `98` | `M=O/I; PL=7` | `G1` = `7` | `98` → `300` |
| `98` | `M=O/I; PL=8` | `G1` = `8` | `98` → `300` |
| `98` | `M=O/I; PL=9` | `G1` = `9` | `98` → `300` |
| `98` | `M=OFF; PL=1` | `G1` = `1` | `98` → `300` |
| `98` | `M=OFF; PL=2` | `G1` = `2` | `98` → `300` |
| `98` | `M=OFF; PL=3` | `G1` = `3` | `98` → `300` |
| `98` | `M=OFF; PL=4` | `G1` = `4` | `98` → `300` |
| `98` | `M=OFF; PL=5` | `G1` = `5` | `98` → `300` |
| `98` | `M=OFF; PL=6` | `G1` = `6` | `98` → `300` |
| `98` | `M=OFF; PL=7` | `G1` = `7` | `98` → `300` |
| `98` | `M=OFF; PL=8` | `G1` = `8` | `98` → `300` |
| `98` | `M=OFF; PL=9` | `G1` = `9` | `98` → `300` |
| `98` | `M=ON; PL=1` | `G1` = `1` | `98` → `300` |
| `98` | `M=ON; PL=2` | `G1` = `2` | `98` → `300` |
| `98` | `M=ON; PL=3` | `G1` = `3` | `98` → `300` |
| `98` | `M=ON; PL=4` | `G1` = `4` | `98` → `300` |
| `98` | `M=ON; PL=5` | `G1` = `5` | `98` → `300` |
| `98` | `M=ON; PL=6` | `G1` = `6` | `98` → `300` |
| `98` | `M=ON; PL=7` | `G1` = `7` | `98` → `300` |
| `98` | `M=ON; PL=8` | `G1` = `8` | `98` → `300` |
| `98` | `M=ON; PL=9` | `G1` = `9` | `98` → `300` |
| `98` | `M=PUL; PL=1` | `G1` = `1` | `98` → `300` |
| `98` | `M=PUL; PL=2` | `G1` = `2` | `98` → `300` |
| `98` | `M=PUL; PL=3` | `G1` = `3` | `98` → `300` |
| `98` | `M=PUL; PL=4` | `G1` = `4` | `98` → `300` |
| `98` | `M=PUL; PL=5` | `G1` = `5` | `98` → `300` |
| `98` | `M=PUL; PL=6` | `G1` = `6` | `98` → `300` |
| `98` | `M=PUL; PL=7` | `G1` = `7` | `98` → `300` |
| `98` | `M=PUL; PL=8` | `G1` = `8` | `98` → `300` |
| `98` | `M=PUL; PL=9` | `G1` = `9` | `98` → `300` |
| `98` | `M=SU_GIU; PL=1` | `G1` = `1` | `98` → `300` |
| `98` | `M=SU_GIU; PL=2` | `G1` = `2` | `98` → `300` |
| `98` | `M=SU_GIU; PL=3` | `G1` = `3` | `98` → `300` |
| `98` | `M=SU_GIU; PL=4` | `G1` = `4` | `98` → `300` |
| `98` | `M=SU_GIU; PL=5` | `G1` = `5` | `98` → `300` |
| `98` | `M=SU_GIU; PL=6` | `G1` = `6` | `98` → `300` |
| `98` | `M=SU_GIU; PL=7` | `G1` = `7` | `98` → `300` |
| `98` | `M=SU_GIU; PL=8` | `G1` = `8` | `98` → `300` |
| `98` | `M=SU_GIU; PL=9` | `G1` = `9` | `98` → `300` |
| `98` | `M=SU_GIU_M; PL=1` | `G1` = `1` | `98` → `300` |
| `98` | `M=SU_GIU_M; PL=2` | `G1` = `2` | `98` → `300` |
| `98` | `M=SU_GIU_M; PL=3` | `G1` = `3` | `98` → `300` |
| `98` | `M=SU_GIU_M; PL=4` | `G1` = `4` | `98` → `300` |
| `98` | `M=SU_GIU_M; PL=5` | `G1` = `5` | `98` → `300` |
| `98` | `M=SU_GIU_M; PL=6` | `G1` = `6` | `98` → `300` |
| `98` | `M=SU_GIU_M; PL=7` | `G1` = `7` | `98` → `300` |
| `98` | `M=SU_GIU_M; PL=8` | `G1` = `8` | `98` → `300` |
| `98` | `M=SU_GIU_M; PL=9` | `G1` = `9` | `98` → `300` |
| `98` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `98` |
| `98` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `98` |
| `98` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `98` |
| `98` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `98` |
| `98` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `98` |
| `98` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `98` |
| `98` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `98` |
| `98` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `98` |
| `98` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `98` |
| `98` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `98` |
| `98` | `I=0` | `DEST_LEV` = `1` | `98` |
| `98` | `I=1` | `DEST_LEV` = `0` | `98` |
| `98` | `I=2` | `DEST_LEV` = `2` | `98` |
| `98` | `I=3` | `DEST_LEV` = `3` | `98` |
| `98` | `I=4` | `DEST_LEV` = `4` | `98` |
| `98` | `I=5` | `DEST_LEV` = `5` | `98` |
| `98` | `I=6` | `DEST_LEV` = `6` | `98` |
| `98` | `I=7` | `DEST_LEV` = `7` | `98` |
| `98` | `I=8` | `DEST_LEV` = `8` | `98` |
| `98` | `I=9` | `DEST_LEV` = `9` | `98` |
| `98` | `I=CEN` | `DEST_LEV` = `10` | `98` |
| `99` | `I=0` | `DEST_LEV` = `1`; `INST_LEV` = `1` | `99` |
| `99` | `M=0` | `M` = `0`; `ADDR_TYPE` = `2` | `99` |
| `99` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `99` |
| `99` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `99` |
| `99` | `I=1` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `99` |
| `99` | `M=1` | `T_TIME ` = `1`; `M` = `1`; `ADDR_TYPE` = `2` | `99` |
| `99` | `M=2` | `M` = `1`; `T_TIME ` = `2`; `ADDR_TYPE` = `2` | `99` |
| `99` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `99` |
| `99` | `I=2` | `DEST_LEV` = `2`; `INST_LEV` = `3` | `99` |
| `99` | `I=3` | `DEST_LEV` = `3`; `INST_LEV` = `4` | `99` |
| `99` | `M=3` | `T_TIME ` = `3`; `M` = `1`; `ADDR_TYPE` = `2` | `99` |
| `99` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `99` |
| `99` | `M=4` | `T_TIME ` = `4`; `M` = `1`; `ADDR_TYPE` = `2` | `99` |
| `99` | `I=4` | `DEST_LEV` = `4`; `INST_LEV` = `5` | `99` |
| `99` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `99` |
| `99` | `M=5` | `T_TIME ` = `5`; `M` = `1`; `ADDR_TYPE` = `2` | `99` |
| `99` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `99` |
| `99` | `I=5` | `DEST_LEV` = `5`; `INST_LEV` = `6` | `99` |
| `99` | `I=6` | `DEST_LEV` = `6`; `INST_LEV` = `7` | `99` |
| `99` | `M=6` | `M` = `1`; `T_TIME ` = `6`; `ADDR_TYPE` = `2` | `99` |
| `99` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `99` |
| `99` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `99` |
| `99` | `M=7` | `M` = `1`; `T_TIME ` = `7`; `ADDR_TYPE` = `2` | `99` |
| `99` | `I=7` | `INST_LEV` = `8`; `DEST_LEV` = `7` | `99` |
| `99` | `M=8` | `M` = `1`; `T_TIME ` = `8`; `ADDR_TYPE` = `2` | `99` |
| `99` | `I=8` | `DEST_LEV` = `8`; `INST_LEV` = `9` | `99` |
| `99` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `99` |
| `99` | `I=9` | `DEST_LEV` = `9`; `INST_LEV` = `10` | `99` |
| `99` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `99` |
| `99` | `I=CEN` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `99` |
| `99` | `M=CEN` | `CEN_BUTT_2 ` = `2`; `CEN_BUTT_1 ` = `1` | `99` |
| `99` | `M=O/I` | `M` = `9`; `ADDR_TYPE` = `2` | `99` |
| `99` | `M=OFF` | `M` = `10`; `ADDR_TYPE` = `2` | `99` |
| `99` | `M=ON` | `M` = `11`; `ADDR_TYPE` = `2` | `99` |
| `99` | `M=PUL` | `M` = `15`; `ADDR_TYPE` = `2` | `99` |
| `99` | `M=SU_GIU` | `M` = `12`; `ADDR_TYPE` = `2` | `99` |
| `99` | `M=SU_GIU_M` | `M` = `13`; `ADDR_TYPE` = `2` | `99` |
| `99` | `M=0; PL=1` | `G1` = `1` | `99` → `300` |
| `99` | `M=0; PL=2` | `G1` = `2` | `99` → `300` |
| `99` | `M=0; PL=3` | `G1` = `3` | `99` → `300` |
| `99` | `M=0; PL=4` | `G1` = `4` | `99` → `300` |
| `99` | `M=0; PL=5` | `G1` = `5` | `99` → `300` |
| `99` | `M=0; PL=6` | `G1` = `6` | `99` → `300` |
| `99` | `M=0; PL=7` | `G1` = `7` | `99` → `300` |
| `99` | `M=0; PL=8` | `G1` = `8` | `99` → `300` |
| `99` | `M=0; PL=9` | `G1` = `9` | `99` → `300` |
| `99` | `M=1; PL=1` | `G1` = `1` | `99` → `300` |
| `99` | `M=1; PL=2` | `G1` = `2` | `99` → `300` |
| `99` | `M=1; PL=3` | `G1` = `3` | `99` → `300` |
| `99` | `M=1; PL=4` | `G1` = `4` | `99` → `300` |
| `99` | `M=1; PL=5` | `G1` = `5` | `99` → `300` |
| `99` | `M=1; PL=6` | `G1` = `6` | `99` → `300` |
| `99` | `M=1; PL=7` | `G1` = `7` | `99` → `300` |
| `99` | `M=1; PL=8` | `G1` = `8` | `99` → `300` |
| `99` | `M=1; PL=9` | `G1` = `9` | `99` → `300` |
| `99` | `M=2; PL=1` | `G1` = `1` | `99` → `300` |
| `99` | `M=2; PL=2` | `G1` = `2` | `99` → `300` |
| `99` | `M=2; PL=3` | `G1` = `3` | `99` → `300` |
| `99` | `M=2; PL=4` | `G1` = `4` | `99` → `300` |
| `99` | `M=2; PL=5` | `G1` = `5` | `99` → `300` |
| `99` | `M=2; PL=6` | `G1` = `6` | `99` → `300` |
| `99` | `M=2; PL=7` | `G1` = `7` | `99` → `300` |
| `99` | `M=2; PL=8` | `G1` = `8` | `99` → `300` |
| `99` | `M=2; PL=9` | `G1` = `9` | `99` → `300` |
| `99` | `M=3; PL=1` | `G1` = `1` | `99` → `300` |
| `99` | `M=3; PL=2` | `G1` = `2` | `99` → `300` |
| `99` | `M=3; PL=3` | `G1` = `3` | `99` → `300` |
| `99` | `M=3; PL=4` | `G1` = `4` | `99` → `300` |
| `99` | `M=3; PL=5` | `G1` = `5` | `99` → `300` |
| `99` | `M=3; PL=6` | `G1` = `6` | `99` → `300` |
| `99` | `M=3; PL=7` | `G1` = `7` | `99` → `300` |
| `99` | `M=3; PL=8` | `G1` = `8` | `99` → `300` |
| `99` | `M=3; PL=9` | `G1` = `9` | `99` → `300` |
| `99` | `M=4; PL=1` | `G1` = `1` | `99` → `300` |
| `99` | `M=4; PL=2` | `G1` = `2` | `99` → `300` |
| `99` | `M=4; PL=3` | `G1` = `3` | `99` → `300` |
| `99` | `M=4; PL=4` | `G1` = `4` | `99` → `300` |
| `99` | `M=4; PL=5` | `G1` = `5` | `99` → `300` |
| `99` | `M=4; PL=6` | `G1` = `6` | `99` → `300` |
| `99` | `M=4; PL=7` | `G1` = `7` | `99` → `300` |
| `99` | `M=4; PL=8` | `G1` = `8` | `99` → `300` |
| `99` | `M=4; PL=9` | `G1` = `9` | `99` → `300` |
| `99` | `M=5; PL=1` | `G1` = `1` | `99` → `300` |
| `99` | `M=5; PL=2` | `G1` = `2` | `99` → `300` |
| `99` | `M=5; PL=3` | `G1` = `3` | `99` → `300` |
| `99` | `M=5; PL=4` | `G1` = `4` | `99` → `300` |
| `99` | `M=5; PL=5` | `G1` = `5` | `99` → `300` |
| `99` | `M=5; PL=6` | `G1` = `6` | `99` → `300` |
| `99` | `M=5; PL=7` | `G1` = `7` | `99` → `300` |
| `99` | `M=5; PL=8` | `G1` = `8` | `99` → `300` |
| `99` | `M=5; PL=9` | `G1` = `9` | `99` → `300` |
| `99` | `M=6; PL=1` | `G1` = `1` | `99` → `300` |
| `99` | `M=6; PL=2` | `G1` = `2` | `99` → `300` |
| `99` | `M=6; PL=3` | `G1` = `3` | `99` → `300` |
| `99` | `M=6; PL=4` | `G1` = `4` | `99` → `300` |
| `99` | `M=6; PL=5` | `G1` = `5` | `99` → `300` |
| `99` | `M=6; PL=6` | `G1` = `6` | `99` → `300` |
| `99` | `M=6; PL=7` | `G1` = `7` | `99` → `300` |
| `99` | `M=6; PL=8` | `G1` = `8` | `99` → `300` |
| `99` | `M=6; PL=9` | `G1` = `9` | `99` → `300` |
| `99` | `M=7; PL=1` | `G1` = `1` | `99` → `300` |
| `99` | `M=7; PL=2` | `G1` = `2` | `99` → `300` |
| `99` | `M=7; PL=3` | `G1` = `3` | `99` → `300` |
| `99` | `M=7; PL=4` | `G1` = `4` | `99` → `300` |
| `99` | `M=7; PL=5` | `G1` = `5` | `99` → `300` |
| `99` | `M=7; PL=6` | `G1` = `6` | `99` → `300` |
| `99` | `M=7; PL=7` | `G1` = `7` | `99` → `300` |
| `99` | `M=7; PL=8` | `G1` = `8` | `99` → `300` |
| `99` | `M=7; PL=9` | `G1` = `9` | `99` → `300` |
| `99` | `M=8; PL=1` | `G1` = `1` | `99` → `300` |
| `99` | `M=8; PL=2` | `G1` = `2` | `99` → `300` |
| `99` | `M=8; PL=3` | `G1` = `3` | `99` → `300` |
| `99` | `M=8; PL=4` | `G1` = `4` | `99` → `300` |
| `99` | `M=8; PL=5` | `G1` = `5` | `99` → `300` |
| `99` | `M=8; PL=6` | `G1` = `6` | `99` → `300` |
| `99` | `M=8; PL=7` | `G1` = `7` | `99` → `300` |
| `99` | `M=8; PL=8` | `G1` = `8` | `99` → `300` |
| `99` | `M=8; PL=9` | `G1` = `9` | `99` → `300` |
| `99` | `M=O/I; PL=1` | `G1` = `1` | `99` → `300` |
| `99` | `M=O/I; PL=2` | `G1` = `2` | `99` → `300` |
| `99` | `M=O/I; PL=3` | `G1` = `3` | `99` → `300` |
| `99` | `M=O/I; PL=4` | `G1` = `4` | `99` → `300` |
| `99` | `M=O/I; PL=5` | `G1` = `5` | `99` → `300` |
| `99` | `M=O/I; PL=6` | `G1` = `6` | `99` → `300` |
| `99` | `M=O/I; PL=7` | `G1` = `7` | `99` → `300` |
| `99` | `M=O/I; PL=8` | `G1` = `8` | `99` → `300` |
| `99` | `M=O/I; PL=9` | `G1` = `9` | `99` → `300` |
| `99` | `M=OFF; PL=1` | `G1` = `1` | `99` → `300` |
| `99` | `M=OFF; PL=2` | `G1` = `2` | `99` → `300` |
| `99` | `M=OFF; PL=3` | `G1` = `3` | `99` → `300` |
| `99` | `M=OFF; PL=4` | `G1` = `4` | `99` → `300` |
| `99` | `M=OFF; PL=5` | `G1` = `5` | `99` → `300` |
| `99` | `M=OFF; PL=6` | `G1` = `6` | `99` → `300` |
| `99` | `M=OFF; PL=7` | `G1` = `7` | `99` → `300` |
| `99` | `M=OFF; PL=8` | `G1` = `8` | `99` → `300` |
| `99` | `M=OFF; PL=9` | `G1` = `9` | `99` → `300` |
| `99` | `M=ON; PL=1` | `G1` = `1` | `99` → `300` |
| `99` | `M=ON; PL=2` | `G1` = `2` | `99` → `300` |
| `99` | `M=ON; PL=3` | `G1` = `3` | `99` → `300` |
| `99` | `M=ON; PL=4` | `G1` = `4` | `99` → `300` |
| `99` | `M=ON; PL=5` | `G1` = `5` | `99` → `300` |
| `99` | `M=ON; PL=6` | `G1` = `6` | `99` → `300` |
| `99` | `M=ON; PL=7` | `G1` = `7` | `99` → `300` |
| `99` | `M=ON; PL=8` | `G1` = `8` | `99` → `300` |
| `99` | `M=ON; PL=9` | `G1` = `9` | `99` → `300` |
| `99` | `M=PUL; PL=1` | `G1` = `1` | `99` → `300` |
| `99` | `M=PUL; PL=2` | `G1` = `2` | `99` → `300` |
| `99` | `M=PUL; PL=3` | `G1` = `3` | `99` → `300` |
| `99` | `M=PUL; PL=4` | `G1` = `4` | `99` → `300` |
| `99` | `M=PUL; PL=5` | `G1` = `5` | `99` → `300` |
| `99` | `M=PUL; PL=6` | `G1` = `6` | `99` → `300` |
| `99` | `M=PUL; PL=7` | `G1` = `7` | `99` → `300` |
| `99` | `M=PUL; PL=8` | `G1` = `8` | `99` → `300` |
| `99` | `M=PUL; PL=9` | `G1` = `9` | `99` → `300` |
| `99` | `M=SU_GIU; PL=1` | `G1` = `1` | `99` → `300` |
| `99` | `M=SU_GIU; PL=2` | `G1` = `2` | `99` → `300` |
| `99` | `M=SU_GIU; PL=3` | `G1` = `3` | `99` → `300` |
| `99` | `M=SU_GIU; PL=4` | `G1` = `4` | `99` → `300` |
| `99` | `M=SU_GIU; PL=5` | `G1` = `5` | `99` → `300` |
| `99` | `M=SU_GIU; PL=6` | `G1` = `6` | `99` → `300` |
| `99` | `M=SU_GIU; PL=7` | `G1` = `7` | `99` → `300` |
| `99` | `M=SU_GIU; PL=8` | `G1` = `8` | `99` → `300` |
| `99` | `M=SU_GIU; PL=9` | `G1` = `9` | `99` → `300` |
| `99` | `M=SU_GIU_M; PL=1` | `G1` = `1` | `99` → `300` |
| `99` | `M=SU_GIU_M; PL=2` | `G1` = `2` | `99` → `300` |
| `99` | `M=SU_GIU_M; PL=3` | `G1` = `3` | `99` → `300` |
| `99` | `M=SU_GIU_M; PL=4` | `G1` = `4` | `99` → `300` |
| `99` | `M=SU_GIU_M; PL=5` | `G1` = `5` | `99` → `300` |
| `99` | `M=SU_GIU_M; PL=6` | `G1` = `6` | `99` → `300` |
| `99` | `M=SU_GIU_M; PL=7` | `G1` = `7` | `99` → `300` |
| `99` | `M=SU_GIU_M; PL=8` | `G1` = `8` | `99` → `300` |
| `99` | `M=SU_GIU_M; PL=9` | `G1` = `9` | `99` → `300` |
| `100` | `I=0` | `INST_LEV` = `1`; `DEST_LEV` = `1` | `100` |
| `100` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `100` |
| `100` | `I=1` | `DEST_LEV` = `0`; `INST_LEV` = `1` | `100` |
| `100` | `M=1` | `M` = `1`; `ADDR_TYPE` = `2` | `100` |
| `100` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `100` |
| `100` | `I=2` | `INST_LEV` = `3`; `DEST_LEV` = `2` | `100` |
| `100` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `100` |
| `100` | `M=2` | `M` = `2`; `ADDR_TYPE` = `2` | `100` |
| `100` | `I=3` | `INST_LEV` = `4`; `DEST_LEV` = `3` | `100` |
| `100` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `100` |
| `100` | `M=3` | `M` = `3`; `ADDR_TYPE` = `2` | `100` |
| `100` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `100` |
| `100` | `I=4` | `DEST_LEV` = `4`; `INST_LEV` = `5` | `100` |
| `100` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `100` |
| `100` | `I=5` | `DEST_LEV` = `5`; `INST_LEV` = `6` | `100` |
| `100` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `100` |
| `100` | `I=6` | `DEST_LEV` = `6`; `INST_LEV` = `7` | `100` |
| `100` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `100` |
| `100` | `I=7` | `INST_LEV` = `8`; `DEST_LEV` = `7` | `100` |
| `100` | `I=8` | `DEST_LEV` = `8`; `INST_LEV` = `9` | `100` |
| `100` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `100` |
| `100` | `I=9` | `DEST_LEV` = `9`; `INST_LEV` = `10` | `100` |
| `100` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `100` |
| `100` | `I=CEN` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `100` |
| `100` | `M=0` | `ADDR_TYPE` = `2` | `100` |
| `100` | `M=0; PL=1` | `G1` = `1` | `100` → `300` |
| `100` | `M=0; PL=2` | `G1` = `2` | `100` → `300` |
| `100` | `M=0; PL=3` | `G1` = `3` | `100` → `300` |
| `100` | `M=0; PL=4` | `G1` = `4` | `100` → `300` |
| `100` | `M=0; PL=5` | `G1` = `5` | `100` → `300` |
| `100` | `M=0; PL=6` | `G1` = `6` | `100` → `300` |
| `100` | `M=0; PL=7` | `G1` = `7` | `100` → `300` |
| `100` | `M=0; PL=8` | `G1` = `8` | `100` → `300` |
| `100` | `M=0; PL=9` | `G1` = `9` | `100` → `300` |
| `100` | `M=1; PL=1` | `G1` = `1` | `100` → `300` |
| `100` | `M=1; PL=2` | `G1` = `2` | `100` → `300` |
| `100` | `M=1; PL=3` | `G1` = `3` | `100` → `300` |
| `100` | `M=1; PL=4` | `G1` = `4` | `100` → `300` |
| `100` | `M=1; PL=5` | `G1` = `5` | `100` → `300` |
| `100` | `M=1; PL=6` | `G1` = `6` | `100` → `300` |
| `100` | `M=1; PL=7` | `G1` = `7` | `100` → `300` |
| `100` | `M=1; PL=8` | `G1` = `8` | `100` → `300` |
| `100` | `M=1; PL=9` | `G1` = `9` | `100` → `300` |
| `100` | `M=2; PL=1` | `G1` = `1` | `100` → `300` |
| `100` | `M=2; PL=2` | `G1` = `2` | `100` → `300` |
| `100` | `M=2; PL=3` | `G1` = `3` | `100` → `300` |
| `100` | `M=2; PL=4` | `G1` = `4` | `100` → `300` |
| `100` | `M=2; PL=5` | `G1` = `5` | `100` → `300` |
| `100` | `M=2; PL=6` | `G1` = `6` | `100` → `300` |
| `100` | `M=2; PL=7` | `G1` = `7` | `100` → `300` |
| `100` | `M=2; PL=8` | `G1` = `8` | `100` → `300` |
| `100` | `M=2; PL=9` | `G1` = `9` | `100` → `300` |
| `100` | `M=3; PL=1` | `G1` = `1` | `100` → `300` |
| `100` | `M=3; PL=2` | `G1` = `2` | `100` → `300` |
| `100` | `M=3; PL=3` | `G1` = `3` | `100` → `300` |
| `100` | `M=3; PL=4` | `G1` = `4` | `100` → `300` |
| `100` | `M=3; PL=5` | `G1` = `5` | `100` → `300` |
| `100` | `M=3; PL=6` | `G1` = `6` | `100` → `300` |
| `100` | `M=3; PL=7` | `G1` = `7` | `100` → `300` |
| `100` | `M=3; PL=8` | `G1` = `8` | `100` → `300` |
| `100` | `M=3; PL=9` | `G1` = `9` | `100` → `300` |
| `100` | `M=4` | `ADDR_TYPE` = `2` | `100` |
| `100` | `M=4; PL=1` | `G1` = `1` | `100` → `300` |
| `100` | `M=4; PL=2` | `G1` = `2` | `100` → `300` |
| `100` | `M=4; PL=3` | `G1` = `3` | `100` → `300` |
| `100` | `M=4; PL=4` | `G1` = `4` | `100` → `300` |
| `100` | `M=4; PL=5` | `G1` = `5` | `100` → `300` |
| `100` | `M=4; PL=6` | `G1` = `6` | `100` → `300` |
| `100` | `M=4; PL=7` | `G1` = `7` | `100` → `300` |
| `100` | `M=4; PL=8` | `G1` = `8` | `100` → `300` |
| `100` | `M=4; PL=9` | `G1` = `9` | `100` → `300` |
| `100` | `M=5` | `ADDR_TYPE` = `2` | `100` |
| `100` | `M=5; PL=1` | `G1` = `1` | `100` → `300` |
| `100` | `M=5; PL=2` | `G1` = `2` | `100` → `300` |
| `100` | `M=5; PL=3` | `G1` = `3` | `100` → `300` |
| `100` | `M=5; PL=4` | `G1` = `4` | `100` → `300` |
| `100` | `M=5; PL=5` | `G1` = `5` | `100` → `300` |
| `100` | `M=5; PL=6` | `G1` = `6` | `100` → `300` |
| `100` | `M=5; PL=7` | `G1` = `7` | `100` → `300` |
| `100` | `M=5; PL=8` | `G1` = `8` | `100` → `300` |
| `100` | `M=5; PL=9` | `G1` = `9` | `100` → `300` |
| `100` | `M=6` | `ADDR_TYPE` = `2` | `100` |
| `100` | `M=6; PL=1` | `G1` = `1` | `100` → `300` |
| `100` | `M=6; PL=2` | `G1` = `2` | `100` → `300` |
| `100` | `M=6; PL=3` | `G1` = `3` | `100` → `300` |
| `100` | `M=6; PL=4` | `G1` = `4` | `100` → `300` |
| `100` | `M=6; PL=5` | `G1` = `5` | `100` → `300` |
| `100` | `M=6; PL=6` | `G1` = `6` | `100` → `300` |
| `100` | `M=6; PL=7` | `G1` = `7` | `100` → `300` |
| `100` | `M=6; PL=8` | `G1` = `8` | `100` → `300` |
| `100` | `M=6; PL=9` | `G1` = `9` | `100` → `300` |
| `100` | `M=7` | `ADDR_TYPE` = `2` | `100` |
| `100` | `M=7; PL=1` | `G1` = `1` | `100` → `300` |
| `100` | `M=7; PL=2` | `G1` = `2` | `100` → `300` |
| `100` | `M=7; PL=3` | `G1` = `3` | `100` → `300` |
| `100` | `M=7; PL=4` | `G1` = `4` | `100` → `300` |
| `100` | `M=7; PL=5` | `G1` = `5` | `100` → `300` |
| `100` | `M=7; PL=6` | `G1` = `6` | `100` → `300` |
| `100` | `M=7; PL=7` | `G1` = `7` | `100` → `300` |
| `100` | `M=7; PL=8` | `G1` = `8` | `100` → `300` |
| `100` | `M=7; PL=9` | `G1` = `9` | `100` → `300` |
| `100` | `M=8` | `ADDR_TYPE` = `2` | `100` |
| `100` | `M=8; PL=1` | `G1` = `1` | `100` → `300` |
| `100` | `M=8; PL=2` | `G1` = `2` | `100` → `300` |
| `100` | `M=8; PL=3` | `G1` = `3` | `100` → `300` |
| `100` | `M=8; PL=4` | `G1` = `4` | `100` → `300` |
| `100` | `M=8; PL=5` | `G1` = `5` | `100` → `300` |
| `100` | `M=8; PL=6` | `G1` = `6` | `100` → `300` |
| `100` | `M=8; PL=7` | `G1` = `7` | `100` → `300` |
| `100` | `M=8; PL=8` | `G1` = `8` | `100` → `300` |
| `100` | `M=8; PL=9` | `G1` = `9` | `100` → `300` |
| `100` | `M=O/I` | `ADDR_TYPE` = `2` | `100` |
| `100` | `M=OFF` | `ADDR_TYPE` = `2` | `100` |
| `100` | `M=ON` | `ADDR_TYPE` = `2` | `100` |
| `100` | `M=PUL` | `ADDR_TYPE` = `2` | `100` |
| `100` | `M=SU_GIU` | `ADDR_TYPE` = `2` | `100` |
| `100` | `M=SU_GIU_M` | `ADDR_TYPE` = `2` | `100` |
| `100` | `M=O/I; PL=1` | `G1` = `1` | `100` → `300` |
| `100` | `M=O/I; PL=2` | `G1` = `2` | `100` → `300` |
| `100` | `M=O/I; PL=3` | `G1` = `3` | `100` → `300` |
| `100` | `M=O/I; PL=4` | `G1` = `4` | `100` → `300` |
| `100` | `M=O/I; PL=5` | `G1` = `5` | `100` → `300` |
| `100` | `M=O/I; PL=6` | `G1` = `6` | `100` → `300` |
| `100` | `M=O/I; PL=7` | `G1` = `7` | `100` → `300` |
| `100` | `M=O/I; PL=8` | `G1` = `8` | `100` → `300` |
| `100` | `M=O/I; PL=9` | `G1` = `9` | `100` → `300` |
| `100` | `M=OFF; PL=1` | `G1` = `1` | `100` → `300` |
| `100` | `M=OFF; PL=2` | `G1` = `2` | `100` → `300` |
| `100` | `M=OFF; PL=3` | `G1` = `3` | `100` → `300` |
| `100` | `M=OFF; PL=4` | `G1` = `4` | `100` → `300` |
| `100` | `M=OFF; PL=5` | `G1` = `5` | `100` → `300` |
| `100` | `M=OFF; PL=6` | `G1` = `6` | `100` → `300` |
| `100` | `M=OFF; PL=7` | `G1` = `7` | `100` → `300` |
| `100` | `M=OFF; PL=8` | `G1` = `8` | `100` → `300` |
| `100` | `M=OFF; PL=9` | `G1` = `9` | `100` → `300` |
| `100` | `M=ON; PL=1` | `G1` = `1` | `100` → `300` |
| `100` | `M=ON; PL=2` | `G1` = `2` | `100` → `300` |
| `100` | `M=ON; PL=3` | `G1` = `3` | `100` → `300` |
| `100` | `M=ON; PL=4` | `G1` = `4` | `100` → `300` |
| `100` | `M=ON; PL=5` | `G1` = `5` | `100` → `300` |
| `100` | `M=ON; PL=6` | `G1` = `6` | `100` → `300` |
| `100` | `M=ON; PL=7` | `G1` = `7` | `100` → `300` |
| `100` | `M=ON; PL=8` | `G1` = `8` | `100` → `300` |
| `100` | `M=ON; PL=9` | `G1` = `9` | `100` → `300` |
| `100` | `M=PUL; PL=1` | `G1` = `1` | `100` → `300` |
| `100` | `M=PUL; PL=2` | `G1` = `2` | `100` → `300` |
| `100` | `M=PUL; PL=3` | `G1` = `3` | `100` → `300` |
| `100` | `M=PUL; PL=4` | `G1` = `4` | `100` → `300` |
| `100` | `M=PUL; PL=5` | `G1` = `5` | `100` → `300` |
| `100` | `M=PUL; PL=6` | `G1` = `6` | `100` → `300` |
| `100` | `M=PUL; PL=7` | `G1` = `7` | `100` → `300` |
| `100` | `M=PUL; PL=8` | `G1` = `8` | `100` → `300` |
| `100` | `M=PUL; PL=9` | `G1` = `9` | `100` → `300` |
| `100` | `M=SU_GIU; PL=1` | `G1` = `1` | `100` → `300` |
| `100` | `M=SU_GIU; PL=2` | `G1` = `2` | `100` → `300` |
| `100` | `M=SU_GIU; PL=3` | `G1` = `3` | `100` → `300` |
| `100` | `M=SU_GIU; PL=4` | `G1` = `4` | `100` → `300` |
| `100` | `M=SU_GIU; PL=5` | `G1` = `5` | `100` → `300` |
| `100` | `M=SU_GIU; PL=6` | `G1` = `6` | `100` → `300` |
| `100` | `M=SU_GIU; PL=7` | `G1` = `7` | `100` → `300` |
| `100` | `M=SU_GIU; PL=8` | `G1` = `8` | `100` → `300` |
| `100` | `M=SU_GIU; PL=9` | `G1` = `9` | `100` → `300` |
| `100` | `M=SU_GIU_M; PL=1` | `G1` = `1` | `100` → `300` |
| `100` | `M=SU_GIU_M; PL=2` | `G1` = `2` | `100` → `300` |
| `100` | `M=SU_GIU_M; PL=3` | `G1` = `3` | `100` → `300` |
| `100` | `M=SU_GIU_M; PL=4` | `G1` = `4` | `100` → `300` |
| `100` | `M=SU_GIU_M; PL=5` | `G1` = `5` | `100` → `300` |
| `100` | `M=SU_GIU_M; PL=6` | `G1` = `6` | `100` → `300` |
| `100` | `M=SU_GIU_M; PL=7` | `G1` = `7` | `100` → `300` |
| `100` | `M=SU_GIU_M; PL=8` | `G1` = `8` | `100` → `300` |
| `100` | `M=SU_GIU_M; PL=9` | `G1` = `9` | `100` → `300` |
| `101` | `M=0` | `ADDR_TYPE` = `1`; `M` = `0` | `101` |
| `101` | `M=0; PL=1` | `A` = `1` | `101` → `301` |
| `101` | `M=0; PL=2` | `A` = `2` | `101` → `301` |
| `101` | `M=0; PL=3` | `A` = `3` | `101` → `301` |
| `101` | `M=0; PL=4` | `A` = `4` | `101` → `301` |
| `101` | `M=0; PL=5` | `A` = `5` | `101` → `301` |
| `101` | `M=0; PL=6` | `A` = `6` | `101` → `301` |
| `101` | `M=0; PL=7` | `A` = `7` | `101` → `301` |
| `101` | `M=0; PL=8` | `A` = `8` | `101` → `301` |
| `101` | `M=0; PL=9` | `A` = `9` | `101` → `301` |
| `101` | `M=1` | `ADDR_TYPE` = `1` | `101` |
| `101` | `M=1; PL=1` | `A` = `1` | `101` → `301` |
| `101` | `M=1; PL=2` | `A` = `2` | `101` → `301` |
| `101` | `M=1; PL=3` | `A` = `3` | `101` → `301` |
| `101` | `M=1; PL=4` | `A` = `4` | `101` → `301` |
| `101` | `M=1; PL=5` | `A` = `5` | `101` → `301` |
| `101` | `M=1; PL=6` | `A` = `6` | `101` → `301` |
| `101` | `M=1; PL=7` | `A` = `7` | `101` → `301` |
| `101` | `M=1; PL=8` | `A` = `8` | `101` → `301` |
| `101` | `M=1; PL=9` | `A` = `9` | `101` → `301` |
| `101` | `M=2` | `ADDR_TYPE` = `1` | `101` |
| `101` | `M=2; PL=1` | `A` = `1` | `101` → `301` |
| `101` | `M=2; PL=2` | `A` = `2` | `101` → `301` |
| `101` | `M=2; PL=3` | `A` = `3` | `101` → `301` |
| `101` | `M=2; PL=4` | `A` = `4` | `101` → `301` |
| `101` | `M=2; PL=5` | `A` = `5` | `101` → `301` |
| `101` | `M=2; PL=6` | `A` = `6` | `101` → `301` |
| `101` | `M=2; PL=7` | `A` = `7` | `101` → `301` |
| `101` | `M=2; PL=8` | `A` = `8` | `101` → `301` |
| `101` | `M=2; PL=9` | `A` = `9` | `101` → `301` |
| `101` | `M=3` | `ADDR_TYPE` = `1` | `101` |
| `101` | `M=3; PL=1` | `A` = `1` | `101` → `301` |
| `101` | `M=3; PL=2` | `A` = `2` | `101` → `301` |
| `101` | `M=3; PL=3` | `A` = `3` | `101` → `301` |
| `101` | `M=3; PL=4` | `A` = `4` | `101` → `301` |
| `101` | `M=3; PL=5` | `A` = `5` | `101` → `301` |
| `101` | `M=3; PL=6` | `A` = `6` | `101` → `301` |
| `101` | `M=3; PL=7` | `A` = `7` | `101` → `301` |
| `101` | `M=3; PL=8` | `A` = `8` | `101` → `301` |
| `101` | `M=3; PL=9` | `A` = `9` | `101` → `301` |
| `101` | `M=4` | `ADDR_TYPE` = `1` | `101` |
| `101` | `M=4; PL=1` | `A` = `1` | `101` → `301` |
| `101` | `M=4; PL=2` | `A` = `2` | `101` → `301` |
| `101` | `M=4; PL=3` | `A` = `3` | `101` → `301` |
| `101` | `M=4; PL=4` | `A` = `4` | `101` → `301` |
| `101` | `M=4; PL=5` | `A` = `5` | `101` → `301` |
| `101` | `M=4; PL=6` | `A` = `6` | `101` → `301` |
| `101` | `M=4; PL=7` | `A` = `7` | `101` → `301` |
| `101` | `M=4; PL=8` | `A` = `8` | `101` → `301` |
| `101` | `M=4; PL=9` | `A` = `9` | `101` → `301` |
| `101` | `M=5` | `ADDR_TYPE` = `1` | `101` |
| `101` | `M=5; PL=1` | `A` = `1` | `101` → `301` |
| `101` | `M=5; PL=2` | `A` = `2` | `101` → `301` |
| `101` | `M=5; PL=3` | `A` = `3` | `101` → `301` |
| `101` | `M=5; PL=4` | `A` = `4` | `101` → `301` |
| `101` | `M=5; PL=5` | `A` = `5` | `101` → `301` |
| `101` | `M=5; PL=6` | `A` = `6` | `101` → `301` |
| `101` | `M=5; PL=7` | `A` = `7` | `101` → `301` |
| `101` | `M=5; PL=8` | `A` = `8` | `101` → `301` |
| `101` | `M=5; PL=9` | `A` = `9` | `101` → `301` |
| `101` | `M=6` | `ADDR_TYPE` = `1` | `101` |
| `101` | `M=6; PL=1` | `A` = `1` | `101` → `301` |
| `101` | `M=6; PL=2` | `A` = `2` | `101` → `301` |
| `101` | `M=6; PL=3` | `A` = `3` | `101` → `301` |
| `101` | `M=6; PL=4` | `A` = `4` | `101` → `301` |
| `101` | `M=6; PL=5` | `A` = `5` | `101` → `301` |
| `101` | `M=6; PL=6` | `A` = `6` | `101` → `301` |
| `101` | `M=6; PL=7` | `A` = `7` | `101` → `301` |
| `101` | `M=6; PL=8` | `A` = `8` | `101` → `301` |
| `101` | `M=6; PL=9` | `A` = `9` | `101` → `301` |
| `101` | `M=7` | `ADDR_TYPE` = `1` | `101` |
| `101` | `M=7; PL=1` | `A` = `1` | `101` → `301` |
| `101` | `M=7; PL=2` | `A` = `2` | `101` → `301` |
| `101` | `M=7; PL=3` | `A` = `3` | `101` → `301` |
| `101` | `M=7; PL=4` | `A` = `4` | `101` → `301` |
| `101` | `M=7; PL=5` | `A` = `5` | `101` → `301` |
| `101` | `M=7; PL=6` | `A` = `6` | `101` → `301` |
| `101` | `M=7; PL=7` | `A` = `7` | `101` → `301` |
| `101` | `M=7; PL=8` | `A` = `8` | `101` → `301` |
| `101` | `M=7; PL=9` | `A` = `9` | `101` → `301` |
| `101` | `M=8` | `ADDR_TYPE` = `1` | `101` |
| `101` | `M=8; PL=1` | `A` = `1` | `101` → `301` |
| `101` | `M=8; PL=2` | `A` = `2` | `101` → `301` |
| `101` | `M=8; PL=3` | `A` = `3` | `101` → `301` |
| `101` | `M=8; PL=4` | `A` = `4` | `101` → `301` |
| `101` | `M=8; PL=5` | `A` = `5` | `101` → `301` |
| `101` | `M=8; PL=6` | `A` = `6` | `101` → `301` |
| `101` | `M=8; PL=7` | `A` = `7` | `101` → `301` |
| `101` | `M=8; PL=8` | `A` = `8` | `101` → `301` |
| `101` | `M=8; PL=9` | `A` = `9` | `101` → `301` |
| `101` | `M=O/I` | `ADDR_TYPE` = `1`; `M` = `9` | `101` |
| `101` | `M=OFF` | `ADDR_TYPE` = `1`; `M` = `10` | `101` |
| `101` | `M=ON` | `ADDR_TYPE` = `1`; `M` = `11` | `101` |
| `101` | `M=PUL` | `ADDR_TYPE` = `1`; `M` = `15` | `101` |
| `101` | `M=SU_GIU` | `ADDR_TYPE` = `1`; `M` = `12` | `101` |
| `101` | `M=SU_GIU_M` | `ADDR_TYPE` = `1`; `M` = `13` | `101` |
| `101` | `M=O/I; PL=1` | `A` = `1` | `101` → `301` |
| `101` | `M=O/I; PL=2` | `A` = `2` | `101` → `301` |
| `101` | `M=O/I; PL=3` | `A` = `3` | `101` → `301` |
| `101` | `M=O/I; PL=4` | `A` = `4` | `101` → `301` |
| `101` | `M=O/I; PL=5` | `A` = `5` | `101` → `301` |
| `101` | `M=O/I; PL=6` | `A` = `6` | `101` → `301` |
| `101` | `M=O/I; PL=7` | `A` = `7` | `101` → `301` |
| `101` | `M=O/I; PL=8` | `A` = `8` | `101` → `301` |
| `101` | `M=O/I; PL=9` | `A` = `9` | `101` → `301` |
| `101` | `M=OFF; PL=1` | `A` = `1` | `101` → `301` |
| `101` | `M=OFF; PL=2` | `A` = `2` | `101` → `301` |
| `101` | `M=OFF; PL=3` | `A` = `3` | `101` → `301` |
| `101` | `M=OFF; PL=4` | `A` = `4` | `101` → `301` |
| `101` | `M=OFF; PL=5` | `A` = `5` | `101` → `301` |
| `101` | `M=OFF; PL=6` | `A` = `6` | `101` → `301` |
| `101` | `M=OFF; PL=7` | `A` = `7` | `101` → `301` |
| `101` | `M=OFF; PL=8` | `A` = `8` | `101` → `301` |
| `101` | `M=OFF; PL=9` | `A` = `9` | `101` → `301` |
| `101` | `M=ON; PL=1` | `A` = `1` | `101` → `301` |
| `101` | `M=ON; PL=2` | `A` = `2` | `101` → `301` |
| `101` | `M=ON; PL=3` | `A` = `3` | `101` → `301` |
| `101` | `M=ON; PL=4` | `A` = `4` | `101` → `301` |
| `101` | `M=ON; PL=5` | `A` = `5` | `101` → `301` |
| `101` | `M=ON; PL=6` | `A` = `6` | `101` → `301` |
| `101` | `M=ON; PL=7` | `A` = `7` | `101` → `301` |
| `101` | `M=ON; PL=8` | `A` = `8` | `101` → `301` |
| `101` | `M=ON; PL=9` | `A` = `9` | `101` → `301` |
| `101` | `M=PUL; PL=1` | `A` = `1` | `101` → `301` |
| `101` | `M=PUL; PL=2` | `A` = `2` | `101` → `301` |
| `101` | `M=PUL; PL=3` | `A` = `3` | `101` → `301` |
| `101` | `M=PUL; PL=4` | `A` = `4` | `101` → `301` |
| `101` | `M=PUL; PL=5` | `A` = `5` | `101` → `301` |
| `101` | `M=PUL; PL=6` | `A` = `6` | `101` → `301` |
| `101` | `M=PUL; PL=7` | `A` = `7` | `101` → `301` |
| `101` | `M=PUL; PL=8` | `A` = `8` | `101` → `301` |
| `101` | `M=PUL; PL=9` | `A` = `9` | `101` → `301` |
| `101` | `M=SU_GIU; PL=1` | `A` = `1` | `101` → `301` |
| `101` | `M=SU_GIU; PL=2` | `A` = `2` | `101` → `301` |
| `101` | `M=SU_GIU; PL=3` | `A` = `3` | `101` → `301` |
| `101` | `M=SU_GIU; PL=4` | `A` = `4` | `101` → `301` |
| `101` | `M=SU_GIU; PL=5` | `A` = `5` | `101` → `301` |
| `101` | `M=SU_GIU; PL=6` | `A` = `6` | `101` → `301` |
| `101` | `M=SU_GIU; PL=7` | `A` = `7` | `101` → `301` |
| `101` | `M=SU_GIU; PL=8` | `A` = `8` | `101` → `301` |
| `101` | `M=SU_GIU; PL=9` | `A` = `9` | `101` → `301` |
| `101` | `M=SU_GIU_M; PL=1` | `A` = `1` | `101` → `301` |
| `101` | `M=SU_GIU_M; PL=2` | `A` = `2` | `101` → `301` |
| `101` | `M=SU_GIU_M; PL=3` | `A` = `3` | `101` → `301` |
| `101` | `M=SU_GIU_M; PL=4` | `A` = `4` | `101` → `301` |
| `101` | `M=SU_GIU_M; PL=5` | `A` = `5` | `101` → `301` |
| `101` | `M=SU_GIU_M; PL=6` | `A` = `6` | `101` → `301` |
| `101` | `M=SU_GIU_M; PL=7` | `A` = `7` | `101` → `301` |
| `101` | `M=SU_GIU_M; PL=8` | `A` = `8` | `101` → `301` |
| `101` | `M=SU_GIU_M; PL=9` | `A` = `9` | `101` → `301` |
| `101` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `101` |
| `101` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `101` |
| `101` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `101` |
| `101` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `101` |
| `101` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `101` |
| `101` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `101` |
| `101` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `101` |
| `101` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `101` |
| `101` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `101` |
| `101` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `101` |
| `102` | `I=0` | `DEST_LEV` = `1`; `INST_LEV` = `1` | `102` |
| `102` | `M=0` | `M` = `0`; `ADDR_TYPE` = `1` | `102` |
| `102` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `102` |
| `102` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `102` |
| `102` | `I=1` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `102` |
| `102` | `M=1` | `T_TIME ` = `1`; `M` = `1`; `ADDR_TYPE` = `1` | `102` |
| `102` | `M=2` | `M` = `1`; `T_TIME ` = `2`; `ADDR_TYPE` = `1` | `102` |
| `102` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `102` |
| `102` | `I=2` | `DEST_LEV` = `2`; `INST_LEV` = `3` | `102` |
| `102` | `I=3` | `DEST_LEV` = `3`; `INST_LEV` = `4` | `102` |
| `102` | `M=3` | `T_TIME ` = `3`; `M` = `1`; `ADDR_TYPE` = `1` | `102` |
| `102` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `102` |
| `102` | `M=4` | `T_TIME ` = `4`; `M` = `1`; `ADDR_TYPE` = `1` | `102` |
| `102` | `I=4` | `DEST_LEV` = `4`; `INST_LEV` = `5` | `102` |
| `102` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `102` |
| `102` | `M=5` | `T_TIME ` = `5`; `M` = `1`; `ADDR_TYPE` = `1` | `102` |
| `102` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `102` |
| `102` | `I=5` | `DEST_LEV` = `5`; `INST_LEV` = `6` | `102` |
| `102` | `I=6` | `DEST_LEV` = `6`; `INST_LEV` = `7` | `102` |
| `102` | `M=6` | `M` = `1`; `T_TIME ` = `6`; `ADDR_TYPE` = `1` | `102` |
| `102` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `102` |
| `102` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `102` |
| `102` | `M=7` | `M` = `1`; `T_TIME ` = `7`; `ADDR_TYPE` = `1` | `102` |
| `102` | `I=7` | `INST_LEV` = `8`; `DEST_LEV` = `7` | `102` |
| `102` | `M=8` | `M` = `1`; `T_TIME ` = `8`; `ADDR_TYPE` = `1` | `102` |
| `102` | `I=8` | `DEST_LEV` = `8`; `INST_LEV` = `9` | `102` |
| `102` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `102` |
| `102` | `I=9` | `DEST_LEV` = `9`; `INST_LEV` = `10` | `102` |
| `102` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `102` |
| `102` | `I=CEN` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `102` |
| `102` | `M=CEN` | `CEN_BUTT_2 ` = `2`; `CEN_BUTT_1 ` = `1` | `102` |
| `102` | `M=O/I` | `M` = `9`; `ADDR_TYPE` = `1` | `102` |
| `102` | `M=OFF` | `M` = `10`; `ADDR_TYPE` = `1` | `102` |
| `102` | `M=ON` | `M` = `11`; `ADDR_TYPE` = `1` | `102` |
| `102` | `M=PUL` | `M` = `15`; `ADDR_TYPE` = `1` | `102` |
| `102` | `M=SU_GIU` | `M` = `12`; `ADDR_TYPE` = `1` | `102` |
| `102` | `M=SU_GIU_M` | `M` = `13`; `ADDR_TYPE` = `1` | `102` |
| `102` | `M=0; PL=1` | `A` = `1` | `102` → `301` |
| `102` | `M=0; PL=2` | `A` = `2` | `102` → `301` |
| `102` | `M=0; PL=3` | `A` = `3` | `102` → `301` |
| `102` | `M=0; PL=4` | `A` = `4` | `102` → `301` |
| `102` | `M=0; PL=5` | `A` = `5` | `102` → `301` |
| `102` | `M=0; PL=6` | `A` = `6` | `102` → `301` |
| `102` | `M=0; PL=7` | `A` = `7` | `102` → `301` |
| `102` | `M=0; PL=8` | `A` = `8` | `102` → `301` |
| `102` | `M=0; PL=9` | `A` = `9` | `102` → `301` |
| `102` | `M=1; PL=1` | `A` = `1` | `102` → `301` |
| `102` | `M=1; PL=2` | `A` = `2` | `102` → `301` |
| `102` | `M=1; PL=3` | `A` = `3` | `102` → `301` |
| `102` | `M=1; PL=4` | `A` = `4` | `102` → `301` |
| `102` | `M=1; PL=5` | `A` = `5` | `102` → `301` |
| `102` | `M=1; PL=6` | `A` = `6` | `102` → `301` |
| `102` | `M=1; PL=7` | `A` = `7` | `102` → `301` |
| `102` | `M=1; PL=8` | `A` = `8` | `102` → `301` |
| `102` | `M=1; PL=9` | `A` = `9` | `102` → `301` |
| `102` | `M=2; PL=1` | `A` = `1` | `102` → `301` |
| `102` | `M=2; PL=2` | `A` = `2` | `102` → `301` |
| `102` | `M=2; PL=3` | `A` = `3` | `102` → `301` |
| `102` | `M=2; PL=4` | `A` = `4` | `102` → `301` |
| `102` | `M=2; PL=5` | `A` = `5` | `102` → `301` |
| `102` | `M=2; PL=6` | `A` = `6` | `102` → `301` |
| `102` | `M=2; PL=7` | `A` = `7` | `102` → `301` |
| `102` | `M=2; PL=8` | `A` = `8` | `102` → `301` |
| `102` | `M=2; PL=9` | `A` = `9` | `102` → `301` |
| `102` | `M=3; PL=1` | `A` = `1` | `102` → `301` |
| `102` | `M=3; PL=2` | `A` = `2` | `102` → `301` |
| `102` | `M=3; PL=3` | `A` = `3` | `102` → `301` |
| `102` | `M=3; PL=4` | `A` = `4` | `102` → `301` |
| `102` | `M=3; PL=5` | `A` = `5` | `102` → `301` |
| `102` | `M=3; PL=6` | `A` = `6` | `102` → `301` |
| `102` | `M=3; PL=7` | `A` = `7` | `102` → `301` |
| `102` | `M=3; PL=8` | `A` = `8` | `102` → `301` |
| `102` | `M=3; PL=9` | `A` = `9` | `102` → `301` |
| `102` | `M=4; PL=1` | `A` = `1` | `102` → `301` |
| `102` | `M=4; PL=2` | `A` = `2` | `102` → `301` |
| `102` | `M=4; PL=3` | `A` = `3` | `102` → `301` |
| `102` | `M=4; PL=4` | `A` = `4` | `102` → `301` |
| `102` | `M=4; PL=5` | `A` = `5` | `102` → `301` |
| `102` | `M=4; PL=6` | `A` = `6` | `102` → `301` |
| `102` | `M=4; PL=7` | `A` = `7` | `102` → `301` |
| `102` | `M=4; PL=8` | `A` = `8` | `102` → `301` |
| `102` | `M=4; PL=9` | `A` = `9` | `102` → `301` |
| `102` | `M=5; PL=1` | `A` = `1` | `102` → `301` |
| `102` | `M=5; PL=2` | `A` = `2` | `102` → `301` |
| `102` | `M=5; PL=3` | `A` = `3` | `102` → `301` |
| `102` | `M=5; PL=4` | `A` = `4` | `102` → `301` |
| `102` | `M=5; PL=5` | `A` = `5` | `102` → `301` |
| `102` | `M=5; PL=6` | `A` = `6` | `102` → `301` |
| `102` | `M=5; PL=7` | `A` = `7` | `102` → `301` |
| `102` | `M=5; PL=8` | `A` = `8` | `102` → `301` |
| `102` | `M=5; PL=9` | `A` = `9` | `102` → `301` |
| `102` | `M=6; PL=1` | `A` = `1` | `102` → `301` |
| `102` | `M=6; PL=2` | `A` = `2` | `102` → `301` |
| `102` | `M=6; PL=3` | `A` = `3` | `102` → `301` |
| `102` | `M=6; PL=4` | `A` = `4` | `102` → `301` |
| `102` | `M=6; PL=5` | `A` = `5` | `102` → `301` |
| `102` | `M=6; PL=6` | `A` = `6` | `102` → `301` |
| `102` | `M=6; PL=7` | `A` = `7` | `102` → `301` |
| `102` | `M=6; PL=8` | `A` = `8` | `102` → `301` |
| `102` | `M=6; PL=9` | `A` = `9` | `102` → `301` |
| `102` | `M=7; PL=1` | `A` = `1` | `102` → `301` |
| `102` | `M=7; PL=2` | `A` = `2` | `102` → `301` |
| `102` | `M=7; PL=3` | `A` = `3` | `102` → `301` |
| `102` | `M=7; PL=4` | `A` = `4` | `102` → `301` |
| `102` | `M=7; PL=5` | `A` = `5` | `102` → `301` |
| `102` | `M=7; PL=6` | `A` = `6` | `102` → `301` |
| `102` | `M=7; PL=7` | `A` = `7` | `102` → `301` |
| `102` | `M=7; PL=8` | `A` = `8` | `102` → `301` |
| `102` | `M=7; PL=9` | `A` = `9` | `102` → `301` |
| `102` | `M=8; PL=1` | `A` = `1` | `102` → `301` |
| `102` | `M=8; PL=2` | `A` = `2` | `102` → `301` |
| `102` | `M=8; PL=3` | `A` = `3` | `102` → `301` |
| `102` | `M=8; PL=4` | `A` = `4` | `102` → `301` |
| `102` | `M=8; PL=5` | `A` = `5` | `102` → `301` |
| `102` | `M=8; PL=6` | `A` = `6` | `102` → `301` |
| `102` | `M=8; PL=7` | `A` = `7` | `102` → `301` |
| `102` | `M=8; PL=8` | `A` = `8` | `102` → `301` |
| `102` | `M=8; PL=9` | `A` = `9` | `102` → `301` |
| `102` | `M=O/I; PL=1` | `A` = `1` | `102` → `301` |
| `102` | `M=O/I; PL=2` | `A` = `2` | `102` → `301` |
| `102` | `M=O/I; PL=3` | `A` = `3` | `102` → `301` |
| `102` | `M=O/I; PL=4` | `A` = `4` | `102` → `301` |
| `102` | `M=O/I; PL=5` | `A` = `5` | `102` → `301` |
| `102` | `M=O/I; PL=6` | `A` = `6` | `102` → `301` |
| `102` | `M=O/I; PL=7` | `A` = `7` | `102` → `301` |
| `102` | `M=O/I; PL=8` | `A` = `8` | `102` → `301` |
| `102` | `M=O/I; PL=9` | `A` = `9` | `102` → `301` |
| `102` | `M=OFF; PL=1` | `A` = `1` | `102` → `301` |
| `102` | `M=OFF; PL=2` | `A` = `2` | `102` → `301` |
| `102` | `M=OFF; PL=3` | `A` = `3` | `102` → `301` |
| `102` | `M=OFF; PL=4` | `A` = `4` | `102` → `301` |
| `102` | `M=OFF; PL=5` | `A` = `5` | `102` → `301` |
| `102` | `M=OFF; PL=6` | `A` = `6` | `102` → `301` |
| `102` | `M=OFF; PL=7` | `A` = `7` | `102` → `301` |
| `102` | `M=OFF; PL=8` | `A` = `8` | `102` → `301` |
| `102` | `M=OFF; PL=9` | `A` = `9` | `102` → `301` |
| `102` | `M=ON; PL=1` | `A` = `1` | `102` → `301` |
| `102` | `M=ON; PL=2` | `A` = `2` | `102` → `301` |
| `102` | `M=ON; PL=3` | `A` = `3` | `102` → `301` |
| `102` | `M=ON; PL=4` | `A` = `4` | `102` → `301` |
| `102` | `M=ON; PL=5` | `A` = `5` | `102` → `301` |
| `102` | `M=ON; PL=6` | `A` = `6` | `102` → `301` |
| `102` | `M=ON; PL=7` | `A` = `7` | `102` → `301` |
| `102` | `M=ON; PL=8` | `A` = `8` | `102` → `301` |
| `102` | `M=ON; PL=9` | `A` = `9` | `102` → `301` |
| `102` | `M=PUL; PL=1` | `A` = `1` | `102` → `301` |
| `102` | `M=PUL; PL=2` | `A` = `2` | `102` → `301` |
| `102` | `M=PUL; PL=3` | `A` = `3` | `102` → `301` |
| `102` | `M=PUL; PL=4` | `A` = `4` | `102` → `301` |
| `102` | `M=PUL; PL=5` | `A` = `5` | `102` → `301` |
| `102` | `M=PUL; PL=6` | `A` = `6` | `102` → `301` |
| `102` | `M=PUL; PL=7` | `A` = `7` | `102` → `301` |
| `102` | `M=PUL; PL=8` | `A` = `8` | `102` → `301` |
| `102` | `M=PUL; PL=9` | `A` = `9` | `102` → `301` |
| `102` | `M=SU_GIU; PL=1` | `A` = `1` | `102` → `301` |
| `102` | `M=SU_GIU; PL=2` | `A` = `2` | `102` → `301` |
| `102` | `M=SU_GIU; PL=3` | `A` = `3` | `102` → `301` |
| `102` | `M=SU_GIU; PL=4` | `A` = `4` | `102` → `301` |
| `102` | `M=SU_GIU; PL=5` | `A` = `5` | `102` → `301` |
| `102` | `M=SU_GIU; PL=6` | `A` = `6` | `102` → `301` |
| `102` | `M=SU_GIU; PL=7` | `A` = `7` | `102` → `301` |
| `102` | `M=SU_GIU; PL=8` | `A` = `8` | `102` → `301` |
| `102` | `M=SU_GIU; PL=9` | `A` = `9` | `102` → `301` |
| `102` | `M=SU_GIU_M; PL=1` | `A` = `1` | `102` → `301` |
| `102` | `M=SU_GIU_M; PL=2` | `A` = `2` | `102` → `301` |
| `102` | `M=SU_GIU_M; PL=3` | `A` = `3` | `102` → `301` |
| `102` | `M=SU_GIU_M; PL=4` | `A` = `4` | `102` → `301` |
| `102` | `M=SU_GIU_M; PL=5` | `A` = `5` | `102` → `301` |
| `102` | `M=SU_GIU_M; PL=6` | `A` = `6` | `102` → `301` |
| `102` | `M=SU_GIU_M; PL=7` | `A` = `7` | `102` → `301` |
| `102` | `M=SU_GIU_M; PL=8` | `A` = `8` | `102` → `301` |
| `102` | `M=SU_GIU_M; PL=9` | `A` = `9` | `102` → `301` |
| `103` | `I=0` | `INST_LEV` = `1`; `DEST_LEV` = `1` | `103` |
| `103` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `103` |
| `103` | `I=1` | `DEST_LEV` = `0`; `INST_LEV` = `1` | `103` |
| `103` | `M=1` | `M` = `1`; `ADDR_TYPE` = `1` | `103` |
| `103` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `103` |
| `103` | `I=2` | `INST_LEV` = `3`; `DEST_LEV` = `2` | `103` |
| `103` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `103` |
| `103` | `M=2` | `M` = `2`; `ADDR_TYPE` = `1` | `103` |
| `103` | `I=3` | `INST_LEV` = `4`; `DEST_LEV` = `3` | `103` |
| `103` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `103` |
| `103` | `M=3` | `M` = `3`; `ADDR_TYPE` = `1` | `103` |
| `103` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `103` |
| `103` | `I=4` | `DEST_LEV` = `4`; `INST_LEV` = `5` | `103` |
| `103` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `103` |
| `103` | `I=5` | `DEST_LEV` = `5`; `INST_LEV` = `6` | `103` |
| `103` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `103` |
| `103` | `I=6` | `DEST_LEV` = `6`; `INST_LEV` = `7` | `103` |
| `103` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `103` |
| `103` | `I=7` | `INST_LEV` = `8`; `DEST_LEV` = `7` | `103` |
| `103` | `I=8` | `DEST_LEV` = `8`; `INST_LEV` = `9` | `103` |
| `103` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `103` |
| `103` | `I=9` | `DEST_LEV` = `9`; `INST_LEV` = `10` | `103` |
| `103` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `103` |
| `103` | `I=CEN` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `103` |
| `103` | `M=0` | `ADDR_TYPE` = `1` | `103` |
| `103` | `M=0; PL=1` | `A` = `1` | `103` → `301` |
| `103` | `M=0; PL=2` | `A` = `2` | `103` → `301` |
| `103` | `M=0; PL=3` | `A` = `3` | `103` → `301` |
| `103` | `M=0; PL=4` | `A` = `4` | `103` → `301` |
| `103` | `M=0; PL=5` | `A` = `5` | `103` → `301` |
| `103` | `M=0; PL=6` | `A` = `6` | `103` → `301` |
| `103` | `M=0; PL=7` | `A` = `7` | `103` → `301` |
| `103` | `M=0; PL=8` | `A` = `8` | `103` → `301` |
| `103` | `M=0; PL=9` | `A` = `9` | `103` → `301` |
| `103` | `M=1; PL=1` | `A` = `1` | `103` → `301` |
| `103` | `M=1; PL=2` | `A` = `2` | `103` → `301` |
| `103` | `M=1; PL=3` | `A` = `3` | `103` → `301` |
| `103` | `M=1; PL=4` | `A` = `4` | `103` → `301` |
| `103` | `M=1; PL=5` | `A` = `5` | `103` → `301` |
| `103` | `M=1; PL=6` | `A` = `6` | `103` → `301` |
| `103` | `M=1; PL=7` | `A` = `7` | `103` → `301` |
| `103` | `M=1; PL=8` | `A` = `8` | `103` → `301` |
| `103` | `M=1; PL=9` | `A` = `9` | `103` → `301` |
| `103` | `M=2; PL=1` | `A` = `1` | `103` → `301` |
| `103` | `M=2; PL=2` | `A` = `2` | `103` → `301` |
| `103` | `M=2; PL=3` | `A` = `3` | `103` → `301` |
| `103` | `M=2; PL=4` | `A` = `4` | `103` → `301` |
| `103` | `M=2; PL=5` | `A` = `5` | `103` → `301` |
| `103` | `M=2; PL=6` | `A` = `6` | `103` → `301` |
| `103` | `M=2; PL=7` | `A` = `7` | `103` → `301` |
| `103` | `M=2; PL=8` | `A` = `8` | `103` → `301` |
| `103` | `M=2; PL=9` | `A` = `9` | `103` → `301` |
| `103` | `M=3; PL=1` | `A` = `1` | `103` → `301` |
| `103` | `M=3; PL=2` | `A` = `2` | `103` → `301` |
| `103` | `M=3; PL=3` | `A` = `3` | `103` → `301` |
| `103` | `M=3; PL=4` | `A` = `4` | `103` → `301` |
| `103` | `M=3; PL=5` | `A` = `5` | `103` → `301` |
| `103` | `M=3; PL=6` | `A` = `6` | `103` → `301` |
| `103` | `M=3; PL=7` | `A` = `7` | `103` → `301` |
| `103` | `M=3; PL=8` | `A` = `8` | `103` → `301` |
| `103` | `M=3; PL=9` | `A` = `9` | `103` → `301` |
| `103` | `M=4` | `ADDR_TYPE` = `1` | `103` |
| `103` | `M=4; PL=1` | `A` = `1` | `103` → `301` |
| `103` | `M=4; PL=2` | `A` = `2` | `103` → `301` |
| `103` | `M=4; PL=3` | `A` = `3` | `103` → `301` |
| `103` | `M=4; PL=4` | `A` = `4` | `103` → `301` |
| `103` | `M=4; PL=5` | `A` = `5` | `103` → `301` |
| `103` | `M=4; PL=6` | `A` = `6` | `103` → `301` |
| `103` | `M=4; PL=7` | `A` = `7` | `103` → `301` |
| `103` | `M=4; PL=8` | `A` = `8` | `103` → `301` |
| `103` | `M=4; PL=9` | `A` = `9` | `103` → `301` |
| `103` | `M=5` | `ADDR_TYPE` = `1` | `103` |
| `103` | `M=5; PL=1` | `A` = `1` | `103` → `301` |
| `103` | `M=5; PL=2` | `A` = `2` | `103` → `301` |
| `103` | `M=5; PL=3` | `A` = `3` | `103` → `301` |
| `103` | `M=5; PL=4` | `A` = `4` | `103` → `301` |
| `103` | `M=5; PL=5` | `A` = `5` | `103` → `301` |
| `103` | `M=5; PL=6` | `A` = `6` | `103` → `301` |
| `103` | `M=5; PL=7` | `A` = `7` | `103` → `301` |
| `103` | `M=5; PL=8` | `A` = `8` | `103` → `301` |
| `103` | `M=5; PL=9` | `A` = `9` | `103` → `301` |
| `103` | `M=6` | `ADDR_TYPE` = `1` | `103` |
| `103` | `M=6; PL=1` | `A` = `1` | `103` → `301` |
| `103` | `M=6; PL=2` | `A` = `2` | `103` → `301` |
| `103` | `M=6; PL=3` | `A` = `3` | `103` → `301` |
| `103` | `M=6; PL=4` | `A` = `4` | `103` → `301` |
| `103` | `M=6; PL=5` | `A` = `5` | `103` → `301` |
| `103` | `M=6; PL=6` | `A` = `6` | `103` → `301` |
| `103` | `M=6; PL=7` | `A` = `7` | `103` → `301` |
| `103` | `M=6; PL=8` | `A` = `8` | `103` → `301` |
| `103` | `M=6; PL=9` | `A` = `9` | `103` → `301` |
| `103` | `M=7` | `ADDR_TYPE` = `1` | `103` |
| `103` | `M=7; PL=1` | `A` = `1` | `103` → `301` |
| `103` | `M=7; PL=2` | `A` = `2` | `103` → `301` |
| `103` | `M=7; PL=3` | `A` = `3` | `103` → `301` |
| `103` | `M=7; PL=4` | `A` = `4` | `103` → `301` |
| `103` | `M=7; PL=5` | `A` = `5` | `103` → `301` |
| `103` | `M=7; PL=6` | `A` = `6` | `103` → `301` |
| `103` | `M=7; PL=7` | `A` = `7` | `103` → `301` |
| `103` | `M=7; PL=8` | `A` = `8` | `103` → `301` |
| `103` | `M=7; PL=9` | `A` = `9` | `103` → `301` |
| `103` | `M=8` | `ADDR_TYPE` = `1` | `103` |
| `103` | `M=8; PL=1` | `A` = `1` | `103` → `301` |
| `103` | `M=8; PL=2` | `A` = `2` | `103` → `301` |
| `103` | `M=8; PL=3` | `A` = `3` | `103` → `301` |
| `103` | `M=8; PL=4` | `A` = `4` | `103` → `301` |
| `103` | `M=8; PL=5` | `A` = `5` | `103` → `301` |
| `103` | `M=8; PL=6` | `A` = `6` | `103` → `301` |
| `103` | `M=8; PL=7` | `A` = `7` | `103` → `301` |
| `103` | `M=8; PL=8` | `A` = `8` | `103` → `301` |
| `103` | `M=8; PL=9` | `A` = `9` | `103` → `301` |
| `103` | `M=O/I` | `ADDR_TYPE` = `1` | `103` |
| `103` | `M=OFF` | `ADDR_TYPE` = `1` | `103` |
| `103` | `M=ON` | `ADDR_TYPE` = `1` | `103` |
| `103` | `M=PUL` | `ADDR_TYPE` = `1` | `103` |
| `103` | `M=SU_GIU` | `ADDR_TYPE` = `1` | `103` |
| `103` | `M=SU_GIU_M` | `ADDR_TYPE` = `1` | `103` |
| `103` | `M=O/I; PL=1` | `A` = `1` | `103` → `301` |
| `103` | `M=O/I; PL=2` | `A` = `2` | `103` → `301` |
| `103` | `M=O/I; PL=3` | `A` = `3` | `103` → `301` |
| `103` | `M=O/I; PL=4` | `A` = `4` | `103` → `301` |
| `103` | `M=O/I; PL=5` | `A` = `5` | `103` → `301` |
| `103` | `M=O/I; PL=6` | `A` = `6` | `103` → `301` |
| `103` | `M=O/I; PL=7` | `A` = `7` | `103` → `301` |
| `103` | `M=O/I; PL=8` | `A` = `8` | `103` → `301` |
| `103` | `M=O/I; PL=9` | `A` = `9` | `103` → `301` |
| `103` | `M=OFF; PL=1` | `A` = `1` | `103` → `301` |
| `103` | `M=OFF; PL=2` | `A` = `2` | `103` → `301` |
| `103` | `M=OFF; PL=3` | `A` = `3` | `103` → `301` |
| `103` | `M=OFF; PL=4` | `A` = `4` | `103` → `301` |
| `103` | `M=OFF; PL=5` | `A` = `5` | `103` → `301` |
| `103` | `M=OFF; PL=6` | `A` = `6` | `103` → `301` |
| `103` | `M=OFF; PL=7` | `A` = `7` | `103` → `301` |
| `103` | `M=OFF; PL=8` | `A` = `8` | `103` → `301` |
| `103` | `M=OFF; PL=9` | `A` = `9` | `103` → `301` |
| `103` | `M=ON; PL=1` | `A` = `1` | `103` → `301` |
| `103` | `M=ON; PL=2` | `A` = `2` | `103` → `301` |
| `103` | `M=ON; PL=3` | `A` = `3` | `103` → `301` |
| `103` | `M=ON; PL=4` | `A` = `4` | `103` → `301` |
| `103` | `M=ON; PL=5` | `A` = `5` | `103` → `301` |
| `103` | `M=ON; PL=6` | `A` = `6` | `103` → `301` |
| `103` | `M=ON; PL=7` | `A` = `7` | `103` → `301` |
| `103` | `M=ON; PL=8` | `A` = `8` | `103` → `301` |
| `103` | `M=ON; PL=9` | `A` = `9` | `103` → `301` |
| `103` | `M=PUL; PL=1` | `A` = `1` | `103` → `301` |
| `103` | `M=PUL; PL=2` | `A` = `2` | `103` → `301` |
| `103` | `M=PUL; PL=3` | `A` = `3` | `103` → `301` |
| `103` | `M=PUL; PL=4` | `A` = `4` | `103` → `301` |
| `103` | `M=PUL; PL=5` | `A` = `5` | `103` → `301` |
| `103` | `M=PUL; PL=6` | `A` = `6` | `103` → `301` |
| `103` | `M=PUL; PL=7` | `A` = `7` | `103` → `301` |
| `103` | `M=PUL; PL=8` | `A` = `8` | `103` → `301` |
| `103` | `M=PUL; PL=9` | `A` = `9` | `103` → `301` |
| `103` | `M=SU_GIU; PL=1` | `A` = `1` | `103` → `301` |
| `103` | `M=SU_GIU; PL=2` | `A` = `2` | `103` → `301` |
| `103` | `M=SU_GIU; PL=3` | `A` = `3` | `103` → `301` |
| `103` | `M=SU_GIU; PL=4` | `A` = `4` | `103` → `301` |
| `103` | `M=SU_GIU; PL=5` | `A` = `5` | `103` → `301` |
| `103` | `M=SU_GIU; PL=6` | `A` = `6` | `103` → `301` |
| `103` | `M=SU_GIU; PL=7` | `A` = `7` | `103` → `301` |
| `103` | `M=SU_GIU; PL=8` | `A` = `8` | `103` → `301` |
| `103` | `M=SU_GIU; PL=9` | `A` = `9` | `103` → `301` |
| `103` | `M=SU_GIU_M; PL=1` | `A` = `1` | `103` → `301` |
| `103` | `M=SU_GIU_M; PL=2` | `A` = `2` | `103` → `301` |
| `103` | `M=SU_GIU_M; PL=3` | `A` = `3` | `103` → `301` |
| `103` | `M=SU_GIU_M; PL=4` | `A` = `4` | `103` → `301` |
| `103` | `M=SU_GIU_M; PL=5` | `A` = `5` | `103` → `301` |
| `103` | `M=SU_GIU_M; PL=6` | `A` = `6` | `103` → `301` |
| `103` | `M=SU_GIU_M; PL=7` | `A` = `7` | `103` → `301` |
| `103` | `M=SU_GIU_M; PL=8` | `A` = `8` | `103` → `301` |
| `103` | `M=SU_GIU_M; PL=9` | `A` = `9` | `103` → `301` |
| `104` | `M=0` | `ADDR_TYPE` = `3`; `M` = `0` | `104` |
| `104` | `M=1` | `ADDR_TYPE` = `3` | `104` |
| `104` | `M=2` | `ADDR_TYPE` = `3` | `104` |
| `104` | `M=3` | `ADDR_TYPE` = `3` | `104` |
| `104` | `M=4` | `ADDR_TYPE` = `3` | `104` |
| `104` | `M=5` | `ADDR_TYPE` = `3` | `104` |
| `104` | `M=6` | `ADDR_TYPE` = `3` | `104` |
| `104` | `M=7` | `ADDR_TYPE` = `3` | `104` |
| `104` | `M=8` | `ADDR_TYPE` = `3` | `104` |
| `104` | `M=O/I` | `ADDR_TYPE` = `3`; `M` = `9` | `104` |
| `104` | `M=OFF` | `ADDR_TYPE` = `3`; `M` = `10` | `104` |
| `104` | `M=ON` | `ADDR_TYPE` = `3`; `M` = `11` | `104` |
| `104` | `M=PUL` | `ADDR_TYPE` = `3`; `M` = `15` | `104` |
| `104` | `M=SU_GIU` | `ADDR_TYPE` = `3`; `M` = `12` | `104` |
| `104` | `M=SU_GIU_M` | `ADDR_TYPE` = `3`; `M` = `13` | `104` |
| `104` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `104` |
| `104` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `104` |
| `104` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `104` |
| `104` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `104` |
| `104` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `104` |
| `104` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `104` |
| `104` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `104` |
| `104` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `104` |
| `104` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `104` |
| `104` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `104` |
| `104` | `I=0` | `DEST_LEV` = `1` | `104` |
| `104` | `I=1` | `DEST_LEV` = `0` | `104` |
| `104` | `I=2` | `DEST_LEV` = `2` | `104` |
| `104` | `I=3` | `DEST_LEV` = `3` | `104` |
| `104` | `I=4` | `DEST_LEV` = `4` | `104` |
| `104` | `I=5` | `DEST_LEV` = `5` | `104` |
| `104` | `I=6` | `DEST_LEV` = `6` | `104` |
| `104` | `I=7` | `DEST_LEV` = `7` | `104` |
| `104` | `I=8` | `DEST_LEV` = `8` | `104` |
| `104` | `I=9` | `DEST_LEV` = `9` | `104` |
| `104` | `I=CEN` | `DEST_LEV` = `10` | `104` |
| `105` | `I=0` | `DEST_LEV` = `1`; `INST_LEV` = `1` | `105` |
| `105` | `M=0` | `M` = `0`; `ADDR_TYPE` = `3` | `105` |
| `105` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `105` |
| `105` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `105` |
| `105` | `I=1` | `INST_LEV` = `1`; `DEST_LEV` = `0` | `105` |
| `105` | `M=1` | `T_TIME ` = `1`; `M` = `1`; `ADDR_TYPE` = `3` | `105` |
| `105` | `M=2` | `M` = `1`; `T_TIME ` = `2`; `ADDR_TYPE` = `3` | `105` |
| `105` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `105` |
| `105` | `I=2` | `DEST_LEV` = `2`; `INST_LEV` = `3` | `105` |
| `105` | `I=3` | `DEST_LEV` = `3`; `INST_LEV` = `4` | `105` |
| `105` | `M=3` | `T_TIME ` = `3`; `M` = `1`; `ADDR_TYPE` = `3` | `105` |
| `105` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `105` |
| `105` | `M=4` | `T_TIME ` = `4`; `M` = `1`; `ADDR_TYPE` = `3` | `105` |
| `105` | `I=4` | `DEST_LEV` = `4`; `INST_LEV` = `5` | `105` |
| `105` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `105` |
| `105` | `M=5` | `T_TIME ` = `5`; `M` = `1`; `ADDR_TYPE` = `3` | `105` |
| `105` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `105` |
| `105` | `I=5` | `DEST_LEV` = `5`; `INST_LEV` = `6` | `105` |
| `105` | `I=6` | `DEST_LEV` = `6`; `INST_LEV` = `7` | `105` |
| `105` | `M=6` | `M` = `1`; `T_TIME ` = `6`; `ADDR_TYPE` = `3` | `105` |
| `105` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `105` |
| `105` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `105` |
| `105` | `M=7` | `M` = `1`; `T_TIME ` = `7`; `ADDR_TYPE` = `3` | `105` |
| `105` | `I=7` | `INST_LEV` = `8`; `DEST_LEV` = `7` | `105` |
| `105` | `M=8` | `M` = `1`; `T_TIME ` = `8`; `ADDR_TYPE` = `3` | `105` |
| `105` | `I=8` | `DEST_LEV` = `8`; `INST_LEV` = `9` | `105` |
| `105` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `105` |
| `105` | `I=9` | `DEST_LEV` = `9`; `INST_LEV` = `10` | `105` |
| `105` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `105` |
| `105` | `I=CEN` | `INST_LEV` = `1`; `DEST_LEV` = `10` | `105` |
| `105` | `M=CEN` | `CEN_BUTT_2 ` = `2`; `CEN_BUTT_1 ` = `1` | `105` |
| `105` | `M=O/I` | `M` = `9`; `ADDR_TYPE` = `3` | `105` |
| `105` | `M=OFF` | `M` = `10`; `ADDR_TYPE` = `3` | `105` |
| `105` | `M=ON` | `M` = `11`; `ADDR_TYPE` = `3` | `105` |
| `105` | `M=PUL` | `M` = `15`; `ADDR_TYPE` = `3` | `105` |
| `105` | `M=SU_GIU` | `M` = `12`; `ADDR_TYPE` = `3` | `105` |
| `105` | `M=SU_GIU_M` | `M` = `13`; `ADDR_TYPE` = `3` | `105` |
| `106` | `I=0` | `INST_LEV` = `1`; `DEST_LEV` = `1` | `106` |
| `106` | `AUX=0` | `IN_AUX_CHANNEL` = `0` | `106` |
| `106` | `I=1` | `DEST_LEV` = `0`; `INST_LEV` = `1` | `106` |
| `106` | `M=1` | `M` = `1`; `ADDR_TYPE` = `3` | `106` |
| `106` | `AUX=1` | `IN_AUX_CHANNEL` = `1` | `106` |
| `106` | `I=2` | `INST_LEV` = `3`; `DEST_LEV` = `2` | `106` |
| `106` | `AUX=2` | `IN_AUX_CHANNEL` = `2` | `106` |
| `106` | `M=2` | `M` = `2`; `ADDR_TYPE` = `3` | `106` |
| `106` | `I=3` | `INST_LEV` = `4`; `DEST_LEV` = `3` | `106` |
| `106` | `AUX=3` | `IN_AUX_CHANNEL` = `3` | `106` |
| `106` | `M=3` | `M` = `3`; `ADDR_TYPE` = `3` | `106` |
| `106` | `AUX=4` | `IN_AUX_CHANNEL` = `4` | `106` |
| `106` | `I=4` | `DEST_LEV` = `4`; `INST_LEV` = `5` | `106` |
| `106` | `AUX=5` | `IN_AUX_CHANNEL` = `5` | `106` |
| `106` | `I=5` | `DEST_LEV` = `5`; `INST_LEV` = `6` | `106` |
| `106` | `AUX=6` | `IN_AUX_CHANNEL` = `6` | `106` |
| `106` | `I=6` | `DEST_LEV` = `6`; `INST_LEV` = `7` | `106` |
| `106` | `AUX=7` | `IN_AUX_CHANNEL` = `7` | `106` |
| `106` | `I=7` | `INST_LEV` = `8`; `DEST_LEV` = `7` | `106` |
| `106` | `I=8` | `DEST_LEV` = `8`; `INST_LEV` = `9` | `106` |
| `106` | `AUX=8` | `IN_AUX_CHANNEL` = `8` | `106` |
| `106` | `I=9` | `DEST_LEV` = `9`; `INST_LEV` = `10` | `106` |
| `106` | `AUX=9` | `IN_AUX_CHANNEL` = `9` | `106` |
| `106` | `I=CEN` | `INST_LEV` = `1`; `DEST_LEV` = `10` | `106` |
| `106` | `M=0` | `ADDR_TYPE` = `3` | `106` |
| `106` | `M=4` | `ADDR_TYPE` = `3` | `106` |
| `106` | `M=5` | `ADDR_TYPE` = `3` | `106` |
| `106` | `M=6` | `ADDR_TYPE` = `3` | `106` |
| `106` | `M=7` | `ADDR_TYPE` = `3` | `106` |
| `106` | `M=8` | `ADDR_TYPE` = `3` | `106` |
| `106` | `M=O/I` | `ADDR_TYPE` = `3` | `106` |
| `106` | `M=OFF` | `ADDR_TYPE` = `3` | `106` |
| `106` | `M=ON` | `ADDR_TYPE` = `3` | `106` |
| `106` | `M=PUL` | `ADDR_TYPE` = `3` | `106` |
| `106` | `M=SU_GIU` | `ADDR_TYPE` = `3` | `106` |
| `106` | `M=SU_GIU_M` | `ADDR_TYPE` = `3` | `106` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1524` and the installed model | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware without treating wildcard sentinels as literal installed values | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`400`, `401`, `402`, `403`, `404`, `405`, `406`, `408`, `409`, `427`, `430`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions, and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

### Existing Device-specific diagnostic notes


| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 16`, brand, line, and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe physical firmware despite wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3`, `6`, `13` | hardware, microcontroller, Device ID when supported | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | determine selected Objects on the two Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine Module system/address configuration | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability


Depending on configuration, this Device crosses multiple OpenWebNet domains. The Device definition establishes that those roles can exist on this hardware; the linked functional references remain authoritative for wire semantics.

- [`WHO 1` - Lighting](../../functional/who-1-lighting/)
- [`WHO 2` - Automation](../../functional/who-2-automation/)
- scenario/`CEN` behavior
- sound diffusion
- video door-entry related control
- `AUX`/transversal control

## Observed behavior and corroboration

No additional publishable runtime observation is asserted beyond observations explicitly retained elsewhere on this page.

## Programming


A correct programmer must evaluate `SPE`, `M`, address-scope fields, level/interface fields, and the associated condition/conversion graph before selecting an Object. It must not treat “Special control” as one fixed Object.

See [Configuration Programming](../../programming/configuration-programming.md) and [Programming Validation](../../programming/validation.md).

## Source reconciliation


The nine-page `MQ00285-d-EN` sheet has been reconciled as a Device-specific function map rather than only as a list of reusable Objects:

- lighting functions include simple, timed, dimming and special light-control variants selected through `M`, `SPE` and the level fields;
- `LIV1` / `LIV2` participate in published dimming/special-function selection and must not be treated as generic numeric fields without the surrounding mode;
- automation, Device lock/unlock, scenario-module, programmed-scenario, PLUS-scenario, video-door-entry, staircase/floor-call, sound-system and `AUX` roles share the same Physical Device but use different button/address semantics;
- the sheet documents programming/editing behavior for scenario functions, including product-level activation/programming distinctions that are not visible from Object identity alone;
- operation across SCS/SCS interfaces uses installation/destination-level concepts that correspond to reusable `INST_LEV` / `DEST_LEV` fields;
- audio/video and sound roles reuse `PL/PF`, level and special-function fields contextually, so a validator must interpret them only after resolving the selected function family.

This source is now represented as a product-specific selector/function model. Remaining gaps are commercial variants, exact package relationships and hardware corroboration, not omission of the principal published function families.

## Evidence limits and open work


- Archive and hash `MQ00285-d-EN`, language variants, and any earlier/later revisions.
- Locate authoritative product sheets for the other nine records sharing item `1524`.
- Capture known hardware to corroborate `modobj`, expected physical configurator count, firmware, Object projection, addressing, and configuration.
- Review every condition/conversion branch against the published function tables, preserving mismatches or implementation-only branches.
- Determine the exact commercial/package relationships across Arnould, BTicino, Legrand Arteor, Céliane, and Mosaic records.

## Sources


- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
- [Programming](../../programming/)
