# Two-channel normally closed relay actuator

## Summary

This DIN-rail actuator switches two independent lighting loads through normally closed relays. Its distinctive behavior is that loss of SCS bus power leaves the contacts closed, keeping the loads on. It has a local button and status LED for each channel.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0141` | Project identity |
| Technical description | Two-channel normally closed relay actuator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `003843`, `F411/2NC` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1596` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `140` | Main association; independent of project ID |
| Firmware definition | `173` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `2` | Firmware metadata |
| Categories | Actuators | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `003843` | Established catalogue identity | Manufacturer database commercial record `1704` explicitly links this SKU to item `1596` |
| BTicino | `F411/2NC` | Established catalogue identity | Manufacturer database commercial record `1596` explicitly links this SKU to item `1596` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `F411-2NC-italian-product-sheet.pdf` | Exact Italian product export | `Captured 05/10/2026; compliance-template date does not establish product publication date` | PDF pp. 1-1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/a3/db/a3dbc68476037873e8a4a76662b70fc4f20b035a613dac04d5e16f9c9644f44e.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F411_2NC) |
| `MQ00191_d_EN.pdf` | Exact-product manufacturer original | `MQ00191_d_EN; 30/04/2014` | PDF pp. 1-1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/75/d2/75d2f02b31ac6ef73a477f0f0ba9731ae4a1e8f8532f8dee66159d718f9a4106.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MQ00191_d_EN.pdf) |
| `MQ00191_d_IT.pdf` | Exact-product manufacturer original | `MQ00191_d_IT; 30/04/2014` | PDF pp. 1-1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/61/2d/612da6f156a3cb85aa02d0d7488935c144e3015ca57c4d4b8605896a191ff9fb.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MQ00191_d_IT.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1596`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS nominal / operating supply | `27 Vdc / 18..27 Vdc` | `MQ00191_d_EN` printed/PDF p. 1 |
| Current draw | `28 mA` | `MQ00191_d_EN` printed/PDF p. 1 |
| Temperature | `0..40 °C` | `MQ00191_d_EN` printed/PDF p. 1 |
| Mounting | `2 DIN modules` | `MQ00191_d_EN` printed/PDF p. 1 |
| Incandescent / halogen, 230 Vac | `1380 W / 6 A` | `MQ00191_d_EN` printed/PDF p. 1 |
| Linear fluorescent / electronic transformer | `150 W / 0.65 A` | `MQ00191_d_EN` printed/PDF p. 1 |
| Ferromagnetic transformer | `230 VA / 1 A; cos phi 0.5` | `MQ00191_d_EN` printed/PDF p. 1 |
| Outputs | `two independent NC relay contacts` | `MQ00191_d_EN` printed/PDF p. 1 |
| Bus-power loss | `closed contacts / loads ON` | `MQ00191_d_EN` printed/PDF p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1596` | Canonical catalogue |
| Technical item description | 2 relays DIN NC actuator 10 A | Canonical catalogue |
| Item family | 0; key `2` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `140` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `173` | `-1` | `-1` | `-1` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `173` | `1` | `6` Light actuator | Fixed/designated metadata | `604` | `6` | `419` |
| `173` | `2` | `6` Light actuator | Fixed/designated metadata | `605` | `6` | `419` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `173` | Virtual Configuration | `1` | Association key `1` |
| `173` | Advanced Configuration | `2` | Association key `2` |
| `173` | Physical configuration | `0` | Association key `3` |


No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `M=PUL` | `ON` monostable; ignores room/general | `MQ00191_d_EN` printed/PDF p. 1 |
| `M=SLA` | slave of same-address master | `MQ00191_d_EN` printed/PDF p. 1 |
| `M=1,2,3,4` | corresponding slave `OFF` after 1,2,3,4 minutes; point-to-point only | `MQ00191_d_EN` printed/PDF p. 1 |
| `Interlocked motor role` | excluded by exact NC sheet | `MQ00191_d_EN` printed/PDF p. 1 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `173` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `173` | `A` | `0..9` | `0` | A; Enviroment |
| `173` | `PL1` | `0..9` | `0` | PL1; PL1 - (0-9) |
| `173` | `PL2` | `0..9` | `0` | PL2; PL2 - (0-9) |
| `173` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |
| `173` | `M` | `0..4`; `15` = `PUL` | `0` | M; Mode (0-4, Pul) |

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
| `173` | `1` | `6` | `4147` | No textual predicate stored | `1` |
| `173` | `2` | `6` | `4147` | No textual predicate stored | `1` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `173` | `6` | `389` | `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open (entire reusable range retained) | `0` | Relay state on device reset |
| `173` | `6` | `390` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `173` | `6` | `391` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `173` | `6` | `392` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `173` | `6` | `1865` | `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing (entire reusable range retained) | `0` | Load_control_mode |
| `173` | `6` | `2476` | `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |

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
| `DIMENSION 1` | Corroborate item model `140` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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

Use the NC contact arrangement shown in the sheet. `ON` closes the contacts and lights the corresponding LED; `OFF` opens the contacts. The sheet excludes functions requiring interlocked relays, so do not use this model as a shutter motor interlock. `M=PUL` ignores room/general commands; `M=SLA` follows a master with the same address; `M=1..4` delays the corresponding slave `OFF` by `1..4` minutes for point-to-point operation. Local pushbuttons act on their respective loads. Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session/validation method remains in [Programming](../../programming/).

## Source reconciliation

The database calls this item a 10 A actuator, while the exact 2014 sheet gives 6 A incandescent and smaller load-specific ratings. The Italian product export also says 10A. These source labels do not establish that the retained sheet’s 6 A limit can be replaced by 10 A for all production revisions or load types. F411/2NC and 003843 identities are established by explicit database links; the 2014 table remains independently scoped.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `F411-2NC-italian-product-sheet.pdf` | Exact named commercial/product export; values and descriptive defects reconciled against technical documents. Compliance-template dates do not date the product. |
| `MQ00191_d_EN.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |
| `MQ00191_d_IT.pdf` | Exact-product or explicitly shared manufacturer material; technical/procedural facts, source revision and remaining variant limits are reconciled above. Manual sections outside the stated scope remain available in the retained original. |

## Evidence limits and open work

The production revision behind the differing 10 A label, modern LED/CFL ratings, and bus-loss behavior on actual hardware remain uncorroborated.

No installed hardware revision or microcontroller fingerprint is retained for this cluster. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Canonical catalogue extraction and reconciliation are complete for the retained evidence; further documentation discovery, runtime corroboration and final evidence closure remain partial.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
