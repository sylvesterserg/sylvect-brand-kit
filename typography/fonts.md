# Sylvect IT Services — Typography

## Brand typefaces

| Role | Typeface | Google Fonts | Stack |
|---|---|---|---|
| Headings / UI | **DM Sans** | [DM Sans](https://fonts.google.com/specimen/DMSans) | `"DM Sans", system-ui, sans-serif` |
| Eyebrows / labels / numbers | **IBM Plex Mono** | [IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono) | `"IBM Plex Mono", ui-monospace, monospace` |
| Serif accents / logo "S" | **Georgia** (system serif) | — | `Georgia, "Playfair Display", serif` |
| Logo wordmark | **Arial Narrow** | — (system) | `"Arial Narrow", "Liberation Sans", Arial, sans-serif` |

Web fallback for the serif accent: [Playfair Display](https://fonts.google.com/specimen/Playfair+Display).

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

## Type scale (web)

| Element | Font | Size / weight | Notes |
|---|---|---|---|
| Display headline | DM Sans | 64–88px / 700 | Tight tracking (-0.02em), white or gold |
| Section headline | DM Sans | 40–48px / 700 | White on dark, ink on light |
| Subhead | DM Sans | 24–28px / 500 | Body color |
| Body | DM Sans | 17–18px / 400 | `rgba(255,255,255,.7)` on dark, `#151515` on light |
| Eyebrow / kicker | IBM Plex Mono | 13–15px / 500 | ALL CAPS, letter-spacing 0.25em, gold (dark) / dark gold (light) |
| Button | DM Sans | 16px / 700 | White on CTA red |
| Caption / meta | IBM Plex Mono | 13px / 400 | Muted gray |

## Rules

- Headings: DM Sans Bold, never the serif. The serif belongs to the logo mark and pull-quote accents only.
- Eyebrows are always Plex Mono, always caps, always letterspaced, always gold (on dark) or dark gold (on light).
- CTA red is for buttons, never for text links. Text links: gold, underline on hover.
- Maximum two typefaces per visual. The wordmark font (Arial Narrow) is logo-only — never set headlines in it.
