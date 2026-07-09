# 2 — Plan

## Approach

Append a fifth **Fidelity** lens to the shared charter's numbered list, add one earned-clean
discipline bullet, and update the seven "four lenses" count words to "five" across the skill core
(charter ×2, METHODOLOGY ×1, SKILL ×1, stage-3 ×2, stage-6 ×1).
Then mirror every edited source file into the installed copy and prove sync. No code, no logic,
no measurement instrumentation beyond `git diff` / `grep` / `diff` and one cold-reviewer
enumeration pass.

The design rationale (unconditional 5th lens; append at position 5; count-only cross-doc edits)
is argued in `1-spec.md` "Key design decision" and gated by C3/C4.

## Exact edits (verbatim proposed text)

### E1 — `stages/charter.md`, numbered lens list — append lens 5

After the existing line:

> 4. **Unstated assumptions & risks** — what's being taken for granted that could be false.

add:

> 5. **Fidelity** — does the artifact implement the *mechanism the owner specified*, or a
>    convenient **proxy** for it? Pin each loaded operational term in the spec/request ("agent",
>    "drive", "human", "reproduce", "replace", …) to its concrete mechanism from owner intent; an
>    artifact that substitutes a convenient or pre-existing implementation for that mechanism is
>    **untrusted** until the owner confirms the substitution. A definition inherited from a prior
>    artifact or a **memory note** is a *claim to re-verify against owner intent*, not a spec.

### E2 — `stages/charter.md`, discipline bullets — add earned-clean fidelity guard

Immediately **after** the existing bullet "**A clean *factual* lens must be earned with
citations.** …" (and before "**Spot-verify the citations themselves.**"), insert:

> - **A clean *fidelity* lens must be earned by pinning the terms.** A "no fidelity issue"
>   verdict is valid only if the review **names the loaded operational terms** in the spec/request
>   and, for each, states the concrete mechanism it was pinned to and shows the artifact
>   implements *that* mechanism, not a proxy. A clean fidelity verdict that pins no terms is
>   treated as an un-run review and re-run — the same guard the factual lens carries. Watch
>   specifically for a definition inherited from a prior artifact or a **memory note**: it is a
>   claim to re-verify against owner intent, not a spec.

Placement rationale: groups the two "earned-clean lens" guards (factual, fidelity) adjacently.
Position-lens check: no discipline bullet works *because* of its slot (the set is a flat
rule-list, not a recency/precedence stack), so insertion here displaces nothing behavioural; the
inserted bullet does not sit between a rule and an input it governs.

### E2b — `stages/charter.md`, "Spot-verify the citations themselves." bullet — cover fidelity pins

Per red-team M1: the spot-verify bullet currently only covers "cited file:lines / log rows," so it
does not obviously reach the fidelity guard's evidence (named terms + pinned mechanism). Append one
clause to that existing bullet's final sentence. **Match only the wrap-free fragment on charter L39**
(round-2 caught that a longer quote straddling the L38→L39 newline would not match a literal
find-replace — the same wrap hazard as F1). Change the L39-contiguous string:

> `guard itself must be spot-checked (cheap: verify a few, not all).`

to:

> `guard itself must be spot-checked (cheap: verify a few, not all) — and, for a clean *fidelity* lens, spot-check that the named term→mechanism pins are real: the term appears in the spec/request and the pinned mechanism is the one the owner meant, not a proxy.`

### E3 — `stages/charter.md`, two internal count words

- `~L16`: "The reviewer attacks on **four** **separate** lenses" → "**five** **separate**
  lenses". (Keep the `**separate**` emphasis exactly; only the number word changes.)
- `~L46`: "the METHODOLOGY charter **core** verbatim — the **four** lenses + the unconditional
  discipline" → "the **five** lenses + the unconditional discipline".

### E4 — count word in the other four docs (number word only, nothing else on the line)

- `METHODOLOGY.md` L82: "The **red-team charter** (**four** lenses + discipline + provenance …)" →
  "**five** lenses".
