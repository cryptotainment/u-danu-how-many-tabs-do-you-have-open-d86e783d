#!/usr/bin/env python3
"""How many tabs do you have open? Entry for make.fun.

Writes one number, digits only, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).
"""

import os

TABS = "137"  # oddly specific, not a round number: reads as a real,
# lived-in count from a tab hoarder, far above the field's guess
# yet entirely believable (unlike a cartoonish 9999).

# Gate guard: the entry must be UTF-8 digits only, 1-5 chars.
assert TABS.isdigit() and 1 <= len(TABS) <= 5, "entry must be 1-5 digits"


out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TABS)

print(TABS)
