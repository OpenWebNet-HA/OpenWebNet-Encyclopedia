# Extended control

## Summary

This two-module extended SCS control sends configured lighting, automation, scenario or sound commands. Its installation-level selectors allow commands to target the local bus, logically expanded sections or the main riser, making it useful in installations with several bus domains.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0014` | Project identity |
| Technical description | Two-module extended configurable command | Catalogue + official MyHOME documentation |
| Catalogue item | `1104` - “Extended control item” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `9` | Implementation evidence |
| Firmware definition | wildcard `-1.-1.-1`, firmware `153` | Implementation evidence |
| Declared Modules | `2` | Implementation evidence |
| Configuration modes | Physical, Virtual | Implementation evidence |
| Categories | Command, Multifunction | Capability model |

The Extended control is a two-Module configurable command whose catalogue capability model spans lighting, automation, locking, scenario, `AUX`, video-door-entry and sound-diffusion roles. It is therefore best treated as a multifunction command platform rather than as one fixed functional button.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4655` | Documented commercial identity | Catalogue + archived MyHOME Automation guide |
| BTicino - LivingLight | `L4655` | Documented commercial identity | Catalogue + archived MyHOME Automation guide |
| Legrand - Mosaic | `078466` | Shared technical item | Implementation evidence; direct product document pending |
| Legrand - Mosaic | `078467` | Shared technical item | Implementation evidence; direct product document pending |
| Legrand - Mosaic | `078469` | Shared technical item | Implementation evidence; direct product document pending |
| Legrand - Mosaic | `079266` | Shared technical item | Implementation evidence; direct product document pending |
| Legrand - Mosaic | `079267` | Shared technical item | Implementation evidence; direct product document pending |
| Legrand - Mosaic | `079269` | Shared technical item | Implementation evidence; direct product document pending |

The archived MyHOME Automation guide also associates the extended-control function with historical catalogue references used in older ranges. Those references should be added to the commercial index only after the exact printed-reference relationship has been checked against the corresponding catalogue revision.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Automation guide | System / product guide | revision/date not yet pinned | `H4655` / `L4655`: index on printed p. 2 / PDF p. 4; substantive mentions on printed pp. 36, 58, 61, 70, 87, 88, 91, 133, 160 / PDF pp. 38, 60, 63, 72, 89, 90, 93, 135, 162 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/80/6a/806a55bffb924f5ef7b25398432c0a86ab210722adc30b81f33558c6ec36f561.pdf) | publisher source not currently retained |

The guide documents cross-bus / extended-control use cases. Direct sheets for the six Mosaic references remain a documentation gap.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2-module configurable command | Catalogue + archived MyHOME Automation guide |
| Physical configuration surface | `A`, `PL`, `M`, `LIV1`, `LIV2`, `SPE`, `I` | Archived MyHOME Automation guide + implementation evidence |
| Installation-level selector | `I` distinguishes local section, logical-expansion buses and main riser | Archived MyHOME Automation guide |

