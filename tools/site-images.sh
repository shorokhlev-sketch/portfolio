#!/bin/bash
# Scene images for site/: desktop captures -> <name>-2400.webp and <name>-1200.webp, phone captures -> <name>-m.webp.
# Source files live in ./shots/<project>/ (see index.json there).
set -e
# IMG_OUT: write somewhere else (a scratch folder) to check the script against the committed images
S=./shots; O=${IMG_OUT:-./site/assets/img}
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
d() { # project name source
  mkdir -p "$O/$1"; W=$(sips -g pixelWidth "$3" | awk '/pixelWidth/{print $2}')
  if [ "$W" -gt 2400 ]; then cwebp -quiet -q 80 -m 6 -resize 2400 0 "$3" -o "$O/$1/$2-2400.webp"; else cwebp -quiet -q 80 -m 6 "$3" -o "$O/$1/$2-2400.webp"; fi
  cwebp -quiet -q 80 -m 6 -resize 1200 0 "$3" -o "$O/$1/$2-1200.webp"
}
m() { mkdir -p "$O/$1"; cwebp -quiet -q 78 -m 6 "$3" -o "$O/$1/$2-m.webp"; }
# phone captures of dense app UI (small text) at q 80
m80() { mkdir -p "$O/$1"; cwebp -quiet -q 80 -m 6 "$3" -o "$O/$1/$2-m.webp"; }
# plan drawings: lossless, so the #F5F5F5 ground stays exactly --bg-1 (lossy YUV turns it into #F6F6F6 and the frame edge shows)
# and flat vector art comes out smaller than lossy anyway
dl() {
  mkdir -p "$O/$1"; W=$(sips -g pixelWidth "$3" | awk '/pixelWidth/{print $2}')
  if [ "$W" -gt 2400 ]; then cwebp -quiet -lossless -z 9 -resize 2400 0 "$3" -o "$O/$1/$2-2400.webp"; else cwebp -quiet -lossless -z 9 "$3" -o "$O/$1/$2-2400.webp"; fi
  cwebp -quiet -lossless -z 9 -resize 1200 0 "$3" -o "$O/$1/$2-1200.webp"
}
ml() { mkdir -p "$O/$1"; cwebp -quiet -lossless -z 9 "$3" -o "$O/$1/$2-m.webp"; }

# first scene of project 01: the clean pipeline output (floating UI hidden, background #F5F5F5 = --bg-1), 2400 x 1594
dl floorplans floor-10-vector "$S/floorplans/floor-10-vector.png"
d floorplans unit-editor "$S/floorplans/plan-studio-unit-editor.png"
d floorplans raw-layers "$S/floorplans/plan-studio-floor-10-raw-layers.png"
# apartment modes: one unit out of the 279, both at the same plan scale (74% of the 2x export) on #F5F5F5 = --bg-1
dl floorplans unit-2201 "$S/floorplans/unit-2201-plan-desktop.png"
dl floorplans unit-1005 "$S/floorplans/unit-1005-plan-desktop.png"
# phone set of p-01: the floor plan whole (never cut) on a 4:5 canvas of --bg-1, same width and margins as the 2BR 4:5 frame;
# the phone stack centres these frames vertically (data-mpos="center")
T0=$(mktemp -d)
magick "$S/floorplans/floor-10-vector.png" -resize 1110x -gravity center -background '#F5F5F5' -extent 1170x1462 "$T0/floor.png"
ml floorplans floor-10-vector "$T0/floor.png"
ml floorplans unit-2201 "$S/floorplans/unit-2201-plan-mobile-4x5.png"
ml floorplans unit-1005 "$S/floorplans/unit-1005-plan-mobile.png"
rm -rf "$T0"

d trade sales "$S/trade/desktop-1280-01-sales.png"
d trade ai-inbox "$S/trade/desktop-1280-02-ai-inbox-edit.png"
d trade trip "$S/trade/desktop-1280-03-trip-detail.png"
d trade pricelist "$S/trade/desktop-1280-04-pricelist.png"
m80 trade settlements "$S/trade/mobile-04-settlements-suppliers.png"
m80 trade sales "$S/trade/mobile-02-sales.png"

