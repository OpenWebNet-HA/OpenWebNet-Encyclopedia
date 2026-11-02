# Configured scene inputs in MyHOMEServer1 and F460

The inspected packages supply manager settings and selected file-loading code, but no genuine populated scene/module export. This limits reconstruction of complete configured behavior. Manufacturer defaults and storage paths can explain application structure; they do not replace actual configured objects.

## Available assets and their roles

| Source | Retained material | Interpretation |
| --- | --- | --- |
| MyHOMEServer1 `3.87.13` normal/recovery | Six scheduler-manager settings and a declared scene-directory prefix | No populated scene admitted in that selected scope |
| F460 `2.0.12` normal/recovery | Scheduler-manager defaults and scene-directory prefix | No populated scene admitted in that selected scope |
| F461 `2.0.11` | Packaged manager/plugin logging and communication settings | No commissioned module instance or accepted runtime record |
| MyHOME Suite and MH202 defaults | Project/plant templates and separate default-project assets | Product-specific manufacturer templates, not MHS/F46 configured scenes |

These are finite source-admission results, not runtime directory-emptiness or product-capability conclusions. The [asset evidence](../../project/review/firmware-analysis/configured-inputs-2026-11-02/reviews/asset-admission-review.txt) identifies exact sources without exporting private values.

## F460 filesystem selection

A selected `scheduling_manager` prefix obtains a directory-iterator entry, requests extension/path operations and compares a locally constructed `.json` path. The matching branch leaves the inspected interval; a later zero-state continuation is a separate predecessor premise. It is not a complete extension filter or list of accepted files.

A later selected comparison uses a path constructed from `action_schedule.json`. Zero bypasses an immediately following allocation; nonzero reaches a scene-construction boundary. The compared storage's origin and semantic identity are not fully established. This local gate therefore does not prove a global basename exclusion, ignored-file policy or successful parse. [Filesystem source evidence](../../project/review/firmware-analysis/configured-inputs-2026-11-02/reviews/f460-source-review.txt) retains the object and branch conditions.

## F460 scene input file opening

The selected SceneRunner constructor passes its destination and supplied source argument into a local helper. After path/status requests and a selected continuing branch, the source's first word becomes the filename argument to `basic_filebuf::open` with numeric mode `8`. Zero return leaves the inspected interval; the selected nonzero path requests stream-state clearing and constructs JSON reader/value objects.

The retained interval ends before a parse call or result. It establishes a conditional source-to-open request, not successful reading, parsed-root publication, accepted JSON or a complete schema. Composition with the filesystem gate requires natural caller correlation, valid preserved objects and functioning providers; register/storage reuse alone does not establish the same semantic object. [Input source evidence](../../project/review/firmware-analysis/configured-inputs-2026-11-02/packets/f460-input/REPORT.txt) records the actual call and boundary.

## MyHOMEServer1 validation-order caution

In selected MyHOMEServer1 code, nonconst category lookup precedes later membership checks. Under ordinary JsonCpp behavior, membership tested after lookup does not alone prove that the original input required that member. Conversely, absence of a name-presence test in one numeric branch does not establish that names are optional throughout the parser.

This is an interpretation constraint, not a complete schema, newly demonstrated accepted input or defect. MHS Thumb layouts, F460 AArch64 layouts and F461 module settings remain separate. See the [policy evidence](../../project/review/firmware-analysis/configured-inputs-2026-11-02/mhs-policy-note.txt) and [MyHOMEServer1 implementation](myhomeserver1-3.87.13-research-synthesis.md).

## Evidence limits

The [source/review record](../../project/review/firmware-analysis/configured-inputs-2026-11-02/README.md) retains exact identities, selected paths, interpretation history and method limits. The evidence is source inspection and asset metadata; it does not execute a configured file, parser or target process.

A genuine scene export or attributed generator asset is needed to connect actual values to these loaders. Parsing/root publication, complete validation policy, effective providers and natural object correlation remain unresolved. These source prefixes are insufficient to publish a complete offline validator or guarantee deployed behavior.
