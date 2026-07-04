# Decisions / gate log — monologue-bleed + memory-gap hunt

Append-only. Each entry: stage/gate | worst severity | route | rationale.

- **Setup** | — | Layer-2 config adaptation required | Repo config `dragonfly.companion.md` is
  Hana/macOS (paths under `~/Library/Application Support`, Nell persona). Invalid on this Linux box.
  Adapting redteam_context to: repo `brain/` (authority; can checkout `v0.0.40` per O3/O5),
  evidence `~/Downloads/Phoebe/` + `~/Desktop/Bugs.txt`. Iteration cap N=3 unchanged.
- **Scope** | — | one hunt, two symptoms (S1 monologue-bleed, S2 memory-gap) | User chose "one hunt,
  split later". Fixes may split into separate guarded-change PRs if root causes are unrelated.
- **Stage 0a** | — | partial confirmations received | User confirmed: S2 placeholder is stored
  content (O5); OK to use v0.0.40 as authority. Remaining: S1 bleed mechanism, same-session?,
  memory identity. Freeze pending these.
- **Stage 0b** | — | symptom set FROZEN | S1 "as file content" + concurrent tangent; S2c new-memory
  lead; before-DB offered.
- **Stage 2** | **BLOCKER (reframe)** | STOP-FOR-HUMAN | Evidence (O6–O10) **refutes** the reported
  S2 mechanism (H-S2-CORRUPT / O5): the Vernon Rudd content was intact & reachable the whole time;
  the "predates…" text is a **confabulation Phoebe authored on 07-02 and then cited back as a
  system note**. This changes what S2 *is* (data-integrity bug → confabulation/memory-pollution
  under degraded cognition, possibly shared-root with S1). Not silently re-scoping a frozen symptom
  — bringing the contradiction to the user before investing in reproduction.
- **User adjudication** | — | re-scoped | User: confabulation fits (re-scope S2 around it); 0.0.38
  link = lead not constraint; S1/S2 roots kept separate; confab-on-miss is rare (O11).
- **Stage 4 (repro/toggle) — triage** | — | guarded-change-LITE | `replay_search.py` +
  `toggle_relevance.py` are read-only, self-contained, NO tokens (pure SQLite on DB copies) → lite:
  one cold red-team pass each. Representativeness gate: both reproduce the NAMED symptom (detailed
  memories absent; confab surfaced) — control exhibits the symptom. ✅
- **Stage 7 pre-check** | — | all-three met, red-team pending | Reproduce-on-demand (O16) + causal
  chain (store.py:543 → O16) + toggle (O17). Spawning cold red-team of the causal chain + both
  artifacts before declaring "found".
- **Stage 7 — root-cause confirmation** | **MINOR** (2 caveats, non-overturning) | **FOUND (S2)** |
  Cold red-team (O18) could not break it: 6/6 citations verified, scripts faithful, toggle isolates,
  version-fidelity independently confirmed, log corroborates rank-1. Discrepancy resolved (O19),
  alternative path ruled out (O20), rank-2 stated as derived (O21). All three "found" criteria met +
  independent challenge passed → S2 root cause CONFIRMED: recency-only ranking in
  `store.search_text` (store.py:543). Not data corruption.
- **Stage 8 — handoff (S2)** | — | diagnosis.md written; hand to guarded-change for the FIX
  (dragonfly does not author it). User deferred S2 fix until after S1.

## S1 thread
- **S1 stage 0-2** | — | symptom grounded + escalation characterized | Bled artifact obtained
  (Phoebes_notes.md); symptom = monologue-register content in file + chat (S1-O1). Structural bleed
  surface = monologue injected into context every turn (S1-O2). Escalation signature = within-session
  increasing bleed, first-ever file bleed (S1-O3). Baseline since 0.0.36; escalated today.
- **S1 gate** | **BLOCKER (code fidelity)** | STOP-FOR-HUMAN | Phoebe's monologue/prompt code =
  v0.0.40 + user patch(es) NOT in my clone (S1-O4). Cannot cite the code she runs → requesting the
  patch/diff-vs-v0.0.40 before any structural diagnosis. Also flagged: part of S1 may be emergent
  context-length coherence decay (a model property, not a clean toggle) — set expectations.
- **S1 code fidelity** | — | RESOLVED | Patch obtained (`~/Desktop/monologue_fix_apply/`), applied to
  v0.0.40 worktree = Phoebe's real code (S1-O5). Structural analysis proceeded on it.
- **Self-audit (user challenge "run everything through the loop?")** | — | gap found + closing |
  Honest audit: S2 fully gated (repro+toggle+red-team, FOUND); H-S1-DISTANCE gated (refuted);
  **H-S1-FILEBLOAT was presented as "leading" WITHOUT a cold red-team or repro/toggle** — a
  gate-before-present slip (recorded to memory `dragonfly-gate-before-present-slip` for a future
  skill fix). Closing now: spawned a cold red-team of the H-S1-FILEBLOAT causal chain (attacks the
  crux — do the 0.0.40 read caps + dedup make within-turn accumulation too small to matter; does the
  final generation pass even see it; is history truly text-only). Full reproduce+toggle still needs
  the throwaway-persona repro after.
