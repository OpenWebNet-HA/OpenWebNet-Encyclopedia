# Eight-output DIN ON/OFF actuator 16 A

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0101` | Project identity |
| Technical description | Eight-output DIN ON/OFF lighting actuator with zero-current switching | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSW1005`, `002604` | Canonical commercial records and publisher guides |
| Catalogue item | `1156` | Canonical catalogue |
| Main catalogue system | Automation (`lighting_automation`) | Canonical catalogue |
| Item model / `modobj` | `159` | Canonical catalogue |
| Firmware definition | `-1.-1.-1` | Canonical catalogue wildcard applicability |
| Declared Modules | `8` | Canonical firmware catalogue |
| Categories | Lighting, Actuator, DIN, Lighting Management | Catalogue and publisher capability evidence |

This Device is the shared technical definition behind Legrand `0 026 04 / 002604` and BTicino `BMSW1005`. It provides eight independently controlled ON/OFF lighting outputs, local output controls, BUS/SCS integration, zero-current switching, physical/virtual configuration, and - in the earlier Lighting Management documentation - Push'n Learn association.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSW1005` | Established identity | canonical item `1156`; 2025 MyHOME guide and BUS/SCS guides |
| Legrand | `0 026 04` / `002604` | Established identity | canonical item `1156`; dedicated technical sheets, PEP and BUS/SCS guides |

