#!/usr/bin/env python3
"""extract_records.py — recover a subagent's VERBATIM final message from the harness transcript.

Why this exists: a previous runner declared three cold reviews "un-run" because the inline return was
lost, while the full text sat on disk untouched. A later audit found a record titled "verbatim" that was
actually a condensed paraphrase (21,962 chars against the agent's real 28,855). Both failures are avoided
by extracting from the harness's own JSONL rather than by re-typing anything.

The header is built from `agent-<id>.meta.json`, which is written by the harness, so model /
parentAgentId / spawnDepth are FIRST-HAND and not reviewer-reported.

Usage: extract_records.py <out-dir> <TAG>=<agentId> [<TAG>=<agentId> ...]
"""
import sys, os, json

SUB = os.path.expanduser(
    "~/.claude/projects/-home-zero-Desktop-claude-code-skills-"
    "-claude-worktrees-recursing-visvesvaraya-b40a0c/"
    "45cb99a2-543d-4447-a3e3-2a38963b0775/subagents")


def final_text(path):
    """The last assistant message carrying text. Concatenated blocks, nothing dropped."""
    last = None
    with open(path) as fh:
        for line in fh:
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get("type") != "assistant":
                continue
            c = d.get("message", {}).get("content")
            if isinstance(c, list):
                t = "".join(b.get("text", "") for b in c
                            if isinstance(b, dict) and b.get("type") == "text")
                if t.strip():
                    last = t
    return last


def main():
    if len(sys.argv) < 3:
        sys.stderr.write(__doc__)
        return 2
    outdir = sys.argv[1]
    os.makedirs(outdir, exist_ok=True)
    rc = 0
    for pair in sys.argv[2:]:
        tag, aid = pair.split("=", 1)
        meta_p = os.path.join(SUB, "agent-%s.meta.json" % aid)
        jsonl_p = os.path.join(SUB, "agent-%s.jsonl" % aid)
        if not os.path.isfile(jsonl_p):
            print("MISSING  %s  no transcript at %s" % (tag, jsonl_p))
            rc = 1
            continue
        meta = json.load(open(meta_p)) if os.path.isfile(meta_p) else {}
        body = final_text(jsonl_p)
        if not body:
            print("EMPTY    %s  transcript has no assistant text" % tag)
            rc = 1
            continue
        hdr = (
            "# Reviewer %s — VERBATIM final message\n\n"
            "**Extracted from the harness transcript, not re-typed.** Everything below the rule is the\n"
            "agent's own final message, byte for byte.\n\n"
            "| Field | Value | Source |\n|---|---|---|\n"
            "| agentId | `%s` | harness |\n"
            "| agentType | `%s` | `agent-%s.meta.json` |\n"
            "| model | `%s` | `agent-%s.meta.json` |\n"
            "| parentAgentId | `%s` | `agent-%s.meta.json` |\n"
            "| spawnDepth | `%s` | `agent-%s.meta.json` |\n"
            "| transcript | `%s` | harness |\n"
            "| chars | %d | measured |\n\n"
            "**These identity fields are FIRST-HAND** — read from the harness's own sidecar, not from\n"
            "anything the reviewer said about itself.\n\n---\n\n"
            % (tag, aid, meta.get("agentType"), aid, meta.get("model"), aid,
               meta.get("parentAgentId"), aid, meta.get("spawnDepth"), aid,
               jsonl_p, len(body)))
        out = os.path.join(outdir, "reviewer-%s-verbatim.md" % tag)
        with open(out, "w") as fh:
            fh.write(hdr + body)
        print("WROTE    %s  %d chars  -> %s" % (tag, len(body), out))
    return rc


if __name__ == "__main__":
    sys.exit(main())
