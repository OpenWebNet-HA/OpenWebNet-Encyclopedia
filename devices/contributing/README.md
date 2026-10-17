# Contributing Device Definitions

This directory contains the authoring guidance for canonical Device definitions.

Start from the [Device Page Template](device-page-template.md). Device pages remain subject to the repository-wide [Encyclopedia Core Values](../../project/encyclopedia-core-values.md) and [Encyclopedia Style Guide](../../project/encyclopedia-style-guide.md), including evidence qualification, canonical model terminology, technical-literal formatting, semantic links, and explicit preservation of unresolved points.

The [Device Definition Presentation Profile](device-definition-presentation-profile.md) governs the section architecture, evidence tables and eight-check acceptance gate. The section-wide completion policy and identity model are defined in [Devices](../README.md).

## Maintenance tools

The closed review run retains its machine-readable acceptance ledger and detailed project review reports. Future evidence changes reopen the affected checks under the presentation profile; hardware corroboration remains optional when its absence and consequences are explicit.

Run `python3 devices/tools/build-device-work-queue.py --check` from the repository root to validate the ledger without generating a public progress page. An optional `--output` path outside the repository exports a research dashboard. `python3 devices/tools/build-device-inventory.py --output-dir <private-directory>` exports raw catalogue research tables outside the repository. These exports are working aids rather than curated reference pages; do not publish them in place of Device definitions. Both tools can check an existing export with `--check`.

Run `python3 devices/tools/check-device-definitions.py` for catalogue completeness and Device presentation checks, and the repository ECV/ESG and artifact checks for evidence integrity, privacy and links. The Device check also requires every accepted definition and every canonical commercial record to remain discoverable in the index. A read-only canonical catalogue copy can be supplied with `--database`; otherwise the registered private source cache is used.

## Authoring branch and artifact registration

Create and update Device descriptions directly on `docs/devices-foundation`.

When a new vendor artifact is retained, upload its original bytes to the appropriate archive bucket and verify its SHA-256 and size. Immediately register the verified artifact in `sources/artifact-manifest.yaml` on `main` using the [main artifact registration workflow](../../sources/ARTIFACTS.md#registering-a-newly-archived-artifact). Register it before continuing the Device description; registration must not wait for the documentation branch or a pull request to merge. Sync the authoritative manifest into `docs/devices-foundation` before referencing the new artifact.
