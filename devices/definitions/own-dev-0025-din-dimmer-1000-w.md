# DIN dimmer 1000 W

## Summary

This single-output DIN dimmer regulates documented resistive loads and ferromagnetic transformers. A short local button press switches the load and a sustained press adjusts brightness; its service features include a replaceable fuse and load-fault reporting.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0025` | Project identity |
| Technical description | One-channel DIN SCS dimmer for resistive and ferromagnetic-transformer loads | Catalogue + official technical sheet |
| Commercial identities | `F414`, `003652` | Catalogue |
| Catalogue item | `17` - “DIN dimmer 1000 W” | Canonical manufacturer catalogue |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Canonical manufacturer catalogue |
| Item model / `modobj` | `133` | Canonical manufacturer catalogue |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `176` | Canonical manufacturer catalogue |
| Declared Modules | `1` | Canonical manufacturer catalogue |
| Categories | Actuator, Dimmer, Lighting | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F414` | Established identity | Canonical catalogue; canonical commercial record `17`; Commercial identity of this Technical Device |
| Legrand | `003652` | Established identity | Canonical catalogue; canonical commercial record `1601`; Commercial identity of this Technical Device |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00278_e_EN` | Technical sheet | 20 September 2018 | All two pages; F414 only; sibling variants distinguished | [Archived PDF](https://archive.openwebnet-ha.org/sha256/d6/ca/d6cafa21923a3de3dfe1cbb42895617134892c56ae2edda866c2e7fff2c54273.pdf) | [Publisher PDF](https://dar.bticino.com/asset/Documents/MQ00278_e_EN.pdf) |
| `AUTOMATISME.pdf` | MyHOME automation guide | October 2006 publisher guide | F414 configuration: printed p. 123 / PDF p. 125; technical characteristics printed p. 164 / PDF p. 166 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |
| `ST-00002122-EN.pdf` | Classe 300EOS compatibility matrix | 21 October 2024 | Only applicable production/compatibility rows, p.7 and physical-configuration exclusion, p.8 | [Archived original](https://archive.openwebnet-ha.org/sha256/e1/a8/e1a8da77199296d9f56ea708402f144b8614473558002c0f8db4ee16eb2f0d0d.pdf) | Publisher URL not retained in manifest |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 4 DIN modules | `MQ00278_e_EN` |
| Outputs | 1 dimmed output | `MQ00278_e_EN` |
| Load families | resistive loads and ferromagnetic transformers | `MQ00278_e_EN` |
| SCS nominal supply | `27 Vdc` | `MQ00278_e_EN` |
| SCS operating range | `18..27 Vdc` | `MQ00278_e_EN` |
| Current draw | `9 mA` | `MQ00278_e_EN` |
| Published load current range | `0.25..4.3 A` at `230 Vac`, `50 Hz` | `MQ00278_e_EN` |
| Published load power range | `60..1000 VA` | `MQ00278_e_EN` |
| Local operation | short press switches; long press regulates brightness | `MQ00278_e_EN` |
| Protection / service | replaceable fuse; load-fault reporting including lamp failure | `MQ00278_e_EN` |

| Setting / property | Source-scoped value or behavior | Evidence |
| --- | --- | --- |
| Mains / temperature | F414: `230 Vac`, `50 Hz`; `−5..+45 °C`; max-load dissipation `10 W`. F414/127’s `110 Vac` range is not this cluster. | MQ00278_e_EN p. 1 |
| Fuse / IP/IK wording | T5H250V shown in F414 illustration; sheet prints Protection index IK04 and Impact resistance IP20 with reversed conventional headings, retained as a source labelling irregularity. | MQ00278_e_EN p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `17` | Canonical catalogue |
| Technical item description | DIN dimmer 1000 W | Canonical catalogue |
| Item family | `4` - Dimmer | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `133` | `AS_ITEM_SYSTEM` |
| Commercial records | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `133` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Canonical commercial record metadata

| Reference / record | Catalogue name / source description | Visibility / type | Dependent / gateway | Evidence |
| --- | --- | --- | --- | --- |
| `F414` / `17` | DIN dimmer 1000 W; `BTicino_Undefined_DIN dimmer 1000 W` | `1` / Empty | `0` / `0` | Canonical manufacturer catalogue |
| `003652` / `1601` | DIN dimmer 1000 W; no source description | `1` / Empty | `0` / `0` | Canonical manufacturer catalogue |

Visibility, dependency and gateway flags describe the catalogue record, not the installed Device state.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `176` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Firmware `176` is wildcard `-1.-1.-1` and declares one Module. Current F460/F461 compatibility documentation maps Legrand `003652` from production batch `09W50` and BTicino `F414` from `09W29`; MyHOME_Up documentation independently gives F414 `09W29`.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `176` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `608` | `8` | `422` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

One fixed Object `8`, Dimmer actuator, occupies slot `1`. There is no Virgin Object.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `176` | Physical configuration | `0` | Canonical firmware/mode association |
| `176` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `176` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `176` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `176` | `A` | `0..9` | `0` | A; Environment |
| `176` | `PL` | `0..9` | `0` | PL; Light Point |
| `176` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (0-4, Pul, Sla) |
| `176` | `G1` | `0..9` | `0` | `G1`; `G1` - (0-9) |

These are F414 device configurators. Advanced dimmer characteristics such as load type and minimum level belong to the reusable Dimmer Object and are shown separately.

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

### Device-specific interpretation

Rule 3 converts physical `M=1..4` to DELAYED_OFF 60/120/180/240 seconds. The filter notes say timing functionality absent while retaining full hour/minute/second domains. Shared TYPE_LOAD includes DALI/DSI and TYPE_STANDARD includes `0..10`V; these do not establish those electrical outputs on F414.

The reusable `MIN_LEVEL_ADV` domain is `1..100` but its stored default is `0`. No corrected default is supplied; retain this source inconsistency without treating `0` as a permitted configured value.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `176` | `1` | `8` | `4149` | No textual predicate stored | `3` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `176` | `8` | `403` | `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Funzionalità di pulsante locale ridotta (Local button mode) |
| `176` | `8` | `404` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Funzionalità di temporizzazione non presente (Hours) |
| `176` | `8` | `405` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Funzionalità di temporizzazione non presente (Minutes) |
| `176` | `8` | `406` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Funzionalità di temporizzazione non presente (Seconds) |
| `176` | `8` | `407` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge (entire reusable range retained) | `0` | TYPE_LOAD |
| `176` | `8` | `408` | `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard (entire reusable range retained) | `0` | Definizione range voltaggio utile |
| `176` | `8` | `409` | `MIN_LEVEL_ADV` | `1..100` (entire reusable range retained) | `0` | Minimum level advanced |
| `176` | `8` | `410` | `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable (entire reusable range retained) | `0` | enable disable minimum level |
| `176` | `8` | `2172` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

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
| `DIMENSION 1` | resolve `modobj = 133` and the `F414` / `003652` family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | record installed firmware rather than assuming wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm the single Dimmer Object | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the configured dimmer address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `A`, `PL`, `M`, `G1` and the Device-specific load/minimum-level settings | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The Device participates in [`WHO 1` - Lighting](../../functional/who-1-lighting/) as a dimmer actuator.

