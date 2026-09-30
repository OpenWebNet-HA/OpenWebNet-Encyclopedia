# Flush-mounted dimmer

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0027` | Project identity |
| Technical description | Flush-mounted SCS dimmer actuator | Catalogue + official automation documentation |
| Catalogue item / model | `23` / `modobj 5` | Implementation evidence |
| Firmware applicability | firmware `198`, `-1.-1.-1`, one slot | Implementation evidence |
| Commercial identities | `H4674`, `L/N/NT4674` | Catalogue |
| Categories | Dimmer, Lighting | Capability model |

## Commercial identities

The canonical catalogue groups Axolute `H4674` and Living/Light/Light Tech `L/N/NT4674` under technical item `23`.

## Documentation

The archived MyHOME automation guide documents the 4674 dimmer family in the same automation system context. The database supplies the exact firmware/Object/configuration topology used by MyHOME Suite.

## Identity

Catalogue item `23` maps to Automation `modobj = 5`.

## Firmware and hardware

Firmware `198` is wildcard `-1.-1.-1` and declares one Module. Installed hardware remains to be corroborated.

## Module, Object, and Virgin Object model

The single Module resolves to Object `8`, **Dimmer actuator**. Object `8` is also associated with Virgin Object `532` elsewhere in the catalogue; this firmware itself has no Device-specific Virgin Object row.

## Configuration modes

Physical Configuration and Virtual Configuration are declared.

## Firmware-scoped configuration

Firmware `198` exposes `A`, `PL`, `M`, `G1` and `AID`. Its firmware description constrains `M` to the documented dimmer mode family `0` / `I/O`. The reusable Dimmer actuator Object also contains local-button, delayed-off, state-saving, minimum-level, load-type and group fields; those generic fields must only be applied when permitted by this Device's firmware/configuration path.

## Object configuration surfaces

Object `8` is the reusable dimmer surface. The database records one condition for this technical item, so configuration consumers must evaluate the catalogue condition rather than assuming every generic Object field is active.

## Conditions, filters, and conversions

The technical inventory records one condition and no Device-specific conversion rule.

## Diagnostic applicability

Use the standard identity, firmware, Object, address and configuration diagnostics in [Diagnostics](../../diagnostics/).

## Functional applicability

The Device participates in [`WHO 1` - Lighting](../../functional/who-1-lighting/).

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact item is currently retained.

## Programming

Treat the product as one addressed dimmer Module. Do not infer modern universal-dimmer load-selection semantics merely because they exist on the shared Object `8` surface.

## Source reconciliation

The catalogue establishes one Dimmer actuator Module and the two commercial identities. The archived automation documentation corroborates the 4674 family role. Shared Object `8` contains fields used by newer dimmers as well, so this dossier deliberately distinguishes Object capability from firmware-applicable configuration.

## Evidence limits and open work

- Recover and archive a dedicated H4674/L4674 technical-sheet revision if a publisher original is located.
- Add a sanitized hardware fingerprint.
- Resolve the single catalogue condition into a human-readable Device-specific rule.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
