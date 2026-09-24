#!/usr/bin/env bash
# ORACLE-IDCOLLIDE — the mnemonic-rule-ID naming rule, as an instrument.
#
# RULE (Layer-2 config, guarded-change.architect.md): "A new ID must be a standalone uppercase token
# that is not a substring of another ID or of an ordinary uppercase corpus word."
#
# TWO STATED EXEMPTION CLASSES — both explicit, both reported, never silent:
#  (1) FAMILY  — a shorter ID deliberately the stem of a longer one (CMP<CMP2, TPL<TPL1/2/3). These are
#                intentional families; without this exemption the oracle would flag the baseline corpus
#                wholesale and be useless. A checker that fails everything is no more an oracle than one
#                that passes everything.
#  (2) GRANDFATHERED — pre-existing baseline IDs that violate the rule and are NOT renamed by this
#                cycle (out of scope). Listed by name so the debt is visible, not hidden. NEW ids get
#                no grandfathering.
# Everything else is a COLLISION and exits non-zero.
#
# Usage: idcollide.sh <tree-root> [id ...]     ids default to METHODOLOGY's cross-file index rows
set -uo pipefail
ROOT="${1:?tree root}"; shift || true
cd "$ROOT" || exit 2
FILES=(SKILL.md METHODOLOGY.md README.md)
for d in stages templates examples; do [ -d "$d" ] && while IFS= read -r f; do FILES+=("$f"); done < <(find "$d" -name '*.md'|sort); done

if [ "$#" -gt 0 ]; then IDS=("$@"); else
  mapfile -t IDS < <(grep -oE '^\| \*\*[A-Z][A-Z0-9-]*\*\*' METHODOLOGY.md | sed 's/^| \*\*//; s/\*\*$//' | sort -u)
fi

FAMILY="CMP CMP2|TPL TPL1|TPL TPL2|TPL TPL3"
# GRANDFATHERED: baseline IDs this cycle does not rename. Both are word-boundary-SAFE except the
# file-level 'ON TOP OF' phantom, which ruleid-sitemap.sh excludes and REPORTS.
# GRANDFATHERED: ONLY tokens that ACTUALLY EXIST in the baseline corpus. Pre-blessing a token that is
# absent at baseline (pass 2 did this with TOPGATE and DECOMPOSITION) lets a NEW collision through, so
# those two pairs were DELETED after reviewer E demonstrated the leak by adding TOPGATE as a live token.
GRAND="DEC DECOMPOSE|DEC DECOMPOSES|TOP HARDSTOP|TOP TOP-LEVEL"
in_list() { echo "$2" | tr '|' '\n' | grep -qx "$1"; }

mapfile -t TOKENS < <(cat "${FILES[@]}" | grep -oE '\b[A-Z][A-Z0-9_-]{1,}\b' | sort -u)

rc=0
for id in "${IDS[@]}"; do
  for tok in "${TOKENS[@]}"; do
    [ "$tok" = "$id" ] && continue
    case "$tok" in *"$id"*) : ;; *) continue ;; esac
    if   in_list "$id $tok" "$FAMILY"; then echo "exempt-family   : $id  <  $tok"
    elif in_list "$id $tok" "$GRAND";  then echo "grandfathered   : $id  <  $tok   (baseline debt, not renamed this cycle)"
    else echo "COLLISION       : $id  is a substring of  $tok"; rc=1; fi
  done
done
[ $rc -eq 0 ] && echo "IDCOLLIDE: OK (${#IDS[@]} ids vs ${#TOKENS[@]} corpus tokens)"
exit $rc
