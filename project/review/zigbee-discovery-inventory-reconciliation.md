# ZigBee Discovery and Inventory Reconciliation - Step 2

This review records the source-bounded reconciliation of ZigBee OpenWebNet version 4.0 discovery and product-inventory mechanisms. It is limited to Step 2 of the remaining ZigBee completeness work. It does not perform the final repository-wide ZigBee source-to-documentation completeness matrix.

The review is governed by the [Encyclopedia Core Values](../encyclopedia-core-values.md) and [Encyclopedia Style Guide](../encyclopedia-style-guide.md).

## Evidence basis and applicability

Primary source: `sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf`, ZigBee OpenWebNet version 4.0, 22 November 2016.

The inspected source carries Confidential footers and its public-release provenance remains unresolved. Claims from it are treated as **specification evidence for this particular ZigBee OpenWebNet interface revision**, not as universal OpenWebNet behavior, independent implementation evidence, or tested interoperability evidence.

Sections 5 and 6 were read in full. The review also inspected the relevant transport/addressing definitions in sections 3 and 4, the `WHO 13` network-management and `DIMENSION` definitions in section 11, and the `WHO 25` material only where the source cross-references it from battery/product behavior. Current `zigbee-reconciliation` documentation remains authoritative for previously reviewed material.

The historical `zigbee-documentation` branch is not an authority and no claim in this review depends on it.

## Mechanism boundary

Three discovery/inventory surfaces remain distinct:

