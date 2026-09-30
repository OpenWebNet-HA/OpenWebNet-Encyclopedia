# Two-channel universal dimmer

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0001` | Project identity |
| Technical description | Two-channel universal dimmer, 4 DIN modules | Catalogue + vendor documentation |
| Commercial identities | BTicino `F418U2`; Legrand `0 036 51` / catalogue `003651` | Catalogue + vendor documentation |
| Catalogue item | `2065` - “2x1,6A universal dimmer, 4DIN” | Implementation evidence |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `77` | Implementation evidence |
| Catalogue brand / line | `BRAND = 5`; `LINE = 0` | Implementation evidence |
| Firmware definition | `1.0.5` (`EN_FIRMWARE 590`) | Implementation evidence |
| Declared Modules | 2 | Implementation evidence |
| Categories | Actuator, Lighting, Dimmer | Derived from capability model |

The F418U2 is a two-channel SCS universal dimmer. The official technical sheet identifies `F418U2` and `0 036 51` on the same document, while MyHOME Suite stores `F418U2` and `003651` as separate Device records sharing item `2065`. They are therefore treated as commercial identities of this technical Device definition.

## Commercial identities

| Brand / range | SKU / reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino MyHOME | `F418U2` | Established commercial identity | Catalogue + vendor technical sheet |
| Legrand | `0 036 51` / `003651` | Equivalent commercial reference | Same vendor technical sheet + same catalogue item |

No preference between these references is implied by the Device ID.

## Documentation

The source archive should retain every distinct revision found for this Device. The following official material is currently known:

| Document | Type | Revision / date | Status | Source |
| --- | --- | --- | --- | --- |
| `MQ01019_a_EN` - Universal dimmer 2x300W | Technical sheet | 20/09/2018 | [Archived original](../../sources/devices/documents/device-doc-f418u2-mq01019-en/MQ01019_a_EN.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ01019_a_EN.pdf) |
| `LE07383AB` | Instruction sheet | Current BTicino catalogue listing | [Archived original](../../sources/devices/documents/device-doc-f418u2-le07383ab/LE07383AB.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE07383AB.pdf) |
| `LE07383AC` | Instruction sheet | Historical revision | [Archived original](../../sources/devices/documents/device-doc-f418u2-le07383ac/LE07383AC.pdf) | [Official source](https://dar.bticino.com/asset/Documents/LE07383AC.pdf) |
| `LE07383AD` | Instruction sheet | 07/23 | [Archived original](../../sources/devices/documents/device-doc-f418u2-le07383ad/LE07383AD.pdf) | [Official source](https://dar.bticino.com/asset/Documents/LE07383AD.pdf) |
| `ST-00001620-EN` | Technical sheet | Current BTicino catalogue listing | [Archived original](../../sources/devices/documents/device-doc-f418u2-st00001620-en/ST-00001620-EN.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00001620-EN.pdf) |
| `GUI-MHOME` | MyHOME installation guide | Current BTicino catalogue listing | Official source identified, archival copy pending | [BTicino product page](https://www.bticino.com/products/bt-f418u2) |

See the [Device Source Index](../../sources/devices/index.md) for archival status and provenance.

## Physical and electrical characteristics

The 2018 technical sheet establishes the following product-specific characteristics:

| Property | Value | Evidence |
| --- | --- | --- |
| Width | 4 DIN modules | Vendor technical sheet |
| SCS supply | `18..27 Vdc` | Vendor technical sheet |
| SCS absorption | max. `18 mA` | Vendor technical sheet |
| Mains supply | `110..127 Vac` or `220..240 Vac`, `50..60 Hz` | Vendor technical sheet |
| Device consumption | max. `5 W` | Vendor technical sheet |
| Operating temperature | `0..40 °C` | Vendor technical sheet |
| Channels | 2, with parallel operation supported by the product documentation | Vendor technical sheet |
| Nominal channel load at `220..240 V` | up to `300 W` per channel | Vendor technical sheet |
| Parallel load at `220..240 V` | up to `600 W` | Vendor technical sheet |
| Load families | dimmable LED, dimmable CFL, halogen, electronic transformers | Vendor technical sheet |
| Local operation | local channel pushbuttons | Vendor technical sheet |

The current BTicino product page also lists the Device as a 4-module, 27 Vdc MyHOME dimmer with an 18 mA bus current. Historical and current documents should both be preserved because product-sheet wording and supported-load guidance can change between revisions.

### Revision-specific hardware evidence

Later instruction sheet `LE07383AD` introduces material that must remain revision-scoped:

- Devices from production batch `23W16` use a revised light-level adjustment and may produce different brightness levels from earlier production batches at the same nominal setting.
- Its load table differs from the older 2018 `MQ01019_a_EN` technical sheet, including lower printed per-channel wattage/VA figures for the shown supply cases.
- The current BTicino catalogue page contains structured metadata that can conflict with its own narrative description, so generic catalogue fields must not override Device-specific technical documentation.

These differences are archival evidence that F418U2 documentation and product behavior changed over time. Do not collapse the revisions into one timeless specification.

## Identity

### Catalogue identity

| Field | Value | Evidence state |
| --- | --- | --- |
| `EN_DEVICE.code` | `F418U2` / sibling `003651` | Implementation evidence |
| `EN_ITEM.id_item` | `2065` | Implementation evidence |
| `EN_ITEM.descr` | “2x1,6A universal dimmer, 4DIN” | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `77` | Implementation evidence |
| `EN_BRAND.brand_modobj` | `5` | Implementation evidence |
| `EN_LINE.line_modobj` | `0` | Implementation evidence |

For the ordinary addressed identity mechanism, these catalogue values are the product-specific values to resolve through [`DIMENSION 1` Device Identity](../../diagnostics/dim1-device-identity.md). The generic frame grammar and field ranges are intentionally not duplicated here.

### Firmware identity

The canonical catalogue contains one firmware definition for item `2065`:

| Catalogue firmware | Version | Build | Slots | Default flag | Evidence |
| --- | --- | --- | ---: | ---: | --- |
| `590` | `1.0` | `5` | 2 | 0 | `MHCatalogue.db` |

This is catalogue applicability data. It does not by itself prove that every physical F418U2 reports `1.0.5`.

Firmware, hardware, microcontroller, and Device ID reads use the canonical [Diagnostic Dimension Reference](../../diagnostics/dimension-reference.md). Observed values should be added as corroborating evidence without replacing the catalogue definition.

## Module and Object model

Firmware `590` declares two Modules.

| Object | Description | Slots | Relationship | Evidence |
| --- | --- | --- | --- | --- |
| `8` | Dimmer actuator | `1`, `2` | designated / fixed Object | Implementation evidence |
| `136` | Double Dimmer actuator | `1` | alternative Object | Implementation evidence |
| Virgin Object `528` | Dimmer actuator virgin | `1`, `2` | permits Objects `8` and `136` | Implementation evidence |

The installed Module/Object projection is obtained through [`DIMENSION 30`](../../diagnostics/dim30-modules.md). The generic `SLOT`, `KEYO`, and `STATE` frame semantics remain canonical there.

## Configuration modes

The catalogue associates firmware `590` with all three configuration modes:

- Physical configuration
- Virtual Configuration
- Advanced Configuration

The vendor technical sheet independently documents physical configuration and MyHOME Suite configuration.

## Firmware-scoped configuration

These are the complete firmware-scoped configuration fields stored for firmware `590`, excluding only database bookkeeping columns.

| Field | Progressive | Type | Catalogue domain | Product-document interpretation | Evidence |
| --- | ---: | --- | --- | --- | --- |
| `AID` | 0 | user value | Device ID field | not a physical configurator | Implementation evidence |
| `A` | 1 | zone / room address | `0..9` | physical `A=1..9`; virtual room `0..10` | Catalogue + vendor PDF |
| `PL1` | 2 | point-to-point address | `0..9` | physical `PL1=1..9`; virtual `0..15` | Catalogue + vendor PDF |
| `PL2` | 3 | point-to-point address | `0..9` | physical `PL2=0..9`; virtual `0..15` | Catalogue + vendor PDF |
| `M` | 4 | mode enum | `0,1,2,3,4,11=SLA,15=PUL` | Master, delayed ON modes, Slave, Master PUL | Catalogue + vendor PDF |
| `G` | 5 | group | `0..9` | physical `0..9`; virtual group `0..255` | Catalogue + vendor PDF |
| `TY` | 6 | enum | `0..3` | per-channel leading/trailing-edge load selection | Catalogue + vendor PDF |
| `MIN1` | 7 | enum | `0..9` | channel 1 minimum level selector | Catalogue + vendor PDF |
| `MIN2` | 8 | enum | `0..9` | channel 2 minimum level selector | Catalogue + vendor PDF |

The catalogue includes `0` in the stored physical ranges for `A` and `PL1`, while the 2018 technical sheet prints `A=1..9` and `PL1=1..9`. Preserve this as a source-level difference rather than silently reconciling the domains.

### Physical mode `M`

| Stored value | Vendor label / effect | Evidence |
| ---: | --- | --- |
| `0` | Master | Catalogue + vendor PDF |
| `1` | Master with delayed switch-off, 1 minute | Vendor PDF |
| `2` | Master with delayed switch-off, 2 minutes | Vendor PDF |
| `3` | Master with delayed switch-off, 3 minutes | Vendor PDF |
| `4` | Master with delayed switch-off, 4 minutes | Vendor PDF |
| `11` / `SLA` | Slave | Catalogue + vendor PDF |
| `15` / `PUL` | Master PUL | Catalogue + vendor PDF |

Virtual configuration exposes the delayed-off value as a Device/Object parameter rather than restricting it to the four physical presets.

### Physical load selector `TY`

| `TY` | Channel 1 | Channel 2 | Evidence |
| ---: | --- | --- | --- |
| `0` | leading edge | leading edge | Vendor PDF |
| `1` | trailing edge | trailing edge | Vendor PDF |
| `2` | leading edge | trailing edge | Vendor PDF |
| `3` | trailing edge | leading edge | Vendor PDF |

### Physical minimum-level selectors

| Selector value | Minimum level | Evidence |
| ---: | ---: | --- |
| `0` | default, 10% in the 2018 sheet | Vendor PDF |
| `1` | 1% | Vendor PDF |
| `2` | 5% | Vendor PDF |
| `3` | 10% | Vendor PDF |
| `4` | 15% | Vendor PDF |
| `5` | 20% | Vendor PDF |
| `6` | 25% | Vendor PDF |
| `7` | 30% | Vendor PDF |
| `8` | 35% | Vendor PDF |
| `9` | 40% | Vendor PDF |

The vendor sheet makes `MIN2` conditional on the second channel configuration and parallel-channel use. Preserve those conditions when producing a future programmer or validator.

## Object configuration surface

Objects `8` and `136` expose the same catalogue configuration surface in the canonical database. These are reusable Object definitions; the table records the complete candidate surface, while Device/firmware filters and vendor documentation determine which values are meaningful for F418U2.

| Parameter | Catalogue values | Notes |
| --- | --- | --- |
| `A` | `0..10` | area |
| `PL` | `0..15` | light point |
| `M` | `0=Master`, `11=Slave`, `15=Master PUL`, `16=Slave and PUL` | actuator mode |
| `LOCAL_BUTTON` | `0=Toggle`, `9=ON-OFF`, `15=Pushbutton`, `18=Timed ON` | local button behavior |
| `DELAYED_OFF` | `0..255 s` | hidden implementation parameter |
| `STATE_SAVING_ON_RESET` | `0=Disabled`, `1=Enabled` | reset behavior |
| `HOURS` | `0..255` | hidden timed-operation component |
| `MINUTES` | `0..59` | hidden timed-operation component |
| `SECONDS` | `0..59`, default `30` | hidden timed-operation component |
| `MIN_LEVEL` | `1..100`, default `1` | minimum level |
| `TYPE_LOAD` | reusable enum values `0,1,2,3,5..14` | candidate Object-level load taxonomy |
| `TYPE_STANDARD` | `0=1-10V`, `1=0-10V` | reusable Object-level field |
| `MIN_LEVEL_ADV` | `1..100` | hidden advanced minimum level |
| `MIN_AUTO` | `0=not editable`, `1=editable` | minimum-level editability |
| `G1..G10` | each `0..255` | group memberships |

The reusable `TYPE_LOAD` Object enum includes load technologies beyond those documented for F418U2. Do not promote every reusable Object value to a product capability. The F418U2 technical sheet is the stronger product-specific evidence for its supported load families.

## Diagnostic applicability

The Device-specific knowledge above projects through the general diagnostic model:

| Diagnostic surface | F418U2-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | identify item model `77`, brand `5`, line `0`; obtain installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | obtain installed firmware version | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | obtain hardware version when supported | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | obtain microcontroller version when supported | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 13` | obtain physical Device ID | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | enumerate the two installed Modules and active Objects | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | obtain configured Module addresses | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | obtain configuration values | [Configuration](../../diagnostics/dim35-configuration.md) |

