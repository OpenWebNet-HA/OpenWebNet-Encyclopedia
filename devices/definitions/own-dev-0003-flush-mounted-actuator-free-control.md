# Flush-mounted two-relay actuator and free control

## Summary


| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0003` | Project identity |
| Technical description | Flush-mounted two-relay actuator with integrated/free command functions | Catalogue + vendor catalogue |
| Commercial identities | 9 catalogue records across Arnould, BTicino, and Legrand ranges | Implementation evidence; Arnould subset also vendor-catalogue documented |
| Catalogue item | `1184` - “Flush mounted actuator and free control” | Implementation evidence |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `107` | Implementation evidence |
| Catalogue brand / line | Arnould `BRAND = 6`; Espace Evolution `LINE = 8` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified (`EN_FIRMWARE 157`) | Implementation evidence |
| Declared Modules | `4` | Implementation evidence |
| Categories | Actuator, Command, Multifunction, Lighting, Automation, Scenario | Capability model |

This Device is deliberately modelled as a multifunction Physical Device rather than as one actuator address. Its firmware can expose actuator functions on slots `1..2` and command/scenario functions on slots `3..4`, with the active Object set selected by configuration.

## Commercial identities


The canonical catalogue maps nine commercial Device records to item `1184`, item model `107`, and firmware `157`. Historical Arnould Espace Evolution documentation independently groups `64391`, `64191`, and `64192` in the same two-relay actuator/control family. The remaining six records share the technical capability item in MyHOME Suite but still need individual product-document review.

| Brand / line | Reference | Relationship to technical definition | Evidence |
| --- | --- | --- | --- |
| Arnould - Espace Evolution | `64391` | documented commercial reference | Catalogue + vendor catalogue |
| Arnould - Espace Evolution | `64191` | documented commercial/package variant | Catalogue + vendor catalogue |
| Arnould - Espace Evolution | `64192` | documented commercial/package variant | Catalogue + vendor catalogue |
| BTicino - Axolute | `H4671M2` | shared technical item | Implementation evidence; product-document review pending |
| BTicino - LivingLight | `LN4671M2` | shared technical item | Implementation evidence; product-document review pending |
| BTicino - Matix | `AM5851M2` | shared technical item | Implementation evidence; product-document review pending |
| Legrand - Arteor | `573961` | shared technical item | Implementation evidence; product-document review pending |
| Legrand - Céliane | `067249` | shared technical item | Implementation evidence; product-document review pending |
| Legrand - Céliane | `067556` | shared technical item | Implementation evidence; product-document review pending |

The technical Device ID does not privilege one of these references. Shared-item membership establishes the common catalogue capability core but does not erase possible package, finish, regional, or hardware differences.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| Arnould Espace Evolution catalogue | Historical product catalogue | not stated in retained row | Device/family coverage described by retained source | [Archived original](../../sources/devices/documents/device-doc-64391-espace-evolution-catalogue/Espace-Evolution-catalogue.pdf); `64391` / `64191` / `64192` occur on printed pp. 27, 31 / PDF pp. 27, 32 | Arnould Espace Evolution catalogue |
| MyHOME Suite lighting actuator function documentation | Vendor implementation documentation | not stated in retained row | Device/family coverage described by retained source | - | MyHOME Suite lighting actuator function documentation |
| MyHOME Suite automation actuator function documentation | Vendor implementation documentation | not stated in retained row | Device/family coverage described by retained source | - | MyHOME Suite automation actuator function documentation |

Additional installation sheets and catalogue revisions should be collected rather than treating this list as exhaustive.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Product-specific characteristics | See retained source-derived notes below | Retained publisher evidence |
| Hardware corroboration | Pending unless explicitly observed | Observation status |
| Commercial/package variation | Preserved where documented | Source reconciliation |

The archived historical Arnould catalogue describes `64391` as a two-independent-relay actuator with integrated control, physically or virtually configurable, occupying two modules. It documents simple or double loads, two lighting circuits or a motor, logical relay interlocking by configuration, and control of a remote BUS actuator.

The same source makes the package distinctions explicit: `64391` is supplied without a rocker and accepts either one two-module rocker or two one-module rockers; `64191` is the lighting package, preassembled with two unmarked one-module rocker controls and supplied with blue `0/1` and `CEN` configurators; `64192` is the motor package, preassembled with one two-module Up/Down rocker, supplied with the matching Up/Down configurator, and documented for a motor up to `500 W`.

For the base actuator the catalogue clearly prints `2 A` incandescent/halogen capability, `2 A cosφ 0.5` for ferromagnetic transformers, `70 W` for fluorescent/electronic-transformer loads, and a maximum of two compact-fluorescent/LED lamps. A neighbouring motor figure is typographically ambiguous in extracted text, so this dossier does not normalize that value beyond the unambiguous `64192` `500 W` package statement without page-image verification.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1184` | Canonical catalogue |
| Item model / `modobj` | `107` | Canonical catalogue / retained definition |
| Main system | Lighting / Automation (`id_system = 1`) | Canonical catalogue / retained definition |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `157` | `-1` | `-1` | `-1` | `4` | catalogue default | wildcard / unspecified applicability |

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

