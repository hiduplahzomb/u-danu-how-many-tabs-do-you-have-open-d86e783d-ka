"""How Many Tabs Do You Have Open? — make.fun entry.

The entry is a single number: the honest count of open browser tabs.
This count reads as a real, lived-in tab hoard — three digits, low 200s:
big enough to surprise, small enough to believe. It is the kind of number
a person accumulates over months of "I'll read this later" and never
closing anything: not a round number, not an absurd one, just the honest
tally of a browser that has not been cleaned up in a very long time.
"""

import os
import sys

TEXT = "217"


def main() -> int:
    """Write the tab count to /output/entry.txt and verify it."""
    text = TEXT
    if not (1 <= len(text) <= 5):
        print("gate failed: entry must be 1-5 characters", file=sys.stderr)
        return 1
    if not text.isdigit():
        print("gate failed: entry must be digits only", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("verification failed: entry.txt does not match TEXT", file=sys.stderr)
        return 1
    print(f"wrote {path}: {text!r} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
