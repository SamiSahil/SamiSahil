"""Generate the LinkedIn profile banner for Samiuzzaman Sahil.

Run:  python make_linkedin_banner.py
Output:
  assets/linkedin-banner.png   (1584 x 396)

LinkedIn crops the banner behind the profile photo on the left, so keep the
left third mostly clear and put copy on the right.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1584, 396
SCALE = 2
w, h = W * SCALE, H * SCALE

BG_TOP = (10, 12, 16)
BG_BOTTOM = (22, 20, 24)
COPPER = (217, 154, 108)
WHITE = (245, 243, 240)
MUTED = (168, 163, 156)
FAINT = (120, 116, 110)

FONTS = Path(r"C:\Windows\Fonts")
OUT = Path(__file__).parent / "assets" / "linkedin-banner.png"


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size * SCALE)


def tracked(draw, xy, text, fnt, fill, tracking):
    x, y = xy
    for char in text:
        draw.text((x, y), char, font=fnt, fill=fill)
        x += draw.textlength(char, font=fnt) + tracking * SCALE


def gradient(size, top, bottom):
    ramp = Image.linear_gradient("L").resize(size)
    return Image.composite(Image.new("RGB", size, bottom), Image.new("RGB", size, top), ramp)


def main():
    base = gradient((w, h), BG_TOP, BG_BOTTOM).convert("RGBA")

    dots = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    dot = ImageDraw.Draw(dots)
    step = 22 * SCALE
    for x in range(0, w, step):
        for y in range(0, h, step):
            dot.ellipse((x, y, x + 1.5 * SCALE, y + 1.5 * SCALE), fill=(255, 255, 255, 14))
    base = Image.alpha_composite(base, dots)

    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    g = ImageDraw.Draw(glow)
    g.ellipse((1050 * SCALE, -300 * SCALE, 1900 * SCALE, 380 * SCALE), fill=(176, 106, 69, 80))
    g.ellipse((-400 * SCALE, 240 * SCALE, 500 * SCALE, 900 * SCALE), fill=(176, 106, 69, 26))
    glow = glow.filter(ImageFilter.GaussianBlur(140 * SCALE))
    base = Image.alpha_composite(base, glow)

    d = ImageDraw.Draw(base)
    x = 620 * SCALE

    tracked(d, (x, 94 * SCALE), "FULL-STACK DEVELOPER", font("consola.ttf", 15), COPPER, 3.4)
    d.rectangle((x, 128 * SCALE, x + 58 * SCALE, 133 * SCALE), fill=COPPER)

    d.text((x - 3 * SCALE, 148 * SCALE), "Samiuzzaman Sahil", font=font("segoeuib.ttf", 50), fill=WHITE)
    d.text((x, 216 * SCALE), "Building clean, reliable web applications", font=font("segoeui.ttf", 22), fill=MUTED)
    d.text((x, 248 * SCALE), "from database to interface.", font=font("segoeui.ttf", 22), fill=MUTED)
    d.text(
        (x, 298 * SCALE),
        "React   \u00b7   Node.js   \u00b7   Express   \u00b7   MongoDB   \u00b7   PostgreSQL",
        font=font("consola.ttf", 14),
        fill=FAINT,
    )

    d.line((84 * SCALE, 330 * SCALE, 1500 * SCALE, 330 * SCALE), fill=(255, 255, 255, 22), width=1 * SCALE)
    d.text((84 * SCALE, 346 * SCALE), "samisahil.github.io/portfolio", font=font("consola.ttf", 14), fill=COPPER)
    d.text(
        (1500 * SCALE, 346 * SCALE),
        "Dhaka, Bangladesh   \u00b7   Open to internships",
        font=font("segoeui.ttf", 14),
        fill=FAINT,
        anchor="ra",
    )

    out = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    out.alpha_composite(base.resize((W, H), Image.LANCZOS))
    OUT.parent.mkdir(exist_ok=True)
    out.convert("RGB").save(OUT, "PNG", optimize=True)
    print("wrote", OUT, OUT.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
