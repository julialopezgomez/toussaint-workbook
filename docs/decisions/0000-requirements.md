# Decision Record 0000 — Requirements (Phase 0)

Date: 2026-08-12

## Paths
- `VAULT_ROOT`: `/Users/julialg2002/PhD-Literature` (contains active `.obsidian`)
- `PDF_SOURCE_DIR`: `/Users/julialg2002/PhD-Literature/Courses/Marc Toussaint's Robot and ML Stack/original notes`
- `PROJECT_DIR`: `/Users/julialg2002/PhD-Literature/Courses/Marc Toussaint's Robot and ML Stack/workbook`
- `CONTENT_OUTPUT_DIR`: `/Users/julialg2002/PhD-Literature/Courses/Marc Toussaint's Robot and ML Stack/generated-notes` (not yet created — will be created only if/when Obsidian-readable notes are actually generated)
- A second, unrelated Obsidian vault exists at `/Users/julialg2002/Documents/Obsidian Vault` — explicitly out of scope, never touched.

## Obsidian access
`KNOWLEDGE_BASE_INCLUDE`: user said "feel free to inspect anything" but specifically named Literature Notes, Implementations, Courses, PhD_Daily, Steve, Presentations as useful for context (papers being read, writing style, daily activity). `KNOWLEDGE_BASE_EXCLUDE`: none explicitly named. Constraint: the workbook must stay **independent** — inspection for calibration/context is fine, but the workbook should not be built to depend on or deep-link into vault content. Link style not yet exercised in practice; default remains Obsidian `[[wikilink]]` with relative paths unless contradicted.

## Background (self-reported, verbatim intent preserved)
- Linear algebra & calculus: rusty, needs step-by-step reminders to compute again, not just notation review.
- Programming: strong Python, ~no C/C++.
- Optimization/control/RL: basics only, no mastery.
- ODEs/dynamics: weakest area, wants manual-first then scale-up pedagogy.
- ML: has done a lot before, but wants to relearn manual MLP forward/backward computation matched line-by-line to PyTorch.
- Overall goal: derive things properly, not just recognize formulas. Full detail in memory file `user_math_ml_background.md` (project-external persistent memory).

## Timeline & usage
- No deadline, no fixed weekly hours — show estimated hours per module.
- Fully private, local-first. No deployment, no accounts, no API keys in v1.

## Grading
- No API-based auto-grading chosen (explained to user: would need a paid Anthropic API key in a local server env var; skipped given local/private scope).
- Default stack: deterministic checks (MCQ/numeric/code tests) → SymPy symbolic equivalence where reliable → rubric self-assessment + clipboard-based "Review with Claude" (no API key).

## External sourcing
Approved, unconditionally. Candidate texts named by user: Sutton & Barto (RL — user's own PhD report also cites this directly, independent confirmation), Lynch & Park *Modern Robotics*, and Siciliano et al. *Robotics: Modelling, Planning and Control* (user confirmed "Severiano's" = Siciliano). Otherwise, use judgment for comprehensiveness and fit. Source-only curriculum pass must complete first (done — see Phase 1 audit); external material must be cited separately from Toussaint-derived material.

## Output format
Both: interactive Astro+TypeScript site (primary) and printable/book export (print CSS + optional compiled PDF), per original architecture defaults. Not print-first, so no Astro-vs-Quarto/Jupyter-Book comparison was triggered.

## Status
All Phase 0 items resolved. See `0001-corpus-update-and-priorities.md` for the second-pass corpus addition and priority-tier corrections made after this record was written.
