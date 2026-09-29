# Archived Device Documents

This directory stores byte-for-byte originals of device-specific documents that the project can lawfully retain and redistribute.

Each distinct source revision lives under its stable source ID:

```text
documents/
    <source-id>/
        <original-filename>
```

Do not use brand or SKU as the canonical storage hierarchy. One document may apply to several commercial identities, and one commercial identity may have many document revisions.

Every retained file must also be registered in [the source manifest](../../manifest.yaml) and listed in the [Device Source Index](../index.md).

Never overwrite an archived source with a newer revision. Add the newer revision as a new source.
