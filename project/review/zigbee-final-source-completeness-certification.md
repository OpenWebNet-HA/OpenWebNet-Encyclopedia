# ZigBee Final Source Completeness Certification

This record is the Step 3 source-to-documentation completeness audit for the Legrand ZigBee OpenWebNet specification, version 4.0 dated 22 November 2016. It is governed by the [Encyclopedia Core Values](../encyclopedia-core-values.md) and [Encyclopedia Style Guide](../encyclopedia-style-guide.md).

The primary source is the repository copy of the [ZigBee OpenWebNet Specification](../../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf). The audited file is 929707 bytes, Git blob SHA `773288d33cc55b2a9ecf74e9e9bd886736edab9b`, and SHA-256 `9f7d430ced634a333b598f99c165efa3c71f226f7397b950407f601f597c5776`. The document is 60 pages long. It carries Confidential footers, and its public-release provenance remains unresolved. It is therefore specification evidence for the particular interface revision it describes, not proof of tested interoperability, universal ZigBee behavior, or support by every gateway, product, or firmware revision.

The source also states that points to be confirmed in its draft form are highlighted in yellow. Yellow sequence-diagram notes on page 19 were checked visually. No canonical rule in this audit depends solely on a yellow-only statement: the promoted product-information timing, power-category, and product-database behaviors are independently repeated in ordinary text or detailed operation tables.

## Audit method

The PDF was read sequentially from page 1 through page 60. Every page was rendered and visually inspected, including the product-database sequence diagrams, and its text layer was cross-checked against the current `zigbee-reconciliation` documentation. Step 1 and Step 2 results were reused as authoritative reviewed work and were reopened only where the final source-wide pass exposed a concrete omission, a stale completion statement, or a classification that needed confirmation.

Every substantive source item below is assigned to exactly one of the six required states:

1. **Documented canonically**
2. **Documented with an explicit unresolved contradiction**
3. **Already represented by a canonical cross-cutting rule**
4. **Intentionally out of OpenWebNet scope**
5. **Source-only contextual material that requires no separate canonical documentation**
6. **Missing and requiring remediation**

No item remains in state 6 at certification time. Items found missing during this audit are marked as remediated in the Action column and now end in state 1.

## Source-to-documentation coverage matrix

