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

SUB = os.environ.get("EXTRACT_SUB_DIR") or os.path.expanduser(
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


def has_terminated(path):
    """Whether the agent has finished — and in this harness THE TRANSCRIPT CANNOT TELL YOU.

    MEASURED 2026-07-29, not assumed. Reviewer T's transcript was inspected directly:
      * every assistant record carries stop_reason = None, mid-task and final alike;
      * there is no `result` / `task_complete` record type at all (types are exactly
        {user, assistant, attachment});
      * a mid-task narration turn ("Now let me read the other key files...") and the real final
        report are STRUCTURALLY IDENTICAL — both are text-only assistant turns with no tool_use.

    An earlier version of this gate inferred termination from "the last assistant turn is not a tool
    call". That is unsound for exactly the reason above, and it failed in production: run against a live
    reviewer T it declared termination, wrote a 120-character mid-task fragment, and titled it "VERBATIM
    final message" -- the precise defect the gate had been added to prevent, one layer down.

    So the inference is REMOVED rather than improved. Termination is a fact only the CALLER has: it
    receives the harness completion notification. The caller must assert it with --terminated. Default is
    to refuse, because failing closed is the whole point.
    """
    return False, ("termination is not inferable from this harness's transcript "
                   "(stop_reason is None on every turn, and no terminal record type exists); "
                   "pass --terminated once the completion notification has arrived")


def main():
    if len(sys.argv) < 3:
        sys.stderr.write(__doc__)
        return 2
    force = "--allow-live" in sys.argv
    if force:
        sys.argv.remove("--allow-live")
    asserted = "--terminated" in sys.argv
    if asserted:
        sys.argv.remove("--terminated")
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
        term, why = has_terminated(jsonl_p)
        if asserted:
            term, why = True, "caller asserted --terminated (harness completion notification)"
        if not term and not force:
            print("LIVE     %s  REFUSED to write: %s" % (tag, why))
            print("         Point this at a scratch directory, or pass --allow-live and accept that the")
            print("         output is a mid-task fragment and MUST NOT be titled a final message.")
            rc = 1
            continue
        meta = json.load(open(meta_p)) if os.path.isfile(meta_p) else {}
        body = final_text(jsonl_p)
        if not body:
            print("EMPTY    %s  transcript has no assistant text" % tag)
            rc = 1
            continue
        title = ("# Reviewer %s — VERBATIM final message" if term else
                 "# Reviewer %s — MID-TASK FRAGMENT. NOT A FINAL MESSAGE. NOT A VERDICT.") % tag
        provenance = ("**Extracted from the harness transcript, not re-typed.** Everything below the rule\n"
                      "is the agent's own final message, byte for byte." if term else
                      "**THE AGENT WAS STILL RUNNING WHEN THIS WAS WRITTEN.** The text below is whatever\n"
                      "it had said last at that moment. It is NOT a verdict and must not be cited as one.")
        body_hdr = "\n".join([
            title, "",
            provenance, "",
            "| Field | Value | Source |",
            "|---|---|---|",
            "| agentId | `%s` | harness |" % aid,
            "| agentType | `%s` | `agent-%s.meta.json` |" % (meta.get("agentType"), aid),
            "| model | `%s` | `agent-%s.meta.json` |" % (meta.get("model"), aid),
            "| parentAgentId | `%s` | `agent-%s.meta.json` |" % (meta.get("parentAgentId"), aid),
            "| spawnDepth | `%s` | `agent-%s.meta.json` |" % (meta.get("spawnDepth"), aid),
            "| terminated | `%s` | %s |" % (term, why),
            "| transcript | `%s` | harness |" % jsonl_p,
            "| chars | %d | measured |" % len(body),
            "",
            "**These identity fields are FIRST-HAND** — read from the harness's own sidecar, not from",
            "anything the reviewer said about itself.",
            "", "---", "", ""])
        hdr = body_hdr
        out = os.path.join(outdir, "reviewer-%s-verbatim.md" % tag)
        with open(out, "w") as fh:
            fh.write(hdr + body)
        print("WROTE    %s  %d chars  -> %s" % (tag, len(body), out))
    return rc


if __name__ == "__main__":
    sys.exit(main())
