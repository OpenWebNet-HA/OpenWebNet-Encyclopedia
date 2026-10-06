# Room Controller 1 Output 16 Amps

## Summary

This room controller switches one lighting load and connects local SCS sensors or controls through RJ45 ports. It combines a relay and a controller in the catalogue’s two-Module model, with documented local load testing and remote configuration.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0082` | Project identity |
| Technical description | Room Controller 1 Output 16 Amps | Canonical catalogue; shared load ratings in `U3773B` |
| Commercial identities | `BMSW3001`, `048840` | Canonical commercial records |
| Catalogue item | `130` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `166` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `2` | Canonical firmware catalogue |
| Categories | Automation, Room Controller | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSW3001` | Established identity | Catalogue item `130`; named in `U3773B`, PDF p. 1 |
| Legrand | `048840` | Established catalogue identity | canonical commercial record for item `130` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| `U3773B.pdf` | installation instruction sheet | `U3773B01SY-09W51` | `BMSW3001` and `BMSW3002`; ratings/mounting PDF p. 1, panels 1-2; factory association/wiring/test/setup PDF p. 2, panels 3-6; no printed pagination | [Archived original](https://archive.openwebnet-ha.org/sha256/60/ae/60ae6cf3046778b4d5fcb59b99f9d59f24bfb86d9a7a2ffdd0eb1142b2e9e8c3.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/U3773B.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mains supply | `100..240` V~; `50..60 Hz` | `U3773B`, PDF p. 1, panel 1 |
| Physical output | One switched output on `BMSW3001`; `BMSW3002` is a separate two-output product | `U3773B`, PDF p. 1 drawings; catalogue item 130 |
| Terminations / local bus | 2 × 2.5 mm²; RJ45; local ports 1+2 together ≤`200 mA` | `U3773B`, PDF p. 1, panel 1 |
| Operating temperature | −`5..45 °C` | Same load-rating panel |
| Incandescent / halogen loads | 230 V: `3680 W` / `16 A`; 110 V: `1760 W` / `16 A` | `U3773B`, PDF p. 1, bulb/halogen columns |
| Fluorescent loads | 230 V: 10 × (`2 × 36 W`), `4.3 A`; 110 V: 5 × (`2 × 36 W`), `4.3 A` | Same panel, fluorescent column |
| Transformer-fed lamp loads | Both illustrated transformer categories: 230 V 3680 VA / `16 A`; 110 V 1760 VA / `16 A` | Same panel; separate source pictograms retained in original |
| Compact fluorescent load | 230 V: 1150 VA / `5 A`; 110 V: 550 VA / `5 A` | Same panel; VA retained rather than converted to W |
| Mounting | Fixing studs with quarter-turn lock; support/wire arrangements illustrated | `U3773B`, PDF p. 1, panel 2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `130` | Canonical catalogue |
| Technical item | Room Controller 1 Output 16 Amps | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `166` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `166` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `130` | `BMSW3001` | `1` | `5` | Empty in source |
| `1804` | `048840` | `2` | `5` | Empty in source |

| Record | Visible | Dependent | Gateway flag | Visibility type |
| --- | --- | --- | --- | --- |
| `130` | `1` | `0` | `0` | Empty in source |
| `1804` | `1` | `0` | `0` | Empty in source |

These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `300` | `-1` | `-1` | `-1` | `2` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `300` | `1` | `6` Light actuator | Fixed/designated metadata | `998` | `6` | `603` |
| `300` | `2` | `167` Room controller | Fixed/designated metadata | `997` | `167` | `602` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `300` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `300` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

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

### Device-specific interpretation

Firmware `300` is a Deprecated wildcard definition with two diagnostic Modules: relay Object `6` and controller Object `167`. This is one physical load output, not `BMSW3002`. Empty predicates `4145` do not prove unconditional activation. The only firmware field is `AID`; only Advanced Configuration `2` is associated. `STATE_RESET` filter `1105` and `LOAD_CONTROL_MODE` filter `1872` store no narrower legal subset. Controller MODE `0` standalone / `1` supervision, default `0`, is an Object field, not a second output or the catalogue configuration-mode ID.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `300` | `1` | `6` | `4145` | No textual predicate stored | None |
| `300` | `2` | `167` | `4145` | No textual predicate stored | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `300` | `6` | `1105` | `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open (entire reusable range retained) | `0` | Per energy management (State on Reset) |
| `300` | `6` | `1872` | `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing (entire reusable range retained) | `0` | Load_control_mode |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `130` / `modobj = 166` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`6`, `167`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `6` Light actuator | Automation | Firmware/Object capability association; resolve the slot and configuration first |
| `167` Room controller | Automation | Firmware/Object capability association; resolve the slot and configuration first |

These are catalogue Object/system associations, not `WHO` numbers, physical connector claims or observed command acceptance. Resolve the active Module/Object and its restrictions before using the [Functional Protocol](../../functional/).

### Published product functions

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Local test | Output button switches the illustrated load on/off with indication | `U3773B`, PDF p. 2, panel 5 |
| Local sensing/control | Sensor/control connections via local RJ45 bus are illustrated | PDF p. 2, panel 4 |
| Configuration | Remote and LEARN button shown; exact complete pairing sequence not specified in text | PDF p. 2, panel 6 |
| Standalone/supervision | MODE 0 standalone or 1 supervision, reusable default 0 | Object `167`; installed mode unobserved |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

`U3773B` illustrates mounting (PDF p. 1, panel 2), local-bus wiring (p. 2, panel 4), load testing (panel 5) and configuration remote/LEARN controls (panel 6). The catalogue associates only Advanced Configuration `2` and exposes AID. The p. 2 wiring drawing shows the two-output sibling `BMSW3002`: its L1+L2 aggregate rating must not be presented as a two-load `BMSW3001` specification. A complete reset/update/transfer procedure for this exact reference is not retained.

## Source reconciliation

`U3773B` directly names `BMSW3001` and `BMSW3002`; its shared p. 1 ratings apply to both, while drawings and the two-output p. 2 diagram have separate product scope. The `BMSW3001` has one physical output despite two catalogue Modules. The 150 m wiring span and aggregate 16 A appear on the `BMSW3002` drawing and are not adopted as an independent `BMSW3001` network/output rating. Historical EN50428 marking is manufacturer declaration scope, not a current certification assessment. Catalogue 048840 equivalence is established, but a separately applicable Legrand sheet is absent.

Catalogue interpretation is detailed under [Object configuration surfaces](#object-configuration-surfaces); the complete firmware, topology and restriction tables remain authoritative for software applicability.

## Evidence limits and open work

- Obtain an exact 048840 regional specification and fuller `BMSW3001` configuration/reset/update procedure.
- Corroborate the active relay/controller Objects and effective state/load-control fields on hardware.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [`BMSW3001`/BMSW3002 installation instruction sheet, archived original](https://archive.openwebnet-ha.org/sha256/60/ae/60ae6cf3046778b4d5fcb59b99f9d59f24bfb86d9a7a2ffdd0eb1142b2e9e8c3.pdf)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0081-0090-2026-10-06.md#own-dev-0082)
