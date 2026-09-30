#!/usr/bin/env python3
"""Nameplate only. No slogan."""
from __future__ import annotations

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "banner.svg")

W, H = 1040, 120
BG, LINE = "#0b0b0c", "#2a2a2e"
TEXT, MUTED = "#f4f4f5", "#71717a"


def main() -> None:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-sans-serif, system-ui, Segoe UI, Helvetica, Arial, sans-serif">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <text x="4" y="62" fill="{TEXT}" font-size="44" font-weight="650" letter-spacing="-1.2">Navneet Nanda</text>
  <line x1="4" y1="86" x2="168" y2="86" stroke="{MUTED}" stroke-width="1"/>
</svg>
'''
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
