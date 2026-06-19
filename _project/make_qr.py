"""
Generate 8 creative QR variants — playful, elegant, not corporate.
Run: .venv/bin/python _project/make_qr.py
"""

import qrcode
from qrcode.constants import ERROR_CORRECT_H
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import (
    CircleModuleDrawer, RoundedModuleDrawer,
    GappedSquareModuleDrawer, VerticalBarsDrawer,
)
from qrcode.image.styles.colormasks import (
    SolidFillColorMask, RadialGradiantColorMask,
)
from PIL import Image, ImageDraw, ImageEnhance

URL      = "https://regalo.sudheim.eu"
PORTRAIT = "_project/portrait.png"
QR_SIZE  = 1200

# ── Palette ───────────────────────────────────────────────────
CREAM  = (250, 249, 247)   # site cream
CHALK  = (245, 240, 232)   # warmer off-white
DARK   = (15,  15,  26 )   # site dark (cool navy)
WARM   = (28,  16,  6  )   # warm espresso dark
BALTIC = (13,  43,  34 )   # dark Baltic green
DEEP   = (22,  16,  34 )   # deep warm purple

# ── Helpers ───────────────────────────────────────────────────
def make_qr(drawer, fg, bg):
    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(URL)
    qr.make(fit=True)
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=drawer,
        color_mask=SolidFillColorMask(back_color=bg, front_color=fg),
    ).convert("RGBA")
    return img.resize((QR_SIZE, QR_SIZE), Image.LANCZOS)

def make_qr_gradient(drawer, bg, center_color, edge_color):
    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(URL)
    qr.make(fit=True)
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=drawer,
        color_mask=RadialGradiantColorMask(
            back_color=bg,
            center_color=center_color,
            edge_color=edge_color,
        ),
    ).convert("RGBA")
    return img.resize((QR_SIZE, QR_SIZE), Image.LANCZOS)

def load_portrait(frac, brightness=1.5):
    px  = int(QR_SIZE * frac)
    raw = Image.open(PORTRAIT).convert("RGBA")
    w, h = raw.size; side = min(w, h)
    img = raw.crop(((w-side)//2, (h-side)//2, (w+side)//2, (h+side)//2))
    img = img.resize((px, px), Image.LANCZOS)
    return ImageEnhance.Brightness(img).enhance(brightness), px

def rr_mask(w, h, r):
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w-1, h-1], radius=r, fill=255)
    return m

def rounded(img, r):
    out = img.copy().convert("RGBA")
    out.putalpha(rr_mask(img.width, img.height, r))
    return out

def block(color, w, h):
    return Image.new("RGBA", (w, h), color + (255,))

