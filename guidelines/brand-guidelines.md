# Sylvect IT Services — Brand Guidelines

Version 1.0 · 2026-10-01 · Source palette and logo verified from sylvect.biz (2026-09-25).

## 1. Who we are

**Sylvect IT Services** — reliable technology, better business systems. Managed IT, cybersecurity, automation, and infrastructure for New Jersey and NYC small businesses. The brand reads as *dark luxury IT consultancy*: premium, precise, no fluff.

**Voice:** blunt, builder-grade, plainspoken. Say what it does, show the work, skip the jargon. If a sentence wouldn't survive a client reading it twice, cut it.

## 2. Logo

`logos/svg/` holds the master vector files; `logos/png/` holds web-ready rasters.

| File | Use |
|---|---|
| `sylvect-logo-horizontal-*.svg` | Default lockup — website header, documents, email |
| `sylvect-logo-stacked-*.svg` | Square-ish spaces — splash screens, print covers |
| `sylvect-icon-*.svg` | Avatars, favicons, app icons, watermarks |
| `*-transparent-*.svg` | Place over photos, gradients, or video |
| `*-mono-white.svg` / `*-mono-black.svg` | One-color print, fax-grade docs, engraving, single-ink jobs |

**Pick by background:** `dark` variants on dark surfaces, `light` variants on light surfaces, `transparent-dark` over dark imagery, `transparent-light` over light imagery.

### Clear space

Keep clear space around the logo equal to the cap-height of the "S" mark on all sides. Nothing — no text, no rules, no imagery edges — enters that zone.

### Minimum sizes

| Lockup | Digital min | Print min |
|---|---|---|
| Horizontal | 140 px wide | 38 mm wide |
| Stacked | 96 px wide | 26 mm wide |
| Icon | 32 px | 8 mm |

Below these, the diamonds and "IT SERVICES" stop being legible — use the icon alone.

### Don'ts

- Never stretch, squash, rotate, or re-set the wordmark in another font.
- Never recolor the logo outside the supplied variants (no gold-on-gold, no red wordmark).
- Never put the full-color logo on a red background or a busy photo without a scrim.
- Never add drop shadows, bevels, outlines, or gradients to the logo.
- Never rearrange the lockup (mark always left/above, wordmark right/below).

## 3. Color

Full swatches: `colors/sylvect-palette.svg`. Code: `colors/sylvect.css`, `colors/sylvect-tokens.json`, `colors/sylvect-tailwind.js`.

**The ratio: 60 / 30 / 10.** 60% near-black (or paper on light layouts), 30% white/gray text and card surfaces, 10% gold. Red is a *CTA accent*, not a brand color for decoration — one red element per visual, max ~5% of the canvas.

| Color | Hex | Job |
|---|---|---|
| Brand gold | `#C9A84C` | Emphasis, headlines accents, hovers, dividers |
| Dark gold | `#7A5F25` | Eyebrows on light, logo diamonds |
| CTA red | `#C0272D` (hover `#9E2025`) | Primary buttons only |
| Near-black | `#0B0B0B` | Default background |
| Cards | `#121212` / `#171717` / `#1D1D1D` | Layered dark surfaces |
| Paper | `#F7F7F5` | Light section background |
| Ink | `#151515` | Dark text |

**Contrast checks (must pass):** gold `#C9A84C` on near-black — large text and accents only, never small body copy. Body copy on dark is `#FFFFFF` at 70%. On light sections, eyebrows switch to dark gold `#7A5F25`.

## 4. Typography

Spec: `typography/fonts.md`. Short version: **DM Sans** for headings/UI, **IBM Plex Mono** for eyebrows/labels (always caps, letterspaced, gold), **Georgia** serif for the logo mark and pull-quote accents only. Arial Narrow is logo-wordmark-only.

## 5. Imagery & graphic style

Dark editorial: near-black grounds, a soft gold radial glow, a faint grid, glassy gradient cards, subtle film grain. Real build photos beat stock — console screenshots, racks, cable runs. When a visual carries the brand, put the lockup top-left or bottom-right and keep to one red accent.

## 6. Social

Sizes and safe zones: `templates/social-specs.md`. Ready-made starting points: `templates/sylvect-avatar.svg` (profile picture), `templates/sylvect-cover-banner.svg` (1920×640 headers), `templates/sylvect-post-4x5.svg` (1080×1350 post template), `templates/sylvect-story-9x16.svg` (1080×1920 story template). SVGs open in Figma/Illustrator/Inkscape — replace the `[bracketed]` placeholder copy, keep the styles.

## 7. Email signature

`templates/email-signature.html` — table-based, works in Gmail/Outlook/Apple Mail. Swap in the real name, title, and phone. The logo hotlinks the `main` branch of this repo, so it stays current automatically.

## 8. Files & versioning

- Masters are the SVGs. PNGs are exports — regenerate with `bin/build_logos.py` / `bin/build_templates.py`, don't hand-edit.
- Name new exports `sylvect-<what>-<variant>@<width>.png`.
- This kit is v1.0. Note the version and date in commit messages when the kit changes.

---
© Slate Enterprises LLC, operating as Sylvect IT Services. All rights reserved.
