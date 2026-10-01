# Energy display 2 modules

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0048` | Project identity |
| Technical description | Energy display 2 modules | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `H4710`, `LN4710`, `067205`, `64171` | Canonical commercial records |
| Catalogue item | `1884` | Canonical catalogue |
| Main catalogue system | New energy saving and load control | Canonical catalogue |
| Item model / `modobj` | `14` | Canonical inventory |
| Firmware definition | `1.0.-1` | Canonical firmware catalogue |
| Declared Modules | `10` | Canonical firmware catalogue |
| Categories | Energy management, Display, Load control | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4710` | established catalogue identity for item `1884` | canonical commercial record |
| BTicino - LivingLight | `LN4710` | established catalogue identity for item `1884` | canonical commercial record |
| Legrand - Céliane | `067205` | established catalogue identity for item `1884` | canonical commercial record |
| Arnould - Espace Evolution | `64171` | established catalogue identity for item `1884` | canonical commercial record |
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ01014_a_EN` | technical sheet | revision a | Energy display functions, pages and measuring/load-management relationships | [Archived original](../../sources/devices/documents/device-doc-energy-display-mq01014-a-en/MQ01014_a_EN.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ01014_a_EN.pdf) |
| BTicino `H4710` catalogue page | product page | current catalogue | Current `H4710` electrical characteristics and product role | Not applicable - web page | [Official product page](https://catalogue.bticino.com/product/smart-home-solutions/my-home---home-automation-system/consumption-display/BTI-H4710-EN) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display | `1.6 inch` consumption/load-control display | `MQ01014_a_EN` / current catalogue |
| Supply | `27 Vdc` | Current BTicino `H4710` catalogue |
| Input current | `33 mA` | Current BTicino `H4710` catalogue |
| Width | 2 wiring-device modules | Current BTicino `H4710` catalogue |
| System role | Displays energy data and can control load-management actuators | `MQ01014_a_EN` / current catalogue |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1884` | Canonical catalogue |
| Technical item | Energy display 2 modules | Canonical catalogue |
| Main system | New energy saving and load control | Canonical catalogue |
| Item model / `modobj` | `14` | Canonical inventory |
| Commercial records | `4` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `405` | `1` | `0` | `-1` | `10` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `405` | `2315, 2316, 2317, 2318, 2319, 2320, 2321, 2322, 2323` | `606` Measurement data visualization | catalogue firmware/Object relation |
| `405` | `2324, 2325, 2326, 2327, 2328, 2329, 2330, 2331, 2332` | `492` Load control actuator visualization | catalogue firmware/Object relation |
| `405` | `2333` | `608` Energy display settings | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| `405` | `531` | catalogue candidate/template association |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `405` | Advanced Configuration | supported configuration route for this Device family |
| `405` | Physical configuration | supported configuration route for this Device family |
| `405` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `405` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `405` | `M1` | catalogue-defined domain | catalogue-scoped | Energy display basic mode for installation in France |
| `405` | `M2` | catalogue-defined domain | catalogue-scoped | Energy display basic mode for installation in Italy |

## Object configuration surfaces

### Object `492` - Load control actuator visualization

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `PRIORITY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Priority |
| `PHASE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Phase |

### Object `606` - Measurement data visualization

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `LINE_1_OPERATION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Value of the first address |
| `LINE_1_ADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | First address |
| `LINE_2_OPERATION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Operation with the second address |
| `LINE_2_ADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Second address |
| `LINE_3_OPERATION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Operation with the third address |
| `LINE_3_ADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Third address |
| `LINE_4_OPERATION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Operation with the fourth address |
| `LINE_4_ADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Fourth address |
| `LINE_5_OPERATION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Operation with the fifth address |
| `LINE_5_ADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Fifth address |
| `LINE_6_OPERATION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Operation with the sixth address |
| `LINE_6_ADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Sixth address |
| `COEFFICIENT_K_USE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | State of multiplication factor (for all the lines) |
| `COEFFICIENT_K_L` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Multiplication factor (low) |
| `COEFFICIENT_K_H` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Multiplication factor (high) |
| `ICON` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Icon |
| `MEASUREMENT_UNIT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Measurement unit |

### Object `608` - Energy display settings

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `BACKLIGHT_LEVEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Display backlight level |
| `BUZZER` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Enable/Disable beep |
| `DATE_FORMAT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Display date format |
| `THRESHOLD_USE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Threshold use |
| `THRESHOLD_ADDRESS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Threshold address |
| `THRESHOLD_VALUE_L` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Threshold value L |
| `THRESHOLD_VALUE_H` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Threshold value H |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | `1907`, `1908`, `1909`, `1910` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | none | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1884` / `modobj = 14` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`492`, `606`, `608`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Energy-consumption visualization and load-management control with up to ten declared logical Modules and catalogue-selected energy/load-control Object families.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The technical sheet names H4710, 067205 and LN4710 and prints the Arnould reference as 064171; the canonical catalogue records 64171. The reference-format discrepancy is retained rather than silently normalized.

## Evidence limits and open work

- Archive the identified publisher documents locally where licensing and repository policy allow.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate relation filters and condition-selected topology against MyHOME Suite and controlled hardware observations.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
