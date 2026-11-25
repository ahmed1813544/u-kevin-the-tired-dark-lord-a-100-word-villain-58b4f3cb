#!/usr/bin/env python3
"""Write the Tired Dark Lord monologue to /output/entry.txt.

Deterministic: the same text is written on every run.
Standard library only.
"""

import os

TEXT = (
    "You found the stairs. Good. Most heroes die in the thorn hedge "
    "\u2014 I planted it in forty-three, when the farmers paid in "
    "chickens. Sit. No, not the chair; the springs have gone. The "
    "sword can stay on the table. I have read your speech before, "
    "four times now, each of you louder than the last. The crown? On "
    "the shelf, beside the pickled wyrm. Take it. All it does is "
    "whisper tax figures all night. But \u2014 the door locks behind "
    "you, hero. And the hedge? It remembers every name. Mine is... ah. "
    "On the tip of my tongue."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
