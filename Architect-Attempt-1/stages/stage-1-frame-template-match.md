# Stage 1 — Frame + template-match

**What this stage does:** orient a plan node — state what it plans and at what altitude — and **match
it against the catalog** so the draft either **instantiates a known skeleton** or is marked
**create-new**. Run once per node, before drafting. The top orchestrator also does the run-level setup
here (create the run-root, seed the catalog on first run).

## Procedure

1. **Run-level setup (top orchestrator, first node only).** Create the **run-root OUTSIDE any target
   repo** (config `run_root`), with the layout in `METHODOLOGY.md` ("What a run produces"): `RUN.md`,
   `index.md`, `config/planning.md`, `plan/decisions.md`, `plan/topgate/` (empty), `tree/`. If the
   user-space catalog `~/.claude/architect/templates/` does not yet exist, **seed it** from
   `templates/seed/` and `git init` it (first-run bootstrap — see `templates/seed/README.md`).
2. **Frame the node.** Write, into the node's `plan.md` header, the node's **problem/intent** and
   **altitude** (root / a named branch / a candidate leaf) and the slice of the parent's seams it owns.
   Read the Layer-2 `domain_context` + `scale_context` + `required_sections` so the draft and the cold
   critics share the same picture of what is load-bearing.
3. **Match against the catalog (TPL1).** Compare the node's situation to the catalog skeletons. If one
   **matches**, record `template: <name>` in `index.md` and mark `plan.md` for instantiation at stage 2.
   If **none matches**, record `template: create-new` — the node is planned from the bare 7-section
   spine and, once gated clean, a new skeleton is distilled back to the catalog (TPL2, stage 6).
4. **Never force a match.** A spurious match imports a skeleton whose sections do not fit and seeds a
   hole. When the match is uncertain, prefer **create-new** and let the completeness critic judge the
   drafted result.

## Rules governing this stage

**Match or create, never force (TPL1).** A node either instantiates a genuinely-matching catalog
skeleton or is planned create-new. A forced match is worse than no match — it imports the wrong spine
and hides a gap the generative critic then has to re-discover. The matcher **discriminates**: a
no-match node triggers create-new, not a nearest-neighbour instantiation.

**Seed the catalog on first run (TPL).** The user-space git-tracked catalog
`~/.claude/architect/templates/` is populated from `templates/seed/` on first run and `git init`'d so
back-propagation (TPL3) has an audit trail. The seed set ships in the skill; the live catalog is
user-space so it is reused cross-project.

## Cross-cutting rules

**Run-root OUTSIDE any target repo (RST).** The run tree is created outside any repo the plan targets;
off-limits paths (the target repo, protected paths) are read-only context the run never writes into.

**Disk is the truth (RST).** Everything this stage produces is on disk (`index.md`, the node's `plan.md`
header, the seeded catalog). A restart re-reads them; nothing is held only in chat.
