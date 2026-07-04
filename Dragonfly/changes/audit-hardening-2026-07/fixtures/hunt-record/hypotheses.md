# Hypotheses — monologue-bleed + memory-gap hunt

Ranked, falsifiable. Status: open / confirmed / refuted.

## S2 — "predates current memory infrastructure"

- **H-S2-CORRUPT (user's original O5 model): a memory record's content was overwritten/never
  populated, leaving a placeholder.**
  - Confirm: find a memories.db record whose `content` is the placeholder standing in for the real
    Vernon Rudd content, with the real content absent.
  - Refute: real content present + intact; placeholder only in separately-created records.
  - **STATUS: REFUTED** by O6 (real content intact, 06-19) + O8 (placeholder is in new 07-02 records).

- **H-S2-CONFAB (leading): Phoebe confabulated a "memory infrastructure gap," persisted it to
  memory, then surfaced/cited her own fabrication as a system fact to Roy.** No data was lost.
  - Confirm: real content exists & was reachable at search time (O6, O7); the "predates…" text
    originates in 07-02 records Phoebe authored (O8); she reported it to Roy as a search result
    (O9); the cited text matches her own just-written note (O10). ✅ all present.
  - Refute: would need the real content to have been genuinely absent/unreachable at 15:56–16:10.
  - **STATUS: strongly supported; not yet root-caused.** Open sub-question: WHY the initial search
    didn't surface/ get recognized the rich 06-19 memories (ranking/recall miss vs degraded
    reading), which is what triggered the confabulation.

- **H-S2-RECENCY (CONFIRMED, pending cold red-team) — ROOT CAUSE of the user-visible S2 symptom:**
  `search_memories` is keyword-LIKE (O13); `store.search_text` ranks `ORDER BY created_at DESC` with
  a small per-token limit (O14, store.py:543), identical in v0.0.40 and HEAD. For a query whose
  generic tokens ("Vernon"/"Rudd") match many memories, the top-5 fills with the NEWEST matches, so
  (a) the older detailed 06-19 church memories are never returned (miss → gap → confab), and (b) the
  freshly-written confab (`35589a3e`, 16:03) surfaces as a top result at 16:09 → Phoebe cites it to
  Roy as "the search note."
  - Confirm: replay shows detailed-06-19 NONE in top-5, confab at rank 2 (O16); toggle to relevance
    ranking surfaces the real memory at rank 1 and drops the confab (O17). ✅
  - Refute: would need the detailed memories to appear in top-5 under the real recency pipeline, or
    the confab NOT to surface at 16:09. Neither holds.
  - **STATUS: reproduce-on-demand ✅ + cited causal chain ✅ + toggle ✅ → awaiting stage-7 cold
    red-team before "found".**
  - NOTE (honest scope): recency-ranked retrieval is the toggleable CODE root of the symptom Roy
    saw. Phoebe's *choice* to confabulate rather than say "couldn't find it" (rare per O11, given
    Roy's strong expectation O12) is a model-behaviour contributor, not fixable at the retrieval
    layer — but a relevance fix removes the trigger, so the confab never gets its opening.

- **H-S2-SELFCITE (sub-hypothesis of the loop): the 16:09 search surfaced Phoebe's own 16:03
  confab (35589a3e), which she cited at 16:10.**
  - Discriminate: replay "Vernon Rudd knife fight church duel" offline; does 35589a3e rank in top-K?
  - (Bounded by truncated tool-log; offline replay is the representative test.)

## S1 — monologue bleed into speech + file content

> **STATUS UPDATE (cold red-team S1-O7): H-S1-DISTANCE mechanism REFUTED (MAJOR).** The structural
> facts hold, but the escalation mechanism (progressive burial) is invalid — the static directive is
> a FIXED pre-history slot, and the anti-bleed reminder ("never quote interior; second person") lives
> in the reply frame that never moved and is still last. The patch is NEUTRAL on bleed (fixes firing,
> a different symptom); HEAD ships the same structure. **H-S1-EMERGENT is now the leading account.**

> **REOPENED (user, 2026-07-02): pure-emergent account INSUFFICIENT.** This session was SHORT in
> messages sent, the worked file was deliberately short, and file reads/writes are NOT in the sent
> chat history — yet the decay/bleed hit. So conversation-length can't be the driver. User's lead:
> the bloat comes from the **FILE-ACCESS system introduced in 0.0.38** (matches the 0.0.38
> recurrence + the "cognitive regression = context bloat" framing). Some fixes were made to that
> system but not all suggestions applied, and those may have been insufficient. → **H-S1-FILEBLOAT.**