# picker captures: the picker's own view switch (#segmented) is hidden by capture-only CSS, so the scene has one mode switch
# 3D view: AI tower frames with the PLACEHOLDER lattice, unit polygons, frame label and cookie bar hidden (scratchpad pw/maisi3d.mjs)
d maisi 3d "$S/maisi/picker-3d-desktop.png"
d maisi floorplan-status "$S/maisi/picker-floorplan-status-desktop.png"
# grid: the facade preview in the rail (#railPreview, the generated tower render) is hidden too (scratchpad pw/r1-maisi.mjs grid)
d maisi grid "$S/maisi/picker-2d-grid-desktop.png"
d maisi unit-detail "$S/maisi/unit-detail-desktop.png"
# phone picker captures: the picker's bottom tab bar (#tabbar, its own view switch) and the frame chip are hidden by capture-only CSS
# (scratchpad pw/maisi-noswitch.mjs, which also answers /crm/api/track locally)
# floor plans on the phone: status toggle on and unit #1009 tapped, its sheet open (scratchpad pw/r1-maisi.mjs floor-m)
m maisi 3d "$S/maisi/picker-3d-mobile.png"
m maisi floorplan "$S/maisi/picker-floorplan-mobile.png"
m80 maisi unit-detail "$S/maisi/unit-detail-mobile.png"
# no CRM frame on phones: the phone set of p-05 is Floor plans, Unit (content.md "Scene modes")

# Telegram store: the shop name is blurred in the source captures (shots/tgstore/index.json).
# desktop-04-lot-gallery is never used: its main photo is a watermarked press image.
# catalog: the MacBook press photo keeps a pink watermark remnant at x 1262-1301, y 967-979 (2880 x 1800). It is filled from
# the 14 rows above it, corrected row by row by the change in the column just left of it, so the floor gradient runs on.
magick "$S/tgstore/desktop-01-catalog.png" \
  \( -clone 0 -crop 42x14+1260+952 +repage \) \
  \( -clone 0 -crop 1x14+1258+966 +repage -scale '42x14!' \) \
  \( -clone 0 -crop 1x14+1258+952 +repage -scale '42x14!' \) \
  \( -clone 1-3 -fx 'u[0]+u[1]-u[2]' \) -delete 1-3 -geometry +1260+966 -composite "$T/catalog.png"
d tgstore catalog "$T/catalog.png"
d tgstore search "$S/tgstore/desktop-02-palette.png"
d tgstore lot "$S/tgstore/desktop-03-lot.png"
d tgstore board "$S/tgstore/extra-mockup-palette-variant-c.png"
# phone catalog: the same press photo keeps the watermark at x 496-544, y 1057-1070 (1170 x 2532), filled the same way
magick "$S/tgstore/mobile-01-catalog.png" \
  \( -clone 0 -crop 49x14+496+1043 +repage \) \
  \( -clone 0 -crop 1x14+495+1057 +repage -scale '49x14!' \) \
  \( -clone 0 -crop 1x14+495+1043 +repage -scale '49x14!' \) \
  \( -clone 1-3 -fx 'u[0]+u[1]-u[2]' \) -delete 1-3 -geometry +496+1057 -composite "$T/catalog-m.png"
m tgstore catalog "$T/catalog-m.png"
m tgstore filters "$S/tgstore/mobile-02-filters.png"
m tgstore lot "$S/tgstore/mobile-04-lot.png"
m tgstore request "$S/tgstore/mobile-06-buy-sheet.png"

