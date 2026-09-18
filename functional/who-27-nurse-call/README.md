# `WHO 27` - Nurse Call Basic Level

MyHOME Suite `OPEN.db` identifies functional `WHO 27` as Nurse Call basic level and assigns diagnostic family `WHO 1027`.

## Evidence boundary

The current public corpus contains no dedicated `WHO 27` functional specification. `OPEN.db` marks the system `managed = 0`, so it does not establish a normal managed-Device workflow or an ordinary functional `WHAT` table.

Nevertheless, nine `EN_OPEN` records are associated with the system. They cover password challenge/result handling, general diagnostic requests and masks, automatic diagnostic events, WebServer model identification, and MAC-address retrieval.

Those records establish a concrete service/diagnostic surface. Most are parameterized by `[WHO]`; substitution and session context must be resolved from the database workflow before assigning them to functional `WHO 27` or diagnostic `WHO 1027`. They must not be presented as an invented Nurse Call functional vocabulary.

## Decoder guidance

- Recognize `WHO 27` as Nurse Call basic level.
- Preserve unknown functional fields losslessly.
- Treat `WHO 1027` as a distinct diagnostic namespace.
- Do not infer room, bed, call-state, acknowledgement, or alarm values from the application domain.
- Use the associated service templates only in the context established by their `OPEN.db` sequence and parameter records.

## Evidence basis

The namespace name, diagnostic-family assignment, management flag, and associated service records come from `OPEN.db`. See [MyHOME Suite `OPEN.db` Coverage](../open-db-coverage.md) for the exact templates and [Functional Source Coverage](../source-coverage.md) for the absence rule.
