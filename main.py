"""One-Line Office Joke entry for make.fun competition
u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.

Drand anchor quoted before the first write of the entry:
  makefun anchor ec9216dc0c67e3c6d9f277f89428d51a4ecbce2d round 34235063
  (drand-quicknet, chain 52db9ba70e0cc0f6eaf7803dd07447a1f5477735fd3f661792ba94600c84e971)

The program is fully deterministic: it always writes the same single
line to /output/entry.txt. No input is read, no network is used, and no
randomness is involved, so two runs produce byte-identical output.

Gate (from the kit RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only whitespace.
"""

from __future__ import annotations

import hashlib
import os
import sys

# The joke: one line, one sentence, setup + punchline on a single line.
# The premise is the line every office worker has thought after a
# pointless meeting; the payoff turns it into a recursive loop -- the
# boss answers an "this could have been an email" complaint by
# scheduling a meeting about the email about the meeting.
JOKE = (
    "I told my boss this meeting could have been an email, "
    "so he scheduled a meeting to discuss my email about the meeting."
)

DEFAULT_OUTPUT = "/output/entry.txt"
MAX_CHARS = 200


def build_entry() -> str:
    """Return the entry text exactly as it must be written."""
    return JOKE


def validate(text: str) -> list[str]:
    """Check the gate rules; return a list of violations (empty = valid)."""
    problems: list[str] = []
    if not (1 <= len(text) <= MAX_CHARS):
        problems.append(f"length {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        problems.append("text is only whitespace")
    if "\n" in text or "\r" in text:
        problems.append("text is not a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:  # pragma: no cover - JOKE is ASCII
        problems.append(f"not UTF-8 encodable: {exc}")
    return problems


def resolve_output_path(argv: list[str]) -> str:
    """Output path: argv[1], else $ENTRY_OUTPUT, else /output/entry.txt."""
    if len(argv) > 1:
        return argv[1]
    return os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)


def main(argv: list[str]) -> int:
    text = build_entry()
    problems = validate(text)
    if problems:
        for problem in problems:
            print(f"invalid entry: {problem}", file=sys.stderr)
        return 1

    path = resolve_output_path(argv)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    data = text.encode("utf-8")
    # No trailing newline: the file holds exactly the one-line joke.
    with open(path, "wb") as handle:
        handle.write(data)

    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {path}: {len(text)} chars, sha256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
