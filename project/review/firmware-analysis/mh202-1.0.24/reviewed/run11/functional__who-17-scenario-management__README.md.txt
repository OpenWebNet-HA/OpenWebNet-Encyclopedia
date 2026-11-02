# `WHO 17` - Scenario Management

`WHO 17` controls scenes managed by scenario-programmer/gateway devices. Its published functional model consists of Start, Stop, Enable and Disable operations addressed to a scene identifier, together with status requests and event reporting.

It is distinct from [`WHO 0`](../who-0-scenarios/): `WHO 0` invokes and programs scenario-module memories, whereas `WHO 17` controls the execution state of scenes managed by a scenario programmer.

## `WHAT` reference

| `WHAT` | Meaning |
| ---: | --- |
| `1` | Start scene |
| `2` | Stop scene |
| `3` | Enable scene |
| `4` | Disable scene |

These values are both command operations and reported scene states/events. Their interpretation is scoped to `WHO 17`.

## `WHERE`

| `WHERE` | Meaning |
| --- | --- |
| `0` | General |
| `1..300` | Scene number on MH200N |
| Numeric value | Scene identifier on MH202 |

The public specification intentionally gives MH202 as a numeric scene identifier rather than imposing the MH200N `1..300` range. Implementations should therefore preserve the target-device distinction instead of globally validating every `WHO 17` `WHERE` against the MH200N range.

## Start scene - `WHAT 1`

Command: `*17*1*WHERE##`.

On a command connection the gateway acknowledges an accepted operation with `ACK`. The corresponding event is `*17*1*WHERE##` on the event connection.

Start changes the execution state of the addressed scene; it is not equivalent to `WHO 0` selecting a numbered slot in an F420 scenario module.

## Stop scene - `WHAT 2`

Command: `*17*2*WHERE##`.

The event form is the same frame on an event connection. Stop terminates execution of the addressed scene without changing whether that scene is enabled for subsequent activation.

## Enable scene - `WHAT 3`

Command: `*17*3*WHERE##`.

Enable controls scene availability. It is therefore orthogonal to the Start/Stop execution pair: an enabled scene can subsequently be started, while a disabled scene is not available for normal activation.

## Disable scene - `WHAT 4`

Command: `*17*4*WHERE##`.

The corresponding event uses the same functional frame. Disable changes availability rather than merely stopping a currently executing scene.

## Status request

The published status request is `*#17*WHERE##`.

The server reports scene state using the same `WHO 17` `WHAT` vocabulary and then terminates the response with `ACK`. The specification groups the possible returned states as `WHAT 1..2` and `WHAT 3..4`, reflecting the two independent aspects of scene state:

| State axis | Returned `WHAT` |
| --- | --- |
| Execution | `1` Start / running, `2` Stop / stopped |
| Availability | `3` Enabled, `4` Disabled |

A status request can therefore produce more than one functional state frame before the final `ACK`; clients should not assume a single scalar status.

## Event connection

The event connection reports changes with the same four normal frames:

| Event | Frame |
| --- | --- |
| Scene started | `*17*1*WHERE##` |
| Scene stopped | `*17*2*WHERE##` |
| Scene enabled | `*17*3*WHERE##` |
| Scene disabled | `*17*4*WHERE##` |

Command acknowledgement and event propagation are separate. `ACK` confirms the command transaction, while the event frame represents the functional scene state/event visible to event-session clients.

## MyHOME_Suite extended scenario-programmer operations

The MyHOME_Suite `OPEN.db` definitions contain additional scenario-programmer operations beyond the four ordinary functional commands published in the `WHO 17` document. These include starting scenario programming, resetting programming, ending programming, setting/requesting scenario state through `DIMENSION 40`, reporting scenario errors through `DIMENSION 41`, and testing scenario activation.

These definitions establish that MyHOME_Suite has a richer scenario-programmer workflow than the public Start/Stop/Enable/Disable reference. They should be interpreted in their sequence/session context rather than assigned ordinary `WHAT` semantics without the corresponding frame definitions.

In particular, the implementation data distinguishes operations for:

| Operation family | Established implementation role |
| --- | --- |
| Programming start | Enter scenario-programming workflow |
| Scenario reset | Reset scenario-programming state |
| Programming end | Finish scenario programming |
| `DIMENSION 40` | Set, request and report scenario state |
| `DIMENSION 41` | Scenario error reporting |
| Test activation | Exercise scenario activation in the programming workflow |

The public `WHO 17` functional state model remains the canonical interpretation of `WHAT 1..4`; implementation-only programming operations are complementary and must not be collapsed into that four-value table.

## MH202 1.0.24 implementation evidence

The selected native `bt_taskmanager` dispatcher implements `WHAT 1..4` through launch, stop, enable and disable helpers. Separate status renderers choose execution/control `2/1` from one record field and availability `3/4` from another. Their output/callback paths remain distinct from accepted network syntax, final acknowledgement, complete event delivery and physical script execution.

