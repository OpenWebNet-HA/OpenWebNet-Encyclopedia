# F450 and F459 database-format evidence

No plaintext application database was recovered from the inspected F450 standard/PROD `2.0.10` and F459 archive `020105`/local `2.1.5` views. This is a finite format-search result, not a product-capability or universal database-absence claim. The [application-data reference](remaining-firmware-database-handoff.md) separates database bytes from compiled SQL, libraries and requested pathnames.

## Original-byte scope and result

The source scope is three packages and four separate filesystem views: F450 standard/PROD normal images and F459 normal/recovery images. Each selected regular-file occurrence is identified by its own manifest size/hash; identical payloads share a byte search with separate provenance. The search covers every byte offset for its declared finite signature set, not all possible formats or encodings.

| Candidate | Result | Interpretation |
| --- | --- | --- |
| SQLite3 signature | Seven occurrences; none passes the selected header checks | No database promoted at those offsets |
| SQLite2/BDB/GDBM/LMDB words/prefixes | Forty-one occurrences | Unparsed leads without assigned header layout or extent |
| Candidate-containing files | ELF magic at file start | Container context only; an ELF may contain data in principle |
| Eligible archive content | Encrypted support container; no plaintext members opened | No decrypted database bytes |

A signature does not establish a complete header, page extent or readable schema. SQLite3 checks require an ordinary selected format version, valid page-size/fraction constraints, reserved bytes and first-page admission. A stale/legacy header pagecount is not used to reject a candidate. The [official format specification](https://www.sqlite.org/fileformat.html) provides format context, not the vendor's effective library version.

Alternate signatures remain unparsed. Other compression/encryption, fragmented/custom stores, unallocated image content and runtime-created/configured data are outside this result. [Exact format evidence](../../project/review/firmware-analysis/sequential-databases-2026-11-02/README.md) records original inputs, candidate offsets, header rejection reasons and scope qualifications.

## Original data

F450 PROD `50.xtz` has an encrypted member named `50/master.sqlite`. The original container is preserved as supporting data, while its plaintext database remains unrecovered. Its [classified record and receipt](../../project/review/firmware-analysis/remaining-firmware-2026-11-01/archive-index.json) do not identify a recovered SQLite schema or rows. This source scope contains one preserved encrypted support object and zero plaintext database objects.

## Evidence limits

The [F450/F459 source contracts](f450-f453av-f455-f459-mh200n.md#selected-implementation-contracts) identify consumers and representations; they do not establish a packaged plaintext database, accepted data, provider binding or successful persistence. A properly attributed original plaintext file, configured export or qualified alternate-format extent remains the missing data source. No SQL query, repair, transformation or decryption result supports this format assessment.
