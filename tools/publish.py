#!/usr/bin/env python3
"""Publish an allowlisted subset of an Obsidian vault as GitHub Markdown."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.parse import quote

NOTE_FOLDERS = ("Algebra II", "Precalculus", "Calculus I", "Quizzes")
OWNED_PATHS = (*NOTE_FOLDERS, "assets", "README.md")
SCREENSHOT_PREFIXES = ("Pasted image", "Pasted Image", "Screenshot")
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp"}
EMBED_RE = re.compile(r"!\[\[([^\]]+)\]\]")
WIKILINK_RE = re.compile(r"(?<!!)\[\[([^\]]+)\]\]")


@dataclass(frozen=True)
class Note:
    source: Path
    title: str
    folder: str
    content: str


@dataclass(frozen=True)
class Report:
    classified: dict[str, tuple[str, ...]]
    skipped: tuple[str, ...]
    screenshots: tuple[str, ...]
    warnings: tuple[str, ...]
    output_files: tuple[str, ...]


def _has_wikilink(content: str, target: str) -> bool:
    pattern = rf"\[\[\s*{re.escape(target)}(?:[|#][^\]]*)?\s*\]\]"
    return re.search(pattern, content, flags=re.IGNORECASE) is not None


def classify_note(filename: str, content: str) -> str | None:
    if filename.casefold().startswith("quiz"):
        return "Quizzes"
    if _has_wikilink(content, "Multistep") or re.search(
        r"\bmulti-step\b", content, flags=re.IGNORECASE
    ):
        return "Quizzes"
    for folder, aliases in (
        ("Calculus I", ("Calculus I", "Calculus")),
        ("Precalculus", ("Precalculus",)),
        ("Algebra II", ("Algebra II",)),
    ):
        if any(_has_wikilink(content, alias) for alias in aliases):
            return folder
    return None


def _split_wikilink(value: str) -> tuple[str, str]:
    target_with_alias = value.split("#", 1)[0]
    target, separator, alias = target_with_alias.partition("|")
    target = target.strip()
    return target, alias.strip() if separator else target


def _image_targets(content: str) -> tuple[str, ...]:
    targets: list[str] = []
    for match in EMBED_RE.finditer(content):
        target, _ = _split_wikilink(match.group(1))
        if Path(target).suffix.casefold() in IMAGE_SUFFIXES:
            targets.append(Path(target).name)
    return tuple(dict.fromkeys(targets))


def _resolve_screenshot(images_dir: Path, target: str) -> Path | None:
    basename = Path(target).name
    if target != basename or not basename.startswith(SCREENSHOT_PREFIXES):
        return None
    candidate = images_dir / basename
    if not candidate.exists() or not candidate.is_file() or candidate.is_symlink():
        return None
    if candidate.resolve().parent != images_dir.resolve():
        return None
    return candidate


def _render_markdown(
    content: str,
    note_links: dict[str, str],
    image_links: dict[str, str],
) -> tuple[str, tuple[str, ...]]:
    warnings: list[str] = []

    def replace_embed(match: re.Match[str]) -> str:
        target, label = _split_wikilink(match.group(1))
        basename = Path(target).name
        if basename in image_links:
            return f"![]({image_links[basename]})"
        if Path(target).suffix.casefold() in IMAGE_SUFFIXES:
            return label
        if target in note_links:
            return f"[{label}]({note_links[target]})"
        warnings.append(f"Unpublished or rejected embed: {target}")
        return label

    def replace_link(match: re.Match[str]) -> str:
        target, label = _split_wikilink(match.group(1))
        if target in note_links:
            return f"[{label}]({note_links[target]})"
        return label

    rendered = EMBED_RE.sub(replace_embed, content)
    return WIKILINK_RE.sub(replace_link, rendered), tuple(warnings)


def _scan_notes(math_dir: Path) -> tuple[list[Note], list[str]]:
    notes: list[Note] = []
    skipped: list[str] = []
    for source in sorted(math_dir.glob("*.md"), key=lambda path: path.name.casefold()):
        if source.is_symlink() or not source.is_file():
            continue
        content = source.read_text(encoding="utf-8")
        folder = classify_note(source.name, content)
        if folder is None:
            skipped.append(source.name)
        else:
            notes.append(Note(source, source.stem, folder, content))
    return notes, skipped


def _note_links(notes: list[Note], current: Note) -> dict[str, str]:
    links: dict[str, str] = {}
    for note in notes:
        target = Path(note.folder) / note.source.name
        relative = os.path.relpath(target, current.folder).replace(os.sep, "/")
        links[note.title] = "/".join(quote(part) for part in relative.split("/"))
    return links


def _readme(notes: list[Note]) -> str:
    lines = [
        "# Math Notes",
        "",
        (
            "Public notes from Algebra II, Precalculus, and Calculus I. "
            "On the Math Academy Calculus I track, synced from Obsidian Vault daily."
        ),
        "",
    ]
    for folder in NOTE_FOLDERS:
        lines.extend((f"## {folder}", ""))
        for note in (candidate for candidate in notes if candidate.folder == folder):
            target = f"{quote(folder)}/{quote(note.source.name)}"
            lines.append(f"- [{note.title}]({target})")
        lines.append("")
    return "\n".join(lines)


def build_publication(math_dir: Path, images_dir: Path, stage: Path) -> Report:
    if stage.exists():
        raise ValueError(f"Stage already exists: {stage}")
    if not math_dir.is_dir() or not images_dir.is_dir():
        raise ValueError("Math and image sources must be directories")
    stage.mkdir(parents=True)
    for folder in (*NOTE_FOLDERS, "assets"):
        (stage / folder).mkdir()

    notes, skipped = _scan_notes(math_dir)
    selected_images: dict[str, Path] = {}
    warnings: list[str] = []
    for note in notes:
        for target in _image_targets(note.content):
            resolved = _resolve_screenshot(images_dir, target)
            if resolved is None:
                warnings.append(
                    f"{note.source.name}: rejected or missing image {target}"
                )
            else:
                selected_images[resolved.name] = resolved

    for basename, source in selected_images.items():
        shutil.copy2(source, stage / "assets" / basename)

    for note in notes:
        image_links = {
            target: f"../assets/{quote(target)}"
            for target in _image_targets(note.content)
            if target in selected_images
        }
        rendered, note_warnings = _render_markdown(
            note.content,
            _note_links(notes, note),
            image_links,
        )
        rendered = "\n".join(line.rstrip() for line in rendered.splitlines()).rstrip()
        rendered += "\n"
        warnings.extend(f"{note.source.name}: {item}" for item in note_warnings)
        (stage / note.folder / note.source.name).write_text(
            rendered,
            encoding="utf-8",
        )

    (stage / "README.md").write_text(_readme(notes), encoding="utf-8")
    validate_stage(stage)
    classified = {
        folder: tuple(note.source.name for note in notes if note.folder == folder)
        for folder in NOTE_FOLDERS
    }
    output_files = tuple(
        path.relative_to(stage).as_posix()
        for path in sorted(stage.rglob("*"))
        if path.is_file()
    )
    return Report(
        classified=classified,
        skipped=tuple(skipped),
        screenshots=tuple(sorted(selected_images)),
        warnings=tuple(warnings),
        output_files=output_files,
    )


def validate_stage(stage: Path) -> None:
    root = stage.resolve()
    for path in stage.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Symlink rejected: {path}")
        resolved = path.resolve()
        if resolved != root and root not in resolved.parents:
            raise ValueError(f"Path escapes staging directory: {path}")
        relative = path.relative_to(stage)
        top = relative.parts[0]
        if len(relative.parts) == 1:
            if path.is_file() and path.name != "README.md":
                raise ValueError(f"Unexpected root file: {path}")
            if path.is_dir() and top not in (*NOTE_FOLDERS, "assets"):
                raise ValueError(f"Unexpected root directory: {path}")
        elif top in NOTE_FOLDERS:
            if path.is_file() and path.suffix.casefold() != ".md":
                raise ValueError(f"Unexpected note type: {path}")
        elif top == "assets":
            if path.is_file() and not path.name.startswith(SCREENSHOT_PREFIXES):
                raise ValueError(f"Unexpected asset: {path}")
        else:
            raise ValueError(f"Unexpected output path: {path}")


def _owned_snapshot(root: Path) -> dict[str, bytes]:
    snapshot: dict[str, bytes] = {}
    for name in OWNED_PATHS:
        target = root / name
        if target.is_file():
            snapshot[name] = target.read_bytes()
        elif target.is_dir():
            for path in target.rglob("*"):
                if path.is_file():
                    snapshot[path.relative_to(root).as_posix()] = path.read_bytes()
    return snapshot


def sync_owned_output(stage: Path, repository: Path) -> bool:
    validate_stage(stage)
    repository = repository.resolve()
    if repository == Path(repository.anchor):
        raise ValueError("Filesystem root cannot be a repository destination")
    if not (repository / ".git").is_dir():
        raise ValueError(f"Destination is not a Git checkout: {repository}")
    if _owned_snapshot(stage) == _owned_snapshot(repository):
        return False
    for name in OWNED_PATHS:
        target = repository / name
        if target.is_symlink():
            raise ValueError(f"Owned output path is a symlink: {target}")
        if target.is_dir():
            shutil.rmtree(target)
        elif target.exists():
            target.unlink()
    for folder in (*NOTE_FOLDERS, "assets"):
        shutil.copytree(stage / folder, repository / folder)
    shutil.copy2(stage / "README.md", repository / "README.md")
    return True


def _print_report(report: Report) -> None:
    for folder, names in report.classified.items():
        print(f"\n[{folder}] ({len(names)})")
        for name in names:
            print(name)
    print(f"\n[Skipped] ({len(report.skipped)})")
    for name in report.skipped:
        print(name)
    print(f"\n[Screenshots] ({len(report.screenshots)})")
    for name in report.screenshots:
        print(name)
    print(f"\n[Warnings] ({len(report.warnings)})")
    for warning in report.warnings:
        print(warning)
    print(f"\n[Public files] ({len(report.output_files)})")
    for name in report.output_files:
        print(name)


def _git(repository: Path, *arguments: str, capture: bool = False):
    return subprocess.run(
        ("git", "-C", str(repository), *arguments),
        check=True,
        text=True,
        capture_output=capture,
    )


def fast_forward(repository: Path) -> None:
    status = _git(repository, "status", "--porcelain", capture=True).stdout
    if status:
        raise RuntimeError("Repository has uncommitted changes")
    _git(repository, "pull", "--ff-only")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--math-dir", type=Path, required=True)
    parser.add_argument("--images-dir", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-push", action="store_true")
    args = parser.parse_args(argv)
    repository = Path(__file__).resolve().parents[1]
    if not args.dry_run:
        fast_forward(repository)

    with tempfile.TemporaryDirectory(prefix="math-notes-publisher-") as temporary:
        stage = Path(temporary) / "stage"
        report = build_publication(args.math_dir, args.images_dir, stage)
        _print_report(report)
        if args.dry_run:
            return 0
        if not sync_owned_output(stage, repository):
            print("\nNo generated changes.")
            return 0
        _git(repository, "add", "--", *OWNED_PATHS)
        _git(repository, "diff", "--cached", "--check")
        _git(
            repository,
            "commit",
            "-m",
            f"math notes sync: {date.today().isoformat()}",
        )
        if not args.no_push:
            _git(repository, "push", "origin", "HEAD")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
