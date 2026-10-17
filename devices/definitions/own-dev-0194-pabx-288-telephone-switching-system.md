# PABX 288 telephone switching system

## Summary

345829 PABX 288 combines an analogue telephone exchange with two-wire video-entry and MyHOME integration. Its base configuration serves two outside lines and eight extensions, while expansion accessories increase capacity; connected compatible phones can answer entrance calls and send remote commands.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0194` | Project identity |
| Technical description | PABX 288 telephone switching system | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `345829` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1819` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `33` | Main association; independent of project ID |
| Firmware definition | `10`, `94`, `95` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Gateways and interfaces, Audio video | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `345829` | Established catalogue identity | Manufacturer database commercial record `1958` explicitly links this SKU to item `1819` |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `345829` | PABX288 automatic telephone switching system | Canonical commercial record `1958` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `345829-italian-product-sheet.pdf` | Exact Italian publisher product export | `Export retrieved 05.10.2026; compliance dates are boilerplate` | Exact commercial description and technical attributes; EAN used only if explicitly present; European compliance boilerplate is not a publication revision. | [Archived original](https://archive.openwebnet-ha.org/sha256/c0/2f/c02f7175ac39f1b45fdbb55479662090469d5ded62dea10d93ab1f8f0592c4c3.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-345829) |
| `BT00478_a_IT.pdf` | 345829 PABX technical sheet | `BT00478-a-IT; printed publication date not established` | Printed/PDF pp. 1-6: supply / current, capacity / expansion, interfaces / cables, integration and wiring examples; diagram and text differences preserved. | [Archived original](https://archive.openwebnet-ha.org/sha256/ab/e7/abe77364fdab3dbcbea80c7cfae5a6aae9054fb4aa4381e6e53d9189aed7ed5e.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/BT00478_a_IT.pdf) |
| `U2131F.pdf` | 345829 multilingual installation leaflet | `U2131F01PC-12W08` | PDF pp. 1-4: mains / backup connections, cable lengths, interface diagram, mounting / expansion; source cable codes preserved. | [Archived original](https://archive.openwebnet-ha.org/sha256/a3/b9/a3b9b5ac80174c8c754178901b1e9b1a2c62ddfdedeb555d19fb5b07073f5537.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/U2131F.pdf) |
| `U2132C_S_IT.pdf` | TiPABX software manual | `U2132C_S_IT; cover 11/11-01 PC` | Printed/PDF pp. 4-26: prerequisites, PC connection, telephone / video parameters, project / scenarios / commands, validation, transfer and firmware update. | [Archived original](https://archive.openwebnet-ha.org/sha256/50/83/5083ca71ad737d475fb186e5984cdc6ddcd477163b58b57cccdaa049c66bc12f.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/U2132C_S_IT.pdf) |
| `U2132F_U_IT.pdf` | 345829 PABX user manual | `U2132F_U_IT; cover 08/13-01 PC` | Printed/PDF pp. 6-16: telephone / video-entry operation, DISA/DOSA, home automation commands, scenarios and recorded messages; source-dependent phone capabilities. | [Archived original](https://archive.openwebnet-ha.org/sha256/c9/d0/c9d072a0fccf2022ad1983f73adf85dda50175464b9e17a81a0dc5aa8906a721.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/U2132F_U_IT.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1819`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mains supply / draw | `110..240 Vac, 50/60 Hz; 130..210 mA` | `BT00478_a_IT.pdf` printed/PDF p. 1; `U2131F.pdf` PDF pp. 1-4 |
| 12 Vdc backup draw | `390 mA standby / 1100 mA with 8 phones engaged` | `BT00478_a_IT.pdf` printed/PDF p. 1; `U2131F.pdf` PDF pp. 1-4 |
| Maximum dissipated power | `13 W` | `BT00478_a_IT.pdf` printed/PDF p. 1; `U2131F.pdf` PDF pp. 1-4 |
| Operating temperature / mounting | `0..40 °C; 10 DIN modules` | `BT00478_a_IT.pdf` printed/PDF p. 1; `U2131F.pdf` PDF pp. 1-4 |
| Base / expanded capacity | `2 external analogue lines / 4 with 345831; 8 extensions / 24 with two 345830` | `BT00478_a_IT.pdf` printed/PDF p. 1; `U2131F.pdf` PDF pp. 1-4 |
| Phone wiring / distance | `0.28 mm² pair: 500 m; specified BUS cable: 700 m` | `BT00478_a_IT.pdf` printed/PDF p. 1; `U2131F.pdf` PDF pp. 1-4 |
| Dialling / MyHOME commands | `Pulse or multifrequency; nine customisable voice commands` | `BT00478_a_IT.pdf` printed/PDF p. 1; `U2131F.pdf` PDF pp. 1-4 |
| Connections | `Video-entry terminals; SCS; telephone lines/extensions; mini-USB; RS232; Ethernet 10/100; expansion; 12 Vdc backup` | `BT00478_a_IT.pdf` printed/PDF p. 1; `U2131F.pdf` PDF pp. 1-4 |
| Indicators | `SPEED, FULL, LINK and SYSTEM` | `BT00478_a_IT.pdf` printed/PDF p. 1; `U2131F.pdf` PDF pp. 1-4 |
| Italian export supply / draw / power | `110..230 Vac`; `130..210 mA`; `13 W`; supply range differs from technical sheet | `345829-italian-product-sheet.pdf` PDF p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1819` | Canonical catalogue |
| Technical item description | PABX288 automatic telephone switching system | Canonical catalogue |
| Item family | Source placeholder description `0`; key `100` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `33` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `33` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Video door entry system 8 wires | private riser | Canonical item/bus relationship |
| Video door entry system 8 wires | public riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `10` | `2` | `1` | `0` | `1` | Catalogue default | Official |
| `94` | `2` | `0` | `23` | `1` | Not catalogue default | Official |
| `95` | `1` | `0` | `23` | `1` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `10` | `351` | BTicino (key `1`) | `0` | external software | `TiPABX_0200` |
| `94` | `58` | BTicino (key `1`) | `0` | external software | `TiPABX_0200` |
| `95` | `102` | BTicino (key `1`) | `0` | external software | `TiPABX_0101` |

All 3 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

The Official releases are catalogue-default `10: 2.1.0`, `94: 2.0.23` and `95: 1.0.23`. The shared item/Object `FW_VER=3.0.0` default is not an additional firmware release. All three use Object `101` in slot `1`, with no attached filters, slot predicates, conversions or Virgin membership.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `10` | `1` | `101` 2 wires interface PABX | Fixed / designated metadata | `1388` | `101` | `734` |
| `94` | `1` | `101` 2 wires interface PABX | Fixed / designated metadata | `1389` | `101` | `735` |
| `95` | `1` | `101` 2 wires interface PABX | Fixed / designated metadata | `1390` | `101` | `736` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `10` | Product Programming | `3` | Canonical firmware/mode association |
| `94` | Product Programming | `3` | Canonical firmware/mode association |
| `95` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `10` | Ethernet | Canonical firmware/connection association |
| `10` | USB | Canonical firmware/connection association |
| `94` | Ethernet | Canonical firmware/connection association |
| `94` | USB | Canonical firmware/connection association |
| `95` | Ethernet | Canonical firmware/connection association |
| `95` | USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Base exchange | 2 outside analogue lines; 8 extensions | `BT00478_a_IT.pdf` printed/PDF p. 1; `U2131F.pdf` pp. 1-4; `U2132C_S_IT.pdf`; `U2132F_U_IT.pdf` |
| Expansion | 345831: 4 outside lines; two 345830: 24 extensions | `BT00478_a_IT.pdf` printed/PDF p. 1; `U2131F.pdf` pp. 1-4; `U2132C_S_IT.pdf`; `U2132F_U_IT.pdf` |
| Voice commands | 9 customisable MyHOME commands | `BT00478_a_IT.pdf` printed/PDF p. 1; `U2131F.pdf` pp. 1-4; `U2132C_S_IT.pdf`; `U2132F_U_IT.pdf` |
| Phone cable / length | 0.28 mm² pair 500 m; specified BUS cable 700 m; differing cable codes retained | `BT00478_a_IT.pdf` printed/PDF p. 1; `U2131F.pdf` pp. 1-4; `U2132C_S_IT.pdf`; `U2132F_U_IT.pdf` |
| PC setup | TiPBX; serial/USB/Ethernet associations scoped in catalogue / manual | `BT00478_a_IT.pdf` printed/PDF p. 1; `U2131F.pdf` pp. 1-4; `U2132C_S_IT.pdf`; `U2132F_U_IT.pdf` |
| Phone-dependent operations | Additional video-control / remote activations require compatible BTicino phones | `BT00478_a_IT.pdf` printed/PDF p. 1; `U2131F.pdf` pp. 1-4; `U2132C_S_IT.pdf`; `U2132F_U_IT.pdf` |
| Backup supply | E47/12 and 3505/12 battery; separate 12 Vdc consumption values | `BT00478_a_IT.pdf` printed/PDF p. 1; `U2131F.pdf` pp. 1-4; `U2132C_S_IT.pdf`; `U2132F_U_IT.pdf` |

### Default installation and phone limits

U2131F p. 4 and BT00478-a-IT p. 2 give CITO1 `1`, CITO2 `2`, principal entrance `00`, and associated internal-video addresses `09` and `10`. These factory installation values are separate from the reusable Object `SYSADDRESS=1`. The user manual explicitly excludes a 56K modem downstream of the exchange and says to connect it directly to the telephone line (U2132F_U_IT p. 6), qualifying the technical sheet’s generic modem-compatibility statement. On mains loss, extensions 401/402 remain associated with outside lines 1/2 (p. 12); this is distinct from the specified optional 12 V backup supply and does not establish backup runtime.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `10` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `10` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `10` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `10` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `94` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `94` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `94` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `94` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `95` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `95` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `95` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `95` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `101` - 2 wires interface PABX

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

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
| `DIMENSION 1` | Corroborate item model `33` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `101` - 2 wires interface PABX | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `101` - 2 wires interface PABX | Integration function | `26` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

### Related functional reference families

The correspondence below is a semantic cross-reference based on the named role and the canonical functional reference; it does not assert captured frames or support for every operation.

| Catalogue role | Related canonical reference | Evidence limit |
| --- | --- | --- |
| Video-entry-related roles | [Basic video entry](../../functional/who-6-basic-video-door-entry/);[Video entry and telephony](../../functional/who-8-video-door-entry-telephony/) | Related canonical families; which namespace and operation applies to each installed component is not established by the product manual alone |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

TiPBX configures and updates the exchange through its documented PC routes. Use `U2132C_S_IT.pdf` for project setup, telephone / video-entry parameters, address book, voice commands and transfer; `U2132F_U_IT.pdf` covers user telephone and video-entry operations. Install base and expansion connections from `U2131F.pdf`. Functions stated as available only with BTicino phones remain phone-dependent.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

TiPABX validates the project before allowing Download; errors disable that action. Download sets date/time and offers Ethernet address/discovery, serial COM/discovery or automatic USB detection. Upload retrieves the existing project; firmware update selects a `.fwz` and uses those connection routes (U2132C_S_IT, pp. 8, 24–26). The hardware’s serial connector is documented even though the catalogue connection associations list only Ethernet and USB.

## Source reconciliation

The exact technical sheet identifies 345829, base / expanded capacities and backup supply separately. The technical sheet names cable 336904 whereas the installation leaflet names L4669/346904: their shared 700 m figure is retained without assuming all cable references are interchangeable. The nominal mains specification is 50/60 Hz despite a diagram legend mentioning 60 Hz. The Italian product export gives `110..230` Vac, while the technical sheet and installation label give `110..240` Vac; these source ranges are kept separately. The single catalogue Object is the two-wire PABX interface, independent of the telephone-extension count.

The catalogue stores private/public 8-wire video-entry bus labels, while the exact hardware sheet, U2131F and Object `101` explicitly describe a two-wire interface. Both source scopes are preserved; the database labels are not used to describe the physical wiring. The technical sheet says pulse or multifrequency dialling, but its service text says extension DC signalling is not detected and requires DTMF; the generic compatibility wording is not a promise of every legacy handset service.

## Evidence limits and open work

Actual expansion accessories, compatible phone features, supplied cable applicability, backup runtime and installed firmware release remain to be corroborated.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0191-0200-2026-10-07.md#own-dev-0194)
