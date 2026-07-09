# 3 — Red-team of the plan (verbatim record)

## Provenance
- **Reviewer:** cold `general-purpose` subagent, no shared context (agentId af91e8a4517026445),
  Claude Opus 4.8.
- **Charter given:** METHODOLOGY charter core verbatim (the four lenses in effect at review time +
  the unconditional discipline bullets: cite-or-it-doesn't-count, rank, flag-unverifiable,
  clean-per-lens-allowed, clean-factual-earned, report-hashes) + the stage-3 additions
  (coverage-challenge mandatory, label audit) + the four named design-decision challenges. Full
  prompt archived in the run transcript (Agent call preceding this record).
- **Context list (closed set):** the three change artifacts (1-spec, 1.5-criteria, 2-plan) +
  the skill source being edited (stages/charter.md, SKILL.md, METHODOLOGY.md, stages/stage-3.md,
  stages/stage-6.md, stages/stage-1.5.md) + tree-wide grep of the repo. Paths validated (decisions.md).
- **Reviewer-reported reads (sha256, abbrev):** charter.md 6b98164d…5dcaf8; SKILL.md e6641d12…92d1fe;
  METHODOLOGY.md 095c8eca…9641cde; stage-3.md 6aa67d67…b42c568b; stage-6.md 550a7b6e…dccef1;
  stage-1.5.md d262a147…e5e4bd66. Installed mirror confirmed `diff -r`-clean vs source at review time.

## Verdict: **BLOCKER** (route back to fix criteria/plan)

### FACTUAL — clean except one BLOCKER
All seven count-word locations, the E1 anchor (charter L22), and the E2 insertion point verified
exactly as the plan claims. README.md / companion.md confirmed to contain zero lens/count refs
(spec "not touched" claim correct). Touched-file list complete.

**BLOCKER F1 — the C5 verification regex cannot detect a stale `charter.md:16`.** C5's grep
(`four .{0,4}lens\|four separate lens` in 1.5 L31; `four[^.]{0,6}lens` in plan L84) fails to match
`four **separate** lenses`: the span between `four ` and `lens` is 13+ chars (` **separate** `),
exceeding both length bounds, and the `**` bold markers defeat the `four separate lens` literal
branch. A build that fixes the other six count words but forgets charter:16 → **C5 returns 0 hits
and PASSES**, certifying a tree that still says "four **separate** lenses" — the single
most-emphasized target of the change. C6 (git-diff hunks) is only a partial, human-judgement
backstop, not the mechanical gate C5 advertises. Fix: broaden the regex to tolerate markdown/longer
spans, OR assert the positive post-state ("five **separate** lenses" present at charter:16).

### LOGICAL — MINOR
**L1** — plan-table row for C6 (L85) drops the "(plus charter list/bullet additions)" parenthetical
that 1.5 L36 has; an operator reading only the table could over-tighten and false-fail. Cosmetic.
Sequencing otherwise sound.

### MISSED-OPPORTUNITY — MINOR
**M1** — the new fidelity earned-clean bullet is inserted before "Spot-verify the citations
themselves," which only speaks of "cited file:lines/log rows" and does not obviously cover the
fidelity guard's "named terms + pinned mechanism" evidence. Cheap completion: extend spot-verify to
name the fidelity pins as spot-checkable too. Low value, not spec-required.
**M2** (advisory, not a defect) — design is well-aimed: the Bob failure was a stage-6-shaped
(built-instrument) failure and the lens correctly runs at both stages.

### UNSTATED-ASSUMPTIONS & RISKS (incl. coverage challenge)
- **Decision 1 (unconditional):** sound; the "failure to notice a term is loaded" argument is
  correct and the noise cost is honestly disclosed (A1). No underweighted downside. CLEAN.
- **Decision 2 (append at pos 5 / order non-semantic):** verified true — charter L16 states the
  lenses are a flat set; the only numeric refs are `(lens 4)` tags (charter L56/L67, stage-3
  L21/L29) which all point at lens 4 and are unaffected by appending lens 5. CLEAN.
- **Decision 4 (four elements delivered):** all of (a) pin terms, (b) proxy⇒untrusted, (c)
  inherited-definition-is-a-claim, (d) earned-clean present in E1+E2. No gap.
