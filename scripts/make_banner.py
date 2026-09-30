#!/usr/bin/env python3
"""Wave header and footer. Same structure as the capsule-render profiles."""
from __future__ import annotations

import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")


def header() -> str:
    w, h = 1200, 300
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#1b1038"/>
      <stop offset="0.55" stop-color="#3b1d63"/>
      <stop offset="1" stop-color="#111827"/>
    </linearGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#sky)"/>
  <circle cx="180" cy="70" r="90" fill="#f59e0b" fill-opacity="0.12"/>
  <circle cx="980" cy="40" r="140" fill="#60a5fa" fill-opacity="0.10"/>
  <path d="M0 210 C 180 160, 320 250, 520 210 C 740 164, 900 250, 1200 190 L 1200 300 L 0 300 Z" fill="#0b0b10"/>
  <path d="M0 236 C 220 190, 400 270, 640 228 C 860 190, 1000 250, 1200 214 L 1200 300 L 0 300 Z" fill="#f59e0b" fill-opacity="0.9"/>
  <text x="64" y="108" fill="#fafafa" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="68" font-weight="700" letter-spacing="-1.8">Navneet</text>
  <text x="66" y="150" fill="#e4e4e7" font-family="Georgia, Times New Roman, serif" font-size="18">“The function of good software is to make the complex appear to be simple.”</text>
  <text x="66" y="176" fill="#a1a1aa" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="14">Grady Booch</text>
</svg>
'''


def footer() -> str:
    w, h = 1200, 90
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <rect width="{w}" height="{h}" fill="#0b0b10"/>
  <path d="M0 40 C 200 10, 400 70, 640 36 C 880 2, 1040 60, 1200 28 L 1200 0 L 0 0 Z" fill="#f59e0b"/>
</svg>
'''


def main() -> None:
    for name, body in (("banner.svg", header()), ("footer.svg", footer())):
        path = os.path.join(ROOT, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(body)
        print("wrote", path)


if __name__ == "__main__":
    main()
