# Two-module zero-crossing actuator and control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0006` | Project identity |
| Technical description | Two-module two-relay actuator with integrated command functions and zero-crossing switching | Catalogue + official technical sheet |
| Catalogue item | `2180` - “Flush mounted actuator and free control with zero crossing” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `82` | Implementation evidence |
| Firmware definition | `1.0.-1` wildcard-build applicability, firmware `707` | Implementation evidence |
| Declared Modules | 4 | Implementation evidence |
| Categories | Actuator, Command, Multifunction, Lighting, Automation, Scenario | Capability model |

Item `2180` is the zero-crossing counterpart of the multifunction actuator/control family. It contains two independent relays and front controls, and can expose actuator functions on slots `1..2` plus command/scenario functions on slots `3..4`.

The official 2021 technical sheet directly documents all seven commercial references in the current catalogue cluster.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Arnould Espace Evolution | `64195` | Documented commercial reference | Catalogue + official technical sheet |
| Arnould Espace Evolution | `64196` | Documented commercial reference | Catalogue + official technical sheet |
| Arnould Espace Evolution | `64393` | Documented commercial reference | Catalogue + official technical sheet |
| BTicino Axolute | `H4672M2` | Documented commercial reference | Catalogue + official technical sheet |
| BTicino L/N/NT | `LN4672M2` | Documented commercial reference | Catalogue + official technical sheet |
| BTicino Matix | `AM5852M2` | Documented commercial reference | Catalogue + official technical sheet |
| Legrand Céliane | `067561` / printed `0 675 61` | Documented commercial reference | Catalogue + official technical sheet |

