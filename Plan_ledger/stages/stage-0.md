# Stage 0 — Setup

1. **Config.** Find `plan-ledger.*.md`. Validate every path in it (invariants_path, ledger_dir,
   adjacent_goals, inherited_stores, build hand-off). Dead path → stop and ask. Record the validation in
   the ledger's Decisions log.
2. **Invariants doc.** Open `invariants_path` in full. If absent: seed it from `stages/invariants-template.md`
   using only rulings you can quote (owner words + timestamp/source per line), mark the file
   `status: FOR OWNER REVIEW`, and tell the owner. An unreviewed invariants doc blocks stage 6, not
   stages 1-5.
3. **Ledger.** Create `<ledger_dir>/<slug>-LEDGER.md` from `stages/ledger-template.md`. Set
   `status: ACTIVE`, sheet version 0, a fresh random hex Secret token. Record the owner's name as
   configured (used in the `[OWNER …]` tag; `owner_tag` in config).
4. **Inherited stores.** For every entry in `inherited_stores` that the work will touch, add a ledger
   line tagged `[INHERITED:<where> | UNEXAMINED]` now, before any design talk. This is what turns "the
   table already exists" into a decision that must be posed (stage 2) instead of an accident.
5. **Adjacent goals.** Read each `adjacent_goals` entry (a doc, issue, or ruling that states WHY a
   neighbouring piece of work exists). Summarize each in one sentence in the ledger's Adjacent goals
   section with its source. Stage 5/6 agents check the spec against these; a spec that quietly
   optimizes against a neighbour's goal (e.g. "keep this PR disjoint" defeating "one database") is a
   finding.
6. Tell the owner the ledger path and the Secret token in one line. Proceed to stage 1.
