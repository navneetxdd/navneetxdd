#!/usr/bin/env python3
"""Wide nameplate. No degree line."""
from __future__ import annotations

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "banner.svg")

W, H = 900, 148
BG, PANEL, LINE = "#0c0a09", "#1c1917", "#44403c"
AMBER, TEXT, MUTED = "#f59e0b", "#fafaf9", "#a8a29e"


def main() -> None:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <defs>
    <linearGradient id="bbg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{PANEL}"/>
      <stop offset="1" stop-color="{BG}"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" rx="14" fill="url(#bbg)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{LINE}"/>
  <rect x="0" y="0" width="6" height="{H}" fill="{AMBER}"/>
  <text x="36" y="28" fill="{MUTED}" font-size="11" letter-spacing="2">NAVNEET@LAB</text>
  <text x="36" y="78" fill="{TEXT}" font-size="36" font-weight="700">Navneet Nanda</text>
  <text x="36" y="112" fill="{AMBER}" font-size="15">Phone timelines. A voice on the machine. A few rooms that stay shut.</text>
  <text x="{W-36}" y="28" fill="{MUTED}" font-size="11" text-anchor="end">file 01</text>
</svg>
'''
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
