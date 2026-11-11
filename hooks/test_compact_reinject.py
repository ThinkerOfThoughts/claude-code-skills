#!/usr/bin/env python3
"""Tests for compact_reinject.py. The hook runs as a subprocess with HOME and cwd pointed at a scratch
directory, so the real run marker and the real hooks-state folder are never touched.
Run: python3 -m unittest test_compact_reinject   (from this folder)"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.realpath(__file__))
HOOK = os.path.join(HERE, "compact_reinject.py")

RUN_LINE = "an overnight run is on: read your handoff doc in full and invoke the overnight-run skill again"
# Golden text of the hook before the source branches existed, with no active ledger (scratch HOME).
OLD_OUTPUT = (
    "[post-compaction re-injection — a compaction just happened; the rules below are the ones that decay]\n"
    "1. Answer the owner's question FIRST, in its own message. One question per message. When data was asked for, give the data, not a summary of it.\n"
    "2. No relay/status traffic from sibling lanes in owner-facing messages; it goes in the handoff/ledger file.\n"
    "3. Claims about the past (what was said/decided/why, by you or the owner) are LOOKUPS: quote the transcript or file, or mark the claim unverified.\n"
    "4. Before quoting or editing any file, re-read the relevant part now; your pre-compaction memory of it is stale.\n"
    "5. Read the project handoff doc IN FULL and quote its `## Secret:` token before substantive work (global handoff rule).\n"
    "6. No active plan_ledger run found.\n"
)


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.home = os.path.realpath(self.tmp.name)
        self.state = os.path.join(self.home, ".claude", "hooks-state")
        os.makedirs(self.state)
        self.assertNotEqual(self.home, os.path.realpath(os.path.expanduser("~")))

    def tearDown(self):
        self.tmp.cleanup()

    def marker(self, on=True):
        p = os.path.join(self.state, "overnight-run-active")
        if on:
            open(p, "w").close()
        elif os.path.exists(p):
            os.remove(p)

    def run_hook(self, payload, env_extra=None, raw=None):
        env = {k: v for k, v in os.environ.items() if k != "OVERNIGHT_EGGTIMER_PING"}
        env["HOME"] = self.home
        env.update(env_extra or {})
        stdin = raw if raw is not None else json.dumps(payload)
        p = subprocess.run([sys.executable, HOOK], input=stdin, capture_output=True, text=True,
                           env=env, cwd=self.home, timeout=30)
        self.assertEqual(p.returncode, 0, p.stderr)
        return p.stdout

    def compacted(self, sid="s1"):
        return os.path.exists(os.path.join(self.state, sid, "compacted"))


class TestCompact(Base):
    def check_compact_like(self, payload=None, raw=None):
        self.marker(False)
        self.assertEqual(self.run_hook(payload, raw=raw), OLD_OUTPUT)
        self.assertTrue(self.compacted())
        os.remove(os.path.join(self.state, "s1", "compacted"))
        self.marker(True)
        self.assertEqual(self.run_hook(payload, raw=raw), OLD_OUTPUT + RUN_LINE + "\n")
        self.assertTrue(self.compacted())

    def test_compact(self):
        self.check_compact_like({"source": "compact", "session_id": "s1", "cwd": self.home})

    def test_source_absent(self):
        self.check_compact_like({"session_id": "s1", "cwd": self.home})

    def test_source_empty_string(self):
        self.check_compact_like({"source": "", "session_id": "s1", "cwd": self.home})

    def test_source_not_a_string(self):
        self.check_compact_like({"source": 5, "session_id": "s1", "cwd": self.home})

    def test_malformed_stdin(self):
        # session id unknown: marker goes under "unknown" in the scratch home
        for marker in (False, True):
            self.marker(marker)
            out = self.run_hook(None, raw="{not json")
            self.assertEqual(out, OLD_OUTPUT + (RUN_LINE + "\n" if marker else ""))
            self.assertTrue(self.compacted("unknown"))


class TestStartResume(Base):
    def test_with_marker_prints_only_run_line(self):
        for src in ("startup", "resume"):
            self.marker(True)
            self.assertEqual(self.run_hook({"source": src, "session_id": "s1", "cwd": self.home}), RUN_LINE + "\n")
            self.assertFalse(self.compacted())

    def test_without_marker_prints_nothing(self):
        for src in ("startup", "resume"):
            self.marker(False)
            self.assertEqual(self.run_hook({"source": src, "session_id": "s1", "cwd": self.home}), "")
            self.assertFalse(self.compacted())


class TestSilent(Base):
    def test_clear_and_unknown_source(self):
        for src in ("clear", "other"):
            for marker in (False, True):
                self.marker(marker)
                self.assertEqual(self.run_hook({"source": src, "session_id": "s1", "cwd": self.home}), "")
                self.assertFalse(self.compacted())

    def test_eggtimer_ping(self):
        for src in ("compact", "startup", "resume", None):
            for marker in (False, True):
                self.marker(marker)
                payload = {"session_id": "s1", "cwd": self.home}
                if src:
                    payload["source"] = src
                self.assertEqual(self.run_hook(payload, env_extra={"OVERNIGHT_EGGTIMER_PING": "1"}), "")
                self.assertFalse(self.compacted())

    def test_ping_variable_other_value_is_ignored(self):
        self.marker(True)
        out = self.run_hook({"source": "startup", "session_id": "s1"}, env_extra={"OVERNIGHT_EGGTIMER_PING": "0"})
        self.assertEqual(out, RUN_LINE + "\n")


if __name__ == "__main__":
    unittest.main()
