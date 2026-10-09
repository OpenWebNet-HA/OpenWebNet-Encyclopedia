# Shutter flush mounted actuator

## Summary

H4671/2 / L4671/2 is a flush-mounted shutter actuator with two interlocked motor relays and local up/down controls. The catalogue also maps AM5851/2 to this item; the retained H/L guide establishes timed and slave operation, while the AM variant’s hardware details remain unverified.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0098` | Project identity |
| Technical description | Shutter flush mounted actuator | Canonical catalogue |
| Commercial identities | `H4671/2`, `L4671/2`, `AM5851/2` | Canonical commercial records |
| Catalogue item | `1122` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `102` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `2` | Canonical firmware catalogue |
| Categories | Automation, Actuator, Shutter control | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4671/2` | Established catalogue identity | canonical commercial record for item `1122` |
| BTicino | `L4671/2` | Established catalogue identity | canonical commercial record for item `1122` |
| BTicino - Matix | `AM5851/2` | Established catalogue identity | canonical commercial record for item `1122` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| `AUTOMATISME.pdf` | MyHOME automation guide | historical publisher guide | H/L4671/2 configuration: printed p. 113 / PDF p. 115; motor load table printed p. 159 / PDF p. 161; consumption/dissipation printed p. 160 / PDF p. 162; only cited applicable leaves examined; unrelated guide pages and linked dedicated documents unexamined | [Archived PDF](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Construction / power | Two wiring modules; two interlocked motor relays; `27 Vdc`, `13.5 mA`; dissipation `0.9 W` | AUTOMATISME printed p. 113/PDF p. 115; ratings printed p. 160/PDF p. 162; H/L only |
| Motor load | `2 A` / `500 W` at `50/60 Hz`; source row does not specify a voltage for this rating | AUTOMATISME printed p. 159/PDF p. 161 |
| Controls / sockets | Local up/down controls and LED; rear A/PL/M/G configurator positions | AUTOMATISME printed p. 113/PDF p. 115; AM construction not established |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1122` | Canonical catalogue |
| Technical item | Shutter flush mounted actuator | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `102` | Canonical inventory |
| Commercial records | `3` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `102` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `7` | `H4671/2` | `1` | `2` | Empty in source |
| `1122` | `L4671/2` | `1` | `4` | Empty in source |
| `1635` | `AM5851/2` | `1` | `3` | `BTicino_Matix_Shutter flush mounted actuator` |

| Record | Visible | Dependent | Gateway flag | Visibility type |
| --- | --- | --- | --- | --- |
| `7` | `1` | `0` | `0` | Empty in source |
| `1122` | `1` | `0` | `0` | Empty in source |
| `1635` | `1` | `0` | `0` | Empty in source |

These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `188` | `-1` | `-1` | `-1` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `188` | `1` | `7` Automation actuator | Fixed/designated metadata | `643` | `7` | `447` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `188` | Physical configuration | `0` | Canonical firmware/mode association |
| `188` | Virtual Configuration | `1` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `188` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `188` | `A` | `0..9` | `0` | A; Environment |
| `188` | `PL` | `0..9` | `0` | PL; Light Point |
| `188` | `M` | `0..4`; `15` = `PUL` | `0` | M; Mode (0-4, Pul) |
| `188` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

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

### Device-specific interpretation

Official/default wildcard firmware `188` declares two Modules but only slot `1` with Object `7` is stored; no slot-2 mapping or Virgin exists. This is a catalogue topology gap, not proof of two independent physical loads or permission to invent a second Object. Firmware M permits `0..4` and 15 PUL. Rule `2` also stores numeric `5..9` and symbolic I/O, PUL and SLA branches; the extra numeric values and I/O/SLA lie outside the firmware domain. Stored STOP_TIME codes retain 60/62/65/70/0 and shorter branches; symbolic conversion outputs I/`O=13`, `PUL=15`, `SLA=11` do not establish extra firmware legal inputs. Reusable STOP_TIME lacks values 18 and 61; no replacements are supplied. Ten reusable group fields and broad gate/garage SUBTYPE labels do not prove ten physical sockets or distinct gate hardware. The exact H/L source documents one G socket and physical SLA operation, which remains a source/catalogue discrepancy. AM5851/2 has an established canonical identity but no retained exact-variant hardware sheet.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `188` | `1` | `7` | `4148` | No textual predicate stored | `2` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | - | None | - | No relation-specific filters associated | - | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `2` | `M=0` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `60` | `2` |
| `2` | `M=1` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `62` | `2` |
| `2` | `M=2` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `65` | `2` |
| `2` | `M=3` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `70` | `2` |
| `2` | `M=4` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `0` | `2` |
| `2` | `M=5` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `20` | `2` |
| `2` | `M=6` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `10` | `2` |
| `2` | `M=7` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `5` | `2` |
| `2` | `M=8` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `15` | `2` |
| `2` | `M=9` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `30` | `2` |
| `2` | `M=I/O` | `LOCAL_BUTTON` = `13`; `M` = `0`; `STOP_TIME` = `60` | `2` |
| `2` | `M=PUL` | `LOCAL_BUTTON` = `12`; `M` = `15`; `STOP_TIME` = `60` | `2` |
| `2` | `M=SLA` | `LOCAL_BUTTON` = `12`; `M` = `11` | `2` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1122` / `modobj = 102` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`7`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `7` Automation actuator | Automation | Firmware/Object capability association; resolve the slot and configuration first |

Catalogue system identifiers are not `WHO` numbers. The source establishes the roles shown, not a complete command vocabulary or proof of every installed function. Correlate the selected role with [Functional Protocol](../../functional/) before sending functional commands. Product behavior is additionally bounded by the publisher evidence below; uncorroborated transport and firmware details remain open work.

### Manufacturer-documented functions

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Shutter operation | Interlocked directions; source physical M timing: 60 s, 2 min, 5 min, 10 min or infinite until next command | Same guide printed p. 113; physical settings separate from STOP_TIME enum |
| Slave scope | Physical SLA slave setting documented for H/L4671/2 | Same guide; source/canonical M discrepancy retained |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

AUTOMATISME, printed p. 113 / PDF p. 115, supplies local A/PL/M/G configuration and timed direction control. Physical timed settings cover unconfigured/`0..4` and the source separately documents SLA; canonical firmware `188` does not admit SLA, but records `PUL=15`. No source establishes an offset or precedence that resolves these scopes. Do not substitute two independently switched lighting loads for the interlocked shutter motor.

No retained exact AM5851/2 manual establishes its connector diagram or local commissioning. Neither the guide nor canonical association supplies a universal factory reset, software transfer or firmware-update procedure.

## Source reconciliation

Exact H/L pages establish motor load, power and local operation; they are not direct physical evidence for AM5851/2. The database declares two Modules while supplying only slot `1`, and that missing slot remains explicit. Physical two-relay construction does not fill this logical-data gap. Source SLA and software PUL domains remain separate.

The catalogue-domain and conversion discrepancies are explained under [Device-specific interpretation](#device-specific-interpretation), alongside the complete reusable fields.

## Evidence limits and open work

- Resolve the missing declared slot `2`, physical SLA/canonical M applicability and exact AM5851/2 construction from further evidence.
- No installed timing, reset or update behavior has been observed.
- Applicable exact-product guide leaves were inspected; unrelated guide pages and linked dedicated documents remain unexamined.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0091-0100-2026-10-06.md#own-dev-0098)
