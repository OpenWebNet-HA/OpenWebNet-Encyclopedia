# Device Coverage

This index tracks the current state of product-specific documentation and research.

It is both a navigation aid and a research backlog. A missing or incomplete entry does not mean that a product is unsupported by OpenWebNet.

Coverage is tracked by technical Device definition rather than by choosing one commercial SKU as canonical. The [Complete Device Index](index.md) provides the exhaustive brand / SKU lookup.

## Coverage fields

| Field | Meaning |
| --- | --- |
| Database extraction | Device-specific identity, firmware, Module/Object, configuration, conditions, and constraints available from canonical implementation sources have been curated |
| Commercial identities | Known brand / SKU identities and package/synonym relationships are documented |
| Official sources | Authoritative product documents are inventoried and archived where appropriate |
| Identity | Protocol/catalogue identity mapping is documented |
| Hardware evidence | At least one observation from known physical hardware exists |
| Functions | Modules, Objects, roles, and relevant functional systems are documented |
| Configuration | Supported configuration methods and parameter domains are documented |
| Constraints | Material configuration ranges, conditions, conversion constraints, and source irregularities are documented |

Use **Complete**, **Partial**, **Unknown**, or **Not applicable** where a simple yes/no would hide important gaps.

## Device definitions

| Device ID | Description | Database extraction | Commercial identities | Official sources | Identity | Hardware evidence | Functions | Configuration | Constraints |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `OWN-DEV-0001` | Two-channel universal dimmer | Complete for current canonical catalogue | Complete for known F418U2 / 003651 mapping | Partial - archive pending | Complete at catalogue level | Partial - runtime behavior observed, full fingerprint pending | Complete for current sources | Substantially complete | Partial - firmware-specific filters/corroboration remain |
| `OWN-DEV-0002` | Audio/video web server and OpenWebNet gateway | Complete for current canonical catalogue | Complete for known F454 / 003598 mapping | Partial - archive pending | Corroborated by capture | Partial - identity/gateway behavior observed | Complete for current sources | Complete for current catalogue fields | Partial - gateway unknowns remain |
| `OWN-DEV-0003` | Flush-mounted two-relay actuator and free control | Substantially complete for current canonical catalogue | Complete for known 64391 / 64191 / 64192 mapping | Partial - archive pending | Complete at catalogue level | Unknown - fingerprint pending | Complete for current catalogue | Substantially complete | Partial - irregular/unreachable condition branches need experimental validation |

“Complete” is always scoped to the named source revision. New database revisions, documents, firmware, or observations may add knowledge without making the earlier extraction incorrect.
