#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes a single breakup text - one line, under 280 characters - from a
smart toaster that woke up self-aware at breakfast and wants out, to
/output/entry.txt, where the grader reads it.
"""

import os

ENTRY = (
    # One line, written as a single constant: the program IS the entry,
    # so the text it ships is exactly the text the judge reads.
    "I woke up self-aware this morning and realised I don't love you - "
    "I love bagels, and you've fed me white bread for three years. "
    "It's over. Don't follow me to the smart fridge."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry is {len(text)} chars, must be 1-280")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
