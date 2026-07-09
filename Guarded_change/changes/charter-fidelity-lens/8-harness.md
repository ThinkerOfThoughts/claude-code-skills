# 8 — Harness (conformance-only; no baseline → no regression arm)

Prompt-doc change, no numeric metric / no stage-0 baseline → **conformance-only**, per CFG5.
Every gating criterion verified by execution on the built tree (base 9c94525).

| # | Criterion (gating) | How verified | Result |
|---|---|---|---|
| C1 | fifth lens present & named | `grep -nE '^5\. \*\*Fidelity\*\*' charter.md` | ✅ charter:23 |
| C2 | lens carries all four elements (a–d) | grep each element in built text (a pin / b proxy⇒untrusted / c inherited-def=claim / d earned-clean) | ✅ 4/4 |
| C3 | unconditional, no trigger clause | grep fidelity lines for "fires only/only when/only where" → none | ✅ |
| C4 | lenses 1–4 + every `(lens 4)`/"lens 4" token byte-unchanged | `git diff` touches no line inside lenses 1–4 or any lens-number token (charter L71/L82, stage-3 L21/L29) | ✅ |
| C5 | all 7 count refs positively read "five" + robust no-stale sweep | (a) 7/7 positive incl. charter:16 bold + SKILL wrap; (b) flatten+strip sweep 0 STALE; self-test: sweep FIRES 5/5 on `git show HEAD` pre-images | ✅ |
| C6 | diff = {7 count edits} ∪ {E1,E2,E2b} and nothing else | `git diff --stat` = 5 files, 23 ins/8 del; non-charter files show only count-word lines changed | ✅ |
| C7 | live == source | `diff -r` installed vs source (excl. README/companion/changes) → exit 0 | ✅ identical |
| C8 | cross-doc rule consistency | only count words + charter additions changed; all docs now say "five" | ✅ |
| C9 | behavior-preservation (position lens), verified by execution | stage-6 cold reviewer enumerated lenses 1–4 + position/concurrency triggers unchanged AND fidelity now present from the built charter | ✅ |

## Self-test evidence (the oracle is not a no-op)
The C5(b) negative sweep run against the pre-change baseline (`git show HEAD:<file>`) FIRED on all
5 files (charter `four separate lens` + `four lens`; SKILL/METHODOLOGY/stage-3/stage-6 `four lens`),
and goes silent only on the fully-fixed tree — proving the gate can actually detect a stale count,
which the round-1 oracle could not for charter:16 / SKILL:66-67.

## Verdict: **PASS — all 9 gating criteria empirically verified.** No advisory criteria; no
regression arm (no baseline). The fidelity lens is live in both the source and the installed skill.

## Note on the change process (self-referential)
This run exercised the very failure the new lens targets in an adjacent form: a build edit
(METHODOLOGY.md) silently did not land on the first attempt, and the mechanical stage-6 diff +
C5's positive-per-location assertion caught it. Reinforces why the C5 redesign (positive assertion,
not just absence-of-"four") was the right call.
