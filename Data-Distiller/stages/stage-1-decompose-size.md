# Stage 1 — Decompose + size

**What this stage does:** turn the corpus into a **static pyramid of analyzable items**, pick a
**size strategy** for each artifact, assign each item a **tier + redundancy**, compute the **static
concurrency budget**, and build the **`tree/` skeleton** — all from disk, all before any analyst
runs. The coordinator does this itself (no findings are read; there are none yet).

## Procedure

1. **Decompose** the corpus into items of the Layer-2 `atomic_unit` shape (e.g. one run = one arm of
   one pass). Every multi-arm/multi-pass container expands to **one item per arm per pass**. Record
   each item in `index.md` with its artifact paths, its Layer-2 config, and any **degraded** flags
   (missing layers). List genuinely-unanalyzable containers in a `## SKIP` appendix with the reason.
   Adjudicate ambiguities (mis-filed / mirrored / byte-identical copies) explicitly in `index.md`.

2. **Pre-flight EVERY artifact's size — mandatory, before any dispatch.** `du -h` each artifact.
   **Never `Read` a multi-hundred-MB file** — inspect its structure first with `wc -l`, `head -c`,
   and a max-line-length probe (`awk '{if(length>m)m=length}END{print m}'`). Anything above ~50 MB
   is slimmed before it is ever handed to a leaf. (This is the OOM guardrail — issues-log #2.)

3. **Pick the size strategy by WHAT is big** — a selection among **three**, not "slim everything":
   - **(a) redundant/irrelevant BINARY bulk → replace-with-descriptive-tag.** Run the **streaming
     slimmer** (below). Output the slimmed copy to `_prepared/<item>/`; **leave the original
     untouched**. Point leaves at the slimmed copy; tell them the tag is ground truth for what the
     blob was (so a hallucinated description is still detectable).
   - **(b) analytically-relevant TEXT bulk → subdivide** into context-complete pieces on Layer-2
     `legal_cuts` boundaries with the declared overlap. Write the split plan to `index.md` and the
     piece manifests to `_prepared/<item>/`. **Requires the stage-2 human cut-gate.**
   - **(c) genuinely irreducible → escalate the model tier** (toward the Opus reserve). If even Opus
     can't fit it, **stop for the human** (do not silently truncate).

4. **The streaming slimmer (for strategy a).** Process the file **line-by-line** (never load the
   whole file into memory). For each row, recursively replace any string above a size threshold
   (default >200 KB — exclusively the binary blob; no analytically-relevant text field is that big
   *for this corpus class*. **The threshold is a Layer-2-tunable knob** — raise it for a corpus with
   legitimately large text fields so a real text field is never tagged away)
   with a **descriptive placeholder tag** stating what the blob was, keeping every relevant TEXT
   field **verbatim**. For a *real* (not noise) binary, extract + view the first blob first (memory-
   safe streaming extraction → decode → view) so the tag describes the true content, not a guess.
   The original 1.2 GB-class file is **only read, never modified**.

5. **Size AFTER (a), then tier.** Estimate each item's **dispatch-token** size on the text that will
   actually be sent (post-slim — **bytes ≠ tokens**). Assign the **cheapest tier that fits with
   headroom**: **Haiku → Sonnet → Opus**. A within-window item may **escalate** when judged
   dense/complex (a judgment call, recorded in `plan/decisions.md`). **Prefer subdivide + cheapest
   fit; Opus is the irreducible reserve.** **Set the `borderline` flag** (`borderline: yes` in the
   item's `index.md` record) for any item **near a tier boundary** or whose **atomic-unit choice is
   ambiguous** — the sizer *produces* this flag here; the stage-2 cut-gate *consumes* it (borderline
   items join subdivided items in the gate).

6. **Set redundancy from the tier.** **Haiku items → 6 analysts; Sonnet/Opus items → 3.** A
   subdivided item's Haiku-sized pieces each get the 6-analyst treatment. **One verifier per
   analysis list.** Write `{tier, analyst-count, split-plan, borderline, degraded}` per item to
   `index.md`.

7. **Compute the static concurrency budget.** From the decomposition + redundancy, compute peak
   concurrent agents and **cap it to the Layer-2 `concurrency_ceiling`**; write the number +
   derivation to `plan/budget.md`. Dispatch later **serializes within this cap** (no reactive
   scaling). This is the OOM/usage headroom, planned not reactive.

8. **Build the static `tree/` skeleton + write `RUN.md`.** Create the whole recursive node structure
   at decompose-time (SET nodes → item nodes → piece nodes for subdivided items), each with an empty
   `_status.md`. An **empty leaf dir IS the "not done yet" marker.** For **subdivided/borderline**
   items, mark the skeleton + this item's slice of the budget **provisional-pending-gate** — the
   stage-2 human may revise the splits, and nothing dispatches against a stale split. **Also write
   `RUN.md`** — the self-contained apex runbook (mission in one paragraph; the hard rules —
   blindness, read-only, off-limits, concurrency cap; the key paths; and the restart procedure:
   read `RUN.md` + `index.md` + walk `tree/` for the first node whose expected output is missing →
   resume there). `RUN.md` is authored here so a post-compaction coordinator can resume from it +
   the tree alone (see `stages/stage-7-restart-resume.md`).

## Rules governing this stage

- **Size-check is a mandatory pre-dispatch gate**, same tier as the read-only clause. An artifact
  large enough to OOM the host must never reach a leaf (issues-log #2).
- **The original corpus is never modified** — `_prepared/` holds the only transformed copies.
- **The static tree is fixed here.** No mid-run restructuring; tree height comes from corpus
  divisibility, decided now.
- **Provisional-until-approved for subdivided items.** Their piece dirs + budget slice are re-derived
  at stage 2 if the human revises the cut (see `stages/stage-2-cut-gate.md`).