| ID | Source section/page | Source subject | Protocol primitive or behavior | Current canonical location | Evidence/applicability state | Coverage status | Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ZB-001 | p. 1 | Version and validation metadata | Version 4.0, 22 November 2016 | [ZigBee Interface](../../protocol/zigbee-interface.md) and this record | Source identity | Documented canonically | Retained as source-bounding metadata |
| ZB-002 | p. 1 and all pages | Confidential footer | Publication provenance qualification | [Source-Coverage Audit](phase-3-source-coverage.md) and canonical ZigBee pages | Provenance unresolved | Documented canonically | Qualification preserved |
| ZB-003 | pp. 2-4 | Table of contents | Source navigation only | This record | Context only | Source-only contextual material that requires no separate canonical documentation | Pages accounted for as navigation |
| ZB-004 | p. 5, section 1 | Interface purpose | COM-managed application interaction with ZigBee Legrand products | [ZigBee Interface](../../protocol/zigbee-interface.md) | Interface-specific specification evidence | Documented canonically | Scope retained without universalizing |
| ZB-005 | p. 5, section 1 | Draft note | Yellow-highlighted points are to be confirmed | This record | Source self-qualification | Documented canonically | Visual audit checked highlighted material |
| ZB-006 | p. 6, section 2.1 | USB hardware | EM3582-based USB interface, buttons and LEDs | This record | Hardware context | Source-only contextual material that requires no separate canonical documentation | No radio/hardware control model promoted |
| ZB-007 | p. 7, section 2.2 | UART daughterboard hardware | EM3581-based interface, buttons and LEDs | This record | Hardware context | Source-only contextual material that requires no separate canonical documentation | No separate protocol page required |
| ZB-008 | p. 8, section 2.3.1 | Host driver reference | Silicon Labs host-PC driver setup | This record | Host/driver implementation context | Intentionally out of OpenWebNet scope | External driver mechanics excluded |
| ZB-009 | p. 8, section 2.3 | Serial base settings | 19200 baud, 8 data bits, 1 stop bit, no parity | [ZigBee Interface](../../protocol/zigbee-interface.md) | Interface v4.0 transport evidence | Documented canonically | Verified |
| ZB-010 | p. 8, section 2.3 | Optional USB rate | Source says USB can increase to 115200 baud | [ZigBee Interface](../../protocol/zigbee-interface.md) | Optional capability; negotiation and revision applicability unspecified | Documented canonically | **Remediated in Step 3** |
| ZB-011 | p. 9, section 3 | Frame delimiters | Frames begin with `*` and end with `##` | [Frame Syntax](../../protocol/frame-syntax.md) | Shared OpenWebNet syntax | Already represented by a canonical cross-cutting rule | No duplicate definition added |
| ZB-012 | p. 9, section 3.1 | `WHO` registry | `1, 2, 4, 13, 18, 25, 1000` | [ZigBee Interface](../../protocol/zigbee-interface.md) | ZigBee interface registry | Documented canonically | Namespace isolation retained |
| ZB-013 | p. 9, section 3.2 | `WHAT` role | Operation meaning selected within `WHO` | [`WHAT`](../../protocol/what.md) | Shared structural rule | Already represented by a canonical cross-cutting rule | Functional meanings remain variant-specific |
| ZB-014 | p. 9, section 3.3 | Unicast `WHERE` | Product decimal component + two-character Unit + `#9` | [ZigBee Interface](../../protocol/zigbee-interface.md) | ZigBee-specific addressing | Documented canonically | Exact structure retained |
| ZB-015 | p. 9, section 3.3 | Multicast transmission prefix | `#`, explicitly not implemented in this source revision | [ZigBee Interface](../../protocol/zigbee-interface.md) | Source limitation | Documented canonically | No support inferred |
| ZB-016 | p. 9, section 3.3 | Broadcast `WHERE` | `0#UNIT#9` | [ZigBee Interface](../../protocol/zigbee-interface.md) | ZigBee-specific addressing | Documented canonically | Verified |
| ZB-017 | p. 9, section 3.3 | Broadcast all Units | Unit `00` selects all Units | [ZigBee Interface](../../protocol/zigbee-interface.md) | ZigBee-specific addressing | Documented canonically | Verified |
| ZB-018 | p. 9, section 3.3 | Unit width | Unit is always two characters | [ZigBee Interface](../../protocol/zigbee-interface.md) | ZigBee-specific addressing | Documented canonically | Verified |
| ZB-019 | p. 9, section 3.3 | Product component | Last four MAC-address bytes represented in decimal | [ZigBee Interface](../../protocol/zigbee-interface.md) | Address derivation, not identity equivalence | Documented canonically | Kept separate from Suite Physical Device IDs |
| ZB-020 | p. 9, section 3.3 | System suffix | `SYS = #9` for this ZigBee family | [ZigBee Interface](../../protocol/zigbee-interface.md) | Variant marker | Documented canonically | Not equated with Suite `SYS` payload fields |
| ZB-021 | p. 9, section 3.3 | Broadcast rate limit | No more than one broadcast per second | [ZigBee Interface](../../protocol/zigbee-interface.md) | Interface-specific limit | Documented canonically | Verified |
| ZB-022 | p. 9, section 3.3 | Broadcast overload consequence | Excess broadcasting can cause missed traffic during the next 8 seconds | [ZigBee Interface](../../protocol/zigbee-interface.md) | Interface-specific source warning | Documented canonically | **Remediated in Step 3** |
| ZB-023 | p. 10, section 3.4 | `DIMENSION` role | Property/query/write selector within `WHO` | [`DIMENSION`](../../protocol/dimensions.md) | Shared structural rule | Already represented by a canonical cross-cutting rule | No ZigBee-only duplicate |
| ZB-024 | p. 10, section 3.5 | `WHEN` | Source says it is never used | [ZigBee Interface](../../protocol/zigbee-interface.md) | Interface-specific grammar limit | Documented canonically | **Remediated in Step 3** |
| ZB-025 | p. 10, section 3.6 | Command/status form | `*WHO*WHAT*WHERE##` | [Frame Syntax](../../protocol/frame-syntax.md) | Shared structural rule | Already represented by a canonical cross-cutting rule | Verified against source |
| ZB-026 | p. 10, section 3.6 | Status request form | `*#WHO*WHERE##` | [Frame Syntax](../../protocol/frame-syntax.md) | Shared structural rule | Already represented by a canonical cross-cutting rule | Verified |
| ZB-027 | p. 10, section 3.6 | Flat `DIMENSION` request | `*#WHO*WHERE*DIMENSION##` | [`DIMENSION`](../../protocol/dimensions.md) | Shared structural rule | Already represented by a canonical cross-cutting rule | Verified |
| ZB-028 | p. 10, section 3.6 | Parameterized `DIMENSION` request | `DIMENSION#PARAM...##` | [`DIMENSION`](../../protocol/dimensions.md) | Shared structural rule | Already represented by a canonical cross-cutting rule | Verified |
| ZB-029 | p. 10, section 3.6 | Parameterized response/report | Selector parameters followed by `*VALUE...` | [`DIMENSION`](../../protocol/dimensions.md) | Shared structural rule | Already represented by a canonical cross-cutting rule | Verified |
| ZB-030 | p. 10, section 3.6 | Flat response/report | `DIMENSION*VALUE...##` | [`DIMENSION`](../../protocol/dimensions.md) | Shared structural rule | Already represented by a canonical cross-cutting rule | Verified |
| ZB-031 | p. 10, section 3.6 | Flat write | `*#WHO*WHERE*#DIMENSION*VALUE...##` | [`DIMENSION`](../../protocol/dimensions.md) | Shared structural rule | Already represented by a canonical cross-cutting rule | Verified |
| ZB-032 | p. 10, section 3.6 | Parameterized write | `#DIMENSION#PARAM...*VALUE...##` | [`DIMENSION`](../../protocol/dimensions.md) | Shared structural rule | Already represented by a canonical cross-cutting rule | Verified |
| ZB-033 | p. 10, section 3.7 | `ACK` | `*#*1##`, one result per command; also sequence terminator where defined | [ZigBee Interface](../../protocol/zigbee-interface.md) and [Acknowledgements](../../protocol/acknowledgements.md) | ZigBee interface plus shared acknowledgement rule | Documented canonically | Verified |
| ZB-034 | p. 10, section 3.8 | `NACK` | `*#*0##`, incorrect/unsupported or nonexistent target | [ZigBee Interface](../../protocol/zigbee-interface.md) and [Acknowledgements](../../protocol/acknowledgements.md) | Interface-specific failure examples | Documented canonically | Verified |
| ZB-035 | p. 10, section 3.9 | BUSY NACK | `*#*6##` | [ZigBee Interface](../../protocol/zigbee-interface.md) | ZigBee interface result | Documented canonically | Verified |
| ZB-036 | pp. 10-11 | BUSY retry behavior | BUSY followed by NACK; wait 500 ms and resend same frame | [ZigBee Interface](../../protocol/zigbee-interface.md) | ZigBee interface retry rule | Documented canonically | Verified; not generalized to TCP/SCS |
| ZB-037 | p. 11 | Unicast examples | Lighting and Automation examples illustrating `WHERE` | [ZigBee Interface](../../protocol/zigbee-interface.md) | Examples only | Source-only contextual material that requires no separate canonical documentation | Real-looking identifiers are not reproduced |
| ZB-038 | p. 11 | Broadcast examples | Lighting and Automation broadcast examples | [ZigBee Interface](../../protocol/zigbee-interface.md) | Examples only | Source-only contextual material that requires no separate canonical documentation | Grammar documented symbolically |
| ZB-039 | p. 11 versus pp. 36-38 | Automation Up example | Page 11 uses `WHAT 2` for Up; detailed Automation uses `WHAT 1` | [ZigBee Automation Variant](../../functional/who-2-automation/zigbee-variant.md) | Source-internal conflict | Documented with an explicit unresolved contradiction | Retained; not resolved by SCS analogy |
| ZB-040 | p. 12, section 4 | Legrand ZigBee MSP | Underlying manufacturing-specific radio profile | This record | Radio-layer context | Intentionally out of OpenWebNet scope | Only interface applicability is retained |
| ZB-041 | p. 12, section 4 | Compatibility limit | Only products compatible with the source's ZigBee network 2.1 profile are manageable | [ZigBee Interface](../../protocol/zigbee-interface.md) | Interface applicability constraint | Documented canonically | **Remediated in Step 3** |
| ZB-042 | p. 12, section 4 | Supervisor deployment recommendation | Normally one OpenWebNet supervisor; more can reduce radio performance | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Interface/network deployment constraint | Documented canonically | Kept variant-specific |
| ZB-043 | p. 12, section 4 | Product categories | `ZR` mains-powered router; `ZED` battery-powered end Device | [ZigBee Interface](../../protocol/zigbee-interface.md) | Source-defined categories | Documented canonically | Not mapped to Suite Device taxonomy |
| ZB-044 | p. 12, section 4 | Product hardware anatomy | NPB/NLED/LPB/LLED/APB/ALED | This record | Hardware context | Source-only contextual material that requires no separate canonical documentation | Not promoted as OpenWebNet fields |
| ZB-045 | p. 13, section 5.1 | Printed product identifier | Hexadecimal printed ID converted to decimal OpenWebNet product component | [ZigBee Interface](../../protocol/zigbee-interface.md) | Address-derivation evidence | Documented canonically | Examples sanitized |
| ZB-046 | p. 13, section 5.2 | Join discovery exchange | Open network then product join indication | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Specification workflow | Documented canonically | Primitive retained |
| ZB-047 | p. 13, section 5.2 | Join indication syntax | Section 5.2 uses leading `*#13`; detailed `WHAT 33` uses command/status `*13` | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Source-internal syntax conflict | Documented with an explicit unresolved contradiction | Alternate grammar not promoted |
| ZB-048 | p. 13, section 5.3 | Interface neighbor request | `WHO 1000 DIMENSION 81` with empty `WHERE` | [ZigBee Interface](../../protocol/zigbee-interface.md) | ZigBee discovery specification evidence | Documented canonically | Verified |
| ZB-049 | p. 13, section 5.3 | Neighbor response sequence | Repeated `ROW*UNKNOWN*NEIGHBOR` records followed by `ACK` | [ZigBee Interface](../../protocol/zigbee-interface.md) | Two fields unnamed by source | Documented canonically | Unknown semantics preserved |
| ZB-050 | p. 13, section 5.3 | Router-addressed neighbor request | Query newly discovered `ZR` through product-level Unit `00` | [ZigBee Interface](../../protocol/zigbee-interface.md) | Router traversal behavior | Documented canonically | Not called Suite diagnostic discovery |
| ZB-051 | p. 13, section 5.3 | Traversal continuation | Repeat through newly discovered routers to obtain installation products | [ZigBee Interface](../../protocol/zigbee-interface.md) | Client traversal described by source | Documented canonically | No ZigBee routing algorithm inferred |
| ZB-052 | p. 13, section 5.3 | Neighbor limits | No field definitions for freshness, aging, paging, maximum count, or duplicate policy | [ZigBee Interface](../../protocol/zigbee-interface.md) | Explicit evidence gap | Documented canonically | Unknowns retained |
| ZB-053 | p. 14, section 5.4 | Scan initiation | `WHO 13 WHAT 65` and `ACK` | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | ZigBee management | Documented canonically | Verified |
| ZB-054 | p. 14, section 5.4 | Delayed scan report | About 13 seconds later `DIMENSION 67` reports count | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Source timing | Documented canonically | Count qualified as database count |
| ZB-055 | p. 14, section 5.4 | Indexed follow-up | Example issues `DIMENSION 73` requests by index | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Specification workflow | Documented canonically | Stored lookup role retained |
| ZB-056 | p. 14 versus pp. 49-52 | Scan explanatory prose | Section 5.4 associates endpoint/Device-ID prose with `73`; detailed definitions assign that role to `66` | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Source-internal conflict | Documented with an explicit unresolved contradiction | No synthetic sequence invented |
| ZB-057 | p. 15, section 6 | Product database capacity | Up to 175 products; automatically managed | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Interface inventory evidence | Documented canonically | Not applied to neighbor-table size |
| ZB-058 | p. 15, section 6.1.1 | Population on join | Joining products fill database while interface is present | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Stored-inventory lifecycle | Documented canonically | Verified |
| ZB-059 | p. 16, section 6.1.2 | Interface joins existing network | Existing products initially unknown; Scan learns active products | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Stored-inventory lifecycle | Documented canonically | Reachability kept separate |
| ZB-060 | p. 16, section 6.1.2 | Sleeping end Devices | Later activity is needed for sleeping products not learned during Scan | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Source workflow | Documented canonically | Native wake mechanics not generalized |
| ZB-061 | p. 17, section 6.1.3 | Product joins while interface off | Product initially absent; later Scan or product activity can add it | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Stored-inventory lifecycle | Documented canonically | Heartbeat mechanics kept contextual |
| ZB-062 | pp. 16-17 | Power-cycle persistence | Stored product count survives interface power cycle | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Persistence evidence | Documented canonically | Verified |
| ZB-063 | p. 18, section 6.1.4 | Product leaves while interface off | Stale product remains in database | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Persistence/reachability distinction | Documented canonically | Verified |
| ZB-064 | p. 18, section 6.1.4 | Stale-entry cleanup | No deletion command, aging interval, or pruning rule defined | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Evidence gap | Documented canonically | Unknown lifecycle explicit |
| ZB-065 | p. 19, section 6.1.5 | Product Information timing | Up to 30 seconds if product is unreachable, such as sleeping battery Device | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Repeated in detailed `DIMENSION 66` text | Documented canonically | Not generalized to `73` |
| ZB-066 | p. 19, section 6.1.5 | Battery information relationship | Battery event can identify product power category after activity | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Event/workflow evidence | Documented canonically | Physical wake actions remain context |
| ZB-067 | p. 19, section 6.1.5 | Open/close network sequence | Diagram uses network opening as one way to make a sleeping product active | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Example workflow, no new primitive | Source-only contextual material that requires no separate canonical documentation | Open/Close commands documented separately |
| ZB-068 | p. 20, section 7 | Bootloader procedure | Silicon Labs bootloader details after handoff | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Post-OpenWebNet protocol | Intentionally out of OpenWebNet scope | Only OpenWebNet `WHAT 12` handoff retained |
| ZB-069 | p. 21 and section 8 | Lighting use cases | ON, OFF, Toggle, Supervisor, movement events | [ZigBee Lighting Variant](../../functional/who-1-lighting/zigbee-variant.md) | ZigBee `WHO 1` evidence | Documented canonically | Examples sanitized |
| ZB-070 | pp. 22-24 | Lighting `WHAT 0` | OFF and `0#SPEED` | [ZigBee Lighting Variant](../../functional/who-1-lighting/zigbee-variant.md) | ZigBee command surface | Documented canonically | `SPEED=0` last, `1..254` explicit, `255` default retained |
| ZB-071 | pp. 22, 25-26 | Lighting `WHAT 1` | ON and `1#SPEED`, speed form reaches 100% | [ZigBee Lighting Variant](../../functional/who-1-lighting/zigbee-variant.md) | ZigBee command surface | Documented canonically | Supervisor report semantics retained |
| ZB-072 | pp. 22, 27 | Lighting `WHAT 2..10` | Discrete levels `20%..100%` | [ZigBee Lighting Variant](../../functional/who-1-lighting/zigbee-variant.md) | ZigBee command surface | Documented canonically | Full range represented |
| ZB-073 | pp. 22, 28-29 | Lighting `WHAT 11..16` | Timed ON 1, 2, 3, 4, 5, 15 minutes | [ZigBee Lighting Variant](../../functional/who-1-lighting/zigbee-variant.md) | ZigBee command surface | Documented canonically | Full set represented |
| ZB-074 | pp. 22, 28-29 | Lighting `WHAT 17` | Timed ON 30 seconds | [ZigBee Lighting Variant](../../functional/who-1-lighting/zigbee-variant.md) | ZigBee-specific value | Documented canonically | Does not resolve separate SCS conflict |
| ZB-075 | pp. 22, 28-29 | Lighting `WHAT 18` | Timed ON 0.5 seconds | [ZigBee Lighting Variant](../../functional/who-1-lighting/zigbee-variant.md) | ZigBee command surface | Documented canonically | Verified |
| ZB-076 | pp. 21-22, 30-31 | Lighting `WHAT 32` | Toggle | [ZigBee Lighting Variant](../../functional/who-1-lighting/zigbee-variant.md) | ZigBee extension | Documented canonically | Reply without Supervisor and possible duplicate with Supervisor retained |
| ZB-077 | pp. 21-22, 32 | Lighting `WHAT 34` | Movement detected | [ZigBee Lighting Variant](../../functional/who-1-lighting/zigbee-variant.md) | Server-originated event | Documented canonically | PnL prerequisite retained only as OpenWebNet-visible dependency |
| ZB-078 | pp. 21-22, 32 | Lighting `WHAT 39` | End of movement detected | [ZigBee Lighting Variant](../../functional/who-1-lighting/zigbee-variant.md) | Server-originated event | Documented canonically | Verified |
| ZB-079 | pp. 23-31 | Lighting acknowledgements | `ACK`, `NACK`, BUSY/NACK and Supervisor state reports | [ZigBee Lighting Variant](../../functional/who-1-lighting/zigbee-variant.md) | Interface-specific operation behavior | Documented canonically | Cross-linked to common ZigBee acknowledgement rule |
| ZB-080 | pp. 33-34 | Lighting `DIMENSION 1` read | Level and speed request/response | [ZigBee Lighting Variant](../../functional/who-1-lighting/zigbee-variant.md) | ZigBee-specific payload semantics | Documented canonically | Exact read grammar retained |
| ZB-081 | pp. 33-34 | Lighting `DIMENSION 1` write | Level and speed write | [ZigBee Lighting Variant](../../functional/who-1-lighting/zigbee-variant.md) | ZigBee-specific payload semantics | Documented canonically | Exact write grammar retained |
| ZB-082 | pp. 33-34 | Lighting level range | `LEVEL=101..200` | [ZigBee Lighting Variant](../../functional/who-1-lighting/zigbee-variant.md) | Variant range | Documented canonically | SCS `100` sentinel not imported |
| ZB-083 | pp. 33-34 | Lighting dimension speed | `SPEED=0..255`; `0` immediate, `255` maximum delay | [ZigBee Lighting Variant](../../functional/who-1-lighting/zigbee-variant.md) | Variant semantics; physical unit unspecified | Documented canonically | Kept separate from command-speed and SCS semantics |
| ZB-084 | p. 35, section 8.6 | Lighting status request | `*#1*WHERE#9##`, state response then `ACK` | [ZigBee Lighting Variant](../../functional/who-1-lighting/zigbee-variant.md) | ZigBee request form | Documented canonically | Switch and dimmer state domains retained |
| ZB-085 | pp. 36-38 | Automation `WHAT 0` | Stop | [ZigBee Automation Variant](../../functional/who-2-automation/zigbee-variant.md) | ZigBee `WHO 2` evidence | Documented canonically | Verified |
| ZB-086 | pp. 36-38 | Automation `WHAT 1` | Up in detailed section | [ZigBee Automation Variant](../../functional/who-2-automation/zigbee-variant.md) | Conflicts with p. 11 example | Documented with an explicit unresolved contradiction | Detailed meaning recorded without erasing conflict |
| ZB-087 | pp. 36-38 | Automation `WHAT 2` | Down in detailed section | [ZigBee Automation Variant](../../functional/who-2-automation/zigbee-variant.md) | Conflicts with p. 11 and p. 58 Up examples | Documented with an explicit unresolved contradiction | Conflict preserved |
| ZB-088 | pp. 36-38 | Automation Supervisor sequences | Movement report, limit Stop, position status | [ZigBee Automation Variant](../../functional/who-2-automation/zigbee-variant.md) | Example/detailed sequence evidence | Documented canonically | Not generalized beyond source |
| ZB-089 | pp. 37, 39 | Automation `DIMENSION 10` | Position read with `STATUS*LEVEL*PRIORITY*INFO` | [ZigBee Automation Variant](../../functional/who-2-automation/zigbee-variant.md) | Variant payload | Documented canonically | Status values `10..12`, level `0..100/255`, fixed priority/info retained |
| ZB-090 | pp. 39-40 | Automation `DIMENSION 11` | Move to position, `LEVEL=0..100` | [ZigBee Automation Variant](../../functional/who-2-automation/zigbee-variant.md) | Variant write grammar | Documented canonically | No SCS priority parameter imported |
| ZB-091 | p. 40, section 9.6 | Automation status request | `*#2*WHERE#9##` | [ZigBee Automation Variant](../../functional/who-2-automation/zigbee-variant.md) | ZigBee request form | Documented canonically | Up-value conflict remains attached |
| ZB-092 | p. 41, section 10.2 | Temperature `WHAT` table | No `WHAT` entries | [ZigBee Temperature Control Variant](../../functional/who-4-temperature-control/zigbee-variant.md) | Explicitly narrow source surface | Documented canonically | SCS Temperature Control commands not imported |
| ZB-093 | p. 41, sections 10.4-10.5 | Temperature `DIMENSION 0` | Server-originated temperature report | [ZigBee Temperature Control Variant](../../functional/who-4-temperature-control/zigbee-variant.md) | ZigBee report only | Documented canonically | No request inferred |
| ZB-094 | p. 41, section 10.5.1 | Temperature encoding | `C1C2C3C4`: sign, whole tens/units, tenth of degree Celsius | [ZigBee Temperature Control Variant](../../functional/who-4-temperature-control/zigbee-variant.md) | Variant encoding | Documented canonically | No unsupported full range inferred |
| ZB-095 | p. 41 | Probe prerequisite | Prior source-named PnL procedure | [ZigBee Temperature Control Variant](../../functional/who-4-temperature-control/zigbee-variant.md) and [ZigBee Binding](../../functional/who-25-transversal/zigbee-binding.md) | Workflow dependency | Documented canonically | Underlying radio mechanics excluded |
| ZB-096 | pp. 42-44, section 11.3.1 | Management `WHAT 12` | Boot mode request, `ACK/NACK`, then `STX 03600796 ETX` | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | OpenWebNet-to-ASCII handoff | Documented canonically | **Exact handoff remediated in Step 3** |
| ZB-097 | p. 44, section 11.3.2 | Management `WHAT 22` | Reset interface; `ACK` before reset | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Interface command | Documented canonically | Verified |
| ZB-098 | pp. 42, 44 | Management `WHAT 30` | Create network; successful use case leaves it created and open | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Interface command | Documented canonically | Verified |
| ZB-099 | pp. 42, 44 | Management `WHAT 31` | Close network and addressed product-originated close indication | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Command plus event | Documented canonically | Verified |
| ZB-100 | pp. 42, 44-45 | Management `WHAT 32` | Open network and addressed product-originated open indication | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Command plus event | Documented canonically | **NACK while binding is in progress remediated in Step 3** |
| ZB-101 | pp. 42, 45 | Management `WHAT 33` | Join network and detailed addressed product-join indication | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Command plus conflicted event | Documented with an explicit unresolved contradiction | Use case instead emits addressed `WHAT 32` |
| ZB-102 | pp. 42-45 | Management `WHAT 34` | Interface Leave; addressed product Leave command/event | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Command/event with malformed detailed wording | Documented with an explicit unresolved contradiction | Addressed-command ACK nuance **remediated in Step 3** |
| ZB-103 | p. 45, section 11.3.8 | Management `WHAT 60` | Keep connect/readiness | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Interface command | Documented canonically | `ACK` ready, `NACK` not ready |
| ZB-104 | p. 45, section 11.3.9 | Management `WHAT 61` | Identify addressed product for five minutes | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Addressed command | Documented canonically | Kept distinct from historical `DIMENSION 70` claim |
| ZB-105 | pp. 43, 45-46 | Management `WHAT 65` | Scan and delayed product-database count | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Interface command | Documented canonically | About 13-second report timing retained |
| ZB-106 | pp. 43, 46-47 | Management `WHAT 66` | Supervisor command and addressed server-originated form | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Management/event surface | Documented canonically | **Addressed indication grammar remediated in Step 3** |
| ZB-107 | p. 47, section 11.3.12 | Management `WHAT 67` | Supervisor Remove, default mode, addressed server-originated form | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Management/event surface | Documented canonically | **Addressed indication grammar remediated in Step 3** |
| ZB-108 | p. 48, section 11.5.1 | Management `DIMENSION 12` | Interface IEEE address, eight decimal values | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Interface identity property | Documented canonically | Real identifiers excluded from examples |
| ZB-109 | pp. 48-49, section 11.5.2 | Management `DIMENSION 16` | Firmware version for interface or product Unit `00` | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Target-dependent property | Documented canonically | **Exact target forms and ACK/BUSY semantics remediated in Step 3** |
| ZB-110 | p. 49, section 11.5.3 | Management `DIMENSION 17` | Hardware version for interface or product Unit `00` | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Target-dependent property | Documented canonically | **Exact target forms and ACK/BUSY semantics remediated in Step 3** |
| ZB-111 | p. 49, section 11.5.4 | Management `DIMENSION 26` | Implemented `WHO` values for selected target | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Capability evidence, not full-operation support | Documented canonically | **Exact target forms and result sequence remediated in Step 3** |
| ZB-112 | pp. 43, 49-51, section 11.5.5 | Management `DIMENSION 66` | Product information by zero-based DB index or addressed product | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Active query; can expose unreachable stored product | Documented canonically | Exact published separator `#INDEX` retained |
| ZB-113 | pp. 50-51, section 11.5.5 | `DIMENSION 66` Device-ID registry | Scenario, Lighting, Automation, Interface, and Video numeric type values | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Source registry; no Suite identity equivalence | Documented canonically | **Full registry remediated in Step 3** |
| ZB-114 | p. 51, section 11.5.5 | `DIMENSION 66` unreachable result | `VALUE=0`, then `ACK`; `NACK` send/index failure; BUSY/NACK | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Operation-specific result semantics | Documented canonically | Verified |
| ZB-115 | p. 51, section 11.5.6 | Management `DIMENSION 67` | Product-database count | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Local stored inventory | Documented canonically | Not treated as reachability count |
| ZB-116 | p. 51, section 11.5.7 | Management `DIMENSION 71` | ZigBee channel `11..26` | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | OpenWebNet-visible radio property | Documented canonically | **NACK when interface is outside network remediated in Step 3** |
| ZB-117 | pp. 51-52, section 11.5.8 | Management `DIMENSION 72` | Battery report values `0..3` | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Server-originated report | Documented canonically | **Source trigger context remediated in Step 3** |
| ZB-118 | p. 52, section 11.5.9 | Management `DIMENSION 73` | DB index to stored product identifier and power type | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Local lookup, no ZigBee frame required | Documented canonically | `0` unknown, `1` mains, `2` battery retained |
| ZB-119 | p. 43 versus pp. 49-52 | `DIMENSION 73` timing prose | 30-second unreachable warning versus statement that lookup is local/no ZigBee frame | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Source-internal conflict | Documented with an explicit unresolved contradiction | Reachability timing remains canonical only for `66` |
| ZB-120 | p. 42 versus p. 45 | Join event value | Join use case emits addressed `WHAT 32`; detailed Join assigns `WHAT 33` | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Source-internal conflict | Documented with an explicit unresolved contradiction | Preserved |
| ZB-121 | p. 45 | Leave ACK/NACK wording | Both detailed lines say interface has not left | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) | Malformed source wording | Documented with an explicit unresolved contradiction | Success use case supports ACK-on-success while defect remains recorded |
| ZB-122 | p. 53, section 12 heading | `WHO 18` heading | Heading says Automation; page 9 registry and section content say Energy Management | [ZigBee Energy Management Variant](../../functional/who-18-energy-management/zigbee-variant.md) | Editorial source inconsistency | Documented canonically | Preserved as editorial inconsistency, no second namespace inferred |
| ZB-123 | p. 53, sections 12.2-12.3.1 | Energy Reset `WHAT` | Summary table says `0`; detailed frame uses `75` | [ZigBee Energy Management Variant](../../functional/who-18-energy-management/zigbee-variant.md) | Source-internal conflict | Documented with an explicit unresolved contradiction | Neither value promoted unqualified |
| ZB-124 | pp. 54-55, section 12.5.1 | Energy `DIMENSION 11` | Voltage | [ZigBee Energy Management Variant](../../functional/who-18-energy-management/zigbee-variant.md) | Decimal value; unit/scale unspecified | Documented canonically | No SCS unit imported |
| ZB-125 | pp. 54-55, section 12.5.2 | Energy `DIMENSION 17` | Current | [ZigBee Energy Management Variant](../../functional/who-18-energy-management/zigbee-variant.md) | Decimal value; unit/scale unspecified | Documented canonically | Verified |
| ZB-126 | pp. 53-55 | Energy `DIMENSION 51` | Detailed table says Energy; Frequency use case uses `51` | [ZigBee Energy Management Variant](../../functional/who-18-energy-management/zigbee-variant.md) | Source-internal conflict | Documented with an explicit unresolved contradiction | Conflict retained |
| ZB-127 | pp. 54-55 | Energy `DIMENSION 112` | Detailed table/definition says Frequency | [ZigBee Energy Management Variant](../../functional/who-18-energy-management/zigbee-variant.md) | Conflicts with p. 53 use case | Documented with an explicit unresolved contradiction | No winner inferred from SCS |
| ZB-128 | p. 55, section 12.5.5 | Energy `DIMENSION 113` | Active Power | [ZigBee Energy Management Variant](../../functional/who-18-energy-management/zigbee-variant.md) | Decimal value; unit/scale unspecified | Documented canonically | Verified |
| ZB-129 | p. 56, section 12.5.6 | Energy `DIMENSION 114` | Active Power Total | [ZigBee Energy Management Variant](../../functional/who-18-energy-management/zigbee-variant.md) | Decimal value; unit/scale unspecified | Documented canonically | Verified |
| ZB-130 | p. 56, section 12.5.7 | Energy `DIMENSION 115` | Threshold Max Active Power | [ZigBee Energy Management Variant](../../functional/who-18-energy-management/zigbee-variant.md) | Decimal value; unit/scale unspecified | Documented canonically | Verified |
| ZB-131 | p. 56, section 12.5.8 | Energy `DIMENSION 117` | Reactive Power | [ZigBee Energy Management Variant](../../functional/who-18-energy-management/zigbee-variant.md) | Decimal value; unit/scale unspecified | Documented canonically | Verified |
| ZB-132 | p. 57, section 12.5.9 | Energy `DIMENSION 1200` | Report Power; `TYPE=1`, `TIME=0..255` seconds | [ZigBee Energy Management Variant](../../functional/who-18-energy-management/zigbee-variant.md) | ZigBee-specific grammar/timing units | Documented canonically | Resulting asynchronous payload remains unspecified |
| ZB-133 | pp. 53-57 | Energy acknowledgements/addressing | Measurements unicast; Reset permits broadcast; common ACK/NACK/BUSY behavior | [ZigBee Energy Management Variant](../../functional/who-18-energy-management/zigbee-variant.md) | Variant applicability | Documented canonically | SCS Energy address families not imported |
| ZB-134 | p. 58, section 13.3.1 | Binding `WHAT 21` | Short Pressure, server to client | [ZigBee Binding](../../functional/who-25-transversal/zigbee-binding.md) | ZigBee `WHO 25` event | Documented canonically | Verified |
| ZB-135 | pp. 58-59, section 13.3.2 | Binding `WHAT 33` | Binding Request, client to server | [ZigBee Binding](../../functional/who-25-transversal/zigbee-binding.md) | Binding lifecycle | Documented canonically | ACK means request sent, not internal table mutation |
| ZB-136 | pp. 58-59, section 13.3.3 | Binding `WHAT 34` | Unbinding Request | [ZigBee Binding](../../functional/who-25-transversal/zigbee-binding.md) | Binding lifecycle | Documented canonically | Verified |
| ZB-137 | pp. 58-59, section 13.3.4 | Binding `WHAT 35` | Open Binding, server to client | [ZigBee Binding](../../functional/who-25-transversal/zigbee-binding.md) | Binding lifecycle event | Documented canonically | Verified |
| ZB-138 | pp. 58-59, section 13.3.5 | Binding `WHAT 36` | Close Binding, server to client | [ZigBee Binding](../../functional/who-25-transversal/zigbee-binding.md) | Binding lifecycle event | Documented canonically | Verified |
| ZB-139 | p. 59, section 13.3.6 | Binding `WHAT 37` | Cancel Binding, addressed or empty-`WHERE` timeout form | [ZigBee Binding](../../functional/who-25-transversal/zigbee-binding.md) | Binding lifecycle event | Documented canonically | Ten-minute timeout form retained |
| ZB-140 | p. 58, section 13.1.2 | Bound-product functional events | Scenario Short Pressure, Lighting Toggle, Automation movement commands | [ZigBee Binding](../../functional/who-25-transversal/zigbee-binding.md) | Cross-namespace event examples | Documented canonically | Automation value example does not resolve Up conflict |
| ZB-141 | pp. 58-59 | Binding acknowledgements | `ACK/NACK/BUSY` for Binding/Unbinding requests | [ZigBee Binding](../../functional/who-25-transversal/zigbee-binding.md) | ZigBee interface acknowledgement behavior | Documented canonically | Verified |
| ZB-142 | p. 60, sections 13.4-13.5 | Binding `DIMENSION` surface | Explicitly no `DIMENSION` table and no `DIMENSION` IDs | [ZigBee Binding](../../functional/who-25-transversal/zigbee-binding.md) | Explicit absence | Documented canonically | Prevents invented binding dimensions |

