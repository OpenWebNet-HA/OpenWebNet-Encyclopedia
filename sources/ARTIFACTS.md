# External Artifact Archive

sources/artifact-manifest.yaml is the authoritative cross-bucket inventory of vendor-origin artifacts used as evidence by this project.

Git stores project-authored analysis, provenance, hashes, and metadata. Vendor-origin binary artifacts are stored outside Git:

- openwebnet-documents - public publisher documentation
- openwebnet-data - private canonical databases and support data
- openwebnet-software - private installers and firmware

Artifacts are content-addressed by SHA-256. Private bucket endpoints and credentials are intentionally not recorded in Git.

## Documentation language

Every PDF artifact has a language list. ISO 639-1 codes are used when the document language is established. und means the language has not yet been established confidently. language_evidence records whether the value comes from the known canonical corpus, the filename, or remains undetermined.

## Identity

The SHA-256 digest identifies the exact archived bytes. Multiple former repository paths that contained identical bytes are represented by one artifact with multiple former_paths.

## Software

Firmware version labels are retained exactly as established by publisher metadata or filenames. They should not be normalized into a semantic version unless independent evidence establishes that interpretation.
