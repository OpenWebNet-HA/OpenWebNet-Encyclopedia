# MyHOMEServer1 3.87.13 Catalogue Ownership and Scene Factories

Catalogue queries and scene factories resolve different identities in [MyHOMEServer1 Firmware 3.87.13](myhomeserver1-3.87.13.md). A catalogue factory supplies owner-specific query parameters; scene factories turn exact JSON type strings into raw objects and compiled runners. Their local keys are not public WHO values or a product-support list.

## Evidence and product scope

The [catalogue and scene consumers](myhomeserver1-3.87.13-consumers.md) identify the opening and parsed-file boundaries. The [factory evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-factories/README.md) preserves the corresponding constructors, tables, vtables and callers. The complete catalogue data comparison remains canonical under [source profiles](../../internals/mhcatalogue-source-profiles.md).

## Catalogue reader: SQL and concrete owner

The selected reader belongs to class `kobj_value_139`. Its factory constructs a shared-owned wrapper, places the inner object at allocation offset `12`, and passes local key `139` to its base constructor. That constructor copies a `15`-column `EN_CONF` query template and substitutes `$modobj$`, `$line_modobj$`, `$brand_modobj$` and `$key_object$` from its own fields.

The registered initializer constructs both the query template and the selected factory registry. An application walker looks up current keys there and can invoke the `139` entry with context-derived model, line and brand arguments. Actual key-list production, supplied values, registry mutation and live activation remain unresolved.

| Zero-based SQL column | Selected expression | Reader destination |
| ---: | --- | --- |
| `13` | `EN_KEY_OBJECT.slots` | Inner object `+20`, wrapper `+32` |
| `14` | `AS_OBJECT_SYSTEM.id_system` | Inner object `+24`, wrapper `+36` |

The selected reader converts these text results through base-10 `strtol`; later rows can overwrite earlier values. This is not proof of query success, row uniqueness, ordering, later use or complete Firmware eligibility. The independent two-column `AS_ITEM_SYSTEM.main=1` query is a different declaration. [Catalogue ownership evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-factories/catalogue-report.txt) records the full SQL, aliases and substitutions.

## Concrete scene-action schema

Trigger, condition and action factories compare each element's exact `type` against their own tables. Table membership need not lead to construction: the action factory's selected `TIME` entry advances its iterator rather than constructing an action.

| Action type | Local action index | Derived JSON value | Common raw fields |
| --- | ---: | --- | --- |
| `SLEEP` | `10` | `seconds`, converted with `asUInt` | String `id`, local `type`, unsigned `delay` and `duration` |
| `SCENARIO` | `11` | `sceneId`, converted with `asUInt` | Same common fields |

Each selected raw object is `44` bytes and is transferred into the scene's action storage. Its raw class is separate from the compiled action object, which has operational fields and callables. Field names and unsigned conversion do not establish valid input ranges, elapsed timing or target-scene success. [Schema and factory evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-factories/factories-report.txt) retains exact construction and normal-capacity transfer paths; reallocation and exceptional ownership require separate analysis.

## Enabled gate, compiled actions and stop requests

Runner initialization serializes and reparses raw elements before compiling them. The [compiled-action reference](myhomeserver1-3.87.13-actions.md) follows the selected action fields through that boundary.

Two launch functions require scene-enabled to be nonzero. Their selected nonactive paths set the scene-active byte, clear the scene-stop byte, request a thread state containing the runner, start the thread and detach it. One worker evaluates condition predicates before the action worker; the other enters that action worker directly. Successful thread creation and scheduling remain unobserved.

The action worker invokes each compiled action's primary execution method, then tests scene-stop after the call returns. Scene stop sets its own byte and invokes each action's separate stop method. Consequently, a stop request does not establish interruption of a callback already running. [Cancellation](myhomeserver1-3.87.13-cancellation.md) distinguishes these scene bytes from individual completion and the shared action-wait flag.

Trigger and action handles contain pointer/control pairs; conditions use a separate pointer range. Their ownership and teardown are described under [serialization and ownership](myhomeserver1-3.87.13-serialization.md). Memory barriers in selected methods do not alone establish locking or race freedom.

## Evidence limits

These constructions and branch relations are static implementation evidence. Root catalogue-selection policy, configured scene admission, valid live objects, providers, exceptions/unwind and concurrent lifetime remain unresolved. No complete scene execution or physical command outcome is established by a factory entry or launch request.
