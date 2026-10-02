#!/usr/bin/env python3
"""Build Sylvect brand-kit templates: avatar, banner, post, story."""
import os
import sys
import cairosvg

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_logos import (
    mark_group, GOLD, DARK_GOLD, RED, NEAR_BLACK, PAPER, INK,
    WHITE, GRAY_DARK_BG, GRAY_SUB_DARK, SERIF, SANS_NARROW, SANS,
)

ROOT = os.path.expanduser("~/workspace/sylvect-brand-kit")
TDIR = os.path.join(ROOT, "templates")
os.makedirs(TDIR, exist_ok=True)

BRAND = {"s": GOLD, "bar": RED, "dia": DARK_GOLD}
DM = "'DM Sans', 'Liberation Sans', sans-serif"
PLEX = "'IBM Plex Mono', monospace"


def defs_grid_glow(gid="g"):
    return f"""<defs>
    <radialGradient id="{gid}-glow" cx="50%" cy="0%" r="75%">
      <stop offset="0%" stop-color="{GOLD}" stop-opacity="0.16"/>
      <stop offset="60%" stop-color="{GOLD}" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="{GOLD}" stop-opacity="0"/>
    </radialGradient>
    <pattern id="{gid}-grid" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M48 0H0V48" fill="none" stroke="#FFFFFF" stroke-opacity="0.045" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="100%" height="100%" fill="{NEAR_BLACK}"/>
  <rect width="100%" height="100%" fill="url(#{gid}-glow)"/>
  <rect width="100%" height="100%" fill="url(#{gid}-grid)"/>"""


def lockup_group(colors, transform, syl, vect, sub):
    """Horizontal lockup content (no background) as a scalable group."""
    return (
        f'<g transform="{transform}">'
        f'{mark_group(colors, transform="translate(96 76)")}'
        f'<text x="360" y="198" fill="{syl}" font-family="{SANS_NARROW}" font-size="118" font-weight="700" letter-spacing="8">SYL</text>'
        f'<text x="628" y="198" fill="{vect}" font-family="{SANS_NARROW}" font-size="118" font-weight="700" letter-spacing="8">VECT</text>'
        f'<text x="998" y="198" fill="{sub}" font-family="{SANS}" font-size="54" font-weight="700" letter-spacing="6">IT SERVICES</text>'
        f'</g>'
    )


def write(name, svg):
    with open(os.path.join(TDIR, name), "w") as f:
        f.write(svg)


# ---- 1. avatar (512x512) ----------------------------------------------------
avatar = f"""<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512" role="img">
  <rect width="512" height="512" rx="112" fill="{NEAR_BLACK}"/>
  <rect x="30" y="30" width="452" height="452" rx="92" fill="none" stroke="{GOLD}" stroke-width="5" opacity="0.9"/>
  {mark_group(BRAND, transform="translate(103 115) scale(1.387)")}
</svg>
"""
write("sylvect-avatar.svg", avatar)

# ---- 2. cover banner (1920x640) ---------------------------------------------
banner = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="640" viewBox="0 0 1920 640" role="img">
  {defs_grid_glow("b")}
  {lockup_group(BRAND, "translate(429 130) scale(0.72)", WHITE, GOLD, GRAY_SUB_DARK)}
  <rect x="880" y="372" width="160" height="5" fill="{GOLD}"/>
  <text x="960" y="450" text-anchor="middle" fill="{GOLD}" font-family="{PLEX}" font-size="30" letter-spacing="8">RELIABLE TECHNOLOGY &#183; BETTER BUSINESS SYSTEMS</text>
  <text x="960" y="512" text-anchor="middle" fill="#FFFFFF" opacity="0.55" font-family="{PLEX}" font-size="24" letter-spacing="6">MANAGED IT &#183; CYBERSECURITY &#183; AUTOMATION &#183; INFRASTRUCTURE</text>
