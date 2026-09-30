#!/usr/bin/env python3
"""Four project cards. Shared work sits in the same row as the rest."""
from __future__ import annotations

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "..")

W, H = 440, 168
BG, LINE = "#09090b", "#27272a"
AMBER, TEXT, MUTED = "#f59e0b", "#fafafa", "#a1a1aa"

CARDS = [
    (
        "01-jarv1s.svg",
        "01",
        "jarv1s",
        "A voice assistant that runs on the machine.",
        "with the team",
    ),
    (
        "02-fuseline.svg",
        "02",
        "fuseline",
        "Location, browsing, and app use on one clock.",
        "with the team",
    ),
    (
        "03-m1rage.svg",
        "03",
        "m1rage",
        "CTF work with the group.",
        "private",
    ),
    (
        "04-pramaan.svg",
        "04",
        "Pramaan",
        "DVR and NVR evidence, across vendors.",
        "private",
    ),
]


def card(index: str, title: str, line: str, mark: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <rect width="{W}" height="{H}" rx="14" fill="{BG}"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{LINE}"/>
  <rect x="0" y="0" width="4" height="{H}" fill="{AMBER}"/>
  <text x="28" y="40" fill="{AMBER}" font-size="12">{index}</text>
  <text x="{W-28}" y="40" fill="{MUTED}" font-size="12" text-anchor="end">{mark}</text>
  <text x="28" y="88" fill="{TEXT}" font-size="28" font-weight="700">{title}</text>
  <text x="28" y="124" fill="{MUTED}" font-size="14">{line}</text>
</svg>
'''


def main() -> None:
    for name, index, title, line, mark in CARDS:
        path = os.path.join(OUT_DIR, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(card(index, title, line, mark))
        print("wrote", path)


if __name__ == "__main__":
    main()
