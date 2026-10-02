#!/usr/bin/env python3
"""Build the Sylvect brand-kit logo suite: SVG variants + PNG renders."""
import os
import cairosvg

ROOT = os.path.expanduser("~/workspace/sylvect-brand-kit")
SVG_DIR = os.path.join(ROOT, "logos", "svg")
PNG_DIR = os.path.join(ROOT, "logos", "png")
os.makedirs(SVG_DIR, exist_ok=True)
os.makedirs(PNG_DIR, exist_ok=True)

# ---- brand constants -------------------------------------------------------
GOLD = "#C9A84C"
DARK_GOLD = "#7A5F25"
RED = "#C0272D"
NEAR_BLACK = "#0B0B0B"
PAPER = "#F7F7F5"
INK = "#151515"
WHITE = "#FFFFFF"
GRAY_DARK_BG = "#7E7E7E"
GRAY_LIGHT_BG = "#6B6B6B"
GRAY_SUB_DARK = "#B5B5B5"
SERIF = "Georgia, 'Times New Roman', serif"
SANS_NARROW = "'Arial Narrow', 'Liberation Sans', Arial, sans-serif"
SANS = "Arial, 'Liberation Sans', sans-serif"


def mark_group(c, transform=""):
    """The 'S' icon mark. c = dict(s, bar, dia)."""
    return (
        f'<g transform="{transform}">\n'
        f'    <text x="112" y="166" text-anchor="middle" fill="{c["s"]}" '
        f'font-family="{SERIF}" font-size="164" font-weight="700">S</text>\n'
        f'    <rect x="0" y="118" width="224" height="18" rx="4" fill="{c["bar"]}"/>\n'
        f'    <rect x="190" y="0" width="18" height="18" transform="rotate(45 199 9)" fill="{c["dia"]}"/>\n'
        f'    <rect x="216" y="0" width="18" height="18" transform="rotate(45 225 9)" fill="{c["dia"]}"/>\n'
        f'    <rect x="-14" y="186" width="18" height="18" transform="rotate(45 -5 195)" fill="{c["dia"]}"/>\n'
        f'    <rect x="12" y="186" width="18" height="18" transform="rotate(45 21 195)" fill="{c["dia"]}"/>\n'
        f'  </g>'
    )


def horizontal_svg(bg, syl, vect, sub, mark_colors):
    # Wordmark geometry measured for the Arial Narrow stack with Liberation
    # Sans Bold as the wide fallback (PIL-measured incl. letter-spacing):
    #   SYL  @118/ls8  -> 245.5 wide ; VECT @118/ls8 -> 338.7 ; IT SERVICES @54/ls6 -> 395.1
    # Positions leave an airy right margin like the source file and never
    # collide, with or without Arial Narrow installed.
    bg_rect = (f'  <rect width="1600" height="420" rx="36" fill="{bg}"/>\n') if bg else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="420" viewBox="0 0 1600 420" role="img">\n'
        f'{bg_rect}'
        f'  {mark_group(mark_colors, transform="translate(96 76)")}\n'
        f'  <text x="360" y="198" fill="{syl}" font-family="{SANS_NARROW}" font-size="118" font-weight="700" letter-spacing="8">SYL</text>\n'
        f'  <text x="628" y="198" fill="{vect}" font-family="{SANS_NARROW}" font-size="118" font-weight="700" letter-spacing="8">VECT</text>\n'
        f'  <text x="998" y="198" fill="{sub}" font-family="{SANS}" font-size="54" font-weight="700" letter-spacing="6">IT SERVICES</text>\n'
        f'</svg>\n'
    )


def stacked_svg(bg, syl, vect, sub, mark_colors):
    # Stacked lockup, optically centered: SYL end-anchored / VECT start-anchored
    # around x=600 with a 29px ink gap (PIL-measured Liberation Sans Bold).
    bg_rect = (f'  <rect width="1200" height="1000" rx="48" fill="{bg}"/>\n') if bg else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1000" viewBox="0 0 1200 1000" role="img">\n'
        f'{bg_rect}'
        f'  {mark_group(mark_colors, transform="translate(376 110) scale(2)")}\n'
        f'  <text x="531" y="745" text-anchor="end" fill="{syl}" font-family="{SANS_NARROW}" font-size="150" font-weight="700" letter-spacing="12">SYL</text>\n'
        f'  <text x="548" y="745" text-anchor="start" fill="{vect}" font-family="{SANS_NARROW}" font-size="150" font-weight="700" letter-spacing="12">VECT</text>\n'
        f'  <text x="600" y="845" text-anchor="middle" fill="{sub}" font-family="{SANS}" font-size="52" font-weight="700" letter-spacing="14">IT SERVICES</text>\n'
        f'</svg>\n'
    )


def icon_svg(bg, mark_colors):
    bg_rect = (f'  <rect width="600" height="600" rx="120" fill="{bg}"/>\n') if bg else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 600 600" role="img">\n'
        f'{bg_rect}'
        f'  {mark_group(mark_colors, transform="translate(114 127) scale(1.693)")}\n'
        f'</svg>\n'
    )


