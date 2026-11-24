#!/usr/bin/env python3
"""Entry for One Word for the Boss.

Writes exactly one word describing the boss (at most 30 characters) to
/output/entry.txt and prints it to stdout. Pure standard library.
"""

import os

WORD = "Unreachable"

def _check(text, limit):
    """Refuse anything that is not exactly one word inside the limit."""
    if not isinstance(text, str) or not text:
        raise ValueError("entry must be non-empty text")
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")
    if len(text) > limit:
        raise ValueError("entry runs past its character limit")
    for bad in (" ", "\n", "\r", "\t"):
        if bad in text:
            raise ValueError("entry must be exactly one word, no spaces")
    if not text.isalpha():
        raise ValueError("entry must be a single word of letters")
    return text


def main() -> None:
    entry = _check(WORD, 30)
    directory = "/output"
    os.makedirs(directory, exist_ok=True)
    with open(directory + "/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)

if __name__ == "__main__":
    main()
