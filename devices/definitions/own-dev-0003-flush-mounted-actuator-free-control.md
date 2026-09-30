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
| Declared Modules | 4 | Implementation evidence |
| Categories | Actuator, Command, Multifunction, Lighting, Automation, Scenario | Capability model |

This Device is deliberately modelled as a multifunction Physical Device rather than as one actuator address. Its firmware can expose actuator functions on slots `1..2` and command/scenario functions on slots `3..4`, with the active Object set selected by configuration.

## Commercial identities and package variants

The canonical catalogue maps nine commercial Device records to item `1184`, item model `107`, and firmware `157`. Historical Arnould Espace Evolution documentation independently groups `64391`, `64191`, and `64192` in the same two-relay actuator/control family. The remaining six records share the technical capability item in MyHOME Suite but still need individual product-document review.

| Brand / line | Reference | Relationship to technical definition | Evidence |
| --- | --- | --- | --- |
| Arnould Espace Evolution | `64391` | documented commercial reference | Catalogue + vendor catalogue |
| Arnould Espace Evolution | `64191` | documented commercial/package variant | Catalogue + vendor catalogue |
| Arnould Espace Evolution | `64192` | documented commercial/package variant | Catalogue + vendor catalogue |
| BTicino Axolute | `H4671M2` | shared technical item | Implementation evidence; product-document review pending |
| BTicino L/N/NT | `LN4671M2` | shared technical item | Implementation evidence; product-document review pending |
| BTicino Matix | `AM5851M2` | shared technical item | Implementation evidence; product-document review pending |
| Legrand Arteor | `573961` | shared technical item | Implementation evidence; product-document review pending |
| Legrand Céliane | `067249` | shared technical item | Implementation evidence; product-document review pending |
| Legrand Céliane | `067556` | shared technical item | Implementation evidence; product-document review pending |

The technical Device ID does not privilege one of these references. Shared-item membership establishes the common catalogue capability core but does not erase possible package, finish, regional, or hardware differences.

## Documentation

| Document / source | Type | Status | Source |
| --- | --- | --- | --- |
| Arnould Espace Evolution catalogue | Historical product catalogue | Official publisher PDF identified, archival copy pending | [PDF](https://assets.legrand.com/general/legrand-fr/ar/doc_ac/clip%20it-catalogue_230x300mm_bd.pdf) |
| MyHOME Suite lighting actuator function documentation | Vendor implementation documentation | Official web source identified | [Vendor documentation](https://myhomeswupdate.bticino.com/MyHOMESuite_Docs/MHS_function_0304b/EN_MHS_function_0304/modalita_attuatore_luci.html) |
| MyHOME Suite automation actuator function documentation | Vendor implementation documentation | Official web source identified | [Vendor documentation](https://myhomeswupdate.bticino.com/MyHOMESuite_Docs/MHS_function_0304b/EN_MHS_function_0304/attuatore_automazione.html) |

Additional installation sheets and catalogue revisions should be collected rather than treating this list as exhaustive.

## Physical characteristics and marketed capability

The historical Arnould catalogue describes `64391` as a two-independent-relay actuator with integrated control, physically or virtually configurable, occupying two modules.

It documents use for simple or double loads, two lighting circuits or a motor, logical relay interlocking by configuration, and the ability to manage a remote bus actuator. The same catalogue presents the related `64191` / `64192` package references with preassembled rockers/configurators for particular uses.

Electrical ratings should remain tied to the exact archived catalogue revision because OCR and catalogue typography can make unit/value extraction fragile; the original PDF is the canonical evidence.

## Identity

| Field | Value | Evidence state |
| --- | --- | --- |
| `EN_DEVICE.code` | `64391` | Implementation evidence |
| sibling Device records | `64191`, `64192`, `H4671M2`, `LN4671M2`, `AM5851M2`, `573961`, `067249`, `067556` | Implementation evidence |
| `EN_ITEM.id_item` | `1184` | Implementation evidence |
| `EN_ITEM.descr` | “Flush mounted actuator and free control” | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `107` | Implementation evidence |
| `EN_BRAND.brand_name` / `brand_modobj` | Arnould / `6` | Implementation evidence |
| `EN_LINE.line_name` / `line_modobj` | Espace Evolution / `8` | Implementation evidence |
| catalogue system | Lighting / Automation, `sys_modobj = 1` | Implementation evidence |

For an installed ordinary addressed Device, the identity fields should be obtained through [`DIMENSION 1` Device Identity](../../diagnostics/dim1-device-identity.md). `OBJECT_MODEL = 107` alone identifies the shared technical item, not one commercial package reference.

## Firmware

Firmware `157` is stored as:

| Component | Value |
| --- | ---: |
| version | `-1` |
| revision | `-1` |
| build | `-1` |
| slots | `4` |
| default | yes |

The established catalogue convention treats explicit `-1` components as wildcard/unspecified applicability, not as a literal physical firmware version. See [Firmware](../../device-model/firmware.md).

## Configuration modes

Firmware `157` supports all three catalogue modes:

- Physical configuration
- Virtual Configuration
- Advanced Configuration

## Module and Object model

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

## Firmware-scoped physical configuration

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

## Condition-selected topology

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

## Object configuration surfaces

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

## Conversion rules

The condition matrix references conversion rules `4`, `20`, `25`, `26`, `95`, `96`, `97`, and `550`, with additional jump rules in the stored rule graph.

These rules translate physical item fields into selected Object configuration values. Their generic evaluation semantics and known textual irregularities are canonical in [Catalogue Resolution](../../internals/catalogue-resolution.md). Device-specific rule applicability is retained here through the condition table and rule IDs rather than copying hundreds of generic conversion rows verbatim.

A future machine-readable Device Library build should preserve the complete applicable rule graph, including jump targets and raw strings, from the canonical structured source.

## Diagnostic applicability

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

The exact historical electrical ratings and package contents remain revision-sensitive. The official Arnould catalogue has been identified but not yet archived in this branch, so those values are not promoted as timeless specifications and source reconciliation remains partial.

## Corroboration status and open work

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
