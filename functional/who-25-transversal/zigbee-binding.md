# ZigBee Binding

The Legrand ZigBee OpenWebNet specification version 4.0 defines a ZigBee-specific binding family under `WHO 25`. These OpenWebNet operations expose the host-visible binding lifecycle while leaving the underlying ZigBee binding tables, radio association mechanisms, and other ZigBee-internal procedures outside the encyclopedia boundary.

The source is [ZigBee OpenWebNet Specification](../../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf), version 4.0 dated 22 November 2016. The semantics below are **specification evidence** for that interface revision. They do not establish support by every gateway, product, or firmware revision.

## `WHAT` reference

| `WHAT` | Source action | Direction in the detailed definition |
| ---: | --- | --- |
| `21` | Short Pressure | server to client |
| `33` | Binding Request | client to server |
| `34` | Unbinding Request | client to server |
| `35` | Open Binding | server to client |
| `36` | Close Binding | server to client |
| `37` | Cancel Binding | server to client |

These values share `WHO 25` with SCS CEN+ and dry-contact/IR functions, but their grammar and applicability are selected by the ZigBee interface context. A ZigBee binding `WHERE` must not be decoded as an SCS CEN+ virtual Object merely because the numeric `WHO` is the same.

## Addressing

Binding frames use the [ZigBee product-and-Unit `WHERE` grammar](../../protocol/zigbee-interface.md#transport-and-addressing) and family suffix `#9`.

Structurally, Binding Request and Unbinding Request use `*25*WHAT*WHERE#9##`, where `WHERE` identifies the radio product and Unit. Real installation identifiers should not be reproduced in documentation examples.

## Binding lifecycle

The published binding use case establishes this OpenWebNet-visible sequence:

1. The server reports `WHAT 35` when binding is opened for a product Unit.
2. The client sends `WHAT 33` to request binding for that same addressed Unit.
3. `ACK` means the Binding Request command has been sent; `NACK` means it has not. BUSY uses the ZigBee interface's ordinary BUSY/NACK sequence.
4. The server later reports `WHAT 36` when binding is closed.

`ACK` therefore acknowledges the Binding Request command according to the source. It should not be described as proof of the underlying ZigBee binding-table mutation independently of the later lifecycle indications.

## Unbinding lifecycle

The published unbinding use case follows the same host-visible pattern:

1. `WHAT 35` reports an opened binding procedure.
2. The client sends `WHAT 34` to request unbinding.
3. `ACK` or `NACK` reports whether the command was sent, with BUSY handled by the interface-specific BUSY/NACK sequence.
4. `WHAT 36` reports closure of the binding procedure.

The source does not expose the underlying ZigBee operation that performs the association change. That mechanism remains outside scope.

## Cancel Binding

`WHAT 37` is server-originated in the detailed definition. The source defines two forms:

- `*25*37*WHERE#9##` when two products are leaders of the source's "PnL binding" procedure;
- `*25*37*##` when a binding was opened and remained unclosed for ten minutes.

The specification uses the term "PnL" in this context. This page does not expand that acronym into an underlying ZigBee procedure beyond what the OpenWebNet frames establish.

## Events from a bound product

The specification's binding use case shows that later button activity is reported through the functional namespace appropriate to the bound product:

- a scenario product can report `WHO 25 / WHAT 21` Short Pressure;
- a Lighting product can report `WHO 1` Toggle;
- an Automation product can report its Automation movement commands.

The ZigBee specification contains a separate internal conflict over Automation UP/DOWN numeric values. The binding reference therefore does not use the binding example to resolve that conflict or redefine the canonical Automation command table.

## No `DIMENSION` family

The ZigBee specification explicitly states that this `WHO 25` variant has no `DIMENSION` table and no `DIMENSION` IDs. Binding state in this source is represented through `WHAT` traffic, not a parallel binding `DIMENSION` registry.

## Evidence limits

The exploratory ZigBee branch recorded a minimum gateway firmware version of `1.2.3` for explicit binding commands. That threshold is not stated by the inspected ZigBee OpenWebNet specification and is not promoted here without separate implementation provenance.

Likewise, the published binding lifecycle establishes OpenWebNet-visible commands, acknowledgements, and indications; it does not establish the internal ZigBee binding-table representation or radio-layer procedure.

See [ZigBee OpenWebNet Interface](../../protocol/zigbee-interface.md) for the interface-specific `WHERE` and acknowledgement model, and [`WHO 25` - Transversal Functions](README.md) for the other protocol families sharing this namespace.
