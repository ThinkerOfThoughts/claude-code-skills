# Stage 2 — Draft plan node (fill the spine)

**What this stage does:** produce the node's `plan.md` — the **7-section universal spine** filled, plus
the Layer-2 `required_sections`, plus the node's **proposed granularity** (either *leaf* with an atomic
task spec, or a *decomposition* into named children with the **seams between them**). This draft is what
the two cold passes then review; it is **not** presented until both passes are clean-or-resolved (GBP).

## Procedure

1. **Fill the 7-section spine (SPN)** — verbatim section headings from `METHODOLOGY.md`:
   1. Problem / intent — 2. Approach — 3. Interfaces & seams — 4. **Outputs & artifacts (with their
   locations, incl. on-disk/output-folder layout)** — 5. Failure modes & contingencies — 6. State /
   restart story — 7. Verification. If the node instantiated a skeleton (TPL1), fill the skeleton's
   pre-shaped sections; otherwise fill the bare spine. **Section 4 is never omitted** — it is the
   founding-failure section; state where every deliverable lands.
2. **Add the Layer-2 required sections (tier ii).** Every section in the config's `required_sections`,
   filled, on top of the spine.
3. **Propose the granularity (GRN).** State whether this node is a **leaf** (an atomic,
   agent-executable task spec — one agent can execute it with no further planning) or **decomposes**. If
   it decomposes, name the **child nodes** and, critically, the **seams/interfaces between them** (what
   each child hands the others; what contract they share). The seams are part of *this* node's plan — a
   between-child contingency is this node's to catch, not a child's (COV).
4. **Do not self-critique into presentability.** Drafting may note open questions, but the node is not
   whole until the cold completeness pass (stage 3) says so. Resist the confidence that read the
   founding-failure plan as finished.

## Rules governing this stage

**The spine is mandatory and verbatim (SPN).** All seven sections appear with their stable headings,
§4 always present with output **locations**. A leaf's spine **collapses** to an atomic task spec — the
same seven concerns compressed to what one executing agent needs, not dropped.

**Seams are the parent's, not the children's (COV).** When a node decomposes, the contracts *between*
its children are drafted here, in this node's `plan.md`, so the owning orchestrator's passes review
them. This is what makes coverage total rather than leaf-only.

**Granularity is proposed here, validated by the passes (GRN).** The leaf-vs-decompose call is drafted
now and **validated** by the two red-team passes (a wrongly-declared leaf, or a wrong decomposition, is
a Completeness or Logical finding). The formal decompose/leaf execution happens at stage 6.

## Cross-cutting rules

**Gate-before-present (GBP).** This draft is not presentable, finalizable, or assemblable until the
stage-3 and stage-4 passes are both on record and clean-or-resolved.

**Disk is the truth (RST).** `plan.md` is the node's durable state; a restart mid-draft re-runs the
draft fresh (an incomplete `plan.md` is the not-done marker).
