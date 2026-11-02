# `WHO 14` - Special Commands

`WHO 14` is the OpenWebNet Special Commands namespace. The canonical public PDF corpus does not contain a dedicated `WHO 14` specification, but the MyHOME_Suite ScenarioDevices capability databases provide direct implementation evidence for the operations they expose.

## Actuator lock / unlock

ScenarioDevices defines an Object named `miniScenarioSuite.specialCommands.actionLockUnlockActuator.descr` with two scenario actions:

| `WHAT` | Frame | MyHOME_Suite command | Meaning |
| ---: | --- | --- | --- |
| `0` | `*14*0*WHERE##` | `miniScenarioSuite.specialCommands.actionLockUnlockActuator.lock` | Lock actuator |
| `1` | `*14*1*WHERE##` | `miniScenarioSuite.specialCommands.actionLockUnlockActuator.unlock` | Unlock actuator |

This is stronger evidence than the frame templates alone: MyHOME_Suite associates the two wire operations with an explicit lock/unlock actuator capability.

## Addressing

The ScenarioDevices records use `WhereType = 1` and substitute the selected target into the `WHERE` placeholder. The database does not define a separate `WHO 14` address grammar; the address must therefore be interpreted in the context of the selected actuator Object and the underlying system.

A decoder should preserve the literal `WHERE` rather than assume that `WHO 14` introduces a new universal address family.

## Scope of the semantics

The lock/unlock labels are directly established for the MyHOME_Suite actuator lock/unlock Object. They should not be generalized to undocumented `WHO 14` values or to arbitrary target types without further evidence.

The two known commands are ordinary command frames, not `DIMENSION` operations. No additional `WHO 14` `WHAT` or `DIMENSION` vocabulary is established by `OPEN.db` or the ScenarioDevices databases in the current corpus.

## Scenario-engine relationship

ScenarioDevices exposes `WHO 14` as an action capability, so MyHOME_Suite can place actuator lock/unlock operations in higher-level scenarios. This does not make `WHO 14` itself a scenario protocol.

Stored scenarios remain under [`WHO 0`](../who-0-scenarios/), while scenario-programmer execution and management are under [`WHO 17`](../who-17-scenario-management/).

See [Cross-database functional coverage](../cross-database-coverage.md) for the relationship between ScenarioDevices, `OPEN.db`, and `MHCatalogue.db`, and [Scenario Engine](../../scenario-engine/) for the higher-level trigger/condition/action model.

## MH202 implementation evidence

The MH2021.0.24 package contains separately reviewed translator and8-byte pending/ID state-machine code for selected WHAT0/1 paths. The source includes brief-body construction and conditional software receipt/field forwarding under supplied parser, address/configuration and provider premises.

These observations retain the attributed actuator lock/unlock labels above; they do not prove a physical lock operation, universal target grammar, accepted raw command or whole-framework timeout policy.

See the [build-specific continuation](../../reverse-engineering/firmware-analysis/mh202-1.0.24-functional-translation.md#who14-special-commands-and-who15-cen) and [source review capsule](../../project/review/firmware-analysis/mh202-1.0.24/). No new runtime, oracle, specification/database audit or physical observation is reported by this source analysis.
