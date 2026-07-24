# Example — companion-emergence re-sift (worked Layer-2 config)

This folder is a **worked example** of a Data-Distiller Layer-2 corpus config, genericized and
**redacted** from the real T1–T4 cold re-sift (71 items, monologue-bleed / role-leak series). It
shows how a corpus maps onto the config contract in `../../METHODOLOGY.md`.

## Files
| File | What it is |
|---|---|
| `corpus.md` | The Layer-2 config: the shared **artifact-context block**, the **atomic unit** (one arm of one pass), **legal cuts + overlap** (turn boundaries, 1-turn overlap), the **off-limits paths** (redacted), the ledger pointer, and the **concurrency ceiling** (3). |
| `ledger.md` | The optional **label-only** prior-knowledge ledger — known symptom *labels* only, **redacted** of every live protected-dataset path (`<REAL-PATH-REDACTED>`). Used to recognize/label known phenomena, never to narrow the open mandate. |

## What this example demonstrates
- **The artifact-context block as a Layer-2 slot** — dropped verbatim into the analysis + verify
  briefs so analysts know what each artifact is and what is legitimately in-context (not a finding).
- **Size handling on real data** — one arm's `turn_diag.jsonl` was 1.2 GB (inline base64 image);
  the notes show the **tag-replace** strategy (streaming slimmer → descriptive tag, original
  untouched) that prevented an OOM.
- **Redaction (issues-log #3)** — the ledger cites the historical incident location as
  `<REAL-PATH-REDACTED>`, never a live path, so a diligent analyst is never tempted to open a
  protected dataset "just to verify the locator." A shipped example must carry **no** live
  protected path — this one is checked to carry none.

## Adapting it to your corpus
Copy `corpus.md`, then: replace the artifact-context block with your system's; redefine the atomic
unit; set legal cuts + overlap for your data's natural boundaries; list **your** off-limits paths
(the exact real paths to fence — named to be never-opened, not visited); point `ledger` at a
redacted label-only ledger or set it to `none`; and set `concurrency_ceiling` to your host's
headroom. The skill's stages read these to decompose, size/tier, gate, dispatch, merge, and roll up.
