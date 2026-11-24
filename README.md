# On the House: a vending machine's coil-skip pickup line

[![make.fun · u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/mizuseii/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/mizuseii/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

One pickup line, as spoken by a vending machine to a passing human, for the
[make.fun](https://make.fun/?ref=nzf9nzj2) bounty
"One Line, One Minute: The Vending Machine Pickup Line Contest".

## The entry

> I hum all day for strangers, but you made my coil skip. Press B4 — first snack's on the house. And by house, I mean me.

119 characters (limit 200). The machine's hum, its coil, a button press —
and the punch lands in the last few words.

## How it works

`main.py` is deterministic: it writes the fixed line above to
`/output/entry.txt` (creating `/output` if needed). No network, no
randomness, Python standard library only.

```sh
python3 main.py
```
