# Flush-mounted two-relay actuator and free control

## Summary

This flush-mounted device combines two relay outputs with local controls and commands for other SCS actuators. Configuration lets it operate two lighting circuits or an interlocked motor load, while the available rocker packages adapt the front controls to the intended use.


| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0003` | Project identity |
| Technical description | Flush-mounted two-relay actuator with integrated/free command functions | Catalogue + vendor catalogue |
| Commercial identities | 9 catalogue records across Arnould, BTicino, and Legrand ranges | Implementation evidence; Arnould subset also vendor-catalogue documented |
| Catalogue item | `1184` - “Flush mounted actuator and free control” | Implementation evidence |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `107` | Implementation evidence |
| Catalogue brand / line | Arnould `BRAND = 6`; Espace Evolution `LINE = 8` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified (`EN_FIRMWARE 157`) | Implementation evidence |
| Declared Modules | `4` | Implementation evidence |
| Categories | Actuator, Command, Multifunction, Lighting, Automation, Scenario | Capability model |

This Device is deliberately modelled as a multifunction Physical Device rather than as one actuator address. Its firmware can expose actuator functions on slots `1..2` and command/scenario functions on slots `3..4`, with the active Object set selected by configuration.

## Commercial identities


The canonical catalogue maps nine commercial Device records to item `1184`, item model `107`, and firmware `157`. Historical Arnould Espace Evolution documentation independently groups `64391`, `64191`, and `64192` in the same two-relay actuator/control family. The remaining six records share the technical capability item in MyHOME Suite but still need individual product-document review.

| Brand / line | Reference | Relationship to technical definition | Evidence |
| --- | --- | --- | --- |
| Arnould - Espace Evolution | `64391` | documented commercial reference | Catalogue + vendor catalogue |
| Arnould - Espace Evolution | `64191` | documented commercial/package variant | Catalogue + vendor catalogue |
| Arnould - Espace Evolution | `64192` | documented commercial/package variant | Catalogue + vendor catalogue |
| BTicino - Axolute | `H4671M2` | shared technical item | Implementation evidence; product-document review pending |
| BTicino - LivingLight | `LN4671M2` | shared technical item | Implementation evidence; product-document review pending |
| BTicino - Matix | `AM5851M2` | shared technical item | Implementation evidence; product-document review pending |
| Legrand - Arteor | `573961` | shared technical item | Implementation evidence; product-document review pending |
| Legrand - Céliane | `067249` | shared technical item | Implementation evidence; product-document review pending |
| Legrand - Céliane | `067556` | shared technical item | Implementation evidence; product-document review pending |

The technical Device ID does not privilege one of these references. Shared-item membership establishes the common catalogue capability core but does not erase possible package, finish, regional, or hardware differences.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| Arnould Espace Evolution catalogue | Historical product catalogue | not stated in retained row | Device/family coverage described by retained source | [Archived original](https://archive.openwebnet-ha.org/sha256/98/e4/98e446ba788aba89c58c0d0f3e13cce2b357f6850c3c3df31de64ff023e7303a.pdf); `64391` / `64191` / `64192` occur on printed pp. 27, 31 / PDF pp. 27, 32 | Arnould Espace Evolution catalogue |
| MyHOME Suite lighting actuator function documentation | Vendor implementation documentation | not stated in retained row | Device/family coverage described by retained source | - | MyHOME Suite lighting actuator function documentation |
| MyHOME Suite automation actuator function documentation | Vendor implementation documentation | not stated in retained row | Device/family coverage described by retained source | - | MyHOME Suite automation actuator function documentation |

Additional installation sheets and catalogue revisions should be collected rather than treating this list as exhaustive.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Product-specific characteristics | See retained source-derived notes below | Retained publisher evidence |
| Hardware corroboration | Pending unless explicitly observed | Observation status |
| Commercial/package variation | Preserved where documented | Source reconciliation |

The archived historical Arnould catalogue describes `64391` as a two-independent-relay actuator with integrated control, physically or virtually configurable, occupying two modules. It documents simple or double loads, two lighting circuits or a motor, logical relay interlocking by configuration, and control of a remote BUS actuator.

The same source makes the package distinctions explicit: `64391` is supplied without a rocker and accepts either one two-module rocker or two one-module rockers; `64191` is the lighting package, preassembled with two unmarked one-module rocker controls and supplied with blue `0/1` and `CEN` configurators; `64192` is the motor package, preassembled with one two-module Up/Down rocker, supplied with the matching Up/Down configurator, and documented for a motor up to `500 W`.

For the base actuator the catalogue clearly prints `2 A` incandescent/halogen capability, `2 A cosφ 0.5` for ferromagnetic transformers, `70 W` for fluorescent/electronic-transformer loads, and a maximum of two compact-fluorescent/LED lamps. A neighbouring motor figure is typographically ambiguous in extracted text, so this dossier does not normalize that value beyond the unambiguous `64192` `500 W` package statement without page-image verification.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1184` | Canonical catalogue |
| Item model / `modobj` | `107` | Canonical catalogue / retained definition |
| Main system | Lighting / Automation (`id_system = 1`) | Canonical catalogue / retained definition |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `157` | `-1` | `-1` | `-1` | `4` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `157` | `1` | `6` Light actuator | Fixed/designated metadata | `1155` | `6` | `619` |
| `157` | `1` | `7` Automation actuator | Candidate alternative | `1159` | `7` | `621` |
| `157` | `2` | `6` Light actuator | Fixed/designated metadata | `1156` | `6` | `619` |
| `157` | `3` | `400` Light control | Fixed/designated metadata | `1157` | `400` | `620` |
| `157` | `3` | `401` Automation control | Candidate alternative | `1160` | `401` | `622` |
| `157` | `3` | `404` Scheduled scenario | Candidate alternative | `2402` | `404` | `623` |
| `157` | `3` | `406` Scheduled scenario PLUS | Candidate alternative | `2403` | `406` | `624` |
| `157` | `4` | `400` Light control | Fixed/designated metadata | `1158` | `400` | `620` |
| `157` | `4` | `401` Automation control | Candidate alternative | `1161` | `401` | `622` |
| `157` | `4` | `404` Scheduled scenario | Candidate alternative | `1162` | `404` | `623` |
| `157` | `4` | `406` Scheduled scenario PLUS | Candidate alternative | `1163` | `406` | `624` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `157` | `500` Automation double command virgin | `3`, `4` | `400`, `401`, `404`, `406`, `407` | `500` | `31` |
| `157` | `510` Automation relay virgin | `1`, `2` | `1`, `6`, `7` | `510` | `32` |

