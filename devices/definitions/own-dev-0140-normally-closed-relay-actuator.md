# Normally closed relay actuator

## Summary

This DIN SCS actuator switches a load through a normally closed, two-way relay. Its distinctive bus-loss behaviour keeps the contact closed and the load on, with a local button and configured group assignments providing additional control.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0140` | Project identity |
| Technical description | Normally closed relay actuator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `F411/1NC`, `003845` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1593` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `139` | Main association; independent of project ID |
| Firmware definition | `170` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Actuators | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F411/1NC` | Established catalogue identity | Manufacturer database commercial record `1593` explicitly links this SKU to item `1593` |
| Legrand | `003845` | Established catalogue identity | Manufacturer database commercial record `1705` explicitly links this SKU to item `1593` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00190_e_EN.pdf` | Exact manufacturer documentation | `MQ00190_e_EN; 07/06/2014` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-2; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/82/c0/82c0464ab612fc3c8c1a118cfb7cb3e772eb90eacd9a19677bb3cb1724f54b7a.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MQ00190_e_EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `1593` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS nominal / operating supply | `27 Vdc / 18..27 Vdc` | `MQ00190-e-EN` printed/PDF pp. 1-2 |
| Current draw | `22 mA` | `MQ00190-e-EN` printed/PDF pp. 1-2 |
| Operating temperature | `5..35 °C` | `MQ00190-e-EN` printed/PDF pp. 1-2 |
| Mounting | `2 DIN modules` | `MQ00190-e-EN` printed/PDF pp. 1-2 |
| Relay | `one two-way normally closed relay; local control button` | `MQ00190-e-EN` printed/PDF pp. 1-2 |
| Incandescent / halogen | `10 A / 2300 W` | `MQ00190-e-EN` printed/PDF pp. 1-2 |
| LED / CFL | `500 W; maximum 10 lamps` | `MQ00190-e-EN` printed/PDF pp. 1-2 |
| Linear fluorescent / electronic transformer | `4 A / 920 W` | `MQ00190-e-EN` printed/PDF pp. 1-2 |
| Ferromagnetic transformer | `4 A; cos phi 0.5 / 920 VA` | `MQ00190-e-EN` printed/PDF pp. 1-2 |
| Group sockets | `G1, G2, G3; three physical group assignments` | `MQ00190-e-EN` printed/PDF pp. 1-2 |
| Bus-loss state | `contact remains closed; load ON` | `MQ00190-e-EN` printed/PDF pp. 1-2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1593` | Canonical catalogue |
| Technical item description | 1 relay DIN NC actuator 16 A | Canonical catalogue |
| Item family | 0; key `2` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `139` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `170` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `170` | `1` | `6` Light actuator | Fixed/designated metadata | `601` | `6` | `416` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `170` | Virtual Configuration | `1` | Association key `1` |
| `170` | Advanced Configuration | `2` | Association key `2` |
| `170` | Physical configuration | `0` | Association key `3` |


No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

### Published physical actuator modes



| Function | Physical selector | Published virtual scope |
| --- | --- | --- |
| Master | `M=0` | master role |
| Slave | `M=SLA` | follows matching addressed master |
| Master pushbutton | `M=PUL` | ignores room/general controls |
| Delayed slave `OFF` | `M=1..4:1..4 min` | `0..255 s; point-to-point only` |
| Slave `PUL` | no listed physical selector | software configuration required |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `170` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `170` | `A` | `0..9` | `0` | A; Enviroment |
| `170` | `PL` | `0..9` | `0` | PL; Light Point |
| `170` | `M` | `0..4`; `15` = `PUL` | `0` | M; Mode (0-4, Pul) |
| `170` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |
| `170` | `G2` | `0..9` | `0` | G2; G2 - (0-9) |
| `170` | `G3` | `0..9` | `0` | G3; G3 - (0-9) |

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
| `170` | `1` | `6` | `4147` | No textual predicate stored | `1` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `170` | `6` | `377` | `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open (entire reusable range retained) | `0` | Per energy management (State on Reset) |
| `170` | `6` | `378` | `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `170` | `6` | `379` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `170` | `6` | `380` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `170` | `6` | `381` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `170` | `6` | `382` | `SUBTYPE` | `11` = Actuator; `1` = Lamp; `10` = Valve; `15` = Differential restart; `6` = Fan; `7` = Watering; `8` = Controlled socket; `9` = Lock (entire reusable range retained) | `11` | Type of loads |
| `170` | `6` | `1862` | `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing (entire reusable range retained) | `0` | Load_control_mode |

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

No conversion reference is attached to these slot rows. Resolve the active Object and apply its firmware-specific domain restrictions separately. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `139` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `6` - Light actuator | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |


These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The normally closed relay inverts the F411/1N control logic: switching-on closes the contact/LED `ON`, `OFF` opens it/LED `OFF`; losing bus power preserves the closed `ON` path. Use the actual NC wiring and load type; do not assume the ordinary actuator’s power-loss state. Physical A/PL plus up to three G selectors and M provide master, slave, `PUL` and `1..4`-minute delayed-slave modes; Suite exposes ten group fields, `0..255`-second delay and slave `PUL`. The timing applies to the corresponding slave and only point-to-point control.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

## Source reconciliation

F411/1NC/003845 are explicit catalogue identities. The e-sheet heading calls the actuator 10 A, matching incandescent rating, whereas the catalogue/current manufacturer listing calls it 16 A for resistive loads. This is load-class naming, not sufficient evidence to apply 16 A to every load type; the sheet’s load-specific table is preserved. The currently listed older d-UK original URL returned 403 and remains unavailable; e is the retained revision. IP20/IK04 labels are swapped in the printed sheet just as in other historical sheets, without changing the code meanings. Manufacturer listings also expose classification counts/powers that are not an extra independently wired relay.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `MQ00190_e_EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |

## Evidence limits and open work

The older d-UK revision, exact Legrand manual, verified resistive-contact rating by production revision, NC bus-loss behavior and diagnostics remain uncorroborated.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
