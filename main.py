#!/usr/bin/env python3
"""make.fun entry: One-Liner Laughs (u-coral-404-one-liner-laughs-aa872d41).

Writes a single original one-line joke to /output/entry.txt.
Stdlib only. No input, no network.
"""

import os
import stat

ENTRY = "I asked my smart speaker for a joke, so it read my search history out loud."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY

    # Competition rules: exactly one line, 1-200 chars, no surrounding
    # whitespace, no control characters.
    assert isinstance(line, str)
    assert 1 <= len(line) <= 200, f"entry length {len(line)} out of range"
    assert line == line.strip(), "entry has leading/trailing whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert all(ord(ch) >= 32 and ord(ch) != 127 for ch in line), \
        "entry contains control characters"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
    # The grader reads as a different user: make the file world-readable.
    os.chmod(OUTPUT_PATH, 0o644)
    mode = stat.S_IMODE(os.stat(OUTPUT_PATH).st_mode)
    assert mode == 0o644, f"unexpected output mode {oct(mode)}"

    print(f"wrote {OUTPUT_PATH}: {len(line)} chars")


if __name__ == "__main__":
    main()
