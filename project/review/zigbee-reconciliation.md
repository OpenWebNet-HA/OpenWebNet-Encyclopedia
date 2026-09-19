# ZigBee Reconciliation Review

This record preserves the evidence decisions used to reconcile the historical `zigbee-documentation` branch with the reviewed encyclopedia baseline.

## Scope and source

The reconciliation started from `main` commit `7cd8ace8865b910ee1957c5db209fba7d568dfa6` and applies the [Encyclopedia Core Values](../encyclopedia-core-values.md) and [Encyclopedia Style Guide](../encyclopedia-style-guide.md).

The primary source is `sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf`, ZigBee OpenWebNet version 4.0 dated 22 November 2016. The reviewed uploaded copy is byte-identical to the repository object: size `929707` bytes and Git blob SHA `773288d33cc55b2a9ecf74e9e9bd886736edab9b`. Its SHA-256 is `9f7d430ced634a333b598f99c165efa3c71f226f7397b950407f601f597c5776`.

The source carries Confidential footers. This review treats it as available specification evidence while preserving the unresolved publication-provenance qualification already recorded in the [Phase 3 Source-Coverage Audit](phase-3-source-coverage.md).

## Promoted specification-backed knowledge

The reconciliation promotes the ZigBee-specific `WHO 13` management surface, including `WHAT 12`, `22`, `30`, `31`, `32`, `33`, `34`, `60`, `61`, `65`, `66`, and `67`, plus ZigBee `WHO 13` `DIMENSION 12`, `16`, `17`, `26`, `66`, `67`, `71`, `72`, and `73`.

It also promotes the ZigBee `WHO 25` binding family: `WHAT 33` Binding Request, `34` Unbinding Request, `35` Open Binding, `36` Close Binding, and `37` Cancel Binding, with `WHAT 21` Short Pressure retained as the associated scenario-button event shown by the source.

These operations are documented as interface-variant semantics rather than universal OpenWebNet behavior.

## Corrected exploratory-branch claims

The historical branch mixed several non-ZigBee `WHO 13` dimensions into its ZigBee property table. The inspected ZigBee `WHO 13` dimension table does not define `DIMENSION 15`, `19`, `22`, or `70`. Their absence from this source is not proof that no implementation ever exposes them; it is sufficient to prevent presenting them as established semantics of this ZigBee v4.0 interface.

The source defines product identification as `WHAT 61`, not `DIMENSION 70`. It also defines `DIMENSION 73` as the indexed product-identifier/power-type operation omitted by the exploratory page.

The exploratory branch's alternate `DIMENSION 66` request separator, minimum binding firmware `1.2.3`, old-firmware ACK omissions, and similar compatibility statements are not established by this primary source. They remain unpromoted implementation claims until separate provenance is available.

The exploratory statement that Create, Join, and Leave generally require substantially longer OpenWebNet timeouts is also not established by the inspected command definitions. The source does establish a documented scan delay of about 13 seconds and says `DIMENSION 66` Product Information can take up to 30 seconds for an unreachable sleeping battery Device; those narrower timing statements are retained.

## Preserved source inconsistencies

The source's Scan example shows `WHAT 65`, then `DIMENSION 67`, followed by indexed `DIMENSION 73` requests, while its prose under those `DIMENSION 73` exchanges describes endpoints and Device IDs. The detailed `DIMENSION 66` definition assigns endpoint/Device-ID information to `66` and the detailed `73` definition assigns index-to-product-identifier/power-type lookup to `73`. No synthetic canonical sequence is inferred.

The `WHO 13` Join use case shows an addressed `WHAT 32` frame after an interface `WHAT 33` Join request, while the detailed `WHAT` definition assigns product join indications to addressed `WHAT 33` frames. The inconsistency remains explicit.

The detailed Leave definition contains duplicated negative wording for both `ACK` and `NACK` cases. The preceding successful Leave use case supports the ordinary `ACK`-on-success reading, but the source defect is preserved rather than silently erased.

The already-recorded ZigBee Automation UP/DOWN and Energy reset conflicts remain separate from this reconciliation and are not resolved by the binding or management material.

## Functional Step 1 reconciliation

The ZigBee `WHO 1`, `WHO 2`, `WHO 4`, and `WHO 18` sections were subsequently reconciled operation by operation against the reviewed SCS-oriented references. The complete claim matrix, source conflicts, evidence limits, and canonical placements are recorded in [ZigBee Functional Reconciliation - Step 1](zigbee-functional-reconciliation.md).

That review establishes source-bounded completeness for those four namespaces within ZigBee OpenWebNet version 4.0 while preserving the unresolved Automation Up-value, Energy Reset, and Energy Frequency/Energy conflicts. It does not extend the conclusion to runtime support across products or Firmware, `WHO 1000` discovery, or the final ZigBee source-to-documentation completeness matrix.

## Discovery and inventory Step 2 reconciliation

The ZigBee discovery and product-inventory mechanisms in sections 5 and 6 were subsequently reconciled against the detailed `WHO 13` definitions and the interface's transport/addressing model. The complete claim matrix, `WHO 1000 DIMENSION 81` field adjudication, source conflicts, product-database lifecycle, and mechanism boundaries are recorded in [ZigBee Discovery and Inventory Reconciliation - Step 2](zigbee-discovery-inventory-reconciliation.md).

That review establishes source-bounded completeness for the discovery and product-inventory mechanisms exposed by ZigBee OpenWebNet version 4.0. It keeps `WHO 1000 DIMENSION 81` router-neighbor traversal, `WHO 13` Scan/product-database inventory, and MyHOME Suite diagnostic discovery as separate mechanisms. It also preserves the unknown `DIMENSION 81` field, unresolved neighbor freshness/duplicate semantics, the Scan example's `DIMENSION 73`/Product Information conflict, the section 5.2 join-frame syntax inconsistency, the copied-looking `DIMENSION 73` reachability warning, and the undefined stale-entry cleanup lifecycle.

The final repository-wide ZigBee source-to-documentation completeness matrix remains a later task and is intentionally outside Step 2.

## Canonical placement

Cross-cutting transport, addressing, acknowledgement behavior, and applicability remain canonical in [ZigBee OpenWebNet Interface](../../protocol/zigbee-interface.md).

ZigBee `WHO 13` management and product-database semantics are canonical in [ZigBee Network Management](../../functional/who-13-integration-gateway/zigbee-network-management.md). ZigBee `WHO 25` binding semantics are canonical in [ZigBee Binding](../../functional/who-25-transversal/zigbee-binding.md).

Cross-cutting ZigBee discovery and `WHO 1000 DIMENSION 81` are canonical in [ZigBee OpenWebNet Interface](../../protocol/zigbee-interface.md). Diagnostics and Practical Guides link to these variant-specific mechanisms rather than copying them into the Suite diagnostic model.
