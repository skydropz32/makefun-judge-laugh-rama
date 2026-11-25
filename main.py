"""Make the AI Judge Laugh — one office-life joke, under 200 characters.

Writes a single deterministic line to /output/entry.txt.
Standard library only; no randomness, no network, no time.
"""

import os

JOKE = "I set my out-of-office reply to 'back never' and HR replied within minutes — the fastest response I've ever had."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
