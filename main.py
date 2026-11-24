#!/usr/bin/env python3
"""One Word, First Thought -- make.fun entry.

The brief asks for exactly one word: the first word that comes to mind,
nothing else. This program writes that one word to /output/entry.txt.

The word is fixed in the source, so every run produces the same bytes.
No input is read, no network is used, and nothing depends on the clock
or on chance.
"""

import os

WORD = "psithurism"


def main() -> None:
    """Write the entry word to /output/entry.txt."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
