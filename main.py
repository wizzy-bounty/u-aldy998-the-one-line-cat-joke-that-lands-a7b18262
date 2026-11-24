#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands.

Writes a single one-line cat joke (1-200 characters, UTF-8, one line)
to /output/entry.txt. Python standard library only, deterministic,
no network access.
"""

import os

JOKE = "My cat pushed my glass off the table, watched it shatter, then looked at me like I did it."


def validate_line(line: str) -> None:
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"


def main() -> None:
    validate_line(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
