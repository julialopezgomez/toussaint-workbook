"""Reproducible, read-only extraction pass over the Toussaint PDF source corpus.

Reads each PDF in PDF_SOURCE_DIR, never writes to it. Produces, per source:
  - data/source-manifest/raw-text/<id>.md   (page-boundary-preserved extracted text)
  - data/source-manifest/manifest.json      (one entry per source: hash, pages, TOC, metadata, quality heuristics)

Run: .venv/bin/python scripts/ingest/extract_pdfs.py
"""
import hashlib
import json
import re
import sys
from pathlib import Path

import fitz  # PyMuPDF

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = PROJECT_ROOT.parent / "original notes"
MANIFEST_DIR = PROJECT_ROOT / "data" / "source-manifest"
RAW_TEXT_DIR = MANIFEST_DIR / "raw-text"


def source_id(filename: str) -> str:
    stem = Path(filename).stem
    return re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_one(pdf_path: Path) -> dict:
    sid = source_id(pdf_path.name)
    doc = fitz.open(pdf_path)
    n_pages = doc.page_count
    meta = doc.metadata or {}
    toc = doc.get_toc(simple=True)  # [[level, title, page], ...]

    page_char_counts = []
    lines = [f"# {pdf_path.name}", f"<!-- source_id: {sid} -->", ""]
    for i in range(n_pages):
        page = doc.load_page(i)
        text = page.get_text("text")
        page_char_counts.append(len(text.strip()))
        lines.append(f"\n\n===== PAGE {i + 1} =====\n")
        lines.append(text)
    doc.close()

    RAW_TEXT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RAW_TEXT_DIR / f"{sid}.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")

    avg_chars = sum(page_char_counts) / max(n_pages, 1)
    low_text_pages = [i + 1 for i, c in enumerate(page_char_counts) if c < 40]
    likely_scanned = avg_chars < 40  # heuristic: near-empty extraction => image-based page

    return {
        "source_id": sid,
        "filename": pdf_path.name,
        "relative_path": str(pdf_path.relative_to(PROJECT_ROOT.parent)),
        "sha256": sha256_of(pdf_path),
        "page_count": n_pages,
        "pdf_metadata": {
            "title": meta.get("title") or None,
            "author": meta.get("author") or None,
            "subject": meta.get("subject") or None,
            "creation_date": meta.get("creationDate") or None,
            "mod_date": meta.get("modDate") or None,
            "producer": meta.get("producer") or None,
        },
        "embedded_toc": [{"level": lvl, "title": title, "page": pg} for lvl, title, pg in toc],
        "extraction": {
            "avg_chars_per_page": round(avg_chars, 1),
            "low_text_page_count": len(low_text_pages),
            "low_text_pages": low_text_pages,
            "likely_scanned_or_image_pages": likely_scanned,
            "raw_text_file": str(out_path.relative_to(PROJECT_ROOT)),
        },
    }


def main():
    if not SOURCE_DIR.is_dir():
        print(f"Source dir not found: {SOURCE_DIR}", file=sys.stderr)
        sys.exit(1)

    pdfs = sorted(SOURCE_DIR.glob("*.pdf"))
    if not pdfs:
        print(f"No PDFs found in {SOURCE_DIR}", file=sys.stderr)
        sys.exit(1)

    manifest = []
    for pdf_path in pdfs:
        print(f"Extracting {pdf_path.name} ...")
        manifest.append(extract_one(pdf_path))

    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    manifest_path = MANIFEST_DIR / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"\nWrote manifest for {len(manifest)} sources -> {manifest_path}")


if __name__ == "__main__":
    main()
