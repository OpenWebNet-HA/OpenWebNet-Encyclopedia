# Practical Guides

Practical Guides start from an installer or application goal and raw OpenWebNet evidence, then follow the complete resolution path to structured, user-presentable data or a safely validated action. They combine the canonical protocol, Device Model, diagnostics, programming, and MyHOME_Suite implementation references.

Each guide must stand on its own as a complete end-to-end example rather than an alternative protocol specification. When an example and a canonical reference appear to differ, follow the canonical page and record the discrepancy.

## Operating assumption

These guides assume that the installer or application can communicate with the installation as MyHOME_Suite does: establish the required OpenWebNet session, send arbitrary supported frames, receive responses with direction and ordering intact, apply sequence timeouts, and preserve raw traffic. Transport discovery, authentication, and socket implementation are outside the examples unless they directly affect the workflow.

Responses are never assumed to be available spontaneously. Before a guide parses a diagnostic or programming response, it identifies the request or scenario that must be sent to obtain it.

## Guides

| Starting goal | Practical guide |
| --- | --- |
| Build an identified inventory of installed Devices | [Discover and Identify Devices](discover-devices.md) |
| Turn raw interview frames into a user-presentable Device configuration | [Read and Present a Device Configuration](read-device-configuration.md) |
| ↳ Identify an unknown OpenWebNet gateway to catalogue identity | ↳ [Identify an OpenWebNet Gateway](identify-openwebnet-gateway.md) |
| ↳ Find the effective group memberships of an actuator | ↳ [Retrieve an Actuator's Group Memberships](retrieve-actuator-group-memberships.md) |
| ↳ Find every configured CEN button on a Device | ↳ [Retrieve Configured CEN Buttons](retrieve-configured-cen-buttons.md) |
| Decide whether a candidate value is allowed | [Validate a Configuration Value](validate-configuration-value.md) |
| Construct and execute a programming session | [Program a Device](program-device.md) |
| Prove the effective state after programming | [Verify Programming](verify-programming.md) |
| Explain incomplete scans and interviews | [Troubleshoot Diagnostics](troubleshoot-diagnostics.md) |

The `↳` rows are specialized instances of the nearest preceding general guide. They remain independently executable, but inherit their conceptual place in the index from that parent. Use this convention when adding further specialized guides.

## Guide structure

Each page is independently executable. A specialized guide may repeat acquisition and resolution steps from a general guide; links provide deeper reference material but are not prerequisites for completing the workflow.

Whenever a guide retrieves information from a database, it must include a concrete SQL example for that lookup. Cross-database correlations must show the attachment or separate staged queries, identify the correlation keys, and state whether the relationship is a declared key or a semantic mapping.

Where a workflow contains iteration, branching, retries, or several resolution stages, include implementation-oriented pseudocode or an equivalent algorithm. The algorithm must preserve raw evidence, ambiguity, timeouts, and stop conditions rather than presenting only the successful path.

Every guide should:

1. state the user or installer goal;
2. send the request or start frame required to acquire the raw responses;
3. collect the expected responses through an explicit end condition or timeout;
4. resolve every protocol and database identifier in context;
5. transform raw values into user-presentable concepts;
6. apply validation and stop conditions;
7. define the final output or action;
8. preserve provenance, ambiguity, and unresolved semantics.

Concrete captures can be substituted into these workflows without changing their resolution rules. Examples must never invent missing frames, catalogue mappings, display labels, or Device behavior.

## Safety model

Read-only discovery should precede programming. Before any write:

1. identify the installed Device and firmware;
2. resolve every affected Module and Object;
3. validate the complete intended state;
4. preserve the previous state;
5. prepare diagnostic read-back;
6. stop on ambiguity.

Advanced Object programming begins by resetting all Objects. A partially validated payload is therefore unsafe.
