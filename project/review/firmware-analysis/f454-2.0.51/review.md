# Independent review of the initial F454 firmware integration

**No remaining material discrepancy found in this scoped initial integration after the kernel-banner precision correction.** This review covers the new Firmware Analysis index/entry, the changed F454 Device content and the selected documentary evidence capsule. It does not close the full61-row research register or the Device review queue.

Reviewed on branch `docs/static-firmware-analysis-findings`. Only this review file is written by this reviewer. No firmware/native tests, vendor process, gateway/service/network operation, new catalogue extraction, commit or push occurred. The stopped authentication branch was not reopened.

## Final reviewed identities

| Repository file | SHA256 |
|---|---|
| `reverse-engineering/firmware-analysis/README.md` | `6c677a0ca8ef819e5f83feebf8a27b9dde9f56880c514413630292660ab64833` |
| `reverse-engineering/firmware-analysis/f454-2.0.51.md` | `8455eb35067e96b7760f033b1a8c5d3b0f47f1ad43ed43520b701335ddc2ac8b` |
| `devices/definitions/own-dev-0002-audio-video-web-server-gateway.md` | `92e8afc01f715264acc442c83000f889663ad835e29e729763faaacfad57216a` |
| `project/review/firmware-analysis/f454-2.0.51/README.md` | `34520ee3bdcc0d10f48c925c62edd05227942537f7a88f124f146bb9c4e54035` |
| `project/review/firmware-analysis/f454-2.0.51/provenance.json` | `eeb281531b26e8e117ecd7d934170044db9619da9bf8957231942c0fc7914edd` |

The analysis now quotes the actual kernel banner version `2.6.32.17-davinci1-c44221b9cd7e82d5ec494320685310d138f4dd07`, matching the preserved platform report. The prior shortened `2.6.32.17-davinci` wording was corrected in both new analysis and Device row. The alarm row also now names `libopenmsg::openmsg_to_buf`0x2948 separately from the coso callbacks/send call; the original-library VA is clear.

## Documentary provenance and source checks

All eight original analyst-report SHA256 values match the read-only local dossier. For each platform/identity/registry/web/sender/alarm/markup/versions capsule, I independently selected its declared inclusive original line range using byte-preserving line splitting and compared the bytes directly with the retained excerpt. All eight match exactly, as do the eight excerpt hashes. Alarm and markup excerpts are the complete referenced report versions; the other records preserve their stated bounded ranges. These are report excerpts, not vendor source files or independent executions.

All eight selected original-file sizes/hashes match the authoritative normal-image regular-file inventory metadata. This was a document/metadata identity comparison, not a new binary execution or independent semantic audit of those binaries. The research evidence index matches the recorded SHA256 `3a71c4fb8caac033058689279a0f4acde36cc385936c39f3e8d7faa9ad9947df` and1917 entries. The artifact ID, filename, size74448014, archive SHA256 and private-archive-only disposition agree with the existing artifact-manifest entry. No original archive, image or binary is copied into the capsule.

Local-link existence checks pass for the new index, analysis, updated Device and capsule README:3,16,26 and12 local links respectively. Existing external publisher/archive URLs were not fetched or newly certified. New references resolve within the intended repository structure. The original research index/manifest and historical reports were not edited; `git diff --name-only -- sources/` is empty.

## Selected claim and method review

| New incorporation | Review finding |
|---|---|
| Build/platform/storage/version metadata | The exact package and build target remain distinct from a hardware interrogation, current installation, partition geometry and loaded/runtime components. Normal/recovery path counts and325 matching code-section comparisons are not presented as independent implementations or runtime equivalence. OpenSSL release1.0.1m remains separate from ABI filename1.0.0, without a patch/exposure/exploitability claim. |
| Gateway N_CONF provenance | The builder/getter addresses, persistent offset0x15e and eight-byte text slot agree with the identity excerpt. The local code reads cached/persistent metadata rather than calculating the addressed-device configurator count; the meaning of observed15 remains unresolved. No catalogue model/WHO/local-client namespace is merged with it. |
| Diagnostic registration | The five class counts55/4/11/17/17 and104 distinct keys match the exact factory report. Explicit C++ storage primitives, selected owner lookup and untested handlers/physical commands remain bounded. Registry presence is not promoted to universal support. |
| Web callback map | The273/260/13 figures agree with the static exact-bound callback call-presence report. The analysis explicitly rejects a dominance/complete authorization proof or unauthenticated-method verdict. No stopped session/framing experiment is incorporated. |
| Sender policy | Nonpositive write versus native helper−1, close/reset, remaining-write skip, both output deletion paths and sender return0 agree with the reported selected fixtures. Short-positive handling remains a caller/helper observation; descriptor/non-SSL/I/O/free primitives, delivery and real reclamation limits are explicit. |
| Alarm publication | Same staged normal WHO5/WHAT17 object, original callbacks/serializer and exact `*5*17*#5##` ten-byte request agree with the report. One private connection, GLib traversal/string/send primitives and pre-message-destruction stop remain visible; full consumer completion and physical alarm meaning are not inferred. |
| Markup utility | The utility read/chunk guards and selected caller end-parse/close continuation agree with the source. Supplied markup registers are not promoted to real GLib acceptance/recovery, a formal aggregate return contract, full wrapper result or validation-bypass claim. |

The index/capsule correctly distinguish static inspection, bounded original-helper execution, whole-process execution and Physical Device observation. Report hashes identify the basis; the capsule explicitly lacks binaries/full harness/handoffs and does not claim self-contained execution reproduction. Reused setup/reports are not independent corroboration. Literal frame examples remain code-formatted and synthetic.

## Device disposition and remaining work

The updated Device page supersedes the earlier unexamined-payload statement only for the incorporated paths. It keeps catalogue1.0.37/2.0.1 capability records, package2.0.51, official release history and observed gateway identity separate. No new catalogue Firmware row, additional hardware capability, installed version or active Configuration is inferred. Existing physical/capture evidence is linked rather than rerun or replaced.

The work queue intentionally stays `review-ready`: source reconciliation/final review and affected evidence/architecture/usefulness/limits/presentation/validation gates remain pending, while prior identity grouping and hardware-corroboration disposition are retained. This focused review does not change those gates. Further dossier-to-canonical-reference reconciliation, runtime/providers/ownership, persistent/optional assets, VDE activation, energy/temperature/WHO17 meaning and physical applicability remain open.

No further correction is required within the reviewed selected incorporation. Parent mechanical/Device checks are recorded separately; this review does not claim to have independently executed them.