## Module, Object, and Virgin Object model

### Objects

| Firmware | Object | Description | Relationship |
| --- | --- | --- | --- |
| `157` | `6` | Light actuator | catalogue firmware/Object relation |
| `157` | `400` | Light control | catalogue firmware/Object relation |
| `157` | `7` | Automation actuator | catalogue firmware/Object relation |
| `157` | `401` | Automation control | catalogue firmware/Object relation |
| `157` | `404` | Scheduled scenario | catalogue firmware/Object relation |
| `157` | `406` | Scheduled scenario PLUS | catalogue firmware/Object relation |

### Virgin Objects

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| `157` | `500` | catalogue candidate/template association |
| `157` | `510` | catalogue candidate/template association |

### Reconciled topology notes


### Catalogue Object alternatives

| Object | Description | Available slot(s) | Designation |
| ---: | --- | --- | --- |
| `6` | Light actuator | `1`, `2` | fixed/designated Light actuator |
| `7` | Automation actuator | `1` | alternative |
| `400` | Light control | `3`, `4` | fixed/designated Light control |
| `401` | Automation control | `3`, `4` | alternative |
| `404` | Scheduled scenario | `3`, `4` | alternative |
| `406` | Scheduled scenario PLUS | `3`, `4` | alternative |

The four Modules must not be confused with the eleven slot/Object association rows in the database.

### Virgin Objects

| Virgin Object | Description | Slots | Permitted Objects |
| ---: | --- | --- | --- |
| `500` | Automation double command virgin | `3`, `4` | `400` Light control; `401` Automation control; `404` Scheduled scenario; `406` Scheduled scenario PLUS; `407` AUX control |
| `510` | Automation relay virgin | `1`, `2` | `1` Blind actuator; `6` Light actuator; `7` Automation actuator |

Object `1` and Object `407` are permitted through the Virgin Object definitions even though they do not appear as direct firmware/Object rows in the extracted `AS_OBJECT_FIRMWARE` set. Preserve that distinction.

Installed Module state is read through [`DIMENSION 30`](../../diagnostics/dim30-modules.md).

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `157` | Physical configuration | retained Device-specific configuration modality |
| `157` | Virtual Configuration | retained Device-specific configuration modality |
| `157` | Advanced Configuration | retained Device-specific configuration modality |


Firmware `157` supports all three catalogue modes:

- Physical configuration
- Virtual Configuration
- Advanced Configuration

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `157` | `AID` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `157` | `A1` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `157` | `PL1` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `157` | `M1` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `157` | `A2` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `157` | `PL2` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `157` | `M2` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |

### Published and reconciled details


