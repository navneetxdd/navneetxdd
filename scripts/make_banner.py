#!/usr/bin/env python3
"""Type-led header. No wave, no last name."""
from __future__ import annotations

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "banner.svg")


def main() -> None:
    w, h = 1100, 220
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="Georgia, 'Iowan Old Style', 'Palatino Linotype', serif">
  <rect width="{w}" height="{h}" fill="#09090b"/>
  <text x="8" y="48" fill="#a1a1aa" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="13" letter-spacing="3">NAVNEET</text>
  <text x="8" y="112" fill="#fafafa" font-size="32">What I cannot create,</text>
  <text x="8" y="156" fill="#fafafa" font-size="32">I do not understand.</text>
  <text x="8" y="196" fill="#71717a" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="14">Richard Feynman</text>
</svg>
'''
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
