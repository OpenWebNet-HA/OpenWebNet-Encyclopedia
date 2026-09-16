# Protocol

`WHO 17` provides scenario-programmer execution and scenario-management operations. It is distinct from [`WHO 0`](../who-0-scenarios/), whose principal role is invocation of stored scenario numbers.

## Execution-state commands

| `WHAT` | Meaning |
| ---: | --- |
| `1` | Start |
| `2` | Stop |
| `3` | Enable |
| `4` | Disable |

The ordinary execution form is `*17*WHAT*WHERE##`, where `WHERE` identifies the scenario/programmer target defined by the `WHO 17` addressing model. For example, a start operation uses `WHAT 1`; the numeric target remains a `WHO 17` `WHERE`, not a `WHO 0` scenario field.

## Execution versus programming

Starting or stopping a scenario is distinct from modifying its programmed content or state. A client should therefore separate the four execution-state commands from the programming workflow described below.

## MyHOME_Suite programming operations

The MyHOME_Suite `OPEN.db` protocol definitions extend the functional model with explicit scenario-programming operations. The defined workflow includes:

| Operation | Role |
| --- | --- |
| Start scenario programming | Opens programming for the selected scenario target |
| Reset scenario programming | Clears/resets the scenario programming context |
| End scenario programming | Closes the programming operation |
| `DIMENSION 40` | Set/request/report scenario state |
| `DIMENSION 41` | Scenario error information |
| Test scenario activation | Executes/tests the scenario in the programming context |

These operations are implemented as protocol sequences rather than as aliases for `WHAT 1`–`4`. Session state and direction are therefore significant.

## `DIMENSION 40` — scenario state

MyHOME_Suite defines operations to set scenario state and to request/report the same state through `DIMENSION 40`. Implementations should distinguish the write, request, and response frame classes even though they share the identifier.

## `DIMENSION 41` — scenario error

`DIMENSION 41` reports scenario-programming error information. Error values belong to the scenario-management workflow and should not be treated as general OpenWebNet `NACK` codes.

## Relationship to `WHO 0`

`WHO 0` and `WHO 17` can both result in scenario execution, but they expose different protocol abstractions. `WHO 0` addresses the scenario function directly; `WHO 17` exposes scenario-programmer execution and management. Applications should preserve the originating namespace instead of normalizing both to one synthetic command family.

See [`../../programming/`](../../programming/) for configuration/programming concepts that span protocol systems.