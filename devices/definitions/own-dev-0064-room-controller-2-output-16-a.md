# Room Controller - 2 outputs 16 A

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0064` | Project identity |
| Technical description | Room Controller - 2 outputs 16 A | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSW3002`, `048841` | Canonical commercial records |
| Catalogue item | `59` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `167` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `3` | Canonical firmware catalogue |
| Categories | Lighting Management, Room Controller, Relay actuator | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSW3002` | Established identity | Catalogue item `59`; named in `U3773B`, PDF p. 1 |
| Legrand | `048841` | Established identity | canonical commercial record for item `59` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BTicino General Catalogue product sheet | catalogue product sheet | current publisher catalogue | `BMSW3002` Room Controller functional and electrical summary | Not applicable - web page | [Official product page](https://catalogo.bticino.it/prodotto/soluzioni-per-lefficienza-energetica/lighting-control---sistema-filare-bus-scs/attuatori/BTI-BMSW3002-IT) |
| `U3773B.pdf` | installation instruction sheet | `U3773B01SY-09W51` | `BMSW3001` and `BMSW3002`; ratings/mounting PDF p. 1, panels 1-2; factory association/wiring/test/setup PDF p. 2, panels 3-6; no printed pagination | [Archived original](https://archive.openwebnet-ha.org/sha256/60/ae/60ae6cf3046778b4d5fcb59b99f9d59f24bfb86d9a7a2ffdd0eb1142b2e9e8c3.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/U3773B.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `100..240 Vac`, `50..60 Hz` | `U3773B`, PDF p. 1, panel 1; no printed pagination |
| Outputs | `2` independently controlled outputs; `I_L1 + I_L2 <= 16 A` total, subject to load-specific ratings | `U3773B`, PDF p. 2, panel 4; no printed pagination; catalogue item `59` |
| Terminal conductor capacity | `2 x 2.5 mm²` | `U3773B`, PDF p. 1, panel 1; no printed pagination |
| BUS connector type | RJ45 | `U3773B`, PDF p. 1, panel 1; no printed pagination |
| Combined sensor/control-port allowance | Ports `1 + 2`: maximum `200 mA`; not the Device's own consumption | `U3773B`, PDF p. 1, panel 1; no printed pagination; port pictograms |
| Operating temperature | `-5..45 °C` | `U3773B`, PDF p. 1, panel 1; no printed pagination |
| Mounting | Two supplied fixing studs; illustrated quarter-turn locking and screw fastening to a support | `U3773B`, PDF p. 1, panel 2; no printed pagination |
| Sensor/control wiring length | `150 m` maximum on the illustrated RJ45 branch to connected devices; not a whole-installation BUS limit | `U3773B`, PDF p. 2, panel 4; no printed pagination |
| SCS trunk input | `1` terminal/RJ45 input | BTicino General Catalogue product sheet; `U3773B`, PDF p. 2, panel 4; no printed pagination shows RJ45 SCS BUS connection |
| Protection | `IP20` | BTicino General Catalogue product sheet; not specified in `U3773B` |
| Installation | Ceiling / false-ceiling installation | BTicino General Catalogue product sheet; mounting arrangements `U3773B`, PDF p. 1, panel 2; no printed pagination |

### Published load ratings

| Load pictogram / class | At `230 Vac` | At `110 Vac` | Published current | Evidence |
| --- | --- | --- | --- | --- |
| Incandescent lamp | `3680 W` | `1760 W` | `16 A` | `U3773B`, PDF p. 1, panel 1; no printed pagination |
| Mains halogen lamps | `3680 W` | `1760 W` | `16 A` | `U3773B`, PDF p. 1, panel 1; no printed pagination |
| Fluorescent tube | `10 x (2 x 36 W)` | `5 x (2 x 36 W)` | `4.3 A` | `U3773B`, PDF p. 1, panel 1; no printed pagination |
| Transformer-fed lamp, first transformer pictogram | `3680 VA` | `1760 VA` | `16 A` | `U3773B`, PDF p. 1, panel 1; no printed pagination |
| Transformer-fed lamp, second transformer pictogram | `3680 VA` | `1760 VA` | `16 A` | `U3773B`, PDF p. 1, panel 1; no printed pagination |
| Compact fluorescent lamp | `1150 VA` | `550 VA` | `5 A` | `U3773B`, PDF p. 1, panel 1; no printed pagination |

The sheet identifies the load classes pictorially; the two transformer columns are retained separately without inventing a transformer specification. No LED-load rating is given. The `16 A` aggregate limit applies across both `BMSW3002` outputs; the matrix does not authorize simultaneous `16 A` loads on each output.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `59` | Canonical catalogue |
| Technical item | Room Controller - 2 outputs 16 A | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `167` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `281` | `-1` | `-1` | `-1` | `3` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `281` | `1` | `6` Light actuator | Fixed/designated metadata | `994` | `6` | `600` |
| `281` | `2` | `6` Light actuator | Fixed/designated metadata | `995` | `6` | `600` |
| `281` | `3` | `167` Room controller | Fixed/designated metadata | `996` | `167` | `601` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `281` | Advanced Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `281` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

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


### Object `167` - Room controller

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `MODE` | `0` = Stand-alone mode; `1` = Supervision mode | `0` | Modality; Mode |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `281` | `6` | `1104` | `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open (entire reusable range retained) | `0` | Relay state on device reset |
| `281` | `6` | `1871` | `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing (entire reusable range retained) | `0` | Load_control_mode |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `59` / `modobj = 167` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`6`, `167`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Lighting Management Room Controller with two independently controlled zero-crossing outputs and local BUS connections for sensors/commands. Catalogue firmware `281` exposes external Object `6` in Module slots `1` and `2` and external Object `167` in slot `3`. Two actuator placements share the reusable Object definition; they are distinct Device-local Modules.

| Published function | Scope / behavior | Evidence |
| --- | --- | --- |
| Factory association | Diagram associates sensor/control port `1` with `L1` and port `2` with `L2` on the illustrated two-output controller; `L2` applies to `BMSW3002` | `U3773B`, PDF p. 2, panel 3; no printed pagination |
| Local test | Illustrated output `1` button turns `L1` on, then off on the next press; the indicator is shown lit before the second press and unlit afterwards | `U3773B`, PDF p. 2, panel 5; no printed pagination |
| Setup interfaces | A handheld remote is directed at a sensor; controller `LEARN` control identified; no remote reference or complete sequence specified | `U3773B`, PDF p. 2, panel 6; no printed pagination |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

The catalogue registers Advanced Configuration for this technical item and declares `3` Modules. Resolve the selected Module/Object and apply the firmware-specific fields and effective restrictions recorded above.

| Product procedure | Published scope / boundary | Evidence |
| --- | --- | --- |
| Installation | Follow the illustrated fixing-stud arrangements and quarter-turn locking; rejected fastening positions are crossed out | `U3773B`, PDF p. 1, panel 2; no printed pagination |
| Wiring | The two-output drawing identifies mains supply, switched loads, SCS BUS and sensor/control branches; `L2` and the summed current limit apply to `BMSW3002` | `U3773B`, PDF p. 2, panel 4; no printed pagination |
| Output test | The illustrated output `1` button toggles the displayed load on and off; no press-duration timing is specified | `U3773B`, PDF p. 2, panel 5; no printed pagination |
| Configuration / learning | Sensor-directed remote and controller `LEARN` control illustrated; sheet does not identify remote model, timed learning sequence or transfer procedure | `U3773B`, PDF p. 2, panel 6; no printed pagination |

The installation sheet supplies no complete factory-reset, project-transfer or firmware-update procedure and no mapping from these local controls to the catalogue configuration fields or diagnostic serialization. Its numbered panels are illustration identifiers; the mounting diagram's `1/4` denotes a quarter turn, not a page reference.

## Source reconciliation

The canonical catalogue binds `BMSW3002` and Legrand `048841` to item `59`. `U3773B`, revision `U3773B01SY-09W51`, explicitly names `BMSW3001` and `BMSW3002` on PDF p. 1. It directly supports the BTicino reference and the shared electrical/load/mounting facts above. The Legrand reference remains catalogue-derived; the sheet does not name it. The existing BTicino catalogue summary and the retained instruction sheet agree on mains supply, the combined control-port allowance and the total two-output current limit. The sheet adds load-specific limits, temperature, mounting and illustrated commissioning controls.

The `200 mA` value belongs to the combined port pictograms, not an own-consumption measurement. The `150 m` label bounds the illustrated sensor/control branch in the two-output wiring diagram; it is not a universal SCS installation length. The remote/`LEARN` illustration does not establish a complete learning workflow. The source revision does not identify an installed firmware tuple. Catalogue fields, product procedures and hardware/runtime behavior retain their separate evidence scopes.

## Evidence limits and open work

- Obtain directly applicable Legrand `048841` documentation and fuller setup/reset/transfer/update instructions.
- Establish any required own-consumption, LED-load and transformer-type specifications from directly applicable publisher evidence.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate relation filters, active topology and local-control to catalogue/diagnostic mappings on controlled hardware.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [BMSW3001/BMSW3002 installation instruction sheet, archived original](https://archive.openwebnet-ha.org/sha256/60/ae/60ae6cf3046778b4d5fcb59b99f9d59f24bfb86d9a7a2ffdd0eb1142b2e9e8c3.pdf)
