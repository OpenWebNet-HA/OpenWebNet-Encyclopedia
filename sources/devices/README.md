# Device Sources

This directory is the archival source corpus for device-specific material used by the [Devices](../../devices/) section.

The project treats device documentation as archival evidence. Vendor product pages and files may disappear or be silently replaced when products age out of support, so distinct source revisions should be preserved when they can be lawfully retained and redistributed.

## Archival policy

Preserve every distinct obtainable revision of a relevant device document rather than replacing an older file with the latest version.

Relevant material includes:

- technical and product datasheets;
- installation sheets;
- configuration and commissioning instructions;
- programming manuals;
- user manuals containing technical behavior;
- product catalogue pages;
- compatibility tables;
- Firmware documentation and release notes;
- official application notes;
- official documentation variants whose content materially differs by language, region, or revision.

Prefer manufacturer or publisher originals over mirrors when both are available, but do not discard an older or otherwise unavailable revision merely because only a secondary copy remains accessible.

The original URL is provenance, not availability. Once a document is archived, its evidentiary value must not depend on the vendor continuing to host it.

## Organization

Do not organize canonical source files by one preferred brand or SKU. A single document may apply to several commercial identities or several technical Device definitions.

Use a stable source identity for each distinct document revision:

```text
sources/devices/
├── README.md
├── index.md
└── documents/
    ├── README.md
    ├── <source-id>/
    │   └── <original-filename>.pdf
    └── <source-id>/
        └── <original-filename>.pdf
```

Identical bytes should be stored once even when they apply to many SKUs. Distinct revisions, languages, or region-specific documents remain separate sources when their bytes or substantive content differ.

## Device Source Index

[Device Source Index](index.md) is the human-readable inventory of preserved and known device documentation.

It should make it possible to find documents by brand, SKU, title, document number, revision, date, or language.

## Provenance

Every retained source file must be registered in [the source manifest](../manifest.yaml) and fingerprinted with SHA-256.

For each document, preserve or record as much of the following as can be established:

- stable source ID;
- publisher;
- brand or brands;
- applicable SKU or SKUs;
- related technical Device definition IDs;
- document title;
- document or reference number;
- document type;
- language;
- publication date;
- revision;
- retrieval date;
- original URL or URLs;
- original filename;
- SHA-256;
- redistribution / archival status;
- supersedes / superseded-by relationships where established.

If redistribution is uncertain or not permitted, do not commit the document solely for convenience. Record enough provenance to identify the exact source, including its authoritative URL and fingerprint when the bytes are available locally.

The absence of a redistributed PDF must not erase the existence of the source from the research record.

## Preservation

Files retained under `sources/` are canonical evidence and remain byte-for-byte originals.

Do not annotate, normalize, re-save, OCR, translate, optimize, or otherwise modify archived originals in place.

Derived notes, extracted facts, normalized configuration models, and interpretations belong on Device definitions or in the appropriate Encyclopedia reference section.

## Relationship to Device pages

Every Device definition should include a **Documentation** section linking directly to all applicable archived originals, including older revisions where available.

A source can apply to several Device definitions. A Device definition can cite many source revisions.

## Relationship to implementation sources

Vendor databases and software artifacts under other source sets may contain product identity, capability, and configuration facts not present in published PDFs.

Those artifacts remain separate source sets. Device definitions may combine evidence from official documents, implementation artifacts, and physical observations while preserving the provenance and evidence status of each claim.
