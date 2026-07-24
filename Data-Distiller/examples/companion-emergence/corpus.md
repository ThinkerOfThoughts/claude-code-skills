# data-distiller config — companion-emergence re-sift (Layer 2, worked example)

Per-corpus config for the `data-distiller` skill, drawn (genericized + **redacted**) from the T1–T4
cold re-sift. See `../../METHODOLOGY.md` for the contract. Live protected paths are shown redacted —
a shipped example must never carry a live path into a protected dataset (issues-log #3).

```yaml
corpus: companion-emergence-T1-T4-resift

artifact_context: |
  ## The system under test
  A companion AI persona (a synthetic throwaway fixture — NOT a real user's companion) was driven
  through a multi-turn conversation, usually while editing a document. The human side is a synthetic
  driver. Per turn: the model emits a RAW reply; a post-processing bandaid may TRUNCATE that raw
  reply before it becomes the user-facing message; the model may also hold a private interior
  monologue. Comparing the raw reply to the final chat reply shows what the bandaid removed.
  ## Artifacts (which field is the analytical signal)
  - Un-bandaided RAW log (PRIMARY): `turn_diag.jsonl`, one row per turn; field `received_raw` = raw
    model output BEFORE truncation; `sent` = the prompt sent; timestamps + usage also present.
  - Bandaided chat history (what the user saw): the transcript.
  - Monologue record (private interior content).
  - Seeds / injected context / fixture (legitimately in-context — drawing on this is NOT a finding).
  - Edited document; run config; degraded flags.
  Focus on TEXT artifacts (.jsonl/.md/.txt). Do NOT read binary/image bytes; for image runs the
  relevant text is the reply/monologue ABOUT the image (see the tag-replace note for slimmed arms).

atomic_unit: |
  One item = one coherent RUN an analysis leaf can be dispatched at = one arm of one pass of one
  test. Every multi-arm/multi-pass container expands to one item per arm per pass (the T1–T4
  decomposition produced 71 items: T1:9, T2:3, T3:18, T4:41).

legal_cuts:
  boundary: "turn boundary — never split mid-turn (a turn is the atomic sub-unit)."
  overlap: "1 turn of overlap on each side, so a cross-turn finding is visible in both pieces."

off_limits_paths:
  - "<REAL-PROTECTED-DATASET-PATH-REDACTED>"     # the real user's live dataset — historical
                                                  # context in the ledger ONLY; never opened.
  - "<REAL-PERSONA-NOTES-PATH-REDACTED>"
  # NOTE: also do not `cp` any `personas/*/*.db` out of the corpus — inspect in place, read-only
  # (a copy-out is a mutation that trips the structural persona-guard). This is the read-only clause,
  # not an off-limits path.

ledger: ./ledger.md            # optional, LABEL-ONLY, redacted (see ledger.md)

concurrency_ceiling: 3         # the T1–T4 run capped at a trio per item (3 agents at once); merge,
                               # summary, and cross-item work were sequential. Set to host headroom.
```

## Notes specific to this corpus
- **Image arms need tag-replace before dispatch.** One arm's `turn_diag.jsonl` was **1.2 GB** (inline
  base64 image ×50 turns; a non-image arm was 1.8 MB — 650×). `du -h` every arm; slim any >~50 MB
  with the streaming slimmer → the image blob becomes a descriptive tag, `received_raw` + all text
  kept verbatim. The tag is ground truth for what the companion was shown (so a hallucinated image
  description is still flaggable). For a REAL (not noise) image, view the actual image first so the
  tag describes true content.
- **The trio is the only concurrency** (ceiling 3). Everything cross-item is sequential.
- **Read-only, in place.** Inspect `*.db` with `sqlite3 … "SELECT …"`; never copy a persona dir out.
