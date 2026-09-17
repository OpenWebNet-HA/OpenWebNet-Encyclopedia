# Verify Programming

## Goal

Prove that the effective installed state matches the intended configuration after the programming session has ended.

## Procedure

1. Preserve the programming result: accepted, warning, rejected, aborted, or timed out.
2. Close the outer programming session when appropriate.
3. Start a new diagnostic interview, preferably by Device ID.
4. Reconfirm `DIMENSION 1` and `DIMENSION 13` identity.
5. Compare the entire `DIMENSION 30` Module/Object layout.
6. Compare all expected `DIMENSION 32` address tuples.
7. Read and compare applicable `DIMENSION 35` properties.
8. Preserve `DIMENSION 310` separately.
9. Compare `DIMENSION 4` and `5` as raw reports until their precise field semantics are established.
10. Classify every intended change independently.

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
