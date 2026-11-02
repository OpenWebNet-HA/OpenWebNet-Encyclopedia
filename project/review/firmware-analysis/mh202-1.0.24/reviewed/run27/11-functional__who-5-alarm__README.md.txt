# `WHO 5` - Alarm

`WHO 5` defines the OpenWebNet Burglar Alarm system. The published protocol is primarily a monitoring and state-reporting interface: it exposes central-unit state, zone state, alarm events, power and battery conditions, technical and silent alarms, and a small set of programming-related operations.

## Reference

| Subject | Page |
| --- | --- |
| Session behavior and status reporting | [Protocol](protocol.md) |
| Published `WHAT` vocabulary | [`WHAT` Reference](what.md) |
| Central unit, zone, sensor and auxiliary addressing | [Addressing](addressing.md) |

## State model

Alarm traffic is not reducible to one armed/disarmed Boolean. A central-unit status request can produce several frames describing system mode, engagement, battery and mains conditions, active/divided zones, and alarm conditions before the terminating `ACK`.

Zone-specific requests similarly report whether a selected zone is engaged or divided. Alarm events identify their scope through the `WHO 5` `WHERE` grammar, which is independent of Lighting/Automation `A`/`PL` addressing.

The published interface does not define a general-purpose modern security-control API. Implementations should therefore expose the documented states and events without inventing write semantics for status values that are only established as reports.

`WHO 5` is distinct from Access Control [`WHO 23`](../who-23-access-control/) and from diagnostic protocol families. Common frame/session syntax is documented under [Protocol](../../protocol/).
## MH202 implementation evidence

A selected MH2021.0.24 reverse translation maps opcode text42/status text09 to candidate `*5*27*##`. The existing published WHAT27 label Stop programming remains unchanged, while the physical significance of this incoming status path is unverified. The empty WHERE remains literal; a later isolated original-parser case constructs a kind1 object with a NULL WHERE member. This does not assign a published target role or establish downstream delivery. The report assigns no observed arming/control behavior. See [MH202 alarm status translation](../../reverse-engineering/firmware-analysis/mh202-1.0.24-functional-translation.md#alarm-status-and-the-published-command-vocabulary).

See [the exact generated-candidate parser results](../../reverse-engineering/firmware-analysis/mh202-1.0.24-functional-translation.md#native-parsing-of-the-generated-candidates) and [conditional post-decoded routing](../../reverse-engineering/firmware-analysis/mh202-1.0.24-functional-translation.md#conditional-post-decoded-alarm-routing) for the distinct parsing and admission boundaries.

The [same-object serializer test](../../reverse-engineering/firmware-analysis/mh202-1.0.24-functional-translation.md#same-object-serialization-preserves-both-strings) reproduces the exact alarm empty field text under explicit private models. This closes local parsing/formatting for that case, while publication, active field state and physical behavior remain separate.
