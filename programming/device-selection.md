# Device Selection

Programming begins by selecting one installed Physical Device within a management `WHO`. The canonical scenarios support selection by diagnostic address, by 32-bit Device ID, or through a local-interaction workflow.

## Selection frames

| Method | Frame | First-response window |
| --- | --- | ---: |
| Address | `*[WHO]*1*[WHERE]##` | 15 s |
| Device ID | `*[WHO]*9#[ID]*0##` | 15 s |
| Local-interaction scenario | `*[WHO]*1*[WHERE]##` | 300 s |

The Device ID has the `OPEN.db` range `0`–`4294967295`. Observed interfaces render it as eight hexadecimal characters; the wire template carries the `ID` field without defining that display representation.

## Selecting by Device ID

Use the installed instance identifier returned by diagnostic `DIMENSION 13`. Do not substitute:

- `EN_DEVICE.id_device`;
- `EN_ITEM.id_item`;
- `OBJECT_MODEL`;
- a Module address;
- a catalogue SKU.

The ID-based scenario proceeds to advanced Object configuration. It does not include the virtual-configurator sequence.

## Selecting by address

`WHERE` follows the selected management family's address grammar. It is not one universal integer and must be generated from the applicable `OPEN.db` address rule.

A Physical Device can expose several Modules and functional addresses. The diagnostic/programming selection address must therefore remain distinct from per-Module addresses written through `DIMENSION 32`. Observed `WHO 1001` traffic often correlates the Device context with internal slot `1`, but this is not a universal rule.

The address-selected programming scenario proceeds to virtual-configurator transfer and does not include `ConfKO`.

## Local-interaction selection

The `ConfLocalButton` sequence uses the same start frame and response order as `ConfAddressed` but assigns a 300-second first-response window. Its scenario then permits advanced Object configuration followed by virtual-configurator transfer.

The database name establishes a local-button workflow; the frame does not encode the physical interaction. An implementation must coordinate the installer action outside the OpenWebNet payload and must not infer which Device was selected solely from the long timeout.

## Initial identity checks

Before transmitting configuration, compare the returned initial projection with the intended target:

- `DIMENSION 1` item/model, physical configurator count, brand, and line;
- `DIMENSION 2` firmware version;
- `DIMENSION 13` Device ID;
- `DIMENSION 30` configured Object or Virgin Object by internal slot;
- `DIMENSION 32` current Module addresses where reported.

Resolve the Device through the documented catalogue path and retain ambiguity where several SKUs share an item.

## Failure handling

A `NACK` on the mandatory start frame transitions the canonical state to Undefined. No first response before the applicable timer also leaves target selection unestablished. Do not send transfer frames after ambiguous selection.

`WHAT 3` indicates Device abort during the entry sequence. Preserve any partial identity records but mark the programming session aborted.

See [Device Discovery](../diagnostics/device-discovery.md), [Address Discovery](../diagnostics/address-discovery.md), and [Device Identity](../diagnostics/dim1-device-identity.md) for the read-only discovery procedures.
