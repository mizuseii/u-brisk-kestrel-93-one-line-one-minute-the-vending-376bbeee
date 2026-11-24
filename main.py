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
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
