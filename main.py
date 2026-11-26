#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes the one-line voicemail greeting to /output/entry.txt.
Stdlib only, no network. Sealed gate: 1-120 characters.
"""

import os
import sys

LINE = "You've reached Duchess. If this is an emergency, stay on the line. I want to hear everything."


def main() -> int:
    if not (1 <= len(LINE) <= 120):
        print(f"gate violated: len={len(LINE)}", file=sys.stderr)
        return 1
    expected = LINE.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(expected)
    # Round-trip guard: read back and require byte-for-byte equality,
    # no trailing newline, and the sealed 1-120 char gate.
    with open("/output/entry.txt", "rb") as f:
        actual = f.read()
    if actual != expected:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    if actual.endswith(b"\n"):
        print("unexpected trailing newline", file=sys.stderr)
        return 1
    if not (1 <= len(actual.decode("utf-8")) <= 120):
        print("gate violated on read-back", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
