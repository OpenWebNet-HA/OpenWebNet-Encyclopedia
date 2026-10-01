# Local Display

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0018` | Project identity |
| Technical description | Multifunction local display for scenarios, sound and temperature-control functions | Catalogue + product documentation |
| Catalogue item | `1147` - Local Display | Implementation evidence |
| Main catalogue system | Temperature control; also Automation | Implementation evidence |
| Item model / `modobj` | `64` | Implementation evidence |
| Firmware definition | `1.3 build 7` | Implementation evidence |
| Declared Modules | `4` | Implementation evidence |
| Configuration mode | Product Programming | Implementation evidence |
| Programming connection | USB | Implementation evidence |
| Categories | User Interface, Multifunction, Thermoregulation, Scenarios | Capability model |

The Local Display is a multifunction wall user interface whose catalogue topology is selected by the firmware-level `FUN` parameter. The same Physical Device can expose scenario-control, sound-diffusion, or temperature-probe behavior. The catalogue therefore must be read as a conditional topology rather than as three simultaneous fixed functions.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC/HS/HD4685` | Documented 4685-family identity | Catalogue + family documentation |
| BTicino - LivingLight | `L/N/NT4685` | Documented 4685-family identity | Catalogue + family documentation |
| Legrand - Arteor | `573916` | Shared technical item | Implementation evidence |
| Legrand - Arteor | `573917` | Shared technical item | Implementation evidence |
| Legrand - Céliane | `067281` | Shared technical item | Implementation evidence |
| Legrand - Céliane | `067282` | Shared technical item | Implementation evidence |

