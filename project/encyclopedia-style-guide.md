# Encyclopedia Style Guide

The Encyclopedia Style Guide (ESG) defines how the human-facing OpenWebNet Encyclopedia is written, structured, and presented.

It does not define standards of evidence or truth. Those are governed by the [Encyclopedia Core Values](encyclopedia-core-values.md). It also does not define the schema or formatting requirements of the Machine KB.

## I. Language and terminology

### 1. Use concise, technical, descriptive prose

Canonical reference material uses clear, impersonal technical prose. Prefer direct statements and explicit qualifications over rhetorical or conversational phrasing.

Practical Guides may use direct instructional language where it improves execution of a workflow.

### 2. Use canonical model terminology consistently

Formal model entities are capitalized:

- Physical Device
- Firmware
- Module
- Object
- Virgin Object
- Configuration

Use these terms consistently when referring to the corresponding concepts.

The implementation or database counterpart to a Module index is written as `slot`. Use `slot` when referring to the literal numeric or indexed concept exposed by protocol frames or database structures. Do not use "internal slot" as a formal model term.

Database identifiers retain their literal source names and are formatted as code, for example `EN_DEVICE.name`.

### 3. Use precise evidence and uncertainty vocabulary

Use evidence labels consistently when they are needed:

- **Published protocol** - behavior or semantics stated by a canonical public protocol document.
- **Implementation evidence** - behavior, structure, labels, ranges, mappings, or capabilities established by software, databases, or other implementation artifacts.
- **Observed behavior** - behavior directly seen in protocol captures or controlled Device experiments.
- **Unresolved** - the available evidence does not yet establish one sufficiently supported interpretation.

Use uncertainty terms precisely:

- **Unknown** means the relevant value, field, relationship, or concept exists, but its semantics are not established.
- **Unresolved** means evidence exists but leaves a material question open, including competing or incomplete interpretations.
- **Inferred** means the interpretation is supported by evidence but is not directly stated by an authoritative source.
- **Observed** means the statement describes direct evidence from a capture or experiment and does not, by itself, imply universal behavior.

Do not substitute stronger wording for a weaker evidence state merely to improve prose.

### 4. Define non-obvious abbreviations and project-specific terms

Define uncommon abbreviations and project-specific terminology at first meaningful use on a page unless the term is already obvious from the immediate canonical context.

Protocol primitives such as `WHO`, `WHAT`, `WHERE`, `DIMENSION`, `ACK`, and `NACK` may be used directly in protocol-focused reference material.

## II. Protocol and technical notation

### 5. Format protocol and implementation literals as code

Write protocol fields, literal values, database entities, identifiers, paths when discussed as paths, and short frames as inline code.

Preferred forms include:

- `WHO 1`
- `WHAT 0`
- `DIMENSION 30`
- `A=2`
- `PL=3`
- `EN_DEVICE.name`
- `*#1001*0*13##`

A complete short frame may remain inline when it fits naturally within prose or a table.

### 6. Use canonical range and hexadecimal notation

Write integer domains as inclusive ranges using two periods, for example `0..2047`.

Physical Device hexadecimal IDs are written as exactly eight hexadecimal characters, zero-padded where necessary, with no `0x` prefix. This mirrors the representation used on Physical Device labels, for example `004FBEC8`.

Generic hexadecimal numbers may use an `0x` prefix when that improves clarity. Do not add the prefix when the hexadecimal representation is used literally in an OpenWebNet frame, query, stored identifier, or other syntax that expects the unprefixed value.

Preserve fixed-width representations when the width is semantically or operationally meaningful.

### 7. Use fenced blocks for multiline machine-readable material

Use fenced code blocks for:

- multi-frame exchanges;
- SQL;
- pseudocode;
- multiline configuration or data;
- any machine-readable material where line structure or ordering matters.

Keep isolated short literals inline.

### 8. Make frame direction explicit

In explanatory prose, semantic direction may be written compactly, for example `Client → Gateway`.

In fenced transcripts, every frame line must identify source and destination explicitly using ASCII direction syntax:

```text
Client -> Gateway: *#1001*0*13##
Gateway -> Client: *#1001*15*13*004FBEC8##
```

Direction labels describe observed message flow. They do not, by themselves, prove that the transport endpoint originated the underlying event, state, or bus message.

## III. Page architecture

### 9. Use one descriptive H1 and a logical heading hierarchy

Every page has one descriptive H1. Subsequent headings should reflect the conceptual structure of the material and should not skip levels without a clear reason.

Heading text should describe the content it introduces rather than use vague labels such as "More information".

### 10. Follow a recommended reference-page flow without forcing a template

Where appropriate, reference pages should broadly progress through:

1. definition or scope;
2. reference or navigation;
3. substantive semantics and structure;
4. evidence or source basis;
5. limits, unresolved points, or related material.

This is a recommended workflow, not a compulsory template. Different subject types may use different structures when that improves comprehension.

### 11. Split pages to support distinct ideas and navigability

Split a subject across pages when it contains distinct reference ideas that benefit from independent treatment, or when a single page becomes materially harder to navigate or understand.

Do not split merely to satisfy an arbitrary length threshold. Conversely, keep small or tightly coupled subjects together when separation would fragment comprehension.

Each documentation directory uses its `README.md` as its landing-page overview.

### 12. Standardize recurring sections

When sections serve the same recurring purpose across pages, prefer stable names and ordering. Common examples include:

- Reference
- Scope
- Evidence
- Evidence limits
- Source roles
- Related material

Variation is acceptable when the content genuinely requires a different distinction. Do not create near-synonymous recurring headings without a reason.

## IV. Navigation and information presentation

### 13. Link semantically and preserve canonical treatment

Use human-readable link text. Natural-language link text inside a sentence is acceptable and often preferable.

Do not use a destination filename or directory name as the visible label unless that path itself is the subject being discussed.

Concepts should link to their canonical treatment. Non-canonical pages may provide enough local context for comprehension, but substantial definitions and reference tables should normally be linked rather than duplicated.

Practical Guides are largely exempt from the non-duplication rule when repeating canonical material is necessary to keep a workflow independently executable and understandable.

### 14. Match the presentation form to the information

Use:

- prose for explanation, qualification, and interpretation;
- tables for structured comparison or reference data with repeated fields;
- ordered lists for actual sequences, procedures, or workflows;
- unordered lists for non-sequential collections.

Do not force explanatory material into oversized tables merely for compactness, and do not turn genuine procedures into prose when ordering matters.

### 15. Mark examples explicitly and keep evidence status visible

Synthetic or illustrative examples must be explicitly identified as examples. They must never be presented in a way that could be mistaken for captured or experimentally observed traffic.

When evidence class, uncertainty, or applicability materially affects interpretation, present that status visibly in the surrounding prose, table, or recurring evidence section rather than leaving it implicit.

## V. Editorial mechanics

Use a simple hyphen (`-`) for parenthetical breaks and title separators. Do not use the Unicode em dash.

Otherwise, prefer ordinary, consistent Markdown and readable technical English over a large set of arbitrary punctuation rules. Mechanical conventions should be added only when they improve clarity, consistency, or maintainability across the encyclopedia.