- `SKILL.md` L66–67: "(cold subagent, **four** / lenses, evidence discipline)" → "**five**"
  (the word wraps across the line break; only the number word changes).
- `stages/stage-3.md` L6: "the full red-team charter (the **four** lenses + the discipline …" →
  "**five** lenses".
- `stages/stage-3.md` L15: "Charter it with the **four** lenses + evidence discipline …" →
  "**five** lenses".
- `stages/stage-6.md` L6: "the full red-team charter (the **four** lenses + the discipline …" →
  "**five** lenses".

### E5 — sync to installed copy

Copy each edited file from source → `~/.claude/skills/guarded-change/` (same relative path).
`README.md`, `guarded-change.companion.md`, `changes/` are repo-only and not mirrored.

## Measurement (how the criteria are verified — stage 8)

Pure conformance (no baseline / no numeric metric):

| Criterion | Verification command / method |
|---|---|
| C1 fifth lens present | `grep -nE '^5\. \*\*Fidelity\*\*' stages/charter.md` |
| C2 four elements present | operator rubric over the added E1+E2 text (a,b,c,d locatable) |
| C3 unconditional | inspection: lens in core list; bullet has no "fires only when" clause |
| C4 lens-number tokens byte-unchanged | `git diff` shows no edit inside lenses 1–4 or any `(lens 4)`/"lens 4" token in charter.md **or** stage-3.md |
| C5 positive five + robust no-stale-four | (a) all 7 positive post-strings found (wrap-tolerant; SKILL via portable `tr '\n' ' '\|grep -o 'subagent, five *lenses'`, no `-P/-z`); (b) flatten+strip sweep `tr '\n' ' '\|sed 's/\*\*//g'\|grep -oiE 'four[a-z ]{0,15}lens'` → 0 STALE; **self-test:** same sweep on `git show HEAD:<file>` pre-images must FIRE on all 5 files |
| C6 diff = known spots + charter additions, nothing else | `git diff` hunks = {7 count edits} ∪ {E1 lens entry, E2 fidelity bullet, E2b spot-verify clause} and no other |
| C7 live == source | `diff -r ~/.claude/skills/guarded-change <source> --exclude=README.md --exclude=*.companion.md --exclude=changes` → empty |
| C8 cross-doc rule consistency | `git diff` review: only count words + charter additions changed |
| C9 position/behavior-preservation | C4 + stage-6 cold reviewer enumerates lenses 1–4 & triggers unchanged, + fidelity now present |

## Instrumentation

None to add — `git`, `grep`, `diff` suffice. The stage-6 reviewer's enumeration (C9) is the only
"execution" and is produced by the cold review itself.

## Thresholds (routing)

Standard severity. Blocker (breaks a gating criterion / the loop's own guarantee) → back to spec.
Major (design weakness, e.g. the reviewer argues conditional-vs-unconditional is wrong) → back to
plan. Minor (wording) → fix-and-proceed. Clean → build. Iteration cap: 2 bounces on the same
finding class at a gate → stop for the human.

## Risks / assumptions

- **A1** — Adding an *unconditional* lens raises the cost of every future red-team by one
  term-pinning pass. Accepted deliberately (spec rationale): the failure mode is failure-to-notice,
  so conditionality is self-defeating; the cost is one line for changes with no loaded terms.
  The red-team should challenge this if it disagrees.
- **A2** — Appending at position 5 assumes lens order is non-semantic. Backed by the charter's own
  words ("separate ... so one doesn't crowd out the others"). C4 pins 1–4 unchanged.
- **A3 (corrected after red-team F1)** — The real oracle risk was **under-match, not over-match**:
  a line-based `four…lens` grep silently misses markdown emphasis (`charter:16`) and line-wraps
  (`SKILL:66-67`). Mitigated by the C5 redesign: a **positive per-location** assertion (can't be
  fooled by a missing edit) + a **flatten-and-strip negative sweep** + a **self-test** that the
  sweep actually fires on the pre-change tree and goes silent only when all seven are fixed (a
  stage-8 step). An over-match, if any, is caught by C6 pinning the exact hunks.
