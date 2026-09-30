#!/usr/bin/env python3
"""Project cards in the pin-card shape used on designed profiles."""
from __future__ import annotations

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..")

W, H = 540, 188

CARDS = [
    ("01-jarv1s.svg", "#f59e0b", "jarv1s", ["Listens, runs tools, and answers on the machine."], ""),
    ("02-fuseline.svg", "#2dd4bf", "fuseline", ["One timeline from location, browsing, and app use."], ""),
    ("03-datum.svg", "#c084fc", "Datum", ["Baselines a site, then flags defacement and exposure."], ""),
    ("04-sentinel.svg", "#fb7185", "Sentinel", ["Finds a DDoS flood and runs the mitigation."], ""),
    (
        "05-m1rage.svg",
        "#60a5fa",
        "m1rage",
        ["CTF platform by Team NullBorn", "for Amrita Cybernation 2026."],
        "Private",
    ),
    ("06-pramaan.svg", "#e7e5e4", "Pramaan", ["Pulls and reads evidence from DVR and NVR systems."], "Private"),
]


def card(accent: str, title: str, lines: list[str], mark: str) -> str:
    text = ""
    y = 108
    for line in lines:
        text += f'<text x="22" y="{y}" fill="#d4d4d8" font-size="15">{line}</text>'
        y += 22
    badge = ""
    if mark:
        badge = f'<text x="{W - 22}" y="44" fill="#a1a1aa" font-size="12" text-anchor="end">{mark}</text>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI, Helvetica, Arial, sans-serif">
  <rect width="{W}" height="{H}" rx="14" fill="#0e0e12"/>
  <rect x="0.6" y="0.6" width="{W - 1.2}" height="{H - 1.2}" rx="14" fill="none" stroke="#27272a"/>
  <rect width="7" height="{H}" fill="{accent}"/>
  <circle cx="36" cy="42" r="7" fill="{accent}"/>
  {badge}
  <text x="54" y="48" fill="#fafafa" font-size="26" font-weight="700">{title}</text>
  {text}
</svg>
'''


def main() -> None:
    for name, accent, title, lines, mark in CARDS:
        path = os.path.join(OUT, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(card(accent, title, lines, mark))
        print("wrote", path)


if __name__ == "__main__":
    main()