### Reconciled topology notes


### Catalogue Object alternatives

| Object | Description | Available slot(s) | Designation |
| ---: | --- | --- | --- |
| `6` | Light actuator | `1`, `2` | fixed/designated Light actuator |
| `7` | Automation actuator | `1` | alternative |
| `400` | Light control | `3`, `4` | fixed/designated Light control |
| `401` | Automation control | `3`, `4` | alternative |
| `404` | Scheduled scenario | `3`, `4` | alternative |
| `406` | Scheduled scenario PLUS | `3`, `4` | alternative |

The four Modules must not be confused with the eleven slot/Object association rows in the database.

### Virgin Objects

| Virgin Object | Description | Slots | Permitted Objects |
| ---: | --- | --- | --- |
| `500` | Automation double command virgin | `3`, `4` | `400` Light control; `401` Automation control; `404` Scheduled scenario; `406` Scheduled scenario PLUS; `407` `AUX` control |
| `510` | Automation relay virgin | `1`, `2` | `1` Blind actuator; `6` Light actuator; `7` Automation actuator |

Object `1` and Object `407` are permitted through the Virgin Object definitions even though they do not appear as direct firmware/Object rows in the extracted `AS_OBJECT_FIRMWARE` set. Preserve that distinction.

Installed Module state is read through [`DIMENSION 30`](../../diagnostics/dim30-modules.md).

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `157` | Physical configuration | retained Device-specific configuration modality |
| `157` | Virtual Configuration | retained Device-specific configuration modality |
| `157` | Advanced Configuration | retained Device-specific configuration modality |


Firmware `157` supports all three catalogue modes:

- Physical configuration
- Virtual Configuration
- Advanced Configuration

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `157` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `157` | `A1` | `0..9` | `0` | A1; Configurator A1 (0-9) |
| `157` | `PL1` | `0..9` | `0` | PL1; PL1 - (0-9) |
| `157` | `M1` | `0..8`; `9` = `O/I`; `14` = `CEN`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `10` = `OFF`; `15` = `PUL` | `0` | M1; Mode physical configurator (0-8, `O/I`,SU_GIU,SU_GIU_M,`CEN`,`OFF`,`PUL`) |
| `157` | `A2` | `0..9` | `0` | A2; Configurator A2 (0-9) |
| `157` | `PL2` | `0..9` | `0` | PL2; PL2 - (0-9) |
| `157` | `M2` | `0..8`; `9` = `O/I`; `14` = `CEN`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `10` = `OFF`; `15` = `PUL` | `0` | M2; Mode physical configurator (0-8, `O/I`,SU_GIU,SU_GIU_M,`CEN`,`OFF`,`PUL`) |




### Published and reconciled details



The six fields `A1/PL1/M1/A2/PL2/M2` are the Device's physical configurator surface in the canonical catalogue. `AID` is an identity field and is not counted as a physical configurator position.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `6` - Light actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality |
| `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open | `0` | Relay state on device reset |
| `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing | `0` | Load control mode |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `SUBTYPE` | `11` = Actuator; `1` = Lamp; `10` = Valve; `15` = Differential restart; `6` = Fan; `7` = Watering; `8` = Controlled socket; `9` = Lock | `11` | Type of load |
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


### Object `7` - Automation actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality |
| `LOCAL_BUTTON` | `12` = Bistable control; `13` = Monostable control; `14` = Bistable and blades control | `12` | Local button modality |
| `STOP_TIME` | `0` = Infinite; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min | `60` | Stop time |
| `SUBTYPE` | `11` = Actuator; `2` = Shutter; `3` = Curtain; `4` = Gate; `5` = Garage door; `15` = Differential restart | `11` | Type of load |
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


The tables below preserve the complete reusable Object parameter surfaces referenced by firmware `157`. They are candidate configuration capabilities; firmware conditions, filters, and conversion rules determine the reachable subset for a concrete 64391 configuration.

### Object `6` - Light actuator

| Parameter | Domain |
| --- | --- |
| `A` | `0..10` |
| `PL` | `0..15` |
| `M` | `0=Master`, `11=Slave`, `15=Master PUL`, `16=Slave and PUL` |
| `LOCAL_BUTTON` | `0=Toggle`, `1=ON/OFF`, `9=ON-OFF`, `15=Pushbutton`, `18=Timed ON` |
| `DELAYED_OFF` | `0..255 s` |
| `STATE_RESET` | `0=Restore last value`, `1=Closed`, `2=Open` |
| `LOAD_CONTROL_MODE` | `0=With zero crossing`, `1=Without zero crossing` |
| `HOURS` / `MINUTES` / `SECONDS` | `0..255` / `0..59` / `0..59` |
| `SUBTYPE` | Actuator, Lamp, Valve, Differential restart, Fan, Watering, Controlled socket, Lock |
| `G1..G10` | each `0..255`, where `0` means no group |

### Object `7` - Automation actuator

| Parameter | Domain |
| --- | --- |
| `A` | `0..10` |
| `PL` | `0..15` |
| `M` | `0=Master`, `11=Slave`, `15=Master PUL`, `16=Slave and PUL` |
| `LOCAL_BUTTON` | `12=Bistable`, `13=Monostable`, `14=Bistable and blades` |
| `STOP_TIME` | Infinite; `1..17 s`; `19..60 s`; `2..10 min` through stored values `62..70` |
| `SUBTYPE` | Actuator, Shutter, Curtain, Gate, Garage door, Differential restart |
| `G1..G10` | each `0..255`, where `0` means no group |

