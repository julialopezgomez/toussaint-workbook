"""Fetch the HTML twins of the 7 short lecture notes from Toussaint's teaching site.

These pages are hand-authored with real MathJax/LaTeX source ($...$, \\[...\\]),
which is strictly more reliable for exact math transcription than text reconstructed
from the PDF's embedded glyph layout. Read-only against the external site; writes
only into this project's data/source-manifest/ directory.

Run: .venv/bin/python scripts/ingest/fetch_html_notes.py
"""
import json
import re
import urllib.request
from pathlib import Path

from bs4 import BeautifulSoup

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MANIFEST_DIR = PROJECT_ROOT / "data" / "source-manifest"
HTML_TEXT_DIR = MANIFEST_DIR / "html-text"

# (source_id, url filename) -- filenames are case-sensitive on the server
NOTES = [
    ("energy", "energy"),
    ("entropy", "entropy"),
    ("gaussians", "gaussians"),
    ("quaternions", "quaternions"),
    ("robotkin", "robotKin"),
    ("splines", "splines"),
    ("svd", "svd"),
]

BASE = "https://www.user.tu-berlin.de/mtoussai/notes/"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="replace")


def clean_article(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    article = soup.find("section", class_="page__content") or soup.find("article")
    if article is None:
        return ""
    for tag in article.find_all(["script", "style"]):
        tag.decompose()
    return article.get_text("\n", strip=True)


def main():
    HTML_TEXT_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    for source_id, fname in NOTES:
        url = f"{BASE}{fname}.html"
        print(f"Fetching {url} ...")
        html = fetch(url)
        text = clean_article(html)
        out_path = HTML_TEXT_DIR / f"{source_id}.md"
        out_path.write_text(f"<!-- source_id: {source_id}, fetched from: {url} -->\n\n{text}", encoding="utf-8")
        math_blocks = len(re.findall(r"\\\[", text))
        inline_math = len(re.findall(r"\$[^$]+\$", text))
        results.append({
            "source_id": source_id,
            "html_url": url,
            "html_text_file": str(out_path.relative_to(PROJECT_ROOT)),
            "display_math_blocks": math_blocks,
            "inline_math_spans": inline_math,
            "char_count": len(text),
        })

    index_path = MANIFEST_DIR / "html-sources.json"
    index_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\nWrote {len(results)} HTML-sourced notes -> {HTML_TEXT_DIR}")
    print(f"Index -> {index_path}")


if __name__ == "__main__":
    main()
