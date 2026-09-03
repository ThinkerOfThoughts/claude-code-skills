# Stage 8 — Handoff

**What this stage does:** emit the diagnosis artifact and hand the fix to guarded-change. Dragonfly
finds the bug; it does **not** author the fix.

## Procedure

- **Write `diagnosis.md`** (A-8-1): the root cause, the causal chain **with each level's depth-check
  status**, the **named residuals**, the representative repro, and the recommended fix.
- **The recommended fix carries a regression-safety history check (B-HIST-1).** Before the recommended
  fix enters `diagnosis.md`, check the history of the code it would touch, on whichever fronts exist:
  **(a) git archaeology** — `git log -S`/`blame` the lines the fix would change and **read the
  introducing commit's message**, because a bandaid is often itself a *prior fix* whose message names
  the earlier bug and the constraints it defends; and **(b) issue/PR history** — search **closed and
  open** issues/PRs touching that file/component/subsystem. Record the prior fix's stated constraints as
  **hard bounds the fix must not trip**, and state — against the **three regression modes**: does the
  direction (1) **re-introduce a previously-patched bug**, (2) **worsen an existing one**, or (3)
  **create a new one**? — why it trips none. Dragonfly has no stage that postdates the recommended fix,
  so this is an **author-side archaeology + self-stated** check that **hands the bounds forward as a
  record**; the independent *red-team* of the fix direction against them is **guarded-change's**, whose
  charter carries the same HIST duty at stages 3/6 and **re-derives the bounds independently rather than
  trusting the forwarded values** (B-VER-1's inherited-claim principle). A direction that silences
  today's symptom but revives the bug the code was patching is a regression, not a fix — surface it as
  such rather than recommending it. (Applies equally to a **mitigation direction** riding a
  "characterized, not found" handoff.)
- **The recommended fix must conform to the touched module's stated design intent (B-DES-1,
  fix-direction half).** Before the recommended fix enters `diagnosis.md`, check it against the
  **documented purpose** of the code it would touch (docstring / the plan or spec it implements): a fix
  that silences today's symptom but **contradicts the module's design intent** is a wrong root, not a
  fix — surface it as such rather than recommending it. Watch specifically for a fix that would make
  the design produce **less** than its documented purpose (e.g. "carry the section forward unchanged"
  against a docstring that says the section must keep shrinking). Like B-HIST-1, this is an
  **author-side self-check** that **hands the design-intent bounds forward as a record**; dragonfly has
  no stage that postdates the recommended fix, so the independent *red-team* of the fix direction
  belongs to **guarded-change** (dragonfly diagnoses; guarded-change makes and challenges the fix),
  which re-derives the bounds rather than trusting the forwarded values (B-VER-1's inherited-claim
  principle). (Applies equally to a **mitigation direction** riding a "characterized, not found"
  handoff. The diagnosis-side half — an empty-input symptom is a relay when the content is
  present-but-mis-routed — is at stages 3 and 7.)
- **Hand `diagnosis.md` to guarded-change to make the fix. Dragonfly does NOT author the fix itself**
  (A-8-2). This is the legitimate workflow handoff — a compose relationship, not a rules dependency:
  dragonfly diagnoses, guarded-change makes the fix, and dragonfly then verifies it at stage 9.
- **Surface the incidental-bug ledger as a parking lot — on either terminal verdict** (a "found"
  `diagnosis.md` **or** a "characterized, not found" handoff). If `incidental-ledger.md` is non-empty,
  the handoff lists it as **out-of-scope findings for future, separately-scoped investigation** — kept
  **distinct** from the diagnosed root cause and its named residuals (which are `S#`-related by
  definition). It is surfaced, **not** routed to guarded-change (each incidental bug is a future hunt of
  its own, if pursued). (If a hunt halts mid-loop at the convergence-cap stop-for-human without reaching
  stage 8, the parked findings are on disk + in the cold-start carry-over brief — not lost.)

## "Characterized, not found" — the only other legal terminal verdict (A-8-3)

If the hunt ends short of "found," it may end ONLY as "characterized," requiring ALL of: (a) what IS
established (each claim cited + cold-red-teamed); (b) which hypotheses were refuted, with evidence;
(c) WHY the full bar is unreachable — a named reason; (d) **explicit human sign-off**; (e) presentation
tier stays "characterization," never "the cause." Mitigation directions may ride the handoff **marked
as such** (verified at stage 9 on symptom evidence only — no cause-resolution claim). Missing any of
(a)–(e) → not a legal stop.
