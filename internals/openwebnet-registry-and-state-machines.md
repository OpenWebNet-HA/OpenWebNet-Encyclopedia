# OpenWebNet Registry and State Machines

`OPEN.db` is MyHOME Suite’s implementation registry for OpenWebNet systems and management workflows. It represents frame templates and their composition; it is not a complete copy of the public functional protocol.

## Registry layers

| Layer | Principal tables | Role |
| --- | --- | --- |
| Systems | `EN_SYSTEM` | functional namespace label, functional `WHO`, diagnostic `WHO`, and managed flag |
| System operations | `AS_OPEN_SYSTEM`, `EN_OPEN` | concrete frame templates associated with selected systems |
| Parameters | `AS_OPEN_PARAM`, `EN_OPEN_PARAM` | placeholder descriptions and transport constraints |
| Addressing | `AS_SYSTEM_ADDRESS_RULE`, `EN_ADDRESS_RULE` | system-specific Virtual and advanced address grammars |
| Scenarios | `EN_SCENARIO`, `AS_SCENARIO_SEQUENCE` | named high-level operations composed from sequences |
| Sequences | `EN_SEQUENCE`, `AS_OPEN_SEQUENCE` | ordered frames, direction-sensitive variants, repetition, and transition metadata |
| Timing | `AS_TIMEOUT_OPEN_SEQUENCE`, `EN_TIMEOUT` | timers, defaults, start/stop actions, and timeout transitions |

An `EN_SYSTEM` row proves namespace knowledge. It does not prove that `EN_OPEN` contains every functional command for that `WHO`.

## State-machine assembly

A management operation is resolved in two stages:

1. select an `EN_SCENARIO` and order its sequences through `AS_SCENARIO_SEQUENCE.sequence_order`;
2. for each selected `EN_SEQUENCE`, order its frame definitions through `AS_OPEN_SEQUENCE.open_order`.

Sequence metadata controls whether a frame is mandatory or repeated, its direction-sensitive registry row, and state changes for `NACK`, structured errors, and timeouts.

A repeated sequence association permits application-level repetition but does not encode the iteration count. Likewise, a repeated frame can collect or emit multiple rows, but the database does not determine how many a particular Device supports.

## Frame records

`EN_OPEN.open_string` stores parameterized frames such as diagnostic `DIMENSION 30`, programming `DIMENSION 35`, and session-control `WHAT` values. Related fields classify address and parameter presence, direction/type, diagnostic use, errors, and Object-programming use.

The same textual frame shape can appear in different directions or workflow contexts. Programmer and Device aborts, for example, share a wire form but are distinct registry rows. Always retain the `EN_OPEN` row, direction, active scenario and sequence, current Device selector, and last outstanding command.

The wire protocol has no transaction identifier that can recover this context after ambiguous pipelining.

## `OpenQuery.txt` as a data-access contract

`OpenQuery.txt` defines named SQL statements for selected registry reads:

| Query key | Data loaded |
| --- | --- |
| `systemDictQuery` | all systems ordered by internal system ID |
| `systemaddressruleDictQuery` | system/address-rule associations and rule fields |
| `openframeErrDictQuery` | frames marked as errors |
| `openframeabortconfQueryList` | programmer abort rows |
| `openframegatewayconnectionQueryList` | selected gateway-connection frames |
| `openframescsbusQuery` | the SCS-bus frame |
| `timeoutscsbusQuery` | SCS-bus timeout default |
| `scenarioQuery` | scenario identity and type by label |
| `scenseq1Query` | ordered sequence composition |
| `openseq1Query` | ordered frame composition plus selected parameter metadata |
| `opentimeoutQuery` | timeouts and transitions for a sequence |

The file records the columns and ordering MyHOME Suite intended to request. It does not prove when each query runs, how results are cached, or how application classes interpret every field.

## Incompleteness preserved in the source

The file itself records unfinished work:

- an Italian note says the sequence-only part still had to be defined;
- a second note says queries needed for scenario traversal were still missing;
- `openparamsQuery` is literally `TODO`;
- the operation-specific address-rule query is commented out.

These are source facts. `OpenQuery.txt` cannot be treated as a complete schema-access specification.

The `systemaddressruleDictQuery` select list contains the SQLite expression `ar.address_rule_adv&ar.level_2_rule`. As written, `&` is a bitwise operator, not a column separator. Do not silently rewrite it as a comma. Whether the expression is intentional, unused, or a defect requires runtime evidence.

## Runtime algorithm

A safe reimplementation should select the system and management family without numerically joining another database’s system ID; resolve the scenario by label; preserve sequence/frame order and repetition; bind only established parameters; create timers from timeout associations; serialize ambiguous requests; and classify terminal, error, `NACK`, and timeout transitions separately.

The concrete diagnostic and programming state machines are documented in [Diagnostics](../diagnostics/) and [Programming](../programming/).
