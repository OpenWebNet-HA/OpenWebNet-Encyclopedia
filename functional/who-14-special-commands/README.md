# Overview

The MyHOME_Suite `ScenarioDevices.sqlite` capability data identifies `WHO 14` as Special Commands and defines `WHO 14` command templates. The canonical public PDF corpus does not contain a dedicated `WHO 14` document.

## Known commands

| Frame template | Meaning |
| --- | --- |
| `*14*0*WHERE##` | Special-command operation with `WHAT 0` |
| `*14*1*WHERE##` | Special-command operation with `WHAT 1` |

The current corpus establishes these command forms but does not justify assigning more specific semantics to `WHAT 0` and `WHAT 1` without the associated command/Object context. They therefore remain identified by their protocol values rather than inferred labels.