The selected loader searches numbered `.spt` files `1..300` under `extra/4` and continues across failed opens. The packaged PHP configuration index also enumerates up to `300` entries but stops at the first missing name and transmits each entry's separate XML scene ID. Neither loop establishes a universal `WHO 17` `WHERE 1..300` validator for MH202. The native control field can remain nonzero during a stop request; a formatted state alone does not prove a live child process.

See [MH202 scenario ownership and limits](../../reverse-engineering/firmware-analysis/mh202-1.0.24.md#scenario-engine-and-who-17) for exact build identities, code locations and source reviews. Missing configured script bodies, trigger matching, only-if/restart/panic lifecycle, child/FIFO state and transport remain open at this checkpoint.

The later [MH202 state/control continuation](../../reverse-engineering/firmware-analysis/mh202-1.0.24-state-and-routing.md#control-state-fifo-messages-and-restoration) joins matched trigger callbacks, configured panic-frame gating, PID/control-state messages and saved-state restoration. `$RESTART=SI` gates relaunch of a saved-active record on the inspected startup pass; it is not established as automatic rerun after every normal completion. The subsequent always-start pass has separate guards. A later action-level `OWRITE` path checks a matching runtime `DISABLED` pathname and returns before its selected request write. The taskmanager/interpreter names and runtime globals still need to match, and this does not establish all-action suppression or successful script execution. The selected `OREAD` prefix has a different path. See the [action-level boundary](../../reverse-engineering/firmware-analysis/mh202-1.0.24-state-and-routing.md#action-level-disablement-and-ipc-producers).

The [later caller and storage refinement](../../reverse-engineering/firmware-analysis/mh202-1.0.24-state-and-routing.md#action-return-values-and-timing) distinguishes a stored `OWRITE` return from its ignored standalone return; neither is a delivery-success signal. The [saved-state file contract](../../reverse-engineering/firmware-analysis/mh202-1.0.24-state-and-routing.md#saved-state-file-contract) separates local marker/read/write policy from complete restart or crash-recovery behavior. A further [clock helper](../../reverse-engineering/firmware-analysis/mh202-1.0.24-state-and-routing.md#clock-comparison-is-a-numeric-result) returns a three-way numeric comparison; full configured statement/condition behavior remains open. The [query-readiness refinement](../../reverse-engineering/firmware-analysis/mh202-1.0.24-state-and-routing.md#query-readiness-and-the-mode-4-gate) also separates list completion, command gating and successful data acquisition. The [isolated ordinary-comparator corpus](../../reverse-engineering/firmware-analysis/mh202-1.0.24-state-and-routing.md#original-ordinary-comparator-evidence) adds original helper execution under explicit primitives, without proving accepted trigger scripts or physical behavior. These build-specific implementation findings do not change the public four-command vocabulary.

The later [packaged-copy helper evidence](../../reverse-engineering/firmware-analysis/mh202-1.0.24-state-and-routing.md#exact-packaged-copy-helper) narrows selected suffix-copy behavior, while retaining the original interpreter, complete grammar and configured-script boundaries. COSO feedback and pending-query state remain separate from WHO 17 scheduling.

The [later normalizer-body calls](../../reverse-engineering/firmware-analysis/mh202-1.0.24-state-and-routing.md#executed-normalizer-body-under-supplied-parser-fields) execute mutation and comparator handoffs under explicit parser primitives. A separate [calendar helper](../../reverse-engineering/firmware-analysis/mh202-1.0.24-state-and-routing.md#calendar-comparison-uses-utc-date-fields) compares UTC date components. Complete configured trigger/statement acceptance and resulting actions remain unproved.

The [numeric-record continuation](../../reverse-engineering/firmware-analysis/mh202-1.0.24-state-and-routing.md#numeric-records-conditional-text-and-later-action-prefix) connects stored helper results to an explicit IIF integer comparison and later action-prefix checks. Complete configured language and actual guarded actions remain unproved.

The [ordinary native-parser normalization](../../reverse-engineering/firmware-analysis/mh202-1.0.24-state-and-routing.md#actual-common-parser-drives-ordinary-normalization) now uses actual parser fields under explicit primitive/binding models. [Operand extraction](../../reverse-engineering/firmware-analysis/mh202-1.0.24-state-and-routing.md#ordinary-operand-extraction-before-iif) remains separate from IIF line rewriting and complete configured language.

## Relationship to scenario systems

[`WHO 0`](../who-0-scenarios/) addresses scenario modules such as F420 and their stored scenario slots. `WHO 17` addresses scenes managed by scenario-programmer/gateway devices. The MyHOME_Suite [Scenario Engine](../../scenario-engine/) is a higher-level capability model that can compose functional operations from multiple `WHO` namespaces.

See [Protocol](../../protocol/) for common command, status and event-session behavior.

The [functional overview](../) groups `WHO 0` and `WHO 17` under scenario-related functions without merging their protocol namespaces.
