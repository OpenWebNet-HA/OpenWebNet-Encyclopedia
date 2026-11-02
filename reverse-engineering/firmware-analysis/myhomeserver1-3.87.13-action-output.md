# MyHOMEServer1 3.87.13 Action Request Handoff

Selected `BN3L` action callables construct local objects with `jsonrpc`, `method`, `id` and `params`, then pass them to the same scheduler request helper. This connects the [compiled action](myhomeserver1-3.87.13-actions.md) to a concrete software interface in [MyHOMEServer1 Firmware 3.87.13](myhomeserver1-3.87.13.md), without establishing a complete payload, natural callback order, delivery or physical effects.

## Compiled action and callable captures

The raw `BN3L` action (`64` bytes), compiled `Bn3lActionRunner` (`116` bytes) and heap captures have different roles. Each callable adapter reads the first word of its callable storage to obtain its capture receiver; that receiver is not the compiled action itself.

| Callable | Selected captured storage |
| --- | --- |
| First | `52` bytes: copied configured ID, selected compiled value payload and operational duration |
| Conditional second | `24` bytes: its own copied configured ID, without the first capture's six-word payload |

Construction and copy-manager paths request separate capture allocations and string copies. Capture duration at offset `48` is not the compiled object's thread holder at offset `48`. Normal allocation/copy returns, valid unchanged receivers and capture lifetime remain premises. [Capture evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-action-output/README.md) retains the exact adapter, constructor and field correspondence.

## Local request interface

On the first body's selected prefix, nonzero captured duration permits a query using the configured target ID; zero bypasses that prefix. Query success, suitable record type, matching/fresh state and any snapshot interpretation remain separate premises.

Both callable bodies request the local descriptor constructor. Its [request values](myhomeserver1-3.87.13-action-request-values.md) identify version `2.0`, method `light.setStatus` and an outer correlation-ID producer. Each selected body builds a parameter object through its own conversion source.

| Local member | Source role |
| --- | --- |
| `jsonrpc` | Descriptor version string |
| `method` | Descriptor method string |
| `id` | Descriptor's outer request-ID string |
| `params` | Value returned by the parameter converter using that body's supplied record |

The first and second call sites use their own object, method-string and conversion storage, but source relocations resolve the same request-helper receiver. This proves common local source addressing; it does not establish an initialized runtime object, remote endpoint, equal parameter values, a causal request pair or rollback.

The helper call is the examined output boundary. Destruction of temporary JSON storage is requested after normal return, and the first body continues beyond that point. Neither call is a complete callback-return proof or a send/delivery acknowledgment. Underlying receiving and transport behavior is not inferred from the local key names.

## Evidence limits

[Source evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-action-output/README.md) preserves the exact captures, copies, local receiver and calls. The [value producers](myhomeserver1-3.87.13-action-request-values.md) and [retained-state consumer](myhomeserver1-3.87.13-action-retained-state.md) describe selected parameters rather than a complete generator.

Branch admission, effective binding, provider returns, valid object/type/ID/freshness, allocation/unwind and concurrent lifetime remain unresolved. No natural paired invocation, successful prior-state restoration, public OpenWebNet mapping or physical operation follows from the private method/class names.
