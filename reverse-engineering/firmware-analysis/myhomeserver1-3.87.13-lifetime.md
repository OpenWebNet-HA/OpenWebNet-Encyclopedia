# MyHOMEServer1 3.87.13 Worker Lifetime and Action Construction

The scheduler owns thread-state objects, receiver objects and compiled-action handles through different mechanisms. A detached thread holder or disposed state does not by itself establish that an action/scene receiver remains alive or that its worker has completed. These findings apply to [MyHOMEServer1 Firmware 3.87.13](myhomeserver1-3.87.13.md).

## Thread state ownership and receiver lifetime differ

The examined action-wait and scene-worker states contain a raw receiver pointer. Their destructors delete the small state without locally retaining or releasing that receiver. The packaged candidate thread entry invokes the worker and then the state destructor under its normal-return contract.

A successful detach clears a separate thread-holder word and can therefore precede worker completion. The selected teardown paths differ:

| Owner path | Local request |
| --- | --- |
| Scene disposal | Join a present holder whose word is nonzero before releasing compiled-action handles |
| `SLEEP` action disposal | Delete a present holder when its word is zero; nonzero reaches termination, without a local join in that body |
| Compiled-action vector release | Decrement control counts and request disposal on the selected last-owner branch |

Other owners may remain. These source paths do not establish their actual ordering, successful provider outcomes, safe lifetime or a use-after-free/leak. [Worker ownership evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-lifetime/worker-ownership-report-v2.txt) retains the exact local methods and provider boundary.

## Shared cancellation and object-relative stores

Several stores to offset `72` belong to stack, allocation or supplied-object receivers, including inline string construction. They cannot be equated with the shared action-stop flag merely because the numeric offset matches. The examined receiver-origin analysis has not produced another positive shared reset owner; wider, indirect and reinitialization paths remain unresolved. [Receiver evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-lifetime/reset-alias-report.txt) retains that finite search.

## BN3L schema and construction

The raw action factory and the separate compiled dispatcher both select local `BN3L` index `12`. The raw object is `64` bytes; the selected compiled object is `116` bytes. Construction serializes/reparses the raw action, moves operational fields and callables and appends its handle to compiled action storage. [Serialization](myhomeserver1-3.87.13-serialization.md#the-raw-serializer-emits-a-sparse-representation) explains the selected value contract.

| Raw schema input | Selected constructor rule |
| --- | --- |
| `status` | Exact `on`, `off`, `noStatus` become local `0`, `1`, `-1` |
| `brightness`, `saturation`, `hue`, `temperature`, `speed` | Optional signed words, initially `-1` |
| Positive brightness/saturation/hue/temperature | Also set local status `0` |
| Speed | Does not perform that particular status override |
| Delay and duration | Preserved together by the common move into operational fields |

These local values are not public bus commands, validated numeric domains or physical measurements. This construction supplies a concrete duration-bearing action path, without proving configured admission, successful callable/timer execution or a universal two-phase schedule. [Schema/construction evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-lifetime/schema-activation-report.txt) records the original paths.

## Evidence limits

Compiled-action retention and selected teardown callers are described under [serialization and ownership](myhomeserver1-3.87.13-serialization.md). Natural last-owner/removal order, raw receiver survival, complete exception/unwind behavior and concurrency remain unresolved. No safe or failing interleaving, successful cancellation or physical action outcome is inferred from the presence of a destructor or a cleared holder.
