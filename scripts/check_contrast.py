#!/usr/bin/env python3
"""WCAG 2.1 contrast check for Azimuth color tokens. Stdlib only."""

def lin(c):
    c = c / 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

def lum(hexstr):
    h = hexstr.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)

def ratio(fg, bg):
    a, b = lum(fg), lum(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)

INK = "#0E1418"
SURFACE = "#11181C"
CHECKS = [
    ("text on ink",        "#D6E0E4", INK,     4.5),
    ("muted on ink",       "#7E939B", INK,     4.5),
    ("accent on ink",      "#5FB3A3", INK,     3.0),  # links: also underlined
    ("ink on accent btn",  "#0E1418", "#5FB3A3", 4.5),
    ("muted on surface",   "#7E939B", SURFACE, 4.5),
    ("text on surface",    "#D6E0E4", SURFACE, 4.5),
]
fail = False
for name, fg, bg, mn in CHECKS:
    r = ratio(fg, bg)
    ok = r >= mn
    fail |= not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name:22s} {r:5.2f} (min {mn})")
raise SystemExit(1 if fail else 0)
