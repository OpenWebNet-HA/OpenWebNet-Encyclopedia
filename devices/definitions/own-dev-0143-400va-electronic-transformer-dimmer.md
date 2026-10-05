# 400 VA electronic-transformer dimmer

## Summary

F415 is a DIN-rail dimmer for low-voltage lamps supplied through electronic transformers. It controls one 60–400 VA load and provides local switching and brightness adjustment. Its load class and capacity differ from the F414 that shares its technical sheet.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0143` | Project identity |
| Technical description | 400 VA electronic-transformer dimmer | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `003653`, `F415` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1599` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `135` | Main association; independent of project ID |
| Firmware definition | `181` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Actuators | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `003653` | Established catalogue identity | Manufacturer database commercial record `1600` explicitly links this SKU to item `1599` |
| BTicino | `F415` | Established catalogue identity | Manufacturer database commercial record `1599` explicitly links this SKU to item `1599` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `F415-italian-product-sheet.pdf` | Exact Italian product export | `Captured 05/10/2026; compliance-template date does not establish product publication date` | PDF pp. 1-1: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/c6/73/c6737bb7d64dac9864e183183e56a756eada757e6f7e89b0db39678db86fb109.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-F415) |
| `MQ00278_e_IT.pdf` | Legacy manufacturer technical documentation | `MQ00278_e_IT; 20/09/2018` | Shared F414/F415 exact-product sheet, PDF pp. 1-2: use F415-specific values. The 1000VA heading applies to F414, not the separately tabulated 400VA F415. | [Archived original](https://archive.openwebnet-ha.org/sha256/fc/29/fc296454ad251c4f28cb3c71452fff97e9a7f4e8a0fd2d100e5a4bf922fddf95.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/MQ00278_e_IT.pdf) |
| `MQ00278_e_EN.pdf` | English counterpart of manufacturer-linked document | `MQ00278_e_EN; 20/09/2018` | Shared F414/F415 exact-product sheet, PDF pp. 1-2: use F415-specific values. The 1000VA heading applies to F414, not the separately tabulated 400VA F415. | [Archived original](https://archive.openwebnet-ha.org/sha256/d6/ca/d6cafa21923a3de3dfe1cbb42895617134892c56ae2edda866c2e7fff2c54273.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MQ00278_e_EN.pdf) |
| `AUTOMATISME.pdf` | Exact manufacturer documentation | `AUTOMATISME; printed publication date not established` | F415: physical configuration printed p. 123 / PDF p. 125; load table printed p. 158 / PDF p. 160; technical data/wiring printed p. 164 / PDF p. 166. Historical edition; not a current compatibility guarantee. | [Archived original](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |
| `ST-00002703-EN.pdf` | Technical Sheet ST-00002703-EN | `ST-00002703-EN; 16/06/2026` | Retained 19-page original; exact-product technical, configuration and operating sections reviewed where applicable. Source-specific facts and remaining limits are scoped in the dossier; this does not claim a line-by-line review of every manual page. | [Archived original](https://archive.openwebnet-ha.org/sha256/b2/f5/b2f5090b601e33cdef9ba666108848ff4d9800792ccd5b7c14385da300bf0ffa.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002703-EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1599`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS nominal / operating supply | `27 Vdc / 18..27 Vdc` | `MQ00278_e_EN` printed/PDF pp. 1-2; `AUTOMATISME` printed pp. 123,158,164 / PDF pp. 125,160,166 |
| 2018 current draw | `22 mA; older historical catalogue says 9 mA` | `MQ00278_e_EN` printed/PDF pp. 1-2; `AUTOMATISME` printed pp. 123,158,164 / PDF pp. 125,160,166 |
| Electronic-transformer load | `230 Vac, 50 Hz; 60..400 VA; 0.25..1.7 A` | `MQ00278_e_EN` printed/PDF pp. 1-2; `AUTOMATISME` printed pp. 123,158,164 / PDF pp. 125,160,166 |
| Temperature / size | `-5..45 °C; 4 DIN modules` | `MQ00278_e_EN` printed/PDF pp. 1-2; `AUTOMATISME` printed pp. 123,158,164 / PDF pp. 125,160,166 |
| Maximum dissipation | `11 W` | `MQ00278_e_EN` printed/PDF pp. 1-2; `AUTOMATISME` printed pp. 123,158,164 / PDF pp. 125,160,166 |
| Outputs | `one dimmed output` | `MQ00278_e_EN` printed/PDF pp. 1-2; `AUTOMATISME` printed pp. 123,158,164 / PDF pp. 125,160,166 |
| Protection codes | `IP20 / IK04; sheet property labels reversed` | `MQ00278_e_EN` printed/PDF pp. 1-2; `AUTOMATISME` printed pp. 123,158,164 / PDF pp. 125,160,166 |
| Historical fuse marking | `T2.5H 250 V in F415 wiring drawing; F414 T5H marking is separate` | `MQ00278_e_EN` printed/PDF pp. 1-2; `AUTOMATISME` printed pp. 123,158,164 / PDF pp. 125,160,166 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1599` | Canonical catalogue |
| Technical item description | DIN dimmer 400 VA | Canonical catalogue |
| Item family | 0; key `4` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `135` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `181` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `181` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `620` | `8` | `426` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `181` | Virtual Configuration | `1` | Association key `1` |
| `181` | Advanced Configuration | `2` | Association key `2` |
| `181` | Physical configuration | `0` | Association key `3` |


No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `A / PL / G` | physical `1..9` / `1..9` / `0..9`; virtual room `0..10`, point `0..15`, ten groups `0..255` | `MQ00278_e_EN` printed/PDF pp. 1-2; `AUTOMATISME` printed pp. 123,158,164 / PDF pp. 125,160,166 |
| `M=0 / SLA / PUL` | master / slave / monostable master | `MQ00278_e_EN` printed/PDF pp. 1-2; `AUTOMATISME` printed pp. 123,158,164 / PDF pp. 125,160,166 |
| `M=1..4` | slave `OFF` delay `1..4` min; virtual `0..255` s | `MQ00278_e_EN` printed/PDF pp. 1-2; `AUTOMATISME` printed pp. 123,158,164 / PDF pp. 125,160,166 |
| `Virtual-only options` | slave `PUL`; minimum power-on brightness | `MQ00278_e_EN` printed/PDF pp. 1-2; `AUTOMATISME` printed pp. 123,158,164 / PDF pp. 125,160,166 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `181` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `181` | `A` | `0..9` | `0` | A; Enviroment |
| `181` | `PL` | `0..9` | `0` | PL; Light Point |
| `181` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (0-4, Pul, Sla) |
| `181` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `8` - Dimmer actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality; mode (M,S + PULL) |
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
| `181` | `1` | `8` | `4149` | No textual predicate stored | `3` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `181` | `8` | `499` | `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Funzionalità di pulsante locale ridotta (Local button mode) |
| `181` | `8` | `500` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Funzionalità di temporizzazione non presente (Hours) |
| `181` | `8` | `501` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Funzionalità di temporizzazione non presente (Minutes) |
| `181` | `8` | `502` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Funzionalità di temporizzazione non presente (Seconds) |
| `181` | `8` | `503` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge (entire reusable range retained) | `0` | TYPE_LOAD |
| `181` | `8` | `504` | `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard (entire reusable range retained) | `0` | Definizione range voltaggio utile |
| `181` | `8` | `505` | `MIN_LEVEL_ADV` | `1..100` (entire reusable range retained) | `0` | Minimum level advanced |
| `181` | `8` | `506` | `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable (entire reusable range retained) | `0` | enable disable minimum level |
| `181` | `8` | `2176` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `3` | `M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `3` |
| `3` | `M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `3` |
| `3` | `M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `3` |
| `3` | `M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `3` |
| `3` | `M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `3` |
| `3` | `M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `3` |
| `3` | `M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `3` |
| `3` | `M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `3` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `135` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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


These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system/model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Physical A/PL addressing uses `1..9`; Suite uses room `0..10` and lighting point 0..15. Physical group G uses `0..9`; Suite provides ten group fields 0..255. Master `M=0`, slave `M=SLA` and monostable master `M=PUL` are documented; `PUL` ignores room/general controls. Delayed slave `OFF` uses `M=1..4` minutes physically or `0..255` seconds in Suite, for point-to-point control only: the master switches off immediately, its slave after the delay. Slave `PUL` requires software. Short local presses switch the load; holding adjusts brightness. Suite provides minimum brightness at power-on and slave `PUL`. The sheet says MyHOME Server automatically configures one channel. The historical diagram distinguishes F415’s electronic-transformer connection and fuse from F414’s resistive/ferromagnetic arrangement. The actuator reports load faults such as lamp failure and has a replaceable fuse; use the actual production instructions when servicing. The later EOS compatibility table qualifies F415 from 09W22 and 003653 from 10W07 and excludes physical-configurator devices in that system.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session/validation method remains in [Programming](../../programming/).

## Source reconciliation

MQ00278_e explicitly covers F414, F414/127, F415 and F415/127 despite its broad “1000VA” heading. F415’s separate 400 VA/230 V table applies here; neither F414’s 1000 VA nor F415/127’s 110 V ratings are transferred. The 2018 sheet gives 22 mA, whereas the historical catalogue and Italian export give 9 mA; no production boundary resolving that difference is established. The Italian compressed description “60400VA” is reconciled with its own 400VA field and the technical sheet’s `60..400`VA interval. Printed IP/IK property labels are reversed.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `F415-italian-product-sheet.pdf` | Exact named commercial/product export; values and descriptive defects reconciled against technical documents. Compliance-template dates do not date the product. |
| `MQ00278_e_IT.pdf` | Shared F414/F415 sheet; F415-specific load, current and configuration rows apply. The shared 1000VA heading does not raise F415 capacity. |
| `MQ00278_e_EN.pdf` | Shared F414/F415 sheet; F415-specific load, current and configuration rows apply. The shared 1000VA heading does not raise F415 capacity. |
| `AUTOMATISME.pdf` | Historical F415 configuration, load table and wiring at printed pp. 123,158,164 / PDF pp. 125,160,166; 9 mA differs from the later sheet’s 22 mA. |
| `ST-00002703-EN.pdf` | Explicit compatibility/reference inventory and ecosystem restrictions for this product; EOS electrical/display specifications are not transferred. |

## Evidence limits and open work

The current-draw revision boundary, exact fuse requirements of installed units, transformer compatibility and hardware diagnostics remain uncorroborated.

No installed hardware revision or microcontroller fingerprint is retained for this cluster. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Canonical catalogue extraction and reconciliation are complete for the retained evidence; further documentation discovery, runtime corroboration and final evidence closure remain partial.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
