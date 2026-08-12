# Decision Record 0002 — Phase 2 Approval & Pilot Kickoff

Date: 2026-08-12

## Phase 2 approval
User approved `data/curriculum/CURRICULUM.md` and `data/curriculum/ARCHITECTURE.md` as proposed, no restructuring requested ("3. all good").

Three open sub-decisions from the Phase 2 proposal, resolved:
1. **Pilot module choice**: user answered "either or both." Decision: build ML-03 first (Neural Networks: Manual Forward/Backward Pass ↔ PyTorch) since it most directly answers the Phase 0 request and exercises every pilot requirement in the spec (derivation, worked example, numeric + symbolic exercise, tiered hints, PyTorch cross-check, cheat-sheet link, mastery check). KIN-02 (quaternions) queued as the second pilot-style module once ML-03's approach is confirmed, rather than building both simultaneously and risking a diluted review.
2. **Symbolic grading**: user chose full automation ("more automated with sympy where possible") over the simpler rubric-only fallback. Implemented as a local Flask server (`scripts/grading/sympy_server.py`, localhost-only, no auth) that the site calls via `fetch` when a `symbolic` exercise is checked.
3. **ODE external source**: still not picked — non-blocking, deferred to when Block ODE is actually authored (Phase 4).

## Pilot build (Phase 3)
Full technical detail in `PROJECT_STATE.md` "Completed — Phase 3." Key point for future reference: two non-obvious Astro/MDX bugs were hit and fixed, unrelated to content:
- `@astrojs/mdx`'s `remarkPlugins`/`rehypePlugins` options are deprecated and silently inert in this Astro version (7.2.1) — plugins must be passed via `markdown.processor: unified({...})` in `astro.config.mjs` instead, which `@astrojs/mdx` then inherits.
- `remark-math` is required for more than rendering: MDX's JSX parser treats raw `{` `}` in prose as embedded JS expressions, and LaTeX like `\dfrac{a}{b}` breaks that parser unless `remark-math` intercepts the math span first. This applies only to MDX prose — JSON-sourced exercise text never goes through the MDX parser and is rendered via client-side KaTeX auto-render instead.

Two content-adjacent bugs were also caught by self-testing before this went to the user:
- The symbolic-equivalence checker's initial implementation (`sympy.simplify(diff) == 0`) failed on a numerically-equal expression in a different functional form. Fixed by switching to numeric sampling as the primary check.
- Progress was initially only recorded on correct answers, contradicting the "attempted-work-based, not correctness-gated" progress-tracking requirement from the original spec. Fixed.

## Status
Pilot built, self-tested (numeric/symbolic/rubric grading flows, IndexedDB progress, KaTeX rendering, production build all verified working). Awaiting user's own review of the pedagogical style/depth and a manual check of the Review-with-Claude clipboard behavior (couldn't be confirmed in the sandboxed browser testing tool) before proceeding to KIN-02 and then Phase 4 batch production.
