# Open Questions

This page records Scenario Engine semantics that are not yet established strongly enough for normative documentation.

## Database selection

- Which application workflow opens `ScenarioDevices-program-files.sqlite`?
- Which workflow opens `ScenarioDevices-programdata.sqlite`?
- Are they product variants, generated and packaged revisions, or inputs to different MyHOME_Suite components?
- When both are available, which file takes precedence?

## Category and family fields

- Confirm the application's own labels for `CategoryFlag 0` and `1`; the data establishes primary/start and complementary/stop event categories, but not one universal public name.
- The local editor-family grouping of `FamilyId` is established in [Database Model](database-model.md). Determine whether application code defines any additional cross-source mapping; equal values alone do not establish one.
- Confirm the runtime/editor purpose of the established primary/complementary category pairs that share a resource key.

## Matching identifiers

- Establish the purpose of `ObjectMatchingId` and `CommandMatchingId`.
- Determine how the application uses the established cross-role matching groups at runtime or in the editor: event binding, suggested actions, display grouping, serialization, or another purpose.
- Test whether matching identifiers are local to one file or stable across both revisions.

## Object identifiers

- Determine whether `DeviceObjects.ObjectId` maps to ScenarioDevices-only concepts, catalogue Objects, public protocol constructs, or a mixture.
- Do not infer equality with `EN_KEY_OBJECT.key_object` from numeric coincidence.
- Identify which installed Device/Object evidence MyHOME_Suite uses to filter the scenario editor's Object list.

## Command identifiers

- Determine the namespace and stability of `Commands.CommandId`.
- Establish whether equal `CommandId` values under different Objects mean semantic equivalence.
- Correlate commands with the functional `WHAT` or `DIMENSION` reference only where the stored frame or independent source supports it.

## Address metadata

- Enumerate `WhereType` semantics.
- Establish how `WherePlaceholder` and `WhereName` interact with system-specific address editors.
- Determine how virtual, group, general, and multi-level addresses are represented.

## Parameter metadata

- Enumerate parameter `Type` values.
- Enumerate `OperatorType` values and their relationship to triggers and conditions.
- Determine when `Value` is a default, fixed selector, comparison operator operand, or enumeration key.
- Document composite placeholders whose grammar cannot be expressed by `Min`, `Max`, and `Step` alone.

## Symbolic and missing frames

- Locate the application mapping for symbolic values such as `ResetSOS[WHERE]`.
- Determine why some trigger/condition rows have no stored frame.
- Establish whether missing frames are matched against incoming events by IDs, by another database, or by application code.

## Execution model

The databases describe capabilities but do not obviously store complete user-authored scenario graphs. Further work should identify:

- where scenario instances are persisted;
- how triggers, conditions, and actions are ordered;
- how delays, timers, and branching are represented;
- how incoming frames are matched to triggers;
- how actions are scheduled and errors handled;
- whether the engine retries, serializes, or parallelizes actions.

## Investigation method

For each hypothesis:

1. query both ScenarioDevices revisions;
2. preserve file and row provenance;
3. compare resource keys, parents, frames, and parameters;
4. correlate with the functional protocol reference;
5. inspect other preserved MyHOME_Suite support files where available;
6. compare with observed UI behavior or execution;
7. record counterexamples;
8. promote the interpretation only when it explains all relevant rows.

Implementation labels are evidence, not automatically public protocol terminology.
