# Device Support-Page ECV/ESG Review - 8 October 2026

This review covers the 22 Markdown pages under Devices that are not individual Device descriptions, against the current [Encyclopedia Core Values](../encyclopedia-core-values.md) and [Encyclopedia Style Guide](../encyclopedia-style-guide.md). Four obsolete working pages are retired; 18 supporting pages remain. This is a supporting-documentation review, not renewed semantic acceptance of the 210 Device definitions or independent certification of the Machine KB.

## Findings and corrections

| Pages reviewed | Findings and disposition |
| --- | --- |
| [Devices](../../devices/README.md) | Replaced the implication that every included product exposes an OpenWebNet endpoint; bounded completion to catalogue `3.5.38`; preserved concrete documentation/runtime limits and access to the acceptance history. Removed closed progress views from navigation and corrected the actual Device filename example. |
| [Complete Device Index](../../devices/index.md) | The previous index contained 561 lookup rows but only 199 of the 210 accepted Devices. Missing Devices were `OWN-DEV-0010` and `OWN-DEV-0021` through `OWN-DEV-0030`, covering 31 canonical commercial records. Added those records and six already documented printed sensor references; split two three-reference cells into individual rows. The resulting 602 rows cover all 541 catalogue records and all 210 definitions. Normalized brand/line presentation and code formatting, kept source conflicts and variant qualifiers, and corrected the statement that an explicit catalogue identity remains unresolved without product documentation. |
| [Device Definitions](../../devices/definitions/README.md) | Corrected the example filename for `OWN-DEV-0042`; removed obsolete claims about designated mature exemplars. The written profile and template remain normative. |
| [Contributing Device Definitions](../../devices/contributing/README.md) | Linked the presentation profile and acceptance gate; documented ledger validation and optional private research exports after retiring the public working pages. Existing branch and immediate artifact-registration policy remains applicable. |
| [Presentation Profile](../../devices/contributing/device-definition-presentation-profile.md) | Checked section architecture, Summary prose, identity/documentation boundaries, commercial/EAN placement, evidence columns, namespace separation and all eight acceptance criteria. Retained the current policy, including reopening affected checks and non-blocking hardware corroboration. |
| [Device Page Template](../../devices/contributing/device-page-template.md) | Checked correspondence with the profile and canonical diagnostic links. Disambiguated Module `slot` positions from `EN_SLOTS.id_slot` database row identifiers in topology and conditions tables. |
| [Category directory](../../devices/categories/README.md) and all ten category pages | Checked scope introductions, reference/role tables, variant and Firmware qualifications, category coverage and links to accepted definitions. All 210 definitions remain covered. Centralized two repeated policy paragraphs in the directory page; retained concise links and product-specific qualifications in each category. Gateways and Interfaces keeps separate gateway/interface tables and evidence at row level; a catalogue gateway flag or Ethernet connection is not an observed endpoint. |
| [Catalogue Evidence](../../devices/inventory/README.md) | Replaced stale research-backlog presentation with permanent source scope and ancillary-association guidance. Distinguished the seven source gateway-flag records from the evidence-qualified gateway classification; retained the 4534 package set/range associations and their examination limits. |
| Retired `devices/coverage.md` | Removed the repetitive ten-column progress matrix after checking its distinct documentation, identity, hardware and configuration qualifications against the canonical definitions. Source-scoped completion and concrete evidence gaps remain visible in Devices, the definitions and review history. |
| Retired `devices/work-queue.md` | Removed the rendered closed queue and empty next-work table. The authoritative YAML ledger, actual eight-check results, per-item notes and detailed semantic review reports remain intact. |
| Retired `devices/inventory/commercial-records.md` and `devices/inventory/technical-items.md` | Removed pre-curation raw database tables after completing the public lookup. Complete canonical catalogue surfaces remain on accepted definitions; supplementary package associations remain retained. Raw exports remain available as private maintenance aids. |

