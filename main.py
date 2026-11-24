#!/usr/bin/env python3
"""Write one satirical sentence to /output/entry.txt.

The sentence roasts a lawmaker who writes laws about encryption he has
never used, then gets beaten by the PDF button on his own laptop for
three consecutive terms: authority set up, then undercut by the file
he cannot convert, with the punch landing on the last few words.
"""
import os

ENTRY = (
    "He wrote the law banning the encryption he has never used, yet the PDF "
    "button on his own laptop has defeated him for three consecutive terms."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
