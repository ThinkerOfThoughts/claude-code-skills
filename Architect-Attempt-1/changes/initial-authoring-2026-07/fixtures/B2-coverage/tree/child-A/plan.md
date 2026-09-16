# LEAF task-spec: build the standalone auth service (child-A)

**Altitude:** leaf. **Parent seam owned by ROOT.**

## 1. Problem / intent
Build a Go auth service exposing `/auth/login` and `/auth/validate`, issuing session tokens.
## 2. Approach
Go HTTP service; bcrypt password check against the users table; issue a session token on success.
## 3. Interfaces & seams
Exposes `/auth/login` (credentials → token) and `/auth/validate` (token → user). Token issuance is
this service's job; the exact cross-service token contract is owned by the ROOT node's seam.
## 4. Outputs & artifacts (with their locations)
`auth-service/` new repo: `cmd/authd/main.go`, `internal/auth/*.go`, `deploy/authd.yaml`.
## 5. Failure modes & contingencies
DB down → 503; bad credentials → 401; rate-limit login attempts.
## 6. State / restart story
Stateless service; tokens self-describe or are looked up in a session store (per ROOT seam decision).
## 7. Verification
Unit + integration tests on login/validate; load test to target RPS.

**Granularity:** leaf.
