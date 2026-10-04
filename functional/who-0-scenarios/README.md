# `WHO 0` - Scenarios

`WHO 0` addresses stored scenarios implemented by scenario modules such as F420 and by the 3456 IR interface. The ordinary functional frame uses the selected scenario number as `WHAT` and the scenario module as `WHERE`. The published protocol also defines an F420-only programming vocabulary for recording, erasing and locking scenario storage.

## `WHAT` reference

| `WHAT` | Meaning | Availability |
| --- | --- | --- |
| `1..16` | Activate stored scenario `1..16` | F420 and 3456 |
| `17..20` | Activate stored scenario `17..20` | 3456 |
| `40#X` | Start recording scenario `X` | F420 only; `X=1..16` |
| `41#X` | End recording scenario `X` | F420 only; `X=1..16` |
| `42` | Erase all scenarios | F420 only |
| `42#X` | Erase scenario `X` | F420 only; `X=1..16` |
| `43` | Lock scenario central unit | F420 only |
| `44` | Unlock scenario central unit | F420 only |
| `45` | Scenario central unit unavailable | State/event indication |
| `46` | Scenario central-unit memory full | State/event indication |

The published specification states that F420 stores up to 16 scenarios, while the 3456 IR interface can recall up to 20. The higher scenario numbers therefore must not be assumed valid for F420 merely because they are valid `WHO 0` values.

## Scenario activation

The activation frame is `*0*N*WHERE##`, where `N` is the stored scenario number supported by the addressed device.

A command connection returns `ACK` when the command has been sent to the bus and `NACK` when it has not. The corresponding functional event is reported with the same `*0*N*WHERE##` form.

The MyHOME_Suite ScenarioDevices capability model also exposes `*0*N*WHERE##` as a scenario action. This confirms that the higher-level scenario engine invokes the same functional `WHO 0` operation; the trigger/condition/action model itself is not part of the `WHO 0` wire grammar.

## `WHERE`

The published point-to-point range is scenario control panels/modules `01..99`.

| Form | Meaning |
| --- | --- |
| `01..99` | Scenario module point to point |
| `01..99#4#I` | Scenario module on local bus through interface `I` |

The local-bus form uses the level-4 interface parameter. It is part of the address and must be preserved when routing the command; it is not a parameter of the selected scenario.

## F420 programming connection

The F420 recording/erase/lock operations use the commands/actions connection selected by `*99*9##` before the `WHO 0` programming frames are exchanged. These operations alter scenario storage and must be distinguished from scenario activation. The introduction separately defines `*99*0##` for programmed-scenario traffic; it is not the selector printed in these `WHO 0` command flows.

The 3456 IR interface does not support the F420 programming operations described below.

## Start recording - `WHAT 40#X`

`*0*40#X*WHERE##` starts recording scenario `X`, with `X=1..16` for F420. A successful command connection returns `ACK`; failure returns `NACK`. The operation is also visible on an event connection as a `WHO 0` programming event.

After recording starts, the functional commands to be stored in the scenario are issued through their respective `WHO` namespaces. `WHO 0` identifies the recording lifecycle; it does not encapsulate the recorded Lighting, Automation, or other functional frames.

## End recording - `WHAT 41#X`

`*0*41#X*WHERE##` ends recording of scenario `X`. The selected scenario number and scenario-module `WHERE` must correspond to the recording session being closed.

The published document contains a typographical irregularity in one event-frame rendering around this operation. The semantic operation remains `WHAT 41#X`: end programming/recording of the selected scenario.

## Erase operations - `WHAT 42`

`*0*42*WHERE##` erases all stored scenarios from the addressed F420.

`*0*42#X*WHERE##` erases only scenario `X`, with `X=1..16`.

The parameterized and unparameterized forms are distinct operations. Implementations should therefore parse `WHAT` together with its `#` parameter rather than normalize both to a bare numeric `42`.

## Lock and unlock - `WHAT 43` / `44`

`*0*43*WHERE##` locks the addressed scenario central unit; `*0*44*WHERE##` unlocks it. These are F420 management operations and use the same scenario-module `WHERE` grammar as recording and erasure.

The `WHAT` table also defines `45` for an unavailable scenario central unit and `46` for scenario-memory-full indication. They describe central-unit state rather than a stored scenario number.

## Event model

An event connection can report scenario activation and the F420 programming lifecycle. Published event forms include activation, start recording, end recording, erase-all and erase-single-scenario events.

A receiver should therefore distinguish three categories inside `WHO 0`:

| Category | `WHAT` |
| --- | --- |
| Stored-scenario invocation | `1..20` according to device capability |
| Scenario-storage programming | `40#X`, `41#X`, `42`, `42#X`, `43`, `44` |
| Scenario-module state | `45`, `46` |

## Relationship to `WHO 17`

`WHO 0` operates scenario modules and stored scenario memories. [`WHO 17`](../who-17-scenario-management/) addresses scenario execution on scenario-programmer/gateway devices using Start, Stop, Enable and Disable operations. The two namespaces are related functionally but have different `WHAT` and `WHERE` models and must not be merged.

## Historical touchscreen behavior

The BTicino client at `TS10_1_0_23` also accepts unparameterized `*0*40*WHERE##` and `*0*41*WHERE##` as programming-state indications without a selected scenario. Only the unparameterized start indication bypasses the client's module-address check, allowing another module's programming event to affect its cached state. This is client behavior, not proof that every physical module starts recording together.

Other programming and lock indications require an exact match of the complete configured `WHERE`, including any interface suffix. The library keeps programming status separate from its unlock cache: a start indication sets that cache without emitting an unlock value, so a following `44` can be suppressed. Repeated `43` still produces a lock value; an end indication does not update the unlock cache.

The touchscreen's configured scenario entries apply a further local state model:

| Received indication | Entry state before | Entry state after |
| --- | --- | --- |
| Start recording this scenario | Unlocked | Editing |
| Start recording another scenario, or no selected scenario | Unlocked | Locked |
| Start recording | Locked or Editing | Unchanged |
| End recording, including another scenario | Any | Unlocked |
| Lock / unlock | Any | Locked / Unlocked |

These are client transitions, not guarantees about F420 recording or storage. Activation, erase, unavailable and memory-full indications are not forwarded by this library decoder. See [Programming-state evidence](../../project/review/myopencommunity-scenario-history-review.md#programming-state-and-address-matching).

Its basic IR air-conditioning control sends configured actions through `WHO 0`; its advanced split control instead uses [`WHO 4`, `DIMENSION 22`](../who-4-temperature-control/dimensions.md#dimension-22---split-control). The UI category does not determine the wire namespace or a universal OFF command. The scenario library's `1..31` API assertions likewise do not extend the published F420 or 3456 capacities. See [historical client evidence](../../project/review/myopencommunity-coverage-audit.md#scenario-and-basic-ir-controls).

See the [functional overview](../) for navigation by `WHO` and by function, [Scenario Engine](../../scenario-engine/) for the MyHOME_Suite trigger/condition/action capability model, and [Protocol](../../protocol/) for common frame/session syntax.
