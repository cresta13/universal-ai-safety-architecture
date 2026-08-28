from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
W, H = 1200, 630
INK = "#302D36"
SOFT = "#6A6472"
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
    draw.multiline_text((x + 24, y + 68), body, fill=INK, font=font(24), spacing=7)


def draw_card(out: Path, title: str, line: str, notes: list[tuple[str, str, str]], footer: str) -> None:
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    for x in range(-120, W, 36):
        draw.line((x, 0, x + 140, H), fill="#F2EBDD", width=1)
    draw.rectangle((125, 70, 1075, 150), fill=MAUVE)
    draw.text((155, 82), title, fill=INK, font=font(46, True))
    draw.text((155, 176), line, fill=INK, font=font(40, True))
    xs = [120, 460, 800]
    sizes = [(285, 190), (285, 220), (285, 185)]
    for (x, size, item) in zip(xs, sizes, notes):
        fill, note_title, body = item
        note(draw, (x, 280 if x != 460 else 255), size, fill, note_title, body)
    draw.line((405, 375, 460, 365), fill=INK, width=5)
    draw.line((745, 365, 800, 380), fill=INK, width=5)
    draw.text((155, 535), footer, fill=SOFT, font=font(25, True))
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, quality=92)
    print(f"Generated {out}")


def main() -> None:
    draw_card(
        ROOT / "docs" / "assets" / "og-en.png",
        "UAIS — Intelligence Does Not Imply Authority",
        "Can do ≠ may do.",
        [
            (BLUE, "Capability", "what the system\ncan do"),
            (PISTACHIO, "Authority", "what was\nlegitimately granted"),
            (PEACH, "Evidence", "why a decision\nis accountable"),
        ],
        "Universal AI Safety Architecture · Draft 1.0 Candidate 3",
    )
    draw_card(
        ROOT / "docs" / "assets" / "og-ru.png",
        "UAIS — Интеллект не означает полномочия",
        "Может сделать ≠ имеет право сделать.",
        [
            (BLUE, "Возможность", "что система\nможет сделать"),
            (PISTACHIO, "Полномочие", "что ей\nразрешено"),
            (PEACH, "Доказательство", "почему решение\nлегитимно"),
        ],
        "Universal AI Safety Architecture · Draft 1.0 Candidate 3",
    )


if __name__ == "__main__":
    main()
