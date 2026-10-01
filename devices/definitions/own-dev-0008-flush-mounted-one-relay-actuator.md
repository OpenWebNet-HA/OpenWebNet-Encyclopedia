# Flush-mounted one-relay actuator

## Summary


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
| Arnould Espace Evolution | `64390` | Established identity | Catalogue + official technical sheet |
| BTicino Axolute | `H4671/1` | Established identity | Catalogue + official technical sheet |
| BTicino L/N/NT | `L4671/1` | Established identity | Catalogue + official technical sheet + PEP |
| BTicino Matix | `AM5851/1` | Established identity | Catalogue + official technical sheet + PEP |
| Arnould Espace Evolution | `64190` | Shared technical item | Implementation evidence; package/product-document review pending |
| Legrand Céliane | `067559` | Shared technical item | Implementation evidence; product-document review pending |

The Product Environmental Profile independently identifies `L4671/1` as its reference product and states that the environmental data also represents `H4671/1` and `AM5851/1`.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00072-e-FR` | Technical sheet | 29/04/2014 | `H4671/1`, `L4671/1`, `AM5851/1`, `64390` | [Archived PDF](../../sources/devices/documents/device-doc-one-relay-mq00072-e-fr/MQ00072-e-FR.pdf) | [Official source](https://assets.legrand.com/general/legrand-fr/bt/np-ft-gt/mq00072-e-fr.pdf) |
| `BT-L4671_1-EN` | Product Environmental Profile | revision/date to verify | `L4671/1`, `H4671/1`, `AM5851/1` | [Archived PDF](../../sources/devices/documents/device-doc-one-relay-pep-l4671-1-en/BT-L4671_1-EN.pdf) | [Official source](https://dar.bticino.com/asset/Documents/BT-L4671_1-EN.pdf) |

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

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `186` | `-1` | `-1` | `-1` | `1` | catalogue default | wildcard / unspecified applicability |

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

## Module, Object, and Virgin Object model

### Objects

| Firmware | Object | Description | Relationship |
| --- | --- | --- | --- |
| `186` | `6` | Light actuator | catalogue firmware/Object relation |

### Virgin Objects

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

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

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `186` | `AID` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `186` | `A` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `186` | `PL` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `186` | `M` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `186` | `G1` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `186` | `G2` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |

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
| `0` | Master cyclic ON/OFF |
| `O/I` | upper button ON, lower button OFF |
| `SLA` | Slave |
| `PUL` | monostable ON / ignores room and general commands |
| `1` | Master with 1-minute delayed slave OFF |
| `2` | Master with 2-minute delayed slave OFF |
| `3` | Master with 3-minute delayed slave OFF |
| `4` | Master with 4-minute delayed slave OFF |

Firmware `186`'s stored `M` range omits value `2` even though the official 2014 sheet includes it. This is retained as a source discrepancy. Do not constrain a physical configurator validator to the database enum without accounting for the published Device documentation.

## Object configuration surfaces

### Object `6` - Light actuator

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `M` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `LOCAL_BUTTON` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DELAYED_OFF` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `STATE_RESET` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `LOAD_CONTROL_MODE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `HOURS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `MINUTES` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SECONDS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SUBTYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G3` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G4` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G5` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G6` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G7` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G8` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G9` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G10` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Reconciled Object notes

The fixed Light actuator Object `6` provides this reusable lighting-actuator parameter model:

| Configuration family | Surface |
| --- | --- |
| Addressing | `A`, `PL` |
| Actuator mode | master / slave / PUL |
| Local control | local-button behavior |
| Timing | delayed-off settings |
| Restart behavior | reset state |
| Load semantics | load-control mode and subtype |
| Group membership | reusable Object group fields |

Firmware `186` exposes `G1` and `G2` directly as physical fields, while the reusable Object model can represent a larger group-membership set under virtual configuration.

## Conditions, filters, and conversions

### Relation filters

| Scope | Filter IDs | Interpretation |
| --- | --- | --- |
| Device/Object relations | `573`, `1866` | apply before exposing reusable Object values |

### Slot conditions and conversions

| Scope | Condition IDs | Conversion treatment |
| --- | --- | --- |
| Device slots | `4147` | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

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

The delayed-Slave modes `M=1..4` are product behaviors, not merely enum labels: a Master command can turn linked loads on together while a subsequent Master OFF leaves the Slave output active for the configured delay. The documentation uses this for arrangements such as a light with delayed ventilation. `M=2` is therefore a genuine published physical mode despite its absence from firmware `186`'s stored enum.

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
