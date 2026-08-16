#!/usr/bin/env python3
"""Validate the public catalog and create deterministic per-skill ZIP files."""

from __future__ import annotations

import json
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
DIST_DIR = ROOT / "dist"


def read_frontmatter(skill_file: Path) -> dict[str, str]:
    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{skill_file} is missing YAML frontmatter")
    _, frontmatter, _ = text.split("---", 2)
    values: dict[str, str] = {}
    for line in frontmatter.strip().splitlines():
        key, separator, value = line.partition(":")
        if separator:
            values[key.strip()] = value.strip().strip('"')
    return values


def main() -> None:
    catalog = json.loads((ROOT / "skills.json").read_text(encoding="utf-8"))
    entries = catalog.get("skills", [])
    names = [entry["name"] for entry in entries]
    folders = sorted(path.name for path in SKILLS_DIR.iterdir() if path.is_dir())
    if sorted(names) != folders:
        raise ValueError("skills.json and skills/ contain different skill names")

    shutil.rmtree(DIST_DIR, ignore_errors=True)
    DIST_DIR.mkdir()

    for name in names:
        skill_dir = SKILLS_DIR / name
        frontmatter = read_frontmatter(skill_dir / "SKILL.md")
        if frontmatter.get("name") != name:
            raise ValueError(f"{name}/SKILL.md has a mismatched name")
        if not frontmatter.get("description"):
            raise ValueError(f"{name}/SKILL.md has no description")

        archive_path = DIST_DIR / f"{name}.zip"
        with zipfile.ZipFile(
            archive_path,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
        ) as archive:
            for source in sorted(skill_dir.rglob("*")):
                if source.is_file():
                    archive.write(source, source.relative_to(skill_dir))
        print(f"built {archive_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
