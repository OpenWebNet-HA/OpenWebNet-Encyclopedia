# Verify Programming

## Goal

Prove that the effective installed state matches the intended configuration after the programming session has ended.

## Acquire the verification frames

1. Preserve the programming result: accepted, warning, rejected, aborted, or timed out.
2. Close the outer programming session with `*[WHO]*2*0##` when the canonical workflow reaches close.
3. Start an independent diagnostic interview, preferably with `*[WHO]*10#[ID]*0##`. Use `*#[WHO]*[WHERE]*0##` only when address selection is required.
4. Collect the interview projection through Device `WHAT 4` or a classified timeout.
5. After resolving the returned Module/Object layout, send `*#[WHO]*0*38#0##`.
6. Collect repeated `DIMENSION 35` and any `DIMENSION 310` response during the detailed-read window.

## Compare the effective state

1. Reconfirm `DIMENSION 1` and `DIMENSION 13` identity.
2. Compare the entire `DIMENSION 30` Module/Object layout.
3. Compare all expected `DIMENSION 32` address tuples.
4. Compare the newly requested `DIMENSION 35` properties.
5. Preserve `DIMENSION 310` separately.
6. Compare `DIMENSION 4` and `5` as raw reports until their precise field semantics are established.
7. Classify every intended change independently.

## Result classes

| Result | Meaning |
| --- | --- |
| verified | effective state matches |
| verified with warnings | state matches but programming reported nonfatal omissions |
| contradicted | read-back differs |
| unverifiable | the Device did not report the relevant optional value |
| indeterminate | identity, timeout, or transport state prevents comparison |

After advanced Object programming, verify the whole Module layout because the canonical sequence resets all Objects before rebuilding them.

A positive protocol result is not diagnostic proof. Conversely, a missing optional response does not establish failure.

See [Programming Verification](../programming/verification.md).
