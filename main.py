#!/usr/bin/env python3
"""Dog Ate My Homework — entry program.

Writes one line to /output/entry.txt: the excuse a dog gives after being
caught eating the homework. The dog's reasoning is simple and, to the dog,
airtight: homework is the thing that takes its human away to school every
morning, so removing the homework keeps the human home. The dog is proud
of this. The dog has done nothing wrong.

Run: python3 main.py
Output: $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt)
"""

import os
import sys

# The excuse, in the dog's own voice. One line, 94 characters.
EXCUSE = (
    "I ate your homework so school couldn't take you away. "
    "Look, you're still here. You're welcome."
)


def main() -> int:
    # The sealed scorer only accepts 1-200 characters, so refuse to write
    # anything outside that window instead of shipping a bad file.
    if not 1 <= len(EXCUSE) <= 200 or not EXCUSE.strip():
        print(f"refusing to write an excuse of {len(EXCUSE)} characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)
    print(EXCUSE)
    print(f"wrote {path} ({len(EXCUSE)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
