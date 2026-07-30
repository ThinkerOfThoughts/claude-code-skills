#!/usr/bin/env python3
"""citecheck.py — N-13's MISSING ARM: is the owner quotation actually AT the record it cites?

Why this exists, and why nothing else could do it. Every other oracle in this run is DOCS-ONLY: they read
the nine files and compare them to each other or to the design spec. Not one can open the session
transcript. So a claim of the form "the owner said X at record N" was structurally outside what any of them
could evaluate -- they can confirm the sentence is PRESENT and CONSISTENT, never that the ADDRESS is right.
The set's own charter names this failure: a docs-only reviewer "can only catch internal inconsistency,
never a plan that is confidently wrong about the world it plans in."

It is not a new criterion. `1.5-criteria-v2.md` N-13 is GATING and already requires RAT1's "owner's
response verbatim with a durable source the author did not author" -- and the same file's coverage table
records, in its own words: "N-13 RAT1/RAT2 | Text presence only | Never had an arm." This is that arm.

MEASURED, not hypothetical. On 2026-07-30 the runner adjudicating pass 4 read the transcript into a
0-indexed list and reported every locus one low, then wrote the discrepancy up as an off-by-one IN THE
CORPUS. Five review rounds, four oracles and 157 mutants had nothing to say about it. The orchestrator
caught it by opening two records by hand. This probe is that hand-check, made mechanical.

Usage: citecheck.py <set-dir> [transcript.jsonl]
Exit:  0 every cited record resolves and every adjacent quotation is present in it
       1 a citation does not resolve, or a quotation is absent from the record it names
       2 usage error
"""
import sys, os, re, json, glob

DEFAULT_JSONL = os.path.expanduser(
    "~/.claude/projects/-home-zero-Desktop-claude-code-skills-"
    "-claude-worktrees-recursing-visvesvaraya-b40a0c/"
    "45cb99a2-543d-4447-a3e3-2a38963b0775.jsonl")

CITE = re.compile(r"record[s]?\s+\*{0,2}(\d{3,5})\*{0,2}", re.I)

# Record kinds that a citation may legitimately name. Derived from what the artifact actually cites:
#   user/user        a genuine owner turn                       (1258, 1449, 2524, 2680, 3119)
#   assistant/*      an orchestrator turn, cited AS one         (1254 the question, 1787 an insertion)
#   attachment/*     an owner-supplied file                     (1044, the original spec)
# Everything else -- system records, pr-link records, tool results, task-notification envelopes -- carries
# no authored text and is never a legitimate citation target. Citing one is always an error.
CITABLE = ("user/user", "assistant/assistant", "attachment/None")
NOTIFICATION = "<task-notification>"


def kind_of(line):
    try:
        r = json.loads(line)
    except Exception:
        return None, ""
    m = r.get("message") or {}
    c = m.get("content")
    text = ""
    if isinstance(c, list):
        text = "".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text")
    elif isinstance(c, str):
        text = c
    return "%s/%s" % (r.get("type"), m.get("role")), text


def main():
    if len(sys.argv) < 2:
        sys.stderr.write(__doc__)
        return 2
    set_dir = sys.argv[1]
    jsonl = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_JSONL
    if not os.path.isdir(set_dir) or not os.path.isfile(jsonl):
        sys.stderr.write("usage: citecheck.py <set-dir> [transcript.jsonl]\n")
        return 2
    lines = open(jsonl).read().split("\n")

    fail = checked = 0
    for path in sorted(glob.glob(os.path.join(set_dir, "*.md"))):
        name = os.path.basename(path)
        for i, ln in enumerate(open(path).read().split("\n"), 1):
            for m in CITE.finditer(ln):
                n = int(m.group(1))
                checked += 1
                idx = n - 1     # 1-BASED: record N is line N. Breaking this is what produced the defect.
                if idx < 0 or idx >= len(lines) or not lines[idx].strip():
                    print("FAIL  N-13/%s:%d  record %d does not exist" % (name, i, n))
                    fail += 1
                    continue
                kind, text = kind_of(lines[idx])
                if kind is None:
                    print("FAIL  N-13/%s:%d  record %d is not parseable" % (name, i, n))
                    fail += 1
                elif kind not in CITABLE:
                    print("FAIL  N-13/%s:%d  record %d is a %s -- carries no authored text, "
                          "never a legitimate citation target" % (name, i, n, kind))
                    fail += 1
                elif NOTIFICATION in text:
                    print("FAIL  N-13/%s:%d  record %d is a task-notification envelope, not an "
                          "authored turn" % (name, i, n))
                    fail += 1
                else:
                    print("PASS  N-13/%s:%d  record %d is a %s" % (name, i, n, kind))
    print("==== citecheck: %d cited records, %d not citable ====" % (checked, fail))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
