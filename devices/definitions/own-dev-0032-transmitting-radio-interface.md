# Transmitting radio interface

## Summary

This transmitting interface links configured SCS controls to compatible 868 MHz radio devices. It allows commands from the wired installation to reach the radio side, with the transmitted action determined by its configured role.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0032` | Project identity |
| Technical description | SCS-powered radio transmitting interface | Catalogue + official documentation |
| Commercial identities | `HC/HS4576`, `HD4576`, `L/N/NT4576` | Catalogue |
| Catalogue item | `34` - “Transmitting radio interface” | Implementation evidence |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `21` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `215` | Implementation evidence |
| Declared Modules | `1` | Implementation evidence |
| Categories | Radio interface, Control bridge, Lighting / Automation | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC/HS4576` | Established identity | Canonical catalogue; canonical commercial record `34`; Commercial identity of this Technical Device |
| BTicino - LivingLight | `L/N/NT4576` | Established identity | Canonical catalogue; canonical commercial record `1828`; Commercial identity of this Technical Device |
| BTicino - Axolute | `HD4576` | Established identity | Canonical catalogue; canonical commercial record `1829`; Commercial identity of this Technical Device |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `AUTOMATISME.pdf` | MyHOME automation guide | historical publisher guide | 4576 transmitting interface configuration: printed p. 155 / PDF p. 157; interface technical data printed p. 173 / PDF p. 175 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply / maximum current | `27 Vdc` / `40 mA` | `AUTOMATISME.pdf`, printed pp. 155, 173 / PDF pp. 157, 175; `HC/HS4576` and suffixed `L/N/NT4576N` rows |
| Operating temperature | `-5..35 °C` | `AUTOMATISME.pdf`, printed pp. 155, 173 / PDF pp. 157, 175 |
| Radio / open-field range | `868 MHz` / `100 m`; metal and concrete reduce range | `AUTOMATISME.pdf`, printed pp. 155, 173 / PDF pp. 157, 175 |
| Mounting / connection | 2 flush-mounted modules; SCS terminal, LED and programming key | `AUTOMATISME.pdf`, printed pp. 155, 173 / PDF pp. 157, 175 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `34` | Canonical catalogue |
| Technical item description | Transmitting radio interface | Canonical catalogue |
| Item family | `27` - Radio device | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `21` | AS_ITEM_SYSTEM |
| Commercial records | `3` | EN_DEVICE |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `21` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `215` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No AS_FW_PACKAGE association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `215` | `1` | `172` Radio Interface Transmitter | Fixed/designated metadata | `1506` | `172` | `754` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

Slot `1` is fixed Object `172`, Radio Interface Transmitter.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `215` | Physical configuration | `0` | Canonical firmware/mode association |
| `215` | Virtual Configuration | `1` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `215` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `215` | `A` | `0..9` | `0` | A; Environment |
| `215` | `PL` | `0..9` | `0` | PL; Light Point |
| `215` | `M` | `0..1` | `0` | M; mode (0/1) |

Firmware `215` narrows `M` to `0` / `1`. The reusable transmitter Object has a wider generic mode family, which must not be projected back onto this Device.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `172` - Radio Interface Transmitter

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..9` | `0` | Area |
| `PL` | `0..9` | `0` | Light point |
| `M` | `1`; `6..8`; `14` = `CEN`; `0` = None | `0` | Modality; Mode (0,1,6,7,8,`CEN`) |

### Device-specific interpretation

Firmware `M=0..1` and reusable Object `172` modes `0/1/6/7/8/CEN` have different scopes. The transmitter guide documents logical extension with `M=1`; it does not establish the other reusable modes. Filter `1631` references `TYPE_CONTACT` in another Object scope and supplies no legal values. It does not establish a contact input on this radio transmitter.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `215` | `172` | `1631` | `TYPE_CONTACT` | No legal values specified in source (entire reusable range retained) | `0` | Contact type; field definition belongs to a different Object scope; do not alias it to a similarly named field |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 21` and the 4576 transmitter family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware rather than assuming wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm fixed Object `172`, Radio Interface Transmitter | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the configured SCS-side address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `A`, `PL`, `M` and the Device-specific contact-type restriction | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The interface bridges configured SCS control semantics to the supported radio side. Functional meaning depends on the configured command role; it should not be hard-coded as a single lighting action.

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact technical item is currently retained.

## Programming

Treat firmware 215's `M` values 0/1 domain as authoritative for this Device unless direct revision-specific evidence establishes additional modes.

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Logical extension | Set physical `M=1`. Only one transmitter is allowed in the documented wired installation. | `AUTOMATISME.pdf`, printed pp. 155, 173 / PDF pp. 157, 175 |
| Address partition | A/PL divide wired and radio ranges; the guide example boundary `62` reserves `11..61` for wired devices and `63..99` for radio devices. | `AUTOMATISME.pdf`, printed pp. 155, 173 / PDF pp. 157, 175 |
| Coexisting receiver | The guide permits its non-SB receiver only in logical extension `M=1` or remote-scenario `M=6/7/8`; it recommends adjacent interface addresses. | `AUTOMATISME.pdf`, printed pp. 155, 173 / PDF pp. 157, 175 |

## Source reconciliation

The canonical catalogue establishes the one-slot Radio Interface Transmitter model and the three grouped commercial records. Official historical documentation corroborates the family role and physical format, but suffix naming differs between the implementation catalogue and printed guide; that mismatch remains explicit.

The guide directly lists `HC/HS4576` and the suffixed `L/N/NT4576N`; the database lists unsuffixed `L/N/NT4576` plus `HD4576`. These explicit catalogue identities remain established, but equivalence of each historical suffix and HD electrical ratings is not independently proved. The guide also calls a transmitter diagram a receiver and repeats inconsistent references in surrounding text; those labels are not used to reclassify the Device. Firmware `M=0..1` is narrower than reusable Object `172` modes; no examined source establishes the extra modes on this transmitter.

## Evidence limits and open work

- Recover a dedicated publisher technical sheet for the exact database-listed 4576 variants if one exists.
- Hardware-corroborate firmware identity and transmitted command behavior.
- Resolve the Contact type filter into a human-readable Device-specific rule.

- Exact unsuffixed `L/N/NT4576` and `HD4576` electrical/configuration revisions were not retained; historical suffixed guide figures remain source-scoped. A separate transmitter pairing instruction was not found in the examined manufacturer sources.

- Linked programming software/help, other product-download revisions and unrelated multi-product guide pages were not inspected; the Documentation table gives the examined scope. Catalogue mode associations and reusable schemas are not observed installed behavior.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0031-0040-2026-10-06.md#own-dev-0032)
