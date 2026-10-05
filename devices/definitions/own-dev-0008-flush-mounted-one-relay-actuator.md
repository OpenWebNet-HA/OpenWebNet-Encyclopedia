# Flush-mounted one-relay actuator

## Summary

This flush-mounted SCS actuator switches a lighting load through one integrated relay. Upper and lower pushbuttons provide local operation, with an LED for feedback; the permissible load depends on the lamp or transformer type.


| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0008` | Project identity |
| Technical description | Flush-mounted single-relay lighting actuator with local control | Catalogue + official technical sheet |
| Catalogue item | `1121` - “Flush mounted actuator 1 relay” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `101` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `186` | Implementation evidence |
| Declared Modules | `1` | Implementation evidence |
| Categories | Actuator, Lighting | Capability model |

This Device is a single-Module lighting actuator with one electromechanical relay, local buttons, LED indication, physical configurator positions, and MyHOME Suite configuration.

## Commercial identities


| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Arnould - Espace Evolution | `64390` | Established identity | Catalogue + official technical sheet |
| BTicino - Axolute | `H4671/1` | Established identity | Catalogue + official technical sheet |
| BTicino - LivingLight | `L4671/1` | Established identity | Catalogue + official technical sheet + PEP |
| BTicino - Matix | `AM5851/1` | Established identity | Catalogue + official technical sheet + PEP |
| Arnould - Espace Evolution | `64190` | Shared technical item | Implementation evidence; package/product-document review pending |
| Legrand - Céliane | `067559` | Shared technical item | Implementation evidence; product-document review pending |

The Product Environmental Profile independently identifies `L4671/1` as its reference product and states that the environmental data also represents `H4671/1` and `AM5851/1`.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00072-e-FR` | Technical sheet | 29/04/2014 | `H4671/1`, `L4671/1`, `AM5851/1`, `64390` | [Archived PDF](https://archive.openwebnet-ha.org/sha256/b6/39/b63971b46893557a9c8b4c930da6a55fc3165997d79768e612ef5db3087f5ea0.pdf) | [Official source](https://assets.legrand.com/general/legrand-fr/bt/np-ft-gt/mq00072-e-fr.pdf) |
| `BT-L4671_1-EN` | Product Environmental Profile | revision/date to verify | `L4671/1`, `H4671/1`, `AM5851/1` | [Archived PDF](https://archive.openwebnet-ha.org/sha256/85/34/853429f229cda5612efb9210cd2e044cd7ce8a346cf96d643eba5f26f9acfe27.pdf) | [Official source](https://dar.bticino.com/asset/Documents/BT-L4671_1-EN.pdf) |

The MyHOME Suite function documentation is also a vendor implementation source for the actuator modes and should remain distinct from the product PDFs.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Relay | 1 integrated electromechanical relay | Publisher documentation cited in this section |
| Mounting size | 2 flush-mounted modules | Publisher documentation cited in this section |
| Local interface | upper/lower pushbuttons plus LED | Publisher documentation cited in this section |
| SCS nominal supply | `27 Vdc` | Publisher documentation cited in this section |
| SCS operating supply | `18..27 Vdc` | Publisher documentation cited in this section |
| Current draw | `16.5 mA` | Publisher documentation cited in this section |
| Incandescent / halogen load at 230 Vac | `1380 W / 6 A` | Publisher documentation cited in this section |
| LED / compact fluorescent | `150 W`, maximum 3 lamps | Publisher documentation cited in this section |
| Linear fluorescent / electronic transformer | `150 W / 0.65 A` | Publisher documentation cited in this section |
| Ferromagnetic transformer | `460 VA / 2 A`, cos φ 0.5 | Publisher documentation cited in this section |
| Dissipation at maximum load | `0.9 W` | Publisher documentation cited in this section |
| Physical configurator positions | `A`, `PL`, `M`, `G1`, `G2` | Publisher documentation cited in this section |

The 2014 technical sheet establishes:


The five printed configurator positions provide independent evidence for the expected ordinary addressed-form configurator count. Hardware observation is still required before marking `N_CONF = 5` as corroborated.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1121` | Canonical catalogue |
| Item model / `modobj` | `101` | Canonical catalogue / retained definition |
| Main system | Lighting / Automation | Canonical catalogue / retained definition |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `186` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `186` | `1` | `6` Light actuator | Fixed/designated metadata | `641` | `6` | `445` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `186` | Physical configuration | retained Device-specific configuration modality |
| `186` | Virtual Configuration | retained Device-specific configuration modality |
| `186` | Advanced Configuration | retained Device-specific configuration modality |


The catalogue declares:

- Physical configuration
- Virtual Configuration

No Advanced Configuration association is present for firmware `186` in the canonical database.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `186` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `186` | `A` | `0..9` | `0` | A; Environment |
| `186` | `PL` | `0..9` | `0` | PL; Light Point |
| `186` | `M` | `0..1`; `3..4`; `11` = `SLA`; `15` = `PUL`; `9` = `O/I` | `0` | M; Mode (0-4, Pul, Sla, I/O) |
| `186` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |
| `186` | `G2` | `0..9` | `0` | G2; G2 - (0-9) |




### Published and reconciled details


| Field | Catalogue domain | Published role |
| --- | --- | --- |
| `AID` | Device identity field | not a physical configurator |
| `A` | `0..9` | room/environment address |
| `PL` | `0..9` | lighting point |
| `M` | stored values `0`, `1`, `3`, `4`, `O/I`, `SLA`, `PUL` | actuator mode |
| `G1` | `0..9` | physical group membership |
| `G2` | `0..9` | physical group membership |

### Database/PDF discrepancy for `M=2`

The published technical sheet explicitly documents:

| Physical `M` | Function |
| --- | --- |
| `0` | Master cyclic `ON`/`OFF` |
| `O/I` | upper button `ON`, lower button `OFF` |
| `SLA` | Slave |
| `PUL` | monostable `ON` / ignores room and general commands |
| `1` | Master with 1-minute delayed slave `OFF` |
| `2` | Master with 2-minute delayed slave `OFF` |
| `3` | Master with 3-minute delayed slave `OFF` |
| `4` | Master with 4-minute delayed slave `OFF` |

Firmware `186`'s stored `M` range omits value `2` even though the official 2014 sheet includes it. This is retained as a source discrepancy. Do not constrain a physical configurator validator to the database enum without accounting for the published Device documentation.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `6` - Light actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality |
| `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open | `0` | Relay state on device reset |
| `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing | `0` | Load control mode |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `SUBTYPE` | `11` = Actuator; `1` = Lamp; `10` = Valve; `15` = Differential restart; `6` = Fan; `7` = Watering; `8` = Controlled socket; `9` = Lock | `11` | Type of load |
| `G1` | `0..255` | `0` | Group 1; Group = 0 means no group |
| `G2` | `0..255` | `0` | Group 2; Group = 0 means no group |
| `G3` | `0..255` | `0` | Group 3; Group = 0 means no group |
| `G4` | `0..255` | `0` | Group 4; Group = 0 means no group |
| `G5` | `0..255` | `0` | Group 5; Group = 0 means no group |
| `G6` | `0..255` | `0` | Group 6; Group = 0 means no group |
| `G7` | `0..255` | `0` | Group 7; Group = 0 means no group |
| `G8` | `0..255` | `0` | Group 8; Group = 0 means no group |
| `G9` | `0..255` | `0` | Group 9; Group = 0 means no group |
| `G10` | `0..255` | `0` | Group 10; Group = 0 means no group |


### Reconciled Object notes

The fixed Light actuator Object `6` provides this reusable lighting-actuator parameter model:

| Configuration family | Surface |
| --- | --- |
| Addressing | `A`, `PL` |
| Actuator mode | master / slave / `PUL` |
| Local control | local-button behavior |
| Timing | delayed-off settings |
| Restart behavior | reset state |
| Load semantics | load-control mode and subtype |
| Group membership | reusable Object group fields |

Firmware `186` exposes `G1` and `G2` directly as physical fields, while the reusable Object model can represent a larger group-membership set under virtual configuration.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `186` | `1` | `6` | `4147` | No textual predicate stored | `1` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `186` | `6` | `573` | `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open (entire reusable range retained) | `0` | Per energy management (State on Reset) |
| `186` | `6` | `1866` | `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing (entire reusable range retained) | `0` | Load_control_mode |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `1` | `M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `1` |
| `1` | `M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `1` |
| `1` | `M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `1` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1121` and the installed model | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware without treating wildcard sentinels as literal installed values | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`6`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions, and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

### Existing Device-specific diagnostic notes


| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 101`, brand, line, and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware despite wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm the single Light actuator Object | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | obtain the configured lighting address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/virtual configuration values | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability


The Device participates in [`WHO 1` - Lighting](../../functional/who-1-lighting/). General lighting command syntax remains canonical there.

The product-specific dossier establishes which actuator modes, load ratings, physical configuration fields, and product identities apply.

## Observed behavior and corroboration

No additional publishable runtime observation is asserted beyond observations explicitly retained elsewhere on this page.

## Programming


Programming should preserve the distinction between:

- physical `A/PL/M/G1/G2` fields;
- reusable Object configuration fields;
- published Device-specific mode values that may not be represented faithfully by the firmware enum.

See [Configuration Programming](../../programming/configuration-programming.md) and [Programming Validation](../../programming/validation.md).

## Source reconciliation


The archived product sheet has been reconciled with the database discrepancy around `M=2`.

The delayed-Slave modes `M=1..4` are product behaviors, not merely enum labels: a Master command can turn linked loads on together while a subsequent Master `OFF` leaves the Slave output active for the configured delay. The documentation uses this for arrangements such as a light with delayed ventilation. `M=2` is therefore a genuine published physical mode despite its absence from firmware `186`'s stored enum.

The remaining completeness gap is commercial documentation/hardware corroboration, not the physical `M=2` semantics.

## Evidence limits and open work


- Locate authoritative product documentation for `64190` and `067559`.
- Search for additional language/revision variants of `MQ00072`.
- Add a sanitized hardware fingerprint to corroborate `modobj`, firmware, expected configurator count, address, and configuration.
- Experimentally confirm the published `M=2` mode on known hardware or another independent implementation source.
- Establish whether `64190` differs from `64390` only by supplied cover/package.

## Sources


- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [MyHOME Suite lighting actuator function documentation](https://myhomeswupdate.bticino.com/MyHOMESuite_Docs/MHS_function_0304b/EN_MHS_function_0304/modalita_attuatore_luci.html)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
- [Programming](../../programming/)
