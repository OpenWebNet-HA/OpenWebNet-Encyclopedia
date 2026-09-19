# Encyclopedia Core Values

The Encyclopedia Core Values (ECV) define the standards by which knowledge enters, changes, and remains in the OpenWebNet Encyclopedia.

They govern truth, evidence, interpretation, scope, provenance, completeness, and stewardship. They are distinct from the [Encyclopedia Style Guide](encyclopedia-style-guide.md), which governs presentation of the human-facing documentation.

## I. Truth and epistemic integrity

### 1. Truth before completeness

The encyclopedia must never fill a knowledge gap merely to appear complete. Unknown, unresolved, or insufficiently evidenced matters must be identified as such. A smaller body of trustworthy knowledge is preferable to a larger body containing unsupported conclusions.

### 2. Distinguish evidence, inference, confidence, and applicability

Published specification, catalogue or database evidence, observed traffic, experimentally confirmed behavior, inference, and hypothesis must remain distinguishable. Claims must also communicate their confidence and the Devices, implementations, versions, transports, or circumstances to which they are known to apply.

### 3. Preserve epistemic history

Contradictions, superseded interpretations, and rejected hypotheses are part of the knowledge base. They must not be silently erased. When stronger evidence changes a conclusion, the canonical interpretation should change while preserving enough provenance to understand why.

### 4. Generalize only as far as the evidence permits

Behavior observed for one Device, firmware, transport, implementation, or experiment must not automatically become a universal protocol rule. Likewise, "not observed" must not be transformed into "does not exist" without sufficient evidence.

## II. Sources, coverage, and provenance

### 5. Exhaust the relevant sources of truth

For every protocol area, systematically identify and examine all reasonably available relevant source families before considering the subject comprehensively documented. These may include official specifications and technical documents, protocol captures, catalogue and database material, Device behavior, configuration software behavior, legitimately observable firmware-facing interfaces, and prior validated research.

### 6. Track source coverage and evidence gaps explicitly

Documentation maturity depends not only on the confidence of existing claims but also on how thoroughly the relevant evidence space has been examined. Known unexamined sources, incomplete datasets, and coverage gaps must remain visible.

### 7. Respect source authority and triangulate evidence

Every source must be used only for conclusions it is capable of supporting. Important conclusions should, where practicable, be checked against independent evidence. Agreement increases confidence; disagreement must trigger investigation rather than arbitrary source preference.

### 8. Preserve provenance and reproducibility

Significant claims must remain traceable to the evidence supporting them. Another researcher should be able to understand how a conclusion was reached and, where reasonably possible, reproduce the analysis.

## III. Interpretation discipline

### 9. Preserve namespace and value semantics

Values belong to their respective namespaces and contexts. Numerical equality must never, by itself, establish semantic identity, a database relationship, or a protocol relationship. Sentinel, reserved, empty, and otherwise special values must be interpreted explicitly rather than treated automatically as ordinary data.

### 10. Separate syntax, capability, semantics, and behavior

A syntactically valid frame does not establish that a Device supports it; support does not necessarily establish universal semantics; documented semantics do not guarantee identical runtime behavior on every implementation. These layers must remain distinct.

## IV. Protocol scope and architecture

### 11. OpenWebNet defines the encyclopedia boundary

The encyclopedia documents technologies insofar as they are exposed, represented, transported, configured, or controlled through OpenWebNet. Underlying technologies may be described sufficiently to explain the OpenWebNet interface, but should not become independent encyclopedias inside this project.

This includes technologies such as ZigBee: their OpenWebNet-visible integration belongs here; unrelated ZigBee internals do not.

### 12. Protocol variants and transports must not be universalized

Behavior specific to SCS, ZigBee-backed systems, a particular gateway, transport, Device generation, or implementation must be identified as such unless evidence establishes broader applicability. SCS behavior in particular must not silently become synonymous with OpenWebNet itself.

### 13. Canonical placement follows the OpenWebNet model

Knowledge should live primarily where it belongs in the protocol architecture or wire model. Related material elsewhere should cross-reference the canonical treatment rather than creating competing definitions.

### 14. Keep protocol mechanisms conceptually distinct

Discovery, identification or interview, diagnostics, runtime control, configuration reading, and programming may interact but are not interchangeable concepts. Documentation must preserve their boundaries and describe only behavior actually exposed through OpenWebNet.

## V. Entity and data-model integrity

### 15. Preserve abstraction boundaries

Physical products, Physical Devices, protocol identities, addresses, Modules, Objects, catalogue entities, and database records are distinct concepts unless evidence establishes a relationship between them. In particular, Physical Device, Module, and Object must not be used interchangeably.

### 16. Separate capability knowledge from runtime state

What a catalogue or database says a Device can support is different from what a particular Physical Device currently exposes or has configured. Neither should silently substitute for the other.

## VI. Documentation stewardship

### 17. Documentation and examples must remain evidence-grounded

Examples must never masquerade as observations. Synthetic or illustrative protocol frames must be recognizable as such, and documentation must not manufacture evidence merely to make an explanation easier.

### 18. Privacy is a property of the knowledge base

Private information is not protocol knowledge. Evidence must be sanitized where necessary, and neither the human encyclopedia nor the Machine KB may retain unnecessary real-world identifiers such as private IP addresses, MAC addresses, credentials, personal information, or equivalent infrastructure-specific data.

### 19. Canonical knowledge must remain consistent across representations

Stable findings should be promoted from experiments, captures, discussions, and research notes into canonical documentation. Human-oriented documentation and the Machine KB must express the same evidence-backed body of knowledge; the machine representation must not become a more speculative parallel encyclopedia.

### 20. Aim for implementation-ready comprehensiveness

The encyclopedia should strive to cover the complete OpenWebNet-visible protocol surface to the extent supported by available evidence. Its goal is knowledge sufficiently precise, interconnected, and comprehensive that installers, researchers, and developers can understand observed behavior and build interoperable implementations without concealing genuine uncertainty or gaps.
