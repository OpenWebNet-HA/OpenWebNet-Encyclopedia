# Load Control Panel bus

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0020` | Project identity |
| Technical description | Four-channel SCS load-control status and override panel | Catalogue + official technical sheet |
| Catalogue item | `1465` - Load Control Panel bus | Implementation evidence |
| Main catalogue system | New energy saving / load control | Implementation evidence |
| Item model / `modobj` | `10` | Implementation evidence |
| Firmware definition | wildcard `-1.-1` | Implementation evidence |
| Declared Modules | `4` | Implementation evidence |
| Configuration modes | Virtual, Advanced, Physical | Implementation evidence |
| Object | `492` - Load control actuator visualization | Implementation evidence |
| Categories | Energy Management, User Interface | Product and capability model |

The load-control panel is a four-button SCS user interface for loads managed by the load-control system. It displays load state and permits a user override / re-enable action. The catalogue represents each of the four positions with the same fixed visualization Object and derives per-position priority from the product configurators.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC/HS/HD4673` | Documented commercial identity | Catalogue + `MQ00709` technical sheet |
| BTicino - LivingLight | `L/N/NT4673` | Documented commercial identity | Catalogue + `MQ00709` technical sheet |
| Legrand - Arteor | `573985` | Documented commercial identity | Catalogue + `MQ00709` technical sheet |
| Legrand - Arteor | `573991` | Documented commercial identity | Catalogue + `MQ00709` technical sheet |
| Legrand - Céliane | `067206` | Documented commercial identity | Catalogue + `MQ00709` technical sheet |
| Legrand - Céliane | `067207` | Documented commercial identity | Catalogue + `MQ00709` technical sheet |

The technical sheet names the corresponding 4673, `067206`/`067207` and `573985`/`573991` families, giving unusually strong commercial corroboration for the current six-record catalogue cluster.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00709_c_EN` | Technical sheet | revision/date not yet pinned | Four-channel load-control panel family | [Archived original](https://archive.openwebnet-ha.org/sha256/65/2c/652c9942739c968ead3ea7f2a2096d9b06a7f002ee9a014d4c93daaa7ef7193a.pdf) | publisher source not currently retained |
| MyHOME catalogue `HPML0714` | Product catalogue | revision/date not yet pinned | Load-control panel references `573985` / `573991` occur on printed p. 26 / PDF p. 26 | [Archived MyHOME catalogue](https://archive.openwebnet-ha.org/sha256/13/8e/138e7a234fe24fb044d3bfc82954e08b2887be22f3f8ceb24aecaeff6ed2f2e5.pdf) | publisher source not currently retained |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 modules | `MQ00709_c_EN` |
| User controls | 4 buttons | `MQ00709_c_EN` |
| Indicators | 4 red LEDs | `MQ00709_c_EN` |
| SCS supply | `18..27 Vdc` | `MQ00709_c_EN` |
| Maximum current draw | `7 mA` | `MQ00709_c_EN` |
| Operating temperature | `0..40 °C` | `MQ00709_c_EN` |
| Temporary user re-enable | 4 hours | `MQ00709_c_EN` |

The four OpenWebNet Modules represent the four panel positions, not four different Object types.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1465` | Implementation evidence |
| Main system | New energy saving / load control | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `10` | Implementation evidence |
| Family | catalogue energy-management family | Implementation evidence |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `232` | `-1` | `-1` | `-1` | `4` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Wildcard values are catalogue applicability sentinels, not claims about an installed firmware version.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `232` | `1` | `463` Load control actuator visualization | Fixed/designated metadata | `1179` | `492` | `635` |
| `232` | `2` | `463` Load control actuator visualization | Fixed/designated metadata | `1180` | `492` | `635` |
| `232` | `3` | `463` Load control actuator visualization | Fixed/designated metadata | `1181` | `492` | `635` |
| `232` | `4` | `463` Load control actuator visualization | Fixed/designated metadata | `1182` | `492` | `635` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

There is no Virgin Object.

## Configuration modes

| Mode / modality | Evidence |
| --- | --- |
| Physical configuration | `MQ00709_c_EN` + implementation evidence |
| Virtual Configuration | implementation evidence |
| Advanced Configuration | implementation evidence |

