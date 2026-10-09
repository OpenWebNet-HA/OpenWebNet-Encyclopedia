# Do Not Disturb / Make Up Room indicator

## Summary

This outside-door indicator displays Do Not Disturb, Make Up Room and configured room-presence information. Its front bell button is disabled while Do Not Disturb is active, combining staff-facing status with a local call function.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0105` | Project identity |
| Technical description | Outside-door DND/MUR indicator with room-number backlight and call-bell contact | Published technical sheets; canonical catalogue |
| Commercial identities | `H4650`, `LN4650`, `067590` | Three catalogue records and both technical-sheet headers |
| Catalogue item | `1680` | Canonical MyHOME Suite `3.5.38` catalogue |
| Main catalogue system | Access control | Main item/system association |
| Item model / `modobj` | `8` | Main item/system association |
| Firmware definition | `-1.-1.-1` (wildcard / unspecified applicability) | Canonical catalogue; not an observed installed release |
| Declared Modules | `1` | Canonical firmware metadata |
| Categories | User interfaces | Source-derived roles |

DND means Do Not Disturb; MUR means Make Up Room. These are room-service notifications. Two physical wiring-device modules do not imply two protocol Modules.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4650` | Established commercial variant | Item `1680`; `MM00774-b-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| BTicino - LivingLight | `LN4650` | Established commercial variant | Item `1680`; `MM00774-b-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Legrand - Céliane | `067590` | Established commercial variant | Item `1680`; `MM00774-b-EN` / French counterpart, printed p. 1 / PDF p. 1 |

