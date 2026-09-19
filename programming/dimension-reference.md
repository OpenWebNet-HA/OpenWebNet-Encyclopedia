# Programming `DIMENSION` Reference

Programming `DIMENSION` writes transfer virtual configurator values, Object assignments, Module addresses, and indexed parameters. Related Device responses report the written state or structured errors.

## Write frames

| `DIMENSION` | Frame | Meaning | Sequence |
| ---: | --- | --- | --- |
| `4` | `*#[WHO]*0*#4*[C1]*[C2]*[C3]*[C4]*[C5]*[C6]##` | write configurator positions 1..6 | `ConfConfigurators` |
| `5` | `*#[WHO]*0*#5*[C7]*[C8]*[C9]*[C10]*[C11]*[C12]##` | write configurator positions 7..12 | `ConfConfigurators` |
| `30` | `*#[WHO]*0*#30*[SLOT]*[KEYO]##` | assign Object to `slot` | `ConfKO` |
| `32` | `*#[WHO]*0*#32#[SLOT]*[SYS]*[ADDR]##` | assign Object system/address | `ConfKO` |
| `35` | `*#[WHO]*0*#35#[INDEX]#[SLOT]*[VAL_PAR]##` | write indexed configuration value | `ConfKO` |

`DIMENSION 4` is mandatory in `ConfConfigurators`; `5` is optional. `DIMENSION 30` is mandatory and repeatable in `ConfKO`; `32` and `35` are optional and repeatable.

## Related response and error frames

| `DIMENSION` | Frame | Meaning |
| ---: | --- | --- |
| `4` | `*#[WHO]*[WHERE]*4*[C1]*[C2]*[C3]*[C4]*[C5]*[C6]##` | Device configurator report `1..6` |
| `5` | `*#[WHO]*[WHERE]*5*[C7]*[C8]*[C9]*[C10]*[C11]*[C12]##` | Device configurator report `7..12` |
| `30` | `*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##` | configured Object or Virgin Object state |
| `31` | `*#[WHO]*[WHERE]*31*[SLOT]*[CODE]*[STATE]##` | Object state/error |
| `32` | `*#[WHO]*[WHERE]*32#[SLOT]*[SYS]*[ADDR]##` | effective Module address |
| `34` | `*#[WHO]*[WHERE]*34*[SLOT]*[ERROR]##` | address error |
| `35` | `*#[WHO]*[WHERE]*35#[INDEX]#[SLOT]*[VAL_PAR]##` | effective indexed parameter |
| `39` | `*#[WHO]*[WHERE]*39*[SLOT]*[INDEX]*[ERROR]##` | indexed parameter warning/error |

## Transport ranges

| Field | Range in `OPEN.db` |
| --- | ---: |
| `C1..C12` | `0..255` |
| `SLOT` | `1..255` |
| `KEYO` | `1..65535` |
| `SYS` | `1..255` |
| `ADDR` | `0..65535` |
| `INDEX` | `0..255` |
| `VAL_PAR` | `0..65535` |
| `STATE`, `ERROR` | `0..1` |

These are frame-field capacities. Catalogue and address rules define the values valid for a particular Device.

## `DIMENSION 4` and `5`

`OPEN.db` labels the fields “Configurator value” and describes the sequence as virtual configuration. `N_CONF` gives the Device's physical configurator-position count, but the relationship between each `C` field and jumper presence/value has not yet been established. Preserve all twelve raw positions.

## `DIMENSION 30`

The write carries a configured Object number. Diagnostic state determines how a previously reported `KEYO` is resolved:

- `STATE = 1`: `EN_KEY_OBJECT.key_object`;
- `STATE = 0`: `EN_VIRGIN_OBJECT.virgin_key_object`.

The target write must use a permitted configured Object, validated through Virgin Object, firmware, and slot associations.

## `DIMENSION 32`

`#32#[SLOT]` is the parameterized `DIMENSION` selector: the leading `#` selects the write form and the following `#` attaches `SLOT` to the selector. `SYS` and `ADDR` are ordinary `DIMENSION` values separated with `*`. They require the Object/system address rule and must not all be decoded as `A`/`PL`.

## `DIMENSION 35`

The two `#` separators before `INDEX` and `SLOT` are significant. `INDEX` correlates with context-resolved `EN_CONF.idx`. Apply ranges, filters, conditions, and conversions before encoding `VAL_PAR`.

## Error dimensions

`DIMENSION 31` provides five fixed Object-state codes. `DIMENSION 34` and `39` carry boolean error fields without enumerated causes.

`DIMENSION 39` is intentionally nonfatal in the canonical advanced sequence: it maps to Warning so an unmanaged parameter does not necessarily reject the rest of the transfer.

## Source boundary

The same numeric dimensions appear in diagnostics because programming writes and diagnostic read-back project related state. Direction, frame form, and active sequence distinguish them. See the [Diagnostic `DIMENSION` Reference](../diagnostics/dimension-reference.md) for read-only interpretation.
