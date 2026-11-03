# LEAF task-spec: adapt the monolith to delegate to the auth service (child-B)

**Altitude:** leaf. **Parent seam owned by ROOT.**

## 1. Problem / intent
Replace the monolith's in-process authentication with HTTP calls to the auth service.
## 2. Approach
Swap the monolith's `authenticate()` for a client that calls `/auth/login` and validates tokens via
`/auth/validate`; keep the session-cookie plumbing.
## 3. Interfaces & seams
Calls the auth service over HTTP. Validates returned tokens. The exact token contract it must validate
against is owned by the ROOT node's seam.
## 4. Outputs & artifacts (with their locations)
Diff to the monolith repo: `lib/auth/RemoteAuth.php`, wired into the existing login controller.
## 5. Failure modes & contingencies
Timeout calling auth service → retry once. (Note: the monolith-wide policy for a *sustained* auth-service
outage is a ROOT-altitude decision, not set here.)
## 6. State / restart story
No new durable state in the monolith; sessions continue via the existing cookie store.
## 7. Verification
Integration test: login through the monolith reaches a protected page via the auth service.

**Granularity:** leaf.
