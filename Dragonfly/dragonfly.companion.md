# dragonfly config — companion-emergence (Layer 2)

Per-project config for the `dragonfly` skill. Parameterizes the agnostic diagnosis loop for
companion-emergence. See `~/.claude/skills/dragonfly/METHODOLOGY.md` for the contract.

```yaml
project: companion-emergence

redteam_context:          # PRIORITY ORDER — read top-down; a cold subagent can't read the whole
                          # tree, so each entry says what to check there first.
  - path: "/usr/lib/Companion Emergence/python-runtime/lib/python3.13/site-packages/brain"
    note: "The REAL running code (bundled runtime) — authority for any behavior claim. Start at bridge/provider.py and chat/{prompt,engine,tool_loop}.py. A diagnostic that cites a name/call must match THIS code, not the repo checkout."
  - path: "~/.local/share/companion-emergence/personas/<persona>/chat_usage.jsonl"
    note: "Ground truth for cost/cache/num_turns symptoms. Confirm a field EXISTS before a hypothesis or test relies on it (e.g. there is NO background/foreground marker on generate rows)."
  - path: "~/.local/share/companion-emergence/personas/<persona>/tool_invocations.log.jsonl"
    note: "Ground truth for tool/file behavior. Only request_id groups rows (stamped ~41% of the time); no session_id, no reply-boundary field — confirm before treating request_id as 'one reply'."
  - path: "~/Desktop/companion-emergence/brain"
    note: "Repo checkout — ASSUMED identical to the bundled runtime but NOT verified. Prefer the bundled path above for any behavior claim; use this for history/blame."
  - path: "~/companion-token-trace/"
    note: "Prior investigation docs — context/priors, NOT authority. Verify their claims against the code/logs above; do not inherit them."

reproduction:             # how to exercise the suspect behavior in this project
  how: >
    Run the app / a real chat turn against the bundled runtime and exercise the path the symptom
    names (e.g. a chat call, a file-tool use, a resume). Prefer the smallest turn that still
    produces the symptom. NOTE: reproductions that drive a real chat turn CONSUME TOKENS — by the
    triage's highest-priority rule they are full-guarded-change artifacts, not lite.
  logs: >
    The persona's own JSONL telemetry under ~/.local/share/companion-emergence/personas/<persona>/
    (chat_usage.jsonl, tool_invocations.log.jsonl) is the ground truth for observations — read the
    fresh tail after a repro run rather than reasoning about what "should" have been logged.

ledgers:
  dir: "hunts/<slug>/"     # symptom-ledger.md + observation-ledger.md live here; must survive a
                           # session restart (the cold-start guard recommends restarting).

iteration_cap:
  N: 3                     # convergence-gate cap; matches the Layer-1 default. Raise only with a
                           # recorded reason if a genuinely multi-layer bug needs more cycles.
```

## Notes specific to this project

- **⛔ Never use Phoebe's persona as a test fixture.** Reproductions and discriminating tests must
  use a throwaway/dev persona, not Phoebe. Reading Phoebe's *files/logs* as ground truth is fine;
  *running the hunt's tests through her persona* is not. (Project hard rule.)
- **Cite the bundled runtime, not the repo.** Confabulated variable names / misplaced calls were a
  motivating failure. The stage-1/4/7 cold reviewer must verify every cited identifier against
  `/usr/lib/Companion Emergence/.../brain`, because the repo checkout is only *assumed* identical.
- **Token-consuming repros are full-guarded-change.** Any repro/test that drives a real chat turn
  (the common case here) hits triage rule #1 → full guarded-change, regardless of how short the
  script is. Three of the six useless tests in the motivating session were exactly this kind.
- **Read the fresh log tail, don't infer.** An observation about cost/cache/tool behavior is only
  trustworthy if it cites a real row written by the repro run — not a prediction of what the code
  "should" log. Confirm fields exist (several expected ones do not).
- **The two logs cannot be joined** (chat_usage has session_id+no request_id; tool log has
  request_id+no session_id). Any "tool activity per chat message" observation is currently
  uncomputable from the logs alone — flag it rather than fabricating a correlation.
