# 3485STD burglar-alarm unit with local contacts

## Summary

3485STD is a burglar-alarm control unit with a PSTN telephone communicator and two local contact inputs. It supervises alarm zones, stores activation scenarios and events, and supports keypad or transponder operation, voice alarm calls and programmed responses by other MyHOME equipment.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0191` | Project identity |
| Technical description | 3485STD burglar-alarm unit with local contacts | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `3485STD` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1804` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Burglar alarm system | Main system association |
| Item model / `modobj` | `204` | Main association; independent of project ID |
| Firmware definition | `668` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Polyx | `3485STD` | Established catalogue identity | Manufacturer database commercial record `1931` explicitly links this SKU to item `1804` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `BQ01001-a-EN.pdf` | 3485STD technical sheet | `BQ01001-a-EN; 05/06/2014` | Printed/PDF pp. 1-3: zones, scenarios / keys, PSTN / local interfaces, current / temperature / dimensions, Contact ID events and wiring protection notes. | [Archived original](https://archive.openwebnet-ha.org/sha256/3f/f2/3ff2590acd901029aba31134d64f37c9c60eaf951a62fa3b7fa9d038e3902625.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/BQ01001-a-EN.pdf) |
| `RA00100AG_I_EN.pdf` | 3485STD installer manual | `RA00100AG_I_EN; cover 10/15-01 PC` | Printed/PDF pp. 3-4 contents; installation / startup, local contacts, alarm / telephone setup, maintenance and p. 90 technical/OPEN-SCS families; source-specific operating procedures. | [Archived original](https://archive.openwebnet-ha.org/sha256/cb/07/cb07372bda190848f48b90c7e55ad2f1d208e011daea23a408bffbe71780caa1.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00100AG_I_EN.pdf) |
| `RA00100AD_U_EN.pdf` | 3485STD user manual | `RA00100AD_U_EN; printed publication date not established` | Printed/PDF contents and user-operation sections: arming, partition / scenario selection, event review and telephone commands; not an electrical installation authority. | [Archived original](https://archive.openwebnet-ha.org/sha256/52/02/52025757b3d00de752207b712511e6ca8c5897c99f126b35e2b63a37de4634ef.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00100AD_U_EN.pdf) |
| `RA00100AB_S_EN.pdf` | TiSecurityStandard software manual | `RA00100AB_S_EN; cover 06/13-01-PC` | Printed/PDF software workflow and project sections: receive / edit / send, vocal messages, firmware update and alarm / telephone settings; payload encoding unexamined. | [Archived original](https://archive.openwebnet-ha.org/sha256/2a/73/2a735a9346f86d294db13ffa081ab8d19b05098c984feb953238183b86953494.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00100AB_S_EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1804`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Nominal SCS supply | `27 Vdc, technical sheet; 18..28 Vdc operating range in installer manual` | `BQ01001-a-EN.pdf` printed/PDF pp. 1-3; `RA00100AG_I_EN.pdf` printed/PDF p. 90 |
| Absorption | `55 mA standby / 90 mA maximum` | `BQ01001-a-EN.pdf` printed/PDF pp. 1-3; `RA00100AG_I_EN.pdf` printed/PDF p. 90 |
| Operating temperature | `5..40 °C` | `BQ01001-a-EN.pdf` printed/PDF pp. 1-3; `RA00100AG_I_EN.pdf` printed/PDF p. 90 |
| Dimensions, sheet / installer manual | `H128 × W125 × D25 mm / W125 × H128 × D31 mm` | `BQ01001-a-EN.pdf` printed/PDF pp. 1-3; `RA00100AG_I_EN.pdf` printed/PDF p. 90 |
| Mounting / protection | `Wall mounted; IP30 in installer manual` | `BQ01001-a-EN.pdf` printed/PDF pp. 1-3; `RA00100AG_I_EN.pdf` printed/PDF p. 90 |
| Local contacts | `Two separate rear contact lines; separate tamper terminals` | `BQ01001-a-EN.pdf` printed/PDF pp. 1-3; `RA00100AG_I_EN.pdf` printed/PDF p. 90 |
| User interface | `Graphic display; transponder reader; keypad; microphone; loudspeaker` | `BQ01001-a-EN.pdf` printed/PDF pp. 1-3; `RA00100AG_I_EN.pdf` printed/PDF p. 90 |
| Capacity | `16 activation scenarios; zones 0 activators, 1..8 sensors, 9 technical alarms; up to 50 keys` | `BQ01001-a-EN.pdf` printed/PDF pp. 1-3; `RA00100AG_I_EN.pdf` printed/PDF p. 90 |
| PSTN / external interfaces | `Telephone IN/OUT; serial PC connector; alarm BUS; Contact ID` | `BQ01001-a-EN.pdf` printed/PDF pp. 1-3; `RA00100AG_I_EN.pdf` printed/PDF p. 90 |
| Telephone limits, installer manual | `Jolly number plus 10 numbers; 9 simplified telephone commands` | `BQ01001-a-EN.pdf` printed/PDF pp. 1-3; `RA00100AG_I_EN.pdf` printed/PDF p. 90 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1804` | Canonical catalogue |
| Technical item description | Burglar alarm control unit with contacts | Canonical catalogue |
| Item family | Source placeholder description `0`; key `14` | Canonical catalogue |
| Main system | Burglar alarm system; key `3` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `204` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `668` | `9` | `0` | `0` | `1` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `668` | `1` | `133` Burglar Alarm central unit with communicator PSTN with internal contact | Fixed / designated metadata | `2506` | `627` | `1156` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `668` | Product Programming | `3` | Association key `4` |

| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `668` | Serial | `1` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `668` | `1` | `4` | `TiSecurityStandard_0100` | Parameter type `7`; payload not inspected |

Brand / line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Physical configurators | Not required; local keypad / display or TiSecurityStandard | `RA00100AG_I_EN.pdf` printed/PDF pp. 46-74, 90; `BQ01001-a-EN.pdf` pp. 1-3 |
| Zones 0 / `1..8` / 9 | Activators / burglar sensors / technical alarms | `RA00100AG_I_EN.pdf` printed/PDF pp. 46-74, 90; `BQ01001-a-EN.pdf` pp. 1-3 |
| Scenario / key limits | 16 activation scenarios; up to 50 keys with optional day / time restrictions | `RA00100AG_I_EN.pdf` printed/PDF pp. 46-74, 90; `BQ01001-a-EN.pdf` pp. 1-3 |
| Local contacts / tamper | Two separate programmable contact lines; local tamper distinct from contact inputs | `RA00100AG_I_EN.pdf` printed/PDF pp. 46-74, 90; `BQ01001-a-EN.pdf` pp. 1-3 |
| PSTN / GSM scope | Built-in PSTN; separate 3489GSM required for GSM option | `RA00100AG_I_EN.pdf` printed/PDF pp. 46-74, 90; `BQ01001-a-EN.pdf` pp. 1-3 |
| Repeated incorrect key | Three consecutive incorrect keys block arm / disarm / menu for one minute, technical sheet p. 1 | `RA00100AG_I_EN.pdf` printed/PDF pp. 46-74, 90; `BQ01001-a-EN.pdf` pp. 1-3 |
| Ademco Contact ID | DTMF event reporting to surveillance; independent of OpenWebNet gateway communication | `RA00100AG_I_EN.pdf` printed/PDF pp. 46-74, 90; `BQ01001-a-EN.pdf` pp. 1-3 |
| Published OPEN-SCS families | `WHO 0`, 1, 2, 4, 5, 9 in installer manual p. 90; installed revision / operations uncorroborated | `RA00100AG_I_EN.pdf` printed/PDF pp. 46-74, 90; `BQ01001-a-EN.pdf` pp. 1-3 |
| Zone 0 capacity | Maximum nine activators | `BQ01001-a-EN.pdf` p. 1 |
| Contact ID technical events | `AUX=8` fire, `AUX=1` gas, `AUX=2` freezer, `AUX=3` flooding, `AUX=9` remote assistance; `Z=9` auxiliary tampering; event origin zone / device where applicable | `BQ01001-a-EN.pdf` p. 2 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `668` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `133` - Burglar Alarm central unit with communicator PSTN with internal contact

Catalogue Object key `627` maps to external Object `133`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `NUM_PSTN` | No legal values specified in source | Not specified in source | Telephone number PSTN |
| `FW_VER` | `######` = Firmware version | `9.0.0` | Firmware version |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | Not applicable | None | Not applicable | No relation-specific filters associated | Not applicable | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `204` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Read installed firmware and compare with the applicability table | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Obtain hardware revision; no source-backed installed value | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Obtain microcontroller identity; no fingerprint retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve active Modules/Objects independently of candidate metadata | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Corroborate installed addressing and distinguish physical from reusable ranges | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Compare installed configuration with the exact firmware/Object restrictions | [Configuration](../../diagnostics/dim35-configuration.md) |

These are catalogue-derived diagnostic candidates. No Device-specific response or support across all commercial variants is established by a hardware capture.

## Functional applicability

| Catalogue Object / role | Applicability | Evidence |
| --- | --- | --- |
| `133` - Burglar Alarm central unit with communicator PSTN with internal contact | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `133` - Burglar Alarm central unit with communicator PSTN with internal contact | Burglar alarm system | `3` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `133` - Burglar Alarm central unit with communicator PSTN with internal contact | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

No physical configurators are required; use the keypad / display or TiSecurityStandard. The installer manual covers installation and first activation, system self-learning, contact programming, zones / scenarios, event memory, automations, maintenance and dialler setup. The user manual covers arming, partitioning, scenario selection, event review and telephone use; the software manual covers receive / edit / send, vocal messages and firmware updates. Configure Contact ID and telephone numbers according to the exact retained revision.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The exact technical sheet and installer manual agree on absorption and temperature but differ in depth (25 versus 31 mm) and give nominal versus operating supply values. Both depth values remain scoped, with no inferred mounting allowance. PSTN communication is intrinsic; GSM use requires separate 3489GSM and is not described as a built-in modem. Installer manual p. 90 explicitly lists an OPEN-SCS interface for `WHO 0`, 1, 2, 4, 5, 9; applicability to installed firmware and operations is still uncorroborated.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `BQ01001-a-EN.pdf` | Printed/PDF pp. 1-3: zones, scenarios / keys, PSTN / local interfaces, current / temperature / dimensions, Contact ID events and wiring protection notes. |
| `RA00100AG_I_EN.pdf` | Printed/PDF pp. 3-4 contents; installation / startup, local contacts, alarm / telephone setup, maintenance and p. 90 technical/OPEN-SCS families; source-specific operating procedures. |
| `RA00100AD_U_EN.pdf` | Printed/PDF contents and user-operation sections: arming, partition / scenario selection, event review and telephone commands; not an electrical installation authority. |
| `RA00100AB_S_EN.pdf` | Printed/PDF software workflow and project sections: receive / edit / send, vocal messages, firmware update and alarm / telephone settings; payload encoding unexamined. |

## Evidence limits and open work

Applicable mechanical revision, battery capacity / runtime, production support for each documented protocol operation and installed telephone service remain unestablished.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

### Retained original fingerprints

All incorporated originals were checked against the public archive by SHA-256 and byte length. Their manifest registrations were pushed on main before incorporation; previously registered originals were reused by fingerprint.

| Original | SHA-256 | Retention / size |
| --- | --- | --- |
| `BQ01001-a-EN.pdf` | `3ff2590acd901029aba31134d64f37c9c60eaf951a62fa3b7fa9d038e3902625` | 241683 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/3f/f2/3ff2590acd901029aba31134d64f37c9c60eaf951a62fa3b7fa9d038e3902625.pdf) |
| `RA00100AG_I_EN.pdf` | `cb07372bda190848f48b90c7e55ad2f1d208e011daea23a408bffbe71780caa1` | 8291268 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/cb/07/cb07372bda190848f48b90c7e55ad2f1d208e011daea23a408bffbe71780caa1.pdf) |
| `RA00100AD_U_EN.pdf` | `52025757b3d00de752207b712511e6ca8c5897c99f126b35e2b63a37de4634ef` | 18692498 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/52/02/52025757b3d00de752207b712511e6ca8c5897c99f126b35e2b63a37de4634ef.pdf) |
| `RA00100AB_S_EN.pdf` | `2a735a9346f86d294db13ffa081ab8d19b05098c984feb953238183b86953494` | 40161553 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/2a/73/2a735a9346f86d294db13ffa081ab8d19b05098c984feb953238183b86953494.pdf) |
