#!/usr/bin/env python3
"""Terminal dossier card — amber lab aesthetic."""
from __future__ import annotations

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "dossier.svg")

W, H = 500, 376
BG, PANEL, LINE = "#0c0a09", "#1c1917", "#44403c"
AMBER, CYAN, TEXT, MUTED = "#f59e0b", "#2dd4bf", "#fafaf9", "#a8a29e"


def row(y: float, key: str, val: str, delay: float) -> str:
    return f'''<g opacity="0" transform="translate(0,5)">
  <text x="22" y="{y}" fill="{AMBER}" font-size="12.5" font-weight="700">{key}</text>
  <text x="118" y="{y}" fill="{TEXT}" font-size="12.5">{val}</text>
  <animate attributeName="opacity" from="0" to="1" begin="{delay:.2f}s" dur="0.35s" fill="freeze"/>
  <animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="{delay:.2f}s" dur="0.35s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
</g>'''


def main() -> None:
    rows = [
        (78, "Now", "Building timelines that hold up under scrutiny"),
        (100, "Also", "CTF curious · packet nerd · ships when it works"),
        (122, "Edu", "B.Tech CSE (Cybersecurity)"),
        (144, "Loc", "Between Wireshark and the debugger"),
        (176, "— Lab", ""),
        (198, "Forensics", "Plaso · ADB · SQLite · timeline correlation"),
        (220, "Defense", "Network monitoring · DDoS mitigation ideas"),
        (242, "Build", "Python · FastAPI · React · TypeScript"),
        (264, "Ops", "Linux · Docker · Git · PowerShell"),
        (296, "Ship", "fuseline · Sentinel · CyberShield · c0mr4d35"),
        (328, "Mood", "caffeine optional · evidence mandatory"),
    ]

    parts = []
    delay = 0.12
    for y, k, v in rows:
        if k.startswith("—"):
            parts.append(
                f'''<g opacity="0">
  <text x="22" y="{y}" fill="{CYAN}" font-size="12.5" font-weight="700">{k}</text>
  <line x1="78" y1="{y-4}" x2="478" y2="{y-4}" stroke="{LINE}" stroke-opacity="0.85"/>
  <animate attributeName="opacity" from="0" to="1" begin="{delay:.2f}s" dur="0.35s" fill="freeze"/>
</g>'''
            )
        else:
            parts.append(row(y, k, v, delay))
        delay += 0.06

    # blinking cursor
    parts.append(
        f'''<text x="22" y="358" fill="{MUTED}" font-size="12">navneet@lab:~$</text>
<rect x="128" y="346" width="8" height="14" fill="{AMBER}">
  <animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/>
</rect>'''
    )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <defs>
    <linearGradient id="dbg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{PANEL}"/><stop offset="1" stop-color="{BG}"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" rx="12" fill="url(#dbg)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{LINE}"/>
  <line x1="0" y1="30" x2="{W}" y2="30" stroke="{LINE}"/>
  <circle cx="18" cy="15" r="5" fill="#ff5f56"/>
  <circle cx="34" cy="15" r="5" fill="#ffbd2e"/>
  <circle cx="50" cy="15" r="5" fill="#27c93f"/>
  <text x="{W/2}" y="19.5" fill="{MUTED}" font-size="11.5" text-anchor="middle">navneet@lab: ~$ casefile --brief</text>

  <text x="22" y="56" font-size="14" font-weight="700">
    <tspan fill="#f59e0b">navneet</tspan><tspan fill="{MUTED}">@</tspan><tspan fill="{CYAN}">lab</tspan>
  </text>
  <line x1="150" y1="52" x2="478" y2="52" stroke="{LINE}" stroke-opacity="0.8"/>

  {"".join(parts)}
</svg>
'''
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
