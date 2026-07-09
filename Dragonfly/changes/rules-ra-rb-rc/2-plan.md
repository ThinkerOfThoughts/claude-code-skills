# 2 — Plan (verbatim proposed text)

## Charter edits (`stages/charter.md`)

### E1a — append lens 5 (after "4. **Unstated assumptions & risks** …")
> 5. **Fidelity** — does the artifact implement the *mechanism the owner specified*, or a convenient
>    **proxy** for it? Pin each loaded operational term in the request ("agent", "drive", "human",
>    "reproduce", …) to its concrete mechanism from owner intent; an instrument that substitutes a
>    convenient or pre-existing implementation for that mechanism is **untrusted** until the owner
>    confirms the substitution. A definition inherited from a prior artifact or a **memory note** is
>    a *claim to re-verify against owner intent*, not a spec.

### E1b — earned-clean fidelity guard (after the "A clean *factual* lens must be earned…" bullet, before "Spot-verify the citations")
> - **A clean *fidelity* lens must be earned by pinning the terms.** A "no fidelity issue" verdict is
>   valid only if the review **names the loaded operational terms** in the request and, for each,
>   states the concrete mechanism it was pinned to and shows the instrument implements *that*
>   mechanism, not a proxy. A clean fidelity verdict that pins no terms is treated as an **un-run**
>   review and re-run — the same guard the factual lens carries.

### E1c — fidelity aim (append to "Diagnosis-specific aiming", after "What assumption does the live hypothesis set share…")
> - **Does the instrument implement the mechanism the owner specified, or a convenient proxy?** (the
>   fidelity challenge — the wrong-KIND-of-instrument failure; see B-FID-1)

### E1e — spot-check-the-pins clause for twin parity (per red-team M1)
Dragonfly's "Spot-verify the citations themselves" bullet currently ends (charter L38-40):
> … actually exist and say what's claimed (cheap: verify a few, not all). Citations are the one
> guard defending the loop's founding failure; a fabricated citation would defeat it.

Append to that final sentence (match the wrap-free L40 fragment `a fabricated citation would defeat
it.`):
> `a fabricated citation would defeat it. And for a clean *fidelity* lens, spot-check that the named term→mechanism pins are real: the term appears in the request and the pinned mechanism is the one the owner meant, not a proxy.`

### E1d — count words
- L3: `the four lenses, the discipline` → `the five lenses, the discipline`
- L21: `attacks on four **separate** lenses` → `attacks on five **separate** lenses`

## Stage edits

### E2 — `stages/stage-2.md`, append to "Cross-cutting rules governing this stage" (after B-EVID-1)
> **Verify, don't just cite — especially your own claims and memory (B-VER-1).** Every factual claim
> about the code, data, or timeline is **verified against the source** before it enters a ledger or a
> conclusion — including (especially) a claim the agent itself just made, and a definition or fact
> sitting in a **memory note** that is steering the hunt. Memory is where a convenient-but-wrong
> definition ossifies; a memory-encoded claim that drives a decision is re-verified against the
> source, not trusted because it is written down. This strengthens B-EVID-1 (cite) to
> cite-**and-verify**: an unverified assertion — however confident, however often repeated — is not
> a finding.

### E3 — `stages/stage-3.md`, new section after "The gate-before-present rule", before "Cross-cutting rules"
> ## The timeline rule (B-TIME-1, mandatory)
>
> A root cause **cannot post-date its symptom.** If a symptom exists in the past, its root cause
> exists in the past. So for every candidate: establish (a) the symptom's **first-appearance**
> version/point and (b) the candidate factor's **introduction** version/point — both cited — and
> **discard as *root* any factor introduced after the symptom first appeared.** Such a factor may
> still be an **exacerbating/amplifying** contributor (rank it as one, not as root). Establishing the
> two points is part of forming the hypothesis — a candidate whose timeline is unestablished stays
> `ungated` and may not be ranked as leading.

### E3b — `stages/stage-3.md`, B-VER-1 pointer (append to "Cross-cutting rules governing this stage")
> **Verify, don't just cite (B-VER-1).** A hypothesis's confirm/refute predictions, its ranking, and
> any timeline point (B-TIME-1) are **verified against source**, not asserted from memory — including
> claims the agent just made or ones carried in a memory note. (Full rule at stage 2.)

