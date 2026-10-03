# Contributing Device definitions

This directory contains the authoring guidance for canonical Device definitions.

Start from the [Device Page Template](device-page-template.md). Device pages remain subject to the repository-wide [Encyclopedia Core Values](../../project/encyclopedia-core-values.md) and [Encyclopedia Style Guide](../../project/encyclopedia-style-guide.md), including evidence qualification, canonical model terminology, technical-literal formatting, semantic links, and explicit preservation of unresolved points.

The section-wide completion policy and identity model are defined in [Devices](../README.md).

## Authoring branch and artifact registration

Create and update Device descriptions directly on `docs/devices-foundation`.

When a new vendor artifact is retained, upload its original bytes to the appropriate archive bucket and verify its SHA-256 and size. Immediately register the verified artifact in `sources/artifact-manifest.yaml` on `main` using the [main artifact registration workflow](../../sources/ARTIFACTS.md#registering-a-newly-archived-artifact). Register it before continuing the Device description; registration must not wait for the documentation branch or a pull request to merge. Sync the authoritative manifest into `docs/devices-foundation` before referencing the new artifact.
