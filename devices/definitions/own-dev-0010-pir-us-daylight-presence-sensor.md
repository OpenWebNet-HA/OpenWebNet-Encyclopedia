# PIR+US daylight and presence sensor

## Summary


| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0010` | Project identity |
| Technical description | Flush-mounted dual-technology PIR+ultrasound presence and daylight sensor with IR scenario-control projection | Catalogue + official technical sheets |
| Catalogue item | `1559` - “PIR+US flush mounted sensor” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `44` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `220` | Implementation evidence |
| Declared Modules | `17` | Implementation evidence |
| Categories | Sensor, Lighting, Scenario | Capability model |

The Device combines PIR and ultrasonic presence detection with a brightness sensor, local ON/OFF and learning controls, and an IR transmitter. The canonical firmware projects one configurable sensor Module plus sixteen fixed IR scenario-control Modules.

## Commercial identities


The current 2024 official technical sheet directly names the complete 12-record catalogue cluster:

| Brand / line | References |
| --- | --- |
| BTicino Axolute | `HC/HS/HD4658` |
| BTicino L/N/NT | `L/N/NT4658N` |
| BTicino Light Now | `YD4658`, `YG4658`, `YW4658` |
| BTicino Matix | `AM5658` |
| Legrand Arteor Advance / catalogue Eden Park line | `AC5220MB`, `AC5220MW` |
| Legrand | `067226`, `078486`, `574048`, `574098` |

The current product page markets AC5220MB/MW under Arteor Advance, while MyHOME Suite 3.5.38 assigns those records to the stored line name “Eden Park”. Preserve the source-version naming difference.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00473-f-EN` | official source | 09/06/2014 | six earlier references | [Archived PDF](../../sources/devices/documents/device-doc-pirus-mq00473-f-en/MQ00473-f-EN.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00473-f-EN.pdf) |
| `MQ00473-f-FR` | official source | 22/04/2014 | six earlier references | [Archived PDF](../../sources/devices/documents/device-doc-pirus-mq00473-f-fr/MQ00473-f-FR.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00473-f-FR.pdf) |
| `ST-00001844-EN` | official source | 12/08/2024 | all 12 current cluster references | [Archived PDF](../../sources/devices/documents/device-doc-pirus-st00001844-en/ST-00001844-EN.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00001844-EN.pdf) |
| `ST-00001844-FR` | official source | 12/08/2024 | all 12 current cluster references | [Archived PDF](../../sources/devices/documents/device-doc-pirus-st00001844-fr/ST-00001844-FR.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00001844-FR.pdf) |
| `LE15098AA` | official source | revision to verify | current family | [Archived PDF](../../sources/devices/documents/device-doc-pirus-le15098aa/LE15098AA.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE15098AA.pdf) |

### Material revision difference

The 2014 English sheet specifies `17 mA` current draw. The 2024 successor specifies `15 mA`.

Both originals are retained because this may represent a product revision, documentation correction, or later hardware family expansion. Do not collapse the values into one timeless specification.

The 2024 sheet also updates the software-configuration workflow from MyHOME Suite to Home + Project while explicitly retaining physical configuration.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 flush-mounted modules | Publisher documentation cited in this section |
| Supply | `27 Vdc` | Publisher documentation cited in this section |
| Current draw | `15 mA` in the 2024 sheet | Publisher documentation cited in this section |
| Detection technology | PIR + ultrasound, 180° | Publisher documentation cited in this section |
| Brightness sensor | integrated | Publisher documentation cited in this section |
| Front controls | ON/OFF button + LEARN button / LED | Publisher documentation cited in this section |
| IR | integrated transmitter | Publisher documentation cited in this section |
| Flush box depth | `40 mm` | Publisher documentation cited in this section |
| Weight | `60 g` | Publisher documentation cited in this section |
| Impact protection | `IK04` | Publisher documentation cited in this section |
| Ingress protection | `IP20` | Publisher documentation cited in this section |
| Time-delay range | `5 s .. 59 min 59 s` | Publisher documentation cited in this section |
| Brightness range | `20 .. 1275 lux` | Publisher documentation cited in this section |
| Operating temperature | `-5 .. +45 °C` | Publisher documentation cited in this section |
| Storage temperature | `-20 .. +70 °C` | Publisher documentation cited in this section |
| Physical configurator sockets | `A`, `PL`, `M`, `S`, `T`, `D` | Publisher documentation cited in this section |

The 2024 sheet establishes:


