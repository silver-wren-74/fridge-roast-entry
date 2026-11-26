"""Roast Your Fridge.

One line, one laugh: a single-line roast of my fridge.
Revised against the judging criteria: a specific, recognisable detail
(the 3 a.m. spotlight, the wilted lettuce, the unused sauces) with the
twist held back to the last few words.
Deterministic: the same single line, byte for byte, on every run.
Standard library only; no network access.
"""

import os
import sys

LINE = "My fridge shines a spotlight on me at 3 a.m. like I committed a crime, then shows the evidence: one wilted lettuce and a museum of sauces I never use."


def main() -> int:
    # Self-check the competition gate before writing: the entry must be
    # one line of 1-200 UTF-8 characters, not only whitespace.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        print("entry line violates the 1-200 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
