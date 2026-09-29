# Portfolio page: design spec

Target: https://lab.prfo.design/portfolio/ (relative asset paths only).
Copy: content.md, nothing else.
Language source: the SCENE & RAIL visual language (private design system) (chapters 01-13, _changelog-1.1, tokens.css, inspo/services/NOTES.md, inspo/picks/PICKS.md), Lev's own build rebuild-test/maisi (index-d.html, select.html, css/*), live https://lab.prfo.design/maisi/ (layer A, no variant D).

This file has no em dash, no en dash, no emoji. Builders keep it that way in every file they write.

---

## 0. The idea in one paragraph

The page is a dark layer A landing (the CMG / 26 MAISI landing: #161616, Nunito Sans 300, fixed glass header, warm #F7F6F3 inserts) that contains five layer C "app islands" (the FLAT.SHOW picker: white rail, grey scene, white glass controls in the corners, one dark-ink active segment). Each project is shown the way the picker shows a building: the screenshots are the scene, the facts sit in the white panel, the controls live in the corners, the centre stays free. The one filled button on the page is Telegram.

A judge must be able to put a screenshot of this page next to cmg-home-desktop.png and cmg-picker-floors-desktop.png and see the same hand.

---

## 1. Layer mapping, tokens, fonts

### 1.1 Which layer where

| Part of the page | Layer | Attribute | Why |
|---|---|---|---|
| `<html>`, header, intro, "What I do", stack, contacts, dialog backdrop | A landing-dark | `<html data-theme="landing-dark">` | R-PRINCIPLES-4: the landing sells the mood, dark, airy, weight 300 |
| Every project scene: screenshots, controls over them (segments, capsule, stepper, rail handle, fullscreen glyph) | C app | `data-theme="app"` on the scene element | R-PRINCIPLES-2, R-APP-2: everything over a scene is white glass |
| D1 only: the facts rail / panel next to the scene | C app | same `data-theme="app"` element as the scene | R-PRINCIPLES-22: the instrument panel never goes dark under a dark landing |
| D2 only: the number insert and facts under each scene | A, warm light surface `--bg-light` | inherits A | R-PRINCIPLES-16 rhythm, taste vault rule 11 (number is the hero) |
| Layer B (blue corporate) | not used | none | no chromatic brand, no photo mosaic |

The threshold between layers (R-PRINCIPLES-4) is the edge of the first project scene: dark shell above, white/grey app below.

Brand parameter for layer C: keep the tokens.css default `--brand: #162C25` (L* < 25, so `--fg-0 = --brand` by R-COLOR-4). It reads as near-black ink, which is what we want: one dark accent that means "active". Do not introduce any other brand color. Layer A brand stays monochrome `#E6E6E6` (R-PRINCIPLES-8).

The screenshots keep their own palettes (Clip Factory orange on black, Trade System black, MAISI CRM blue). R-COLOR-24: pre-rendered assets carry their own palette, the language never recolors them and never picks up their colors for UI.

### 1.2 Token subset (copy into assets/css/tokens.css verbatim)

Values are copied from tokens.css. Do not add colors, sizes or durations that are not here. Where tokens.css declares a property twice in `:root` (it does for `--size-sticky-cta-h` 73/60 and `--size-sticky-cta-btn-w` 166/136), the v1.1 value wins (R-LANDING-37); only the v1.1 value is listed. `rgb(from ...)` values are written as their literal fallbacks (R-COLOR-27).

```css
:root {
  /* breakpoints, reference only (media queries use literals) R-RESP-1 */
  --bp-sm: 600px; --bp-md: 960px; --bp-lg: 1200px; --bp-xl: 1920px;

  /* spacing R-LAYOUT-38 */
  --space-4: 4px; --space-5: 5px; --space-8: 8px; --space-10: 10px; --space-15: 15px;
  --space-16: 16px; --space-20: 20px; --space-24: 24px; --space-30: 30px; --space-32: 32px;
  --space-40: 40px; --space-48: 48px; --space-64: 64px; --space-100: 100px;

  /* radii R-SURFACE-2/3 */
  --radius-0: 0; --radius-xs: 3px; --radius-sm: 4px; --radius-md: 5px; --radius-image: 6px;
  --radius-lg: 8px; --radius-xl: 10px; --radius-track: 12px; --radius-capsule: 25px;
  --radius-arrow: 20%; --radius-circle: 50%;

  /* lines, blur, shadows R-SURFACE-4/8/13 */
  --border-w: 1px; --blur-glass: 8px; --blur-header: 10px;
  --shadow-none: none;
  --shadow-float: 0 0 3px #D2D2D2;
  --shadow-capsule: 0 0 10px rgba(128,128,128,.24);
  --shadow-header-landing: 0 6px 13px rgba(0,0,0,.19);
  --shadow-underline: inset 0 -1px 0 0 currentColor;

  /* motion R-MOTION-1/2 */
  --motion-duration-instant: 100ms; --motion-duration-fast: 150ms; --motion-duration-base: 200ms;
  --motion-duration-button: 250ms; --motion-duration-menu: 300ms; --motion-duration-panel: 500ms;
  --motion-duration-filter: 600ms;
  --motion-ease-standard: ease-in-out; --motion-ease-app: cubic-bezier(.4,0,.2,1);
  --motion-ease-panel: cubic-bezier(.25,.1,.25,1);
  --motion-scale-spinner-hover: 1.05;

  /* type families and weights R-TYPE-1/2 */
  --font-family-landing-dark: 'Nunito Sans', 'NunitoNew', Arial, sans-serif;
  --font-family-app: 'AppFont', 'DM Sans', 'Manrope', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
  --font-weight-light: 300; --font-weight-regular: 400; --font-weight-medium: 500;
  --font-weight-semibold: 600; --font-weight-bold: 700;
  --tracking-0: 0; --tracking-caption: .5px; --tracking-label: 1px; --tracking-nav-tight: -.7px;
  --text-button-size: 14px; --text-min-size: 11px;
  --text-measure-body: 670px; --text-measure-lead: 700px;

  /* controls R-CONTROL-1 */
  --size-control-icon: 40px; --size-control: 44px; --size-control-cta: 45px; --size-control-cta-lg: 48px;
  --size-control-field-landing: 50px; --size-control-cta-mobile: 66px; --size-touch-min: 40px;

  /* icons R-IMG-1/5 */
  --size-icon: 24px; --size-icon-control: 21px; --size-icon-action: 14px;
  --size-icon-spinner-hover: 30px;
  --icon-stroke: 1.4px; --icon-stroke-strong: 2px; --icon-linecap: round;

  /* app elements */
  --size-badge-h: 22px;
  --size-rotate-pill-w: 140px; --size-rotate-pill-h: 76px; --size-rotate-pill-pad: 16px; --size-rotate-btn: 44px;
  --size-collapse-handle-w: 24px;
  --size-stepper-w: 48px;
  --size-fullscreen-btn: 44px;

  /* landing elements */
  --size-hero-separator-w: 636px;
  --size-sticky-cta-h: 73px;          /* v1.1 R-LANDING-37 */

  /* layout R-LAYOUT-1..26 */
  --layout-container-max: 1200px; --layout-container-inset: 20px; --layout-container-content: 1160px;
  --layout-container-fluid-pad: 10px; --layout-gutter-desktop: 140px;
  --layout-gutter-mobile: 24px; --layout-gutter-mobile-app: 20px;
  --layout-header-h: 64px; --layout-header-btn-gap: 8px;
  --layout-kpi-gap: 45px;
  --layout-section-pad-top: 64px; --layout-section-pad-bottom: 58px;
  --layout-two-col-left-w: 545px; --layout-two-col-gap-min: 39px;
  --layout-rail-w: 460px; --layout-rail-pad: 30px; --layout-rail-content-w: 400px;
  --layout-header-h-app: 55px;
  --layout-scene-inset: 32px; --layout-scene-inset-left: 30px; --layout-scene-inset-mobile: 20px;
  --layout-table-row-h: 48px;
  --layout-segment-pad: 10px 16px; --layout-badge-pad: 2px 5px;
  --layout-filter-gap-x: 8px; --size-filter-field-w: 196px;

  /* z R-LAYOUT-37/41 */
  --z-scene: 0; --z-scene-controls: 1; --z-scene-controls-top: 6; --z-rail: 10;
  --z-rail-handle: 99; --z-header: 990; --z-modal: 100010;
}

[data-theme="landing-dark"] {
  color-scheme: dark;
  --bg-0: #161616; --bg-1: #0E0E0E; --bg-2: #1F1F1F; --bg-3: #222222;
  --bg-light: #F7F6F3;
  --fg-0: #FFFFFF; --fg-1: #E6E6E6; --fg-2: #BABABA; --fg-3: #868686;
  --fg-on-light-0: #222222; --fg-on-light-1: #2A2A2A;
  --line-1: rgba(255,255,255,.4);
  --line-on-light: rgba(0,0,0,.25);
  --line-on-light-hairline: #E9E9E9;
  --line-hairline-on-dark: rgba(255,255,255,.08);
  --line-hero-separator: rgba(255,255,255,.1);
  --brand: #E6E6E6; --brand-hover: #D0D0D0; --on-brand: #161616;
  --overlay-header: rgba(15,15,15,.95);
  --overlay-modal: rgba(0,0,0,.6);
  --overlay-ghost-hover: rgba(255,255,255,.1);
  --overlay-tap: rgba(255,255,255,.1);
  --btn-primary-bg: var(--brand); --btn-primary-bg-hover: var(--brand-hover); --btn-primary-fg: var(--on-brand);
  --btn-submit-bg: #FFFFFF;
  --btn-secondary-bg: #222222; --btn-secondary-bg-hover: #4C4C4C;
  --btn-ghost-border: var(--line-1); --btn-ghost-border-on-light: var(--line-on-light);
  --btn-ghost-hover-bg: var(--overlay-ghost-hover); --btn-ghost-hover-border: #FFFFFF;
  --btn-ghost-hover-invert-bg: #222222;
  --btn-radius-header: var(--radius-xs);
  --focus-ring: #2015FF; --focus-ring-offset: 4px;
  --font-family-display: var(--font-family-landing-dark);
  --font-family-body: var(--font-family-landing-dark);
  --font-family-nav: 'NunitoSans', var(--font-family-landing-dark);
  --motion-duration-hover: var(--motion-duration-base);
  --motion-ease-hover: var(--motion-ease-standard);

  --text-display: 300 55px/69px var(--font-family-display);
  --text-display-mobile: 300 36px/45px var(--font-family-display);
  --text-h2: 300 42px/65px var(--font-family-display);
  --text-h2-mobile: 300 26px/40px var(--font-family-display);
  --text-lead: 300 22px/28px var(--font-family-body);
  --text-lead-mobile: 300 16px/20px var(--font-family-body);
  --text-lead-2: 300 16px/20px var(--font-family-body);
  --text-body: 300 16px/25px var(--font-family-body);
  --text-body-mobile: 300 14px/22px var(--font-family-body);
  --text-body-sm: 300 14px/22px var(--font-family-body);
  --text-caption: 300 12px/19px var(--font-family-body);
  --text-label: 300 11px/14px var(--font-family-body);
  --text-kpi: 600 20px/25px var(--font-family-body);
  --text-kpi-mobile: 600 18px/normal var(--font-family-body);
  --text-stat: 700 52px/81px var(--font-family-display);
  --text-stat-mobile: 700 32px/50px var(--font-family-display);
  --text-card-index: 300 11px/17px var(--font-family-body);
  --text-button: 400 14px/21.7px var(--font-family-body);
  --text-nav: 400 13px/normal var(--font-family-nav);
  --text-nav-drawer: 700 16px/normal var(--font-family-nav);
  --text-footer: 300 13px/20px var(--font-family-body);
}

[data-theme="app"] {
  color-scheme: light;
  --bg-0: #FFFFFF; --bg-1: #F5F5F5; --bg-2: #F6F7F6;
  --bg-stepper-cell: #EEEEEE; --bg-stepper-arrow: #ECEBEB;
  --fg-0: #162C25; --fg-2: #757575; --fg-3: #797979;
  --line-1: rgba(34,36,38,.15); --line-2: #D6D2D2; --line-3: #E0E0E0; --line-row: #E5E5E5;
  --line-stepper: #EEEEEE;
  --brand: #162C25;
  --brand-90: rgba(22,44,37,.9);        /* = rgb(from var(--brand) r g b / .9) */
  --brand-tint-4: rgba(22,44,37,.04);   /* = rgb(from var(--brand) r g b / .04) */
  --on-brand: #FFFFFF;
  --badge-type-bg: #4286A0; --badge-id-bg: var(--brand); --badge-fg: var(--on-brand);
  --overlay-glass-90: rgba(255,255,255,.9); --overlay-glass-80: rgba(255,255,255,.8);
  --overlay-glass-60: rgba(255,255,255,.6); --overlay-glass-30: rgba(255,255,255,.3);
  --overlay-tap: transparent;
  --btn-outlined-border: var(--line-1); --btn-outlined-active-bg: var(--brand-tint-4);
  --btn-float-bg: var(--overlay-glass-80); --btn-float-bg-hover: #FFFFFF;
  --btn-float-disabled-bg: var(--overlay-glass-60); --btn-float-disabled-fg: #999999;
  --segment-active-bg: var(--brand-90); --segment-active-fg: var(--on-brand);
  --segment-idle-bg: var(--overlay-glass-90); --segment-idle-fg: var(--brand);
  --stepper-active-bg: var(--brand); --stepper-active-fg: var(--on-brand);
  --stepper-idle-bg: var(--bg-stepper-cell);
  --icon-fg: var(--brand);
  --focus-ring: var(--brand);
  --scrollbar-thumb: rgba(0,0,0,.25);
  --btn-radius: var(--radius-xl);
  --font-family-display: var(--font-family-app);
  --font-family-body: var(--font-family-app);
  --motion-duration-hover: var(--motion-duration-button);
  --motion-ease-hover: var(--motion-ease-app);

  --text-h1: 700 26px/32px var(--font-family-display);
  --text-h3: 600 20px/28px var(--font-family-display);
  --text-body: 400 16px/24px var(--font-family-body);
  --text-body-sm: 400 14px/18px var(--font-family-body);
  --text-caption: 400 12px/18px var(--font-family-body);
  --text-control: 400 14px/21px var(--font-family-body);
  --text-badge: 400 12px/18px var(--font-family-body);
  --text-button: 500 14px/24.5px var(--font-family-body);
}

@media (prefers-reduced-motion: reduce) {
  :root {
    --motion-duration-panel: 250ms;
    --motion-duration-filter: 250ms;
  }
}
```

`html { font-size: 16px }` (A root). Inside `[data-theme="app"]` set `font-size: 14px` on the element (R-TYPE, 2.1 note) and never use rem inside it.

### 1.3 Fonts (self-hosted woff2, no runtime requests)

All four families on Google Fonts are variable: one woff2 per subset covers every weight. Download once with a desktop Chrome User-Agent:

```sh
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
curl -s -A "$UA" "https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300..700&display=swap"   # take the /* latin */ and /* cyrillic */ src urls
curl -s -A "$UA" "https://fonts.googleapis.com/css2?family=DM+Sans:wght@400..700&display=swap"        # /* latin */ only (DM Sans has no Cyrillic)
curl -s -A "$UA" "https://fonts.googleapis.com/css2?family=Manrope:wght@400..700&display=swap"        # /* cyrillic */ only
```

| File in assets/fonts/ | Family / subset | Weights used | Layer |
|---|---|---|---|
| nunito-sans-latin.woff2 | Nunito Sans, latin (U+0000-00FF and the rest of Google's latin range) | 300, 400, 600, 700 | A |
| nunito-sans-cyrillic.woff2 | Nunito Sans, cyrillic (U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116) | 300, 400, 600, 700 | A |
| dm-sans-latin.woff2 | DM Sans, latin | 400, 500, 600, 700 | C, all Latin letters and every digit |
| manrope-cyrillic.woff2 | Manrope, cyrillic | 400, 500, 600, 700 | C, Cyrillic letters |

The only non-ASCII, non-Cyrillic character in content.md is U+00B2 (m², м²); it is inside both latin subsets.

```css
@font-face { font-family: 'Nunito Sans'; src: url(../fonts/nunito-sans-latin.woff2) format('woff2');
  font-weight: 300 700; font-style: normal; font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }
@font-face { font-family: 'Nunito Sans'; src: url(../fonts/nunito-sans-cyrillic.woff2) format('woff2');
  font-weight: 300 700; font-style: normal; font-display: swap;
  unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116; }
/* AppFont = DM Sans for Latin and digits, Manrope for Cyrillic (R-TYPE-2, chapter 02 section 2.1) */
@font-face { font-family: 'AppFont'; src: url(../fonts/dm-sans-latin.woff2) format('woff2');
  font-weight: 400 700; font-display: swap; unicode-range: U+00??, U+0100-024F, U+1E??; }
@font-face { font-family: 'AppFont'; src: url(../fonts/manrope-cyrillic.woff2) format('woff2');
  font-weight: 400 700; font-display: swap; unicode-range: U+04??, U+0500-052F, U+2DE0-2DFF, U+A640-A69F; }
```

Copy the exact unicode-range lines Google returns for the latin block (the list above is what it returns today). Preload only `nunito-sans-latin.woff2` (`<link rel="preload" as="font" type="font/woff2" crossorigin>`). No Instrument Serif, no Georgia wordmarks: Lev's variant D serif and the 26 MAISI logo belong to that client, not to this page.

---

## 2. Shell: grid, spacing, header, language switch, CTA, footer

### 2.1 Grid and gutters

| Width | Container | Side gutter | Rule |
|---|---|---|---|
| >= 1220 | 1200 centred, inner inset 20, content 1160 | (100% - 1200) / 2 + 20, so x = 140 at 1440 and x = 380 at 1920 | R-LAYOUT-1, R-LAYOUT-2 |
| 960 - 1219 | fluid, `padding: 0 var(--layout-container-fluid-pad)` plus inset 20 | 30 | R-LAYOUT-2 |
| 600 - 959 | fluid, content max `--text-measure-body` 670 for text blocks | 24 | R-RESP-1 (tablet = mobile layout, wider) |
| < 600 | one column | `--layout-gutter-mobile` 24 (A), `--layout-gutter-mobile-app` 20 (inside C panels) | R-LAYOUT-3, R-LAYOUT-26 |

Media queries use literals only: `(min-width: 600px)`, `(min-width: 960px)`, `(min-width: 1200px)`, `(min-width: 1920px)`. No other breakpoints (R-RESP-35).

Full-bleed elements use `width: 100%` of `<body>`, never `100vw` (100vw includes the scrollbar and creates horizontal scroll on Windows). Heights derived from width use `aspect-ratio`, not `vw`.

Vertical rhythm: sections start content after `--layout-section-pad-top` 64 and end with `--layout-section-pad-bottom` 58 (R-LAYOUT-6). Height is content driven, never "one screen".

### 2.2 Header (fixed, R-LANDING-1)

```
1440 x 64, fixed, z 990
x140 [Lev Skorokhodov]                                         [EN|RU]  8  [Telegram]   right edge x1300
```

| Element | Spec |
|---|---|
| Bar | `position: fixed; top: 0; left: 0; right: 0; height: var(--layout-header-h)` 64; `z-index: var(--z-header)`; `background: var(--overlay-header)`; `backdrop-filter: blur(var(--blur-header))` (plus `-webkit-`); `box-shadow: var(--shadow-header-landing)`; bottom hairline `border-bottom: 1px solid var(--line-hairline-on-dark)`. Inner row is the page container, `display: flex; align-items: center; justify-content: space-between`. |
| Name (wordmark) | `<a href="#top">` with the content "Name" string; `font: var(--text-nav-drawer)` (700 16) `letter-spacing: var(--tracking-nav-tight)` (the one place negative tracking is allowed, R-TYPE-21); color `--fg-0`; hover `--fg-3` over 200ms. Height 44 hit area (`display: inline-flex; align-items: center; min-height: 44px`). |
| Right cluster | language segment + Telegram, `gap: var(--layout-header-btn-gap)` 8. Order: language, then CTA (R-LANDING-2). No nav links: content.md has no section names in both languages. |
| Control height | 44 (`--size-control`), not the reference 38: hard rule tap target >= 44. Recorded as deviation D-2. |
| Mobile < 600 | same 64 bar (R-LANDING-35: no Tilda scaling artefacts), gutter 24; name left, language segment right; Telegram leaves the header and goes to the bottom bar (2.5). |

### 2.3 Language switch as a segment control

Two languages only, so both codes are visible as a segment (deviation D-3 from R-LANDING-4 / R-CONTENT-3 dropdown; with two items a dropdown hides one tap behind another). No flags (imagery rule: no decorative images, R-IMG-3).

| Part | Spec |
|---|---|
| Container | `<div role="group" aria-label="EN / RU">`; `display: inline-flex; height: 44px; background: var(--btn-secondary-bg)` #222222; `border-radius: var(--btn-radius-header)` 3; `overflow: hidden` (R-SURFACE-16: one radius on the container, segments have none) |
| Segment | `<button type="button" lang="en">EN</button>`, `<button lang="ru">RU</button>`; `min-width: 44px; padding: 0 12px; font: var(--text-nav)` 13px; `letter-spacing: var(--tracking-label)` 1px (caps rule R-TYPE-20) |
| Idle | color `--fg-3` #868686, weight 400 |
| Active | color `--fg-0`, weight 700, `aria-pressed="true"`; the code gets `box-shadow: var(--shadow-underline)` on an inner `<span>` (the only inset shadow the language allows, R-SURFACE-21). No fill: the one light fill on the bar belongs to Telegram (R-PRINCIPLES-10). |
| Hover (idle) | color `--fg-1` over `--motion-duration-hover` 200ms `--motion-ease-standard`, inside `@media (hover:hover) and (pointer:fine)` |
| Behaviour | click sets `?lang=` via `history.replaceState`, stores `localStorage.lang` (wrapped in try/catch), swaps all strings, `alt`s, `<html lang>`, `<title>`, meta description. Load order: `?lang=` beats `localStorage` beats default `en`. An inline script in `<head>` sets `document.documentElement.lang` before first paint (R-UX-42: one dictionary in js/i18n.js, keys shared by EN and RU). |

### 2.4 Contact action: the single filled CTA (R-PRINCIPLES-5, R-PRINCIPLES-10)

Telegram is the only filled control on the page. Everything else is outline, glass or text.

| State | Spec (desktop header, >= 600) |
|---|---|
| Default | `<a href="https://t.me/prfowax" target="_blank" rel="noopener">Telegram</a>`; `height: 44px; padding: 0 20px; display: inline-flex; align-items: center`; `background: var(--btn-primary-bg)` #E6E6E6; `color: var(--btn-primary-fg)` #161616; `font: var(--text-button)` 400 14; `border-radius: var(--btn-radius-header)` 3; no shadow (A buttons have none, R-CONTROL-2) |
| Hover | background `--btn-primary-bg-hover` #D0D0D0, 200ms ease-in-out, size unchanged (R-MOTION-4) |
| Focus | see 4.5 |

Every other Telegram link on the page (contacts block) is a ghost button, so a viewport never holds two filled buttons.

### 2.5 Mobile bottom bar (< 600, R-LANDING-30, R-LANDING-37)

`position: fixed; left: 0; right: 0; bottom: 0; height: calc(var(--size-sticky-cta-h) + env(safe-area-inset-bottom))` (73 + safe area); `background: var(--bg-3)` #222222; `backdrop-filter: blur(var(--blur-glass))`; `padding: 11px var(--layout-gutter-mobile) calc(11px + env(safe-area-inset-bottom))`; `z-index: var(--z-header)`. One button, full width, height 51 (42 x 1.21875, R-LANDING-37), `background: var(--btn-submit-bg)` #FFFFFF, `color: var(--on-brand)` #161616, `font: var(--text-button)` 14, radius 0, label "Telegram". `body { padding-bottom: calc(var(--size-sticky-cta-h) + env(safe-area-inset-bottom)) }` below 600. The header Telegram button is `display: none` below 600.

### 2.6 Intro block (hero replacement, both directions)

Deviation D-1: no 100vh photo hero (R-LANDING-8). There is no photograph of Lev and the only allowed images are project screenshots; a screenshot under a dark veil would be a fake hero. Instead the intro is content height and the first project scene must start inside the first viewport: at 1440 x 900 its top edge is at y <= 620; at 390 x 844 the Telegram bar is visible on load.

Layer A, `background: var(--bg-0)`, container, `padding: calc(var(--layout-header-h) + var(--space-100)) 0 var(--layout-section-pad-bottom)` desktop; `calc(64px + 40px) 0 40px` below 600.

Stack (R-LANDING-9 order, shortened):

| # | Content key | Spec |
|---|---|---|
| 1 | Header.Role ("AI engineer" / "AI-инженер") | `<p>` `font: var(--text-label)` 300 11/14, `text-transform: uppercase`, `letter-spacing: var(--tracking-label)`, color `--fg-2`. Caps is 1 to 2 words, within R-TYPE-20. |
| 2 | Header.Name | `<h1>` `font: var(--text-display)` 300 55/69, `letter-spacing: 0`, color `--fg-0`, margin-top 16. Mobile `--text-display-mobile` 36/45. The only element above 40px in the viewport (R-TYPE-3). |
| 3 | Header.Line | `<p>` `font: var(--text-lead)` 300 22/28, max-width `--text-measure-lead` 700, color `--fg-0`, margin-top 24. Mobile `--text-lead-mobile` 16/20. |
| 4 | hairline | `width: min(100%, var(--size-hero-separator-w))` 636; 1px `--line-hero-separator`; margin 42 0 24 (mobile 32 0 24) |
| 5 | What I do (3 items) | `<ul>` grid, 3 columns on >= 960 with `column-gap: var(--layout-kpi-gap)` 45 (3 x 356 in 1160), 1 column below 960 with `row-gap: 24`. Each `<li>`: the text before the first ". " (kept with its period) in `<strong>` `font: var(--text-kpi)` 600 20/25 color `--fg-0` (mobile `--text-kpi-mobile` 18); the rest in `<span>` on its own line, `font: var(--text-body-sm)` 300 14/22, `letter-spacing: var(--tracking-caption)`, color `--fg-2`, margin-top 8. Numbers inside ("7") stay in the span, weight 600 via `<b>` (R-PRINCIPLES-15: numbers by weight, not color). |

No hero CTA pill: the header already carries Telegram; a second Telegram in the same viewport is noise.

### 2.7 Stack and contacts (end of page = footer)

Stack block: layer A `--bg-0` section, container, padding 64 / 58. One `<p>` with the verbatim list, `font: var(--text-body)` 300 16/25, color `--fg-2`, max-width `--text-measure-body` 670. No heading (content has no RU heading for it; an EN-only heading would mix languages, R-CONTENT-20).

Contacts block acts as the footer (R-PRINCIPLES-16: the page ends on the darkest surface): `<footer>` on `--bg-1` #0E0E0E, container, padding 64 / 58 (+73 bottom bar space below 600).

| Order | Content | Spec |
|---|---|---|
| 1 | Contacts.Line | `<h2>` `font: var(--text-h2)` 300 42/65, color `--fg-0`, max 700; mobile `--text-h2-mobile` 26/40 |
| 2 | Telegram @prfowax, GitHub | two ghost links in a row, gap 14 (R-LAYOUT-10); each `height: var(--size-control-field-landing)` 50, `padding: 0 24px`, `border: 1px solid var(--btn-ghost-border)`, radius 0, `font: var(--text-button)`, color `--fg-0`; hover `background: var(--btn-ghost-hover-bg)` + `border-color: var(--btn-ghost-hover-border)` 200ms (R-LANDING-21). Below 600: stacked, full width, height `--size-control-cta-mobile` 66 (R-RESP-22). Labels: "Telegram @prfowax" and "GitHub" exactly as content (RU: "Telegram @prfowax", "GitHub"). |

Nothing else in the footer: no copyright line, no repeated name, no "made with".

---

## 3. The project block: screenshots are the scene

### 3.1 Principles for both directions

1. The scene is the screenshot (R-PRINCIPLES-1). It is never shrunk into a card, never given a device frame, border or drop shadow (R-PRINCIPLES-19: the scene is full size and frameless).
2. Controls live in the scene corners; the centre stays empty (R-PRINCIPLES-3, R-APP-39): mode switch top right at inset 32/32 (20 below 960), capsule bottom centre, stepper right edge centre (D1), rail handle left edge centre (D1). Top left stays empty (allowed by R-IMG-34).
3. Everything over the scene is white glass: `--overlay-glass-90` panels, `--overlay-glass-80` buttons, `--overlay-glass-30` capsule, shadow `--shadow-float` / `--shadow-capsule`, no backdrop blur over the scene (R-SURFACE-9, R-APP-2). The only dark-ink fill over a scene is the active segment `--segment-active-bg` rgba(22,44,37,.9) (R-PRINCIPLES-5, R-APP-16).
4. Facts are text, numbers are weight: every number token inside a fact (digits with their unit or suffix: "25", "0.05 m²", "$0.16", "39k", "1.9k", "2 hours 40 minutes" is split as "2" and "40") is wrapped in `<b>` weight 700 in C, 600 in A (R-PRINCIPLES-15, R-TYPE-4). The sentence text is not changed.
5. Labels from content.md structure (Kind, Result, Facts, Data, Stack, Links) are keys, not copy: they are never printed. Hierarchy comes from size, weight and grey (NOTES rule 3).
6. "[PENDING]" tokens are not printed. The element that carried one gets `data-pending="true"` so the markup still records it. (Open question for Lev: see section 7.)

### 3.2 Screenshot sets (read each index.json again before building; matscout had no folder at spec time)

Desktop set is used at >= 600. Mobile set is used below 600 when it exists; otherwise the desktop set is used in the landscape mobile scene (3.5). Order in the table is the segment order.

| Project | Desktop set (shots/...) | Mobile set | Avoid (from quality_notes) |
|---|---|---|---|
| 01 matscout | from shots/matscout/index.json when it appears: up to 4, prefer entries whose quality_notes say best / hero; poll every 60 s up to 15 min, then use whatever PNG/WebP exists | its 390x844 captures if any | any shot with visible secrets or local URLs |
| 02 Floor plan pipeline | floorplans/plan-studio-floor-10-raw-layers, floorplans/plan-studio-floor-10-house-style, floorplans/floor-10-vector, floorplans/floor-10-picker-desktop (before, rules, output, live) | none (landscape scene) | floor-02/22/26 (weight budget) |
| 03 Content Factory | factory/desktop-02-scenes, factory/desktop-05-style-cinema, factory/desktop-07-polish, factory/desktop-09-trim | factory/mobile-02-scenes, factory/mobile-05-style-cinema, factory/mobile-07-polish | the *-full.png captures, desktop-01-source (Russian-only helper line, "Local" chip) |
| 04 Trade System | trade/desktop-01-sales, trade/desktop-02-ai-inbox, trade/desktop-07-settlements-suppliers, trade/desktop-09-purchases | trade/mobile-04-settlements-suppliers, trade/mobile-02-sales | desktop-04 (possible real client name), desktop-05/06 (broken data), mobile-01/03 (layout bugs) |
| 05 26 MAISI | maisi/picker-3d-desktop, maisi/picker-floorplan-status-desktop, maisi/unit-detail-desktop, maisi-crm/crm-agent-cabinet-dashboard | maisi/picker-3d-mobile-selected, maisi/unit-detail-mobile | landing-hero-* (headline baked into the bitmap, R-IMG-23), landing-layouts (same render three times), *-ru variants |

A project with one image renders no mode switch and no capsule. A project with zero images (only possible for matscout if its shots never arrive) renders the facts panel full width and no scene; no placeholder, no "coming soon".

### 3.3 Image pipeline and weight

| Item | Spec |
|---|---|
| Tool | `cwebp -q 80 -m 6 -resize W 0 in.png -o out.webp` (only downscale; never upscale a 1x source such as the CRM jpg at 1528 px) |
| Variants | desktop captures: `<name>-2400.webp` (2400 w) and `<name>-1200.webp` (1200 w); mobile captures (1170 x 2532): `<name>-m.webp` at native 1170 w |
| Paths | `assets/img/<project>/<name>-2400.webp` etc., relative |
| Markup | `<img src="...-1200.webp" srcset="...-1200.webp 1200w, ...-2400.webp 2400w" sizes="(min-width:1200px) calc(100vw - 460px), 100vw" width="2400" height="1500" alt="..." loading="lazy" decoding="async">`; width/height are the real pixel size of the 2400 variant (16:10 captures give 2400 x 1500; floor-10-vector gives 2400 x 1594). Only the first image of project 01 is `loading="eager" fetchpriority="high"` when it is above the fold. |
| Inactive segments | not in the DOM `src` until first activation (store URLs in `data-src`/`data-srcset`); on desktop, prefetch the next image on `pointerenter` of the mode switch |
| Budget | first full scroll (all first images, fonts, css, js) under 4 MB at 1440 and at 390. Expected: 5 first images x 150-350 KB + 4 fonts about 150 KB + css/js under 60 KB. The builder measures with Playwright (sum of `transferSize` after scrolling to the bottom) and reports the number. |
| Alt text | built from content strings only: `<Project heading without number>: <Kind>, <n>/<N>` in the current language, for example "matscout: MCP server and research agent, 1/4", RU "matscout: MCP-сервер и исследовательский агент, 1/4". Updated on language switch. |

### 3.4 Mode switch (top right, R-APP-16, R-CONTROL-16)

| Part | Spec |
|---|---|
| Position | `position: absolute; top: var(--layout-scene-inset); right: var(--layout-scene-inset)` 32/32 (>= 960), 20/20 at 600-959; `z-index: var(--z-scene-controls-top)`. Hidden below 600 (R-RESP-7: one switcher per screen; the capsule takes over). |
| Container | `<div role="radiogroup" aria-label="<project heading>">`; `display: inline-flex; height: var(--size-control)` 44; `border-radius: var(--radius-md)` 5; `overflow: hidden`; `box-shadow: var(--shadow-float)`; background `--segment-idle-bg` |
| Segment | `<button type="button" role="radio">` buttons in the `role="radiogroup"`, `aria-checked`, roving tabindex (checked segment `tabindex="0"`, others `-1`); labels taken from the content.md "Scene modes" block (visible mode names, never digits, never invented; the build checks every label against content.md); `min-width: 44px; padding: var(--layout-segment-pad)` 10 16; `font: var(--text-control)` 14/21; idle color `--segment-idle-fg` (brand), weight 400 |
| Active | `background: var(--segment-active-bg)`; color `--segment-active-fg`; weight 700 |
| Hover (idle) | `background: var(--btn-float-bg-hover)` #FFFFFF, 250ms `--motion-ease-app`, inside hover guard; no scale, no size change |
| Keyboard | Tab reaches the checked segment; Left/Right and Up/Down arrows move between segments and activate, Home/End jump to the first/last (roving tabindex) |

### 3.5 Mobile behaviour of a scene (< 600, chapter 11)

Two scene shapes, chosen per project, never mixed inside one project so the height never jumps while switching (R-PRINCIPLES-13):

| Shape | When | Spec |
|---|---|---|
| Portrait scene | project has a mobile set | full width, `height: min(calc(100svh - 64px - 73px), 700px)`; `object-fit: cover; object-position: 50% 0` (anchor top, R-IMG-36: cut only the bottom); background `--bg-1` |
| Landscape scene | no mobile set | full width, `aspect-ratio: 16 / 10` (floor-10-vector: `object-fit: contain` on `--bg-1`), whole image visible, no crop |

Controls on both shapes:
- Capsule (R-APP-17, R-CONTROL-7), bottom centre: `bottom: var(--layout-scene-inset-mobile)` 20; `width: var(--size-rotate-pill-w)` 140, `height: var(--size-rotate-pill-h)` 76, `padding: var(--size-rotate-pill-pad)` 16, `background: var(--overlay-glass-30)`, `border-radius: var(--radius-capsule)` 25, `box-shadow: var(--shadow-capsule)`; two buttons `--size-rotate-btn` 44 x 44, `border-radius: var(--radius-arrow)`, `background: var(--btn-float-bg)`, chevron glyph 24 stroke 1.4 color `--brand`. The first/last image wraps around (spinner behaviour, R-IMG-34). Deviation D-5: kept at desktop size, not 116 x 56 with 40 px buttons (R-RESP-16), because of the 44 px tap rule. Landscape scene at 390 is 244 px tall: capsule 76 fits with 20 inset.
- Detail view: the whole scene image is a `<button>` whose accessible name is the image alt. Tap opens a `<dialog>` (z `--z-modal`, backdrop `--overlay-modal` rgba(0,0,0,.6)) with the same image at the 2400 variant, `height: 100%` of the dialog and natural width, inside `overflow: auto` so the user pans horizontally; close button top right 44 x 44 on `--overlay-glass-80` with an X glyph 21; Esc and backdrop click close; focus returns to the scene button. On >= 960 in D1 a corner glyph (fullscreen, 24, stroke 1.4) sits bottom right at inset 32/30 inside a 44 x 44 `--overlay-glass-80` square radius `--radius-lg` 8 (R-IMG-21 fullscreen button) and opens the same dialog.

Page-level horizontal scroll must stay at zero; only the dialog pans.

### 3.6 Scene image switching

Stacked `<img>` in one box, `position: absolute; inset: 0`. The incoming image is decoded (`img.decode()`) before it fades in; `opacity 0 -> 1` over `--motion-duration-filter` 600 ms `--motion-ease-app` (R-APP-36: a frame change is the only slow motion in the app), the outgoing one fades out after. Box size never changes.

---

## 4. Motion (chapter 10) and imagery (chapter 09)

### 4.1 Motion that applies

| What | Duration / curve | Rule |
|---|---|---|
| A hovers (links, ghost buttons, Telegram, language) | color / background / border, 200 ms `ease-in-out` | R-MOTION-4, R-LANDING-32 |
| C hovers (segments, outlined links, capsule buttons, stepper cells) | 250 ms `cubic-bezier(.4,0,.2,1)` | R-COLOR-18, R-APP-36 |
| Capsule button hover | background to #FFFFFF, `scale(var(--motion-scale-spinner-hover))` 1.05, glyph 24 to `--size-icon-spinner-hover`: use 26 to 30 only if the glyph is drawn at 26; otherwise keep 24 and skip the glyph growth | R-MOTION-10 |
| Scene image change | opacity 600 ms `--motion-ease-app` | R-APP-36 |
| D1 rail collapse | rail width 460 to 0, 500 ms `--motion-ease-app` | R-APP-36 panel |
| Dialog open / close | opacity 300 ms `ease-in-out` | R-MOTION-18 (A overlay) |
| Stepper jump to project | `scrollIntoView({behavior: 'smooth'})`, `'auto'` under reduced motion | R-MOTION-34 |

Forbidden: scroll-reveal / appear animations (R-MOTION-23; the optional 2 s H1 appear is also skipped, readers have 60 seconds), parallax, Ken Burns, count-up numbers (6.3 note), loops or pulsing dots (R-MOTION-24), bounce or back easing (R-MOTION-2), any hover that moves or resizes neighbours (R-PRINCIPLES-13), slide or scale entrances of popovers (R-MOTION-13).

Hover effects that scale live inside `@media (hover:hover) and (pointer:fine)`; touch gets `-webkit-tap-highlight-color: var(--overlay-tap)` (A rgba(255,255,255,.1), C transparent) (R-MOTION-29, R-RESP-19). `cursor: pointer` on everything clickable (R-MOTION-28).

`prefers-reduced-motion: reduce`: the tokens block shortens panel and filter to 250 ms; in addition set `scroll-behavior: auto`, dialog transition 0, capsule scale off.

### 4.2 Focus (R-MOTION-30)

`outline: none` without replacement is forbidden. Deviation D-7: the A token `--focus-ring` #2015FF has about 2:1 contrast on #161616, below the 3:1 needed for a visible focus indicator. On A dark surfaces use `outline: 2px solid var(--fg-0); outline-offset: var(--focus-ring-offset)` (4). On `--bg-light` inserts and inside `[data-theme="app"]` use `outline: 2px solid var(--focus-ring)` (brand #162C25) with offset 2. Use `:focus-visible`.

### 4.3 Imagery that applies

| Rule | Application |
|---|---|
| R-IMG-1, R-IMG-2, R-IMG-5 | All icons inline SVG on a 24 grid, `fill: none; stroke: currentColor; stroke-width: 1.4; stroke-linecap: round; stroke-linejoin: round`; sizes only 24 / 21 / 14. Rail handle chevron stroke 2 (`--icon-stroke-strong`). |
| R-IMG-3 | One glyph family. Glyphs needed and their paths: chevron left `M15 6l-6 6 6 6`, chevron right `M9 6l6 6-6 6`, chevron up `M6 15l6-6 6 6`, chevron down `M6 9l6 6 6-6`, fullscreen `M4 9V4h5M15 4h5v5M20 15v5h-5M9 20H4v-5`, close `M6 6l12 12M18 6L6 18`. No arrow characters in text, no link-out glyphs. |
| R-PRINCIPLES-19, R-IMG-21 | Scene frameless; the detail dialog is the "gallery in a frame". |
| R-IMG-23 | No text baked into images we produce. The screenshots themselves show product UI text; that is the product, not decoration. MAISI landing hero captures with a headline in the bitmap are excluded. |
| R-IMG-24, R-IMG-36 | Mobile uses cover with top anchor for portrait captures; nothing is cropped at the top. |
| R-IMG-25 | Raster served at the box size (2400 / 1200 / 1170 variants), icons only SVG. |
| R-COLOR-24 | Screenshots keep their palettes; UI next to them stays neutral. |
| R-IMG-22, R-IMG-27 | No stock, no reference renders or CMG / Piazza / Rybalsky material, no 26 MAISI logo outside the MAISI screenshots. |
| R-IMG-8 | No zoom-on-hover on scenes (app rule: images do not zoom; a frame is not a link to elsewhere). |

---

## 5. Two structural directions

Both share sections 1 to 4: header, intro, stack, contacts, tokens, fonts, image sets, mode switch, mobile scene, dialog, motion. They differ in how a project is laid out.

### D1 "Scene and rail": the page reads as one product

Page order: header, intro (A), app region with the five projects stacked (C), stack (A `--bg-0`), contacts footer (A `--bg-1`).

The app region is one continuous surface: white rail column on the left, grey scene column on the right, five times. From the first project to the last it looks like the picker scrolled through five buildings.

#### D1.1 Project block, >= 1200

```
+--------- rail 460 (#FFF, pad 30, shadow-float) ---------+----------------- scene (#F5F5F5) ------------------------+
| [01][MCP server and research agent]         h 55 row   |                                     [1|2|3|4]  top32 r32 |
| matscout                                   26/32 700   |                                                          |
| Turns a plain question about materials ... 16/24       |    +------------------------------------------+   [^]    |
| -------------------------------------------- line-row  |    |                                          |   [01]   |
| 25 tools behind one MCP server. ...        14/18       |    |          screenshot, contain            |   [02]   |
| --------------------------------------------            |    |                                          |   [03]  r20
| Two phase agent: discovery on 11 tools ...             |    |                                          |   [04]   |
| ...                                                    |    +------------------------------------------+   [05]   |
| Materials Project, OPTIMADE federation ... 12/18 grey  |                                                    [v]    |
| Python, FastMCP, OpenAI Responses API ...  12/18 grey  |                                                          |
| [ Live            ] [ MCP endpoint     ]  outlined 44  |[<] handle                                        [ fs ]  |
+--------------------------------------------------------+----------------------------------------------------------+
```

| Element | Spec |
|---|---|
| Block | `<section class="project" data-theme="app" id="p-01" aria-labelledby="p-01-title">`; `display: grid; grid-template-columns: var(--layout-rail-w) 1fr; min-height: clamp(640px, calc(100svh - 64px), 900px)`; height grows with the rail if the rail is taller (no inner rail scroll on a page). Blocks touch; from the second block on, the rail gets `border-top: 1px solid var(--line-3)`. |
| Rail | `background: var(--bg-0)`; `padding: var(--layout-rail-pad)` 30; `box-shadow: var(--shadow-float)`; `position: relative; z-index: var(--z-rail)`; content width 400 |
| Rail head | `min-height: var(--layout-header-h-app)` 55, `display: flex; flex-wrap: wrap; align-items: center; gap: var(--space-5)`: id badge (project number "01" from the heading) on `--badge-id-bg`, then type badge (Kind) on `--badge-type-bg` #4286A0 (R-APP-12 order: what, which). Both: `font: var(--text-badge)` 12/18, color `--badge-fg`, `min-height: var(--size-badge-h)` 22, `padding: var(--layout-badge-pad)` 2 5, `border-radius: var(--radius-xs)` 3; long Kind wraps inside its badge. |
| Title | `<h2 id="p-01-title">` the heading without its number ("matscout", "Floor plan pipeline", "Content Factory", "Trade System", "26 MAISI"); `font: var(--text-h1)` 700 26/32; color `--fg-0`; margin-top 8 |
| Result | `<p>` `font: var(--text-body)` 400 16/24, color `--fg-0`, margin 12 0 20 |
| Facts | `<ul>`; `border-top: 1px solid var(--line-row)`; each `<li>`: `min-height: var(--layout-table-row-h)` 48, `padding: 15px 0`, `border-bottom: 1px solid var(--line-row)`, `font: var(--text-body-sm)` 400 14/18, color `--fg-0`; numbers `<b>` 700 (R-APP-28 table rhythm, R-PRINCIPLES-15) |
| Data (01 only) | `<p>` `font: var(--text-caption)` 12/18, color `--fg-2`, margin-top 16 |
| Stack | `<p>` same style, margin-top 8 (16 when there is no Data line). RU "Stack: same as EN." renders the EN list. |
| Links | `margin-top: 24px; display: grid; grid-template-columns: repeat(2, var(--size-filter-field-w)); gap: var(--layout-filter-gap-x)` (the filter grid, R-LAYOUT-15); a link whose label is wider than 164 px spans both columns. Each is an outlined button (R-APP-29): `height: var(--size-control)` 44, `padding: 0 16px`, `border: 1px solid var(--btn-outlined-border)`, `border-radius: var(--btn-radius)` 10, `font: var(--text-button)` 500 14, sentence case (uppercase belongs to primary only, R-TYPE-11), color `--brand`, `target="_blank" rel="noopener"`; hover `background: var(--btn-outlined-active-bg)` 250 ms. Items without a URL ("CRM (login required, screenshots only)", RU "CRM (за логином, только скриншоты)") and the trailing "(3 free runs)" / "(3 бесплатных запуска)" are plain `<span>` `font: var(--text-caption)` color `--fg-3`, placed in the grid cell after their link. No filled button in the rail (R-PRINCIPLES-10: on the scene screen the active segment plays the CTA role). |
| Scene | `position: relative; overflow: hidden; background: var(--bg-1)` #F5F5F5 |
| Image box | `position: absolute; top: 96px; right: 96px; bottom: 30px; left: var(--layout-scene-inset-left)` (top = 32 + 44 + 20 clears the mode switch; right = 20 + 48 + 28 clears the stepper); images `width: 100%; height: 100%; object-fit: contain; object-position: center`. This is the floor-plan mode of the picker (R-LAYOUT-19: a raster without its own margins gets scene padding so it never touches the controls). Deviation D-8 from cover cropping: UI captures lose meaning when cropped. |
| Mode switch | 3.4, top 32 right 32 |
| Project stepper | the floor stepper reused for projects (R-APP-20, R-CONTROL-18): `<nav aria-label="01-05">` absolute, `right: var(--space-20); top: 50%; transform: translateY(-50%)`; `width: var(--size-stepper-w)` 48; `box-shadow: var(--shadow-float)`; rows: up arrow cell, five cells "01".."05", down arrow cell. Each row 48 x 44 (deviation D-4: 44 instead of 32/33 for the tap rule), `border-bottom: 1px solid var(--line-stepper)`. Cells: `background: var(--stepper-idle-bg)` #EEEEEE, color `--brand`, `font: var(--text-control)` 14; current project `background: var(--stepper-active-bg)`, color `--stepper-active-fg`, 700, `aria-current="true"`. Arrow cells `background: var(--bg-stepper-arrow)` #ECEBEB, chevron 21. Up on 01 and down on 05 are `disabled` with `opacity: .45` (R-CONTROL-23). Click scrolls the page so that project block top meets the header bottom (`scroll-margin-top: 64px`). |
| Rail handle | R-APP-19: `<button aria-expanded="true">` at the scene's left edge, vertical centre; visual 24 x 44, `background: var(--overlay-glass-90)`, `border-radius: 0 var(--radius-track) var(--radius-track) 0`, `box-shadow: var(--shadow-float)`, chevron stroke 2, `z-index: var(--z-rail-handle)`; hit area 44 x 44 (transparent `::before` 20 px to the right). Collapsed: rail width 0 with `visibility: hidden`, scene takes the full width, chevron flips. Per project, not persisted. |
| Fullscreen | 3.5 corner square, bottom 30 right 32, opens the dialog |

#### D1.2 Project block, 600 to 1199 (deviation D-6)

The split starts at 1200, not 960 (R-RESP-2): at 1024 a 564 px scene would show a 16:10 capture at about 440 px, unreadable. Between 600 and 1199 the block stacks:

1. Scene: `aspect-ratio: 16 / 10`, full width, image fills (contain on `--bg-1`, no padding); mode switch at 20/20 over the image; no stepper, no handle, no corner fullscreen (the image button opens the dialog).
2. Panel: the rail content in the same order, `background: var(--bg-0)`, `padding: var(--space-24)`, inner `max-width: var(--text-measure-body)` 670; `box-shadow: var(--shadow-float)`.

#### D1.3 Project block, < 600

Scene (3.5 portrait or landscape, capsule), then the panel with `padding: var(--layout-gutter-mobile-app)` 20; links in one column, each full width, `height: var(--size-control-cta)` 45 (R-RESP-12 keeps text sizes; only the grid changes). Nothing is scaled down in C (R-TYPE-19: the app never scales type).

#### D1.4 Page at each judge width

| Width | What the first viewport shows |
|---|---|
| 1920 x 1080 | intro in the 1200 container (x 380), app region full width: rail 460, scene 1460, image box about 1334 x 774 |
| 1440 x 900 | intro, the top of project 01 at y <= 620 (rail head, title, top of the scene with the mode switch) |
| 1024 x 768 | intro, then project 01 scene 1024 x 640 (stacked) |
| 768 x 1024 | intro, scene 768 x 480 |
| 390 x 844 | intro, Telegram bar at the bottom |

### D2 "Landing A": dark editorial long scroll

Page order: header, intro, then for each project three bands: head (dark), scene (full bleed), number insert (warm light); then stack, contacts footer. Rhythm (R-PRINCIPLES-16): dark, picture, warm light, dark, picture, warm light ... darkest.

#### D2.1 Project head (A, `--bg-0`)

Container, `padding: var(--layout-section-pad-top) 0 var(--space-40)`. Grid >= 960: `grid-template-columns: var(--layout-two-col-left-w) 1fr; column-gap: var(--layout-two-col-gap-min)` (545 | 39 | 576 in the 1160 content); one column below.

| Column | Content | Spec |
|---|---|---|
| left | number "01" | `font: var(--text-card-index)` 300 11/17, `letter-spacing: var(--tracking-caption)`, color `--fg-2` |
| left | title (heading without number) | `<h2>` `font: var(--text-h2)` 300 42/65, color `--fg-0`; mobile `--text-h2-mobile` 26/40 |
| left | Kind | `font: var(--text-lead-2)` 300 16/20, color `--fg-2`, margin-top 8. Not caps: Kind is longer than 3 words (R-TYPE-20). |
| right | Result | `font: var(--text-lead)` 300 22/28, color `--fg-0`, max-width `--text-measure-lead`, `align-self: end`; mobile `--text-lead-mobile`. Exception: project 03, see D2.3. |

#### D2.2 Scene (C island, full bleed)

`<div class="scene" data-theme="app">`, `width: 100%`.

| Width | Size | Image |
|---|---|---|
| >= 600 | `aspect-ratio: 16 / 10; max-height: calc(100svh - 64px)` | `object-fit: cover; object-position: 50% 0` (top anchor; at 1440 x 900 it cuts 64 px at the bottom, at 1920 x 1080 about 15 percent; never more than 20 percent: if `100svh - 64` is below 80 percent of the 16:10 height, switch to `contain` on `--bg-1`). floor-10-vector (1.506) uses `contain` on `--bg-1`. |
| < 600 | 3.5 | 3.5 |

Controls: mode switch top right (3.4) at >= 600; capsule bottom centre below 600. No fullscreen corner at >= 600 (the capture is already at about native size); below 600 the image button opens the dialog. Background under a contained image: `--bg-1`.

#### D2.3 Number insert (A warm light, `--bg-light` #F7F6F3)

Container, `padding: var(--layout-section-pad-top) 0 var(--layout-section-pad-bottom)`. Grid >= 960: left `--layout-two-col-left-w` 545 | right 1fr, gap as in D2.1 (the services block geometry, R-LANDING-19). One column below 960.

Left column: the hero number and its sentence (taste vault rule 11, R-TYPE-6, R-PRINCIPLES-15).

| Part | Spec |
|---|---|
| Number | `<p class="num" aria-hidden="true">`; `font: var(--text-stat)` 700 52/81; color `--fg-on-light-0` #222222; `letter-spacing: 0`; mobile `--text-stat-mobile` 32/50. It is a substring of the sentence under it, copied character for character. |
| Sentence | `<p>` the full source sentence, `font: var(--text-body)` 300 16/25, `letter-spacing: var(--tracking-caption)`, color `--fg-on-light-1` #2A2A2A, max-width 545; its numbers `<b>` 600. This sentence is removed from wherever else it would appear in the project, so it is shown once (R-CONTENT-16). |

| Project | Number EN | Number RU | Source sentence |
|---|---|---|---|
| 01 matscout | 25 | 25 | Fact 1 ("25 tools behind one MCP server. ..." / "25 инструментов за одним MCP-сервером. ...") |
| 02 Floor plan pipeline | 0.05 m² | 0,05 м² | Fact 2 ("Areas match the official schedule within 0.05 m²." / "Площади сходятся с официальной экспликацией до 0,05 м².") |
| 03 Content Factory | $0.16 | $0,16 | Result ("Cuts a 45 minute episode ..." / "Режет 45-минутную серию ..."); the 03 head therefore shows no Result |
| 04 Trade System | 10 to 30 | 10-30 | Fact 3 ("10 to 30 invoices a day, peak 60." / "10-30 накладных в день, пик 60.") |
| 05 26 MAISI | 279 | 279 | Fact 1 ("Apartment picker over 279 units: ..." / "Подбор по 279 квартирам: ...") |

Right column, top to bottom:

| Part | Spec |
|---|---|
| Remaining facts | `<ul>`; each `<li>` `padding: 12px 0; border-top: 1px solid var(--line-on-light-hairline)` (last also `border-bottom`); `font: var(--text-body-sm)` 300 14/22, `letter-spacing: var(--tracking-caption)`, color `--fg-on-light-1`; numbers `<b>` 600 |
| Data (01), Stack | `<p>` `font: var(--text-caption)` 300 12/19, `letter-spacing: var(--tracking-caption)`, color `--fg-on-light-1`, margin-top 16 / 8 |
| Links | row, `gap: 14px`, margin-top 24. Ghost on light (R-LANDING-20): `height: var(--size-control-field-landing)` 50, `padding: 0 24px`, `border: 1px solid var(--btn-ghost-border-on-light)`, radius 0, `font: var(--text-button)` 400 14, color `--fg-on-light-0`; hover: `background: var(--btn-ghost-hover-invert-bg)` #222222, color `--fg-0` #FFFFFF, border #222222, 200 ms ease-in-out. Below 600: stacked, full width, height `--size-control-cta-mobile` 66 (R-RESP-22). No-URL items as `<span>` `--text-caption` `--fg-on-light-1`. |

No shadows, no radius on the insert or its rows (R-SURFACE-2, R-PRINCIPLES-20: the landing has almost no shadows).

#### D2.4 Page at each judge width

| Width | Notes |
|---|---|
| 1920 | head and insert in the 1200 container; scene 1920 wide, height 1016, top anchored |
| 1440 | scene 1440 x 836, capture close to native size |
| 1024 | head two columns (>= 960), scene 1024 x 640 |
| 768 | head one column, scene 768 x 480, insert one column |
| 390 | head, portrait or landscape scene with capsule, insert with 32/50 number, stacked 66 px links |

#### D1 vs D2 in one line each

D1: a hiring manager scrolls one continuous picker, facts always next to the picture, jump between projects with the stepper; denser, more "instrument".
D2: a slower editorial read, each project gets a full-bleed picture and one big number on warm paper; more "landing", closer to the CMG home page rhythm.

---

## 6. Markup, scripts, a11y

- `index.html`: `<html lang="en" data-theme="landing-dark">`, `<header>`, `<main>` (intro `<section>`, five project `<section>` in fixed order 01..05, stack `<section>`), `<footer>`. DOM order equals reading order (R-CONTENT-10). One `<h1>` (name); each project title `<h2>`; contacts line `<h2>`.
- `<title>`: "Lev Skorokhodov | AI engineer" / "Лев Скороходов | AI-инженер" (content strings joined by the language's " | " separator, R-SURFACE-17). Meta description = Header.Line. `<link rel="alternate" hreflang="en" href="./">`, `hreflang="ru" href="./?lang=ru"`, `x-default`.
- `assets/js/i18n.js`: `{ en: {...}, ru: {...} }` holding every visible string plus alts, keyed like `p01.fact1`; `assets/js/page.js`: language switch, mode switch, capsule, stepper, rail handle, dialog. Vanilla, no build, `defer`. With JS off the page shows EN, first image of each project, working links.
- Non-content strings: the only strings not taken from content.md are four invisible accessible names for icon-only controls, in the i18n dictionary: close "Close" / "Закрыть", previous "Previous" / "Назад", next "Next" / "Далее", rail handle uses the project title. Nothing visible is invented. Mode labels come from content.md Scene modes; alts are '<project title>: <mode label>'.
- No external requests at runtime (fonts local, no analytics, no CDN). All outbound links `rel="noopener"`.
- No horizontal page scroll at 390, 768, 1024, 1440, 1920 (`document.documentElement.scrollWidth <= innerWidth`). Tap targets >= 44 x 44 everywhere (header controls, segments, capsule buttons, stepper rows, handle hit area, links, dialog close).
- Text contrast: `--fg-2` #BABABA on #161616 and `--fg-3` #797979 on #FFFFFF pass for their sizes; do not put `--fg-3` (A, #868686) text on `--bg-light`.
- Scrollbar inside the dialog: 10 px, thumb `--scrollbar-thumb` (R-MOTION-31).

---

## 7. Deviations from the language (all deliberate)

| ID | Rule | What we do | Why |
|---|---|---|---|
| D-1 | R-LANDING-8, R-PRINCIPLES-1 (hero part) | Content-height intro, no photo hero | No own photo; screenshots are the only images; first scene enters the first viewport instead |
| D-2 | R-LANDING-2 (38 px header controls) | 44 px | Hard 44 px tap rule |
| D-3 | R-LANDING-4, R-CONTENT-3 (dropdown with flag) | EN/RU segment, no flag | Two languages; one tap; no decorative imagery |
| D-4 | R-CONTROL-18 (32/33 px stepper rows) | 48 x 44 rows | Tap rule |
| D-5 | R-RESP-16 (116 x 56 capsule, 40 px buttons on mobile) | 140 x 76, 44 px buttons | Tap rule |
| D-6 | R-RESP-2 (split from 960) | split from 1200 (`--bp-lg`) | 16:10 captures unreadable in a 500-740 px scene |
| D-7 | R-MOTION-30 (#2015FF ring in A) | white 2 px ring on dark, brand ring on light | #2015FF on #161616 is about 2:1 |
| D-8 | R-IMG-24 / R-IMG-36 cover crop (D1 desktop) | contain inside scene padding, as floor-plan mode | UI captures lose meaning when cropped |
| D-9 | content.md "[PENDING]" | token hidden, `data-pending="true"` kept | A reader must not see a verification marker. Lev decides whether the token itself must be visible. |

---

## 8. Judge checklist (R-rule IDs)

Principles
- [ ] R-PRINCIPLES-1: each project's screenshot is the dominant surface of its block; first scene visible in the first viewport at 1440 x 900.
- [ ] R-PRINCIPLES-2 / R-APP-2 / R-SURFACE-9: controls over scenes are white glass with `--shadow-float` / `--shadow-capsule`, no dark or colored plates, no backdrop blur over scenes.
- [ ] R-PRINCIPLES-3 / R-APP-39 / R-LAYOUT-18: mode switch top right at 32/32 (20/20 below 960), capsule bottom centre, stepper right edge centre (D1), handle left edge centre (D1); scene centre empty.
- [ ] R-PRINCIPLES-4 / R-PRINCIPLES-22: dark A shell, light C islands; C never darkened.
- [ ] R-PRINCIPLES-5 / R-PRINCIPLES-10 / R-CONTROL-2: exactly one filled button per viewport (Telegram: header >= 600, bottom bar < 600); brand ink only on active segment, active stepper cell, focus ring, outlined link text.
- [ ] R-PRINCIPLES-6: no brand color on backgrounds, borders, meta text.
- [ ] R-PRINCIPLES-9: attention order scene, then title, then numbers, then grey meta.
- [ ] R-PRINCIPLES-13: no hover moves or resizes anything; scene box size fixed while switching.
- [ ] R-PRINCIPLES-15: numbers inside facts are bold, never colored.
- [ ] R-PRINCIPLES-16 (D2): dark, picture, warm light rhythm; page ends on `--bg-1`.
- [ ] R-PRINCIPLES-18: no #000 backgrounds or text; warm greys in A, neutral greys in C.
- [ ] R-PRINCIPLES-19: scenes frameless, no borders, shadows or device mockups on screenshots.
- [ ] R-PRINCIPLES-20: A without shadows except header; C shadows only on floating elements.

Type and color
- [ ] R-TYPE-1 / R-TYPE-2: Nunito Sans in A; AppFont (DM Sans Latin and digits, Manrope Cyrillic) in C; all four woff2 local; Cyrillic renders without fallback fonts.
- [ ] R-TYPE-3 / R-TYPE-4: display 300 55/69 (36/45 mobile) is the only element over 40 px in its viewport (D2 stat band is its own band); A headings weight 300; bold only numbers.
- [ ] R-TYPE-11: every button label 14 px.
- [ ] R-TYPE-13 / R-TYPE-19: C text sizes only 12, 14, 16, 20, 26; C does not scale type between widths.
- [ ] R-TYPE-20: caps only on the role eyebrow and language codes, tracking >= 1 px.
- [ ] R-COLOR-1 / R-COLOR-4: one chromatic ink (#162C25) plus `--badge-type-bg` #4286A0 on the Kind badge (D1), nothing else; no colors outside section 1.2.
- [ ] R-COLOR-10 / R-COLOR-24: screenshots untouched, UI around them neutral.
- [ ] R-COLOR-14: A borders are white or black alpha only.

Layout and surfaces
- [ ] R-LAYOUT-1 / R-LAYOUT-2 / R-LAYOUT-3: 1200 container, content x = 140 at 1440; 24 px gutter below 600, 20 px inside C panels.
- [ ] R-LAYOUT-6: section paddings 64 / 58.
- [ ] R-LAYOUT-13 / R-APP-1 (D1): rail 460, padding 30, `--shadow-float`; split only at >= 1200 (D-6).
- [ ] R-LAYOUT-15 (D1): links grid 2 x 196, gap 8.
- [ ] R-LAYOUT-19 (D1): image inside scene padding, never under the switch or stepper.
- [ ] R-LAYOUT-37 / R-LAYOUT-41: z values only from the token ladder.
- [ ] R-LAYOUT-39 / R-CONTROL-1: control heights 44 / 45 / 50 / 51 / 66 only.
- [ ] R-SURFACE-2 / R-SURFACE-3: A blocks and buttons radius 0 (header controls 3); C radii 3 / 5 / 8 / 10 / 12 / 25 by role.
- [ ] R-SURFACE-16: segment controls are one container with one radius and `overflow: hidden`.
- [ ] R-SURFACE-17: fact rows separated by `border-bottom`, no `<hr>`.
- [ ] R-SURFACE-21: no colored shadows, glows, gradient borders or inset shadows (except underline).

Components
- [ ] R-LANDING-1: header fixed 64, `--overlay-header` + blur 10 + `--shadow-header-landing` + hairline.
- [ ] R-LANDING-2: header order name, language, CTA; equal heights, gap 8.
- [ ] R-LANDING-9: intro order eyebrow, H1, line, hairline 636, three items.
- [ ] R-LANDING-19 / R-LANDING-20 (D2): warm insert geometry 545 | 586; ghost buttons on light invert on hover.
- [ ] R-LANDING-21: contacts ghost links on dark.
- [ ] R-LANDING-30 / R-LANDING-37: bottom bar 73, `--bg-3`, blur 8, one 51 px button, body padded.
- [ ] R-APP-12 (D1): badges id then type, 22 px, radius 3.
- [ ] R-APP-16 / R-CONTROL-16: segment switch 44 high, active `--brand-90` white 700, idle glass-90 brand 400.
- [ ] R-APP-17 / R-CONTROL-7: capsule 140 x 76, glass-30, radius 25, buttons 44 glass-80, hover white + scale 1.05.
- [ ] R-APP-19 (D1): rail handle 24 x 44 visual, 44 x 44 hit, radius 0 12 12 0.
- [ ] R-APP-20 / R-CONTROL-18 (D1): stepper 48 wide, idle #EEEEEE, active brand, arrows #ECEBEB.
- [ ] R-APP-28 (D1): fact rows min 48 with `--line-row`.
- [ ] R-APP-29: only outlined / text / (none) contained in C.
- [ ] R-CONTROL-5 / R-CONTROL-25: no native-styled controls, no text carets or arrow characters.

Imagery, motion, responsive, content
- [ ] R-IMG-1 / R-IMG-2 / R-IMG-3 / R-IMG-5: SVG glyphs 24 grid, stroke 1.4, currentColor, one family.
- [ ] R-IMG-21: detail dialog with pan, close 44, Esc, focus return.
- [ ] R-IMG-23: no MAISI landing captures with baked headlines.
- [ ] R-IMG-25: 2400 / 1200 / 1170 WebP variants, width and height attributes, lazy below the fold; total under 4 MB after full scroll.
- [ ] R-IMG-36: mobile portrait scenes anchored top.
- [ ] R-MOTION-1 / R-MOTION-2: durations only 200 / 250 / 300 / 500 / 600, no bounce.
- [ ] R-MOTION-13 / R-MOTION-23 / R-MOTION-24: no appear-on-scroll, no loops, no animated counters.
- [ ] R-MOTION-29 / R-RESP-19: hover inside the hover guard; tap highlight set.
- [ ] R-MOTION-30: visible `:focus-visible` on every control (D-7 colors).
- [ ] R-MOTION-34: reduced motion honoured (smooth scroll off, 250 ms caps).
- [ ] R-RESP-1 / R-RESP-35: breakpoints 600 / 960 / 1200 / 1920 only; no page horizontal scroll at 390, 768, 1024, 1440, 1920.
- [ ] R-RESP-7: one switcher per scene per width (segment >= 600, capsule < 600).
- [ ] R-RESP-18: every tap target >= 44 (task rule, stricter than the token 40).
- [ ] R-RESP-22: stacked full-width 66 px links below 600 in A.
- [ ] R-CONTENT-9 / R-CONTENT-26: one H2 per section, no section intros or eyebrows beyond the role.
- [ ] R-CONTENT-10: DOM order equals visual order.
- [ ] R-CONTENT-20: no language mixing; RU mode shows only RU strings (plus brand names, stack list, URLs, "Telegram", "GitHub").
- [ ] R-UX-42: one i18n dictionary, `?lang=ru` works, choice remembered in localStorage.
- [ ] Lev: no emoji, no em or en dash, no decorative unicode in any file, alt or title; every visible string traceable to content.md; no helper plates, footnotes or marketing words.
