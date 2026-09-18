# Machine Knowledge Privacy Policy

The machine-readable knowledge base is public and may be copied into language-model contexts, embeddings, search indexes, training or evaluation sets, logs, caches, and downstream databases. It must never contain private information.

This is a publication gate, not a best-effort cleanup step. Generation must fail closed if a value cannot be shown to be safe.

## Prohibited content

Generated artifacts must not contain concrete:

- IPv4 or IPv6 addresses, including protocol payload forms whose octets are separated by `*`;
- MAC addresses in hexadecimal, decimal-octet, or raw frame form;
- installed Device IDs, gateway IDs, serial numbers, UUIDs, hardware identifiers, or other instance identifiers;
- passwords, password-derived material, authentication challenges, nonces, proofs, tokens, keys, cookies, or credentials;
- private hostnames, local domains, SSIDs, network names, ports paired with private endpoints, or service-discovery records;
- email addresses, usernames, account identifiers, personal names from captures, filesystem user paths, or other user-identifying data;
- geographic coordinates, street addresses, site names, room assignments, or customer/project identifiers;
- raw or reconstructed private capture frames, timestamps, traffic sequences, logs, screenshots, inventories, or configuration exports;
- installation topology, configured functional addresses, group memberships, scenarios, schedules, usage patterns, or device-to-room associations derived from a private installation;
- hashes or opaque identifiers that refer back to private source files, captures, people, installations, or accounts.

The prohibition applies equally to text, JSON fields, metadata, stable IDs, filenames, URLs, examples, comments, logs, fixtures, embeddings, and derived summaries.

## Allowed abstractions

The knowledge base may describe a sensitive field as a protocol concept without publishing a concrete observed value. Use symbolic forms such as `IP1*IP2*IP3*IP4`, `MAC1*MAC2*MAC3*MAC4*MAC5*MAC6`, `[DEVICE_ID]`, `[WHERE]`, and `[REDACTED]`.

Publicly documented ranges, field widths, schemas, algorithms, and placeholder frames are allowed when they cannot identify an installation or person. Synthetic examples are allowed only when unmistakably marked as synthetic and when the privacy validator cannot confuse them with real data. Prefer placeholders over realistic values.

Public source provenance may include the repository-relative source path, publication title, publisher, document version, and public URL. It must not include local filesystem paths, private storage locations, or private-source hashes.

## Extraction rules

1. Classify the source and every candidate field before copying text.
2. Exclude private captures, logs, inventories, screenshots, and user-provided configuration exports from all machine-input sets.
3. Replace concrete sensitive values in otherwise publishable prose before chunking or claim extraction.
4. Generalize capture-supported conclusions to the narrowest non-identifying statement supported by the documentation.
5. Do not use a sensitive source value to construct a record ID, filename, relationship key, or embedding label.
6. Propagate a privacy classification through every derived record.
7. Write generated output only after pre-generation privacy checks pass.
8. Scan the complete generated tree again before publication and fail on every match.

Redaction markers must identify the value class without retaining reversible material. Never hash or encode a private value as a substitute for deletion.

## Required metadata

Each generated record must carry a privacy classification. The initial vocabulary is:

| Value | Meaning |
| --- | --- |
| `public` | Derived only from publishable sources and contains no concrete private value |
| `sanitized` | One or more private or installation-specific values were removed before this record was constructed |

No `private`, `unknown`, or missing privacy classification is publishable. A `sanitized` record must name the removed value classes, such as `device_id` or `network_address`, without recording the values.

## Validation and release gate

[`validate_privacy.py`](../tools/validate_privacy.py) scans generated artifacts for forbidden concrete forms. Schema validation must also require the privacy classification and reject unexpected fields that could carry unreviewed data.

Pattern scanning cannot establish safety on its own. Generation must combine source allowlisting, field-aware transformations, schema restrictions, and final scanning. Any positive match, ambiguous value, or validator failure blocks publication until the artifact is corrected and regenerated.
