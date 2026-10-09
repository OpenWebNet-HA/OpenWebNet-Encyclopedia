# MYHOME lighting command and actuator

## Summary

This MYHOME device combines lighting-actuator functions with configurable commands for lighting, automation and scenarios. The catalogue establishes both switching and command roles; the actual relay arrangement, load limits and front-control layout remain undocumented in the retained exact-product sources.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0112` | Project identity |
| Technical description | MYHOME lighting command and actuator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `H4672M2L`, `LN4672M2L`, `067586` | All three SKU-to-item mappings explicitly established by the manufacturer catalogue |
| Catalogue item | `2247` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `111` | Main association; independent of project ID |
| Firmware definition | `774` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `5` | Firmware metadata |
| Categories | Actuators, Commands, User interfaces, Multifunction devices | Source-derived roles |

The catalogue defines two Light actuator Modules, two command Modules and a separate User interface Module. Five logical Modules do not establish five physical outputs. The manufacturer catalogue explicitly establishes all three SKU-to-item mappings. Exact-product PDFs have not been found; physical specifications remain a documentation gap.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4672M2L` | Established catalogue identity | `EN_DEVICE` record `2599` explicitly links this SKU to item `2247` |
| BTicino | `LN4672M2L` | Established catalogue identity | `EN_DEVICE` record `2600` explicitly links this SKU to item `2247` |
| Legrand - Céliane | `067586` | Established catalogue identity | `EN_DEVICE` record `2601` explicitly links this SKU to item `2247` |

The manufacturer catalogue explicitly links all three SKUs to this technical item through `EN_DEVICE.id_item` relationships. It labels the H reference Axolute, the LN reference Living (internal `L/N/NT`), and the Legrand reference Céliane. Those catalogue identities are established independently of PDF availability. Online searches did not locate exact-product sheets; unavailable product endpoints do not invalidate the catalogue records. The retained similar-reference source describes `67586` as an Epure satin-steel thermostat probe. It is excluded as product evidence: reference resemblance does not establish equivalence or contradict these SKU-to-item mappings.

### Complete catalogue commercial metadata

| Record | Reference | Catalogue name | Brand key | Line key | Visible | Visibility type | Dependent | Gateway | Catalogue description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `2599` | `H4672M2L` | `Comando-Attuatore MYHOME Luci ` | `1` | `2` | `1` |  | `0` | `0` | `Comando-Attuatore MYHOME Luci Axolute` |
| `2600` | `LN4672M2L` | `Comando-Attuatore MYHOME Luci ` | `1` | `4` | `1` |  | `0` | `0` | `Comando-Attuatore MYHOME Luci Living` |
| `2601` | `067586` | `Comando-Attuatore MYHOME Luci ` | `2` | `13` | `1` |  | `0` | `0` | `Comando-Attuatore MYHOME Luci Celiane` |

