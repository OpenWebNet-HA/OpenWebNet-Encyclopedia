# `WHAT` Reference

`WHAT` in `WHO 1` expresses Lighting commands and states. Ordinary frames use `*1*WHAT*WHERE##`; status requests use `*#1*WHERE##`.

## Switching and levels

| `WHAT` | Meaning |
| ---: | --- |
| `0` | OFF |
| `1` | ON |
| `2..10` | `20%..100%` in ten-percent steps |
| `30` | Increase one level |
| `31` | Decrease one level |

The parameterized forms `0#SPEED` and `1#SPEED` switch OFF or ON using the requested transition speed. `30#LEVELS#SPEED` and `31#LEVELS#SPEED` change several levels at the specified speed. These forms must not be reduced to their leading numeric `WHAT`.

For the published speed field, `0` means the last speed used, `1..254` are explicit speeds, and `255` selects the default speed.

## Timed operations

| `WHAT` | ON duration |
| ---: | --- |
| `11` | 1 minute |
| `12` | 2 minutes |
| `13` | 3 minutes |
| `14` | 4 minutes |
| `15` | 5 minutes |
| `16` | 15 minutes |
| `17` | Unresolved duration: summary table says 30 seconds; section 3.1.9 says 30 minutes |
| `18` | 0.5 seconds |

Timed commands switch the target ON for the encoded duration. Their event sequence can include immediate ON followed by a later status report; clients should not treat the initiating `WHAT` as the final persistent state.

### Target-dependent MyHOME Suite label for `WHAT 17`

ScenarioDevices contains `miniScenarioSuite.automation.actionAutomationDoorLock.on` with frame `*1*17*WHERE##`. This establishes a stored door-lock-specific capability label, not the duration or observed emission of the command. It does not resolve the conflict between the `WHO 1` summary table (30 seconds) and section 3.1.9 (30 minutes).

A decoder should retain timed ON with unresolved duration for `WHAT 17`; an Object-aware application may additionally present the contextual label. Establish the duration on the applicable target before relying on either source value.

## Blinking operations

| `WHAT` | Blink period |
| ---: | --- |
| `20..29` | `0.5..5` seconds in 0.5-second increments |

## Command translation - `WHAT 1000`

The published Lighting specification defines `1000#INNER_WHAT` as a command-translation wrapper:

~~~text
*1*1000#INNER_WHAT*WHERE##
~~~

Section 3.1.21 says the command is valid for dimmers too and shows the same wrapper on the event session. This does not establish a dimmer-only restriction or support on every Lighting target. `INNER_WHAT` is a value from the Lighting `WHAT` table. Preserve both the wrapper and inner operation; do not normalize it silently to `INNER_WHAT` because the wrapper itself is observable protocol information.

## ScenarioDevices coverage

ScenarioDevices stores ordinary OFF/ON templates for Lighting Objects and for controlled-socket and fan action Objects. It also contains timed-light and 100-level dimmer actions. Several capability types therefore share a frame template; these rows do not establish which template MyHOME Suite emits for an installed Physical Device.

## Evidence basis

The complete value table, parameterized switching/step forms, speed values, timed and blinking operations, and `WHAT 1000` wrapper come from [`WHO 1` specification](../../sources/openwebnet-public/pdf/WHO_1.pdf). The door-lock label and scenario coverage come from the ScenarioDevices databases and are implementation-specific enrichment.

See [`DIMENSION` Reference](dimensions.md), [Addressing](addressing.md), and [Cross-database functional coverage](../cross-database-coverage.md).
