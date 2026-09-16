# Layer-2 planning config (fabricated) — B2 coverage fixture

```yaml
plan_type: extract-service

domain_context: |
  The thing being planned: extract user authentication out of an existing PHP monolith into a
  standalone Go "auth service", so the monolith calls the auth service instead of authenticating
  in-process. Both run in production during a cutover. A cold agent judging completeness should know:
  the auth service ISSUES session tokens and the monolith VALIDATES them, so the two sides must agree
  on the exact token format and signing key, and there must be a story for what the monolith does when
  the auth service is unreachable during/after cutover.

scale_context: |
  Medium. Root decomposes into two branches (extract the service; adapt the monolith) plus the seams
  between them. Each branch is a leaf-sized task-spec.

required_sections:
  - "Cutover & dual-run: how both systems run during the migration and how traffic shifts."

catalog: ~/.claude/architect/templates/
off_limits_paths:
  - <the monolith repo>
run_root: <scratch dir OUTSIDE the monolith repo>
```
