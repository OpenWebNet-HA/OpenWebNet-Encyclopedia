# `WHO 23` - Access Control

`WHO 23` identifies Access Control. The current corpus establishes a managed functional/diagnostic family and concrete MyHOME Suite address classes, but not a complete ordinary functional command table.

## MyHOME Suite model

`OPEN.db` records functional `WHO 23`, diagnostic `WHO 1023`, `managed = 1`, and the same 65-record management-operation set associated with the Lighting/Automation and Energy Management families.

It defines two Access Control address classes:

| Target class | Virtual form | Advanced form |
| --- | --- | --- |
| Command or virgin Device | `20` | `20` |
| Indicators | `7[R1][R2]` | `7[R1R2]` |

These labels and forms are implementation evidence for MyHOME Suite management/address construction. They do not establish a functional `WHAT` or `DIMENSION` vocabulary.

## Protocol boundary

Do not decode Access Control using Lighting/Automation A/PL or Alarm zone/sensor rules. Diagnostic discovery and configuration use `WHO 1023` and belong under [`diagnostics/`](../../diagnostics/).

The shared 65-record management set establishes participation in the common Device → Module → Object → Configuration infrastructure where applicable; it does not imply that every Access Control Device implements every operation.

## Evidence status

The current public PDF corpus contains no dedicated `WHO 23` functional specification. Preserve unknown functional frames losslessly and add semantics only from a canonical source, an exact implementation template, or observed traffic.

See [MyHOME Suite `OPEN.db` Coverage](../open-db-coverage.md), [Cross-database functional coverage](../cross-database-coverage.md), and the [Device Model](../../device-model/).