The six documented sockets independently support the expected ordinary addressed-form configurator count, pending hardware corroboration.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1559` | Canonical catalogue |
| Item model / `modobj` | `44` | Canonical catalogue / retained definition |
| Main system | Lighting / Automation | Canonical catalogue / retained definition |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `220` | `-1` | `-1` | `-1` | `17` | catalogue default | wildcard / unspecified applicability |

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

## Module, Object, and Virgin Object model

### Objects

| Firmware | Object | Description | Relationship |
| --- | --- | --- | --- |
| `220` | `431` | IR scenario control | catalogue firmware/Object relation |
| `220` | `119` | Stand alone presence sensor | catalogue firmware/Object relation |
| `220` | `128` | Scenarios daylight and presence sensor | catalogue firmware/Object relation |
| `220` | `164` | Scenarios daylight sensor | catalogue firmware/Object relation |
| `220` | `165` | Scenarios presence sensor | catalogue firmware/Object relation |
| `220` | `166` | Stand alone daylight sensor | catalogue firmware/Object relation |
| `220` | `168` | Stand alone daylight and presence sensor | catalogue firmware/Object relation |

### Virgin Objects

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

### Reconciled topology notes


### Slot 1 - sensing role

The firmware offers these sensor Objects on slot `1`:

| Object | Description | Physical-condition evidence |
| ---: | --- | --- |
| `119` | Stand alone presence sensor | no firmware condition row |
| `128` | Scenarios daylight and presence sensor | `M=2` |
| `164` | Scenarios daylight sensor | no firmware condition row |
| `165` | Scenarios presence sensor | no firmware condition row |
| `166` | Stand alone daylight sensor | `M=1` or `M=4` |
| `168` | Stand alone daylight and presence sensor | `M=0` or `M=3`; designated Object |

Objects without physical condition rows remain valid catalogue alternatives for virtual/advanced configuration; they must not be declared unreachable solely because the physical-condition table does not select them.

### Slots `2..17` - IR scenario controls

Object `431`, **IR scenario control**, is fixed on slots `2..17`, producing sixteen scenario-control Modules.

Its reusable parameters are:

- scenario number `1..255`;
- regulation type: all, lights only, shutters only, stereo amplifiers only;
- identifier fields `ID1 0..255`, `ID2 0..255`, `ID3 0..15`;
- unit/pushbutton number `0..15`.

This is why the Device has 17 catalogue Modules despite appearing physically as one sensor.

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `220` | Catalogue configuration route(s) described in retained notes | retained Device-specific configuration modality |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `220` | `AID` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `220` | `A` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `220` | `PL` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `220` | `M` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `220` | `S` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `220` | `T` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `220` | `D` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |

### Published and reconciled details


| Field | Catalogue domain | Published physical meaning |
| --- | --- | --- |
| `AID` | Device identity | not a physical configurator |
| `A` | `0..9` | physical `1..9`; environment/address |
| `PL` | `0..9` | physical `1..9`; light point |
| `M` | `0..4` | operating mode |
| `S` | `0..4` | movement sensitivity; published physical values no-configurator / `1..3` |
| `T` | `0..9` | timeout preset |
| `D` | `0..5` | daylight threshold preset |

The sheets explicitly state that physical addresses `A=0` and `PL=0` do not exist even though the firmware database stores zero in the underlying ranges.

### Physical timeout and sensitivity mappings

| `T` | Timeout |
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

| `S` | PIR sensitivity |
| ---: | --- |
| no configurator | Low |
| `1` | Medium |
| `2` | High |
| `3` | Very high |

| `D` | Brightness threshold |
| ---: | ---: |
| no configurator | 300 lux |
| `1` | 20 lux |
| `2` | 100 lux |
| `3` | 300 lux |
| `4` | 500 lux |
| `5` | 1000 lux |

## Object configuration surfaces

### Object `119` - Stand alone presence sensor

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `MAIN_GROUP` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `HOURS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `MINUTES` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SECONDS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `FUNC_MODE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PIR` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `US` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `INITIAL_OCCUPANCY` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `MAINTAIN_OCCUPANCY` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `RETRIGGER` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `ALERT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `ENABLE_LOAD_CONTROL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `128` - Scenarios daylight and presence sensor

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `HOURS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `MINUTES` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SECONDS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SCHEMA` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PIR` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `US` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `164` - Scenarios daylight sensor

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `165` - Scenarios presence sensor

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `HOURS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `MINUTES` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SECONDS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SCHEMA` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PIR` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `US` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `166` - Stand alone daylight sensor

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `TYPE_LOOP` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `GD` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DAYLIGHT_SETPOINT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PROVISION_OF_LIGHT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `FUNC_MODE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `LIGHTING_REGULATION` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DAYLIGHT_FACTOR` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `NATURAL_LIGHT_FACTOR` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DAYLIGHT_LEVEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `168` - Stand alone daylight and presence sensor

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `MAIN_GROUP` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `TYPE_LOOP` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `GD` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DAYLIGHT_SETPOINT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PROVISION_OF_LIGHT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `HOURS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `MINUTES` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SECONDS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `FUNC_MODE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PIR` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `US` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `INITIAL_OCC` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `MAINTAIN_OCC` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `RE-TRIGGER` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `ALERT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `LOAD_CONTROL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `LIGHTING_REGULATION` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `NATURAL_LIGHT_FACTOR` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DAYLIGHT_FACTOR` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DAYLIGHT_LEVEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `431` - IR scenario control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `PPT_SCE_1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `TYPE_OF_REGULATION` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `ID1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `ID2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `ID3` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `UNIT_NUMBER` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Reconciled Object notes


The reusable sensor Objects extend far beyond the six physical sockets.

### Presence-oriented Objects `119`, `128`, `165`

These expose combinations of:

- point/group addressing;
- delay as hours/minutes/seconds;
- PIR and ultrasound sensitivity levels Low/Medium/High/Maximum;
- detection scheme: PIR only, US only, PIR and US, PIR or US;
- initial, maintain and retrigger detection selection where applicable;
- automatic, walkthrough, manual-ON/auto-OFF and partial/group modes;
- visual/acoustic alert;
- optional load-control enablement.

### Daylight Object `166`

This adds:

- point/group and reference-actuator addressing;
- open/closed-loop regulation;
- daylight cell group;
- daylight setpoint encoded in 5-lux increments from `0..1275 lux`;
- light contribution from Automatic through `5..1275 lux`;
- auto/manual/partial functional modes;
- lighting-regulation enablement;
- read-only daylight/natural-light factors and measured daylight level.

### Combined daylight/presence Object `168`

This combines the daylight model with:

- up to two sensor groups;
- time delay;
- auto ON/OFF, walkthrough, manual ON/auto OFF and partial/group modes;
- PIR and US sensitivities;
- initial/maintain/retrigger technology selection;
- visual/acoustic alerts;
- load-control and lighting-regulation settings;
- read-only light-factor measurements.

The published 2024 sheet independently documents remote-control adjustment of delay, PIR/US detection scheme, brightness threshold, Auto/Walkthrough/Eco modes, alarm, calibration, adjustment, and contribution-of-light behavior.

## Conditions, filters, and conversions

### Relation filters

| Scope | Filter IDs | Interpretation |
| --- | --- | --- |
| Device/Object relations | `2221`, `2222`, `2223`, `2224`, `2225`, `2226`, `2227`, `2374`, `2387`, `2455`, `2467` | apply before exposing reusable Object values |

### Slot conditions and conversions

| Scope | Condition IDs | Conversion treatment |
| --- | --- | --- |
| Device slots | `4439`, `4461`, `4477`, `4491`, `4505` | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1559` and the installed model | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware without treating wildcard sentinels as literal installed values | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`119`, `128`, `164`, `165`, `166`, `168`, `431`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions, and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

