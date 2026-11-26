# SPDX-License-Identifier: MIT
"""Monday Morning Punchlines entry.

Writes one joke about Monday mornings to /output/entry.txt.
The gate accepts UTF-8 text of 1 to 200 characters.
"""

from pathlib import Path

JOKE = "Monday morning is just Sunday night in a fake mustache, holding a 9 a.m. meeting invite."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("entry text must be 1 to 200 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