The stored `STOP_TIME` enum notably has no `18 s` entry. Preserve the database domain exactly.

### Object `400` - Light control

| Parameter | Domain |
| --- | --- |
| `M` | Toggle, timed `ON`, dimmer variants, `ON`/`OFF` variants, `OFF`, `ON`, `PUL`, blinking `0.5..8 s`, fixed dimmer levels `10..90%`, and customized modes `128..134` |
| `ADDR_TYPE` | `0=Point to point`, `1=Area`, `2=Group`, `3=General` |
| `A` | `0..10` |
| `PL` | `0..15` |
| `G` | `1..255` |
| `INST_LEV` | Private riser, Local bus `1..15`, Standard |
| `DEST_LEV` | Private riser, Local bus `1..15`, All systems |
| `A_R` | `0..10`; `0` means no reference |
| `PL_R` | `0..15`; `0` means no reference |
| `HOURS` / `MINUTES` / `SECONDS` | custom timed-`ON` components |
| `LEVEL` | `0..100` for customized modes |
| `START_S` / `STOP_S` / `DIMMING_S` | `0..255` for customized modes |
| `T_TIME` | stored timed presets: 1,2,3,4,5,6,15 minutes; 30 seconds; 0.5 seconds; 2 seconds; 10 minutes |
| `IN_AUX_CHANNEL` | `0..15` |

### Object `401` - Automation control

| Parameter | Domain |
| --- | --- |
| `M` | `12=Bistable`, `13=Monostable`, `14=Blades control and bistable` |
| `ADDR_TYPE` | Point to point, Area, Group, General |
| `A` | `0..10` |
| `PL` | `0..15` |
| `G` | `1..255` |
| `INST_LEV` | Private riser, Local bus `1..15`, Standard |
| `DEST_LEV` | Private riser, Local bus `1..15`, All systems |
| `A_R` | `0..10` |
| `PL_R` | `0..15` |
| `IN_AUX_CHANNEL` | `0..15` |

### Object `404` - Scheduled scenario

| Parameter | Domain |
| --- | --- |
| `A` | `0..10` |
| `PL` | `0..15` |
| `BUTTON_1` | `0..31`, default `1` |
| `BUTTON_2` | `0..31`, default `2` |
| `IN_AUX_CHANNEL` | `0..15` |
| `START_DELAY` | `0..255 s`, default `10` |

### Object `406` - Scheduled scenario PLUS

| Parameter | Domain |
| --- | --- |
| `PPT_CEN_LOW` | `0..255`, default `1` |
| `PPT_CEN_HIG` | `0..7`, default `0` |
| `BUTTON_1` | `0..31`, default `1` |
| `BUTTON_2` | `0..31`, default `2` |

