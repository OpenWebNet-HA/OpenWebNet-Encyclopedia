# Protocol

`WHO 0` addresses stored scenarios. In the ordinary functional form the scenario number occupies `WHAT`, while `WHERE` identifies the scenario device or scenario unit that stores or exposes the scenario.

## Scenario activation

The canonical command form is `*0*N*WHERE##`, where `N` identifies the stored scenario. The published functional range is `1`–`16`.

| Field | Meaning |
| --- | --- |
| `WHO` | `0` |
| `WHAT` | Stored scenario number `N` |
| `WHERE` | Scenario target |

This differs from most command-oriented systems because the ordinary `WHAT` is principally an indexed scenario selection rather than a small fixed verb vocabulary.

The MyHOME_Suite ScenarioDevices data uses `*0*N*WHERE##` as the functional scenario-action template, confirming that stored-scenario activation is also exposed to the application's higher-level scenario engine.

## Programming operations

The published `WHO 0` family also defines parameterized programming operations, including forms based on `WHAT 40#N`. The parameterized `WHAT` must be retained as structured protocol syntax; `40#N` is not equivalent to an ordinary activation of scenario `N`.

Programming changes the scenario definition or programming context, whereas `*0*N*WHERE##` invokes an already stored scenario. Implementations should keep these operations separate even when they address the same scenario unit.

## Relationship to `WHO 17`

[`WHO 17`](../who-17-scenario-management/) provides scenario-programmer execution and management functions such as start, stop, enable and disable, together with MyHOME_Suite scenario-state/programming operations. `WHO 0` remains the canonical namespace for direct stored-scenario activation.

## Relationship to the MyHOME_Suite scenario engine

The MyHOME_Suite scenario engine represents triggers, conditions and actions across many functional `WHO` systems. A `WHO 0` frame can be one such action, but the capability graph itself is not part of the `WHO 0` wire protocol. See [`../../scenario-engine/`](../../scenario-engine/).

A protocol implementation should therefore preserve three layers: the `WHO 0` frame, the scenario device addressed by `WHERE`, and any higher-level application rule that caused the frame to be sent.