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
| BTicino / Axolute | `HC/HS/HD4563` | `25` | Commercial identity of this Technical Device | Canonical catalogue |
| BTicino / L/N/NT | `L/N/NT4563` | `1838` | Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `mh_diff-sonore2008.pdf` | Two-wire sound-system technical guide | historical publisher guide | 4563 rotary-control technical-data section; printed page unresolved / 1-based PDF page unresolved | [Archived PDF](../../sources/devices/documents/device-doc-radio-wired-interface-sound-guide/mh_diff-sonore2008.pdf) | [Publisher PDF](https://assets.legrand.com/general/cession/bt/np-ft-gt/mh_diff-sonore2008.pdf) |
| `AUTOMATISME.pdf` | MyHOME automation guide | historical publisher guide | 4563 control-family sections; printed page unresolved / 1-based PDF page unresolved | [Archived PDF](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

The printed and 1-based PDF page locators remain unresolved and are retained explicitly as an evidence gap.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 wiring-device modules | `mh_diff-sonore2008.pdf` |
| SCS operating supply | `18..27 Vdc` | `mh_diff-sonore2008.pdf` |
| Maximum current draw | `5 mA` | `mh_diff-sonore2008.pdf` |
| Operating temperature | `5..35 °C` | `mh_diff-sonore2008.pdf` |
| Local interface | central pushbutton plus rotary knob | `mh_diff-sonore2008.pdf` |
| Published local actions | ON/OFF, programmed radio-station or track change, and volume adjustment | `mh_diff-sonore2008.pdf` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `25` | Canonical catalogue |
| Technical item description | Regulation rotative control | Canonical catalogue |
| Item family | `1` - Control | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `11` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `213` | `-1` | `-1` | `-1` | `1` | not stated | wildcard applicability |

Firmware `213` is wildcard `-1.-1.-1` with one Module.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `213` | `606` | `451` | `451` | Knob control |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `1009` | `1` | `451` | fixed | Knob control |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| - | - | - | - | No firmware-scoped Virgin Object | - | - |

The Module resolves to Object `451`, **Knob control**, a one-slot Object associated with Automation and the relevant command-control collections. No Virgin Object is declared for this firmware.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `213` | `1` | `1` | Virtual Configuration |
| `213` | `3` | `0` | Physical configuration |

Physical Configuration and Virtual Configuration are declared.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | MyHOME Suite / catalogue identity field - not a physical configurator |
| `A` | `0..9` | `0` | area / environment configurator |
| `PL` | `0..9` | `0` | light-point configurator |
| `M` | `0` / `O/I` / `OFF` / `ON` / `UP/DOWN` / `UP/DOWN` monostable / `CEN` / `PUL` | `0` | operating / function mode |
| `LIV1` | `0..99` | `1` | first regulation level |
| `LIV2` | `0..99` | `1` | second regulation level |
| `SPE` | `0..9` | `0` | special-function selector |
| `I` | `0` / `CEN` | `0` | additional function selector |

`LIV1` / `LIV2` are the two regulation-level fields. `SPE` and `I` are additional command selectors whose semantics depend on the selected operating mode.

## Object configuration surfaces

### Object `451` - Knob control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..9` | `0` | Area |
| `PL` | `0..9` | `0` | Light point |
| `M` | `O/I` / `OFF` / `ON` / `UP/DOWN` / `UP/DOWN` monostable / `CEN` / `PUL` / `None` | `0` | Modality |
| `LIV1` | `0..99` | `1` | Configurator `LIV1` |
| `LIV2` | `0..99` | `1` | Configurator `LIV2` |
| `SPE` | `0..9` | `0` | Special function command control (`0..9`) |
| `I` | `None` / `CEN` | `0` | Configurator `I` |

**Firmware relationship.** No additional Object/Firmware range filter in the catalogue.

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `0` | Device/Firmware topology conditions |
| Object/Firmware filters | `0` | Conditional Object configuration exposure |
| Referenced conversion rules | `0` | None |

Generic condition/conversion evaluation remains canonical in [Catalogue Resolution](../../internals/catalogue-resolution.md); these tables preserve this Device's exact applicability records.

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
- Pin exact printed and 1-based PDF page locations for each applicable multi-product guide citation.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf)
