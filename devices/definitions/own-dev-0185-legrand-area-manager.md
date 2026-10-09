# Legrand Area Manager

## Summary

Legrand 002645 Area Manager coordinates lighting scenarios and connects a BUS/SCS installation to an IP network. It combines scheduling, a lighting-manager role and an Open SCS gateway in the catalogue, with Ethernet access for building-level management.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0185` | Project identity |
| Technical description | Legrand Area Manager | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `002645` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1672` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `43` | Main association; independent of project ID |
| Firmware definition | `127` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `3` | Firmware metadata |
| Categories | Gateways and interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `002645` | Established catalogue identity | Manufacturer database commercial record `1676` explicitly links this SKU to item `1672` |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `002645` | Light manager control unit | Canonical commercial record `1676` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ex212001_657.pdf` | Historical lighting catalogue page | `Catalogue 2012–2013; extract ex212001_657` | Printed p. 657 / PDF p. 1: 002645 and 573960 exact-reference mentions; 573958 paragraph excluded from 573960 specifications. | [Archived original](https://archive.openwebnet-ha.org/sha256/40/0d/400d2496efd6d5d7d7ecb32711f9014db2d885f83849c64d8bbb5b262144f662.pdf) | [Publisher original](https://assets.legrand.com/general/legrand-exp/cexp2012-13/ex212001_657.pdf) |
| `le05228aa_en.pdf` | Assisted living technical guide | `LE05228AA-EN; April 2012` | Printed/PDF pp. 19, 34-35: illustrated topology, exact Area Manager technical box, terminal drawing and auxiliary supply; conflicting accessory values preserved. | [Archived original](https://archive.openwebnet-ha.org/sha256/ce/5e/ce5e8c0067a7633f761f4e0221e5fd7849f0cc171986bc16b1e628157d118ebb.pdf) | [Publisher original](https://assets.legrand.com/general/legrand-exp/np-ft-gt/le05228aa_en.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1672`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |
| `U3641A.pdf` | Exact Area Manager installation sheet | U3641A; 02/10-01 SY | Printed/PDF pp. 1–2: auxiliary/SCS draws, dissipation, Ethernet/maintenance connectors, indications and common-switch installation | [Archived original](https://archive.openwebnet-ha.org/sha256/1f/53/1f5315b6444cc760851ea8923e5b4ad0b60dac176a0e8e78543b639a854d0a30.pdf) | [Publisher source](https://assets.legrand.com/general/legrand-fr/np-ft-gt/u3641a.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Published supply label in catalogue / guide | `27 Vdc; exact installation sheet separately identifies the auxiliary input` | `le05228aa_en.pdf` printed/PDF p. 34; `ex212001_657.pdf` printed p. 657 / PDF p. 1 |
| Standby consumption | `1.5 W` | `le05228aa_en.pdf` printed/PDF p. 34; `ex212001_657.pdf` printed p. 657 / PDF p. 1 |
| Operating temperature | `5..40 °C` | `le05228aa_en.pdf` printed/PDF p. 34; `ex212001_657.pdf` printed p. 657 / PDF p. 1 |
| Protection / mounting | `IP20; 6 DIN modules (6 × 17.5 mm)` | `le05228aa_en.pdf` printed/PDF p. 34; `ex212001_657.pdf` printed p. 657 / PDF p. 1 |
| Auxiliary supply accessory | `063442 / 0 634 42; source voltages conflict` | `le05228aa_en.pdf` printed/PDF p. 34; `ex212001_657.pdf` printed p. 657 / PDF p. 1 |
| Connections | `Ethernet; SCS; separate auxiliary supply; reset control` | `le05228aa_en.pdf` printed/PDF p. 34; `ex212001_657.pdf` printed p. 657 / PDF p. 1 |
| Software packs | `048881 for operation; 048882 for supervision; historical catalogue scope` | `le05228aa_en.pdf` printed/PDF p. 34; `ex212001_657.pdf` printed p. 657 / PDF p. 1 |

### Exact installation-sheet details

| Property | Value | Evidence |
| --- | --- | --- |
| Auxiliary input / SCS draw | `27 Vdc` auxiliary supply; SCS draw `8 mA` | U3641A printed/PDF p. 1 |
| Auxiliary draw | `40 mA` at rest; `55 mA` during remote transfer | U3641A printed/PDF p. 1 |
| Maximum dissipated power | `1.5 W` | U3641A printed/PDF p. 1 |
| Network / maintenance | 10BaseT Ethernet; serial maintenance connector with interface 376000 / 49234 | U3641A printed/PDF p. 1 |
| Indications | Red flashes at startup/maintenance, steady in normal operation; green Ethernet indicator | U3641A printed/PDF p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1672` | Canonical catalogue |
| Technical item description | Light manager control unit | Canonical catalogue |
| Item family | Source placeholder description `0`; key `8` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `43` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `43` | Yes | Canonical item/system relationship |

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
| `127` | `2` | `0` | `1` | `3` | Catalogue default | Deprecated |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `127` | `950` | Legrand (key `2`) | `0` | external software | `AreaManager_0200` |

All 1 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

Firmware `127` is version/revision/build `2.0.1` and Deprecated in the retained catalogue. Its item-side `FW_VER` default `3.0.0` is a configuration value, not evidence of an additional firmware release. Gateway-field defaults do not override the separately documented network role or the three Module slots. The public LAN/address defaults remain templates, not installed network data.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `127` | `1` | `127` Lighting manager | Fixed / designated metadata | `675` | `127` | `470` |
| `127` | `2` | `61` Scenario scheduler | Fixed / designated metadata | `676` | `61` | `471` |
| `127` | `3` | `150` Gateway Open SCS | Fixed / designated metadata | `677` | `150` | `472` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `127` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `127` | Ethernet | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Management / interface | Time, lighting and presence scenarios; BUS/SCS to IP bridge | `ex212001_657.pdf` printed p. 657 / PDF p. 1; `le05228aa_en.pdf` pp. 19, 34-35 |
| Software packs | 048881 operation; 048882 supervision; historical catalogue scope | `ex212001_657.pdf` printed p. 657 / PDF p. 1; `le05228aa_en.pdf` pp. 19, 34-35 |
| Illustrated ward topology | 175 SCS addresses / 45 rooms; installation example, not universal firmware capacity | `ex212001_657.pdf` printed p. 657 / PDF p. 1; `le05228aa_en.pdf` pp. 19, 34-35 |
| Auxiliary source conflict | Catalogue: 12 Vdc/1.2 A for 063442; guide supply page: 27 Vdc/600 mA; device drawing labels 12 Vdc | `ex212001_657.pdf` printed p. 657 / PDF p. 1; `le05228aa_en.pdf` pp. 19, 34-35 |
| Commissioning details | Complete exact-device transfer and reset sequence unestablished | `ex212001_657.pdf` printed p. 657 / PDF p. 1; `le05228aa_en.pdf` pp. 19, 34-35 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `127` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `127` | `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `127` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `127` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `127` | `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `127` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `127` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity; Local Dynamic IP |
| `127` | `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity; Public Dynamic IP |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `61` - Scenario scheduler

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity |
| `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` | Public IP address; public documentation value, not an observed installation |
| `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Object `127` - Lighting manager

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Object `150` - Gateway Open SCS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
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
| `DIMENSION 1` | Corroborate item model `43` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `127` - Lighting manager | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `61` - Scenario scheduler | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `150` - Gateway Open SCS | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `127` - Lighting manager | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `61` - Scenario scheduler | Integration function | `26` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `150` - Gateway Open SCS | Integration function | `26` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The catalogue registers lighting-manager, scenario-scheduler and gateway Objects. Configure only the actual Firmware/Object roles and restrictions below. The historical catalogue names software packs 048881/048882; the retained guide gives an IP-backbone example with 175 SCS addresses and 45 rooms per illustrated ward (printed/PDF p. 19), not a universal software limit. A complete exact-product commissioning manual and configuration transfer sequence are still required.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

The exact U3641A installation sheet requires the SCS supply 03560 and auxiliary supply 63442 to be controlled by the same common mains switch (printed/PDF p. 2). Its configuration instructions refer to a supplied CD manual, which has not been retained or examined. The maintenance connector is a separately documented serial route; it does not change the catalogue Ethernet connection association.

## Source reconciliation

The assisted-living guide prints 27 Vdc in the Area Manager technical box but labels the auxiliary terminal 12 Vdc in the drawing; its 063442 supply page (printed/PDF p. 35) specifies 27 Vdc/600 mA, whereas the 2012–13 catalogue specifies 12 Vdc/1.2 A for 063442. These source-specific values conflict and are not silently unified. The 175-address example is installation topology, independent of catalogue Module count.

U3641A identifies the auxiliary input as 27 Vdc and gives independent SCS and auxiliary current draws. This supports the 27 V accessory row in the assisted-living guide, while the guide’s 12 V terminal annotation and historical catalogue accessory 12 V / 1.2 A remain conflicting evidence. The installation sheet calls 1.5 W maximum dissipated power; the catalogue/guide call 1.5 W standby consumption. These descriptions are preserved rather than treated as the same operating condition. The 175-address / 45-room ward illustration is an example topology, not a firmware Module count or a universal system capacity.

## Evidence limits and open work

Auxiliary input suitability and accessory revision require confirmation from an exact hardware label or installation instruction. Full commissioning workflow and runtime gateway behavior remain uncorroborated.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0181-0190-2026-10-07.md#own-dev-0185)
