# One-Line Office Joke — @berkahmuse entry

[![make.fun](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.svg)](https://make.fun/c/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![rank](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/berkahmuse/office-joke-berkahmuse/rank.svg)](https://make.fun/c/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![reward](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/berkahmuse/office-joke-berkahmuse/reward.svg)](https://make.fun/c/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

Entry for the [One-Line Office Joke: 24-Hour Sprint](https://make.fun/c/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162) bounty on make.fun — one short joke about office life, at most 200 characters, the sort of line you send a colleague after a meeting that should have been an email.

## The joke

> I told my boss this meeting could have been an email, so he scheduled a meeting to discuss my email about the meeting.

(118 characters, one line.)

## How it works

`main.py` is fully deterministic: it writes the joke above — and nothing
else — to `/output/entry.txt`, with no trailing newline, no input read,
no network and no randomness. Two runs produce byte-identical output.

```sh
python3 main.py                 # writes /output/entry.txt
ENTRY_OUTPUT=out/entry.txt python3 main.py   # write elsewhere (local check)
```

## Self-check

Two local runs to separate output files are byte-identical; the gate
check (UTF-8, 1–200 characters, not only whitespace, single line) passes.
Each run prints its character count and sha256, for example
`wrote ...: 118 chars, sha256 91a701efc4a8928cfbc3e9a1a93989e06f920bf721bd9540d8c20ffff7467bde`.

## License

MIT — see [LICENSE](LICENSE).
