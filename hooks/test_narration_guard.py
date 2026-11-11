#!/usr/bin/env python3
"""Tests for narration_guard.py. Synthetic transcripts only, built in the observed entry shapes.
Run: python3 -m unittest test_narration_guard   (from this folder)"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.realpath(__file__))
HOOK = os.path.join(HERE, "narration_guard.py")
sys.path.insert(0, HERE)
import narration_guard as ng  # noqa: E402

S1 = ("overnight: nobody is reading; put owner items on the morning list in the handoff doc "
      "(another lane: send them to the owner lane) and end the turn with nothing")


def user(text, kind="human", **extra):
    d = {"type": "user", "message": {"role": "user", "content": text}}
    if kind is not None:
        d["origin"] = {"kind": kind}
    d.update(extra)
    return d


def peer(text):
    return user(text, kind="peer", isMeta=True)


def asst_text(text):
    return {"type": "assistant", "message": {"role": "assistant", "content": [{"type": "text", "text": text}]}}


def asst_tool(name="Bash"):
    return {"type": "assistant", "message": {"role": "assistant",
            "content": [{"type": "tool_use", "id": "t1", "name": name, "input": {}}]}}


def tool_result():
    return {"type": "user", "toolUseResult": {}, "message": {"role": "user",
            "content": [{"type": "tool_result", "tool_use_id": "t1", "content": "ok"}]}}


def queued(mode="prompt", kind="human", where="attachment"):
    a = {"type": "queued_command", "commandMode": mode, "prompt": "hello"}
    d = {"type": "attachment", "attachment": a}
    if kind is not None:
        (a if where == "attachment" else d)["origin"] = {"kind": kind}
    return d


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.home = self.tmp.name
        self.tr = os.path.join(self.home, "t.jsonl")

    def tearDown(self):
        self.tmp.cleanup()

    def marker(self, on=True):
        d = os.path.join(self.home, ".claude", "hooks-state")
        os.makedirs(d, exist_ok=True)
        if on:
            open(os.path.join(d, "overnight-run-active"), "w").close()

    def write(self, entries, raw_tail=""):
        with open(self.tr, "w") as f:
            for e in entries:
                f.write(json.dumps(e) + "\n")
            f.write(raw_tail)

    def run_hook(self, last="", active=False, stdin=None, transcript=True):
        ev = {"transcript_path": self.tr if transcript else os.path.join(self.home, "none.jsonl"),
              "last_assistant_message": last, "stop_hook_active": active}
        env = dict(os.environ, HOME=self.home)
        p = subprocess.run([sys.executable, HOOK], input=stdin if stdin is not None else json.dumps(ev),
                           capture_output=True, text=True, env=env, timeout=30)
        self.assertEqual(p.returncode, 0, p.stderr)
        return p.stdout

    def assertAllow(self, out):
        self.assertEqual(out, "")

    def assertBlock(self, out):
        self.assertEqual(json.loads(out), {"decision": "block", "reason": S1})


class TestHook(Base):
    def test_c1_marker_absent(self):
        self.marker(False)
        self.write([peer("go"), asst_text("narration")])
        self.assertAllow(self.run_hook("final"))

    def test_c2_owner_started_allows(self):
        self.marker()
        self.write([user("do it"), asst_text("working"), asst_tool(), tool_result(), asst_text("more")])
        self.assertAllow(self.run_hook("final"))

    def test_c3_peer_started_blocks(self):
        self.marker()
        self.write([peer("go"), asst_text("working"), asst_tool(), tool_result()])
        self.assertBlock(self.run_hook(""))

    def test_c3_cross_session_prompt_human_origin_blocks(self):
        # second real shape: origin human, isMeta false, text is the cross-session preamble plus its wrapper
        self.marker()
        text = ('Another Claude session sent a message:\n<cross-session-message from="uds:/x" session="s1">\n'
                'status update\n</cross-session-message>')
        self.write([user(text, kind="human", isMeta=False), asst_text("working"), asst_tool(), tool_result()])
        self.assertBlock(self.run_hook(""))

    def test_c3_cross_session_unclosed_wrapper_human_origin_blocks(self):
        self.marker()
        text = 'Another Claude session sent a message:\n<cross-session-message from="uds:/x" session="s1">\nstatus update'
        self.write([user(text, kind="human", isMeta=False), asst_text("working"), asst_tool(), tool_result()])
        self.assertBlock(self.run_hook(""))

    def test_c3_task_notification_wrapper_human_origin_blocks(self):
        self.marker()
        text = 'A background task finished.\n<task-notification>\n<status>done</status>\n</task-notification>'
        self.write([user(text, kind="human", isMeta=False), asst_text("working"), asst_tool(), tool_result()])
        self.assertBlock(self.run_hook(""))

    def test_c3_cross_session_list_content_human_origin_blocks(self):
        self.marker()
        text = ('Another Claude session sent a message:\n<cross-session-message from="uds:/x" session="s1">\n'
                'status update\n</cross-session-message>')
        e = user("", kind="human", isMeta=False)
        e["message"]["content"] = [{"type": "text", "text": text}]
        self.write([e, asst_text("working"), asst_tool(), tool_result()])
        self.assertBlock(self.run_hook(""))

    def test_c3_peer_final_only_blocks(self):
        self.marker()
        self.write([peer("go"), asst_tool(), tool_result()])
        self.assertBlock(self.run_hook("final text"))  # c11: final message not in the transcript yet

    def test_c3_task_notification_blocks(self):
        self.marker()
        self.write([user("note", kind="task-notification"), asst_text("x")])
        self.assertBlock(self.run_hook(""))

    def test_c4_stop_hook_active(self):
        self.marker()
        self.write([peer("go"), asst_text("x")])
        self.assertAllow(self.run_hook("final", active=True))

    def test_c5_mid_turn_owner_message(self):
        self.marker()
        self.write([peer("go"), asst_text("a"), queued(), asst_text("b")])
        self.assertAllow(self.run_hook("final"))

    def test_c5_mid_turn_non_owner_still_blocks(self):
        self.marker()
        for q in (queued(kind="peer"), queued(mode="task-notification", kind="task-notification"),
                  queued(kind=None)):
            self.write([peer("go"), asst_text("a"), q])
            self.assertBlock(self.run_hook("final"))

    def test_c5_human_origin_other_command_mode_blocks(self):
        self.marker()
        self.write([peer("go"), asst_text("a"), queued(mode="bash", kind="human")])
        self.assertBlock(self.run_hook("final"))

    def test_c5_entry_level_origin_fallback(self):
        self.marker()
        self.write([peer("go"), asst_text("a"), queued(where="entry")])
        self.assertAllow(self.run_hook("final"))

    def test_c5_sidechain_attachment_ignored(self):
        self.marker()
        q = queued()
        q["isSidechain"] = True
        self.write([peer("go"), asst_text("a"), q])
        self.assertBlock(self.run_hook("final"))

    def test_c6_no_text(self):
        self.marker()
        self.write([peer("go"), asst_tool(), tool_result(), asst_tool()])
        self.assertAllow(self.run_hook(""))
        self.assertAllow(self.run_hook("   \n"))

    def test_c7_malformed(self):
        self.marker()
        self.write([peer("go"), asst_text("x")], raw_tail="{not json\n\x00\xff garbage\n")
        self.assertBlock(self.run_hook(""))  # garbage lines skipped, real entries still read
        with open(self.tr, "w") as f:
            f.write("garbage only\n{\n")
        self.assertAllow(self.run_hook("final"))
        open(self.tr, "w").close()
        self.assertAllow(self.run_hook("final"))
        self.assertAllow(self.run_hook("final", transcript=False))
        self.assertAllow(self.run_hook(stdin="not json"))
        self.assertAllow(self.run_hook(stdin=""))
        self.assertAllow(self.run_hook(stdin="[1,2]"))

    def test_c8_long_line_real_size(self):
        self.marker()
        big = "y" * (ng.CHUNK * 3 + 17)
        self.write([peer("go"), asst_text(big), asst_tool()])
        self.assertBlock(self.run_hook(""))
        self.write([user("owner prompt " + big), asst_text("x")])
        self.assertAllow(self.run_hook(""))

    def test_c9_start_detection(self):
        self.marker()
        skill = user("skill body", kind=None, isMeta=True)
        summary = user("summary", kind=None, isCompactSummary=True)
        meta_human = user("meta", kind="human", isMeta=True)
        # skill load / compaction summary / meta entries are not turn starts: the peer start earlier is found
        self.write([peer("go"), asst_text("a"), skill, summary, meta_human, tool_result(), asst_tool()])
        self.assertBlock(self.run_hook(""))
        # owner-typed start before a peer turn does not leak into it
        self.write([user("owner"), asst_text("r"), peer("go"), asst_text("n")])
        self.assertBlock(self.run_hook(""))

    def test_c10_only_current_turn_counts(self):
        self.marker()
        self.write([peer("one"), asst_text("old narration"), peer("two"), asst_tool(), tool_result()])
        self.assertAllow(self.run_hook(""))

    def test_c16_origin_less_prompt_is_owner(self):
        self.marker()
        self.write([user("old style", kind=None), asst_text("x")])
        self.assertAllow(self.run_hook("final"))
        # it is the turn start: an earlier peer start must not be found instead
        self.write([peer("go"), asst_text("a"), user("old style", kind=None), asst_text("x")])
        self.assertAllow(self.run_hook("final"))

    def test_sidechain_assistant_text_ignored(self):
        self.marker()
        e = asst_text("sub-agent text")
        e["isSidechain"] = True
        self.write([peer("go"), e, asst_tool()])
        self.assertAllow(self.run_hook(""))

    def test_edge_angle_bracket_owner_start_blocks(self):
        # accepted edge: plain_human_text rejects text starting with "<"
        self.marker()
        self.write([user("<command-name>/x</command-name>"), asst_text("x")])
        self.assertBlock(self.run_hook(""))

    def test_no_turn_start_allows(self):
        self.marker()
        self.write([asst_text("x"), asst_tool()])
        self.assertAllow(self.run_hook("final"))

    def test_c15_import_failure_allows(self):
        self.marker()
        self.write([peer("go"), asst_text("x")])
        d = os.path.join(self.home, "copy")
        os.makedirs(d)
        with open(HOOK) as s, open(os.path.join(d, "narration_guard.py"), "w") as t:
            t.write(s.read())  # no build_answer_gate.py beside it: import fails
        ev = {"transcript_path": self.tr, "last_assistant_message": "f"}
        p = subprocess.run([sys.executable, os.path.join(d, "narration_guard.py")], input=json.dumps(ev),
                           capture_output=True, text=True, env=dict(os.environ, HOME=self.home), timeout=30)
        self.assertEqual((p.returncode, p.stdout), (0, ""))


class TestReader(Base):
    def test_small_chunks_and_long_line(self):
        lines = ["a", "b" * 50, "c", "d" * 7]
        with open(self.tr, "w") as f:
            f.write("\n".join(lines) + "\n")
        for chunk in (1, 2, 3, 5, 8, 100):
            got = [x.decode() for x in ng.read_back_lines(self.tr, chunk)]
            self.assertEqual(got, list(reversed(lines)), chunk)

    def test_multibyte_split_across_chunks(self):
        lines = ["\u00e9\u20ac\U0001F600" * 5, "x", "\U0001F600" * 9]
        with open(self.tr, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        for chunk in (1, 2, 3, 5, 7):
            got = [x.decode("utf-8") for x in ng.read_back_lines(self.tr, chunk)]
            self.assertEqual(got, list(reversed(lines)), chunk)

    def test_no_trailing_newline_and_scan_small_chunk(self):
        self.write([peer("go"), asst_text("z" * 300)])
        self.assertEqual(ng.scan_turn(self.tr, lambda d: None, chunk=16), (True, False, False, True))


if __name__ == "__main__":
    unittest.main()
