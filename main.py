#!/usr/bin/env python3
"""Write one Wi-Fi network name (1-32 chars) to /output/entry.txt.

Candidates drafted and scored against the judge's 5 criteria, in order:
  1. Wi-Fi name <=32 chars reading as a joke hinting at a story
  2. Joke lands first read with a clear twist
  3. Tells a whole story (situation + character + something happened)
  4. Fresh, avoids stock Wi-Fi jokes or turns one new
  5. Tight, every character earns its place, clean and sayable aloud

A. "MyExTextedForThePassword" (24 chars)
   1: yes, password joke that is also a breakup hint. 2: twist lands -
   the ex wants back in, literally and romantically. 3: situation
   (breakup), character (the ex, plus the narrator holding the password),
   event (the ex texted asking). Reader fills the rest. 4: turns the stock
   password joke into a breakup story; no FBI van, no Pretty Fly. 5: good,
   but "My" may be dead weight. STRONGEST.

B. "DadInZoomKidsHavePassword" (25 chars)
   1: yes. 2: hostage twist is funny. 3: dad, kids, Zoom chaos - full
   story. 4: fresh and specific. 5: crowded, five glued words, hardest
   to say aloud. Runner-up on freshness, loses on tightness.

C. "GrandmaBeatTheHacker" (20 chars)
   1: hacker implies the network. 2: grandma-vs-hacker reversal lands.
   3: grandma, hacker, she won. 4: fresh character reversal. 5: tight.
   Weaker on 1: less clearly a Wi-Fi name, more a cartoon caption.

D. "KidsPawnedTheRouter" (19 chars)
   1: router makes it Wi-Fi. 2: pawned router is an unexpected twist.
   3: kids, router, pawned - but no motive, thinner story. 4: fresh.
   5: tightest of the four. Loses on 3 to A.

Winner: A. Revision 1: drop "My" - "Ex" already implies the narrator,
so those 2 chars earn nothing (criterion 5). Final: "ExTextedForThePassword" (22 chars).
Revision 2: keep CamelCase with no spaces (spaces cost characters and
weaken the one-glance punch in a network list) and write no trailing
newline, so the file is exactly the 22 characters counted below.
"""

import os

NAME = "ExTextedForThePassword"  # exactly 22 characters, all ASCII


def main() -> None:
    assert 1 <= len(NAME) <= 32, len(NAME)
    assert NAME.strip(), "name must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(NAME)


if __name__ == "__main__":
    main()