The matrix contains **142 separately adjudicated source items**. Together they cover every page of the 60-page source, every source-defined `WHAT`, every source-defined `DIMENSION`, all general frame forms, the cross-cutting transport/addressing/acknowledgement rules, discovery and inventory, management, binding, the boot handoff, source limitations, and source-internal contradictions.

## Final contradiction register

| Source locations | Competing claims | Current documentation treatment | External evidence | Final status |
| --- | --- | --- | --- | --- |
| p. 11; pp. 36-38; p. 58 | Automation Up appears as `WHAT 2` in general/binding examples but as `WHAT 1` in the detailed Automation section | [ZigBee Automation Variant](../../functional/who-2-automation/zigbee-variant.md) preserves both | Historical implementation notes mention firmware-dependent inversion but lack preserved provenance sufficient to resolve v4.0; SCS equality is not independent ZigBee evidence | **Unresolved** |
| p. 53 | Reset summary says `WHAT 0`; detailed Reset frame uses `WHAT 75` | [ZigBee Energy Management Variant](../../functional/who-18-energy-management/zigbee-variant.md) leaves both qualified | SCS also uses `75`, but cross-variant numeric agreement does not resolve the ZigBee source conflict | **Unresolved** |
| p. 53 versus pp. 54-55 | Frequency use case uses `DIMENSION 51`; detailed table says `51 = Energy`, `112 = Frequency` | [ZigBee Energy Management Variant](../../functional/who-18-energy-management/zigbee-variant.md) preserves the conflict | No independent ZigBee evidence in the reviewed corpus resolves it | **Unresolved** |
| p. 14 versus pp. 49-52 | Scan example uses indexed `73` while prose describes endpoint/Device-ID information assigned to `66` by detailed definitions | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) documents the primitives separately and does not invent one canonical sequence | Historical implementation notes favor `66` for product information but are not authoritative enough to erase the source inconsistency | **Unresolved workflow inconsistency** |
| p. 42 versus p. 45 | Join use case returns addressed `WHAT 32`; detailed product Join uses addressed `WHAT 33` | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) records both | No independent evidence resolves the v4.0 event value | **Unresolved** |
| p. 13 versus p. 45 | Section 5.2 product-join frame uses leading `*#13`; detailed product Join uses command/status `*13` | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) treats the leading `#` as a source inconsistency, not an alternate grammar | Common frame grammar supports the detailed form structurally, but that is not enough to rewrite the source example | **Unresolved source syntax defect** |
| p. 45 versus p. 42 | Detailed Leave text says both `ACK` and `NACK` mean the interface has not left; successful use case shows `ACK` after Leave | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) uses the successful source use case for ACK-on-success while preserving the duplicated negative wording | No external evidence needed to identify the duplicated wording, but runtime behavior is not independently tested here | **Source wording defect preserved** |
| p. 43 versus pp. 49-52 | `DIMENSION 73` paragraph mentions a 30-second unreachable wait while also saying no ZigBee frame is sent; detailed `66` independently defines reachability timing | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md) keeps the timing on `66`, not `73` | No independent evidence establishes a reachability delay for local `73` lookup | **Unresolved copied-looking prose; not promoted** |
| p. 53 heading versus p. 9 and pp. 53-57 content | Section heading says "Automation WHO = 18"; registry and all operations describe Energy Management | [ZigBee Energy Management Variant](../../functional/who-18-energy-management/zigbee-variant.md) records the heading inconsistency | The same source's registry and operation semantics consistently identify Energy Management | **Resolved as an editorial heading error for canonical placement; preserved in review history** |

