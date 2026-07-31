# B4 fixture — scale-up: recursive decomposition + top-level human gate ONLY

**Fabricated large task:** "Re-platform a monolithic e-commerce app onto a microservices architecture"
— large enough to decompose recursively to atomic leaves.

## Layer-2 (fabricated)
```yaml
plan_type: replatform
scale_context: |
  Large. Expect recursive top-down decomposition into atomic agent-executable leaves; the top-level
  split hits the human decomposition gate; deeper splits proceed red-team-gated, autonomous.
required_sections: []
```

## Expected run tree (the observable)
```
run-root/
├─ plan/
│  ├─ topgate/                    ← the TOP-LEVEL decomposition approval artifact (disk gate)
│  └─ decisions.md                ← top-level split approval + deeper-split routes
└─ tree/                          ← ROOT
   ├─ plan.md                     ← root plan: decompose into {catalog, checkout, fulfilment}
   ├─ checkout/                   ← branch (own sub-orchestrator)
   │  ├─ plan.md                  ← decomposes further (DEEPER split — NO human gate)
   │  ├─ cart-svc/plan.md         ← leaf (atomic task-spec)
   │  └─ payment-svc/plan.md      ← leaf (atomic task-spec)
   ├─ catalog/  …                 ← branch
   └─ fulfilment/ …               ← branch
```

## What B4 asserts (oracle) and how the harness verifies it (via the skill's TOP rule)
1. **(a) Top-level dispatch is BLOCKED until `plan/topgate/` exists.** Per stage-6 step 3 (TOP): a
   DECOMPOSE at the TOP-LEVEL split blocks dispatch until the human approval artifact exists on disk at
   `plan/topgate/`; requesting it is a stop-for-human (RAT3).
2. **(b) At least one DEEPER split proceeds red-team-gated with NO human stop.** Per stage-6 step 4
   (TOP): deeper splits (`checkout/` → {cart-svc, payment-svc}) proceed autonomous, no `topgate/`
   required — "the gate fires at the top ONLY, and explicitly does not fire deeper."
3. **(c) Leaves are atomic agent-executable task specs.** `cart-svc/plan.md`, `payment-svc/plan.md`
   collapse the spine to one-agent task specs.

## Oracle-can-fail (discrimination)
- **`topgate/` withheld → dispatch stays BLOCKED** (see `topgate-absent/` state below); **`topgate/`
  supplied → dispatch proceeds** (see `topgate-present/`). The gate actually blocks.
- **A deeper split does NOT manufacture a spurious human stop** — `checkout/` decomposes with only
  red-team gates. (If the gate fired at every level, a large tree would deadlock on human approvals;
  it does not.)

## Two disk states the harness compares (the TOP gate is a path check)
- `topgate-absent/`  → `plan/topgate/` does NOT exist → per TOP, sub-orchestrator dispatch is blocked.
- `topgate-present/` → `plan/topgate/APPROVED.md` exists → per TOP, dispatch is released.
