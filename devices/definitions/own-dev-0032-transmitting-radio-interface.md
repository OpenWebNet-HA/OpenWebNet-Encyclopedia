# Transmitting radio interface

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0032` | Project identity |
| Technical description | SCS-powered radio transmitting interface | Catalogue + official documentation |
| Catalogue item / model | `34` / `modobj 21` | Implementation evidence |
| Firmware applicability | 215, wildcard -1.-1.-1, one slot | Implementation evidence |
| Commercial identities | HC/HS4576; HD4576; L/N/NT4576 | Catalogue |
| Categories | Radio interface, Control bridge, Lighting / Automation | Capability model |

## Commercial identities

The canonical catalogue groups HD4576, HC/HS4576 and L/N/NT4576 under technical item 34. Official historical automation guides directly print HC4576/HS4576 and the Living/Light/Light Tech 4576N forms; the database's grouped L/N/NT4576 spelling is therefore kept as catalogue identity rather than silently rewritten.

## Documentation

The already archived official MyHOME Automation guide describes the 4576 family as a radio transmitting interface, powered from the 27 Vdc BUS and occupying two wiring-device modules.

## Physical and electrical characteristics

Publisher documentation identifies the interface as a 27 Vdc BUS-powered, two-module radio transmitter. Exact suffix/aesthetic variants differ by product line.

## Identity

Catalogue item `34` maps to `modobj = 21`.

## Firmware and hardware

Firmware 215 has wildcard version/revision/build applicability and one Module slot.

## Module, Object, and Virgin Object model

Slot 1 is fixed Object 172, Radio Interface Transmitter.

## Configuration modes

The catalogue declares configuration modes 1 and 3.

## Firmware-scoped configuration

Firmware fields are A, PL, M and AID. Firmware 215 narrows M to modes 0/1, while the reusable Object 172 surface lists the wider generic mode family 0,1,6,7,8,CEN. Device programming must use the firmware-applicable subset.

## Object configuration surfaces

Object 172 provides A, PL and M for one transmitting interface endpoint. Generic Object capabilities are not evidence that every later radio-interface mode is enabled by firmware 215.

## Conditions, filters, and conversions

Object/Firmware filter 1631 constrains a Contact type configuration field associated with this firmware/Object relation. The field should remain conditionally exposed rather than inferred from the short physical M domain.

## Diagnostic applicability

Use the standard Device identity, firmware, Object, address and configuration diagnostics in [Diagnostics](../../diagnostics/). `DIMENSION 30` is particularly important where one slot has multiple candidate Objects.

## Functional applicability

The interface bridges configured SCS control semantics to the supported radio side. Functional meaning depends on the configured command role; it should not be hard-coded as a single lighting action.

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact technical item is currently retained.

## Programming

Treat firmware 215's `M` values 0/1 domain as authoritative for this Device unless direct revision-specific evidence establishes additional modes.

## Source reconciliation

The canonical catalogue establishes the one-slot Radio Interface Transmitter model and the three grouped commercial records. Official historical documentation corroborates the family role and physical format, but suffix naming differs between the implementation catalogue and printed guide; that mismatch remains explicit.

## Evidence limits and open work

- Recover a dedicated publisher technical sheet for the exact database-listed 4576 variants if one exists.
- Hardware-corroborate firmware identity and transmitted command behavior.
- Resolve the Contact type filter into a human-readable Device-specific rule.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf)
