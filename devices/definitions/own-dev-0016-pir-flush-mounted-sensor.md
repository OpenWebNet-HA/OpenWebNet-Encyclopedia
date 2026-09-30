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
| Declared Modules | `17` | Implementation evidence |
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
| BTicino Axolute catalogue combined code | `HC/HS/HD4659` | Catalogue combined identity | Implementation evidence |
| BTicino L/N/NT catalogue combined code | `L/N/NT4659N` | Catalogue combined identity | Implementation evidence |

These documents collectively cover every commercial record in the canonical item cluster.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00474-e-FR` | Historical technical sheet | revision/date not yet pinned | legacy PIR Green Switch family | [Archived PDF](../../sources/devices/documents/device-doc-pir-mq00474-e-fr/MQ00474-e-FR.pdf) | publisher source not currently retained |
| `ST_00000220_EN` | Current-generation technical sheet | revision/date not yet pinned | `K4659` and PIR flush-mounted sensor | [Archived PDF](../../sources/devices/documents/device-doc-pir-st00000220-en/ST_00000220_EN.pdf) | publisher source not currently retained |
| `ST-00002122-EN` | Compatibility table | revision/date not yet pinned | PIR family references occur on printed pp. 8, 11 / PDF pp. 8, 11 | [Archived PDF](../../sources/devices/documents/device-doc-myhome-compatibility-st00002122-en/ST-00002122-EN.pdf) | publisher source not currently retained |

Historical and current sheets should remain separate evidence because product ranges, software requirements and presentation evolved.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Sensor functions | PIR motion/presence and ambient-daylight sensing | `MQ00474-e-FR` / `ST_00000220_EN` |
| Mounting | flush-mounted | `MQ00474-e-FR` / `ST_00000220_EN` |
| Configuration | physical configurators and software configuration | `MQ00474-e-FR` / `ST_00000220_EN` |

Historical and current sheets remain revision-scoped; contemporary software requirements must not be projected backwards onto every legacy unit.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1566` | Implementation evidence |
| Main system | Lighting / Automation | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `43` | Implementation evidence |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `222` | `-1` | `-1` | `-1` | `17` | not stated | wildcard applicability |

Wildcard values are catalogue applicability sentinels, not claims about an installed firmware version.

## Module, Object, and Virgin Object model

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

## Configuration modes

| Mode / modality | Evidence |
| --- | --- |
| Physical configuration | product documentation + implementation evidence |
| Virtual Configuration | implementation evidence |
| Advanced Configuration | implementation evidence |

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | identity field | - | not a physical configurator |
| `A` | `0..9` | - | environment/address; published physical values `1..9` |
| `PL` | `0..9` | - | light point; published physical values `1..9` |
| `M` | `0..4` | - | sensor operating mode |
| `S` | `0..4` | - | sensitivity selector in database; published physical selector `0..3` |
| `T` | `0..9` | - | time selector |
| `D` | `0..5` | - | daylight threshold selector |

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

## Object configuration surfaces

The following subsections account for the complete reusable Object field surface present in the canonical catalogue. They preserve field identity without reproducing database serialization. Detailed Device-specific interpretation follows where available.

### Object `119` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `ADDR_TYPE`, `A`, `PL`, `G` | Addressing type; Area; Light point; Group number |
| Object-specific | `A_R`, `PL_R`, `MAIN_GROUP`, `G1`, `G2`, `PIR`, `US`, `INITIAL_OCCUPANCY`, `MAINTAIN_OCCUPANCY`, `RETRIGGER`, `ALERT`, `ENABLE_LOAD_CONTROL` | Referent area address; Referent light point address; Enable secondary groups; Secondary group 1; Secondary group 2; PIR sensitivity; US sensitivity; Initial occupancy; Maintain detection; Retrigger; Alert; Enable load control |
| Timing | `HOURS`, `MINUTES`, `SECONDS` | Hours; Minutes; Seconds |
| Mode / behavior | `FUNC_MODE` | Functional_mode |

