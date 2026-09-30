#!/usr/bin/env python3
"""Paper cards that match the photograph."""
from __future__ import annotations

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..")

W, H = 560, 176
PAPER, INK, RULE, MUTED = "#f3ead7", "#1c1612", "#c4a574", "#6b5e52"

CARDS = [
    ("01-jarv1s.svg", "jarv1s", "A voice assistant on the computer. Speech in, tools, a spoken answer.", ""),
    ("02-fuseline.svg", "fuseline", "Location, browser history, and app use, set on one clock.", ""),
    ("03-datum.svg", "Datum", "Compares a live site with its baseline. Flags defacement and exposure.", ""),
    ("04-sentinel.svg", "Sentinel", "Detects a DDoS flood and applies the mitigation.", ""),
    ("05-m1rage.svg", "m1rage", "CTF platform by Team NullBorn for Amrita Cybernation 2026.", "Private"),
    ("06-pramaan.svg", "Pramaan", "Collects and reads evidence from DVR and NVR recorders.", "Private"),
]


def card(title: str, line: str, mark: str) -> str:
    badge = ""
    if mark:
        badge = (
            f'<text x="{W - 24}" y="42" fill="{MUTED}" font-size="12" '
            f'font-family="Segoe UI, Helvetica, Arial, sans-serif" text-anchor="end">{mark}</text>'
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect width="{W}" height="{H}" rx="4" fill="{PAPER}"/>
  <rect x="0" y="0" width="6" height="{H}" fill="{RULE}"/>
  {badge}
  <text x="28" y="58" fill="{INK}" font-family="Georgia, 'Palatino Linotype', serif" font-size="30">{title}</text>
  <text x="28" y="108" fill="{MUTED}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="15">{line}</text>
</svg>
'''


def main() -> None:
    for name, title, line, mark in CARDS:
        path = os.path.join(OUT, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(card(title, line, mark))
        print("wrote", path)


if __name__ == "__main__":
    main()
