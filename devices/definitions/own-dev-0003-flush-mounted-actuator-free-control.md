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

The canonical catalogue maps nine commercial Device records to item `1184`, item model `107`, and firmware `157`. Historical Arnould Espace Evolution documentation independently groups `64391`, `64191`, and `64192` in the same two-relay actuator/control family. The Spanish manufacturer leaf directly covers the three BTicino references. The three remaining Legrand references have established catalogue identities but lack retained exact-product sheets.

| Brand / line | Reference | Relationship to technical definition | Evidence |
| --- | --- | --- | --- |
| Arnould - Espace Evolution | `64391` | Established identity | Catalogue + vendor catalogue |
| Arnould - Espace Evolution | `64191` | Established commercial variant | Catalogue + vendor catalogue |
| Arnould - Espace Evolution | `64192` | Established commercial variant | Catalogue + vendor catalogue |
| BTicino - Axolute | `H4671M2` | Shared technical-item identity | Catalogue + `BT00411-b-ES`, printed pp. 749–753 / PDF pp. 180–184 |
| BTicino - LivingLight | `LN4671M2` | Shared technical-item identity | Catalogue + `BT00411-b-ES`, printed pp. 749–753 / PDF pp. 180–184 |
| BTicino - Matix | `AM5851M2` | Shared technical-item identity | Catalogue + `BT00411-b-ES`, printed pp. 749–753 / PDF pp. 180–184 |
| Legrand - Arteor | `573961` | Shared technical-item identity | Canonical catalogue; retained exact-product sheet absent |
| Legrand - Céliane | `067249` | Shared technical-item identity | Canonical catalogue; retained exact-product sheet absent |
| Legrand - Céliane | `067556` | Shared technical-item identity | Canonical catalogue; retained exact-product sheet absent |

