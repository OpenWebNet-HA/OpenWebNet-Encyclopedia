# Functional Correlations

Literal ScenarioDevices frames provide direct implementation evidence for functional OpenWebNet operations offered by the MyHOME_Suite scenario editor.

Across `ScenarioDevices-program-files.sqlite`, 57 Commands contain OpenWebNet-shaped templates. Every one has a non-null `ChiOpen`, and the parsed frame `WHO` agrees with `ChiOpen` in all 57 rows.

## Explicit functional coverage

| `WHO` | Literal templates | Scenario editor coverage |
| ---: | ---: | --- |
| `0` | 1 | scenario-module action |
| `1` | 17 | Lighting, timed Lighting, dimming, controlled socket, fan, and an Object-contextual door-lock action |
| `2` | 18 | shutter, curtain, advanced positioning, and movement actions |
| `4` | 19 | Temperature Control modes, protection, setpoint, local control, and fan-coil speed |
| `14` | 2 | actuator lock and unlock |

`ChiOpen=2` occurs on 19 Commands because the Delay action also stores `2` while its `Frame` is `NULL`. It is not included among the 18 literal `WHO 2` templates.

## `WHO 0`: scenario action

The Scenario action row stores:

`*0*N*WHERE##`

The Parameter row supplies placeholder `N` with numeric metadata. Interpret `N` and `WHERE` through the [`WHO 0` reference](../functional/who-0-scenarios/) rather than treating the ScenarioDevices numeric metadata as a complete protocol grammar.

## `WHO 1`: target-dependent editor semantics

ScenarioDevices stores ordinary Lighting actions such as:

- `*1*0*WHERE##` - OFF;
- `*1*1*WHERE##` - ON;
- `*1*11*WHERE##` through `*1*16*WHERE##` - fixed timed actions;
- `*#1*WHERE*#2*ora*min*sec##` - parameterized timed action;
- `*#1*WHERE*#1*liv*v##` - 100-level dimming action.

It also labels `*1*17*WHERE##` as `automation.actionAutomationDoorLock.on`. Public `WHO 1` semantics still apply at the wire level; the door-lock label is an Object-contextual MyHOME_Suite presentation. This demonstrates that user-facing meaning can depend on the target Object as well as `WHO` and `WHAT`.

See the [`WHO 1` reference](../functional/who-1-lighting/) and [cross-database functional coverage](../functional/cross-database-coverage.md).

## `WHO 2`: Automation

The templates cover:

- UP, DOWN, and STOP;
- absolute position through `DIMENSION 11`;
- advanced movement with a step parameter;
- advanced STOP;
- step-by-step movement.

Shutter and Curtain editor Objects can emit identical wire templates with different user-facing labels. Preserve the selected Object context while decoding the frame through the [`WHO 2` reference](../functional/who-2-automation/).

## `WHO 4`: Temperature Control

ScenarioDevices supplies implementation templates using functional Dimensions:

| Function | Template form |
| --- | --- |
| comfort/eco/protection modes | `*#4*ZAZB*#7*[MODE]*[FUNCTION]*##` |
| setpoint | `*#4*ZAZB*#7*[MODE]*1*c1c2c3c4##` |
| OFF | `*#4*ZAZB*#7*0*5*##` |
| local control | `*#4*ZAZB*#5*val##` |
| fan-coil speed | `*#4*ZAZB*#11*val##` |

The exact stored rows distinguish Heat, Cool, Auto, and Generic modes and Comfort, Eco, Protection, Setpoint, and OFF functions. The semantic-to-wire conversion for `c1c2c3c4` and the enumeration of `val` require the [`WHO 4` reference](../functional/who-4-temperature-control/) or additional application evidence.

The local-control and fan-coil-speed rows exist only in the Program Files revision.

## `WHO 14`: actuator lock and unlock

ScenarioDevices provides direct labels for two otherwise sparsely documented operations:

| Resource-key command | Frame | Implementation meaning |
| --- | --- | --- |
| `.lock` | `*14*0*WHERE##` | lock actuator |
| `.unlock` | `*14*1*WHERE##` | unlock actuator |

This is MyHOME_Suite implementation evidence scoped to the Lock/Unlock Actuator Object. See the [`WHO 14` reference](../functional/who-14-special-commands/).

## Symbolic capabilities

Five non-null frames are not OpenWebNet frame strings:

- `ResetSOS[WHERE]`;
- `DND ON` and `DND OFF`;
- `MUR ON` and `MUR OFF`.

These values establish named internal operations, not complete wire frames. No `WHO` should be manufactured from them.

## Frame-absent capabilities

Ninety-five Commands have `Frame=NULL`, including most triggers and conditions, CEN/CEN+ events, time capabilities, Virtual Key Card events, and the Delay action.

Their resource keys and Parameters are useful application evidence. They do not establish an incoming or outgoing OpenWebNet frame without another source.

## Cross-source rule

ScenarioDevices can enrich a protocol frame with editor Object/command context. It cannot override the functional protocol grammar, prove Device applicability, or establish a cross-database Object join by numeric coincidence.
