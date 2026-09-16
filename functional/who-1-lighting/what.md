# `WHAT` Reference

`WHAT` in `WHO 1` expresses lighting commands and states. Ordinary command and status frames use `*1*WHAT*WHERE##`; status requests use `*#1*WHERE##`.

## Switching and dimming

| `WHAT` | Meaning |
| ---: | --- |
| `0` | OFF |
| `1` | ON |
| `2` | 20% |
| `3` | 30% |
| `4` | 40% |
| `5` | 50% |
| `6` | 60% |
| `7` | 70% |
| `8` | 80% |
| `9` | 90% |
| `10` | 100% |
| `30` | Step up |
| `31` | Step down |

The discrete dimmer levels represented by `WHAT 2`–`10` are the protocol's ten-percent steps from 20% through 100%. Finer level control is provided by Lighting `DIMENSION` operations rather than by additional ordinary `WHAT` values.

## Timed operations

| `WHAT` | ON duration |
| ---: | --- |
| `11` | 1 minute |
| `12` | 2 minutes |
| `13` | 3 minutes |
| `14` | 4 minutes |
| `15` | 5 minutes |
| `16` | 15 minutes |
| `17` | 30 seconds |
| `18` | 0.5 seconds |

Timed commands switch the target ON for the duration encoded by the selected `WHAT`.

### Target-dependent MyHOME_Suite label for `WHAT 17`

The ScenarioDevices capability database contains a useful implementation-specific case: `miniScenarioSuite.automation.actionAutomationDoorLock.on` emits the frame `*1*17*WHERE##`.

This does not invalidate the published Lighting definition of `WHAT 17` as 30-second timed ON. It shows that MyHOME_Suite presents that same wire operation as **Automation Door Lock ON** when the selected target Object is a door-lock capability. The higher-level capability label is therefore target-dependent even though the wire-level `WHO`/`WHAT` pair is unchanged.

Implementations that know the target Object may expose the more specific door-lock action. Generic OpenWebNet decoders should retain the protocol-level `WHO 1` / `WHAT 17` interpretation and must not globally rename `WHAT 17` to door lock.

## Blinking operations

| `WHAT` | Blink period |
| ---: | --- |
| `20` | 0.5 seconds |
| `21` | 1 second |
| `22` | 1.5 seconds |
| `23` | 2 seconds |
| `24` | 2.5 seconds |
| `25` | 3 seconds |
| `26` | 3.5 seconds |
| `27` | 4 seconds |
| `28` | 4.5 seconds |
| `29` | 5 seconds |

These meanings are local to `WHO 1`; the same numeric `WHAT` values in another `WHO` do not inherit Lighting semantics.

## ScenarioDevices command coverage

MyHOME_Suite's scenario engine emits ordinary `WHO 1` OFF/ON frames for Lighting Objects and also for controlled-socket and fan action Objects. It additionally contains timed-light commands and 100-level dimmer actions. This confirms that ScenarioDevices models **functional capability**, not a one-to-one physical Device class: several different Object types can intentionally compile to the same OpenWebNet frame.

See [`dimensions.md`](dimensions.md) for Lighting level, transition-speed, temporization, and operating-time `DIMENSION` values, [`addressing.md`](addressing.md) for `WHERE` forms, and [`../cross-database-coverage.md`](../cross-database-coverage.md) for the cross-database implementation model.