The table documents applicability and Device-specific expectations. Frame grammar and generic field semantics belong to the linked reference pages.

## Functional behavior and corroboration

F418U2 is a `WHO 1` Lighting dimmer. General commands, addressing, and dimension grammar are documented under [Lighting](../../functional/who-1-lighting/).

First-hand evidence already adds several Device-specific observations:

- `DIMENSION 1` and functional `DIMENSION 4` are distinct state surfaces on the tested F418U2 even when they report the same `LEVEL100`;
- at `LEVEL100 = 130`, observed trailing values differed between those two dimensions;
- through MH202, explicit reads of both dimensions were observed;
- through F454, an OFF-state `DIMENSION 1` request was observed to return a `DIMENSION 4` frame;
- through an MH200 running firmware 2.1.0, the preserved public trace shows working `DIMENSION 1` reads/writes while explicit `DIMENSION 4` requests received no response in the captured windows.

These observations corroborate runtime behavior but do not change the canonical generic frame definitions. See [`WHO 1` Dimensions](../../functional/who-1-lighting/dimensions.md) and the [Open Questions](../../reverse-engineering/open-questions.md).

## Programming

F418U2 programming should use the canonical [Programming](../../programming/) workflow. The Device-specific data required by a validator is captured above:

- two-slot firmware topology;
- allowed Object alternatives;
- physical configuration fields and domains;
- reusable Object parameter domains;
- product-document constraints on channel configuration, loads, and minimum levels.

