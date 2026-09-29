# Device Definitions

This directory contains the canonical technical Device pages.

## Identity and filenames

Each Device definition receives a stable project-assigned Device ID, for example `OWN-DEV-0042`.

Use that ID plus a concise technical descriptor in the filename:

```text
own-dev-0042-two-channel-din-lighting-actuator.md
```

The stable ID is the canonical Encyclopedia identity. The descriptive suffix exists only to keep directory listings and repository searches understandable.

Do not use a manufacturer or SKU as the canonical filename merely to select one commercial identity over another.

## Commercial identities

A Device definition may include several brand / SKU identities. Their equivalence must be supported by evidence and may be revised when new evidence appears.

The [Complete Device Index](../index.md) must contain a separate searchable row for every known commercial identity.

## Split and merge behavior

If later evidence shows that identities grouped under one Device definition are technically distinct, create a new Device definition and document the split. Do not reuse a Device ID for a different technical Device.

If two previously separate definitions are established to describe the same technical Device, preserve both histories and document the relationship rather than silently deleting provenance.

## Page structure

Start new definitions from the [Device Page Template](../contributing/device-page-template.md).
