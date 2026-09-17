# Diagnostic `DIMENSION` Reference

Diagnostic `DIMENSION` values describe identity, versions, health, Modules, addresses, and configuration. They are scoped to the selected diagnostic `WHO` even where the canonical implementation reuses one template across several families.

The tables below cover the Device interview and detailed configuration sequences. Additional system-level service diagnostics with an empty `WHERE` are listed separately because they are not part of the standard per-Device interview.

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

`OPEN.db` describes each version placeholder as version/release/build components. Its parameter rows assign `1`–`99` to `FW_VERSION` and `0`–`99` to `HW_VERSION` and `MICRO_VERSION`, but the compact placeholder does not by itself establish how the three components are packed into the transmitted fields. Preserve the actual field sequence until capture evidence establishes the encoding.

`N_CONF` in `DIMENSION 1` reports how many physical configurator slots the Device provides. It counts available positions rather than currently inserted configurators and excludes the catalogue's common `AID`/ID field. See [Device Identity](dim1-device-identity.md) for the capture, catalogue, and product-diagram correlations.

`DIMENSION 4` and `5` each carry six configurator values in the range `0`–`255`. They are Device-level physical/virtual configurator reports, not `EN_CONF.idx` configuration parameters. The relationship between their twelve positional values and unused physical positions should be preserved from captures rather than inferred solely from `N_CONF`.

`DIMENSION 7` and `8` are typed as 24-bit bitmasks. `OPEN.db` does not define individual bit meanings, so bit labels require family-specific implementation or capture evidence.

## Modules, addresses, and configuration

| `DIMENSION` | Frame | Meaning |
| ---: | --- | --- |
| `30` | `*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##` | configured Object or unconfigured Virgin Object by Module |
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

`DIMENSION 31` records have different `error_open` classifications in `OPEN.db`: codes `0`, `2`, `3`, and `4` are errors, while busy code `1` is classified as error-and-information. These implementation categories do not add wire fields.

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

## General and gateway service forms

`OPEN.db` contains a second diagnostic surface using an empty `WHERE` field:

| `DIMENSION` | Frame | Database meaning |
| ---: | --- | --- |
| `1` | `*#[WHO]**1*[OBJECT_MODEL]*[N_CONF]*[BRAND]*[LINE]##` | gateway model identity response |
| `7` | `*#[WHO]**7##` | request general diagnostic A |
| `7` | `*#[WHO]**7*[BIT]##` | diagnostic/autodiagnostic bitmask response |
| `11` | `*#[WHO]**11*[BIT]##` | automatic hardware/software diagnostic event |
| `12` | `*#[WHO]**12##` / `*#[WHO]**12*[MAC1]*[MAC2]*[MAC3]*[MAC4]*[MAC5]*[MAC6]##` | MAC-address request/response |
| `15` | `*#[WHO]**15##` / `*#[WHO]**15*[OBJECT_MODEL]##` | WebServer model request/response |

The general `DIMENSION 7`, `11`, `12`, and `15` records are directly associated with the Nurse Call system in `AS_OPEN_SYSTEM`. `OpenQuery.txt` also selects the general `DIMENSION 7` frames and the gateway `DIMENSION 1` form for gateway-connection handling. This supports reuse in a gateway/service workflow but does not make these frames part of every diagnostic family’s Device interview.

## Requests and unsolicited values

The canonical database includes both sequence-driven responses and general diagnostic forms. `DIMENSION 7`, for example, has Device-specific and general diagnostic templates. A collector should retain unknown or unsolicited diagnostic frames and interpret them only within the selected `WHO`, active sequence, and source direction.

The `diag_open` flag in `EN_OPEN` is broader than this page: it also marks configuration, Object programming, and scenario-programming frames. Sequence membership and frame direction are required to classify an operation correctly.
