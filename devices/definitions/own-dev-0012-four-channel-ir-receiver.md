# Four-channel IR receiver

## Summary

This four-channel infrared receiver translates commands from compatible handheld remotes into SCS actions. Each configured channel can serve lighting, automation, scenarios or other documented system functions, bringing remote operation to otherwise wired controls.

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
| Legrand - Mosaic | `078465` | Established catalogue identity | Canonical catalogue; exact-product technical sheet not retained |
| Legrand - Mosaic | `079265` | Established catalogue identity | Canonical catalogue; exact-product technical sheet not retained |

The MyHOME Suite catalogue stores some finish variants as combined codes, so one catalogue row may represent several printed BTicino references.

The canonical `EN_DEVICE.code` retains combined `HS/HD/HC4654` and `L/N/NT4654N`. The named finish references above expand those catalogue codes; their ordering does not imply a different technical item.

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `HC4654` | `8012199745633` | [Archived original](https://archive.openwebnet-ha.org/sha256/9e/95/9e9591626666bbcf78b4d7c3168066f05d2b8f4ef5b4f1532ca59158ba383999.pdf), `HC4654-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `HS4654` | `8012199745640` | [Archived original](https://archive.openwebnet-ha.org/sha256/fd/dc/fddcaad93e0fcb251f742091057a578b331259a1a29ffc68ae3264dc6ea0860f.pdf), `HS4654-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `HD4654` | `8012199986227` | [Archived original](https://archive.openwebnet-ha.org/sha256/6e/d7/6ed760ddbe69f4660bdb3e572e4caebc34876b72d48cca3b88f80dfc30736d41.pdf), `HD4654-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `L4654N` | `8012199765617` | [Archived original](https://archive.openwebnet-ha.org/sha256/ff/db/ffdb9e0a99012ec0016fc25661513a84df7a30581840c550e4f499cd07331a10.pdf), `L4654N-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `N4654N` | `8012199765624` | [Archived original](https://archive.openwebnet-ha.org/sha256/fd/fa/fdfaf8d50aadc1b1eeb96e97818e9de499b9afb2ec6dbc8b79eed4843e2e2d68.pdf), `N4654N-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `NT4654N` | `8012199765631` | [Archived original](https://archive.openwebnet-ha.org/sha256/9c/72/9c728ac545a3d2ecc106c9418604806488aeaeec545eeab1b6a66d047e1ff32f.pdf), `NT4654N-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00071-d-EN` | Technical sheet | 05/06/2014; PDF pp. 1–4 | Exact named references and all Device-specific configuration/programming pages inspected | [Archived PDF](https://archive.openwebnet-ha.org/sha256/23/77/2377847553a0c47193ebc21f19d7bc31c55e1b897f424f0a4ee3f44dd9514abe.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00071-d-EN.pdf) |
| `MQ00071-d-FR` | Technical sheet | 29/04/2014; PDF pp. 1–4 | Exact named references and all Device-specific configuration/programming pages inspected | [Archived PDF](https://archive.openwebnet-ha.org/sha256/58/3e/583ecd811160edb5e46567918b78e2ffc8dd61301e756fa1c80815f044490e78.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00071-d-FR.pdf) |
| `MQ00071-d-IT` | Technical sheet | 29/04/2014; PDF pp. 1–4 | Exact named references and all Device-specific configuration/programming pages inspected | [Archived PDF](https://archive.openwebnet-ha.org/sha256/ec/df/ecdf700916a509417e86448e095a9e780b29251daac28659b8e558f648588e13.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00071-d-IT.pdf) |
| `HC4654-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HC4654` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/9e/95/9e9591626666bbcf78b4d7c3168066f05d2b8f4ef5b4f1532ca59158ba383999.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4654) |
| `HS4654-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HS4654` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/fd/dc/fddcaad93e0fcb251f742091057a578b331259a1a29ffc68ae3264dc6ea0860f.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4654) |
| `HD4654-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HD4654` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/6e/d7/6ed760ddbe69f4660bdb3e572e4caebc34876b72d48cca3b88f80dfc30736d41.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HD4654) |
| `L4654N-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `L4654N` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/ff/db/ffdb9e0a99012ec0016fc25661513a84df7a30581840c550e4f499cd07331a10.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4654N) |
| `N4654N-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `N4654N` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/fd/fa/fdfaf8d50aadc1b1eeb96e97818e9de499b9afb2ec6dbc8b79eed4843e2e2d68.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-N4654N) |
| `NT4654N-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `NT4654N` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/9c/72/9c728ac545a3d2ecc106c9418604806488aeaeec545eeab1b6a66d047e1ff32f.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-NT4654N) |

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

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `22` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `216` | `-1` | `-1` | `-1` | `4` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Wildcard values are catalogue applicability sentinels, not claims about an installed firmware version.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `216` | `1` | `34` IR receiver | Fixed/designated metadata | `1169` | `34` | `628` |
| `216` | `2` | `34` IR receiver | Fixed/designated metadata | `1170` | `34` | `628` |
| `216` | `3` | `34` IR receiver | Fixed/designated metadata | `1171` | `34` | `628` |
| `216` | `4` | `34` IR receiver | Fixed/designated metadata | `1172` | `34` | `628` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

There is no Virgin Object and no slot-condition row for firmware `216`.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `216` | Physical configuration | `0` | Canonical firmware/mode association |
| `216` | Virtual Configuration | `1` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `216` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `216` | `A` | `0..9` | `0` | A; Environment |
| `216` | `PL1` | `0..9`; `10` = `OFF`; `11` = `ON`; `12` = `GEN`; `13` = `UP/DOWN`; `14` = `UP/DOWN` monostable; `15` = `AMB` | `0` | PL1; PL1 (0-9, `OFF`,`ON`,`GEN`,SU_GIU,SU_GIU_M,`AMB`) |
| `216` | `PL2` | `0..9`; `10` = `OFF`; `11` = `ON`; `12` = `GEN`; `13` = `UP/DOWN`; `14` = `UP/DOWN` monostable; `15` = `AMB` | `0` | PL2; PL2 (0-9, `OFF`,`ON`,`GEN`,SU_GIU,SU_GIU_M,`AMB`) |
| `216` | `PL3` | `0..9`; `10` = `OFF`; `11` = `ON`; `12` = `GEN`; `13` = `UP/DOWN`; `14` = `UP/DOWN` monostable; `15` = `AMB` | `0` | PL3; PL3 (0-9, `OFF`,`ON`,`GEN`,SU_GIU,SU_GIU_M,`AMB`) |
| `216` | `PL4` | `0..9`; `10` = `OFF`; `11` = `ON`; `12` = `GEN`; `13` = `UP/DOWN`; `14` = `UP/DOWN` monostable; `15` = `AMB` | `0` | PL4; PL4 (0-9, `OFF`,`ON`,`GEN`,SU_GIU,SU_GIU_M,`AMB`) |
| `216` | `M` | `0..9`; `14` = `CEN` | `0` | M; Mode (0-9,`CEN`) |

The database uses `PL1`..`PL4` while the official sheet labels each socket `PLn/PFn` because its meaning depends on `M`.

### Published operating modes

The official sheet documents five broad modes:

| Mode | Physical selection | Function |
| --- | --- | --- |
| Remote control | `M=1..4` | four generic `ON`/`OFF`/`UP/DOWN`-style remote control channels |
| Advanced scenarios | `M=CEN` | commands a scenario programmer such as MH200N |
| Self-learning | no `M` configurator | learns functions for the remote keys |
| Scenario module | `M=6` | activates up to 16 scenarios stored in F420-style scenario modules |
| Sound diffusion | `M=9` | controls amplifier/audio functions |

The sheet also documents lighting, automation, video-door-entry and scenario behavior through the remote-control key assignments.

The generic functional frame grammar remains canonical under the relevant [Functional Protocol](../../functional/) sections.

### Addressing model

The Device has one environment field `A` and four per-channel physical selectors. Depending on the selected mode, a `PLn/PFn` position may identify:

- a lighting point;
- `ON`/`OFF`/general/room-style lighting scope;
- an automation `UP/DOWN` function;
- a scenario or programmed-scenario function;
- an audio/sound function.

This contextual reuse is why the firmware parameter enum is wider than the reusable Object `PL=0..9` field.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `34` - IR receiver

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..9` | `0` | Area |
| `PL` | `0..9` | `0` | Light point |
| `MOD` | `0..4` | `0` | Modality; Mode 0-4 |

