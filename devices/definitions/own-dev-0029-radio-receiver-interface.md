# Radio receiver interface

## Summary

This radio receiver converts compatible 868 MHz wireless controls into SCS bus actions. Configured functions include sound-system switching, volume and source selection, with other roles determined by the selected operating mode.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0029` | Project identity |
| Technical description | Flush-mounted 868 MHz radio-to-SCS receiving interface | Catalogue + official documentation |
| Commercial identities | `HC/HS/HD4575`, `L/N/NT4575`, `L/N/NT4575N` | Catalogue |
| Catalogue item | `28` - “Receiving radio interface” | Implementation evidence |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `20` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `214` | Implementation evidence |
| Declared Modules | `1` | Implementation evidence |
| Categories | Radio interface, Control bridge | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino - Axolute | `HC/HS/HD4575` | Established identity | canonical commercial record `28`; Commercial identity of this Technical Device | Canonical catalogue |
| BTicino - LivingLight | `L/N/NT4575` | Established identity | canonical commercial record `1839`; Commercial identity of this Technical Device | Canonical catalogue |
| BTicino - LivingLight | `L/N/NT4575N` | Established identity | canonical commercial record `1840`; Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `mh_diff-sonore2008.pdf` | Radio/wired interface and sound-system technical guide | historical publisher guide | 4575 radio/wired interface: printed p. 99 / PDF p. 99; installation/configuration context printed pp. 60-61 / PDF pp. 60-61 and 66-67 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/f4/96/f496f0943750657477c03e43eae6708271a8e798101831991ebc02904673dccd.pdf) | [Publisher PDF](https://assets.legrand.com/general/cession/bt/np-ft-gt/mh_diff-sonore2008.pdf) |

The printed and 1-based PDF page locators remain unresolved and are retained explicitly as an evidence gap.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply | `27 Vdc` | `mh_diff-sonore2008.pdf` |
| Radio frequency | `868 MHz` | `mh_diff-sonore2008.pdf` |
| Published current draw | `2 mA` for the documented `L/N/NT4575N` and `HC/HS4575` variants | `mh_diff-sonore2008.pdf` |
| Mounting | 2 wiring-device modules | `mh_diff-sonore2008.pdf` |
| Operating temperature | `5..35 °C` | `mh_diff-sonore2008.pdf` |
| Service interface | status LED and programming micro-button | `mh_diff-sonore2008.pdf` |
| Bus connection | SCS BUS connector | `mh_diff-sonore2008.pdf` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `28` | Canonical catalogue |
| Technical item description | Receiving radio interface | Canonical catalogue |
| Item family | `27` - Radio device | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `20` | AS_ITEM_SYSTEM |
| Commercial records | `3` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `214` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Firmware `214` is wildcard `-1.-1.-1` and declares one Module.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `214` | `1` | `27` Radio receiver | Fixed/designated metadata | `1010` | `27` | `607` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

The single Module resolves to Object `27`, **Radio receiver**. No Virgin Object is declared for this firmware.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `214` | `1` | `1` | Virtual Configuration |
| `214` | `3` | `0` | Physical configuration |

Physical Configuration and Virtual Configuration are declared.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `214` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `214` | `A` | `0..9` | `0` | A; Environment |
| `214` | `PL` | `0..9` | `0` | PL; Light Point |
| `214` | `M` | `0..1`; `6..8`; `14` = `CEN` | `0` | M; Mode (0,1,6,7,8,`CEN`) |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `A` | `0..9` | area / environment configurator |
| `PL` | `0..9` | light-point configurator |
| `M` | `0` / `1` / `6` / `7` / `8` / `CEN` | operating / function mode |


The firmware exposes only `A`, `PL`, `M` and `AID`. The reusable radio-receiver Object uses the corresponding `MOD` concept.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `27` - Radio receiver

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..9` | `0` | Area |
| `PL` | `0..9` | `0` | Light point |
| `MOD` | `1`; `6..8`; `14` = `CEN` | `1` | Modality; Mode (1,6,7,8,`CEN`) |


### Product interpretation and source differences

**Object `27` - Radio receiver - product interpretation.**

**Firmware relationship.** No additional Object/Firmware range filter in the catalogue.

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

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
| `DIMENSION 1` | resolve `modobj = 20` and the 4575 radio-interface family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | record installed firmware rather than assuming wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm the single Radio-receiver Object | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the configured SCS-side address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `A`, `PL`, `M` and Device-specific radio/contact configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The official documentation shows that the receiver can translate radio controls into SCS functions. A sound-system guide specifically documents amplifier on/off, volume, source selection and radio-station/track changes when appropriately configured. Other configured modes must be interpreted from their own functional context.

## Observed behavior and corroboration

No sanitized first-hand capture for this exact receiver is currently retained.

## Programming

Preserve the configured `M/MOD` role, including `CEN`, rather than assuming all received radio commands are ordinary lighting commands.

## Source reconciliation

The canonical database and publisher technical guide agree on a one-Module radio receiver with physical configurators and SCS BUS connection. The official guide directly covers two of the catalogue's reference forms; the remaining grouped references are catalogue-correlated and should not be represented as separately documented variants.

## Evidence limits and open work

- Add sanitized hardware and pairing traces.
- Recover dedicated documentation for the catalogue-only `HD4575` and `L/N/NT4575` forms if distinct publisher sheets exist.
- Map each `M/MOD` value to verified emitted OpenWebNet behavior.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [mh_diff-sonore2008.pdf](https://archive.openwebnet-ha.org/sha256/f4/96/f496f0943750657477c03e43eae6708271a8e798101831991ebc02904673dccd.pdf)
