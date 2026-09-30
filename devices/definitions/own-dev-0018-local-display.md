# Local Display

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0018` | Project identity |
| Technical description | Multifunction local display for scenarios, sound and temperature-control functions | Catalogue + product documentation |
| Catalogue item | 1147 - Local Display | Implementation evidence |
| Main catalogue system | Temperature control; also Automation | Implementation evidence |
| Item model / `modobj` | `64` | Implementation evidence |
| Firmware definition | `1.3 build 7` | Implementation evidence |
| Declared slots | `4` | Implementation evidence |
| Configuration mode | Product Programming | Implementation evidence |
| Programming connection | USB | Implementation evidence |
| Categories | User Interface, Multifunction, Thermoregulation, Scenarios | Capability model |

The Local Display is a multifunction wall user interface whose catalogue topology is selected by the firmware-level `FUN` parameter. The same Physical Device can expose scenario-control, sound-diffusion, or temperature-probe behavior. The catalogue therefore must be read as a conditional topology rather than as three simultaneous fixed functions.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino Axolute | `HC/HS/HD4685` | Documented 4685-family identity | Catalogue + family documentation |
| BTicino L/N/NT | `L/N/NT4685` | Documented 4685-family identity | Catalogue + family documentation |
| Legrand Arteor | `573916` | Shared technical item | Implementation evidence |
| Legrand Arteor | `573917` | Shared technical item | Implementation evidence |
| Legrand Céliane | `067281` | Shared technical item | Implementation evidence |
| Legrand Céliane | `067282` | Shared technical item | Implementation evidence |

All six records share catalogue item `1147` and `modobj` 64. Direct variant-specific documentation remains desirable for the Legrand references.

## Documentation

| Document | Coverage | Status |
| --- | --- | --- |
| `U1063B` | 4685 Local Display family instruction sheet | [Official source](https://dar.bticino.com/asset/Documents/U1063B.pdf) |
| MyHOME catalogue HPML0714 | Local Display product context and family functions | [Archived MyHOME catalogue](../../sources/devices/documents/device-doc-myhome-catalogue-hpml0714/BR-MyHOME-HPML0714.pdf) |

The official `U1063B` publisher endpoint currently rejects automated archival retrieval in this environment. The dossier retains the official URL and does not replace it with a mirror.

## Product role

Period product material describes an OLED local touch display used as a compact MyHOME interface. Its relevant systems include scenario control, sound diffusion and temperature regulation. The implementation database adds the exact conditional Object topology and the programming/configuration fields needed to represent those roles deterministically.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1147` | Implementation evidence |
| main system | thermoregulation / Temperature control | Implementation evidence |
| additional system | lighting_automation / Automation | Implementation evidence |
| `modobj` | 64 in both system mappings | Implementation evidence |
| family | `1` | Implementation evidence |

## Firmware and programming applicability

| Catalogue firmware | Version | Build | Localization | Slots | Default |
| --- | --- | ---: | ---: | ---: | ---: |
| `110` | `1.3` | `7` | `1` | `4` | yes |

The catalogue declares Product Programming only and a USB programming connection. That is materially different from many configurable command Devices: the Local Display topology is selected through product-level configuration rather than represented as a generic Virgin Object.

## Conditional Module / Object topology

Three reusable Objects are mapped across the four catalogue slots:

| `FUN` value | Object | Description | Slot mapping / fixed anchors |
| ---: | ---: | --- | --- |
| `1` | `413` | Scenario module control | slots `1..4` participate; slot 1 is fixed |
| `2` | `419` | Sound diffusion control | slots `1..4` participate; slot 2 is fixed |
| `3` | `460` | Local display as temperature control probe | slots `1..4` participate; slots 3 and 4 are fixed |
| `4` | `460` | Local display as temperature control probe | same catalogue Object and anchors as `FUN=3` |

There is no Virgin Object. Conditions `FUN=1`, `FUN=2`, `FUN=3` and `FUN=4` are explicit catalogue predicates. `FUN=3` and `FUN=4` intentionally select the same reusable Object in the current source; this dossier does not invent a distinction not represented by that source.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | Device identity field |
| `ZA` | `0..9` | 0 | first thermoregulation zone digit |
| `ZB` | `0..9` | 1 | second thermoregulation zone digit |
| `M` | 0, 3, 4, 5, 6, 7, 8 | 0 | product mode configurator domain |
| `FUN` | 0, 1, 2, 3, 4 | 0 | function selector that controls Object applicability |

The database labels `M=0` and `FUN=0` as None. Numeric M values `3..8` and `FUN` values `1..4` are preserved as raw catalogue values unless a product document supplies stronger names.

## Object configuration surfaces

### Object `460` - Local display as temperature control probe

The reusable probe exposes `ZAZB` zone, `SLA` slave number, `COLD` summer enable, `WARM` winter enable, and `ZAZB_CENTRAL` control-unit address. This is the configuration surface used when `FUN` selects the temperature-control role.

### Object `413` - Scenario module control

The scenario role exposes modality, scenario-module address, installation/destination levels, contact type, scenario number and activation delay. The reusable scenario address spans the standard A/PL combinations represented by the catalogue; scenario number is `1..16` and contact type can be normally open or normally closed.

### Object `419` - Sound diffusion control

The sound role exposes modality (including `VOL` / `ON_OFF`), addressing type, area, audio point, follow-me, source/sub-source, contact type and channel. These are reusable Object domains and should not be interpreted as proof that every field is visible in every product-programming screen.

## Diagnostic applicability

| Surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | identify `modobj` 64 and commercial family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | confirm installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | observe which conditional Modules are exposed | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect addresses for the selected role | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | correlate `FUN`/M and role-specific configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

A hardware fingerprint is especially valuable here because DIM30 can test whether runtime exposure follows the source-level `FUN` conditions exactly.

## Functional applicability

Depending on `FUN`, the Device participates in scenario, sound-diffusion or temperature-control behavior. Generic frame syntax remains canonical under Functional Protocol. This page records the Device-specific applicability and the conditional topology.

## Programming

The catalogue presents this Device as product-programmed over USB. Configuration tooling should preserve `FUN` as a topology selector: changing it can change which reusable Object model is applicable, not merely a value inside one unchanged Object.

## Evidence limits and open work

- Obtain sanitized fingerprints for at least one BTicino 4685 and one Legrand commercial variant.
- Archive the official `U1063B` revision when the publisher endpoint permits automated retrieval.
- Find direct official sheets for `573916`/`573917` and `067281`/`067282`.
- Establish the vendor-facing names for M=`3..8` and the distinction between `FUN=3` and `FUN=4` without guessing.
- Check whether firmware later than catalogue `1.3.7` changes role selection or slot anchoring.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
