# F459T HVAC Driver Manager

## Summary

F459T is the HVAC Driver Manager reference explicitly identified in the manufacturer’s MyHOME Suite catalogue. Its retained implementation model supplies a Driver Manager Object with network-address and device-code settings. Exact-product manufacturer documentation has not been located, so its HVAC identity is established while supported integrations, physical construction and operating limits remain documentation gaps.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0209` | Project identity |
| Technical description | F459T HVAC Driver Manager | Canonical manufacturer catalogue |
| Commercial identities | `F459T` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `2335` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `141` | Main association; independent of project ID |
| Firmware definition | `907` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Gateways and interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F459T` | Established catalogue identity | Manufacturer database commercial record `2697` explicitly links this SKU to item `2335` |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `F459T` | Driver Manager HVAC | Canonical commercial record `2697` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2335`: complete retained canonical associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply and consumption | Not established | No exact F459T manufacturer electrical specification retained; F459 ratings excluded |
| Housing and physical interfaces | Not established | Catalogue connection labels are implementation associations, not an inspected housing or connector specification |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2335` | Canonical catalogue |
| Technical item description | Driver Manager HVAC | Canonical catalogue |
| Item family | Source placeholder description `0`; key `8` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `141` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `141` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Burglar alarm | private riser | Canonical item/bus relationship |
| Multimedia | private riser | Canonical item/bus relationship |
| Multimedia | public riser | Canonical item/bus relationship |
| Network | LAN | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `907` | `1` | `0` | `0` | `1` | Not catalogue default | Official |
| `907` | `1` | `0` | `1` | `1` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `907` | `1143` | Undefined (key `5`) | `0` | Extra | `2335_1.0_LGG\xml\Extra\extra.xml` |
| `907` | `1144` | Undefined (key `5`) | `0` | Protocol and other device parameters | `2335_1.0_LGG\xml\Protocol\protocol.xml` |

All 2 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

Builds `0` and `1` are two explicit rows attached to the same Official firmware `907` version `1`, revision `0`; the default flag is unset. They are not two commercial Devices or measured installed releases. Both parameter-file associations use LGG brand scope with line `0`; their XML payloads are absent from the reviewed catalogue evidence.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `907` | `1` | `142` Driver Manager | Fixed / designated metadata | `4822` | `642` | `2119` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

Slot `1` directly designates external Driver Manager Object `142` (database key `642`), with four reusable fields for static/DHCP selection, local IP, gateway enable and system code. `192.168.1.45` is a catalogue documentation default, not a verified installed endpoint. There are no Virgin, slot predicate, relation filter, conversion or package associations. Five catalogue bus scopes, including burglar-alarm and multimedia risers, do not establish corresponding physical connectors or HVAC protocol compatibility.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `907` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `907` | Ethernet | Canonical firmware/connection association |
| `907` | Ethernet over USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Exact-product procedure | No exact F459T manufacturer commissioning original located. Catalogue modes and paths in this dossier remain implementation metadata, with XML payloads and installed behavior unexamined. | Canonical item `2335` evidence |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `907` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `142` - Driver Manager

Catalogue Object key `642` maps to external Object `142`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.45` | Local IP address; public documentation value, not an observed installation |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

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

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `141` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `142` - Driver Manager | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `142` - Driver Manager | Integration function | `26` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The catalogue associates the programming modes and parameter paths listed under Configuration modes. Those associations provide an implementation inventory, not an inspected F459T installation procedure. Do not apply the F459 web credentials, supply ratings, driver lists or update procedures merely because the Driver Manager Object is reused.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

`EN_DEVICE` record 2697 explicitly links F459T to `EN_ITEM` 2335 and names Driver Manager HVAC. This establishes catalogue identity independently of PDF availability. Exact searches of BTicino and Legrand domains and both current / regional catalogue entry points found no exact manufacturer document: the global page returned 404, the Italian product route redirected to the catalogue home page and the export returned 500. Broader manufacturer guides describe F459, without the T suffix; they do not establish F459T physical equivalence or HVAC-driver compatibility. Secondary distributor listings were discovery leads, not primary verification of specifications or an EAN.

No exact-product document original is retained for this item. The canonical database is the source for the identity and configuration inventory; product-document discovery remains partial.

The 7 October review repeated exact-SKU manufacturer-domain searches and direct global/Italian entry checks. No exact manufacturer payload was established. Distributor listings remain discovery leads; their repeated EAN and electrical classifications have not been promoted to verified manufacturer facts. Catalogue commercial record `2697` is BTicino brand key `6`, line key `5`, while its parameter paths use LGG scope. Those independent metadata scopes do not change the explicit SKU-to-item relationship.

## Evidence limits and open work

Exact-product electrical ratings, housing, interfaces, manufacturer-verified EAN, HVAC driver / system compatibility, licensing, firmware packages and installation / update procedures remain undocumented here. This is a documentation gap, not an unresolved catalogue identity. Further manufacturer or regional / historical exact-SKU evidence is required to close it.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

The general Living Now 2026 catalogue was searched for an exact F459T reference and yielded F459 only. Its original is a discovery candidate excluded from incorporated evidence: 125579283 bytes exceeds the installed PDF archive helper’s 100 MiB limit. No derivative or compressed file substitutes for it. The exact F459T documentation gap therefore remains open; no F459 ratings were transferred.

Semantic acceptance of this bounded catalogue description does not close exact-product document discovery or archive coverage. Discovery completion covers the examined inventory and renewed search scope; archival coverage remains pending. No source from the unsuffixed F459 is substituted. Required follow-up is an exact F459T manufacturer specification covering electrical and mechanical limits, HVAC protocols/drivers and commissioning/licensing.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0201-0210-2026-10-07.md#own-dev-0209)
