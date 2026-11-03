#!/usr/bin/env python3
"""sigmatch.py — N-04's MISSING HALF: does each role file's closed set agree with its SIGNATURE?

Why this exists. N-04 is gating and reads: "Each dispatched role file states its own exact input list, and
each list matches its function's signature in ~/Documents/Architect.md." Its four probes were literal
substring `present` checks, ALL FOUR against charter-common.md. Not one read a role file's list; not one
read a signature. So the criterion's operative conjunct had no coverage at all.

Reviewer U (pass 4) and reviewer X (pass 5) both walked through the hole. X's version, verbatim from its
record: append to leaf.md's closed set

    "... and the **granularity floor** - plus your **depth** and your **node_id**, which is what makes
     `Ask_human` available to you."

Spawn_leaf(string task, string plan, string granularity) has neither. And charter-common.md 6 makes the
closed set THE GATE on reaching the owner: "only a role whose closed set (5) contains both may call it."
So one appended clause forges a leaf that can escalate to the human. Both oracles passed it clean.

shared_spans.py structurally CANNOT catch this: a single-file addition duplicates nothing, so there is no
shared span to find. It needs a POSITIVE check against an external source, which is what this is. The
source is the design spec, which the author of the role files does not control unilaterally -- that is the
same "bounded from outside the author" argument the closed-set rule itself rests on.

Usage: sigmatch.py <set-dir> [spec-path]
Exit:  0 all role files agree with their signatures | 1 a disagreement | 2 usage
"""
import sys, os, re

# Which function each dispatched role file is the prompt for. The two aiming files complete redteam.md's
# set, so they answer to the same signature.
ROLE_FN = {
    "leaf.md":          "Spawn_leaf",
    "node.md":          "Spawn_node",
    "divider.md":       "Divisible",
    "redteam.md":       "Spawn_redteam",
    "redteam-plan.md":  "Spawn_redteam",
    "redteam-split.md": "Spawn_redteam",
}
# combiner.md is handled separately: it is ONE file dispatched as three functions, so its closed set is
# the union of Consensus, Union and Severity.
COMBINER_FNS = ["Consensus", "Union", "Severity"]

# The argument names whose presence in a closed set is a claim about the signature. Deliberately a closed
# vocabulary: these are the ones that grant power (node_id/depth gate Ask_human; granularity gates the
# floor). A name not in this list is not checked, and that limit is stated rather than hidden.
WATCHED = ["node_id", "depth", "granularity", "plan", "task", "issues"]


def signatures(spec):
    """name -> set of argument identifiers, parsed from the spec's declarations."""
    out = {}
    for m in re.finditer(r"\b(\w+)\s*\(([^)]*)\)\s*;", spec):
        name, args = m.group(1), m.group(2)
        out.setdefault(name, set()).update(
            re.findall(r"\b_?(\w+)\s*(?:,|$)", args))
    return out


def closed_set_section(text):
    """The ENUMERATION SENTENCE, not the whole section.

    Every dispatched role file states its closed set as a paragraph beginning "Exactly" -- that is the
    convention, and it is what N-04 means by "states its own exact input list". Scoping to it matters in
    both directions, and both were found by running this against the shipped set rather than by reasoning:

      * TOO WIDE gives false positives. divider.md's section continues into a blockquote headed "You
        receive NO PLAN", which MENTIONS `plan` in order to DENY it. A whole-section scan read that denial
        as a claim and failed a correct file.
      * The two aiming files have no "Your inputs" heading at all -- they say "Exactly one thing beyond
        the common list", because they COMPLETE redteam.md's set rather than restating it. Anchoring on
        the heading skipped both of them entirely and reported that as a failure.

    Anchoring on "Exactly" handles all eight dispatched files with one rule.
    """
    m = re.search(r"^\**Exactly\b(.*?)(?=\n\s*\n)", text, re.M | re.S)
    if m:
        return m.group(1)
    # redteam.md alone states a PARTIAL list -- "Common to both kinds: ..." -- because by design it names
    # no artifact and each aiming file completes it. That is the manifest's stated reason for the split,
    # not a missing section, so it is checked on its own partial sentence rather than reported absent.
    m = re.search(r"^\**Common to both kinds\b(.*?)(?=\n\s*\n)", text, re.M | re.S)
    return m.group(1) if m else None


def main():
    if len(sys.argv) < 2:
        sys.stderr.write(__doc__)
        return 2
    set_dir = sys.argv[1]
    spec_p = sys.argv[2] if len(sys.argv) > 2 else os.path.expanduser("~/Documents/Architect.md")
    if not os.path.isdir(set_dir) or not os.path.isfile(spec_p):
        sys.stderr.write("usage: sigmatch.py <set-dir> [spec-path]\n")
        return 2
    sigs = signatures(open(spec_p).read())
    fail = 0
    checked = 0
    for role in sorted(list(ROLE_FN) + ["combiner.md"]):
        p = os.path.join(set_dir, role)
        if not os.path.isfile(p):
            print("FAIL  N-04/%s  role file missing" % role); fail += 1; continue
        sec = closed_set_section(open(p).read())
        if sec is None:
            print("FAIL  N-04/%s  no 'Your inputs (the closed set)' section to check" % role)
            fail += 1; continue
        fns = COMBINER_FNS if role == "combiner.md" else [ROLE_FN[role]]
        missing = [f for f in fns if f not in sigs]
        if missing:
            print("FAIL  N-04/%s  no signature in the spec for %s" % (role, ",".join(missing)))
            fail += 1; continue
        allowed = set().union(*(sigs[f] for f in fns))
        # A closed set may name an argument the signature HAS. Naming one it LACKS is the forgery.
        for arg in WATCHED:
            claimed = re.search(r"(?<![\w-])%s(?![\w])" % re.escape(arg), sec) is not None
            checked += 1
            if claimed and arg not in allowed:
                print("FAIL  N-04/%s  closed set claims '%s', which %s does not take"
                      % (role, arg, "/".join(fns)))
                fail += 1
    print("==== sigmatch: %d closed-set/signature assertions, %d failed ====" % (checked, fail))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
