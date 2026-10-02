# Addressing

Temperature Control uses a zone/probe-oriented `WHERE` grammar rather than the `A`/`PL` grammar used by Lighting and Automation. Leading zeroes are significant because they distinguish address classes.

## Published functional `WHERE` forms

| Scope | Form | Meaning |
| --- | --- | --- |
| General probes | `0` | All probes |
| Master probe | `1..99` | Master probe of zone `1..99` |
| All probes in zone | `001..099` | Master and slave probes belonging to the selected zone |
| Individual probe | `PZZ` | Probe `P` (`1..8`) of zone `ZZ` (`01..99`) |
| Central unit | `#0` | Temperature Control central unit |
| Zone via central unit | `#1..#99` | Selected zone controlled through the central unit |

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

Actuator-oriented `DIMENSION` operations can append an actuator selector to the zone address. This is distinct from addressing a probe in the same zone and is used by operations such as actuator state reported by read-only `DIMENSION 20`. The public forms are `Z#N` for actuator `N` (`1..9`) in zone `Z` (`0..99`), `Z#0` for all actuators of a zone, and `0#0` for all actuators. Split control uses the additional prefix `3#Z#N` under `DIMENSION 22`.

## Central-unit addressing

A leading `#` identifies central-unit scope in the published functional grammar. `#0` addresses the central unit itself; `#N` addresses zone `N` through the central unit. Central-unit commands include zone mode changes, setpoint changes, program/scenario selection, and holiday operations.

## Historical central-unit variants

The BTouch source distinguishes 3550 (99-zone) and 4695 (four-zone) central units. The mature four-zone probe implementation composes a probe/zone address with a central selector, such as `23#1`, and writes a controlled setpoint through `#23#1`. These application variants must remain distinct from ordinary `#N` central-zone addressing.

For the four-zone case where probe and central share an address, the source describes a missing setpoint-change notification after entering manual mode. The client schedules a setpoint read after 10 seconds if the report has not arrived. The affected Firmware revisions are not named. This workaround is implementation evidence, not a deadline or a defect established for every 4695. Older external-probe code describes addresses `x00` with `x = 1..9`; that historical rule does not override the exact test addresses used by the later [external-temperature operation](dimensions.md#historical-external-probe-dimension-15).

See [Temperature Control evidence](../../project/review/myopencommunity-integration.md#temperature-control).

See [`WHAT` Reference](what.md) for central-unit commands, [`DIMENSION` Reference](dimensions.md) for operation-specific payloads, and [Addressing](../../protocol/addressing.md) for the common system-scoped addressing model.
