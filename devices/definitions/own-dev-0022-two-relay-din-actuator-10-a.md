# Two-relay DIN actuator 10 A

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0022` | Project identity |
| Technical description | Two-independent-relay DIN actuator for lighting, automation and paired motor loads | Catalogue + official documentation |
| Commercial identities | `F411/2`, `003842` | Catalogue |
| Catalogue item | `2` - “2 relays DIN actuator 10 A” | Implementation evidence |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `129` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `132` | Implementation evidence |
| Declared Modules | `2` | Implementation evidence |
| Categories | Actuator, Lighting, Automation, Shutter | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino | `F411/2` | Established identity | canonical commercial record `2`; Commercial identity of this Technical Device | Canonical catalogue |
| Legrand | `003842` | Established identity | canonical commercial record `1708`; Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `AUTOMATISME.pdf` | MyHOME automation guide | historical publisher guide | F411/2 configuration: printed p. 121 / PDF p. 123; load/specification tables: printed pp. 157-160 / PDF pp. 159-162 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |
| BTicino `F411/2` product record | Current product record | current | whole product page | - | [Publisher page](https://www.bticino.com/products/bt-f411-2) |

For the multi-product guide, the printed and 1-based PDF page locators remain unresolved and are retained explicitly as an evidence gap.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 DIN modules | Current BTicino product record |
| Outputs | 2 relay contacts | Current BTicino product record |
| Local interface | manual controls with LED indication | Current BTicino product record |
| SCS nominal supply | `27 Vdc` | Current BTicino product record |
| SCS operating range | `18..27 Vdc` | Current BTicino product record |
| Current draw | `28 mA` | Current BTicino product record |
| Maximum switching power | `1380 W` | Current BTicino product record |
| Resistive load | `10 A` | Current BTicino product text |
| Filament load | `6 A` | Current BTicino product text |
| Motor reducers | `500 W` | Current BTicino product text |
| Ferromagnetic transformer | `2 A`, cos φ `0.5` | Current BTicino product text |
| Fluorescent load | `250 W` | Current BTicino product text |
| Paired motor/shutter use | relay pair can be logically interlocked | Publisher automation documentation |

Historical guides publish lower limits for some load classes; those values remain revision-scoped rather than being silently normalized to the current product record.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2` | Canonical catalogue |
| Technical item description | 2 relays DIN actuator 10 A | Canonical catalogue |
| Item family | `2` - Actuator | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `129` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `132` | `-1` | `-1` | `-1` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Firmware `132` is wildcard `-1.-1.-1` and declares two Modules.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `132` | `1` | `6` Light actuator | Fixed/designated metadata | `275` | `6` | `275` |
| `132` | `1` | `7` Automation actuator | Candidate alternative | `274` | `7` | `274` |
| `132` | `2` | `6` Light actuator | Fixed/designated metadata | `276` | `6` | `275` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `132` | `510` Automation relay virgin | `1`, `2` | `1`, `6`, `7` | `510` | `5` |

Slots `1` and `2` default to Object `6`, Light actuator. Slot `1` also has Object `7`, Automation actuator, as a candidate. Virgin Object `510`, Automation relay virgin, applies to both slots and permits Object `1` Blind actuator, Object `6` Light actuator and Object `7` Automation actuator.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `132` | `1` | `1` | Virtual Configuration |
| `132` | `2` | `2` | Advanced Configuration |
| `132` | `3` | `0` | Physical configuration |

Physical configuration, Virtual Configuration and Advanced Configuration.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `132` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `132` | `A` | `0..9` | `0` | A; Environment |
| `132` | `PL1` | `0..9` | `0` | PL1; PL1 - (0-9) |
| `132` | `PL2` | `0..9` | `0` | PL2; PL2 - (0-9) |
| `132` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |
| `132` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (0-4, Pul, Sla) |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `A` | `0..9` | area / environment configurator |
| `PL1` | `0..9` | output 1 light-point configurator |
| `PL2` | `0..9` | output 2 light-point configurator |
| `G1` | `0..9` | group configurator 1 |
| `M` | `0..4` / `SLA` / `PUL` | operating / function mode |


The shared area plus separate `PL1` / `PL2` fields address the two outputs. Object selection and interlock topology are resolved separately from these firmware configurators.

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


