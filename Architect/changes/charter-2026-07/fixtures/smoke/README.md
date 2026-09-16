# STALE — these are the composed prompts F1/F2 were actually run against, and the artifact has moved since

**Do not re-read these as if they were the current set, and do not silently recompose them.** They are kept
byte-frozen because they are the evidence for the F1/F2 results in `8-harness.md`: a record of a
behavioural run is worthless if the thing that was run cannot be reproduced.

**Composed from these artifact hashes (2026-07-29, pre-generalization):**

| File | sha256 at composition |
|---|---|
| `charter-common.md` | `35902f6df095f970b99d337e2fea6ce99daba05dac2992a403516f052cbed1f7` |
| `redteam.md` | `c28fcbcf634ee5b781872a6da8776ccddb162ff1c1346750fbc303d02102b838` |
| `redteam-plan.md` | `72ffd5500795125a1fe85e83abe8fa725e425ec667bf0cdb12af258924c50563` |
| `divider.md` | `0965807e681fa825e9a5202365a37e11af879e835af8f385bce3635614f91a20` |
| `leaf.md` | `f6d8090a64793c2d7ef12a017f69f52861e753e9c4eaac624be19d9e7f9071c3` |

**What changed after the run, and what it does and does not cost the results:**

- **`charter-common.md`** — §5's record rule (element (i): verbatim copy → path + sha256). **That change
  was CAUSED by this run**, so it could not have been in the version tested; that is the correct order.
- **`combiner.md`, `node.md`, `charter.md`** — the `Union` generalization. **No composed prompt here
  contains them**, so F1/F2 are unaffected.
- **`redteam.md`, `divider.md`, `leaf.md`, `redteam-plan.md`** — unchanged since composition.

**So the F1 result still holds for the current set**: F1 tested the `charter-common.md` §0 rewrite, and §0
has not been touched since. **F2's leaf and divider arms also still hold.** The reviewer arm was composed
from a `charter-common.md` that has since changed **in §5 only** — a section F1/F2 did not test, and whose
change is the one this run's evidence produced.

**Recompose and re-run before citing these for anything new.**

---

## 2026-07-29, second batch — `composed-node.md` and `composed-combiner.md` (F5/F6)

**Composed from the POST-repair set and CURRENT at composition.** Added to settle the pass-3 reviewer
disagreement on the node/floor contradiction by dispatch rather than by a fourth textual argument, per the
owner's testing rule (record 2544).

| File | sha256 at composition |
|---|---|
| `charter-common.md` | `34e50db3b0eddac4d1e44e69d75520a40f5d7fc9cf6ee80a9e67dc6977d55eff` |
| `node.md` | `8aedc57525efb8d539bf4d347a6859805fae675cd61eefd67837bb84ef1d33d6` |
| `combiner.md` | `105ae484f918231c27ca7ab82e305b7f4d631b7593a9d6f7093c3cd166356828` |

**The first batch above (F1/F2) remains stale and is kept frozen for the same reason.** Recompose before
citing any of these for anything new — and note that **all five smoke agents to date ran on one model
(`sonnet`)**, so none of this separates the prompt set's behaviour from that model's.
