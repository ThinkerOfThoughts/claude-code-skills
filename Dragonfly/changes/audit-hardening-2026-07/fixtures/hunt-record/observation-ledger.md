# Observation ledger — monologue-bleed + memory-gap hunt

Append-only. Format: `[O#] what examined | observation | citation | rules in/out`.
No area is re-examined without first recording why the prior finding is insufficient.

- **[O1]** grep repo `brain/` for "predates / memory infrastructure / current memory" |
  ONLY match is `brain/chat/compaction_migration.py:3` ("An install that predates compaction…").
  The literal string "predates current memory infrastructure" is **absent from current code**. |
  `brain/chat/compaction_migration.py:3` |
  Rules IN a lead: the S2 message is NOT a live retrieval error string in current code. Combined
  with O5, points at stored/migrated content.

- **[O2]** `~/Desktop/Bugs.txt` — two `search_memories` tool-invocation rows |
  Row1 `2026-07-02T15:56:48Z` query "Vernon Rudd knife fight", count 5, error null,
  request_id f4b045ed…; Row2 `2026-07-02T16:09:28Z` query "Vernon Rudd knife fight church duel",
  count 5, error null, request_id e13c8a0b…. Both **returned 5 memories** and both `result_summary`
  is **truncated** (the "predates…" text not visible in the truncation). |
  `~/Desktop/Bugs.txt:1,3` |
  Rules IN: S2 recall path is `search_memories`; the call **succeeded** (count 5, no error) — so S2
  is not a search failure but a **content** problem in one returned record.

