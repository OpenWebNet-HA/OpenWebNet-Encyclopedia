# `DIMENSION 32`: Module Addressing

`DIMENSION 32` reports the configured system and address associated with one internal slot.

## Frame

`*#[WHO]*[WHERE]*32#[SLOT]*[SYS]*[ADDR]##`

| Field | Range in `OPEN.db` | Meaning |
| --- | ---: | --- |
| `SLOT` | `1`–`255` | Device-local internal slot |
| `SYS` | `1`–`255` | system selector |
| `ADDR` | `0`–`65535` | encoded address value |

The `#` before `SLOT` is part of the frame grammar.

## Interpretation boundary

`SYS` and `ADDR` are not a complete address description in isolation. Resolve them with:

- the diagnostic family;
- the Object reported for the same internal slot by `DIMENSION 30`;
- the functional system’s addressing rules;
- catalogue configuration metadata where corroborated.

The range `0`–`65535` is storage capacity, not a universal set of valid functional addresses.

## Device address versus Module address

The outer `WHERE` is the diagnostic response context. `ADDR` is the configured address of the Module identified by `SLOT`. They can coincide, but they are not defined as the same field.

In observed `WHO 1001` Device interviews, the ordinary diagnostic `WHERE` often matched the `A`/`PL` address of internal slot `1`. Other Modules on the same Physical Device reported different addresses. This correlation remains capture-derived and must not be used as a universal Device-address rule.

## Lighting and Automation

For Lighting/Automation Objects, an encoded value can be rendered as `A`/`PL` only after applying the relevant address rule. Documentation should record both the raw `ADDR` and the decoded components.

An observed Device layout included:

| Internal slot | Object | `A` | `PL` | Rendered `WHERE` |
| ---: | ---: | ---: | ---: | ---: |
| `1` | `6` | `1` | `0` | `10` |
| `2` | `6` | `1` | `6` | `16` |
| `3` | `400` | `1` | `0` | `10` |

The repeated `10` demonstrates that different Modules can share an address while exposing different Objects.

## Other systems

Temperature Control zones, CEN/CEN+ identifiers, Energy Management targets, and Access Control addresses use different grammars. For example, CEN virtual identifiers occupy `0`–`2047`; that domain must not be decoded as `A`/`PL`.

Keep the raw tuple `(SYS, ADDR)` whenever the system-specific decoder is unavailable.

## Missing records

Not every Module necessarily produces `DIMENSION 32`. A missing address can indicate an unconfigured Module, an Object without an address, unsupported reporting, or an incomplete interview. One observed light-control-only Device returned Module data without an observed `DIMENSION 32`; that single capture does not establish the reason.

## Address errors

`DIMENSION 34` reports an address error for one internal slot:

`*#[WHO]*[WHERE]*34*[SLOT]*[ERROR]##`

`ERROR` is boolean in `OPEN.db`. The database does not enumerate finer error causes, so retain the raw flag and surrounding Module/Object context.
