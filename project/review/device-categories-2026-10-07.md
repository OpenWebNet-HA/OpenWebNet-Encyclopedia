# Device Category Review - 7 October 2026

## Scope and outcome

Reviewed the landing page and all ten category pages against the [Encyclopedia Core Values](../encyclopedia-core-values.md) and [Encyclopedia Style Guide](../encyclopedia-style-guide.md). This is a navigation and category-summary review against the accepted canonical Device definitions and their recorded evidence, not a new acceptance review of the Devices or certification of installed behavior.

The original category tables contained 381 entries covering 189 of the 210 reviewed Device definitions. The corrected tables contain 439 entries covering all 210. Existing category memberships are retained; 58 supported memberships were added, including the 21 previously uncategorized definitions (OWN-DEV-0031 through OWN-DEV-0050 and OWN-DEV-0065).

## Findings and corrections

| Review area | Finding | Correction / evidence basis |
| --- | --- | --- |
| Scope and architecture | Category pages began directly with tables, leaving category meaning and capability scope implicit. | Added category definitions, stable reference/evidence/navigation sections, and explicit separation of installed Configuration from documented or catalogue-derived roles. Canonical definitions remain the technical authority. |
| Commercial identities | Early entries used database record counts and generic family labels as commercial identities. | Replaced them with selected literal references from each definition's Commercial identities section. Selection and combined finish notation are explicit; full variant inventories remain canonical. |
| Abstraction boundaries | Some rows described capacitive buttons as independently configured command positions, or juxtaposed physical relays and logical Modules without applicability. | Clarified physical button/relay functions and conditional command roles, including OWN-DEV-0003, 0006, 0007, 0009, 0014, 0016, 0019 and 0027. A slave-dimmer controller is distinguished from its load-handling slaves. |
| Gateway classification | The combined table mixed OpenWebNet gateways, SCS/DALI/radio bridges, contacts, displays, infrastructure and driver integration. | Split into 16 OpenWebNet gateway entries and 34 other interfaces/integration entries, with gateway evidence and restrictions visible per row. Catalogue gateway candidates are explicitly not runtime endpoint observations. |
| Gateway coverage and provenance | BMNE500, MH200 and H4684 were absent; MH202's gateway evidence was not surfaced. | BMNE500's accepted definition supplies its manufacturer access settings and catalogue Open SCS role. The [published gateway model table](../../functional/who-13-integration-gateway/dimensions.md#dimension-15---device-type) names MH200 and H4684; H4684 evidence is not extended to L4684. The [observed MH202 case](../../guides/identify-openwebnet-gateway.md#7-worked-case-mh202) establishes scoped gateway responses without universalizing command support. |
| Specialized interfaces | OPEN-password fields, Ethernet labels and XOpen SCS metadata could be mistaken for proof of a general OpenWebNet gateway. | Kept multimedia displays, F458 infrastructure, F524 logging, Vigik GPRS, F459 driver integration and F459T's documentation-limited role visibly scoped. F450 remains a documented specialized OPEN/BACnet bridge. |
| Reader usefulness | Some function cells described completed review/extraction work rather than the device's purpose; abbreviations and literals were inconsistent. | Replaced review-status wording with useful function summaries, expanded non-obvious abbreviations before the tables, formatted references and `FUN` literals, and normalized formal Firmware/Virgin Object terminology. |
| Completeness and evidence limits | Missing category memberships concealed accepted devices; generic family wording could imply identical hardware. | Restored supported navigation, retained source-specific restrictions, distinguished selected commercial variants, and stated that missing exact-product documentation is an evidence gap rather than an unresolved identity. |

## Validation

All category-local links and heading anchors resolve. Tables have consistent column counts and no duplicate Device entries within a page. Every selected commercial literal occurs in its linked canonical definition; all original memberships are preserved; every reviewed definition has at least one category entry. The gateway split retains each entry exactly once on that page.

Repository ECV and ESG checks report zero objective failures. The Device completeness checker passes all 210 definitions. Existing Machine KB privacy and artifact-manifest checks pass; the manifest retains 807 originals. No new source artifact, Device acceptance state or generated Machine KB content was introduced by this category review.
