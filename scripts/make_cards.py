#!/usr/bin/env python3
"""Project posters. One sentence each."""
from __future__ import annotations

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "..")

W, H = 560, 210

# file, accent, title, line, mark
CARDS = [
    ("01-jarv1s.svg", "#f59e0b", "jarv1s", "Voice assistant that runs on the machine.", ""),
    ("02-fuseline.svg", "#2dd4bf", "fuseline", "Location, browsing, and app use in one timeline.", ""),
    ("03-datum.svg", "#a78bfa", "Datum", "Detects website defacement and checks exposure.", ""),
    ("04-sentinel.svg", "#fb7185", "Sentinel", "Detects and mitigates DDoS traffic.", ""),
    (
        "05-m1rage.svg",
        "#60a5fa",
        "m1rage",
        "CTF platform by Team NullBorn, Amrita Cybernation 2026.",
        "Private",
    ),
    ("06-pramaan.svg", "#f4f4f5", "Pramaan", "DVR and NVR analysis across vendors.", "Private"),
]


def card(accent: str, title: str, line: str, mark: str) -> str:
    mark_svg = ""
    if mark:
        mark_svg = (
            f'<text x="{W - 28}" y="46" fill="#a1a1aa" font-size="13" text-anchor="end">{mark}</text>'
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-sans-serif, system-ui, Segoe UI, Helvetica, Arial, sans-serif">
  <rect width="{W}" height="{H}" rx="18" fill="#101014"/>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="#2a2a30"/>
  <rect x="0" y="0" width="{W}" height="6" rx="3" fill="{accent}"/>
  <rect x="28" y="36" width="28" height="4" fill="{accent}"/>
  {mark_svg}
  <text x="28" y="108" fill="#fafafa" font-size="36" font-weight="700">{title}</text>
  <text x="28" y="152" fill="#a1a1aa" font-size="16">{line}</text>
</svg>
'''


def main() -> None:
    for name, accent, title, line, mark in CARDS:
        path = os.path.join(OUT_DIR, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(card(accent, title, line, mark))
        print("wrote", path)


if __name__ == "__main__":
    main()