All six records share catalogue item `1147` and `modobj` 64. Direct variant-specific documentation remains desirable for the Legrand references.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `U1063B` | Instruction sheet | revision/date not yet pinned | 4685 Local Display family instruction sheet | not archived in repository | [Official source](https://dar.bticino.com/asset/Documents/U1063B.pdf) |
| MyHOME catalogue `HPML0714` | Product catalogue | revision/date not yet pinned | Generic “Local display - Sound distribution” context on printed p. 5 / PDF p. 5; the `4685` family is not named | [Archived MyHOME catalogue](../../sources/devices/documents/device-doc-myhome-catalogue-hpml0714/BR-MyHOME-HPML0714.pdf) | publisher source not currently retained |

The former official `U1063B` publisher URL currently returns an access/error response and the current Legrand document CDN does not expose that filename. An external reference copy of the same `U1063B` revision has therefore been used only to recover Device facts. The older MyHOME catalogue provides only generic Local Display / sound-distribution context and does not identify the `4685` family or corroborate its complete role set. The external copy is not archived or represented as an official original; byte-for-byte publisher evidence is still required.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| User interface | OLED touch display | `U1063B` reference copy |
| Connections | BUS/SCS, serial programming connector and external-probe connector | `U1063B` reference copy |
| Supported external probe | `3457` | `U1063B` reference copy |
| External probe characteristic | `10 kΩ` at `25 °C`, `BETA = 3435` | `U1063B` reference copy |
| Maximum probe connection length | `10 m` | `U1063B` reference copy |
| SCS supply | `18..27 Vdc` | `U1063B` reference copy |
| Maximum standby consumption | approximately `20 mA` | `U1063B` reference copy |
| Maximum operating consumption | approximately `60 mA` | `U1063B` reference copy |
| Operating temperature | `5..35 °C` | `U1063B` reference copy |

These values remain provisional until the exact official `U1063B` bytes are archived; they do not override the canonical implementation topology.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1147` | Implementation evidence |
| Main system | thermoregulation / Temperature control | Implementation evidence |
| Additional system | lighting_automation / Automation | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `64` in both mappings | Implementation evidence |
| Family | `1` | Implementation evidence |

## Firmware and hardware

| Catalogue firmware | Version | Build | Localization | Slots | Default |
| --- | --- | ---: | ---: | ---: | ---: |
| `110` | `1.3` | `7` | `1` | `4` | yes |

The catalogue declares Product Programming only and a USB programming connection. That is materially different from many configurable command Devices: the Local Display topology is selected through product-level configuration rather than represented as a generic Virgin Object.

## Module, Object, and Virgin Object model

Three reusable Objects are mapped across the four catalogue slots:

| `FUN` value | Object | Description | Slot mapping / fixed anchors |
| ---: | ---: | --- | --- |
| `1` | `413` | Scenario module control | slots `1..4` participate; slot 1 is fixed |
| `2` | `419` | Sound diffusion control | slots `1..4` participate; slot 2 is fixed |
| `3` | `460` | Local display as temperature control probe | slots `1..4` participate; slots 3 and 4 are fixed |
| `4` | `460` | Local display as temperature control probe | same catalogue Object and anchors as `FUN=3` |

There is no Virgin Object. Conditions `FUN=1`, `FUN=2`, `FUN=3` and `FUN=4` are explicit catalogue predicates. `FUN=3` and `FUN=4` intentionally select the same reusable Object in the current source; this dossier does not invent a distinction not represented by that source.

## Configuration modes

| Mode / modality | Evidence |
| --- | --- |
| Product Programming | implementation evidence |
| USB programming connection | implementation evidence |

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | Device identity field |
| `ZA` | `0..9` | `0` | first thermoregulation zone digit |
| `ZB` | `0..9` | `1` | second thermoregulation zone digit |
| `M` | `0`, `3`, `4`, `5`, `6`, `7`, `8` | `0` | product mode configurator domain |
| `FUN` | `0`, `1`, `2`, `3`, `4` | `0` | function selector that controls Object applicability |

The database labels `M=0` and `FUN=0` as None. Numeric M values `3..8` and `FUN` values `1..4` are preserved as raw catalogue values unless a product document supplies stronger names.

## Object configuration surfaces

The following subsections account for the complete reusable Object field surface present in the canonical catalogue. They preserve field identity without reproducing database serialization. Detailed Device-specific interpretation follows where available.

### Object `413` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Object-specific | `M` | Modality |
| Addressing | `APL`, `INST_LEV`, `DEST_LEV` | Scenario module address; Installation level; Destination level (`0..15`) |
| Mode / behavior | `TYPE_CONTACT` | Contact type |
| Scenario / button | `SCE_BUTT_1`, `DEL_BUTTON_1` | Scenario number; Activation delay of scenario number |

### Object `419` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Object-specific | `M` | Mode (VOL,ON_OFF) |
| Addressing | `ADDR_TYPE`, `A`, `PF` | Addressing type; Area; Audio point |
| Mode / behavior | `TYPE_CONTACT` | Contact type |
| Audio / media | `IS_FOLLOW_ME`, `SOURCE`, `SUB_SOURCE`, `CHANNEL` | Follow me; Source; Sub source; Channel (BB-Stereo) |

### Object `460` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `ZAZB`, `ZAZB_CENTRAL` | Zone; Control unit address |
| Object-specific | `SLA` | Slave number |
| Sensing / regulation | `COLD`, `WARM` | Summer mode; Winter mode |

### Additional Device-specific interpretation

| Object | Role | Principal configuration |
| --- | --- | --- |
| `460` | Local display as temperature-control probe | `ZAZB`, `SLA`, `COLD`, `WARM`, `ZAZB_CENTRAL` |
| `413` | Scenario module control | modality, scenario address, levels, contact type, scenario, delay |
| `419` | Sound diffusion control | modality, addressing, area/audio point, follow-me, source, channel |

#### Object `460` - Local display as temperature control probe

The reusable probe exposes `ZAZB` zone, `SLA` slave number, `COLD` summer enable, `WARM` winter enable, and `ZAZB_CENTRAL` control-unit address. This is the configuration surface used when `FUN` selects the temperature-control role.

#### Object `413` - Scenario module control

The scenario role exposes modality, scenario-module address, installation/destination levels, contact type, scenario number and activation delay. The reusable scenario address spans the standard `A` / `PL` combinations represented by the catalogue; scenario number is `1..16` and contact type can be normally open or normally closed.

#### Object `419` - Sound diffusion control

The sound role exposes modality (including `VOL` / `ON_OFF`), addressing type, area, audio point, follow-me, source/sub-source, contact type and channel. These are reusable Object domains and should not be interpreted as proof that every field is visible in every product-programming screen.

## Conditions, filters, and conversions

| Selector | Object | Applicability |
| --- | --- | --- |
| `FUN=1` | `413` | scenario module control |
| `FUN=2` | `419` | sound diffusion control |
| `FUN=3` | `460` | temperature-control probe role |
| `FUN=4` | `460` | temperature-control probe role; product documentation distinguishes role context |

The same Object for `FUN=3` and `FUN=4` is intentional in the current implementation source and must not be split without evidence.

### Catalogue filter references

No filter rows are associated with this Device firmware in the canonical catalogue.

### Catalogue slot-condition references

| Condition | Slot | Object | Predicate | Conversion reference |
| --- | --- | --- | --- | --- |
| `4190` | `1` | `460` | `FUN=3` | `1000` |
| `4191` | `1` | `460` | `FUN=4` | `1000` |
| `4190` | `2` | `460` | `FUN=3` | `1000` |
| `4191` | `2` | `460` | `FUN=4` | `1000` |
| `4190` | `3` | `460` | `FUN=3` | `1000` |
| `4191` | `3` | `460` | `FUN=4` | `1000` |
| `4190` | `4` | `460` | `FUN=3` | `1000` |
| `4191` | `4` | `460` | `FUN=4` | `1000` |
| `4912` | `1` | `413` | `FUN=1` | `` |
| `4912` | `2` | `413` | `FUN=1` | `` |
| `4912` | `3` | `413` | `FUN=1` | `` |
| `4912` | `4` | `413` | `FUN=1` | `` |
| `4913` | `1` | `419` | `FUN=2` | `` |
| `4913` | `2` | `419` | `FUN=2` | `` |
| `4913` | `3` | `419` | `FUN=2` | `` |
| `4913` | `4` | `419` | `FUN=2` | `` |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | identify `modobj` 64 and commercial family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | confirm installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | observe which conditional Modules are exposed | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect addresses for the selected role | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | correlate `FUN` / `M` and role-specific configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

A hardware fingerprint is especially valuable here because `DIMENSION 30` can test whether runtime exposure follows the source-level `FUN` conditions exactly.

## Functional applicability

Period product material describes an OLED local touch display used as a compact MyHOME interface. Its relevant systems include scenario control, sound diffusion and temperature regulation. The implementation database adds the exact conditional Object topology and the programming/configuration fields needed to represent those roles deterministically.

Depending on `FUN`, the Device participates in scenario, sound-diffusion or temperature-control behavior. Generic frame syntax remains canonical under Functional Protocol. This page records the Device-specific applicability and the conditional topology.

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

The catalogue presents this Device as product-programmed over USB. Configuration tooling should preserve `FUN` as a topology selector: changing it can change which reusable Object model is applicable, not merely a value inside one unchanged Object.

## Source reconciliation

The `U1063B` Local Display documentation clarifies the conditional roles represented by `FUN`:

- `FUN=1` is the scenario-oriented display role;
- `FUN=2` is the sound-diffusion display/control role;
- `FUN=3` uses the Local Display with an external temperature probe;
- `FUN=4` associates the Local Display with a thermoregulation probe/zone role rather than merely duplicating `FUN=3`.

The same documentation describes a short display wake/active interval after user interaction, product programming through the documented local programming connection, and use with external probe reference `3457` in the applicable temperature role. It also supplies the external-probe and electrical/temperature data recorded above.

Because the publisher endpoint for `U1063B` still prevents repository archival in this environment, these meanings are recorded as document-derived findings pending byte-for-byte archival verification. The earlier open question about the distinction between `FUN=3` and `FUN=4` is therefore narrowed to verification/correlation with the catalogue topology rather than basic semantic naming.

## Evidence limits and open work

- Obtain sanitized fingerprints for at least one BTicino 4685 and one Legrand commercial variant.
- Archive the official `U1063B` revision when the publisher endpoint permits automated retrieval.
- Find direct official sheets for `573916`/`573917` and `067281`/`067282`.
- Establish vendor-facing names for `M=3..8` and verify the documented `FUN=3` / `FUN=4` distinction against an archived `U1063B` original and real hardware.
- Check whether firmware later than catalogue `1.3.7` changes role selection or slot anchoring.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
