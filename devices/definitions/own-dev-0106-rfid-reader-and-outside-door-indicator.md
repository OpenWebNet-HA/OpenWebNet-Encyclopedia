# RFID reader and outside-door DND/MUR indicator

## Summary

This outside-door unit combines an RFID room-access reader with Do Not Disturb, Make Up Room and presence indications. It recognizes documented Mifare cards and can operate a configured bell or door-release arrangement, with access-management functions dependent on the installed hotel system.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0106` | Project identity |
| Technical description | RFID reader and outside-door DND/MUR indicator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `H4651`, `LN4651`, `067591` | All three catalogue commercial records; confidence scoped below |
| Catalogue item | `1681` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Access control | Main system association |
| Item model / `modobj` | `6` | Main association; independent of project ID |
| Firmware definition | `254` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Commands, User interfaces | Source-derived roles |

DND means Do Not Disturb; MUR means Make Up Room. This reader is separate from the non-RFID 4650 indicator. Two physical wiring-device modules contain one catalogue Module. Mifare compatibility and visual alarms have an explicit production-lot boundary.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4651` | Established commercial variant | Catalogue record `1737`; published family/variant scope reconciled below |
| BTicino - LivingLight | `LN4651` | Established commercial variant | Catalogue record `1999`; published family/variant scope reconciled below |
| Legrand - Céliane | `067591` | Established commercial variant | Catalogue record `2000`; published family/variant scope reconciled below |

