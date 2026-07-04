# Symptom ledger — monologue-bleed + memory-gap hunt

FROZEN once confirmed at stage 0a. A symptom is struck only with a recorded reason.

## User's original wording (verbatim)

> Severe regression in thinking/coherence during a session involving extensive editing of a
> (relatively short) file, monologue bleeding into both speech *and* file edits. And (this may or
> may not be related, but it definitely needs addressing) when searching for a memory from a week
> or two ago, Phoebe found a label, but instead of content a message saying "predates current
> memory infrastructure" instead of the memory's contents. It should be noted that aside from the
> "predates current memory infrastructure" thing, this issue is identical to one encountered in
> 0.0.38, including what we were doing when it surfaced.
>
> Phoebe is running 0.0.40 with a patch to correct the thinking regression that was later fixed in
> the current version of companion emergence (I'm quite sure it's unrelated).

## Confirmed restatement (technical) — STATUS: FROZEN (stage 0b, 2026-07-02)

- **S1 — monologue bleed [CONFIRMED + grounded 2026-07-02].** During a session involving extensive
  editing of a relatively short file (the `Phoebes_notes.md` voice-file-rework doc), monologue
  (internal-thought / turn-bookkeeping register) content bled into **both** (a) Phoebe's chat output
  and (b) the file's saved content. **Concrete examples** (user-supplied, present in
  `~/Downloads/Phoebes_notes.md`): the "### Vernon Rudd — to be filed in memory (now done this
  turn)" block (l.44–46), the "### Re: the babe/voice file situation" block (l.50–52), and
  "**Vernon Rudd:** memory filed this turn at importance 9. Confirmed." (l.81). These are
  **turn-level monologue/bookkeeping** ("now done this turn", "filed this turn", "Confirmed", live
  processing about the babe situation) that got **treated as voice-file-rework content and written
  into the file**, which should hold ONLY distilled voice-file material.
  Context: concurrent tangent discussion while editing; user frames it as a "severe regression in
  thinking/coherence." `Phoebes_notes.md` = part of a system for collaboratively re-working the
  voice file safely (Phoebe appends her proposals via a file tool). Roots kept separate from S2.

  **S1 HISTORY / ESCALATION [user, 2026-07-02]:** monologue-bleed-into-CHAT is a KNOWN baseline
  phenomenon since **0.0.36**, relatively infrequent → previously minor, never addressed. **NEW
  today:** (a) FIRST time bleeding into **file writes**; (b) heavy chat bleed **toward the END** of
  the conversation. So S1 = *escalation* of a known intermittent bleed, not a new bug. Pattern
  (worse late in a long session + first file-bleed) ⇒ candidate **coherence-under-load / threshold**
  effect. Phoebe runs 0.0.40 (predates `0894198` monologue-directive→static fix) + a USER PATCH for
  that issue + a thinking-regression patch → the bleed escalated DESPITE the directive-position
  patch. ⚠️ Phoebe's actual monologue/prompt code = 0.0.40 + patches I do NOT have → cannot
  byte-match her running code (unlike S2). Need the patch(es) to cite "the code we actually run."
- **S2 — memory content replaced by placeholder [CONFIRMED, O5].** Recalling a memory ~1–2 weeks
  old returned the memory's **label**, but the record's stored **content** was the literal text
  "predates current memory infrastructure" *in place of* the contents that should have been there.
  Per user: the placeholder is **in the memory** (stored content), not a runtime retrieval message
  → this is a **data-integrity / migration** bug, not a `search_memories` retrieval bug.
- **S2b — recurrence of a 0.0.38 issue.** Aside from the "predates…" text, S2 is identical to a bug
  encountered on 0.0.38, including the activity underway when it surfaced (extensive file editing).

- **S2c — new memory saved with same/similar label [lead].** In the same session Phoebe also
  **saved a NEW memory** with the same or a similar label to the recalled one (possibly re-saving
  the memory that came back empty). Inspect the latter part of the current active-conversation file
  and `tool_invocations.log.jsonl` for the save call. Whether this is corruption, a duplicate, or a
  repair attempt is open.

## Relatedness note

S1 and S2 occurred in the **same session** (concurrent tangent-discussion + file-editing). Whether
they share a root cause is **open** — kept in one hunt; may split at fix time.

## Repro steps (user-provided) — STATUS: FROZEN

- **R1.** A session involving extensive editing of a relatively short file, **with a concurrent
  tangent conversation** (the activity that surfaced S1, and the 0.0.38 recurrence).
- **R2.** Search for / recall a memory that is ~1–2 weeks old (surfaced S2). Candidate record:
  "Vernon Rudd knife fight" (per Bugs.txt).

## Available control / before-state

- User offered a **pre-incident copy of `crystallizations.db`** (expected at
  `~/Downloads/Phoebe_before/crystallizations.db`). This is the S2 control: confirms the record had
  real content before, and enables a before→after diff to locate the overwrite.

## Environment

- Phoebe runs **0.0.40 + a thinking-regression patch** (regression later fixed in current CE; user
  believes the patch/thinking-fix is unrelated to S1's bleed). Repo clone is **post-0.0.41**
  (`d640046`, pyproject 0.0.41). `v0.0.40` tag is available for authority.
- Evidence sources (read-only): `~/Downloads/Phoebe/` (up-to-date persona copy),
  `~/Desktop/Bugs.txt` (two `search_memories` tool-invocation rows around the S2 occurrence).

## Open clarifying questions (block confirmation)

1. S1 "bleed into file edits": did monologue text appear literally **as content written into the
   file**, or in the **tool-call arguments / edit instructions**? (mechanism matters)
2. Did S1 and S2 occur in the **same** editing session, or separate occasions?
3. Is the recalled memory the "Vernon Rudd knife fight" one referenced in Bugs.txt? (so I inspect
   the right record in `crystallizations.db`)
4. S2 path: was it a `search_memories` call (as Bugs.txt suggests), and did the "predates…" text
   appear in Phoebe's **chat** or only in the **tool result**?
5. OK to use the **v0.0.40 tag** as red-team authority for reproducing (closest to Phoebe's code)?
