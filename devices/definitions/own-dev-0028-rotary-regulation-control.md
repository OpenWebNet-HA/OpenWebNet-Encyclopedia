# Rotary regulation control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0028` | Project identity |
| Technical description | Flush-mounted rotary SCS control | Catalogue + official documentation |
| Commercial identities | `HC/HS/HD4563`, `L/N/NT4563` | Catalogue |
| Catalogue item | `25` - “Regulation rotative control” | Implementation evidence |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `11` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `213` | Implementation evidence |
| Declared Modules | `1` | Implementation evidence |
| Categories | Control, Lighting/Automation command | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino - Axolute | `HC/HS/HD4563` | Established identity | canonical commercial record `25`; Commercial identity of this Technical Device | Canonical catalogue |
| BTicino - LivingLight | `L/N/NT4563` | Established identity | canonical commercial record `1838`; Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `mh_diff-sonore2008.pdf` | Two-wire sound-system technical guide | historical publisher guide | 4563 rotary-control specification: printed p. 100 / PDF p. 100; sound-function configuration context printed p. 83 / PDF p. 83 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/f4/96/f496f0943750657477c03e43eae6708271a8e798101831991ebc02904673dccd.pdf) | [Publisher PDF](https://assets.legrand.com/general/cession/bt/np-ft-gt/mh_diff-sonore2008.pdf) |
| `AUTOMATISME.pdf` | MyHOME automation guide | historical publisher guide | No 4563-family reference found in this retained guide; generic system context only, not Device-specific specification evidence | [Archived PDF](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

The printed and 1-based PDF page locators remain unresolved and are retained explicitly as an evidence gap.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 wiring-device modules | `mh_diff-sonore2008.pdf` |
| SCS operating supply | `18..27 Vdc` | `mh_diff-sonore2008.pdf` |
| Maximum current draw | `5 mA` | `mh_diff-sonore2008.pdf` |
| Operating temperature | `5..35 °C` | `mh_diff-sonore2008.pdf` |
| Local interface | central pushbutton plus rotary knob | `mh_diff-sonore2008.pdf` |
| Published local actions | `ON`/`OFF`, programmed radio-station or track change, and volume adjustment | `mh_diff-sonore2008.pdf` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `25` | Canonical catalogue |
| Technical item description | Regulation rotative control | Canonical catalogue |
| Item family | `1` - Control | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `11` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `213` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Firmware `213` is wildcard `-1.-1.-1` with one Module.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `213` | `1` | `451` Knob control | Fixed/designated metadata | `1009` | `451` | `606` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

The Module resolves to Object `451`, **Knob control**, a one-slot Object associated with Automation and the relevant command-control collections. No Virgin Object is declared for this firmware.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `213` | `1` | `1` | Virtual Configuration |
| `213` | `3` | `0` | Physical configuration |

Physical Configuration and Virtual Configuration are declared.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `213` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `213` | `A` | `0..9` | `0` | A; Environment |
| `213` | `PL` | `0..9` | `0` | PL; Light Point |
| `213` | `M` | `0`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `14` = `CEN`; `15` = `PUL` | `0` | M; Mode cmd (`O/I`,`OFF`,`ON`,`PUL`,SU_GIU,SU_GIU_M) |
| `213` | `LIV1` | `0..99` | `1` | LIV1; Configurator LIV1 |
| `213` | `LIV2` | `0..99` | `1` | LIV2; Configurator LIV2 |
| `213` | `SPE` | `0..9` | `0` | SPE; Special function command control (0-9) |
| `213` | `I` | `0`; `14` = `CEN` | `0` | I; Configurator I |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `A` | `0..9` | area / environment configurator |
| `PL` | `0..9` | light-point configurator |
| `M` | `0` / `O/I` / `OFF` / `ON` / `UP/DOWN` / `UP/DOWN` monostable / `CEN` / `PUL` | operating / function mode |
| `LIV1` | `0..99` | first regulation level |
| `LIV2` | `0..99` | second regulation level |
| `SPE` | `0..9` | special-function selector |
| `I` | `0` / `CEN` | additional function selector |


`LIV1` / `LIV2` are the two regulation-level fields. `SPE` and `I` are additional command selectors whose semantics depend on the selected operating mode.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `451` - Knob control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..9` | `0` | Area |
| `PL` | `0..9` | `0` | Light point |
| `M` | `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `14` = `CEN`; `15` = `PUL`; `0` = None | `0` | Modality; Mode cmd (`O/I`,`OFF`,`ON`,`PUL`,SU_GIU,SU_GIU_M) |
| `LIV1` | `0..99` | `1` | Configurator LIV1 |
| `LIV2` | `0..99` | `1` | Configurator LIV2 |
| `SPE` | `0..9` | `0` | Special function command control (0-9) |
| `I` | `0` = None; `14` = `CEN` | `0` | Configurator I |


### Product interpretation and source differences

**Object `451` - Knob control - product interpretation.**

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
| `DIMENSION 1` | resolve `modobj = 11` and the 4563 rotary-control family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | record installed firmware rather than assuming wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm the single Knob-control Object | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the configured control address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `M`, `LIV1`, `LIV2`, `SPE` and `I` together with the address fields | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The selected command mode determines the functional command emitted. The dossier therefore does not collapse the Device to a single lighting action without first resolving configuration.

## Observed behavior and corroboration

No sanitized hardware fingerprint or first-hand command trace is currently retained for this exact family.

## Programming

Preserve the complete `M/LIV1/LIV2/SPE/I` configuration rather than translating the rotary control to a simple on/off command.

## Source reconciliation

The database is internally consistent: both commercial identities share firmware `213`, one Knob control Object and the same eight configuration fields. Dedicated publisher documentation remains a discovery gap, so physical interaction details beyond the database model are not inferred.

## Evidence limits and open work

- Locate and archive a publisher-original 4563-family technical sheet.
- Add a sanitized hardware fingerprint and first-hand command traces.
- Establish human-readable semantics for each `LIV1/LIV2/SPE/I` combination.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)
