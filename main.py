#!/usr/bin/env python3
"""Self-checkout judgement: one smug line, written to entry.txt.

Stdlib only. Deterministic: the same line every run -- no clock, no
randomness, no network, no reads outside this file. Writes nothing
outside the output directory.
"""

import os
import sys

LINE = (
    "One cucumber, one tub of ice cream, no bag. "
    "Bold. Reckless, even. "
    "Please place your poor decisions in the bagging area."
)

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print("wrote %d chars to %s" % (len(LINE), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
