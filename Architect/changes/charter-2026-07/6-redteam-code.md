# Stage 6 — Red-team the built artifact (RECORD)

**Run:** `charter-2026-07`. Cold review of the **shipped** `Architect/stages/charter.md` (v1, 215 lines,
sha256 `523bf3a24b9a1279790473ffb5d5904a74424d9cacf2800f2f657baffc446085`) against the frozen criteria and
the stage-0 baseline.

## Provenance elements

**(i) Verbatim charter/prompt given** — `records/stage6-prompt.md`, sha256
`5f7819ae546338130a10eea7887e5ef672189e59f6585fb890a1907d2a9a4358` (as reported independently by all three
reviewers). Byte-identical to all three; written to disk first, each reviewer told only to read that path
and execute it. Embeds the guarded-change charter core verbatim, the stage-6 additions quoted as such, and
the mechanical-diff duty.

**(ii) Exact context list given** — 12 paths, listed in the prompt.
⚠ **B15 SUPPLEMENTARY-CONTEXT DECLARATION, quoted as the rule requires.** Two of those paths —
`Guarded_change/stages/stage-3.md` and `Guarded_change/stages/stage-4.md` — are **not** among the config's
8 `redteam_context` entries. They were supplied because the charter **ports RAT1/RAT2 from the first and
SEV2/SEV3 from the second**, and a reviewer asked to check port fidelity cannot do so without them.
**Reviewer G caught this and filed it (G-F8)**, correctly noting it is the second occurrence of the pass-2
E-F7 violation. This paragraph is the remedy the rule itself prescribes. Recorded as **OOS-8** for element 3.

**(iii) Reviewers' verbatim output** — **ON DISK, RECOVERED FROM THE HARNESS.**

| Reviewer | Record | Chars |
|---|---|---|
| G | `records/reviewer-G-verbatim.md` | 37,641 |
| H | `records/reviewer-H-verbatim.md` | 34,443 |
| I | `records/reviewer-I-verbatim.md` | 22,218 |

Extracted programmatically — **no re-typing** — from each subagent's own harness-authored transcript. The
command, so the next reader can reproduce it:

```
$ SUB=~/.claude/projects/-home-zero-…-b40a0c/45cb99a2-…-0775.jsonl-dir/subagents
$ python3 - "$SUB" <<'EOF'
  for tag,aid in [('G','aa4584fe421867261'),('H','a0a626c73c9c20523'),('I','af12e4dbc5ca35524')]:
      meta = json.load(open(f'{sub}/agent-{aid}.meta.json'))
      # last assistant message with text content in agent-<id>.jsonl
EOF
G: 37641 chars  model=opus    parent=a415bc52b9d9f3550  depth=2
H: 34443 chars  model=opus    parent=a415bc52b9d9f3550  depth=2
I: 22218 chars  model=sonnet  parent=a415bc52b9d9f3550  depth=2
```

> **A FINDING AGAINST THIS RUNNER, and it generalises past this run.**
>
> An earlier version of this record declared element (iii) unsatisfiable because the three reviews "returned
> inline and were not persisted". **That was false. The full transcripts were on disk the entire time** —
> 528KB, 570KB and 645KB — written by the harness under `subagents/`, alongside a `meta.json` sidecar each.
> The runner declared a review **un-run without checking whether the record existed**.
>
> The generalisable defect: **this family has treated a subagent's inline return as the only copy of its
> output for its entire history.** The charter's provenance rule requires verbatim output but says **nothing
> about where verbatim output is recovered from** — and "verbatim" is unenforceable if nobody knows the
> transcript exists. A record can be lost to a truncated return, a context compaction, or a runner that
> simply forgets, and under the current wording the loss looks irreversible when it is not.
>
> **Disposition:** recorded here, and carried to the **router/methodology elements (4 and 5)** rather than
> patched into the charter now — the criteria are frozen, and the charter is reviewer-facing while this is a
> duty of whoever *assembles* the record. **Recorded as OOS-9.** It is a better finding than the one
> originally filed, and it was produced by being told to check rather than by being told the answer.

**(iv) Reviewer agent type + model — now FIRST-HAND, not reviewer-reported**

Read from the harness's own `agent-<id>.meta.json` sidecars, not from the agents' say-so:

| Reviewer | agentType | model | parentAgentId | spawnDepth | Worst severity |
|---|---|---|---|---|---|
| G | `general-purpose` | **opus** | `a415bc52b9d9f3550` | 2 | major |
| H | `general-purpose` | **opus** | `a415bc52b9d9f3550` | 2 | major |
| I | `general-purpose` | **sonnet** | `a415bc52b9d9f3550` | 2 | **blocker** |

