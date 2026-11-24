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

# The gate allows 1 to 24 characters and refuses whitespace-only text.
# Check the word against it here, so a bad word fails loudly at build
# time instead of silently producing an entry the gate rejects.
MAX_CHARS = 24


def _check_word(word: str) -> None:
    """Refuse any word the gate would refuse."""
    if not 1 <= len(word) <= MAX_CHARS:
        raise SystemExit("entry word must be 1 to 24 characters")
    if not word.strip():
        raise SystemExit("entry word must not be only whitespace")
    if len(word.split()) != 1:
        raise SystemExit("entry must be exactly one word")


def main() -> None:
    """Write the entry word to /output/entry.txt."""
    _check_word(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
