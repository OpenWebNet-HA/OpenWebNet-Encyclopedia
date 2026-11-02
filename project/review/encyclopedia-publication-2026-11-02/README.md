# Publication Follow-up

This record supplements the [completed editorial reconciliation](../encyclopedia-editorial-reconciliation-2026-11-02/). The earlier unstaged whitespace check did not include newly added files. Staging exposed one surplus final blank line in a reference page and authentic whitespace in preserved tool-output exports.

| Material | Publication treatment |
| --- | --- |
| `internals/device-application-databases.md` | Removed exactly one surplus final newline; prose, tables, section identities and source-unit line locations are unchanged |
| Firmware evidence `.txt` exports | Preserve original bytes, including tool padding and blank records; scope Git whitespace handling to these verbatim exports |
| One exact `source-checks.json` evidence record and the exact publication before-copy | Preserve their original bytes under the same narrowly declared treatment |
| Ordinary Markdown, Python and other structured inputs | Retain normal whitespace checking |

The [exact old/current mappings](identity-mappings.json) and byte-identical before copies preserve the prior identities. Existing editorial/evidence indexes remain historical snapshots of their recorded assembly; this addendum explains the two current-file differences rather than silently changing their expected hashes.

A fresh official parse of the complete 393-document canonical tree produced an [identical semantic IR](ir-equivalence.json) to the fully validated projection. Curated assertions, generator/schema/privacy/Device-gate code, source evidence bytes and generated knowledge artifacts are unchanged. The earlier complete build/global check therefore concerns the same semantic inputs and outputs; the fresh parse is not represented as a second complete global validation run.

Git supports path-specific whitespace treatment through the documented [`whitespace` attribute](https://git-scm.com/docs/gitattributes#_checking_whitespace_errors). These declarations preserve verbatim evidence and do not waive the encyclopedia's presentation or evidence standards. Commit/push results and exact-commit catalogue status belong to the actual GitHub commit and private publication receipts, rather than a predicted result in this prepared tree.
