# OpenWebNet Scope and Architecture

The encyclopedia covers technologies to the extent that OpenWebNet exposes, represents, transports, configures, or controls them. A bus, radio network, product catalogue, configuration application, or firmware subsystem belongs here only where it establishes an OpenWebNet-visible interface or the applicability of that interface.

This boundary includes SCS and ZigBee-backed behavior that is visible through OpenWebNet. It does not make either underlying technology synonymous with OpenWebNet, and it does not extend the encyclopedia into unrelated SCS electrical design, ZigBee radio internals, or a vendor application's private implementation.

## Architectural layers

| Layer | Canonical treatment | Boundary |
| --- | --- | --- |
| Interface and transport | [Connection and Sessions](sessions.md), [ZigBee Interface](zigbee-interface.md) | Establishes how OpenWebNet frames are carried for an applicable interface; one interface's setup and retry rules do not automatically apply to another. |
| Common frame mechanics | [Frame Syntax](frame-syntax.md), [Addressing](addressing.md), [`WHAT`](what.md), [`DIMENSION`](dimensions.md), and [Acknowledgements](acknowledgements.md) | Defines shared structure only where the applicable sources agree; it does not supply namespace-specific values or Device support. |
| Runtime functional control | [`functional/`](../functional/) | Each functional `WHO` owns its command, event, state, address, and functional-property semantics. Runtime control does not discover a product model or program its stored configuration merely because fields look similar. |
| Device discovery | [Device Discovery](../diagnostics/device-discovery.md) and [Address Discovery](../diagnostics/address-discovery.md) | Finds or selects installed Physical Device instances. Enumeration does not constitute a Device interview. |
| Device interview | [Device Interview](../diagnostics/device-interview.md) | Reads identity, versions, health, Modules, Objects, and addresses reported for one selected Physical Device. It does not by itself provide every detailed configuration value. |
| Detailed configuration reading | [`DIMENSION 35`: Configuration Parameters](../diagnostics/dim35-configuration.md) | Reads the diagnostic projection of indexed configuration where the target supports the operation. The unresolved `DIMENSION 38` effect boundary remains part of this treatment. |
| Programming | [`programming/`](../programming/) | Requests stored configuration changes through the applicable management workflow. Acceptance of a request is distinct from diagnostic verification of effective state. |
| Catalogue capability | [`device-model/`](../device-model/) | Describes products, firmware definitions, possible Modules, Objects, and constraints. Catalogue capability is not installed runtime state. |
| Suite implementation | [`internals/`](../internals/) and [`scenario-engine/`](../scenario-engine/) | Describes implementation artifacts and application capability within their demonstrated versions; it is not universal protocol behavior. |

These layers can participate in one workflow without becoming the same mechanism. For example, discovery can select a Physical Device for interview, interview can establish the Module/Object context needed for a configuration read, programming can request a change, and a new interview can verify effective state.

## Interface and variant applicability

OpenWebNet frame delimiters or a shared `WHO` number do not establish that two interfaces use the same sessions, `WHERE` grammar, acknowledgement behavior, operations, or Device support.

The SCS-oriented public references and MyHOME Suite management data support much of the common and management documentation. The supplied ZigBee specification describes a separate serial interface with product/unit addressing, interface-specific acknowledgement behavior, `WHO 1000` discovery, and separate management and binding surfaces. Its cross-cutting applicability is canonical on the [ZigBee Interface](zigbee-interface.md); operation semantics belong under the relevant functional `WHO` or mechanism page when evidence supports them.

## Entity and identity boundaries

The canonical Device hierarchy is defined in the [Device Model](../device-model/). The following wire and catalogue identities remain distinct:

| Concept | Role | Canonical boundary |
| --- | --- | --- |
| Catalogue Device record and SKU | Describes a product model offered by the catalogue | Not an installed Physical Device ID or protocol address |
| Physical Device | One installed hardware product instance | Can expose several Modules, Objects, and functional addresses |
| Installed Device ID | Selects or identifies an installed instance in supported management workflows | Not `EN_DEVICE.id_device`, a SKU, an Object number, or a functional address |
| Diagnostic `WHERE` | Selects or contextualizes a management response according to its diagnostic family | Does not replace the installed Device ID or a Module's configured address |
| Functional `WHERE` | Selects a runtime target according to one functional `WHO` and interface variant | Not a universal Physical Device identity |
| Module and `slot` | Module is the firmware-exposed logical container; `slot` is its numeric protocol/catalogue position | Neither is a Physical Device or an Object |
| Object and Virgin Object | Object is a regular configured logical function; Virgin Object is a configurable capability template and is the identity used by `DIMENSION 30` while a Module is disabled | Their external numbers and database keys remain separate namespaces |
| Configuration | Instance-specific values and associations interpreted in resolved Device, firmware, Module, and Object context | A configuration index is not a functional `WHAT`, `WHERE`, or scenario parameter merely because values coincide |

[Sources and Identifier Boundaries](../device-model/sources-and-identifiers.md) owns the detailed cross-source namespace rules. Functional pages own runtime wire semantics; the Device Model owns catalogue entities; Diagnostics owns reported installed state; Programming owns write workflows.

## Canonical placement rule

Common wire mechanics live under Protocol. Namespace-specific runtime behavior lives under its functional `WHO`. Entity definitions and catalogue relationships live under Device Model. Discovery, interview, and configuration reading live under Diagnostics. Configuration writes live under Programming.

Other pages may retain enough local context to explain a workflow. Substantial definitions and reference tables should link to these owners. Practical Guides may repeat operational material needed for independent execution, but their copies must preserve the canonical applicability and uncertainty qualifications.
