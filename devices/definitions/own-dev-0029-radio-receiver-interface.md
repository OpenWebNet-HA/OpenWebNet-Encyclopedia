# Radio receiver interface

## Summary

This radio receiver converts compatible 868 MHz wireless controls into SCS bus actions. Configured functions include sound-system switching, volume and source selection, with other roles determined by the selected operating mode.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0029` | Project identity |
| Technical description | Flush-mounted 868 MHz radio-to-SCS receiving interface | Catalogue + official documentation |
| Commercial identities | `HC/HS/HD4575`, `L/N/NT4575`, `L/N/NT4575N` | Catalogue |
| Catalogue item | `28` - “Receiving radio interface” | Canonical manufacturer catalogue |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Canonical manufacturer catalogue |
| Item model / `modobj` | `20` | Canonical manufacturer catalogue |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `214` | Canonical manufacturer catalogue |
| Declared Modules | `1` | Canonical manufacturer catalogue |
| Categories | Radio interface, Control bridge | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC/HS/HD4575` | Established identity | Canonical catalogue; canonical commercial record `28`; Commercial identity of this Technical Device |
| BTicino - LivingLight | `L/N/NT4575` | Established identity | Canonical catalogue; canonical commercial record `1839`; Commercial identity of this Technical Device |
| BTicino - LivingLight | `L/N/NT4575N` | Established identity | Canonical catalogue; canonical commercial record `1840`; Commercial identity of this Technical Device |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `mh_diff-sonore2008.pdf` | Radio/wired interface and sound-system technical guide | historical publisher guide | 4575 radio/wired interface: printed p. 99 / PDF p. 99; installation/configuration context printed pp. 60-61 / PDF pp. 60-61 and 66-67 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/f4/96/f496f0943750657477c03e43eae6708271a8e798101831991ebc02904673dccd.pdf) | [Publisher PDF](https://assets.legrand.com/general/cession/bt/np-ft-gt/mh_diff-sonore2008.pdf) |
| `livinglight-historical-catalogue.pdf` | Spanish LivingLight catalogue | January 2012 page imprint | Applicable L/N/NT family descriptions only; printed p.83 /PDF p.85 | [Archived original](https://archive.openwebnet-ha.org/sha256/db/75/db75d0071e27ea0904973b8ebaa936334347e3646135884b7b7081e110a3f414.pdf) | [Publisher source](https://www.bticino.es/pdf/livinglight.pdf) |
| `AUTOMATISME.pdf` | MyHOME automation guide | October 2006 | Receiver setup printed pp.152–154 /PDF pp.154–156; consumption p.161 /PDF p.163; technical p.173 /PDF p.175 | [Archived original](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | Publisher URL not retained in manifest |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply | `27 Vdc` | `mh_diff-sonore2008.pdf` |
| Radio frequency | `868 MHz` | `mh_diff-sonore2008.pdf` |
| Published current draw | `2 mA` for the documented `L/N/NT4575N` and `HC/HS4575` variants | `mh_diff-sonore2008.pdf` |
| Mounting | 2 wiring-device modules | `mh_diff-sonore2008.pdf` |
| Operating temperature | `5..35 °C` | `mh_diff-sonore2008.pdf` |
| Service interface | status LED and programming micro-button | `mh_diff-sonore2008.pdf` |
| Bus connection | SCS BUS connector | `mh_diff-sonore2008.pdf` |

| Setting / property | Source-scoped value or behavior | Evidence |
| --- | --- | --- |
| Alternative guide ratings | Automation guide: −`5..35` °C, `22 mA` maximum, `100m` open-field range. Its consumption table instead gives `18 mA` for HC/HS4575 and L/N/NT4575N. Walls, metal and concrete reduce range. | AUTOMATISME.pdf printed pp.161, 173 /PDF pp.163, 175 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `28` | Canonical catalogue |
| Technical item description | Receiving radio interface | Canonical catalogue |
| Item family | `27` - Radio device | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `20` | `AS_ITEM_SYSTEM` |
| Commercial records | `3` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `20` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Canonical commercial record metadata

| Reference / record | Catalogue name / source description | Visibility / type | Dependent / gateway | Evidence |
| --- | --- | --- | --- | --- |
| `HC/HS/HD4575` / `28` | Receiving radio interface; no source description | `1` / Empty | `0` / `0` | Canonical manufacturer catalogue |
| `L/N/NT4575` / `1839` | Receiving radio interface; no source description | `1` / Empty | `0` / `0` | Canonical manufacturer catalogue |
| `L/N/NT4575N` / `1840` | Receiving radio interface; no source description | `1` / Empty | `0` / `0` | Canonical manufacturer catalogue |

Visibility, dependency and gateway flags describe the catalogue record, not the installed Device state.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `214` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Firmware `214` is wildcard `-1.-1.-1` and declares one Module.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `214` | `1` | `27` Radio receiver | Fixed/designated metadata | `1010` | `27` | `607` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

The single Module resolves to Object `27`, **Radio receiver**. No Virgin Object is declared for this firmware.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `214` | Physical configuration | `0` | Canonical firmware/mode association |
| `214` | Virtual Configuration | `1` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `214` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `214` | `A` | `0..9` | `0` | A; Environment |
| `214` | `PL` | `0..9` | `0` | PL; Light Point |
| `214` | `M` | `0..1`; `6..8`; `14` = `CEN` | `0` | M; Mode (0, 1, 6, 7, 8,`CEN`) |

The firmware exposes only `A`, `PL`, `M` and `AID`. The reusable radio-receiver Object uses the corresponding `MOD` concept.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `27` - Radio receiver

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..9` | `0` | Area |
| `PL` | `0..9` | `0` | Light point |
| `MOD` | `1`; `6..8`; `14` = `CEN` | `1` | Modality; Mode (1, 6, 7, 8,`CEN`) |

### Device-specific interpretation

The firmware M enum stores 0/1/`6..8`/CEN; the automation guide documents self-learning, physical extension and F420 scenarios for those numeric selectors. CEN’s emitted behavior is not established by these guides. No relation-specific filters, conversions or Virgin association are stored.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | - | None | - | No relation-specific filters associated | - | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 20` and the 4575 radio-interface family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | record installed firmware rather than assuming wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm the single Radio-receiver Object | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the configured SCS-side address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `A`, `PL`, `M` and Device-specific radio/contact configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The official documentation shows that the receiver can translate radio controls into SCS functions. A sound-system guide specifically documents amplifier on/off, volume, source selection and radio-station/track changes when appropriately configured. Other configured modes must be interpreted from their own functional context.

## Observed behavior and corroboration

No sanitized first-hand capture for this exact receiver is currently retained.

## Programming

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| `M=1` physical extension | One receiver per installation; transmitter 4576 permitted only also `M=1`. A/PL separates wired lower addresses from radio higher addresses; example receiver 61 sends destinations below 61 to bus. Use radio controls with address configurators. Up to 128 radio codes. | AUTOMATISME.pdf printed p.152 /PDF p.154 |
| `M=0` self-learning | Multiple receivers allowed; no 4576 transmitter. `A=0..9`, `PL=1..9`; associate individual 3527 keys with cyclic/dimmer, timed ON, flashing, up/down stop, lock/unlock, scenario or named AUX functions. Up to 18 learned functions (three six-key remotes). | Same guide printed p.153 /PDF p.155 |
| `M=6/7/8` F420 scenarios | Match F420 A/PL. Six keys map to scenarios `1..6` /`7..12` /`13..16` (last bank only four). Up to 20 similar remotes; guide also states 128 codes. F420 learning must be enabled. | Same guide printed p.154 /PDF p.156 |
| Pair / learn | Hold microbutton 3 s until red LED; press transmitter key within 20 s. Physical extension flashes confirmation. `M=0` then operate desired bus command within 5 min; `M=6..8` configure scene actions and press microbutton to finish. | Same guide pp.152–154 |
| Erase | Hold 8 s, release, press unwanted remote key within 20 s to remove one association. Hold about 12 s to clear interface associations. This does not erase F420 scenes; F420 DEL for 10 s handles its own memory with learning enabled. | Same guide pp.152–154 |
| Battery-free exclusion | 4572SB requires its dedicated 4575SB interface; ordinary 4575 receiver is excluded. SB is a distinct product, not another firmware mode of this cluster. | Same guide printed p.173 /PDF p.175 |

## Source reconciliation

The sound guide printed/PDF p.99 states 2 mA and `+5..35 °C` for HC/HS4575 and L/N/NT4575N. The automation guide printed p.173 /PDF p.175 gives 22 mA maximum and `−5..35 °C`, while its printed p.161 /PDF p.163 table gives 18 mA. These incompatible figures are retained by source; no revision or measurement condition resolves them. The automation guide’s three setup roles are established separately from sound functionality (sound guide p.83). Spanish LivingLight catalogue printed p.83 /PDF p.85 corroborates the N-suffix radio-to-sound role. Catalogue HD4575 and unsuffixed L/N/NT4575 relationships establish identity without separately establishing those variants’ ratings. The guessed MQ00101_b_EN endpoint returned 403 and contributed no evidence.

The firmware `M` domain includes `0` with default `0`, but reusable Object `27` field `MOD` omits `0` and defaults to `1`. The guide documents self-learning `M=0`; no conversion or alias establishes how that physical mode projects into Object `MOD`. Preserve the discrepancy rather than declaring those fields equivalent.

## Evidence limits and open work

- Add sanitized hardware and pairing traces.
- Recover dedicated documentation for the catalogue-only `HD4575` and `L/N/NT4575` forms if distinct publisher sheets exist.
- Map each `M/MOD` value to verified emitted OpenWebNet behavior.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [mh_diff-sonore2008.pdf](https://archive.openwebnet-ha.org/sha256/f4/96/f496f0943750657477c03e43eae6708271a8e798101831991ebc02904673dccd.pdf)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0021-0030-2026-10-06.md#own-dev-0029)
