# CEN Events

`WHO 15` carries CEN button events. The event identifies the CEN command/button together with the event phase encoded by the parameterized `WHAT` form.

Known CEN button identifiers occupy the range `00` through `31`. Event parameters distinguish button interaction phases including initial activation, short release, extended release, and extended activation.

CEN+ is a distinct protocol family carried under [`WHO 25`](../who-25-transversal/cen-plus.md); CEN and CEN+ should not be collapsed into one `WHAT` table merely because they represent related user-command functions.