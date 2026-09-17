# Address Programming

Address programming assigns the effective functional system and address of one configured Module during advanced Object transfer.

## Write frame

`*#[WHO]*0*#32#[SLOT]*[SYS]*[ADDR]##`

`#32#[SLOT]` is the parameterized `DIMENSION` selector. The leading `#` selects the write form, and the following `#` attaches `SLOT` to that selector. `SYS` and `ADDR` are ordinary `DIMENSION` values separated with `*`.

| Field | `OPEN.db` range | Meaning |
| --- | ---: | --- |
| `SLOT` | `1`–`255` | Device-local internal slot |
| `SYS` | `1`–`255` | Object system selector |
| `ADDR` | `0`–`65535` | encoded address |

These ranges are transport capacity, not universal validity.

## Resolution procedure

1. Resolve the Device, firmware, internal slot, and target Object.
2. Determine the functional system supported by that Object.
3. Select the applicable `OPEN.db` address rule for the management family and Object/device family.
4. Validate component values, fixed prefixes, padding, advanced offsets, level rules, and validity conditions.
5. Encode the complete `ADDR` without discarding significant zero padding.
6. Preserve `SYS` as a separate field.
7. Send the address only after the corresponding Object write.
8. Verify the effective tuple through diagnostic `DIMENSION 32`.

`SYS` is labelled “KeyObject system” by `OPEN.db`. It is not automatically a functional `WHO`, diagnostic `WHO`, or internal `EN_SYSTEM.id_system`. A numeric mapping requires Object/system and capture corroboration.

## Address families

Programming reuses system-specific grammars rather than one generic `A`/`PL` form. The canonical implementation includes, among others:

- Lighting/Automation point-to-point and interface forms;
- Temperature Control zone, actuator, slave-probe, and external-probe forms;
- Video Door Entry interface forms;
- Energy Management control-unit and actuator forms;
- Access Control command and indicator forms.

The complete implementation inventory is maintained in [Address Discovery](../diagnostics/address-discovery.md).

## Physical counterparts

For Lighting/Automation, decoded `A` and `PL` can correspond to physical configurator positions declared by the firmware. That correspondence establishes physical capability, not the active programming method.

A value outside the established physical range can exclude physical configuration. A value within it remains ambiguous because advanced or virtual programming can produce the same effective address.

See [Physical-configurator counterparts](../device-model/configuration.md#physical-configurator-counterparts).

## Address error

The Device can report:

`*#[WHO]*[WHERE]*34*[SLOT]*[ERROR]##`

`ERROR` is boolean. `OPEN.db` supplies no more detailed reason. Preserve the attempted Object, `SYS`, raw `ADDR`, internal slot, and applicable address rule when reporting the failure.

The address write is optional and repeatable within `ConfKO`. Omission can be valid for an Object without an address; it must not be used to infer that every unaddressed Module is erroneous.
