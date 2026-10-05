# Rotary regulation control

## Summary

This flush-mounted rotary SCS control combines a central pushbutton with a knob for adjustment. In the documented sound-system configuration, it switches the amplifier, adjusts volume and changes the selected radio station or track; the active function follows its configuration.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0028` | Project identity |
| Technical description | Flush-mounted rotary SCS control | Catalogue + official documentation |
| Commercial identities | `HC/HS/HD4563`, `L/N/NT4563` | Catalogue |
| Catalogue item | `25` - “Regulation rotative control” | Canonical manufacturer catalogue |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Canonical manufacturer catalogue |
| Item model / `modobj` | `11` | Canonical manufacturer catalogue |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `213` | Canonical manufacturer catalogue |
| Declared Modules | `1` | Canonical manufacturer catalogue |
| Categories | Control, Lighting/Automation command, Sound | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC/HS/HD4563` | Established identity | Canonical catalogue; canonical commercial record `25`; Commercial identity of this Technical Device |
| BTicino - LivingLight | `L/N/NT4563` | Established identity | Canonical catalogue; canonical commercial record `1838`; Commercial identity of this Technical Device |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `mh_diff-sonore2008.pdf` | Two-wire sound-system technical guide | October 2006 publisher guide | 4563 rotary-control specification: printed p. 100 / PDF p. 100; sound-function configuration context printed p. 83 / PDF p. 83 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/f4/96/f496f0943750657477c03e43eae6708271a8e798101831991ebc02904673dccd.pdf) | [Publisher PDF](https://assets.legrand.com/general/cession/bt/np-ft-gt/mh_diff-sonore2008.pdf) |
| `AUTOMATISME.pdf` | MyHOME automation guide | October 2006 publisher guide | No 4563-family reference found in this retained guide; generic system context only, not Device-specific specification evidence | [Archived PDF](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |
| `livinglight-historical-catalogue.pdf` | Spanish LivingLight catalogue | January 2012 page imprint | Applicable L/N/NT family descriptions only; printed pp.69, 82 /PDF pp.71, 84 | [Archived original](https://archive.openwebnet-ha.org/sha256/db/75/db75d0071e27ea0904973b8ebaa936334347e3646135884b7b7081e110a3f414.pdf) | [Publisher source](https://www.bticino.es/pdf/livinglight.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 wiring-device modules | `mh_diff-sonore2008.pdf` |
| SCS operating supply | `18..27 Vdc` | `mh_diff-sonore2008.pdf` |
| Maximum current draw | `5 mA` | `mh_diff-sonore2008.pdf` |
| Operating temperature | `5..35 °C` | `mh_diff-sonore2008.pdf` |
| Local interface | central pushbutton plus rotary knob | `mh_diff-sonore2008.pdf` |
| Published local actions | `ON`/`OFF`, programmed radio-station or track change, and volume adjustment | `mh_diff-sonore2008.pdf` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `25` | Canonical catalogue |
| Technical item description | Regulation rotative control | Canonical catalogue |
| Item family | `1` - Control | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `11` | `AS_ITEM_SYSTEM` |
| Commercial records | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `11` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Canonical commercial record metadata

| Reference / record | Catalogue name / source description | Visibility / type | Dependent / gateway | Evidence |
| --- | --- | --- | --- | --- |
| `HC/HS/HD4563` / `25` | Regulation rotative control; `BTicino_Axolute_Regulation rotative control` | `1` / Empty | `0` / `0` | Canonical manufacturer catalogue |
| `L/N/NT4563` / `1838` | Regulation rotative control; no source description | `1` / Empty | `0` / `0` | Canonical manufacturer catalogue |

Visibility, dependency and gateway flags describe the catalogue record, not the installed Device state.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `213` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Firmware `213` is wildcard `-1.-1.-1` with one Module.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `213` | `1` | `451` Knob control | Fixed/designated metadata | `1009` | `451` | `606` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

The Module resolves to Object `451`, **Knob control**, a one-slot Object associated with Automation and the relevant command-control collections. No Virgin Object is declared for this firmware.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `213` | Physical configuration | `0` | Canonical firmware/mode association |
| `213` | Virtual Configuration | `1` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `213` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `213` | `A` | `0..9` | `0` | A; Environment |
| `213` | `PL` | `0..9` | `0` | PL; Light Point |
| `213` | `M` | `0`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `14` = `CEN`; `15` = `PUL` | `0` | M; Mode cmd (`O/I`,`OFF`,`ON`,`PUL`, SU_GIU, SU_GIU_M) |
| `213` | `LIV1` | `0..99` | `1` | LIV1; Configurator LIV1 |
| `213` | `LIV2` | `0..99` | `1` | LIV2; Configurator LIV2 |
| `213` | `SPE` | `0..9` | `0` | SPE; Special function command control (0-9) |
| `213` | `I` | `0`; `14` = `CEN` | `0` | I; Configurator I |

`LIV1` / `LIV2` are the two regulation-level fields. `SPE` and `I` are additional command selectors whose semantics depend on the selected operating mode.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `451` - Knob control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..9` | `0` | Area |
| `PL` | `0..9` | `0` | Light point |
| `M` | `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `14` = `CEN`; `15` = `PUL`; `0` = None | `0` | Modality; Mode cmd (`O/I`,`OFF`,`ON`,`PUL`, SU_GIU, SU_GIU_M) |
| `LIV1` | `0..99` | `1` | Configurator LIV1 |
| `LIV2` | `0..99` | `1` | Configurator LIV2 |
| `SPE` | `0..9` | `0` | Special function command control (0-9) |
| `I` | `0` = None; `14` = `CEN` | `0` | Configurator I |

### Device-specific interpretation

Firmware LIV1/LIV2 `0..99` with default 1 is wider than the sound guide’s physical LIV1 absent/`1..9` and LIV2 absent. `SPE=1` selects sound in that guide; the Spanish catalogue independently documents advanced dimmer control. No filter or conversion supplies a complete physical matrix for every reused mode.

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
| `DIMENSION 1` | resolve `modobj = 11` and the 4563 rotary-control family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | record installed firmware rather than assuming wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm the single Knob-control Object | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the configured control address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `M`, `LIV1`, `LIV2`, `SPE` and `I` together with the address fields | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The selected command mode determines the functional command emitted. The dossier therefore does not collapse the Device to a single lighting action without first resolving configuration.

## Observed behavior and corroboration

No sanitized hardware fingerprint or first-hand command trace is currently retained for this exact family.

## Programming

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Sound selector | `SPE=1`; I and LIV2 absent. Point `A=1..9`, `PL=0..9`, room `A=AMB`, `PL=0..9`, general `A=GEN`, PL unused. | mh_diff-sonore2008.pdf printed/PDF p.83 |
| Startup source / volume | M absent follows last active source; `M=1..4` selects source first. LIV1 absent restores saved volume, `1..9` sets startup level. | Same guide p.83 |
| Local operation | Central button ON/OFF and station/track change; rotary volume. The selected function determines command interpretation. | Same guide printed/PDF p.100 |
| Lighting role | LivingLight L/N/NT4563 also provides advanced dimmer adjustment `1..99`%, soft-start, central ON/OFF. This does not supply a complete physical selector matrix. | livinglight-historical-catalogue.pdf printed p.69 /PDF p.71 |

## Source reconciliation

The sound guide explicitly names HC/HS/L/N/NT4563 and supplies the physical sound settings and ratings (printed/PDF pp.83, 100). HD4563 identity is established by the catalogue but is not separately named in those electrical paragraphs. The Spanish LivingLight catalogue printed pp.69, 82 /PDF pp.71, 84 independently documents L/N/NT4563 lighting and sound uses. Thus lack of a dedicated sheet does not erase retained exact-family evidence. Firmware LIV1/LIV2 are broader than the published sound setup; unexamined mode combinations remain outside confirmed physical behavior.

## Evidence limits and open work

- A dedicated 4563 technical sheet and exact HD electrical corroboration remain unretained.
- The complete lighting selector matrix and runtime meaning of every broader LIV1/LIV2/SPE/I combination are not established; retained sound-mode selectors are explicit above.
- No hardware fingerprint or emitted-command trace has been inspected. Linked regional manuals outside the retained rows remain unexamined.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0021-0030-2026-10-06.md#own-dev-0028)
