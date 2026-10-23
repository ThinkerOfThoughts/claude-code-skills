# Template catalog — seed set + the skeletonize / match / reuse / back-propagate mechanism

This folder is the **seed skeleton set** that ships with the skill. On **first run**, it populates the
**git-tracked user-space catalog** `~/.claude/architect/templates/` — the live catalog every run reads
and writes. User-space → **cross-project reuse** (a skeleton distilled from planning project A is
available for project B). Git-tracked → **audit trail + revertible back-propagation**. (TPL)

## The mechanism (Layer-1 core; the catalog *content* is Layer-2 data)

1. **Skeletonize.** A skeleton is a reusable, pre-shaped instance of the 7-section spine (SPN) for a
   recognizable planning situation — the section headings plus prompts for what each must contain for
   *that* situation. Skeletons carry no project specifics; they are shapes, not filled plans.
2. **Match / instantiate (TPL1).** At stage 1 a node is compared to the catalog. A genuine match →
   instantiate that skeleton into the node's `plan.md` and record `template: <name>` in `index.md`.
   **Never force a match** — an uncertain match is planned **create-new** instead (a forced match seeds
   the wrong spine and hides a gap).
3. **Create-new (TPL2).** A node matching no skeleton is planned from the bare spine; once it is **gated
   clean** (both cold passes clear), a **new skeleton** is distilled from it and committed to the
   user-space catalog — so the next project inherits it.
4. **Back-propagate (TPL3).** When a plan-fix patches a hole in a node that came from a skeleton, the
   **same fix is applied to the skeleton** and committed to the user-space catalog — a real
   **`git commit`** in `~/.claude/architect/templates/`, not an in-memory or run-local note. This is
   guarded-change-on-itself self-improvement: a hole caught once is not re-drafted into the next project.

## First-run bootstrap

If `~/.claude/architect/templates/` does not exist, the top orchestrator (stage 1) copies this seed set
there and runs `git init` so back-propagation has a history. The seed set is intentionally small and
generic; real catalogs grow via create-new (TPL2) and back-propagation (TPL3).

## Seed skeletons in this set

| File | Situation it shapes |
|---|---|
| `generic-node.md` | Any interior plan node — the bare 7-section spine with per-section prompts |
| `decomposition-node.md` | An interior node that **decomposes** — spine + a named children-and-seams block |
| `leaf-task-spec.md` | A **leaf** — the spine collapsed to an atomic, agent-executable task spec |

Each is a **starting shape** the completeness critic still reviews — instantiating a skeleton does not
skip a gate; it gives the draft a whole-looking spine that the generative critic (tier iii) still probes
for the section *no* skeleton anticipated.
