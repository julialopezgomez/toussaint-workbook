# Project State — Toussaint Workbook

## Current phase
**Phase 3 (pilot module) built and self-tested end-to-end. Awaiting user review of the pedagogical style and interaction design before Phase 4 (batch production).**

## Approved decisions
See `docs/decisions/0000-requirements.md`, `0001-corpus-update-and-priorities.md`, `0002-phase2-and-pilot-approval.md` for full records. Summary:
- Paths: `VAULT_ROOT=/Users/julialg2002/PhD-Literature`, `PDF_SOURCE_DIR=../original notes`, `PROJECT_DIR=workbook/`, `CONTENT_OUTPUT_DIR=../generated-notes/`.
- Fully private/local, no deployment, no API keys.
- Grading: deterministic (client-side) + symbolic via a **local SymPy sidecar server** (user chose full automation over rubric-only fallback) + rubric self-check + clipboard "Review with Claude".
- External sourcing finalized: Sutton & Barto, Lynch & Park *Modern Robotics*, Siciliano et al. *Robotics: Modelling, Planning and Control*.
- Output: both interactive Astro site and printable/book export.
- No deadline; estimated hours per module instead.
- User background: rusty calculus/linear algebra (step-by-step re-derivation needed), no C/C++, strong Python, basics-only in optimization/control/RL, weakest in ODEs/dynamics, wants manual MLP↔PyTorch bridge. Strong (not rusty) in open-chain kinematics/Jacobians/rotations (Edinburgh teaching background) — paced as revision except quaternions (confirmed weak spot, full-length).
- User's PhD research (CDT-D2AIR Year-1 report): "Learning Representations of Reachable Behaviour for Planning in Long-Horizon Robotics Tasks," supervised by Dr. Steve Tonneau — TAMP, trajectory optimization/optimal control, MPC, predictive/world models, RL, goal-conditioned policies, manifold/constrained sampling. Full detail in memory `toussaint_workbook_project.md`.
- Priority tiers confirmed (`AUDIT_REPORT.md` §6b): grasping/legged locomotion elevated; SLAM demoted to reference-only; propositional/first-order logic + PDDL/MLN elevated (scoped to TAMP); tree search kept as MCTS prerequisite; general CSP-solving low priority.
- Curriculum (`data/curriculum/CURRICULUM.md`, 13 blocks/~63 modules) and architecture (`data/curriculum/ARCHITECTURE.md`) approved as proposed, no changes requested.
- Pilot module: **ML-03** (Neural Networks: Manual Forward/Backward Pass ↔ PyTorch) built first; KIN-02 (quaternions) is next once ML-03's style is approved.

## Completed — Phase 3 (pilot)
- **Astro + TypeScript site scaffolded** at `workbook/` (merged into existing project files, nothing overwritten). MDX, KaTeX (build-time via `remark-math`/`rehype-katex` through `markdown.processor`, client-side via `katex/contrib/auto-render` for JSON-sourced exercise text).
- **Content collections** (`src/content.config.ts`): `course`, `questions`, `solutions`, `cheatsheets`, matching `ARCHITECTURE.md`'s schemas. Custom multi-entry JSON loader written for `questions`/`solutions` (one file per module containing an array — the built-in `file()` loader doesn't support that shape).
- **ML-03 authored in full**: motivation, objectives, prereq readiness check, notation box, worked example (forward + backward pass, hand-verified numbers), 6 exercises spanning short-text/derivation/symbolic/numeric/code/proof answer types, summary, retrieval questions, mastery checklist, source citations. Citations distinguish source-adapted (2 exercises, from `lecture-maths` Ex.4/5, original numbering preserved) from newly-authored (rest).
- **All worked-example and exercise numbers independently verified**: NumPy analytic + numeric-gradient-check, cross-checked against real PyTorch `autograd` output (installed CPU-only PyTorch in `.venv` for this) — every number in the lesson matches to float32 precision.
- **Grading components built and tested live**: `ExerciseCard.astro` dispatches by answer type. Deterministic numeric checker tested (correct + incorrect). Symbolic checker tested against the running local SymPy server via a real browser fetch (correct exact match, correct equivalent-but-differently-shaped match, correct rejection). Rubric "I've attempted this" flow tested. Review-with-Claude clipboard button implemented; clipboard write itself couldn't be confirmed in this sandboxed browser tool (likely environment permission issue, not a code defect) — **user should verify this one interaction themselves**.
- **Bug found and fixed during testing**: `sympy.simplify()` alone failed to recognize a numerically-equal-but-differently-shaped expression (`exp(-z)/(1+exp(-z))**2` vs `1/(4*cosh(z/2)**2)`) as equivalent. Fixed by switching the symbolic checker to numeric sampling at 25 random points as the primary equivalence test.
- **Bug found and fixed during testing**: progress was only being recorded on *correct* answers, contradicting the "attempted-work-based progress" requirement. Fixed — any genuine (non-empty) attempt now records progress and unlocks the solution, regardless of correctness.
- **Progress storage** (`src/lib/progress/store.ts`, IndexedDB) tested live: attempts recorded correctly for both pass/fail cases, module status auto-derived to "in-progress".
- **Cheat sheet** (`neural-networks-backprop`) authored and linked bidirectionally from ML-03.
- **Production build verified**: `npm run build` succeeds cleanly, 3 static pages, 0 errors.
- Two real bugs were also hit and fixed purely from getting the toolchain working (not content bugs): Astro 7's `mdx({remarkPlugins})` is silently deprecated/non-functional — plugins must go through `markdown.processor`; and raw LaTeX braces in MDX prose need `remark-math` specifically to avoid being misparsed as JSX expressions, not just for rendering.

## Pending — user review of the pilot
- Read `src/content/course/ML/ML-03.mdx` at `http://localhost:4321/course/ML/ML-03` (dev server: `npm run dev`; symbolic checking needs `npm run grading-server` running too) and confirm: pedagogical style, exercise difficulty/tiering, hint quality, whether the manual-derivation depth matches what you actually want.
- Confirm the Review-with-Claude clipboard button actually copies for you (couldn't be verified in the automated browser tool).
- Once approved: build **KIN-02** (quaternions) as the second pilot-style module, per your Phase 2 "either or both" answer, then move to Phase 4 batch production.

## Known uncertainties
- ~598 pages of the 4 large lecture PDFs were not visually spot-checked as rendered images — deferred to per-module authoring time, per `AUDIT_REPORT.md` §6.
- Cross-reference numbers (`\ref`/`\eqref`) extract as `??` in PDF text — resolve against the live PDF when a module cites them (not needed for ML-03, which drew from `lecture-maths` pages without such references, and from HTML-sourced short notes).
- Review-with-Claude clipboard behavior unverified in a real browser (see above).

## Validation status
- Extraction pipeline: clean, 0 errors, 13/13 sources.
- Astro type check (`npx astro check`): 0 errors.
- Production build: succeeds, 3 pages.
- Manual + automated interaction testing: numeric checker ✓, symbolic checker (live SymPy round-trip) ✓, rubric/attempt flow ✓, IndexedDB progress ✓, KaTeX rendering (132 spans confirmed rendered) ✓, cheat sheet page ✓, homepage ✓. Clipboard copy: untested (see above).

## Next exact action
Wait for user review of the ML-03 pilot (style/depth/interaction approval), then build KIN-02 as the second pilot module, then move to Phase 4 (batch production) once both are approved.
