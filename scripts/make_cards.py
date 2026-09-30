#!/usr/bin/env python3
"""Project cards. One fact each. No slogans."""
from __future__ import annotations

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "..")

W, H = 500, 176
BG, LINE = "#111113", "#2a2a2e"
TEXT, MUTED, MARK = "#f4f4f5", "#a1a1aa", "#e4e4e7"

# filename, number, title, description, corner label or ""
CARDS = [
    (
        "01-jarv1s.svg",
        "01",
        "jarv1s",
        "Voice assistant that runs on the machine.",
        "",
    ),
    (
        "02-fuseline.svg",
        "02",
        "fuseline",
        "Location, browsing, and app use in one timeline.",
        "",
    ),
    (
        "03-datum.svg",
        "03",
        "Datum",
        "Detects website defacement and checks exposure.",
        "",
    ),
    (
        "04-sentinel.svg",
        "04",
        "Sentinel",
        "Detects and mitigates DDoS traffic.",
        "",
    ),
    (
        "05-m1rage.svg",
        "05",
        "m1rage",
        "CTF platform by Team NullBorn",
        "for Amrita Cybernation 2026.",
        "Private",
    ),
    (
        "06-pramaan.svg",
        "06",
        "Pramaan",
        "DVR and NVR analysis across vendors.",
        "Private",
    ),
]


def card(index: str, title: str, lines: list[str], mark: str) -> str:
    body = ""
    y = 108
    for line in lines:
        body += f'  <text x="28" y="{y}" fill="{MUTED}" font-size="15">{line}</text>\n'
        y += 22
    corner = ""
    if mark:
        corner = (
            f'  <text x="{W - 28}" y="42" fill="{MARK}" font-size="12" '
            f'text-anchor="end">{mark}</text>\n'
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-sans-serif, system-ui, Segoe UI, Helvetica, Arial, sans-serif">
  <rect width="{W}" height="{H}" rx="16" fill="{BG}"/>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="16" fill="none" stroke="{LINE}"/>
  <text x="{W - 16}" y="148" fill="#1c1c20" font-size="84" font-weight="700" text-anchor="end">{index}</text>
  <text x="28" y="42" fill="{MUTED}" font-size="12" letter-spacing="1.6">{index}</text>
{corner}  <text x="28" y="78" fill="{TEXT}" font-size="28" font-weight="650">{title}</text>
{body}</svg>
'''


def main() -> None:
    for item in CARDS:
        name, index, title, *rest = item
        mark = rest[-1]
        lines = list(rest[:-1])
        path = os.path.join(OUT_DIR, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(card(index, title, lines, mark))
        print("wrote", path)


if __name__ == "__main__":
    main()
