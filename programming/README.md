# Programming

The programming protocol changes the installed configuration of a Physical Device, its Modules, and their selected Objects. It uses OpenWebNet management frames together with catalogue capability and validation data.

Programming is distinct from diagnostics. Diagnostics reports installed state; programming requests a state change. A successful protocol response does not replace validation before the write or diagnostic read-back after it.

## Reference

| Subject | Page |
| --- | --- |
| Programming roles, layers, and source boundaries | [Architecture](architecture.md) |
| Programming session states and termination | [Session Lifecycle](session-lifecycle.md) |
| Selecting a target by Device ID or address | [Device Selection](device-selection.md) |
| Selecting or replacing an Object | [Object Programming](object-programming.md) |
| Programming functional addresses | [Address Programming](address-programming.md) |
| Programming indexed configuration values | [Configuration Programming](configuration-programming.md) |
| Evaluating catalogue ranges, filters, and conditions | [Validation](validation.md) |
| Protocol errors, rejection, timeout, and recovery | [Error Handling](error-handling.md) |
| Diagnostic read-back and state comparison | [Verification](verification.md) |
| Programming `WHAT` values | [Programming `WHAT` Reference](what-reference.md) |
| Programming `DIMENSION` values | [Programming `DIMENSION` Reference](dimension-reference.md) |

## Programming flow

1. Resolve the Physical Device and firmware.
2. Resolve the target internal slot, current Object, or Virgin Object.
3. Validate the requested Object, address, and configuration values.
4. Select the installed Device through the applicable programming mechanism.
5. Apply Object, address, and configuration changes in the required order.
6. interpret acknowledgements, errors, and termination.
7. Perform a new diagnostic interview and compare the effective state.

Exact frames, direction, repetition, and state transitions will be documented from `OPEN.db`, `OpenQuery.txt`, catalogue constraints, and observed MyHOME_Suite behavior.

## Boundaries

This section defines programming protocol behavior. Reusable Device capability belongs under [Device Model](../device-model/), diagnostic read-back belongs under [Diagnostics](../diagnostics/), and end-to-end operator procedures belong under the planned practical guides.

Unknown operations or state transitions remain explicitly unresolved until supported by implementation data or observed behavior.
