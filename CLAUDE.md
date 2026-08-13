# CLAUDE.md — Toussaint Workbook

Local-first learning workbook built from Marc Toussaint's TU Berlin course PDFs. The source code and authored content live in a **private** git repo (briefly made public, then reverted, see `docs/decisions/0003-public-repo.md`); the site itself is also local-only, no hosted/deployed version. Because the repo is private, actual figures from the source PDFs are embedded directly where they help (not just original redrawn diagrams) — this was an explicit tradeoff made contingent on staying private, so **do not make this repo public again without re-checking that decision with the user first**, since it would put copyrighted figures into public distribution. Full context in `PROJECT_STATE.md` (resumable ledger) and `docs/decisions/` (decision records). Read those before making changes if resuming after a gap.

## Non-negotiable rules

1. **Source PDFs are read-only, always.** `../original notes/` (never move, rename, overwrite, or edit) and are never committed to the repo. Same for any Obsidian vault content under `VAULT_ROOT` (read-only, inspect only within folders the user has approved).
2. **No content generation ahead of an approval gate.** Gates: (1) requirements + source audit, (2) curriculum + architecture, (3) pilot module, (4) batch production, (5) final QA. Each ends with a report and an explicit wait for user approval; do not skip ahead, even if the next step seems obvious.
3. **No API keys, no hosted deployment, no accounts, no analytics, no database** in this project, ever, unless the user explicitly reverses that decision in a new decision record. (The repo being public is a separate decision from deployment; see `docs/decisions/0003-public-repo.md`, it does not reverse this rule.)
4. **Every source-derived claim, equation, example, or exercise must cite `filename + page range`, with a visible provenance tag** (source-adapted / newly-authored / external-sourced) since the content is now public: see the README's "Credit and source material" section, which every module's citations must stay consistent with.
5. **No exercise solutions exist in the source corpus.** Every rubric/solution/answer key in this workbook is newly authored: mark it as such, don't imply it came from Toussaint's materials.
6. **Don't show a complete solution before an attempt** unless the user explicitly asks.
7. **Full extracted text of the source PDFs never gets committed**, even though the workbook content derived from them does. `data/source-manifest/raw-text/` and `html-text/` stay in `.gitignore` permanently.

## Paths
- `PDF_SOURCE_DIR`: `../original notes/`
- `VAULT_ROOT`: `/Users/julialg2002/PhD-Literature`
- `CONTENT_OUTPUT_DIR` (Obsidian-readable generated notes, if ever produced): `../generated-notes/`
- This directory (`workbook/`) is `PROJECT_DIR`.

## Structure
- `src/content/course/{block}/{id}.mdx` — module lesson content (frontmatter = schema in `src/content.config.ts`). Only `ML/ML-03.mdx` exists so far (pilot).
- `src/content/questions/{module-id}.json` — one file per module, `{moduleId, exercises: [...]}`. Loaded via a custom multi-entry loader (see `content.config.ts`) since one file → many collection entries.
- `src/content/solutions/{module-id}.json` — one file per module, `{solutions: [...]}`, same custom-loader pattern. Kept in a separate collection from `course`/`questions` so full solution text isn't bundled with the lesson page by default.
- `src/content/cheatsheets/{id}.mdx` — cheat sheets, bidirectionally linked from modules via `cheatsheetLinks`.
- `src/components/exercise/ExerciseCard.astro` — renders one exercise, dispatches grading by `answerType`/`checkMode` (deterministic client-side / symbolic via local SymPy fetch / rubric self-check + Review-with-Claude clipboard packet). Progress recorded to IndexedDB on any genuine attempt, regardless of correctness.
- `src/layouts/` — `BaseLayout` (KaTeX client-side auto-render, theme), `ModuleLayout`, `CheatsheetLayout`.
- `src/lib/progress/store.ts` — IndexedDB wrapper: `recordAttempt`, `getAttempts`, `exportProgress`/`importProgress` (versioned JSON).
- `labs/` — Jupyter notebooks, computational labs only (Phase 3+, none yet)
- `data/source-manifest/` — extraction pipeline output: `manifest.json`, `raw-text/*.md`, `html-text/*.md`, `AUDIT_REPORT.md`
- `data/curriculum/` — `CURRICULUM.md` (block/module structure, IDs, sources, time estimates, assessment schedule) and `ARCHITECTURE.md` (content schemas, grading design, progress storage, site structure), both from Phase 2
- `scripts/ingest/` — `extract_pdfs.py` (PDF text extraction) and `fetch_html_notes.py` (HTML/LaTeX-source fetch for the 7 short notes that have an HTML twin on Toussaint's site), both reproducible and read-only (run via `.venv/bin/python`)
- `scripts/grading/sympy_server.py` — local-only symbolic-equivalence checker (Flask, localhost:5055). Uses numeric sampling at random points as the primary equivalence test, not `sympy.simplify()` alone — plain simplify can fail to recognize equal expressions in very different forms (e.g. an `exp(...)` vs. `cosh(...)` form of the same sigmoid derivative); numeric sampling catches those the honest way, with symbolic simplify only used as an informational secondary check.
- `scripts/validate/` — quality-check scripts (Phase 4+, none yet)
- `docs/decisions/` — one file per approval gate / major decision, numbered sequentially
- `.venv/` — local Python env for the ingest + grading scripts (PyMuPDF, SymPy, Flask, NumPy, PyTorch-CPU for authoring-time verification); not for the Astro site itself
- **KaTeX note**: MDX prose renders math at build time via `remark-math`/`rehype-katex`, wired through `markdown.processor` in `astro.config.mjs` (NOT via `mdx({remarkPlugins:...})`, which is deprecated in this Astro version and silently does nothing). This is required, not just cosmetic — raw LaTeX like `\dfrac{a}{b}` contains literal `{ }` that MDX's JSX parser otherwise fails to parse. Exercise prompts/hints/solutions live in JSON, not MDX, so they never hit that parser — those render via client-side KaTeX auto-render instead (see `BaseLayout.astro`).

## Commands
- Re-run extraction (only if source PDFs change — check `manifest.json` hashes first): `npm run extract-pdfs`
- Re-fetch HTML-sourced notes: `npm run fetch-html-notes`
- Dev server: `npm run dev` (localhost:4321)
- Production build: `npm run build` → `dist/`
- Local symbolic-grading server (needed for `symbolic` answer-type exercises; optional otherwise): `npm run grading-server` (localhost:5055, local-only, no auth)
- Type check: `npx astro check`

## Content schema (to be finalized in Phase 2)
Stable content IDs must survive file reorganization. Exercise IDs follow `{source_id}-ex{N}-{subpart}` where source-derived, or `new-{topic}-{N}` where newly authored.

## Quality gates (to be implemented, Phase 4+)
Schema validity, duplicate IDs, broken internal links, missing citations, missing rubrics/solutions, orphaned source sections, invalid curriculum ordering, missing prerequisites, KaTeX rendering, code-exercise tests, numeric validator correctness, accessibility, production build.
