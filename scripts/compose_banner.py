#!/usr/bin/env python3
"""Lay the name and quote into the dark left of the photograph."""
from __future__ import annotations

import os

from PIL import Image, ImageDraw, ImageFont

SRC = r"C:\Users\navne\.cursor\projects\c-Users-navne-Desktop-jarv1s\assets\profile-banner.jpg"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "banner.jpg")

NAME = r"C:\Windows\Fonts\georgiab.ttf"
ITALIC = r"C:\Windows\Fonts\georgiai.ttf"
SANS = r"C:\Windows\Fonts\segoeui.ttf"


def main() -> None:
    im = Image.open(SRC).convert("RGB")
    im = im.resize((1600, 900), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(im)
    name = ImageFont.truetype(NAME, 92)
    quote = ImageFont.truetype(ITALIC, 28)
    attr = ImageFont.truetype(SANS, 18)
    cream = (245, 236, 220)
    dim = (196, 176, 146)
    x, y = 72, 250
    draw.text((x, y), "Navneet", font=name, fill=cream)
    draw.text((x + 2, y + 120), "The details are not the details.", font=quote, fill=cream)
    draw.text((x + 2, y + 158), "They make the design.", font=quote, fill=cream)
    draw.text((x + 2, y + 210), "Charles Eames", font=attr, fill=dim)
    im.save(OUT, "JPEG", quality=90, optimize=True)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
