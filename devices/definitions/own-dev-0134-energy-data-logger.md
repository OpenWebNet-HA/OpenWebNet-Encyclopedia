# Energy data logger

## Summary

This DIN energy data logger collects readings from up to ten electricity, water, gas or heat lines through compatible meters and pulse interfaces. Ethernet access, detailed electrical recording, export and microSD backup support consumption review over time.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0134` | Project identity |
| Technical description | Energy data logger | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `F524`, `003566` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1475` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | New energy saving and load control | Main system association |
| Item model / `modobj` | `13` | Main association; independent of project ID |
| Firmware definition | `98` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Energy management, Gateways and interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F524` | Established catalogue identity | Manufacturer database commercial record `1475` explicitly links this SKU to item `1475` |
| Legrand | `003566` | Established catalogue identity | Manufacturer database commercial record `1986` explicitly links this SKU to item `1475` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F524` | `8005543448984` | [Archived original](https://archive.openwebnet-ha.org/sha256/78/fc/78fc076141a2ad69164d75249a2577c63f1422990965db7d88655a3bf94e562e.pdf), `F524-publisher-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

### Catalogue labels and classifications

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `F524` | Energy data logger | Canonical commercial record `1475` |
| `003566` | Energy data logger | Canonical commercial record `1986` |

Both commercial records are enabled for catalogue display, have no visibility-type value, and are not marked dependent or gateway in this historical commercial table. These classifications do not establish market availability, installed state or functional gateway capability. Empty or truncated internal description labels are not used to infer additional product features.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MyHOME-Technical-Guide.pdf` | English system technical guide | `AD-EXMH25GT; Versione 6/2025 printed on rear cover` | AD-EXMH25GT, Versione 6/2025 rear-cover label; exact F524 entry printed/PDF p. 101 examined. No exact 3456/F450 match; other product ratings/wiring excluded from those items. | [Archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) | [Publisher original](https://www.bticino.com/sites/default/files/2024-02/MyHOME%20Technical%20Guide.pdf) |
| `MQ00521-b-EN.pdf` | Technical Sheet MQ00521-B-EN | `MQ00521-b-EN; 09/06/2014` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-1; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/f8/e2/f8e2e80cb63d90c27d42c42bc2e8445cbf99a581a7a432adbe3038849f4b2044.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MQ00521-b-EN.pdf) |
| `O2074C.pdf` | Instruction Use O2074C | `O2074C-01PC-12W45` | Exact F524 4-page multilingual mounting leaflet; English reset/LED instructions on pp. 1–2 examined, translations not fully rechecked. | [Archived original](https://archive.openwebnet-ha.org/sha256/d2/f4/d2f4b257e60493b94067392cf25173a90fee831bb1c6b2dd9613ff91bfa7ecec.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/O2074C.pdf) |
| `RA00040AB_I_EN.pdf` | Technical Guide RA00040AB_I_EN | `RA00040AB_I_EN; source filename revision; printed publication date not established` | Exact F524 24-page installer manual examined in full; commissioning/LED/reset/network and `5..45` °C rating. Historical Windows/browser requirements, not modern compatibility evidence. | [Archived original](https://archive.openwebnet-ha.org/sha256/32/f0/32f016c987a230e14cfbec922206a62cb4d5d6d2c68add541235d7bd0f2e445b.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00040AB_I_EN.pdf) |
| `RA00040AC_U_EN.pdf` | Technical Guide RA00040AC_U_EN | `RA00040AC_U_EN; source filename revision; printed publication date not established` | Exact F524 32-page user manual examined in full; energy/tariff/virtual-line/admin/data/IP recovery functions and source limits. | [Archived original](https://archive.openwebnet-ha.org/sha256/4d/df/4ddf61377d61579eade05ba8958a938b426b20c1157027517de374107fb528d4.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00040AC_U_EN.pdf) |
| `RA00040AF_I_EN.pdf` | Technical Guide RA00040AF_I_EN | `RA00040AF_I_EN; source filename revision; printed publication date not established` | Exact F524/003566 16-page installer manual examined in full; additional load-management function and retained reset/network/`5..45` °C scope. | [Archived original](https://archive.openwebnet-ha.org/sha256/87/4f/874fb89da0129e8582e4c2c5a9a1ff9fabc513bb6870f8a0a1febf851a9d0f47.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00040AF_I_EN.pdf) |
| `RA00040AF_U_EN.pdf` | Technical Guide RA00040AF_U_EN | `RA00040AF_U_EN; source filename revision; printed publication date not established` | Exact F524/003566 36-page user manual examined in full; energy and added F521 load forcing/actuator setup, reset/IP differences and source limits. | [Archived original](https://archive.openwebnet-ha.org/sha256/ce/5c/ce5c45316fdf9df635d1ac94de35a1f5d44979c5dfcce7b2fc9b48dd9617fbda.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00040AF_U_EN.pdf) |
| `F524-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 04.10.2026` | Exact references, specifications and configuration/wiring as applicable: PDF pp. 1-3; printed pages coincide where numbered; unnumbered product exports are identified separately. | [Archived original](https://archive.openwebnet-ha.org/sha256/78/fc/78fc076141a2ad69164d75249a2577c63f1422990965db7d88655a3bf94e562e.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-F524&include_technical=1) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `1475` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply | `18..27 Vdc` | `MQ00521-b-EN` p. 1 |
| Current draw | `30 mA` | `MQ00521-b-EN` p. 1 |
| Operating temperature, technical sheet | `5..40 °C` | `MQ00521-b-EN` p. 1 |
| Operating temperature, installation manuals | `5..45 °C` | `RA00040AB_I_EN` p. 23; `RA00040AF_I_EN` p. 14 |
| Mounting | `1 DIN module` | `MQ00521-b-EN` p. 1 |
| Energy lines | `maximum 10 electric/water/gas/heat lines` | `MQ00521-b-EN` p. 1 |
| Electrical sources | `F520 meters or F521 central units` | `MQ00521-b-EN` p. 1 |
| Non-electrical sources | `3522 pulse-counter interfaces` | `MQ00521-b-EN` p. 1 |
| Detailed electric recording | `15-minute intervals; Excel export` | `MQ00521-b-EN` p. 1 |
| Electric tariffs | `up to 8 time bands/tariffs` | `MQ00521-b-EN` p. 1 |
| Backup | `microSD; daily per-line consumption records` | `MQ00521-b-EN` p. 1 |
| Interfaces | `Ethernet; SCS; reset key; status LED` | `MQ00521-b-EN` p. 1 |

### Publisher export attributes

These are the captured publisher classification values for the named variants. They do not override a technical sheet’s ratings or prove runtime protocol support. A negative radio-bus/connected-object classification is not evidence against separately documented gateway or Wi-Fi behavior.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `F524` export p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `F524` export p. 2 |
| Bus system radio frequency | `No` | `F524` export p. 2 |
| Bus system LON | `No` | `F524` export p. 2 |
| Bus system Powernet | `No` | `F524` export p. 2 |
| Other bus systems | `Other` | `F524` export p. 2 |
| Model | `Energy meter` | `F524` export p. 2 |
| Connection type | `Convertible` | `F524` export p. 2 |
| Reactive power | `No` | `F524` export p. 2 |
| Approved according to PTB | `No` | `F524` export p. 2 |
| S0 impulse interface | `None` | `F524` export p. 2 |
| Tariff switch | `Yes` | `F524` export p. 2 |
| Connected object | `No` | `F524` export p. 2 |

### Published network and setup indications

| State | LED indication | Source |
| --- | --- | --- |
| no network / awaiting address | slow regular red | AF installer p. 5 |
| awaiting configuration | slow regular green | AF installer p. 5 |
| time not set | fast regular green | AF installer p. 5 |
| configured/operating | slow irregular green | AF installer p. 5 |
| IP or microSD error | fast red/green | AF installer p. 5 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1475` | Canonical catalogue |
| Technical item description | Energy data logger | Canonical catalogue |
| Item family | 0; key `8` | Canonical catalogue |
| Main system | New energy saving and load control; key `20` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `13` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| New energy saving and load control | `13` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `98` | `1` | `0` | `1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `98` | `53` | BTicino (key `1`) | `0` | Extra | `1475_1.0_BT\xml\Extra\extra.xml` |
| `98` | `55` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1475_1.0_BT\xml\Protocol\protocol.xml` |
| `98` | `339` | Legrand (key `2`) | `0` | Extra | `1475_1.0_LG\xml\Extra\extra.xml` |
| `98` | `340` | Legrand (key `2`) | `0` | Protocol and other device parameters | `1475_1.0_LG\xml\Protocol\protocol.xml` |

All 4 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `98` | `1` | `219` Energy Data Logger | Fixed/designated metadata | `1391` | `528` | `737` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `98` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `98` | Ethernet | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `98` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `98` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `98` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity; Local Dynamic IP |
| `98` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `98` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `219` - Energy Data Logger

Catalogue Object key `528` maps to external Object `219`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
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

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `13` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `219` - Energy Data Logger | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |

These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Configure built-in web pages and set date/time before enabling logging. The installer guide uses a ten-second hold for restart and a twenty-second hold for restart plus dynamic IP selection. Distinguish a device restart, IP reset and administrator data erase. Normal users view energy and, in the AF revision, load-control/forcing pages; administrators configure physical/virtual lines, actuators, credentials and IP authorization. Virtual lines can sum/difference existing lines or multiply a line by a factor >=0.001; a virtual address and unit must be assigned. Water/gas conversion uses single rates without electric time bands. Use actual electrical-line integration, not mathematical virtual lines, to infer physical channels.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

### Energy-line setup and data boundaries

AC user pp. 11–28 and AF user pp. 11–32 separate display/exports, tariff setup and administrator configuration. Set real meter/interface addresses in `1..127`, the family, unit, description, decimal precision and consumption/production direction. Virtual sum/difference/multiplication lines have their own display address and unit; multiplication factors must be at least 0.001. The examples' virtual addresses do not describe an installed channel allocation.

Electric tariffs can use up to eight bands; coverage must span the full day, week and holidays. Other consumption tariffs are single-rate. Holiday customization is lost when the year changes. User and installer passwords are separate roles, with 8–12-character changes and security-question recovery to the published factory password; these are manufacturer defaults and procedures, not installation credentials. Data Reset deletes selected energy-line data; it is distinct from the front-panel restart/IP procedures. AF adds actuator phase/priority configuration and F521 load status/temporary forced reactivation; the logger does not replace the central unit's shedding logic.

The last-12-month display/export and optional microSD backup are documented, but card capacity, filesystem, failure recovery and guaranteed physical retention are not established here. The pulse-interface example states 254 pulses/hour without independently establishing its applicability to every supported interface revision. Do not use a virtual multiplier to infer a larger physical pulse acquisition rate.

Installation AB p. 22 and AF p. 13 recover the published fixed IP/mask through a power-up/reset sequence. AC user p. 30 instead describes automatic IP assignment; AF user p. 34 describes the fixed pair without the power-up distinction. Preserve these revision/procedure differences alongside the common timed 10/20-second reset controls. Legacy Windows discovery and listed browser versions document historical setup; current operating-system/browser support remains untested.

## Source reconciliation

The AB installer and AC user editions are preserved beside both AF editions. AF installer reorganizes legacy operating-system/network instructions; AF user adds load-control pages and administrator actuator configuration absent from AC. These are material UI/document revisions, not catalogue Firmware version proof. The one-page sheet’s ten-line/logging/tariff claims agree with the guides. The web administrator pages expose more capability than the catalogue’s single energy-data-logger Object; they do not establish extra local Modules.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `MyHOME-Technical-Guide.pdf` | June 2025 shared energy guide: wiring, load control and consumption topology; no exact 3456/F450 match and no specifications transferred to those products. |
| `MQ00521-b-EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `O2074C.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `RA00040AB_I_EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `RA00040AC_U_EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `RA00040AF_I_EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `RA00040AF_U_EN.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `F524-publisher-product-sheet.pdf` | Captured exact-variant identity and complete technical classification attributes tabulated above; document links are discovery provenance, not additional independently verified capability. |

### Semantic review findings

One fixed Object `219`, no Virgin/conditions/filters/conversions, and four XML parameter associations describe historical catalogue coverage, not ten local meter Objects. The source's ten energy lines are collected from external devices; virtual arithmetic does not create physical channels. The AB/AF installers retain a 10-second restart and 20-second restart plus dynamic-IP selection. Their troubleshooting also describes powering while holding reset to recover a fixed factory address/mask, whereas AC user troubleshooting describes DHCP recovery and AF user troubleshooting specifies the fixed pair: these distinct and partly inconsistent procedures must not be collapsed into a universal factory reset. Installation manuals permit `5..45 °C`; the exact b technical sheet specifies `5..40 °C`. Both ranges are attributed rather than merged. AF adds F521 load status/forcing and actuator configuration beyond AC. The user guides' last-12-month export/display interval is not an independently proven storage-retention guarantee. The generic 254-pulses/hour example is not established as a hardware limit for every `3522`/`3522N` revision. Published OPENWebNet consumption access does not supply a complete diagnostic/protocol implementation here.

The retained June 2025 guide's exact F524 entry is printed/PDF p. 101. It names `3522N` where the older b sheet/manuals name `3522`; their payloads and firmware-specific support are not established by substituting the identifiers. Adjacent F520 photovoltaic wiring and unrelated range pages do not establish F524 production wiring. Its current export describes external consumption sources and OPENWebNet consumption display while classification says Energy meter and S0 interface None; those labels do not create a direct toroid/pulse input on the logger.

## Evidence limits and open work

Supported microSD capacity/formats, exact HTTP/OPEN diagnostics, retention limits, installed revision and backup/restore behavior remain uncorroborated.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0131-0140-2026-10-06.md#own-dev-0134)
