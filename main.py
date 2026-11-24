"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is an alien tourist's one-line review of Earth after a
# two-day stopover: stars, highlights, and one docked star for Mondays.
import os

TEXT = (
    "Five stars. Earth: gorgeous sunsets, locals queuing hours to stare "
    "at a rock, and snacks worth the gravity. Docked one star \u2014 "
    "nobody warned me about Mondays."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# One line, 157 characters: a real-review shape, punch at the end.
