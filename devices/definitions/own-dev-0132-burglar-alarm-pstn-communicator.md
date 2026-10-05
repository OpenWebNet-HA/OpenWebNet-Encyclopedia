# Burglar alarm unit with PSTN communicator

## Summary

This burglar-alarm central unit combines intrusion-system management with a fixed-line telephone communicator. Its documented zone organization includes intrusion and technical alarms, with 16 partition scenarios and published OPEN-SCS functions for system interaction.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0132` | Project identity |
| Technical description | Burglar alarm unit with PSTN communicator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `573934`, `067520` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1423` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Burglar alarm system | Main system association |
| Item model / `modobj` | `203` | Main association; independent of project ID |
| Firmware definition | `105`, `641` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | User interfaces, Gateways and interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand - Arteor | `573934` | Established catalogue identity | Manufacturer database commercial record `976` explicitly links this SKU to item `1423` |
| Legrand - Céliane | `067520` | Established catalogue identity | Manufacturer database commercial record `1423` explicitly links this SKU to item `1423` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `u3500a.pdf` | Installation manual | `u3500a; 11/08-01 PC` | Exact-product specifications, operating/configuration material and source limitations; retained 84-page original; relevant product sections reviewed. Printed pagination and 1-based PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/a3/75/a375768955e0bd9d19a227b8f9416584cbbdfa7443d0cf23552aecb20a68b6d0.pdf) | [Publisher original](https://assets.legrand.com/general/legrand-exp/np-ft-gt/u3500a.pdf) |
| `u3501a_s_uk.pdf` | SecurityConfig manual | `u3501a_s_uk; original publication date not established` | Exact-product specifications, operating/configuration material and source limitations; retained 54-page original; relevant product sections reviewed. Printed pagination and 1-based PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/72/35/7235899a2edacb9dddd4ba11aed4a033b2c2a03d7c8897bcee4ccc123ea453ac.pdf) | [Publisher original](https://assets.legrand.com/general/legrand-exp/np-ft-gt/u3501a_s_uk.pdf) |
| `U3887A.pdf` | French/English Céliane installation manual | `U3887A; 11/09-01 PC` | 067520: English commissioning/function section printed/PDF pp. 87-164; technical data p. 163; OPEN commands pp. 151-162. French counterpart occupies the first half. | [Archived original](https://archive.openwebnet-ha.org/sha256/40/7e/407e5481847fadc8e3180c703fcc464a2c1c6c2987079be71d34690d8d70d983.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/U3887A.pdf) |
| `u3499a.pdf` | Exact historical manufacturer documentation | `u3499a; 11/08-01 PC` | Exact-product specifications, operating/configuration material and source limitations; retained 40-page original; relevant product sections reviewed. Printed pagination and 1-based PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/b7/c3/b7c3620e398e201f98ff2760806a8c885a81e4f2e953dc20a7e0d6ce47566882.pdf) | [Publisher original](https://assets.legrand.com/general/legrand-exp/np-ft-gt/u3499a.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `1423` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply, Arteor manual | `18..28 V` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Current draw, as printed | `standby 55..90 mA Max` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Operating temperature | `5..40 °C` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Dimensions, both manuals | `125 x 128 x 31 mm` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Enclosure | `IP30` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Zones | `0: up to 9 connectors; 1..8: intrusion sensors; 9: technical/auxiliary alarms` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Partition scenarios | `16` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Telephone book | `jolly number + 10 stored numbers` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Simplified telephone commands | `9` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Telephone interface | `two-wire pair; DTMF/pulses line label; selection specified DTMF only` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1423` | Canonical catalogue |
| Technical item description | Burglar alarm central unit with communicator | Canonical catalogue |
| Item family | 0; key `10` | Canonical catalogue |
| Main system | Burglar alarm system; key `3` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `203` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `105` | `1` | `0` | `17` | `1` | Catalogue default | Official |
| `641` | `2` | `0` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `105` | `1` | `13` AI Control Unit With Communicator Pstn | Fixed/designated metadata | `2262` | `13` | `940` |
| `641` | `1` | `13` AI Control Unit With Communicator Pstn | Fixed/designated metadata | `2466` | `13` | `1118` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `105` | Product Programming | `3` | Association key `4` |
| `641` | Product Programming | `3` | Association key `4` |


| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `105` | Serial | `1` |
| `641` | Serial | `1` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `105` | `2` | `0` | `SecurityConfig_020030` | Parameter type `7`; payload not inspected |
| `105` | `2` | `2` | `SecurityConfig_0100` | Parameter type `7`; payload not inspected |
| `105` | `2` | `4` | `UNAVAILABLE_0000` | Parameter type `7`; payload not inspected |
| `641` | `2` | `2` | `SecurityConfig_0200` | Parameter type `7`; payload not inspected |
| `641` | `2` | `4` | `SecurityConfig_0200` | Parameter type `7`; payload not inspected |


Brand/line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `105` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `641` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

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
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | Not applicable | None | Not applicable | No relation-specific filters associated | Not applicable | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `203` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `13` - AI Control Unit With Communicator Pstn | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |


These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

U3500A printed/PDF p. 81 explicitly lists OPEN-SCS families `WHO 0`, `WHO 1`, `WHO 2`, `WHO 4`, `WHO 5`, `WHO 9`; its commands on pp. 69-80 include alarm status, auxiliary commands, scenarios and stored-event readback. These are published capabilities, not measured installed responses.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Commission through system learning, sensor/zone test, scenario and key setup, date/time and telephone-dialler configuration. The installer workflow separately exposes zones, devices, event history, automation associations, preferences, maintenance, jolly/directory numbers, call events, vocal messages and telephone commands. SecurityConfig transfers configuration/history, customizes voice messages and updates firmware. Three incorrect keys block arming/disarming/menu access for one minute. The Céliane manual’s English section repeats these commissioning and OPEN command functions for 067520. Telephone service compatibility and Contact ID monitoring are documented capabilities, not contemporary provider availability or installed behavior. Credentials and installation-specific values are not reproduced.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

## Source reconciliation

573934 and 067520 are explicit Legrand - Arteor/Céliane database identities. U3500A covers 573934/35; U3887A covers 067520. The adjacent 573935 model is not an extra member of this cluster. The rich installer/software configuration remains outside the database’s three sparse Object `13` fields; sparse fields do not negate those published functions. U3500A’s standby wording and DTMF/pulses versus DTMF-only statements are retained as separate source claims. The later Céliane manual is a different product-line scope, not proof that every Arteor physical dimension applies to Céliane.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `u3500a.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `u3501a_s_uk.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `U3887A.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `u3499a.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |

The Céliane appendix independently repeats the `125 x 128 x 31 mm`, supply, current, temperature and IP30 data; those facts therefore have direct support for both product lines. The physical rechargeable battery is documented in installation, while its exact chemistry/capacity is not fixed by the quoted technical tables.

## Evidence limits and open work

Battery replacement applicability, PSTN provider compatibility, per-line physical differences, installed firmware, telephone security behavior and device-specific captures remain open.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