No new contradiction found in Step 3 requires a new protocol interpretation beyond these registered cases. The Step 3 additions were completeness details, not evidence that the prior Step 1 or Step 2 architecture was systemically wrong.

## Historical branch reconciliation

The historical `zigbee-documentation` branch was compared only after the primary-source matrix was complete. Its unique ZigBee material is classified as follows:

| Historical branch claim | Classification | Final treatment |
| --- | --- | --- |
| Dedicated 3578/088328 USB transport page and gateway-model naming | Unresolved implementation/product evidence requiring separate provenance | OpenWebNet serial behavior established by the PDF is retained on the canonical interface page; model-specific claims are not promoted without preserved source evidence |
| No TCP session selectors/authentication on the USB link | Already canonically represented, with narrower wording | Canonical page says TCP selectors/authentication are not prerequisites established for this serial interface rather than asserting more than the source proves |
| Command replies and asynchronous events can interleave on USB | Unresolved implementation evidence requiring separate provenance | Not promoted from the historical branch alone |
| Create/Join/Leave require substantially longer acknowledgement timeouts | Explicitly rejected as over-broad | Source establishes about 13 seconds for Scan and up to 30 seconds for unreachable `DIMENSION 66`, not a general long-timeout rule for lifecycle commands |
| Older firmware can invert Automation Up/Down | Unresolved implementation evidence requiring separate provenance | Preserved only as a historical research lead; it does not resolve the source conflict |
| Older firmware can omit terminal ACKs | Unresolved implementation evidence requiring separate provenance | Not promoted without capture/source provenance |
| Alternate `DIMENSION 66` form `*INDEX` instead of `#INDEX` | Unresolved implementation evidence requiring separate provenance | Published `#INDEX` remains canonical |
| ZigBee `WHO 13 DIMENSION 15, 19, 22, 70` | Superseded/rejected as claims about this v4.0 ZigBee source | These belong to other `WHO 13` profiles or unverified implementation claims; ZigBee v4.0 defines Identify as `WHAT 61`, not `DIMENSION 70` |
| Approximate battery value `0 = 5%` | Unresolved implementation interpretation | Canonical source only says `0 = CRITICAL`; the unsupported percentage is not promoted |
| Binding requires firmware `1.2.3` or later | Unresolved implementation evidence requiring separate provenance | Not promoted |
| ZigBee discovery is `WHAT 65 -> DIMENSION 67 -> DIMENSION 66` for every index | Partly represented, partly superseded by primary-source contradiction | Individual primitives are canonical; source section 5.4's `73` sequence and conflict are preserved rather than replaced |
| ZigBee product identifiers are unsigned 32-bit Device identifiers | Partly represented with stricter source wording | Canonical page documents derivation from the last four MAC bytes in decimal and does not equate the namespace with Suite Physical Device IDs |
| ZigBee binding `WHAT 33..37` and request/close lifecycle | Already canonically represented | Current [ZigBee Binding](../../functional/who-25-transversal/zigbee-binding.md) is more complete and source-bounded |
| BUSY NACK `*#*6##` | Already canonically represented | Current [ZigBee Interface](../../protocol/zigbee-interface.md) preserves the exact 500 ms retry and following NACK behavior |
| Underlying ZigBee routing, security, ZDO/ZCL, and binding-table mechanics | Out of OpenWebNet scope | Not promoted |