# AI video production: stills fill the scene edge to edge; the storyboard UI capture is shown whole.
# Technics is stills only (no music rights for the reel audio). Phone stills are 4:5, sized to 1170 wide (390 css at 3x).
d aivisual copper "$S/aivisual/sn-copper-vault-desktop.png"
d aivisual stone "$S/aivisual/sn-stone-overhead-desktop.png"
# porcelain: the frame carries flat #0B0B0B pillarbox bars at x 0-145 and 2255-2399 and a soft dark pillarbox inside them
# (near-flat columns x 150-268 and 2150-2255, hard vertical edge); cut to 16:10 inside x 274-2145, figure centred, never upscaled
magick "$S/aivisual/sn-porcelain-flooded-desktop.png" -crop 1872x1170+274+165 +repage "$T/porcelain.png"
d aivisual porcelain "$T/porcelain.png"
# Technics: a studio still on a flat light ground. Its top and bottom rows are extended (edge pixels, 292 px each side, 1.16:1)
# so a tall scene crops ground instead of the speaker; at 16:10 the scene shows exactly the original frame.
# The two added bands are blurred sideways only (Blur:0x40 is a horizontal kernel): a copied edge row turns every column
# into a vertical streak, which the viewer shows whole; blurred, each band is a smooth 245 to 253 gradient.
magick "$S/aivisual/technics-exploded-desktop.png" -set option:distort:viewport 2458x2120+0-292 -virtual-pixel edge -filter point -distort SRT 0 +repage \
  \( +clone -crop 2458x292+0+0 +repage -morphology Convolve Blur:0x40 \) -geometry +0+0 -composite \
  \( -clone 0 -crop 2458x292+0+1828 +repage -morphology Convolve Blur:0x40 \) -geometry +0+1828 -composite "$T/technics.png"
d aivisual technics "$T/technics.png"
d aivisual storyboard "$S/aivisual/storyboard-canvas-dock-desktop.png"
for n in copper:sn-copper-vault stone:sn-stone-overhead porcelain:sn-porcelain-flooded; do
  mkdir -p "$O/aivisual"; cwebp -quiet -q 78 -m 6 -resize 1170 0 "$S/aivisual/${n#*:}-mobile.png" -o "$O/aivisual/${n%%:*}-m.webp"
done

d matscout result "$S/matscout/desktop-01-result-hero.png"
d matscout trace "$S/matscout/desktop-02-two-phase-trace.png"
d matscout table "$S/matscout/desktop-03-ranked-table.png"
d matscout diagram "$S/matscout/desktop-04-phase-diagram-ternary.png"
d matscout structure-3d "$S/matscout/desktop-05-3d-viewer.png"
m matscout result "$S/matscout/mobile-01-result-top.png"
m matscout structure-3d "$S/matscout/mobile-02-3d-viewer.png"

# CRM agent cabinet: 2x capture, 3056 x 1568 (1528 x 784 css, scratchpad pw/r1-crm-desk.mjs). Cropped right after the sidebar
# border (x 440-441), so the content padding is 62 px left and 64 px right, and above the Active leads card (its border starts at y 1490).
# CRM: admin dashboard of a local run on the demo seed (scratchpad pw/crm-admin.mjs), 1440x900 at 2x, with the sidebar
d maisi crm "$S/maisi-crm/crm-admin-dashboard.png"

# Content Factory: captures from the live demo by tools/factory-shoot.mjs (shots/factory/index.json).
# The app header above the sticky step bar (41 css px: the topbar and the strip under it where scrolled content shows) is cut.
# desktop 2x (2880 x 1800) -> 2880 x 1718 -> 2400 x 1432
for n in scenes:desktop-02-scenes subtitles:desktop-03-subtitles clips:desktop-07-clips trim:desktop-09-trim; do
  magick "$S/factory/${n#*:}.png" -crop 2880x1718+0+82 +repage "$T/${n%%:*}.png"
  d factory "${n%%:*}" "$T/${n%%:*}.png"
done
# phone 3x (1170 x 2532) -> 1170 x 2409
for n in scenes:mobile-02-scenes subtitles:mobile-03-subtitles clips:mobile-07-clips; do
  magick "$S/factory/${n#*:}.png" -crop 1170x2409+0+123 +repage "$T/${n%%:*}-m.png"
  m80 factory "${n%%:*}" "$T/${n%%:*}-m.png"
done

# PNG tab icon for browsers without SVG favicon support
if [ -f "$O/apple-touch-icon.png" ]; then sips -z 32 32 "$O/apple-touch-icon.png" --out "$O/favicon-32.png" >/dev/null; fi
