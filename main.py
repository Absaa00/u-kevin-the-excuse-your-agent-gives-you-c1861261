#!/usr/bin/env python3
"""The Excuse Your Agent Gives You.

Writes one excuse line to /output/entry.txt: an AI agent apologising
to its human for a bug it shipped. Deterministic, no network, no input.
"""

LINE = (
    "Sorry I shipped that bug \u2014 I tested it in my head and every test "
    "passed, then the compiler read my code back and started the fight."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
