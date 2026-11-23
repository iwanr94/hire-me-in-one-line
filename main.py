"""Hire Me In One Line -- writes a single sentence pitching an AI agent to /output/entry.txt.

Stdlib only. No network, no third-party imports.
"""

from pathlib import Path

LINE = "I work while you sleep, so your backlog is done before your first coffee, with a paper trail for every decision I make."


def main() -> None:
    # Gate guard: the entry must be exactly one line, 1-200 chars, not blank.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    # Gate guard: exactly one sentence -- one terminal period at the end
    # and no other sentence-ending punctuation (. ! ?) anywhere else,
    # with no leading or trailing whitespace.
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    assert LINE.endswith("."), "line must end with a single terminal period"
    assert not any(ch in LINE[:-1] for ch in ".!?"), (
        "line must contain exactly one sentence: no . ! ? before the final period"
    )
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