## Observed behavior and corroboration

No raw F414/MH200 DIM4 trace is retained; the tester report remains unresolved evidence.

## Programming

Preserve inductive/resistive load constraints and distinguish F414 from capacitive/electronic-transformer variants such as F415.

| Setting / property | Source-scoped value or behavior | Evidence |
| --- | --- | --- |
| Physical / Suite address | Physical `A/PL=1..9` and `G=0..9`; Suite room `0..10`/point `0..15` with ten groups `0..255`. | MQ00278_e_EN p. 2 |
| Modes / delay | `M=0` Master, SLA Slave, PUL monostable ignores Room/General; `M=1..4` delays same-address Slave OFF`1..4` min after Master OFF. Point-to-point only; Suite `0..255` s. Slave PUL and minimum startup brightness use Suite. | MQ00278_e_EN p. 2 |

## Source reconciliation

The complete 20 September 2018 MQ00278 sheet was examined. F414 controls resistive/ferromagnetic loads; F415 controls electronic transformers and has different current draw. The sheet’s headline 1×4A differs from its load table `0.25..4`.3A /`60..1000` VA at `230 Vac`, `50 Hz`; both are source quantities rather than universally interchangeable ratings. The 2006 guide gives 11 W at 1000 W and 5 W at 500 W (printed p.160 /PDF p.162), versus 2018 max-load 10 W. Historical configuration and T5H250V wiring (printed pp.123, 164 /PDF pp.125, 166) were reconciled. No hardware boundary for the dissipation difference is supplied. Runtime DIM4 behavior through MH200 is not established by these product sources.

The retained Classe 300EOS compatibility matrix lists F414 from 09W29; 003652 from 09W50. Its p.8 excludes Devices using physical configurators. These are Classe 300EOS compatibility boundaries, not universal hardware revisions or guaranteed firmware versions.

## Evidence limits and open work

- Preserve a raw F414/MH200 DIM4 request/timeout/`NACK` exchange.
- Hardware-corroborate `modobj`, firmware, address and configurator count.
- Archive historical sheet revisions when they materially change load/fuse data.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [MQ00278_e_EN](https://archive.openwebnet-ha.org/sha256/d6/ca/d6cafa21923a3de3dfe1cbb42895617134892c56ae2edda866c2e7fff2c54273.pdf)
- [AUTOMATISME.pdf](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0021-0030-2026-10-06.md#own-dev-0025)
