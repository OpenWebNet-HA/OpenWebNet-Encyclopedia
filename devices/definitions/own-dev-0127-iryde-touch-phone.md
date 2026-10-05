# Iryde Touch Phone

## Summary

Iryde Touch Phone combines telephone and two-wire video-door-entry functions in a device with a handset and 4.3-inch touchscreen. PSTN/PABX and SCS connections bring both communication systems to the unit, with hands-free operation and dedicated entry-function keys.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0127` | Project identity |
| Technical description | Iryde Touch Phone | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `345020`, `345021` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1175` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Video door entry system | Main system association |
| Item model / `modobj` | `165` | Main association; independent of project ID |
| Firmware definition | `68` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Audio video, User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `345020` | Established catalogue identity | Manufacturer database commercial record `1174` explicitly links this SKU to item `1175` |
| BTicino | `345021` | Established catalogue identity | Manufacturer database commercial record `1175` explicitly links this SKU to item `1175` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `345020-italian-product-sheet.pdf` | Exact Italian product export | `Retrieved 04/10/2026; old compliance-template date does not establish product publication date` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-1; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/0c/c3/0cc339212c6450a1e7069045024634f309606c2062734ba2cfafe7b941686230.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-345020) |
| `345021-italian-product-sheet.pdf` | Exact Italian product export | `Retrieved 04/10/2026; old compliance-template date does not establish product publication date` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-1; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/e0/68/e06864160cf7c67b074a53b8d46643790e9ff7d3d1b4c0e6f9c148c9c65790bc.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-345021) |
| `BT00650_b_IT.pdf` | Manufacturer legacy documentation | `BT00650_b_IT; 22/01/2014` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-5; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/5a/b8/5ab87783add80df4bc0d990f800b9a0297251e3f331522da35a8f7f4bde1c388.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/BT00650_b_IT.pdf) |
| `BT00650_b_EN.pdf` | Exact historical manufacturer documentation | `BT00650_b_EN; 22/01/2014` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-5; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/2f/19/2f194a23331d8b4371df7f2a4aa15f783b95cb5517b0e41b76b87ebb64129125.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/BT00650_b_EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `1175` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `18..27 Vdc` | `BT00650-b-EN/IT` printed/PDF pp. 1-5 |
| Bus draw | `35 mA standby; up to 160 mA telephone use; 350 mA ON; 20 mA with additional supply` | `BT00650-b-EN/IT` printed/PDF pp. 1-5 |
| Operating temperature | `5..45 °C` | `BT00650-b-EN/IT` printed/PDF pp. 1-5 |
| Display | `4.3-inch 16:9 colour LCD touch screen` | `BT00650-b-EN/IT` printed/PDF pp. 1-5 |
| Dimensions, technical sheets | `235 x 120 x 22 mm` | `BT00650-b-EN/IT` printed/PDF pp. 1-5 |
| Dimensions, Italian 345020 export | `235 x 120 x 20 mm` | `BT00650-b-EN/IT` printed/PDF pp. 1-5 |
| Mounting accessories | `345024 wall bracket; 345023 tabletop support` | `BT00650-b-EN/IT` printed/PDF pp. 1-5 |
| Interfaces | `PSTN/PABX; 2-wire SCS video; supplementary 1-2 supply; mini-USB` | `BT00650-b-EN/IT` printed/PDF pp. 1-5 |
| Controls | `backlit keypad; magnetic handset/Hall detection; handsfree speaker/microphone; camera, staircase, ringtone, handsfree and door-lock keys` | `BT00650-b-EN/IT` printed/PDF pp. 1-5 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1175` | Canonical catalogue |
| Technical item description | VideoTouchTelephone | Canonical catalogue |
| Item family | 0; key `26` | Canonical catalogue |
| Main system | Video door entry system; key `4` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `165` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `68` | `1` | `2` | `24` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `68` | `1` | `153` Telephonic Internal Unit | Fixed/designated metadata | `2270` | `475` | `948` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `68` | Product Programming | `3` | Association key `4` |


| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `68` | USB | `3` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `68` | `1` | `0` | `TiIrydeTouchPhone_0102` | Parameter type `7`; payload not inspected |


Brand/line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `68` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `68` | `N_1` | `0..9` | `0` | N |
| `68` | `N_2` | `0..9` | `0` | N |
| `68` | `P` | `0..9` | `0` | P |
| `68` | `M` | `0` | `0` | M |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `153` - Telephonic Internal Unit

Catalogue Object key `475` maps to external Object `153`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `N` | `0..3999` | `0` | Address |
| `P` | `0..95` | `0` | Associated external unit |
| `HAND_FREE` | `0` = Disable; `1` = Enable | `0` | HAND_FREE |
| `PRO_STUDIO` | `0` = Disable; `1` = Enable | `0` | Professional Studio |
| `DOOR_STATE` | `0` = Disable; `1` = Enable | `0` | Door state display |
| `PEOPLE_S` | `1..2`; `0` = No | `0` | PeopleSearching |
| `MENU_PRE` | `0..99` | `0` | MenuPreset |
| `RING_T_OUT` | `1..30` | `10` | RingTimeOut |
| `CALL_T_OUT` | `10..180` | `30` | Call timeout |
| `PE_T_OUT` | `3..90` | `6` | EUConnectionTimeOut |
| `PI_T_OUT` | `3..90` | `18` | IUConnectionTimeOut |
| `TEL_T_OUT` | `3..180` | `90` | TelConnectionTimeout |
| `ASS_SWITCH` | `0..95` | `0` | AssociatedSwitchboard |
| `BEEP` | `0` = Disable; `1` = Enable | `0` | BEEP |
| `IS_SLAVE` | `0` = Not slave; `1` = Slave | `0` | Slave |
| `RISER_EU` | `0..95` | `0` | Associated Riser EU |
| `VDEADDRESS1` | `0..99` | `0` | VDE additional address (CITO 1) |
| `VDEADDRESS2` | `0..99` | `1` | VDE additional address (CITO 2) |
| `VDEADDRESS1_ENABLE` | `0` = disable; `1` = enable | `0` | Enable VDEaddress1 (CITO1) |
| `VDEADDRESS2_ENABLE` | `0` = disable; `1` = enable | `0` | Enable VDEaddress2 (CITO2) |
| `VDEGENADDRESS_ENABLE` | `1` = enable | `0` | VDE general CITO enable |

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
| `DIMENSION 1` | Corroborate item model `165` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `153` - Telephonic Internal Unit | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |


These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Basic setup selects a language and exposes video/telephone/settings functions; physical N/P selects handset and associated entrance-panel addresses. PC software allows customized menus and MyHOME functions beyond that basic setup. Set termination for the actual bus topology. The sheet permits four ITPs without additional supply; simultaneous activation of multiple screens and telephone continuity during bus loss depend on supplementary power. The PABX example uses switchboard 345829; configure the presence of PABX in the menu/software. Door lock, intercom, camera cycling, office, paging, telephone routing and alarm/system menu pages depend on the installed system.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

## Source reconciliation

345020 and 345021 are explicitly co-listed as Iryde Touch Phone in the exact bilingual sheet and database. The 345020 product export reports 20 mm depth while both technical sheets report 22 mm; no source explains the measurement boundary. Handset/telephone UI capability is broader than the single configured Object `153`; it does not establish all displayed subsystem Objects as active device-local Modules. Labels/legend numbering in the sheet’s English translation are inconsistent; port names and diagrams govern the documented physical interface, not the shifted list indices.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `345020-italian-product-sheet.pdf` | Exact named product export; identity and available commercial/physical attributes retained; compliance-template date does not date the product. |
| `345021-italian-product-sheet.pdf` | Exact named product export; identity and available commercial/physical attributes retained; compliance-template date does not date the product. |
| `BT00650_b_IT.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `BT00650_b_EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |

## Evidence limits and open work

Exact software manual and model-specific firmware/update/reset procedure, depth clarification, concurrent handset behavior and diagnostic captures remain missing.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
