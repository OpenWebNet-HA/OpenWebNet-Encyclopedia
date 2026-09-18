# `WHO 5` - Alarm

`WHO 5` defines the OpenWebNet Burglar Alarm system. The published protocol is primarily a monitoring and state-reporting interface: it exposes central-unit state, zone state, alarm events, power and battery conditions, technical and silent alarms, and a small set of programming-related operations.

## Reference

| Subject | Page |
| --- | --- |
| Session behavior and status reporting | [`protocol.md`](protocol.md) |
| Published `WHAT` vocabulary | [`what.md`](what.md) |
| Central unit, zone, sensor and auxiliary addressing | [`addressing.md`](addressing.md) |

## State model

Alarm traffic is not reducible to one armed/disarmed Boolean. A central-unit status request can produce several frames describing system mode, engagement, battery and mains conditions, active/divided zones, and alarm conditions before the terminating `ACK`.

Zone-specific requests similarly report whether a selected zone is engaged or divided. Alarm events identify their scope through the `WHO 5` `WHERE` grammar, which is independent of Lighting/Automation `A`/`PL` addressing.

The published interface does not define a general-purpose modern security-control API. Implementations should therefore expose the documented states and events without inventing write semantics for status values that are only established as reports.

`WHO 5` is distinct from Access Control [`WHO 23`](../who-23-access-control/) and from diagnostic protocol families. Common frame/session syntax is documented under [`../../protocol/`](../../protocol/).