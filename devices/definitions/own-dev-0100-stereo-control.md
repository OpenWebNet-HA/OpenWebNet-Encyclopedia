# Stereo control

## Summary

This DIN stereo-source control connects an external stereo source to the sound-system installation. Its audio connections and infrared transmitter arrangement provide the documented source interface and remote-control path.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0100` | Project identity |
| Technical description | Stereo control | Canonical catalogue |
| Commercial identities | `L4561N`, `003586` | Canonical commercial records |
| Catalogue item | `1130` | Canonical catalogue |
| Main catalogue system | Sound system | Canonical catalogue |
| Item model / `modobj` | `6` | Canonical inventory |
| Firmware definition | `4.0.6` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Sound system | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `L4561N` | Established catalogue identity | canonical commercial record for item `1130` |
| Legrand | `003586` | Established catalogue identity | canonical commercial record for item `1130` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| MyHOME residential automation catalogue | Product catalogue | not stated in retained row | L4561N stereo source interface: printed p. 28 / PDF p. 28; commercial cross-reference printed p. 34 / PDF p. 34 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/13/8e/138e7a234fe24fb044d3bfc82954e08b2887be22f3f8ceb24aecaeff6ed2f2e5.pdf) | [Official source](https://assets.legrand.com/pim/DOCUMENT/BR%20MyHOME%20HPML0714.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Programming / connectivity surface | Serial | canonical inventory |

| Property | Value | Evidence |
| --- | --- | --- |
| DIN width | 4 modules of `17.5 mm` | Arteor catalogue, printed p. 28 / PDF p. 28 |
| Connection / role | Stereo-source interface; RCA/RCA and jack cables for IR transmitter connection | Same source |
| Remote control | IR remote control supported | Same source |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1130` | Canonical catalogue |
| Technical item | Stereo control | Canonical catalogue |
| Main system | Sound system | Canonical catalogue |
| Item model / `modobj` | `6` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `65` | `4` | `0` | `6` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `65` | `1` | `161` Phonic source | Fixed/designated metadata | `2298` | `161` | `976` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `65` | Product Programming | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `65` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `65` | `S1` | `0..4` | `0` | S1 |
| `65` | `M1` | `0..4` | `0` | M1 |
| `65` | `M2` | `0..6` | `0` | M2 |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `161` - Phonic source

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `RECEIVE_MODE` | `0..1` | `0` | Set the reception mode of the radio signal |
| `NUM_STATION` | `0..3` | `0` | Set the number of station presets. 0 or 1for 5 station, 2 for 10 station and 3 for 15 station |
| `S` | `0..255` | `1` | Area |
| `SUB_SOURCE` | `0..15` | `0` | Max subsource |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | - | None | - | No relation-specific filters associated | - | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1130` / `modobj = 6` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`161`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `161` Phonic source | Sound system | Firmware/Object capability association; resolve the slot and configuration first |

Catalogue system identifiers are not `WHO` numbers. The source establishes the roles shown, not a complete command vocabulary or proof of every installed function. Correlate the selected role with [Functional Protocol](../../functional/) before sending functional commands. Product behavior is additionally bounded by the publisher evidence below; uncorroborated transport and firmware details remain open work.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

The catalogue registers Product Programming for this technical item. Use the firmware-specific fields, selected Module/Object and effective restrictions on this page as the configuration boundary. This item has one declared Module; do not treat candidate Object rows as additional channels.

The retained sources establish only the Device-specific procedures described below; reset, transfer or update details not covered by those sources remain open work. The catalogue mode registration alone does not establish a universal physical-button or gateway-session workflow.

## Source reconciliation

The implementation item is named Stereo control, and the directly applicable Arteor product catalogue describes `L4561N` as a stereo control/source interface with IR control and four DIN modules. Preserve the implementation label in Identity; use the publisher source-interface role to interpret the catalogue title. The printed cross-reference uses `03586`, while the implementation identity is `003586`; preserve the raw forms and do not infer packaging equivalence from formatting alone.

## Evidence limits and open work

- Locate and archive dedicated publisher documentation for the exact commercial references where available.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate relation filters and condition-selected topology against MyHOME Suite and controlled hardware observations.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
