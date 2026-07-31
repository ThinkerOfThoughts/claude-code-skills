# Example — authoring a skill (worked Layer-2 config)

A **worked example** of an Architect Layer-2 planning config, for the plan-type **"authoring a Claude
Code skill."** It is the **dogfood**: Architect could have planned itself, and the Data-Distiller /
Architect scope records are worked specimens of exactly this plan-type's output. It shows how a
plan-type maps onto the config contract in `../../METHODOLOGY.md`.

## Files
| File | What it is |
|---|---|
| `planning.md` | The Layer-2 config: the `plan_type`, the **domain context** (skill files are prompts; authored inside guarded-change; skill-creator validator constraints), the **scale context** (medium, shallow decomposition), the **required_sections** (frontmatter/validator, cross-file rule consistency, charter provenance, position/placement), the **catalog** pointer, the **off-limits paths** (the target repo, read-only), and the **run_root** (outside the target repo). |

## What this example demonstrates
- **`required_sections` as the tier-(ii) floor** — the anticipated skill-authoring sections, each with
  *why it is load-bearing*, on top of the 7-section spine.
- **The generative tier still bites** — the config note states plainly that tiers (i)–(ii) are the
  floor and the generative critic (iii) still hunts for the section on neither list (the founding
  failure's true shape).
- **Run-root OUTSIDE the target repo** — the run tree is a scratch dir, never inside the skill repo
  being authored; off-limits paths name the repo as read-only context.

## Adapting it to your plan-type
Copy `planning.md`, then: rename `plan_type`; replace `domain_context` with your thing's world (enough
for a cold agent to judge what is load-bearing); set `scale_context` to your expected tree shape;
replace `required_sections` with your plan-type's anticipated sections **each annotated with why it is
load-bearing** (so a cold critic's flag is auditable); point `catalog` at the user-space catalog; list
**your** off-limits paths; and set `run_root` to a scratch dir **outside** any repo you plan for. The
skill's stages read these to frame, draft, complete-critic, adversarially review, gate, decompose, and
assemble.
