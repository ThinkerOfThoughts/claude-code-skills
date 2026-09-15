# plan-ledger config — companion-emergence (Layer 2)

Per-project config for the `plan-ledger` skill. See `~/.claude/skills/plan-ledger/METHODOLOGY.md` for the
contract.

```yaml
project: companion-emergence
owner_tag: OWNER
invariants_path: "~/.claude/plans/companion-emergence-DESIGN-INVARIANTS.md"
ledger_dir: "~/.claude/plans/"

inherited_stores:
  - path_or_name: "embeddings.db / embedding_cache (content_hash PK)"
    note: "Pre-existing content-addressed vector cache from the original substrate; served ingest dedup. Any reuse for per-memory attributes is a fork, not a given."
  - path_or_name: "hebbian.db / hebbian_edges"
    note: "Separate file from memories.db; scheduled to fold INTO memories.db. Do not design new work around its being separate."
  - path_or_name: "memories.db emotions_json column + monologue_emotion / self_model_reconcile rows"
    note: "Two overlapping emotion representations; a cleanup issue governs their shape. Do not add a third."
  - path_or_name: "tunables.py"
    note: "USER-facing tunables; physiology constants are fenced out of it. The DEV-facing prompt/constants file is a separate surface."

adjacent_goals:
  - source: "issue #128 and the memory-rework umbrella"
    goal: "One memories database: hebbian associations fold into memories.db because separate DB files have proven fragile across VM moves."
  - source: "issue #259"
    goal: "A per-memory attribute (e.g. an embedding) is stored on the memory row or a memories-side table keyed by memory id, never in a content-hash side file."
  - source: "issue #250 and the owner's standing view"
    goal: "Behaviour thresholds are derived or self-calibrating; a hardcoded empirical constant is a defect to be tracked, not a finished answer."
  - source: "issues #222 / #224 (P4 Stage 1)"
    goal: "Emotions and journal leave memories.db into their own small bounded stores; memories.db holds genuine memories and their associations."

redteam_context:
  - path: "~/Desktop/companion-emergence/brain"
    note: "Repo checkout at origin/main. Verify currency (git rev-list --left-right --count HEAD...origin/main = 0 0) before trusting a read; the shared working tree has drifted before."
  - path: "~/.claude/plans/memory-dream-rework-PLANNING-plan.md"
    note: "The phase plan of record; prior rulings live here with dates. A claim about a prior ruling must be quoted from it, not recalled."

build_handoff:
  lane: "the Fixing session (a peer, not a subordinate: spec deltas with line references, milestones only)"
  guarded_change_config: "~/Desktop/claude-code-skills/Guarded_change/guarded-change.companion.md"

models:
  cold_agents: sonnet
```

## Notes specific to this project

- Persona-facing strings are the owner's byte-exact call and must be free of LLM tells (no em-dashes);
  they are finalized at the end of a build, not mid-design.
- Never drive the live persona as a test fixture; synthetic users are named in the harness notes.
- The working tree used by spawned readers has been stale before; point code reads at `origin/main`.