def mat_frame(photo, pad, r_photo, bg):
    """Photo with rounded corners sitting on a slightly larger rounded bg."""
    sz = photo.width + pad * 2
    f  = Image.new("RGBA", (sz, sz), (0, 0, 0, 0))
    f.paste(block(bg, sz, sz), mask=rr_mask(sz, sz, r_photo + pad // 2))
    f.paste(rounded(photo, r_photo), (pad, pad), rounded(photo, r_photo))
    return f

def stroke_frame(photo, r, sw, color):
    """Photo with a solid rounded border."""
    sz = photo.width + sw * 2
    f  = Image.new("RGBA", (sz, sz), (0, 0, 0, 0))
    f.paste(block(color, sz, sz), mask=rr_mask(sz, sz, r + sw))
    f.paste(rounded(photo, r), (sw, sw), rounded(photo, r))
    return f

def double_frame(photo, r, pad, sw, inner_bg, outer_color):
    """Photo → cream mat → thin colored stroke. Two layers."""
    cs   = photo.width + pad * 2
    cr   = r + pad // 2
    mat  = Image.new("RGBA", (cs, cs), (0, 0, 0, 0))
    mat.paste(block(inner_bg, cs, cs), mask=rr_mask(cs, cs, cr))
    mat.paste(rounded(photo, r), (pad, pad), rounded(photo, r))
    ts   = cs + sw * 2
    f    = Image.new("RGBA", (ts, ts), (0, 0, 0, 0))
    f.paste(block(outer_color, ts, ts), mask=rr_mask(ts, ts, cr + sw))
    f.paste(mat, (sw, sw), mat)
    return f

def place(base, overlay):
    b   = base.copy()
    pos = ((b.width - overlay.width) // 2, (b.height - overlay.height) // 2)
    b.paste(overlay, pos, overlay)
    return b

def save(img, n, label):
    path = f"_project/qr_v{n}.png"
    img.save(path, dpi=(300, 300))
    print(f"  {path}  —  {label}")


# ═══════════════════════════════════════════════════ VARIANTS

print("Generating…\n")

# V1 ── Warm espresso dots · cream mat
# Dots feel friendlier than squares. Warm dark reads less "tech", more "print".
p, px = load_portrait(0.30)
r     = px // 6
frame = mat_frame(p, 18, r, CREAM)
save(place(make_qr(CircleModuleDrawer(), WARM, CREAM), frame), 1,
     "Warm espresso dots · cream mat · 30% photo")

# V2 ── Baltic green dots · chalk bg · coastal double frame
# The Baltic sea is dark green. This makes the QR feel like it belongs to the place.
p, px = load_portrait(0.28)
r     = px // 6
frame = double_frame(p, r, 14, 5, CHALK, BALTIC)
save(place(make_qr(CircleModuleDrawer(), BALTIC, CHALK), frame), 2,
     "Baltic green dots · chalk bg · coastal double frame")

# V3 ── Rounded modules · large photo · site palette
# Rounded modules soften the whole thing. Big photo lets them see each other first.
p, px = load_portrait(0.36)
r     = px // 4
frame = mat_frame(p, 20, r, CREAM)
save(place(make_qr(RoundedModuleDrawer(), DARK, CREAM), frame), 3,
     "Rounded modules · large photo 36% · cream mat")

# V4 ── Gapped squares · pill photo · dark stroke
# The gap between squares gives air. Pill-shaped photo against grid: playful contrast.
p, px = load_portrait(0.28)
r     = px // 2
frame = stroke_frame(p, r, 7, DARK)
save(place(make_qr(GappedSquareModuleDrawer(), DARK, CREAM), frame), 4,
     "Gapped squares · pill photo · dark stroke")

# V5 ── Radial gradient dots · warm-to-cool · cream mat
# Modules fade from warm espresso at centre to cool navy at edges.
# Gives the QR a glow that draws the eye inward toward the photo.
p, px = load_portrait(0.30)
r     = px // 5
frame = mat_frame(p, 18, r, CREAM)
save(place(make_qr_gradient(CircleModuleDrawer(), CREAM, WARM, DARK), frame), 5,
     "Gradient dots: warm centre → cool edges · cream mat")

# V6 ── Rounded modules · Baltic canvas · chalk mat · 32%
# Larger photo on Baltic green QR. Coastal, specific to the destination.
p, px = load_portrait(0.32)
r     = px // 4
frame = mat_frame(p, 18, r, CHALK)
save(place(make_qr(RoundedModuleDrawer(), BALTIC, CHALK), frame), 6,
     "Rounded modules · Baltic green · chalk bg · 32% photo")

# V7 ── Vertical bars · warm · generous mat
# Vertical bars give a completely different texture — less "QR code", more pattern.
p, px = load_portrait(0.28)
r     = px // 6
frame = mat_frame(p, 24, r, CREAM)
save(place(make_qr(VerticalBarsDrawer(), WARM, CREAM), frame), 7,
     "Vertical bars · warm dark · generous cream mat")

# V8 ── Dots · very large photo · deep purple tone
# 40% photo is bold. Deep purple-dark is warm without being brown.
p, px = load_portrait(0.40)
r     = px // 4
frame = mat_frame(p, 14, r, CREAM)
save(place(make_qr(CircleModuleDrawer(), DEEP, CREAM), frame), 8,
     "Dots · deep purple-dark · very large photo 40%")

print("\nDone.")