Virgin Object `500` additionally permits `AUX` control Object `407`; its reusable Object parameters should be incorporated when a reachable 64391 configuration or authoritative product source establishes that capability for this Device.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `157` | `1` | `6` | `4145` | No textual predicate stored | None |
| `157` | `1` | `6` | `4232` | `M1=0` | `20` |
| `157` | `1` | `6` | `4239` | `M1=1` | `20` |
| `157` | `1` | `6` | `4241` | `M1=2` | `20` |
| `157` | `1` | `6` | `4243` | `M1=3` | `20` |
| `157` | `1` | `6` | `4245` | `M1=4` | `20` |
| `157` | `1` | `6` | `4256` | `M1=CEN;M2=0` | `25` |
| `157` | `1` | `6` | `4258` | `M1=CEN;M2=1` | `25` |
| `157` | `1` | `6` | `4260` | `M1=CEN;M2=2` | `25` |
| `157` | `1` | `6` | `4262` | `M1=CEN;M2=3` | `25` |
| `157` | `1` | `6` | `4264` | `M1=CEN;M2=4` | `25` |
| `157` | `1` | `6` | `4266` | `M1=CEN;M2=O/I` | `25` |
| `157` | `1` | `6` | `4268` | `M1=CEN;M2=PUL` | `25` |
| `157` | `1` | `6` | `4273` | `M1=O/I` | `20` |
| `157` | `1` | `6` | `4292` | `M1=PUL` | `20` |
| `157` | `1` | `7` | `4247` | `M1=5` | `26` |
| `157` | `1` | `7` | `4249` | `M1=6` | `26` |
| `157` | `1` | `7` | `4251` | `M1=7` | `26` |
| `157` | `1` | `7` | `4253` | `M1=8` | `26` |
| `157` | `1` | `7` | `4280` | `M1=OFF` | `26` |
| `157` | `1` | `7` | `4298` | `M1=SU_GIU` | `26` |
| `157` | `1` | `7` | `4306` | `M1=SU_GIU_M` | `26` |
| `157` | `2` | `6` | `4145` | No textual predicate stored | None |
| `157` | `2` | `6` | `4256` | `M1=CEN;M2=0` | `25` |
| `157` | `2` | `6` | `4258` | `M1=CEN;M2=1` | `25` |
| `157` | `2` | `6` | `4260` | `M1=CEN;M2=2` | `25` |
| `157` | `2` | `6` | `4262` | `M1=CEN;M2=3` | `25` |
| `157` | `2` | `6` | `4264` | `M1=CEN;M2=4` | `25` |
| `157` | `2` | `6` | `4266` | `M1=CEN;M2=O/I` | `25` |
| `157` | `2` | `6` | `4268` | `M1=CEN;M2=PUL` | `25` |
| `157` | `3` | `400` | `4145` | No textual predicate stored | None |
| `157` | `3` | `400` | `4231` | `M1=0` | `4` |
| `157` | `3` | `400` | `4238` | `M1=1` | `4` |
| `157` | `3` | `400` | `4240` | `M1=2` | `4` |
| `157` | `3` | `400` | `4242` | `M1=3` | `4` |
| `157` | `3` | `400` | `4244` | `M1=4` | `4` |
| `157` | `3` | `400` | `4255` | `M1=CEN;M2=0` | `4` |
| `157` | `3` | `400` | `4257` | `M1=CEN;M2=1` | `4` |
| `157` | `3` | `400` | `4259` | `M1=CEN;M2=2` | `4` |
| `157` | `3` | `400` | `4261` | `M1=CEN;M2=3` | `4` |
| `157` | `3` | `400` | `4263` | `M1=CEN;M2=4` | `4` |
| `157` | `3` | `400` | `4265` | `M1=CEN;M2=O/I` | `4` |
| `157` | `3` | `400` | `4267` | `M1=CEN;M2=PUL` | `4` |
| `157` | `3` | `400` | `4272` | `M1=O/I` | `4` |
| `157` | `3` | `400` | `4291` | `M1=PUL` | `4` |
| `157` | `3` | `401` | `4246` | `M1=5` | `4` |
| `157` | `3` | `401` | `4248` | `M1=6` | `4` |
| `157` | `3` | `401` | `4250` | `M1=7` | `4` |
| `157` | `3` | `401` | `4252` | `M1=8` | `4` |
| `157` | `3` | `401` | `4279` | `M1=OFF` | `4` |
| `157` | `3` | `401` | `4299` | `M1=SU_GIU` | `550` |
| `157` | `3` | `401` | `4307` | `M1=SU_GIU_M` | `550` |
| `157` | `4` | `400` | `4145` | No textual predicate stored | None |
| `157` | `4` | `400` | `4194` | `M1<>CEN;M2=0;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `157` | `4` | `400` | `4195` | `M1<>CEN;M2=0;A2=AMB` | `97` |
| `157` | `4` | `400` | `4197` | `M1<>CEN;M2=0;A2=GEN` | `95` |
| `157` | `4` | `400` | `4198` | `M1<>CEN;M2=0;A2=GR` | `96` |
| `157` | `4` | `400` | `4201` | `M1<>CEN;M2=O/I;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `157` | `4` | `400` | `4202` | `M1<>CEN;M2=O/I;A2=AMB` | `97` |
| `157` | `4` | `400` | `4204` | `M1<>CEN;M2=O/I;A2=GEN` | `95` |
| `157` | `4` | `400` | `4205` | `M1<>CEN;M2=O/I;A2=GR` | `96` |
| `157` | `4` | `400` | `4206` | `M1<>CEN;M2=OFF;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `157` | `4` | `400` | `4207` | `M1<>CEN;M2=OFF;A2=AMB` | `97` |
| `157` | `4` | `400` | `4209` | `M1<>CEN;M2=OFF;A2=GEN` | `95` |
| `157` | `4` | `400` | `4210` | `M1<>CEN;M2=OFF;A2=GR` | `96` |
| `157` | `4` | `400` | `4211` | `M1<>CEN;M2=ON;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `157` | `4` | `400` | `4212` | `M1<>CEN;M2=ON;A2=AMB` | `97` |
| `157` | `4` | `400` | `4214` | `M1<>CEN;M2=ON;A2=GEN` | `95` |
| `157` | `4` | `400` | `4215` | `M1<>CEN;M2=ON;A2=GR` | `96` |
| `157` | `4` | `400` | `4216` | `M1<>CEN;M2=PUL;A2<>AUX;A2<>GR;A2<>AMB;A2<>GEN` | `4` |
| `157` | `4` | `400` | `4217` | `M1<>CEN;M2=PUL;A2=AMB` | `97` |
| `157` | `4` | `400` | `4219` | `M1<>CEN;M2=PUL;A2=GEN` | `95` |
| `157` | `4` | `400` | `4220` | `M1<>CEN;M2=PUL;A2=GR` | `96` |
| `157` | `4` | `400` | `4255` | `M1=CEN;M2=0` | `4` |
| `157` | `4` | `400` | `4257` | `M1=CEN;M2=1` | `4` |
| `157` | `4` | `400` | `4259` | `M1=CEN;M2=2` | `4` |
| `157` | `4` | `400` | `4261` | `M1=CEN;M2=3` | `4` |
| `157` | `4` | `400` | `4263` | `M1=CEN;M2=4` | `4` |
| `157` | `4` | `400` | `4265` | `M1=CEN;M2=O/I` | `4` |
| `157` | `4` | `400` | `4267` | `M1=CEN;M2=PUL` | `4` |
| `157` | `4` | `400` | `4908` | `M1<>CEN;M2<>CEN;A2<>AUX;A2<>GR;A2<>AMB;A2<>GE` | `4` |
| `157` | `4` | `401` | `4222` | `M1<>CEN;M2=SU_GIU;A2=AMB` | `97` |
| `157` | `4` | `401` | `4224` | `M1<>CEN;M2=SU_GIU;A2=GEN` | `95` |
| `157` | `4` | `401` | `4225` | `M1<>CEN;M2=SU_GIU;A2=GR` | `96` |
| `157` | `4` | `401` | `4227` | `M1<>CEN;M2=SU_GIU_M;A2=AMB` | `97` |
| `157` | `4` | `401` | `4229` | `M1<>CEN;M2=SU_GIU_M;A2=GEN` | `95` |
| `157` | `4` | `401` | `4230` | `M1<>CEN;M2=SU_GIU_M;A2=GR` | `96` |
| `157` | `4` | `401` | `4909` | `M1<>CEN;M2=SU_GIU_M;A2<>AUX;A2<>GR;A2<>AMB;A2` | `4` |
| `157` | `4` | `401` | `4910` | `M1<>CEN;M2=SU_GIU;A2<>AUX;A2<>GR;A2<>AMB;A2<>` | `4` |
| `157` | `4` | `404` | `4199` | `M1<>CEN;M2=CEN` | `4` |
| `157` | `4` | `406` | `4200` | `M1<>CEN;M2=FAKE` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `157` | `6` | `1167` | `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `157` | `6` | `1168` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `157` | `6` | `1169` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `157` | `6` | `1170` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `157` | `6` | `1172` | `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open (entire reusable range retained) | `0` | Relay state on device reset |
| `157` | `6` | `1873` | `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing (entire reusable range retained) | `0` | Load_control_mode |
| `157` | `7` | `1195` | `LOCAL_BUTTON` | `12` = Bistable control; `13` = Monostable control; `14` = Bistable and blades control (entire reusable range retained) | `12` | Funzionalità di pulsante locale ridotta (Local button mode) |
| `157` | `7` | `1196` | `SUBTYPE` | `15` = Differential restart | `11` | subtype(ASTCBR); reusable default `11` is outside this subset; filter supplies no replacement default |
| `157` | `400` | `1184` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `157` | `400` | `1185` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `157` | `400` | `1186` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `157` | `400` | `1187` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `157` | `400` | `1188` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `157` | `400` | `1189` | `LEVEL` | `0..100` (entire reusable range retained) | `100` | Level |
| `157` | `400` | `1190` | `START_S` | `0..255` (entire reusable range retained) | `255` | Soft start speed |
| `157` | `400` | `1191` | `STOP_S` | `0..255` (entire reusable range retained) | `255` | Soft stop speed |
| `157` | `400` | `1192` | `DIMMING_S` | `0..255` (entire reusable range retained) | `255` | Dimming speed |
| `157` | `400` | `1193` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `157` | `400` | `1194` | `M` | `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `4` = Toggle `ON`/`OFF`; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `5` = `ON`/`OFF`; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `130` = Customized `ON`/`OFF` and point to point dimmer; `131` = Customized toggle dimmer; `132` = Customized `ON`/`OFF` and dimmer; `133` = Customized toggle dimmer without regulation; `134` = Customized `ON`/`OFF` and dimmer without regulation; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90% | `0` | Mode; reusable default `0` is outside this subset; filter supplies no replacement default |
| `157` | `401` | `1200` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `157` | `401` | `1201` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `157` | `401` | `1202` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `157` | `404` | `1203` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `157` | `404` | `1204` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `157` | `404` | `1205` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `157` | `404` | `1704` | `START_DELAY` | `0..255` (entire reusable range retained) | `10` | Start delay |

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
| `20` | `M1=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `20` |
| `20` | `M1=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `20` |
| `20` | `M1=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `20` |
| `20` | `M1=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `20` |
| `20` | `M1=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `20` |
| `20` | `M1=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `20` |
| `20` | `M1=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `20` |
| `20` | `M1=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `20` |
| `25` | `M2=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `25` |
| `25` | `M2=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `25` |
| `25` | `M2=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `25` |
| `25` | `M2=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `25` |
| `25` | `M2=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `25` |
| `25` | `M2=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `25` |
| `25` | `M2=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `25` |
| `25` | `M2=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `25` |
| `26` | `M2=0` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `60` | `26` |
| `26` | `M2=1` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `62` | `26` |
| `26` | `M2=2` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `65` | `26` |
| `26` | `M2=3` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `70` | `26` |
| `26` | `M2=4` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `0` | `26` |
| `26` | `M2=5` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `20` | `26` |
| `26` | `M2=6` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `10` | `26` |
| `26` | `M2=7` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `5` | `26` |
| `26` | `M2=8` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `15` | `26` |
| `26` | `M2=9` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `30` | `26` |
| `26` | `M2=I/O` | `LOCAL_BUTTON` = `13`; `M` = `0`; `STOP_TIME` = `60` | `26` |
| `26` | `M2=PUL` | `LOCAL_BUTTON` = `12`; `M` = `15`; `STOP_TIME` = `60` | `26` |
| `26` | `M2=SLA` | `LOCAL_BUTTON` = `12`; `M` = `11` | `26` |
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
| `550` | `M1=0` | `M` = `0` | `550` |
| `550` | `M1=1` | `M` = `1`; `T_TIME ` = `1` | `550` |
| `550` | `M1=2` | `M` = `1`; `T_TIME ` = `2` | `550` |
| `550` | `M1=3` | `M` = `1`; `T_TIME ` = `3` | `550` |
| `550` | `M1=4` | `M` = `1`; `T_TIME ` = `4` | `550` |
| `550` | `M1=5` | `M` = `1`; `T_TIME ` = `5` | `550` |
| `550` | `M1=6` | `M` = `1`; `T_TIME ` = `6` | `550` |
| `550` | `M1=7` | `M` = `1`; `T_TIME ` = `7` | `550` |
| `550` | `M1=8` | `M` = `1`; `T_TIME ` = `8` | `550` |
| `550` | `M1=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `2` | `550` |
| `550` | `M1=O/I` | `M` = `9` | `550` |
| `550` | `M1=OFF` | `M` = `10` | `550` |
| `550` | `M1=ON` | `M` = `11` | `550` |
| `550` | `M1=PUL` | `M` = `15` | `550` |
| `550` | `M1=SU_GIU` | `M` = `12` | `550` |
| `550` | `M1=SU_GIU_M` | `M` = `13` | `550` |
| `550` | `A1=1` | `A` = `1` | `550` |
| `550` | `A1=2` | `A` = `2` | `550` |
| `550` | `A1=3` | `A` = `3` | `550` |
| `550` | `A1=4` | `A` = `4` | `550` |
| `550` | `A1=5` | `A` = `5` | `550` |
| `550` | `A1=6` | `A` = `6` | `550` |
| `550` | `A1=7` | `A` = `7` | `550` |
| `550` | `A1=8` | `A` = `8` | `550` |
| `550` | `A1=9` | `A` = `9` | `550` |
| `550` | `PL1=1` | `PL` = `1` | `550` |
| `550` | `PL1=1; M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `550` → `1` |
| `550` | `PL1=1; M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `550` → `1` |
| `550` | `PL1=1; M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `550` → `1` |
| `550` | `PL1=2` | `PL` = `2` | `550` |
| `550` | `PL1=2; M=0` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `60` | `550` → `2` |
| `550` | `PL1=2; M=1` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `62` | `550` → `2` |
| `550` | `PL1=2; M=2` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `65` | `550` → `2` |
| `550` | `PL1=2; M=3` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `70` | `550` → `2` |
| `550` | `PL1=2; M=4` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `0` | `550` → `2` |
| `550` | `PL1=2; M=5` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `20` | `550` → `2` |
| `550` | `PL1=2; M=6` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `10` | `550` → `2` |
| `550` | `PL1=2; M=7` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `5` | `550` → `2` |
| `550` | `PL1=2; M=8` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `15` | `550` → `2` |
| `550` | `PL1=2; M=9` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `30` | `550` → `2` |
| `550` | `PL1=2; M=I/O` | `LOCAL_BUTTON` = `13`; `M` = `0`; `STOP_TIME` = `60` | `550` → `2` |
| `550` | `PL1=2; M=PUL` | `LOCAL_BUTTON` = `12`; `M` = `15`; `STOP_TIME` = `60` | `550` → `2` |
| `550` | `PL1=2; M=SLA` | `LOCAL_BUTTON` = `12`; `M` = `11` | `550` → `2` |
| `550` | `PL1=3` | `PL` = `3` | `550` |
| `550` | `PL1=3; M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `550` → `3` |
| `550` | `PL1=3; M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `550` → `3` |
| `550` | `PL1=3; M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `550` → `3` |
| `550` | `PL1=4` | `PL` = `4` | `550` |
| `550` | `PL1=4; M1=0` | `M` = `0` | `550` → `4` |
| `550` | `PL1=4; M1=1` | `M` = `1`; `T_TIME ` = `1` | `550` → `4` |
| `550` | `PL1=4; M1=2` | `M` = `1`; `T_TIME ` = `2` | `550` → `4` |
| `550` | `PL1=4; M1=3` | `M` = `1`; `T_TIME ` = `3` | `550` → `4` |
| `550` | `PL1=4; M1=4` | `M` = `1`; `T_TIME ` = `4` | `550` → `4` |
| `550` | `PL1=4; M1=5` | `M` = `1`; `T_TIME ` = `5` | `550` → `4` |
| `550` | `PL1=4; M1=6` | `M` = `1`; `T_TIME ` = `6` | `550` → `4` |
| `550` | `PL1=4; M1=7` | `M` = `1`; `T_TIME ` = `7` | `550` → `4` |
| `550` | `PL1=4; M1=8` | `M` = `1`; `T_TIME ` = `8` | `550` → `4` |
| `550` | `PL1=4; M1=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `2` | `550` → `4` |
| `550` | `PL1=4; M1=O/I` | `M` = `9` | `550` → `4` |
| `550` | `PL1=4; M1=OFF` | `M` = `10` | `550` → `4` |
| `550` | `PL1=4; M1=ON` | `M` = `11` | `550` → `4` |
| `550` | `PL1=4; M1=PUL` | `M` = `15` | `550` → `4` |
| `550` | `PL1=4; M1=SU_GIU` | `M` = `12` | `550` → `4` |
| `550` | `PL1=4; M1=SU_GIU_M` | `M` = `13` | `550` → `4` |
| `550` | `PL1=4; M2=0` | `M` = `0` | `550` → `4` |
| `550` | `PL1=4; M2=1` | `M` = `1`; `T_TIME ` = `1` | `550` → `4` |
| `550` | `PL1=4; M2=2` | `M` = `1`; `T_TIME ` = `2` | `550` → `4` |
| `550` | `PL1=4; M2=3` | `M` = `1`; `T_TIME ` = `3` | `550` → `4` |
| `550` | `PL1=4; M2=4` | `M` = `1`; `T_TIME ` = `4` | `550` → `4` |
| `550` | `PL1=4; M2=5` | `M` = `1`; `T_TIME ` = `5` | `550` → `4` |
| `550` | `PL1=4; M2=6` | `M` = `1`; `T_TIME ` = `6` | `550` → `4` |
| `550` | `PL1=4; M2=7` | `M` = `1`; `T_TIME ` = `7` | `550` → `4` |
| `550` | `PL1=4; M2=8` | `M` = `1`; `T_TIME ` = `8` | `550` → `4` |
| `550` | `PL1=4; M2=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `2` | `550` → `4` |
| `550` | `PL1=4; M2=O/I` | `M` = `9` | `550` → `4` |
| `550` | `PL1=4; M2=OFF` | `M` = `10` | `550` → `4` |
| `550` | `PL1=4; M2=ON` | `M` = `11` | `550` → `4` |
| `550` | `PL1=4; M2=PUL` | `M` = `15` | `550` → `4` |
| `550` | `PL1=4; M2=SU_GIU` | `M` = `12` | `550` → `4` |
| `550` | `PL1=4; M2=SU_GIU_M` | `M` = `13` | `550` → `4` |
| `550` | `PL1=5` | `PL` = `5` | `550` |
| `550` | `PL1=5; M1=0` | `M` = `0` | `550` → `5` |
| `550` | `PL1=5; M1=O/I` | `M` = `9` | `550` → `5` |
| `550` | `PL1=5; M1=OFF` | `M` = `10` | `550` → `5` |
| `550` | `PL1=5; M1=ON` | `M` = `11` | `550` → `5` |
| `550` | `PL1=5; M1=PUL` | `M` = `15` | `550` → `5` |
| `550` | `PL1=5; M1=SU_GIU` | `M` = `12` | `550` → `5` |
| `550` | `PL1=5; M1=SU_GIU_M` | `M` = `13` | `550` → `5` |
| `550` | `PL1=5; M2=0` | `M` = `0` | `550` → `5` |
| `550` | `PL1=5; M2=O/I` | `M` = `9` | `550` → `5` |
| `550` | `PL1=5; M2=OFF` | `M` = `10` | `550` → `5` |
| `550` | `PL1=5; M2=ON` | `M` = `11` | `550` → `5` |
| `550` | `PL1=5; M2=PUL` | `M` = `15` | `550` → `5` |
| `550` | `PL1=5; M2=SU_GIU` | `M` = `12` | `550` → `5` |
| `550` | `PL1=5; M2=SU_GIU_M` | `M` = `13` | `550` → `5` |
| `550` | `PL1=5; PL1=0` | `OUT_AUX_CHANNEL` = `0` | `550` → `5` |
| `550` | `PL1=5; PL1=1` | `OUT_AUX_CHANNEL` = `1` | `550` → `5` |
| `550` | `PL1=5; PL1=2` | `OUT_AUX_CHANNEL` = `2` | `550` → `5` |
| `550` | `PL1=5; PL1=3` | `OUT_AUX_CHANNEL` = `3` | `550` → `5` |
| `550` | `PL1=5; PL1=4` | `OUT_AUX_CHANNEL` = `4` | `550` → `5` |
| `550` | `PL1=5; PL1=5` | `OUT_AUX_CHANNEL` = `5` | `550` → `5` |
| `550` | `PL1=5; PL1=6` | `OUT_AUX_CHANNEL` = `6` | `550` → `5` |
| `550` | `PL1=5; PL1=7` | `OUT_AUX_CHANNEL` = `7` | `550` → `5` |
| `550` | `PL1=5; PL1=8` | `OUT_AUX_CHANNEL` = `8` | `550` → `5` |
| `550` | `PL1=5; PL1=9` | `OUT_AUX_CHANNEL` = `9` | `550` → `5` |
| `550` | `PL1=5; PL2=0` | `OUT_AUX_CHANNEL` = `0` | `550` → `5` |
| `550` | `PL1=5; PL2=1` | `OUT_AUX_CHANNEL` = `1` | `550` → `5` |
| `550` | `PL1=5; PL2=2` | `OUT_AUX_CHANNEL` = `2` | `550` → `5` |
| `550` | `PL1=5; PL2=3` | `OUT_AUX_CHANNEL` = `3` | `550` → `5` |
| `550` | `PL1=5; PL2=4` | `OUT_AUX_CHANNEL` = `4` | `550` → `5` |
| `550` | `PL1=5; PL2=5` | `OUT_AUX_CHANNEL` = `5` | `550` → `5` |
| `550` | `PL1=5; PL2=6` | `OUT_AUX_CHANNEL` = `6` | `550` → `5` |
| `550` | `PL1=5; PL2=7` | `OUT_AUX_CHANNEL` = `7` | `550` → `5` |
| `550` | `PL1=5; PL2=8` | `OUT_AUX_CHANNEL` = `8` | `550` → `5` |
| `550` | `PL1=5; PL2=9` | `OUT_AUX_CHANNEL` = `9` | `550` → `5` |
| `550` | `PL1=6` | `PL` = `6` | `550` |
| `550` | `PL1=6; M=3` | `ADDR_TYPE` = `0`; `MAIN_GROUP` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1`; `REG` = `1` | `550` → `6` |
| `550` | `PL1=6; M=4` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `1` | `550` → `6` |
| `550` | `PL1=6; M=5` | `ADDR_TYPE` = `0`; `MAIN_GROUP` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `0` | `550` → `6` |
| `550` | `PL1=6; M=6` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `1` | `550` → `6` |
| `550` | `PL1=6; M=7` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `3`; `REG` = `0` | `550` → `6` |
| `550` | `PL1=6; M=8` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1`; `REG` = `1` | `550` → `6` |
| `550` | `PL1=6; S=0` | `PIR` = `0` | `550` → `6` |
| `550` | `PL1=6; S=1` | `PIR` = `1` | `550` → `6` |
| `550` | `PL1=6; S=2` | `PIR` = `2` | `550` → `6` |
| `550` | `PL1=6; S=3` | `PIR` = `3` | `550` → `6` |
| `550` | `PL1=6; T=0` | `HOURS` = `0`; `MINUTES` = `0`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=1` | `HOURS` = `0`; `MINUTES` = `0`; `SECONDS` = `30` | `550` → `6` |
| `550` | `PL1=6; T=2` | `HOURS` = `0`; `MINUTES` = `1`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=3` | `HOURS` = `0`; `MINUTES` = `2`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=4` | `HOURS` = `0`; `MINUTES` = `5`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=5` | `HOURS` = `0`; `MINUTES` = `10`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=6` | `HOURS` = `0`; `MINUTES` = `15`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=7` | `HOURS` = `0`; `MINUTES` = `20`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=8` | `HOURS` = `0`; `MINUTES` = `30`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; T=9` | `HOURS` = `0`; `MINUTES` = `40`; `SECONDS` = `0` | `550` → `6` |
| `550` | `PL1=6; M=0` | `ADDR_TYPE` = `0`; `MAIN_GROUP` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1` | `550` → `6` |
| `550` | `PL1=6; M=1` | `ADDR_TYPE` = `0`; `LOAD_CONTROL` = `1`; `FUNCTIONAL_MODE` = `1`; `REG` = `0` | `550` → `6` |
| `550` | `PL1=7` | `PL` = `7` | `550` |
| `550` | `PL1=7` | Referenced conversion rule absent from source | `550` → `7` |
| `550` | `PL1=8` | `PL` = `8` | `550` |
| `550` | `PL1=8` | Referenced conversion rule absent from source | `550` → `8` |
| `550` | `PL1=9` | `PL` = `9` | `550` |
| `550` | `PL1=9; M=0` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `20` | `550` → `9` |
| `550` | `PL1=9; M=1` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `15` | `550` → `9` |
| `550` | `PL1=9; M=2` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `25` | `550` → `9` |
| `550` | `PL1=9; M=3` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `60` | `550` → `9` |
| `550` | `PL1=9; M=PUL` | `DELAY_DOORS` = `3`; `LOCAL_BUTTON` = `12`; `M` = `15`; `STOP_TIME` = `20` | `550` → `9` |
| `550` | `PL1=9; M=SLA` | `LOCAL_BUTTON` = `12`; `M` = `11` | `550` → `9` |
| `550` | `M2=0` | `M` = `0` | `550` |
| `550` | `M2=1` | `M` = `1`; `T_TIME ` = `1` | `550` |
| `550` | `M2=2` | `M` = `1`; `T_TIME ` = `2` | `550` |
| `550` | `M2=3` | `M` = `1`; `T_TIME ` = `3` | `550` |
| `550` | `M2=4` | `M` = `1`; `T_TIME ` = `4` | `550` |
| `550` | `M2=5` | `M` = `1`; `T_TIME ` = `5` | `550` |
| `550` | `M2=6` | `M` = `1`; `T_TIME ` = `6` | `550` |
| `550` | `M2=7` | `M` = `1`; `T_TIME ` = `7` | `550` |
| `550` | `M2=8` | `M` = `1`; `T_TIME ` = `8` | `550` |
| `550` | `M2=CEN` | `CEN_BUTT_1 ` = `1`; `CEN_BUTT_2 ` = `2` | `550` |
| `550` | `M2=O/I` | `M` = `9` | `550` |
| `550` | `M2=OFF` | `M` = `10` | `550` |
| `550` | `M2=ON` | `M` = `11` | `550` |
| `550` | `M2=PUL` | `M` = `15` | `550` |
| `550` | `M2=SU_GIU` | `M` = `12` | `550` |
| `550` | `M2=SU_GIU_M` | `M` = `13` | `550` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1184` and the installed model | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware without treating wildcard sentinels as literal installed values | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`6`, `7`, `400`, `401`, `404`, `406`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions, and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

### Existing Device-specific diagnostic notes


| Diagnostic surface | 64391-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve item model `107`, brand `6`, line `8`, and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | installed firmware observation, despite wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` / `6` / `13` | hardware, microcontroller, and Device ID when supported | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | determine active Object at each of four Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine per-Module configured system/address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values and physical-configurability flags | [Configuration](../../diagnostics/dim35-configuration.md) |

