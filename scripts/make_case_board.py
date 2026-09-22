#!/usr/bin/env python3
"""Forensic case-board SVG — timeline + radar, not an ASCII portrait."""
from __future__ import annotations

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "case-board.svg")

W, H = 380, 376
BG, PANEL, LINE = "#0c0a09", "#1c1917", "#44403c"
AMBER, AMBER2, TEXT, MUTED = "#f59e0b", "#fb923c", "#fafaf9", "#a8a29e"
DIM = "#78716c"


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main() -> None:
    # Timeline event markers (purely decorative identity art)
    events = [
        (48, "GPS"),
        (110, "ADB"),
        (172, "HTTP"),
        (234, "CALL"),
        (296, "LOC"),
    ]

    ticks = []
    for x, label in events:
        ticks.append(
            f'<line x1="{x}" y1="248" x2="{x}" y2="268" stroke="{AMBER}" stroke-width="2"/>'
            f'<circle cx="{x}" cy="248" r="4.5" fill="{AMBER}"/>'
            f'<text x="{x}" y="286" fill="{MUTED}" font-size="9" text-anchor="middle">{label}</text>'
        )

    # Radar rings
    cx, cy, r0 = 190, 128, 62
    rings = []
    for i, r in enumerate([r0 * 0.35, r0 * 0.6, r0 * 0.85, r0]):
        rings.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="none" stroke="{LINE}" '
            f'stroke-opacity="{0.35 + i * 0.1}" stroke-dasharray="3 4"/>'
        )
    # Sweep wedge (static with soft animate)
    sweep = (
        f'<path d="M{cx},{cy} L{cx},{cy - r0} A{r0},{r0} 0 0 1 {cx + r0 * 0.55:.1f},{cy - r0 * 0.84:.1f} Z" '
        f'fill="{AMBER}" fill-opacity="0.12">'
        f'<animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" '
        f'to="360 {cx} {cy}" dur="8s" repeatCount="indefinite"/>'
        f"</path>"
    )
    blips = [
        (cx + 28, cy - 18, 3.2),
        (cx - 36, cy + 8, 2.6),
        (cx + 12, cy + 34, 2.4),
        (cx - 18, cy - 40, 2.8),
    ]
    blip_svg = "".join(
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="{AMBER2}">'
        f'<animate attributeName="opacity" values="0.35;1;0.35" dur="{1.6 + i * 0.35:.2f}s" repeatCount="indefinite"/>'
        f"</circle>"
        for i, (x, y, r) in enumerate(blips)
    )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <defs>
    <linearGradient id="cbg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{PANEL}"/><stop offset="1" stop-color="{BG}"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" rx="12" fill="url(#cbg)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{LINE}"/>
  <line x1="0" y1="30" x2="{W}" y2="30" stroke="{LINE}"/>
  <circle cx="18" cy="15" r="5" fill="#ff5f56"/>
  <circle cx="34" cy="15" r="5" fill="#ffbd2e"/>
  <circle cx="50" cy="15" r="5" fill="#27c93f"/>
  <text x="{W/2}" y="19.5" fill="{MUTED}" font-size="11.5" text-anchor="middle">navneet@lab · CASE BOARD</text>

  <text x="20" y="54" fill="{AMBER}" font-size="11" font-weight="700">ACTIVE CASE</text>
  <text x="20" y="72" fill="{TEXT}" font-size="13" font-weight="700">mobile timeline correlation</text>
  <text x="20" y="90" fill="{DIM}" font-size="11">fuse GPS · browsing · app usage into one clock</text>

  {"".join(rings)}
  {sweep}
  <line x1="{cx - r0}" y1="{cy}" x2="{cx + r0}" y2="{cy}" stroke="{LINE}" stroke-opacity="0.5"/>
  <line x1="{cx}" y1="{cy - r0}" x2="{cx}" y2="{cy + r0}" stroke="{LINE}" stroke-opacity="0.5"/>
  {blip_svg}
  <text x="{cx}" y="{cy + r0 + 18}" fill="{MUTED}" font-size="10" text-anchor="middle">signal sweep · live artifacts</text>

  <text x="20" y="232" fill="{AMBER}" font-size="11" font-weight="700">FUSELINE STRIP</text>
  <line x1="20" y1="248" x2="360" y2="248" stroke="{LINE}" stroke-width="2"/>
  {"".join(ticks)}

  <text x="20" y="318" fill="{MUTED}" font-size="10">STATUS</text>
  <text x="78" y="318" fill="{AMBER2}" font-size="10">shipping · learning · breaking things on purpose</text>
  <text x="20" y="340" fill="{MUTED}" font-size="10">FOCUS</text>
  <text x="78" y="340" fill="{TEXT}" font-size="10">forensics · networks · systems security</text>
  <text x="20" y="362" fill="{DIM}" font-size="9">not a dashboard. a desk.</text>
</svg>
'''
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
