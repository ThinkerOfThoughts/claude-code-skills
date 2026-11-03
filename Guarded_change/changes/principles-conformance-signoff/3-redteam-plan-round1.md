# Stage-3 red-team, round 1 (record; CONDENSED by the runner)

Disclosure: the reviewer's full output was about 250 lines. This record keeps its header facts and its complete ranked finding
list verbatim in substance; the five lens bodies are summarised, not copied. The full text was in the runner's turn only.

- Charter given: `stages/charter.md` (sha256 1f8beb8b306a4b88) and `stages/stage-3.md` (1a3ca877dc4ea823), read in full by the
  reviewer, plus the up-front five-lens + coverage-challenge + label-audit shape and the position/HIST instructions.
- Context list (closed set): `1-spec.md` (ee6a095dff71bbdd), `1.5-criteria.md` (8f7ac4a1a4385ef0), `2-plan.md` (ddb7b885ff3e47f8),
  `stages/{charter,stage-2,stage-3,stage-4,stage-6,stage-1,stage-1.5,stage-7,stage-8}.md`, `SKILL.md`, `METHODOLOGY.md`,
  `guarded-change.companion.md`, `README.md`. The reviewer also read the principles sheet of the oracle project on its own
  initiative; that read is outside the closed set and was not relied on for any finding.
- Reviewer: general-purpose subagent, model sonnet, foreground (`run_in_background: false`).

## Reviewer's ranked findings
Overall: no blocker; five majors.
1. major: criteria lack an executed behaviour-preservation criterion for adding a large bullet to a position-sensitive assembly
   (ST1.5d); C4 was diff/grep only.
2. major: C5 is not a representative proof (facts file replaces discovery; runner/reviewer roles mixed in the replay; n=1; no
   negative control; stage 6 unexercised; toggle confounded).
3. major: the conformance bullet names owner decisions the closed input set does not contain, and the spec is not a stage-6 input.
4. major: the MAJOR floor on every entry over-fires and conflicts with the severity model's "materially wrong approach"; no
   "different job" carve-out; floor, per-entry form and mechanism table are unratified elaboration (RAT2).
5. major: C1-C4/C6 proof homes were "reading and grep" for a prompt artifact, with no command, expected output or known-bad
   self-test.
6. minor: search scope limited to `redteam_context` + touched files; the shared module may be neither.
7. minor: bullet unconditional but placed in the conditional block and unnamed in the provenance composition sentence.
8. minor: "what this stage adds" intro lists and SKILL.md table rows not updated.
9. minor: applicability to post-6 checks and harness arms undefined; "answer" in the owner's words dropped without saying so.
10. minor: `principles_context` shape unspecified; config sources vs the fidelity lens's memory-note distrust unreconciled;
    escalation/invariant entries not covered by "principle, default and ruling".
11. minor: C6 and C3 greps unfalsifiable or failing against pre-existing text.
12. minor: the bare-`unlink` claim is untestable under the facts file; "and/or" masks it.
13. minor: "or any verdict that does not route the artifact back" circular; "un-run for it" ambiguous (section-only vs full re-run).
14. minor: installed-copy sync step missing from the plan.
15. nitpick: charter.md header "Verbatim from METHODOLOGY" stale (pre-existing).
Ratification note: the owner's ruling is quoted with a timestamp but its durable source is the requester's task statement,
which the reviewer cannot see: unverifiable-source, not invalid.