All three catalogue descriptions explicitly identify an indicator without RFID. The reader family `H4651` / `LN4651` / `067591`, item `1681`, remains a separate Device despite sharing mounting instructions.

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `H4650` | `8005543502556` | [Archived original](https://archive.openwebnet-ha.org/sha256/93/c5/93c59840ea69129a1dc5c4a6a7fd30456ec4dd7627d59fb6d04c4163c741dfa4.pdf), `H4650-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `LN4650` | `8005543502570` | [Archived original](https://archive.openwebnet-ha.org/sha256/66/bb/66bba020f08ee8c006b13559e8b03f5473ddac5e4dc7d7622affee826032862c.pdf), `LN4650-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

### Complete catalogue commercial metadata

| Record | Reference | Catalogue name | Brand key | Line key | Visible | Visibility type | Dependent | Gateway | Catalogue description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `1736` | `H4650` | `DO NOT DISTURB-MAKE UP ROOM indicator` | `1` | `2` | `1` | Empty | `0` | `0` | `DND/MUR indicator NO RFID Axolute` |
| `2001` | `LN4650` | `DO NOT DISTURB-MAKE UP ROOM indicator` | `1` | `4` | `1` | Empty | `0` | `0` | `DND/MUR indicator NO RFID Living` |
| `2002` | `067590` | `DO NOT DISTURB-MAKE UP ROOM indicator` | `2` | `13` | `1` | Empty | `0` | `0` | `DND/MUR indicator NO RFID Celiane` |

Empty catalogue values are retained as empty metadata; none is an installed-state or market-availability observation.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MM00774_b_EN.pdf` | English technical sheet | `MM00774-b-EN`, `15/01/2015` | All three identities; specifications/legend printed p. 1 / PDF p. 1; physical/software configuration printed p. 2 / PDF p. 2; hotel-room system example printed p. 3 / PDF p. 3 | [Archived original](https://archive.openwebnet-ha.org/sha256/8e/26/8e26a521c7eb27d3d4dfce71fceaeb87badeeda3110a8331ca6c4d08e83d5ec4.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MM00774_b_EN.pdf) |
| `MM00774-b-FR.pdf` | French technical sheet | `MM00774-b-FR`, `15/01/2015` | All three identities; specifications/legend printed p. 1 / PDF p. 1; physical/software configuration printed p. 2 / PDF p. 2; hotel-room system example printed p. 3 / PDF p. 3 | [Archived original](https://archive.openwebnet-ha.org/sha256/ad/da/adda1e950ff03d6c5b44197ca5082dbc7b86e606fa624b707450a33e6d3ee45b.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MM00774-b-FR.pdf) |
| `LE06116AC.pdf` | Multilingual label installation / reader declarations | `LE06116AC-02PC-19W15` | Indicator identities plus separate reader H4651/LN4651/067591; shared label installation; RF statements scoped to reader; no printed pagination / PDF p. 1 | [Archived original](https://archive.openwebnet-ha.org/sha256/19/00/1900dc5ccac4aff7c789eb73808d36b7bae7ad046bf9bc34bd0d7e574e1ea41e.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/LE06116AC.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1680`; complete commercial, firmware, Module/Object and configuration records | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| `H4650-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `H4650` to EAN-13 relationship at printed/PDF p. 1. Exact identifier, product description and technical attributes examined during semantic review; prices are not adopted as durable technical facts. | [Archived original](https://archive.openwebnet-ha.org/sha256/93/c5/93c59840ea69129a1dc5c4a6a7fd30456ec4dd7627d59fb6d04c4163c741dfa4.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4650) |
| `LN4650-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `LN4650` to EAN-13 relationship at printed/PDF p. 1. Exact identifier, product description and technical attributes examined during semantic review; prices are not adopted as durable technical facts. | [Archived original](https://archive.openwebnet-ha.org/sha256/66/bb/66bba020f08ee8c006b13559e8b03f5473ddac5e4dc7d7622affee826032862c.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4650) |
| `H4650-publisher-product-sheet.pdf` | Exact manufacturer product export | DATASHEET; 06.10.2026 | Exact H4650 or LN4650; description/contact/bus attributes pp. 1-2; complete download list examined. Printed/PDF pages coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/e8/f0/e8f0a14245222ce05aad03c488ad7b88a1632c149f5552c985c43eb2128318f9.pdf) | [Publisher source](https://www.bticino.com/products/pdf?sku=BT-H4650&include_technical=1) |
| `LN4650-publisher-product-sheet.pdf` | Exact manufacturer product export | DATASHEET; 06.10.2026 | Exact H4650 or LN4650; description/contact/bus attributes pp. 1-2; complete download list examined. Printed/PDF pages coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/49/f6/49f6dfd24dfc1eba6777bc4812f414dc13c9f4bb5c213bb5ffb4d8452f70bbda.pdf) | [Publisher source](https://www.bticino.com/products/pdf?sku=BT-LN4650&include_technical=1) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | Two flush-mounted wiring-device modules | `MM00774-b-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| SCS BUS supply | `18..27 Vdc` | `MM00774-b-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Rear interfaces | SCS BUS terminals and physical configurator socket | `MM00774-b-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Standby / maximum current | `10 mA` standby; `20 mA` maximum | `MM00774-b-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Operating temperature | `5..40 °C` | `MM00774-b-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| DND indication | Red LED on: Do Not Disturb; active DND disables the call pushbutton | `MM00774-b-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| MUR indication | Green LED on: Make Up Room | `MM00774-b-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Room-number area | Customizable label with white backlight for room presence and applicable alarm notification | `MM00774-b-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Local output | Normally open contact operated by front call key; bell active while key is held | `MM00774-b-EN` / French counterpart, printed p. 1 / PDF p. 1; `MM00774-b-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| Published contact rating | `12 Vac/dc..230 Vac`, maximum `1 A` | `MM00774-b-EN` / French counterpart, printed p. 1 / PDF p. 1; bell diagram `MM00774-b-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| Terminal naming discrepancy | Rear legend shows `L`, `L1`; bell schematic shows `L1`, `L2`; use exact product markings when wiring | `MM00774-b-EN` / French counterpart, printed p. 1 / PDF p. 1; `MM00774-b-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| Physical configurator positions | `R1`, `R2`, `M`, `L` | `MM00774-b-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| Visual alarm applicability | MH201 plus MyHOME Suite programming; lot `14w40` or later (2014 week 40) | `MM00774-b-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Published standards | `EN 60669-2-1`, `EN 50491-5-1`, `EN 50428` | `MM00774-b-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Exact dimensions / IP / storage / MCU | Not established by the retained indicator-specific sheets | Two-module mounting size does not establish metric dimensions; no hardware fingerprint |
| H4650/LN4650 export contact limit | One contact; `1 A`, `12..230 V`, maximum `230 W` | Original H/LN product exports p. 2; power figure is SKU-scoped, not a new Céliane rating |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1680` | Canonical catalogue |
| Technical item description | DO NOT DISTURB-MAKE UP ROOM indicator | Canonical catalogue |
| Item family | Access control device (`101`) | Catalogue family association |
| Main system | Access control; system key `8` | `AS_ITEM_SYSTEM.main` association; not a functional WHO number |
| Item model / `modobj` | `8` | Main item/system mapping |
| Brand / line keys | BTicino brand key `1`, Axolute line key `2`, LivingLight line key `4`; Legrand brand key `2`, Céliane line key `13` | Commercial database keys; different from software parameter model namespaces |
| Commercial records | `3`; record IDs `1736`, `2001`, `2002` | Three shared-item catalogue variants |
| Gateway metadata | None of the three records is marked as a gateway | Commercial metadata; an MH201 software route is an external system connection |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Access control | `8` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `255` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Hardware revision, microcontroller and installed firmware are unknown. The indicator lot boundary `14w40` is a published production-lot limit, not a firmware version, and cannot be recovered from the wildcard tuple.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `255` | `1` | `488` Hotel indicator | Fixed/designated metadata | `1346` | `554` | `704` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `255` | Physical configuration | `0` | Canonical firmware/mode association ; association mode key `3` |
| `255` | Virtual Configuration | `1` | Canonical firmware/mode association ; association mode key `1` |
| `255` | Advanced Configuration | `2` | Canonical firmware/mode association ; association mode key `2` |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

Both technical sheets document physical configurators and MyHOME Suite software configuration. The software route uses the PC Ethernet network and external MH201 scenario module; the control/indicator itself remains on SCS BUS. No connection association is stored for this firmware in `AS_CONNECTION_FIRMWARE`; this absence does not invalidate the published Ethernet route. No Product Programming mode association is stored for this firmware.

## Firmware-scoped configuration

Domains and defaults below are catalogue evidence. `AID` is an eight-character mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `255` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `255` | `R1` | `0..9` | `0` | Room tens |
| `255` | `R2` | `0..9` | `0` | Room unit |
| `255` | `M` | `0..2` | `0` | DND/MUR indicator mode; Stand alone with SCE - Value : 0 Stand alone with `CEN` - Value : 1 With IP Scenario Module - Value : 2 |
| `255` | `L` | `0..7` | `0` | led function; 0 : Presence `ON=occupied`, Presence `OFF=free`; DND Active; MUR Active 1 : Presence `ON=occupied`, Presence `OFF=free`; DND Active; MUR Hidden 2 : Presence `ON=free`, Presence `OFF=occupied`; DND Active; MUR Active 3 : Presence `ON=free`, Presence `OFF=occupied`; DND Active; MUR Hidden 4 : Presence always `ON`; DND Active; MUR Active 5 : Presence always `ON`; DND Active; MUR Hidden 6 : Presence always `OFF`; DND Active; MUR Active 7 : Presence always `OFF`; DND Active; MUR Hidden |

### Published physical mode mapping

| Configurator | Value / meaning | Evidence |
| --- | --- | --- |
| `R1`, `R2` | Room address tens and units; each `0..9` in catalogue | Catalogue; `MM00774-b-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| `M=0` | With F420 | `MM00774-b-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| `M=1` | With MH200N | `MM00774-b-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| `M=2` | With MH201 | `MM00774-b-EN` / French counterpart, printed p. 2 / PDF p. 2 |

### Physical `L` configurator

| `L` | White room backlight | Red DND LED | Green MUR LED |
| --- | --- | --- | --- |
| `0` | On when occupied; off when free | Enabled | Enabled |
| `1` | On when occupied; off when free | Enabled | Disabled |
| `2` | On when free; off when occupied | Enabled | Enabled |
| `3` | On when free; off when occupied | Enabled | Disabled |
| `4` | Always on | Enabled | Enabled |
| `5` | Always on | Enabled | Disabled |
| `6` | Always off | Enabled | Enabled |
| `7` | Always off | Enabled | Disabled |

Both technical sheets print this mapping on p. 2 / PDF p. 2; it agrees with firmware `L` descriptions. Software Object `DND_ENABLE` separately permits disabling DND; that value is not a ninth physical L choice.

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
| `APL` | `0..175` | `0` | Address of the Key card switch; Complete stored mapping: `A=floor(value/16)`, `PL=value mod 16`; labels include `A=0..10` and `PL=0..15`, not a decimal physical A/PL configurator domain. |
| `LOCAL_RELAY_FUNCTION` | `0` = Doorbell; `1` = Door opening | `0` | Local relay function; In case of Doorbell, parameter "Door relay address" must be different from 0. |
| `APL_DOOR` | `0..175` | `1` | Address of the actuator of door relay; Complete stored mapping: `A=floor(value/16)`, `PL=value mod 16`; labels include `A=0..10` and `PL=0..15`, not a decimal physical A/PL configurator domain. |
| `DOOR_RELAY_TIMER` | `1..100` | `10` | Door relay timing [s]; Complete stored label mapping: time in seconds equals value / 10 (`0.1..10 s`); stored default `10` = `1 s`. This catalogue mapping does not by itself establish a protocol wire representation. |
| `BACKLIGHT_INTENSITY` | `1` = Level 1; `2` = Level 2; `3` = Level 3; `4` = Level 4; `5` = Level 5; `6` = Level 6; `7` = Level 7; `8` = Level 8; `9` = Level 9; `10` = Level 10 | `5` | Backlight intensity |
| `ROOM_GENERIC_SERVICE` | `0` = Enabled; `1` = Disabled | `1` | Room_Generic_Service; link to PUL_Signal Frame |

`ENTRANCE_ENABLE_GROUP` is described as applicable only in `MODE=0`; the catalogue does not attach an equivalent condition row. The generic MODE description about local/IP badge storage is explicitly for indicators with RFID and does not establish an RFID reader in these three NO-RFID variants. The `ROOM_GENERIC_SERVICE` description names `PUL_Signal` without defining the frame or its Device-specific behavior.

### Semantic review findings

The product is explicitly non-RFID. Object `488` generic reader/group/door fields are software metadata, not evidence of indicator radio hardware. Preserve the literal room default 01 and filter admitting only 0; the nonzero doorbell-address requirement is prose, not enforced by a stored condition. New H/LN exports corroborate one contact and add a SKU-scoped 230 W maximum.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `255` | `488` | `1378` | `LOCAL_RELAY_FUNCTION` | `0` = Doorbell; `1` = Door opening (entire reusable range retained) | `0` | Local relay function |
| `255` | `488` | `1380` | `DOOR_RELAY_TIMER` | `1..100` (entire reusable range retained; value / 10 seconds) | `10` | Door relay timer, step 100ms |
| `255` | `488` | `1792` | `APL_DOOR` | `0..175` (entire reusable range retained; `A=floor(value/16)`, `PL=value mod 16`) | `1` | Address of the actuator of door relay |
| `255` | `488` | `3096` | `ROOM_GENERIC_SERVICE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Room_Generic_Service |
| `255` | `488` | `3106` | `R1R2` | `0` | `01` | Room address; reusable default `01` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion rule or selection predicate is associated with these placements. Validate the firmware domain and the selected Object/Firmware filters separately; empty selection metadata does not establish an active Object. Generic resolution remains in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Compare discovered model and system with catalogue main model `8` in Access control; this is a source-derived identification target, not a verified response | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Corroborate installed firmware before relating observations to wildcard catalogue applicability; also retain physical lot label for the visual-alarm boundary | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Corroborate hardware revision separately from firmware; no verified response retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Corroborate microcontroller revision if this managed Device supports the query; no verified response retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Discover active Objects and Modules: slot `1`, external Object `488`; no Virgin Object association. Do not report database relation IDs as KEYO | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Read applicable active Object addressing; room-address semantics belong to Access Control, not Lighting A/PL; device address encoding requires actual discovery context | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Read/compare the selected Object configuration against its reusable domain/default and firmware context; default is not installed state | [Configuration](../../diagnostics/dim35-configuration.md) |

These are candidate corroboration surfaces of the managed Device model. Catalogue associations do not prove that every operation succeeds on this firmware/transport. Access Control management uses `WHO 1023`; catalogue system key `8` is not `WHO 8`.

## Functional applicability

The main catalogue family is [Access Control (`WHO 23`)](../../functional/who-23-access-control/). That implementation family has managed addressing infrastructure; its numeric catalogue system key and item model are separate namespaces. No complete DND/MUR functional WHAT or DIMENSION vocabulary is established by the retained product sheets.

| Function | Published or implementation applicability | Evidence |
| --- | --- | --- |
| DND / MUR display | Red DND and green MUR indicators; DND disables the front bell key | Both technical sheets p. 1 / PDF p. 1 |
| Presence indication | White room-number backlight; physical L selects presence/inverted/always-on/always-off modes | Both technical sheets p. 2 / PDF p. 2 |
| Local bell | Normally open contact active while front key is held, within published load rating | Both technical sheets pp. 1-2 / PDF pp. 1-2 |
| Visual alarm | MH201 system, MyHOME Suite configuration and production lot 14w40 or later | Both technical sheets p. 1 / PDF p. 1; blinking pattern/event list unspecified |
| Software door / service options | Reusable Object `488` includes local door opening, address/time, entrance/leaving groups and room service | Catalogue capability; exact non-RFID runtime mapping not corroborated |

## Observed behavior and corroboration

No sanitized hardware fingerprint, protocol capture or commissioning experiment is retained for this exact technical item. Source diagrams, room number `127`, switch states and example addresses are publisher illustrations, not observed project installations.

## Programming

MyHOME Suite software configuration uses PC Ethernet through MH201 to the SCS system; it offers more options than physical configuration. The technical sheets do not define a complete transfer wizard, erase scope, firmware-update package or recovery procedure. Validate the active Object and its complete configuration before applying changes; absence of slot predicates does not supply a selection algorithm.

Set R1/R2 for the bus room address, M for the installed scenario module and L for white/MUR indications. Confirm the physical lot is `14w40` or later before enabling the MH201-only visual alarm in software. The alarm trigger set, flash pattern and reset procedure are not specified by these sheets. Bell wiring must follow the exact terminal markings and published contact rating.

Both sheet examples show room label `127`, bus address `R1=2`, `R2=7`, `M=2`, `L=0`; labels and bus addresses are different scopes. The p. 3 / PDF p. 3 multi-device diagram additionally prints `A=1`, `PL=1`, `T=2` beside this indicator, although the dedicated physical configurator inventory and firmware fields do not define those positions. Preserve this diagram discrepancy; it does not establish additional firmware fields.

`LE06116AC-02PC-19W15`, PDF p. 1, illustrates removal of the front/label, printing and cutting a room-number insert, then reinsertion and refitting. Its `13.56 MHz` and RED declarations explicitly name H4651/LN4651/067591 readers; neither establishes a radio in H4650/LN4650/067590.

## Source reconciliation

The English and French technical sheets have the same `b`, `15/01/2015` revision and agree on the Device-specific specifications, modes, procedures and scope described above. Their three-reference headers independently support the catalogue cluster. General vendor/contact text and certification marks remain in the originals; listed standards are publisher declarations, not a new certification audit. Physical wiring-device module count is independent of protocol Module count. Catalogue status/default metadata and published operating descriptions are not observations of installed firmware or behavior.

| Source issue | Reconciliation / unresolved limit | Evidence |
| --- | --- | --- |
| Room-address default | Firmware R1 and R2 defaults each `0`; reusable Object R1R2 default is literal `01`. Filter `3106` restricts R1R2 to `0`, outside reusable default `01`, while physical addresses have two decimal digits. This unresolved software restriction is preserved; no replacement default or generic runtime-address ban inferred | Firmware `255`; Object `488` |
| Relay requirement | Reusable LOCAL_RELAY_FUNCTION default Doorbell (`0`) accompanies APL_DOOR default `1`; the description requires nonzero Door relay address in Doorbell mode. The legal address domain also contains `0`, without an attached condition/filter enforcing the requirement | Object `488`; relay-function/address filters retain full ranges, without a conditional nonzero rule |
| Physical and reusable LEDs | Physical L always enables red DND; software DND_ENABLE can disable it; white-presence labels and software levels are separate fields, without a conversion table | Both sheets p. 2; Object `488` |
| Indicator and reader scope | Shared instruction RF/declaration text is expressly for the 4651/067591 reader family; catalogue names this 4650/067590 cluster NO RFID | LE06116AC p. 1; commercial catalogue |
| Extra diagram fields | Hotel diagram prints A/PL/T beside the indicator although physical configuration lists R1/R2/M/L only and the firmware has no A/PL/T fields | Both sheets pp. 2-3; firmware `255` |
| Bell terminal naming | Rear legend labels L/L1; bell wiring sketch labels L1/L2. No unwitnessed terminal equivalence established | Both sheets pp. 1-2 |
| Hardware boundary | Visual alarm requires lot 14w40 or later plus MH201/software; wildcard firmware cannot establish this production-lot capability | Both sheets p. 1; firmware `255` |
| Software RFID prose | Generic MODE field describes badge storage for RFID variants; address/group/door fields remain reusable software capability with unverified non-RFID runtime scope | Object `488` |

The illustrated instruction revision `LE06116AC-02PC-19W15` has been incorporated for label handling. Multilingual reader regulatory statements add no indicator-specific radio capability; their applicability remains explicitly separate.

The `06.10.2026` H4650/LN4650 originals corroborate one contact and `230 W` maximum, two wiring-device modules, LED, local control and SCS bus. They classify RF/KNX/LON/Powernet as No and connected-object as No; these are commercial classifications. “Different phases connectable” is not an installation instruction or permission to exceed the technical-sheet contact rating. Their LE06116AC/MM00774_b_EN links reuse retained originals. The H4650 broad catalogue `3211578` and linked drawing files remain unexamined; the known Italian MM00774_b_IT translation is not independently reconciled. No metric dimensions or IP rating appears in these two exports.

## Evidence limits and open work

- Resolve the firmware `00` versus reusable Object `01` room default and filter `3106` restriction to 0, unenforced nonzero relay-address requirement, extra A/PL/T diagram positions and L/L1 versus L1/L2 terminal notation.
- Obtain lot-scoped hardware evidence for the MH201 visual-alarm feature, including trigger events, indication pattern, reset/acknowledgement and accepted configuration fields.
- Verify non-RFID applicability of reusable door opening, door timer, entrance/leaving group and generic-service fields; inspect the relevant software definitions before asserting wire encoding.
- Corroborate Object `488`, room address, bell interlock/contact behavior and LED mapping for all three variants; exact metric dimensions, IP and MCU remain undocumented by retained indicator sheets.
- Retained exact-product source reconciliation is scoped to the listed revisions; current commercial catalogues/translations and future revisions can extend it.

## Sources

Catalogue tables were read from the registered `MHCatalogue.db` original, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. `EN_ITEM`, `EN_DEVICE`, firmware/system associations, `EN_SLOTS`, Object/Virgin relationships, `EN_CONF`/`EN_CONF_RANGE`, slot conditions, filters, conversions and configuration-mode associations define the implementation scope. Exact archived PDF revisions and publisher URLs are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue metadata and retained fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- `H4650-ean-product-sheet.pdf`, printed/PDF p. 1: exact `H4650` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/93/c5/93c59840ea69129a1dc5c4a6a7fd30456ec4dd7627d59fb6d04c4163c741dfa4.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4650); SHA-256 `93c59840ea69129a1dc5c4a6a7fd30456ec4dd7627d59fb6d04c4163c741dfa4`.
- `LN4650-ean-product-sheet.pdf`, printed/PDF p. 1: exact `LN4650` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/66/bb/66bba020f08ee8c006b13559e8b03f5473ddac5e4dc7d7622affee826032862c.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4650); SHA-256 `66bba020f08ee8c006b13559e8b03f5473ddac5e4dc7d7622affee826032862c`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0101-0110-2026-10-06.md#own-dev-0105)
