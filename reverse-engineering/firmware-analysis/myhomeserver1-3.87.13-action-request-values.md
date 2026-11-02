# MyHOMEServer1 3.87.13 Action Request Values

The local action-request descriptor supplies version `2.0` and method `light.setStatus`. A selected first-callable path supplies a configured target ID and a conditionally positive signed `speed` value to its parameters. These are construction contracts for [MyHOMEServer1 Firmware 3.87.13](myhomeserver1-3.87.13.md), separate from a complete payload or successful delivery.

## Descriptor constants and separate identities

The descriptor constructor initializes a request representation and then its `LightSetStatusBean` class. The parameter serializer is a separate nonvirtual helper; its address must not be inferred from a primary virtual slot. Descriptor, raw action, compiled runner, captures and parameter records remain different objects.

| Descriptor component | Selected constructor source |
| --- | --- |
| Version | Exact `2.0` string |
| Method | Exact `light.setStatus` string |
| Outer request ID | UUID generation, lowercase formatting and string assignment requests |
| Parameter presence | Initially clear, with source-specific merge setting the subobject present |

There are two UUID generation/conversion request pairs. Under selected normal returns, the later assignment replaces the earlier outer-ID string. This is source order, not a generated UUID observation, uniqueness/randomness proof or defect.

The outer request ID differs from `params.id`: the former comes from UUID requests; the latter comes from the action's captured configured ID. Equal key spelling at different nesting levels does not merge those namespaces. [Descriptor evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-action-request-values/README.md) identifies the actual literals, constructor and argument sources.

## Parameter value producers

The first callable builds a source parameter record, copies the captured ID and marks it present. A signed-positive test on the selected captured word controls the speed value and its presence marker. That is this caller's condition, not a universal accepted range or a physical speed unit.

Because the fresh descriptor's parameters are initially absent, the selected merge follows its out-of-line copy branch. Under present-ID and normal string-copy premises, it copies the ID into the descriptor and marks the subobject present. An explicit pair copy then transfers the speed presence/value into the actual converter input. The relation is established by copy destinations and the supplied argument, rather than equal offsets on unrelated records.

| Converter input | Selected assignment request |
| --- | --- |
| ID present | Construct a JSON string and assign key `id` |
| Speed present | Construct `Json::Value(int)` from its signed word and assign key `speed` |

The converter does not repeat the caller's positive test on that selected arm. Member/map/move/assignment behavior remains a provider premise. Other parameter fields, complete merge behavior and arbitrary malformed records are not covered. The second callable uses the same descriptor constants, but equality of its actual parameters with the first is not established.

## Evidence limits

Together with the [local handoff](myhomeserver1-3.87.13-action-output.md), these fields provide a source-backed interpretation of selected request construction. The [retained-state path](myhomeserver1-3.87.13-action-retained-state.md) separately supplies one `status` value. Neither forms a complete command generator or assigns public WHO semantics, physical speed domains, natural callback ordering or successful delivery.

Configured input, valid current state and type/ID/freshness, effective providers, complete errors/unwind, ownership and concurrency remain unresolved. The [source records](../../project/review/firmware-analysis/myhomeserver1-3.87.13-action-request-values/README.md) retain exact code and copy proofs without supplying or exporting a runtime UUID or private Configuration value.