Shared item membership and the common technical sheet jointly establish this commercial-identity set. Range-specific dimensions and packaging remain commercial metadata.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher URL |
| --- | --- | --- | --- | --- | --- |
| `ST-00000898-EN` | Technical sheet | 23/03/2021 | all seven references | [Archived PDF](../../sources/devices/documents/device-doc-zero-crossing-st00000898-en/ST-00000898-EN.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00000898-EN.pdf) |
| `ST-00000898-FR` | Technical sheet | 23/03/2021 | all seven references | [Archived PDF](../../sources/devices/documents/device-doc-zero-crossing-st00000898-fr/ST-00000898-FR.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00000898-FR.pdf) |
| `LE09285AB` | Instruction sheet | 03/21 | `AM5852M2`, `H4672M2`, `LN4672M2` | [Archived PDF](../../sources/devices/documents/device-doc-zero-crossing-le09285ab/LE09285AB.pdf) | [Official source](https://dar.bticino.com/asset/Documents/LE09285AB.pdf) |
| `LE09287AB` | Instruction sheet | revision not yet decoded | `067561` | [Archived PDF](../../sources/devices/documents/device-doc-zero-crossing-le09287ab/LE09287AB.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE09287AB.pdf) |

The English and French technical sheets are distinct archived byte streams and therefore remain separate source revisions/language variants.

## Physical and electrical characteristics

The 2021 technical sheet establishes:

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting size | 2 flush-mounted modules | Official technical sheet |
| Front controls | 4 buttons and 4 two-colour LEDs | Official technical sheet |
| Local outputs | 2 independent relays | Official technical sheet |
| SCS supply | `18..27 Vdc` | Official technical sheet |
| Current draw | `7 mA` standby; `16 mA` max with one shutter/light; `24 mA` max with two lights | Official technical sheet |
| Operating temperature | `0..40 °C` | Official technical sheet |
| Storage temperature | `-5..45 °C` | Official technical sheet |
| Mains side | `110..230 Vac`, `50..60 Hz` | Official technical sheet |
| Maximum resistive/incandescent class at 230 Vac with neutral | `1380 W / 6 A` | Official technical sheet |
| Motor/LED-CFL class at 230 Vac with neutral | `460 W / 2 A`; `250 W / 1 A` respectively | Official technical sheet |
| Fluorescent/electronic-transformer class at 230 Vac with neutral | `460 W / 2 A` | Official technical sheet |
| Ferromagnetic-transformer class at 230 Vac with neutral | `460 VA / 2 A`, cos φ 0.5 | Official technical sheet |
| Physical configurator positions | `A1`, `PL1`, `M1`, `A2`, `PL2`, `M2` | Official technical sheet |

The sheet also documents reduced load limits when used without a connected neutral. Keep neutral-dependent load tables revision-scoped rather than collapsing them into one rating.

The control and contact parts are physically separable and can be wired separately.

## Identity and firmware

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2180` | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `82` | Implementation evidence |
| System | Lighting / Automation | Implementation evidence |
| Firmware | `707` | Implementation evidence |
| Firmware applicability | version `1`, revision `0`, build `-1` | Implementation evidence |
| Firmware slots | `4` | Implementation evidence |

The wildcard build does not assert that installed hardware reports build `-1`. Read the actual firmware through the canonical diagnostic path.

Brand and line values differ by commercial identity, so `modobj = 82` identifies the technical core while `BRAND` and `LINE` narrow the marketed reference.

## Module and Object model

Firmware `707` declares the same four-role structural pattern as the non-zero-crossing actuator/control family, but it is a distinct technical item and firmware definition.

| Object | Description | Slots | Relationship |
| ---: | --- | --- | --- |
| `6` | Light actuator | `1`, `2` | designated actuator Object |
| `7` | Automation actuator | `1` | alternative |
| `400` | Light control | `3`, `4` | designated command Object |
| `401` | Automation control | `3`, `4` | alternative |
| `404` | Scheduled scenario | `3`, `4` | alternative |
| `406` | Scheduled scenario PLUS | `3`, `4` | alternative |

Virgin Object `510`, **Automation relay virgin**, applies to slots `1..2` and permits Blind actuator `1`, Light actuator `6`, and Automation actuator `7`.

Virgin Object `500`, **Automation double command virgin**, applies to slots `3..4` and permits Light control `400`, Automation control `401`, Scheduled scenario `404`, Scheduled scenario PLUS `406`, and AUX control `407`.

Installed Object selection belongs to [`DIMENSION 30`](../../diagnostics/dim30-modules.md).

## Configuration modes

The catalogue declares:

- Physical configuration
- Virtual Configuration
- Advanced Configuration

The official sheet independently documents physical configuration and MyHOME Suite configuration. In virtual configuration, front-button functions can be independent from local actuator functions, and the software exposes four independent addresses: two actuator addresses and two front-control addresses.

## Firmware-scoped physical configuration

| Field | Catalogue domain | Role |
| --- | --- | --- |
| `AID` | Device identity field | not a physical configurator |
| `A1` | `0..9` | local actuator address |
| `PL1` | `0..9` | local actuator point |
| `M1` | `0..8`, `O/I`, `OFF`, `UP/DOWN`, `UP/DOWN monostable`, `CEN`, `PUL` | first/local mode |
| `A2` | `0..9` | second actuator or remote-control address |
| `PL2` | `0..9` | second actuator or remote-control point |
| `M2` | same stored enum as `M1` | second/remote mode |

The 2021 technical sheet uses physical `A1/A2 = 1..9` and `PL1/PL2 = 1..9` for ordinary point-to-point addressing, while virtual configuration supports room `0..10`, lighting point `0..15`, and group `0..255` ranges.

### Source irregularities

The catalogue condition matrix contains selectors that are absent from the firmware-level enum, including `M2=ON`, scope values such as `A2=GEN/GR/AMB`, and malformed/truncated condition strings. The official technical sheet independently documents ON, room, group, and general remote-control modes.

Preserve this as a source-model difference: the stored firmware field domain is not sufficient by itself to enumerate every condition token used by the converter.

## Condition-selected topology

The high-level branches are:

| Module | Selected Object | Principal selector family |
| ---: | --- | --- |
| `1` | Light actuator `6` | `M1=0..4`, `O/I`, `PUL`; or two-light mode with `M1=CEN` |
| `1` | Automation actuator `7` | `M1=5..8`, `OFF`, `UP/DOWN`, `UP/DOWN monostable` |
| `2` | Light actuator `6` | two-load lighting branches under `M1=CEN` |
| `3` | Light control `400` | front/local command paired with lighting mode |
| `3` | Automation control `401` | front/local command paired with automation mode |
| `4` | Light control `400` | remote lighting command branches |
| `4` | Automation control `401` | remote automation command branches |
| `4` | Scheduled scenario `404` | `M2=CEN` branch |
| `4` | Scheduled scenario PLUS `406` | stored implementation selector branch |

The matrix references conversion rules `4`, `20`, `25`, `26`, `95`, `96`, `97`, and `550`. Generic conversion-rule evaluation belongs in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Published operating modes

The official sheet documents four major product arrangements:

1. one lighting or shutter load with local control;
2. two independent lighting loads with two local controls;
3. one lighting load with local control plus remote-actuator/scenario control;
4. one shutter load with local control plus remote-actuator/scenario control.

For lighting, physical modes include cyclic ON/OFF, separate ON/OFF, slave operation, PUL, and delayed-OFF presets. For automation, physical modes include timed UP/DOWN, bistable and monostable shutter control.

The remote-control side supports point-to-point, room, group, and general addressing plus lighting, automation, and programmed-scenario functions. Virtual configuration exposes a broader parameter surface than physical configurators.

Generic WHO frame grammar remains canonical under [WHO 1 - Lighting](../../functional/who-1-lighting/) and [WHO 2 - Automation](../../functional/who-2-automation/).

## Reusable Object configuration surfaces

The Device references the same reusable actuator/control Object families already documented by the Device Model:

- Light actuator `6`: address, master/slave/PUL mode, local-button mode, delayed off, reset state, load-control behavior, subtype, groups;
- Automation actuator `7`: address, actuator mode, shutter-control mode, stop time, subtype, groups;
- Light control `400`: point/area/group/general addressing, command mode, installation/destination level, reference address, timing/dimming fields;
- Automation control `401`: point/area/group/general addressing, bistable/monostable/blades mode, installation/destination level;
- Scheduled scenario `404`: address, button numbers, AUX input, restart delay;
- Scheduled scenario PLUS `406`: scenario-number and button fields;
- AUX control `407`: AUX channel and command mode when reached through Virgin Object `500`.

A reusable Object parameter is a candidate capability until the firmware condition/filter model makes it reachable for this Device.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 82`, brand, line, and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware/build | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3`, `6`, `13` | hardware, microcontroller, and Device ID when supported | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | determine the four installed Module/Object roles | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine Module system/address configuration | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values | [Configuration](../../diagnostics/dim35-configuration.md) |

The six physical configurator positions documented by the official sheet provide independent evidence for the expected ordinary addressed-form configurator count, but an observed `DIMENSION 1` read is still required for hardware corroboration.

## Programming

A programmer must resolve local actuator topology and front/remote command topology separately. It must evaluate the Device-specific condition/conversion graph rather than treating this as one fixed actuator Object.

See [Configuration Programming](../../programming/configuration-programming.md), [Object Programming](../../programming/object-programming.md), and [Programming Validation](../../programming/validation.md).

## Corroboration status and open work

- Add sanitized hardware fingerprints for at least one commercial variant.
- Corroborate installed `modobj`, firmware/build, configurator count, Module/Object topology, addresses, and configuration.
- Continue document discovery for older revisions and range-specific sheets.
- Compare zero-crossing item `2180` experimentally with non-zero-crossing item `1184`, keeping hardware and load-control differences explicit.
- Resolve catalogue conditions that use values outside the firmware-level physical enum.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
- [Programming](../../programming/)