### Object `128` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | Area; Light point |
| Timing | `HOURS`, `MINUTES`, `SECONDS` | Time delay - Hours; Time delay - Minutes; Time delay - Seconds |
| Object-specific | `SCHEMA`, `PIR`, `US` | Detection scheme; PIR sensitivity; US sensitivity |

### Object `164` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | Area; Light point |

### Object `165` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | Area; Light point |
| Timing | `HOURS`, `MINUTES`, `SECONDS` | Time delay - Hours; Time delay - Minutes; Time delay - Seconds |
| Object-specific | `SCHEMA`, `PIR`, `US` | Detection scheme; PIR sensitivity; US sensitivity |

### Object `166` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `ADDR_TYPE`, `A`, `PL`, `G` | Addressing type; Area; Light point; Group number |
| Object-specific | `A_R`, `PL_R`, `GD` | Area of reference actuator; Light point of reference actuator; Daylight cell group |
| Mode / behavior | `TYPE_LOOP`, `FUNC_MODE` | Loop type; Functional_mode (auto/manual/partial) |
| Sensing / regulation | `DAYLIGHT_SETPOINT`, `PROVISION_OF_LIGHT`, `LIGHTING_REGULATION`, `DAYLIGHT_FACTOR`, `NATURAL_LIGHT_FACTOR`, `DAYLIGHT_LEVEL` | Daylight setpoint (Lux); Provision of light (Lux); Lighting regulation; Daylight factor; Natural light factor; Daylight level |

### Object `168` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `ADDR_TYPE`, `A`, `PL`, `G` | Addressing type; Area; Light point; Group number |
| Object-specific | `A_R`, `PL_R`, `MAIN_GROUP`, `G1`, `G2`, `GD`, `PIR`, `US`, `INITIAL_OCC`, `MAINTAIN_OCC`, `RE-TRIGGER`, `ALERT`, `LOAD_CONTROL` | Referent area address; Referent light point address; Enable secondary groups; Sensor group 1; Sensor group 2; Daylight cell group; PIR sensitivity; US sensitivity; Initial detection; Maintain detection; Re-trigger; Alert; Enable load control |
| Mode / behavior | `TYPE_LOOP`, `FUNC_MODE` | Loop type; Functional_mode |
| Sensing / regulation | `DAYLIGHT_SETPOINT`, `PROVISION_OF_LIGHT`, `LIGHTING_REGULATION`, `NATURAL_LIGHT_FACTOR`, `DAYLIGHT_FACTOR`, `DAYLIGHT_LEVEL` | Daylight setpoint (Lux); Provision of light (Lux); Lighting regulation; Natural light factor; Daylight factor; Daylight level |
| Timing | `HOURS`, `MINUTES`, `SECONDS` | Hours; Minutes; Seconds |

### Object `431` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Scenario / button | `PPT_SCE_1` | Scenario number |
| Sensing / regulation | `TYPE_OF_REGULATION` | Regulation type |
| Object-specific | `ID1`, `ID2`, `ID3`, `UNIT_NUMBER` | ID1; ID2; ID3; Push button number |

### Additional Device-specific interpretation

| Object | Role | Principal configuration |
| --- | --- | --- |
| `119` | Stand-alone presence | addressing, referent, groups, timing, sensitivity, detection |
| `128` | Scenario daylight + presence | `A`/`PL`, delay, detection schema, sensitivity |
| `164` | Scenario daylight | `A`/`PL` |
| `165` | Scenario presence | scenario presence configuration |
| `166` | Stand-alone daylight | addressing, loop, daylight group/setpoints/factors |
| `168` | Stand-alone daylight + presence | presence surface plus daylight regulation/factors |
| `431` | IR scenario control | scenario number, regulation type, ID components, push-button/unit |

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

## Conditions, filters, and conversions

