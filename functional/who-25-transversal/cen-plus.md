# CEN+

CEN+ is carried within `WHO 25` and provides a virtual-object command/event model for short press, extended press and rotary-selector interactions. It is related to CEN under [`WHO 15`](../who-15-cen/) but uses a different field allocation and address space.

## `WHAT` reference

| `WHAT` | Meaning |
| ---: | --- |
| `21` | Short pressure, less than 0.5 seconds |
| `22` | Start of extended pressure, at least 0.5 seconds |
| `23` | Extended pressure / keep pressing |
| `24` | Release after an extended pressure |
| `25` | Rotary selector, slow clockwise rotation |
| `26` | Rotary selector, fast clockwise rotation |
| `27` | Rotary selector, slow counter-clockwise rotation |
| `28` | Rotary selector, fast counter-clockwise rotation |

Unlike `WHO 15`, the interaction type is encoded by `WHAT`; the virtual pushbutton number is carried as a parameter.

## Pushbutton parameter

The parameter attached to `WHAT` identifies the virtual pushbutton and has the range `0..31`.

The general form is `*25*WHAT#PUSHBUTTON*WHERE##`.

`PUSHBUTTON` and the Object embedded in `WHERE` are independent fields: the first identifies the control on the source Object, while the second identifies the configured CEN+ virtual Object.

## `WHERE` - virtual Object

CEN+ uses a virtual address formed from the prefix `2` and an Object value in the range `0..2047`.

Conceptually:

`WHERE = 2 + OBJECT`

Published examples include `21` for Object 1, `20` for Object 0, `2101` for Object 101, `22010` for Object 2010, and `22047` for Object 2047. The field is therefore a protocol composition, not a decimal arithmetic addition.

A decoder should remove/interpret the CEN+ prefix according to the `WHO 25` grammar rather than parse the complete field as a Lighting/Automation `A`/`PL` address.

## Short pressure - `WHAT 21`

Action frame: `*25*21#PUSHBUTTON*WHERE##`.

A short interaction is complete in one event. It represents a press and release occurring before the 0.5-second extended-pressure threshold; there is no separate short-release `WHAT` analogous to CEN `WHO 15` `#1`.

