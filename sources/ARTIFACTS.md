# External Artifact Archive

sources/artifact-manifest.yaml is the authoritative cross-bucket inventory of vendor-origin artifacts used as evidence by this project.

Git stores project-authored analysis, provenance, hashes, and metadata. Vendor-origin binary artifacts are stored outside Git:

- openwebnet-documents - public publisher documentation
- openwebnet-data - private canonical databases and support data
- openwebnet-software - private installers and firmware

Artifacts are content-addressed by SHA-256. Private bucket endpoints and credentials are intentionally not recorded in Git.

## Manifest roles

The manifests have deliberately different responsibilities:

- sources/artifact-manifest.yaml is authoritative for artifact identity, storage location, visibility, redistribution status, language metadata, and repository history.
- sources/archive/pdf-manifest.json is an operational public-document index. Every entry must be represented by the authoritative artifact manifest.
- sources/manifest.yaml describes the canonical evidence corpus and source-set semantics. MyHOME Suite artifact fingerprints and R2 locations recorded there must agree with the authoritative artifact manifest.

CI enforces these relationships so the views cannot silently drift apart.

## Documentation language

Every PDF artifact has a language list. ISO 639-1 codes are used when a single document language is established. mul denotes multilingual content and und is reserved for genuinely undetermined language. language_evidence records how the assignment was established.

## Identity and repository history

The SHA-256 digest identifies the exact archived bytes. Multiple former repository paths that contained identical bytes are represented by one artifact.

Historical Git locations are recorded only when an artifact was actually tracked by this repository, under repository_history.former_paths. This is distinct from publisher provenance such as source_url and from original installation paths such as a MyHOME Suite path under C:\ProgramData.

## Software and private data

openwebnet-data and openwebnet-software remain private by default. Public metadata preserves exact identity and provenance without making OpenWebNet-HA a redistribution mirror for vendor data, installers, or firmware.

Firmware version labels are retained exactly as established by publisher metadata or filenames. They are not normalized into semantic versions unless independent evidence establishes that interpretation.