These physical/configuration facts describe the command surface. Electrical ratings not established in the retained source set remain an evidence gap rather than being inferred.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1104` | Implementation evidence |
| Main system | Lighting / Automation | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `9` | Implementation evidence |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `153` | `-1` | `-1` | `-1` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Wildcard values are catalogue applicability sentinels, not claims about an installed firmware version.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `153` | `1` | `400` Light control | Fixed/designated metadata | `701` | `400` | `486` |
| `153` | `1` | `401` Automation control | Candidate alternative | `703` | `401` | `487` |
| `153` | `1` | `402` Lock/unlock actuator control | Candidate alternative | `705` | `402` | `488` |
| `153` | `1` | `403` Scenario module control | Candidate alternative | `707` | `403` | `489` |
| `153` | `1` | `404` Scheduled scenario | Candidate alternative | `709` | `404` | `490` |
| `153` | `1` | `407` `AUX` control | Candidate alternative | `711` | `407` | `491` |
| `153` | `1` | `408` Open lock control | Candidate alternative | `713` | `408` | `492` |
| `153` | `1` | `409` Sound diffusion control | Candidate alternative | `715` | `409` | `493` |
| `153` | `2` | `400` Light control | Fixed/designated metadata | `702` | `400` | `486` |
| `153` | `2` | `401` Automation control | Candidate alternative | `704` | `401` | `487` |
| `153` | `2` | `402` Lock/unlock actuator control | Candidate alternative | `706` | `402` | `488` |
| `153` | `2` | `403` Scenario module control | Candidate alternative | `708` | `403` | `489` |
| `153` | `2` | `404` Scheduled scenario | Candidate alternative | `710` | `404` | `490` |
| `153` | `2` | `407` `AUX` control | Candidate alternative | `712` | `407` | `491` |
| `153` | `2` | `408` Open lock control | Candidate alternative | `714` | `408` | `492` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `153` | `501` Special double command virgin | `1`, `2` | `400`, `401`, `402`, `403`, `404`, `405`, `406`, `407`, `408`, `409`, `427`, `430` | `501` | `27` |

The firmware provides two configurable Modules. Direct firmware/Object associations are:
Virgin Object `501`, **Special double command virgin**, applies to both slots and permits the direct Objects above plus:
- `405` Scenario PLUS Lighting Management;
- `406` Scheduled scenario PLUS;
- `427` Floor call control;
- `430` Staircase light control.
This gives 12 candidate Object roles across the two Modules.

## Configuration modes

| Mode / modality | Evidence |
| --- | --- |
| Physical configuration | product documentation + implementation evidence |
| Virtual Configuration | implementation evidence |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `153` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `153` | `A` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB` | `0` | A; Area (0-9 `GEN`,`GR`,`AMB`) |
| `153` | `PL` | `0..9` | `0` | PL; Light Point |
| `153` | `M` | `0..8`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `14` = `CEN`; `15` = `PUL` | `0` | M; Mode physical configurator (0-8, `O/I`,`OFF`,`ON`,SU_GIU,SU_GIU_M,`CEN`,`PUL`) |
| `153` | `LIV1` | `0..99` | `1` | LIV1; Configurator LIV1 |
| `153` | `LIV2` | `0..9` | `1` | LIV2; Configurator LIV2 |
| `153` | `SPE` | `0..9` | `0` | SPE; Special function command control (0-9) |
| `153` | `I` | `0..9`; `14` = `CEN` | `0` | I; Configurator I (0-9, `CEN`) |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `A` | `0..9`, `GEN`, `GR`, `AMB` | stored values `12..14` for symbolic scopes |
| `PL` | `0..9` | point / function target |
| `M` | `0..8`, `O/I`, `OFF`, `ON`, `UP/DOWN`, `UP/DOWN monostable`, `CEN`, `PUL` | multifunction mode |
| `LIV1` | `0..99` | level/configuration field |
| `LIV2` | `0..9` | level/configuration field |
| `SPE` | `0..9` | special-function selector |
| `I` | `0..9`, `CEN` | interface / destination-related selector |

### Source-model irregularity: `AUX`

Several slot-condition rows explicitly reference an `AUX` variable, but firmware `153` contains no firmware-scoped configuration field named `AUX`.

This must remain an unresolved source-model fact. Do not silently map `AUX` to `I`, an Object `AUX` channel, or another field without independent evidence.

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


### Object `407` - `AUX` control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `9` = `ON`/`OFF` and point to point dimming; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `12` = Bistable control; `13` = Monostable control; `4` = Reset BI; `5` = Reset TRI; `6` = Reset `GEN`; `1` = Disable (lower button); `2` = Enable (lower button); `3` = Disable (upper button) - enable (lower button) | `0` | Modality |
| `OUT_AUX_CH` | `1..15` | `1` | `AUX` channel |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |


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


### Additional Device-specific interpretation

| Role / Object | Principal configuration fields | Device applicability note |
| --- | --- | --- |
| `400` Light control | modes; address scope; `A`/`PL`/`G`; levels; timing; `AUX` | direct candidate |
| `401` Automation control | modes; address scope; levels; referent; `AUX` | direct candidate |
| `402`/`407`/`408` lock/`AUX`/door-entry | role-specific address and `AUX` surfaces | direct candidates; published reachability differs |
| `403`..`406` scenario roles | scenario target, levels, buttons, delays, PLUS scenario fields | direct and Virgin-only candidates |
| `409` Sound diffusion | addressing, source, follow-me, `AUX` | direct candidate on slot 1 |
| `427`/`430` | floor-call / staircase-light fields | Virgin-only candidates requiring reachability proof |

The complete candidate surface is large because the firmware reuses generic command Objects. The Device-specific dossier preserves the reachable Object set while the detailed reusable parameter semantics remain canonical in the Device Model and programming material.

### Lighting and automation

Object `400` exposes 42 stored command modes including toggle, timed `ON`, dimming, blinking, fixed-level and customized command forms; point/area/group/general addressing; installation/destination levels; referent address; timing components; level/ramp parameters; and `AUX` input.

Object `401` exposes bistable, monostable and blades-control modes with point/area/group/general addressing, installation/destination levels, referent address and `AUX` input.

### Lock, `AUX` and door-entry roles

| Topic | Source-derived detail |
| --- | --- |
| Object `402` | disable/enable lock modes, broad address scopes and `AUX` input. |
| Object `407` | `AUX` command mode, output `AUX` channel `1..15`, input `AUX` channel `0..15`. |
| Object `408` | external-unit address `0..95`, segment scope and `AUX` input. |
| Object `427` | point-to-point/general floor call, internal-unit address split across `N1/N2`, segment scope and `AUX` input. |
| Object `430` | staircase-light control with internal-unit address, segment scope and `AUX` input. |

