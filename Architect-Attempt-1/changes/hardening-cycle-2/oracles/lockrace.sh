#!/usr/bin/env bash
# lockrace.sh — the EXECUTED test for the catalog lock. Reviewer E proved pass 2's design broken:
# a SIGKILLed holder LEAKED the lock (a trap cannot run on SIGKILL, and an Architect HARDSTOP *is* a kill),
# and the H4 "unguarded control" passed without the lock (sub-PIPE_BUF appends are atomic).
# THE DESIGN WAS CHANGED, not just the script:
#   * the lock is an ATOMIC SYMLINK whose TARGET IS THE HOLDER'S PID  -> lock and owner appear in ONE
#     indivisible step, closing pass 2's mkdir-then-write-pid window (D/5);
#   * a lock whose target pid is NOT ALIVE is STALE BY DEFINITION and any run may remove it -> a killed
#     holder cannot deadlock the next run, and no manual BROKEN-BY dance is needed (E/4);
#   * the lock is a SIBLING of the catalog, so a first run (no catalog dir) can still take it.
# The control is a genuine READ-MODIFY-WRITE (a lost update), not an atomic append.
set -uo pipefail
T="${1:-$(mktemp -d)}"; CAT="$T/catalog"; LOCK="$T/catalog.lock"; rm -rf "$T"; mkdir -p "$T"
acquire(){ ln -s "$$" "$LOCK" 2>/dev/null && return 0
           local p; p=$(readlink "$LOCK" 2>/dev/null) || return 1
           if [ -n "${p:-}" ] && ! kill -0 "$p" 2>/dev/null; then rm -f "$LOCK"; ln -s "$$" "$LOCK" 2>/dev/null && { echo "  (broke stale lock of dead pid $p)" >&2; return 0; }; fi
           return 1; }
release(){ [ "$(readlink "$LOCK" 2>/dev/null)" = "$$" ] && rm -f "$LOCK"; }
fail=0
echo "== CASE 1: two concurrent contenders, first run, catalog dir absent"
( acquire && echo A-WON || echo A-LOST ) > "$T/a" & ( acquire && echo B-WON || echo B-LOST ) > "$T/b" & wait
w=$(grep -c WON "$T/a" "$T/b" | awk -F: '{n+=$2}END{print n}'); echo "  winners=$w (want exactly 1)"; [ "$w" = 1 ] || fail=1
rm -f "$LOCK"
echo "== CASE 2: holder is SIGKILLed (an Architect HARDSTOP). Pass 2's design LEAKED here."
bash -c 'ln -s $$ "'"$LOCK"'"; kill -9 $$' >/dev/null 2>&1
echo "  lock present after kill: $([ -L "$LOCK" ] && echo yes || echo no)  target pid: $(readlink "$LOCK" 2>/dev/null)"
if acquire; then echo "  next run ACQUIRED -> NOT deadlocked  [PASS]"; release; else echo "  next run BLOCKED -> DEADLOCK  [FAIL]"; fail=1; fi
echo "== CASE 3: holder is alive -> must NOT be broken"
sleep 300 & LIVE=$!; rm -f "$LOCK"; ln -s "$LIVE" "$LOCK"
if acquire; then echo "  broke a LIVE holder's lock  [FAIL]"; fail=1; else echo "  refused to break a live holder  [PASS]"; fi
kill $LIVE 2>/dev/null; rm -f "$LOCK"
echo "== CASE 4: H4 unguarded control — a genuine READ-MODIFY-WRITE, so it MUST fail without the lock"
rmw(){ local g="$1" i v; for i in $(seq 1 40); do
         if [ "$g" = guarded ]; then until acquire; do :; done; fi
         v=$(cat "$T/n"); sleep 0.002; echo $((v+1)) > "$T/n"
         if [ "$g" = guarded ]; then release; fi; done; }
for g in unguarded guarded; do echo 0 > "$T/n"; rm -f "$LOCK"
  rmw $g & rmw $g & rmw $g & wait; got=$(cat "$T/n")
  if [ "$g" = unguarded ]; then [ "$got" -lt 120 ] && echo "  unguarded: $got/120 — LOST UPDATES, control fails without the guard  [PASS]" || { echo "  unguarded: $got/120 — control passes unguarded, proves nothing  [FAIL]"; fail=1; }
  else [ "$got" = 120 ] && echo "  guarded:   $got/120 — no lost update  [PASS]" || { echo "  guarded:   $got/120 — lock did not protect  [FAIL]"; fail=1; }; fi
done
echo; [ $fail -eq 0 ] && echo "LOCKRACE: ALL 4 CASES PASS" || echo "LOCKRACE: FAILURES PRESENT"; exit $fail