> **REFUTED — BLOCKER (cold red-team S1-O13).** The Python tool-loop accumulation this hypothesis
> depends on is DEAD CODE on Phoebe's `claude-cli` provider (tool calls run in the subprocess via MCP;
> `run_tool_loop` returns after one pass). Caps + 80K budget bound it even on Ollama. The prior "#5"
> was a token-COST finding, not coherence. Second S1 hypothesis killed by a false architectural
> assumption (cf. H-S1-DISTANCE). **Do not resurrect without a claude-cli-aware mechanism.**

- **H-S1-WRITECONTENT-IMITATION (candidate, UNGATED — from the S1-O13 red-team):** on claude-cli the
  model, within one agentic subprocess turn, has its own monologue + the `propose_write` content it
  just authored in-context (the content also re-enters via the pending-write surface,
  `app/.../PendingWriteCard.tsx`); it imitates the FORM of what it just wrote/thought → bleed. Fits
  the 0.0.38 timeline (write tool) with NO bloat story. **NOT gated — do not present as leading; needs
  a behavioural repro to test.** This is essentially the emergent/imitation account localised to the
  subprocess's shared turn-context.

- **H-S1-WRITELOAD-DOSE (candidate, UNGATED — strengthened refinement, 2026-07-02, S1-O14/O15/O16):**
  the unifying account. S1's two faces (coherence *degradation* AND monologue *bleed*) share one
  **dose-dependent driver: how much persona-authored, full-file content accumulates in the
  claude-subprocess context per unit of file work.** `propose_write` (0.0.38) makes the persona
  re-author the **entire file body in-voice** for every op (propose_write.py:35), in her
  monologue-laden generative context, and a write→re-read→rewrite loop repeats it → context fills
  **fast, on small files**, driving decay AND supplying monologue-adjacent imitation material. The
  **old native-edit path** (≤v0.0.31, `--dangerously-skip-permissions` + built-in Edit/Write,
  S1-O16) emitted **surgical diffs on a read-once cached file** → same failure mode but a **much
  higher threshold** (large files / long sessions) — exactly the user's A/B (S1-O15). Subsumes
  H-S1-WRITECONTENT-IMITATION (bleed) and the salvageable core of the refuted H-S1-FILEBLOAT
  (accumulation) — relocated from the dead Python tool-loop (S1-O13) to the **subprocess context**,
  where it is live.
  - Timeline fit: native direct-edit ~0.0.25→0.0.31 (slow/large-file degradation) → capability gap →
    propose_write 0.0.38 (fast/small-file degradation + first file-write bleed). ✅ 3 data points.
  - Confirm (behavioural DOSE-RESPONSE, NOT yet done): on a throwaway persona through the real
    claude-cli path, hold everything constant and vary **(mechanism × file size × #full-content
    rewrites)**; degradation+bleed onset should be **monotonic in accumulated authored-content volume**
    and hit **sooner for propose_write than for a surgical-edit control at equal file size**.
  - Refute: onset independent of authored-content volume; or propose_write and a surgical-edit control
    degrade at the same dose; or bleed present equally in a no-file-write control at equal context size.
  - **GATE MARKER: ungated.** Static reasoning only (a sibling accumulation hypothesis was already
    refuted once, S1-O13). Present as a strengthened *candidate*, never the cause, until the
    dose-response repro runs. CONSUMES TOKENS → full guarded-change per triage.
  - Fix DIRECTIONS (guarded-change, not authored here): (a) make propose_write patch-based / diff-based
    (append/section-replace) so the persona doesn't re-emit the whole body; (b) bound/evict authored
    file content from the running subprocess context; (c) session/turn caps on file-write volume;
    (d) the monologue↔reply separation mitigations from H-S1-EMERGENT still stack.

- **H-S1-FILEBLOAT (REFUTED — kept for record): the file-access system (read_file/propose_write, added 0.0.38)
  bloats the model's effective context** — likely by injecting full file-read contents (and/or tool
  I/O) into the context in a way that ACCUMULATES (within-turn across many reads, and/or across turns
  if the underlying CLI session persists), so effective context grows large during file-heavy work
  even when the persisted chat is short. This drives BOTH the coherence decay ("cognitive
  regression") and the monologue bleed, and explains why it hit on a short conversation + short file,
  and why it escalated toward the end (accumulated file I/O), and the 0.0.38 origin.
  - Discriminate (offline, low/no token): trace how read_file's result enters the model context
    (`engine.py` tool loop / `provider.py` CLI invocation) — does it persist/accumulate across turns
    or reset per turn? Is file content bounded/evicted? Measure the effective context size of the
    incident turns vs a baseline. Check what 0.0.38 introduced + which fixes/suggestions were/ weren't
    applied.
  - Confirm: file-read content accumulates unbounded in the context the model sees; incident turns
    show large effective context despite short chat. Refute: read results are bounded/evicted and the
    effective context on incident turns was small.
  - **REFINED (S1-O9/O10/O11):** mechanism = **within-turn** tool-loop accumulation (#5, tool_loop.py
    :334/393/423) — the final generation pass sees ALL tool I/O accumulated over the ≤4 iterations.
    Bloat is WITHIN-turn (across-turn history is text-only, S1-O10). The accumulation mechanism
    PREDATES 0.0.38 (tool_loop/read_file identical 36→38); the 0.0.38 **WRITE tool (propose_write)**
    is what (a) made file-write bleed possible ("first time in files") and (b) drives a
    write→re-read→write workflow that EXERCISES the accumulation hard. So H-S1-FILEBLOAT is really
    "pre-existing within-turn accumulation, newly hammered by the 0.0.38 write workflow."
  - **Magnitude UNMEASURED** (Phoebe's usage logger didn't record the incident, S1-O12) → confirm via
    throwaway-persona repro (deterministic: file-heavy vs file-light turn context size; probabilistic:
    bleed). Full guarded-change (tokens). Until then: LEADING lead, NOT confirmed cause.
  - Fix DIRECTION (guarded-change): bound/evict the within-turn tool-result payload so file content
    doesn't accumulate into the final generation context (the #5 structural fix the prior report
    flagged); optionally summarise old tool results within the loop.

