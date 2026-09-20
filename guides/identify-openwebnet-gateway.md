# Identify an OpenWebNet Gateway

## Goal

Determine and present the catalogue identity of an unknown classic SCS/TCP OpenWebNet gateway from raw protocol responses and the canonical MyHOME_Suite databases.

This is a specialized instance of [Read and Present a Device Configuration](read-device-configuration.md). It narrows that general workflow to gateway identity and remains independently executable: acquire the relevant responses, preserve their provenance, resolve the diagnostic identity through the catalogue, and stop when the evidence does not justify a unique product identity.

The intended result is not merely a guessed model name. It is a reproducible identity record containing the raw frames, the separate `WHO 13` and diagnostic `WHO 1013` values, the exact catalogue lookup, every surviving `EN_DEVICE` candidate, and an explicit resolution status.

## Prerequisites

- a command session to the gateway that can send supported OpenWebNet read requests and preserve response direction and order;
- access to the canonical `OPEN.db` and `MHCatalogue.db` revision used for the lookup;
- the raw gateway traffic, including timeouts, `ACK`/`NACK`, and transport closure where present;
- classic SCS/TCP gateway context. The ZigBee `WHO 13` registry is a separate variant and is not identified by this procedure.

No gateway model is assumed before the protocol and catalogue evidence are resolved.

## Evidence boundary

| Statement used by this guide | Epistemic status | Permitted use |
| --- | --- | --- |
| Classic `WHO 13 DIMENSION 15` is the published Device type/model property | **Published protocol** | Record the historical gateway-type value exactly as returned |
| MyHOME_Suite defines diagnostic `WHO 1013` for Integration Functions and a gateway `DIMENSION 1` response carrying `OBJECT_MODEL`, `N_CONF`, `BRAND`, and `LINE` | **Implementation evidence** | Parse the four gateway-identity fields without merging their namespace with `WHO 13 DIMENSION 15` |
| `OBJECT_MODEL`, `BRAND`, and `LINE` correlate with `AS_ITEM_SYSTEM.modobj`, `EN_BRAND.brand_modobj`, and `EN_LINE.line_modobj` in the resolved catalogue system | **Implementation evidence** with corroborated cross-source correlation | Resolve catalogue candidates through the established semantic mapping, not numeric primary-key equality |
| Observed MH202 and F454 captures both return `WHO 13 DIMENSION 15 = 200`; their `WHO 1013 DIMENSION 1` payloads are `5*15*5*0` and `51*15*5*0` respectively | **Observed behavior** | Demonstrate that `200` is non-unique and exercise the catalogue-resolution path on two concrete gateways |
| `DIMENSION 15 = 200` cannot uniquely distinguish MH202 from F454 | Derived from the two observations above | Require additional identity evidence before selecting one of those models |
| Support for `WHO 1013 DIMENSION 1` across every older gateway model and firmware revision | **Unresolved** | A timeout or absent response must remain an absence of evidence, not a compatibility or age claim |

The gateway form reuses the field names `OBJECT_MODEL`, `N_CONF`, `BRAND`, and `LINE`. Do not automatically import every range or interpretation from the ordinary addressed Device form into this gateway variant. In particular, the observed MH202 and F454 gateway tuples contain values outside some ordinary addressed-form ranges. This guide therefore preserves `N_CONF` as the raw gateway-variant field and does not use it to identify the catalogue model.

## 1. Read the documented `WHO 13` gateway type

Send the published read request:

```text
Client -> Gateway: *#13**15##
Gateway -> Client: *#13**15*[MODEL]##
```