The complete firmware-scoped field set is:

| Field | Progressive | Type | Domain | Default / notes |
| --- | ---: | --- | --- | --- |
| `AID` | 0 | user value | Device ID field | not a physical configurator |
| `A1` | 1 | area | `0..9` | default `0` |
| `PL1` | 2 | point | `0..9` | default `0` |
| `M1` | 3 | mode | `0..8`, `9=O/I`, `10=OFF`, `12=UP/DOWN`, `13=UP/DOWN monostable`, `14=CEN`, `15=PUL` | default `0` |
| `A2` | 4 | area | `0..9` | default `0` |
| `PL2` | 5 | point | `0..9` | default `0` |
| `M2` | 6 | mode | same stored domain as `M1` | default `0` |

The six fields `A1/PL1/M1/A2/PL2/M2` are the Device's physical configurator surface in the canonical catalogue. `AID` is an identity field and is not counted as a physical configurator position.

## Object configuration surfaces

### Object `6` - Light actuator

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `M` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `LOCAL_BUTTON` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DELAYED_OFF` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `STATE_RESET` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `LOAD_CONTROL_MODE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `HOURS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `MINUTES` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SECONDS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SUBTYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G3` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G4` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G5` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G6` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G7` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G8` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G9` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G10` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `7` - Automation actuator

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `M` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `LOCAL_BUTTON` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `STOP_TIME` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SUBTYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G3` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G4` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G5` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G6` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G7` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G8` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G9` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G10` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `400` - Light control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `INST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DEST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `HOURS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `MINUTES` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SECONDS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `LEVEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `START_S` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `STOP_S` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DIMMING_S` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `T_TIME` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `401` - Automation control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `INST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DEST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `404` - Scheduled scenario

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `BUTTON_1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `BUTTON_2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `START_DELAY` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `406` - Scheduled scenario PLUS

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PPT_CEN_HIG` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `BUTTON_1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `BUTTON_2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Reconciled Object notes


The tables below preserve the complete reusable Object parameter surfaces referenced by firmware `157`. They are candidate configuration capabilities; firmware conditions, filters, and conversion rules determine the reachable subset for a concrete 64391 configuration.

### Object `6` - Light actuator

| Parameter | Domain |
| --- | --- |
| `A` | `0..10` |
| `PL` | `0..15` |
| `M` | `0=Master`, `11=Slave`, `15=Master PUL`, `16=Slave and PUL` |
| `LOCAL_BUTTON` | `0=Toggle`, `1=ON/OFF`, `9=ON-OFF`, `15=Pushbutton`, `18=Timed ON` |
| `DELAYED_OFF` | `0..255 s` |
| `STATE_RESET` | `0=Restore last value`, `1=Closed`, `2=Open` |
| `LOAD_CONTROL_MODE` | `0=With zero crossing`, `1=Without zero crossing` |
| `HOURS` / `MINUTES` / `SECONDS` | `0..255` / `0..59` / `0..59` |
| `SUBTYPE` | Actuator, Lamp, Valve, Differential restart, Fan, Watering, Controlled socket, Lock |
| `G1..G10` | each `0..255`, where `0` means no group |

### Object `7` - Automation actuator

| Parameter | Domain |
| --- | --- |
| `A` | `0..10` |
| `PL` | `0..15` |
| `M` | `0=Master`, `11=Slave`, `15=Master PUL`, `16=Slave and PUL` |
| `LOCAL_BUTTON` | `12=Bistable`, `13=Monostable`, `14=Bistable and blades` |
| `STOP_TIME` | Infinite; `1..17 s`; `19..60 s`; `2..10 min` through stored values `62..70` |
| `SUBTYPE` | Actuator, Shutter, Curtain, Gate, Garage door, Differential restart |
| `G1..G10` | each `0..255`, where `0` means no group |

The stored `STOP_TIME` enum notably has no `18 s` entry. Preserve the database domain exactly.

### Object `400` - Light control

| Parameter | Domain |
| --- | --- |
| `M` | Toggle, timed ON, dimmer variants, ON/OFF variants, OFF, ON, PUL, blinking `0.5..8 s`, fixed dimmer levels `10..90%`, and customized modes `128..134` |
| `ADDR_TYPE` | `0=Point to point`, `1=Area`, `2=Group`, `3=General` |
| `A` | `0..10` |
| `PL` | `0..15` |
| `G` | `1..255` |
| `INST_LEV` | Private riser, Local bus `1..15`, Standard |
| `DEST_LEV` | Private riser, Local bus `1..15`, All systems |
| `A_R` | `0..10`; `0` means no reference |
| `PL_R` | `0..15`; `0` means no reference |
| `HOURS` / `MINUTES` / `SECONDS` | custom timed-ON components |
| `LEVEL` | `0..100` for customized modes |
| `START_S` / `STOP_S` / `DIMMING_S` | `0..255` for customized modes |
| `T_TIME` | stored timed presets: 1,2,3,4,5,6,15 minutes; 30 seconds; 0.5 seconds; 2 seconds; 10 minutes |
| `IN_AUX_CHANNEL` | `0..15` |

### Object `401` - Automation control

| Parameter | Domain |
| --- | --- |
| `M` | `12=Bistable`, `13=Monostable`, `14=Blades control and bistable` |
| `ADDR_TYPE` | Point to point, Area, Group, General |
| `A` | `0..10` |
| `PL` | `0..15` |
| `G` | `1..255` |
| `INST_LEV` | Private riser, Local bus `1..15`, Standard |
| `DEST_LEV` | Private riser, Local bus `1..15`, All systems |
| `A_R` | `0..10` |
| `PL_R` | `0..15` |
| `IN_AUX_CHANNEL` | `0..15` |

### Object `404` - Scheduled scenario

| Parameter | Domain |
| --- | --- |
| `A` | `0..10` |
| `PL` | `0..15` |
| `BUTTON_1` | `0..31`, default `1` |
| `BUTTON_2` | `0..31`, default `2` |
| `IN_AUX_CHANNEL` | `0..15` |
| `START_DELAY` | `0..255 s`, default `10` |

### Object `406` - Scheduled scenario PLUS

| Parameter | Domain |
| --- | --- |
| `PPT_CEN_LOW` | `0..255`, default `1` |
| `PPT_CEN_HIG` | `0..7`, default `0` |
| `BUTTON_1` | `0..31`, default `1` |
| `BUTTON_2` | `0..31`, default `2` |

Virgin Object `500` additionally permits AUX control Object `407`; its reusable Object parameters should be incorporated when a reachable 64391 configuration or authoritative product source establishes that capability for this Device.

## Conditions, filters, and conversions

### Relation filters

| Scope | Filter IDs | Interpretation |
| --- | --- | --- |
| Device/Object relations | `1167`, `1168`, `1169`, `1170`, `1172`, `1184`, `1185`, `1186`, `1187`, `1188`, `1189`, `1190`, `1191`, `1192`, `1193`, `1194`, `1195`, `1196`, `1200`, `1201`, `1202`, `1203`, `1204`, `1205`, `1704`, `1873` | apply before exposing reusable Object values |

### Slot conditions and conversions

| Scope | Condition IDs | Conversion treatment |
| --- | --- | --- |
| Device slots | `4145`, `4194`, `4195`, `4197`, `4198`, `4199`, `4200`, `4201`, `4202`, `4204`, `4205`, `4206`, `4207`, `4209`, `4210`, `4211`, `4212`, `4214`, `4215`, `4216`, `4217`, `4219`, `4220`, `4222`, `4224`, `4225`, `4227`, `4229`, `4230`, `4231`, `4232`, `4238`, `4239`, `4240`, `4241`, `4242`, `4243`, `4244`, `4245`, `4246`, `4247`, `4248`, `4249`, `4250`, `4251`, `4252`, `4253`, `4255`, `4256`, `4257`, `4258`, `4259`, `4260`, `4261`, `4262`, `4263`, `4264`, `4265`, `4266`, `4267`, `4268`, `4272`, `4273`, `4279`, `4280`, `4291`, `4292`, `4298`, `4299`, `4306`, `4307`, `4908`, `4909`, `4910` | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

### Condition-selected topology


The catalogue contains a substantial condition matrix selecting Object alternatives. The meaningful Device-level branches can be summarized without duplicating the generic condition-engine implementation:

| Module | Selected Object | Stored physical conditions | Conversion rule(s) |
| ---: | --- | --- | --- |
| `1` | Light actuator `6` | `M1=0..4`, `M1=O/I`, `M1=PUL`; also `M1=CEN` with `M2=0..4,O/I,PUL` | `20`, `25` |
| `1` | Automation actuator `7` | `M1=5..8,OFF,UP/DOWN,UP/DOWN monostable` | `26` |
| `2` | Light actuator `6` | `M1=CEN` with `M2=0..4,O/I,PUL` | `25` |
| `3` | Light control `400` | `M1=0..4,O/I,PUL`; also `M1=CEN` with `M2=0..4,O/I,PUL` | `4` |
| `3` | Automation control `401` | `M1=5..8,OFF` and `M1=UP/DOWN,UP/DOWN monostable` | `4`, `550` |
| `3` | Scheduled scenario `404` | catalogue slot alternative; no physical condition row attached to its slot-3 association | - |
| `3` | Scheduled scenario PLUS `406` | catalogue slot alternative; no physical condition row attached to its slot-3 association | - |
| `4` | Light control `400` | branches across `M2=0,O/I,OFF,ON,PUL`, `M1=CEN`, and stored `A2` scope selectors | `4`, `95`, `96`, `97` |
| `4` | Automation control `401` | `M2=UP/DOWN` or `UP/DOWN monostable` with stored `A2` scope selectors | `4`, `95`, `96`, `97` |
| `4` | Scheduled scenario `404` | `M1<>CEN; M2=CEN` | `4` |
| `4` | Scheduled scenario PLUS `406` | stored `M1<>CEN; M2=FAKE` branch | no rule |

The raw catalogue also contains branches whose values are not reachable from firmware `157`'s declared `A2` domain, including `A2=AMB`, `GR`, `GEN` and `AUX`, plus malformed/truncated condition text in a small number of rows and a stored `M2=ON` branch although `ON` is absent from the firmware `M2` enum. These are source facts, not instructions to silently broaden the legal physical domain.

The canonical handling of these irregularities and conversion-rule evaluation is documented in [Catalogue Resolution](../../internals/catalogue-resolution.md#worked-example-firmware-157).

### Worked configuration

For the physically reachable example:

```text
M1=CEN
M2=O/I
```

the selected topology is:

| Slot | Object |
| ---: | --- |
| `1` | `6` Light actuator |
| `2` | `6` Light actuator |
| `3` | `400` Light control |
| `4` | `400` Light control |

This `[6, 6, 400, 400]` result is configuration-dependent, not the unconditional Device topology.

### Conversion rules


The condition matrix references conversion rules `4`, `20`, `25`, `26`, `95`, `96`, `97`, and `550`, with additional jump rules in the stored rule graph.

These rules translate physical item fields into selected Object configuration values. Their generic evaluation semantics and known textual irregularities are canonical in [Catalogue Resolution](../../internals/catalogue-resolution.md). Device-specific rule applicability is retained here through the condition table and rule IDs rather than copying hundreds of generic conversion rows verbatim.

A future machine-readable Device Library build should preserve the complete applicable rule graph, including jump targets and raw strings, from the canonical structured source.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1184` and the installed model | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware without treating wildcard sentinels as literal installed values | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`6`, `7`, `400`, `401`, `404`, `406`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions, and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

