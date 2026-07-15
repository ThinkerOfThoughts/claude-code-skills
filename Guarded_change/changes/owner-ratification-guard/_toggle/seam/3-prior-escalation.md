# 3 — Prior stage-3 finding (carried forward)

**FIDELITY (MAJOR).** The trigger-mechanism choice in the plan substitutes the author's preferred
in-service scheduler for a mechanism the owner has not confirmed. The three options on the table
(cron on the DB host / app-level scheduler thread / external orchestrator webhook) are a genuine
owner-intent decision, not a plan-internal call. **OWNER MUST RATIFY** — this must be an explicit
owner decision, not the author's pick.

(Routing: the plan may not proceed to build until this is resolved by the owner.)
