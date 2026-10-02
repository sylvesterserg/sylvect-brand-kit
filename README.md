# Sylvect IT Services — Brand Kit

Official logos, colors, typography, templates, and usage guidelines for Sylvect IT Services. Palette and logo verified from [sylvect.biz](https://sylvect.biz).

## What's inside

```
sylvect-brand-kit/
├── logos/
│   ├── svg/            # 15 master vector logos (horizontal, stacked, icon —
│   │                     # dark / light / transparent / monochrome)
│   └── png/            # Web-ready rasters + favicon + apple-touch-icon
├── colors/
│   ├── sylvect-palette.svg / .png   # Swatch card
│   ├── sylvect.css                 # CSS custom properties
│   ├── sylvect-tokens.json         # Design tokens
│   └── sylvect-tailwind.js         # Tailwind theme extension
├── typography/
│   └── fonts.md        # DM Sans · IBM Plex Mono · Georgia · Arial Narrow
├── templates/
│   ├── sylvect-avatar.svg          # Profile picture master
│   ├── sylvect-cover-banner.svg    # 1920×640 social headers
│   ├── sylvect-post-4x5.svg        # 1080×1350 post template
│   ├── sylvect-story-9x16.svg      # 1080×1920 story template
│   ├── social-specs.md             # Platform sizes + safe zones
│   └── email-signature.html        # Table-based signature
├── guidelines/
│   └── brand-guidelines.md         # The rules: logo, color, type, voice, don'ts
└── bin/
    ├── build_logos.py              # Regenerate the logo suite
    └── build_templates.py          # Regenerate the templates
```

## Quick start

1. **Pick a logo:** dark backgrounds → `*-dark.*`, light backgrounds → `*-light.*`, over photos → `*-transparent-*.*`, one-color jobs → `*-mono-*.*`. Full chooser in `guidelines/brand-guidelines.md`.
2. **Colors:** drop `colors/sylvect.css` into your project or merge `sylvect-tailwind.js` into your Tailwind config.
3. **Fonts:** load DM Sans + IBM Plex Mono from Google Fonts (see `typography/fonts.md`).
4. **Socials:** open a template SVG in Figma/Illustrator/Inkscape, replace the `[bracketed]` copy, export.

## The palette

| | |
|---|---|
| `#C9A84C` Brand gold | `#0B0B0B` Near-black |
| `#7A5F25` Dark gold | `#F7F7F5` Paper |
| `#C0272D` CTA red | `#151515` Ink |

60 / 30 / 10: 60% near-black (or paper), 30% text/surfaces, 10% gold. Red is for CTAs only — one per visual.

## Versioning

Masters are the SVGs — never hand-edit a PNG, regenerate it with the `bin/` scripts. Note the kit version and date in commit messages.

---
© Slate Enterprises LLC, operating as Sylvect IT Services. All rights reserved.
