"""The Office Joke Open entry: write one office joke, single line, to /output/entry.txt."""

import os

JOKE = (
    "Our daily standup is so efficient we spend 45 minutes explaining why "
    "yesterday's 15-minute standup ran long \u2014 and Jira still lists the "
    "ticket as 'in progress' since March."
)


def main() -> None:
    # Self-check the competition gate: single line, at most 200 chars
    # (current joke: 171 chars, verified by the run below).
    assert len(JOKE) <= 200, f"joke is {len(JOKE)} chars, over the 200-char limit"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