The publisher technical sheets name all three references together. The catalogue `L/N/NT` grouping is marketed as LivingLight for `LN4651`. `3547` is a card accessory, not a fourth reader identity.

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `H4651` | `8005543502563` | [Archived original](https://archive.openwebnet-ha.org/sha256/31/2d/312de05eac5c7e1ba2ec242feb4dba44daea6bcf456b76788df056b0f97886e9.pdf), `H4651-publisher-product-sheet.pdf`, printed/PDF p. 1 |
| `LN4651` | `8005543502587` | [Archived original](https://archive.openwebnet-ha.org/sha256/13/1e/131ee5ff8ae4cf69a158b11ed49f06174dd0e8fb8ab5eca46936a7f6ebdd4204.pdf), `LN4651-publisher-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MM00776_c_EN.pdf` | English technical sheet | `MM00776-c-EN; 22/05/2015` | All three references; specifications/lot boundary p. 1; modes p. 2; cards and two wiring examples p. 3; hotel-room diagram p. 4. Printed and PDF pp. 1-4 coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/c0/8c/c08cb70885340cf17728b2b7622cb3cd488f22c6b7dde910e93ef46da26c13d5.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MM00776_c_EN.pdf) |
| `MM00776-c-FR.pdf` | French technical sheet | `MM00776-c-FR; 22/05/2015` | All three references; printed and PDF pp. 1-4 coincide, including card procedures and hotel-room wiring. | [Archived original](https://archive.openwebnet-ha.org/sha256/cf/38/cf3830140b6c58c9a6c7c7b4ecc276377a47ddb68b520a03f2e5921048122550.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MM00776-c-FR.pdf) |
| `LE06116AC.pdf` | Multilingual installation / radio declarations | `LE06116AC-02PC-19W15` | Shared 4650 indicator and 4651 reader families; reader-specific RF declaration, label removal/printing/refitting; no printed pagination / PDF p. 1. | [Archived original](https://archive.openwebnet-ha.org/sha256/19/00/1900dc5ccac4aff7c789eb73808d36b7bae7ad046bf9bc34bd0d7e574e1ea41e.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/LE06116AC.pdf) |
| `H4651-publisher-product-sheet.pdf` | Manufacturer product export | `DATASHEET; 03.10.2026` | `H4651` description, commercial line and attributes; printed and PDF pp. 1-3 coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/31/2d/312de05eac5c7e1ba2ec242feb4dba44daea6bcf456b76788df056b0f97886e9.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-H4651&include_technical=1) |
| `LN4651-publisher-product-sheet.pdf` | Manufacturer product export | `DATASHEET; 03.10.2026` | `LN4651` description, marketed line and attributes; printed and PDF pp. 1-3 coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/13/1e/131ee5ff8ae4cf69a158b11ed49f06174dd0e8fb8ab5eca46936a7f6ebdd4204.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-LN4651&include_technical=1) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1681`: all firmware/commercial/system/Object/Module/Virgin/field/filter/mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | Two flush-mounted wiring-device modules | `MM00776-c-EN/FR`, printed p. 1 / PDF p. 1 |
| Supply | `18..27 Vdc` from SCS BUS | `MM00776-c-EN/FR`, printed p. 1 / PDF p. 1 |
| Current conditions | Standby `10 mA`; relay active `20 mA`; RFID maximum `55 mA` | `MM00776-c-EN/FR`, printed p. 1 / PDF p. 1 |
| Operating temperature | `5..40 °C` | `MM00776-c-EN/FR`, printed p. 1 / PDF p. 1 |
| Relay contact | Normally open; `12 Vac/dc..230 Vac`, maximum `1 A`; bell or lock function | `MM00776-c-EN/FR`, printed p. 1 / PDF p. 1 |
| Reader technology | Mifare Classic `ISO 14443`, including card `3547`, lot `14w40` or later | `MM00776-c-EN/FR`, printed p. 1 / PDF p. 1 |
| Radio frequency | `13.56 MHz`; reader family explicitly named | `LE06116AC-02PC-19W15`, no printed pagination / PDF p. 1 |
| Alarm boundary | White backlight visual alarm requires MH201, MyHOME Suite programming and lot `14w40` or later | `MM00776-c-EN/FR`, printed p. 1 / PDF p. 1 |
| Front controls/status | Call key; red DND; green MUR; customizable white room label; reader LED green=valid, red=error, flashing=card programming | `MM00776-c-EN/FR`, printed p. 1 / PDF p. 1 |
| Rear interfaces | SCS, configurator socket, normally open relay; wiring sketches mark `L1`, `L` | `MM00776-c-EN/FR`, printed p. 1 / PDF p. 1; `MM00776-c-EN/FR`, printed p. 3 / PDF p. 3 |
| Physical positions | `R1`, `R2`, `M`, `L`, `A`, `PL`, `T` | `MM00776-c-EN/FR`, printed p. 2 / PDF p. 2 |
| `H4651`/`LN4651` metric size | `45 x 45 x 24 mm`; minimum box depth `55 mm`; `IP20` | Both original product exports, printed/PDF p. 2 |
| `H4651`/`LN4651` storage/connection | `-10..70 °C`; terminals `0.34..2.5 mm²`, flexible or rigid wire | Both product exports, pp. 2-3 |
| `H4651` construction | Thermoplastic; untreated glossy finish, transparent attribute; RAL-like `9011` | `H4651` export p. 2; no Céliane extension |
| SKU-scoped attributes | Both exports: bidirectional radio Yes; RF bus No; SCS; one actuation point/button; LED and no display, thermostat or IR sensor. `H4651` label-area Yes | Exports pp. 2-3; radio bus classification distinct from card-reader RF |
| Published standards | `EN 60669-2-1`, `EN 50491-5-1`, `EN 50428` | `MM00776-c-EN/FR`, printed p. 1 / PDF p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1681` | Canonical catalogue |
| Technical item description | DO NOT DISTURB-MAKE UP ROOM reader | Canonical catalogue |
| Item family | Device for Access Control system; key `101` | Canonical catalogue |
| Main system | Access control; key `8` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `6` | `AS_ITEM_SYSTEM` |
| Commercial record count | `3` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `254` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `254` | `1` | `488` Hotel indicator | Fixed/designated metadata | `1345` | `554` | `703` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `254` | Virtual Configuration | `1` | Association key `1` |
| `254` | Advanced Configuration | `2` | Association key `2` |
| `254` | Physical configuration | `0` | Association key `3` |


No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

The published physical route uses rear configurators. MyHOME Suite uses Ethernet through external MH201 on SCS, not an Ethernet port on this reader. The registered Virtual/Advanced/Physical labels do not establish wire-level programming mechanics.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `254` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `254` | `R1` | `0..9` | `0` | Room tens |
| `254` | `R2` | `0..9` | `0` | Room unit |
| `254` | `M` | `0..2` | `0` | DND/MUR indicator mode; (Stand alone with SCE: 0) (Stand alone with `CEN`: 1) (With IP Scenario Module: 2) |
| `254` | `L` | `0..7` | `0` | led function; 0 : Presence `ON=occupied`, Presence `OFF=free`; DND Active; MUR Active 1 : Presence `ON=occupied`, Presence `OFF=free`; DND Active; MUR Hidden 2 : Presence `ON=free`, Presence `OFF=occupied`; DND Active; MUR Active 3 : Presence `ON=free`, Presence `OFF=occupied`; DND Active; MUR Hidden 4 : Presence always `ON`; DND Active; MUR Active 5 : Presence always `ON`; DND Active; MUR Hidden 6 : Presence always `OFF`; DND Active; MUR Active 7 : Presence always `OFF`; DND Active; MUR Hidden |
| `254` | `A` | `0..9` | `0` | Area; address of door lock actuator (if not configured, the on board relay of the indicator is used for door lock) |
| `254` | `PL` | `0..9` | `0` | Light point; address of door lock actuator (if not configured, the on board relay of the indicator is used for door lock) |
| `254` | `T` | `0..9` | `0` | Relay timing for door lock acutator; (0=0.5s, 1...9 = 1s...9s) |

### Published physical meanings

| Configurator | Meaning | Evidence |
| --- | --- | --- |
| `R1`, `R2` | Room tens and units | `MM00776-c-EN/FR`, printed p. 2 / PDF p. 2 |
| `M=0` | F420; catalogue standalone scenario mode | `MM00776-c-EN/FR`, printed p. 2 / PDF p. 2 |
| `M=1` | MH200N; catalogue standalone `CEN` mode | `MM00776-c-EN/FR`, printed p. 2 / PDF p. 2 |
| `M=2` | MH201; catalogue IP scenario-module mode | `MM00776-c-EN/FR`, printed p. 2 / PDF p. 2 |
| `A`, `PL` | SCS address of external door-lock actuator; absent actuator configuration uses on-board relay per firmware description | `MM00776-c-EN/FR`, printed p. 2 / PDF p. 2; firmware `254` |
| `T=0` | `0.5 s` | `MM00776-c-EN/FR`, printed p. 2 / PDF p. 2 |
| `T=1..9` | `1..9 s`, value equals seconds | `MM00776-c-EN/FR`, printed p. 2 / PDF p. 2 |

### Complete physical LED mapping

| `L` | White backlight | Red DND | Green MUR | Evidence |
| --- | --- | --- | --- | --- |
| `0` | On occupied / off free | Enabled | Enabled | `MM00776-c-EN/FR`, printed p. 2 / PDF p. 2 |
| `1` | On occupied / off free | Enabled | Disabled | `MM00776-c-EN/FR`, printed p. 2 / PDF p. 2 |
| `2` | On free / off occupied | Enabled | Enabled | `MM00776-c-EN/FR`, printed p. 2 / PDF p. 2 |
| `3` | On free / off occupied | Enabled | Disabled | `MM00776-c-EN/FR`, printed p. 2 / PDF p. 2 |
| `4` | Always on | Enabled | Enabled | `MM00776-c-EN/FR`, printed p. 2 / PDF p. 2 |
| `5` | Always on | Enabled | Disabled | `MM00776-c-EN/FR`, printed p. 2 / PDF p. 2 |
| `6` | Always off | Enabled | Enabled | `MM00776-c-EN/FR`, printed p. 2 / PDF p. 2 |
| `7` | Always off | Enabled | Disabled | `MM00776-c-EN/FR`, printed p. 2 / PDF p. 2 |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `488` - Hotel indicator

Catalogue Object key `554` maps to external Object `488`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `R1R2` | `0..99` | `01` | Room address |
| `DND_ENABLE` | `0` = Enabled; `1` = Disabled | `0` | Enable DO NOT DISTURB indicator |
| `MUR_ENABLE` | `0` = Enabled; `1` = Disabled | `0` | Enable MAKE UP ROOM indicator |
| `PRESENCE_LED` | `0` = `ON=Presence`, `OFF=No` presence; `1` = `OFF=Presence`, `ON=No` presence; `2` = Always `OFF`; `3` = Always `ON` | `0` | LED presence |
| `MODE` | `0` = Stand alone with scenaro; `1` = Stand alone with `CEN`; `2` = With IP Scenario Module | `0` | DO NOT DISTURB/MAKE UP ROOM indicator mode; For indicator with RFID: 0 = Badge stored locally 1 = Badge stored locally 2 = Badge stored in IPSM |
| `ENTRANCE_ENABLE_GROUP` | `0..255` | `0` | Group address enabled on entrance; Only for Mode = 0 |
| `LEAVING_DISABLE_GROUP` | `0..255` | `0` | Group address disabled on leaving |
| `APL` | `0..175`; A = floor(value / 16), PL = value modulo 16 | `0` | Address of the Key card switch |
| `LOCAL_RELAY_FUNCTION` | `0` = Doorbell; `1` = Door opening | `0` | Local relay function; In case of Doorbell, parameter "Door relay address" must be different from 0. |
| `APL_DOOR` | `0..175`; A = floor(value / 16), PL = value modulo 16 | `1` | Address of the actuator of door relay |
| `DOOR_RELAY_TIMER` | `1..100`; seconds = value / 10 (`0.1..10 s`) | `10` | Door relay timing [s] |
| `BACKLIGHT_INTENSITY` | `1` = Level 1; `2` = Level 2; `3` = Level 3; `4` = Level 4; `5` = Level 5; `6` = Level 6; `7` = Level 7; `8` = Level 8; `9` = Level 9; `10` = Level 10 | `5` | Backlight intensity |
| `ROOM_GENERIC_SERVICE` | `0` = Enabled; `1` = Disabled | `1` | Room_Generic_Service; link to PUL_Signal Frame |

The address and timer compression above preserves every enumerated catalogue value. Standalone modes `0/1` store cards locally; mode `2` stores them in the IP scenario module according to Object `488` prose. Physical `T=0` and software timer value `5` both label `0.5 s` in their separate sources; no attached conversion equates their wire encoding.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `254` | `488` | `3095` | `ROOM_GENERIC_SERVICE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Room_Generic_Service |
| `254` | `488` | `3105` | `R1R2` | `0` | `01` | Room address; reusable default `01` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion reference is attached to these slot rows. Resolve the active Object and apply its firmware-specific domain restrictions separately. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `6` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Read installed firmware and compare with the applicability table | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Obtain hardware revision; no source-backed installed value | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Obtain microcontroller identity; no fingerprint retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve active Modules/Objects independently of candidate metadata | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Corroborate installed addressing and distinguish physical from reusable ranges | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Compare installed configuration with the exact firmware/Object restrictions | [Configuration](../../diagnostics/dim35-configuration.md) |

These are catalogue-derived diagnostic candidates. No Device-specific response or support across all commercial variants is established by a hardware capture.

## Functional applicability

| Function | Applicability | Evidence / canonical reference |
| --- | --- | --- |
| Hotel access | DND/MUR/presence and RFID room access | [`WHO 23`](../../functional/who-23-access-control/); diagnostic management context `WHO 1023`, independent of catalogue system key `8` |
| Door/bell actuation | Front-key local relay or configured external door actuator; valid badge opening | Technical sheets pp. 1-3; local relay is not an unconditional Automation Object |
| Scenario integration | F420/MH200N/MH201 depends on `M`; PC card validity, guest details and access controls require MH201 | Technical sheets pp. 2-3; system integration does not add runtime Objects |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Resolve the actual firmware and Object before writing configuration. Keep two-digit room addresses separate from printed room labels: the wiring example label `110` uses bus `R1=1`, `R2=0`; label `115` uses `1`, `5`. The whole-room example label `127` uses `2`, `7`. Check production lot before relying on Mifare Classic cards or visual alarms.

| Operation | Published procedure / effect | Evidence |
| --- | --- | --- |
| First start without master | All cards are accepted until a master is programmed | `MM00776-c-EN/FR`, printed p. 3 / PDF p. 3 |
| Store master | Hold call key `10 s`, then present master card; master cannot be changed by ordinary card programming | `MM00776-c-EN/FR`, printed p. 3 / PDF p. 3 |
| Reset all cards | Disconnect supply; reconnect while holding call key `10 s`; deletes every stored card | `MM00776-c-EN/FR`, printed p. 3 / PDF p. 3 |
| Add customer | Present master (green slow flash); present customer (green steady `2 s`); press call key to finish | `MM00776-c-EN/FR`, printed p. 3 / PDF p. 3 |
| Delete customers | Present master; present again (green fast flash); third presentation gives green steady `5 s`, then off | `MM00776-c-EN/FR`, printed p. 3 / PDF p. 3 |
| Add service | Present master; press call key (orange flash); present service card (orange steady `2 s`); press call key to finish | `MM00776-c-EN/FR`, printed p. 3 / PDF p. 3 |
| Delete services | Present master; press call key; present master again (fast flash); third presentation gives orange steady `5 s`, then off | `MM00776-c-EN/FR`, printed p. 3 / PDF p. 3 |
| PC card administration | MH201-only; validity, guest information, further access controls; EN calls these scheduled accesses, FR calls these limited accesses | `MM00776-c-EN/FR`, printed p. 3 / PDF p. 3 |
| Bell plus external lock | Room 110: `M=2`, `A=1`, `PL=1`, `T=2`; front key operates local bell, valid card operates F411/1N door lock for `2 s`, actuator `M=PUL` | `MM00776-c-EN/FR`, printed p. 3 / PDF p. 3 |
| Local lock only | Room 115: `M=2`, absent `A/PL`, `T=3`; valid card operates local lock `3 s`, front key disabled; MH201 required | `MM00776-c-EN/FR`, printed p. 3 / PDF p. 3 |
| Labels and mounting | Remove front/label, print and cut room-number insert, reinsert/refit; use the shared sheet drawings | `LE06116AC-02PC-19W15`, PDF p. 1 |


The hotel-room diagram on p. 4 / PDF p. 4 includes LN4648, LN4653, LN4652, LN4691, MH201, F430R8 and F411/1N with E49. It is an example: choose protection and actuators for installed loads; E46ADCN is the published alternative if E49 current is insufficient.

## Source reconciliation

The two `c` technical-sheet translations agree on the three-reference cluster, ratings, complete physical mappings, lot restrictions, card operations and wiring. Their PC-card access descriptions differ and remain source-scoped. Shared `LE06116AC` expressly attributes the RF declaration to the reader family, while retaining non-RFID indicator mounting coverage. The H/LN exports corroborate marketed lines and add SKU-scoped construction/dimensions; they do not date installed hardware.

| Issue | Reconciliation / unresolved limit | Evidence |
| --- | --- | --- |
| Room restriction | Firmware digits default `0/0`; Object R1R2 defaults literal `01`, but filter `3105` admits only `0`, with no replacement default. Do not reinterpret this as a documented runtime ban on physical room addresses | Firmware `254`; Object `488`; published R1/R2 |
| Relay constraint | LOCAL_RELAY_FUNCTION Doorbell requires nonzero APL_DOOR in prose; legal APL_DOOR still contains `0`, with no attached conditional enforcement. Default `1` satisfies the prose, but not every legal value does | Object `488` |
| Lot boundary | Mifare/3547 and visual alarm apply from `14w40`; wildcard firmware cannot prove a pre/post-lot Physical Device | Sheets p. 1 |
| Reader/local relay | Introductory legend says relay activated by front key; local-lock wiring disables front key and uses card acceptance. These are configuration-dependent examples, not contradictory unconditional behavior | Sheets pp. 1, 3 |
| RF attribute | RF-bus No and bidirectional-radio Yes describe different attribute scopes; `13.56 MHz` identifies the card-reader radio. No RF automation bus inferred | Exports p. 2; LE06116AC |
| Unspecified limits | Card capacity, badge data format, acceptance algorithm, alarm trigger/reset and key-programming timeouts are not specified by retained sources | All reader originals |

## Evidence limits and open work

- Resolve filter `3105` room restriction and physical-to-Object mappings using actual software parameters or sanitized captures.
- Establish card capacity, pre-`14w40` card compatibility, credential semantics and alarm event/reset behavior; corroborate the published permissive pre-master state and reset sequence.
- Verify firmware/hardware identity and relay timing/feedback on all three variants. Céliane metric dimensions/protection have no exact retained product export.
- Parameter/radio payloads, production-lot behavior and current additional commercial catalogues remain beyond the retained revisions.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- `H4651-publisher-product-sheet.pdf`, printed/PDF p. 1: exact `H4651` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/31/2d/312de05eac5c7e1ba2ec242feb4dba44daea6bcf456b76788df056b0f97886e9.pdf); [publisher source](https://www.bticino.com/products/pdf?sku=BT-H4651&include_technical=1); SHA-256 `312de05eac5c7e1ba2ec242feb4dba44daea6bcf456b76788df056b0f97886e9`.
- `LN4651-publisher-product-sheet.pdf`, printed/PDF p. 1: exact `LN4651` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/13/1e/131ee5ff8ae4cf69a158b11ed49f06174dd0e8fb8ab5eca46936a7f6ebdd4204.pdf); [publisher source](https://www.bticino.com/products/pdf?sku=BT-LN4651&include_technical=1); SHA-256 `131ee5ff8ae4cf69a158b11ed49f06174dd0e8fb8ab5eca46936a7f6ebdd4204`.