The later BUS/SCS guides explicitly write the pair as “`0 026 04` or `BMSW1005`”, providing direct publisher evidence that the two commercial references describe the same technical actuator.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `F01132EN-04.pdf` | technical sheet | `/04`, updated `2017-11-06` | Full document, PDF pp. 1-3; `0 026 04` | [Archived original](https://archive.openwebnet-ha.org/sha256/f0/c6/f0c6c1e4cf149269079d9b0a542d29c05fa790c9b3afe5e438697d51b456b3a2.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/F01132EN-04.pdf) |
| `F01132FR-03.pdf` | technical sheet | `/03`, updated `2013-03-01` | Full document, PDF pp. 1-3; `0 026 04` | [Archived original](https://archive.openwebnet-ha.org/sha256/44/c2/44c2f82aa9be266ec385f9219b996f343fac7b5c261d38fbf95287866121e667.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/F01132FR-03.pdf) |
| `LE03171AC.pdf` | installation / wiring sheet | revision `AC` | Full document, PDF pp. 1-2; `0 026 04` | [Archived original](https://archive.openwebnet-ha.org/sha256/67/a0/67a04907f1904828ce69f3599014c3a72aaeffc6a6259e9f0a158a3986567cb1.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE03171AC.pdf) |
| `LE04385AB_EN.pdf` | Push'n Learn technical guide | revision `AB`, 2014-07 | Full 10-page guide; programming workflow referenced by the `/03` sheet | [Archived original](https://archive.openwebnet-ha.org/sha256/1a/6d/1a6dc1f2007ad55b85f50fdede27c0fe3024dbcb1b45773254189e9aff6d8c78.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE04385AB_EN.pdf) |
| `LE04385AB_FR.pdf` | Push'n Learn technical guide | revision `AB`, 2014-07 | Full 10-page guide; French revision of the same workflow | [Archived original](https://archive.openwebnet-ha.org/sha256/fb/fb/fbfbd3e8d941aa3dd17f73097e4c4dbffbd29b8e9eb34b913ad5dffa05cb6fe9.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE04385AB_FR.pdf) |
| `LGRP-2013-015-V1-FR.pdf` | Product Environmental Profile | `V1-FR`, 2013-01 | Full document, PDF pp. 1-4; `0 026 04` | [Archived original](https://archive.openwebnet-ha.org/sha256/36/55/36558f262322d9a75109b71193fc3f0c7a7d7addb9e24bf75045057390a6e48d.pdf) | [Official source](https://assets.legrand.com/pim/DOCUMENT/LGRP-2013-015-V1-FR.pdf) |
| `MyHOME-Technical-Guide.pdf` | system / product guide | current archived revision, metadata 2025-06 | Printed p. 99 / PDF p. 99; `BMSW1005` identity, description and load table | [Archived original](https://archive.openwebnet-ha.org/sha256/a5/c9/a5c96905fdb4d86e833293da14f6e8e49f3b54c20ccf40203eca3def705c71d9.pdf) | [Official source](https://www.bticino.com/sites/default/files/2024-02/MyHOME%20Technical%20Guide.pdf) |
| `le10699ad-en.pdf` | BUS/SCS hotel / device guide | revision `AD`, 2019 | Printed/PDF p. 36; programming example printed/PDF p. 157 | [Archived original](https://archive.openwebnet-ha.org/sha256/02/bd/02bde8a8120d34ca8921a8ffeb82c725880b5e09b42888548561c18001d35607.pdf) | [Official source](https://assets.legrand.com/general/mediagrp/np-ft-gt/le10699ad-en.pdf) |
| `le10699aa-fr.pdf` | BUS/SCS hotel / device guide | revision `AA`, 2018 | Printed/PDF p. 24; programming example printed/PDF p. 103 | [Archived original](https://archive.openwebnet-ha.org/sha256/48/54/4854112b1d66d371515e11e1759d3a88d68cd2dad465a25c8799d55a74298d30.pdf) | [Official source](https://assets.legrand.com/general/mediagrp/np-ft-gt/le10699aa-fr.pdf) |
| `LE04280AA.pdf` | publisher-linked wiring sheet | revision `AA` | Publisher-linked from the `002604` product page, but the PDF itself depicts `0 026 02` / 4 x 16 A; excluded from Device-specific facts | [Archived original](https://archive.openwebnet-ha.org/sha256/94/7c/947c7c7db73629689e1858107d83ceea972e69af85d4066fbf22e7bd664ffb36.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE04280AA.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Outputs | `8` independent ON/OFF channels | dedicated sheets; MyHOME guide |
| Mains supply | `100..240 Vac`, `50/60 Hz` | `F01132EN-04`, `F01132FR-03`, `LE03171AC` |
| Output technology | relay switching with zero-current synchronisation / zero-crossing | dedicated sheets; later BUS/SCS guides |
| Per-output local control | one local control button per output; usable before configuration | dedicated sheets; BUS/SCS guides |
| BUS connection | `1 x RJ45` BUS/SCS connection | dedicated sheets |
| Supply terminals | `1` supply terminal block; screw terminals; input capacity `2 x 2.5 mm²` | `F01132EN-04` |
| Load terminals | `8` load terminal blocks; output capacity `2 x 1.5 mm²` or `1 x 2.5 mm²` | `F01132EN-04` |
| DIN width | `10` modules | dedicated sheets; MyHOME guide |
| Envelope / impact protection | `IP20` when installed in an enclosure; `IK04` | dedicated sheets |
| Operating temperature | `-5..+45 °C` | dedicated sheets |
| Storage temperature | `-20..+70 °C` | dedicated sheets |
| No-load consumption | `0.9 W` | dedicated sheets; BUS/SCS guides |
| Product weight | `310 g` | dedicated sheets |
| Packaged mass | `457 g` including unit packaging | `LGRP-2013-015-V1-FR` |
| Resistive / tungsten-halogen load at `230 V` | `3680 W / 16 A` per output | dedicated sheets; MyHOME guide |
| Linear fluorescent load at `230 V` | `10 x (2 x 36 W) / 4.3 A` per output | dedicated sheets; MyHOME guide |
| Separate transformer load at `230 V` | `3680 VA / 16 A` per output | dedicated sheets; MyHOME guide |
| Compact fluorescent load at `230 V` | `1150 VA / 5 A` per output | dedicated sheets; MyHOME guide |
| LED load at `230 V` | `1 x 500 VA / 2.1 A` per output | dedicated sheets; MyHOME guide |
| Single-phase requirement | all output contacts use the same supply phase; required for zero-current switching | `F01132EN-04`, `F01132FR-03`, `LE03171AC` |

The older dedicated sheets describe the contact as a bistable relay. The later BUS/SCS guides instead describe a normally-open monostable relay while also documenting status memory. This conflict is retained under Source reconciliation rather than normalized.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1156` | canonical catalogue |
| Technical item description | `DIN - Switch 8 x 16 A - 230V` | canonical catalogue |
| Main system | `lighting_automation` / Automation | canonical catalogue |
| Item model / `modobj` | `159` | canonical catalogue |
| Commercial records | `2` | canonical catalogue |
| Commercial codes | `002604`, `BMSW1005` | canonical catalogue and publisher sources |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `199` | `-1` | `-1` | `-1` | `8` | catalogue default | wildcard / unspecified firmware applicability |

The `-1.-1.-1` tuple is preserved as the catalogue sentinel for “any / unspecified” firmware applicability. No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

### Objects

| Firmware | Relation | Object | Description |
| --- | --- | --- | --- |
| `199` | Object/Firmware relation `506` | Object `6` | Light actuator |

### Module / slot relationships

| Slot | Catalogue slot ID | Object | Condition | Conversion rule |
| --- | --- | --- | --- | --- |
| `1` | `737` | `6` Light actuator | `4956` (empty condition expression) | `7206` |
| `2` | `738` | `6` Light actuator | `4937` (empty condition expression) | `7207` |
| `3` | `739` | `6` Light actuator | `4938` (empty condition expression) | `7208` |
| `4` | `740` | `6` Light actuator | `4957` (empty condition expression) | `7209` |
| `5` | `741` | `6` Light actuator | `4958` (empty condition expression) | `7210` |
| `6` | `742` | `6` Light actuator | `4959` (empty condition expression) | `7211` |
| `7` | `743` | `6` Light actuator | `4961` (empty condition expression) | `7212` |
| `8` | `744` | `6` Light actuator | `4962` (empty condition expression) | `7213` |

All eight slots are fixed to the same Light actuator Object. The distinct conversion rules preserve the channel-specific mapping; the empty condition expressions do not make the conversion rules interchangeable.

### Virgin Objects

| Firmware | Relation | Virgin Object | Description | Associated Objects |
| --- | --- | --- | --- | --- |
| `199` | - | - | No Virgin Object association is declared for the selected firmware | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Description |
| --- | --- | --- | --- |
| `199` | Virtual Configuration | `1` | software configuration route |
| `199` | Advanced Configuration | `2` | catalogue-declared advanced route |
| `199` | Physical configuration | `0` | physical configurator route |

The 2013 French sheet also documents Push'n Learn as a Lighting Management association procedure. That procedure is not represented as a separate firmware configuration-mode row in the canonical catalogue and disappears from the parameter-setting list of the 2017 English sheet.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` (configuration `2018`) | physical documentation: `1..9`; software uses Area `0..10` | catalogue-scoped | area / zone base |
| `G` (configuration `4065`) | physical documentation: `1..9` | catalogue-scoped | physical group number |
| `M` (configuration `2027`) | codes `0..4` select the documented standard/timed modes; `PUL` selects pushbutton behavior and `SLA` selects slave operation | catalogue-scoped | operating modality |
| `AID` (configuration `5441`) | catalogue-defined | catalogue-scoped | implementation ID |

Physical configuration has no `PL` configurator for this product. The published rule is that the eight actuator addresses are derived by incrementing the base address across outputs 1 through 8.

## Object configuration surfaces

### Object `6` - Light actuator

| Field | Domain / Device restriction | Default | Meaning |
| --- | --- | --- | --- |
| `A` | software documentation: `0..10`; physical base `1..9` | catalogue-scoped | Area |
| `PL` | software documentation: `0..15`; channel mapping must respect the eight fixed slots | catalogue-scoped | Light point |
| `M` | master/slave operation with pushbutton variants; physical forms use `PUL` for pushbutton and `SLA` for slave | catalogue-scoped | Modality |
| `LOCAL_BUTTON` | filter `1894`: `1` = `ON/OFF`; `9` = `ON-OFF`; `15` = `Pushbutton`; `18` = `Timed ON` | catalogue-scoped | Local button modality |
| `DELAYED_OFF` | software documentation: `0..255 s` where applicable | catalogue-scoped | Delayed OFF for Slave |
| `STATE_RESET` | filter `725`, whole reusable range retained | catalogue-scoped | Relay state on device reset / status memory |
| `LOAD_CONTROL_MODE` | filter `1870`, whole reusable range retained | catalogue-scoped | Load control mode |
| `HOURS` | filter `1895`, whole reusable range retained | catalogue-scoped | Hours |
| `MINUTES` | filter `1896`, whole reusable range retained | catalogue-scoped | Minutes |
| `SECONDS` | filter `1897`, whole reusable range retained | catalogue-scoped | Seconds |
| `SUBTYPE` | software types include actuator, lamp, valve, differential restart, fan, watering, controlled socket and lock | catalogue-scoped | Type of load |
| `G1` | software group slot 1; values `0..255`; up to 10 groups per output | catalogue-scoped | Group 1 |
| `G2` | software group slot 2; values `0..255`; up to 10 groups per output | catalogue-scoped | Group 2 |
| `G3` | software group slot 3; values `0..255`; up to 10 groups per output | catalogue-scoped | Group 3 |
| `G4` | software group slot 4; values `0..255`; up to 10 groups per output | catalogue-scoped | Group 4 |
| `G5` | software group slot 5; values `0..255`; up to 10 groups per output | catalogue-scoped | Group 5 |
| `G6` | software group slot 6; values `0..255`; up to 10 groups per output | catalogue-scoped | Group 6 |
| `G7` | software group slot 7; values `0..255`; up to 10 groups per output | catalogue-scoped | Group 7 |
| `G8` | software group slot 8; values `0..255`; up to 10 groups per output | catalogue-scoped | Group 8 |
| `G9` | software group slot 9; values `0..255`; up to 10 groups per output | catalogue-scoped | Group 9 |
| `G10` | software group slot 10; values `0..255`; up to 10 groups per output | catalogue-scoped | Group 10 |

Reusable Object `6` exposes a broader surface than the dedicated product sheets explain. Device relation filters `725`, `1870`, `1894`, `1895`, `1896`, and `1897` must be applied before presenting the reusable Object values as Device capability.

## Conditions, filters, and conversions

### Conditions and conversions

| Slot | Object | Condition | Conversion rule |
| --- | --- | --- | --- |
| `1` / `737` | `6` | `4956` - empty expression | `7206` |
| `2` / `738` | `6` | `4937` - empty expression | `7207` |
| `3` / `739` | `6` | `4938` - empty expression | `7208` |
| `4` / `740` | `6` | `4957` - empty expression | `7209` |
| `5` / `741` | `6` | `4958` - empty expression | `7210` |
| `6` / `742` | `6` | `4959` - empty expression | `7211` |
| `7` / `743` | `6` | `4961` - empty expression | `7212` |
| `8` / `744` | `6` | `4962` - empty expression | `7213` |

### Filters

| Object | Field | Filter / allowed subset | Evidence |
| --- | --- | --- | --- |
| `6` | `STATE_RESET` | filter `725`, whole range | canonical catalogue |
| `6` | `LOAD_CONTROL_MODE` | filter `1870`, whole range | canonical catalogue |
| `6` | `LOCAL_BUTTON` | filter `1894`: `1` ON/OFF; `9` ON-OFF; `15` Pushbutton; `18` Timed ON | canonical catalogue |
| `6` | `HOURS` | filter `1895`, whole range | canonical catalogue |
| `6` | `MINUTES` | filter `1896`, whole range | canonical catalogue |
| `6` | `SECONDS` | filter `1897`, whole range | canonical catalogue |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate catalogue item `1156` / `modobj = 159` identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | resolve the applicable firmware tuple while preserving wildcard `-1.-1.-1` semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate the eight fixed Light actuator Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect the eight incremented lighting addresses only after slot/Object context is known | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | compare runtime configuration with the `A/G/M/AID` firmware surface and Object restrictions | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The Device is an eight-channel lighting actuator in the Automation system and exposes Light actuator Object `6` on all eight fixed slots. Its primary functional surface is [Lighting](../../functional/who-1-lighting/README.md). Publisher material also positions it in Lighting Management and hotel-room BUS/SCS installations.

## Observed behavior and corroboration

No publishable Device-specific hardware capture is currently retained for this exact technical item. Publisher documentation does establish that local output buttons remain usable before configuration and that the zero-current-switching function requires the product supply and output contacts to use the same phase.

## Programming

Programming must preserve the eight fixed Light actuator channels and the distinction between physical, virtual, and advanced configuration. Physical configuration uses `A`, `G`, and `M`, derives the eight output addresses from the configured base, and does not use a separate `PL` configurator per channel. Software programming should resolve each output through its catalogue slot/Object relationship and Device-specific filters rather than treating reusable Object `6` as an unconstrained Light actuator surface.

Push'n Learn is documented by the earlier Lighting Management material but is omitted from the parameter-setting section of the 2017 English technical sheet, so it should be treated as revision-dependent rather than universally available.

## Source reconciliation

The canonical catalogue, dedicated technical sheets, later BUS/SCS guides, and current MyHOME guide agree that `002604 / 0 026 04` and `BMSW1005` are the same eight-output actuator and agree on the principal supply, form factor, BUS connection, zero-current switching, local controls, and load ratings. The `310 g` product mass in the technical sheets and the `457 g` packaged mass in the PEP have different scopes and are not contradictory.

The main revision difference concerns programming: the 2013 French sheet and 2014 EN/FR Push'n Learn guides document the manual association workflow, while the 2017 English sheet omits Push'n Learn from parameter setting. A separate publisher conflict remains unresolved: the dedicated `F01132` sheets describe a bistable relay, while the later `le10699AA/AD` guides describe a normally-open monostable relay and also document status memory. The catalogue's `STATE_RESET` surface supports configurable reset-state behavior but does not resolve the mechanical relay terminology.

`LE04280AA.pdf` is linked from the current `002604` product page but its content is for `0 026 02` / four outputs. It is retained in the archive for provenance and excluded from this Device's electrical and topology facts.

## Evidence limits and open work

- Capture a sanitized hardware fingerprint covering identity, firmware, all eight Modules, addresses and configuration.
- Resolve the publisher conflict between “bistable relay” in the dedicated sheets and “normally-open monostable relay” in the later BUS/SCS guides.
- The current BTicino generated product-sheet endpoint for `BMSW1005` was access-controlled/non-PDF during this run, so its binary was not archived; the current publisher catalogue page remains useful corroborating web evidence.
- `AID` is retained from the canonical implementation model, but the reviewed product PDFs do not give a Device-specific semantic explanation beyond the implementation label “ID”.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Lighting](../../functional/who-1-lighting/README.md)
