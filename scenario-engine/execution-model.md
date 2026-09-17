# Execution Model

The ScenarioDevices databases define editor capabilities, not a complete runtime state machine. This page separates the execution behavior that can be derived from stored templates from behavior that requires other evidence.

## Established pipeline

For an action with a literal OpenWebNet template, a safe application can:

1. resolve the selected Object System, Device Object, Command, and Parameters;
2. confirm the Command belongs to an action category;
3. resolve the target installed Device/Module using diagnostics and the Device Model;
4. validate the target functional address under the stored or parsed `WHO`;
5. validate and encode every Parameter;
6. render and reparse the complete frame;
7. send it through the appropriate command session, authenticated where the selected gateway requires it;
8. collect acknowledgement and functional state evidence where applicable;
9. record the action result independently from the scenario's future control flow.

Steps 1–6 are partly represented by ScenarioDevices. Transport/session behavior, acknowledgements, retries, scheduling, and state persistence are not defined by these tables.

## Trigger and condition model

Event and condition Commands commonly have `Frame=NULL`. Their resource keys, category, IDs, matching IDs, address metadata, and Parameters still describe editor concepts, but the database does not directly provide a complete incoming-frame matcher.

Possible runtime inputs include:

- an event decoded elsewhere and identified by `CommandId`;
- application code mapping functional frames to Commands;
- a separate persistence or capability layer;
- matching identifiers linking incoming concepts with actions;
- non-bus events such as time, delay, or Virtual Key Card activity.

The current evidence does not select one universal mechanism.

## Matching semantics

`ObjectMatchingId` and `CommandMatchingId` demonstrably group related lighting and hotel concepts across category rows. A runtime or editor can use this relationship to find semantic counterparts, but the database does not specify whether matching is used for:

- event subscription;
- condition evaluation;
- suggested action selection;
- display grouping;
- serialization compatibility.

Document the grouping; keep the runtime purpose provisional.

## Scenario graph boundary

The four ScenarioDevices tables contain no obvious scenario-instance, node, edge, ordering, branch, schedule, or execution-history tables. Therefore they cannot, by themselves, persist a complete user-authored scenario graph.

A complete engine model still needs evidence for:

| Concern | Missing evidence |
| --- | --- |
| scenario identity | instance table or file format |
| graph structure | nodes, edges, branches, ordering |
| trigger bindings | mapping from runtime events to stored Commands |
| condition state | evaluation operands and persistence |
| action ordering | serial, parallel, delayed, or transactional behavior |
| error policy | retry, continue, abort, compensation |
| scheduling | clocks, recurrence, timezone, missed-event handling |
| runtime state | active executions and recovery after restart |

## Action execution algorithm

```text
function execute_literal_action(capability, target, inputs):
    require capability category is action
    require capability Frame is literal OpenWebNet syntax

    address = resolve target under functional WHO grammar
    parameters = validate and encode all capability Parameters
    frame = render placeholders atomically
    parsed = parse rendered frame

    require parsed WHO agrees with established capability context
    require parsed WHERE agrees with selected target
    require no placeholder remains

    send frame through the appropriate command transport
    collect ACK/NACK and applicable state feedback

    return transmitted frame, raw responses, and classified result
```

Do not generalize this action algorithm to triggers, conditions, symbolic frames, delay rows, or time-based rows.

## Result classification

| Result | Meaning |
| --- | --- |
| rendered | a complete frame was produced and validated, but not sent |
| transmitted | transport accepted the outgoing bytes; Device effect not yet proven |
| acknowledged | an applicable positive acknowledgement was received |
| rejected | `NACK` or another explicit rejection was received |
| observed effective | later functional state evidence matches the intended action |
| timeout | no terminal evidence arrived within the applicable window |
| indeterminate | transport loss or ambiguous feedback prevents a conclusion |
| unresolved capability | template, address, Parameter, or symbolic mapping was insufficient |

An acknowledgement and an observed state change answer different questions and should not be collapsed into one success flag.

## Relationship to `OPEN.db`

`OPEN.db` describes MyHOME_Suite communication scenarios for diagnostics and Device programming. It does not define the Scenario Engine graph or replace the functional meanings of ScenarioDevices action frames.

Use the common OpenWebNet session documentation for transport behavior and the functional `WHO` pages for command semantics. Do not search for ScenarioDevices row IDs in `OPEN.db` unless a separate mapping is established.