Empty catalogue values are retained as empty metadata; none is an installed-state or market-availability observation.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `Arnould-historical-selection-guide.pdf` | French commercial guide; excluded similar-reference evidence | `No publication date established in retained original` | Printed/PDF p. 18 identifies 67586 as Epure satin-steel thermostat probe, not the catalogue lighting command/actuator. Exact reference and description on this leaf checked; no specifications transferred. | [Archived original](https://archive.openwebnet-ha.org/sha256/50/44/50445914174b741659c19b5610642a52db530765041d1700c399f55c0f414bdb.pdf) | [Publisher original](https://assets.legrand.com/general/ouidoo/pdf/legrand-art-arnould-guide-de-choix.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2247`: all firmware/commercial/system/Object/Module/Virgin/field/filter/mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

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
| `EN_ITEM.id_item` | `2247` | Canonical catalogue |
| Technical item description | Comando-Attuatore MYHOME Luci | Canonical catalogue |
| Item family | 0; key `2` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `111` | `AS_ITEM_SYSTEM` |
| Commercial record count | `3` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `111` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `774` | `1` | `0` | No build row | `5` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `774` | `1` | `6` Light actuator | Fixed/designated metadata | `3048` | `6` | `1455` |
| `774` | `2` | `6` Light actuator | Fixed/designated metadata | `3049` | `6` | `1455` |
| `774` | `3` | `400` Light control | Fixed/designated metadata | `3050` | `400` | `1456` |
| `774` | `3` | `401` Automation control | Candidate alternative | `2986` | `401` | `1418` |
| `774` | `3` | `402` Lock/unlock actuator control | Candidate alternative | `2988` | `402` | `1419` |
| `774` | `3` | `406` Scheduled scenario PLUS | Candidate alternative | `2990` | `406` | `1420` |
| `774` | `3` | `408` Open lock control | Candidate alternative | `2994` | `408` | `1422` |
| `774` | `3` | `427` Floor call control | Candidate alternative | `2992` | `427` | `1421` |
| `774` | `3` | `430` Staircase light control | Candidate alternative | `2996` | `430` | `1423` |
| `774` | `3` | `463` Load control actuator visualization | Candidate alternative | `3000` | `492` | `1425` |
| `774` | `3` | `145` Shutter control (2 slots) | Candidate alternative | `3124` | `650` | `1503` |
| `774` | `4` | `400` Light control | Fixed/designated metadata | `3051` | `400` | `1456` |
| `774` | `4` | `401` Automation control | Candidate alternative | `2987` | `401` | `1418` |
| `774` | `4` | `402` Lock/unlock actuator control | Candidate alternative | `2989` | `402` | `1419` |
| `774` | `4` | `406` Scheduled scenario PLUS | Candidate alternative | `2991` | `406` | `1420` |
| `774` | `4` | `408` Open lock control | Candidate alternative | `2995` | `408` | `1422` |
| `774` | `4` | `427` Floor call control | Candidate alternative | `2993` | `427` | `1421` |
| `774` | `4` | `430` Staircase light control | Candidate alternative | `2997` | `430` | `1423` |
| `774` | `4` | `463` Load control actuator visualization | Candidate alternative | `3001` | `492` | `1425` |
| `774` | `5` | `143` User interface settings for command | Fixed/designated metadata | `3052` | `644` | `1457` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `774` | `501` Special double command virgin | `3`, `4` | `400`, `401`, `402`, `403`, `404`, `405`, `406`, `407`, `408`, `409`, `427`, `430` | `501` | `92` |

Slots `1/2` designate Light actuator Object `6`. Command slots `3/4` each have eight common alternatives: `400`, `401`, `402`, `406`, `408`, `427`, `430`, `463`. Two-slot Object `145` has one stored starting placement at slot `3`; UI Object `143` is in slot `5`. Virgin Object `501` covers command slots `3/4` only; it does not cover the actuator or UI slots. Virgin `501` permits `400..409`, `427` and `430`, while direct firmware membership excludes `403/404/405/407/409` and adds `145/463`; these relations must remain separate. No selection predicate or conversion rule reconciles them automatically.

## Configuration modes

### Complete catalogue mode and connection associations

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `774` | Physical configuration | `0` | Canonical firmware/mode association |
| `774` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `774` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `774` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `774` | `A1` | `0..9` | `0` | Configurator A1 (0-9) |
| `774` | `PL1` | `0..9` | `0` | PL1 - (0-9) |
| `774` | `M1` | `0..8`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `14` = `CEN`; `15` = `PUL` | `0` | Modality; Mode physical configurator (0-8, `O/I`,`OFF`,`ON`,SU_GIU,SU_GIU_M,`CEN`,`PUL`) |
| `774` | `A2` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB` | `0` | Automation A addressing space (for configurator A2) |
| `774` | `PL2` | `0..9` | `0` | PL2 - (0-9) |
| `774` | `M2` | `0..8`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `15` = `PUL` | `0` | Modality; Mode physical configurator (0-8, `O/I`,`OFF`,`ON`,SU_GIU,SU_GIU_M,`CEN`,`PUL`) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `6` - Light actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality |
| `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON/OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
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

### Object `400` - Light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `1` = Timed `ON`; `2` = Toggle dimmer; `3` = `ON/OFF` and dimming; `4` = Toggle `ON/OFF`; `5` = `ON/OFF`; `9` = `ON/OFF` and point to point dimming; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90%; `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `130` = Customized `ON/OFF` and point to point dimmer; `131` = Customized toggle dimmer; `132` = Customized `ON/OFF` and dimmer; `133` = Customized toggle dimmer without regulation; `134` = Customized `ON/OFF` and dimmer without regulation | `0` | Modality; Standard mode means: with regulation for Point-to-point addressing, without regulation for Area, Group and General addressing |
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

### Object `403` - Scenario module control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Scenario activation and modification; `1` = Scenario activation | `0` | Modality |
| `APL` | `0` = `A=0` `PL=0`; `1` = `A=0` `PL=1`; `2` = `A=0` `PL=2`; `3` = `A=0` `PL=3`; `4` = `A=0` `PL=4`; `5` = `A=0` `PL=5`; `6` = `A=0` `PL=6`; `7` = `A=0` `PL=7`; `8` = `A=0` `PL=8`; `9` = `A=0` `PL=9`; `10` = `A=0` `PL=10`; `11` = `A=0` `PL=11`; `12` = `A=0` `PL=12`; `13` = `A=0` `PL=13`; `14` = `A=0` `PL=14`; `15` = `A=0` `PL=15`; `16` = `A=1` `PL=0`; `17` = `A=1` `PL=1`; `18` = `A=1` `PL=2`; `19` = `A=1` `PL=3`; `20` = `A=1` `PL=4`; `21` = `A=1` `PL=5`; `22` = `A=1` `PL=6`; `23` = `A=1` `PL=7`; `24` = `A=1` `PL=8`; `25` = `A=1` `PL=9`; `26` = `A=1` `PL=10`; `27` = `A=1` `PL=11`; `28` = `A=1` `PL=12`; `29` = `A=1` `PL=13`; `30` = `A=1` `PL=14`; `31` = `A=1` `PL=15`; `32` = `A=2` `PL=0`; `33` = `A=2` `PL=1`; `34` = `A=2` `PL=2`; `35` = `A=2` `PL=3`; `36` = `A=2` `PL=4`; `37` = `A=2` `PL=5`; `38` = `A=2` `PL=6`; `39` = `A=2` `PL=7`; `40` = `A=2` `PL=8`; `41` = `A=2` `PL=9`; `42` = `A=2` `PL=10`; `43` = `A=2` `PL=11`; `44` = `A=2` `PL=12`; `45` = `A=2` `PL=13`; `46` = `A=2` `PL=14`; `47` = `A=2` `PL=15`; `48` = `A=3` `PL=0`; `49` = `A=3` `PL=1`; `50` = `A=3` `PL=2`; `51` = `A=3` `PL=3`; `52` = `A=3` `PL=4`; `53` = `A=3` `PL=5`; `54` = `A=3` `PL=6`; `55` = `A=3` `PL=7`; `56` = `A=3` `PL=8`; `57` = `A=3` `PL=9`; `58` = `A=3` `PL=10`; `59` = `A=3` `PL=11`; `60` = `A=3` `PL=12`; `61` = `A=3` `PL=13`; `62` = `A=3` `PL=14`; `63` = `A=3` `PL=15`; `64` = `A=4` `PL=0`; `65` = `A=4` `PL=1`; `66` = `A=4` `PL=2`; `67` = `A=4` `PL=3`; `68` = `A=4` `PL=4`; `69` = `A=4` `PL=5`; `70` = `A=4` `PL=6`; `71` = `A=4` `PL=7`; `72` = `A=4` `PL=8`; `73` = `A=4` `PL=9`; `74` = `A=4` `PL=10`; `75` = `A=4` `PL=11`; `76` = `A=4` `PL=12`; `77` = `A=4` `PL=13`; `78` = `A=4` `PL=14`; `79` = `A=4` `PL=15`; `80` = `A=5` `PL=0`; `81` = `A=5` `PL=1`; `82` = `A=5` `PL=2`; `83` = `A=5` `PL=3`; `84` = `A=5` `PL=4`; `85` = `A=5` `PL=5`; `86` = `A=5` `PL=6`; `87` = `A=5` `PL=7`; `88` = `A=5` `PL=8`; `89` = `A=5` `PL=9`; `90` = `A=5` `PL=10`; `91` = `A=5` `PL=11`; `92` = `A=5` `PL=12`; `93` = `A=5` `PL=13`; `94` = `A=5` `PL=14`; `95` = `A=5` `PL=15`; `96` = `A=6` `PL=0`; `97` = `A=6` `PL=1`; `98` = `A=6` `PL=2`; `99` = `A=6` `PL=3`; `100` = `A=6` `PL=4`; `101` = `A=6` `PL=5`; `102` = `A=6` `PL=6`; `103` = `A=6` `PL=7`; `104` = `A=6` `PL=8`; `105` = `A=6` `PL=9`; `106` = `A=6` `PL=10`; `107` = `A=6` `PL=11`; `108` = `A=6` `PL=12`; `109` = `A=6` `PL=13`; `110` = `A=6` `PL=14`; `111` = `A=6` `PL=15`; `112` = `A=7` `PL=0`; `113` = `A=7` `PL=1`; `114` = `A=7` `PL=2`; `115` = `A=7` `PL=3`; `116` = `A=7` `PL=4`; `117` = `A=7` `PL=5`; `118` = `A=7` `PL=6`; `119` = `A=7` `PL=7`; `120` = `A=7` `PL=8`; `121` = `A=7` `PL=9`; `122` = `A=7` `PL=10`; `123` = `A=7` `PL=11`; `124` = `A=7` `PL=12`; `125` = `A=7` `PL=13`; `126` = `A=7` `PL=14`; `127` = `A=7` `PL=15`; `128` = `A=8` `PL=0`; `129` = `A=8` `PL=1`; `130` = `A=8` `PL=2`; `131` = `A=8` `PL=3`; `132` = `A=8` `PL=4`; `133` = `A=8` `PL=5`; `134` = `A=8` `PL=6`; `135` = `A=8` `PL=7`; `136` = `A=8` `PL=8`; `137` = `A=8` `PL=9`; `138` = `A=8` `PL=10`; `139` = `A=8` `PL=11`; `140` = `A=8` `PL=12`; `141` = `A=8` `PL=13`; `142` = `A=8` `PL=14`; `143` = `A=8` `PL=15`; `144` = `A=9` `PL=0`; `145` = `A=9` `PL=1`; `146` = `A=9` `PL=2`; `147` = `A=9` `PL=3`; `148` = `A=9` `PL=4`; `149` = `A=9` `PL=5`; `150` = `A=9` `PL=6`; `151` = `A=9` `PL=7`; `152` = `A=9` `PL=8`; `153` = `A=9` `PL=9`; `154` = `A=9` `PL=10`; `155` = `A=9` `PL=11`; `156` = `A=9` `PL=12`; `157` = `A=9` `PL=13`; `158` = `A=9` `PL=14`; `159` = `A=9` `PL=15`; `160` = `A=10` `PL=0`; `161` = `A=10` `PL=1`; `162` = `A=10` `PL=2`; `163` = `A=10` `PL=3`; `164` = `A=10` `PL=4`; `165` = `A=10` `PL=5`; `166` = `A=10` `PL=6`; `167` = `A=10` `PL=7`; `168` = `A=10` `PL=8`; `169` = `A=10` `PL=9`; `170` = `A=10` `PL=10`; `171` = `A=10` `PL=11`; `172` = `A=10` `PL=12`; `173` = `A=10` `PL=13`; `174` = `A=10` `PL=14`; `175` = `A=10` `PL=15` | `0` | Scenario module address |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15 | `0` | Destination level |
| `SCE_BUTT_1` | `1..16` | `1` | Upper button scenario |
| `SCE_BUTT_2` | `1..16` | `2` | Lower button scenario |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `43` = 43 s; `44` = 44 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for upper button |
| `DEL_BUTTON_2` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `36` = 36 s; `37` = 37 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `69` = 9 min; `70` = 10 min | `0` | Activation delay for lower button |

### Object `404` - Scheduled scenario (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `BUTTON_1` | `0..31` | `1` | Upper button |
| `BUTTON_2` | `0..31` | `2` | Lower button |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input AUX channel |
| `START_DELAY` | `0..255` | `10` | Time of restart device (s) |

### Object `405` - Scenario PLUS Lighting Management (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_SCE_1` | `1..255` | `1` | Upper button scenario; Delay (20) |
| `PPT_SCE_2` | `1..255` | `2` | Lower button scenario; Delay (21) |
| `TYPE_OF_REGULATION` | `0` = Regulate all; `1` = Lights only; `2` = Shutters only; `3` = Stereo amplifiers only | `0` | Regulation type; Only if Scenario1=Scenario2 |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for upper button; Only if Scenario1<>Scenario2 |
| `DEL_BUTTON_2` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for lower button; Only if Scenario1<>Scenario2 |

### Object `407` - AUX control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `9` = `ON/OFF` and point to point dimming; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `12` = Bistable control; `13` = Monostable control; `4` = Reset `BI`; `5` = Reset `TRI`; `6` = Reset `GEN`; `1` = Disable (lower button); `2` = Enable (lower button); `3` = Disable (upper button) - enable (lower button) | `0` | Modality |
| `OUT_AUX_CH` | `1..15` | `1` | AUX channel |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input AUX channel |

### Object `409` - Sound diffusion control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `3` = General | `0` | Addressing type |
| `A` | `0..9` | `0` | Area |
| `PF` | `0..9` | `0` | Audio point |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input AUX channel |
| `IS_FOLLOW_ME` | `0` = No; `1` = Yes | `1` | Follow me |
| `SOURCE` | `1..9` | `1` | Source |

### Semantic review findings

The five declared Modules comprise two Object `6` actuator placements, two command placements and UI Object `143`. Object `6` LOCAL_BUTTON filter `3655` excludes default `0`; ten groups, reset state, zero crossing and timer fields remain reusable capability, without physical ratings. The five Virgin-only candidate Objects add 28 reusable fields; direct/allowed membership and two-slot Object `145` occupancy remain distinct.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `774` | `6` | `3655` | `LOCAL_BUTTON` | `1` = `ON/OFF`; `15` = Pushbutton; `18` = Timed `ON`; `9` = `ON` - `OFF` | `0` | Local button modality; reusable default `0` is outside this subset; filter supplies no replacement default |
| `774` | `6` | `3656` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `774` | `6` | `3657` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `774` | `6` | `3658` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `774` | `400` | `3519` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `774` | `400` | `3520` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `774` | `400` | `3521` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `774` | `401` | `3382` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `774` | `401` | `3383` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `774` | `401` | `3384` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `774` | `402` | `3385` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `774` | `402` | `3386` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `774` | `402` | `3387` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `774` | `408` | `3389` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `774` | `427` | `3388` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `774` | `430` | `3390` | `IN_AUX_CHANNEL` | `0..15` (entire reusable range retained) | `0` | Input `AUX` channel |
| `774` | `430` | `4126` | `N2` | `0..15` (entire reusable range retained) | `0` | Associated Internal Unit address - hundreds |
| `774` | `430` | `4139` | `N1` | `100..255` | `0` | Internal unit address; reusable default `0` is outside this subset; filter supplies no replacement default |
| `774` | `143` | `3418` | `ENABLE_DISABLE_LED_COMMAND` | `0` = All Led Enabled; `1` = Presence Led Enabled - State Update Led Disable; `2` = Presence Led Disable - State Update Led Enable; `3` = All Led Disable (entire reusable range retained) | `0` | Enable-Disable LED |
| `774` | `143` | `3419` | `PRESENCE_LED_INTENSITY_LEVEL_COMMAND` | `0` = Standard level; `1` = High intensity level (entire reusable range retained) | `0` | Presence LED intensity level |
| `774` | `145` | `3522` | `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard (entire reusable range retained) | `16` | Installation level |
| `774` | `145` | `3523` | `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `15` = Local bus 15; `16` = All systems (entire reusable range retained) | `0` | Destination level |
| `774` | `145` | `3524` | `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety (entire reusable range retained) | `1` | Priority |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion reference is attached to these slot rows. Resolve the active Object and apply its firmware-specific domain restrictions separately. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `111` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| Lighting actuator | Two designated Object `6` placements; relay and load behavior is reusable catalogue capability | [`WHO 1`](../../functional/who-1-lighting/) |
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

The catalogue configuration modes and firmware `774` associations are listed above. Resolve the active Object and preserve the command, actuator and UI placements separately. Candidate membership is not simultaneous activation, and a multi-slot Object cannot be assumed to coexist with another Object occupying its span. No slot-condition or referenced conversion row supplies selection precedence.

Apply Object `6` restrictions independently to the two actuator Modules. Its LOCAL_BUTTON subset excludes the reusable default; this does not authorize choosing a replacement. Reusable zero-crossing and relay-state options are not a prescribed mains-wiring or load-rating procedure.

Object `430` N1 is restricted to `100..255`, excluding default `0`; no replacement is established. Object `145` DEST_LEV omits value `14` in both its reusable domain and the retained filter, even though similarly named destination domains include it. Preserve those exact scopes. No exact-product manual establishes commissioning, reset, transfer, update, physical configurator meanings or wiring; those procedures remain open rather than borrowed from similarly named controls.

## Source reconciliation

The complete canonical catalogue defines this technical item and its catalogue-established identities, firmware, Module/Object/Virgin topology, legal fields, filters, modes and related parameter/connection/package metadata. The retained publisher source is incorporated as excluded similar-reference evidence only. Its dimensions, electrical ratings, functions and installation instructions describe a different product and are not attributed to this Device.

| Issue | Reconciliation / unresolved limit | Evidence |
| --- | --- | --- |
| Catalogue identity | All three SKUs explicitly map to item `2247`; missing exact-product PDFs affect documentation coverage, not identity status | Canonical `EN_DEVICE` records |
| Excluded source applicability | The retained similar-reference source describes a different product/line. No equivalence is established, and its specifications are not transferred; this does not invalidate the catalogue mappings | Documentation inventory and source-scoped comparison |
| Shared item versus physical substitution | The H, LN and Legrand references share this catalogue technical item. That grouping does not establish interchangeable physical parts or equivalence to newer Living Now K-series products | Explicit catalogue mappings; physical interchangeability not documented |
| Firmware build | Firmware `774` is `1.0` with no build row; not default. Neither catalogue status nor absent build proves a shipped release | Canonical `EN_FIRMWARE` / build associations |
| Staircase-light default | Object `430` N1 effective domain `100..255` excludes default `0`; no replacement | Attached firmware filter |
| Destination-domain hole | Object `145` DEST_LEV omits `14`; similar domains do not fill the gap | Reusable Object and firmware filter |
| Virgin/direct membership | Allowed generic Virgin Objects and firmware-associated active Objects differ; no automatic conversion is proven | Exact relations enumerated above |
| Local-button restriction | Object `6` LOCAL_BUTTON permits `1/9/15/18`, excluding reusable default `0`; filter `3655` gives no replacement | Exact firmware/Object filter |
| Actuator semantics | Two Object `6` placements expose relay reset, zero crossing, timing and ten groups in the reusable definition; physical relay ratings remain unknown | Catalogue metadata; no matching installation sheet |

## Evidence limits and open work

- Locate exact-product sheets, instructions or packaging for `H4672M2L`, `LN4672M2L` and `067586` to establish physical specifications and product-specific procedures.
- Establish physical ratings, wiring, mounting, controls and complete commissioning/reset/update procedures.
- Corroborate accepted Object selection, Virgin transitions, multi-slot occupancy and firmware restrictions; no parameter-file association is stored for this item.
- Obtain sanitized hardware evidence for installed firmware/build, hardware revision, MCU identity and functional behavior; none is retained.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0111-0120-2026-10-06.md#own-dev-0112)
