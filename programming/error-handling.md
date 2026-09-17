# Programming Error Handling

Programming failures must preserve the operation, target Device, internal slot, Object, property, attempted value, and active session state.

## Planned coverage

- ordinary `NACK`;
- Object-selection errors;
- address errors;
- configuration-parameter errors;
- unsupported operations;
- busy state;
- invalid sequence transitions;
- timeout;
- abort;
- transport interruption;
- safe retry and recovery.

A missing response is not equivalent to a negative acknowledgement. A protocol error also does not by itself identify which catalogue constraint was violated unless the frame carries that distinction.