Generic `DIMENSION` write syntax and validation sequencing belong in [Configuration Programming](../../programming/configuration-programming.md) and [Programming Validation](../../programming/validation.md).

## Source reconciliation

Known F418U2 product documentation and runtime research have been reconciled as follows:

- the local channel pushbuttons are Device controls, not additional OpenWebNet Modules; their status/fault indication belongs to the product-level behavior of the two dimmer channels;
- vendor documentation distinguishes normal status from load/fault and configuration indications on the front LEDs and documents a Device-level two-channel setup path in the MyHOME Server tooling;
- group configuration is not a legal physical interpretation of Slave operation, and the second channel inherits product constraints from the selected channel/load arrangement rather than being an unconstrained duplicate;
- later instruction material warns against mixing incompatible load technologies and keeps minimum-level/load-type behavior revision-scoped;
- the runtime `DIMENSION 4` evidence remains Device-specific and unresolved in four places: the exact `ON/OFFspeed` encoding, whether the observed F454 positive write failure is systematic, whether MH200 non-response is gateway/firmware-wide or interaction-specific, and whether the reported F414/MH200 timeout followed by `NACK` can be reproduced from a preserved raw exchange.

Five identified F418U2-specific official PDFs are now archived byte-for-byte and reconciled here: `MQ01019_a_EN`, `LE07383AB`, `LE07383AC`, `LE07383AD`, and `ST-00001620-EN`. The separately listed `GUI-MHOME` is a system-wide MyHOME installation guide rather than a Device-specific F418U2 revision; its exact publisher binary remains unresolved, but no additional F418U2-specific fact has been identified that is absent from the archived Device sheets. Source reconciliation is therefore complete for the currently identified Device-specific PDF set while generic-guide archival remains open.

## Evidence limits and open work

- Recover and archive the exact `GUI-MHOME` publisher binary if its download endpoint becomes available; treat it as generic system documentation unless it adds F418U2-specific facts.
- Add a sanitized fingerprint capture from a known physical F418U2 so installed identity, firmware, hardware, Module/Object state, addresses, and configuration can be tied to one evidence record.
- Resolve the source-level `A` / `PL1` physical-domain difference between catalogue data and the 2018 technical sheet.
- Preserve production-batch-specific behavior from later instruction sheets as revision-scoped product evidence rather than generalizing it backwards.
- Determine which reusable Object configuration values are filtered out specifically for firmware `590`.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Physical Devices](../../device-model/physical-devices.md#f418u2)
- [Firmware](../../device-model/firmware.md)
- [Virgin Objects](../../device-model/virgin-objects.md#dimmer-actuator-virgin)
- [`WHO 1` Dimensions](../../functional/who-1-lighting/dimensions.md)
