# Address Discovery

Address discovery locates or probes a Device through a diagnostic `WHERE`. It is useful when the functional or installation address is known but the Device ID is not.

## Frames

| Purpose | Frame |
| --- | --- |
| Scan one address | `*#[WHO]*[WHERE]*1##` |
| Identity response | `*#[WHO]*[WHERE]*1*[OBJECT_MODEL]*[N_CONF]*[BRAND]*[LINE]##` |
| Start full addressed interview | `*#[WHO]*[WHERE]*0##` |

`OPEN.db` additionally defines two specialized scan templates:

| Scope | Frame | Database association |
| --- | --- | --- |
| Lighting/Automation room/area | `*#[WHO]*[A]*1##` | general Light/Automation address rule |
| Thermoregulation zone | `*#[WHO]*00[ZAZB]*1##` | general Thermoregulation address rule |

`OPEN.db` names the repeated scan workflow `ScanAddressed`. It sends the generic address scan and expects repeated `DIMENSION 1` identity responses. `ScanAreaTimeWait` gives this step an eight-second default window before advancing to the next area or zone.

The full addressed interview uses a different start frame and can return the broader diagnostic response set. In the higher-level `ScanPlant` scenario, MyHOME_Suite follows discovery with repeated addressed interviews, detailed configuration reads, and close operations.

## Interpreting `WHERE`

Diagnostic `WHERE` follows the address rules of the selected diagnostic family. It is not one universal integer format and it is not necessarily the only address exposed by the Device.

For Lighting and Automation, a Device can contain multiple Modules with different functional `A`/`PL` addresses. `DIMENSION 32` reports those per-`slot` addresses. The address used to find or interview the Physical Device must therefore be kept distinct from the Module addresses learned during the interview.

Observed `WHO 1001` captures suggest that the diagnostic `WHERE` commonly corresponds to the configured address of `slot` `1`. The observation is useful for implementation testing but is not sufficient to define a universal rule for every Object layout, Device, or diagnostic family.

## Scan procedure

1. Choose the diagnostic `WHO` from an established system mapping.
2. Generate only `WHERE` values valid for that family’s address rule.
3. Send `*#[WHO]*[WHERE]*1##` for each candidate.
4. Collect the `DIMENSION 1` response, if any.
5. Preserve the queried `WHERE`, returned identity fields, and raw frame together.
6. Use an ID-based interview when `DIMENSION 13` later supplies a stable Device identity.

Silence can mean no Device, an unsupported diagnostic operation, an invalid address for the selected family, transport loss, or a Device that is temporarily unavailable. Do not collapse these cases into a positive “address unused” result without retry and timeout policy.

## Address rules in `OPEN.db`

The diagnostic family selects the system; the system and, in several cases, the Device/Object family select the address rule.

| Diagnostic family | Target class | Virtual form | Advanced form |
| ---: | --- | --- | --- |
| `1001` | Lighting/Automation general | `[A][PL]` | `[A][PL]+` |
| `1001` | F422 logic/physical extension | `[I3][I4]` | `[I3][I4]+` |
| `1004` | Thermoregulation general | `[ZA][ZB]` | `[ZAZB]` |
| `1004` | four-zone control unit | `#0#[ZA][ZB]` | `#0#[ZAZB]` |
| `1004` | actuator | `[ZA][ZB]#[N]` | `[ZAZB]#[N]` |
| `1004` | slave probe | `[SLA][ZA][ZB]` | `[SLA][ZAZB]` |
| `1004` | external probe | `[PL_N]00` | `[PL_N]00` |
| `1008` | public-riser interface | `1[I1][I2][I3][I4]` | `1[I1I2I3I4]` |
| `1013` | burglar-alarm interface | `[I4]` | `[I4]` |
| `1013` | galvanic/new physical separation | `[I4]` | `[I4]` |
| `1018` | control unit/measurement target | `5[A1][A2][A3]` | `5[A123]` |
| `1018` | actuator | `7[P1][P2]#0` | `7[P]#[PHASE]` |
| `1023` | command or virgin Device | `20` | `20` |
| `1023` | indicator | `7[R1][R2]` | `7[R1R2]` |

The table reproduces MyHOME_Suite’s address-rule vocabulary. It does not claim that every rule is valid for every Object in the family. `object_device_family`, validity conditions, and offsets further qualify several entries.

`OPEN.db` provides no system address rule for every diagnostic family named in `EN_SYSTEM`; absence of a rule is not permission to reuse `A`/`PL`.

## Range and safety

Address ranges belong to the selected system. The numeric capacity of a database parameter is not itself permission to probe every value, and the visible string grammar can include fixed prefixes, family selectors, or `#` components.

Avoid broad address sweeps on live installations unless the transport and Device behavior are understood. Prefer ID enumeration when the diagnostic family supports it, because enumeration does not require inventing candidate functional addresses.

## Identity resolution

The returned `OBJECT_MODEL`, `BRAND`, and `LINE` can be correlated with catalogue fields as documented in [`DIMENSION 1`: Device Identity](dim1-device-identity.md). `N_CONF` represents the number of physical configurator positions provided by the Device. It is a hardware-interface characteristic and must not be confused with Module count, Object identity, logical configuration parameters, or product form factor. See [`DIMENSION 1`: Device Identity](dim1-device-identity.md) for the evidence and interpretation.

Address rules come from `OPEN.db`; product identity comes from `MHCatalogue.db`. Equal internal system IDs across those databases must not be joined. See [Sources and Identifier Boundaries](../device-model/sources-and-identifiers.md).
