# Flush-mounted temperature central unit

## Summary

The 4695 is a temperature-control central unit for up to four zones, including its local zone. Its display provides heating and cooling management, with weekly programmes and manual, holiday or timed operating modes.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0017` | Project identity |
| Technical description | Flush-mounted four-zone temperature-control central unit | Catalogue + official documentation |
| Catalogue item | `168` - Flush mounted temperature central unit | Implementation evidence |
| Main catalogue system | Temperature control | Implementation evidence |
| Item model / `modobj` | `48` | Implementation evidence |
| Firmware definition | `1.0 build 35` | Implementation evidence |
| Declared Modules | `1` | Implementation evidence |
| Configuration modes | Virtual, Physical, Product Programming | Implementation evidence |
| Programming connection | Serial | Implementation evidence |
| Categories | Thermoregulation, User Interface | Product and capability model |

This Device is the four-zone MyHOME temperature-control central unit sold under several BTicino and Legrand references. It provides the system-level scheduling and zone-management interface while the catalogue exposes one fixed OpenWebNet Object representing the four-zone control-unit role.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC/HS4695` | Established catalogue identity; 4695 family documentation applies | Catalogue + official 4695 documentation |
| BTicino - Axolute | `HD4695` | Established catalogue identity; 4695 family documentation applies | Catalogue + official 4695 documentation |
| BTicino - LivingLight | `L/N/NT4695` | Established catalogue identity; 4695 family documentation applies | Catalogue + official 4695 documentation |
| BTicino - Matix | `AM5875` | Established identity | Catalogue + U1809C installation-manual cover |
| Legrand - Vela | `683090` | Established catalogue identity | Canonical catalogue; exact-product technical sheet not retained |
| Legrand - Vela | `687390` | Established catalogue identity | Canonical catalogue; exact-product technical sheet not retained |
| Legrand - Vela | `687890` | Established catalogue identity | Canonical catalogue; exact-product technical sheet not retained |

