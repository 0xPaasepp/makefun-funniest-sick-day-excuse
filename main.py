"""The Funniest Sick-Day Excuse (make.fun).

Writes one line - a sick-day excuse, in the texter's own voice - to
/output/entry.txt. The grader's gate checks the file is UTF-8 text of
1 to 200 characters, not only white space. Pure standard library.
"""

import os

# The entry line: exactly one line, under 200 characters. A pulled
# muscle is a reason a boss might half believe; the cause (reaching
# for the work laptop) and the prescription (a week off from
# reaching) are the laugh, and the funniest word lands last.
# Verified 2026-11-25: 115 characters, 117 bytes, single line, no
# trailing newline; grader-style runs (python3 -P -s, two cwds)
# write byte-identical /output/entry.txt, sha256 f2714bd9...
LINE = (
    "I can't come in \u2014 I pulled a muscle reaching for my work "
    "laptop, so my doctor says I need a week off from reaching."
)


def main() -> None:
    text = LINE
    if not text or text.strip() != text:
        raise SystemExit("entry must be non-empty and not only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be exactly one line (no internal newlines)")
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