### Existing Device-specific diagnostic notes


| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 44`, commercial identity fields and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | enumerate one sensor Object plus sixteen IR scenario-control Objects | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | resolve sensor/scenario addressing | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/virtual/advanced configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Functional applicability follows the resolved firmware/Object topology and the documented product roles above.

## Observed behavior and corroboration

No additional publishable runtime observation is asserted beyond observations explicitly retained elsewhere on this page.

## Programming

Programming must validate firmware applicability, active Module/Object topology, relation filters, and Device-specific configuration constraints.

## Source reconciliation


The archived 2014/2024 PIR+US material has been reconciled beyond the basic `M/S/T/D` configurator table.

The product-level configuration surface additionally includes:

- Auto and Walkthrough occupancy behaviors;
- Eco/manual-on behavior and switch-off warning;
- Initial, Holding and Retrigger detection-stage choices;
- brightness calibration/adjustment and natural-light contribution;
- software/remote configuration paths in addition to physical configurators;
- product reset and learning/programming workflows;
- revision-dependent software tooling, including the transition from MyHOME Suite-era configuration to Home + Project while retaining physical setup.

These settings explain why reusable sensor Objects expose more behavior than the six physical sockets alone. They remain product-level semantics and should not be collapsed into one generic presence-sensor mode.

## Evidence limits and open work


- Obtain a sanitized fingerprint from known hardware and verify the unusual 17-Module projection.
- Correlate old and new production batches with the 17 mA versus 15 mA documentation difference.
- Determine whether all 12 commercial variants share identical hardware or whether the current technical sheet intentionally spans revised electronics.
- Corroborate the six physical configurator positions and slot-1 mode selection through diagnostics.
- Record real-world IR scenario Object behavior for slots `2..17`.

## Sources


- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
- [Programming](../../programming/)