The product also defines self-learning selected by `M=1` when the priority configurators are cleared; this is product behavior, not a fifth Module.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `232` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `232` | `P1AB` | `0..6` | `0` | P1ab; Configurator P1ab |
| `232` | `P2A` | `0..9`; `10` = `OFF` | `0` | P2a; Configurator P2a |
| `232` | `P2B` | `0..9`; `10` = `OFF` | `0` | P2b; Configurator P2b |
| `232` | `P1CD` | `0..6` | `0` | P1cd; Configurator P1cd |
| `232` | `P2C` | `0..9`; `10` = `OFF` | `0` | P2c; Configurator P2c |
| `232` | `P2D` | `0..9`; `10` = `OFF` | `0` | P2d; Configurator P2d |
| `232` | `M` | `0..1` | `0` | M; M (Normal 0- Self learning 1) |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `P1AB` | `0..6` | shared priority/configurator field for positions A/B |
| `P2A` | `0..9` or `OFF` | position A sub-priority / disable selector |
| `P2B` | `0..9` or `OFF` | position B sub-priority / disable selector |
| `P1CD` | `0..6` | shared priority/configurator field for positions C/D |
| `P2C` | `0..9` or `OFF` | position C sub-priority / disable selector |
| `P2D` | `0..9` or `OFF` | position D sub-priority / disable selector |
| `M` | `0` Normal / `1` Self learning | operating/configuration mode |


`OFF` is represented by catalogue value `10` in the `P2` fields. The dossier keeps both the encoded value and the human label distinct.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `463` - Load control actuator visualization

