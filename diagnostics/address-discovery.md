# Address Discovery

Address discovery locates or probes a Device through a diagnostic `WHERE`. It is useful when the functional or installation address is known but the Device ID is not.

## Frames

| Purpose | Frame |
| --- | --- |
| Scan one address | `*#[WHO]*[WHERE]*1##` |
| Identity response | `*#[WHO]*[WHERE]*1*[OBJECT_MODEL]*[N_CONF]*[BRAND]*[LINE]##` |
| Start full addressed interview | `*#[WHO]*[WHERE]*0##` |

`OPEN.db` names the repeated scan workflow `ScanAddressed`. It sends the address scan and expects `DIMENSION 1` identity responses. The full addressed interview uses a different start frame and can return the broader diagnostic response set.

## Interpreting `WHERE`

Diagnostic `WHERE` follows the address rules of the selected diagnostic family. It is not one universal integer format and it is not necessarily the only address exposed by the Device.

For Lighting and Automation, a Device can contain multiple Modules with different functional `A`/`PL` addresses. `DIMENSION 32` reports those per-internal-slot addresses. The address used to find or interview the Physical Device must therefore be kept distinct from the Module addresses learned during the interview.

Observed `WHO 1001` captures suggest that the diagnostic `WHERE` commonly corresponds to the configured address of internal slot `1`. The observation is useful for implementation testing but is not sufficient to define a universal rule for every Object layout, Device, or diagnostic family.

## Scan procedure

1. Choose the diagnostic `WHO` from an established system mapping.
2. Generate only `WHERE` values valid for that family’s address rule.
3. Send `*#[WHO]*[WHERE]*1##` for each candidate.
4. Collect the `DIMENSION 1` response, if any.
5. Preserve the queried `WHERE`, returned identity fields, and raw frame together.
6. Use an ID-based interview when `DIMENSION 13` later supplies a stable Device identity.

Silence can mean no Device, an unsupported diagnostic operation, an invalid address for the selected family, transport loss, or a Device that is temporarily unavailable. Do not collapse these cases into a positive “address unused” result without retry and timeout policy.

## Range and safety

Address ranges belong to the selected system. For example, CEN virtual identifiers occupy `0`–`2047`, while Lighting/Automation point-to-point addresses are interpreted as `A`/`PL`. The numeric capacity of a database parameter is not itself permission to probe every value.

Avoid broad address sweeps on live installations unless the transport and Device behavior are understood. Prefer ID enumeration when the diagnostic family supports it, because enumeration does not require inventing candidate functional addresses.

## Identity resolution

The returned `OBJECT_MODEL`, `BRAND`, and `LINE` can be correlated with catalogue fields as documented in [`dim1-device-identity.md`](dim1-device-identity.md). `N_CONF` remains unresolved and must not be used to infer a Module, Object, or product form factor.