### Existing Device-specific diagnostic notes


| Diagnostic surface | 64391-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve item model `107`, brand `6`, line `8`, and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | installed firmware observation, despite wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` / `6` / `13` | hardware, microcontroller, and Device ID when supported | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | determine active Object at each of four Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine per-Module configured system/address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values and physical-configurability flags | [Configuration](../../diagnostics/dim35-configuration.md) |

No generic diagnostic frame is duplicated here.

## Functional applicability


Depending on selected Objects, the Device can participate in:

- [`WHO 1` - Lighting](../../functional/who-1-lighting/) through Light actuator / Light control Objects;
- [`WHO 2` - Automation](../../functional/who-2-automation/) through Automation actuator / Automation control Objects;
- scenario/CEN behavior through Scheduled scenario and Scheduled scenario PLUS Objects.

The Device page establishes **which functions can exist on this hardware**. The linked functional sections remain authoritative for command syntax and general runtime semantics.

## Observed behavior and corroboration

No additional publishable runtime observation is asserted beyond observations explicitly retained elsewhere on this page.

## Programming


This Device is a strong validation case because physical fields can change the active Object topology.

A correct programmer must:

1. resolve the legal firmware-scoped physical domain;
2. evaluate reachable slot conditions;
3. select the resulting Object per Module;
4. apply the relevant conversion-rule graph;
5. validate Object-scoped configuration values;
6. write/verify through the canonical programming workflow.

See [Configuration Programming](../../programming/configuration-programming.md), [Object Programming](../../programming/object-programming.md), and [Programming Validation](../../programming/validation.md).

## Source reconciliation


The historical Arnould material and MyHOME Suite implementation help establish more product detail than the shared technical-item mapping alone:

- `64391` is the two-relay actuator/control base product; `64191` and `64192` are package/use variants in the same documented family rather than independent OpenWebNet capability definitions;
- the marketed product supports simple or double loads, two lighting circuits or one motor, with relay interlocking selected by configuration;
- the integrated controls can operate the local relays or be assigned to remote bus functions, so the four-Module model is intentional rather than an artefact of the catalogue;
- the lighting and automation implementation help supplies the product-specific Master/Slave/PUL and actuator-mode interpretation used by the condition/conversion model.

The historical Arnould catalogue is now archived byte-for-byte and its Device/package facts are reconciled above. Its electrical ratings remain revision-scoped rather than timeless specifications. The MyHOME Suite lighting and automation help remain official external implementation sources and are already represented in the configuration/Object interpretation. Source reconciliation is complete for the currently identified `64391`/`64191`/`64192` source set; direct documentation for the six other commercial records remains a commercial-identity discovery gap.

## Evidence limits and open work


The current dossier is substantially complete for the canonical MyHOME Suite 3.5.38 database representation, but physical-hardware corroboration is still missing.

Priority evidence:

- a sanitized fingerprint from a known physical 64391/64191/64192;
- observed `DIMENSION 1` identity tuple and firmware/hardware versions;
- observed `DIMENSION 30` topology under several physical configurations;
- `DIMENSION 32` and `35` snapshots tied to those configurations;
- authoritative installation sheets documenting the physical configurator layout and package variants;
- confirmation of whether AUX control Object `407` is reachable on this firmware despite appearing only through Virgin Object `500`;
- controlled validation of the catalogue branches whose stored conditions use values outside the declared physical domains.

When these observations arrive, they should be added as corroborating evidence to the existing database-derived facts rather than replacing them.

## Sources


- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Physical Devices](../../device-model/physical-devices.md#64391-64191-and-64192)
- [Firmware](../../device-model/firmware.md#firmware-example)
- [Modules](../../device-model/modules.md#combined-device-example)
- [Objects](../../device-model/objects.md#device-and-object-descriptions)
- [Virgin Objects](../../device-model/virgin-objects.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md#worked-example-firmware-157)
