# Canonical Sources

This directory is the evidence corpus used to document and reverse-engineer OpenWebNet.

## Canonical-source policy

Files under `sources/` are preserved as original evidence. They must not be modified to encode inferred relationships, corrections, normalized data, or other analysis. Derived schemas, ERDs, exports, and interpretations belong outside this directory.

`manifest.yaml` is the machine-readable provenance registry. SHA-256 is the canonical fingerprint. Git blob SHAs are repository identifiers and are not used as source fingerprints.

## Source sets

- `myhome-suite/3.5.38/` — files copied unmodified from MyHOME Suite 3.5.38.
- `openwebnet-public/` — publicly distributed OpenWebNet protocol documentation.

The MyHOME Suite installer is fingerprinted in the manifest for provenance but is not redistributed in this repository.

## Private evidence

Network captures are intentionally excluded from the repository because they can contain private installation and network information. Conclusions supported by private captures may be documented, but the captures themselves are not part of the published corpus.

## Verification

For a source file, calculate SHA-256 over the exact file bytes and compare it with the corresponding `sha256` entry in `manifest.yaml`. A mismatch means the file must not be treated as the canonical source identified by that manifest entry.
