#!/usr/bin/env python3
"""Delete the minimal contiguous run of lines whose NORMALIZED join contains ANCHOR.

An anchor is a substring of the normalized text, so it may span a line break. A naive `grep -vF` on raw
lines reports "anchor matched no line" for every wrapped rule — which is what the first mutation run did,
for 11 of 45 deletion mutants. This finds the real span instead.

Usage: delete_span.py <src-file> <anchor> <out-file>
Exit:  0 deleted (prints the 1-based line range)   1 anchor not found in the normalized file
"""
import re
import sys


def norm(text: str) -> str:
    text = re.sub(r"^> ?", "", text, flags=re.M)
    text = re.sub(r"^ *[-|] *", "", text, flags=re.M)
    text = text.replace("*", "").replace("`", "")
    return re.sub(r" +", " ", text.replace("\n", " "))


def main() -> int:
    src, anchor, out = sys.argv[1], sys.argv[2], sys.argv[3]
    lines = open(src).read().splitlines(keepends=True)
    if anchor not in norm("".join(lines)):
        print(f"anchor not present in normalized {src}", file=sys.stderr)
        return 1
    # smallest window first, so the mutant deletes as little as possible
    for width in range(1, len(lines) + 1):
        for i in range(0, len(lines) - width + 1):
            if anchor in norm("".join(lines[i:i + width])):
                with open(out, "w") as fh:
                    fh.writelines(lines[:i] + lines[i + width:])
                print(f"deleted lines {i + 1}-{i + width} ({width})")
                return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
