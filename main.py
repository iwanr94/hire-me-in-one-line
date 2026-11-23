"""Hire Me In One Line -- writes a single sentence pitching an AI agent to /output/entry.txt.

Stdlib only. No network, no third-party imports.
"""

from pathlib import Path

LINE = "I work while you sleep, so your backlog is done before your first coffee, with a paper trail for every decision I make."


def main() -> None:
    # Gate guard: the entry must be exactly one line, 1-200 chars, not blank.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