The published action sequence acknowledges the virtual action with `ACK` and shows the corresponding CEN+ frame on event connections. Firmware-specific reply and bus-output observations are distinguished in [Gateway compatibility](#gateway-compatibility-and-hardware-boundaries).

## Start of extended pressure - `WHAT 22`

Action frame: `*25*22#PUSHBUTTON*WHERE##`.

This marks that the button has reached the extended-pressure threshold. It begins the long-interaction sequence and is distinct from the periodic continued-pressure event `WHAT 23`.

## Extended pressure - `WHAT 23`

Action frame: `*25*23#PUSHBUTTON*WHERE##`.

While a physical CEN+ button remains pressed, continued-pressure events can follow the initial `WHAT 22`. Multiple `WHAT 23` frames may therefore belong to one physical interaction.

## End of extended pressure - `WHAT 24`

Action frame: `*25*24#PUSHBUTTON*WHERE##`.

This marks release after an extended interaction and closes the sequence begun by `WHAT 22`.

A typical held-button event sequence is therefore:

`WHAT 22` → zero or more `WHAT 23` → `WHAT 24`.

The published examples show both sequences with repeated `23` frames and a sequence in which `22` is followed directly by `24` when release occurs before another continued-pressure interval is emitted.

## Rotary-selector events - `WHAT 25..28`

CEN+ also defines directional rotary interactions:

| Direction | Slow | Fast |
| --- | ---: | ---: |
| Clockwise | `25` | `26` |
| Counter-clockwise | `27` | `28` |

These operations use the same virtual Object/pushbutton addressing model. Their presence is an important difference from Basic/Evolved CEN under `WHO 15`.

## Action and event connections

The published CEN+ action and event sequences show a client sending the functional frame on an action connection and receiving `ACK`; event-session clients receive the corresponding frame when the gateway reads the CEN+ event on the SCS bus. This is the published exchange, not an unconditional acknowledgement rule for every gateway firmware.

The same event form can therefore represent an interaction originating from a physical CEN+ command or from a virtual action submitted through a gateway. The functional frame itself identifies the interaction, pushbutton and Object rather than its origin.

Historical touchscreen scenario actions send the configured frame literally. Their CEN+ description labels and internal command identifiers do not select a wire `WHAT` or synthesize an extended-pressure sequence. See [Configured-action handling](../../scenario-engine/execution-model.md#historical-touchscreen-condition-evaluation) and [CEN/CEN+ implementation evidence](../../project/review/myopencommunity-cen-history-review.md#cen-and-cen-configured-actions).

## CEN+ configuration model

The published CEN documentation states that CEN+ devices use Advanced Virtual Configuration and do not use a conventional SCS bus address for this function. The configured virtual Object becomes the OpenWebNet `WHERE`, while the button number is represented by the `WHAT` parameter.

This is materially different from Basic/Evolved CEN, where `WHO 15` `WHERE` can represent an `A`/`PL` source address and the button number itself occupies `WHAT`.

## Relationship to CEN

| Property | CEN - `WHO 15` | CEN+ - `WHO 25` |
| --- | --- | --- |
| Button number | `WHAT 00..31` | `WHAT` parameter `0..31` |
| Interaction phase | optional `WHAT` parameter `#1..#3` | `WHAT 21..24` |
| Source/target | `A`/`PL` and advanced CEN `WHERE` forms | virtual Object `0..2047` with prefix `2` |
| Rotary events | not defined in the published CEN table | `WHAT 25..28` |

The two systems should be modeled separately even when a physical command device is capable of both modes.

## Gateway compatibility and hardware boundaries

**Published protocol.** The [CEN/CEN+ specification](https://archive.openwebnet-ha.org/sha256/8b/f0/8bf06ff1394615dbf6d46a1fc8b9c53573ed96f1c1b112b2dd8a6021faf3dd21.pdf), page 24, lists the following CEN+ compatibility. A firmware value of “not stated” preserves the source's scope rather than asserting support across every firmware release.

| Gateway model | Firmware in source | Published CEN+ support |
| --- | --- | --- |
| MH200 | Not stated | No |
| MH200N / 03565 | Not stated | Yes |
| F453AV | `1.0.19` | No |
| F453AV / 573992 | `2.1.7` | Yes |
| F453 | Not stated | Yes |
| F452V | Not stated | No |
| F452 | Not stated | No |

The same table lists CEN (`WHO 15`) support for MH200, while CEN+ is unavailable. This function-level distinction does not establish a response to every frame in the wider `WHO 25` namespace. The [dry-contact/IR specification](dry-contact-ir.md#gateway-compatibility-and-hardware-boundaries) has its own compatibility table.

**Current oracle v3 result inspection.** The pinned results at own-firmware-oracle revision `8a61bbeb1d26354241debac84a7310142e5ab3a5` record the following for both `*25*21#1*21##` and `*25*23#8*233##`. These observations are from executed firmware under a simulated PIC, inspected here without rerunning it; they are separate from physical gateway observations.

| Gateway model | Firmware | Recorded socket reply | Recorded bus-output verdict | Original result |
| --- | --- | --- | --- | --- |
| MH200 | `020102` | `NACK` | `silent` - no bus bytes recorded | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/8a61bbeb1d26354241debac84a7310142e5ab3a5/results/MH200/020102/oracle/full/who25-messages.tsv#L18-L19) |
| MH200N | `010108` | `ACK` | `out` - bus bytes recorded | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/8a61bbeb1d26354241debac84a7310142e5ab3a5/results/MH200N/010108/oracle/full/who25-messages.tsv#L18-L19) |
| F453 | `010100` | `ACK` | `out` - bus bytes recorded | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/8a61bbeb1d26354241debac84a7310142e5ab3a5/results/F453/010100/oracle/full/who25-messages.tsv#L18-L19) |
| F454 | `020051` | `ACK` | `out` - bus bytes recorded | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/8a61bbeb1d26354241debac84a7310142e5ab3a5/results/F454/020051/oracle/full/who25-messages.tsv#L18-L19) |
| MH202 | `010024` | `ACK` | `out` - bus bytes recorded | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/8a61bbeb1d26354241debac84a7310142e5ab3a5/results/MH202/010024/oracle/full/who25-messages.tsv#L18-L19) |
| MyHomeServer1 | `028206` | `NACK` | `out` - bus bytes recorded | [Pinned result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/8a61bbeb1d26354241debac84a7310142e5ab3a5/results/MyHomeServer1/028206/oracle/full/who25-messages.tsv#L18-L19) |

All six records declare the full harness, `oracle_version=3`, a simulated PIC responder, `reset=0` and `settle_ms=3000`. The latter is a declared limit, not proof of a complete three-second observation. The upstream [$04 PIC acknowledgement fix](https://github.com/OpenWebNet-HA/own-firmware-oracle/commit/fe0eff552b9b031c692f8e08b428a94ebddf31c2) and [CPU-idle settling change](https://github.com/OpenWebNet-HA/own-firmware-oracle/commit/2e45bfac7e2c4e34b8c8ec3d2779285065ab7d05) explain why the newer comparison must be scoped separately from v1. MH200N and F454 now record ACK with bus output; MH202 now records bus output as well. MyHomeServer1 still records NACK with bus output, so a socket acknowledgement remains distinct from forwarding. Recorded bus bytes do not establish physical execution, and these two CEN+ inputs do not establish acceptance of every WHO 25 operation.

**Physical MH200 capture inspection.** In the [2026-10-22 contributor capture](../../evidence/cap-mh200-who25-boundary-20261022/manifest.json), the identified MH200 firmware 2.1.0 returns NACK for `*25*21#1*21##` after 57.430 ms and `*25*23#8*233##` after 24.200 ms. The first frame uses pushbutton 1 on CEN+ Object 1 (`WHERE 21`); the second uses pushbutton 8 on Object 33 (`WHERE 233`). These are recorded replies to those literal probes on that setup, not a namespace-wide rejection rule. Other families are described separately in [ScenarioPlus controls](README.md#historical-scenarioplus-controls) and [Dry Contact and IR](dry-contact-ir.md#gateway-compatibility-and-hardware-boundaries).

The contributor declared a 2000 ms command/event observation window per probe, and no WHO 25 event frame occurs in the eight recorded probe windows. A physical lighting positive control shows that the event session was live. No WHO 25 transmitter or dry-contact/IR interface was installed or configured, and no independent physical SCS bus capture was made. Incoming WHO 25 event handling and physical bus forwarding therefore remain untested. The raw log does not include an explicit final observation-end marker. We inspected and privacy-projected the contributor recording; we did not run hardware ourselves. The [projection record](../../evidence/cap-mh200-who25-boundary-20261022/projection.json) describes filtering and fingerprints. See the [gateway evidence review](../../project/review/who25-gateway-compatibility.md) for the withdrawn capture, original source hashes and review limits.

**Historical oracle v1 records.** The following superseded harness observations come from the pinned `who25-messages` results at own-firmware-oracle revision `af8ec0ceaff4c82a1a71f2a3ac5d01ad2095de7b`. For both CEN+ inputs `*25*21#1*21##` and `*25*23#8*233##`, the recorded reply and bus-output verdict are:

| Gateway model | Firmware | Recorded socket reply | Recorded bus-output verdict | Original result |
| --- | --- | --- | --- | --- |
| MH200N | `010108` | `NACK` | `out` - bus bytes recorded | [MH200N result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/af8ec0ceaff4c82a1a71f2a3ac5d01ad2095de7b/results/MH200N/010108/oracle/full/who25-messages.tsv#L18-L19) |
| F454 | `020051` | `NACK` | `out` - bus bytes recorded | [F454 result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/af8ec0ceaff4c82a1a71f2a3ac5d01ad2095de7b/results/F454/020051/oracle/full/who25-messages.tsv#L18-L19) |
| MH202 | `010024` | `ACK` | `silent` - no bus bytes recorded | [MH202 result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/af8ec0ceaff4c82a1a71f2a3ac5d01ad2095de7b/results/MH202/010024/oracle/full/who25-messages.tsv#L18-L19) |
| MyHomeServer1 | `028206` | `NACK` | `out` - bus bytes recorded | [MyHomeServer1 result](https://github.com/OpenWebNet-HA/own-firmware-oracle/blob/af8ec0ceaff4c82a1a71f2a3ac5d01ad2095de7b/results/MyHomeServer1/028206/oracle/full/who25-messages.tsv#L18-L19) |

The records declare the full harness, a simulated PIC responder, and `settle_ms=300`; MH200N uses `reset=each`, while the other three use `reset=0`. These are inspected published results, not a new emulator run or a physical-hardware observation. `NACK` with bus output must not be described as proof that the frame never reached the bus, and `ACK` without recorded bus output does not establish physical execution. Neither result determines gateway-wide support or rejection of unrelated `WHO 25` operations. Source hashes and review limits are recorded in the [gateway evidence review](../../project/review/who25-gateway-compatibility.md).

The v1 rows are preserved as historical recording facts. Their response/output combinations must not be used as the current firmware comparison: the later PIC responder and settling fixes changed the harness conditions. The original source fingerprints and claim identities remain traceable.

## Other `WHO 25` functions

`WHO 25` also carries dry-contact and IR functions using `WHAT 31` and `32`. Those operations use different parameters and `WHERE` grammars and are documented in [Dry Contact and IR](dry-contact-ir.md).
