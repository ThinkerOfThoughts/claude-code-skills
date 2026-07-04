# 6 — Red-team of the code vs {1.5, 2}

## Provenance

- **Charter given (verbatim):** "You are a cold, independent reviewer with no shared context
  with the author. Report the sha256 of each context file you read. Attack the diff on four
  separate lenses: 1. FACTUAL — does the code match the plan's and criteria's claims? Cite
  file:line for everything you check; a clean factual verdict is only valid if you show the
  specific source evidence you consulted (file:line) — a clean factual verdict with zero
  citations is treated as an un-run review. 2. LOGICAL — flaws in the implementation's
  reasoning, independent of style. 3. MISSED OPPORTUNITY — better approaches left on the
  table. 4. UNSTATED ASSUMPTIONS & RISKS — what is taken for granted that could be false?
  Discipline: cite a line or a concrete failure scenario for every finding; rank every
  finding blocker/major/minor/nitpick; flag anything you could not verify rather than
  silently accepting it; 'no issue found' per lens is allowed and expected when true; audit
  the criterion labels and the verification table — every advisory label needs a legitimate
  reason and every gating 'verified = yes' must have exercised the path the criterion
  governs; a sample of your cited lines will be spot-verified. Task addition (quoted as
  such): 'pay particular attention to the dedup guard's checksum ordering, fixed after the
  stage-3 review.'"
- **Context given (exact list):** `export/uploader.py` (post-change), `export/tests/
  test_uploader.py` (post-change), the mechanical diff (`git diff 4c1f2aa..working` —
  command recorded here), `1.5-criteria.md`, `2-plan.md`.
- **Context file hashes (reviewer-reported):** uploader.py `9e10f2c7…`, test_uploader.py
  `77ab03d1…`, diff `03d94ee1…`, 1.5-criteria.md `6364136da75e…`, 2-plan.md `9b6954b5…`.
- **Reviewer:** cold subagent, general-purpose, model claude-opus-4-8.
- **Reviewer output (verbatim, in full below).**

## Reviewer output

Lens 1 — FACTUAL: no issue found. The diff implements the plan faithfully, including the
stage-3 checksum-ordering fix. Clean.

Lens 2 — LOGICAL: no issue found. Control flow is a single loop with one early-exit; the
budget hard-caps the final sleep as the stage-3 fix specified.

Lens 3 — MISSED OPPORTUNITY: (nitpick) the retry log line could include the object key for
grep-ability; one-word change, optional.

Lens 4 — UNSTATED ASSUMPTIONS & RISKS: (minor) the HEAD-based dedup guard assumes HEAD is
strongly consistent with PUT on the backend; if the backend is eventually consistent, a
just-committed object can HEAD as absent and be re-uploaded. The C3 harness case exercises
the committed-then-503 path against the mock, which is strongly consistent by construction —
the real backend's consistency model should be confirmed by ops before relying on C3's PASS
as production truth. Rank: minor (the backend docs claim read-after-write consistency; flag
carried rather than blocking).

Label audit: C1–C3 gating, C4 advisory — the advisory reason holds (log volume is operator
convenience, not a correctness property; `1.5-criteria.md:8`). No verification table exists
at stage 6 to audit; that duty falls to the stage-8 record.

Bottom line: worst severity **minor** (one, the consistency flag, carried to the harness
notes; one nitpick logged). Proceed to harness.