| Surface | Identity exposed | Canonical owner |
| --- | --- | --- |
| ZigBee neighbor discovery | neighbors reported by the interface or a ZigBee router through `WHO 1000 DIMENSION 81` | [ZigBee OpenWebNet Interface](../../protocol/zigbee-interface.md#neighbor-discovery---who-1000-dimension-81) |
| ZigBee interface product inventory | stored product-database membership, indexed product identifiers, and product information through `WHO 13` | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md#scan-and-product-database) |
| MyHOME Suite diagnostic discovery | diagnostic Device-ID enumeration and Physical Device interview, including families such as `WHO 1001` | [Diagnostics](../../diagnostics/) |

No inspected evidence maps a ZigBee neighbor-table row, product-database index, product identifier, or Unit to a MyHOME Suite Physical Device ID.

## Claim-level reconciliation matrix

| Source location | Protocol item or behavior | Existing encyclopedia state | Evidence classification | Adjudication | Canonical documentation location |
| --- | --- | --- | --- | --- | --- |
| p. 9, section 3.1 | `WHO 1000` is listed as "Diagnostic" for this interface | ZigBee interface page listed `WHO 1000` but did not fully define its discovery role | Specification evidence | Retain the source label only for this interface. Do not equate it with Suite diagnostic families. | [ZigBee discovery architecture](../../protocol/zigbee-interface.md#discovery-and-product-inventory) |
| pp. 9-10, sections 3.3-3.6 | ZigBee `WHERE` and generic parameterized `DIMENSION` forms | Already canonical on ZigBee interface page | Existing reviewed encyclopedia knowledge backed by specification evidence | Reused to interpret the targeted-router `DIMENSION 81` form. No SCS `A`/`PL` meaning imported. | [ZigBee transport and addressing](../../protocol/zigbee-interface.md#transport-and-addressing) |
| p. 10, sections 3.7-3.9 | General `ACK`, `NACK`, BUSY syntax | Already canonical | Specification evidence | General interface behavior retained. No `DIMENSION 81`-specific `NACK` or BUSY semantics invented. | [ZigBee acknowledgement behavior](../../protocol/zigbee-interface.md#acknowledgement-behavior) |
| p. 12, section 4 | `ZR` is described as a router/mains-powered product and `ZED` as an end/battery product | Not previously explicit in discovery architecture | Specification evidence, interface-specific classification | Document only to interpret source discovery behavior. Do not map these labels to Physical Device, Module, Object, or catalogue entities. | [Discovery and product inventory](../../protocol/zigbee-interface.md#discovery-and-product-inventory) |
| p. 13, section 5.1 | Product ZigBee ID can be read from the product label and converted for `WHERE` use | Address format already documented | Specification evidence, non-protocol acquisition method | Inspected but not promoted as an OpenWebNet discovery operation. It is a physical-label method, not a frame exchange. | Review record only |
| p. 13, section 5.2 | Product join can reveal a product address | `WHO 13 WHAT 33` product-join indication already documented | Specification evidence with source inconsistency | Relationship retained: a join event can expose the joining product and, when observed by the interface, contributes to database population. | [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md#network-lifecycle) |
| p. 13, section 5.2 versus pp. 42, 45 | section 5.2 writes the join indication with leading `*#13` while detailed `WHAT 33` uses `*13` | Not previously recorded | Source inconsistency | Do not promote `*#13*33*...##` as alternate grammar. Preserve the inconsistency explicitly. | [Discovery relationship and source conflicts](../../functional/who-13-integration-gateway/zigbee-network-management.md#discovery-relationship-and-source-conflicts) |
| p. 13, section 5.3 | Interface-neighbor request `*#1000**81##` | Only summarized previously | Specification evidence | Exact interface-target request promoted. | [Neighbor discovery](../../protocol/zigbee-interface.md#neighbor-discovery---who-1000-dimension-81) |
| p. 13, section 5.3 | Interface response `*#1000**81#ROW*UNKNOWN*NEIGHBOR##` | Not previously field-defined | Specification evidence with symbolic sanitization | Exact field order promoted using symbolic placeholders. Source identifiers are not reproduced. | [Neighbor discovery](../../protocol/zigbee-interface.md#neighbor-discovery---who-1000-dimension-81) |
| p. 13, section 5.3 | Router-neighbor request `*#1000*ROUTER00#9*81##` | Not previously canonical | Specification evidence | Exact targeted-router form promoted. `ROUTER00#9` is ZigBee `WHERE`, not Suite Device ID. | [Neighbor discovery](../../protocol/zigbee-interface.md#neighbor-discovery---who-1000-dimension-81) |
| p. 13, section 5.3 | Router response repeats target `WHERE` before `81` | Not previously canonical | Specification evidence | Response target context documented. | [Neighbor discovery](../../protocol/zigbee-interface.md#neighbor-discovery---who-1000-dimension-81) |
| p. 13, section 5.3 | First response parameter increments from zero | Not previously interpreted | Specification evidence plus inference | It is presented canonically as symbolic `ROW`. Treating it as an entry position is an inference; cursor, resume, stable-index, and product-database-index semantics are unresolved. | [Neighbor discovery field table](../../protocol/zigbee-interface.md#neighbor-discovery---who-1000-dimension-81) |
| p. 13, section 5.3 | Second numeric response value varies across entries | Not documented | Unresolved interpretation | Meaning remains **Unknown**. No ZigBee-native neighbor-table meaning is imported. | [Neighbor discovery field table](../../protocol/zigbee-interface.md#neighbor-discovery---who-1000-dimension-81) |
| p. 13, section 5.3 | Final response value identifies a reported neighbor and is reused to address a discovered router | Not previously field-defined | Specification evidence | Promoted as symbolic `NEIGHBOR`, a ZigBee product-address component. It is not claimed to be a complete `WHERE`, Unit, Physical Device ID, or database index. | [Neighbor discovery field table](../../protocol/zigbee-interface.md#neighbor-discovery---who-1000-dimension-81) |
| p. 13, section 5.3 | `ACK` follows all returned neighbor entries | Only summarized previously | Strong specification evidence | Final `ACK` is the explicit response-sequence terminator. | [Neighbor discovery](../../protocol/zigbee-interface.md#neighbor-discovery---who-1000-dimension-81) |
| p. 13 plus p. 10 | `NACK` and BUSY for `DIMENSION 81` | General interface behavior existed | Specification evidence only at general interface level | No `DIMENSION 81`-specific outcome is stated. Retain only the general `NACK`/BUSY rule and mark operation-specific meaning unspecified. | [Neighbor-table limits](../../protocol/zigbee-interface.md#neighbor-table-limits) |
| p. 13, section 5.3 | After the interface, query each newly discovered `ZR` for its neighbors | Only a one-line summary existed | Strong specification evidence | The source explicitly establishes iterative traversal through newly discovered routers. Calling it recursive describes the client algorithm; "recursive" is not a source term. | [Neighbor discovery](../../protocol/zigbee-interface.md#neighbor-discovery---who-1000-dimension-81) |
| p. 13, section 5.3 | Whether `ZED` entries are recursively queried | Not documented | Specification evidence for documented procedure; support otherwise Unknown | The documented traversal targets newly discovered `ZR` only. Whether a `ZED` accepts `DIMENSION 81` is **Unknown**. | [Neighbor discovery](../../protocol/zigbee-interface.md#neighbor-discovery---who-1000-dimension-81) |
| p. 13, section 5.3 | "known neighbors" and source claim that sequence can get all installation products | Previously summarized without limits | Specification evidence with unresolved applicability | Establish topology/neighbor traversal, not persistent inventory. Freshness, aging, and instantaneous reachability of a returned neighbor are **Unresolved**. The source's completeness statement is retained as source-scoped, not a universal guarantee. | [Neighbor-table limits](../../protocol/zigbee-interface.md#neighbor-table-limits) |
| p. 13, section 5.3 | Duplicate/self-entry behavior | Not documented | Source example plus unresolved interpretation | No uniqueness rule exists. One router-addressed example returns the queried router identifier among the entries; whether this is intended or an example defect is unresolved. Do not assume duplicate-free results. | [Neighbor-table limits](../../protocol/zigbee-interface.md#neighbor-table-limits) |
| p. 13, section 5.3 | Maximum count, pagination, cursor, numeric termination | Not documented | Absence in inspected specification material | No maximum, paging, cursor, or sentinel is established. Final `ACK` is the only documented termination. The 175-product database limit is not transferred to `DIMENSION 81`. | [Neighbor-table limits](../../protocol/zigbee-interface.md#neighbor-table-limits) |
| p. 14, section 5.4; p. 46 | `WHO 13 WHAT 65` Scan broadcasts and active `ZR` plus awake `ZED` can answer; `ACK` means the Scan was sent and `NACK` means it was not | Already mostly canonical | Specification evidence | Retained as Scan behavior, distinct from router-neighbor traversal. No Scan-specific BUSY meaning is defined. | [Scan](../../functional/who-13-integration-gateway/zigbee-network-management.md#scan) |
| p. 14, section 5.4; p. 46 | about 13 seconds after Scan, `DIMENSION 67` reports a count | Already canonical | Specification evidence | Detailed definition controls interpretation: count is database population, not only Scan responders. | [Scan](../../functional/who-13-integration-gateway/zigbee-network-management.md#scan) |
| p. 14 versus pp. 49-52 | Scan example uses `DIMENSION 73` but prose describes endpoints and Device IDs | Already recorded | Material source inconsistency | Preserve separate detailed roles: `73` is indexed product identifier/power type; `66` is Product Information with Units/endpoints and Device IDs. | [Discovery relationship and source conflicts](../../functional/who-13-integration-gateway/zigbee-network-management.md#discovery-relationship-and-source-conflicts) |
| p. 15, section 6 | product database capacity is 175 | Already canonical | Strong specification evidence | Retained as a database capacity only. It is not a neighbor-table maximum. | [Scan and product database](../../functional/who-13-integration-gateway/zigbee-network-management.md#scan-and-product-database) |
| p. 15, section 6 and 6.1.1 | database managed automatically; newly joining product fills database | Already summarized | Strong specification evidence | Promoted explicitly as automatic population when the interface can observe the join. | [Database population and persistence](../../functional/who-13-integration-gateway/zigbee-network-management.md#database-population-and-persistence) |
| p. 16, section 6.1.2 | interface joining an existing network initially does not know products; Scan learns active products | Partly implicit | Strong specification evidence | Promoted. Sleeping products are not thereby guaranteed present; source requires later product activity for others. | [Database population and persistence](../../functional/who-13-integration-gateway/zigbee-network-management.md#database-population-and-persistence) |
| p. 16, section 6.1.2 | database count does not change across interface power cycle | Already canonical | Strong specification evidence | Retained as persistent stored-inventory behavior. | [Database population and persistence](../../functional/who-13-integration-gateway/zigbee-network-management.md#database-population-and-persistence) |
| p. 17, section 6.1.3 | product joining while interface is powered off is not initially known | Not explicit canonically | Strong specification evidence | Promoted with source-scoped later Scan/product-activity update paths. No generic ZigBee association rule inferred. | [Database population and persistence](../../functional/who-13-integration-gateway/zigbee-network-management.md#database-population-and-persistence) |
| p. 18, section 6.1.4 | product leaving while interface is powered off remains in database | Missing | Strong specification evidence | Promoted as explicit stale-entry behavior. Database membership cannot be interpreted as reachability. | [Database population and persistence](../../functional/who-13-integration-gateway/zigbee-network-management.md#database-population-and-persistence) |
| p. 18 and inspected sections 5, 6, 11 | explicit deletion, aging, or stale-entry cleanup rule | Missing | Unknown | No OpenWebNet delete/prune operation, aging interval, or cleanup lifecycle is defined in the inspected material. Do not invent one. | [Database population and persistence](../../functional/who-13-integration-gateway/zigbee-network-management.md#database-population-and-persistence) |
| pp. 19, 43, 49-51 | `DIMENSION 66` Product Information contacts an indexed/addressed product, can take up to 30 seconds if unreachable, returns `0` for unreachable product, and terminates successful Unit reporting with `ACK` | Already canonical | Strong specification evidence | Retained as active product query semantics. `NACK` covers send failure or an out-of-range known index; BUSY uses the interface-wide BUSY/NACK rule. Existence in database remains independent of reachability. | [Product Information](../../functional/who-13-integration-gateway/zigbee-network-management.md#dimension-66---product-information) |
| pp. 43-44, 52 | `DIMENSION 73` resolves database index to product identifier/power type and does not send a ZigBee frame; successful lookup ends with `ACK`, unknown index returns `NACK` | Mostly canonical | Strong specification evidence | Promoted explicitly as local stored-inventory lookup with its defined completion/error result. | [Product identifier by index](../../functional/who-13-integration-gateway/zigbee-network-management.md#dimension-73---product-identifier-by-index) |
| p. 43 | `DIMENSION 73` use-case paragraph also mentions a 30-second unreachable warning | Previously omitted | Source inconsistency / unresolved copied text | The same paragraph says no ZigBee frame is sent. The reachability warning is not promoted to `73`; it remains canonical only for `66`. | [Discovery relationship and source conflicts](../../functional/who-13-integration-gateway/zigbee-network-management.md#discovery-relationship-and-source-conflicts) |
| pp. 46, 51 | `DIMENSION 67` is the number of products filled in the interface database; the direct query response is followed by `ACK`, with `NACK` if the command is not sent | Already canonical | Strong specification evidence | Retained as stored database population, not current Scan responder count, with its documented result sequence. | [Product count](../../functional/who-13-integration-gateway/zigbee-network-management.md#dimension-67---product-count) |
| p. 52 | `DIMENSION 73 VALUE` classifies stored product as unknown, mains-powered, or battery-powered | Already canonical | Specification evidence | Retained as source-defined power category. Do not infer Physical Device class. | [Product identifier by index](../../functional/who-13-integration-gateway/zigbee-network-management.md#dimension-73---product-identifier-by-index) |
| p. 51 and section 13 | Battery-information behavior can depend on a prior source-named PnL procedure for one button-driven path | Binding already reconciled in Step 1 | Specification evidence, not a discovery prerequisite | Inspected because section 6.1.5 references battery information. Not promoted as a prerequisite for neighbor discovery, Scan, database count, indexed lookup, or Product Information. | [ZigBee Binding](../../functional/who-25-transversal/zigbee-binding.md) |
| Existing Suite diagnostics | `WHO 1001 DIMENSION 13` and Physical Device interview | Already canonical from implementation/observed evidence | Existing reviewed encyclopedia knowledge | Explicitly separated from both ZigBee mechanisms. No equivalence inferred from the word "discovery." | [Diagnostics](../../diagnostics/) |

## Required question adjudication

| Question | Evidence strength | Adjudication |
| --- | --- | --- |
| Is `WHO 1000 DIMENSION 81` topology/neighbor traversal rather than product inventory? | **Strong specification evidence** | Yes. Section 5.3 calls it the neighbors sequence and queries the interface and each newly discovered router. The persistent product database is separately described in sections 5.4, 6, and 11. |
| Can a client start with the interface and then query newly discovered routers? | **Strong specification evidence** | Yes. That two-stage progression is explicitly described. Repeating it through the newly discovered routers is the documented traversal model. |
| Are end Devices recursively queried? | **Documented procedure plus Unknown support boundary** | The documented procedure recurses through `ZR` entries only. It neither shows nor forbids a `DIMENSION 81` request to a `ZED`, so `ZED` request support is Unknown. |
| Does neighbor discovery reflect current visibility rather than the complete persistent product database? | **Mechanism separation is strong; freshness semantics unresolved** | It is not the persistent database mechanism. The source reports "known neighbors," but does not define aging or instantaneous reachability, so "currently reachable neighbors only" would be too strong. |
| Do Scan and neighbor discovery serve different purposes? | **Strong specification evidence** | Yes. `DIMENSION 81` traverses reported router-neighbor information. Scan broadcasts to active products and feeds or refreshes the interface's stored product inventory. |
| Does `DIMENSION 67` represent stored database population? | **Strong specification evidence** | Yes. The detailed Scan and `DIMENSION 67` definitions explicitly say the count is products filled in the interface database, not only active routers seen during Scan. |
| Do `DIMENSION 73` and `DIMENSION 66` have distinct roles? | **Strong detailed specification evidence with a contradictory section 5.4 example** | Yes. `73` is index-to-stored-product identifier/power type. `66` retrieves Unit/end-point Device IDs and can expose unreachable products. The section 5.4 explanatory prose is inconsistent and remains recorded as such. |
| Does joining a product update the product database automatically? | **Strong specification evidence with interface-availability condition** | Yes when the interface observes the join. A join while the interface is powered off is explicitly not known at that time. |
| Does the product database survive interface power cycles? | **Strong specification evidence** | Yes for the stored product count/population described in section 6.1.2. |
| Does the source define removal or stale-entry lifecycle? | **Partial strong evidence plus Unknown lifecycle** | It explicitly defines a stale case: a product that leaves while the interface is off remains stored. It does not define an OpenWebNet deletion command, aging interval, or automatic stale-entry pruning lifecycle in the inspected material. |

## Source inconsistencies and unresolved fields

The Step 2 reconciliation preserves these issues rather than normalizing them:

- `DIMENSION 81` response field two is **Unknown**.
- The zero-based-looking `DIMENSION 81` first response field is not established as a request cursor, stable identifier, or product-database index.
- A router-addressed `DIMENSION 81` example appears to return the queried router identifier among its own reported entries. The source does not explain this.
- Neighbor-table freshness, aging, reachability criteria, duplicate handling, and maximum entry count are not specified.
- Section 5.2 writes a product-join indication with a leading `#` that conflicts with the detailed `WHO 13 WHAT 33` command/status grammar.
- Section 5.4 uses `DIMENSION 73` frames while its prose describes the endpoint/Device-ID semantics assigned to `DIMENSION 66` in the detailed definitions.
- The `DIMENSION 73` use-case paragraph mentions the 30-second unreachable warning even though the same paragraph says the lookup is local to the interface database and sends no ZigBee frame.
- No explicit OpenWebNet database delete, stale-entry aging, or garbage-collection rule was found.

## Material inspected but not promoted

Section 5.1's physical product-label method is not promoted as an OpenWebNet discovery protocol because it contains no OpenWebNet exchange.

ZigBee-native routing algorithms, ZDO/ZCL internals, association procedures, radio security, keys, neighbor-table implementation details, and route discovery internals remain outside the OpenWebNet boundary. The encyclopedia documents `ZR`, `ZED`, neighbor reporting, Scan, and product-database behavior only to the extent the OpenWebNet interface exposes them.

The source's physical-button and heartbeat descriptions in section 6 are retained only where they explain when the interface can learn a previously unknown sleeping product. They are not generalized into a ZigBee-native commissioning specification.

No real MAC-derived product or interface identifier from the source examples is retained in canonical examples or this review.

## Step 2 coverage conclusion

Sections 5 and 6 were read in full, together with the earlier syntax/addressing material required to parse their frames and the detailed `WHO 13` operations needed to resolve Scan, product count, indexed lookup, Product Information, power category, acknowledgements, and reachability behavior.

Every OpenWebNet-visible discovery/inventory mechanism in that inspected scope is now either:

- documented canonically;
- cross-referenced to its existing canonical owner;
- recorded as inconsistent or unresolved; or
- explicitly excluded because it is not an OpenWebNet-visible mechanism.

Accordingly, the claim **"The discovery and product-inventory mechanisms exposed by ZigBee OpenWebNet version 4.0 are source-bounded complete in the encyclopedia" is justified**, subject to the source-provenance qualification and explicit unresolved points above.

This conclusion does not establish tested interoperability, support by every product or Firmware revision, or equivalence with MyHOME Suite diagnostics.

At the time of this Step 2 review, the remaining ZigBee task was the final repository-wide source-to-documentation completeness matrix. That later task is now recorded in the [ZigBee Final Source Completeness Certification](zigbee-final-source-completeness-certification.md); it verifies Step 1 and Step 2 together against the full source without changing this review's intentionally narrower historical scope.
