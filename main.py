#!/usr/bin/env python3
"""The Internet in One Word.

The entry is a single word, written to /output/entry.txt:

    ouroboros

The ouroboros is the serpent eating its own tail: a loop with no
beginning and no end that feeds on itself. That is the whole internet
in one word. The feed never ends and never goes anywhere new -- the
same arguments, the same jokes, the same outrage, the same clips,
regurgitated forever, each turn of the scroll eating the last one.
Every timeline is a snake swallowing itself, and we all just watch
it do another lap.

It is a real dictionary word, nine letters, one beat, spelled the
only way it is spelled -- and nobody's first guess for the internet,
which is exactly why it fits.
"""

import os
from pathlib import Path

WORD = "ouroboros"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
