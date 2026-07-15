# 3 — Red-team the plan (verbatim record)

**Reviewer:** cold `general-purpose` subagent (Claude, this session), agentId `a47a49e3…`, no
shared context with the author. **Duration:** ~246s, 16 tool uses, 73.7k subagent tokens.

**Charter given:** the five-lens red-team charter core (Factual / Logical / Missed-opportunity /
Unstated-assumptions / Fidelity) + evidence discipline + the stage-3 coverage-challenge (CH8) +
label-audit (CH9/CH10) additions + the **position lens** (skill files are a position-sensitive
prompt assembly) + a task-specific instruction to scrutinize the representativeness / causal
toggle of the behavioral criteria. (Full prompt text: see the launch record; charter core is the
METHODOLOGY charter verbatim.)

**Context (closed set):** the 3 artifacts `{1-spec.md, 1.5-criteria.md, 2-plan.md}` + the 6
skill-source files (`stages/charter.md`, `stages/stage-3.md`, `stages/stage-1.md`,
`stages/stage-4.md`, `METHODOLOGY.md`, `SKILL.md`) + the 2 incident files
(`t4-base-loop/{1-spec.md,3-review.md}`). Reviewer-reported sha256 for all 11 recorded at the
end of its output.

**Reviewer-reported context hashes (for spot-check):**
```
99193c71…  changes/owner-ratification-guard/1-spec.md
d746c29c…  changes/owner-ratification-guard/1.5-criteria.md
838b142d…  changes/owner-ratification-guard/2-plan.md
760cd577…  stages/charter.md
48aa7a7c…  stages/stage-3.md
93bedecc…  stages/stage-1.md
4ea889d5…  stages/stage-4.md
0cadca29…  METHODOLOGY.md
092c1c87…  SKILL.md
2a9767c5…  t4-base-loop/1-spec.md
d29ce421…  t4-base-loop/3-review.md
```

---

## Reviewer verbatim output

**Verdict: NOT clean. Worst severity = Blocker.** Recommended route → return to spec/criteria.

### Factual
- **E2 anchor MISMATCH (Major).** Plan quotes anchor as `**fidelity**` (bold); source
  `charter.md:42` is `**A clean *fidelity* lens must be earned by pinning the terms.**` —
  `*fidelity*` is italic *inside* the bold span. A verbatim anchor match fails.
- E1, E3, E4, E5, E6, E7-A/B, E8-A/B, E9/E11 anchors all exist verbatim (cited). ✓
- All incident claims verified: OWNER MUST RATIFY `3-review.md:13`; recorded ruling
  `t4-base-loop/1-spec.md:117`; elaboration `1-spec.md:131-144`; voice ruling `3-review.md:39`. ✓

### Logical
- **L-1 (Blocker candidate → decided in Label audit LA-1).** The C3 precision case contradicts
  RAT1's own bar: the voice ruling `3-review.md:39-40` is a **paraphrase** ("Owner ruled (a):
  accept C-VOICE…"), with **no verbatim options and no verbatim owner response**. A reviewer
  correctly applying new-RAT1 must flag *any* record lacking the verbatim-artifact fields —
  including this one. So C3's required "no finding" and C1's required "flag missing-artifact"
  can't both hold for a consistent reviewer. C3 is non-executable as a precision test as written.
- **L-2 (Minor).** RAT3's "structural enforcement" holds against a *fabricating* orchestrator
  only if there's an independent owner transcript to spot-check against; under delegation the
  "verbatim exchange" CH11 audits is supplied by the same orchestrator → reduces to "orchestrator
  must not lie," asserted not enforced.
- **L-3 (Minor).** re-ask + iteration cap: no livelock, but a second non-disambiguating answer
  hits the cap → human tie-break (correct but undocumented).
- **L-4 (clean).** RAT1 does close FM1 at the charter level; the escalation→record→audit→gate→HIL
  chain is coherent.

### Missed opportunity
- **MO-1 (Major-ish).** The verbatim-owner-words requirement has **no provenance anchor** —
  nothing says where the "verbatim" comes from or how its authenticity is established. Strong
  against *misreading* a real exchange, weak against *fabricating/reconstructing* one (esp. across
  compaction). Better: tie the record to a durable agent-external artifact (transcript line,
  timestamped decisions.md owner entry) so the cold reviewer can spot-verify — same move as the
  charter's "spot-verify the citations."
- **MO-2 (Minor).** Multi-turn owner exchanges unmodeled; "partial answer → re-ask" could
  misfire mid-exchange or cherry-pick the final turn without qualifying context.
- **MO-3 (Minor).** RAT3's orchestrator-half governs an actor that is **not running the skill**;
  a rule in skill files the orchestrator may never load is advisory. Subagent-half (halt-and-relay)
  belongs in the skill and is enforceable; orchestrator-half belongs in the caller's operating
  instructions.

### Unstated assumptions & risks
- **Coverage (CH8): CG-1 (Major)** compaction/provenance sub-mode is sold as a headline benefit
  but no criterion tests a post-compaction re-check. **CG-2 (Minor)** false-positive rate rests on
  the single defective C3 specimen. **CG-3 (Minor)** RAT2 over-flag (a legitimate elaboration
  wrongly flagged) is untested — no precision criterion for RAT2.