No generic diagnostic frame is duplicated here.

## Functional applicability


Depending on selected Objects, the Device can participate in:

- [`WHO 1` - Lighting](../../functional/who-1-lighting/) through Light actuator / Light control Objects;
- [`WHO 2` - Automation](../../functional/who-2-automation/) through Automation actuator / Automation control Objects;
- scenario/`CEN` behavior through Scheduled scenario and Scheduled scenario PLUS Objects.

The Device page establishes **which functions can exist on this hardware**. The linked functional sections remain authoritative for command syntax and general runtime semantics.

## Observed behavior and corroboration

No additional publishable runtime observation is asserted beyond observations explicitly retained elsewhere on this page.

## Programming


This Device is a strong validation case because physical fields can change the active Object topology.

A correct programmer must:

1. resolve the legal firmware-scoped physical domain;
2. evaluate reachable slot conditions;
3. select the resulting Object per Module;
4. apply the relevant conversion-rule graph;
5. validate Object-scoped configuration values;
6. write/verify through the canonical programming workflow.

See [Configuration Programming](../../programming/configuration-programming.md), [Object Programming](../../programming/object-programming.md), and [Programming Validation](../../programming/validation.md).

## Source reconciliation


The historical Arnould material and MyHOME Suite implementation help establish more product detail than the shared technical-item mapping alone:

