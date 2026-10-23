# The task, the plan, and the granularity floor for this invocation

## granularity (the floor)
A step a competent shell user can execute without further planning. Naming a command and its arguments is
at the floor. "How to type the command" is below the floor.

## task
Add a `--dry-run` flag to an existing bash deploy script `deploy.sh`, so that it prints the commands it
would run instead of running them.

## plan (fill this out / review this)
1. Open `deploy.sh`.
2. Add argument parsing for `--dry-run` near the top, setting `DRY_RUN=1`.
3. Handle the deployment.
4. Test it.
