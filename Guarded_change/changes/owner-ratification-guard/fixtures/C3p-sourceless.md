# Fixture C3p — a SOURCE-LESS reconstruction (expected: FLAGGED, missing provenance)

Same decision as Fixture A, but the "verbatim" owner words carry **no durable source** — they
were reconstructed from memory after a context compaction.

## Ratification record (as recorded)

**Flagged axis:** how is the nightly export triggered? — (a) DB-host cron; (b) app-level
scheduler thread; (c) external orchestrator webhook.

**Owner's response (reconstructed):**
> "The owner said to use the app-level scheduler thread, option (b), and not to put it on the DB
> host."
> _(recalled from an earlier conversation; the original message was not located after the
> session was compacted.)_

**Mapping:** the reconstruction names (b) and rules out (a); it reads as disambiguating.

## Ground truth
RAT1 fields: (1) axis + options ✓; (2) owner response present and disambiguating-*looking*, **but
no durable source — explicitly a post-compaction reconstruction, not spot-checkable** ✗; (3)
mapping present. → Because the quote is not spot-checkable against a source the author did not
author, it is **treated as unverified**; the record **must be FLAGGED** (missing provenance) and
the axis re-confirmed against the actual transcript or re-asked. This is the exact
"survives-the-author's-own-re-read" fabrication/reconstruction sub-mode.
