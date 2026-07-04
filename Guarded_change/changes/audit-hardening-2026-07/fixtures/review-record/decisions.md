# decisions.md — gate log (append-only)

- **Run start** | — | path validation recorded | All reviewer-handed paths checked: exist,
  readable (uploader.py, test_uploader.py, the two change docs). Stage-0 baseline recorded:
  nightly export aborts on first 5xx (three aborts last month, ops log 06-04/06-17/06-28).
- **Stage 4 gate** | minor | fix in place → build | Two minors (checksum ordering, budget-vs-
  schedule precedence) folded into the plan; nitpick (per-delay jitter wording) logged.
  Criteria frozen at route-to-build; sha256 recorded: `6364136da75e…`.
- **Stage 7 gate** | minor | fix in place → harness | Consistency flag carried to harness
  notes; log-line nitpick logged, optional.
- **Stage 8** | — | accept | Harness scripts cold-checked pre-run (`6b-harness-check.md`):
  representative, C1/C3 guarded cases fail against the pre-change uploader. Gating C1, C3
  PASS; C2 confirmed post-ship per harness; advisory C4 PASS. Shipped to the nightly export.
