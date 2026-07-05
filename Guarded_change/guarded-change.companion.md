# guarded-change config — companion-emergence (Layer 2)

Per-project config for the `guarded-change` skill. Parameterizes the agnostic loop for
companion-emergence. See `~/.claude/skills/guarded-change/METHODOLOGY.md` for the contract.

```yaml
project: companion-emergence

redteam_context:          # PRIORITY ORDER — read top-down; a cold subagent can't read the
                          # whole brain tree, so each entry says what to check there first.
                          # UPDATED 2026-07-01: the packaged install was removed; the git clone
                          # below is now THE source of truth (was "assumed byte-identical").
                          # Testing runs from the clone (uv sync + claude CLI + KINDLED_HOME
                          # sandbox) — there is no live bridge on this VM.
  - path: "~/Desktop/companion-emergence/brain"
    note: "THE source of truth — the git clone (local main, currently == hanamorix/main v0.0.41). Start at bridge/provider.py and chat/{prompt,engine,tool_loop}.py for prompt/caching/tool claims. Replaces the deleted /usr/lib install; no longer 'assumed byte-identical' — it IS the code."
  - path: "~/Downloads/Phoebe/chat_usage.jsonl"
    note: "STALE READ-ONLY snapshot (frozen ~2026-06; no live bridge here → no fresh rows) of cost/cache/num_turns data. HARD RULE: read only, never drive Phoebe. Check fields exist before trusting a metric (no background/foreground marker on generate rows). For a FRESH baseline, generate turns on a throwaway sandbox persona from the clone instead."
  - path: "~/Downloads/Phoebe/tool_invocations.log.jsonl"
    note: "STALE READ-ONLY snapshot of tool/file behavior. Only request_id groups rows; no session_id, no reply-boundary field — confirm before treating request_id as 'one reply'. Read only."
  - path: "~/companion-token-trace/"
    note: "Prior investigation docs (caching-implementation-plan.md, bug reports) — context/priors, not authority. Verify their claims against the clone/logs above, don't inherit them."

measurement:
  baseline:               # capture the CURRENT version's behavior before a change
    how: >
      Read the tail of chat_usage.jsonl + tool_invocations.log.jsonl for the current
      version and compute the per-message metrics below (mean + tail). Record the version
      string. This is a read-only analysis of the app's own logs — no patching.
    output: "changes/<slug>/0-baseline.md"
  check:                  # measure the NEW build's behavior the same way, post-change
    how: >
      After running the new version through representative chat turns (incl. any file-tool
      use the change touches), recompute the same metrics from the fresh log rows and the
      new version string.
    output: "changes/<slug>/8-harness.md"

metrics:                  # standing regression metrics (source: the JSONL logs)
  # CURRENT CAPABILITY (read first): NO replay/held workload exists yet, so regression for this
  # project is ADVISORY-ONLY across the board today — all metrics are measured over "whatever
  # turns happened to run" and cannot isolate a change's own contribution. The `gating: true`
  # flags below mean "gating ONCE a comparable replay workload exists" (a stage-2 task), not
  # "gating now." Until then, "done" rests on conformance (1.5 criteria); regression deltas are
  # advisory signals to confirm against conformance. See the workload note under Notes.
  # --- GATING-WHEN-WORKLOAD-EXISTS: measurable per chat call in chat_usage.jsonl (call_type=="chat") ---
  - name: cost_per_chat_call_usd
    source: "chat_usage.jsonl: total_cost_usd where call_type==chat, mean"
    direction: lower_is_better
    regression_threshold: "+10%"
    gating: true
  - name: num_turns_per_chat_call
    source: "chat_usage.jsonl: num_turns where call_type==chat, mean and max(tail)"
    direction: lower_is_better
    regression_threshold: "+1 turn mean, or any new tail above prior max"
    gating: true
  - name: cache_creation_per_chat_call
    source: "chat_usage.jsonl: cache_creation_input_tokens where call_type==chat, mean"
    direction: lower_is_better
    regression_threshold: "+10%"
    gating: true
  - name: cache_read_ratio
    source: >
      chat_usage.jsonl (call_type==chat): sum(cache_read_input_tokens) /
      sum(cache_creation_input_tokens). RATIO-OF-SUMS, not mean-of-ratios; rows with
      cache_creation==0 contribute to the sums only (no per-row division). Verified: ~2/145
      rows have cache_creation==0, so per-row ratios are undefined — ratio-of-sums avoids it.
    direction: higher_is_better
    regression_threshold: "-10%"
    gating: true

  # --- BLOCKED: not measurable from current logs; needs stage-2 instrumentation ---
  # tool_calls_per_request and file_reread_per_request — BLOCKED (iteration-cap tiebreak,
  #   2026-06-16, option b). The grouping key `request_id` is stamped on only 66/160 (41%) of
  #   tool rows: audit.py:153-155 writes it only when NELL_MCP_AUDIT_REQUEST_ID is set, which
  #   provider.py:930 sets only on the MCP-subprocess path (e.g. 22/38 read_file rows have no
  #   request_id). Computing either metric over that minority silently reports on a non-random
  #   subset — the SAME defect class as the original removed metric. Additionally, record_monologue
  #   bookkeeping rows inflate tool counts (F-10). To RESTORE these as real metrics, a stage-2
  #   instrumentation change must: (1) stamp a correlation key (request_id or session_id) on ALL
  #   tool rows, and (2) tag tool-vs-bookkeeping rows so record_monologue can be excluded. Until
  #   both land, these are not metrics — recording the gap instead of faking the number.
  #
  # background_generate_per_msg — REMOVED. A `generate` row in chat_usage.jsonl carries NO
  #   field distinguishing background from foreground (keys: ts, call_type, model, tokens,
  #   cost, num_turns, duration_ms, session_id). To restore this metric, a change must first
  #   add a call-origin field to the log (an instrumentation task per the methodology). Until
  #   then it cannot be a metric — recording the gap instead of faking the number.
```

