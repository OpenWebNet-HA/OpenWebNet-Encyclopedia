# Local Display 1.2 inch bus

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0037` | Project identity |
| Technical description | Two-module 1.2-inch OLED touch display for up to four MyHOME functions | Catalogue + `MQ00692-b-EN` |
| Commercial identities | `L/N/NT4891`, `HC/HS/HD4891`, `067271`, `067272`, `573716`, `573717` | Catalogue + official documentation |
| Catalogue item | `1657` | Implementation evidence |
| Main catalogue system | Local Display / multifunction user interface | Implementation evidence |
| Item model / `modobj` | `70` | Implementation evidence |
| Firmware definition | `11` / `1.0.1` | Implementation evidence |
| Declared Modules | `2` | Implementation evidence |
| Categories | User interface, Scenario, Sound, Temperature control, Energy management | Capability model |

The Local Display is one Physical Device with two catalogue Modules: a function-selected first Module and a fixed Local Display Module. The function selector exposes several protocol roles without turning the product into separate Devices.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - LivingLight | `L/N/NT4891` | established grouped identity | catalogue + `MQ00692-b-EN` |
| BTicino - Axolute | `HC/HS/HD4891` | established grouped identity | catalogue + `MQ00692-b-EN` |
| Legrand - Céliane | `067271` | established identity | catalogue + `MQ00692-b-EN` |
| Legrand - Céliane | `067272` | established identity | catalogue + `MQ00692-b-EN` |
| Legrand - Arteor | `573716` | established identity | catalogue + `MQ00692-b-EN` |
| Legrand - Arteor | `573717` | established identity | catalogue + `MQ00692-b-EN` |
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00692-b-EN` | Technical sheet | revision b / 2014-04-17 | all six current catalogue identity groups; hardware, configuration and available functions | [Archived original](https://archive.openwebnet-ha.org/sha256/b8/56/b856e489d0b6da84d20534a4aafdd61d540cc2d46b15edb0c9c47d0e12d59bc6.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00692_b_EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display | 1.2-inch OLED touch display | `MQ00692-b-EN` |
| Mounting | 2 flush-mounted modules | `MQ00692-b-EN` |
| BUS supply | `18..27 Vdc` | `MQ00692-b-EN` |
| Standby current | max `10 mA` at `27 Vdc` / max `15 mA` at `18 Vdc` | `MQ00692-b-EN` |
| Operating current | max `50 mA` at `27 Vdc` / max `70 mA` at `18 Vdc` | `MQ00692-b-EN` |
| Operating temperature | `5..35 °C` | `MQ00692-b-EN` |
| Local connections | SCS BUS, external temperature probe terminal and USB | `MQ00692-b-EN` |
| Software capacity | `1..4` configured functions | `MQ00692-b-EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1657` | Implementation evidence |
| Main system | Local Display / multifunction user interface | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `70` | Implementation evidence |
| Catalogue buses | `1`, `11`, `12`, `16`, `19` | Implementation evidence |
| Commercial records | `6` | Implementation evidence |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `11` | `1` | `0` | `1` | `2` | catalogue default | explicit catalogue revision |

## Module, Object, and Virgin Object model

| Module / slot | Selection | Object | Role |
| --- | --- | --- | --- |
| `1` | condition `FUN=1` | `617` | Scenario module control - local display |
| `1` | condition `FUN=2` | `419` | Sound diffusion control |
| `1` | condition `FUN=3` | `546` | Slave probe |
| `1` | condition `FUN=4` | `460` | Local display as temperature-control probe |
| `1` | condition `FUN=5` | `468` | Energy load control actuator |
| `2` | fixed | `618` | Local Display |

The first slot is function-selected while Object `618` remains fixed at slot `2`. No Virgin Object relation is present for firmware `11`.

## Configuration modes

| Mode | Meaning | Evidence |
| --- | --- | --- |
| `4` | Product Programming | Implementation evidence + USB/software configuration in `MQ00692-b-EN` |

The official sheet also documents physical configurator use. Catalogue mode `4` describes the implementation programming association; it does not erase the physical configuration surface printed on the product.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | Device identity | - | implementation identity field |
| `A` | `0..9` | `0` | catalogue address field corresponding to the first zone/address configurator position |
| `PL` | `0..9` | `0` | catalogue address field corresponding to the second zone/address configurator position |
| `MOD` | `0..4` | `0` | mode selector |
| `FUN` | stored enum `0..4` | `0` | function selector; slot conditions also reference `FUN=5` |

The rear product labelling uses `ZA/ZB`, `MOD` and `FUN`, while firmware `11` names the two address fields `A` and `PL`. This naming difference is preserved. More importantly, the stored `FUN` enumeration stops at `4` while catalogue slot condition `4931` selects Object `468` with `FUN=5`.

## Object configuration surfaces

### Object `617` - Scenario module control - local display

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `SCE_BUTT_1` | `1..16` | `1` | scenario button 1 |
| `SCE_BUTT_2` | `1..16` | `2` | scenario button 2 |
| `SCE_BUTT_3` | `1..16` | `3` | scenario button 3 |
| `SCE_BUTT_4` | `1..16` | `4` | scenario button 4 |

### Object `419` - Sound diffusion control

| Surface | Fields | Meaning |
| --- | --- | --- |
| Mode | `M` | ON/volume, OFF/volume, track/source and toggle roles |
| Addressing | `ADDR_TYPE`, `A`, `PF` | point, area or general audio addressing |
| Input behavior | `TYPE_CONTACT`, `IS_FOLLOW_ME` | contact type and follow-me behavior |
| Source selection | `SOURCE`, `SUB_SOURCE`, `CHANNEL` | source, sub-source and audio/video channel |

### Object `546` - Slave probe

| Surface | Fields | Meaning |
| --- | --- | --- |
| Zone | `ZAZB`, `SLA`, `ZAZB_CENTRALE` | zone, slave number and central-unit address |
| Local behavior | `LED_ENABLE`, `EXTERNAL_SENSOR_TYPE` | LED and external sensor selection |
| Seasonal mode | `RISC`, `COND` | winter and summer enable state |

### Object `460` - Local display as temperature control probe

| Surface | Fields | Meaning |
| --- | --- | --- |
| Zone | `ZAZB`, `SLA`, `ZAZB_CENTRAL` | zone, slave number and control-unit address |
| Seasonal mode | `COLD`, `WARM` | summer and winter enable state |

### Object `468` - Energy load control actuator

| Surface | Fields | Meaning |
| --- | --- | --- |
| Load identity | `PHASE`, `P`, `LOAD_TYPE`, `STATE_ON_ENABLE`, `WITH_SENSOR` | phase, priority, load type, central-unit enable behavior and sensor presence |
| Electrical model | `VOLTAGE_TYPE`, `AC_RATED_VOLTAGE`, `DC_RATED_VOLTAGE`, `POWER_FACTOR` | AC/DC selection and rated electrical values |
| Diagnostics and thresholds | `IDIFF_LOW_THR`, `IDIFF_HIGH_THR`, `STANDBY_THRESHOLD` | differential-current and standby thresholds |

### Object `618` - Local Display

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `ADDRESS` | `0..95` | `0` | Local Display address |

## Conditions, filters, and conversions

| Condition ID | Slot | Predicate | Selected Object | Meaning |
| --- | --- | --- | --- | --- |
| `4912` | `1` | `FUN=1` | `617` | scenario function |
| `4913` | `1` | `FUN=2` | `419` | sound diffusion function |
| `4929` | `1` | `FUN=3` | `546` | slave temperature probe |
| `4930` | `1` | `FUN=4` | `460` | local display temperature-control probe |
| `4931` | `1` | `FUN=5` | `468` | energy/load-control function |

| Filter ID | Object | Field | Meaning |
| --- | --- | --- | --- |
| `3755` | `546` | `EXTERNAL_SENSOR_TYPE` | External temperature sensor type |

The `FUN=5` condition lies outside the stored firmware `FUN` enum `0..4`. It is retained as a catalogue inconsistency and must not be “corrected” by guessing whether the condition or enum is stale.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 70` and product identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | corroborate firmware `1.0.1` | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | identify the function-selected slot-1 Object and fixed Object `618` | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | observe the address context for the selected function | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configured `A`/`PL`/`MOD`/`FUN` and software/physical configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The publisher lists scenario control, temperature control, sound system, consumption display, load management and software-only advanced scenario functions. The active OpenWebNet-facing first Module depends on `FUN`; Object `618` represents the Local Display itself as the second Module.

## Observed behavior and corroboration

No sanitized hardware fingerprint is currently retained. Runtime testing is especially useful here because `FUN=5` is present in topology conditions but absent from the stored firmware enum.

## Programming

The USB interface supports configuration, firmware-related operations and character/icon resources. Programming software must resolve the function-selected Object before presenting Object-specific settings and must preserve the `A`/`PL` versus printed `ZA/ZB` naming boundary.

## Source reconciliation

`MQ00692-b-EN` corroborates all six commercial identity groups, the two-module hardware, 1.2-inch display, electrical limits, USB/external-probe connections and the product-level function set. The catalogue adds the two-Module topology and exact reusable Object surfaces.

Two implementation tensions remain explicit: the database names the physical address fields `A`/`PL` while the product labels them `ZA/ZB`, and `EN_CONF_RANGE` lists `FUN=0..4` while slot condition `4931` requires `FUN=5`.

## Evidence limits and open work

- Hardware-corroborate `DIMENSION 30` for each available `FUN` role.
- Determine whether `FUN=5` is accepted by firmware `1.0.1` despite its absence from the stored firmware enum.
- Correlate the catalogue `A`/`PL` field names with the printed `ZA/ZB` positions through a real configuration read.

## Sources

- [Device Source Index](../../sources/devices/index.md)
- [Device Database Inventory](../inventory/)
- [`MQ00692-b-EN` archived original](https://archive.openwebnet-ha.org/sha256/b8/56/b856e489d0b6da84d20534a4aafdd61d540cc2d46b15edb0c9c47d0e12d59bc6.pdf)
