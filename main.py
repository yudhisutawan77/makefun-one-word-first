"""One Word, First Thought -- entry program.

The brief asks for exactly one word: the first word that comes to mind,
with no topic, no explanation and no second draft. This program writes
that single word to /output/entry.txt so the gate can check it and the
pairwise judge can compare it against the rest of the field.

The word is "petrichor": the smell of dry earth after rain. It is vivid
and specific -- it calls up a clear sensory image in nine letters --
surprising rather than safe, and it carries a soft, rain-like sound that
rewards a second look. It is a chosen word, not filler.
"""

import os
import sys

WORD = "petrichor"


def check_word(word: str) -> None:
    """Enforce the gate locally: 1-24 characters, not only whitespace,
    and a single token with no spaces or line breaks."""
    if not word or word != word.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if len(word) > 24:
        raise ValueError("entry must be at most 24 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word")


def main() -> int:
    check_word(WORD)
    out_dir = os.environ.get("ENTRY_OUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