Preserve `MODEL` exactly as received. The published historical model table in the [`WHO 13 DIMENSION` Reference](../functional/who-13-integration-gateway/dimensions.md#dimension-15---device-type) gives meanings for the values defined by that specification, but it is not an exhaustive catalogue of later gateways.

Do not use this value as a direct key into `MHCatalogue.db`. In particular:

- do not equate `WHO 13 DIMENSION 15.MODEL` with `AS_ITEM_SYSTEM.modobj`;
- do not infer an `EN_DEVICE` row from numeric equality;
- do not generalize historical cases where a `DIMENSION 15` value happens to resemble another model identifier.

For the observed MH202 and F454 captures, this step yields the same value:

```text
Gateway -> Client: *#13**15*200##
```

That observation is sufficient to prove that `200` is not a unique discriminator between those two gateway models. Continue with the diagnostic identity layer.

## 2. Read diagnostic `WHO 1013 DIMENSION 1`

For the Integration Functions diagnostic family, send the empty-`WHERE` `DIMENSION 1` read:

```text
Client -> Gateway: *#1013**1##
```

The gateway identity response has the form:

```text
Gateway -> Client: *#1013**1*[OBJECT_MODEL]*[N_CONF]*[BRAND]*[LINE]##
```

Retain the complete raw frame before interpreting its fields. The canonical MyHOME_Suite implementation names these fields:

| Position | Field | Use in this guide |
| ---: | --- | --- |
| 1 | `OBJECT_MODEL` | Resolve against `AS_ITEM_SYSTEM.modobj` inside the Integration Functions catalogue system |
| 2 | `N_CONF` | Preserve as returned; do not use it as a catalogue key |
| 3 | `BRAND` | Resolve against `EN_BRAND.brand_modobj` |
| 4 | `LINE` | Resolve against `EN_LINE.line_modobj` |

If the request receives no matching response, times out, is rejected, or the connection closes, preserve that outcome and stop the primary catalogue-resolution path. Report `WHO 1013 DIMENSION 1` as not obtained. Do not report that the gateway is too old, that it does not support the operation, or that older gateways generally lack the operation unless separate factual evidence establishes that conclusion.

## 3. Keep the two model namespaces separate

The two identity layers answer different questions:

| Value | Namespace | Safe interpretation |
| --- | --- | --- |
| `WHO 13 DIMENSION 15.MODEL` | published functional `WHO 13` gateway-type namespace | documented/historical gateway-type evidence |
| diagnostic `WHO 1013 DIMENSION 1.OBJECT_MODEL` | MyHOME_Suite diagnostic identity namespace | catalogue-facing item/model value in the resolved system context |

Never copy a value from one column into the other. Equal numbers are not evidence that the namespaces are identical.

The observed MH202/F454 pair makes this distinction concrete: both return functional model code `200`, while their diagnostic `OBJECT_MODEL` values differ as `5` and `51`.

## 4. Establish the Integration Functions catalogue context

When the databases are separate files, attach them explicitly so that every identifier remains source-qualified:

```sql
ATTACH DATABASE 'OPEN.db' AS open_ref;
ATTACH DATABASE 'MHCatalogue.db' AS catalogue;
```

Confirm the implementation diagnostic-family association by meaning rather than by copying an internal database ID:

```sql
SELECT
    id_system,
    name,
    who,
    diag_who,
    managed
FROM open_ref.EN_SYSTEM
WHERE who = 13
  AND diag_who = 1013;
```

`OPEN.db.EN_SYSTEM.id_system` is an implementation-registry key. It is not the `MHCatalogue.db` catalogue-system key.

For this workflow, the established catalogue context is Integration Functions in `MHCatalogue.db`, `id_system = 26`. Verify that source record directly:

```sql
SELECT
    id_system,
    name,
    sys_modobj
FROM catalogue.EN_SYSTEM
WHERE id_system = 26;
```

The use of catalogue `id_system = 26` is database-defined context for Integration Functions. It is not derived from numeric equality with functional `WHO 13`, diagnostic `WHO 1013`, or an `OPEN.db` system ID.

## 5. Resolve the catalogue candidates

Bind the three identity fields used for catalogue resolution:

```text
:object_model = DIMENSION 1.OBJECT_MODEL
:brand        = DIMENSION 1.BRAND
:line         = DIMENSION 1.LINE
```

Then resolve the shared item and all matching Device records:

```sql
SELECT
    ais.id_system,
    ais.modobj AS object_model,
    i.id_item,
    i.descr AS item_description,
    d.id_device,
    d.code AS sku,
    d.name AS device_description,
    d.is_gateway,
    b.brand_name,
    b.brand_modobj,
    l.line_name,
    l.line_modobj
FROM catalogue.AS_ITEM_SYSTEM AS ais
JOIN catalogue.EN_ITEM AS i
  ON i.id_item = ais.id_item
JOIN catalogue.EN_DEVICE AS d
  ON d.id_item = i.id_item
JOIN catalogue.EN_BRAND AS b
  ON b.id_brand = d.id_brand
JOIN catalogue.EN_LINE AS l
  ON l.id_line = d.id_line
WHERE ais.id_system = 26
  AND ais.modobj = :object_model
  AND b.brand_modobj = :brand
  AND l.line_modobj = :line
ORDER BY d.name, d.code, d.id_device;
```

`AS_ITEM_SYSTEM.id_item -> EN_ITEM.id_item`, `EN_DEVICE.id_item -> EN_ITEM.id_item`, and the Device-to-brand/line joins are catalogue relationships reconstructed from the canonical data rather than wire identifiers. The mappings from the three diagnostic fields to `modobj`, `brand_modobj`, and `line_modobj` are semantic cross-source correlations; they are not declared cross-database foreign keys.

Do not select the first row when several Device records survive. Several marketed SKUs can share one item and identity tuple. Preserve the complete candidate set and classify the identity accordingly.

If the full query returns no row, diagnose the failure in stages instead of weakening the conditions silently. First check the item/model path:

```sql
SELECT
    ais.id_item,
    ais.modobj,
    i.descr AS item_description
FROM catalogue.AS_ITEM_SYSTEM AS ais
JOIN catalogue.EN_ITEM AS i
  ON i.id_item = ais.id_item
WHERE ais.id_system = 26
  AND ais.modobj = :object_model;
```

Then inspect the reported brand and line independently:

```sql
SELECT id_brand, brand_name, brand_modobj
FROM catalogue.EN_BRAND
WHERE brand_modobj = :brand;

SELECT id_line, line_name, line_modobj
FROM catalogue.EN_LINE
WHERE line_modobj = :line;
```

A missing catalogue match means that the current database revision did not resolve the captured tuple. It does not authorize substituting `DIMENSION 15`, dropping brand/line constraints without explanation, or inventing a later product record.

## 6. Classify the result

Use independent status for acquisition and catalogue resolution:

| Condition | Identity status | Presentation |
| --- | --- | --- |
| one matching `EN_DEVICE` row | unique in the inspected catalogue revision | show `EN_DEVICE.name`, SKU, brand, and line, with the raw protocol tuple |
| several matching `EN_DEVICE` rows | shared or ambiguous | show every candidate; do not choose by ordering |
| item/model resolves but brand or line does not | partially resolved | show the shared item and unresolved selector values |
| no Integration Functions item matches `OBJECT_MODEL` | unresolved | preserve the raw tuple and database revision |
| `WHO 1013 DIMENSION 1` was not obtained | unresolved acquisition | retain `WHO 13 DIMENSION 15` as evidence but do not promote it to a catalogue identity |

Use `EN_DEVICE.name` as the standard MyHOME_Suite-facing Physical Device description and `EN_DEVICE.code` as the product code/SKU. `EN_ITEM.descr` describes the shared capability item and must not replace the marketed Device identity.

## 7. Worked case: MH202

The observed MH202 capture contains:

```text
Client -> Gateway: *#13**15##
Gateway -> Client: *#13**15*200##

Client -> Gateway: *#1013**1##
Gateway -> Client: *#1013**1*5*15*5*0##
```

Parse the diagnostic tuple as:

```text
OBJECT_MODEL = 5
N_CONF       = 15
BRAND        = 5
LINE         = 0
```

Run the catalogue query with `id_system = 26`, `object_model = 5`, `brand = 5`, and `line = 0`. The resulting `EN_DEVICE` record or records are the catalogue evidence to present for the MH202 capture. Retain the capture's known MH202 identity as observation provenance; do not use that label in place of the database lookup when implementing the procedure.

The important derived result is that functional `DIMENSION 15 = 200` did not establish MH202 on its own. The diagnostic `OBJECT_MODEL = 5` supplies the discriminating catalogue-facing value.

## 8. Worked case: F454

The observed F454 capture contains:

```text
Client -> Gateway: *#13**15##
Gateway -> Client: *#13**15*200##

Client -> Gateway: *#1013**1##
Gateway -> Client: *#1013**1*51*15*5*0##
```

Parse the diagnostic tuple as:

```text
OBJECT_MODEL = 51
N_CONF       = 15
BRAND        = 5
LINE         = 0
```

Run the same catalogue query with `id_system = 26`, `object_model = 51`, `brand = 5`, and `line = 0`. The resulting `EN_DEVICE` record or records are the catalogue evidence to present for the F454 capture.

Again, `WHO 13 DIMENSION 15 = 200` is identical to the MH202 observation. The diagnostic `OBJECT_MODEL` differs, so the catalogue-resolution stage can distinguish the two observed cases without assigning new semantics to the functional model code.

## Reference algorithm

```text
function identify_gateway(capture_or_session, catalogue_revision):
    dim15 = obtain_or_find_response(
        request = "*#13**15##",
        response = "*#13**15*[MODEL]##"
    )

    retain dim15 raw frame and acquisition status

    dim1 = obtain_or_find_response(
        request = "*#1013**1##",
        response = "*#1013**1*[OBJECT_MODEL]*[N_CONF]*[BRAND]*[LINE]##"
    )

    if dim1 is not obtained:
        return {
            WHO13_model = dim15.MODEL if present,
            catalogue_identity = unresolved,
            reason = exact acquisition outcome,
            no inferred compatibility claim
        }

    retain dim1 raw tuple exactly

    system = require catalogue.EN_SYSTEM.id_system == 26
    candidates = query catalogue where
        AS_ITEM_SYSTEM.id_system == 26 and
        AS_ITEM_SYSTEM.modobj == dim1.OBJECT_MODEL and
        EN_BRAND.brand_modobj == dim1.BRAND and
        EN_LINE.line_modobj == dim1.LINE

    if candidates is empty:
        resolve item/model, brand, and line separately
        return unresolved or partially resolved with provenance

    if candidates has more than one Device:
        return every candidate with status shared_or_ambiguous

    return the single Device with raw frames,
           catalogue revision,
           WHO13 model kept in its own namespace,
           DIMENSION 1 tuple,
           and status unique_in_catalogue_revision
```

Do not add firmware, kernel, distribution, hardware, or microcontroller versions to the primary key used by this algorithm unless an explicit, source-backed catalogue correlation is established for the specific field. Those values can still be valuable supplementary evidence and should be retained separately when present.

## Expected result

```text
Gateway identification
  WHO 13 DIMENSION 15:
    MODEL: <raw value>
    status: documented/observed gateway-type evidence
  Diagnostic identity:
    WHO: 1013
    OBJECT_MODEL: <raw value>
    N_CONF: <raw value, retained separately>
    BRAND: <raw value>
    LINE: <raw value>
  Catalogue context:
    system: Integration Functions
    MHCatalogue id_system: 26
    database revision: <source revision>
  Catalogue candidates:
    - SKU: <EN_DEVICE.code>
      Device: <EN_DEVICE.name>
      brand: <EN_BRAND.brand_name>
      line: <EN_LINE.line_name>
  identity status: unique | shared/ambiguous | partially resolved | unresolved
  acquisition status: complete | timeout | rejected | transport failure
  provenance:
    - raw WHO 13 frame
    - raw WHO 1013 frame or exact absence outcome
    - exact catalogue query and database revision
```

## Evidence limits

- The two worked captures establish successful `WHO 1013 DIMENSION 1` identity responses for the observed MH202 and F454 cases. They do not establish a universal support matrix for every gateway model or firmware revision.
- The ordinary addressed `DIMENSION 1.N_CONF` physical-configurator interpretation is not required to identify these gateway cases and is not generalized to the gateway variant here.
- `WHO 13 DIMENSION 15` and diagnostic `WHO 1013 DIMENSION 1.OBJECT_MODEL` remain independent identifier namespaces. Historical numeric coincidences do not create a mapping.
- A catalogue result is relative to the inspected `MHCatalogue.db` revision. A missing later product in that revision is a database-coverage limit, not proof that the product or protocol behavior does not exist.
- Supplementary software or hardware version fields can corroborate an identity only where their relationship to a catalogue candidate is separately established.

See [`WHO 13 DIMENSION 15`](../functional/who-13-integration-gateway/dimensions.md#dimension-15---device-type), [`DIMENSION 1`: Device Identity](../diagnostics/dim1-device-identity.md), [Physical Devices](../device-model/physical-devices.md), [Sources and Identifier Boundaries](../device-model/sources-and-identifiers.md), and [Catalogue Resolution](../internals/catalogue-resolution.md).
