# Device Sources

This directory inventories authoritative, device-specific source material used by the [Devices](../../devices/) section.

The goal is to locate and preserve provenance for the broadest practical set of official product documentation, including discontinued and historical material.

## Source types

Relevant material includes:

- technical and product datasheets;
- installation sheets;
- configuration and commissioning instructions;
- programming manuals;
- user manuals containing technical behavior;
- product catalogue pages;
- compatibility tables;
- firmware documentation and release notes;
- official application notes;
- official documentation variants whose content materially differs by language, region, or revision.

Prefer manufacturer or publisher originals over mirrors when both are available.

## Organization

When source files are retained in the repository, organize them by manufacturer and SKU where practical:

```text
sources/devices/
    bticino/
        h4652-3/
        f411u2/
    legrand/
        067250/
```

A document covering several products may instead live at the narrowest sensible shared location. Do not duplicate identical source files merely to place them under several SKUs.

## Provenance

Every retained source file must be registered in [the source manifest](../manifest.yaml) and fingerprinted with SHA-256.

For each document, preserve or record as much of the following as can be established:

- publisher;
- title;
- document or reference number;
- applicable SKU or product family;
- language;
- publication or revision date;
- source URL;
- retrieval date;
- original filename;
- SHA-256;
- document type;
- redistribution status.

If redistribution is uncertain or not permitted, do not commit the document solely for convenience. Record enough provenance to identify the exact source, including its authoritative URL and fingerprint when the bytes are available locally.

The absence of a redistributed PDF must not erase the existence of the source from the research record.

## Preservation

Files retained under `sources/` are canonical evidence and remain byte-for-byte originals. Do not annotate, normalize, re-save, OCR, translate, or otherwise modify them in place.

Derived notes, extracted facts, normalized configuration models, and interpretations belong on Device pages or in the appropriate Encyclopedia reference section.

## Relationship to implementation sources

Vendor databases and software artifacts under other source sets may contain product identity, capability, and configuration facts not present in published PDFs.

Those artifacts remain separate source sets. Device pages may combine evidence from official documents, implementation artifacts, and physical observations while preserving the provenance and evidence status of each claim.
