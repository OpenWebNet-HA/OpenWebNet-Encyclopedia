# Flush mounted alarm central unit

## Summary

This flush-mounted alarm central unit manages a four-zone burglar-alarm installation. Its local contact input, internal relay and programmable automations allow configured alarm or system events to trigger associated actions, with stored events available for review.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0088` | Project identity |
| Technical description | Flush-mounted four-zone alarm central unit with local contact and automation relay | Canonical catalogue + `U2860B` |
| Commercial identities | `HC/HS/HD4601`, `L/N/NT4601` | Canonical commercial records |
| Catalogue item | `160` | Canonical catalogue |
| Main catalogue system | Burglar alarm system | Canonical catalogue |
| Item model / `modobj` | `200` | Canonical inventory |
| Firmware definition | `1.0.10` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Burglar alarm system, Burglar alarm | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC/HS/HD4601` | Catalogue association; publisher manual names this family | Catalogue item `160`; `U2860B` cover, PDF p. 1 |
| BTicino | `L/N/NT4601` | Catalogue association; publisher manual names this family | Catalogue item `160`; `U2860B` cover, PDF p. 1 |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| `U2860B.pdf` | installation manual | `U2860B`, `11/09-01 PC` | 4601 family on cover, PDF p. 1; English functions printed pp. 68-69 / PDF pp. 68-69; installation and programming printed pp. 70-105 / PDF pp. 70-105; update printed p. 115 / PDF p. 115; technical data printed p. 116 / PDF p. 116; Italian equivalents printed pp. 10-47, 57-58 / PDF pp. 10-47, 57-58 | [Archived original](https://archive.openwebnet-ha.org/sha256/6a/82/6a8296490e7ec2cf53f48620225dd6bbbac389a146e1eb3ad8e4a30fc2cfd14c.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/U2860B.pdf) |
| `20130411_82719_2.pdf` (`4601 NL`) | Dutch installation manual | Cover `11/09-01 PC`; no part number printed | `HC/HS/HD/L/N/NT4601`; cover PDF p. 1; package printed p. 5 / PDF p. 5; functions printed pp. 10-11 / PDF pp. 10-11; installation/commissioning printed pp. 12-28 / PDF pp. 12-28; settings/functions printed pp. 32-47 / PDF pp. 32-47; update, technical data and recovery printed pp. 57-59 / PDF pp. 57-59 | [Archived original](https://archive.openwebnet-ha.org/sha256/ca/b4/cab40b96a02307873e24b9ba79ac6d703bb5b79f6f7d4a45ca38886fdcd879e0.pdf) | [Publisher original](https://configuratoren.legrand.nl/documize/2013/4/20130411_82719_2.pdf) |
| `U2864B_Software_IT.pdf` | TiSecurityBasic software manual | Version 1.0; 11/09-01-PC | Complete 16-page document: workflow pp. 3–7; firmware pp. 8–11; configuration acquisition/transfer pp. 12–14. Explicit `3485B` and HC/HS/HD/L/N/NT4601 targets | [Archived original](https://archive.openwebnet-ha.org/sha256/0b/ed/0bed021e002ce15f14ea5c7a5d576c323fa31acf791967bcf7c9285eb4a3cbcf.pdf) | [Publisher source](https://dar.bticino.it/asset/Documents/U2864B_Software_IT.pdf) |

`4601 NL` below denotes the Dutch file `20130411_82719_2.pdf`. Its cover revision is November 2009; the April 2013 URL path is not a publication date. It is a separately archived 62-page Dutch edition; the Italian/English `U2860B` contains 120 pages.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply | `18..28 V` | `U2860B`, printed p. 116 / PDF p. 116; Italian technical table, printed p. 58 / PDF p. 58; `4601 NL`, printed p. 58 / PDF p. 58 |
| Current absorption | `50 mA` | `U2860B`, printed p. 116 / PDF p. 116; `4601 NL`, printed p. 58 / PDF p. 58 |
| Operating temperature | `5..40 °C` | `U2860B`, printed p. 116 / PDF p. 116; `4601 NL`, printed p. 58 / PDF p. 58 |
| Dimensions, HC/HS4601 | `118 x 105.5 x 31.7 mm` | Width x height x depth; `U2860B`, printed p. 116 / PDF p. 116; HD4601 dimensions not separately specified; `4601 NL`, printed p. 58 / PDF p. 58 |
| Dimensions, L/N/NT4601 | `118 x 105.5 x 33.2 mm` | Width x height x depth; `U2860B`, printed p. 116 / PDF p. 116; `4601 NL`, printed p. 58 / PDF p. 58 |
| Protection | `IP30` | `U2860B`, printed p. 116 / PDF p. 116; `4601 NL`, printed p. 58 / PDF p. 58 |
| Local relay contact | `12/24 V`, `1 A` | Literal source rating; voltage type not specified; `U2860B`, printed p. 116 / PDF p. 116; `4601 NL`, printed p. 58 / PDF p. 58 |
| Installation housing | Flush-mounted box `506E` | `U2860B`, printed p. 72 / PDF p. 72 |
| Tamper accessory | Rear device `L4630` | `U2860B`, printed p. 71 / PDF p. 71 |
| Local hardware interfaces | Graphic display, alphanumeric/navigation keys and transponder reader | `U2860B`, printed p. 64 / PDF p. 64 |
| Rear connections / controls | SCS BUS, local contact, relay contacts, serial `PROG` connector, `RESET` button and slide switch | `U2860B`, printed p. 70 / PDF p. 70 |
| Backup battery | Battery supplied; capacity, chemistry and voltage not established by this manual | Italian package list, printed p. 5 / PDF p. 5; battery connection `U2860B`, printed p. 70 / PDF p. 70 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `160` | Canonical catalogue |
| Technical item | Flush mounted alarm central unit | Canonical catalogue |
| Main system | Burglar alarm system | Canonical catalogue |
| Item model / `modobj` | `200` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Burglar alarm system | `200` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Burglar alarm | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `142` | `HC/HS/HD4601` | `1` | `2` | `BTicino_Axolute_Flush mounted alarm central u` |
| `160` | `L/N/NT4601` | `1` | `4` | `BTicino_L/N/NT_Flush mounted alarm central un` |

| Record | Visible | Dependent | Gateway flag | Visibility type |
| --- | --- | --- | --- | --- |
| `142` | `1` | `0` | `0` | Empty in source |
| `160` | `1` | `0` | `0` | Empty in source |

These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `22` | `1` | `0` | `10` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `22` | `61` | BTicino (key `1`) | `0` | external software | `TiSecurityBasic_0100` |

All 1 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `22` | `1` | `11` Burglar alarm 4 zones control unit | Fixed/designated metadata | `2297` | `11` | `975` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `22` | Product Programming | `3` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `22` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `11` - Burglar alarm 4 zones control unit

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZONA1` | `1..4` | `1` | First zone AI |
| `ALLARME` | `0..9` | `0` | Allarm setting |

### Published product settings outside the reusable Object field list

| Product setting | Published values / behavior | Evidence |
| --- | --- | --- |
| Local contact `MOD` | `0`: normally closed; `1`: normally closed with delay; `2`: normally open; `3`: normally open with delay | `U2860B`, printed p. 75 / PDF p. 75 |
| Local contact `Z` / `N` | Zone and peripheral number assigned during learning; this page gives an example, not a complete legal domain | `U2860B`, printed p. 75 / PDF p. 75 |
| Intrusion / tamper siren duration | Selectable menu values from brief to `10 min`; intermediate values are not enumerated | `U2860B`, printed p. 103 / PDF p. 103 |
| Entry / exit delay | Selectable menu values between `0 s` and `3 min` for delay-capable devices | `U2860B`, printed p. 103 / PDF p. 103 |
| Per-device delay | Disabling a delayed device's entry delay leaves the configured exit delay effective | `U2860B`, printed p. 103 / PDF p. 103 |
| Clock role | Master distributes time every `10 min`; only one Master per system; others are Slaves; installer access required | `U2860B`, printed p. 96 / PDF p. 96 |
| Device name | Maximum `16` characters for a peripheral's assigned name | `4601 NL`, printed p. 36 / PDF p. 36 |
| Local presentation | Display contrast adjustable; numerical range not specified | `4601 NL`, printed p. 45 / PDF p. 45 |
| Delay acoustic signal | Enable a sound indication on the central unit and system arming interfaces for the configured delay time, where delayed devices are present | `4601 NL`, printed p. 45 / PDF p. 45 |
| Credential use | Transponder, remote and numeric-code entries can individually be enabled or disabled | `4601 NL`, printed p. 45 / PDF p. 45 |
| Periodic interconnection check | Installer can enable or disable the check; disabling suppresses alarms caused by interrupted communication | `4601 NL`, printed p. 47 / PDF p. 47 |
| External siren flash | Armed: `3` flashes; disarmed: `1` flash | `4601 NL`, printed p. 47 / PDF p. 47 |

These local menu settings supplement reusable Object `11`'s `ZONA1`/`ALLARME` fields. The manual supplies no mapping to those catalogue fields, to `AID`, or to diagnostic serialization.

### Device-specific interpretation

Official/default firmware `22`=1.0.10 has one Module with Object `11`, AID only and Product Programming `3`. All six HC/HS/HD/L/N/NT commercial variants map to item `160`. Object `11` has only ZONA1ALLARME and ALLARME reusable fields; complete local-contact, relay, learning and access settings remain in the published product section and are not squeezed into that small schema. No Virgin/condition/filter/conversion, connection or package association is stored; parameter `61` brand `1`, line `0` is shared with the distinct `3485B` item, without proving hardware equivalence. Zones `0` and `5` are bookkeeping/technical contexts, not extra sensor zones or diagnostic Modules.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | - | None | - | No relation-specific filters associated | - | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `160` / `modobj = 200` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`11`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `11` Burglar alarm 4 zones control unit | Burglar alarm system | Firmware/Object capability association; resolve the slot and configuration first |

Catalogue system identifiers are not `WHO` numbers. The source establishes the roles shown, not a complete command vocabulary or proof of every installed function. Correlate the selected role with [Functional Protocol](../../functional/) before sending functional commands. Product functions below are publisher evidence; installed behavior and remote transport acceptance still require corroboration.

### Published 4601 functions

| Function | Published scope / limit | Evidence |
| --- | --- | --- |
| Zone model | Six bookkeeping zones: `0` for arming interfaces, maximum `9`; `1..4` for sensors; `5` for technical/auxiliary alarms | `U2860B`, printed p. 68 / PDF p. 68 |
| Partition scenarios | Maximum `4`; all initially enabled with all sensor zones active; names and included zones can be changed | `U2860B`, printed p. 68 / PDF p. 68; scenario setup printed p. 80 / PDF p. 80 |
| Sensors | Independent management and exclusion; failed communication shows an icon when disarmed and produces an alarm when armed | `U2860B`, printed p. 68 / PDF p. 68 |
| Arming / disarming | Local keypad codes, transponder keys, supported radio remote and other documented system controls | Printed pp. 85-86, 106-107 / PDF pp. 85-86, 106-107 |
| Radio remote prerequisite | Remote `348220` requires a `L/N/NT/HC/HS/HD4618` receiver | `U2860B`, printed p. 85 / PDF p. 85 |
| Incorrect credentials | Three consecutive incorrect entries block further arming/disarming or menu access for `1 min` | `U2860B`, printed p. 68 / PDF p. 68; keypad access printed p. 90 / PDF p. 90 |
| Event memory | Last `200` events with time, type and detecting sensor; installer access required to erase | `U2860B`, printed p. 95 / PDF p. 95 |
| Local automations | `10` entries: first operates the internal relay; other `9` associate partition scenarios with arming, disarming or date/time events | `U2860B`, printed p. 97 / PDF p. 97 |
| Alarm relay | Intrusion/tamper and battery/mains faults use positive safety with `1 s` deactivation; NC contact closes for that interval | `U2860B`, printed p. 99 / PDF p. 99 |
| Technical-alarm relay | Positive safety enabled: NC opens at rest and closes for alarm; disabled: inverse contact behavior | `U2860B`, printed p. 99 / PDF p. 99 |
| Technical-alarm memory | Enabled: alarm relay state persists until next arming/disarming; disabled: follows the originating alarm condition | `U2860B`, printed p. 99 / PDF p. 99 |
| System-state relay | Relay active when armed and at rest when disarmed | `U2860B`, printed p. 99 / PDF p. 99 |
| Event indications | Intrusion, anti-panic, tamper, technical alarms, power/battery, device communication, maintenance and key/code events | Printed pp. 113-114 / PDF pp. 113-114; user display indications, printed pp. 66-67 / PDF pp. 66-67 |

The Dutch manual corroborates the zone/scenario model and the three-error, one-minute access block (printed p. 10 / PDF p. 10), radio-remote prerequisite (printed p. 27 / PDF p. 27), 200-event memory (printed p. 37 / PDF p. 37), ten local automations (printed p. 39 / PDF p. 39) and relay modes (printed p. 41 / PDF p. 41).

| Additional product surface | Published scope / limit | Evidence |
| --- | --- | --- |
| Internal-relay event selection | Alarm family: intrusion, 24-hour, panic, silent, alarm end; technical: auxiliary channels `1..9`; system fault: missing mains, low battery, mains restored; system state | `4601 NL`, printed p. 39 / PDF p. 39; illustrated event-selection tree |
| Other automation triggers | Arming/disarming selected by zone state, arming interface or key; date/time trigger | `4601 NL`, printed p. 39 / PDF p. 39; slots `2..10` |
| Automation management | Each configured automation can be enabled, disabled or removed; the displayed action is the available action for the current state | `4601 NL`, printed p. 44 / PDF p. 44 |
| Peripheral deactivation | All devices initially active; deactivation affects intrusion and 24-hour functions; source says arming interfaces remain operative when zone-0 devices are deactivated | `4601 NL`, printed p. 36 / PDF p. 36; scope and exception retained |

### Commands entered in the product automation menu

| Manual form | Documented result | Scope / evidence |
| --- | --- | --- |
| `*5*8#.........##` | Arm and set active zones to the listed zone numbers | `U2860B`, section 6.6, printed p. 102 / PDF p. 102; dots denote the zone list |
| `*5*9#.........##` | Disarm and set active zones to the listed zone numbers | Same product-menu scope and source |
| `*5*8#12##` | Published example: arm or remain armed; zones `1` and `2` active, `3` and `4` excluded | Same source; equivalent Italian example, printed p. 44 / PDF p. 44 |

The Dutch manual also prints the same two forms and the zone-1/2 example (printed p. 44 / PDF p. 44). The manuals establish these forms as codes entered into the 4601 automation menu. They do not establish a gateway session, TCP acceptance, acknowledgement sequence or unrestricted remote alarm control. Cross-reference [`WHO 5` - Alarm](../../functional/who-5-alarm/) for the broader protocol; do not generalize the product-menu context.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

The catalogue registers Product Programming for firmware `22`. `U2860B` establishes local commissioning and PC-assisted firmware update; its menu operations are separate from OpenWebNet runtime commands.

### Installation and first activation

| Stage | Documented procedure / prerequisite | Evidence |
| --- | --- | --- |
| Battery and installation | Slide switch at `OFF` while connecting the battery with the indicated polarity; protect the rear with `L4630`; switch to `ON` before final fastening in `506E` | Printed pp. 70-72 / PDF pp. 70-72 |
| Initial learning | Choose language; run device learning; configure or skip the local input; enable the slide switch and leave Maintenance with `C` | Printed pp. 73-77 / PDF pp. 73-77 |
| System test | Return to Maintenance and test sensor operation without raising normal alarm events | Printed pp. 78-79 / PDF pp. 78-79 |
| Credentials and personalization | Enroll transponders, five-digit numeric codes or supported radio remotes; set date/time, names and scenarios | Printed pp. 80-89 / PDF pp. 80-89 |
| Changed installation | Repeat learning after adding or removing devices | `U2860B`, printed p. 76 / PDF p. 76 |

### Access, update and recovery

| Path | Published behavior / boundary | Evidence |
| --- | --- | --- |
| User access | Keypad access permits normal operation and selected customization; Maintenance unavailable and automation/event-memory operations restricted | `U2860B`, printed p. 90 / PDF p. 90 |
| Installer access | Maintenance code gives installer menus; does not arm/disarm and cannot enter menus while armed | `U2860B`, printed p. 91 / PDF p. 91; access details printed p. 105 / PDF p. 105 |
| Factory codes | User and Maintenance share `00000` as the publisher's documented factory default; distinguish them by changing Maintenance first | Printed pp. 91, 103, 105 / PDF pp. 91, 103, 105 |
| Leaving Maintenance | Use `C`; this menu has no automatic `30 s` inactivity exit | `U2860B`, printed p. 105 / PDF p. 105 |
| Firmware update | Set rear slide switch to `OFF`, connect the programming cable when prompted and follow TiSecurityBasic; source names cables `3559` / `335919` | `U2860B`, printed p. 115 / PDF p. 115; Italian procedure printed p. 57 / PDF p. 57 |
| Installer-code recovery | Italian/English procedure and Dutch troubleshooting table require disarmed state; Dutch section 6.9 instead says armed, see Source reconciliation. Removal causes a tamper alarm; rear switch `OFF` plus `RESET` enters Maintenance to access the code | `U2860B`, printed pp. 47, 105, 117 / PDF pp. 47, 105, 117; `4601 NL`, printed pp. 47, 59 / PDF pp. 47, 59 |
| Lost user code | Reprogram with TiSecurityBasic | `U2860B`, printed p. 117 / PDF p. 117 |

The Dutch edition corroborates battery polarity and switch-`OFF` connection, rear interfaces and programming cables (printed p. 12 / PDF p. 12), learning and local-contact `MOD = 0..3` (printed pp. 17-19 / PDF pp. 17-19), and the firmware-update procedure (printed p. 57 / PDF p. 57). It also specifies these credential and access details:

| Path | Published behavior / boundary | Evidence |
| --- | --- | --- |
| Transponder enrollment | Hold key less than `1 cm` from the reader; assign a name, save and enable it; already-known keys select the existing record | `4601 NL`, printed pp. 23-24 / PDF pp. 23-24 |
| Numeric-key enrollment | Five-digit code; already-known code selects its existing entry; name, save and enable it | `4601 NL`, printed pp. 25-26 / PDF pp. 25-26 |
| Radio-key enrollment | Press a remote button, then name, save and enable the entry; already-known remote selects its existing record | `4601 NL`, printed pp. 27-28 / PDF pp. 27-28; receiver prerequisite above |
| User programming | Keypad code only; scenario/key naming and enabling, numeric-code updates, automation enable/disable and event viewing permitted; event deletion unavailable | `4601 NL`, printed p. 32 / PDF p. 32 |
| Installer programming | Keypad Maintenance code; all menus except changing the user code; cannot arm/disarm or access menus while the installation is armed | `4601 NL`, printed pp. 33, 47 / PDF pp. 33, 47 |
| Learning options | Automatic scan configures peripherals; manual path inspects and stores connection, device type and tamper state | `4601 NL`, printed p. 46 / PDF p. 46 |
| Key maintenance actions | New, Share (multiple installations), Update, Select (display numeric code), Delete and Delete all; source describes these as key operations, not a central-unit factory reset | `4601 NL`, printed p. 46 / PDF p. 46 |

The separately retained TiSecurityBasic manual now supplies the PC workflow below. Pressing `RESET` in the documented recovery context enters Maintenance; it is not evidence of a full factory erase. The manual does not identify an update package matching catalogue firmware `1.0.10`.

### TiSecurityBasic transfer and update

TiSecurityBasic explicitly selects the correct target, `3485B` or HC/HS/HD/L/N/NT4601. Its Version 1.0 is a software version (`U2864B`, PDF pp. 8–11), not installed panel firmware. For firmware update: enter Maintenance, move the rear slide to OFF, connect serial 335919 or USB 3559 at the six-pin connector, choose the COM port and .fwz file, follow the transfer, disconnect, move slide ON and press physical RESET. That post-update RESET is not documented as a factory erase.

For configuration acquisition/transfer, pp. 12–14 separately describe Maintenance, six-pin connection, COM selection and saving/opening a configuration file. Acquisition retains a backup; transfer restores a saved configuration or transfers it to another correctly selected target. Those pages do not prescribe the update-specific OFF/ON/RESET sequence. No edited parameter domain or transport mapping is inferred from the screenshots. The complete product’s local commissioning still requires its exact hardware manual.

## Source reconciliation

The cover of `U2860B`, revision `11/09-01 PC`, explicitly names `HC/HS/HD/L/N/NT4601`. Both language sections document flush installation and the technical appendix identifies this family. The publisher manual therefore directly supports this dossier's commercial coverage and the physical, functional and commissioning facts recorded above. The four sensor zones agree with reusable Object `11`; the manual's additional zones `0` and `5` are arming-interface and technical-alarm bookkeeping, not additional protocol Modules.

The manual contains source irregularities. Its Italian package list identifies 4601 (printed/PDF p. 5), but the English list identifies `3485B` and a wall bracket (printed/PDF p. 63). Its test-menu text also mentions telephone calls (printed/PDF pp. 46, 104), without identifying a telephone connection in the 4601 rear-interface diagram. These statements do not establish equivalence to Device `OWN-DEV-0086`, a communicator or a telephone port. Dimension rows explicitly name HC/HS4601 and L/N/NT4601; no separate HD4601 dimension is supplied. The relay rating omits AC/DC qualification and the battery specification is incomplete, so neither is inferred.

The Dutch manual names the same commercial family on its cover and correctly identifies 4601 in its packing list (printed p. 5 / PDF p. 5), corroborating the Italian list rather than the English `3485B` label. It supplies the same technical ratings (printed p. 58 / PDF p. 58), but still omits separate HD dimensions and battery ratings. Its test-menu text also retains telephone-call wording (printed p. 46 / PDF p. 46), so this language edition does not resolve the unsupported telephone capability.

Dutch section 6.9 says the installation must be `ingeschakeld` (armed) before Maintenance-code recovery (printed p. 47 / PDF p. 47), whereas its troubleshooting table says `uitgeschakeld` (disarmed) for the same procedure (printed p. 59 / PDF p. 59). The Italian and English procedures and English troubleshooting table all specify disarmed state (`U2860B`, printed pp. 47, 105, 117 / PDF pp. 47, 105, 117). The Dutch Maintenance access paragraph on p. 47 also bars access while armed. Preserve this internal translation contradiction; the dossier does not promote the armed-state variant as a verified procedure.

Local menu settings and automation command forms remain scoped to the published product procedure. The manual neither identifies the installed firmware tuple nor supplies a serialization mapping to the catalogue configuration fields. The catalogue remains the source of firmware `22`, Module slot `1` and external Object `11`; hardware and remote-transport corroboration remain open.

The Dutch package list also retains a metal wall-mounting base despite the family’s documented flush installation; the correct 4601 name does not resolve every packing-list detail. TiSecurityBasic explicitly covers all six 4601 variants and separately the `3485B`. Its update and configuration-transfer procedures have different switch/reset requirements; the shared software does not establish identical hardware or a telephone connection.

Catalogue interpretation is detailed under [Object configuration surfaces](#object-configuration-surfaces); the complete firmware, topology and restriction tables remain authoritative for software applicability.

## Evidence limits and open work

- Retain the English packing-list error despite the Italian/Dutch corroboration of 4601; resolve telephone-call wording and the Dutch armed/disarmed recovery contradiction with further exact-product evidence.
- Establish HD4601 dimensions, backup-battery voltage/capacity/chemistry and local relay voltage type from a directly applicable specification.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate the local-menu to catalogue/diagnostic mapping and any gateway acceptance of the published automation-menu codes on controlled hardware.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [4601 installation manual, archived original](https://archive.openwebnet-ha.org/sha256/6a/82/6a8296490e7ec2cf53f48620225dd6bbbac389a146e1eb3ad8e4a30fc2cfd14c.pdf)
- [Dutch 4601 installation manual, archived original](https://archive.openwebnet-ha.org/sha256/ca/b4/cab40b96a02307873e24b9ba79ac6d703bb5b79f6f7d4a45ca38886fdcd879e0.pdf)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0081-0090-2026-10-06.md#own-dev-0088)
