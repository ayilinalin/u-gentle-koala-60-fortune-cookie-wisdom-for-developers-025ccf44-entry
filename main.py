"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original fortune-cookie line (a single sentence, <= 120
characters) to /output/entry.txt.

Why this line: every developer has watched an estimate turn out wrong,
and the tired senior engineer knows the estimate was never a lie — it was
a prediction made before the future had spoken. The line turns that truth
with a fortune cookie's own trick: it calls the estimate itself a fortune,
so the cookie is quietly about fortune-telling. One balanced sentence,
lands in a single breath, and the second read is the reward.
"""

LINE = "Your estimates are not lies; they are fortunes told before the future has had its say."


def main() -> None:
    import os

    # Gate self-check: the sealed scorer requires UTF-8 text of 1-120
    # characters, not only whitespace, as a single line.
    text = LINE.strip()
    assert 1 <= len(text) <= 120, f"line is {len(text)} chars, must be 1-120"
    assert text.count(".") == 1, "must be one sentence, one breath"
    assert "\n" not in text, "must be a single line"
    assert text and not text.isspace()

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