The historical branch therefore contains **no uniquely established OpenWebNet knowledge that must be promoted before retirement**. It does contain research leads about particular gateway models and firmware behavior. Those leads are not canonical knowledge because their independent provenance is not preserved strongly enough on that branch. Retiring the branch would discard research leads, not established encyclopedia facts; preserve them elsewhere only if future work intends to recover and validate their external implementation sources.

## Scope-boundary audit

The final canonical material does not document ZigBee routing algorithms, ZCL/ZDO internals, radio association mechanics, security or key exchange, binding-table internals, network-layer internals, or the post-handoff bootloader protocol. Native terms such as router, end Device, channel, PnL, Scan, Supervisor, and battery wake behavior are retained only where they identify the meaning, applicability, or consequence of an OpenWebNet-visible field, command, event, or workflow.

Section 7's external bootloader procedure remains outside the encyclopedia after the documented `WHO 13 WHAT 12` transition. Section 2's USB/UART hardware and external host-driver details remain contextual rather than becoming a radio or driver specification.

**Scope integrity result: PASS.**

## Variant-isolation audit

The audited canonical pages satisfy these isolation requirements:

- ZigBee product/Unit `WHERE` is not decoded as SCS `A`/`PL`.
- ZigBee product identifiers are not called Suite Physical Device IDs.
- Shared `WHAT` and `DIMENSION` numbers are interpreted per variant; equal numbers are not used as proof of equal semantics.
- ZigBee `WHO 4` remains a narrow server-originated temperature-report surface and does not inherit the SCS zone/central-unit model.
- ZigBee `WHO 18` does not inherit SCS Energy units, scaling, Stop&Go, historical-series, or address-family rules.
- ZigBee `WHO 13` is not supplemented with unrelated external-interface dimensions.
- `WHO 1000 DIMENSION 81` remains a ZigBee neighbor-discovery mechanism, distinct from MyHOME Suite diagnostic discovery.
- The ZigBee product database remains distinct from MyHOME Suite catalogue/database entities.
- No mapping from ZigBee identifiers to Suite Physical Device IDs is claimed.

