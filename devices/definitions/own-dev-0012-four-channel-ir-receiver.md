# Four-channel IR receiver

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0012` | Project identity |
| Technical description | Four-channel SCS infrared receiver for remote control and scenario functions | Catalogue + official technical sheet |
| Catalogue item | `37` - “IR receiver” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `22` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `216` | Implementation evidence |
| Declared Modules | `4` | Implementation evidence |
| Categories | Command, Interface, Multifunction | Capability model |

The Device receives commands from compatible infrared remote controls and projects four fixed IR-receiver Modules. Physical configuration assigns the function of each IR channel, while virtual configuration can describe the channels through reusable IR receiver Objects.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC4654` | Established identity | Catalogue cluster + official technical sheet |
| BTicino - Axolute | `HS4654` | Established identity | Catalogue cluster + official technical sheet |
| BTicino - Axolute | `HD4654` | Established identity | Catalogue cluster + official technical sheet |
| BTicino - LivingLight | `L4654N` | Established identity | Catalogue cluster + official technical sheet |
| BTicino - LivingLight | `N4654N` | Established identity | Catalogue cluster + official technical sheet |
| BTicino - LivingLight | `NT4654N` | Established identity | Catalogue cluster + official technical sheet |
| BTicino - Matix | `AM5834` | Established identity | Catalogue + official technical sheet |
| Legrand - Arteor | `573900` | Established identity | Catalogue + official technical sheet |
| Legrand - Arteor | `573901` | Established identity | Catalogue + official technical sheet |
| Legrand - Céliane | `067216` | Established identity | Catalogue + official technical sheet |
| Legrand - Mosaic | `078465` | Shared technical item | Implementation evidence; direct product sheet pending |
| Legrand - Mosaic | `079265` | Shared technical item | Implementation evidence; direct product sheet pending |

The MyHOME Suite catalogue stores some finish variants as combined codes, so one catalogue row may represent several printed BTicino references.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00071-d-EN` | Technical sheet | revision/date not yet pinned | principal BTicino, Arteor and Céliane references | [Archived PDF](https://archive.openwebnet-ha.org/sha256/23/77/2377847553a0c47193ebc21f19d7bc31c55e1b897f424f0a4ee3f44dd9514abe.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00071-d-EN.pdf) |
| `MQ00071-d-FR` | Technical sheet | revision/date not yet pinned | IR receiver family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/58/3e/583ecd811160edb5e46567918b78e2ffc8dd61301e756fa1c80815f044490e78.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00071-d-FR.pdf) |
| `MQ00071-d-IT` | Technical sheet | revision/date not yet pinned | IR receiver family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/ec/df/ecdf700916a509417e86448e095a9e780b29251daac28659b8e558f648588e13.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00071-d-IT.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 flush-mounted modules | `MQ00071-d-EN` |
| Compatible remote controls | `3527N` and `3529` | `MQ00071-d-EN` |
| SCS nominal supply | `27 Vdc` | `MQ00071-d-EN` |
| SCS operating supply | `18..27 Vdc` | `MQ00071-d-EN` |
| Current draw | `8.5 mA` | `MQ00071-d-EN` |
| Operating temperature | `5..35 °C` | `MQ00071-d-EN` |
| Physical configurator positions | `A`, `PL1/PF1`, `PL2/PF2`, `PL3/PF3`, `PL4/PF4`, `M` | `MQ00071-d-EN` |

The six physical positions independently support the expected ordinary addressed-form configurator count, pending an observed Device-identity read.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `37` | Implementation evidence |
| Main system | Lighting / Automation | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `22` | Implementation evidence |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `216` | `-1` | `-1` | `-1` | `4` | not stated | wildcard applicability |

Wildcard values are catalogue applicability sentinels, not claims about an installed firmware version.

## Module, Object, and Virgin Object model

| Slot | Object | Description | Relationship |
| ---: | ---: | --- | --- |
| `1` | `34` | IR receiver | fixed |
| `2` | `34` | IR receiver | fixed |
| `3` | `34` | IR receiver | fixed |
| `4` | `34` | IR receiver | fixed |

There is no Virgin Object and no slot-condition row for firmware `216`.

## Configuration modes

| Mode / modality | Evidence |
| --- | --- |
| Physical configuration | product documentation + implementation evidence |
| Virtual Configuration | implementation evidence |

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | Device identity | - | implementation identity field |
| `A` | `0..9` | - | environment / address |
| `PL1` | `0..9` / `OFF` / `ON` / `GEN` / `UP/DOWN` / `UP/DOWN monostable` / `AMB` | - | per-channel contextual physical selector |
| `PL2` | `0..9` / `OFF` / `ON` / `GEN` / `UP/DOWN` / `UP/DOWN monostable` / `AMB` | - | per-channel contextual physical selector |
| `PL3` | `0..9` / `OFF` / `ON` / `GEN` / `UP/DOWN` / `UP/DOWN monostable` / `AMB` | - | per-channel contextual physical selector |
| `PL4` | `0..9` / `OFF` / `ON` / `GEN` / `UP/DOWN` / `UP/DOWN monostable` / `AMB` | - | per-channel contextual physical selector |
| `M` | `0..9` / `CEN` | - | shared operating-mode selector |

The database uses `PL1`..`PL4` while the official sheet labels each socket `PLn/PFn` because its meaning depends on `M`.

### Published operating modes

The official sheet documents five broad modes:

| Mode | Physical selection | Function |
| --- | --- | --- |
| Remote control | `M=1..4` | four generic ON/OFF/UP/DOWN-style remote control channels |
| Advanced scenarios | `M=CEN` | commands a scenario programmer such as MH200N |
| Self-learning | no `M` configurator | learns functions for the remote keys |
| Scenario module | `M=6` | activates up to 16 scenarios stored in F420-style scenario modules |
| Sound diffusion | `M=9` | controls amplifier/audio functions |

The sheet also documents lighting, automation, video-door-entry and scenario behavior through the remote-control key assignments.

The generic functional frame grammar remains canonical under the relevant [Functional Protocol](../../functional/) sections.

### Addressing model

The Device has one environment field `A` and four per-channel physical selectors. Depending on the selected mode, a `PLn/PFn` position may identify:

- a lighting point;
- ON/OFF/general/room-style lighting scope;
- an automation UP/DOWN function;
- a scenario or programmed-scenario function;
- an audio/sound function.

This contextual reuse is why the firmware parameter enum is wider than the reusable Object `PL=0..9` field.

## Object configuration surfaces

The following subsections account for the complete reusable Object field surface present in the canonical catalogue. They preserve field identity without reproducing database serialization. Detailed Device-specific interpretation follows where available.

### Object `34` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | Area; Light point |
| Mode / behavior | `MOD` | Mode 0-4 |

### Additional Device-specific interpretation

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..9` | - | reusable IR receiver area / environment |
| `PL` | `0..9` | - | reusable IR receiver point |
| `MOD` | `0..4` | - | reusable IR receiver mode |