BRAND_MARK = {"s": GOLD, "bar": RED, "dia": DARK_GOLD}
MONO_W = {"s": WHITE, "bar": WHITE, "dia": WHITE}
MONO_B = {"s": "#111111", "bar": "#111111", "dia": "#111111"}


def build_all():
    variants = {
        # horizontal
        "sylvect-logo-horizontal-dark.svg": horizontal_svg(NEAR_BLACK, WHITE, GOLD, GRAY_DARK_BG, BRAND_MARK),
        "sylvect-logo-horizontal-light.svg": horizontal_svg(PAPER, INK, DARK_GOLD, GRAY_LIGHT_BG, BRAND_MARK),
        "sylvect-logo-horizontal-transparent-dark.svg": horizontal_svg(None, WHITE, GOLD, GRAY_SUB_DARK, BRAND_MARK),
        "sylvect-logo-horizontal-transparent-light.svg": horizontal_svg(None, INK, DARK_GOLD, GRAY_LIGHT_BG, BRAND_MARK),
        "sylvect-logo-horizontal-mono-white.svg": horizontal_svg(None, WHITE, WHITE, WHITE, MONO_W),
        "sylvect-logo-horizontal-mono-black.svg": horizontal_svg(None, "#111111", "#111111", "#111111", MONO_B),
        # stacked
        "sylvect-logo-stacked-dark.svg": stacked_svg(NEAR_BLACK, WHITE, GOLD, GRAY_DARK_BG, BRAND_MARK),
        "sylvect-logo-stacked-light.svg": stacked_svg(PAPER, INK, DARK_GOLD, GRAY_LIGHT_BG, BRAND_MARK),
        "sylvect-logo-stacked-mono-white.svg": stacked_svg(None, WHITE, WHITE, WHITE, MONO_W),
        "sylvect-logo-stacked-mono-black.svg": stacked_svg(None, "#111111", "#111111", "#111111", MONO_B),
        # icon
        "sylvect-icon-dark.svg": icon_svg(NEAR_BLACK, BRAND_MARK),
        "sylvect-icon-light.svg": icon_svg(PAPER, BRAND_MARK),
        "sylvect-icon-transparent.svg": icon_svg(None, BRAND_MARK),
        "sylvect-icon-mono-white.svg": icon_svg(None, MONO_W),
        "sylvect-icon-mono-black.svg": icon_svg(None, MONO_B),
    }

    for name, svg in variants.items():
        with open(os.path.join(SVG_DIR, name), "w") as f:
            f.write(svg)
    print(f"wrote {len(variants)} SVGs")

    # ---- PNG renders ------------------------------------------------------------
    # (svg file, png name, output width)
    renders = [
        ("sylvect-logo-horizontal-dark.svg", "sylvect-logo-horizontal-dark@1600.png", 1600),
        ("sylvect-logo-horizontal-dark.svg", "sylvect-logo-horizontal-dark@800.png", 800),
        ("sylvect-logo-horizontal-dark.svg", "sylvect-logo-horizontal-dark@400.png", 400),
        ("sylvect-logo-horizontal-light.svg", "sylvect-logo-horizontal-light@1600.png", 1600),
        ("sylvect-logo-horizontal-light.svg", "sylvect-logo-horizontal-light@800.png", 800),
        ("sylvect-logo-horizontal-transparent-dark.svg", "sylvect-logo-horizontal-transparent-dark@1600.png", 1600),
        ("sylvect-logo-horizontal-mono-white.svg", "sylvect-logo-horizontal-mono-white@1600.png", 1600),
        ("sylvect-logo-stacked-dark.svg", "sylvect-logo-stacked-dark@1200.png", 1200),
        ("sylvect-logo-stacked-dark.svg", "sylvect-logo-stacked-dark@600.png", 600),
        ("sylvect-logo-stacked-light.svg", "sylvect-logo-stacked-light@600.png", 600),
        ("sylvect-icon-dark.svg", "sylvect-icon-dark@1024.png", 1024),
        ("sylvect-icon-dark.svg", "sylvect-icon-dark@512.png", 512),
        ("sylvect-icon-dark.svg", "sylvect-icon-dark@256.png", 256),
        ("sylvect-icon-light.svg", "sylvect-icon-light@512.png", 512),
        ("sylvect-icon-transparent.svg", "sylvect-icon-transparent@1024.png", 1024),
        ("sylvect-icon-dark.svg", "favicon-32.png", 32),
        ("sylvect-icon-dark.svg", "favicon-16.png", 16),
        ("sylvect-icon-dark.svg", "apple-touch-icon-180.png", 180),
    ]
    for src, dst, w in renders:
        cairosvg.svg2png(url=os.path.join(SVG_DIR, src),
                         write_to=os.path.join(PNG_DIR, dst),
                         output_width=w)
    print(f"rendered {len(renders)} PNGs")

    return variants


if __name__ == "__main__":
    build_all()
