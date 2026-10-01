# PDF archive

The Encyclopedia's binary PDF sources are stored in the OpenWebNet-HA R2 archive rather than Git.

- Public base URL: https://archive.openwebnet-ha.org
- Objects are addressed by SHA-256 using sha256/<first-2>/<next-2>/<sha256>.pdf.
- pdf-manifest.json records the former repository path, byte size, SHA-256, object key, and public URL for every migrated PDF.
- Publisher-source URLs remain on the Encyclopedia pages where they were already recorded; the manifest does not invent missing provenance.
- New PDFs must be ingested through the archive workflow and must not be committed to Git.
