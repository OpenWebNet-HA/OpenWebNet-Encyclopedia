# Overview

The MyHOME_Suite `OPEN.db` system definitions identify `WHO 27` as Nurse Call basic level.

## Corpus status

The namespace is directly established by the implementation data. The currently integrated corpus does not, however, establish a complete ordinary functional `WHAT`, `WHERE`, or `DIMENSION` vocabulary at the level required for an implementation table.

## Implementation guidance

A parser should recognize `WHO 27` as Nurse Call and preserve subsequent fields losslessly. Unknown values remain raw protocol values until their semantics are supported by MyHOME_Suite data, a canonical specification, or observed traffic.

The phrase “basic level” is retained from the MyHOME_Suite system definition; it is not expanded here into inferred call-state, room, bed, acknowledgement, or alarm semantics. Those concepts may be plausible for a nurse-call system but are not established by the current corpus.

This evidence boundary prevents application-domain expectations from becoming undocumented protocol claims.