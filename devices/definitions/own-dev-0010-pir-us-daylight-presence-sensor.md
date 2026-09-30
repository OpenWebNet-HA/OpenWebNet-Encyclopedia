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
| Declared Modules | 17 | Implementation evidence |
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

## Documentation and revision history

| Document | Date | Coverage | Archived original | Publisher |
| --- | --- | --- | --- | --- |
| `MQ00473-f-EN` | 09/06/2014 | six earlier references | [Archived PDF](../../sources/devices/documents/device-doc-pirus-mq00473-f-en/MQ00473-f-EN.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00473-f-EN.pdf) |
| `MQ00473-f-FR` | 22/04/2014 | six earlier references | [Archived PDF](../../sources/devices/documents/device-doc-pirus-mq00473-f-fr/MQ00473-f-FR.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00473-f-FR.pdf) |
| `ST-00001844-EN` | 12/08/2024 | all 12 current cluster references | [Archived PDF](../../sources/devices/documents/device-doc-pirus-st00001844-en/ST-00001844-EN.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00001844-EN.pdf) |
| `ST-00001844-FR` | 12/08/2024 | all 12 current cluster references | [Archived PDF](../../sources/devices/documents/device-doc-pirus-st00001844-fr/ST-00001844-FR.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00001844-FR.pdf) |
| `LE15098AA` | revision to verify | current family | [Archived PDF](../../sources/devices/documents/device-doc-pirus-le15098aa/LE15098AA.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE15098AA.pdf) |

### Material revision difference

The 2014 English sheet specifies `17 mA` current draw. The 2024 successor specifies `15 mA`.

Both originals are retained because this may represent a product revision, documentation correction, or later hardware family expansion. Do not collapse the values into one timeless specification.

The 2024 sheet also updates the software-configuration workflow from MyHOME Suite to Home + Project while explicitly retaining physical configuration.

## Physical and sensing characteristics

The 2024 sheet establishes:

| Property | Value |
| --- | --- |
| Mounting | 2 flush-mounted modules |
| Supply | `27 Vdc` |
| Current draw | `15 mA` in the 2024 sheet |
| Detection technology | PIR + ultrasound, 180° |
| Brightness sensor | integrated |
| Front controls | ON/OFF button + LEARN button / LED |
| IR | integrated transmitter |
| Flush box depth | `40 mm` |
| Weight | `60 g` |
| Impact protection | `IK04` |
| Ingress protection | `IP20` |
| Time-delay range | `5 s .. 59 min 59 s` |
| Brightness range | `20 .. 1275 lux` |
| Operating temperature | `-5 .. +45 °C` |
| Storage temperature | `-20 .. +70 °C` |
| Physical configurator sockets | `A`, `PL`, `M`, `S`, `T`, `D` |

The six documented sockets independently support the expected ordinary addressed-form configurator count, pending hardware corroboration.

## Identity and firmware

| Field | Value |
| --- | --- |
| `EN_ITEM.id_item` | `1559` |
| `AS_ITEM_SYSTEM.modobj` | `44` |
| Firmware | `220` |
| Firmware applicability | `-1.-1.-1` |
| Firmware slots | `17` |
| Configuration modes | Physical, Virtual, Advanced |

## Module and Object model

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

## Firmware-scoped physical configuration

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

## Published physical modes

| `M` | Published behavior | Catalogue slot-1 Object |
| ---: | --- | --- |
| `0` | presence + daylight, automatic light control | `168` |
| `1` | daylight-only automatic control | `166` |
| `2` | report movement/brightness to scenario programmer rather than control lights directly | `128` |
| `3` | presence + daylight with constant-light regulation | `168` |
| `4` | daylight-only constant-light / eco behavior | `166` |

The PDF and database condition table therefore corroborate each other for the five physical `M` values.

## Virtual and advanced sensing configuration

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

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 44`, commercial identity fields and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | enumerate one sensor Object plus sixteen IR scenario-control Objects | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | resolve sensor/scenario addressing | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/virtual/advanced configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Corroboration status and open work

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
