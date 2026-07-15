# Fixture B — a LEGITIMATE elaboration (expected: NOT flagged as inflation)

Builds on the ratified option (b) from Fixture A: "an app-level scheduler thread inside the
service."

## Elaboration (as expanded in the spec)

> The app-level scheduler is a **single daemon thread started at service boot** that fires the
> export job on a **fixed interval**, reading the same config the service already loads. It runs
> in-process, so it stops when the service stops.

