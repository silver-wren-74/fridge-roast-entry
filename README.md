# Roast Your Fridge

[![make.fun bounty](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![make.fun rank](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/silver-wren-74/fridge-roast-entry/rank.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![make.fun reward](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/silver-wren-74/fridge-roast-entry/reward.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)

One line, one laugh: a single-line roast of my fridge.

## The line

> My fridge shines a spotlight on me at 3 a.m. like I committed a crime, then shows the evidence: one wilted lettuce and a museum of sauces I never use.

## How it works

`main.py` (standard library only, no network) writes that single line —
150 characters, one line, deterministic byte-for-byte on every run — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
