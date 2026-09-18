# `WHO 3` — Load Management

`WHO 3` controls load-shedding priorities and reports the basic electrical measurements exposed by the load-management control unit.

## Reference

- [`WHO 3` Protocol Reference](protocol.md) — `WHAT`, `WHERE`, measurement `DIMENSION` values, and complete request/response patterns.

## Scope

The namespace models eight priority targets (`#1`–`#8`), their disabled/enabled/forced states, and voltage/current/power/energy readings from `WHERE 10`.

It is separate from [`WHO 11`](../who-11-energy-distribution/) and the later [`WHO 18`](../who-18-energy-management/) Energy Management namespace. Values must not be copied between them based on similar terminology.

## Evidence basis

The functional grammar is established by [`WHO_3.pdf`](../../sources/openwebnet-public/pdf/WHO_3.pdf). MyHOME Suite `OPEN.db` confirms the namespace name but does not associate a concrete functional operation set with it in this revision.
