# Basic actuator

## Summary

This compact SCS relay actuator switches a single documented lighting load from a concealed Basic-module installation. It can follow a master or delay a matching slave's switch-off; its `LED`/CFL limit is much lower than its incandescent rating.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0059` | Project identity |
| Technical description | Basic actuator | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `3475` | Canonical commercial records |
| Catalogue item | `54` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `104` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Lighting, Actuator, Flush-mounted | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `3475` | Established identity | canonical commercial record for item `54` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00076-d-UK` | technical sheet | MQ00076-d-UK; 2013-01-09 | Printed/PDF p. 1; complete exact `3475` sheet, including load-class table and delayed slave operation | [Archived original](https://archive.openwebnet-ha.org/sha256/f3/88/f3886a858806692c3850f820a4cad509ff86bd2789782539b6dbce67992d5574.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00076-d-UK.pdf) |
| `BTicino-MyHOME-Spanish-technical-sheets.pdf` | Historical Spanish technical-sheet compilation | BT00076-c-ES; undated leaf | Printed p. 618 / PDF p. 49; complete exact `3475` sheet | [Archived original](https://archive.openwebnet-ha.org/sha256/89/4f/894f468c301ea2b7aaec22635d91961e1eedc00136a21e21b774e975c378b4eb.pdf) | [Publisher source](https://www.bticino.es/pdf/FICHA_TECNICA_DOMOTICA_MYHOME_BTICINO.pdf) |
| `ch_de_katalog_wohnbau.pdf` | Historical regional catalogue | No dated imprint established | Printed p. 165 / PDF p. 167; exact `3475` consumption and dimensions | [Archived original](https://archive.openwebnet-ha.org/sha256/9f/e5/9fe511c3ac12d861dff7d8d28ddec3b3612a27e99a804afbed89877c73a6b4ed.pdf) | Publisher URL not retained in manifest |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / current | `27 Vdc` nominal SCS; operating `18..27 Vdc`; `13 mA` | MQ00076-d-UK, printed/PDF p. 1 |
| Relay limits at 230 Vac | Incandescent/halogen: `460 W` / `2 A`; `LED`/CFL: `40 W`, maximum one lamp; ferromagnetic transformers: 460 VA / `2 A` cosφ 0.5 | MQ00076-d-UK, printed/PDF p. 1 |
| Installation | Basic module for flush, junction or shutter boxes and trunking; fits behind suitable controls | MQ00076-d-UK, printed/PDF p. 1 |
| Interface | Configurator socket, `LED`, SCS bus and 0.75 mm² load leads | MQ00076-d-UK, printed/PDF p. 1 |
| Regional dimensions | `41 × 41 × 19 mm` | German catalogue, printed p. 165 / PDF p. 167 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `54` | Canonical catalogue |
| Technical item | Basic actuator | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `104` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `104` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `54` | `3475` | `1` | `5` | `BTicino_Undefined_Basic actuator` |

All these records are visible, non-dependent and not marked as gateways; `visibility_type` is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `193` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `193` | `1` | `6` Light actuator | Fixed/designated metadata | `689` | `6` | `478` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `193` | Physical configuration | `0` | Canonical firmware/mode association |
| `193` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `193` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `193` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `193` | `A` | `0..9` | `0` | A; Environment |
| `193` | `PL` | `0..9` | `0` | `PL`; Light Point |
| `193` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (0-4, Pul, Sla) |
| `193` | `G1` | `0..9` | `0` | `G1`; `G1` - (0-9) |

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

### Device-specific interpretation

Firmware `193` designates one Light actuator Object `6`, without a Virgin. Empty condition `4147` references conversion rule `1`. M=`1..4` maps to `DELAYED_OFF=60/120/180/240` seconds, agreeing with published delayed-slave minutes. The I/O conversion branch is outside the firmware enum; do not invent a numeric encoding or a physical input. `SLA` omits a `DELAYED_OFF` assignment, not an implicit zero. Reusable Object `M=16` slave-PUL, ten groups and area/light-point domains exceed the firmware surface. Timing/reset/zero-crossing/local-button fields remain software schema evidence, not proof of a local pushbutton or a separately tested load class.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `193` | `1` | `6` | `4147` | No textual predicate stored | `1` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `193` | `6` | `679` | `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open (entire reusable range retained) | `0` | Per energy management (State on Reset) |
| `193` | `6` | `680` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `193` | `6` | `681` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `193` | `6` | `682` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `193` | `6` | `1795` | `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `193` | `6` | `1867` | `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing (entire reusable range retained) | `0` | Load_control_mode |

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
| `DIMENSION 1` | corroborate technical identity for catalogue item `54` / `modobj = 104` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`6`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Relay operation | Single relay; basic automation modes exclude functions requiring two interlocked relays | MQ00076-d-UK, printed/PDF p. 1 |
| PUL / `SLA` | Monostable ON ignores room/general commands; slave receives commands from master with same address | MQ00076-d-UK, printed/PDF p. 1 |
| Delayed OFF | Master switches off immediately; slave remains on `1..4` min; point-to-point only | MQ00076-d-UK, printed/PDF p. 1 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Physical configuration values and reusable Object settings are separate. The exact 2013 sheet supports PUL, `SLA` and M=`1..4` with delays of `1..4` minutes; delayed OFF affects the matching slave, not the master. Basic operation follows the control except two-relay interlock functions. The canonical firmware supplies A/`PL`/`G1`=`0..9`, but the sheet does not independently specify their full physical address domains.

| Physical M | Published behavior |
| --- | --- |
| PUL | Monostable ON; ignore room/general commands |
| `SLA` | Follow same-address master |
| 1 / 2 / 3 / 4 | Delay slave OFF 1 / 2 / 3 / 4 min, point-to-point only |

## Source reconciliation

The historical Spanish BT00076-c-ES and exact MQ00076-d-UK agree on load-class limits, supply/current and Basic mounting. The German catalogue supplies exact dimensions without proving a new firmware revision. The device-label diagram says cosφ 0.6, while the technical load table says cosφ 0.5; these source scopes remain separate. The previous unqualified 12W31 server-compatibility statement lacked a retained cited original and has been removed pending verification.

Catalogue-specific scope and filter irregularities are detailed under [Object configuration surfaces](#object-configuration-surfaces); those relations do not establish additional physical sensors, load interfaces or installed behavior.

## Evidence limits and open work

- The previously mentioned production-week compatibility cutoff has no retained cited supporting row in this dossier; installed/server-version compatibility remains unverified.
- Load-table versus device-label power-factor wording remains source-specific.
- MyHOME_Suite/glossary help and actual relay/input timing or diagnostics are not independently tested.
- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, software payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0051-0060-2026-10-06.md#own-dev-0059)
