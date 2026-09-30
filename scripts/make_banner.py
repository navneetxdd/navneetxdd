#!/usr/bin/env python3
"""Nameplate. No degree, no forensic framing."""
from __future__ import annotations

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "banner.svg")

W, H = 920, 132
BG, LINE = "#09090b", "#27272a"
AMBER, TEXT, MUTED = "#f59e0b", "#fafafa", "#a1a1aa"


def main() -> None:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <rect width="{W}" height="{H}" rx="16" fill="{BG}"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="none" stroke="{LINE}"/>
  <rect x="28" y="28" width="36" height="3" fill="{AMBER}"/>
  <text x="28" y="68" fill="{TEXT}" font-size="34" font-weight="700">Navneet Nanda</text>
  <text x="28" y="98" fill="{MUTED}" font-size="15">Software, mostly with a team.</text>
</svg>
'''
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