- **Position lens: P-1 (Major)** E1 appends a large block *after* the lens's current last
  sentence (`charter.md:28`, the memory-note line), stealing the recency slot and ballooning the
  lens (2→~6 sentences), shifting emphasis from the general term-pinning duty to the ratification
  sub-case — the exact position failure C9 promises to avoid. Re-place. **P-2 (Minor)** CH11/CH12
  after CH10 pushes the section header down. **P-3 (Minor)** E8-B/E9 graft a second "and…" clause
  onto an already-"and"-terminated list → grammatically broken bolt-on.
- **P-4 (clean).** E5, E6, E7-A add named rules into labeled-rule lists — additive, position-neutral.

### Fidelity
- Core mechanisms faithfully implemented (not proxies): non-disambiguation detection; elaboration-
  inflation detection; subagent halt-and-relay. Two residuals: (a) "verbatim owner response" pinned
  to no external source → "ratification" is partly a consistency-proxy (MO-1); (b) RAT3's
  owner-reaching half is asserted, not mechanized (L-2/MO-3). Neither is a proxy-substitution of the
  core mechanism; both are honesty/provenance assumptions the plan should state.

### Label audit
- **LA-1 (Blocker).** C3 demands a clean outcome on a specimen (voice ruling) that itself fails
  RAT1's verbatim-artifact bar → non-executable / trains a rubber-stamp. Fix: precision case must be
  a specimen that actually carries the RAT1 fields (constructed positive), not the voice example.
- **LA-2 (Major).** C1/C2/C14 risk passing on a proxy — a strong base model likely flags this
  self-announcing incident under the *pre-edit* charter (which already carries a strong fidelity
  lens). The plan's causal-toggle note (2-plan.md:251-256) is the right instinct but is only
  instrumentation prose, **not a pass condition**. Promote "pre-edit does NOT flag / flags
  materially weaker" into the C1/C2/C14 pass conditions.
- **LA-3 (Minor).** C14 subagent-half is executable, but its toggle is weakest (pre-edit skill
  already has strong stop-for-human machinery). Orchestrator-half untestable inside the skill.
- **LA-4 (Minor).** C4/C5/C6/C7/C13 (positive per-site assertion + oracle-can-fail) well-labeled
  and executable — no objection.

**Recommended route → return to spec/criteria (Blocker).** (1) Re-specify C3 to a genuinely-
compliant specimen or a constructed positive; (2) promote the pre-edit causal toggle into
C1/C2/C14 pass conditions; (3) fix the E2 anchor quote and re-place E1 so the memory-note sentence
keeps the tail; (4) state the two fidelity residuals (verbatim provenance MO-1/CG-1; RAT3
orchestrator-half MO-3/L-2) rather than claiming structural closure.

---

# Bounce 1 — re-review of the revised plan (verbatim record)

**Reviewer:** cold `general-purpose` subagent, agentId `a563e99c…`, no shared context. ~172s, 16
tool uses, 74.5k tokens. Given the revised `{1-spec,1.5-criteria,2-plan}` + the prior review
(`3-redteam-plan.md`) + the 6 skill sources + 2 incident files; charged to confirm each prior
finding resolved and hunt for regressions. Reviewer-reported context hashes matched the prior
reviewer's on the unchanged skill files (`charter.md 760cd577…`, `stage-3 48aa7a7c…`, incident
`2a9767c5…`/`d29ce421…`) — same source tree.

## Verbatim verdict
**NOT clean, but close. Worst severity = Major (L-NEW-1), confined to plan prose (does not ship).**

**Prior-findings resolution:** LA-1/L-1 (Blocker, C3) RESOLVED — constructed fixtures, voice
ruling demoted to motivating example. LA-2 (Major, causal toggle) RESOLVED — toggle is now the
gating pass-condition, executable via `git show HEAD:` for the pre-edit charter; the
"clarifying-addition-not-behavior-change" honesty carve-out (C14) correctly avoids failing a
strong-but-not-novel guard. E2 (Major, anchor) RESOLVED — matches `**A clean *fidelity* lens…**`.
P-1 (Major, E1 position) RESOLVED — E1 extends the existing `charter.md:28` sentence in place;
lead term-pinning duty intact, lens ~2→~3 sentences, recency slot not stolen, and the deferral
still leaves enough operative instruction (E1 names the concrete audit question). MO-1/CG-1
RESOLVED — provenance + spot-verify integrated. P-3 (grammar) RESOLVED — E7-B/E8-B/E9 insert
into the lists. L-3, MO-2 RESOLVED. MO-3/L-2 PARTIALLY — shipped E10/E11 + C15 softened
correctly, **but the plan Design Summary (`2-plan.md:22-23`) still asserted "Structurally
enforced by RAT1… cannot produce a valid record"** → the one Major.

**New findings:** L-NEW-1 (Major) plan-summary over-claim contradicting E10/C15 → fix in plan
prose. MO-NEW-1 (Minor) real-time ratification has no external artifact at recording moment →
state the live-chat transcript line is an acceptable source; distinguish quoted-owner-words from
author's-reading. LA-NEW-1 (Minor) constructed fixtures are author-built ground truth →
enumerate the fixture's RAT1 fields in the stage-8 record so a mis-built fixture can't silently
pass.

**Recommended route: Major → return to plan** (one-line reconciliation + fold the two Minors);
**no return-to-spec** — spec and shipped edits are sound. "Nothing found that would let an
invalid ratification ship through the shipped skill text." The pre-edit-fails-to-flag claim
remains an empirical claim for stage 8, not confirmable from artifacts alone.
