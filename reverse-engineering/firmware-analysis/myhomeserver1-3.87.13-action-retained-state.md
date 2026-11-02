# MyHOMEServer1 3.87.13 Retained Action State

The first and second selected `BN3L` callable bodies access the same fixed global storage. A first-callable query can copy a returned state string there; a second-callable branch can convert retained exact `on` into a local `status: on` parameter request. This is conditional dataflow in [MyHOMEServer1 Firmware 3.87.13](myhomeserver1-3.87.13.md), without established callback order, fresh same-ID state or successful restoration.

## Shared retained storage

The [action handoff](myhomeserver1-3.87.13-action-output.md) identifies separate first and second captures. On the selected first path, nonzero captured duration permits a query with the captured configured ID. A null returned pointer skips copying. A suitable nonnull result supplies a string at record `+8` and words at `+36/+40/+44`.

Independent source-address joins resolve the same writable global in both bodies. It lies in memory-only `.bss`, so its runtime contents are not packaged-file data. The first body requests assignment of that returned string to the global's string member and copies the three words to separate global members. Those numeric properties and their consumers remain unclassified.

The query argument does not turn fixed-address storage into a proven per-ID map. The retained global and the adjacent shared action-stop byte have different addresses and roles; adjacency establishes neither aliasing nor ownership. Valid record/type, matching identity/freshness, successful provider returns and continued storage lifetime remain premises. [Retained-state evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-action-retained-state/README.md) preserves the exact source-address and copy joins.

## Retained string to status parameter

The second body reads that same string pointer/length pair. A selected exact two-character `on` comparison reaches a local status assignment: the code stores local status `0` and marks it present. An actual pair copy transfers those presence/value fields into the separate parameter-converter input; the earlier local prefix record is not overlaid on that input.

With status present, the converter increments code `0` to table index `1`, obtains original string `on`, requests a JsonCpp string and assigns exact member `status`. The code is not a public OPEN WHAT or raw action discriminator. Other strings and branches are not generalized into a full state matrix.

If the first path writes a valid `on` string, it survives until the selected second read, all required branches are reached and providers return normally, the second parameter object receives a `status: on` assignment request. The [descriptor contract](myhomeserver1-3.87.13-action-request-values.md) separately supplies `2.0` / `light.setStatus`.

## Evidence limits

The query and local output helpers remain opaque boundaries. Effective record type, ID/freshness, global initialization/mutation/locking, natural paired invocation, complete parameters, ownership, errors/unwind and concurrency remain unresolved. No prior-state restoration, rollback, collision/defect, delivered request or physical outcome is established by this global producer/consumer pair.
