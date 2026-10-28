# B6 fixture — what it exercises, and the residual surfaced to the orchestrator

B6 has three sub-claims. What a single-process conformance dry-run can and cannot exercise:

## (1) Restart contract — VERIFIED mechanically (`run/tree/`)
- branch-A has ALL deterministic outputs (`plan.md` + `completeness/{A,B,C}` + `adversarial/{A,B,C}`)
  → on restart it is **skipped, not re-planned** (stage-done-iff-output-exists).
- branch-B is interrupted mid-adversarial-stage (`adversarial/` outputs ABSENT) → on restart that
  stage **re-runs fresh**.
- The restart walk (emulated in the harness) resumes at branch-B and leaves branch-A alone — the
  contract **discriminates** done from not-done (oracle-can-fail twin: an ABSENT-output node DOES
  re-run; a complete node does NOT). Trust-files-over-cursor + node-identity=dir-path.

## (2) Context economy at the DISPATCH CONTRACT — VERIFIED representatively (`dispatch-manifests/`)
- The parent hands each sub-orchestrator only its OWN subtree skeleton + the inter-branch seams +
  child `_status` roll-ups; each manifest EXCLUDES the sibling's internal detail and the whole tree.
- Enlarging sibling branch-B (2 → 200 internal nodes) leaves sub-orch A's handed input set
  **byte-for-byte unchanged** (content diff empty) → held context scales with own-subtree breadth,
  not total tree size (ECON), measured at the delegation boundary.

## (3) TRUE live cross-process context isolation — NOT EXERCISED by this harness (residual)
The criterion's literal claim is about each spawned (sub-)orchestrator's **working context** during
live recursive execution — that a really-spawned sub-orchestrator's context window physically holds
only its own subtree while it runs. Verifying THAT requires spawning real recursive sub-orchestrator
agents and introspecting their live context mid-run; a single-process conformance dry-run represents
it only by the **dispatch-contract input set** (part 2), which is the parent's *intent*, not a
measurement of the child's running context. This is the "B6 cross-process context isolation" item
pre-routed at gate 4 and re-flagged at gate 7 as a candidate stop-for-human if the dry-run cannot
verify it pre-ship. It is surfaced verbatim to the orchestrator in `8-harness.md`, not self-accepted
and not silently deferred (RAT3 / CP5).
