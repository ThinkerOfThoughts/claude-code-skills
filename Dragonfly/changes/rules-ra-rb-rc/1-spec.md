# 1 — Spec: dragonfly Run 1 — the three owner-dictated rules (R-A, R-B, R-C)

## Source
Memory `dragonfly-next-iter-representativeness-enforcement.md`, section "New RULES to add to the
skill (owner-dictated, 2026-07-08)." This is the **first of two themed dragonfly runs**; Run 2 =
the representativeness-enforcement gaps (result-time gate, test-as-run drift, operator-drift
tripwire) — out of scope here. Companion: the guarded-change **Fidelity lens** shipped this session
(`Guarded_change/changes/charter-fidelity-lens/`, commit 6171c2d); R-C's fidelity element is its
dragonfly-side twin, added to **dragonfly's own** charter (the two skills share no rules — Theme-2
decision — so it is added independently, not referenced).

## The three rules and what each defends against

### R-A — "Assume nothing, verify everything, especially your own claims" (+ memory-as-claim)
Every factual claim about the code, data, or timeline must be **verified against the source** before
it enters a ledger or a conclusion — *including* claims the agent itself just made, and *including*
a definition/fact sitting in a **memory note** that is steering the hunt. Repeated failure in the
motivating hunt: asserting compaction mechanics / version timelines / `propose_write` semantics
from memory, wrong each time; and a memory note's false definition silently drove an instrument's
design. This **strengthens** the existing `B-EVID-1` ("evidence over rhetoric / cite") from *cite*
to *cite-and-verify-against-source, especially your own + memory claims*. It also absorbs **R-C
part 2 (memory notes are unverified claims)** — one rule, not two.

### R-B — Timeline rule: a root cause cannot post-date the symptom
If a symptom exists in the past, its ROOT CAUSE must exist in the past. A feature/code change
introduced **after** a symptom first appeared cannot be the root cause — only an
exacerbating/amplifying factor. Always establish the symptom's **first-appearance** version AND
each candidate factor's **introduction** version; discard as *root* any factor that post-dates the
symptom. Motivating failure: compaction (0.0.40) was inflated as carrier of S1a (pre-0.0.38) twice
before the owner forced the timeline check.

### R-C — Instrument FIDELITY (+ cost-surprise-as-tell)
Three intertwined parts (part 2, memory-as-claim, is merged into R-A above):
1. **Fidelity lens / triage fidelity check.** The triage (`B-TRI-1`) red-teams an instrument for
   correctness/representativeness but never asks *"does this implement the MECHANISM the owner
   specified (per the operational meaning of their terms — 'agent', 'drive', 'human', 'reproduce'),
   or a convenient proxy?"* Motivating failure: "Bob" was built as a stateless headless `claude -p`
   one-shot when the owner mandated an **agent**; it passed correctness review yet was the wrong
   KIND of instrument. Add fidelity as (a) a **5th lens in dragonfly's charter** and (b) an explicit
   **fidelity check in the diagnostic-artifact triage** (loaded operational terms pinned to their
   concrete mechanism at build time; a proxy substitution is untrusted until the owner confirms).
3. **Cost/resource surprise is a TELL, not just a number.** The ~$31 run cost is what exposed the
   Bob mismatch. A surprising resource signal (cost, token burn, latency, call count) must trigger
   *"does my implementation match the intended design?"* — investigate the surprise, don't just
   report it. Home: stage-5 (run & record).

## Design decisions (for the plan to justify, the red-team to challenge)

- **D1 — Fidelity is an UNCONDITIONAL 5th lens** (same rationale locked in the guarded-change
  companion): the failure is *failure to notice a term is loaded*, which is not mechanically
  detectable, so a conditional trigger would recreate the gap. Append at position 5; lenses 1–4 and
  any "lens 4"-style cross-references stay byte-unchanged. (Dragonfly's charter has no numbered
  "(lens 4)" tags like guarded-change did — to be confirmed by grep in the plan.)
- **D2 — R-A strengthens B-EVID-1 rather than replacing it.** B-EVID-1 stays (it is referenced at
  many stages); R-A is a new, distinct rule that raises the bar and is stated once fully (stage-2,
  the ledger-write home) and pointed to where conclusions/rankings are made (charter discipline;
  stages 3, 7). Avoid restating it verbatim at every stage to limit the position-sensitivity surface.
- **D3 — R-B anchored at stage-3, enforced at stage-7.** Forming/ranking hypotheses (stage-3) is
  where first-appearance vs factor-introduction is established; stage-7's depth check ("root or
  relay?") gains a timeline sibling ("root, or a post-dating amplifier?") so a post-dating factor
  cannot be *confirmed* as root.
- **D4 — cost-surprise at stage-5**, where a run's result (and its cost) is recorded.
- **D5 — new rule IDs** (non-colliding with existing B-*/C-*): R-A = `B-VER-1`; R-B = `B-TIME-1`;
  R-C fidelity triage = `B-FID-1`; R-C cost-surprise = `B-COST-1`; the 5th lens is unnumbered like
  lenses 1–4 (it is "lens 5: Fidelity").

## Expected touched files (source `~/Desktop/claude-code-skills/Dragonfly/` + installed mirror `~/.claude/skills/dragonfly/`)
1. `stages/charter.md` — add lens 5 (Fidelity) + its earned-clean discipline guard (mirroring the
   factual-earned bullet); add a fidelity aim to "Diagnosis-specific aiming"; "four→five" at L3 & L21.
   (R-A is author-side discipline, so it lives at stage-2, **not** the reviewer-facing charter — the
   charter's factual lens already covers artifact-vs-source; the fidelity lens already carries the
   memory-note-is-a-claim point for instrument definitions.)
2. `stages/stage-2.md` — add `B-VER-1` (R-A) as the primary cross-cutting rule (ledger-write home).
3. `stages/stage-3.md` — add `B-TIME-1` (R-B: establish first-appearance + factor-introduction;
   discard post-dating factors as root) + a one-line `B-VER-1` pointer.
4. `stages/stage-5.md` — add `B-COST-1` (R-C cost-surprise-as-tell).
5. `stages/stage-7.md` — add the `B-TIME-1` enforcement (depth-check timeline sibling) + a `B-FID-1`
   line in the triage block + a `B-VER-1` pointer.
6. `stages/stage-1.md` — add `B-FID-1` (fidelity check) into the diagnostic-artifact triage; "four→
   five" at L7 & L55.
7. `SKILL.md` — "four lenses"→"five" at L83.
8. `METHODOLOGY.md` — "four lenses"→"five" at L88.

**Count surface (the consistency trap):** exactly 6 "four…lens" sites — charter L3 & L21, SKILL
L83, METHODOLOGY L88, stage-1 L7 & L55 — all → "five". (README/companion state no count → untouched.)

**Not touched:** Run-2 material (rep-gaps); `dragonfly.companion.md` (Layer-2 config); guarded-change
(separate skill). Stage-4 references the charter but states no lens count (verified by grep).
