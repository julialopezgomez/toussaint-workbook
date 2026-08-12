# Project State — Toussaint Workbook

## Current phase
**Phase 3 complete: both pilot modules (ML-03, KIN-02) built, self-tested, and approved by the user (style/depth confirmed acceptable, bugs found and fixed). Repository is public on GitHub. Ready to scope the first real batch for Phase 4, pending user input on batch size/order.**

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

## Resolved after user review of the pilot (2026-08-12, third pass)
- **Real bug found and fixed**: `rehype-katex` bundled its own separate copy of KaTeX (0.16.47) distinct from the directly-installed one (0.18.4), and the two versions use different CSS class-naming conventions (`sizing` vs `katex-sizing`). Build-time-rendered math (all MDX prose, including the cheat sheet's equation table and part of ML-03's own worked example) was rendering with unscaled sub/superscripts as a result, since `katex.min.css` only matched one of the two conventions. Fixed via an `npm overrides` pin (`"katex": "$katex"`) forcing a single KaTeX version across the whole dependency tree, confirmed with a full clean reinstall (deleted `node_modules`/`package-lock.json`). Verified fixed on both the cheat sheet and ML-03 pages; production build still succeeds.
- Root cause of the user's other report (raw `$...$` text, dead buttons) was confirmed to be opening the `.mdx` source file directly (`file://`) instead of through the dev server, not a real defect. `README.md` added with explicit "don't double-click the file" setup/run instructions.
- **Progress export/import UI added**: `store.ts`'s `exportProgress`/`importProgress` functions existed since the pilot build but had no UI. Added `src/components/ProgressControls.astro` (download-as-JSON / upload-to-restore) on the homepage, plus a "Where your answers live" explainer (IndexedDB, browser-local, never touches git-tracked files). Export tested live and works; import wasn't independently exercised with a real file upload in the automated browser tool (same class of limitation as the earlier clipboard-copy caveat), but the code path is small and symmetric with the tested export path.
- **Local git repo initialized** at `workbook/` (not the parent folder), so the source PDFs (`../original notes/`) are structurally outside the repo entirely. `.gitignore` additionally excludes `data/source-manifest/raw-text/` and `html-text/` (full extracted text of Toussaint's copyrighted lecture notes) even though they're inside `workbook/`. Initial commit made, 38 files, no remote configured yet, nothing pushed anywhere.
- Style note from user: avoid em/en-dash asides going forward, prefer colons/semicolons/commas/parentheses. Applying from here on.

## Resolved (2026-08-12, fourth pass): repo made public, KIN-02 built
- **Repository is now public**: `https://github.com/julialopezgomez/toussaint-workbook`, at user's explicit request. See `docs/decisions/0003-public-repo.md`. README has a prominent "Credit and source material" section attributing Marc Toussaint with a link to his teaching page, before anything was pushed.
- **KIN-02 (Quaternions: Exponential/Log Maps, Interpolation & Jacobians) built as the second pilot module**, full-length per the Phase 2 plan (user's confirmed weak spot). 5 exercises (short-text/derivation/symbolic/numeric/proof), all worked-example and exercise numbers independently verified with NumPy (including a finite-difference check on the angular Jacobian) before writing them into the lesson. Tested live: numeric checker ✓, symbolic checker (including a different valid algebraic form, `(1-q0**2)**0.5` vs `sqrt(1-q0**2)`) ✓, KaTeX rendering (174 spans) ✓. Production build clean, 4 pages.
- **Real bug found and fixed**: after adding KIN-02, the dev server briefly served an empty `<article>` for its page. Traced to leftover duplicate `astro dev` processes from earlier in the session competing for/rebinding ports; NOT a content or code bug (the production build had rendered KIN-02 correctly the whole time). Fixed by fully clearing all stale processes on ports 4321-4325 before restarting. Worth remembering for future sessions: always `lsof -ti:<port> | xargs kill -9` before restarting the dev server if multiple restarts have happened in one session.

## Pending — next action needed from user
- **Scope batch 1 of Phase 4.** Both pilot modules are approved and pushed; the two-module-at-a-time pace doesn't scale to ~61 remaining modules. Before generating more content unsupervised, propose a concrete batch (e.g. "finish Block MATH, 5 modules" or "finish Block KIN, 1 more module") and confirm size/order with the user rather than silently producing the whole curriculum. Default recommendation if not specified: proceed block-by-block in the Tier-1 main-route order from `CURRICULUM.md`, starting with the rest of Block MATH (foundational, blocks everything else), in batches of roughly 4-6 modules with a validation/report checkpoint after each, per the original spec's batch-production process.
- Confirm the Review-with-Claude clipboard button and the progress-import file upload actually work for the user (neither could be verified in the automated browser testing tool).

## Known uncertainties
- ~598 pages of the 4 large lecture PDFs were not visually spot-checked as rendered images: deferred to per-module authoring time, per `AUDIT_REPORT.md` §6.
- Cross-reference numbers (`\ref`/`\eqref`) extract as `??` in PDF text: resolve against the live PDF when a module cites them (not needed for ML-03 or KIN-02, both of which drew from sources without such references, or from HTML-sourced notes).
- Review-with-Claude clipboard behavior and progress-import file upload: unverified in a real browser (see above).

## Validation status
- Extraction pipeline: clean, 0 errors, 13/13 sources.
- Astro type check (`npx astro check`): 0 errors.
- Production build: succeeds, 4 pages (index, ML-03, KIN-02, 1 cheatsheet).
- Manual + automated interaction testing across both modules: numeric checker ✓, symbolic checker (live SymPy round-trip, including alternate algebraic forms) ✓, rubric/attempt flow ✓, IndexedDB progress ✓, KaTeX rendering (correct `katex-sizing` classes and 0.7em scaling after the dedup fix) ✓, cheat sheet page ✓, homepage ✓, progress export ✓. Clipboard copy and progress import: not independently exercised in the automated browser tool; user should verify both themselves.
- Git: public repo at `https://github.com/julialopezgomez/toussaint-workbook`, 5 commits, source PDFs and extracted text excluded throughout.

## Next exact action
Propose and confirm the scope of Phase 4 batch 1 with the user (see "Pending" above), then produce that batch, validate it, and report before starting the next one.
