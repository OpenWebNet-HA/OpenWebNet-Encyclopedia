# `WHO 10` — Navigation Commands

The MyHOME_Suite `OPEN.db` system definitions identify `WHO 10` as Navigation commands.

## Corpus status

The namespace is established directly by the implementation model, but the integrated corpus does not yet establish a complete public or implementation-level `WHAT`, `WHERE`, and `DIMENSION` vocabulary.

## Interpretation rule

Navigation is treated as its own protocol namespace. Numeric operations must not be borrowed from multimedia track navigation, CEN button events, or user-interface assumptions merely because those domains also contain directional concepts.

A generic decoder should preserve unknown `WHO 10` frames losslessly and expose their fields as raw values until command semantics are supported by MyHOME_Suite data or captures. This allows future refinement without having to undo speculative labels.

No dedicated `WHO 10` PDF is present in the canonical public corpus used by this repository.