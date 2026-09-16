# Protocol

`WHO 0` addresses stored scenarios. The ordinary functional frame uses the scenario number as `WHAT` and the scenario device or scenario unit as `WHERE`.

## Scenario activation

The canonical command form is `*0*N*WHERE##`, where `N` identifies the stored scenario. The published functional range is scenarios `1` through `16`.

| Field | Meaning |
| --- | --- |
| `WHO` | `0` |
| `WHAT` | Scenario number `N` |
| `WHERE` | Scenario target |

Scenario programming operations published for this family include parameterized `WHAT` forms such as `40#N`. These operations are distinct from the scenario execution-state functions carried by [`WHO 17`](../who-17-scenario-management/).

## MyHOME Suite scenario engine

The MyHOME Suite scenario engine uses `WHO 0` commands as one class of functional action, but the higher-level trigger/condition/action capability model is not itself the `WHO 0` wire protocol. That model is documented separately under [`../../scenario-engine/`](../../scenario-engine/).