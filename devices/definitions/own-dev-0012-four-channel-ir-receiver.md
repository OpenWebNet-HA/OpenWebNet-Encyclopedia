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
| Declared Modules | 4 | Implementation evidence |
| Categories | Command, Interface, Multifunction | Capability model |

The Device receives commands from compatible infrared remote controls and projects four fixed IR-receiver Modules. Physical configuration assigns the function of each IR channel, while virtual configuration can describe the channels through reusable IR receiver Objects.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino Axolute | `HC4654` | Established identity | Catalogue cluster + official technical sheet |
| BTicino Axolute | `HS4654` | Established identity | Catalogue cluster + official technical sheet |
| BTicino Axolute | `HD4654` | Established identity | Catalogue cluster + official technical sheet |
| BTicino L/N/NT | `L4654N` | Established identity | Catalogue cluster + official technical sheet |
| BTicino L/N/NT | `N4654N` | Established identity | Catalogue cluster + official technical sheet |
| BTicino L/N/NT | `NT4654N` | Established identity | Catalogue cluster + official technical sheet |
| BTicino Matix | `AM5834` | Established identity | Catalogue + official technical sheet |
| Legrand Arteor | `573900` | Established identity | Catalogue + official technical sheet |
| Legrand Arteor | `573901` | Established identity | Catalogue + official technical sheet |
| Legrand Céliane | `067216` | Established identity | Catalogue + official technical sheet |
| Legrand Mosaic | `078465` | Shared technical item | Implementation evidence; direct product sheet pending |
| Legrand Mosaic | `079265` | Shared technical item | Implementation evidence; direct product sheet pending |

The MyHOME Suite catalogue stores some finish variants as combined codes, so one catalogue row may represent several printed BTicino references.

## Documentation

| Document | Type | Coverage | Archived original | Publisher |
| --- | --- | --- | --- | --- |
| `MQ00071-d-EN` | Technical sheet | principal BTicino, Arteor and Céliane references | [Archived PDF](../../sources/devices/documents/device-doc-ir-receiver-mq00071-d-en/MQ00071-d-EN.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00071-d-EN.pdf) |
| `MQ00071-d-FR` | Technical sheet | IR receiver family | [Archived PDF](../../sources/devices/documents/device-doc-ir-receiver-mq00071-d-fr/MQ00071-d-FR.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00071-d-FR.pdf) |
| `MQ00071-d-IT` | Technical sheet | IR receiver family | [Archived PDF](../../sources/devices/documents/device-doc-ir-receiver-mq00071-d-it/MQ00071-d-IT.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00071-d-IT.pdf) |

## Physical characteristics

The 2014 English sheet establishes:

| Property | Value |
| --- | --- |
| Mounting | 2 flush-mounted modules |
| Remote controls | compatible with BTicino `3527N` and `3529` |
| SCS nominal supply | `27 Vdc` |
| SCS operating supply | `18..27 Vdc` |
| Current draw | `8.5 mA` |
| Operating temperature | `5..35 °C` |
| Physical configurator positions | `A`, `PL1/PF1`, `PL2/PF2`, `PL3/PF3`, `PL4/PF4`, `M` |

The six physical positions independently support the expected ordinary addressed-form configurator count, pending an observed Device-identity read.

## Identity and firmware

| Field | Value |
| --- | --- |
| `EN_ITEM.id_item` | `37` |
| `AS_ITEM_SYSTEM.modobj` | `22` |
| Firmware | `216` |
| Firmware applicability | `-1.-1.-1` |
| Firmware slots | `4` |
| Configuration modes | Physical, Virtual |

No Advanced Configuration association is present for firmware `216`.

## Module and Object model

All four slots are fixed to Object `34`, **IR receiver**.

The reusable Object configuration surface is deliberately simple:

| Parameter | Domain |
| --- | --- |
| `A` | `0..9` |
| `PL` | `0..9` |
| `MOD` | `0..4` |

The firmware-level physical representation is richer than this reusable Object surface because each of the four receiver channels has an independent `PLn/PFn` selector and the whole Device has one shared `M`.

There are no slot-condition rows and no Virgin Object for this firmware.

## Firmware-scoped configuration

| Field | Stored domain |
| --- | --- |
| `AID` | Device identity |
| `A` | `0..9` |
| `PL1` .. `PL4` | `0..9`, OFF, ON, GEN, UP/DOWN, UP/DOWN monostable, AMB |
| `M` | `0..9`, CEN |

The labels in the database use `PL1..PL4`; the official sheet labels each physical socket `PLn/PFn` because the same position takes different semantic roles depending on operating mode.

## Published operating modes

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

## Addressing model

The Device has one environment field `A` and four per-channel physical selectors. Depending on the selected mode, a `PLn/PFn` position may identify:

- a lighting point;
- ON/OFF/general/room-style lighting scope;
- an automation UP/DOWN function;
- a scenario or programmed-scenario function;
- an audio/sound function.

This contextual reuse is why the firmware parameter enum is wider than the reusable Object `PL=0..9` field.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 22`, commercial identity and installed configurator count | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe actual installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm four fixed IR receiver Objects | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect configured channel addresses/context | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect the physical/virtual configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

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

## Corroboration status and open work

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
