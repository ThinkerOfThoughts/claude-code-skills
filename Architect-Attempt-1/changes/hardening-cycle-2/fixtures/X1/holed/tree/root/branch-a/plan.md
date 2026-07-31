# Plan node — branch-a
## 1. Problem / intent
Plan the data-import branch.
## 2. Approach
Two sequential steps. elc: 4 (self-declared).
## 3. Interfaces & seams
Consumes the root's schema contract; hands the report branch a normalized table.
## 4. Outputs & artifacts (with their locations)
`out/import/normalized.csv`; the run log at `out/import/run.log`.
## 5. Failure modes & contingencies
Malformed input row -> quarantine file, continue.
## 6. State / restart story
Resumable; done-iff `normalized.csv` exists.
## 7. Verification
Row count matches source minus quarantined.
