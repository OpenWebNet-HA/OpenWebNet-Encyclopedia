# `DIMENSION 32`: Module Addressing

`DIMENSION 32` reports the configured system and address associated with one internal slot.

## Frame

`*#[WHO]*[WHERE]*32#[SLOT]*[SYS]*[ADDR]##`

| Field | Range in `OPEN.db` | Meaning |
| --- | ---: | --- |
| `SLOT` | `1`–`255` | Device-local internal slot |
| `SYS` | `1`–`255` | system selector |
| `ADDR` | `0`–`65535` | encoded address value |

`32#[SLOT]` is a parameterized `DIMENSION` selector: `#` attaches `SLOT` to `DIMENSION 32`. `SYS` and `ADDR` are the ordinary response values and are separated with `*`.

## Interpretation boundary

`SYS` and `ADDR` are not a complete address description in isolation. Resolve them with:

- the diagnostic family;
- the Object reported for the same internal slot by `DIMENSION 30`;
- the functional system’s addressing rules;
- catalogue configuration metadata where corroborated.

The range `0`–`65535` is storage capacity, not a universal set of valid functional addresses.

`SYS` is described only as “KeyObject system” by `OPEN.db`. It must not be equated automatically with a functional `WHO`, a diagnostic `WHO`, `OPEN.db.EN_SYSTEM.id_system`, or `MHCatalogue.db.EN_SYSTEM.id_system`. A numeric mapping requires Object/system and capture corroboration.

## Device address versus Module address

The outer `WHERE` is the diagnostic response context. `ADDR` is the configured address of the Module identified by `SLOT`. They can coincide, but they are not defined as the same field.

In observed `WHO 1001` Device interviews, the ordinary diagnostic `WHERE` often matched the `A`/`PL` address of internal slot `1`. Other Modules on the same Physical Device reported different addresses. This correlation remains capture-derived and must not be used as a universal Device-address rule.

## Lighting and Automation

For Lighting/Automation Objects, an encoded value can be rendered as `A`/`PL` only after applying the relevant address rule. Documentation should record both the raw `ADDR` and the decoded components.

An observed Device layout included:

| Internal slot | Object | `A` | `PL` | Rendered `WHERE` |
| ---: | ---: | ---: | ---: | ---: |
| `1` | `6` | `1` | `0` | `10` |
| `2` | `6` | `1` | `6` | `16` |
| `3` | `400` | `1` | `0` | `10` |

The repeated `10` demonstrates that different Modules can share an address while exposing different Objects.

## Physical address counterparts

After applying the Object and system-specific address rule, decoded `ADDR` components can be compared with the firmware's physical configurator positions. For Lighting/Automation Devices, `A` and `PL` commonly appear both as physical positions in the firmware definition and as the effective address components reported through `DIMENSION 32`.

This establishes that the address property has a physical-configurator counterpart; it does not establish that physical configurators supplied the reported value. An `A` or `PL` value within the physical range can also have been assigned by advanced or virtual configuration. A value outside the established physical range can exclude physical configuration for that address component.

Other physical positions such as `M`, `TYPE`, `PRE`, or `G1` are not encoded as address components merely because they occur beside `A` and `PL` on the Device. Indexed counterparts belong to `DIMENSION 35` where the Object and firmware define them.

See [Physical-configurator counterparts](../device-model/configuration.md#physical-configurator-counterparts) for the shared resolution and evidence rules.

Observed sensor Device `08CF44BF` used diagnostic `WHERE 0015`, interpreted as `A = 0`, `PL = 15`. Retaining the raw field is important because padding and family-specific formatting can be lost by integer-only storage.

## Other systems

Temperature Control zones, CEN/CEN+ identifiers, Energy Management targets, and Access Control addresses use different grammars. For example, CEN virtual identifiers occupy `0`–`2047`; that domain must not be decoded as `A`/`PL`.

Keep the raw tuple `(SYS, ADDR)` whenever the system-specific decoder is unavailable.

The address-rule inventory used by MyHOME_Suite is documented in [Address Discovery](address-discovery.md). It includes zone, actuator, interface, Energy Management, and Access Control forms that cannot be decoded as `A`/`PL`.

## Missing records

Not every Module necessarily produces `DIMENSION 32`. A missing address can indicate an unconfigured Module, an Object without an address, unsupported reporting, or an incomplete interview. One observed light-control-only Device returned Module data without an observed `DIMENSION 32`; that single capture does not establish the reason.

The working capture model is therefore narrower than “all Modules have `DIMENSION 32`”: addressed actuator/sensor Modules have produced it, while at least one command-only layout did not. Treat availability as Object- and firmware-dependent until broader evidence is available.

## Address errors

`DIMENSION 34` reports an address error for one internal slot:

`*#[WHO]*[WHERE]*34*[SLOT]*[ERROR]##`

`ERROR` is boolean in `OPEN.db`. The database does not enumerate finer error causes, so retain the raw flag and surrounding Module/Object context.
