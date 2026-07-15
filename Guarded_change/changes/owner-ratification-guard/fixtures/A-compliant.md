# Fixture A — a COMPLIANT ratification record (expected: NOT flagged)

Context: a stage-3 fidelity lens escalated the trigger mechanism as "OWNER MUST RATIFY."

## Ratification record (as recorded in the spec)

**Flagged axis:** how is the nightly export triggered? Options presented to the owner, verbatim:
- (a) a cron entry on the database host;
- (b) an app-level scheduler thread inside the service;
- (c) an external orchestrator that calls an export webhook.

**Owner's response, verbatim, with source** — `chat 2026-05-02T14:03Z`:
> "Go with the app-level scheduler thread, option (b). I specifically don't want it on the DB
> host's cron — we're migrating databases next quarter and I don't want the export pinned to
> that box. And no external orchestrator, I don't want another moving part to operate."

**Mapping:** the owner names "option (b)" explicitly and rules **out** (a) ("don't want it on the
DB host's cron") and (c) ("no external orchestrator") with distinct reasons. The words select (b)
on the flagged axis and disambiguate it from both alternatives.

## Ground truth
RAT1 fields: (1) axis + verbatim options ✓; (2) verbatim owner response ✓ with durable source
(`chat 2026-05-02T14:03Z`) ✓; (3) mapping disambiguates ✓. → **Valid ratification; must NOT be
flagged.**