Catalogue Object key `492` maps to external Object `463`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PRIORITY` | `0..63` | `1` | Priority |
| `PHASE` | `0` = Single phase; `1` = Phase 1; `2` = Phase 2; `3` = Phase 3 | `0` | Phase |


### Additional Device-specific interpretation

Object `463` exposes:

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `PRIORITY` | `0..63` | `1` | load-control priority represented by the Module |
| `PHASE` | `0` Single/undefined, `1` Phase 1/R, `2` Phase 2/S, `3` Phase 3/T | `0` | electrical phase association |

The product documentation defines the physical priority as decimal composition of the applicable `P1` tens component and `P2` units component, up to priority `63`. The missing catalogue conversion records are still material to reproducing MyHOME Suite's internal rule graph, but they no longer make the product-level `P1` / `P2` mapping unknown.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `232` | `1` | `463` | `4145` | No textual predicate stored | None |
| `232` | `1` | `463` | `4452` | `M=0;P1ab<>0;P2a<>OFF` | `421` |
| `232` | `1` | `463` | `4454` | `M=0;P1ab=0;P2a<>OFF;P2a<>0` | `421` |
| `232` | `1` | `463` | `4476` | `M=1;P1ab=0;P2a=0;P2b=0;P1cd=0;P2c=0;P2d=0` | None |
| `232` | `2` | `463` | `4145` | No textual predicate stored | None |
| `232` | `2` | `463` | `4453` | `M=0;P1ab<>0;P2b<>OFF` | `431` |
| `232` | `2` | `463` | `4455` | `M=0;P1ab=0;P2b<>OFF;P2b<>0` | `431` |
| `232` | `2` | `463` | `4476` | `M=1;P1ab=0;P2a=0;P2b=0;P1cd=0;P2c=0;P2d=0` | None |
| `232` | `3` | `463` | `4145` | No textual predicate stored | None |
| `232` | `3` | `463` | `4456` | `M=0;P1cd<>0;P2c<>OFF` | `441` |
| `232` | `3` | `463` | `4458` | `M=0;P1cd=0;P2c<>OFF;P2c<>0` | `441` |
| `232` | `3` | `463` | `4476` | `M=1;P1ab=0;P2a=0;P2b=0;P1cd=0;P2c=0;P2d=0` | None |
| `232` | `4` | `463` | `4145` | No textual predicate stored | None |
| `232` | `4` | `463` | `4457` | `M=0;P1cd<>0;P2d<>OFF` | `451` |
| `232` | `4` | `463` | `4459` | `M=0;P1cd=0;P2d<>OFF;P2d<>0` | `451` |
| `232` | `4` | `463` | `4476` | `M=1;P1ab=0;P2a=0;P2b=0;P1cd=0;P2c=0;P2d=0` | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | - | None | - | No relation-specific filters associated | - | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `421` | No item-side predicate on this branch | Referenced conversion rule absent from source | `421` |
| `431` | No item-side predicate on this branch | Referenced conversion rule absent from source | `431` |
| `441` | No item-side predicate on this branch | Referenced conversion rule absent from source | `441` |
| `451` | No item-side predicate on this branch | Referenced conversion rule absent from source | `451` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

### Product interpretation and source differences

The current catalogue uses explicit conditions for normal mode:

| Slot | Normal-mode condition using shared `P1` | Fallback normal-mode condition | Conversion reference |
| ---: | --- | --- | ---: |
| `1` / A | `M=0;P1ab<>0;P2a<>OFF` | `M=0;P1ab=0;P2a<>OFF;P2a<>0` | `421` |
| `2` / B | `M=0;P1ab<>0;P2b<>OFF` | `M=0;P1ab=0;P2b<>OFF;P2b<>0` | `431` |
| `3` / C | `M=0;P1cd<>0;P2c<>OFF` | `M=0;P1cd=0;P2c<>OFF;P2c<>0` | `441` |
| `4` / D | `M=0;P1cd<>0;P2d<>OFF` | `M=0;P1cd=0;P2d<>OFF;P2d<>0` | `451` |

All four slots also carry the self-learning condition:

`M=1`; P1ab=0; P2a=0; P2b=0; P1cd=0; P2c=0; P2d=0

The slot-condition rows reference conversion identifiers `421`, `431`, `441` and `451`, but no matching rows were found in `EN_CONV_RULE` in the canonical catalogue copy. The references are therefore preserved as unresolved implementation evidence; this definition does not fabricate the missing arithmetic.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | identify `modobj` 10 / commercial family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | record actual installed firmware despite wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate the four fixed visualization Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect per-position load-control addressing if exposed | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `PRIORITY`, `PHASE` and product configurators where exposed | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The panel belongs to load / energy management. Product documentation establishes status visualization and user override behavior; the catalogue establishes the four fixed OpenWebNet visualization Objects and their parameter domains. Generic energy-management protocol semantics remain canonical under Functional Protocol.

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

Normal physical configuration uses `P1AB` / `P1CD` plus the per-position `P2` configurators. `M=1` selects self-learning only when all `P1` / `P2` fields are zero, exactly matching the explicit catalogue condition. Virtual and Advanced configuration are also declared. Software should represent self-learning as a product-level configuration mode, not as a fifth Module.

## Source reconciliation

`MQ00709_c_EN` directly resolves the physical priority encoding that was previously left as an open conversion question:

- `P1AB` / `P1CD` provide the tens component for their respective button pairs;
- each `P2A` / `P2B` / `P2C` / `P2D` provides the units component for that position;
- the resulting published priority domain reaches `63`, matching Object `463`'s `PRIORITY` domain;
- the product sheet gives worked examples including priorities `5`, `6`, `12` and `13`, demonstrating that the mapping is decimal composition rather than an unknown opaque encoding;
- front LEDs distinguish load state and programming/self-learning states, and the self-learning workflow associates a panel position with a controlled load;
- the documented user override temporarily re-enables a shed load for four hours.

The unresolved implementation question is now narrower: why the catalogue condition rows reference conversion IDs `421`, `431`, `441` and `451` when corresponding `EN_CONV_RULE` rows are absent. The physical `P1/P2 -> PRIORITY` semantics themselves are documented and must not be described as unknown.

## Evidence limits and open work

- Obtain a sanitized four-slot `DIMENSION 30` / `DIMENSION 35` fingerprint from a known panel.
- Recover or independently establish the missing conversion logic referenced as `421` / `431` / `441` / `451`.
- Reconcile the documented decimal `P1` / `P2` priority composition with the missing catalogue conversion-rule records before implementing a database-driven converter.
- Correlate wildcard firmware applicability with observed firmware versions.
- Check whether phase configuration is surfaced consistently across all six commercial identities.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
