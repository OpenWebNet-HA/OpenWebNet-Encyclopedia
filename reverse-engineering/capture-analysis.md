# Capture Analysis

Observed traffic supplies runtime evidence that static databases cannot provide. It must be analyzed as a direction-sensitive session governed by an active workflow, not as an unordered collection of frame strings.

## Privacy and evidence boundary

Captures can disclose Device IDs, addresses, network endpoints, authentication traffic, installation topology, user behavior, and configured functions. Raw private captures are intentionally excluded from the repository.

Published examples should be redacted or synthetic unless the identifiers were deliberately supplied as evidence. Redaction must preserve field width, separators, ordering, equality relationships, and any property relevant to the conclusion.

Record the hash and private location of the original capture so that a published derivation remains auditable without committing sensitive data.

## Capture the transport context

Where possible, record both the OpenWebNet payload and the transport events around it:

- connection open and close;
- gateway/session establishment;
- payload direction;
- frame boundaries;
- retransmission or duplicate delivery;
- local-button or Device-mode transition;
- timeout and socket failure.

Do not infer frame direction from syntax alone. Several management frames have identical text in programmer-to-Device and Device-to-programmer contexts.

## Canonical event record

For every event, retain:

| Field | Purpose |
| --- | --- |
| capture identifier | stable reference to the original evidence |
| timestamp | ordering, delay, and timeout analysis |
| direction | distinguishes requests, responses, and same-shaped aborts |
| connection/session | prevents unrelated traffic from being combined |
| raw frame | preserves delimiters, padding, empty fields, and unknown values |
| parsed grammar | separates `WHO`, `WHAT`, `WHERE`, `DIMENSION`, and value fields |
| active operation | discovery, interview, detailed read, programming, or functional traffic |
| active sequence | expected frames and transition context from `OPEN.db` |
| selected Device | address, local interaction, or Device-ID selector |
| correlation key | `slot`, configuration index, or outstanding request where applicable |
| classification | expected, optional, repeated, terminal, error, timeout, or unexpected |
| notes | uncertainty, redaction, or transport anomaly |

Store raw and parsed forms separately. Never normalize leading zeroes, decimal/hex representation, `#` modifiers, empty fields, or `*` separators in the raw record.

## Parse before interpreting

Parsing answers where fields occur; interpretation answers what they mean. Keep the stages separate.

1. Identify the OpenWebNet frame family from delimiters.
2. Split only according to the grammar for that family.
3. Preserve empty and compound fields.
4. Resolve the active management `WHO` and direction.
5. Match an exact `OPEN.db.EN_OPEN` template where available.
6. Attach parameter metadata without treating database labels as universal protocol definitions.
7. Interpret values only after Device, firmware, Module, and workflow context is available.

A placeholder such as `[FW_VERSION]` can expand to `Version*Release*Build`; it is not necessarily one scalar field merely because the template contains one placeholder token.

## Segment the session

Separate traffic into operations before correlating responses:

- Device enumeration;
- per-Device interview;
- detailed Object/configuration read;
- programming entry and readiness;
- Object, address, or configurator transfer;
- programming verification;
- session close, end marker, or abort;
- ordinary functional traffic.

The same management `WHO` can carry several operations. `WHAT` values and `DIMENSION` numbers are meaningful only inside the active operation and direction.

Use `OPEN.db` scenario/sequence metadata as an implementation model:

```text
scenario
→ ordered sequence
→ ordered frame alternatives
→ repetition and mandatory flags
→ timeout/error/terminal transition
```

This model describes MyHOME Suite 3.5.38. It does not guarantee that every Device emits every optional response.

## Correlate requests and responses

Use the narrowest available context, in this order:

1. transport connection and management family;
2. active operation and sequence;
3. selected Physical Device or address;
4. last outstanding request;
5. `slot`, configuration index, or Object selector;
6. repetition and timeout window;
7. terminal or error transition.

OpenWebNet management traffic has no general transaction identifier. Avoid pipelining requests whose responses would share the same shape and selector.

If pipelining is already present, classify ambiguous associations explicitly instead of selecting the nearest request by timestamp.

## Handle repetitions, retries, and duplicates

A repeated response can represent:

- a legitimate multi-row result, such as one row per Module;
- an application retry;
- a Device retransmission;
- the same Device responding to a repeated bus-wide request;
- duplicate transport capture.

Do not deduplicate by frame text alone. Compare direction, timestamps, request cycle, Device selector, sequence position, and expected repetition metadata.

For discovery, preserve each enumeration round. `WHAT 11` quieting, repeated requests, absence of further replies, and `WHAT 12` release are part of the result, not noise around a list of Device IDs.

## Build a structured Device interview

The normalized evidence model is:

```text
Physical Device instance
├─ diagnostic family and discovery selector
├─ DIMENSION 1 catalogue-facing identity
├─ firmware, hardware, and microcontroller V.R.b values
├─ internal Module slot
│  ├─ enabled regular Object or disabled Virgin Object
│  ├─ enabled/disabled state
│  ├─ system and functional address
│  └─ indexed and Object-specific configuration values
└─ errors, omissions, retries, and terminal evidence
```

Preserve protocol slot numbers even when the UI renumbers visible Modules. Attach `DIMENSION 32` and `35` data only with the same Device and `slot` context. `DIMENSION 35.INDEX` is not globally unique.

## Analyze version responses

Record firmware (`DIMENSION 2`), hardware (`3`), and microcontroller (`6`) as three raw components: Version, Release/Revision, and Build.

For firmware correlation:

- compare `V` and `R` with `EN_FIRMWARE`;
- compare `b` with associated `EN_BUILDS` rows;
- preserve explicit `-1` sentinels separately from missing build rows;
- retain all candidates until default, localization, capability, or runtime evidence distinguishes them.

Hardware and microcontroller values currently have no direct catalogue columns. Keep them as installed-state evidence rather than manufacturing a join.

## Use differential captures

The strongest behavioral evidence changes one input while holding the rest constant.

For each experiment:

1. capture a complete baseline operation;
2. change one physical configurator, UI property, Module Object, or address;
3. repeat the identical operation;
4. align frames by operation, Device, and slot;
5. report added, removed, and changed fields;
6. restore and recapture the baseline where practical.

Do not compare two Devices with different firmware and configuration as though one changed variable explains every difference.

## Treat errors as structured evidence

Record `NACK`, structured diagnostic errors, aborts, busy results, timeouts, and positive end markers separately.

An error can establish:

- that the Device parsed a selector;
- that a Module or Object state was reached;
- that a value was outside a supported domain;
- that the operation was unavailable in the current state.

It does not automatically establish which validation layer rejected the request. Transport bounds, catalogue ranges, contextual filters, linked-property rules, firmware behavior, and application prevalidation remain distinct.

## Interpret silence cautiously

When documenting an absent response, preserve the request, selector, Device state, timeout source, timeout duration, retry count, connection health, and terminal outcome.

Silence can mean:

- unsupported optional response;
- invalid Device or Module selector;
- disabled Module or unresolved Object state;
- Device busy or not in the required local mode;
- incomplete interview;
- transport loss;
- no matching Device.

An omission becomes a Device/firmware-specific observation before it becomes a family-wide rule.

## Publication record

A capture-derived conclusion should publish:

- a redacted raw exchange with direction;
- the operation and preceding request;
- Device identity and firmware scope;
- exact parsing and unresolved fields;
- catalogue/specification correlation;
- repetitions and exceptions;
- confidence and falsifier;
- the promoted reference-page link.

Capture evidence is ready for reference documentation only when no competing parse changes the operational conclusion.
