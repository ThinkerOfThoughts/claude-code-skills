# 2 — Plan: uploader-retry-backoff

Wrap `Uploader.put_object` in a retry loop: catch `HTTPError` with `status >= 500`, sleep
per the schedule (1/2/4 s, jitter ±20%), re-attempt up to 3 times, raise after the budget.
Before each retry, HEAD the object key; if present with matching checksum, treat as success
(dedup guard for the succeeded-server-side case).

**Stage-3 fold-ins:** the checksum is computed once, before the first attempt (it is needed
for the PUT header anyway), and the dedup HEAD compares against that stored value — never a
post-PUT recompute. The 90 s budget wins over the schedule: a sleep that would cross the
budget is hard-capped to the budget's remainder, cutting the last retry short.

**Measurement:** C1/C2 against a local mock endpoint scripted to return 503-503-200;
C3 against the mock scripted to return 503 *after* committing the object (the
succeeded-server-side case), asserting exactly one stored copy; C4 by line-count of the run log.

**Instrumentation:** add a `retry` log line (attempt #, delay, status) — needed for C2/C4.

**Thresholds:** any gating criterion failing at stage 8 → bounce per severity table; C4 is
advisory (surfaced, never bounces).
