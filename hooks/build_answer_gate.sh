#!/bin/sh
# Registered PreToolUse command for build_answer_gate.py. Fail closed for the gated lane:
# script exit 0 = allow, 10 = deny (JSON on stdout), anything else (crash, timeout, python missing) =
# deny if the input mentions a needle (an address of the gated lane: a substring, or a `re:` ERE that must match a
# target field), else allow. Always exits 0. The script's own scan budget (20 s) is shorter than the 28 s timeout here.
D=$(dirname "$0")
IN=$(cat)
OUT=$(printf '%s' "$IN" | timeout "${BAG_TIMEOUT:-28}" python3 "$D/build_answer_gate.py" hook)
RC=$?
if [ "$RC" -eq 0 ]; then
  exit 0
fi
if [ "$RC" -eq 10 ]; then
  printf '%s\n' "$OUT"
  exit 0
fi
LOG="$D/build_answer_gate.log.jsonl"
HIT=0
LOW=$(printf '%s' "$IN" | tr 'A-Z' 'a-z')
if [ -r "$D/build_answer_gate.needles" ]; then
  while IFS= read -r N; do
    [ -n "$N" ] || continue
    case "$N" in
      re:*) if printf '%s' "$LOW" | grep -Eq -- "${N#re:}"; then HIT=1; break; fi;;
      *) case "$LOW" in *"$N"*) HIT=1; break;; esac;;
    esac
  done < "$D/build_answer_gate.needles"
else
  if printf '%s' "$LOW" | grep -Eq 'local_[0-9a-f]{8}-|uds:/'; then HIT=1; fi
fi
TS=$(date -u +%Y-%m-%dT%H:%M:%S.000+00:00)
if [ "$HIT" -eq 1 ]; then
  printf '{"ts":"%s","verdict":"deny","reason":"wrapper: script crashed or timed out (rc=%s) on gated-looking input","kind":"CRASH"}\n' "$TS" "$RC" >> "$LOG" 2>/dev/null
  printf '%s\n' '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"build_answer_gate: the gate script crashed or timed out and this message mentions the gated build lane, so it is blocked (fail closed). See ~/.claude/hooks/build_answer_gate.log.jsonl and run build_answer_gate.py by hand."}}'
else
  printf '{"ts":"%s","verdict":"allow","reason":"wrapper: script crashed or timed out (rc=%s) on non-gated input","kind":"CRASH"}\n' "$TS" "$RC" >> "$LOG" 2>/dev/null
fi
exit 0
