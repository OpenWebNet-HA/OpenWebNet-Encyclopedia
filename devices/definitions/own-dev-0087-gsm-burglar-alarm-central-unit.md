# GSM burglar alarm central unit

## Summary

The 3486 is a burglar-alarm central unit with both GSM and PSTN communication. Its manual documents eight sensor zones, 16 partition scenarios, event-driven automations and telephone status/control, with separate channel priorities and Ademco Contact ID reporting.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0087` | Project identity |
| Technical description | GSM burglar alarm central unit | Canonical catalogue |
| Commercial identities | `3486` | Canonical commercial records |
| Catalogue item | `141` | Canonical catalogue |
| Main catalogue system | Burglar alarm system | Canonical catalogue |
| Item model / `modobj` | `197` | Canonical inventory |
| Firmware definition | `8.0.0`; `6.0.0`; `7.0.0` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Burglar alarm system, Burglar alarm | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Pivot | `3486` | Established catalogue identity | canonical commercial record for item `141` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| BTicino/Legrand residential catalogue | product catalogue | historical publisher catalogue | 3486 roles/capacity/programming: printed pp. 147, 187-190 / PDF pp. 149, 189-192; battery printed p. 195 / PDF p. 197 | [Archived original](https://archive.openwebnet-ha.org/sha256/9f/e5/9fe511c3ac12d861dff7d8d28ddec3b3612a27e99a804afbed89877c73a6b4ed.pdf) | [Official source](https://assets.legrand.com/webf/ch/ch_de_katalog_wohnbau.pdf) |
| `U2073I_I_EN.pdf` | 3486 installation manual | `U2073I`, 10/15-01-PC | Complete substantive chapters PDF/printed pp. 6–97: physical interfaces, installation/learning, keys/scenarios, local/PC programming, telephone menus and commands, appendix/recovery; unrelated cover/back matter excluded | [Archived original](https://archive.openwebnet-ha.org/sha256/0e/2b/0e2bdbb00e33d8cb7fac01d6d22188333660136141b05e11b74bbfa0ab8b9877.pdf) | [Publisher source](https://dar.bticino.it/asset/Documents/U2073I_I_EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply / current | `18..28` V; `50 mA` standby, `120 mA` maximum | `U2073I`, printed/PDF p. 96 |
| Temperature / dimensions / protection | `5..40 °C`; `140 × 210 × 35 mm` (L/H/P); IP30 | Same technical appendix |
| Backup battery | 3507/6; 6 V in Swiss compatibility table | `U2073I` p. 15; Swiss printed p. 195 / PDF p. 197; not the 3485 7.2 V battery |
| Local interfaces | Display, navigation/alphanumeric keypad, microphone, speaker, transponder and IR receivers | `U2073I` p. 6 |
| Rear interfaces | PSTN IN/OUT, GSM SIM/antenna, SCS, six-pin serial, RESET, slide, local tamper and sound connection | `U2073I` p. 14 |
| Antenna revision discrepancy | Overview says 3 m cable; installation says supplied 1.5 m with 3483 extension 3.5 m | `U2073I` pp. 6, 15; lengths not silently reconciled |
| Mounting / SIM supply | Wall bracket; GSM carrier SIM required and not supplied | Swiss guide printed p. 190 / PDF p. 192; U2073I installation pp. 15–17, 26 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `141` | Canonical catalogue |
| Technical item | GSM burglar alarm central unit | Canonical catalogue |
| Main system | Burglar alarm system | Canonical catalogue |
| Item model / `modobj` | `197` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Burglar alarm system | `197` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Burglar alarm | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `141` | `3486` | `1` | `9` | `BTicino_Pivot_GSM burglar alarm central unit` |

| Record | Visible | Dependent | Gateway flag | Visibility type |
| --- | --- | --- | --- | --- |
| `141` | `1` | `0` | `0` | Empty in source |

These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `8` | `0` | `0` | `1` | Catalogue default | Official |
| `20` | `6` | `0` | `0` | `1` | Not catalogue default | Official |
| `21` | `7` | `0` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `19` | `60` | BTicino (key `1`) | `6` | external software | `TiSecurityGSM_0300` |
| `20` | `104` | BTicino (key `1`) | `6` | external software | `TiSecurityGSM_0100` |
| `21` | `103` | BTicino (key `1`) | `6` | external software | `TiSecurityGSM_0200` |

All 3 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `1` | `14` AI Control Unit With Communicator Gsm | Fixed/designated metadata | `2276` | `14` | `954` |
| `20` | `1` | `14` AI Control Unit With Communicator Gsm | Fixed/designated metadata | `2278` | `14` | `956` |
| `21` | `1` | `14` AI Control Unit With Communicator Gsm | Fixed/designated metadata | `2277` | `14` | `955` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `19` | Product Programming | `3` | Canonical firmware/mode association |
| `20` | Product Programming | `3` | Canonical firmware/mode association |
| `21` | Product Programming | `3` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `19` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `20` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `21` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `14` - AI Control Unit With Communicator Gsm

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `NUM_PSTN` | No legal values specified in source | Not specified in source | Telephone number PSTN |
| `NUM_GSM` | No legal values specified in source | Not specified in source | Telephone number GSM |
| `FW_VER` | No legal values specified in source | Not specified in source | Firmware version |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |

### Device-specific interpretation

Official firmware `19`=8.0.0 (default), `20`=6.0.0 and `21`=7.0.0 each has one Module with GSM Object `14`. AID is the only firmware-scoped field. `FW_VER` and NUM_PSTN have no reusable domain/default; `IS_GATEWAY` boolean default `0` does not negate the manufacturer’s telephone integration functions. There are no Virgin/condition/filter/conversion rows. Product Programming `3` applies to all three; parameter records `60/104/103` have brand `1`, line `6`, separately from commercial line `9`. No connection or package rows establish a LAN transport. The 2015 installation manual is product/revision evidence, not proof of any of those firmware tuples being installed.

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
| `DIMENSION 1` | corroborate technical identity for catalogue item `141` / `modobj = 197` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`14`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `14` AI Control Unit With Communicator Gsm | Burglar alarm system | Firmware/Object capability association; resolve the slot and configuration first |
| `14` AI Control Unit With Communicator Gsm | Video door entry system | Firmware/Object capability association; resolve the slot and configuration first |

These are catalogue Object/system associations, not `WHO` numbers, physical connector claims or observed command acceptance. Resolve the active Module/Object and its restrictions before using the [Functional Protocol](../../functional/).

### Published product functions

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Zones / scenarios | Zone 0: up to 9 arming interfaces; `1..8` sensor zones; zone 9 technical/auxiliary; 16 partition scenarios, initially enabled | `U2073I` pp. 11, 29, 50 |
| Sensors / keys | Independent sensor deactivation and delays; keypad, IR/transponder and supported radio control; key limitations by days/time/zones; 348220 radio requires L/N/NT/HC/HS4618 receiver | `U2073I` pp. 30–39, 52, 80–86 |
| Access / events | Three incorrect credentials block local access for 1 min; last 200 events; only installer can erase; user/installer privileges separate | `U2073I` pp. 11, 47–48, 53 |
| Automations / commands | 20 event-to-action entries; alarms, technical, faults, arming/disarming, time and point lighting/automation Open events. Sending lighting/automation commands requires F422 interface | `U2073I` pp. 55–58 |
| Alarm/delay settings | Alarm and tamper duration from brief to 10 min; entry/exit 0 s..3 min; source basic settings: 3 min alarm/tamper, 0 s delays | `U2073I` pp. 59, 77 |
| Calling model | Jolly plus 10 numbers; up to 4 indexed recipients per event; up to 4 cycles; call delay `0..60` s; supply-loss delay 10 min..10 h | `U2073I` pp. 62–67, 71–72 |
| Call routing / answer | GSM/PSTN priority then fallback; calls ON/OFF or channel-specific OFF; PSTN answer OFF..8 rings, GSM one ring, answer OFF blocks both | `U2073I` pp. 71–73 |
| Published telephone defaults | Calls ON, PSTN 5 rings, 4 cycles, delay 10 s, DTMF, supply loss 1 h, GSM priority; remote assistance/control and answering-machine support OFF; call wait 0 | `U2073I` p. 77; source defaults, not observed settings |
| Remote telephone services | 9 stored simplified commands, first 4 personalized voice responses; information 922 status, 921 speech, 920 listen up to 1 min; full codes separately documented | `U2073I` pp. 79, 90–93 |
| Contact ID / historical portal | Four reporting levels; optional alarm-end reporting; auxiliary channels 1 gas, 2 freezer, 3 flooding, 4 anti-panic, 5–7 general, 8 fire, 9 assistance. Remote assistance requires System Test | `U2073I` pp. 70, 72, 74–77, 94 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

`U2073I` documents installation and first learning (pp. 14–24), SIM PIN/insertion with supply and battery disconnected (pp. 25–26), testing (27–28), scenarios and key enrollment/limitations (29–39), and local customization (40–42). It requires the panel before other PSTN equipment and illustrates PLT1 line protection/earthing (p. 18); consult that exact installation drawing for the complete wiring.

TiSecurityGSM uses serial 335919 or USB 3559 at the six-pin connector in Maintenance (pp. 43–46). Firmware transfer requires rear slide OFF. Project configuration can be received, edited, sent or saved, with software compatibility comparison; each changed PC configuration requires learning in Update mode and confirmation of forwarding. Voice messages have separate send/receive/record/WAV operations. The separate TiSecurityGSM software manual/payload was referenced but not examined.

Installer menus require a disarmed system; Maintenance code does not arm/disarm, and changing it precedes changing User code (pp. 47–48, 60–61). System Test does not raise ordinary alarms and permits remote assistance. Maintenance requires explicit CLEAR exit. Recovery through OFF/RESET enters Maintenance; the voice-message recovery procedure cancels date/time (p. 97), not a documented factory erase.

Telephone Open codes and simplified 99 forms are manufacturer-documented product contexts (pp. 55, 79, 90–93), not proof of a generic TCP gateway. Incoming remote alarm control requires Telecontrol AI ON or USER. Simplified type 0 forces OFF/DOWN for lights/shutters, but temperature/alarm uses the stored command as type 1 does (p. 91).

## Source reconciliation

The exact 3486 installation manual revision 10/15-01-PC directly supports the physical, menu and GSM/PSTN claims. The Swiss guide independently supports GSM/PSTN integration, eight sensor zones/72-detector selection and 6 V 3507/6 compatibility; the 72-detector limit belongs to that guide rather than an `EN_ITEM` field. The manual has contradictions: antenna cable is 3 m in overview versus 1.5 m in installation; line-test introductory intervals omit 120/336 h included by the illustrated selector (p. 63); the appendix selection text says only DTMF while p. 71 explicitly offers PSTN DTMF/Pulse. Keep these with source scope. The manual’s revision and UI example firmware displays do not identify applicability to each historical catalogue tuple. Historical MyHOME portal, GSM carrier and SSL/service availability are not claimed current. Its published Open-SCS WHO list 0/1/2/5/9 (p. 96) is exact-manual scope, not a universal command inventory.

Catalogue interpretation is detailed under [Object configuration surfaces](#object-configuration-surfaces); the complete firmware, topology and restriction tables remain authoritative for software applicability.

The Swiss shared section printed p. 147 / PDF p. 149 mentions battery `3506` before listing `3485STD` and `3486`; the exact `3486` row printed p. 190 / PDF p. 192 and U2073I p. 15 instead identify `3507/6`. This shared wording does not justify assigning the `3485` battery to `3486`.

## Evidence limits and open work

- Resolve antenna length, line-test interval and DTMF-only appendix conflicts with an applicable revision.
- Examine the linked TiSecurityGSM software/manual and firmware/parameter payloads before claiming their detailed fields or version changes.
- Corroborate current channel/service availability and installed firmware; no hardware observations are retained.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0081-0090-2026-10-06.md#own-dev-0087)
