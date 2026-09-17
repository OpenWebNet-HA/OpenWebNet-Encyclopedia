# Object Programming

Object programming selects the logical function exposed by a configurable Module.

## Resolution model

The procedure will distinguish:

- internal slot carried by the protocol;
- current configured Object;
- current Virgin Object when the Module is unconfigured;
- Objects permitted by the Virgin Object;
- firmware and slot constraints;
- fixed Objects that cannot be replaced.

## Planned procedure

1. Resolve the Physical Device and firmware.
2. Resolve the internal slot.
3. Resolve the current Object or Virgin Object from diagnostic state.
4. Determine the permitted target Objects from catalogue associations.
5. Apply firmware, slot, and condition constraints.
6. Encode and transmit the Object-selection operation.
7. Interpret Object-specific errors.
8. Verify the resulting `DIMENSION 30` state.

Object numbers and internal catalogue identifiers must not be interchanged.
