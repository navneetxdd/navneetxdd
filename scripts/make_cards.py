#!/usr/bin/env python3
"""Wide project rows. The sentence sits on the same line as the name."""
from __future__ import annotations

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..")

W, H = 1100, 84

ROWS = [
    ("01-jarv1s.svg", "#f59e0b", "jarv1s", "Desktop voice assistant. Speech in, tools, spoken answer.", ""),
    ("02-fuseline.svg", "#2dd4bf", "fuseline", "Location, browser history, and app use on one clock.", ""),
    ("03-datum.svg", "#c084fc", "Datum", "Compares a site to its baseline. Flags defacement and exposure.", ""),
    ("04-sentinel.svg", "#fb7185", "Sentinel", "Detects DDoS traffic and applies the mitigation.", ""),
    ("05-m1rage.svg", "#60a5fa", "m1rage", "CTF platform by Team NullBorn. Amrita Cybernation 2026.", "Private"),
    ("06-pramaan.svg", "#e7e5e4", "Pramaan", "Collects and reads evidence from DVR and NVR recorders.", "Private"),
]


def row(accent: str, title: str, line: str, mark: str) -> str:
    end = ""
    if mark:
        end = f'<text x="{W - 28}" y="48" fill="#71717a" font-size="13" text-anchor="end">{mark}</text>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Segoe UI, Helvetica, Arial, sans-serif">
  <rect width="{W}" height="{H}" fill="#09090b"/>
  <line x1="0" y1="{H - 1}" x2="{W}" y2="{H - 1}" stroke="#27272a"/>
  <rect x="0" y="22" width="3" height="40" fill="{accent}"/>
  <text x="24" y="50" fill="#fafafa" font-size="20" font-weight="650">{title}</text>
  <text x="250" y="50" fill="#a1a1aa" font-size="16">{line}</text>
  {end}
</svg>
'''


def main() -> None:
    for name, accent, title, line, mark in ROWS:
        path = os.path.join(OUT, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(row(accent, title, line, mark))
        print("wrote", path)


if __name__ == "__main__":
    main()