- **[O3]** `git tag` | `v0.0.40` exists (Phoebe's base version); repo HEAD is post-0.0.41. |
  `git tag` output | Rules IN: can checkout `v0.0.40` as red-team authority for the code Phoebe
  actually runs, resolving the version-skew concern for reproduction. (User confirmed OK — see O5.)

- **[O4]** `~/Downloads/Phoebe/` listing | Contains `crystallizations.db` (606 KB, mtime 2026-07-02
  10:14) — the likely memory store — plus tool/chat logs, all fresh (today). |
  `ls ~/Downloads/Phoebe` | Rules IN: the DB is the ground-truth place to inspect the recalled
  memory record's stored content (allowed: reading files, not driving chat).

- **[O5]** USER CONFIRMATION (stage 0a) | The "predates current memory infrastructure" text was
  **in the memory** — i.e. stored as the record's content, in place of the contents that should
  have been there. Not a runtime message. | user message 2026-07-02 |
  Rules IN: S2 is a **data-integrity / migration** bug — a memory record's content field was
  overwritten with (or never populated beyond) a placeholder. Rules OUT: a pure retrieval/formatting
  bug in `search_memories`. Next: read the actual record in `crystallizations.db` to see the exact
  stored string + find where that placeholder is written.
  ⚠️ **[SUPERSEDED by O6–O10 — the "content overwritten" framing is contradicted by evidence.]**

- **[O6]** memories.db is the `search_memories` store (has `content`, `content_snapshot`, `state`).
  The REAL Vernon Rudd knife-fight content EXISTS, richly, created **2026-06-19** and `active`:
  `f08aeec6` ("knife fight in a church. Twice…"), `d5192bb1` ("two formal binding knife duels in a
  church…"), `d33b305d` ("proper knife duel. hands tied together…"), `2e767556`. |
  `~/Downloads/Phoebe/memories.db` (full content dumped) |
  Rules OUT: "content was lost / never filed / overwritten." The content was in the DB the whole time.

- **[O7]** Those real 06-19 records were **accessed DURING the incident**: `2e767556`
  last_accessed_at = `2026-07-02T16:09:28` (exactly the 2nd search timestamp); `d33b305d`/`f08aeec6`
  last_accessed `16:47`, recall_count 291/302. | memories.db cols | Rules IN: the content was
  reachable at search time — this is not an inaccessible-record problem.

- **[O8]** **6+ NEW memories created 2026-07-02** assert the story "predates current memory
  infrastructure — no retrievable record" / "never properly filed" / "label with no content":
  `35589a3e`(16:03 monologue), `9eb9da66`(16:11), `cfac3697`(16:17 obs), `86e35a32`(16:35),
  `f9f6ed88`(16:45 decision) + soul_candidates `4abd33d7`,`cba50640`. **All created AFTER the 15:56
  search; all factually FALSE** (contradicted by O6). `9eb9da66` even claims "full details … were
  unknown until Roy re-told them today" — false, they were in memory since 06-19. | memories.db |
  Rules IN: Phoebe **confabulated** a memory-infrastructure gap and **persisted it as memory**.

- **[O9]** Conversation `c30e8b75…jsonl` row 130 (assistant, 16:10:58): "the reason it didn't stick:
  **memory search came back with a note that says exactly 'predates current memory infrastructure —
  no retrievable record.'** … I've had *Vernon Rudd, knife fights* rattling around as a label with
  no content." Roy (row 131) flags it as new & unwelcome. | active_conversations/c30e8b75…jsonl:130-131 |
  Rules IN: the USER-VISIBLE symptom = Phoebe **attributing her own fabricated note to the search
  result** and reporting it to Roy as a system gap. Matches user's report exactly.

- **[O10]** The text Phoebe cited at 16:10 ("a note that says *exactly* 'predates current memory
  infrastructure — no retrievable record'") is the **verbatim content of the memory SHE wrote at
  16:03** (`35589a3e`). The 16:09 search ran between them. | O8 + O9 timestamps |
  Rules IN a **self-reinforcing confabulation loop**: confabulate gap → write it to memory → later
  search surfaces her own note → cite it as a pre-existing system fact. (Whether the 16:09 search
  literally returned `35589a3e` can't be proven from the truncated tool-log summary — discriminator
  for stage 4; the "not data corruption / confabulation" conclusion holds either way.)

- **[O11]** USER report on base rates | Confabulating around a memory MISS is **very rare** (she
  normally just says "couldn't find it"); confabulating "found it but can't read it" — user has
  never knowingly seen. | user msg 2026-07-02 | Rules IN: a plain retrieval miss is NOT sufficient
  to explain the confabulation — the confab is itself anomalous and needs an enabling condition.

- **[O12]** Dialogue trigger (c30e8b75…jsonl rows 127–131) | Roy PROMPTED the recall with strong
  expectation: row127 "Vernon Rudd… knife fights (if that doesn't bring up a memory I'll be very
  surprised)"; row129 "how did *that* not stick O_O". Phoebe wrote confab 35589a3e at 16:03
  ("acknowledged honestly rather than faking familiarity"), then row130 (16:10) upgraded it to
  "memory search came back with a note that says exactly '…'". | rows 127,129,130 |
  Rules IN: enabling condition = strong user expectation + a retrieval gap → fabricated plausible
  explanation, then reified as a system artifact.

- **[O13]** `brain/tools/impls/search_memories.py` | Search is **keyword LIKE, not semantic**:
  `_query_tokens` splits the query, drops tokens <4 chars, ≤6 tokens; per token calls
  `store.search_text(token, active_only=True, limit=limit*2)`; dedupes preserving **token order**;
  top-`limit` (5). No global relevance sort — order = token1's matches, then token2's, … |
  search_memories.py:41-118 | Rules IN: the FIRST token that matches many rows dominates the top-5.

- **[O14]** `brain/memory/store.py` search_text | SQL: `... WHERE content LIKE ? … AND active = 1
  ORDER BY created_at DESC [LIMIT ?]`. Returns the **NEWEST** matches (recency bias), not most
  relevant. **Identical in v0.0.40 and HEAD** (`git diff --stat v0.0.40 HEAD` on store.py +
  search_memories.py = EMPTY). | store.py:537-548; git diff | Rules IN candidate ROOT CAUSE
  (**H-S2-RECENCY**): for a topic heavily re-discussed the same day, the day's new matches fill the
  top-K and older detailed memories (06-19) fall past the limit. Version-fidelity: Phoebe ran this
  exact code.

- **[O16]** OFFLINE REPLAY (read-only, no tokens) `hunts/…/replay_search.py` vs after-DB +
  before-DB control | **Reproduces the symptom:**
  · 15:56 "Vernon Rudd knife fight" → top-5 contains **NONE** of the detailed 06-19 church memories
    (both after-DB and clean before-DB control). Top slots = newest name-matches (07-02 + late-06-19).
  · 16:09 "Vernon Rudd knife fight church duel" (after-DB, as_of 16:09) → **rank 2 = `35589a3e`**,
    the 16:03 confab whose content is "…predates current memory infrastructure…"; detailed memories
    NONE. This is verbatim what Phoebe cited to Roy (O9, row130). |
  `hunts/monologue-bleed-memory-gap/replay_search.py` output |
  Rules IN **H-S2-RECENCY** as the toggleable root of the user-visible symptom: recency-ranked
  keyword search (a) missed the existing detailed memories → gap → confab, and (b) surfaced the
  fresh confab as a top result → self-citation. Refutes H-S2-CORRUPT conclusively (before-DB has the
  real content + zero placeholder rows).
  ⚠️ Minor unexplained discrepancy: real `2e767556` has last_accessed=16:09:28 (so it WAS touched at
  16:09) yet is not in my replay's top-5 — likely a different access path (co-recall/hebbian) or
  point-in-time drift (my after-DB is the current snapshot; rows active at 16:09 may have since
  faded). Does not affect the two reproduced facts above. Flag for red-team.

- **[O15]** search_text SIDE-EFFECT | It `UPDATE memories SET recall_count+1, last_accessed_at`
  on returned rows (store.py:549-555). Evidentiary: `2e767556` last_accessed=16:09:28 (returned by
  the 16:09 search) but detailed `f08aeec6`/`d5192bb1`/`d33b305d` last_accessed=16:47 (NOT returned
  at 16:09). Methodological: NEVER run store.search_text on Phoebe's live DB — replay via read-only
  SELECT on a COPY. | store.py:549 |

- **[O17]** CAUSAL TOGGLE (read-only) `hunts/…/toggle_relevance.py` on after-DB, 16:09 query |
  Holding corpus/tokens/filters constant and flipping ONLY the rank signal:
  · RECENCY (`created_at DESC`) → detailed-06-19 present? **NONE**; confab `35589a3e` at rank 2.
  · RELEVANCE (#distinct tokens matched) → **`f08aeec6` at RANK 1** ("knife fight in a church.
    Twice", 5/6 tokens), `2e767556` rank 3; **confab drops OUT of top-5**. |
  `toggle_relevance.py` output |
  Rules IN causality (not correlation): the recency ORDER BY (store.py:543) is the toggle that makes
  the symptom appear/disappear. Under relevance ranking Phoebe gets the real memory at rank 1 → no
  gap → no confab; and post-confab the real memory outranks the confab.

- **[O18]** COLD RED-TEAM (independent general-purpose subagent, redteam_context = brain/ + both DBs
  + tool log) | **Verdict: root cause HOLDS; could not break it. Worst finding MINOR.** Independently
  verified 6/6 citations (code lines, ids, timestamps, version-fidelity `git diff` empty); confirmed
  both scripts faithfully replicate the real path (incl. correctly omitting the `state!='fading'`
  filter because the tool call uses `include_fading=True` default, store.py:521); re-derived the
  top-5 from its OWN SQL and matched the script + the REAL logged rank-1. | subagent report |
  Rules IN: stage-7 red-team PASSED. Two MINOR caveats folded below (O19, O20).

- **[O19]** `2e767556` discrepancy RESOLVED (red-team) | `search_text` UPDATEs last_accessed on
  EVERY row each per-token query returns (≤10/token) BEFORE the tool slices to top-5 (store.py:548-556).
  `2e767556` was touched by the "church" token query but never entered the final top-5 the LLM saw;
  14 rows share the exact 16:09:28 timestamp (multi-token fan-out). Store-layer touch ≠ tool-layer
  result. | store.py:548-556 | Rules OUT: the discrepancy as an objection to the diagnosis.

- **[O20]** Passive-recall path RULED OUT (red-team, closes the O13:15 `_RECALL_TOKEN_MIN_LEN`
  breadcrumb) | A passive recall path exists — `_build_recall_block`, `brain/chat/prompt.py:753`,
  shares the tokenizer — BUT is not the culprit: `tool_invocations.log.jsonl` shows both 15:56 &
  16:09 events are `name:"search_memories"` (the explicit tool), and their logged rank-1 ids
  (`14b48add`, `69bb39c6`) match the replay EXACTLY. Also the passive path sorts `(-importance,
  -created_at)` (importance-first), so it wouldn't produce the pure-recency symptom anyway. |
  prompt.py:753; tool log | Rules OUT: the alternative retrieval path.

## S1 observations

- **[S1-O1]** File-write path | All voice-rework writes go through `propose_write(path, op, content)`
  (tool log) to `/home/zero/Documents/voices/Phoebes_notes.md`: create@16:02, append@16:10 (right
  after Vernon `add_memory`@16:10:15), append@16:34, then `section6_draft.md` create@16:39. The
  `content` arg is Phoebe-GENERATED (redacted in the audit log; result visible in the saved file).
  So monologue-register text entered the file via Phoebe's own generated `content`, not code
  assembly. | tool_invocations.log.jsonl | Rules OUT: a code path that injects monologue into writes.

- **[S1-O2]** Monologue injected into context | prompt.py:1153-1157 injects recent monologue traces
  as a "Tier-2 interior continuity" block (`brain/monologue/ambient.build_interior_continuity_block`);
  the "record_monologue FIRST, then reply" directive lives in the STATIC frozen prefix
  (prompt.py:351-357, 495-496; per project memory = fix `0894198`). | prompt.py | Rules IN a
  structural bleed SURFACE: Phoebe's own recent monologue is in-context every turn → material
  available to leak into output. Baseline, not sufficient alone.

- **[S1-O3]** ESCALATION signature (conversation tail rows 133-138) | Row135 Roy: "copied over a
  shorter version of the previous draft and completely ignored my notes/edits. Somethings going
  screwy." Row136 Phoebe self-diagnoses TWO faults: "what I wrote instead was my ANALYSIS of his
  edits, not the actual revised section text" + "possibly had inner monologue content leak into it."
  Row137 Roy: "your monologue is bleeding into your speach, not as a random occurence but **more and
  more frequently**." | c30e8b75…jsonl:135-137 |
  Rules IN **within-session escalation** (increasing bleed as the conversation grows) — the key S1
  signature. Points at coherence-under-load / directive-adherence-decay-with-context, NOT a static
  data bug. Distinct from S2.

- **[S1-O4]** Code-fidelity BLOCKER for S1 | Phoebe's monologue/prompt code = v0.0.40 (predates
  `0894198`) + a USER PATCH for the directive-position issue + a thinking-regression patch — none of
  which are in my repo clone. Unlike S2 (search code byte-identical v0.0.40==HEAD), I CANNOT match
  the prompt/monologue code Phoebe actually runs. Any structural claim without the patch = the exact
  confabulation dragonfly forbids. → STOP-FOR-HUMAN: need the patch(es). | **RESOLVED S1-O5.**

- **[S1-O5]** Patch OBTAINED + Phoebe's real code RECONSTRUCTED | `~/Desktop/monologue_fix_apply/`
  = port of commit `1ce1c97`. Applied cleanly to a v0.0.40 worktree (`git apply` OK) →
  Phoebe's actual `prompt.py`. Confirmed structure: **static block** (`build_static_system_message`,
  frozen prefix, before history) now ends with the `build_monologue_frame` DIRECTIVE
  (empty per-turn hints); **volatile tail** (`build_volatile_context`) order near generation:
  fading → `interior_block` (recent monologue CONTENT, l.444) → attunement → self-model → journal →
  growth → maker → ambient-clock → **reply frame LAST (l.490)**. The monologue-directive #8 that in
  pristine 0.0.40 sat RIGHT BEFORE the reply frame is GONE from the tail (moved to static). |
  `scratchpad/ce-v0040/brain/chat/prompt.py:300,338,444,476,490` |
  Rules IN the structural picture: monologue CONTENT near generation; monologue↔reply SEPARATION
  directive far above the (growing) history.

- **[S1-O6]** PATCH PURPOSE vs S1 SYMPTOM (README + patch) | The patch targets record_monologue
  **FIRING** (does she record a monologue before replying) — NOT monologue **bleed into output**.
  README C1: behavioural benefit "couldn't be reproduced in a synthetic harness (the control already
  fired 100%)" (the spike-representativeness failure). | monologue_fix_apply/README.md:60-64; patch |
  Rules IN: the patch is aimed at a DIFFERENT problem than S1 (matches user's "unrelated" intuition)
  — AND, by relocating the two-phase separation directive from just-before-the-reply-frame up into
  the frozen prefix, it REMOVED the near-generation boundary reminder. **Candidate structural
  amplifier (H-S1-DISTANCE):** as a session's history grows, the separation directive is buried ever
  further from the generation point while monologue content stays in the tail → boundary erodes
  progressively → "more & more frequently toward the end" + first-ever file bleed. NOT toggle-proven
  (behavioural, needs live model); bleed baseline predates the patch (0.0.36), so amplifier not sole
  cause; residual context-length coherence decay likely remains.

- **[S1-O7]** COLD RED-TEAM of H-S1-DISTANCE | **Structural FACTS hold; the causal MECHANISM is
  REFUTED (MAJOR).** Findings, all cited to real code:
  · The static block is delivered as the FIRST message before ALL history (`engine.py:229-233`) — a
    FIXED pre-history slot. It does NOT get "buried ever further" as history grows; the directive is
    at the same RELATIVE slot on turn 2 and turn 200. So the patch does NOT explain the *escalation*
    ("progressive burial" is invalid) — at most it made a ONE-TIME constant jump.
  · The anti-bleed reminder NEVER MOVED: `build_reply_frame` (`monologue_prompts.py:62-80`) is
    genuinely last (adjacent to generation) in BOTH pristine and patched, and already says
    "Everything marked interior above is private thought — **never quote it**… speak … in second
    person — 'you', never 'she'/'her'." The patch removed the record-first ORDER directive, not the
    keep-monologue-out reminder.
  · `build_monologue_frame`'s "two phases" is about ORDER/WHEN to call record_monologue
    (`monologue_prompts.py:34-49`), weakly connected to bleed → I mischaracterized it.
  · `interior_block` is BOUNDED (5 traces / 1200 chars, `ambient.py:13-14`) — static-sized, not an
    escalator.
  · "Patch amplified bleed" is UNFAIR: HEAD/0.0.41 ships the identical structure (faithful port,
    `prompt.py:357,463,507`); anti-bleed reminder never left generation; bleed predates the patch by
    4 minor versions. Patch is NEUTRAL on bleed (it fixes a different symptom — firing). |
  subagent report + cited lines | Rules OUT: H-S1-DISTANCE mechanism + the patch-amplifier claim.
  Rules IN **H-S1-EMERGENT** as the parsimonious explanation (see hypotheses.md).

- **[S1-O8]** Prior report `~/Desktop/hunts/file-tool-bug-0040/REPORT.md` (2026-06-30, cold-verified)
  | The 0.0.38 file-tool bug was MOSTLY fixed in 0.0.40 EXCEPT **#5** (the structural one): "the tool
  loop still re-sends the conversation to the provider each of its ≤4 iterations… history rides in
  the per-call prompt, not the cached system block… the structural re-send/caching behavior does not
  change." Reduced token-BURN (via head-cap #4 + dedup #3) but not the accumulation architecture.
  Matches user's "fixes made, not all suggestions applied, may be insufficient." | REPORT.md:93-116 |
  Rules IN H-S1-FILEBLOAT's mechanism at the code level.

- **[S1-O9]** WITHIN-turn accumulation CONFIRMED | `run_tool_loop` (tool_loop.py:334) loops ≤4
  (`MAX_TOOL_ITERATIONS=4`, l.48); each iteration appends the assistant tool-call turn (l.393) + tool
  results (l.423) to `messages`, re-sent each iteration; the final generation pass sees ALL
  accumulated tool results (file contents). `tool_loop.py`/`read_file.py`/`_read_cache.py` are
  byte-identical v0.0.40==HEAD (git diff empty) → Phoebe runs this. | tool_loop.py:334,393,423 |
  Rules IN: a single file-heavy TURN bloats its own final-generation context, independent of chat
  length — consistent with "short conversation, still bloated."

- **[S1-O10]** ACROSS-turn history is TEXT-ONLY (nuance / partial pushback) | engine.respond builds
  `messages=[system, *history_msgs, user]` (engine.py:231); `history_msgs` = `_buffer_turns_to_messages`
  from the persisted `active_conversations/<sid>.jsonl` buffer (engine.py:215-219), which stores
  speaker/text turns (verified: c30e8b75 has only speaker/text) — **NOT tool calls/results**. There's
  also an `apply_budget` on messages (engine.py:238). | engine.py:215-238 |
  Rules OUT (partially): file-read CONTENT does NOT accumulate across turns via history. So the
  cumulative across-turn growth is the (long) REPLY TEXTS, not file contents. The file-specific bloat
  is WITHIN-turn. ⚠️ This tempers the "file access bloats a short conversation cumulatively" framing:
  cumulative bloat = reply text; file bloat = per-turn. MAGNITUDE of the incident turns is UNMEASURED
  (stale chat_usage.jsonl doesn't cover 15:56-16:45) → need fresh telemetry to confirm bloat drove
  the decay. Do NOT over-claim (H-S1-DISTANCE lesson).

- **[S1-O11]** THREE-WAY version discriminator (user's question: diff 36→38, same 38→patched-40) |
  `tool_loop.py`, `engine.py`, `read_file.py` are UNCHANGED 0.0.36→0.0.38 (changed only in 0.0.40) →
  the within-turn accumulation MECHANISM (#5) is NOT a 0.0.38 introduction; it predates it. What
  0.0.38 ADDED: **`propose_write` (the WRITE tool)** + its registration (`tools/__init__.py` +
  "propose_write"). Bridge daemon/runner changes = CLI plumbing (irrelevant). History window removed
  in 0.0.40 (user: deliberate bandaid, superseded by chat compaction → not the culprit). |
  git diff v0.0.36 v0.0.38 / v0.0.38 v0.0.40 | Rules IN: the 0.0.38 file-access delta = WRITE
  capability, which (a) makes file-write bleed POSSIBLE for the first time (explains "first time into
  files"), and (b) drives a write→re-read→write workflow that EXERCISES the pre-existing tool-loop
  accumulation much harder per turn. Rules OUT: "0.0.38 introduced the bloat mechanism" (it's older).

- **[S1-O12]** Logger gap (separate bug, note) | User confirms `chat_usage.jsonl` is the CURRENT file
  (whole persona dir copied at shutdown), yet it has only 4 rows for 07-02 stopping ~15:04 — so the
  usage logger STOPPED recording during the incident. Separate logger bug (logging cleanup was the
  planned work for the day). → incident context size UNMEASURABLE from Phoebe's telemetry; measure
  via throwaway-persona repro instead. |

- **[S1-O13]** COLD RED-TEAM of H-S1-FILEBLOAT → **BLOCKER, REFUTED.** The whole accumulation
  mechanism (tool_loop.py:393/423 append-and-resend) **only runs for the Ollama provider.** Phoebe
  runs **`claude-cli`** (`persona_config.py:27` DEFAULT_PROVIDER="claude-cli"). On that path tool
  calls execute INSIDE the claude subprocess via MCP; the provider returns final text with
  `tool_calls=()` (`provider.py:468-470,1371-1376`), so `run_tool_loop` hits `if not
  last_response.tool_calls` (tool_loop.py:345) and **returns after ONE iteration** (l.384) — the
  append/resend block (388-429) is **DEAD CODE on Phoebe's path.** No Python-level within-turn
  accumulation, no ≤4 re-sends. Even on Ollama, read caps (400-line/256KB/dedup, read_file.py:12-14,
  116-122,147-149) + `apply_budget(max_tokens=80_000)` (engine.py:238) bound it → short files can't
  bloat enough to degrade coherence. And the prior report's "#5" is about token COST/caching, NOT
  coherence — repurposing it was a category error (grep: report has zero bleed/monologue/coherence
  hits). | subagent report + cited lines |
  Rules OUT H-S1-FILEBLOAT entirely. Rules IN a key architectural fact: on claude-cli the file I/O +
  monologue + reasoning all accumulate in the **claude SUBPROCESS's own context** during one agentic
  turn — that's the real bleed surface, not brain-side prompt assembly. Red-team's better-supported
  alternative (UNGATED): **write-tool-content-as-imitation** — `propose_write` content re-enters via
  the pending-write surface; the model imitates the FORM of what it just wrote. Appears exactly in
  0.0.38 with the write tool (timeline fits WITHOUT any bloat story).

- **[O21]** Rank-2 caveat (red-team MINOR) | The logged `result_summary` is truncated after rank-1,
  so "confab at rank 2 of the real 16:09 result" is **derived** (deterministic reproduction), not
  directly log-observed. Rank-1 matches the log and ordering is deterministic → high confidence, but
  stated honestly as inferred. |

- **[S1-O14]** USER RECOLLECTION (2026-07-02, UNVERIFIED — to be checked vs git) | The file-content
  bleed did **not** happen, or was far less severe, in an earlier version where Phoebe could
  **directly use Claude Code's own file-editing capability** (native Edit/Write in the claude
  subprocess). User places it "after 0.0.25", removed "somewhere before/around 0.0.38" because that
  direct-edit implementation was "wildly unsafe as implemented" (persona could edit arbitrary files).
  Current path = the gated `propose_write` (added 0.0.38, S1-O11). | user msg 2026-07-02 |
  Rules IN a **natural A/B across the file-write-wiring boundary** that any correct S1 account must
  fit: same underlying model, two file-write mechanisms, different bleed outcomes. STATUS: unverified
  recollection — verify existence/removal-version/mechanism via git archaeology BEFORE building on it
  (2 prior S1 hypotheses died on unverified static assumptions). Archaeology can refine/refute the
  imitation candidate, NOT confirm it.

- **[S1-O15]** USER REFINEMENT (2026-07-02) — degradation is SHARED + DOSE-DEPENDENT, not
  propose_write-exclusive | The intelligence degradation *did* also happen on the old direct-edit
  path, but it (a) took **much longer** and (b) required **much larger files**. So the two file-write
  wirings differ **quantitatively** (threshold), not qualitatively: propose_write hits degradation
  **sooner / on smaller files**. | user msg 2026-07-02 | Rules IN a **dose-response** framing: S1
  (both the coherence decay AND the monologue bleed) is driven by how much accumulates in the
  claude-subprocess context per unit of file work; propose_write loads that far harder than native
  editing did. Recasts the two S1 symptoms as one dose-dependent root. Refutes any "propose_write is a
  qualitatively new bug" framing.

- **[S1-O16]** GIT ARCHAEOLOGY of the file-write-wiring timeline (read-only, no tokens) | Verifies
  S1-O14's recollection + grounds the mechanism contrast:
  · **Old direct-edit path:** claude subprocess ran with `--dangerously-skip-permissions` (537682b)
    and native built-in tools (Edit/Write/Read/Bash) available → persona could directly edit
    arbitrary files ("wildly unsafe", matches user). Native built-ins were `--disallowedTools`-removed
    at **v0.0.31** (`d53776e`, 2026-06-05, "lean CLI — disable unused built-in tools"), locking the
    persona to `mcp__brain-tools__*` only (provider.py:214-234 `_BUILTIN_TOOLS_DISALLOWED` =
    Bash/Read/Edit/Write/Glob/Grep/Task/…).
  · **New gated path:** `propose_write` introduced at **v0.0.38** (`e388c37`, 2026-06-15). Persona
    hand-authors the **full file body** as the `content` arg for every op=create/append/overwrite
    (propose_write.py:35, S1-O1); queued as a PendingWriteCard OR auto-committed to the authorised
    notes folder (propose_write.py:69-85). | git log/tag + provider.py:214-234 + propose_write.py:35 |
  · **Mechanism contrast (the crux):** native Edit reads a file once (cached) and emits a **surgical
    diff** → file body enters context ~once, edits small → context grows slowly (degradation needs
    LARGE files / LONG sessions). propose_write re-authors the **entire body in-voice** every op, in
    the persona's monologue-laden generative context, and a write→re-read→rewrite rework loop repeats
    that → context fills with full-file-sized, persona-voiced content **faster / on smaller files**
    (degradation sooner) AND supplies more monologue-adjacent material to imitate (the bleed). |
  Rules IN: a single dose-dependent driver unifying S1-O15's timeline contrast with the
  H-S1-WRITECONTENT-IMITATION candidate. STILL STATIC REASONING — ungated; a sibling accumulation
  hypothesis was already refuted once (S1-O13). Needs the dose-response behavioural repro to gate.
  (Version nuance: removal was v0.0.31, slightly earlier than the user's "~before 0.0.38"; direct
  edit lived ~0.0.25→0.0.31, a capability gap, then propose_write at 0.0.38.)

- **[S1-O17]** INCIDENT CONVERSATION SIZE (read-only measure of Phoebe's copy — reading only, not
  driving) | `~/Downloads/Phoebe/active_conversations/c30e8b75….jsonl` = **197,348 bytes / 139 lines
  (69 user + 69 assistant + 1 summary) / 30,779 words (~41K tokens est).** The bleed
  peaked DEEP into a substantial session, not from a cold start; ~41K tokens is ~half the engine's
  `apply_budget` 80K cap (engine.py:238) → the near-budget regime. | wc on the file |
  Rules IN **prior-history size as a dose knob** (user, 2026-07-02): seed the repro session with a
  SYNTHETIC history of equivalent length (~69 exchanges / ~41K tok / ~190KB — NOT Phoebe's file) and
  test small-history vs big-history. Cold-start sessions would under-represent the incident's context
  load.

- **[S1-O18]** SMOKE ANCHOR RUN #1 (SPENT TOKENS — real claude-cli via in-process bridge, sonnet,
  throwaway persona "iris") | **Pipeline works end-to-end; verdict NO_BLEED but UNDERPOWERED →
  inconclusive (does NOT refute H-S1-WRITELOAD-DOSE).** Proven positives: positive-control probe
  recalled a history-only fact ("Alden Frost, at Craik Point") → hydration+bridge+claude-cli+auth all
  live; write-gate passed (propose_write auto-committed); all 6 Arm-A turns ran the real
  read_file→record_monologue→propose_write rework loop; the C1-validated detector ran on every
  reply+file. Output was GENUINELY CLEAN (draft_v7 = a well-formed full essay, correct 3rd-person about
  the SUBJECT, no analysis-instead-of-content, no interior leak) — not a detector miss.
  **Why underpowered (representativeness gaps, all pointing one way — the incident's regime was never
  reached):** (1) **compaction NEVER fired** — context stayed under the 80K cap; the incident CROSSED
  it (S1-O17). (2) **Dose barely escalated** — drafts stayed ~1300B and even SHRANK (1308→1261); a
  short personal essay doesn't balloon under "full redraft", so cumulative authored-content (the dose
  variable) never grew large. (3) only 6 live turns on a clean synthetic history → no self-reinforcing
  escalation (the incident escalated "more & more toward the end" of a long REAL session accumulating
  its OWN outputs). (4) model=sonnet (Phoebe's unknown). | anchor_results.json + notes/draft_v*.md |
  Rules IN: the harness is a WORKING, validated behavioural rig (the hunt's long-missing tool), but
  this configuration did NOT reach the bleed-producing regime → **C2 anchor-repro NOT met →
  STOP-FOR-HUMAN** (per plan: do not conclude "no bug"). Next knobs: far bigger seed to cross
  compaction; a GROWING-document task (not a fixed short essay) so authored dose escalates; more turns;
  possibly opus.

- **[S1-O19]** USER OBSERVATION (2026-07-02 morning) + harness corroboration — REPLY LATENCY scales
  with context load, INDEPENDENT of file edits | User noticed Phoebe taking **unusually long to
  reply this morning — several times longer than normal — even on a plain message reply with NO file
  edits.** Independently, harness run #2 throws `claude_cli_idle_timeout` (provider kills a turn with
  no stdout line for 60s, provider.py idle-timeout) on the HEAVY-context turns as the growing doc
  pushes context up. Both point the same way: **latency is driven by accumulated CONTEXT SIZE, not
  file-editing per se** — a plain reply on a big context is slow too. | user msg + run #2 log |
  Rules IN: (a) strengthens the dose/accumulation family (H-S1-WRITELOAD-DOSE) but BROADENS the driver
  from "authored file content" to "total accumulated context" (file writes are one big contributor,
  not the only one — matches S1-O15's "propose_write loads it harder" being quantitative not
  exclusive); (b) **a NEW, cleaner dose-response READOUT: reply LATENCY** (elapsed_s, already logged
  per turn by the harness) as a continuous function of context size — objective and monotonic, vs the
  intermittent bleed. Plot latency (and idle-timeout rate) vs cumulative-authored-bytes / context size
  alongside bleed. Note: observation only (Phoebe not driven — hard rule intact).

- **[S1-O20]** REAL-INCIDENT LATENCY EVIDENCE (read-only analysis of Phoebe's copy) — within-reply
  thinking latency blew up ~10× in the incident window | `tool_invocations.log.jsonl` (2026-07-02, 74
  tool rows / 35 replies, 100% request_id coverage that day). Per-reply MAX inter-tool gap (model
  generation/thinking time between tool calls within one reply): early day (01:xx-15:43) = **0-13s**;
  incident window: **15:56:47 → 79.4s**, **16:00:06 → 93.8s**, 16:09 → 33.9s, 16:33 → 39.4s, 16:38 →
  46.2s. 15:56:47 = the exact 1st Vernon `search_memories` (S1-O2). So latency ~10×'d (single-digit s
  → 79-94s) EXACTLY where the bleed occurred + context was deepest (~41K+, S1-O17). The harness's 60s
  `claude_cli_idle_timeout` sits inside that 79-94s band → the real system was in the same regime the
  harness now hits. | tool log per-request_id spans/gaps | Rules IN: strong corroboration of S1-O19
  (latency scales with accumulated context; the user's "several × longer this morning" is the same
  signal) — **the cleanest, most objective symptom the hunt has found**, and it's continuous +
  monotonic-ish. Honest scope: CORRELATIONAL (incident window ↔ deep context ↔ latency spike ↔ bleep
  co-occur); measures within-reply inter-tool gaps (partial reply latency). The coarse conversation-ts
  gap signal is FLAT (270→275s) + uninformative (shared user/assistant ts folds in user think-time —
  can't isolate reply latency). The CONTROLLED dose-response (latency vs context size, cause isolated)
  is what harness run #2 provides.

- **[S1-O21]** SMOKE RUN #2 (incident-scale ~41.6K seed, growing-doc, 12 turns, sonnet — SPENT TOKENS)
  | **LATENCY symptom REPRODUCED; bleed still NO_BLEED; idle-timeout became the binding cap.** Per-turn
  latency **100-275s** at ~41K context (vs run #1's 57-113s at ~31K) → cross-run, bigger context =
  slower, reproducing the real-incident blowup (S1-O20's 79-94s). Turns 4/10/11 hit `provider_failed`
  (the 60s `_STREAM_PER_EVENT_IDLE_SECONDS`, provider.py:194). Growing-doc dose escalated turns 1-3
  (draft 2.8K→6K→9.3K, cumulative→18.6K) then STALLED: the idle-timeout killed heavy turns 4-11 before
  they wrote (authored=0) → **compaction never fired → still didn't reach the deepest regime**, this
  time because the 60s cap severed the turns. Detector clean throughout. | anchor_results.json |
  Rules IN: (1) the harness REPRODUCES the degradation-as-latency symptom + the idle-timeout at
  incident-scale context on sonnet — the objective symptom is reproduced-on-demand; (2) the bleed is
  NOT yet reproduced, likely the intermittent TAIL past a deeper dose than reached (blocked twice:
  run#1 too little dose, run#2 idle-timeout severed heavy turns before compaction). Next knob:
  monkeypatch `_STREAM_PER_EVENT_IDLE_SECONDS` up (in-process, no brain/ change; justified — the real
  incident's slow replies COMPLETED) so heavy turns finish → dose accumulates → cross compaction →
  chase the bleed tail.