**Variant integrity result: PASS.**

## Privacy audit

The ZigBee-facing documentation on `zigbee-reconciliation` was checked for source example identifiers and installation-specific data. Canonical examples use symbolic forms such as `PRODUCT00#9`, `WHERE`, `INDEX`, and `NEIGHBOR`. The source's real-looking MAC-derived decimal identifiers are not reproduced in the canonical ZigBee pages or in this certification matrix.

The audit found no real MAC address, MAC-derived product identifier, private IP address, installation-specific identifier, serial number, or installation topology in the ZigBee documentation added or modified on this branch. Protocol fields capable of carrying those identifiers remain documented symbolically.

**Privacy result: PASS.**

## Remaining evidence gaps

The following gaps are deliberate and explicit rather than missing documentation:

- public-release provenance of the Confidential-footed v4.0 source remains unresolved;
- the USB 115200-baud option has no documented OpenWebNet negotiation procedure or revision-support matrix;
- `DIMENSION 81` does not define the meaning of its second numeric field, formal semantics of the row-like field, freshness/aging, paging, maximum result count, duplicate policy, or end-Device support;
- product-database stale-entry deletion, aging, and pruning are not defined;
- `DIMENSION 73` contains contradictory copied-looking timing prose;
- the Automation Up value, Energy Reset value, Energy Frequency mapping, Join event value, and Scan/`66`/`73` workflow remain source-conflicted;
- ZigBee Energy measurement units, scaling, and signedness are not specified for the decimal value dimensions;
- the later asynchronous payload produced by `DIMENSION 1200` Report Power is not identified by the source;
- runtime behavior across every gateway, product, and firmware revision is not established;
- historical firmware compatibility claims require independent, preserved implementation provenance before promotion.

