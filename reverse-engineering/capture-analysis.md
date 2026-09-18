# Capture Analysis

Observed traffic supplies runtime evidence that static databases cannot provide. It must be analyzed as a session, not as an unordered list of frames.

## Privacy boundary

Captures can contain Device IDs, addresses, network endpoints, authentication traffic, and installation topology. Raw private captures are intentionally excluded from the repository.

Published conclusions should use redacted or synthetic examples unless the captured values are already intentionally disclosed as evidence.

## Session record

For every frame, retain:

| Field | Purpose |
| --- | --- |
| timestamp | ordering and timeout analysis |
| direction | distinguishes identical request/response or abort shapes |
| connection/session | prevents unrelated frames from being combined |
| raw frame | preserves delimiters, padding, and unknown fields |
| parsed grammar | separates `WHO`, `WHAT`, `WHERE`, `DIMENSION`, and values |
| active scenario/sequence | supplies state-machine context |
| selected Device | address, local interaction, or Device ID selector |
| classification | expected, optional, repeated, terminal, error, or unexpected |

Do not normalize leading zeroes or rewrite separators before storing the raw form.

## Segmenting management traffic

Separate:

- Device enumeration;
- per-Device interview;
- detailed Object/configuration read;
- programming entry;
- Object/configurator transfer;
- session close or abort;
- ordinary functional traffic.

The same `WHO` can carry several of these workflows, and identical frame text can have different meaning by direction and active sequence.

## Request-response correlation

Associate a response using the narrowest available context:

1. active connection and management family;
2. selected Device or address;
3. current scenario and sequence;
4. last outstanding request;
5. internal slot or configuration index;
6. expected repetition and timeout window.

The protocol provides no general transaction identifier. Avoid pipelining operations that would make responses ambiguous.

## Building Device evidence

Preserve a structured interview result:

```text
Device identity and version
→ internal slot
→ configured Object or Virgin Object
→ system and address
→ indexed configuration values
→ errors and terminal evidence
```

Do not infer absent Modules from UI numbering and do not attach `DIMENSION 35` values using `INDEX` alone. Device and internal-slot context are mandatory.

## Negative observations

Record the request, timeout, retry count, and terminal state when documenting a missing response. Silence can mean unsupported operation, invalid selector, incomplete interview, transport loss, busy Device, or no Device.

An observed omission becomes a Device/firmware-specific fact before it becomes a protocol-family rule.

## Promotion from capture evidence

A capture-derived conclusion is ready for reference documentation when it has:

- an exact request and response context;
- a catalogue or specification interpretation;
- repeated observations or a structurally decisive example;
- explicit Device and firmware scope;
- no unresolved competing parse.
