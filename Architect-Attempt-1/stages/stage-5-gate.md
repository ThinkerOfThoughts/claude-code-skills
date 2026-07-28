# Stage 5 — Gate (route the node)

**What this stage does:** route a node by the **worst finding across both cold passes** (completeness +
adversarial), record the decision in `plan/decisions.md`, and enforce the **gate-before-present**
precondition and the **gate-bounce cap**. A node reaches "gated clean" only here.

## Procedure

Route by the worst finding across the node's `completeness/` and `adversarial/` records:

- **Blocker** (wrong problem / a settled decision contradicted / the node unverifiable as planned) →
  back to **stage 2** (re-draft); under delegation this is a **stop-for-human** (RAT3).
- **Major** (sound goal, materially wrong approach) → back to **stage 2**.
- **Minor** (real but local) → **fix in place**, proceed.
- **Nitpick** (style/clarity) → **log**, proceed.
- **Clean-or-resolved on both passes** → the node is **gated clean**; proceed to stage 6 (granularity
  → decompose-or-leaf).

Append one entry to `plan/decisions.md`: the node, the gate, the worst severity, the route, and — for
any human override — a one-line rationale + name.

## Severity model and gate routing (SEV)

| Severity | Meaning | Route |
|---|---|---|
| **Blocker** | wrong problem / settled decision contradicted / node unverifiable | → stage 2 (stop-for-human under delegation) |
| **Major** | sound goal, materially wrong approach | → stage 2 |
| **Minor** | real but local; fixable in place | fix → proceed |
| **Nitpick** | style/clarity; optional | log → proceed |
| **Clean** | both passes clean-or-resolved (earned per lens) | → stage 6 |

**Gates route by the worst finding's severity.** **The reviewer's severity routes** — the author may
contest only via a logged `decisions.md` entry, and demoting a **blocker or major** additionally
requires the human tie-break. A silent unilateral demotion is a gate violation.

## Rules governing this gate

**Gate-before-present (GBP).** A node is not finalized / presentable / assemblable until **both** the
completeness and adversarial passes are on record and **clean-or-resolved**. A node with an unresolved
finding cannot proceed to stage 6 and cannot appear in `assembled-plan.md`.

**Gate-bounce cap (CAP).** After **2 bounces at the same gate on the same finding class** (same gate +
same targeted node section, regardless of wording — a rephrased objection or the same defect in a
nearby spot still counts), the loop **stops and a human breaks the tie** (accept the risk, change the
node's goal, or kill the branch). Each backward route carries the prior findings forward via
`decisions.md` so the next passes confirm they were addressed rather than re-deriving.

**Completeness before adversarial (PASS-ORD).** The gate reads the `completeness/` records (recorded
first) and the `adversarial/` records (recorded second); a node missing either set is **un-gated**, not
clean.

## Cross-cutting rules

**`decisions.md` is the append-only gate log.** Each gate appends one entry; the **cap depends on it**
(counting bounces + carrying prior findings requires the history to persist). A clean pass-through is a
single line; a human override is the entry that matters most.

**Stop-for-human under delegation (RAT3).** A blocker about to re-draft, or a cap tie-break, **halts the
runner and returns the question verbatim** to the orchestrator to relay to the actual human — never
self-answered.
