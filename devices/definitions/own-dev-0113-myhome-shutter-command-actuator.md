# MYHOME shutter command and actuator

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0113` | Project identity |
| Technical description | MYHOME shutter command and actuator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `H4672M2S`, `LN4672M2S`, `067587` | All three SKU-to-item mappings explicitly established by the manufacturer catalogue |
| Catalogue item | `2248` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `112` | Main association; independent of project ID |
| Firmware definition | `775` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `4` | Firmware metadata |
| Categories | Actuators, Commands, User interfaces, Multifunction devices | Source-derived roles |

The catalogue defines one Shutter actuator Module, two command Modules and a separate User interface Module. Four logical Modules do not establish four physical outputs. The manufacturer catalogue explicitly establishes all three SKU-to-item mappings. Exact-product PDFs have not been found; physical specifications remain a documentation gap.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4672M2S` | Established catalogue identity | `EN_DEVICE` record `2604` explicitly links this SKU to item `2248` |
| BTicino | `LN4672M2S` | Established catalogue identity | `EN_DEVICE` record `2603` explicitly links this SKU to item `2248` |
| Legrand - Céliane | `067587` | Established catalogue identity | `EN_DEVICE` record `2605` explicitly links this SKU to item `2248` |

The manufacturer catalogue explicitly links all three SKUs to this technical item through `EN_DEVICE.id_item` relationships. It labels the H reference Axolute, the LN reference Living (internal `L/N/NT`), and the Legrand reference Céliane. Those catalogue identities are established independently of PDF availability. Online searches did not locate exact-product sheets; unavailable product endpoints do not invalidate the catalogue records. The retained similar-reference source describes `AR-67587` as an Epure tiltable detector. It is excluded as product evidence: reference resemblance does not establish equivalence or contradict these SKU-to-item mappings.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `F01716EN-02.pdf` | English technical sheet; excluded similar-reference evidence | `F01716EN/02; updated 30/03/2021, created 11/12/2015` | AR-67587 is an Epure tiltable detector, not the catalogue shutter command/actuator. Identity/range p. 1; printed/PDF pp. 1-2 coincide. No specifications transferred. | [Archived original](https://archive.openwebnet-ha.org/sha256/f9/08/f908842d39926550837120ecf15295b5fccccac08e26cb9ebb174af13365da09.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/F01716EN-02.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2248`: all firmware/commercial/system/Object/Module/Virgin/field/filter/mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Catalogue-described format | Two-module reference suffix; exact physical format not independently corroborated | Canonical commercial description/reference; not a measured assembly |
| Dimensions, supply/current, operating/storage range | Unknown for these catalogue-established identities | No exact matching retained manufacturer specification |
| Outputs, contacts, motor/load ratings and mounting | Unknown for the physical Device | Logical actuator/command topology is not a load rating or wiring diagram |
| Keys, covers, LEDs, sensors and configurator sockets | Unknown physical arrangement | Reusable UI/configuration fields do not prove construction |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2248` | Canonical catalogue |
| Technical item description | Comando-Attuatore MYHOME Tapparelle | Canonical catalogue |
| Item family | 0; key `2` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `112` | `AS_ITEM_SYSTEM` |
| Commercial record count | `3` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `775` | `1` | `0` | No build row | `4` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `775` | `1` | `218` Shutter actuator | Fixed/designated metadata | `3081` | `514` | `1474` |
| `775` | `2` | `400` Light control | Fixed/designated metadata | `3109` | `400` | `1493` |
| `775` | `2` | `401` Automation control | Candidate alternative | `3103` | `401` | `1490` |
| `775` | `2` | `402` Lock/unlock actuator control | Candidate alternative | `3101` | `402` | `1489` |
| `775` | `2` | `406` Scheduled scenario PLUS | Candidate alternative | `3099` | `406` | `1488` |
| `775` | `2` | `408` Open lock control | Candidate alternative | `3097` | `408` | `1487` |
| `775` | `2` | `427` Floor call control | Candidate alternative | `3112` | `427` | `1495` |
| `775` | `2` | `430` Staircase light control | Candidate alternative | `3095` | `430` | `1486` |
| `775` | `2` | `463` Load control actuator visualization | Candidate alternative | `3083` | `492` | `1476` |
| `775` | `2` | `145` Shutter control (2 slots) | Candidate alternative | `3125` | `650` | `1504` |
| `775` | `3` | `400` Light control | Fixed/designated metadata | `3110` | `400` | `1493` |
| `775` | `3` | `401` Automation control | Candidate alternative | `3104` | `401` | `1490` |
| `775` | `3` | `402` Lock/unlock actuator control | Candidate alternative | `3102` | `402` | `1489` |
| `775` | `3` | `406` Scheduled scenario PLUS | Candidate alternative | `3100` | `406` | `1488` |
| `775` | `3` | `408` Open lock control | Candidate alternative | `3098` | `408` | `1487` |
| `775` | `3` | `427` Floor call control | Candidate alternative | `3113` | `427` | `1495` |
| `775` | `3` | `430` Staircase light control | Candidate alternative | `3096` | `430` | `1486` |
| `775` | `3` | `463` Load control actuator visualization | Candidate alternative | `3084` | `492` | `1476` |
| `775` | `4` | `143` User interface settings for command | Fixed/designated metadata | `3111` | `644` | `1494` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `775` | `501` Special double command virgin | `2`, `3` | `400`, `401`, `402`, `403`, `404`, `405`, `406`, `407`, `408`, `409`, `427`, `430` | `501` | `99` |

Slot `1` designates Shutter actuator Object `218` (catalogue key `514`). Command slots `2/3` each have eight common alternatives: `400`, `401`, `402`, `406`, `408`, `427`, `430`, `463`. Two-slot Object `145` has one stored starting placement at slot `2`; UI Object `143` is in slot `4`. Virgin Object `501` covers command slots `2/3` only. Virgin `501` permits `400..409`, `427` and `430`, while direct firmware membership excludes `403/404/405/407/409` and adds `145/463`; these relations must remain separate. No selection predicate or conversion rule reconciles them automatically.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `775` | Virtual Configuration | `1` | Association key `1` |
| `775` | Advanced Configuration | `2` | Association key `2` |
| `775` | Physical configuration | `0` | Association key `3` |


No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `775` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `775` | `A1` | `0..9` | `0` | Configurator A1 (0-9) |
| `775` | `PL1` | `0..9` | `0` | PL1 - (0-9) |
| `775` | `M1` | `0..1`; `3..7`; `10` = `OFF`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `15` = `PUL` | `0` | Modality; Mode physical configurator (0-8, `O/I`,`OFF`,`ON`,SU_GIU,SU_GIU_M,`CEN`,`PUL`) |
| `775` | `A2` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB` | `0` | Automation A addressing space (for configurator A2) |
| `775` | `PL2` | `0..9` | `0` | PL2 - (0-9) |
| `775` | `M2` | `0..8`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `15` = `PUL` | `0` | Modality; Mode physical configurator (0-8, `O/I`,`OFF`,`ON`,SU_GIU,SU_GIU_M,`CEN`,`PUL`) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `400` - Light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `1` = Timed `ON`; `2` = Toggle dimmer; `3` = `ON`/`OFF` and dimming; `4` = Toggle `ON`/`OFF`; `5` = `ON`/`OFF`; `9` = `ON`/`OFF` and point to point dimming; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90%; `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `130` = Customized `ON`/`OFF` and point to point dimmer; `131` = Customized toggle dimmer; `132` = Customized `ON`/`OFF` and dimmer; `133` = Customized toggle dimmer without regulation; `134` = Customized `ON`/`OFF` and dimmer without regulation | `0` | Modality; Standard mode means: with regulation for Point-to-point addressing, without regulation for Area, Group and General addressing |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
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
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |


### Object `402` - Lock/unlock actuator control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `1` = Disable (lower button); `2` = Enable (lower button); `3` = Disable (lower button) - enable (upper button) | `1` | Modality |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |


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


### Object `463` - Load control actuator visualization

Catalogue Object key `492` maps to external Object `463`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PRIORITY` | `0..63` | `1` | Priority |
| `PHASE` | `0` = Single phase; `1` = Phase 1; `2` = Phase 2; `3` = Phase 3 | `0` | Phase |


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


### Object `143` - User interface settings for command

Catalogue Object key `644` maps to external Object `143`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LED_LEVEL_COMMANDS` | `0` = `OFF`; `1` = Minimum level; `2` = Medium level; `3` = Maximum level | `2` | LED intensity level |
| `ENABLE_DISABLE_LED_COMMAND` | `0` = All Led Enabled; `1` = Presence Led Enabled - State Update Led Disable; `2` = Presence Led Disable - State Update Led Enable; `3` = All Led Disable | `0` | Enable-Disable LED |
| `PRESENCE_LED_INTENSITY_LEVEL_COMMAND` | `0` = Standard level; `1` = High intensity level | `0` | Presence LED intensity level |


### Object `145` - Shutter control (2 slots)

Catalogue Object key `650` maps to external Object `145`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Bistable control; `1` = Monostable control; `2` = Blades control and bistable; `3` = Bistable and blades control | `0` | Modality; Mode (0,1,2,3) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; installation and destination levels are separately scoped fields |
| `A` | `0..10` | `0` | Area; See Automation System Addressing |
| `PL` | `0..15` | `0` | Light point; See Automation System Addressing |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level; See Automation System Addressing |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `15` = Local bus 15; `16` = All systems | `0` | Destination level; See Automation System Addressing |
| `A_R` | `0..10` | `0` | Area of reference actuator |
| `PL_R` | `0..15` | `0` | Light point of reference actuator |
| `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety | `1` | Priority; Shutter management command priority |
| `PRE` | `1..9`; `0` = None | `0` | Preset; Shutter management preset number |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `775` | `400` | `3533` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `775` | `400` | `3534` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `775` | `400` | `3535` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `775` | `401` | `3530` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `775` | `401` | `3531` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `775` | `401` | `3532` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `775` | `402` | `3527` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `775` | `402` | `3528` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `775` | `402` | `3529` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `775` | `408` | `3526` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `775` | `427` | `3538` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `775` | `430` | `3525` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `775` | `430` | `4128` | `N2` | `0..15` (entire reusable range retained) | `0` | Associated Internal Unit address - hundreds |
| `775` | `430` | `4141` | `N1` | `100..255` | `0` | Internal unit address; reusable default `0` is outside this subset; filter supplies no replacement default |
| `775` | `218` | `4445` | `UP_SHUTTER_TIME_MINUTES` | `0..9` (entire reusable range retained) | `0` | UP shutter calbration time (m) |
| `775` | `218` | `4458` | `UP_SHUTTER_TIME_SECONDS` | `0..59` (entire reusable range retained) | `0` | UP shutter calbration time (s) |
| `775` | `218` | `4471` | `DOWN_SHUTTER_TIME_MINUTES` | `0..9` (entire reusable range retained) | `0` | DOWN shutter calbration time (m) |
| `775` | `218` | `4484` | `SLATS_ROTATION_TIME_DOWN_H` | `0..27` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is all the way down - HIGH BYTE (ms) |
| `775` | `218` | `4497` | `SLATS_ROTATION_TIME_DOWN_L` | `0..255` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is all the way down - LOW BYTE (ms) |
| `775` | `218` | `4510` | `SLATS_ROTATION_TIME_MIDDLE_H` | `0..27` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is in middle position - HIGH BYTE (ms) |
| `775` | `218` | `4523` | `SLATS_ROTATION_TIME_MIDDLE_L` | `0..255` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is in middle position - LOW BYTE (ms) |
| `775` | `218` | `4536` | `SLATS_ROTATION_STEP_NUMBER` | `3..100` (entire reusable range retained) | `4` | SLATS ROTATION step number |
| `775` | `218` | `4618` | `SHUTTER_TYPE` | `3` = Standard with slats | `0` | Motor type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `775` | `143` | `3536` | `ENABLE_DISABLE_LED_COMMAND` | `0` = All Led Enabled; `1` = Presence Led Enabled - State Update Led Disable; `2` = Presence Led Disable - State Update Led Enable; `3` = All Led Disable (entire reusable range retained) | `0` | Enable-Disable LED |
| `775` | `143` | `3537` | `PRESENCE_LED_INTENSITY_LEVEL_COMMAND` | `0` = Standard level; `1` = High intensity level (entire reusable range retained) | `0` | Presence LED intensity level |
| `775` | `145` | `3539` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `775` | `145` | `3540` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `775` | `145` | `3541` | `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety (entire reusable range retained) | `1` | Priority |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion reference is attached to these slot rows. Resolve the active Object and apply its firmware-specific domain restrictions separately. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `112` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Read installed firmware and compare with the applicability table | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Obtain hardware revision; no source-backed installed value | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Obtain microcontroller identity; no fingerprint retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve active Modules/Objects independently of candidate metadata | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Corroborate installed addressing and distinguish physical from reusable ranges | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Compare installed configuration with the exact firmware/Object restrictions | [Configuration](../../diagnostics/dim35-configuration.md) |

These are catalogue-derived diagnostic candidates. No Device-specific response or support across all commercial variants is established by a hardware capture.

## Functional applicability

| Role | Conditional applicability | Canonical evidence / reference |
| --- | --- | --- |
| Shutter actuator | One designated Object `218` placement; exact accepted motor/configuration scope requires corroboration | [`WHO 2`](../../functional/who-2-automation/) |
| Lighting command | Object `400` when selected; address, reference actuator, dimming and timing domains are configuration metadata | [`WHO 1`](../../functional/who-1-lighting/) |
| Automation command | Object `401` or two-slot Object `145` when selected; motor actuation requires a separate actuator role | [`WHO 2`](../../functional/who-2-automation/) |
| Actuator lock/unlock | Object `402`; configured actuator eligibility rather than a physical lock output | Object `402` catalogue association |
| Scheduled scenario PLUS | Object `406`; scenario number, button and auxiliary-event fields as defined | [CEN+ in `WHO 25`](../../functional/who-25-transversal/cen-plus.md) |
| Video-entry command | Object `408` lock, `427` floor call or `430` staircase light when selected | [`WHO 6`](../../functional/who-6-basic-video-door-entry/) |
| Load management | Object `463` visualization/override; not evidence of built-in metering | [`WHO 18`](../../functional/who-18-energy-management/) |
| Command UI | Object `143`; configured indicators do not establish physical LEDs or sensors | Reusable catalogue UI definition |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The catalogue configuration modes and firmware `775` associations are listed above. Resolve the active Object and preserve the command, actuator and UI placements separately. Candidate membership is not simultaneous activation, and a multi-slot Object cannot be assumed to coexist with another Object occupying its span. No slot-condition or referenced conversion row supplies selection precedence.

Apply the Object `218` motor-type restriction before considering calibration. The retained high/low-byte labels name a split source representation; no tested conversion or calibration sequence is established here. Do not prescribe movement or infer a safe motor rating without the exact physical product and manufacturer wiring instructions.

Object `430` N1 is restricted to `100..255`, excluding default `0`; no replacement is established. Object `145` DEST_LEV omits value `14` in both its reusable domain and the retained filter, even though similarly named destination domains include it. Preserve those exact scopes. No exact-product manual establishes commissioning, reset, transfer, update, physical configurator meanings or wiring; those procedures remain open rather than borrowed from similarly named controls.

## Source reconciliation

The complete canonical catalogue defines this technical item and its catalogue-established identities, firmware, Module/Object/Virgin topology, legal fields, filters, modes and related parameter/connection/package metadata. The retained publisher source is incorporated as excluded similar-reference evidence only. Its dimensions, electrical ratings, functions and installation instructions describe a different product and are not attributed to this Device.

| Issue | Reconciliation / unresolved limit | Evidence |
| --- | --- | --- |
| Catalogue identity | All three SKUs explicitly map to item `2248`; missing exact-product PDFs affect documentation coverage, not identity status | Canonical `EN_DEVICE` records |
| Excluded source applicability | The retained similar-reference source describes a different product/line. No equivalence is established, and its specifications are not transferred; this does not invalidate the catalogue mappings | Documentation inventory and source-scoped comparison |
| Shared item versus physical substitution | The H, LN and Legrand references share this catalogue technical item. That grouping does not establish interchangeable physical parts or equivalence to newer Living Now K-series products | Explicit catalogue mappings; physical interchangeability not documented |
| Firmware build | Firmware `775` is `1.0` with no build row; not default. Neither catalogue status nor absent build proves a shipped release | Canonical EN_FIRMWARE / build associations |
| Staircase-light default | Object `430` N1 effective domain `100..255` excludes default `0`; no replacement | Attached firmware filter |
| Destination-domain hole | Object `145` DEST_LEV omits `14`; similar domains do not fill the gap | Reusable Object and firmware filter |
| Virgin/direct membership | Allowed generic Virgin Objects and firmware-associated active Objects differ; no automatic conversion is proven | Exact relations enumerated above |
| Motor-type restriction | Object `218` SHUTTER_TYPE is restricted to `3` Standard with slats, excluding reusable default `0`; no replacement | Filter `4618` |
| Calibration fields | Up/down travel and slat timing HIGH/LOW fields and step count are reusable configuration values, not measurements from installed hardware | Object `218` and nine attached actuator filters |
| Firmware selector prose | M1/M2 descriptions mention values, including `CEN`, beyond their stored legal subsets. M1 and M2 have distinct domains and A1 differs from A2 | Seven firmware fields including AID |

## Evidence limits and open work

- Locate exact-product sheets, instructions or packaging for `H4672M2S`, `LN4672M2S` and `067587` to establish physical specifications and product-specific procedures.
- Establish physical ratings, wiring, mounting, controls and complete commissioning/reset/update procedures.
- Inspect registered parameter payloads and corroborate accepted Object selection, Virgin transitions, multi-slot occupancy and firmware restrictions.
- Obtain sanitized hardware evidence for installed firmware/build, hardware revision, MCU identity and functional behavior; none is retained.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