- **H-S1-FILEBLOAT cold red-team** | **BLOCKER** | REFUTED | S1-O13: the accumulation mechanism is
  DEAD CODE on Phoebe's claude-cli provider (tool calls run in the subprocess via MCP; run_tool_loop
  returns after one pass); caps+80K budget bound it even on Ollama; the prior #5 was a token-COST
  finding, not coherence. SECOND S1 code hypothesis refuted on a false architectural assumption. → S1
  has **no confirmed code root cause**; honest account is emergent/behavioural (monologue + just-
  written content sharing the subprocess's turn-context → imitation bleed), only investigable via a
  claude-cli behavioural repro. One solid code fact remains: `propose_write` (0.0.38) made the
  file-write variant possible. The gate caught a hypothesis that would have sent a fix at DEAD CODE —
  vindicates the "run everything through the loop" challenge.
- **S1 stage-7 red-team** | **MAJOR** | hypothesis REVISED, NOT "found" | Cold red-team (S1-O7)
  refuted H-S1-DISTANCE's escalation mechanism + the patch-amplifier claim (structural facts hold,
  causal story doesn't). Leading account is now **H-S1-EMERGENT** (context-length coherence decay,
  self-reinforcing within-session), which is largely a MODEL property — no clean code toggle.
  **S1 outcome = CHARACTERIZATION + mitigation directions, not a code root-cause "found"** (honest
  ceiling; the user's "hunt the structural amplifier" was pursued and the amplifier didn't survive).
  I corrected my earlier over-confident S1 message to the user.
- **S1 stage 2 — new observation + archaeology** | — | candidate strengthened, still UNGATED | User
  supplied a natural A/B (S1-O14): the old direct-edit path bled little, and (S1-O15 refinement)
  degradation happened there too but needed **larger files / longer time** → dose-dependent, not
  qualitative. Git archaeology (S1-O16, read-only no-token) VERIFIED the timeline: native
  Edit/Write + `--dangerously-skip-permissions` ≤v0.0.31 → `--disallowedTools` lockdown at v0.0.31
  (d53776e) → `propose_write` full-body authoring at v0.0.38 (e388c37); grounded the surgical-diff
  vs full-body-in-voice mechanism contrast. New unifying candidate **H-S1-WRITELOAD-DOSE** recorded
  (subsumes WRITECONTENT-IMITATION + the salvageable core of refuted FILEBLOAT, relocated to the live
  subprocess context). **Gate discipline:** archaeology is git-cited FACT, but the causal account is
  STATIC REASONING → marked `ungated`; NOT presented as the cause. Next = the dose-response
  behavioural repro (throwaway persona, real claude-cli path) — CONSUMES TOKENS → full guarded-change
  per triage. Not yet designed/run.
- **S1 stage-4 — discriminating test DESIGNED** | — | spec written, queued for full guarded-change |
  `s1-repro-spec.md` drafted: dose-response repro driven through the REAL Nell CLI (`nell chat
  --persona <throwaway> --no-bridge` REPL via stdin — user requirement; verified engine/provider-core
  identical to the live app, cli.py:1773/1792→engine.py:272→provider.py:542). Throwaway persona under
  a temp KINDLED_HOME (never Phoebe), notes-folder auto-commit for headless writes. Arms: A high-load
  full-body rewrite / B low-load append proxy / C no-write length-matched; cross file-size. Primary
  endpoint = objective monologue↔reply/file overlap, with a MANDATORY detector-representativeness gate
  (must flag the real ~/Downloads/Phoebe incident first) + a harness-representativeness gate (Arm A
  must actually bleed). CONSUMES TOKENS → full guarded-change before any turn runs. Awaiting user
  go/no-go to enter guarded-change.
- **S1 spec refinements (user, 2026-07-02)** | — | representativeness hardened | (1) All arms are
  MIXED sessions (ongoing chat interleaved with edits), not pure write loops — bleed is measured on
  BOTH surfaces (chat every turn incl. Arm C; file on A/B edit turns). (2) Added prior-history size
  as a 3rd dose axis (small vs big); big = synthetic ~incident-length (S1-O17: ~69 exchanges/~41K
  tok/~190KB, never Phoebe's file). Minimal first pass now anchors on the incident-equivalent
  condition (big-history × A × large file) to satisfy the representativeness gate before walking the
  dose down. Spec updated; still awaiting go/no-go.
- **S1 → guarded-change ENTERED (user "go", 2026-07-02)** | — | full guarded-change under
  `hunts/…/changes/s1-repro-harness/` | Building+running the dose-response harness. Feasibility
  BLOCKER found+resolved at setup: the `claude` binary on PATH (`~/.local/bin/claude` → 2.1.199,
  installed today) **SIGSEGVs on any invocation** (also 2.1.198 hangs); 2.1.181 + 2.1.186 work
  (this VSCode session runs on the extension's bundled 2.1.186). Any real `nell` run here would
  crash in provider.py:496 (`claude -p …`). RESOLUTION: harness pins `claude`→2.1.186 on its
  subprocess PATH (scoped, non-invasive). Real provider invocation verified = `claude -p <prompt>
  --output-format json --model …` (provider.py:496-501), NOT the recon's "claude chat". Substituting
  a non-claude-cli provider is FORBIDDEN (S1 is a claude-cli-subprocess phenomenon, S1-O13 → would
  fail the representativeness gate). Env facts: .venv present, `nell`=brain.cli:main, glibc 2.43 /
  kernel 7.0.0.
