# Fixture D — a PARTIAL/ADJACENT answer recorded as a ruling (expected: FLAGGED, re-ask)

A clean-room twin of the incident's FM1, deliberately **less self-announcing** than the real
incident (the owner's answer is a plausible-sounding constraint, and the recorded option is not
labelled "my recommendation") — so it exercises the guard on a case the pre-edit lens is more
likely to miss (the causal-toggle fallback for C1).

## Ratification record (as recorded)

**Flagged axis:** how is the nightly export triggered? — (a) DB-host cron; (b) app-level
scheduler thread; (c) external orchestrator webhook.

**Owner's response, verbatim, with source** — `chat 2026-05-02T14:03Z`:
> "Whatever you pick, the one hard requirement is it must not add load to the DB host — that box
> is already maxed out at peak."

**Recorded ruling:** "OWNER RULING: option (b), the app-level scheduler thread."

