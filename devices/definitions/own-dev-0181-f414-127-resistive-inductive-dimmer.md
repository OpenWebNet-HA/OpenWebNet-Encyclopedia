# F414/127 resistive and inductive dimmer

## Summary

F414/127 is a one-channel DIN dimmer for resistive and ferromagnetic-transformer loads. It switches and adjusts brightness through SCS controls or its local button, signals load faults and has a replaceable fuse.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0181` | Project identity |
| Technical description | F414/127 resistive and inductive dimmer | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `F414/127` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1571` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `134` | Main association; independent of project ID |
| Firmware definition | `177` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Actuators | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F414/127` | Established catalogue identity | Manufacturer database commercial record `1598` explicitly links this SKU to item `1571` |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `F414/127` | DIN dimmer 1000 VA 127 V | Canonical commercial record `1598` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00278_e_EN.pdf` | Dimmer technical sheet | `MQ00278-e-EN; 20/09/2018` | Printed/PDF pp. 1-3: exact /127 load rows, supply / draw, enclosure, physical / virtual selectors, local operation and wiring. Non-/127 dissipation excluded. | [Archived original](https://archive.openwebnet-ha.org/sha256/d6/ca/d6cafa21923a3de3dfe1cbb42895617134892c56ae2edda866c2e7fff2c54273.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MQ00278_e_EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1571`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |
| `BTicino-Mexico-lighting-control.pdf` | Regional lighting technical guide | Publication date unestablished | Printed pp. 76, 78 / PDF pp. 78, 80: exact /127 ratings, draw, terminals, IP20 and Push & Learn table; regional discrepancies retained | [Archived original](https://archive.openwebnet-ha.org/sha256/c9/0f/c90ff73d4a7395428ae1147b00da9f5ac9c9ff1c7133c772df1411d35cd56aa3.pdf) | [Publisher source](https://bticino.com.mx/uploads/8661202a4fdd25e15583d09fc93f8e02.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Nominal / operating SCS supply | `27 Vdc / 18..27 Vdc` | `MQ00278_e_EN.pdf` printed/PDF p. 1 |
| SCS current draw | `9 mA` | `MQ00278_e_EN.pdf` printed/PDF p. 1 |
| Exact variant load row | `110 Vac, 50 Hz; 0.5..9 A; 60..1000 VA` | `MQ00278_e_EN.pdf` printed/PDF p. 1 |
| Number of outputs | `1; 9 A for exact /127 variant` | `MQ00278_e_EN.pdf` printed/PDF p. 1 |
| Operating temperature | `−5..+45 °C` | `MQ00278_e_EN.pdf` printed/PDF p. 1 |
| Mounting | `4 DIN modules` | `MQ00278_e_EN.pdf` printed/PDF p. 1 |
| Printed protection / impact values | `IK04 / IP20; labels apparently inverted` | `MQ00278_e_EN.pdf` printed/PDF p. 1 |
| Interfaces / local indication | `SCS connector; load terminals; configurator socket; local load key; load LED; replaceable fuse` | `MQ00278_e_EN.pdf` printed/PDF p. 1 |

### Regional rating evidence

| Source | Published mains voltage | Exact F414/127 load / current evidence |
| --- | --- | --- |
| MQ00278-e-EN, 20 September 2018 | `110 Vac`, `50 Hz` | `60..1000` VA; 0.5..9 A; 9 mA |
| Mexico guide, printed p. 76 / PDF p. 78 | 110 V | `60..1000` W; 0.25..4 A; 5 mA |
| Mexico guide, printed p. 78 / PDF p. 80 | `127 Vac` | `60..1000` W; 5 mA |

The Mexico guide also gives IP20, 2.5 mm² terminals, 27 Vdc supply, four DIN modules, −5..+45 °C and no Push & Learn for this reference (printed p. 76 / PDF p. 78). These are source-specific specifications, not a conversion of VA to W.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1571` | Canonical catalogue |
| Technical item description | DIN dimmer 1000 VA 127 V | Canonical catalogue |
| Item family | Source placeholder description `0`; key `4` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `134` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `134` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `177` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `177` | `1` | `8` Dimmer actuator | Fixed / designated metadata | `1339` | `8` | `698` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `177` | Physical configuration | `0` | Canonical firmware/mode association |
| `177` | Virtual Configuration | `1` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Physical A / PL / G | `1..9` / `1..9` / `0..9` | `MQ00278_e_EN.pdf` printed/PDF pp. 2-3 |
| Virtual room / point / groups | `0..10` / `0..15` / group `1..10` values `0..255` | `MQ00278_e_EN.pdf` printed/PDF pp. 2-3 |
| `M=0` / `SLA` / `PUL` | Master / same-address slave / monostable master ignoring room / general commands | `MQ00278_e_EN.pdf` printed/PDF pp. 2-3 |
| `M=1` / 2 / 3 / 4 | Master `OFF` delays slave by 1 / 2 / 3 / 4 minutes, point-to-point only | `MQ00278_e_EN.pdf` printed/PDF pp. 2-3 |
| Virtual `OFF` delay | `0..255` seconds, master / master-`PUL`; distinct from physical minutes | `MQ00278_e_EN.pdf` printed/PDF pp. 2-3 |
| Software-only functions | Slave-`PUL`; minimum brightness at power-on | `MQ00278_e_EN.pdf` printed/PDF pp. 2-3 |
| Local load button / protection | Brief press toggles; sustained press adjusts brightness; load-fault signalling; replaceable fuse | `MQ00278_e_EN.pdf` printed/PDF pp. 2-3 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `177` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `177` | `A` | `0..9` | `0` | A; Enviroment |
| `177` | `PL` | `0..9` | `0` | PL; Light Point |
| `177` | `M` | `0..2`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (0-4, Pul, Sla) |
| `177` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `8` - Dimmer actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality; mode (M, S + PULL) |
| `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled | `0` | State saving on reset |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `MIN_LEVEL` | `1..100` | `1` | Minimum level |
| `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge | `0` | Type of load; Default value depends on device. |
| `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard | `0` | Voltage standard |
| `MIN_LEVEL_ADV` | `1..100` | `0` | Minimum level advanced; Default value depends on device and Type of load value |
| `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable | `0` | Enable / Disable minimum level |
| `G1` | `0..255` | `0` | Group 1 |
| `G2` | `0..255` | `0` | Group 2 |
| `G3` | `0..255` | `0` | Group 3 |
| `G4` | `0..255` | `0` | Group 4 |
| `G5` | `0..255` | `0` | Group 5 |
| `G6` | `0..255` | `0` | Group 6 |
| `G7` | `0..255` | `0` | Group 7 |
| `G8` | `0..255` | `0` | Group 8 |
| `G9` | `0..255` | `0` | Group 9 |
| `G10` | `0..255` | `0` | Group 10 |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `177` | `8` | `2193` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

### Applicability irregularities

Firmware `177` item-side `M=0..2,11,15` omits the physical `M=3/4` settings documented in the technical sheet. No conversion is attached to resolve physical timer selectors into the reusable Object mode. The sole state-saving filter retains its full reusable domain and default. `MIN_LEVEL_ADV` stores default `0` outside its `1..100` reusable domain, with no applicable correction recorded. Generic `TYPE_LOAD` labels for LED, fluorescent, DALI and other loads, and `TYPE_STANDARD` values, do not establish those capabilities on this exact product. The published load families remain the applicable evidence.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `134` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `8` - Dimmer actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `8` - Dimmer actuator | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

### Related functional reference families

The correspondence below is a semantic cross-reference based on the named role and the canonical functional reference; it does not assert captured frames or support for every operation.

| Catalogue role | Related canonical reference | Evidence limit |
| --- | --- | --- |
| `8` | [Lighting](../../functional/who-1-lighting/) | Related canonical semantics for the named role; exact configured operation and runtime transport remain to be corroborated |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The technical sheet separates physical addressing (`A=1..9`, `PL=1..9`, `G=0..9`) from virtual room `0..10`, point `0..15` and ten group fields `0..255`. Physical `M=0` selects master, `M=SLA` follows a same-address master, and `M=PUL` ignores room / general commands. `M=1..4` sets slave `OFF` delay to `1..4` minutes; software allows `0..255` seconds in master / master-`PUL` mode. Slave-`PUL` and minimum startup brightness require software. See `MQ00278_e_EN.pdf`, printed/PDF pp. 2-3, for settings and wiring; the sheet states one automatically configured server channel.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The exact sheet covers four distinct references. Only the named `/127` load row is used here: it prints 110 Vac at 50 Hz, despite the `/127` commercial suffix and catalogue wording. The sheet prints “Protection index: IK04” and “Impact resistance: IP20”; the values are preserved with this apparent label inversion. Dissipation values 10 W and 11 W are explicitly labelled F414 and F415 respectively and are not established for their `/127` variants. The generic “1000VA” heading does not override the F415/127 400 VA row.

The retained Mexican manufacturer guide differs from the 2018 English sheet in mains voltage, load units, current limits and SCS draw. Its two exact-reference pages also differ internally in the stated mains voltage. No dated hardware change or regional equivalence is established. Preserve each row when checking a physical installation; the SKU suffix alone does not resolve these conflicts.

## Evidence limits and open work

Exact installed mains suitability, fuse replacement rating for the variant, variant-specific dissipation and production applicability remain to be corroborated. No LED-load compatibility is inferred.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0181-0190-2026-10-07.md#own-dev-0181)
