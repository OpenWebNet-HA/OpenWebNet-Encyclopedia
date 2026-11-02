# Addressing

Published `WHO 5` `WHERE` values include:

| `WHERE` | Meaning |
| --- | --- |
| `1` | Control panel |
| `#0..#8` | Central zone `0..8` |
| `#1..#9` | Auxiliary `1..9` (`WHO 9` relationship in the published table) |
| `01..0n` | Input-zone device |
| `11..1n` | Zone 1 sensor |
| `81..8n` | Zone 8 sensor |
| `#12` | Zone C / AUX C |
| `#15` | Zone F / AUX F |

Zone `0` is used for inputs and the three internal sirens in the published model. Alarm addressing is therefore its own `WHO 5` grammar and must not be parsed as Lighting/Automation A/PL.

## Historical event validation

The `TS10_1_0_23` touchscreen library and its tests use these numeric event-source filters:

| Event | `WHAT` | Accepted `WHERE` |
| --- | ---: | --- |
| Engaged / partialized zone | `11` / `18` | `#1..#8` |
| Intrusion | `15` | `#1..#8` |
| Tamper | `16` | `#0..#15` |
| Anti-panic | `17` | `#9` |
| Technical alarm / reset | `12` / `13` | `#1..#15` |

These are library filters, not a replacement for every published sensor address. Armed/disarmed reports (`WHAT 8`/`9`) are handled without a `WHERE` check. The parser also lacks a numeric-conversion success check for `#N`; its permissiveness does not establish additional valid addresses.

BtExperience applies another filter before adding decoded events to its alarm list:

| Event | Required local Configuration |
| --- | --- |
| Intrusion | Matching configured zone |
| Technical alarm | Matching configured auxiliary source |
| Tamper at source `0..8` | Matching configured zone |
| Tamper at source `9..15`, anti-panic at `9` | No configured source required |

A wire event can therefore be decoded and still omitted from the displayed list. The library handles armed/disarmed state, zone engagement/partialization and the four alarm families above; it does not forward every published maintenance, battery, mains or silent-alarm value to this product model.

See [Alarm evidence](../../project/review/myopencommunity-integration.md#alarm-controls-and-events), the [Alarm history review](../../project/review/myopencommunity-alarm-history-review.md), and [Protocol](protocol.md#event-connection) for local list behavior.