Shared item membership establishes the common catalogue capability core. It does not prove that faceplate, market, hardware revision, or packaging is identical.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `U1809F_U_EN` | User guide | No dated imprint established in inspected original | 4695 user operation and temperature-control behavior | [Archived original](https://archive.openwebnet-ha.org/sha256/f9/0c/f90c3dad042158152e3607dd461b143ea5c18d0dec917f9f411405f30a92d8b4.pdf) | publisher source not currently retained |
| `U1809C_Installatore_UK` | Installation / commissioning manual | November 2009; `11/09-01 PC` | 4695 installation and commissioning | [Archived original](https://archive.openwebnet-ha.org/sha256/c4/46/c4461318739c49ab58078d75876aef57bff823dcaf7f964714a60f154f489dee.pdf) | publisher source not currently retained |
| `U1809B_Software_GB` | Software manual | January 2008; `01/08-01 PC` | TiThermoBasic programming / firmware workflow | [Archived original](https://archive.openwebnet-ha.org/sha256/3d/10/3d1072e42a34c621e60cc455b94985116d4bc475ecfaca52df4de3bfe05f277e.pdf) | publisher source not currently retained |
| MyHOME catalogue `HPML0714` | Product catalogue | No dated imprint established in inspected original | System-level temperature-control context only; the `4695` family is not named. Related Arteor central units `573918` / `573919` occur on printed pp. 16, 24, 32 / PDF pp. 16, 24, 32 | [Archived MyHOME catalogue](https://archive.openwebnet-ha.org/sha256/13/8e/138e7a234fe24fb044d3bfc82954e08b2887be22f3f8ceb24aecaeff6ed2f2e5.pdf) | publisher source not currently retained |

The 4695 documentation describes management of a temperature-control system with up to four zones and PC programming through TiThermoBasic. Where an official PDF could not be fetched by the archival runner, the official publisher URL is retained rather than substituting an unofficial mirror.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 3 flush-mounted modules | 4695 installation documentation |
| User interface | local display and front-panel control | 4695 user / installation documentation |
| Managed installation | temperature-control system with up to 4 zones | 4695 user / installation documentation |
| Product programming | TiThermoBasic PC workflow | 4695 software documentation |

The product-level scheduling and zone-management interface is broader than the single fixed OpenWebNet Object.

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply / current | `18..27` V; maximum `30 mA` display on, typical `8.5 mA` display off | U1809C, p. 62 |
| Operating temperature / enclosure | `0..40` °C; IP30 | Same source |
| Mounting terminology | Three module width, flush box/frame/plate installation; source calls this “3 DIN modules” | U1809C, pp. 12, 62; not proof of DIN-rail mounting |
| Batteries / removable front | Two LR6/AA 1.5 V alkaline batteries for off-base PC programming and clock continuity; bus supplies installed unit | U1809C, p. 13; U1809F, p. 10 |
| Battery-only current | `3 Vdc`; maximum `150 mA` display on, typical `15 mA` display off | U1809C, p. 62; not SCS current |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `168` | Implementation evidence |
| Main system | thermoregulation / Temperature control | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `48` | Implementation evidence |
| Family | `11` | Implementation evidence |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Temperature control | `48` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `23` | `1` | `0` | `35` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Catalogue applicability is not a claim that every surviving commercial variant reports this exact installed build. `DIMENSION 2` remains the authoritative installed-firmware observation when the Device exposes it.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `23` | `63` | BTicino (key `1`) | `0` | external software | `TiThermoBasic_0101` |
| `23` | `620` | Legrand (key `2`) | `1` | external software | `ThermoConfigBasic_0100` |

All 2 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `23` | `1` | `90` Temperature control 4 zones control unit | Fixed/designated metadata | `644` | `90` | `448` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

There is no Virgin Object for this firmware. The slot carries condition record `4163` with an empty condition string and conversion-rule reference `1000` in the implementation database. Because no Device-specific predicate is expressed there, this dossier does not invent one.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `23` | Physical configuration | `0` | Canonical firmware/mode association |
| `23` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `23` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `23` | Serial | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `23` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `23` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `23` | `ZB` | `0..9` | `1` | ZB; ZB thermo zone address |
| `23` | `SLA` | `0..8` | `0` | `SLA`; Thermoregulation slave probe |

The pair `ZA` / `ZB` is represented separately at firmware level. The reusable control-unit Object exposes the combined two-digit zone as `ZAZB`.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `90` - Temperature control 4 zones control unit

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `00..99` | `01` | Zone |
| `WARM` | `0` = Disable; `1` = Enable | `0` | Winter modality; Winter mode |
| `COLD` | `0` = Disable; `1` = Enable | `0` | Summer modality; Summer mode |
| `SLA` | `0..8` | `0` | Slave number |

### Device-specific interpretation

Firmware ZA/ZB digits and reusable ZAZB are different address representations. Weekly profiles, fan-coil control and commissioning are product capabilities beyond the single protocol Module; they do not create new Objects.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `23` | `1` | `90` | `4163` | No textual predicate stored | `1000` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | - | None | - | No relation-specific filters associated | - | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `1000` | `ZA=0; ZB=1..9` | `ZAZB=01..09` | Rule `1000` through branch `1001` |
| `1000` | `ZA=1..9; ZB=0..9` | `ZAZB=10..99` | Rule `1000` through branches `1002..1010` |
| `1000` | `ZA=0; ZB=0` | No `00` mapping stored | Do not widen the conversion from the reusable Object domain |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | identify item model / brand / line where exposed | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware instead of assuming catalogue `1.0.35` | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate the single fixed control-unit Module | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect the configured thermoregulation address when exposed | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `ZA` / `ZB` / `SLA` and Object configuration where exposed | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Weekly | Three programs per season; daily 0–24 h profiles per zone/day | U1809C, p. 11 |
| Manual / Timed | Fixed temperature across zones; Timed up to 24 h 59 min, then restores previous settings | Same source |
| Holiday / Holidays | Holiday runs a selected daily profile until end; Holidays holds protection until end; both restore selected weekly program | Same source; U1809F, pp. 15–16 |
| Protection / Off | Winter antifreeze or summer thermal protection; Off switches the system off | U1809C, p. 11; U1809F, p. 17 |
| Temperature levels | Winter protection/T1/T2/T3 defaults 7/18/20/22 °C; summer 35/20/23/25 °C; 0.5 °C UI steps with T3>T2>T1 | U1809C, p. 37; U1809F, p. 19 |
| Loads / pumps | On/Off, Open/Close, three-speed fan-coil or gateway; heating/cooling/both associations and pump delay settings | U1809C, pp. 48–51 |
| Commissioning / diagnostics | Zone acquisition, actuator/pump setup, fault display, probe adjustment in 0.1 °C steps; System Test puts system Off and disables commands | U1809C, pp. 54–60 |

The single Object `90` is the protocol projection of these product functions. Program/profile counts do not create more catalogue Modules.

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

Configure the integrated local probe with ZA/ZB; the three remaining zones must have consecutive addresses after it. Learning discovers those following addresses (for example local 21 searches 22/23/24), then actuator/pump setup and Send complete zone commissioning. This is a four-zone limit, not a requirement that the local address start at 01 (`U1809C`, pp. 13, 54–55).

TiThermoBasic’s “Serial” catalogue connection uses programming cable 3559 at a PC USB port and its assigned COM address. Select Connect first, put the unit in Maintenance and follow the software’s connection sequence; the manual warns that a wrong port/order can leave it needing recovery (`U1809B`, pp. 25–26). Upload means device-to-project; Download means project-to-device and can Force, Align or Cancel mismatched configuration. Compare and Diagnosis are separate operations; firmware update selects an FWZ file (pp. 27–31). These operations do not justify publishing private installation configuration.

Zone Reset All removes zone configuration and requires Learning again; Total Reset also removes programs and restores factory settings (`U1809C`, pp. 53, 61). System Test’s M30/PIC/HW display is manufacturer diagnostic UI, not a substitute for an observed OpenWebNet firmware fingerprint.

## Source reconciliation

The three archived `4695` manuals establish that the single OpenWebNet control-unit Object represents a much richer four-zone thermoregulation product:

- the central unit manages heating and cooling operation for up to four zones, including the locally controlled zone;
- product programming provides multiple weekly programs and daily zone profiles rather than only a current setpoint;
- user operating states include Manual, Holiday/Holidays, Timed, `OFF` and the heating/cooling protection modes such as antifreeze or thermal protection;
- timed operation supports a finite duration up to the documented day-scale limit, while local operation also supports temperature offset/override behavior;
- fan-coil installations are explicitly supported by the product workflow;
- installation/setup includes zone association, probe configuration, system diagnostics/test procedures and total-reset behavior;
- TiThermoBasic handles project transfer and product programming in addition to ordinary configurator-based setup.

These are Device-level capabilities of the 4695 family. They do not create additional catalogue Modules, but they must be retained so Object `90` is not misread as the entirety of the product behavior.

The installation manual cover names HC/HS/HD4695, L/N/NT4695 and AM5875; the earlier AM5875 documentation-gap statement was incorrect. U1809C has 11/09-01 PC and U1809B 01/08-01 PC imprints. U1809F has no established publication imprint in the inspected text; screenshot dates are not publication dates. The software calls its USB/COM workflow Serial, which does not establish a standard serial port directly on the unit. The installer’s “3 DIN modules” wording is retained alongside its flush-installation diagram. The HPML0714 catalogue names related Arteor products, not the Vela references in this item cluster; those electrical/package details remain unestablished.

## Evidence limits and open work

- Obtain a sanitized `DIMENSION 1` / `DIMENSION 2` / `DIMENSION 30` / `DIMENSION 32` / `DIMENSION 35` fingerprint from a known 4695-family unit.
- Locate exact technical/package evidence for the three Vela references; AM5875 is explicitly named on the retained installation-manual cover.
- Correlate observed installed firmware with catalogue firmware `1.0 build 35`.
- Corroborate the stored `ZA`/`ZB` → `ZAZB` conversion on installed hardware; the canonical conversion records are present.
- Preserve later document revisions separately rather than replacing the current evidence.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)

- [Semantic review record, 5 October 2026](../../project/review/device-reviews-0011-0020-2026-10-05.md#own-dev-0017)
