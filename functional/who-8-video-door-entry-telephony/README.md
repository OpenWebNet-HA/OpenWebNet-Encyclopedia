# `WHO 8` - Video Door Entry and Telephony

`WHO 8` identifies the OpenWebNet Video Door Entry and telephony system. The current corpus establishes the namespace and a narrow MyHOME Suite service operation, but not a complete public functional grammar.

## Established implementation evidence

`OPEN.db` records:

- functional `WHO 8`;
- diagnostic family `WHO 1008`;
- `managed = 1`;
- the F422 public-riser-interface address rule `1[I1][I2][I3][I4]`, with advanced form `1[I1I2I3I4]`;
- one system-associated generic identification template, `*[WHO]*[WHAT]##`, labelled `cmd_ident`.

The template establishes that MyHOME Suite associates a service-identification operation with this system. Because the database does not enumerate the substituted `WHAT` semantics here, it does not justify a `WHAT` table.

## Evidence boundary

The public corpus has no dedicated `WHO 8` specification. `WHO 6`, `WHO 7`, and `WHO 8` share an application domain but remain independent namespaces. Do not reuse `WHO 7` camera commands or addresses under `WHO 8` without direct evidence.

Diagnostic traffic belongs to `WHO 1008`; the numeric relationship does not make functional and diagnostic frames interchangeable.

## Decoder guidance

Recognize the namespace, preserve unknown fields losslessly, and label only the address form and generic identification operation established above. Device-specific Video Door Entry behavior requires a canonical specification, a database template with resolved parameters, or observed traffic.

See [MyHOME Suite `OPEN.db` Coverage](../open-db-coverage.md), [`WHO 6`](../who-6-basic-video-door-entry/), and [`WHO 7`](../who-7-multimedia-video/).
