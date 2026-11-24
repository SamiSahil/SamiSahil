"""Generate dark and light GitHub profile banners for Samiuzzaman Sahil.

Run:  python make_banner.py
Outputs:
  assets/banner-dark.png   (1600 x 420)
  assets/banner-light.png  (1600 x 420)

Edit the CONTENT block below if your details change.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

# ---------------------------------------------------------------------------
# Content
# ---------------------------------------------------------------------------
NAME = "Samiuzzaman Sahil"
EYEBROW = "FULL-STACK DEVELOPER"
TAGLINE = "Building clean, reliable web applications \u2014 end to end."
TECH = "React  \u00b7  Node.js  \u00b7  Express  \u00b7  MongoDB  \u00b7  PostgreSQL  \u00b7  Prisma"
LOCATION = "Dhaka, Bangladesh"
URL = "github.com/SamiSahil"
MONOGRAM = "SS"

W, H = 1600, 420
OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

FONT_DIR = Path(r"C:\Windows\Fonts")
BOLD = str(FONT_DIR / "segoeuib.ttf")
SEMIBOLD = str(FONT_DIR / "seguisb.ttf")
REGULAR = str(FONT_DIR / "segoeui.ttf")
MONO = str(FONT_DIR / "consola.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def draw_tracked(draw, xy, text, fnt, fill, tracking=0.0):
    """Draw text with extra letter spacing."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill, anchor="la")
        x += draw.textlength(ch, font=fnt) + tracking


def vertical_gradient(size, top, bottom):
    grad = Image.linear_gradient("L").resize(size)
    return Image.composite(Image.new("RGB", size, bottom), Image.new("RGB", size, top), grad)


def make_banner(palette, filename):
    base = vertical_gradient((W, H), palette["bg_top"], palette["bg_bottom"]).convert("RGBA")

    # Soft accent glow on the right
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    g = ImageDraw.Draw(glow)
    r, gg, b = palette["accent"]
    g.ellipse((1120, -220, 1820, 480), fill=(r, gg, b, palette["glow_alpha"]))
    g.ellipse((-320, 240, 520, 700), fill=(r, gg, b, max(14, palette["glow_alpha"] // 2)))
    glow = glow.filter(ImageFilter.GaussianBlur(140))
    base = Image.alpha_composite(base, glow)

    # Fine grid
    grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grid)
    line = palette["grid"]
    for x in range(0, W, 80):
        gd.line((x, 0, x, H), fill=line, width=1)
    for y in range(0, H, 80):
        gd.line((0, y, W, y), fill=line, width=1)
    base = Image.alpha_composite(base, grid)

    d = ImageDraw.Draw(base)

    # Small accent bar above the eyebrow
    d.rectangle((110, 84, 154, 90), fill=palette["accent"])

    draw_tracked(d, (110, 104), EYEBROW, font(SEMIBOLD, 20), palette["accent"], tracking=4.2)

    d.text((106, 138), NAME, font=font(BOLD, 76), fill=palette["text"], anchor="la")

    d.rectangle((110, 250, 190, 254), fill=palette["accent"])

    d.text((110, 272), TAGLINE, font=font(REGULAR, 27), fill=palette["muted"], anchor="la")
    d.text((110, 326), TECH, font=font(MONO, 20), fill=palette["tech"], anchor="la")

    # Monogram card
    card = (1322, 116, 1482, 276)
    d.rounded_rectangle(
        card,
        radius=34,
        fill=palette["card"],
        outline=palette["accent"],
        width=3,
    )
    d.text(
        ((card[0] + card[2]) // 2, (card[1] + card[3]) // 2 - 4),
        MONOGRAM,
        font=font(BOLD, 74),
        fill=palette["accent"],
        anchor="mm",
    )
    d.text(
        ((card[0] + card[2]) // 2, 302),
        LOCATION,
        font=font(REGULAR, 20),
        fill=palette["muted"],
        anchor="ma",
    )

    d.text((1490, 372), URL, font=font(MONO, 18), fill=palette["tech"], anchor="ra")

    base.convert("RGB").save(OUT / filename, "PNG", optimize=True)
    print(f"wrote {OUT / filename}")


DARK = {
    "bg_top": (11, 13, 16),
    "bg_bottom": (22, 26, 32),
    "text": (243, 246, 249),
    "muted": (170, 178, 188),
    "tech": (139, 148, 158),
    "accent": (217, 154, 108),
    "card": (27, 31, 38),
    "grid": (255, 255, 255, 9),
    "glow_alpha": 52,
}

LIGHT = {
    "bg_top": (252, 248, 244),
    "bg_bottom": (240, 227, 216),
    "text": (31, 35, 41),
    "muted": (95, 100, 108),
    "tech": (108, 92, 80),
    "accent": (168, 95, 60),
    "card": (255, 255, 255),
    "grid": (60, 45, 35, 8),
    "glow_alpha": 34,
}

if __name__ == "__main__":
    make_banner(DARK, "banner-dark.png")
    make_banner(LIGHT, "banner-light.png")
