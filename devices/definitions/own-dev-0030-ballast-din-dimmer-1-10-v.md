# Ballast DIN dimmer 1-10 V

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0030` | Project identity |
| Technical description | DIN-rail 1-10 V ballast dimmer | Catalogue + official family documentation |
| Catalogue item / model | `31` / `modobj 7` | Implementation evidence |
| Firmware applicability | firmware `174`, `-1.-1.-1`, one slot | Implementation evidence |
| Commercial identities | `F413` | Catalogue |
| Categories | Dimmer, Lighting | Capability model |

## Commercial identities

The canonical catalogue identifies `F413` as the sole commercial record for technical item `31`. Current publisher catalogues use the successor/reference form `F413N`; this dossier does not silently equate the two as identical hardware.

## Documentation

The archived MyHOME automation documentation supplies the historical family context. Current Legrand/BTicino documentation for `F413N` confirms the continuing 1-10 V ballast-dimmer role, but current-product electrical values are not projected backward onto `F413` without a revision-specific source.

## Identity

Catalogue item `31` maps to Automation `modobj = 7`.

## Firmware and hardware

Firmware `174` is wildcard `-1.-1.-1` and declares one Module.

## Module, Object, and Virgin Object model

The Module resolves to Object `8`, **Dimmer actuator**. The catalogue records one Virgin-Object relationship for this technical item through the shared dimmer model.

## Configuration modes

Advanced Configuration, Physical Configuration and Virtual Configuration are declared.

## Firmware-scoped configuration

Firmware `174` exposes `A`, `PL`, `M`, `G1` and `AID`. Its `M` description uses the classic `1..4`, `PUL`, `SLA` mode family. Object `8` also provides the reusable dimmer parameter surface, but firmware applicability must be evaluated before exposing newer load-type/minimum-level fields.

## Object configuration surfaces

The Device is one addressed Dimmer actuator Module. The shared Object surface must not be mistaken for proof that every later dimmer feature exists on F413.

## Conditions, filters, and conversions

The technical inventory records one condition and one conversion rule for this item. Their generic execution semantics are documented in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

Use standard identity, firmware, Object, address and configuration diagnostics.

## Functional applicability

The Device participates in [`WHO 1` - Lighting](../../functional/who-1-lighting/), with dimming applied through its 1-10 V ballast-control role.

## Observed behavior and corroboration

No sanitized F413 hardware fingerprint is currently retained.

## Programming

Preserve the classic `M` mode and group semantics. Do not substitute current F413N electrical specifications or configuration behavior unless the hardware identity has been established.

## Source reconciliation

The canonical database establishes F413 as a one-slot Dimmer actuator with physical, virtual and advanced configuration. Publisher material confirms the 1-10 V family role, while the currently published F413N material represents a later/current reference. The dossier therefore keeps historical F413 identity separate from successor specifications.

## Evidence limits and open work

- Recover and archive a publisher-original F413-specific technical sheet.
- Resolve the recorded condition and conversion rule into human-readable behavior.
- Add a sanitized hardware fingerprint and establish F413 versus F413N revision continuity.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
