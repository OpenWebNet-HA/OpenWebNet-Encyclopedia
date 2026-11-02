# F460 scheduler objects and F461 translation registration

F460 `2.0.12` and F461 `2.0.11` use distinct AArch64 object and registration paths. F460 connects a selected raw scheduler action to its compiled representation; F461 connects a translation descriptor to a local registry and admission checks. These are source-derived contracts, conditional on their objects, providers and callers.

The [package comparison](f460-2.0.12-and-f461-2.0.11.md) establishes exact build identities. The [F460](../../devices/definitions/own-dev-0207-f460-myhome-server.md) and [F461](../../devices/definitions/own-dev-0208-f461-myhome-server-third-party-integration.md) definitions retain distinct product roles.

## F460: a selected raw action reaches a compiled scheduler action

The scheduler's action-name table contains a `SLEEP` row; its table position is not automatically a public action number. An initializer requests the raw object's virtual JSON result and passes that same result to raw reparse and compiled construction.

The raw constructor reads member `seconds` through the imported const JSON accessor and `asUInt`. The compiled constructor copies its result into a distinct layout and prepares a callable. This establishes a source connection between representations; complete JSON/value coherence and functioning providers remain prerequisites. Callable binding alone does not establish invocation or completion.

The [wait/completion contract](f460-f461-deep-analysis.md#f460-sleep-request-units-and-completion-are-separate-contracts) connects the captured value to the actual wait request. Units follow the selected call/ABI contract, not the member name alone. Actual configured scenes and elapsed timing remain unresolved.

## F461: plugin registration and local record admission

The automation translation plugin's `init_plugin` obtains its relocated descriptor, writes fields and requests registration of that same pointer. Relocations identify separate initializer and translator callbacks. The packaged core registration path prepends the descriptor to its manager and conditionally calls its initializer.

The selected translator admits argument pairs `(1,2)` and `(2,1)`. On the inspected `(1,2)` arm, category and representation checks precede four two-character duplication requests from supplied-pointer offsets `0`, `2`, `4` and `6`. The opposite arm has its own representation checks and parsed-object field. Valid strings, effective binding, allocation and normal providers are explicit prerequisites; this local path is not accepted wire grammar or proof of delivered automation commands.

Descriptor fields, registry criteria, translator arguments, record category, representation and public WHO values remain separate namespaces. [Descriptor and admission evidence](../../project/review/firmware-analysis/f460-f461-depth-2026-11-01/README.md) retains the exact imported targets, original layouts and source reviews.

## Evidence limits

The [detailed implementation reference](f460-f461-deep-analysis.md) explains the actual invoker, matcher, complete route identity and selected output records. Active module loading, natural message construction, configuration, provider binding, error handling and ownership remain unresolved. Source registration does not establish a public capability or physical result.