This reusable Object surface is narrower than the contextual firmware-level `PLn/PFn` representation.

## Conditions, filters, and conversions

| Surface | Status | Evidence |
| --- | --- | --- |
| Slot conditions | none | implementation evidence |
| Virgin Object | none | implementation evidence |
| Topology | four fixed Object `34` Modules | implementation evidence |

### Catalogue filter references

No filter rows are associated with this Device firmware in the canonical catalogue.

### Catalogue slot-condition references

No slot-condition rows are associated with this Device firmware in the canonical catalogue.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 22`, commercial identity and installed configurator count | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe actual installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm four fixed IR receiver Objects | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect configured channel addresses/context | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect the physical/virtual configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Depending on shared `M` mode and per-channel selectors, the receiver participates in lighting, automation, programmed scenarios, scenario-module control, sound diffusion, and published video-door-entry-related remote functions. Generic functional frame grammar remains canonical under Functional Protocol.

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

A programmer must interpret each `PLn/PFn` value in the context of the shared `M` operating mode. It must not translate all firmware enum values into ordinary lighting-point addresses.

See [Configuration Programming](../../programming/configuration-programming.md) and [Programming Validation](../../programming/validation.md).

## Source reconciliation

The IR-receiver technical sheets have been reconciled into concrete Device behavior:

- `M=1..4` select remote-control channel blocks; multiple receivers can be arranged to provide up to sixteen distinct remote commands;
- shutter/automation assignments use paired UP/DOWN semantics rather than four unrelated light-point values;
- `M=CEN` selects programmed-scenario/CEN use, while the unconfigured/self-learning mode has its own learn/delete workflow;
- `M=6` is the published scenario-module mode and `M=9` is the published sound-diffusion mode;
- each physical `PLn/PFn` socket is contextual: the same configurator position can mean a light point, automation function, scenario selection or audio point depending on `M`;
- the product includes a programming/lock control whose state affects learning/configuration behavior but is not an OpenWebNet Module.

These facts are the Device-specific interpretation layer above the four fixed Object `34` instances.

## Evidence limits and open work

- Locate direct product documentation for Mosaic `078465` and `079265`.
- Add sanitized hardware fingerprints for at least one commercial variant.
- Corroborate the six physical configurator positions and four fixed Modules.
- Preserve real remote-control observations showing the mapping between physical `M`, channel selectors and emitted functional commands.
- Locate installation sheets and older technical-sheet revisions where available.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
- [Programming](../../programming/)
