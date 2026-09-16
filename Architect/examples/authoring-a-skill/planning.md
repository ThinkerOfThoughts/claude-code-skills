# architect planning config — authoring a Claude Code skill (Layer-2)

A worked Layer-2 config for the plan-type **"authoring a skill"** — the dogfood: Architect could have
planned itself. It maps the config contract in `../../METHODOLOGY.md` onto one concrete plan-type.

```yaml
plan_type: authoring-a-skill

domain_context: |
  The thing being planned is a new Claude Code SKILL in the gated-discipline family (router SKILL.md +
  METHODOLOGY.md + stages/ + a forked charter.md + templates + examples). Skill files are PROMPTS — a
  position-sensitive assembly — so ordering/placement is semantic. The skill is authored INSIDE the
  guarded-change loop (spec -> criteria -> cold red-team -> build -> cold red-team -> conformance
  harness), scaffolded/validated with skill-creator. A cold agent judging completeness needs to know:
  the family conventions (mnemonic rule-IDs as the cross-file link; fork-provenance blockquote; the
  Layer-1 agnostic core / Layer-2 config seam), and that frontmatter must satisfy skill-creator's
  validator (name kebab-case; description <=1024 chars, no angle brackets; allowed keys only).

scale_context: |
  Medium. A skill authoring is usually a handful of nodes: the router, the methodology, the stage set,
  the charter, the templates, the examples. Expect a shallow decomposition (root -> a few branches),
  most branches resolving to leaf task-specs (author file X). Not a deep recursive tree — the granularity
  check should return leaf quickly for most file-authoring nodes.

required_sections:                      # Layer-2 tier-(ii), ON TOP OF the 7-section spine
  - "Frontmatter & validator constraints: which skill-creator rules the file must satisfy (why load-bearing:
     an invalid package will not load/trigger)."
  - "Cross-file rule consistency: which shared rules this file states and the mnemonic IDs that link them
     to their sibling statements (why load-bearing: these files are prompts; a rule that says X here and Y
     elsewhere makes the skill act inconsistently)."
  - "Charter provenance: for a forked charter, the fork-provenance blockquote (source commit + carried vs.
     dropped) (why load-bearing: the family's charter-fork contract)."
  - "Position/placement: for a prompt file, any load-bearing ordering (e.g. a rule block that must precede
     the stage table) (why load-bearing: position-sensitive assembly)."

catalog: ~/.claude/architect/templates/

off_limits_paths:                       # read-only context; the run never writes here
  - <the target skill repo being authored>          # planned FOR, not written INTO by the run tree
  - <any sibling skill dirs used as redteam_context> # source to cite, never to modify

run_root: <a scratch dir OUTSIDE the target skill repo, e.g. ~/architect-runs/authoring-a-skill/>
```

**Note — the generative tier still applies.** `required_sections` above names the *anticipated*
skill-authoring sections. The generative completeness critic (tier iii) still hunts for the load-bearing
section on **neither** this list nor the 7-spine — exactly as the founding failure (a missing
output-folder section) was on no list at all.