- `64391` is the two-relay actuator/control base product; `64191` and `64192` are package/use variants in the same documented family rather than independent OpenWebNet capability definitions;
- the marketed product supports simple or double loads, two lighting circuits or one motor, with relay interlocking selected by configuration;
- the integrated controls can operate the local relays or be assigned to remote bus functions, so the four-Module model is intentional rather than an artefact of the catalogue;
- the lighting and automation implementation help supplies the product-specific Master/Slave/`PUL` and actuator-mode interpretation used by the condition/conversion model.

The historical Arnould catalogue is now archived byte-for-byte and its Device/package facts are reconciled above. Its electrical ratings remain revision-scoped rather than timeless specifications. The MyHOME Suite lighting and automation help remain official external implementation sources and are already represented in the configuration/Object interpretation. Source reconciliation is complete for the currently identified `64391`/`64191`/`64192` source set; direct documentation for the six other commercial records remains a commercial-identity discovery gap.

## Evidence limits and open work


The current dossier is substantially complete for the canonical MyHOME Suite 3.5.38 database representation, but physical-hardware corroboration is still missing.

Priority evidence:

- a sanitized fingerprint from a known physical 64391/64191/64192;
- observed `DIMENSION 1` identity tuple and firmware/hardware versions;
- observed `DIMENSION 30` topology under several physical configurations;
- `DIMENSION 32` and `35` snapshots tied to those configurations;
- authoritative installation sheets documenting the physical configurator layout and package variants;
- confirmation of whether `AUX` control Object `407` is reachable on this firmware despite appearing only through Virgin Object `500`;
- controlled validation of the catalogue branches whose stored conditions use values outside the declared physical domains.

When these observations arrive, they should be added as corroborating evidence to the existing database-derived facts rather than replacing them.

## Sources


- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Physical Devices](../../device-model/physical-devices.md#64391-64191-and-64192)
- [Firmware](../../device-model/firmware.md#firmware-example)
- [Modules](../../device-model/modules.md#combined-device-example)
- [Objects](../../device-model/objects.md#device-and-object-descriptions)
- [Virgin Objects](../../device-model/virgin-objects.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md#worked-example-firmware-157)
