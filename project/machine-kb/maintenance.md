# Machine KB Maintenance

## Normal contributor workflow

1. Edit authoritative, non-guide Encyclopedia documentation and public provenance. Promote a guide-only fact to canonical documentation first.
2. Run python build.py. Generated outputs are never hand-edited.
3. Inspect the complete generated diff, including provenance, relationships, applicability, and privacy classification.
4. Run the single check command: python check.py. It verifies deterministic rebuilds, schemas, freshness, referential integrity, claim consistency, cross-artifact consistency, and privacy.
5. Review affected claims and records with python diff_impact.py --base <base-revision> --head WORKTREE. Treat full_review_required as a full review requirement.
6. Commit authoritative documentation and generated changes together after all checks pass. CI never commits generated artifacts.

Builds and validators remain offline and model-free. Source provisioning is a separate CI setup step; it does not run inside generation. Follow the [privacy policy](../../knowledge/policy/privacy.md): exclude private inputs and sanitize publishable-sensitive material before derivation; never put private values in fixtures, IDs, logs, examples, or review notes.

## Private catalogue CI result

The complete KB workflow requires the authorized maintainer's `Device catalogue validation` GitHub commit status. The catalogue remains on a trusted maintainer machine; no archive credential or private database is supplied to GitHub runners. This CI setup authenticates its read of GitHub status metadata before offline validation. Missing, pending, failed, superseded or stale results cannot satisfy the gate.

After committing and publishing a candidate, run the following from its clean checkout:

```sh
python devices/tools/catalogue_ci_status.py validate-local --commit <full-commit-sha> --publish
```

The local gate verifies the registered private catalogue SHA-256 and byte length, runs complete Device/catalogue validation and all Device gate regressions, and checks that the candidate did not change during execution. It publishes only a status, candidate SHA and digest of public gate inputs. It does not publish database contents or local failure details. `anotherjulien` is the explicitly authorized validator; changes to that trust policy require maintainer review.

Hosted CI verifies the latest result for the pull request's head commit or the pushed commit. The digest includes all Device definitions, index, acceptance ledger, catalogue tools, source manifests, the complete check driver and the KB workflow. A pull-request merge checkout that changes any of those inputs requires a new local validation. Every newly published commit, including a merge or squash commit on main, needs its own local result; a green head-commit result is never silently copied to a different SHA. Other public KB generation, schema, evidence, lifecycle, conservation and privacy gates remain on the GitHub runner. Local `python check.py` still runs catalogue completeness directly; its CI status-file mode is supplied only after authenticated GitHub verification and rechecks the candidate input digest.

The trusted machine must be available to validate a new candidate; it can do so without a recurring approval prompt. No GitHub environment protection or archive secret is created by this arrangement. Do not record private values in status descriptions, test fixtures, logs or public review records.
