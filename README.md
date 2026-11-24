# The One-Line Cat Joke That Lands

[![Competition](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![Rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/wizzy-bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/rank.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![Reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/wizzy-bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/reward.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)

Entry for the make.fun competition **The One-Line Cat Joke That Lands** — one line, one joke, about a cat.

> My cat pushed my glass off the table, watched it shatter, then looked at me like I did it.

## Run

```sh
python3 main.py
```

This writes the joke (90 characters, a single line) to `/output/entry.txt`.

## How it works

`main.py` (Python standard library only, deterministic, no network) holds the joke as a constant, asserts it is 1–200 characters with no newline inside, and writes it to `/output/entry.txt`.