### Device-specific interpretation

Physical sockets are labelled `PLn/PFn` because the shared M mode changes their meaning. Four catalogue Modules do not limit self-learning to four remote keys: the product sheet allows sixteen learned commands. Numeric reusable fields do not replace the contextual physical symbols.

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
| `DIMENSION 1` | resolve `modobj = 22`, commercial identity and installed configurator count | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe actual installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm four fixed IR receiver Objects | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect configured channel addresses/context | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect the physical/virtual configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Depending on shared `M` mode and per-channel selectors, the receiver participates in lighting, automation, programmed scenarios, scenario-module control, sound diffusion, and published video-door-entry-related remote functions. Generic functional frame grammar remains canonical under Functional Protocol.

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| M=`1..4` | Four fixed channel assignments per receiver; up to four receivers yield sixteen distinct commands in the room | MQ00071-d-EN, pp. 2–3 |
| `M=0` / no configurator | Up to sixteen learned commands, including timed/flashing lighting, lock/unlock, AUX shutter/light, door-lock/stair-light and amplifier controls | Same source, p. 3 |
| `M=6` | Up to sixteen F420 scenarios through sixteen remote channels; programming switch and F420 unlock both apply | Same source, p. 4 |
| `M=9` | Up to four amplifiers; brief On/Off, held volume up/down, source cycling and station/track change; Follow Me | Same source, p. 4 |