The technical Device ID does not privilege one of these references. Shared-item membership establishes the common catalogue capability core but does not erase possible package, finish, regional, or hardware differences.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| Arnould Espace Evolution catalogue | Historical product catalogue | No dated imprint established in the inspected original | Device/family coverage described by retained source | [Archived original](https://archive.openwebnet-ha.org/sha256/98/e4/98e446ba788aba89c58c0d0f3e13cce2b357f6850c3c3df31de64ff023e7303a.pdf); `64391` / `64191` / `64192` occur on printed pp. 27, 32 / PDF pp. 27, 32 | Arnould Espace Evolution catalogue |
| MyHOME Suite lighting actuator function documentation | Vendor implementation documentation | No dated imprint established in the inspected original | Device/family coverage described by retained source | - | MyHOME Suite lighting actuator function documentation |
| MyHOME Suite automation actuator function documentation | Vendor implementation documentation | No dated imprint established in the inspected original | Device/family coverage described by retained source | - | MyHOME Suite automation actuator function documentation |
| `BTicino-MyHOME-Spanish-technical-sheets.pdf` | Multi-product technical-sheet compendium (Spanish) | Exact leaf `BT00411-b-ES`; no date established | `H4671M2`, `LN4671M2`, `AM5851M2`: printed pp. 749–753 / PDF pp. 180–184, read in full. Other products outside scope. | [Archived original](https://archive.openwebnet-ha.org/sha256/89/4f/894f468c301ea2b7aaec22635d91961e1eedc00136a21e21b774e975c378b4eb.pdf) | [Publisher source](https://www.bticino.es/pdf/FICHA_TECNICA_DOMOTICA_MYHOME_BTICINO.pdf) |

Additional installation sheets and catalogue revisions should be collected rather than treating this list as exhaustive.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting / outputs | 2 flush-mounted modules; 2 independent relays | Arnould catalogue printed/PDF p. 32; `BT00411-b-ES`, printed pp. 749–750 / PDF pp. 180–181 |
| BTicino front controls | 4 pushbuttons, 4 two-colour LEDs; local LED adjustment/exclusion button | `BT00411-b-ES`, printed p. 749 / PDF p. 180 |
| BTicino SCS supply | Nominal `27 Vdc`; operating `18..27 Vdc` | `BT00411-b-ES`, printed p. 750 / PDF p. 181 |
| BTicino standby current | Maximum `14 mA` | Same exact BTicino leaf |
| BTicino temperature rows | `0..40 °C` and `-5..45 °C`, both labelled operating temperature | Same leaf; second label is a source ambiguity, not silently relabelled storage |
| BTicino incandescent/halogen and shutter motor at `230 Vac` | `460 W / 2 A` for each documented load class | Same leaf; not automatically transferable to Arnould packages |
| BTicino LED/CFL | `70 W`, maximum 2 lamps | Same leaf |
| BTicino fluorescent/electronic transformer | `70 W / 0.3 A` | Same leaf |
| BTicino ferromagnetic transformer | `460 VA / 2 A`, `cosφ=0.5` | Same leaf |
| Arnould base `64391` load classes | Incandescent/halogen `2 A`; ferromagnetic `2 A cosφ=0.5`; fluorescent/electronic `70 W`; maximum 2 CFL/LED lamps | Arnould catalogue printed/PDF p. 32 |
| Arnould base motor figure | Printed `460 pour moteurs`, without a clear unit in the inspected page image | Same catalogue; not normalized to watts |
| `64391` package | No rocker supplied; accepts one 2-module or two 1-module rockers | Same catalogue |
| `64191` lighting package | Two blank 1-module rockers; blue `0/1` and `CEN` configurators supplied | Same catalogue |
| `64192` motor package | One 2-module Up/Down rocker and matching configurator; motor maximum `500 W` | Same catalogue; unresolved difference from BTicino `460 W` leaf |
| Physical sockets | `A1`, `PL1`, `M1`, `A2`, `PL2`, `M2` | BTicino leaf printed pp. 751–753 / PDF pp. 182–184 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1184` | Canonical catalogue |
| Item model / `modobj` | `107` | Canonical catalogue / retained definition |
| Main system | Lighting / Automation (`id_system = 1`) | Canonical catalogue / retained definition |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `107` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These are software applicability associations, not an inventory of physical ports or proof of every functional service.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `157` | `-1` | `-1` | `-1` | `4` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

### Parameter and package associations

No firmware parameter-file associations are stored for this item in the canonical snapshot.

No `AS_FW_PACKAGE` association is stored for these firmware definitions. This is a catalogue coverage statement, not a claim that manufacturer firmware downloads never existed.

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

The four Modules must not be confused with the eleven slot/Object association rows in the database.

Object `1` and Object `407` are permitted through the Virgin Object definitions even though they do not appear as direct firmware/Object rows in the extracted `AS_OBJECT_FIRMWARE` set. Preserve that distinction.

Installed Module state is read through [`DIMENSION 30`](../../diagnostics/dim30-modules.md).

## Configuration modes

| Firmware | Mode | Catalogue mode | Applicability |
| --- | --- | --- | --- |
| `157` | Physical configuration | `0` | Canonical catalogue association; not proof of installed state |
| `157` | Virtual Configuration | `1` | Canonical catalogue association; not proof of installed state |
| `157` | Advanced Configuration | `2` | Canonical catalogue association; not proof of installed state |

Product physical and software setup are distinct from the catalogue mode labels. A declared mode does not prove every reusable Object or programming operation is available.

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

### Virgin-only candidate Objects

The following reusable surfaces occur only through permitted Virgin Object membership; no direct association proves that they become active on this Device.

### Object `1` - Blind actuator (Virgin-only candidate)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master PUL; `16` = Slave and PUL | `0` | Modality |
| `LOCAL_BUTTON` | `12` = Bistable control; `13` = Monostable control | `12` | Local button modality |
| `STOP_TIME` | `0` = Infinite; `1` = 1 s; `2` = 2 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `21` = 21 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min | `60` | Stop time; Only for Master modes |
| `DELAY_DOORS` | `0..60` | `3` | Delay between doors |
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

### Object `407` - AUX control (Virgin-only candidate)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `9` = ON/OFF and point to point dimming; `10` = OFF; `11` = ON; `15` = PUL; `12` = Bistable control; `13` = Monostable control; `4` = Reset BI; `5` = Reset TRI; `6` = Reset GEN; `1` = Disable (lower button); `2` = Enable (lower button); `3` = Disable (upper button) - enable (lower button) | `0` | Modality |
| `OUT_AUX_CH` | `1..15` | `1` | AUX channel |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input AUX channel |

### Applicability interpretation

Object `7`'s reusable `STOP_TIME` enum lacks an `18 s` entry; the Virgin-only Blind Object `1` has a different domain. Objects `1` and `407` above are admitted by Virgin Objects only: no direct firmware/Object association or Device-specific filter establishes their reachability. Their fields are retained as candidate catalogue data, not asserted physical functions.

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

### Source irregularities affecting selection

| Source entry / scope | Issue | Interpretation limit |
| --- | --- | --- |
| Conditions `4908`, `4909`, `4910` | Stored endings `A2<>GE`, standalone `A2`, and `A2<>` are incomplete/unresolved | Do not repair missing tokens or infer condition precedence |
| Remote addressing condition branches | `A2=AMB/GR/GEN` is stored although firmware `A2` has only `0..9` | A stored conversion branch is not proof of a legal physical selector |
| PLUS selector branch | `M2=FAKE` occurs as a predicate; `FAKE` is absent from the declared firmware enum | Published software PLUS capability is distinct from this unresolved stored selector |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve item model `107`, brand `6`, line `8`, and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | installed firmware observation, despite wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` / `6` / `13` | hardware, microcontroller, and Device ID when supported | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | determine active Object at each of four Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine per-Module configured system/address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values and physical-configurability flags | [Configuration](../../diagnostics/dim35-configuration.md) |

No generic diagnostic frame is duplicated here.
## Functional applicability

| Function / configuration | Documented use | Evidence |
| --- | --- | --- |
| Lighting actuator | One local load plus remote control, or two separately addressed lighting loads (`M1=CEN` in the published physical two-load setup) | `BT00411-b-ES`, printed pp. 749, 751–753 |
| Automation actuator | One motor using the two relays and the corresponding shutter rocker; relay interlocking is configuration-dependent | Arnould catalogue p. 32; BTicino leaf pp. 749–751 |
| Remote command / scenario | Right-hand control can target a remote light, automation actuator or MH200N scenarios; physical `M2=CEN` has source-specific address/cover constraints | BTicino leaf p. 752 |

Resolved light and automation Objects relate to [Lighting](../../functional/who-1-lighting/) and [Automation](../../functional/who-2-automation/). Four catalogue Modules represent a configurable projection, not four physical relays.

## Observed behavior and corroboration

No additional publishable runtime observation is asserted beyond observations explicitly retained elsewhere on this page.

## Programming

Use `A1/PL1/M1` for the local actuator and `A2/PL2/M2` for the remote command, or the published two-light arrangement. The BTicino leaf gives motor stop times `M1=5 → 1 min`, `6 → 2 min`, `7 → 5 min`, `8 → until a subsequent command`; `OFF` is a two-minute PUL form, and Up/Down covers select bistable or monostable operation. Do not apply a lighting selector to a motor solely because its numeric value exists in a reusable Object.

For lighting `M1=1..4`, OFF switches the Master off immediately and delays the corresponding Slave by 1–4 minutes; the published note limits this to point-to-point commands. `M1=CEN` in the two-load actuator table is not the same role as `M2=CEN` in the remote scenario-control table. Resolve the firmware slot conditions before applying conversions or writing Object configuration. Generic sequencing remains in [Programming Validation](../../programming/validation.md).

## Source reconciliation

The Arnould catalogue establishes base versus package relationships for `64391/64191/64192`. Its product page is printed/PDF p. 32, not printed p. 31. The page image confirms a unitless motor figure `460`; the explicitly printed `64192` package rating is `500 W`.

The retained Spanish `BT00411-b-ES` leaf covers `H4671M2/LN4671M2/AM5851M2`, supplies their electrical/configuration data, and gives `460 W` for a shutter motor. Catalogue membership establishes a shared technical core but does not resolve the `460` versus `500 W` commercial/revision difference. Its two temperature rows have the same operating-temperature label, so the second is not reclassified by inference.

MyHOME Suite lighting/automation help entries previously listed without retained originals are discovery leads only. The lighting page was reachable during this review, but its original could not be registered through the available task-scoped HTML archival helper; its content is not used as retained claim evidence. Guessed automation-help and English-sheet endpoints were unavailable and do not establish that such revisions do not exist. The retained BTicino leaf now supports the product modes independently.

Firmware `157`'s stored conditions, filters and conversions remain implementation evidence. Out-of-domain selector branches and Virgin-only Objects are retained without inventing precedence or declaring their physical reachability.

## Evidence limits and open work

- Retained exact-product sheets are still absent for Legrand `573961`, `067249`, `067556`; these are documentation gaps, not unresolved catalogue identities.
- Resolve the `64192` `500 W` package rating against the base unitless `460` and the BTicino `460 W` motor rating before transferring ratings between variants.
- Resolve the duplicate temperature label in `BT00411-b-ES`; no publication date is established for that leaf.
- Unretained Suite help and inaccessible guessed endpoints remain discovery leads, not incorporated evidence.
- Known-hardware identity, firmware, four-Module projection and the physical reachability of Virgin-only Objects/out-of-domain branches remain unobserved.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Physical Devices](../../device-model/physical-devices.md#64391-64191-and-64192)
- [Firmware](../../device-model/firmware.md#firmware-example)
- [Modules](../../device-model/modules.md#combined-device-example)
- [Objects](../../device-model/objects.md#device-and-object-descriptions)
- [Virgin Objects](../../device-model/virgin-objects.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md#worked-example-firmware-157)

- [Semantic review record, 5 October 2026](../../project/review/device-reviews-0001-0010-2026-10-05.md#own-dev-0003)
