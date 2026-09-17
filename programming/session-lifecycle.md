# Programming Session Lifecycle

A programming operation must be interpreted as a stateful exchange rather than a collection of unrelated writes.

## Planned coverage

- entry into programming mode;
- target selection;
- Object and configuration transfer;
- acknowledgement and rejection;
- commit or finalization;
- normal termination;
- explicit abort;
- timeout and transport interruption;
- recovery after an incomplete operation.

## Completion states

The reference will distinguish:

| State | Meaning |
| --- | --- |
| Completed | the protocol reached its established successful terminal state |
| Rejected | the Device returned a programming or parameter error |
| Aborted | a participant explicitly ended the operation |
| Timed out | the expected transition was not observed |
| Transport lost | completion cannot be established |
| Verified | a later diagnostic interview reports the intended effective state |

An `ACK` during the session is not by itself proof of verified installed state.
