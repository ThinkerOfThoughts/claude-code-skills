# ONE definition of the pinned corpus. Sourced by every oracle so no script can narrow it.
# `changes/` is NOT in this list and cannot enter: the list is literal, not a glob over the tree.
CORPUS_FILES="SKILL.md METHODOLOGY.md README.md"
CORPUS_DIRS="stages templates examples"
corpus_paths(){ # <tree-root>
  local r="$1" p
  for p in $CORPUS_FILES; do [ -f "$r/$p" ] && echo "$r/$p"; done
  for p in $CORPUS_DIRS;  do [ -d "$r/$p" ] && find "$r/$p" -name '*.md' | sort; done
}
LIVE_IDS="GBP PASS1 PASS2 PASS-ORD CMP CMP2 SPN COV ORC ECON GRN TOP CAP DEC TPL TPL1 TPL2 TPL3 RST RAT3 SEV"
