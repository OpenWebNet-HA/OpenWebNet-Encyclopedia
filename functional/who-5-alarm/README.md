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

In MH202 Firmware `1.0.24`, the inspected reverse-translation path maps opcode text `42` and status text `09` to `*5*27*##`. This source-derived candidate preserves an empty `WHERE`; it is not an observed alarm operation. The published `WHAT 27` meaning, Stop programming, remains unchanged, while the incoming status path's physical significance is unresolved.

An isolated original-parser case represents the empty target with a NULL `WHERE` member. A same-object serialization case preserves the exact empty-field text. These establish selected local parsing/formatting behavior under modeled dependencies, without assigning a physical target or proving downstream publication. See [MH202 alarm translation](../../reverse-engineering/firmware-analysis/mh202-1.0.24-functional-translation.md#native-parsing-of-the-generated-candidates).
