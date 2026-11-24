#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, as spoken by a vending machine to a passing
human, to /output/entry.txt. Deterministic: the same fixed line, no
network, no randomness, standard library only.
"""

import os

ENTRY = (
    "I hum all day for strangers, but you made my coil skip. "
    "Press B4 \u2014 first snack's on the house. "
    "And by house, I mean me."
)


def main() -> None:
    # Gate (competition RULES.txt): /output/entry.txt must be UTF-8,
    # 1-200 chars, not only whitespace. Fail loudly instead of
    # submitting a line the judge would refuse.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
