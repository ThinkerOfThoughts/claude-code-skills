# Stage-3 cold review — reviewer A (VERBATIM RECORD)

**Provenance (charter's provenance rule — all five elements + this run's additions):**
- **(i) Charter given, verbatim:** `3-charter-given.md` (this folder), read in full by the reviewer, plus
  the per-reviewer frame addition quoted below.
- **(ii) Exact context path list given:** the closed set enumerated in `3-charter-given.md` §"Artifact
  under review".
- **(iii) Reviewer's verbatim output:** below, unedited.
- **(iv) Agent type + model:** `general-purpose` subagent (Claude Code Agent tool) / `claude-opus-5`.
- **(v) Reviewer-reported context-file sha256s:** in the output below.
- **`spawn_id` (dispatcher-recorded):** `a1cb9e6c3aa124a3f`. **Reviewer's self-reported identity:**
  session `45cb99a2-543d-4447-a3e3-2a38963b0775`, "no separate agent/dispatch id is reportable to me".
  *(Note for the record: this divergence between dispatcher-observed and self-reported identity is
  itself the substance of reviewer B's finding L-11.)*
- **`frame`:** SOURCE-ANCHORED / FACTUAL.
- **Consumer spot-verify of reported hashes (charter, spot-verify duty):** A's reported hashes for
  `0-baseline.md` / `1-spec.md` / `1.5-criteria.md` / `2-plan.md` are byte-identical to the values
  independently captured in `context-hashes.txt` before dispatch. ✓

## Frame addition given to reviewer A (verbatim)

> **FRAME = SOURCE-ANCHORED / FACTUAL.** Your specialty is: *does the artifact match the source?* You
> are the reviewer who actually opens the cited files and checks. Concretely, spend the bulk of your
> effort on:
> 1. **Every claim the spec/criteria/plan makes about what a FINDING says** — check it against
> `FINDINGS.md`. Does the plan's fix for F1..F10 actually address what that finding says, or a
> convenient re-reading of it? Does the plan claim a finding demands something it does not? Does the
> plan re-fix something FINDINGS.md lists under **"Triaged NOT genuine (or already closed)"**?
> 2. **Every claim about what the Architect skill CURRENTLY says.** `0-baseline.md` section B0.3 makes
> 24 numbered claims (P1..P24) about baseline text, each with a file:line citation at commit 3771038.
> **Spot-verify a substantial sample of them** … Report any citation that does not say what is claimed,
> any claim that overstates or understates the baseline, and any baseline site the table MISSED (e.g. an
> additional site stating the same rule, which would make the planned "state it at every site" edit
> incomplete).
> 3. **Every claim about the model being copied.** The plan says its topgate fix is "modelled on
> guarded-change's RAT1 ratification-record discipline" … check that RAT1/CH11 actually say what the
> plan says they say. Same for any claim about Data-Distiller … or Dragonfly …
> 4. **The rule-ID collision claim.** The plan introduces 13 new uppercase mnemonic IDs: JOIN, SEAM,
> BIND, KIL, PRV, DIV, IDN, RES, CNC, CTX, XPM, ING, DEP. … **Actually test each of the 13 proposed IDs
> against the real corpus** … for substring collisions with existing IDs or with ordinary words that
> appear in the text. Report every ID that would produce phantom or missed sites.
> 5. **The oracle-can-fail claim.** … is there any S- criterion whose assertion would **already pass at
> baseline** (making its oracle vacuous)? S-F4's own text flags one such trap; look for others the
> author missed.

---

## VERBATIM OUTPUT

AGENT TYPE / MODEL: Claude Code subagent (general-purpose / Explore-class, read-only discipline self-imposed per charter) / `claude-opus-5`
SPAWN IDENTITY: session id `45cb99a2-543d-4447-a3e3-2a38963b0775` (derivable from my scratchpad path); no separate agent/dispatch id is reportable to me
FRAME: **SOURCE-ANCHORED / FACTUAL** — open the cited files and check

CONTEXT FILES READ (sha256):
```
0a16c8453e7fffad2dca410fd57acef837f27f1eda47a4b4e45873bc536995ca  <CF>/0-baseline.md
a67a4095eeb3b90f1a4d1295c319acb22143822f2de5ae2e5c7e0bf8c4afb0ff  <CF>/1-spec.md
4c58898f6c71b9e194b7455ed3279601d2ad8363ee323be82fb2cb761c363eb3  <CF>/1.5-criteria.md
dafc0dd434fa26b7b99451f897fcc603ed23a1a3fa123b66565c1ad3af5ab081  <CF>/2-plan.md
7b44f91ad2a88f9d0749f212647ff849c28a7f57d9213af211f3fe9ffe9ab62f  <CF>/3-charter-given.md
75d81bc066bdcf6d78056b529d50420e5872e6c0cb24bf74af9808c17f7a5b0f  <CF>/context-hashes.txt
7584924a2876ef669115f3e47b1721d98b14e4ff3a583906381ea1f8b521c450  <WT>/Architect/SKILL.md
f64f8ee4c80e8b1d38624088c3f0c49cb4355c28782e09009509816a237241fa  <WT>/Architect/METHODOLOGY.md
79c260a928d625316d031879f1d8fa1f10dcfe15af41ff2b04550623f3f0661a  <WT>/Architect/README.md
6134cad8d5edceaa4be6a39bd7eaec430c9236360ddb41ff38511d6a983c7819  <WT>/Architect/stages/charter.md
ef83617b8bdbba0bd1a3152f03cfdcf899da9ab95ba428e11230acf36e2deec5  <WT>/Architect/stages/stage-1-frame-template-match.md
2e76963ce446190ff4bb4d8100a097d8a62e684d5936d38a74e227aea3ad1036  <WT>/Architect/stages/stage-2-draft-node.md
6aac9010c008cdc3a9dff6c57c1d1e3461d3734bab1c2a6835367768a7ccba4e  <WT>/Architect/stages/stage-3-completeness-critic.md
96570a6d9298c67ab6b5fe8653b16cf7068fdbe547373a32bee3e02c0721f07c  <WT>/Architect/stages/stage-4-adversarial-redteam.md
99db26b419d61a86055f4d9e532cb1ccc2fc798b6aa20d5e8d1bf5c2bf1ee5f5  <WT>/Architect/stages/stage-5-gate.md
b202101b7b4b16314d4742851138b53efe40b33f3025886149f02ba4aeac1993  <WT>/Architect/stages/stage-6-granularity-decompose.md
864b74dcfcf43e18b576145327beeb011b1e44bb672f7a10e8d8b0f9ad9cb607  <WT>/Architect/stages/stage-7-assemble.md
97431f52e7487ab34c9e9278496b687ca2b4ca2bf178203de3d76151c35762c1  <WT>/Architect/stages/stage-8-restart-resume.md
d2a86068b92d7ee6b47b7af6dd506f456b589a50a6cac7e0e8d15d23246b3fb4  <WT>/Architect/templates/seed/README.md
7148ec60e18b8cf4606b50b0fc8b49f299731b3d3c26a4787bc0a8bf0be52e89  <WT>/Architect/templates/seed/generic-node.md
b4509defabe16768edcd024a98f44f37c90351aef5fa759b56b0c0930a98cf64  <WT>/Architect/templates/seed/decomposition-node.md
c7341c863a494a41e616e00b70c14bf8034cfe292108e2dca92436847c3f093e  <WT>/Architect/templates/seed/leaf-task-spec.md
b52a22d2012e7a640e68300a2a8f0a985e811e024c0259b26d7d0aabc6ec37ea  <WT>/Architect/examples/authoring-a-skill/planning.md
aa52ab3b03b9e78ea7ca977d7dacfac515d8e21dbdd5c2faf97004abb563b600  <WT>/Architect/examples/authoring-a-skill/README.md   [grep-only, not read whole]
c163ff87588dc97dbffae05cfe675985533ae8248b5d583d3322a090c4aceb8c  <WT>/Architect/guarded-change.architect.md
16dbb31b9ccd2ee83296bf24e0941e05556d3a545f55901e8f28e519b6554df3  <WT>/Guarded_change/stages/stage-3.md
175061c27bb6980ff76c6358d403299d343c409b2952308ffea7485fff880675  <WT>/Guarded_change/stages/stage-4.md   [grep-only]
8f3fe2b322ec802d080aa130ebd5dd526c4407a2f729931763c6a778ea4a7c30  <WT>/Guarded_change/METHODOLOGY.md   [grep-only]
addf17481c57bcada577ff2d3d74628b93ea8b43a89c884d25a670af8889c625  <WT>/Guarded_change/SKILL.md   [grep-only]
0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590  <WT>/Guarded_change/stages/charter.md   [hash-verified only]
b6c14f0669a130f032bf6c18b17a689d1c2d7316fa3250ad20f888b7a03149e6  <WT>/Guarded_change/stages/stage-1.md   [grep-only]
c5d1e2068f35760e373517e243003800c264c64bf3d93d6d8ea6b951990af870  <WT>/Dragonfly/stages/charter.md   [grep-only]
94cb55e86b3fbb1dd9cdf76f3956dcc62ac7aae6f84831f29642f8123ddb13c8  /home/zero/architect-dogfood-2026-07-24/FINDINGS.md
6d8dc31b40a5b388d7f8bc91a01341a3b6a6ee4b20e5afc009475e4edee856ae  /home/zero/architect-hardening-loop/LOOP-STATE.md
d931b61180448f6488072318743ebce4303ce1e3db329ad16738b74493b5330a  Data-Distiller/METHODOLOGY.md   [grep-only]
8b62e82d25fe63533dd20627b4b4275dde36644ad9b7993f3d181f9254ee581c  Data-Distiller/SKILL.md   [grep-only]
f3791564ddba5e5a0fc15895ea1b4246ff2d00a7c789b6b34a209a7111db0d20  Data-Distiller/README.md   [grep-only]
ff671d077db3690356d660d63f831c05887c8dd576a4a93ae83ec6d77fe86de1  Data-Distiller/charter.md   [grep-only]
```
Baseline verification method: `git -C <WT> diff --stat 3771038 HEAD -- Architect/` is **empty**, so the worktree files above *are* the `3771038` baseline byte-for-byte; all `file:line` citations below are valid at the recorded baseline commit.

FILES I WAS GIVEN BUT DID NOT READ: the rest of `<WT>/Dragonfly/` (SKILL.md, METHODOLOGY.md, stages/*) beyond `stages/charter.md`; the rest of `<WT>/Guarded_change/stages/` (stage-2, 5, 6, 7, 8, charter.md body); `Data-Distiller/stages/*` beyond grep hits; `<WT>/Architect/changes/initial-authoring-2026-07/` (frozen record — grep-touched only).

ANYTHING I READ OUTSIDE THE CLOSED SET (declared):
1. `/home/zero/.claude/plans/1-this-is-a-proud-scott.md` (sha256 `aa6c2e12bd274388868570a3cb7b83542eced6eef224e4812f8fd2c044012249`) — **targeted greps only**. Read deliberately: `guarded-change.architect.md:27-30` designates it "THE APPROVED SCOPE/DECISION RECORD — source of truth for every settled decision … Any spec/criteria/plan claim is checked here first", yet the charter's closed set omits it. See F4-2.
2. `…/skill-creator/scripts/quick_validate.py` — existence check only (`find`), to confirm S-SC1's oracle exists.

---

## Lens 1 — FACTUAL

**F1-1 · MAJOR · B0.2's `TOP` row and its "measurement caveat" are both wrong under the very matcher they mandate; R1's reference table cannot pass its own baseline replay.**
`0-baseline.md:43` records TOP's baseline site set as "SKILL, METHODOLOGY, stages 6,**8**, templates/seed/decomposition-node, **examples/…/planning**"; `0-baseline.md:51-56` says the remedy is word-boundary matching and that `templates/seed/generic-node.md` and `examples/…/planning.md` "are **not** baseline TOP sites."
Measured (`grep -rnw -- TOP` over `SKILL.md METHODOLOGY.md stages/ templates/ examples/ README.md`): `SKILL.md:78,104`; `stage-6:15,43`; `METHODOLOGY.md:79,212,264,327`; `decomposition-node.md:27`; **`examples/authoring-a-skill/planning.md:25`**. **Zero hits in `stages/stage-8-restart-resume.md`.**
Two distinct defects:
- (a) `examples/…/planning.md:25` reads `required_sections: # Layer-2 tier-(ii), ON TOP OF the 7-section spine`. The phantom there is ordinary-English **"ON TOP OF"**, not `HARDSTOP` — and `-w` does **not** remove it. `METHODOLOGY.md:79` is the same phantom. So the caveat both misattributes the cause and claims a fix that does not work. `1.5-criteria.md:391`'s self-test ("confirm the word-boundary matcher does **not** report `HARDSTOP` as a `TOP` site") is true and *misses the surviving phantom entirely*.
- (b) `stage-8` is in the TOP row **only** because `stage-8:20` contains `HARDSTOP` — an uncorrected *third* instance of the artifact the caveat claims to have triaged. stage-8 is a `topgate` site (`stage-8:9,14`), not a `TOP`-token site.
Impact: R1 (`1.5-criteria.md:408-414`) oracle = "word-boundary site map of the edited tree vs. the B0.2 table; set difference must be ∅", and the shared `S-` self-test (`1.5-criteria.md:20-24`) requires every preserved-rule assertion to **PASS at baseline**. TOP's row demands a word-boundary `TOP` in stage-8 that the baseline does not have ⇒ **R1 fails its own baseline replay ⇒ `verified = no`** for the gating regression criterion.
Do instead: recapture B0.2 with `grep -rnwo` plus hand-triage of every hit; drop stage-8 from the TOP row (or restate it as a `topgate` site); drop `examples/…/planning.md` + `METHODOLOGY:79` or exclude `ON TOP OF` in the matcher; extend S-SC2's self-test to assert `ON TOP OF` is not reported as a TOP site.

**F1-2 · MAJOR · Two of the 13 new IDs violate this run's own ID rule: `KIL` is a substring of `SKILL`; `ING` of `PLANNING`/`RULING`.**
Rule: `guarded-change.architect.md:114-116` — "A new ID must be a standalone uppercase token that is **not a substring of another ID or of an ordinary corpus word**"; restated at `1.5-criteria.md:37-39` and `1-spec.md:132-133`.
I tested all 13 against the real corpus. Bare `grep -rho` (the documented failure mode): `KIL` → **21 hits across 4 files** (`METHODOLOGY.md`, `SKILL.md`, `README.md`, `examples/…/planning.md`), every one inside `SKILL`; `ING` → 2 hits (`stages/charter.md` inside `RULING`, `SKILL.md` inside `PLANNING`); all other 11 (`JOIN SEAM BIND PRV DIV IDN RES CNC CTX XPM DEP`) → **0**. Word-boundary `grep -rnow` → 0 for all 13, so the mandated matcher is sound — but the *stated constraint* is broken, and 21 phantom sites in the file every reader opens first is strictly worse than the 2-file `TOP`/`HARDSTOP` instance the constraint was written from. Any hand-diff (S-SC2 assertion (c), `1.5-criteria.md:388`), ad-hoc build-time grep, or cycle-2/3 recapture reproduces the exact documented failure.
Forward-looking companion risk: `JOIN SEAM BIND RES DIV DEP ING` are English words/stems, and this corpus uses ALL-CAPS for ordinary emphasis (`OUTSIDE`×14, `RUN`×12, `ONLY`×5, `WITH`×3, `NOT`×3, `PROVEN`, `MUST`, `EVERY`, `ONE`, `INSIDE`, `LEAF`). One emphatic "RESOLVED"/"KILLED"/"JOIN" after the edit yields a phantom (bare grep) or a missed site (word-boundary). The 18 baseline IDs are mostly non-words for exactly this reason; the two that aren't (`TOP`, `CAP`) already caused the documented problem.
Do instead: rename `KIL` (→ `KILB`/`ABRT`) and `ING` (→ `INGM`/`IMOD`) **before** `1.5-criteria.md:39` freezes the set; run the collision check `2-plan.md:281` promises *ahead of* the criteria, not after.

**F1-3 · MAJOR · `BIND` binds only the node's own `plan.md`, while the detector it claims to reuse collects a hash for *every* context file — and `SEAM`'s own reopen rule creates the parent-plan staleness the narrowed field cannot see.**
Claim: `1.5-criteria.md:96-107` / `2-plan.md:89-95` — field `reviewed_plan_sha256`, "the *plan.md hash the reviewer actually read*", and "the rule is stated to be **the already-collected detector** (the charter's context-file sha256), not a new instrument."
Source: `stages/charter.md:96` collects "the reviewer-reported **sha256 of each context file** it read"; `charter.md:97` puts **the parent node's plan** in the closed input set (also `stage-3:17`, `stage-4:14`). The plan narrows a per-context-file detector to a single file and calls it the same detector.
Failure scenario: child C bumps `seam_rev`; per D5 (`2-plan.md:75-79`) the parent re-drafts its seam slice, re-runs both passes and takes a new `plan_sha256`. C's six records still carry `reviewed_plan_sha256 = sha256(C/plan.md)`, unchanged — so BIND passes at stages 5, 6.5 and 7 while every child's review was conducted against a **superseded parent plan and superseded seams**. That is F3's defect one level up, manufactured by this change's own SEAM rule, and invisible to the criterion written to catch F3.
Do instead: keep the field plural (`reviewed_context_sha256:` as a path→hash map, or add `reviewed_parent_plan_sha256`) and make the 6.5/7 comparison cover the parent-plan entry.

**F1-4 · MAJOR · `DIV`'s differential frame collapses into the spine-anchored frame on its declared default path — the F7 defect reproduced one level up.**
Claim: `2-plan.md:127-139` / `1.5-criteria.md:198-199` — frame (B) is "handed **another plan-type's `required_sections`**", converting "tier (iii) from unbounded recall into a **diff**"; "Config supplies (B)'s section list via `differential_section_sets`, **defaulting to the seed skeletons' section sets**."
Source: all three seed skeletons are the *same* tier-(i) spine and contain **no Layer-2 `required_sections` at all**. `templates/seed/generic-node.md:5-29` = §1–7 verbatim, with `:31-33` stating explicitly that Layer-2 sections "are appended below the spine"; `leaf-task-spec.md:7-23` = the same seven collapsed; `decomposition-node.md:6-13` = §1–7 plus exactly **one** non-spine block (`:15` "Decomposition — children and the seams between them").
So when the key is absent — the default, and the only path in the shipped worked example, which declares no `differential_section_sets` (`examples/authoring-a-skill/planning.md:6-43`) — frame (B) is handed the 7-section spine, i.e. **tier (i)**, which frame (A) already covers "by name with coverage citations" (`2-plan.md:128`). The "diff" becomes a duplicate of frame (A) and tier (iii) stays unbounded recall. The mechanism half of the F7 fix is *asserted*, not delivered, exactly as F7 says the original claim was (`FINDINGS.md:89-99`). No criterion observes this: S-F7.5 asserts only that the key is *declared and defaulted*.
Do instead: default (B) to a genuinely different **plan-type's** `required_sections` (the example's own list at `examples/…/planning.md:26-34` is one candidate; a second real plan-type list is needed), or make `differential_section_sets` **required whenever DIV is claimed** and state that its absence makes the pass "declared degraded" — the same treatment DIV already applies to three-same-frames.

**F1-5 · MINOR · P10's site list for the completeness overclaim omits two `SKILL.md` sites; S-F7's self-test undercounts.**
`0-baseline.md:74` cites `SKILL.md:3` (frontmatter), `METHODOLOGY:3-5,41`, `README:10,12`, `stage-7:26`. Measured: `SKILL.md:3` ✓; **`SKILL.md:8-9`** — "no plan reaches \"presentable\" until its completeness is **proven** … not asserted" (the router's opening paragraph); **`SKILL.md:17`** — "Completeness is **proven** in three tiers"; `METHODOLOGY.md:3-5` ✓; `METHODOLOGY.md:**40**` (not 41); `README.md:10` ✓, `README.md:12` ✓; `stage-7:26` ✓ — **8 occurrences across 5 files**, against `1.5-criteria.md:205`'s "present at **5** sites". R2 (`1.5-criteria.md:416-423`) is a per-old-site positive migration assertion keyed off B0.3, so the two missing SKILL.md sites are outside the gating regression check; S-F7.3's corpus sweep would probably catch them, but R2 would not.

**F1-6 · MINOR · The "*Change*-marked" set that R2 gates on is enumerated three incompatible ways, and the version the criterion uses omits rows that do replace a baseline claim.**
`0-baseline.md:63-88`: **all 24** rows are marked "**Change**". `0-baseline.md:103-106` (B0.5/R2): "for each of **P1–P24** marked *Change*". `1.5-criteria.md:417`: "(P4, P9, P10, P15, P16, P21, P23, P24)" — 8. `1-spec.md:141`: "(F5, F7, P4, P15, P16, P24)" — 6.
Rows that replace an existing claim and are in none of the short lists: **P2** (`METHODOLOGY.md:268` "terse done-state + one-line roll-up + gate state" vs. D1's 13-key schema), **P5** (`stage-5:44` "or kill the branch" — KIL redefines it), **P13** (`stage-5:14` and the SEV table row `stage-5:28` "Minor … fix → proceed" — D11/RES adds preconditions). Under R2 as written, `stage-5:28`'s table row can keep saying "fix → proceed" unqualified while the RES text a few lines below adds conditions: a half-migrated rule *inside a single file* — precisely the failure R2 exists to prevent.

**F1-7 · MINOR · The plan's concurrency accessor table misses two baseline `index.md` writers, and neither is on any criterion's site list.**
`2-plan.md:241` enumerates `index.md`'s baseline accessors as "**every** node's owner writes `template:`/status (stage 1:21)". Measured write instructions: `stages/stage-1-frame-template-match.md:20` (the string is on 20, not 21), **`stages/stage-6-granularity-decompose.md:11-12`** ("Record the final decision in `index.md` / the node's `_status.md`"), **`METHODOLOGY.md:195`** ("record the template used in `index.md`"), **`templates/seed/README.md:14`** ("record `template: <name>` in `index.md`"). S-C1.3 (`1.5-criteria.md:255-258`) names METHODOLOGY, SKILL, stage-6, stage-6.5, stage-8, templates/seed/README as CNC sites but does **not** name `stage-1`, where the instruction actually lives, and names the other two only as files, not as the old claim to migrate. The charter's concurrency lens is explicit that "a guard's existence is not coverage" and that the enumeration must include accessors the change did not touch; this one is incomplete.

**F1-8 · MINOR · The change will leave Architect's own fork-provenance blockquote false, breaking a Layer-2 required section the skill ships.**
`stages/charter.md:11-23` records the fork from `Guarded_change/stages/charter.md @ 8d73e5d` sha256 `0e73bacf…` — **verified correct**: `sha256sum <WT>/Guarded_change/stages/charter.md` = `0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590`, byte-identical to the recorded value. The block then enumerates "**ADDED:** a standing sixth Completeness lens with an earned-clean clause" and "**DROPPED:** nothing from the core." This change adds four Architect-only clauses to that file (PRV, DIV, IDN, BIND — `1-spec.md:177-179`, `2-plan.md:27`), after which the ADDED list is incomplete. `examples/authoring-a-skill/planning.md:31-32` makes "Charter provenance … (source commit + carried vs. dropped)" a Layer-2 **required section** for skill-authoring plans, and `guarded-change.architect.md:81` makes "charter fork-provenance blockquote present" a stage-8 conformance item. No criterion requires the ADDED list to be updated.

**F1-9 · MINOR · S-C5's baseline expectation is wrong under its own bar, and the spec does not assign the fix to `generic-node.md`.**
S-C5 (`1.5-criteria.md:304-309`) requires each of the three skeletons to contain "an explicit Layer-2 tier-(ii) slot **heading** + the note". `generic-node.md:31-33` has only the **note** (an italic footer), no heading; the other two have neither ⇒ **3 of 3** fail at baseline, not the self-test's "2 of 3". And `1-spec.md:196` assigns `generic-node.md` only "canonical §4 heading" — so as specified the build would not give it a slot heading and the gating criterion would fail. (`0-baseline.md:83`'s "generic-node.md:32-34 has one" also overstates what is there, and the file is 33 lines long.)

**F1-10 · MINOR · The TOP fix drops the RAT1 clause that actually closes the axis, and X3 does not exercise the audit it claims to add.**
Claim: `1-spec.md:96,151-155` "modelled on guarded-change's RAT1 ratification-record discipline"; `2-plan.md:97-111`.
Source verified — `Guarded_change/stages/stage-3.md:89-111` (RAT1): flagged axis + **the options presented, verbatim** + owner response verbatim with a durable source the author did not author (enumerated: "a chat-transcript line … or a timestamped, owner-attributed `decisions.md` entry") + a mapping; **plus** the operative clause "An owner answer that is **partial or adjacent** … is **not a ratification**: the loop **re-asks the flagged axis** and never resolves the answer into the author's own recommended option." CH11 = the cold audit (`stage-3.md:55,99-103`). D7 carries (i)/(ii)/(iii) faithfully but **omits the partial/adjacent → re-ask clause**, and S-F5's six sub-parts (`1.5-criteria.md:135-157`) do not require it.
Oracle consequence: X3's holed fixture (`1.5-criteria.md:440`) is "written by the runner: no owner quote, source = an intermediary agent's prompt text" — detectable by **field presence** alone. The untested case is the one the dropped clause covers: an `APPROVAL.md` carrying a *real* owner quote that does not select this split ("looks good, keep going") with a runner-constructed mapping. And the intact arm's "durable transcript locus" is necessarily fabricated inside the fixture, so **no arm exercises quote-against-source spot-verification** — the mechanism D7 exists to add.

**F1-11 · NITPICK · Citation drift in B0.3 (checked line by line; substance holds in each case).** Wrong: P2 `METHODOLOGY:267,270` contain no `_status` reference (actual mentions 266, 268; and "named 5×" omits `METHODOLOGY:181,239,240`, `stage-6:25`, `stage-7:20`, `stage-8:14,16` — 13 occurrences total); P9 `METHODOLOGY:215`→**214**, `stage-1:11`→**12**; P15 `stage-1:21`→**20**; P19 `generic-node:32-34`→**32-33**; P24 `SKILL:21`→**18-19**, `METHODOLOGY:123`→**121**; P17 omits `METHODOLOGY:316` (the GBP index row also names exit-plan-mode).
**Verified exactly as cited:** P1 (`stage-6:23-26`, procedure ends at step 7), P3 (`stage-5:58`, `stage-6:66`), P4 (`stage-7:14` "Collate top-down"), P5 (`stage-5:44` "or kill the branch"; `stage-7:10-13` "resume that node's loop"), P6 (`stage-2:20-22`, `stage-4:37-39`), P7 (`charter:96`; `stage-8:15` stage-done = exists-only), P8 (`charter:29,97`; `examples/planning.md:40` contains the literal string `used as redteam_context`; **zero** `redteam_context` in METHODOLOGY.md; the contract at `METHODOLOGY:68-92` declares exactly **7** fields), P9 (`stage-6:17`, `SKILL:77`), P10 (frontmatter, README:10/12, stage-7:26), P11 (`charter:127-129`), P12 (`charter:93-99`), P13 (`stage-5:16,38-40`), P14 (serial-vs-parallel: **no occurrence anywhere** ✓), P16 (`METHODOLOGY:220-223`, `stage-6:27-31`, `decomposition-node:24-25` single-level), P17 (`SKILL:33`, `METHODOLOGY:149`; **no stage file** mentions exit-plan-mode ✓), P18 (**zero** `ingest-and-complete` / `mode:` ✓), P20 (`charter:88-92`), P21 (`stage-6:32-35`, `templates/seed/README:20-23`), P22 (`decomposition-node:19-22`), P23 (`METHODOLOGY:265-272`), P24's five distinct heading spellings ✓ (the spec's "five" at `1-spec.md:65` is *more* accurate than `FINDINGS.md:141`'s "3–4"). **No fabricated citation found.**

## Lens 2 — LOGICAL

**F2-1 · MAJOR · The SEAM reopen has no stated propagation rule, no termination, and the plan simultaneously refuses any bound.**
`2-plan.md:75-79`: a child bumping `seam_rev` reopens the parent, which "re-drafts the seam slice, **re-runs its own two passes**" (6 cold agents) and takes a new `plan_sha256`. The text never says whether the parent's own re-draft bumps *its* `seam_rev`. **Both branches are defects:** if yes → the reopen propagates upward, 6 agents per level per event, unbounded — and `2-plan.md:189-191` explicitly *rejects* a budget/timeout because the cost envelope is out of scope (`1-spec.md:120-123`); if no → the grandparent's seam row for this node is stale and BIND cannot detect it (F1-3). No criterion observes either branch; X4's fixture is static.
Do instead: state the propagation rule explicitly and give the reopen a convergence bound routed through the *existing* CAP/RAT3 machinery (in scope, no new envelope needed), or declare the cascade as named accepted risk.

**F2-2 · MINOR · D3's block-and-poll and D5's reopen can be simultaneously obligatory for the same node.** `2-plan.md:63-66` has the parent polling child dirs until all children are terminal; `2-plan.md:75-79` obliges the same parent to re-draft and re-run stages 2–5 for itself the moment a child bumps `seam_rev`. Nothing states what happens to the still-running children (handed the now-superseded parent plan per `charter.md:97`), nor whether the parent resumes polling or re-dispatches. S-F1 (`1.5-criteria.md:46-75`) asserts the two rules separately and nothing tests the interaction.

**F2-3 · MINOR · "All criteria are gating" and the declared degraded-mode route are in tension.** `2-plan.md:268-271` declares every criterion gating; `1.5-criteria.md:453-455` lets an unrun X- arm be discharged by "named risk-acceptance" or "declared deferred"; `2-plan.md:279` allows the whole scope to be partitioned by priority. That is honest and CP5-compliant, but "all gating" then does not mean what a CH9 reader takes it to mean. The stage-8 record needs a third state (`gating` / `gating-deferred-with-named-acceptance`).

## Lens 3 — MISSED OPPORTUNITY

**F3-1 · MINOR · Specify the `_status.md` schema as a machine-parsable block, not prose.** It is the change's declared keystone (`2-plan.md:42-49`, five fixes key off it). A fenced YAML block with the key list + enumerated values would make S-F1.4's "stated once canonically and **referenced**, not re-specified divergently" mechanically checkable instead of a hand-diff, and let X1/X2/X7's fixtures be validated against the schema rather than hand-fabricated.

**F3-2 · MINOR · Ship the ID-collision check as an oracle, not a promise.** `guarded-change.architect.md:66-68` already mandates word-boundary matching and already records the `TOP`/`HARDSTOP` lesson, and `oracles/ruleid-sitemap.sh` is already planned (`2-plan.md:210-212`). Adding one assertion — "for every ID in METHODOLOGY's index, the token is not a substring of any other word in the corpus" — would have caught `KIL`/`ING` (F1-2) and `ON TOP OF` (F1-1) automatically, and protects cycles 2 and 3 for free.

**F3-3 · NITPICK · Three live baseline IDs are outside both regression criteria.** `TPL1` (`stage-1:19`, `templates/seed/README:13`), `TPL2` (`stage-1:22`, `stage-6:35`, `README:17`) and `SEV` (`stage-5:22`, `stage-4:51`) are used as mnemonic IDs but have **no row** in METHODOLOGY's cross-file rule index (`METHODOLOGY.md:314-333` — 18 rows) and no entry in B0.2's 18-ID map, so R1 and S-SC2 (`1.5-criteria.md:378`) do not protect them. The change edits stage-1, stage-5, stage-6 and templates/seed/README, so erosion is possible and unmeasured. Cheap to add while the index is open anyway.

## Lens 4 — UNSTATED ASSUMPTIONS & RISKS (both conditional lenses fired)

**F4-1 · MAJOR · The artifact's own documented "authoritative" ID-site command does not cover the directories the new IDs are being put in.**
`METHODOLOGY.md:309-312`: "the **authoritative** site set for any ID is `grep -rln -- <ID> SKILL.md METHODOLOGY.md stages/` (the check greps the token, not the column, so the table cannot silently under-list a site)." That command covers neither `templates/` nor `examples/` — yet the index's own rows already cite `templates/seed` as a site (`METHODOLOGY.md:322,330,331`), and this change deliberately puts new IDs there: `DEC` and `TOP`/`APPROVAL.md` at `decomposition-node.md` (S-C2.3, S-F5.2), `DEP` at `decomposition-node.md` + `leaf-task-spec.md` (S-C8), `CNC` at `templates/seed/README.md` (S-C1.1), `CTX` at `examples/…/planning.md` (S-F4.2). S-SC2 (`1.5-criteria.md:381`) asserts that this "authoritative site set = grep the token" statement **"still holds"** — after the change it is false; and the command the criteria actually run (`grep -now` over six paths, per `0-baseline.md:27-28` / `guarded-change.architect.md:66-67`) is a *different* command from the one the skill tells its users to run. A later cycle following `METHODOLOGY:311` silently under-reports every new ID's template/example sites. On no criterion's edit list.

**F4-2 · MAJOR · The closed context set omits the file this run's own config calls the source of truth for settled decisions — so "does this contradict a settled decision?" (a *blocker* in Architect's own severity model) is unverifiable inside the charter's set.**
`guarded-change.architect.md:27-30` makes `/home/zero/.claude/plans/1-this-is-a-proud-scott.md` a `redteam_context` entry: "THE APPROVED SCOPE/DECISION RECORD — source of truth for every settled decision … **Any spec/criteria/plan claim is checked here first**." `3-charter-given.md:30-50` lists six entries and does not include it. `stages/stage-5-gate.md:11,26` rank "a settled decision contradicted" as a **blocker**.
I read it (declared above) and report the result for the record: **no contradiction on assembly direction** — the record settles *decomposition* direction only (`:91` "Large → decompose top-down") and never settles collation direction, while `:118` and `:240` **do** settle ECON ("no single orchestrator's context [scales]"; "holds only **its own subtree's** skeleton + seams + `_status`"), which D12's bottom-up assembly *restores* rather than contradicts — so `2-plan.md:160-165`'s claim is supported. `:92` "Human gate on the top-level decomposition ONLY (Roy): a human approves the first, high-level split" supports D7's "no new human gate". **One undeclared departure:** `:173` fixes `tree/_status.md` as the apex roll-up, and S-C9 (`1.5-criteria.md:343-347`) requires "the baseline ambiguous `tree/_status.md`-as-apex form is **gone**" — a change to the owner-approved on-disk layout recorded nowhere as deliberate. `:175` also settles `_status.md` as "terse done-state + one-line roll-up + gate state", which D1 expands to 13 keys.
Do instead: add the approved-scope record to the reviewers' context set; declare the `tree/_status.md` → `tree/root/_status.md` move in `decisions.md` as a deliberate departure.

**F4-3 · MINOR · Position lens, the element that does not itself change: adding PRV and DIV inside SKILL.md's rule block moves GBP off the block's tail and falsifies the block's own rationale sentence.**
Baseline `SKILL.md:15-41`: rule 1 (CMP/CMP2), rule 2 (PASS1/PASS2/COV/PASS-ORD), rule 3 (GBP), then a parenthetical at `:39-41` naming exactly "**the completeness lens, the two-pass discipline, and gate-before-present**" as the three things placed up front *because these files are prompts*. `2-plan.md:35-38` adds PRV and DIV inside the block and asserts only S-SC3 (block before stage table) afterwards. The displaced element is **GBP** — "the direct gate on the founding failure" (`SKILL.md:36-37`) — which loses the recency slot immediately before Inputs; and `:39-41` becomes an incomplete enumeration of the block it justifies. S-SC3 (`1.5-criteria.md:393-398`) observes only block-vs-table ordering, so intra-block order and the stale rationale are unmeasured. Cheapest fix: put PRV/DIV *before* GBP (PRV qualifies the claim; GBP is the operative gate) and update `:39-41` to enumerate all five.

**F4-4 · MINOR · Concurrency: two accessors of the new shared state are unenumerated.** (a) `<node>/_seamcheck.md` (introduced `2-plan.md:81`) is written at each decomposing node during assembly and read by the parent — **no row** in the accessor table and no writer named. (b) The cross-run catalog lock has a break rule — "a stale lock whose pid is dead may be broken **only with a logged entry**" (`2-plan.md:244`) — but the log is unnamed, and the plan's own partition makes `plan/decisions.md` top-orchestrator-only *per run*: a second run's top orchestrator breaking the lock writes the entry into **its own** run-root, invisible to the run whose lock was broken. S-C1 (`1.5-criteria.md:248-266`) asserts the lock exists; nothing observes the break path.

## Lens 5 — FIDELITY (terms pinned, per the earned-clean requirement)

| loaded term (site) | mechanism pinned from owner intent / source | artifact implements that, or a proxy? |
|---|---|---|
| "human gate" (`1-spec.md:143`, D7) | `1-this-is-a-proud-scott.md:92` "a human approves the first, high-level split (Roy)"; `FINDINGS.md:70-78` demands owner-verbatim + durable source | **the mechanism.** D7 keeps the gate at the top split, removes the runner as writer, requires owner-verbatim + a durable source the runner did not author. No new gate. ✓ |
| "3 independent cold agents" / "independent" (`charter.md:127-129`) | `FINDINGS.md:92-95`: decontamination, explicitly *not* blind-spot diversity | **partly a proxy.** `2-plan.md:140` honestly states DIV "buys **decorrelation, not independence**" — but the default path collapses frame (B) into (A): **F1-4**. |
| "proven" (`SKILL.md:3`, `README:10`) | `FINDINGS.md:89-99`: the gate proves a decontaminated review occurred, not completeness | **the mechanism.** D8's two-halved PRV states both. Budget checked: baseline description = **956 chars, 0 angle brackets**; the removed clause is 69 chars ⇒ **136 chars** of room for the replacement (1024−(956−69)). Feasible but tight — S-SC1 must be *run* after the description edit, not assumed. |
| "resolved" (`stage-5:16`) | `FINDINGS.md:112-115`: today an *unreviewed author edit*, contradicting "nothing self-certifies" (`stage-3:48`) | **the mechanism.** D11's three arms; (a) is a declared bounded exception and `1.5-criteria.md:238` requires the text to say so. ✓ |
| "join" / "blocks on children" | `FINDINGS.md:35-44`: a parent that *waits* and detects a **dead** child (live branch-B failure) | **the mechanism.** D3: "returned without a terminal `_status.md` is **DEAD, not done** — files win (RST)". ✓ |
| "modelled on RAT1" (`1-spec.md:96`) | `Guarded_change/stages/stage-3.md:89-111` | **a narrowed copy** — the partial/adjacent → re-ask clause is dropped: **F1-10**. |
| "blind coordinators" (`1-spec.md:159-161`) | `Data-Distiller/METHODOLOGY.md:107-110`; `README.md:71` "Blindness is a property of the file layout, not operator discipline" | **accurate.** Architect deliberately rejects blindness (`stage-6:51-54` "Blindness is **not** the goal"), and the spec claims only that ECON's bound is where the drop shows. ✓ |
| "charter-fork precedent" (`1-spec.md:162`) | `Dragonfly/stages/charter.md:8` "forked from `Guarded_change/stages/charter.md @ 3d6889b`" | **accurate**; and Architect's own fork sha256 `0e73bacf…` verified byte-identical today. ✓ (its ADDED list going stale = **F1-8**) |

**F5-1 · MINOR · D14 resolves the family's founding rule for the shared catalog into a cold review, without recording it as an orchestrator call.** `2-plan.md:174-179`: "a cold review satisfies it; requiring a human here would add a human gate, which is not this runner's call (cf. F8)." The reading is defensible and correctly refuses to pre-shape F8 — but the artifact being committed lands in a **cross-project, user-space git repo** shared with future runs of *other* projects (`templates/seed/README.md:3-6`), a different risk class from an in-run artifact, and the owner has never been asked. Record it in `decisions.md` as an orchestrator call with the alternative named (stage and leave uncommitted; the owner commits), rather than settling it inside the plan prose.

---

## COVERAGE CHALLENGE

**C1 · MAJOR — the seam-reopen cascade and total fan-out.** Scenario: a 3-level tree; one leaf's seam changes ⇒ its parent re-runs 6 cold agents; if `seam_rev` propagates, the grandparent re-runs 6, the root re-runs 6, and each re-gate invalidates the children's parent-plan context (F1-3). No criterion counts agents, bounds reopens, or asserts termination — and `2-plan.md:189-191` explicitly declines a budget. See F2-1.

**C2 · MAJOR — whether a runner actually *performs* the duties only a grep observes.** Gating criteria with **no** execution arm: S-F4/CTX, S-C1/CNC, S-C3/XPM, S-C4/ING, S-C5, S-C6, S-C7, S-C8/DEP, S-C9, S-C10, and the PRV half of S-F7. The three with the widest behaviour gap:
- **S-C6** (spot-verify duty): pure behaviour. A grep confirms the sentence exists — which is the baseline defect ("the duty is stated and assigned to no stage", `charter:88-92`) one step removed. Scenario: the sentence is present at `stage-5`, and no runner ever opens a cited line; the gate log records "spot-verify: ok".
- **S-C4/ING**: whether ingest emits `ABSENT` marks and labels architect-authored fill instead of silently inventing — the mode the dogfood itself ran in (`FINDINGS.md:134`). Scenario: a draft missing §4 is ingested; the runner writes a plausible §4 unmarked; the completeness critic inherits it as given and the founding failure ships. Grep-only.
- **S-F4/CTX**: whether an absent `redteam_context` actually **stops the run** (`1.5-criteria.md:124-125`) rather than the run proceeding docs-only — F4's live consequence. Cheapest fix: one more X- arm (a config with no `redteam_context` ⇒ required verdict "config error, stop"; two-file fixture).

**C3 · MINOR — restart *during* the new join.** S-F3 amends stage-done for review records, but nothing covers a HARDSTOP while a parent is in the 6.5 poll loop. On resume, a child with a non-terminal `_status.md` is indistinguishable between "not planned yet", "in flight" and "dead": D3's dead-child test keys off "the owner returned", which is **not on disk**. Scenario: the session dies mid-poll; the resuming orchestrator either re-dispatches a live child (two writers to a single-writer file, defeating D1's partition) or waits forever. X1's fixture is static and includes no restart.

**C4 · MINOR — intra-block position in `SKILL.md`** (F4-3). **C5 · MINOR — `_seamcheck.md` and the lock-break path** (F4-4).

**C6 · NITPICK — re-sync direction.** S-SC4 asserts `diff -rq` is empty except the non-shipping paths, and the baseline holds (`0-baseline.md:92-94`) so the check is non-vacuous ✓. But this change **adds** a file and **removes** an apex form, and plan step 8 says only "re-sync"; a naive `cp -r` leaves orphans in the live copy. `diff -rq` would catch it — assert the direction explicitly.

## LABEL AUDIT

**Advisory criteria: none exist** (`2-plan.md:268` — "all criteria … are **gating**"). The "relabel a gate advisory" loophole is therefore not used ✓. The inverse risk is F2-3 (a gating criterion dischargeable by declared deferral); the required named-risk-acceptance route *is* present (`1.5-criteria.md:453-455`, `2-plan.md:279`) ✓, satisfying CH9's last bullet.

Per gating criterion — governed path confirmed exercised, and the evidence checked:

| Criterion | Governed path the planned verification exercises | Verdict |
|---|---|---|
| S-F1 | X1 walks a fabricated run tree with a missing-`_status.md` child + a killed sibling — the disk walk a runner performs | **holds**; gap = no in-flight/restart arm (C3) |
| S-F2 | X4 exercises the assembly-time three-way comparison ✓ | **S-F2.2 (reopen) is grep-only** — X4's fixture is static, so the `seam_rev`-triggered reopen is never executed ⇒ treat S-F2.2 as **unverified** |
| S-F3 | X2 compares real sha256s against real records ✓ | **holds**, but governs less than the finding (F1-3) |
| S-F4 | YAML-key-at-column-0 assertion is a genuinely stronger matcher than a substring hit, and `1.5-criteria.md:130-133` identifies the vacuity trap itself ✓ | **holds structurally**; the "absent ⇒ stop the run" behaviour is unexercised (C2) |
| S-F5 | X3 | **challenged (F1-10)**: discriminates on field presence, not on the audit; no arm spot-verifies a quote against a source ⇒ treat S-F5.4/.6 as **unverified** |
| S-F6 | X1 covers killed-child + parent re-draft ✓ | `plan/ABORTED.md`'s *effect* (run ends, `assembled-plan.md` never written) is grep-only |
| S-F7 | X6 covers frame/spawn-id/contamination detection on the real record shape ✓ | the **PRV** half and the differential frame's *utility* have no arm; F1-4 says the default path is degenerate. Description budget measured: 136 chars of headroom |
| S-F9 | X6 exercises all three defects ✓ | **holds** |
| S-F10 | X7 exercises the traceability test on a real `_status.md` + logged edit ✓ | **holds** |
| S-C1…S-C10 | grep-only, all gating | C2. **S-C10's extraction predicate is unpinned**: headings + spine enumerations ⇒ 6 sites / **5** distinct strings (matching the self-test); *any* occurrence ⇒ adds `stage-3:43` and `METHODOLOGY:322` ("Outputs & artifacts with locations") ⇒ **6** distinct and the self-test's "5" is wrong. S-C10's own site list (`1.5-criteria.md:355-357`) *includes* `stage-3` (prose, not a heading) but *excludes* `METHODOLOGY:322` — so it is unsatisfiable under the broad predicate and cannot cover stage-3 under the narrow one. Pin it. |
| S-SC1 | `quick_validate.py` verified to exist (path in the declaration above, outside the closed set); own self-test (injected `<` + 1100 chars) ✓ | **holds** |
| S-SC2 | word-boundary matcher + index-row + hand-diff | **challenged**: F4-1 (the "still holds" clause becomes false), F1-2 (KIL/ING), F1-1 (self-test misses the surviving `ON TOP OF` phantom) ⇒ **unverified** |
| S-SC3 | real line-offset comparison, self-tested against a swapped variant ✓ | **holds but too narrow** (F4-3) |
| S-SC4 | `diff -rq` before **and** after the re-sync — shown able to fire ✓; non-vacuous at baseline ✓ | **holds** |
| R1 | word-boundary site map vs. B0.2 | **fails its own baseline replay** (F1-1) ⇒ **unverified** until B0.2 is recaptured |
| R2 | per-old-site positive + normalized absence | **challenged**: enumeration inconsistent across three documents and under-inclusive (F1-6, F1-5) |
| X1–X7 | holed/intact discrimination with separately-spawned agents; "both arms same verdict ⇒ `verified = no`" is a real discrimination guard ✓; degraded-mode declared up front ✓ | **X5's arithmetic verified**: 36/40 = 0.90 and 33/36 = 0.917 (both ≥0.8 ⇒ trips); 12/40 = 0.30 and 4/12 = 0.33 (⇒ does not). X3 challenged (F1-10) |

## RATIFICATION AUDIT

**No recorded owner-ruling is relied on anywhere in the spec, criteria or plan**, and here is the evidence. The only owner text in the closed set is the verbatim directive at `LOOP-STATE.md:3-6` and the restart authorization at `:22-24` — both quoted verbatim with a timestamp. The orchestrator calls at `LOOP-STATE.md:16-21` are explicitly labelled "**NOT owner questions**", and the spec/criteria/plan never cite them as authority. The single queued owner question (F8) is correctly left unimplemented: `1-spec.md:116-119` declares it out of scope, `1.5-criteria.md:461-464` refuses to write a criterion for it ("writing a criterion for it would be pre-shaping the owner's ruling"), `2-plan.md:266` routes any F8-touching finding to HALT + verbatim relay, and `2-plan.md:112-113` states TOP's fix leaves F8 untouched. **I found nothing that implements, pre-shapes or forecloses F8** — and D14 (`2-plan.md:177-179`) explicitly declines to add a human gate *because* that is F8's territory. Scope fidelity: `LOOP-STATE.md:50-64`'s cycle-1 scope matches `1-spec.md:89-112` item for item, and the three Tier-3 items outside it are **declared, not silently dropped** (`1-spec.md:120-123`). No refuted finding from `FINDINGS.md:145-159` is re-fixed: "nested spawn may be impossible" is absent from the plan; "no enumerated rule-IDs" is treated as already resolved; "no resume story" is not re-opened (the stage-8 edit is F3/BIND, a genuine finding); the Verification-#7 position hit is handled by re-asserting S7 as S-SC3, which is required because this change *adds* to that block.

Two **CH12-class** observations on the elaboration of the ratified directive (both live in `LOOP-STATE.md`, which the spec treats as the scope authority):

**RAT-1 · MINOR — the termination axis is narrowed beyond the ratified words.** Owner, verbatim (`LOOP-STATE.md:4-6`): *"repeat the loop three times or **until nothing surfaces** (whichever happens first)."* Elaboration (`LOOP-STATE.md:8-10`): *"**Terminate** when a cycle's self-review surfaces **no new blocker or major**."* "Nothing surfaces" does not entail "no blocker or major": under the elaboration a cycle surfacing four minors **terminates the loop**, which the ratified phrase does not license. That is an operative commitment (when the loop stops) absent from and not entailed by the ratified text. Re-ask the axis, or record the narrowing as an orchestrator call rather than folding it into the loop definition.

**RAT-2 · NITPICK — the scope breadth is an interpretation, honestly labelled at source but not carried forward.** "fix **that**" (`LOOP-STATE.md:4`) is expanded to the full ten-finding + thirteen-Tier-3 set (`:12-15`). `LOOP-STATE.md:12` labels it "Interpretation of 'fix that' (**stated so Roy can correct it**)" ✓ — correctly flagged as a claim, not a ruling. `1-spec.md:120` then calls it "the approved cycle-1 scope" without carrying the label. Carry the label.

**Durable-source spot-check performed:** the one verbatim-source claim inside the artifact — `stages/charter.md:11-12`'s fork provenance, "`Guarded_change/stages/charter.md @ 8d73e5d` (sha256 `0e73bacf3af87d8e852e3a9723deda8cdd54f102de54af3880456f7024adc590`)" — is **byte-identical** to `sha256sum <WT>/Guarded_change/stages/charter.md` today. ✓

## RANKED SUMMARY

| # | ID | Sev | One line |
|---|---|---|---|
| 1 | **F1-1** | Blocker-adjacent **MAJOR** | B0.2's TOP row + measurement caveat are wrong under the mandated matcher (`stage-8` is a `HARDSTOP` phantom; `ON TOP OF` survives `-w`) ⇒ **R1 fails its own baseline replay** |
| 2 | **F1-2** | **MAJOR** | `KIL` ⊂ `SKILL` (21 hits, 4 files) and `ING` ⊂ `PLANNING`/`RULING` violate `guarded-change.architect.md:114-116`; rename before the IDs are frozen |
| 3 | **F1-3** | **MAJOR** | BIND narrows a per-context-file detector to one file; the SEAM reopen makes every child's review bind to a superseded **parent** plan, undetected |
| 4 | **F1-4** | **MAJOR** | DIV's differential frame collapses into the spine-anchored frame on its declared default (the seed skeletons carry **no** Layer-2 sections) — the F7 defect one level up |
| 5 | **F2-1** | **MAJOR** | SEAM reopen has no propagation rule and no termination, while the plan explicitly refuses any bound |
| 6 | **F4-1** | **MAJOR** | `METHODOLOGY:311`'s "authoritative" ID grep omits `templates/`+`examples/`, where 5 of the new IDs live; S-SC2's "still holds" becomes false |
| 7 | **F4-2** | **MAJOR** | The reviewers' closed set omits the approved decision record the config calls source-of-truth ⇒ settled-decision checks unverifiable; one undeclared departure found (`tree/_status.md` apex) |
| 8 | **C2** | **MAJOR** | 11 gating criteria (notably S-C6, S-C4/ING, S-F4/CTX) verified only by grep — no execution arm on paths that are purely behavioural |
| 9 | **F1-5** | MINOR | P10 omits `SKILL.md:8-9` and `:17`; the overclaim is at 8 sites, not 5 |
| 10 | **F1-6** | MINOR | R2's *Change* set enumerated 3 incompatible ways; omits P2, P5, P13 |
| 11 | **F1-7** | MINOR | Accessor table misses `index.md` writers at `stage-6:11-12`, `METHODOLOGY:195`, `templates/seed/README:14` |
| 12 | **F1-8** | MINOR | The charter's own fork-provenance ADDED list goes stale, breaking a shipped Layer-2 required section |
| 13 | **F1-9** | MINOR | S-C5's "2 of 3" is wrong (3 of 3 lack the slot heading) and `1-spec.md:196` doesn't assign the fix to `generic-node.md` |
| 14 | **F1-10** | MINOR | The RAT1 copy drops the partial/adjacent → re-ask clause; X3 tests field presence, not the audit |
| 15 | **F4-3** | MINOR | Adding PRV/DIV displaces GBP off the rule block's tail and falsifies `SKILL.md:39-41`; S-SC3 doesn't see it |
| 16 | **F4-4** | MINOR | `_seamcheck.md` and the catalog lock-break log are unenumerated accessors |
| 17 | **F2-2** | MINOR | Block-and-poll vs. reopen can be simultaneously obligatory; unspecified and untested |
| 18 | **F2-3** | MINOR | "All gating" vs. the declared deferral route — needs a third label |
| 19 | **F5-1** | MINOR | D14's "a cold review satisfies the founding rule" for a cross-project repo should be a logged orchestrator call |
| 20 | **C3** | MINOR | Restart during the 6.5 poll loop: dead vs. in-flight is not on disk |
| 21 | **RAT-1** | MINOR | "until nothing surfaces" elaborated to "no new blocker or major" — unratified narrowing |
| 22 | **F3-1/F3-2/F3-3** | MINOR/NITPICK | Machine-parsable `_status.md` schema; ship the collision check as an oracle; index `TPL1`/`TPL2`/`SEV` |
| 23 | **F1-11, C4-C6, RAT-2** | NITPICK | Citation drift in B0.3 (no fabrication found); re-sync direction; carry the "interpretation" label |

**WORST SEVERITY: major**
