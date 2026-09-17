# MyHOME Suite Internals

This section documents the MyHOME Suite 3.5.38 implementation data that connects catalogue capability, OpenWebNet management workflows, validation, and scenario-editor capabilities.

It describes the implementation represented by the preserved databases and support files. It does not claim a complete software-component architecture: the canonical corpus does not include application binaries, decompiled code, runtime traces of database access, or the format used to persist user-authored projects and scenarios.

## Reference

| Subject | Page |
| --- | --- |
| Installed source locations, fingerprints, and version scope | [Installation and Source Layout](installation-and-source-layout.md) |
| Responsibilities and boundaries of each implementation store | [Data Store Responsibilities](data-store-responsibilities.md) |
| How systems, frames, sequences, address rules, and timers are represented | [OpenWebNet Registry and State Machines](openwebnet-registry-and-state-machines.md) |
| How product identity becomes firmware, Module, Object, and configuration capability | [Catalogue Resolution](catalogue-resolution.md) |
| How scenario-editor capabilities are represented and where execution evidence ends | [Scenario Capability Loading](scenario-capability-loading.md) |
| How catalogue, protocol, and linked-property constraints combine | [Validation Layers](validation-layers.md) |
| Resource keys, stored labels, UI terminology, and presentation boundaries | [Localization and Presentation](localization-and-presentation.md) |
| Established behavior, safe inferences, unknowns, and investigation priorities | [Implementation Boundaries](implementation-boundaries.md) |

## Implementation-data pipeline

MyHOME Suite combines several models rather than relying on one universal database:

1. identify a Physical Device and installed firmware from diagnostic traffic;
2. resolve product, Module, Object, and configuration capability in `MHCatalogue.db`;
3. select management frames, address rules, sequences, and timers from `OPEN.db`;
4. apply contextual catalogue filters and, where applicable, linked-property rules from `rules.db3`;
5. resolve scenario-editor commands independently from a ScenarioDevices database;
6. present resolved labels and editable fields through the application UI;
7. send frames and compare the resulting installed state with a new diagnostic read-back.

Each stage has its own identifiers. Equal integers across stores are not joins unless an explicit relationship, an unambiguous frame, or independently observed behavior establishes the correlation.

## Three different kinds of state

| State | Principal evidence | Meaning |
| --- | --- | --- |
| Capability | `MHCatalogue.db`, ScenarioDevices, `rules.db3` | what an implementation can offer in a resolved context |
| Workflow | `OPEN.db` and `OpenQuery.txt` | which frames, transitions, directions, and timers compose an operation |
| Installed state | diagnostic responses and project/UI observations | what one Device currently reports or what a project currently presents |

Confusing these layers produces common errors. A catalogue Object does not prove that a Module currently uses it. An `OPEN.db` template does not prove universal Device support. A scenario-editor action does not prove that every installed Device can execute it.

## Source authority

The canonical files and their SHA-256 fingerprints are registered in [`sources/manifest.yaml`](../sources/manifest.yaml). Database facts in this section describe that exact MyHOME Suite 3.5.38 source set; they are not protocol maxima or claims about later releases.

The public OpenWebNet documents remain authoritative for published functional frame semantics. MyHOME Suite implementation data adds unpublished management structures and editor capability, but differences must be retained as source/version differences rather than silently reconciled.

## Reading rule

Use the narrowest source that answers the question:

- functional frame meaning → [Functional reference](../functional/);
- common frame grammar → [Protocol](../protocol/);
- installed discovery and read-back → [Diagnostics](../diagnostics/);
- Device capability hierarchy → [Device Model](../device-model/);
- programming state changes → [Programming](../programming/);
- scenario-editor vocabulary → [Scenario Engine](../scenario-engine/);
- application data loading and boundaries → this section.

Implementation facts are labelled as established, implementation-derived, inferred, or unknown where the distinction matters.
