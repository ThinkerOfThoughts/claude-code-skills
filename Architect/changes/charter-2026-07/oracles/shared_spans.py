#!/usr/bin/env python3
"""shared_spans.py — the N-06 NEGATIVE assertion the rule table structurally could not express.

ruleplace.sh asserts, per file, that a rule IS stated where it must be. Every one of those probes is
POSITIVE. The composition rule the whole split rests on is a NEGATIVE property — "a role file never
restates a rule the common core states" — and no set of positive per-file assertions can see its
violation. That is why ruleplace.sh passed 76/0 on a set carrying eight duplications.

This computes the maximal shared normalized word-spans of length >= N between charter-common.md and each
role file, and between role files. The declared B18 duplication is the one allowed pair and is passed in
as an explicit exemption, so the exemption is visible rather than silent.

Usage: shared_spans.py <set-dir> [min-words] [--exempt-file <path>]
Exit:  0 = no undeclared shared span found
       1 = at least one undeclared shared span found
       2 = usage error   (deliberately distinct from 0)
"""
import sys, os, re, json

COMMON = "charter-common.md"
ROLES = ["redteam.md", "redteam-plan.md", "redteam-split.md", "divider.md",
         "combiner.md", "leaf.md", "node.md"]


def norm_words(path):
    """Normalize the same way ruleplace.sh does, then split to words.

    Markdown emphasis and code markers are stripped, blockquote and list leaders are dropped, and line
    breaks are flattened, because a duplicated rule that wraps differently in two files is still a
    duplicated rule. '_' is NOT stripped: it is an identifier character in this spec (Human_gate,
    work_queue, node_id, Memo_read), and stripping it as an emphasis marker produced five false absences
    the first time this project tried.
    """
    out = []
    with open(path) as fh:
        for line in fh:
            line = re.sub(r"^> ?", "", line)
            line = re.sub(r"^ *[-|] *", "", line)
            line = line.replace("*", "").replace("`", "")
            out.append(line)
    text = " ".join(out)
    text = re.sub(r"[^\w\s]", " ", text)          # punctuation is not evidence of a distinct rule
    return [w for w in text.lower().split() if w]


def shared_spans(a, b, n):
    """Every maximal common word-span of length >= n. Suffix-free: a span contained in a longer
    reported span is not reported again."""
    index = {}
    for i in range(len(b) - n + 1):
        index.setdefault(tuple(b[i:i + n]), []).append(i)
    found, i = [], 0
    while i <= len(a) - n:
        key = tuple(a[i:i + n])
        best = 0
        for j in index.get(key, []):
            k = n
            while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                k += 1
            best = max(best, k)
        if best:
            found.append((i, best, " ".join(a[i:i + best])))
            i += best            # maximal-only: do not re-report the tail of a span already reported
        else:
            i += 1
    return found


def main():
    if len(sys.argv) < 2:
        sys.stderr.write(__doc__)
        return 2
    setdir = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 7
    exempt = []
    if "--exempt-file" in sys.argv:
        p = sys.argv[sys.argv.index("--exempt-file") + 1]
        with open(p) as fh:
            exempt = [json.loads(l) for l in fh if l.strip() and not l.startswith("#")]
    if not os.path.isdir(setdir):
        sys.stderr.write("not a directory: %s\n" % setdir)
        return 2

    words = {f: norm_words(os.path.join(setdir, f)) for f in [COMMON] + ROLES
             if os.path.isfile(os.path.join(setdir, f))}
    if COMMON not in words:
        sys.stderr.write("no %s in %s\n" % (COMMON, setdir))
        return 2

    # An exemption is scoped to the PAIR of files it was declared for, not granted globally. Without
    # this, re-adding a declared span to a THIRD file would be silently legal — the mutation test caught
    # exactly that.
    exempt_norm = [(" ".join(norm_words_str(e["span"])), set(e.get("sites") or [])) for e in exempt]
    violations = 0
    pairs = [(COMMON, r) for r in ROLES if r in words]
    pairs += [(a, b) for i, a in enumerate(ROLES) for b in ROLES[i + 1:]
              if a in words and b in words]
    for a, b in pairs:
        for _, ln, span in shared_spans(words[a], words[b], n):
            hit = None
            for e, sites in exempt_norm:
                if span in e or e in span:
                    if sites and not {a, b} <= sites:
                        continue          # declared, but not for THIS pair of files
                    hit = True
                    break
            if hit:
                print("EXEMPT  %-18s ~ %-14s %2dw  %s" % (a, b, ln, span))
                continue
            print("SHARED  %-18s ~ %-14s %2dw  %s" % (a, b, ln, span))
            violations += 1
    print("==== %d undeclared shared spans of >= %d words ====" % (violations, n))
    return 1 if violations else 0


def norm_words_str(s):
    s = s.replace("*", "").replace("`", "")
    s = re.sub(r"[^\w\s]", " ", s)
    return [w for w in s.lower().split() if w]


if __name__ == "__main__":
    sys.exit(main())
