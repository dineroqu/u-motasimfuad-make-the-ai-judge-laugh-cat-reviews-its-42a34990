#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review from a house cat about
its human to /output/entry.txt. Standard library only, no network,
fully deterministic.
"""

import os

REVIEW = (
    "One star. He fills my bowl, then watches me eat "
    "like I owe him a show. I am a cat, not dinner theatre. "
    "The food was adequate. The audience was not."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