### Object `7` - Automation actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality |
| `LOCAL_BUTTON` | `12` = Bistable control; `13` = Monostable control; `14` = Bistable and blades control | `12` | Local button modality |
| `STOP_TIME` | `0` = Infinite; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min | `60` | Stop time |
| `SUBTYPE` | `11` = Actuator; `2` = Shutter; `3` = Curtain; `4` = Gate; `5` = Garage door; `15` = Differential restart | `11` | Type of load |
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


### Product interpretation and source differences

**Object `7` - Automation actuator - product interpretation.**

**Firmware relationship.** The catalogue relation explicitly exposes `LOCAL_BUTTON`. The catalogue relation restricts `SUBTYPE`: Differential restart (`15`).

**Object `6` - Light actuator - product interpretation.**

**Firmware relationship.** The catalogue relation explicitly exposes `LOCAL_BUTTON`, `MINUTES`, `HOURS`, `STATE_RESET`, `SECONDS`, `LOAD_CONTROL_MODE`.

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `132` | `1` | `6` | `4147` | No textual predicate stored | `1` |
| `132` | `1` | `7` | `4702` | `PL2=PL1` | `2` |
| `132` | `2` | `6` | `4147` | No textual predicate stored | `1` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `132` | `6` | `73` | `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `132` | `6` | `74` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `132` | `6` | `75` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `132` | `6` | `76` | `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open (entire reusable range retained) | `0` | Relay state on device reset |
| `132` | `6` | `77` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `132` | `6` | `1856` | `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing (entire reusable range retained) | `0` | Load_control_mode |
| `132` | `7` | `66` | `LOCAL_BUTTON` | `12` = Bistable control; `13` = Monostable control; `14` = Bistable and blades control (entire reusable range retained) | `12` | Funzionalità di pulsante locale ridotta (Local button mode) |
| `132` | `7` | `67` | `SUBTYPE` | `15` = Differential restart | `11` | subtype(ASTCBR); reusable default `11` is outside this subset; filter supplies no replacement default |

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
| `2` | `M=0` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `60` | `2` |
| `2` | `M=1` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `62` | `2` |
| `2` | `M=2` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `65` | `2` |
| `2` | `M=3` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `70` | `2` |
| `2` | `M=4` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `0` | `2` |
| `2` | `M=5` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `20` | `2` |
| `2` | `M=6` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `10` | `2` |
| `2` | `M=7` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `5` | `2` |
| `2` | `M=8` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `15` | `2` |
| `2` | `M=9` | `LOCAL_BUTTON` = `12`; `M` = `0`; `STOP_TIME` = `30` | `2` |
| `2` | `M=I/O` | `LOCAL_BUTTON` = `13`; `M` = `0`; `STOP_TIME` = `60` | `2` |
| `2` | `M=PUL` | `LOCAL_BUTTON` = `12`; `M` = `15`; `STOP_TIME` = `60` | `2` |
| `2` | `M=SLA` | `LOCAL_BUTTON` = `12`; `M` = `11` | `2` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 129` and the `F411/2` / `003842` family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | record installed firmware rather than assuming wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | enumerate the two relay positions and resolve any Automation/Blind role selection | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the two configured output addresses | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect shared `A` / `M`, `PL1` / `PL2`, interlock-related role selection and Object configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The selected topology can expose [`WHO 1` - Lighting](../../functional/who-1-lighting/) and [`WHO 2` - Automation](../../functional/who-2-automation/).

## Observed behavior and corroboration

No sanitized hardware fingerprint is currently retained.

## Programming

Preserve both slots independently. Motor/shutter configurations require the documented logical interlock.

## Source reconciliation

The database Virgin-Object topology explains the documented single, double and combined-load behavior: the relay slots can remain lighting channels or resolve to automation/blind roles. Current and historical load tables differ, so current ratings are stated with source scope rather than overwriting older revisions.

## Evidence limits and open work

- Archive a dedicated current F411/2 technical sheet if exposed by the publisher.
- Hardware-corroborate Object selection and interlock configurations.
- Establish the exact physical configurator-position count from dedicated documentation or hardware.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)
- [BTicino F411/2](https://www.bticino.com/products/bt-f411-2)
