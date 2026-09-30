# PIR flush-mounted daylight and presence sensor

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0016` | Project identity |
| Technical description | Flush-mounted PIR daylight and presence sensor with scenario-control functions | Catalogue + official documentation |
| Catalogue item | `1566` - “PIR flush mounted sensor” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `43` | Implementation evidence |
| Firmware definition | wildcard `-1.-1.-1`, firmware `222` | Implementation evidence |
| Declared Modules | 17 | Implementation evidence |
| Configuration modes | Physical, Virtual, Advanced | Implementation evidence |
| Categories | Sensor, Multifunction, Scenario | Capability model |

This family is the PIR-only counterpart to the PIR+US Green Switch family. Its catalogue topology contains one configuration-selected sensor Object at slot `1` and sixteen fixed IR scenario-control Objects at slots `2..17`.

## Commercial identities

The canonical catalogue groups eight Device records. Several BTicino database codes collapse finish variants into one row, so the printed identity list is larger.

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino Axolute | `HC4659`, `HS4659`, `HD4659` | Documented commercial identities | Catalogue cluster + archived historical sheet / compatibility table |
| BTicino L/N/NT | `L4659N`, `N4659N`, `NT4659N` | Documented commercial identities | Catalogue cluster + archived historical sheet / compatibility table |
| BTicino Matix | `AM5659` | Documented commercial identity | Catalogue + archived historical sheet |
| BTicino Living Now | `K4659` | Documented current commercial identity | Catalogue + archived current technical sheet |
| Legrand Arteor | `574046`, `574096` | Documented commercial identities | Catalogue + archived historical sheet / compatibility table |
| Legrand Céliane | `067225` | Documented commercial identity | Catalogue + archived historical sheet / compatibility table |
| Legrand Mosaic | `078485` | Compatibility-documented identity | Catalogue + archived compatibility table |

These documents collectively cover every commercial record in the canonical item cluster.

## Documentation

| Document | Type | Coverage | Archived original |
| --- | --- | --- | --- |
| `MQ00474-e-FR` | Historical technical sheet | legacy PIR Green Switch family | [Archived PDF](../../sources/devices/documents/device-doc-pir-mq00474-e-fr/MQ00474-e-FR.pdf) |
| `ST_00000220_EN` | Current-generation technical sheet | `K4659` and PIR flush-mounted sensor | [Archived PDF](../../sources/devices/documents/device-doc-pir-st00000220-en/ST_00000220_EN.pdf) |
| `ST-00002122-EN` | Compatibility table | current server compatibility across legacy references | [Archived PDF](../../sources/devices/documents/device-doc-myhome-compatibility-st00002122-en/ST-00002122-EN.pdf) |

Historical and current sheets should remain separate evidence because product ranges, software requirements and presentation evolved.

## Product characteristics

The archived documentation describes a flush-mounted PIR motion/presence and daylight sensor for SCS lighting management. It supports physical configurators and software configuration.

The current K4659 sheet documents compatibility requirements for contemporary MyHOME configuration software, while the historical sheet documents the earlier range identities and physical operating concepts. Those revision-specific software requirements should not be projected backwards onto every legacy unit.

## Identity and firmware

| Field | Value |
| --- | --- |
| `EN_ITEM.id_item` | `1566` |
| `AS_ITEM_SYSTEM.modobj` | `43` |
| system | Lighting / Automation |
| firmware | `222` |
| firmware applicability | `-1.-1.-1` wildcard / unspecified |
| slots | `17` |
| configuration modes | Physical, Virtual, Advanced |

## Module and Object model

### Slot 1: sensor role

Slot `1` can represent several sensor roles:

| Object | Description | Stored condition |
| ---: | --- | --- |
| `119` | Stand alone presence sensor | alternative candidate |
| `128` | Scenarios daylight and presence sensor | `M=2` |
| `164` | Scenarios daylight sensor | alternative candidate |
| `165` | Scenarios presence sensor | alternative candidate |
| `166` | Stand alone daylight sensor | `M=1` or `M=4` |
| `168` | Stand alone daylight and presence sensor | `M=0` or `M=3` |

Object `168` is marked fixed/designated in the slot table, while other sensor Objects are alternatives selected by configuration. The absence of explicit condition rows on Objects `119`, `164` and `165` should not be “completed” by guessing missing branches.

### Slots 2 through 17: IR scenario controls

Object `431`, **IR scenario control**, is fixed at each slot from `2` through `17`, giving sixteen IR scenario-control Modules in addition to the primary sensor Module.

There are no Virgin Objects.

## Firmware-scoped physical configuration

| Field | Catalogue domain | Published physical interpretation |
| --- | --- | --- |
| `AID` | identity field | not a physical configurator |
| `A` | `0..9` | environment/address; published physical values `1..9` |
| `PL` | `0..9` | light point; published physical values `1..9` |
| `M` | `0..4` | sensor operating mode |
| `S` | `0..4` | sensitivity selector in database; published physical selector `0..3` |
| `T` | `0..9` | time selector |
| `D` | `0..5` | daylight threshold selector |

### Published `M` modes

The product documentation describes the modes as:

| `M` | Role |
| ---: | --- |
| `0` | automatic load control from motion/presence and ambient brightness |
| `1` | daylight-only operation, movement detection disabled |
| `2` | sends movement/brightness information for scenario-management use |
| `3` | presence plus constant-brightness / dimmer regulation |
| `4` | daylight-oriented manual-ON / automatic-OFF constant-brightness operation |

### Published `T` timing presets

| `T` | Delay |
| ---: | --- |
| no configurator | 15 min |
| `1` | 30 s |
| `2` | 1 min |
| `3` | 2 min |
| `4` | 5 min |
| `5` | 10 min |
| `6` | 15 min |
| `7` | 20 min |
| `8` | 30 min |
| `9` | 40 min |

### Published sensitivity and daylight presets

The published physical sensitivity selector has no configurator = Low, `1=Medium`, `2=High`, `3=Very high`.

The daylight selector documents no configurator = 300 lux, then approximately `20`, `100`, `300`, `500`, and `1000 lux` for `D=1..5`.

## Source-model discrepancies

Two differences must remain explicit:

1. the catalogue allows `A=0` and `PL=0`, while the printed physical ranges are narrower in the product sheet;
2. the catalogue declares `S=0..4`, while the published physical selector only documents `0..3`.

These may reflect virtual/advanced configuration, implementation tolerance, or source drift. They are not grounds for silently changing either source.

## Reusable Object configuration

### Presence and combined sensor roles

Objects `119` and `168` expose point-to-point/group addressing, referent actuator addresses, group membership, timing, functional mode, sensitivity and detection behavior. The combined Object `168` additionally carries daylight-loop/regulation state and daylight factors.

### Daylight roles

Object `166` includes:

- point-to-point/group addressing;
- open/closed loop;
- daylight group;
- encoded daylight setpoint `0..1275 lux` in 5-lux increments;
- provision-of-light value with automatic mode plus `5..1275 lux`;
- functional mode and lighting-regulation flag;
- daylight/natural-light factors and daylight level.

Object `164` is the simpler scenario daylight Object with A/PL addressing.

### Scenario sensor roles

Object `128` combines A/PL, delay, detection schema and sensitivity. Object `165` provides the corresponding scenario presence surface.

### IR scenario Object `431`

Each of the sixteen fixed IR Modules exposes:

- scenario number `1..255`;
- regulation type: all, lights, shutters, or stereo amplifiers;
- three ID components;
- push-button/unit number.

## Diagnostic applicability

| Surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 43`, brand/line and installed configurator count | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 30` | corroborate the selected slot-1 sensor Object and sixteen fixed IR Objects | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect Module address/context | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration and compare physical/virtual domains | [Configuration](../../diagnostics/dim35-configuration.md) |

## Programming

Programming must treat the slot-1 Object as configuration-dependent and slots `2..17` as distinct fixed IR scenario-control Modules. It must also preserve the source-level domain differences above instead of coercing the database to the PDF or vice versa.

## Source reconciliation

The PIR-only sensor documentation has been reconciled beyond the physical `M/S/T/D` selectors.

Product-level settings include Walkthrough and Eco/manual-on behavior, detection-stage choices, switch-off warning, brightness calibration/adjustment, natural-light contribution, software/remote configuration and reset/learning workflows. These settings explain behavior available through the sensor Object configuration surface that is not representable by the six physical sockets alone.

The known source discrepancy in the physical sensitivity domain remains visible, and Objects without explicit physical condition rows remain alternatives requiring configuration/hardware corroboration rather than guessed mappings.

## Corroboration status and open work

- Obtain a sanitized fingerprint from at least one legacy reference and one K4659.
- Verify the observed 17-Module `DIMENSION 30` projection.
- Corroborate the actual physical-configurator count and the `S` domain.
- Establish the precise reachability of Objects `119`, `164` and `165`, which have no explicit slot-condition rows.
- Archive further language and historical revisions of the PIR sheet.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
