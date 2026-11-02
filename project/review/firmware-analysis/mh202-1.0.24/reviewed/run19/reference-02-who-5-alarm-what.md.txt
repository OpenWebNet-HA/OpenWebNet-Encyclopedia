# `WHAT` Reference

| `WHAT` | Meaning | Typical role |
| ---: | --- | --- |
| `0` | Maintenance | Central-unit state |
| `1` | Activation | Central-unit state |
| `2` | Disactivation | State/event |
| `3` | Delay end | Event |
| `4` | System battery fault | Fault state/event |
| `5` | Battery OK | State/event |
| `6` | No network | Mains/network fault state |
| `7` | Network present | Mains/network state |
| `8` | Engage | System state/control context |
| `9` | Disengage | System state/control context |
| `10` | Battery unloads | Battery fault state |
| `11` | Active zone | Zone state |
| `12` | Technical alarm | Alarm event |
| `13` | Reset technical alarm | Alarm event/state |
| `14` | No reception / `ACK` peripheral device | Peripheral state |
| `15` | Intrusion alarm | Alarm event |
| `16` | 24-hour alarm / tampering | Alarm event |
| `17` | Anti-panic alarm | Alarm event |
| `18` | Non-active zone | Zone state |
| `26` | Start programming | Programming operation |
| `27` | Stop programming | Programming operation |
| `31` | Silent alarm | Alarm event |

## Independent state axes

A central-unit status response can contain several of these values in one response transaction. For example, system activation, engagement, battery state and network state are independent properties rather than mutually exclusive members of one enumeration.

Zone state is represented separately: `WHAT 11` reports an engaged/active zone and `WHAT 18` a divided/non-active zone. Alarm frames such as `15`, `16`, and `17` then identify alarm conditions associated with the target selected by `WHERE`.

The labels follow the published `WHO 5` vocabulary. No additional numeric meanings are assigned without implementation or wire evidence.