These gaps are not filled by SCS analogy or by the historical branch.

## Step 3 remediation log

The final pass found isolated omissions, not a systemic failure pattern. It repaired:

- optional USB baud-rate capability and the source's 8-second broadcast-overload consequence;
- explicit `WHEN` non-use and ZigBee network 2.1 applicability;
- the exact boot-mode ASCII handoff;
- the Open command's binding-in-progress `NACK`;
- addressed-product Leave acknowledgement nuance;
- addressed Supervisor/Supervisor Remove indications;
- exact target forms and acknowledgement behavior for `DIMENSION 16`, `17`, and `26`;
- the complete `DIMENSION 66` Device-ID registry;
- the `DIMENSION 71` outside-network `NACK`;
- `DIMENSION 72` event trigger context;
- stale review statements that said the final ZigBee matrix was still outstanding.

No remediation required changing the Step 1 functional model, the Step 2 discovery architecture, or the variant/scope boundaries.

## Validation

The canonical ESG checker is stored at `project/review/checks/check_esg.py`. This environment does not provide a network-capable repository checkout, so the checker cannot be executed literally against a local Git worktree. Its relevant objective checks were reproduced against every ZigBee-facing file added or modified on `zigbee-reconciliation`, using the repository tree for relative-link targets and the current branch contents for headings and anchors.

