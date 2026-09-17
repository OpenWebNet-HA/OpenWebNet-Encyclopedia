# Diagnostic `DIMENSION` Reference

Diagnostic `DIMENSION` values describe identity, versions, health, Modules, addresses, and configuration. They are scoped to the selected diagnostic `WHO` even where the canonical implementation reuses one template across several families.

## Identity and versions

| `DIMENSION` | Response frame | Meaning |
| ---: | --- | --- |
| `1` | `*#[WHO]*[WHERE]*1*[OBJECT_MODEL]*[N_CONF]*[BRAND]*[LINE]##` | Device identity |
| `2` | `*#[WHO]*[WHERE]*2*[FW_VERSION]##` | firmware version |
| `3` | `*#[WHO]*[WHERE]*3*[HW_VERSION]##` | hardware version |
| `4` | `*#[WHO]*[WHERE]*4*[C1]*[C2]*[C3]*[C4]*[C5]*[C6]##` | configurators 1–6 |
| `5` | `*#[WHO]*[WHERE]*5*[C7]*[C8]*[C9]*[C10]*[C11]*[C12]##` | configurators 7–12 |
| `6` | `*#[WHO]*[WHERE]*6*[MICRO_VERSION]##` | microcontroller version |
| `7` | `*#[WHO]*[WHERE]*7*[BITMASK_DIA_A]##` | 24-bit diagnostic bitmask A |
| `8` | `*#[WHO]*[WHERE]*8*[BITMASK_DIA_B]##` | 24-bit diagnostic bitmask B |
| `13` | `*#[WHO]*[WHERE]*13*[ID]##` | 32-bit Device ID |

`OPEN.db` describes the version values as version/release/build components. The compact frame placeholder does not by itself establish a printable dotted-version encoding; preserve the raw components or source representation used by the actual response.

## Modules, addresses, and configuration

| `DIMENSION` | Frame | Meaning |
| ---: | --- | --- |
| `30` | `*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##` | Module/Object assignment and configured state |
| `31` | `*#[WHO]*[WHERE]*31*[SLOT]*[CODE]*[STATE]##` | Object-state result or error |
| `32` | `*#[WHO]*[WHERE]*32#[SLOT]*[SYS]*[ADDR]##` | Module system and address |
| `34` | `*#[WHO]*[WHERE]*34*[SLOT]*[ERROR]##` | Module address error |
| `35` | `*#[WHO]*[WHERE]*35#[INDEX]#[SLOT]*[VAL_PAR]##` | indexed configuration parameter |
| `38` | `*#[WHO]*0*38#[SLOT]##` | select/reset one Module for detailed data |
| `38` | `*#[WHO]*0*38#0##` | select/reset all Modules for detailed data |
| `39` | `*#[WHO]*[WHERE]*39*[SLOT]*[INDEX]*[ERROR]##` | parameter error |
| `310` | `*#[WHO]*[WHERE]*310*[SLOT]*[VAL_PAR]##` | Object-specific parameter without generic index |

The `#` separators before `SLOT` and `INDEX` are part of the canonical templates and must not be normalized away.

## `DIMENSION 31` codes

| Code | `OPEN.db` description |
| ---: | --- |
| `0` | Object not implemented/unset |
| `1` | Object busy |
| `2` | Object already configured |
| `3` | insufficient free Object capacity |
| `4` | requested Object not implemented |

The frame also carries a boolean `STATE` labelled configured/not configured. The two “not implemented” descriptions are preserved from distinct source entries; the source does not further clarify their boundary.

## Value ranges

| Field | Range in `OPEN.db` |
| --- | ---: |
| Device `ID` | `0`–`4294967295` |
| internal `SLOT` | `1`–`255` |
| `KEYO` | `1`–`65535` |
| configured `STATE` | `0`–`1` |
| `SYS` | `1`–`255` |
| `ADDR` | `0`–`65535` |
| configuration `INDEX` | `0`–`255` |
| `VAL_PAR` | `0`–`65535` |
| error flag | `0`–`1` |

These are transport/database ranges, not claims that every Device, Object, or system accepts every value.

## Requests and unsolicited values

The canonical database includes both sequence-driven responses and general diagnostic forms. `DIMENSION 7`, for example, has Device-specific and general diagnostic templates. A collector should retain unknown or unsolicited diagnostic frames and interpret them only within the selected `WHO`, active sequence, and source direction.
