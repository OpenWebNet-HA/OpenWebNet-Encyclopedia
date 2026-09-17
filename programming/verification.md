# Programming Verification

Verification reads the Device again after programming and compares the effective installed state with the intended result.

## Procedure

1. Establish how the programming session ended.
2. Start a new diagnostic interview.
3. confirm Physical Device identity.
4. Compare configured Objects and Virgin Objects through `DIMENSION 30`.
5. Compare effective addresses through `DIMENSION 32`.
6. Compare indexed parameters through `DIMENSION 35`.
7. Retain special Object values separately.
8. Record missing or unsupported read-back data.
9. Classify the requested change as verified, contradicted, or unverifiable.

An accepted programming frame is evidence that the Device accepted an operation, not proof that every requested value became the effective installed state.
