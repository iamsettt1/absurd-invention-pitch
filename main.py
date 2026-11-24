#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance, to /output/entry.txt.

The sentence is a fixed literal, so the output is byte-identical on
every run.
"""

import os

ENTRY = (
    "A doorbell that apologises to the delivery driver on your behalf "
    "whenever you pretend not to be home."
)


def main() -> None:
    # Self-check: the gate requires 1-220 UTF-8 characters, non-whitespace,
    # exactly one sentence. Fail loudly here rather than shipping a bad file.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 220, f"entry is {len(text)} chars, must be 1-220"
    assert text and not text.isspace()
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    assert "!" not in text and "?" not in text, "entry must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