| Surface | Catalogue / implementation | Published product source | Interpretation |
| --- | --- | --- | --- |
| `A`/`PL` | domain includes `0..9` | physical values documented as `1..9` | preserve scope difference |
| `S` | domain `0..4` | physical selector `0..3` | preserve source discrepancy |
| Candidate Objects | `119`/`164`/`165` lack explicit condition rows | no complete printed branch mapping | reachability remains to be corroborated |

### Catalogue filter references

| Filter | Object | Field | Source note |
| --- | --- | --- | --- |
| `2113` | `166` | `DAYLIGHT_FACTOR` | Daylight factor |
| `2128` | `166` | `NATURAL_LIGHT_FACTOR` | Natural light factor |
| `2143` | `166` | `DAYLIGHT_LEVEL` | Daylight level |
| `2158` | `168` | `DAYLIGHT_FACTOR` | Daylight factor |
| `2228` | `128` | `SCHEMA` | Detection scheme |
| `2229` | `128` | `US` | US sensitivity |
| `2230` | `165` | `US` | US sensitivity |
| `2231` | `165` | `SCHEMA` | Detection scheme |
| `2232` | `119` | `US` | US sensitivity |
| `2233` | `119` | `INITIAL_OCCUPANCY` | Initial occupancy |
| `2234` | `119` | `MAINTAIN_OCCUPANCY` | Mantain occupancy |
| `2235` | `119` | `RETRIGGER` | Re-trigger |
| `2236` | `119` | `ALERT` | Alert |
| `2237` | `168` | `NATURAL_LIGHT_FACTOR` | Natural light factor |
| `2238` | `168` | `ALERT` | Alert |
| `2239` | `168` | `INITIAL_OCC` | Initial occupancy |
| `2240` | `168` | `MAINTAIN_OCC` | Mantain occupancy |
| `2241` | `168` | `RE-TRIGGER` | Re-trigger |
| `2321` | `168` | `US` | US sensitivity |
| `2372` | `168` | `DAYLIGHT_LEVEL` | Daylight level |
| `2389` | `431` | `TYPE_OF_REGULATION` | Regulation type |
| `2453` | `168` | `DAYLIGHT_SETPOINT` | Daylight setpoint (Lux) |
| `2465` | `168` | `PROVISION_OF_LIGHT` | Provision of light (Lux) |

### Catalogue slot-condition references

| Condition | Slot | Object | Predicate | Conversion reference |
| --- | --- | --- | --- | --- |
| `4477` | `1` | `128` | `M=2` | `` |
| `4461` | `1` | `166` | `M=1` | `` |
| `4505` | `1` | `166` | `M=4` | `` |
| `4439` | `1` | `168` | `M=0` | `` |
| `4491` | `1` | `168` | `M=3` | `` |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 43`, brand/line and installed configurator count | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 30` | corroborate the selected slot-1 sensor Object and sixteen fixed IR Objects | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect Module address/context | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration and compare physical/virtual domains | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The selected slot-1 sensor role participates in lighting presence/daylight control or scenario-oriented sensing. Slots `2..17` are fixed IR scenario-control Modules. Generic lighting/scenario semantics remain canonical under Functional Protocol.

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

Programming must treat the slot-1 Object as configuration-dependent and slots `2..17` as distinct fixed IR scenario-control Modules. It must also preserve the source-level domain differences above instead of coercing the database to the PDF or vice versa.

## Source reconciliation

The PIR-only sensor documentation has been reconciled beyond the physical `M/S/T/D` selectors.

Product-level settings include Walkthrough and Eco/manual-on behavior, detection-stage choices, switch-off warning, brightness calibration/adjustment, natural-light contribution, software/remote configuration and reset/learning workflows. These settings explain behavior available through the sensor Object configuration surface that is not representable by the six physical sockets alone.

The known source discrepancy in the physical sensitivity domain remains visible, and Objects without explicit physical condition rows remain alternatives requiring configuration/hardware corroboration rather than guessed mappings.

## Evidence limits and open work

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
