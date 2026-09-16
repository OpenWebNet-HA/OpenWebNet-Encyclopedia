# Protocol

`WHO 17` provides scenario-programmer and scenario-management operations. It is distinct from [`WHO 0`](../who-0-scenarios/), which invokes stored scenarios.

## Execution-state commands

| `WHAT` | Meaning |
| ---: | --- |
| `1` | Start |
| `2` | Stop |
| `3` | Enable |
| `4` | Disable |

The MyHOME Suite implementation also contains operations for starting scenario programming, resetting scenario programming, ending programming, setting and requesting scenario state through `DIMENSION 40`, reporting scenario errors through `DIMENSION 41`, and testing scenario activation.

These programming/state-management operations should be interpreted in their session context; they are not interchangeable with ordinary `WHO 0` scenario activation frames.