### Scenario roles

Object `403` provides scenario activation / modification, full A/PL scenario-module target encoding, installation/destination levels, two scenario-button selections and independent delay tables.

Object `404` provides A/PL, two button numbers, `AUX` input and start delay.

Virgin-only Object `405` provides two scenario numbers, regulation target and independent button delays. Object `406` provides the split low/high PLUS scenario number and two button fields.

### Sound diffusion

Object `409` provides point/area/general addressing, area and audio point, source selection, follow-me flag and `AUX` input.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `153` | `1` | `400` | `4145` | No textual predicate stored | None |
| `153` | `1` | `401` | `4673` | `M=SU_GIU;SPE=0;AUX=0` | None |
| `153` | `1` | `402` | `4427` | `M<>0;SPE=1;AUX=0` | None |
| `153` | `1` | `403` | `4429` | `M<>0;SPE=4;AUX=0` | None |
| `153` | `1` | `404` | `4431` | `M<>0;SPE=6;AUX=0` | None |
| `153` | `1` | `407` | `4460` | `M=0;SPE=0;AUX<>0` | None |
| `153` | `1` | `408` | `4432` | `M<>0;SPE=8;AUX=0` | None |
| `153` | `1` | `409` | `4433` | `M<>0;SPE=9;AUX=0` | None |
| `153` | `2` | `400` | `4145` | No textual predicate stored | None |
| `153` | `2` | `401` | `4673` | `M=SU_GIU;SPE=0;AUX=0` | None |
| `153` | `2` | `402` | `4427` | `M<>0;SPE=1;AUX=0` | None |
| `153` | `2` | `403` | `4429` | `M<>0;SPE=4;AUX=0` | None |
| `153` | `2` | `404` | `4431` | `M<>0;SPE=6;AUX=0` | None |
| `153` | `2` | `407` | `4460` | `M=0;SPE=0;AUX<>0` | None |
| `153` | `2` | `408` | `4432` | `M<>0;SPE=8;AUX=0` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `153` | `404` | `1703` | `START_DELAY` | `0..255` (entire reusable range retained) | `10` | Start delay |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

### Product interpretation and source differences

| Surface | Condition / issue | Interpretation |
| --- | --- | --- |
| Object selection | `M`/`SPE`/`AUX` predicates in implementation rows | selects role candidates per Module |
| `AUX` condition variable | referenced by slot conditions but absent from firmware-scoped fields | Unresolved - do not map to `I` or an Object `AUX` field without evidence |
| Published reachability | guide excludes video-door-entry and `AUX` from Special-control functions | Virgin-only candidate reachability requires independent proof |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve item model `9`, brand/line and installed configurator count | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 30` | determine active Object for each of the two Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine configured system/address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration and physical-configurability information | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Depending on selected Object, this Device can participate in lighting, automation, scenario, `AUX`, video-door-entry and sound-diffusion functions.

The Device page establishes the available hardware/Object projection. Generic WHO command syntax belongs under [Functional Protocol](../../functional/).

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

A correct programmer must resolve the selected Object per Module before validating Object-scoped parameters. It must also preserve the unresolved `AUX` condition variable rather than inventing a conversion.

See [Object Programming](../../programming/object-programming.md), [Configuration Programming](../../programming/configuration-programming.md), and [Programming Validation](../../programming/validation.md).

## Source reconciliation

The archived MyHOME automation guide materially narrows the Extended control interpretation:

- physical configurator `I` selects the installation level: `1..9` address another logical-expansion bus, `0` selects the local section, and `CEN` selects the main riser in the documented architecture;
- the published architecture uses this mechanism to extend addressable automation/light-control scope across interfaces;
- `LIV1` / `LIV2` participate in the published extended dimmer/control functions and therefore require the selected function context;
- importantly, the product guide describes Extended control as providing the Special-control functions **except** video-door-entry and `AUX` functions.

That last point conflicts with the broader reusable/Virgin-Object candidate surface in the implementation database. The Device page therefore treats `AUX` and video-door-entry-related Virgin-only candidates as implementation evidence requiring independent reachability proof, not as established published product capabilities.

## Evidence limits and open work

- Locate official product sheets for all six Mosaic references.
- Obtain a sanitized H4655 or L4655 hardware fingerprint.
- Determine the runtime/physical meaning of the condition variable `AUX`.
- Establish whether Virgin-only Objects `405`, `406`, `427` and `430` are reachable through current physical or virtual configuration on this firmware.
- Archive additional language/revision variants of the extended-control documentation.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