For sound mode A=`1..9` is the destination room and PF1..PF4=`0..9` identify amplifiers. Each PF uses four consecutive remote channels. Neither the four Module projection nor numeric PL defaults reduces these contextual functions to four ordinary lighting points.

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

Interpret each PLn/PFn in the context of shared M. `MQ00071-d-EN`, p. 2, requires identical selectors in both positions of a shutter pair; the first sends Up and the second Down. `M=1/2/3/4` chooses remote channels 1–4/5–8/9–12/13–16. CEN pairs up to six 3529 buttons with MH200N scenarios in software.

For self-learning (M empty/0), use `A=0` and PL=`1..9`; the sheet excludes that address from actuators. With the rear switch unlocked, hold programming for three seconds, select a remote key within twenty seconds and issue the required system command. Repeat key/command selection and press programming to exit. To erase one learned key hold programming for at least eight seconds, release within the next four seconds, then select the key within twenty seconds; rapid flashing confirms deletion. Erase all learned commands with an approximately twelve-second hold. The locked rear switch disables programming/deletion.

For `M=6`, also unlock the F420 module (at least 0.5 seconds, green LED). Enter programming with the receiver’s three-second hold, select a remote key within twenty seconds, issue scenario actions and press programming to exit. Individual scenario erasure uses the eight-second receiver hold and key selection; entire scenario memory must be reset on F420. Receiver self-learning erasure and F420 memory erasure are distinct operations. See `MQ00071-d-EN`, pp. 3–4, with corresponding FR/IT sections.

## Source reconciliation

The IR-receiver technical sheets have been reconciled into concrete Device behavior:

- `M=1..4` select remote-control channel blocks; multiple receivers can be arranged to provide up to sixteen distinct remote commands;
- shutter/automation assignments use paired `UP/DOWN` semantics rather than four unrelated light-point values;
- `M=CEN` selects programmed-scenario/`CEN` use, while the unconfigured/self-learning mode has its own learn/delete workflow;
- `M=6` is the published scenario-module mode and `M=9` is the published sound-diffusion mode;
- each physical `PLn/PFn` socket is contextual: the same configurator position can mean a light point, automation function, scenario selection or audio point depending on `M`;
- the product includes a programming/lock control whose state affects learning/configuration behavior but is not an OpenWebNet Module.

These facts are the Device-specific interpretation layer above the four fixed Object `34` instances.

English revision d is dated 5 June 2014; French and Italian d are dated 29 April 2014. Their five mode categories and the inspected self-learning/F420 procedures agree, including three/eight/twelve-second stages and rear programming-lock behavior. The heading “none” for self-learning and the detailed `M=0` notation express the no-configurator setup, distinct from an observed installed value. Named electrical coverage excludes Mosaic 078465/079265; catalogue identities remain established, with their individual electrical/procedure evidence still a documentation gap.

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

- `HC4654-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HC4654` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/9e/95/9e9591626666bbcf78b4d7c3168066f05d2b8f4ef5b4f1532ca59158ba383999.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4654); SHA-256 `9e9591626666bbcf78b4d7c3168066f05d2b8f4ef5b4f1532ca59158ba383999`.
- `HS4654-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HS4654` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/fd/dc/fddcaad93e0fcb251f742091057a578b331259a1a29ffc68ae3264dc6ea0860f.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4654); SHA-256 `fddcaad93e0fcb251f742091057a578b331259a1a29ffc68ae3264dc6ea0860f`.
- `HD4654-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HD4654` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/6e/d7/6ed760ddbe69f4660bdb3e572e4caebc34876b72d48cca3b88f80dfc30736d41.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HD4654); SHA-256 `6ed760ddbe69f4660bdb3e572e4caebc34876b72d48cca3b88f80dfc30736d41`.
- `L4654N-ean-product-sheet.pdf`, printed/PDF p. 1: exact `L4654N` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/ff/db/ffdb9e0a99012ec0016fc25661513a84df7a30581840c550e4f499cd07331a10.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4654N); SHA-256 `ffdb9e0a99012ec0016fc25661513a84df7a30581840c550e4f499cd07331a10`.
- `N4654N-ean-product-sheet.pdf`, printed/PDF p. 1: exact `N4654N` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/fd/fa/fdfaf8d50aadc1b1eeb96e97818e9de499b9afb2ec6dbc8b79eed4843e2e2d68.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-N4654N); SHA-256 `fdfaf8d50aadc1b1eeb96e97818e9de499b9afb2ec6dbc8b79eed4843e2e2d68`.
- `NT4654N-ean-product-sheet.pdf`, printed/PDF p. 1: exact `NT4654N` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/9c/72/9c728ac545a3d2ecc106c9418604806488aeaeec545eeab1b6a66d047e1ff32f.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-NT4654N); SHA-256 `9c728ac545a3d2ecc106c9418604806488aeaeec545eeab1b6a66d047e1ff32f`.

- [Semantic review record, 5 October 2026](../../project/review/device-reviews-0011-0020-2026-10-05.md#own-dev-0012)
