# Device Catalogue Evidence

This directory retains supplementary catalogue associations used by accepted [Device Definitions](../definitions/). The [Complete Device Index](../index.md) provides commercial lookup; each definition owns its technical capability and source reconciliation.

## Source scope

The implementation evidence is the canonical [MyHOME Suite catalogue](../../sources/myhome-suite/3.5.38/databases/), version `3.5.38`, with SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. The database original is restricted archive material; the public source record describes its provenance.

| Source measure | Count |
| --- | ---: |
| Commercial records in `EN_DEVICE` | 541 |
| Technical items referenced by those records | 210 |
| Catalogue brand labels | 4 |
| Catalogue product-line labels | 18 |
| Commercial records with the catalogue gateway flag | 7 |
| Technical items shared by multiple commercial records | 144 |
| Commercial records belonging to shared items | 475 |

These are catalogue counts, not a current sales inventory or a count of observed Physical Devices. In particular, the gateway flag is source metadata rather than an exhaustive classification of OpenWebNet gateways. See [Gateways and Interfaces](../categories/gateways-and-interfaces.md) for the evidence-qualified gateway roles.

Explicit `EN_DEVICE` SKU-to-`EN_ITEM` associations establish catalogue identities. Shared technical-item membership does not establish identical physical construction, installed Firmware or every product-document statement across the group. Catalogue Firmware and direct or Virgin Object associations describe scoped capability; they do not establish an installed Configuration. The [Device Model](../../device-model/) defines these boundaries.

## Retained supplementary associations

[Touch screen package Unicode ranges](touch-screen-package-unicode-ranges.json) retains all 4534 canonical set/range associations used by the [BTicino Multimedia Touch Screen](../definitions/own-dev-0102-multimedia-touch-screen.md) and [Legrand Multimedia Touch Screen](../definitions/own-dev-0107-legrand-multimedia-touch-screen.md). It describes catalogue package metadata; package payloads and installed releases remain unexamined.

The raw commercial and technical-item draft tables have been retired after curation. Their source and review history remain available through the catalogue record, accepted definitions and [Device acceptance ledger](../work-queue.yaml). Maintainer exports can be produced outside the public repository using the [Device maintenance tools](../contributing/README.md#maintenance-tools).
