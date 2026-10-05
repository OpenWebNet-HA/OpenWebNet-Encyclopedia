# GSM burglar alarm central unit

## Summary

This burglar-alarm central unit combines alarm-system control with fixed-line and GSM communication. The documented GSM function requires a separately supplied SIM card, giving the installation a mobile-network communication path alongside the fixed line.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0087` | Project identity |
| Technical description | GSM burglar alarm central unit | Canonical catalogue |
| Commercial identities | `3486` | Canonical commercial records |
| Catalogue item | `141` | Canonical catalogue |
| Main catalogue system | Burglar alarm system | Canonical catalogue |
| Item model / `modobj` | `197` | Canonical inventory |
| Firmware definition | `8.0.0`; `6.0.0`; `7.0.0` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Burglar alarm system, Burglar alarm | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Pivot | `3486` | Established catalogue identity | canonical commercial record for item `141` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| BTicino/Legrand residential catalogue | product catalogue | historical publisher catalogue | 3486 roles/capacity/programming: printed pp. 147, 187-190 / PDF pp. 149, 189-192; battery printed p. 195 / PDF p. 197 | [Archived original](https://archive.openwebnet-ha.org/sha256/9f/e5/9fe511c3ac12d861dff7d8d28ddec3b3612a27e99a804afbed89877c73a6b4ed.pdf) | [Official source](https://assets.legrand.com/webf/ch/ch_de_katalog_wohnbau.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Product description | `GSM burglar alarm central unit` | Catalogue item description; not a complete product specification |
| Additional electrical/mechanical characteristics | Additional properties not established beyond the source-scoped facts on this page | Direct product-source reconciliation remains open |
| Installation | Wall bracket | Residential catalogue, printed p. 190 / PDF p. 192 |
| Compatible battery | `3507/6`, `6 V` | Same catalogue, printed pp. 190, 195 / PDF pp. 192, 197 |
| Communicator | Fixed-line and GSM; SIM card required, not supplied | Same catalogue, printed p. 190 / PDF p. 192 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `141` | Canonical catalogue |
| Technical item | GSM burglar alarm central unit | Canonical catalogue |
| Main system | Burglar alarm system | Canonical catalogue |
| Item model / `modobj` | `197` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `8` | `0` | `0` | `1` | Catalogue default | Official |
| `20` | `6` | `0` | `0` | `1` | Not catalogue default | Official |
| `21` | `7` | `0` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `1` | `14` AI Control Unit With Communicator Gsm | Fixed/designated metadata | `2276` | `14` | `954` |
| `20` | `1` | `14` AI Control Unit With Communicator Gsm | Fixed/designated metadata | `2278` | `14` | `956` |
| `21` | `1` | `14` AI Control Unit With Communicator Gsm | Fixed/designated metadata | `2277` | `14` | `955` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `19` | Product Programming | supported configuration route for this Device family |
| `20` | Product Programming | supported configuration route for this Device family |
| `21` | Product Programming | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `19` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `20` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `21` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `14` - AI Control Unit With Communicator Gsm

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `NUM_PSTN` | No legal values specified in source | Not specified in source | Telephone number PSTN |
| `NUM_GSM` | No legal values specified in source | Not specified in source | Telephone number GSM |
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
| `DIMENSION 1` | corroborate technical identity for catalogue item `141` / `modobj = 197` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`14`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `14` AI Control Unit With Communicator Gsm | Burglar alarm system | Firmware/Object capability association; resolve the slot and configuration first |
| `14` AI Control Unit With Communicator Gsm | Video door entry system | Firmware/Object capability association; resolve the slot and configuration first |

Catalogue system identifiers are not `WHO` numbers. The source establishes the roles shown, not a complete command vocabulary or proof of every installed function. Correlate the selected role with [Functional Protocol](../../functional/) before sending functional commands. Product-specific behavior and transport constraints remain unestablished where no direct source is retained.

| Published capability | Limit / role | Evidence |
| --- | --- | --- |
| Zones | Maximum `8` | Residential catalogue, printed p. 188 / PDF p. 190 |
| Sensors | Maximum `72` | Same source |
| Scenarios | Maximum `16` | Same catalogue, printed p. 190 / PDF p. 192 |
| Alarm transmission | Ademco Contact ID | Same source |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

The catalogue registers Product Programming for this technical item. Use the firmware-specific fields, selected Module/Object and effective restrictions on this page as the configuration boundary. This item has one declared Module; do not treat candidate Object rows as additional channels.

No retained product manual establishes the complete commissioning, reset, transfer or update procedure for these commercial identities. Obtain that evidence before prescribing a Device-specific sequence. The catalogue mode registration alone does not establish a universal physical-button or gateway-session workflow.

| Product path | Evidence |
| --- | --- |
| TiSecurity application software | Residential catalogue, printed p. 190 / PDF p. 192 |
| Direct configuration / transponder or keypad control | Same catalogue, printed p. 147 / PDF p. 149 |

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
