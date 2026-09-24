# Programming Architecture

The programming protocol is a management layer carried in OpenWebNet frames. It selects one installed Physical Device, receives an initial state projection, runs programming sequences labelled virtual or advanced in `OPEN.db`, and closes the programming session.

## Managed systems

The common programming operations are associated in `OPEN.db` with the same managed systems that expose the common diagnostic surface:

| Diagnostic/programming `WHO` | `OPEN.db` system |
| ---: | --- |
| `1001` | Light and Automation system |
| `1004` | Thermoregulation |
| `1018` | Energy Management system |
| `1023` | Access Control |

Association in `OPEN.db` establishes that the templates belong to those system records. It does not prove that every Device or firmware implements every scenario or optional frame.

As in diagnostics, `WHO 1001` covers the broader Lighting/Automation management family even though the literal `EN_SYSTEM.who` value on the combined system row is `1`. Do not manufacture a second database association for functional `WHO 2`.

## Participants

| Participant | Responsibility |
| --- | --- |
| Programmer | resolves capability, selects the Device, validates values, sends writes, and closes or aborts |
| Device | reports identity and installed state, accepts or rejects writes, and reports completion |
| Gateway/transport | carries frames and preserves direction; it does not validate catalogue semantics |
| Catalogue resolver | maps Device, firmware, Module, Object, address, and configuration constraints before transmission |

The wire protocol has no transaction identifier. A programmer should serialize ambiguous programming operations on one connection and retain the active `WHO`, Device selector, scenario, sequence, and `slot` context.

## Three layers of state

| Layer | Established by |
| --- | --- |
| Catalogue capability | `MHCatalogue.db` firmware, slots, Objects, Virgin Objects, configuration definitions, filters, and rules |
| Programming request | frames sent during `ConfConfigurators` or `ConfKO` |
| Effective installed state | a fresh diagnostic interview after programming |

A request can be syntactically valid while being semantically invalid for the resolved Device. Conversely, a positive programming response establishes protocol acceptance, not necessarily complete diagnostic verification.

## `OPEN.db` virtual and advanced programming sequences

### Virtual-configurator transfer

`ConfConfigurators` writes twelve transport positions in two frames:

- `*#[WHO]*0*#4*[C1]*[C2]*[C3]*[C4]*[C5]*[C6]##`
- `*#[WHO]*0*#5*[C7]*[C8]*[C9]*[C10]*[C11]*[C12]##`

Each value has the `OPEN.db` transport range `0..255`. `N_CONF` reports the number of physical configurator positions provided by the Device, but no canonical relation maps `C1..C12` universally to firmware `EN_CONF` definitions or `progressive` ordering. Do not equate a transport field with a physical plug or catalogue position without independent correlation.

### Advanced Object transfer

`ConfKO` rebuilds the Device's Module/Object projection using:

- `DIMENSION 30` for `slot`, enabled/disabled Module state, and regular Object or Virgin Object;
- `DIMENSION 32` for system/address;
- `DIMENSION 35` for indexed configuration values.

The sequence begins with a mandatory reset-all-Objects command and ends with a mandatory programmer end-of-transmission frame. This makes the canonical sequence a replacement-style transfer, not an isolated patch operation.

`OPEN.db` also registers a reset-one-slot command, but the canonical `ConfKO` sequence uses reset-all.

## Direction and acknowledgement

`EN_OPEN.open_type` distinguishes programmer-to-Device and Device-to-programmer frames. Sequence rows additionally define mandatory, repeated, error, `NACK`, and timeout transitions.

Ordinary `ACK` and `NACK` templates exist in `OPEN.db` but are not listed as ordinary ordered members of the six programming sequences. `AS_OPEN_SEQUENCE.status4nack` nevertheless assigns state transitions for `NACK`. A state-machine implementation must therefore handle acknowledgement status separately from ordered frame membership.

## Source reconciliation

| Source | Contribution |
| --- | --- |
| `OPEN.db` | scenarios, frames, direction, parameter ranges, repetition, errors, and timeouts |
| `OpenQuery.txt` | queries used to assemble scenarios and state machines |
| `MHCatalogue.db` | Device/firmware capability and value constraints |
| `rules.db3` | selected Temperature Control linked-parameter rules |
| Public OpenWebNet PDFs | common frame syntax and functional system behavior |
| Observed traffic | actual ordering, optionality, and Device-specific support |
| MyHOME_Suite UI | selectable values, workflow state, and presentation |

`OPEN.db.diag_open` is broader than diagnostics: it marks these programming frames as well. Sequence membership, direction, and scenario type must be used to classify an operation.
