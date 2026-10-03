# Do Not Disturb / Make Up Room control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0104` | Project identity |
| Technical description | Inside-room control for Do Not Disturb (DND) and Make Up Room (MUR) notifications | Published technical sheets; canonical catalogue |
| Commercial identities | `H4653`, `LN4653`, `067593` | Three catalogue records and both technical-sheet headers |
| Catalogue item | `1679` | Canonical MyHOME Suite `3.5.38` catalogue |
| Main catalogue system | Access control | Main item/system association |
| Item model / `modobj` | `9` | Main item/system association |
| Firmware definition | `-1.-1.-1` (wildcard / unspecified applicability) | Canonical catalogue; not an observed installed release |
| Declared Modules | `1` | Canonical firmware metadata |
| Categories | Commands, User interfaces | Source-derived roles |

DND means Do Not Disturb; MUR means Make Up Room. These are room-service notifications. Two physical wiring-device modules do not imply two protocol Modules.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4653` | Established commercial variant | Item `1679`; `MM00775-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| BTicino - LivingLight | `LN4653` | Established commercial variant | Item `1679`; `MM00775-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Legrand - Céliane | `067593` | Established commercial variant | Item `1679`; `MM00775-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |

The LED-colour legend also mentions Arteor, but supplies no Arteor commercial reference. It does not establish an additional identity for this cluster.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MM00775_a_EN.pdf` | English technical sheet | `MM00775-a-EN`, `02/12/2013` | All three identities; specifications/legend printed p. 1 / PDF p. 1; physical/software configuration printed p. 2 / PDF p. 2; hotel-room system example printed p. 3 / PDF p. 3 | [Archived original](https://archive.openwebnet-ha.org/sha256/64/4c/644c203261a27563e37554fbc31c64cfe7fe693c8b7d43c6efd7337867856745.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/MM00775_a_EN.pdf) |
| `MM00775-a-FR.pdf` | French technical sheet | `MM00775-a-FR`, `02/12/2013` | All three identities; specifications/legend printed p. 1 / PDF p. 1; physical/software configuration printed p. 2 / PDF p. 2; hotel-room system example printed p. 3 / PDF p. 3 | [Archived original](https://archive.openwebnet-ha.org/sha256/7c/fb/7cfb238df47d8658200918c41f2030f85ce3cda677dc1b9afc53595f9016eab5.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/MM00775-a-FR.pdf) |
| `H4653` online catalogue | Live product page | Reviewed `2026-10-03`; no fixed revision | H4653 product characteristics and technical attributes; HTML has no printed or PDF pagination | Not retained as an original file | [Publisher product page](https://www.bticino.com/products/bt-h4653) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1679`; complete commercial, firmware, Module/Object and configuration records | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | Two flush-mounted wiring-device modules | `MM00775-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| SCS BUS supply | `18..27 Vdc` | `MM00775-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Rear interfaces | SCS BUS terminals and physical configurator socket | `MM00775-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Maximum current | `7.5 mA` | `MM00775-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Operating temperature | `5..40 °C` | `MM00775-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| Local functions | DND/MUR controls completed with applicable key covers; local LED adjustment/disable pushbutton | `MM00775-a-EN` / French counterpart, printed p. 1 / PDF p. 1; `MM00775-a-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| Axolute / Céliane LED colours | Blue: notification inactive; purple: active; Arteor also named in legend without a SKU | `MM00775-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| LivingLight LED colours | Green: inactive; orange: active | `MM00775-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| LED intensity sequence | Hold adjustment key for more than `2 s`; `60 %` default → `30 %` → `0 %` → `100 %` → `60 %` | `MM00775-a-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| Physical configurator positions | `R1`, `R2`, `M` | `MM00775-a-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| Published standards | `EN 60669-2-1`, `EN 50090-2-2`, `EN 50090-2-3`, `EN 50428` | `MM00775-a-EN` / French counterpart, printed p. 1 / PDF p. 1 |
| H4653 online dimensions / protection | `45 x 45 x 24 mm`; minimum box depth `55 mm`; `IP20` | H4653 live product page, reviewed `2026-10-03` |
| H4653 online storage / terminals | `-10..70 °C`; `0.34..2.5 mm²`, flexible or rigid wire | H4653 live product page, reviewed `2026-10-03` |
| H4653 online construction / interfaces | Plastic / thermoplastic, untreated, opaque; RAL-like `9011`; LED, no label area, display, temperature controller, IR sensor or RF bus | H4653 live attributes; one-button metadata discrepancy reconciled below |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1679` | Canonical catalogue |
| Technical item description | DO NOT DISTURB-MAKE UP ROOM control | Canonical catalogue |
| Item family | Control (`1`) | Catalogue family association |
| Main system | Access control; system key `8` | `AS_ITEM_SYSTEM.main` association; not a functional WHO number |
| Item model / `modobj` | `9` | Main item/system mapping |
| Brand / line keys | BTicino brand key `1`, Axolute line key `2`, LivingLight line key `4`; Legrand brand key `2`, Céliane line key `13` | Commercial database keys; different from software parameter model namespaces |
| Commercial records | `3`; record IDs `1735`, `1998`, `2171` | Three shared-item catalogue variants |
| Gateway metadata | None of the three records is marked as a gateway | Commercial metadata; an MH201 software route is an external system connection |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `253` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.


Hardware revision, microcontroller and installed firmware are unknown. The firmware table records source applicability, not an observed Physical Device.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `253` | `1` | `489` DO NOT DISTURB/MAKE UP ROOM control | Fixed/designated metadata | `1344` | `555` | `702` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `253` | Virtual Configuration | `1` | Catalogue association `1` |
| `253` | Advanced Configuration | `2` | Catalogue association `2` |
| `253` | Physical configuration | `0` | Catalogue association `3` |

Both technical sheets document physical configurators and MyHOME Suite software configuration. The software route uses the PC Ethernet network and external MH201 scenario module; the control/indicator itself remains on SCS BUS. No connection association is stored for this firmware in `AS_CONNECTION_FIRMWARE`; this absence does not invalidate the published Ethernet route. No Product Programming mode association is stored for this firmware.

## Firmware-scoped configuration

Domains and defaults below are catalogue evidence. `AID` is an eight-character mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `253` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `253` | `R1` | `0..9` | `0` | R1; Room tens |
| `253` | `R2` | `0..9` | `0` | R2; Room unit |
| `253` | `M` | `0..2` | `0` | M; Mode |

### Published physical selectors

| Configurator | Published value / meaning | Evidence |
| --- | --- | --- |
| `R1`, `R2` | Room address tens and units; firmware domain `0..9` for each | Catalogue; `MM00775-a-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| `M=0` | DND and MUR, using two one-module key covers | `MM00775-a-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| `M=1` | DND only, using one two-module key cover | `MM00775-a-EN` / French counterpart, printed p. 2 / PDF p. 2 |
| `M=2` | Stored as legal by the catalogue; no physical procedure or key-cover arrangement in the retained sheets | Firmware domain; Object `489.MODE=2` names MUR only but is a separate configuration scope |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `489` - DO NOT DISTURB/MAKE UP ROOM control

Catalogue Object key `555` maps to external Object `489`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `R1R2` | `0..99` | `0` | Room address |
| `MODE` | `0` = DO NOT DISTURB and MAKE UP ROOM; `1` = DO NOT DISTURB only; `2` = MAKE UP ROOM only | `0` | Mode of DO NOT DISTURB/MAKE UP ROOM control |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | Not applicable | None | Not applicable | No relation-specific filters associated | Not applicable | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion rule or selection predicate is associated with these placements. Validate the firmware domain and the selected Object/Firmware filters separately; empty selection metadata does not establish an active Object. Generic resolution remains in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Compare discovered model and system with catalogue main model `9` in Access control; this is a source-derived identification target, not a verified response | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Corroborate installed firmware before relating observations to wildcard catalogue applicability; no hardware fingerprint retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Corroborate hardware revision separately from firmware; no verified response retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Corroborate microcontroller revision if this managed Device supports the query; no verified response retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Discover active Objects and Modules: slot `1`, external Object `489`; no Virgin Object association. Do not report database relation IDs as KEYO | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Read applicable active Object addressing; room-address semantics belong to Access Control, not Lighting A/PL; device address encoding requires actual discovery context | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Read/compare the selected Object configuration against its reusable domain/default and firmware context; default is not installed state | [Configuration](../../diagnostics/dim35-configuration.md) |

These are candidate corroboration surfaces of the managed Device model. Catalogue associations do not prove that every operation succeeds on this firmware/transport. Access Control management uses `WHO 1023`; catalogue system key `8` is not `WHO 8`.

## Functional applicability

The main catalogue family is [Access Control (`WHO 23`)](../../functional/who-23-access-control/). That implementation family has managed addressing infrastructure; its numeric catalogue system key and item model are separate namespaces. No complete DND/MUR functional WHAT or DIMENSION vocabulary is established by the retained product sheets.

| Function | Published or implementation applicability | Evidence |
| --- | --- | --- |
| DND / MUR selection | Inside-room notification control of the corresponding outside-door indicator; physical `M=0` or `M=1`; software Object `489.MODE` also names MUR-only | Both technical sheets pp. 1-2 / PDF pp. 1-2; reusable Object `489` |
| Status feedback | Variant-specific LED colours and local brightness/disable adjustment | Both technical sheets pp. 1-2 / PDF pp. 1-2 |

## Observed behavior and corroboration

No sanitized hardware fingerprint, protocol capture or commissioning experiment is retained for this exact technical item. Source diagrams, room number `127`, switch states and example addresses are publisher illustrations, not observed project installations.

## Programming

MyHOME Suite software configuration uses PC Ethernet through MH201 to the SCS system; it offers more options than physical configuration. The technical sheets do not define a complete transfer wizard, erase scope, firmware-update package or recovery procedure. Validate the active Object and its complete configuration before applying changes; absence of slot predicates does not supply a selection algorithm.

Match room-address configuration to the associated outside indicator. Use two one-module key covers for physical `M=0` or one two-module cover for `M=1.` Catalogue legal `M=2` and reusable Object MUR-only `MODE=2` must remain distinct until an exact physical/software mapping is verified. The local LED adjustment is a press longer than `2 s` with the published brightness cycle.

The sheet p. 3 / PDF p. 3 hotel example uses `R1=2`, `R2=7`, `M=–` alongside LN4650, LN4649, LN4652, LN4691, MH201, F430R8 and E49. A displayed room number `127` is a human label; it does not extend the two-digit bus address domain to 127. Power-supply/load protection and air-conditioning actuator choice depend on the installed loads; the example is not a universal bill of materials.

## Source reconciliation

The English and French technical sheets have the same `a`, `02/12/2013` revision and agree on the Device-specific specifications, modes, procedures and scope described above. Their three-reference headers independently support the catalogue cluster. General vendor/contact text and certification marks remain in the originals; listed standards are publisher declarations, not a new certification audit. Physical wiring-device module count is independent of protocol Module count. Catalogue status/default metadata and published operating descriptions are not observations of installed firmware or behavior.

| Source issue | Reconciliation / unresolved limit | Evidence |
| --- | --- | --- |
| Unprinted physical mode | Catalogue firmware M and Object `489` MODE both admit `2`; only reusable MODE names MUR-only. Technical sheets specify physical `M=0/1` only | Firmware/Object domains; both sheets p. 2 |
| Button count | H4653 live attributes say one button/actuation point; dated sheets show two one-module DND/MUR covers at `M=0` and a two-module DND cover at `M=1.` No universal one-button count substituted | H4653 live page; both sheets pp. 1-2 |
| Room-label scope | Hotel illustration label 127 accompanies bus address 27; a room-number label is not an encoded address or new legal domain | Both sheets p. 3 |
| Arteor colour legend | Arteor is named in LED-colour grouping but no associated SKU is established | Both sheets p. 1 |

## Evidence limits and open work

- Establish whether and how firmware `M=2` selects MUR-only, and which key covers/software procedures apply; no physical `M=2` procedure is retained.
- Resolve the current H4653 one-button attribute against the mode-specific cover arrangements; do not discard either source.
- Corroborate Object `489`, room addressing, status feedback, brightness adjustment and firmware/hardware identity on the three commercial variants.
- Retained exact-product source reconciliation is scoped to the listed revisions; current commercial catalogues/translations and future revisions can extend it. Live product attributes have review-date provenance but no archived byte snapshot.

## Sources

Catalogue tables were read from the registered `MHCatalogue.db` original, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. `EN_ITEM`, `EN_DEVICE`, firmware/system associations, `EN_SLOTS`, Object/Virgin relationships, `EN_CONF`/`EN_CONF_RANGE`, slot conditions, filters, conversions and configuration-mode associations define the implementation scope. Exact archived PDF revisions and publisher URLs are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue metadata and retained fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
- [H4653 official catalogue](https://www.bticino.com/products/bt-h4653)
