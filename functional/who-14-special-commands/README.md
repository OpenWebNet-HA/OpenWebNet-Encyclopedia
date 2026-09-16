# Overview

The MyHOME_Suite ScenarioDevices capability data identifies `WHO 14` as Special Commands. Unlike the major public functional systems, the canonical PDF corpus does not contain a dedicated `WHO 14` specification, so the implementation data is the principal established source for this namespace.

## Established command templates

| Frame template | Established meaning |
| --- | --- |
| `*14*0*WHERE##` | Special-command operation with `WHAT 0` |
| `*14*1*WHERE##` | Special-command operation with `WHAT 1` |

ScenarioDevices exposes these frames as functional capabilities that can participate in higher-level scenario actions. This establishes the wire templates and namespace but does not, by itself, establish universal human-readable semantics for `WHAT 0` and `WHAT 1` independent of their Object/command context.

## Interpretation rule

A decoder should preserve `WHO 14`, `WHAT`, and `WHERE` exactly and resolve any higher-level label from the associated MyHOME_Suite command/Object capability when available. It should not rename `WHAT 0` and `1` by analogy with Lighting, Auxiliaries, or another binary namespace.

## Scenario-engine relationship

The presence of `WHO 14` templates in ScenarioDevices means they are available to the MyHOME_Suite scenario capability model; it does not make `WHO 14` itself a scenario protocol. Stored scenarios remain under [`WHO 0`](../who-0-scenarios/) and scenario-programmer management under [`WHO 17`](../who-17-scenario-management/).

See [`../../scenario-engine/`](../../scenario-engine/) for the higher-level trigger/condition/action model.