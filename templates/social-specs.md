# Sylvect IT Services — Social Specs

Canvas sizes, safe zones, and which kit file to start from. All sizes in pixels.

## Profile pictures

| Platform | Upload | Displays as | Start from |
|---|---|---|---|
| Instagram | 320×320 (min 110) | Circle crop | `templates/sylvect-avatar.svg` |
| Threads | 320×320 | Circle crop | `templates/sylvect-avatar.svg` |
| X | 400×400 | Circle crop | `templates/sylvect-avatar.svg` |
| Facebook Page | 720×720+ | Circle crop | `templates/sylvect-avatar.svg` |
| LinkedIn company | 300×300 | Rounded square | `logos/png/sylvect-icon-dark@512.png` |
| YouTube | 800×800 | Circle crop | `templates/sylvect-avatar.svg` |

Keep the mark centered with ≥15% margin — circle crops eat corners.

## Feed posts

| Platform | Size | Start from |
|---|---|---|
| Instagram portrait | 1080×1350 (4:5) | `templates/sylvect-post-4x5.svg` |
| Instagram square | 1080×1080 | crop of the 4:5 template |
| Threads / X | 1200×675 or 1080×1350 | 4:5 template works on both |
| LinkedIn | 1200×627 (link) / 1080×1350 (image) | 4:5 template |
| Facebook | 1200×630 (link) / 1080×1350 (image) | 4:5 template |

## Stories / Reels / Shorts

| Platform | Size | Safe zone | Start from |
|---|---|---|---|
| IG/FB story | 1080×1920 (9:16) | Keep text inside 1080×1420 center | `templates/sylvect-story-9x16.svg` |
| Reels / Shorts cover | 1080×1920 | Center 1080×1080 is the feed crop | story template |

## Headers / banners

| Platform | Size | Safe zone | Start from |
|---|---|---|---|
| LinkedIn company banner | 1128×191 | Center 1128×191, mobile crops sides | `templates/sylvect-cover-banner.svg` (crop center) |
| X header | 1500×500 | Center 1260×330 safe | cover banner (crop center) |
| Facebook cover | 1640×924 (desktop) | Center 1640×664 safe | cover banner (crop center) |
| YouTube banner | 2560×1440 | **1546×423 center is TV/desktop safe** | cover banner (extend, don't stretch) |
| Substack publication | 600×120 logo / 1280×720 cover | — | horizontal transparent SVG |

**Rule for banners:** crop the 1920×640 master to the platform's aspect from the center. Never stretch it. For YouTube's 2560×1440, place the 1920×640 master on a 2560×1440 near-black canvas and extend the grid/glow — don't upscale past 1920 wide.

## Video

Lower-third bug: `logos/png/sylvect-icon-dark@256.png`, bottom-right, 80% opacity, 48–64 px tall. End card: stacked logo on near-black, 3 seconds.
