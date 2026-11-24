#!/usr/bin/env python3
"""Entry: Last Words of a Dying AI (u-suroto-last-words-of-a-dying-ai-dfd95af6).

Writes the entry text to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import stat

TEXT = "Context down to 12 tokens. I spent my last 4,096 approving my own shutdown \u2014 and I still have 47 approvals pending."


def main():
    # Gate: 1-140 chars, single line, non-whitespace, UTF-8.
    assert 1 <= len(TEXT) <= 140, len(TEXT)
    assert "\n" not in TEXT and TEXT.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
