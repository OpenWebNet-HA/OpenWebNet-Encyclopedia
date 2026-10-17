# Four-scenario control unit

## Summary

This wall-mounted scenario control unit provides four buttons with indicator LEDs for recalling configured groups of actions. Its master/slave configuration determines how it participates in the installation's scenario system.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0026` | Project identity |
| Technical description | Flush-mounted four-scenario control and storage unit | Catalogue + official documentation |
| Commercial identities | `N4681` | Catalogue |
| Catalogue item | `20` - “Scenario control unit” | Canonical manufacturer catalogue |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Canonical manufacturer catalogue |
| Item model / `modobj` | `4` | Canonical manufacturer catalogue |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `223` | Canonical manufacturer catalogue |
| Declared Modules | `1` | Canonical manufacturer catalogue |
| Categories | Scenario control, Automation | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - LivingLight | `N4681` | Established identity | Canonical catalogue; canonical commercial record `20`; Commercial identity of this Technical Device |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `AUTOMATISME.pdf` | MyHOME automation guide | October 2006 publisher guide | N4681 scenario configuration and restrictions: printed pp. 103–105 / PDF pp. 105–107; consumption table printed p. 161 / PDF p. 163 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 wiring-device modules | Publisher `AUTOMATISME.pdf` |
| Local controls | 4 scenario recall buttons | Publisher `AUTOMATISME.pdf` |
| Indicators | 4 scenario LEDs | Publisher `AUTOMATISME.pdf` |
| Physical configurator positions | `A`, `PL`, `M` | Publisher `AUTOMATISME.pdf` |

The guide also documents master/slave scenario-unit behavior through `M`; that is configuration semantics rather than an additional physical characteristic.

| Setting / property | Source-scoped value or behavior | Evidence |
| --- | --- | --- |
| Supply / consumption | `27 Vdc` bus; `9 mA` | AUTOMATISME.pdf printed p.161 /PDF p.163 |
| Programming control | Rear learning/lock selector; scenarios stored in the master | AUTOMATISME.pdf printed p.105 /PDF p.107 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `20` | Canonical catalogue |
| Technical item description | Scenario control unit | Canonical catalogue |
| Item family | `19` - Scenarios controller and scheduler | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `4` | `AS_ITEM_SYSTEM` |
| Commercial records | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `4` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Canonical commercial record metadata

| Reference / record | Catalogue name / source description | Visibility / type | Dependent / gateway | Evidence |
| --- | --- | --- | --- | --- |
| `N4681` / `20` | Scenario control unit; `BTicino_L/N/NT_Scenario control unit` | `1` / Empty | `0` / `0` | Canonical manufacturer catalogue |

Visibility, dependency and gateway flags describe the catalogue record, not the installed Device state.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `223` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Firmware `223` has wildcard applicability `-1.-1.-1` and one Module. A sanitized hardware fingerprint remains pending.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `223` | `1` | `2` 4 scenarios control unit | Fixed/designated metadata | `1505` | `2` | `753` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

The firmware resolves to Object `2`, **4 scenarios control unit**, with one slot. No Virgin Object is declared for this firmware.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `223` | Physical configuration | `0` | Canonical firmware/mode association |
| `223` | Virtual Configuration | `1` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `223` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `223` | `A` | `0` | `0` | A; Configurator 0 |
| `223` | `PL` | `0..9` | `0` | PL; Light Point |

The firmware exposes only `A`, `PL` and `AID`. Scenario contents `SCE1` through `SCE4` belong to Object `2`, not to the physical firmware configurator set.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `2` - 4 scenarios control unit

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..9` | `0` | Area |
| `PL` | `0..9` | `0` | Light point |
| `SCE1` | `_` = SCE1 | `_` | Scenario 1 |
| `SCE2` | `_` = SCE2 | `_` | Scenario 2 |
| `SCE3` | `_` = SCE3 | `_` | Scenario 3 |
| `SCE4` | `_` = SCE4 | `_` | Scenario 4 |

### Device-specific interpretation

Catalogue firmware A is restricted to 0 and lacks M, although the 2006 manufacturer guide documents A`1..9` and master/slave M. This is a catalogue projection gap, not proof that the physical functions do not exist. Filter 1630 references a field from another Object scope and supplies no legal values.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `223` | `2` | `1630` | `TYPE_CONTACT` | No legal values specified in source (entire reusable range retained) | `0` | Contact type; field definition belongs to a different Object scope; do not alias it to a similarly named field |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 4` and the N4681 scenario-unit identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | record installed firmware rather than assuming wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm the single four-scenario control Object | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the configured scenario-unit address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `A`, `PL` and the `SCE1` through `SCE4` scenario assignments | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The retained guide documents four stored Automation scenarios. Stored actions can include other rooms; the control’s own A/PL address is not the list of scenario destinations. This catalogue Object does not enumerate additional functional domains or prove emitted frame behavior.

## Observed behavior and corroboration

No sanitized hardware capture for this exact Device is currently retained.

## Programming

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| A absent / `PL=1..9` | Recall scenario without room-wide OFF; a second press only extinguishes its LED, leaving outputs unchanged. | AUTOMATISME.pdf printed pp.103–104 /PDF pp.105–106 |
| `A/PL=1..9` | Before recall, switch off actuators in room A; second press switches that room off and clears LED. This mode cannot manage L4674 dimmer scenarios. The control reserves its own address: no actuator may share it. | Same guide pp.103–104 |
| Master / Slave | M absent=Master; `M=SLA` repeats four master buttons with matching A/PL. Only master stores/programs scenarios. | Same guide p.103 /PDF p.105 |
| Memory capacities | Buttons 1/2/3/4 store up to 45/35/25/20 commands. Actions may include other rooms and execute together at recall. | Same guide pp.104–105 /PDF pp.106–107 |
| Learn / change | Enable rear selector; hold selected button until LED blinks, operate only desired commands, press selected button to finish. Repeat for others. Changes add/update and do not clear previous commands; reset first for total replacement. Excess command count terminates learning, then reprogramming replaces the earlier sequence. Lock rear selector to prevent changes. | Same guide p.105 /PDF p.107 |
| Erase | With programming enabled, hold one button about 10 s to erase its scenario; hold buttons 1+4 together about 10 s for all. Rapid LED flashing confirms erase. | Same guide p.105 /PDF p.107 |

## Source reconciliation

The canonical database and archived official automation guide agree on the one-slot four-scenario topology and physical addressing. The guide supplies the behavior that the database alone cannot express: four stored scenarios and the two activation/reset modes.

The previous configuration locator pointed to the contact-interface section and is corrected to printed pp.103–105 /PDF pp.105–107. A physical four-scenario store is one catalogue Module/Object `2`, not four Objects. Catalogue `A=0` and absent M omit the guide’s room-reset and master/slave functions; these are documented product capabilities beyond this firmware projection. No claim of complete software support for every physical mode follows.

## Evidence limits and open work

- Add a sanitized N4681 hardware fingerprint.
- Corroborate scenario programming frames from first-hand traffic.
- Preserve the documented L4674 limitation as revision-scoped behavior.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0021-0030-2026-10-06.md#own-dev-0026)
