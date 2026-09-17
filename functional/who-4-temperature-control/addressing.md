# Addressing

Temperature Control uses a zone/probe-oriented `WHERE` grammar rather than the `A`/`PL` grammar used by Lighting and Automation. Leading zeroes are significant because they distinguish address classes.

## Published functional `WHERE` forms

| Scope | Form | Meaning |
| --- | --- | --- |
| General probes | `0` | All probes |
| Master probe | `1`–`99` | Master probe of zone 1–99 |
| All probes in zone | `001`–`099` | Master and slave probes belonging to the selected zone |
| Individual probe | `PZZ` | Probe `P` (`1`–`8`) of zone `ZZ` (`01`–`99`) |
| Central unit | `#0` | Temperature Control central unit |
| Zone via central unit | `#1`–`#99` | Selected zone controlled through the central unit |

Examples of individual-probe encoding include `101` for probe 1 of zone 1, `801` for probe 8 of zone 1, and `899` for probe 8 of zone 99.

The forms `1` and `001` are therefore not equivalent: `1` selects the master probe of zone 1, whereas `001` selects all probes belonging to zone 1.

## MyHOME_Suite address rules

The MyHOME_Suite `OPEN.db` address-rule definitions represent Temperature Control through several operation-specific forms:

| Form | Purpose |
| --- | --- |
| `[ZA][ZB]` | Temperature Control zone |
| `[ZAZB]` | Advanced zone form |
| `#0#[ZA][ZB]` | Four-zone central-unit form |
| `[ZA][ZB]#[N]` | Temperature Control actuator instance |

These implementation forms complement the public functional grammar. The selected operation determines which rule is valid; clients must not normalize all Temperature Control `WHERE` values to one integer zone identifier.

## Actuator addressing

Actuator-oriented `DIMENSION` operations can append an actuator selector to the zone address. This is distinct from addressing a probe in the same zone and is used by operations such as actuator state/control represented by `DIMENSION 20`.

## Central-unit addressing

A leading `#` identifies central-unit scope in the published functional grammar. `#0` addresses the central unit itself; `#N` addresses zone `N` through the central unit. Central-unit commands include zone mode changes, setpoint changes, program/scenario selection, and holiday operations.

See [`what.md`](what.md) for central-unit commands, [`dimensions.md`](dimensions.md) for operation-specific payloads, and [`../../protocol/addressing.md`](../../protocol/addressing.md) for the common system-scoped addressing model.