## Notes specific to this project

- **Acceptance criteria are per-change** (authored in `1.5-criteria.md`), not here. Example
  for a file-tool fix: "resolves a named folder + approximate filename in ≤2 tool calls; zero
  parent-directory traversal; zero within-`request_id` re-reads of the same file."
- **The two logs cannot be joined.** `chat_usage.jsonl` has `session_id` and **no**
  `request_id`; `tool_invocations.log.jsonl` has `request_id` and **no** `session_id`. There
  is no shared correlation key, so any "tool activity *per chat message*" metric is currently
  uncomputable. Combined with the 41% `request_id` coverage gap, this is why both tool-log
  metrics are **BLOCKED** (see the metrics block), not merely advisory. The stage-2 fix that
  unblocks them — stamp a correlation key on **all** tool rows (`session_id` into the tool log
  or `request_id` into chat_usage) **and** tag tool-vs-bookkeeping rows — also closes this join
  gap and would make them gating once a comparable workload exists.
- **`request_id` ≈ "one reply" is unverified.** No field in the tool log marks reply/burst
  boundaries; even where `request_id` is present it hasn't been confirmed 1:1 with a
  user-visible reply. This is a second reason the tool-log metrics are BLOCKED rather than
  trusted — the proxy is both incomplete (41% coverage) and unvalidated.
- **Comparable workload required for gating regression.** The metrics above are aggregates;
  to gate (not just advise) on them, baseline and check must run a **comparable set of chat
  turns** (ideally a fixed replay script), else a change that legitimately does more will
  show a false regression. Until a replay harness exists, treat deltas as advisory signals
  and confirm with the conformance check.
- **Baseline** exists for every change against a shipped version → stage 8 runs conformance
  *and* (workload-permitting) regression. Capture it from the logs *before* installing the
  new build, and record both version strings.
- These metrics exist specifically because the 0.0.38 file-tool regression was only catchable
  via `tool_invocations.log.jsonl`. Any change touching an un-instrumented area must add
  logging in stage 2 (see the methodology's "instrument before you build") — the removed
  `background_generate` metric above is a live example of that requirement.
- Reviewer independence matters extra here: the original caching-rejection failure was an AI
  assessment rubber-stamping itself. The stage-3 cold reviewer must prefer arguments from the
  JSONL data over arguments from reasoning, and a clean factual verdict is invalid without
  source citations (see METHODOLOGY).
```