- **Coverage gap G1 (MINOR)** — no criterion observes stage-3.md's `(lens 4)`/"lens 4" tokens
  (L21/L29); C4 only guards the `(lens 4)` tags *in charter.md*. Untouched by this change → risk
  theoretical, hence MINOR, but unobserved.
- **Coverage gap G2 (MINOR)** — no gate positively asserts "charter:16 now reads five"; C7
  (live==source) and C5 can both be green on a tree where charter:16 never changed. Same root as
  F1; a positive post-state assertion closes both.
- The plan's stated risk A3 reasoned about the wrong failure direction (worried the grep is too
  greedy; the real defect is it's too strict for markdown).

### LABEL AUDIT
All nine criteria labelled gating; none dodged to advisory (legitimate reason given). But **C5's
verification is a proxy that never triggers on its key input class** (charter:16) — the exact
CH9 "verified against a non-triggering input" pattern → C5 not validly verifiable as written until
the regex is fixed. C6 is a git-diff review, not the mechanical gate; should not silently cover C5.

## Author spot-check of the review (charter consumer duty CH6)
Independently reproduced the core claim: `printf 'four **separate** lenses' | grep -niE
'four[^.]{0,6}lens'` → **NO MATCH** (C5 blind, confirmed). Also found an implied **second** blind
spot the reviewer's logic entails: SKILL.md:66-67 wraps `four`\n`lenses` across a line, so a
line-based grep misses that location too. Both real. Findings accepted.

---

# Round 2 — re-review of revised criteria/plan (verbatim record)

## Provenance
- **Reviewer:** cold `general-purpose` subagent, no shared context (agentId a17d2bb9e1c36c87b),
  Claude Opus 4.8. Charter: four lenses + discipline + mandatory coverage-challenge; focused on
  verifying the round-1 fixes (C5 redesign, C4 broaden, E2b) actually hold + anything newly broken.
- **Context (closed set):** revised 1.5-criteria.md, 2-plan.md, 1-spec.md, the round-1 record
  3-redteam-plan.md, + skill source (charter/SKILL/METHODOLOGY/stage-3/stage-6). Paths re-validated.

## Verdict: **MINOR** (fix-and-proceed — no bounce)

Round-1 BLOCKER **genuinely closed**: reviewer independently built stale trees for BOTH hard cases
— charter:16 `**separate**` emphasis and SKILL:66-67 `four`/`lenses` wrap — and confirmed *both* C5
halves catch each; `{0,15}` correctly sized (widest real gap `separate ` =10); positive+negative
halves complementary (cover the mangle-vs-revert gap); C4/C6/C8 internally consistent; enumeration
complete (no 8th count reference; the old broken regex survives only in the round-1 record,
correctly). Round-1 G1/G2 confirmed closed.

Three MINORs, all fixed in-place this pass:
- **MINOR (factual) — E2b "before" quote straddles the L38→L39 wrap** → a literal find-replace
  would not match (ironically the same wrap-hazard class as F1). **RESOLVED:** E2b now targets only
  the L39-contiguous fragment `guard itself must be spot-checked (cheap: verify a few, not all).`
- **MINOR — C5(b) self-test not operationalized as a command.** **RESOLVED:** criteria + plan now
  give the explicit `git show HEAD:<file>` pre-image invocation and require the sweep to FIRE on all
  five baseline files.
- **MINOR — `grep -Pzo` GNU-portability unstated** (load-bearing for the SKILL wrapped check).
  **RESOLVED:** replaced with a portable `tr '\n' ' ' | grep -o 'subagent, five *lenses'` (no
  `-P/-z`), verified 0 pre-build.

## Author verification of the fixes (charter consumer duty)
- charter L36-39 `cat -A`: confirmed the spot-verify sentence wraps L38→L39; E2b retargeted to the
  L39-only fragment (contiguous).
- Portable SKILL check: `tr '\n' ' ' <SKILL.md | grep -o 'subagent, five *lenses'` → 0 now (→1
  post-build); same technique reads the current wrapped `subagent, four lenses`. Verified.

Design decisions 1 (unconditional) & 2 (append pos 5) remained CLEAN in round 2 → frozen.
