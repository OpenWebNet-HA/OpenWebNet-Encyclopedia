# Programming Architecture

The programming protocol connects an installed Physical Device to the catalogue configuration model and requests changes to its runtime state.

## Scope

This page will define:

- programmer and Device roles;
- programming `WHO` families;
- Device-level and Module-level operations;
- relationships among Object selection, addressing, and configuration parameters;
- acknowledgement and error surfaces;
- boundaries between validation, transmission, and verification.

## Evidence layers

| Source | Contribution |
| --- | --- |
| `OPEN.db` | frame templates, parameters, direction, sequences, errors, and timeouts |
| `OpenQuery.txt` | MyHOME_Suite queries and sequence assembly |
| `MHCatalogue.db` | firmware, slots, Objects, Virgin Objects, configuration definitions, and constraints |
| `rules.db3` | selected cross-property validation |
| Observed traffic | actual ordering, repetition, optionality, and termination |
| MyHOME_Suite UI | user-visible choices, editability, and workflow state |

Programming frames do not expose catalogue primary keys merely because the application uses catalogue data to construct them. Each identifier correlation must be established independently.