The pre-cleanup working pages remain recoverable in Git history at commit `bba1c7ea31acc89ea69e77c0d8e263b230d2e435`. No unique accepted source finding, identity, gate result, original artifact or ancillary association was deleted. The shared category policy retains the distinction between catalogue capability and installed behavior, and missing exact-product documentation remains a coverage gap rather than an identity failure.

## Validation

The Device checker now requires each accepted definition and each canonical commercial record to be discoverable under the correct Device in the index. A grouped catalogue finish code must appear literally or through its complete reference expansion. This replaces validation of the retired coverage matrix's layout; it does not remove any Device completeness or acceptance-gate requirement.

Five additional regressions cover missing records, wrong Device mappings, incomplete finish expansions and equivalent printed spacing. All 19 Device/gate regressions pass, and catalogue completeness validation passes for all 210 definitions. Ledger validation passes for 210 items. Private inventory/dashboard generation and freshness checking pass; stale checks do not modify exports, and guards reject regenerating working pages inside the public repository.

Repository ECV/ESG checks, local links, category coverage, artifact integrity and the affected diff are checked. Manual review distinguishes numeric-domain violations from existing filenames, product names and page citations reported as range candidates. No individual Device description, acceptance ledger entry, catalogue appendix, original artifact or Machine KB input/projection changes in this review. The changed supporting pages are outside the canonical KB source set, so prior KB build/schema/lifecycle/privacy/determinism results remain applicable; no regeneration is needed for this cleanup.

## Review history

The following semantic review records retain the Device-specific findings and evidence limits. The [Device acceptance ledger](../../devices/work-queue.yaml) remains the enforceable state record.

| Device IDs | Semantic review record |
| --- | --- |
| `0001..0010` | [Reviews 0001 to 0010](device-reviews-0001-0010-2026-10-05.md) |
| `0011..0020` | [Reviews 0011 to 0020](device-reviews-0011-0020-2026-10-05.md) |
| `0021..0030` | [Reviews 0021 to 0030](device-reviews-0021-0030-2026-10-06.md) |
| `0031..0040` | [Reviews 0031 to 0040](device-reviews-0031-0040-2026-10-06.md) |
| `0041..0050` | [Reviews 0041 to 0050](device-reviews-0041-0050-2026-10-06.md) |
| `0051..0060` | [Reviews 0051 to 0060](device-reviews-0051-0060-2026-10-06.md) |
| `0061..0070` | [Reviews 0061 to 0070](device-reviews-0061-0070-2026-10-06.md) |
| `0071..0080` | [Reviews 0071 to 0080](device-reviews-0071-0080-2026-10-06.md) |
| `0081..0090` | [Reviews 0081 to 0090](device-reviews-0081-0090-2026-10-06.md) |
| `0091..0100` | [Reviews 0091 to 0100](device-reviews-0091-0100-2026-10-06.md) |
| `0101..0110` | [Reviews 0101 to 0110](device-reviews-0101-0110-2026-10-06.md) |
| `0111..0120` | [Reviews 0111 to 0120](device-reviews-0111-0120-2026-10-06.md) |
| `0121..0130` | [Reviews 0121 to 0130](device-reviews-0121-0130-2026-10-06.md) |
| `0131..0140` | [Reviews 0131 to 0140](device-reviews-0131-0140-2026-10-06.md) |
| `0141..0150` | [Reviews 0141 to 0150](device-reviews-0141-0150-2026-10-06.md) |
| `0151..0160` | [Reviews 0151 to 0160](device-reviews-0151-0160-2026-10-07.md) |
| `0161..0170` | [Reviews 0161 to 0170](device-reviews-0161-0170-2026-10-07.md) |
| `0171..0180` | [Reviews 0171 to 0180](device-reviews-0171-0180-2026-10-07.md) |
| `0181..0190` | [Reviews 0181 to 0190](device-reviews-0181-0190-2026-10-07.md) |
| `0191..0200` | [Reviews 0191 to 0200](device-reviews-0191-0200-2026-10-07.md) |
| `0201..0210` | [Reviews 0201 to 0210](device-reviews-0201-0210-2026-10-07.md) |