- **H-S1-EMERGENT (was leading; now a CONTRIBUTING factor / backdrop): context-length coherence
  decay, self-reinforcing within a session.** Still real, but the DRIVER of *why context was large
  here* is H-S1-FILEBLOAT, not message count. The decay is the mechanism by which large context →
  bleed; the file-access bloat is the SOURCE of the large context. As history grows, the fixed last-position
  "never quote interior / second person" reply-frame reminder competes against an accumulating body
  of first-person interior content (interior/recall/journal blocks + the model's OWN prior replies in
  history). Once bleed enters a reply, that reply sits in history and the model imitates its own
  recent style → drift compounds toward the end of a long session. This escalates identically on
  pristine 0.0.40 (fits bleed predating the patch since 0.0.36).
  - NOT a clean code toggle — largely a model property. Confirmation needs a live long-context run.
  - Fix DIRECTIONS (mitigations, all need behavioural test; none a proven root-cause code fix):
    (a) session-length caps / compaction to prevent the accumulation + self-reinforcement (most
    promising, addresses the growth driver); (b) strengthen/repeat the anti-quote reminder or raise
    its salience; (c) reduce interior-content injection in long contexts. Handle via guarded-change.

- **H-S1-DISTANCE (REFUTED — kept for the record):** In Phoebe's real code
  (v0.0.40 + patch, S1-O5), her recent monologue CONTENT rides the volatile tail near the generation
  point (`interior_block`, l.444), while the two-phase "keep monologue separate from the reply"
  DIRECTIVE sits in the frozen static prefix, above the conversation history. As a session's history
  grows, the directive is buried ever further from generation while monologue content stays adjacent
  → the monologue↔output boundary erodes progressively.
  - Explains: within-session escalation ("more & more frequently toward the end", S1-O3); first-ever
    bleed into file writes (propose_write content generated near the eroded boundary, S1-O1);
    baseline bleed since 0.0.36 (interior monologue always in-context); why the FIRING patch didn't
    help (different target, S1-O6) and may have AMPLIFIED (removed the near-generation reminder).
  - Confirm (structural, checkable): reconstruction shows directive in static, absent from tail,
    interior content near generation — ✅ S1-O5.
  - Confirm (behavioural — NOT yet done): a live model, long-context run shows bleed rising with
    history length, and a toggle restoring a near-generation separation cue reduces it. Requires
    tokens + throwaway persona (never Phoebe); bleed is intermittent/load-dependent → instrument-to-
    capture, not a clean offline toggle. **This is why S1 is NOT declared "found".**
  - Refute: bleed present even in short contexts at equal rate; or interior_block not actually
    monologue-register content; or the reply frame itself already re-states the separation.
  - Caveats: amplifier, not sole cause (baseline predates patch); residual context-length coherence
    decay is a model property, not code-fixable.
  - Fix DIRECTION (guarded-change, not authored here): restore a brief monologue↔reply separation
    cue NEAR the reply frame (without undoing the firing fix in static); and/or reconsider
    interior_block position/labelling so its content reads as context, not as draftable output.

- **H-S1-EMERGENT (co-exists): part of the escalation is plain context-length coherence decay** —
  the model gets worse at honouring structural boundaries in very long context regardless of prompt
  layout. Not separately toggleable; bounds what any code fix can achieve. Mitigation: session-length
  limits / compaction.

- Relatedness to S2: same session/window, but user directed roots kept SEPARATE. Held separate.

## Note on the 0.0.38 "identical" incident

User says S2 is identical to a 0.0.38 occurrence. Need to know what THAT was mechanically
(genuine loss/corruption vs the same confabulation) — it discriminates "recurring behavioral bug"
from "different bug that looks similar." → ask user.