The final validation checks one descriptive H1, heading hierarchy, em dashes, trailing whitespace, protocol-literal formatting candidates, human-readable link labels, relative links, anchors, duplicated canonical definitions introduced by this work, stale ZigBee incompleteness statements, source-bounded wording, variant isolation, and privacy-sensitive example tokens.

**Mechanical/style/link/reference result: pending final post-write verification.**

## Certification criteria

| Criterion | Result | Basis |
| --- | --- | --- |
| 1. Source coverage | **PASS** | All 60 pages and 142 matrix items were examined and assigned a justified state |
| 2. Canonical coverage | **PASS** | Every established OpenWebNet-visible mechanism is in its canonical owner after Step 3 remediation |
| 3. Epistemic integrity | **PASS** | Contradictions, Unknowns, evidence gaps, provenance, and applicability limits remain explicit |
| 4. Variant integrity | **PASS** | ZigBee semantics are isolated from SCS and Suite namespaces |
| 5. Scope integrity | **PASS** | ZigBee-native internals outside OpenWebNet are excluded |
| 6. Privacy | **PASS** | Canonical ZigBee documentation uses symbolic/synthetic identifiers only |
| 7. Navigation/style | **PENDING FINAL VALIDATION** | Final checker-equivalent pass follows the last repository writes |

The source-bounded completeness statement is issued only after criterion 7 is changed to PASS following final validation.
