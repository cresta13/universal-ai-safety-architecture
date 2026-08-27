from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "og-ru.png"
W, H = 1200, 630
INK = "#302D36"
PAPER = "#FFFDF8"
MAUVE = "#DDB6D5"
BLUE = "#AEC6E8"
PISTACHIO = "#C8DFB4"
PEACH = "#F4C6A8"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def note(draw: ImageDraw.ImageDraw, xy: tuple[int, int], size: tuple[int, int], fill: str, title: str, body: str) -> None:
    x, y = xy
    w, h = size
    draw.rounded_rectangle((x, y, x + w, y + h), radius=9, fill=fill, outline="#D5CABD", width=2)
    draw.rectangle((x + w - 130, y - 13, x + w - 30, y + 9), fill="#C9B2C8")
    draw.text((x + 24, y + 22), title, fill=INK, font=font(30, True))
    draw.text((x + 24, y + 68), body, fill=INK, font=font(24))


def main() -> None:
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    for x in range(0, W, 36):
        draw.line((x, 0, x + 120, H), fill="#F2EBDD", width=1)
    draw.rectangle((125, 70, 1075, 150), fill=MAUVE)
    draw.text((155, 82), "UAIS — русская интерактивная веб-книга", fill=INK, font=font(48, True))
    draw.text((155, 176), "Может сделать ≠ имеет право сделать.", fill=INK, font=font(40, True))
    note(draw, (120, 280), (285, 190), BLUE, "Возможность", "что система\nможет сделать")
    note(draw, (460, 255), (285, 220), PISTACHIO, "Полномочие", "что ей\nразрешено")
    note(draw, (800, 285), (285, 185), PEACH, "Доказательство", "почему решение\nлегитимно")
    draw.line((405, 375, 460, 365), fill=INK, width=5)
    draw.line((745, 365, 800, 380), fill=INK, width=5)
    draw.text((155, 535), "Universal AI Safety Architecture · Draft 1.0 Candidate 3", fill="#6A6472", font=font(25, True))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, quality=92)
    print(f"Generated {OUT}")


if __name__ == "__main__":
    main()