### E4 — `stages/stage-5.md`, append to "Cross-cutting rules governing this stage"
> **A surprising resource signal is a tell, not just a number (B-COST-1).** When a run's cost, token
> burn, latency, or call-count comes back **surprising** (much higher/lower/different than the design
> implies), treat it as a **fidelity question** — "does my implementation match the intended design?"
> — and investigate the surprise before recording the result as trusted. The surprise is often the
> first evidence that the instrument is the wrong *kind* of thing (see B-FID-1); reporting the number
> without asking why is how a mismatched instrument's readings get consumed. (Motivating case: a ~$31
> run cost exposed a stateless-`claude -p` instrument standing in for a specified agent.)

### E5 — `stages/stage-7.md`, timeline enforcement (append to the "Depth check — root or relay?" paragraph, A-7-4)
> **Timeline sibling — root, or a post-dating amplifier? (A-7-4 / B-TIME-1).** A node cannot be the
> root if it was introduced *after* the symptom first appeared; the stage-7 cold pass challenges the
> claimed root's introduction point against the symptom's first-appearance point (both cited). A
> post-dating node is at most an amplifier — "found" names it as such, never as root.

### E5b — `stages/stage-7.md`, B-FID-1 pointer in the triage block (append after the detector-validation sentence)
> The instrument/toggle also passes the **fidelity check (B-FID-1)** — the mechanism the owner
> specified, not a convenient proxy (full rule at stage 1).

### E6 — `stages/stage-1.md`, B-FID-1 in the diagnostic-artifact triage (append at the END of the triage section, AFTER the C-LITE-1 paragraph, per red-team M2 — so it does not split B-TRI-3 → C-LITE-1)
> **Fidelity check — the instrument the owner specified, not a convenient proxy (B-FID-1).** The
> triage also asks, of every instrument: does it implement the **mechanism the owner specified** —
> per the operational meaning of their loaded terms ("agent", "drive", "human", "reproduce") — or a
> convenient/pre-existing **proxy** for it? Pin each loaded term to its concrete mechanism at build
> time; an instrument that substitutes a proxy (e.g. a stateless one-shot where an *agent* was
> specified) is **untrusted until the owner confirms the substitution**, even if it passes the
> correctness/representativeness review. A definition inherited from a prior artifact or a memory
> note is a claim to re-verify (B-VER-1), not a spec.

### E6b / E7 / E8 — count words
- `stages/stage-1.md` L7: `four lenses + discipline + provenance` → `five lenses + …`
- `stages/stage-1.md` L55: `four lenses + evidence discipline` → `five lenses + evidence discipline`
- `SKILL.md` L83: `four lenses, evidence discipline` → `five lenses, evidence discipline`
- `METHODOLOGY.md` L88: `four lenses + discipline + provenance` → `five lenses + …`

### E9 — sync source → installed for every edited file.

## Measurement (stage-8 conformance)
Per criteria C1–C10. Count oracle C5: positive per-location (6) + robust flatten/strip negative
sweep + `git show HEAD` self-test (must fire on the 4 stale files). Rule presence: grep the 4 new
IDs. Position/behavior: `git diff` shows only additions + count words (no edit inside lenses 1–4 or
existing rule bodies) + a stage-6 cold reviewer enumeration (C8). Sync: `diff -r` (C9).

## Instrumentation / thresholds
None to add (`git`/`grep`/`diff`). Standard severity: blocker → spec; major → plan; minor →
fix-and-proceed; clean → build. Iteration cap 2/gate.

## Risks
- **A1 — count oracle fragility** (Run-0 lesson): naive grep misses markdown/wrap → C5 uses positive
  per-location + robust sweep + baseline self-test.
- **A2 — rule-ID collision**: C6 greps the 4 IDs are absent pre-change.
- **A3 — additive edits displacing a position-load-bearing neighbor**: dragonfly's lens list and
  rule-lists are flat (order non-semantic); C8 pins lenses 1–4 + existing rules byte-unchanged; the
  plan confirms (via the red-team) that no "(lens N)"-style numbered cross-ref exists that appending
  lens 5 would break.
- **A4 — R-A/B-EVID-1 overlap**: R-A strengthens, does not replace; C7 pins B-EVID-1 preserved.