</svg>
"""
write("sylvect-cover-banner.svg", banner)

# ---- 3. post template 4:5 (1080x1350) ----------------------------------------
post = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350" role="img">
  {defs_grid_glow("p")}
  <!-- EDITABLE PLACEHOLDERS: replace bracketed text, keep styles -->
  <text x="120" y="190" fill="{GOLD}" font-family="{PLEX}" font-size="30" letter-spacing="8">[CATEGORY]</text>
  <text x="115" y="330" fill="#FFFFFF" font-family="{DM}" font-size="88" font-weight="700">[Your headline</text>
  <text x="115" y="432" fill="#FFFFFF" font-family="{DM}" font-size="88" font-weight="700">goes here]</text>
  <rect x="120" y="500" width="120" height="6" fill="{GOLD}"/>
  <text x="120" y="600" fill="#FFFFFF" opacity="0.7" font-family="{DM}" font-size="36">[Two or three lines of supporting</text>
  <text x="120" y="652" fill="#FFFFFF" opacity="0.7" font-family="{DM}" font-size="36">copy in your voice.]</text>
  <rect x="120" y="740" width="360" height="92" rx="46" fill="{RED}"/>
  <text x="300" y="798" text-anchor="middle" fill="#FFFFFF" font-family="{DM}" font-size="36" font-weight="700">[Learn more]</text>
  {lockup_group(BRAND, "translate(102 1133) scale(0.22)", WHITE, GOLD, GRAY_SUB_DARK)}
  <text x="960" y="1192" text-anchor="end" fill="{GRAY_DARK_BG}" font-family="{PLEX}" font-size="24" letter-spacing="3">sylvect.biz</text>
</svg>
"""
write("sylvect-post-4x5.svg", post)

# ---- 4. story template 9:16 (1080x1920) --------------------------------------
story = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920" role="img">
  {defs_grid_glow("s")}
  <!-- EDITABLE PLACEHOLDERS: replace bracketed text, keep styles -->
  <g transform="translate(408 170) scale(1.2)">{mark_group(BRAND)}</g>
  <text x="540" y="620" text-anchor="middle" fill="{GOLD}" font-family="{PLEX}" font-size="30" letter-spacing="8">[CATEGORY]</text>
  <text x="540" y="780" text-anchor="middle" fill="#FFFFFF" font-family="{DM}" font-size="96" font-weight="700">[Your]</text>
  <text x="540" y="892" text-anchor="middle" fill="#FFFFFF" font-family="{DM}" font-size="96" font-weight="700">[headline]</text>
  <text x="540" y="1004" text-anchor="middle" fill="#FFFFFF" font-family="{DM}" font-size="96" font-weight="700">[here]</text>
  <text x="540" y="1120" text-anchor="middle" fill="#FFFFFF" opacity="0.7" font-family="{DM}" font-size="36">[One line of context.]</text>
  <rect x="340" y="1230" width="400" height="100" rx="50" fill="{RED}"/>
  <text x="540" y="1294" text-anchor="middle" fill="#FFFFFF" font-family="{DM}" font-size="38" font-weight="700">[Swipe up]</text>
  {lockup_group(BRAND, "translate(336 1560) scale(0.28)", WHITE, GOLD, GRAY_SUB_DARK)}
  <text x="540" y="1720" text-anchor="middle" fill="{GRAY_DARK_BG}" font-family="{PLEX}" font-size="26" letter-spacing="4">sylvect.biz</text>
</svg>
"""
write("sylvect-story-9x16.svg", story)

# ---- PNG previews ------------------------------------------------------------
for src, dst, w in [
    ("sylvect-avatar.svg", "sylvect-avatar@512.png", 512),
    ("sylvect-cover-banner.svg", "sylvect-cover-banner@1920.png", 1920),
    ("sylvect-post-4x5.svg", "sylvect-post-4x5@1080.png", 1080),
    ("sylvect-story-9x16.svg", "sylvect-story-9x16@540.png", 540),
]:
    cairosvg.svg2png(url=os.path.join(TDIR, src),
                     write_to=os.path.join(TDIR, dst), output_width=w)
print("templates built: 4 SVG + 4 PNG previews")
