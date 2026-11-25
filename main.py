#!/usr/bin/env python3
"""Copier for the meeting-that-should-have-been-an-email one-liner.

Reads the entry from entry.txt next to this script, prints it, and
writes it to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt)
for the sealed gate scorer.
"""
import os

ENTRY_FILE = "entry.txt"
MAX_CHARS = 200  # competition cap: one line, at most 200 characters


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, ENTRY_FILE), encoding="utf-8") as f:
        text = f.read().strip()
    if not text or "\n" in text or len(text) > MAX_CHARS:
        raise ValueError("entry must be one line of 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