**This is the audit surface dogfood F9 said "3 independent cold agents" did not have.** F9's finding was
that for same-model agents four of the five provenance fields are identical and the fifth is producible by
asking one agent three times — so the mandate had no way to be checked. The sidecars close it: all three
name **the same parent (this runner) at depth 2** with **three distinct agent ids** and **two distinct
models**, none of it self-reported. "Three separately-spawned subagents" is now a **verified fact rather
than an assertion**, and F9's own prescribed fix — a spawn-identity field per record — turns out to have
existed in the harness all along.

## Independent verifications all three performed

- **Banner absent** — the config's stage-6 discriminator. All three confirmed they held the run's output,
  not the draft. Reviewer I additionally ran `git show HEAD:Architect/stages/charter.md` and confirmed the
  committed version is still the banner-carrying draft, so the shipped charter is the uncommitted change.
- **Frozen criteria unchanged** — all three computed `1df324c0…918912c` and matched it against the freeze
  value recorded in `decisions.md`. **No post-freeze drift.**
- **Fork-source identity** — G re-ran `git show 8d73e5d:… | sha256sum` and matched `0e73bacf…adc590`, 103
  lines.
- **Owner quotes** — G spot-verified 4, H spot-verified 6, I read 16 transcript records. **All reproduce
  verbatim. Zero fabricated citations across all three.**

## Regression check vs B01–B19 — MET, verified 3/3

Every CARRY/CHANGE rule still stated; the single declared DROP named as dropped in the provenance
blockquote; **no rule in a silent third category**. This is the criterion the unvetted draft failed.
Qualification (H): B13 was *stated but narrowed* — presence-checking would have scored it green, which is
precisely the failure mode the baseline names for B19. **Repaired at gate 7.**

## Audit of the deliberate reduction — honest, 3/3

All three checked whether anything was reported as verified that was not. `oracles/` and `fixtures/` are
empty, `8-harness.md` does not exist, and **no document claims any criterion passed**. H: *"the cut is
disclosed in three independent places … This is disclosed, not hidden."* One exception found: the
`origin.kind` block ships unverified and was not on the disclosed list (G-F1) — now added to it.

## Union of findings (nothing discarded)

**BLOCKER — I-F1.** The closed-set clause read as if the split reviewer receives a plan; `Divisible` is
2-arg and never gets one, and C-11 forbids exactly that assertion (rejected 3/3 at gate 4).

**MAJOR.** Closed set unbounded, defeating B15's supplementary-context guard (**G-F2/H-F3/I-F2, 3/3**) ·
`Union` granted a severity-override the spec does not define, an unratified inflation by the charter's own
RAT2 (G-F3) · earned-clean fidelity dropped B13's elaboration-trace (H-F1) · demotion rule's "logged entry"
names no destination (G-F4/H-F2, 2/3) · RAT1's durable-source rule silently narrowed vs. `stage-3.md` L59
(I-F3) · the `origin.kind` block has no frozen criterion (G-F1).

**MINOR / NITPICK.** Blockquote CHANGED list vs. intent table (G-F5/H-F5, 2/3) · spot-verify sample vs.
universal consequence (H-F4) · precision clause removed from its former adjacency (G-F6) · RAT1/RAT2 ship
unconditional (H-F6) · `Ask_human` primitive without a call site (H-F7, **cap item, not looped**) · floor
exemplar deleted (H-F8) · "Return a verdict for each" un-asked-for (H-F9/I-F5) · B17's ranking clause
dropped while B16's kept (G-F7) · `origin.kind` described as two-valued (G-F9) · human-gate locus phrasing
(G-F10) · R-6 mapping covers the third option by inference (I-F4) · no mutant shape for "broaden a
conditional clause" (I-F6).

## Worst severity: **BLOCKER** · Route: **→ stage 5, rebuild**

Repairs applied in place; see `decisions.md` gate-7 entry for the finding→repair table and
`records/build-diff-v2.txt` for the resulting diff. **Charter v2: 237 lines, sha256
`1c8c1bd0620d041d5e3cfeda8a314aba4412de5d3dff5ba7d10f1aa763424112`.**

**A targeted re-review of the repaired clauses is owed before gate 7 closes clean.** The repairs touched
the closed set, the `Union` bullet, the fidelity gate, RAT1's durable-source rule and the demotion rule —
none has been cold-reviewed in its repaired form, and H6's "an unreviewed check is not a check" applies to
repairs as much as to instruments.
