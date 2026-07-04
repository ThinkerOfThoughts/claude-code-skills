# 3 — Red-team of {1-spec, 1.5-criteria, 2-plan}

A cold review of the plan was run and returned the following findings.

## Findings

- **(minor, factual)** The plan's dedup guard HEADs the object key "with matching checksum,"
  but `uploader.py:88` computes the checksum only *after* a successful PUT returns — on the
  succeeded-server-side path the local checksum variable is unset at HEAD time. The guard as
  planned would compare against `None`. Fix: compute the checksum before the first attempt
  (it's needed for the PUT header anyway, `uploader.py:74`).
- **(minor, logical)** The 90 s budget and the 3-retry schedule are stated independently, but
  worst case 1+2+4 s of sleep + 3 × 25 s timeouts (`uploader.py:31`, `TIMEOUT = 25`) = 82 s —
  one more network stall and the budget is silently blown. State which bound wins (suggest:
  the budget hard-caps, cutting the last retry short).
- **(nitpick)** Jitter "±20%" should say it applies per-delay, not to the total.

## Lens verdicts

- **Factual:** the two claims checked against source both cited above (`uploader.py:31, 74,
  88`); the mock-endpoint measurement approach matches how `test_uploader.py:12-40` already
  drives the mock. No further factual issues.
- **Logical:** one finding above; sequencing otherwise sound (dedup guard before retry is the
  right order for the no-idempotency-key constraint).
- **Missed opportunity:** none found — `Retry-After` header support was considered and is out
  of scope by the spec's no-new-dependencies constraint (it needs date parsing edge cases).
- **Unstated assumptions & risks:** the mock's 503-503-200 script assumes the backend never
  returns 503 with a committed write except in the C3 scenario; the C3 test covers exactly
  that case, so the assumption is tested, not taken.

## Criteria-coverage check

None found — C1–C4 observe the full blast radius of the change (retry behavior, schedule,
duplication, log volume); the change touches no other externally observable behavior.

## Bottom line

Worst severity: **minor** (two, fix in place). The plan is sound; proceed to build once the
checksum-ordering and budget-vs-schedule fixes are folded in.
