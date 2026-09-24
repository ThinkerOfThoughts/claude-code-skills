# Your invocation

You are `Union`. You were called with a vector of TWO inputs. Your caller states that a division was made
and the seam is: *the first input owns argument parsing and flag state; the second owns every command site
that must honour the flag; the first produces the variable `DRY_RUN`, which the second consumes.*

## input 1
1. Open `deploy.sh`.
2. Add `--dry-run` to the argument-parsing case block, setting `DRY_RUN=1`.
3. Default `DRY_RUN=0` above the parse loop.

## input 2
1. Wrap each `rsync` invocation so it echoes instead of runs when `DRY_RUN=1`.
2. Wrap the `systemctl restart` invocation the same way.
3. Print a summary line at exit stating whether this was a dry run.
4. Default `DRY_RUN=0` above the parse loop.
