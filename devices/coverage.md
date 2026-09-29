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
| `OWN-DEV-0003` | Flush-mounted two-relay actuator and free control | Substantially complete for current canonical catalogue | Partial - 9-item cluster identified; 3 Arnould references document-correlated | Partial - archive pending | Complete at catalogue level | Unknown - fingerprint pending | Complete for current catalogue | Substantially complete | Partial - irregular/unreachable condition branches need experimental validation |
| `OWN-DEV-0004` | Two-module basic control | Complete for current canonical catalogue | Partial - 19 records identified; 4 directly document-correlated | Partial - one official sheet identified; archive pending | Complete at catalogue level | Unknown - fingerprint pending | Complete for current sources | Complete for current catalogue and identified PDF | Partial - commercial variants and hardware corroboration pending |
| `OWN-DEV-0005` | Two-module special control | Complete for current canonical catalogue | Partial - 13 records identified; 4 directly document-correlated | Partial - one official sheet identified; archive pending | Complete at catalogue level | Unknown - fingerprint pending | Complete for current sources | Complete for current catalogue and identified PDF | Partial - commercial variants and hardware corroboration pending |
| `OWN-DEV-0006` | Two-module zero-crossing actuator and control | Complete for current canonical catalogue | Complete for 7-record item cluster in current official sheet | Partial - four official documents archived; older revisions may exist | Complete at catalogue level | Unknown - fingerprint pending | Complete for current sources | Complete for current catalogue and 2021 technical sheet | Partial - hardware corroboration and source-model irregularities remain |
| `OWN-DEV-0007` | Three-module basic control | Complete for current canonical catalogue | Partial - 6 records identified; 4 directly document-correlated | Partial - four official documents archived; other commercial variants need sources | Complete at catalogue level | Unknown - fingerprint pending | Complete for current sources | Complete for current catalogue and identified sheets | Partial - commercial variants and hardware corroboration pending |
| `OWN-DEV-0008` | Flush-mounted one-relay actuator | Complete for current canonical catalogue | Partial - 6 records identified; 4 directly document-correlated | Partial - technical sheet and PEP archived | Complete at catalogue level | Unknown - fingerprint pending | Complete for current sources | Complete for current catalogue and identified sheet | Partial - M=2 source discrepancy and hardware corroboration remain |
| `OWN-DEV-0009` | Four-zone touch multifunction control | Complete for current canonical catalogue | Partial - 15 records identified; 7 have direct catalogue/compatibility documentation | Partial - technical sheet, instructions, catalogue and compatibility table archived | Complete at catalogue level | Unknown - fingerprint pending | Complete for current database source | Complete for current database and documented Arteor functions | Partial - physical SPE/SET mapping and remaining commercial variants unresolved |
| `OWN-DEV-0010` | PIR+US daylight and presence sensor | Complete for current canonical catalogue | Complete - all 12 records named by current official sheet | Substantially complete - 2014 and 2024 EN/FR sheets plus current instructions archived | Complete at catalogue level | Unknown - fingerprint pending | Complete for current sources | Complete for current database and archived sheets | Partial - hardware corroboration and revision boundary remain |
| `OWN-DEV-0011` | Scenario control | Complete for current canonical catalogue | Partial - principal 12 printed identities documented; 2 Mosaic references remain implementation-only | Partial - EN/FR sheets and instruction guide archived | Complete at catalogue level | Unknown - fingerprint pending | Complete for current sources | Complete for current database and published scenario model | Partial - Mosaic documentation and hardware corroboration remain |
| `OWN-DEV-0012` | Four-channel IR receiver | Complete for current canonical catalogue | Partial - principal 10 printed identities documented; 2 Mosaic references remain implementation-only | Partial - EN/FR/IT technical sheets archived | Complete at catalogue level | Unknown - fingerprint pending | Complete for current sources | Complete for current database and published modes | Partial - Mosaic documentation and hardware corroboration remain |

“Complete” is always scoped to the named source revision. New database revisions, documents, firmware, or observations may add knowledge without making the earlier extraction incorrect.
