#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry program.

Writes exactly one emoji to /output/entry.txt: the single postcard
for a dream vacation. No words, no extra characters — the emoji
itself is the whole entry.

Choice: U+1F3DD DESERT ISLAND.
Refined from the beach-with-umbrella: a lone palm on a desert
island is not just any holiday, it is one particular dream — the
faraway escape, no crowds, no resort, just you and the sea. It
reads as a postcard at a glance, feels personal and specific
rather than generic, and carries a small spark of surprise: most
entries will reach for a beach or a plane, while the island says
"get me away from everything".
"""

import os
import sys

# The entry: exactly one emoji.
ENTRY = "\U0001F3DD"  # 🏝️ desert island

OUTPUT_PATH = "/output/entry.txt"


def validate(entry: str) -> None:
    """The gate requires UTF-8 text of 1 to 8 characters, not only whitespace."""
    if not entry or entry.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if len(entry) > 8:
        raise ValueError(f"entry is {len(entry)} characters, over the 8-character gate")
    entry.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"entry: {ENTRY} ({len(ENTRY)} character(s), "
          f"{len(ENTRY.encode('utf-8'))} byte(s)) -> {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
