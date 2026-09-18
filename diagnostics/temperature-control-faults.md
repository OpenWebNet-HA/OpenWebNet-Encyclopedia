# Temperature Control Fault Diagnostics

The public Temperature Control specification defines a `WHO 1004` fault-reporting surface for a central unit and its zones. It complements the MyHOME Suite Device-discovery/interview model; it does not use that model's `WHAT 10` selection or require an Object interview first.

## Targets and operations

`#0` selects the central unit. `#1`–`#99` select zones through the central unit. The source also lists unprefixed master-probe addresses `1`–`99`, but the detailed central-unit fault flows below use the prefixed forms.

| Purpose | Request | Response/report |
| --- | --- | --- |
| Central-unit diagnostics | `*#1004*#0*7##` | `*#1004*#0*7*BIT##` |
| Central-unit automatic fault notification | No request defined in this flow | `*#1004*#0*11*BIT##` |
| Zones with failures | `*#1004*#0*20##` | One or more `*#1004*#ZONE*21*BIT##` |
| One zone | `*#1004*#ZONE*21##` | `*#1004*#ZONE*21*BIT##` |
| All zones | `*#1004*#0*21##` | One or more `*#1004*#ZONE*21*BIT##` |
| Automatic zone fault notification | No request defined in this flow | `*#1004*#ZONE*22*BIT##` |
| Fault/non-response counts | `*#1004*#0*23##` | `*#1004*#0*23*NO_RESPONSE*FAULTS##` |

`ZONE` is a placeholder for `1`–`99`. `NO_RESPONSE` is the number of non-answering probes; `FAULTS` is the number of probes with failures. Preserve that order.

The collective flows can begin with an echo-shaped header such as `*#1004*#0*20##` or `*#1004*#0*21##`, before the zone data. A command-session sequence then terminates with `ACK` or `NACK`. The request selector need not equal every returned selector: a `DIMENSION 20` request returns `DIMENSION 21` zone records. Correlate using the complete operation, not selector equality alone.

## Central-unit bits

For `DIMENSION 7` and `11`, the source names 24 bits and identifies the following conditions. These are **active-low**: the listed condition is present when its bit is `0`.

| Source bit number | Condition when `0` |
| ---: | --- |
| `13` | Probe failure |
| `14` | Probe does not answer |
| `15` | Central-unit battery fault |
| `16` | EEPROM read/write failure |
| `21` | Generic system trouble |
| `22` | Configuration trouble |
| `23` | Hardware failure |
| `24` | Device busy |

## Zone bits

For `DIMENSION 21` and `22`, the source names 16 bits. Again, `0` indicates the condition.

| Source bit number | Condition when `0` |
| ---: | --- |
| `11` | Probe does not answer |
| `12` | Pump does not answer |
| `13` | EEPROM read/write failure |
| `14` | Temperature out of range |
| `15` | Slave probe does not answer |
| `16` | Actuator does not answer |

These tables preserve the source's bit numbering. The cited sections do not supply a worked numeric mask or an unambiguous serialized bit-order example. Keep `BIT` raw until the target's representation and bit-order convention are established; do not invent meanings for the unlisted bits.

## Scope and completion

These fault labels apply to the published central-unit/zone workflow. They must not be copied to `WHO 1001` or every generic `DIMENSION 7`/`8` Device response. Likewise, the `WHO 1004` zone `DIMENSION 22` is a fault mask, while functional `WHO 4 DIMENSION 22` controls split units.

An empty or failed collective request does not prove a healthy installation. Preserve the acknowledgement outcome, returned records, and timeout state. Asynchronous `DIMENSION 11` and `22` notifications report fault changes; they are not acknowledgement-terminated command transactions.

## Evidence basis

The [Temperature Control Specification](../sources/openwebnet-public/pdf/WHO_4.pdf), version 2.0.0, pages 69–74, defines these targets, sequences, counts, bit labels, and polarity. See [Diagnostic Architecture](architecture.md) for the separate MyHOME Suite management model and [Temperature Control Properties](../functional/who-4-temperature-control/dimensions.md) for functional properties.
