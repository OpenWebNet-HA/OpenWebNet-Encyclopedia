# Server Scene Processing

MyHOMEServer1 Firmware `3.87.13` and F460 Firmware `2.0.12` contain server-side scene processors with JSON-facing records, compiled runners, triggers, conditions and actions. These are source-specific implementations of scene processing; they are separate from the ScenarioSuite/MH202 script compiler and the public [WHO 17 scene-control vocabulary](../functional/who-17-scenario-management/).

## Processing model

| Layer | Role in the inspected source | Boundary |
| --- | --- | --- |
| Scene input | A selected file/source argument enters a loader or constructor path | Packaged settings and a directory name are not a commissioned scene |
| Raw records | Trigger, condition and action classes retain configuration fields | Class names and local type numbers are not catalogue Object or WHO identities |
| Serialization and compilation | Selected raw objects return JSON that is reparsed to construct compiled runners | This is an inspected local call relationship, not a universal lossless JSON round trip |
| Launch admission | Time/local-event callbacks and local state can request scene work | Callback eligibility is separate from natural event delivery and owning lifetime |
| Conditions | Compiled predicates gate entry to the action path | A private return value needs its actual caller's interpretation |
| Actions and cleanup | Local callables, completion markers and scene-control state govern progression | Normal return, marker changes and scene cleanup do not establish delivered actions or physical completion |

The same layer names do not establish identical layouts or policy across products. MyHOMEServer1's ARM32 objects and F460's AArch64 objects require their own source-derived fields, pointer representations and callers.

## Loader and configured-input evidence

| Build | Established source relationship | Unresolved input boundary |
| --- | --- | --- |
| MyHOMEServer1 `3.87.13` | Startup connects a scene container, time-trigger service and configured directory. The selected loader requests JSON parsing, constructs raw records and initializes runners | No genuine populated scene was admitted from the selected retained directory; actual Configuration and successful provider operations remain unobserved |
| F460 `2.0.12` | Selected filesystem gates and a supplied source argument reach a file-open request and JSON-reader setup | The inspected file-input prefix ends before the parse call/result; complete file-to-scene publication is unproved |
| F461 `2.0.11` | Separate configuration and integration-module paths are documented | Shared F46 data/class names do not establish the F460 scene consumer or active feature set in F461 |

See [MyHOMEServer1 scene loading](../reverse-engineering/firmware-analysis/myhomeserver1-3.87.13-startup.md), the [F460 input boundary](../reverse-engineering/firmware-analysis/myhomeserver1-f460-f461-input-admission.md), and [F46 implementation roles](../reverse-engineering/firmware-analysis/f460-f461-knowledge-handoff.md). A complete accepted-input schema or deployable scene generator cannot be inferred from these selected contracts.

## Triggers, conditions and action records

The inspected MyHOMEServer1 paths distinguish time triggers, local state/numeric triggers and compiled condition predicates. For example, the BNLD numeric trigger and BNLD condition use different classes and callers. BNTH consumes a selected typed cached value; its representation does not establish a physical unit or measurement freshness. BNCUSCENE's selected predicate inverts an enabled byte under the ordinary Boolean-value premise; the caller's condition gate gives that result its operational role.

F460 has its own BNIL, BNLD and BNCUSCENE construction, serialization and predicate paths. Operator strings, operand order and local field types must be taken from that build. Neither a repeated name nor equal offset supplies a cross-build schema or public command-support matrix. The [MyHOMEServer1 event/condition reference](../reverse-engineering/firmware-analysis/myhomeserver1-3.87.13-event-routing.md) and [F460 predicates](../reverse-engineering/firmware-analysis/f460-f461-deep-analysis.md) provide the separate contracts.

For selected MyHOMEServer1 actions, the compiled callable passes configured target/body values to a local request interface. Request-envelope IDs and target identities have distinct producers. A request-construction or publication call does not establish accepted OpenWebNet syntax, matching response correlation or bus delivery. See [action request handoff](../reverse-engineering/firmware-analysis/myhomeserver1-3.87.13-action-output.md).

## Completion, cancellation and lifetime

Scene state, action completion and shared cancellation are separate mechanisms. MyHOMEServer1 source distinguishes cleanup of scene activity from resetting action/shared-control state. A detached worker request, cleared holder or destruction request is not proof that callbacks have quiesced.

F460's selected SLEEP path can set its marker after a normal callback return following a non-retry wait error. A separate scene-control flag can also take polling to cleanup without a fresh true action marker. Thus neither the marker nor cleanup certifies elapsed waiting or completion of every configured action. A positive flag writer exists, but its receiver class and natural caller remain unresolved; equal offsets alone do not close that join.

These distinctions matter when interpreting local completion or designing a future source-backed model. They do not establish a product-wide cancellation policy, concurrency safety, measured timing or physical scene outcome. [MyHOMEServer1 cancellation](../reverse-engineering/firmware-analysis/myhomeserver1-3.87.13-cancellation.md) and [F460 execution state](../reverse-engineering/firmware-analysis/f460-f461-knowledge-handoff.md) retain the build-specific evidence.

## Evidence limits

The model summarizes reviewed source paths, with one separately scoped MyHOMEServer1 JSON-provider experiment. That scalar experiment does not execute a whole scene or certify complete serialization/reparse. Actual configured files, natural caller/owner correlation, effective providers, full parser policy, errors/unwind, concurrency, delivered commands and Physical Device behavior remain unresolved where stated above. Evidence and source histories remain linked from the build-specific references.
