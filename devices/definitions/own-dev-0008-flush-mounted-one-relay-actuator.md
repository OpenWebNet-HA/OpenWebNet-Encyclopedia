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
| Declared Modules | 1 | Implementation evidence |
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

| Document | Type | Revision / date | Coverage | Archived original | Publisher URL |
| --- | --- | --- | --- | --- | --- |
| `MQ00072-e-FR` | Technical sheet | 29/04/2014 | `H4671/1`, `L4671/1`, `AM5851/1`, `64390` | [Archived PDF](../../sources/devices/documents/device-doc-one-relay-mq00072-e-fr/MQ00072-e-FR.pdf) | [Official source](https://assets.legrand.com/general/legrand-fr/bt/np-ft-gt/mq00072-e-fr.pdf) |
| `BT-L4671_1-EN` | Product Environmental Profile | revision/date to verify | `L4671/1`, `H4671/1`, `AM5851/1` | [Archived PDF](../../sources/devices/documents/device-doc-one-relay-pep-l4671-1-en/BT-L4671_1-EN.pdf) | [Official source](https://dar.bticino.com/asset/Documents/BT-L4671_1-EN.pdf) |

The MyHOME Suite function documentation is also a vendor implementation source for the actuator modes and should remain distinct from the product PDFs.

## Physical and electrical characteristics

The 2014 technical sheet establishes:

| Property | Value |
| --- | --- |
| Relay | 1 integrated electromechanical relay |
| Mounting size | 2 flush-mounted modules |
| Local interface | upper/lower pushbuttons plus LED |
| SCS nominal supply | `27 Vdc` |
| SCS operating supply | `18..27 Vdc` |
| Current draw | `16.5 mA` |
| Incandescent / halogen load at 230 Vac | `1380 W / 6 A` |
| LED / compact fluorescent | `150 W`, maximum 3 lamps |
| Linear fluorescent / electronic transformer | `150 W / 0.65 A` |
| Ferromagnetic transformer | `460 VA / 2 A`, cos φ 0.5 |
| Dissipation at maximum load | `0.9 W` |
| Physical configurator positions | `A`, `PL`, `M`, `G1`, `G2` |

The five printed configurator positions provide independent evidence for the expected ordinary addressed-form configurator count. Hardware observation is still required before marking `N_CONF = 5` as corroborated.

## Identity and firmware

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1121` | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `101` | Implementation evidence |
| System | Lighting / Automation | Implementation evidence |
| Firmware | `186` | Implementation evidence |
| Firmware applicability | `-1.-1.-1` | Implementation evidence |
| Firmware slots | `1` | Implementation evidence |

The Device has one fixed Light actuator Object `6` on slot `1`.

## Configuration modes

The catalogue declares:

- Physical configuration
- Virtual Configuration

No Advanced Configuration association is present for firmware `186` in the canonical database.

## Firmware-scoped configuration

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

## Object configuration surface

The fixed Light actuator Object `6` provides the reusable lighting-actuator parameter model, including:

- `A` and `PL` address;
- master/slave/PUL mode;
- local-button behavior;
- delayed-off settings;
- reset state;
- load-control mode and subtype;
- group memberships.

Firmware `186` exposes `G1` and `G2` directly as physical fields, while the reusable Object model can represent a larger group-membership set under virtual configuration.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 101`, brand, line, and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware despite wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm the single Light actuator Object | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | obtain the configured lighting address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/virtual configuration values | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional behavior

The Device participates in [`WHO 1` - Lighting](../../functional/who-1-lighting/). General lighting command syntax remains canonical there.

The product-specific dossier establishes which actuator modes, load ratings, physical configuration fields, and product identities apply.

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

## Corroboration status and open work

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
