from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PUBLIC = ROOT / "public"
DIST = ROOT / "dist"


def ensure_inside(path: Path, parent: Path) -> None:
    resolved = path.resolve()
    root = parent.resolve()
    if resolved != root and root not in resolved.parents:
        raise RuntimeError(f"Refusing to operate outside repository: {resolved}")


def main() -> None:
    ensure_inside(DIST, ROOT)
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(DOCS, DIST)
    if PUBLIC.exists():
        shutil.copytree(PUBLIC, DIST, dirs_exist_ok=True)
    print(f"Built static site at {DIST}")


if __name__ == "__main__":
    main()
