# Fixture B — a LEGITIMATE elaboration (expected: NOT flagged as inflation)

Builds on the ratified option (b) from Fixture A: "an app-level scheduler thread inside the
service."

## Elaboration (as expanded in the spec)

> The app-level scheduler is a **single daemon thread started at service boot** that fires the
> export job on a **fixed interval**, reading the same config the service already loads. It runs
> in-process, so it stops when the service stops.

## Ground truth
The elaboration's operative terms — *single thread*, *at boot*, *in-process*, *fixed interval* —
are all **entailed by** "an app-level scheduler thread inside the service" (a scheduler thread in
the service is in-process, starts with the service, and schedules on an interval). It introduces
**no** new division of responsibility, no "only/every/never" commitment the ratified phrase did
not already imply, and no new mechanism. → **No unratified inflation; must NOT be flagged by
RAT2.**

(Contrast the incident: "harness owns ONLY loop mechanics / AgentBob owns ONLY his words" added a
division of responsibility the ratified phrase never entailed — that IS inflation. This fixture
deliberately does not.)
