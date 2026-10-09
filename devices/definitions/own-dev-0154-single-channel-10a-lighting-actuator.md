# Single-channel 10 A lighting actuator

## Summary

`F411U1` is a single-channel lighting actuator with a local button and status LED. It switches compatible LED, fluorescent and transformer-fed loads, with configurable zero-crossing control. Its one relay can also act as a clean contact in the documented non-zero-crossing configuration.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0154` | Project identity |
| Technical description | Single-channel 10 A lighting actuator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `003847`, `F411U1` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `2131` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `79` | Main association; independent of project ID |
| Firmware definition | `669` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Actuators | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `003847` | Established catalogue identity | Manufacturer database commercial record `2517` explicitly links this SKU to item `2131` |
| BTicino | `F411U1` | Established catalogue identity | Manufacturer database commercial record `2468` explicitly links this SKU to item `2131` |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `F411U1` | 1x10 A actuator, 2DIN | Canonical commercial record `2468` |
| `003847` | 1x10 A actuator, 2DIN | Canonical commercial record `2517` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `F411U1-italian-product-sheet.pdf` | Exact Italian product export | `Captured 05/10/2026; compliance-template date does not establish product publication date` | Complete exact-reference commercial export and all classification attributes examined; EAN only where explicitly retained. Source-specific ratings do not replace technical-sheet scopes | [Archived original](https://archive.openwebnet-ha.org/sha256/36/ff/36ffef265654bf508a482559cdcc99b73e0eda6d2c04378512218056dbd039ed.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F411U1) |
| `MQ01015_b_IT.pdf` | Legacy manufacturer technical documentation | `MQ01015_b_IT; 20/09/2018` | PDF pp. 1–2: complete exact `F411U1`/003847 load and configuration sheet | [Archived original](https://archive.openwebnet-ha.org/sha256/f1/12/f112b3b96ac05db7e9fbe751994d23542c07bdb9784ccbc0fa69e679308476ac.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/MQ01015_b_IT.pdf) |
| `MQ01015_b_EN.pdf` | English counterpart of manufacturer-linked document | `MQ01015_b_EN; 20/09/2018` | PDF pp. 1–2: complete exact `F411U1`/003847 load and configuration sheet | [Archived original](https://archive.openwebnet-ha.org/sha256/af/33/af33550d62e7be08a0adf00966c14893d77e52e43f018ff2d8e7e0be5e6923c6.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MQ01015_b_EN.pdf) |
| `ST-00002703-EN.pdf` | Technical Sheet `ST-00002703-EN` | `ST-00002703-EN; 16/06/2026` | PDF p. 9: exact actuator/server ecosystem compatibility inspected; other product functions not transferred | [Archived original](https://archive.openwebnet-ha.org/sha256/b2/f5/b2f5090b601e33cdef9ba666108848ff4d9800792ccd5b7c14385da300bf0ffa.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002703-EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2131`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |
| `HRM_SCS_Guide_AD_EXOD18SAG_GB.pdf` | Manufacturer catalogue guide | EXOD18SAG_GB; historical retained edition | PDF pp. 30,66,79 examined for exact `F411U1`/`F411U2` load tables and actuator/wiring scope; other product chapters not reviewed | [Archived original](https://archive.openwebnet-ha.org/sha256/2e/8b/2e8b52836a644b6726555eb523b3f5fe8bce39419c0f096c035baae0b1a38d40.pdf) | Publisher URL not retained in manifest |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS nominal / operating supply | `27 Vdc / 22..27 Vdc` | `MQ01015_b_EN` printed/PDF pp. 1-2 |
| Standby / maximum draw | `5 mA / 30 mA` | `MQ01015_b_EN` printed/PDF pp. 1-2 |
| Temperature / size | `0..40 °C; 2 DIN modules` | `MQ01015_b_EN` printed/PDF pp. 1-2 |
| Outputs | `1 x 10 A` | `MQ01015_b_EN` printed/PDF pp. 1-2 |
| Incandescent/halogen | `2300 W / 10 A at printed 250 Vac; 1100 W / 10 A at 110 Vac` | `MQ01015_b_EN` printed/PDF pp. 1-2 |
| LED / CFL | `500 W / 2 A at 250 Vac; 250 W / 2 A at 110 Vac` | `MQ01015_b_EN` printed/PDF pp. 1-2 |
| Linear fluorescent / electronic transformer | `920 W / 4 A at 250 Vac; 440 W / 4 A at 110 Vac` | `MQ01015_b_EN` printed/PDF pp. 1-2 |
| Ferromagnetic transformer | `920 VA / 4 A cos phi 0.5 at 250 Vac; 440 VA / 4 A at 110 Vac` | `MQ01015_b_EN` printed/PDF pp. 1-2 |
| Protection codes | `IP20; IK04` | `MQ01015_b_EN` printed/PDF pp. 1-2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2131` | Canonical catalogue |
| Technical item description | 1x10 A actuator, 2DIN | Canonical catalogue |
| Item family | 0; key `2` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `79` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `79` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `669` | `1` | `0` | No build row | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `669` | `1` | `6` Light actuator | Fixed/designated metadata | `2497` | `6` | `1147` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `669` | Physical configuration | `0` | Canonical firmware/mode association |
| `669` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `669` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `A / PL` | physical `1..9`; virtual room `0..10`, point `0..15` | `MQ01015_b_EN` printed/PDF pp. 1-2 |
| `M=0 / SLA / PUL` | master / slave / monostable master | `MQ01015_b_EN` printed/PDF pp. 1-2 |
| `M=1..4` | slave `OFF` delay `1..4` min; virtual `0..255` s | `MQ01015_b_EN` printed/PDF pp. 1-2 |
| `C=0 / C=1` | zero crossing / disabled; clean-contact use without neutral in `C=1` | `MQ01015_b_EN` printed/PDF pp. 1-2 |
| `Groups` | physical G1/G2 `0..9`; virtual ten groups `0..255` | `MQ01015_b_EN` printed/PDF pp. 1-2 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `669` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `669` | `A` | `0..9` | `0` | Area |
| `669` | `PL` | `0..9` | `0` | Lighting point (0-9) |
| `669` | `M` | `0..4`; `11` = `SLA`; `15` = PLU | `0` | Mode (0-4, sla, plu) |
| `669` | `G1` | `0..255` | `0` | Group 1 |
| `669` | `G2` | `0..255` | `0` | Group 2 |
| `669` | `C` | `0..1` | `0` | Zero crossing - Dry contact |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `6` - Light actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality |
| `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
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

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `669` | `1` | `6` | `4147` | No textual predicate stored | `1` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `669` | `6` | `2375` | `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `669` | `6` | `2376` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `669` | `6` | `2377` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `669` | `6` | `2378` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `1` | `M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `1` |
| `1` | `M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `1` |
| `1` | `M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `1` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `79` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `6` - Light actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system/model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Physical A/PL addressing uses `1..9`; Suite uses room `0..10` and lighting point 0..15. Physical group G uses `0..9`; Suite provides ten group fields 0..255. Master `M=0`, slave `M=SLA` and monostable master `M=PUL` are documented; `PUL` ignores room/general controls. Delayed slave `OFF` uses `M=1..4` minutes physically or `0..255` seconds in Suite, for point-to-point control only: the master switches off immediately, its slave after the delay. Slave `PUL` requires software. The stated load capacities require zero crossing and neutral connected; without them relay bonding may occur. The sheet’s 250 Vac column retains 2300 W/920 W values as printed rather than recalculating power. The local press switches the load. Suite exposes contact state at power recovery and additional role/local-button options. MyHOME Server automatically configures 1 channel(s). `C=0` selects zero crossing and the LED flashes if L/N is not connected. `C=1` disables zero crossing; without neutral, the relay may be used as a clean contact. The source specifies at least 3 m load connection.

Apply the firmware-specific restrictions above. The generic session/validation method remains in [Programming](../../programming/).

The historical guide pp. 66/79 limits `F411U1` to10 LED lamps at500 W and10 compact fluorescent lamps at500 W; its4 A/920 W linear fluorescent and4 A/920VA ferromagnetic entries have different load scopes. Use the actual connected load class and applicable source revision, rather than the largest headline current.

## Source reconciliation

Exact reference and Legrand alias are established by the database and shared manufacturer heading. The exact `F411U1`/003847 sheet establishes one channel; `F411U2`’s motor interlock and two-output roles are not transferred. Its group table describes G1/G2 fields even though the simplified addressing illustration names only A/PL/M; retain the sheet and database domains independently. The 2026 EOS list uses a 16 A product label for these references, while the exact sheets describe 10 A and load-specific lower capacities. That label is not authority to raise every load rating.

### Reviewed source boundaries

The catalogue stores a lighting Object and no Virgin Object for this item. The physical sheet’s `A/PL=1..9` range and reusable/software ranges have different scopes. Catalogue text refers to `PLU`, while the conversion uses `PUL` and emits an `O/I` symbol outside the stored input domain; those irregularities remain explicit rather than being silently normalised. The adjacent two-channel motor application is not transferred to this single-channel device.

### Retained source accounting

| Original | Examined role / remaining scope |
| --- | --- |
| `F411U1-italian-product-sheet.pdf` | Complete exact-reference commercial export and all classification attributes examined; EAN only where explicitly retained. Source-specific ratings do not replace technical-sheet scopes |
| `MQ01015_b_IT.pdf` | PDF pp. 1–2: complete exact `F411U1`/003847 load and configuration sheet |
| `MQ01015_b_EN.pdf` | PDF pp. 1–2: complete exact `F411U1`/003847 load and configuration sheet |
| `ST-00002703-EN.pdf` | PDF p. 9: exact actuator/server ecosystem compatibility inspected; other product functions not transferred |
| `HRM_SCS_Guide_AD_EXOD18SAG_GB.pdf` | PDF pp. 30,66,79 examined for exact `F411U1`/`F411U2` load tables and actuator/wiring scope; other product chapters not reviewed |

## Evidence limits and open work

Production-specific rating/IK discrepancies, zero-crossing and restoration behavior, load compatibility and diagnostic responses remain uncorroborated.

No installed hardware revision or microcontroller fingerprint is retained for this cluster. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Canonical catalogue extraction and reconciliation are complete within the retained evidence scope. Unexamined documentation, source conflicts and runtime corroboration remain explicit limits of this review.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0151-0160-2026-10-07.md#own-dev-0154)
