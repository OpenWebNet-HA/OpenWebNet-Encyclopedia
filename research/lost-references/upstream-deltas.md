# Upstream OpenWebNet deltas

## WHO 1 version 1.2

Legrand's current Local Interoperability page serves `WHO_1.pdf` version 1.2 dated 2024-06-01.

- SHA-256: `662ad5bd8817c5732afc1ce0cca17436d47d44fcb422cb2fcb28ee1208de12c5`
- Archived publicly in `openwebnet-documents`.
- This revision contains an explicit WHO 14 section with disable/enable WHAT values and command/event examples.
- Its WHO 1 WHAT table still skips value 19: values 18 and 20 are adjacent.
- Do not silently replace the current canonical source until the revision has been diffed against the previously archived WHO 1 document and affected Encyclopedia claims reviewed.

## Official Open Web Net test clients

Legrand's current Local Interoperability page still distributes Windows and macOS Open Web Net Client packages. Both were recovered from the live publisher URLs and archived privately in `openwebnet-software`.

## First-party integration manuals recovered

The recovery pass also preserved first-party BTicino/Legrand software manuals that expose practical OPEN/OpenWebNet configuration behavior beyond the standalone WHO PDFs:

- MHVISUAL installation manual - guided and raw OPEN command construction, including controlled loads, video door entry, sound, temperature control, and custom frames.
- Legrand Scheduler Config manual - OPEN command blocking and scenario-programmer integration.
- TiF453 software manual - gateway configuration and OPEN command filtering.
- TiMH200N software manual - OPEN command filtering and multi-system/interface configuration.

These manuals are supporting implementation evidence. They do not replace the dedicated functional specifications.


## F459 Driver Manager OpenWebNet configuration

Two first-party F459 documents were recovered from BTicino and archived:

- `MM00883-a-EN.pdf` - product technical sheet.
- `RA00147AA_I_EN.pdf` - 48-page F459 / 003549 Installation Manual.

The installation manual explicitly documents the OPEN password, optional HMAC authentication, trusted-IP ranges, and MyHOME/SCS integration. It is supporting gateway/configuration evidence rather than a replacement for the protocol specifications.


## Historical TiMH200 revision

`TiMH200_FR_STAMPA.pdf` version 1.0 (2005) was recovered from BTicino's support archive and preserved. The later version 2.0 bytes were already present in the artifact corpus as `TiMH200_FR.pdf`.

Version 1 documents the early MH200 Scenario Scheduler configuration workflow and firmware-update tooling. Version 2 later added Ethernet/remote configuration and OPEN-password related controls, so retaining both revisions is useful for historical implementation comparison.
