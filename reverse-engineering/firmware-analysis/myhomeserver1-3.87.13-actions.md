# MyHOMEServer1 3.87.13 Compiled Scene Actions

Compiled scene actions combine raw JSON metadata, operational wait fields and action-specific callables. In [MyHOMEServer1 Firmware 3.87.13](myhomeserver1-3.87.13.md), `SLEEP` and `SCENARIO` have distinct runtime callables, while selected execution and stop methods share a wait/cancellation domain. Local completion is separate from a successful physical action.

## Source and object boundaries

The `44`-byte raw action objects differ from compiled `SleepActionRunner` (`96` bytes) and `ScenarioActionRunner` (`100` bytes). Their secondary serializers and primary runtime methods serve different roles. The compiled object's individual completion byte is read by a separate getter; a shared no-op virtual method is not that getter. [Action evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-actions/README.md) records the exact layouts, vtables and call sites.

## SLEEP: seconds, metadata and the blocking callable

The selected `SLEEP` path stores three JSON-facing fields separately:

| Field | Compiled use on the examined construction path |
| --- | --- |
| `delay` | Copied from retained metadata into the common operational-delay word |
| `duration` | Retained as metadata; the common operational-duration word remains initially zero on this path |
| `seconds` | Captured by value in the action's first callable |

The callable skips the sleep API for captured zero. Otherwise it supplies a two-word interval `[value, 0]` to `nanosleep`, using the same interval storage for the requested and remaining duration. Return `-1` with errno `4` retries; another result leaves the loop. The selected code constructs no independent Boolean sleep-success result.

The packaged libc wrapper sign-extends the first word before its time64 delegate. Under effective same-build binding and the ordinary [nanosleep API contract](https://man7.org/linux/man-pages/man2/nanosleep.2.html), the request is whole seconds with zero fractional nanoseconds. Unsigned JSON conversion, valid interval ranges, provider conversion and actual elapsed time remain separate questions. [SLEEP source evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-actions/sleep-report.txt) retains the exact captures and loop.

This blocking loop does not read the common action-stop flag. Common stop notification therefore does not establish immediate interruption of an already entered `SLEEP`; signals and full cancellation/lifetime behavior remain unresolved.

## Shared waits and completion

The common execute method clears individual completion, then selects a path from operational delay and duration:

| Operational delay | Operational duration | Selected normal path |
| --- | --- | --- |
| Zero | Zero | Invoke the first callable inline, then set completion |
| Zero | Nonzero | Invoke the first callable inline, then request a duration-wait worker |
| Nonzero | Either | Request a delay-wait worker; that worker invokes the first callable and sets completion, without locally chaining the duration phase |

Each examined wait worker multiplies its unsigned operational word by `60,000,000,000` and adds a steady-clock reading using low-`64`-bit arithmetic. The packaged clock provider's seconds-to-nanoseconds conversion supports a nominal scale of `60` seconds per operational unit under successful API binding and valid, nonoverflowing inputs. It does not assign that unit to every similarly named JSON field or prove a measured deadline.

The selected wait uses an absolute deadline and ignores the wait API's returned code. Error returns, spurious wakeups, overflow/domain admission and actual elapsed time remain unobserved. Completion follows a normally returning selected callback; it does not certify successful sleep, nested launch, delivery or physical action. [Common-action evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-actions/common-report.txt) records the exact request arithmetic and branches.

## Shared stop domain

Selected wait workers and the common stop method address the same condition variable, mutex and stop byte. A registered initializer clears that byte. The stop method ignores its incoming action receiver, locks the shared mutex, sets the shared flag, requests notification and unlocks; it does not directly set individual completion or invoke the second action-specific callable.

A selected worker can suppress its callback and completion store if the shared flag directs exit before invocation. Once a callback has entered, these common paths neither interrupt its internals nor recheck stop before their later completion store. This identifies a shared cancellation domain among the inspected methods, without establishing observed cross-scene cancellation, reset policy, race freedom or a permanently latched state. [Scene cancellation](myhomeserver1-3.87.13-cancellation.md) has its own flags.

## SCENARIO: captured ID to conditional local launch

The compiled `SCENARIO` action retains `sceneId` and the registry/context pointer supplied during initialization. [Startup](myhomeserver1-3.87.13-startup.md#the-same-objects-through-loading-and-nested-actions) connects that pointer to the container populated by the scene loader.

The selected callable tests the numeric key in the tree, obtains its two-word handle and, on the normal live-handle branch, passes the scene pointer to condition-checking launch. That launch has separate scene-enabled and scene-active gates. The call does not prove a populated target, satisfied conditions, successful thread creation or completed target actions.

This selected invocation is not classified as a target-stop operation. Expired/error handles, concurrent registry mutation and recursive-scene policy remain unresolved. [SCENARIO evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-actions/scenario-report-v2.txt) records the branches and their operand direction.

## Evidence limits

`SLEEP` metadata and its operational fields must remain separate from other derived actions: a [BN3L construction path](myhomeserver1-3.87.13-lifetime.md#bn3l-schema-and-construction) binds duration to the common duration field and installs a second callable. It does not establish a universal delay-then-duration schedule.

Configured scene files, effective providers, complete errors/unwind, shared reset ownership, concurrency and physical behavior remain unresolved. [Time predicates](myhomeserver1-3.87.13-time-scenarios.md), [cancellation](myhomeserver1-3.87.13-cancellation.md) and [ownership](myhomeserver1-3.87.13-serialization.md) describe the related contracts without assigning MH202 script semantics to this engine.
