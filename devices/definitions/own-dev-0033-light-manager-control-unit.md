# Light manager control unit

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0033` | Project identity |
| Technical description | Lighting Management control unit, Ethernet interface, scenario scheduler and Open/SCS gateway | Catalogue + official documentation |
| Catalogue item / model | `35` / `modobj 35` | Implementation evidence |
| Firmware applicability | 126, version 2.0 build 1, three slots | Implementation evidence |
| Commercial identities | BMNE500 | Catalogue |
| Categories | Gateway, Lighting management, Scenario scheduler, Integration | Capability model |

## Commercial identities

The canonical catalogue maps BMNE500 to technical item 35 and marks it as a gateway.

## Documentation

The current BTicino catalogue describes BMNE500 as a Lighting Management control unit interfacing the Ethernet network and managing scenarios, with software configuration. The official TiBMNE500 software manual documents the Lighting plant, sensor, actuator, zone, scheduling and scenario configuration surfaces.

## Physical and electrical characteristics

Current publisher data gives 12..27 V supply, BUS maximum consumption 8 mA and a six-DIN-module enclosure.

## Identity

Catalogue item `35` maps to `modobj = 35`.

## Firmware and hardware

Firmware 126 is version 2.0 build 1 and declares three Module slots.

## Module, Object, and Virgin Object model

The topology is explicit and fixed: slot 1 is Object 127 Lighting manager; slot 2 is Object 61 Scenario scheduler; slot 3 is Object 150 Gateway Open SCS.

## Configuration modes

The catalogue lists configuration mode 4 only. Publisher documentation independently states that BMNE500 is configured by software.

## Firmware-scoped configuration

Firmware fields include AID, IS_GATEWAY, SYSADDRESS, FW_VER, CMD_PORT, LAN_IP_ADDRESS, LAN_IP_ADDR_TYPE and CONNECTION_METHOD. The three Objects add their own network/gateway and scenario-scheduler configuration surfaces.

## Object configuration surfaces

Object 127 owns Lighting Manager network settings, Object 61 owns scheduler/network fields, and Object 150 represents the Open/SCS gateway. These are three fixed functional Modules of one Physical Device, not three separate products.

## Conditions, filters, and conversions

No Object/Firmware filter rows were returned for the three fixed BMNE500 Object relations in the current canonical catalogue. Network fields still require normal datatype/range validation.

## Diagnostic applicability

Use the standard Device identity, firmware, Object, address and configuration diagnostics in [Diagnostics](../../diagnostics/). `DIMENSION 30` is particularly important where one slot has multiple candidate Objects.

## Functional applicability

BMNE500 spans Lighting Management and integration functions: lighting supervision, scheduling/scenarios and Open/SCS gateway access.

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact technical item is currently retained.

## Programming

Keep gateway/network identity fields separate from runtime lighting objects. Preserve all three fixed Modules and do not collapse BMNE500 to a generic Ethernet gateway.

## Source reconciliation

The canonical database and current publisher material agree that BMNE500 is a software-configured Lighting Management gateway/control unit. The database adds the exact three-slot internal model: Lighting manager, Scenario scheduler and Gateway Open SCS.

## Evidence limits and open work

- Archive the publisher BMNE500 product sheet and TiBMNE500 manual when a stable downloadable endpoint is available to the build environment.
- Add a sanitized BMNE500 hardware fingerprint and gateway-session observations.
- Corroborate firmware 2.0 build 1 against observed DIM2/DIM3/DIM6 diagnostics.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [https://catalogue.bticino.com/pdf/scheda-prodotto/BTI-BMNE500](https://catalogue.bticino.com/pdf/scheda-prodotto/BTI-BMNE500)
- [https://dar.bticino.com/asset/Documents/U4554C_S4_EN.pdf](https://dar.bticino.com/asset/Documents/U4554C_S4_EN.pdf)
