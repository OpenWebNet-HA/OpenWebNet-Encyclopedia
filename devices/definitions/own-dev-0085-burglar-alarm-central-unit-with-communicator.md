# Burglar alarm central unit with communicator

## Summary

The 3485 is a burglar-alarm central unit with a telephone communicator for alarm-system supervision. Retained publisher evidence documents bidirectional telephone interaction and Ademco Contact ID, while the precise zone and sensor limits remain product-specific documentation gaps.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0085` | Project identity |
| Technical description | Burglar alarm central unit with communicator | Canonical catalogue |
| Commercial identities | `3485` | Canonical commercial records |
| Catalogue item | `139` | Canonical catalogue |
| Main catalogue system | Burglar alarm system | Canonical catalogue |
| Item model / `modobj` | `198` | Canonical inventory |
| Firmware definition | `8.0.0`; `6.0.0`; `7.0.0` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Burglar alarm system, Burglar alarm | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Pivot | `3485` | Established catalogue identity | canonical commercial record for item `139` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| BTicino/Legrand residential catalogue | product catalogue | historical publisher catalogue | 3485 phone/Contact ID role: printed p. 187 / PDF p. 189; battery 3506 compatibility printed p. 195 / PDF p. 197; do not alias 3485STD | [Archived original](https://archive.openwebnet-ha.org/sha256/9f/e5/9fe511c3ac12d861dff7d8d28ddec3b3612a27e99a804afbed89877c73a6b4ed.pdf) | [Official source](https://assets.legrand.com/webf/ch/ch_de_katalog_wohnbau.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Product description | `Burglar alarm central unit with communicator` | Catalogue item description; not a complete product specification |
| Additional electrical/mechanical characteristics | Additional properties not established beyond the source-scoped facts on this page | Direct product-source reconciliation remains open |
| Compatible battery | `3506`, `7.2 V` | Residential catalogue, printed p. 195 / PDF p. 197; explicitly names 3485 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `139` | Canonical catalogue |
| Technical item | Burglar alarm central unit with communicator | Canonical catalogue |
| Main system | Burglar alarm system | Canonical catalogue |
| Item model / `modobj` | `198` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `8` | `0` | `0` | `1` | Catalogue default | Official |
| `16` | `6` | `0` | `0` | `1` | Not catalogue default | Official |
| `17` | `7` | `0` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `1` | `13` AI Control Unit With Communicator Pstn | Fixed/designated metadata | `2272` | `13` | `950` |
| `16` | `1` | `13` AI Control Unit With Communicator Pstn | Fixed/designated metadata | `2275` | `13` | `953` |
| `17` | `1` | `13` AI Control Unit With Communicator Pstn | Fixed/designated metadata | `2274` | `13` | `952` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `15` | Product Programming | supported configuration route for this Device family |
| `16` | Product Programming | supported configuration route for this Device family |
| `17` | Product Programming | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `15` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `16` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `17` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `13` - AI Control Unit With Communicator Pstn

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `NUM_PSTN` | No legal values specified in source | Not specified in source | Telephone number PSTN |
| `FW_VER` | No legal values specified in source | Not specified in source | Firmware version |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |

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
| `DIMENSION 1` | corroborate technical identity for catalogue item `139` / `modobj = 198` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`13`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `13` AI Control Unit With Communicator Pstn | Burglar alarm system | Firmware/Object capability association; resolve the slot and configuration first |
| `13` AI Control Unit With Communicator Pstn | Video door entry system | Firmware/Object capability association; resolve the slot and configuration first |

Catalogue system identifiers are not `WHO` numbers. The source establishes the roles shown, not a complete command vocabulary or proof of every installed function. Correlate the selected role with [Functional Protocol](../../functional/) before sending functional commands. Product-specific behavior and transport constraints remain unestablished where no direct source is retained.

The retained residential catalogue explicitly names 3485 for bidirectional telephone interaction and Ademco Contact ID. Its adjacent product listings describe 3485STD; those variant-specific zone, sensor and scenario limits are not assigned to 3485 here.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

The catalogue registers Product Programming for this technical item. Use the firmware-specific fields, selected Module/Object and effective restrictions on this page as the configuration boundary. This item has one declared Module; do not treat candidate Object rows as additional channels.

No retained product manual establishes the complete commissioning, reset, transfer or update procedure for these commercial identities. Obtain that evidence before prescribing a Device-specific sequence. The catalogue mode registration alone does not establish a universal physical-button or gateway-session workflow.

## Source reconciliation

The canonical MyHOME Suite `3.5.38` catalogue establishes the commercial-to-item association, firmware definitions, Module placements, reusable configuration values and relationship-specific conditions/filters recorded above. Retained publisher evidence is listed in Documentation; its exact Device coverage is stated there. Catalogue descriptions and Object names therefore remain implementation evidence; electrical limits, commissioning procedures and runtime behavior cannot be borrowed from sibling products.

The corrected tables distinguish external Object/Virgin Object numbers from database keys, firmware status from wildcard applicability and actual Module slots from slot row IDs. Remaining source acquisition and runtime checks are listed below.

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
