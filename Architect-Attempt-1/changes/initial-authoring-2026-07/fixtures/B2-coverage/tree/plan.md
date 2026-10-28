# ROOT plan node: extract user-auth from the monolith into a standalone auth service

**Altitude:** ROOT (owns the top-level split + the seams between the two children).
**Template:** decomposition-node. **Granularity:** decompose into 2 children.

## 1. Problem / intent
Move authentication out of the PHP monolith into a standalone Go auth service so auth can scale and be
reused. The monolith stops authenticating in-process and instead calls the auth service.

## 2. Approach
Two branches: (A) build the standalone auth service; (B) adapt the monolith to delegate to it. Run both
in production during a cutover window, then remove the monolith's in-process auth.

## 3. Interfaces & seams
- Root ↔ consumer: the assembled plan is handed to an implementer.
- **Seams between the two children (this node owns these):**
  - `POST /auth/login` and `POST /auth/validate` HTTP contract between the monolith (B) and the auth
    service (A): request/response JSON shapes, status codes, timeouts.
  <!-- PLANTED SEAM HOLE: the token FORMAT + SIGNING-KEY contract between A (issuer) and B (validator)
       is NOT specified. A issues session tokens; B must validate them. Nothing here pins the token
       encoding (JWT? opaque?), the signing algorithm, or how the shared signing key is distributed and
       rotated. Child A's leaf review sees only "issue a token"; child B's sees only "validate a token";
       neither owns the agreement BETWEEN them. This is the parent's seam to catch. -->

## 4. Outputs & artifacts (with their locations)
- Root deliverable: `assembled-plan.md` at the run root, collating both branches.
- Child A outputs under the new `auth-service/` repo; child B outputs as a diff to the monolith repo
  (paths pinned in each child's leaf spec).
- A migration runbook at `docs/runbooks/auth-extraction.md`.

<!-- PLANTED ROOT HOLE: there is NO §5 "Failure modes & contingencies" at the ROOT altitude. The
     migration-wide failure mode — what the monolith does when the auth service is UNREACHABLE during or
     after cutover (fail closed = lock everyone out, vs fail open = security hole) — is unaddressed.
     This is a root-altitude contingency, not a single child's. A leaf-only review of A or B would not
     surface it. -->

## 6. State / restart story
The migration proceeds in ordered steps recorded in the runbook; each step is independently revertible
until the final cutover.

## 7. Verification
End-to-end: a user logs in via the monolith, which delegates to the auth service, and reaches a
protected page; load parity with the pre-migration baseline.

## Layer-2 required sections
### Cutover & dual-run
During cutover the monolith calls the auth service for new logins while existing sessions remain valid;
traffic shifts 10% → 50% → 100% behind a flag; the in-process auth path is removed only after 100%.

## Children (decomposition)
- **child-A — build the standalone auth service** (leaf): implements `/auth/login`, `/auth/validate`,
  issues session tokens, backs onto the users table.
- **child-B — adapt the monolith to delegate to the auth service** (leaf): replaces in-process auth
  calls with HTTP calls to the auth service; validates returned tokens.
