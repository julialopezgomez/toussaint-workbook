# Phase 2 — Technical Architecture Proposal

Astro + TypeScript, per the project defaults (no deviation triggered — output priority was "both," not print-first, so no Astro-vs-Quarto/Jupyter-Book comparison was needed). This document specifies the concrete shape: content schema, exercise/grading components, progress storage, site structure. No code is written yet — this is the design for your sign-off before the pilot module (Phase 3) implements a real slice of it.

## Folder structure (refined from `CLAUDE.md`'s placeholder layout)

```
workbook/
  src/
    content/
      course/{block}/{module-id}.mdx        # one file per module, e.g. course/ML/ML-03.mdx
      milestones/{block}-exam.mdx
      cheatsheets/{topic}.mdx
      questions/{module-id}.json             # exercise bank, separate from prose content
      solutions/{module-id}.json             # rubrics/solutions, separate so they're not visible while reading the lesson
    components/
      exercise/{MCQ,Numeric,Symbolic,Derivation,Proof,Code,Diagram}.astro
      GradingPanel.astro                     # dispatches to deterministic/symbolic/rubric checker
      ReviewWithClaude.astro                 # clipboard packet builder
      ProgressBar.astro, Roadmap.astro, PrevNext.astro
    layouts/ModuleLayout.astro, MilestoneLayout.astro, CheatsheetLayout.astro
    lib/
      grading/{deterministic.ts, symbolic.ts}  # symbolic.ts calls a local Python/SymPy sidecar (see below)
      progress/{store.ts, exportImport.ts}
      search/index.ts
    pages/                                    # thin routing layer over content collections
  public/
  data/                                       # unchanged from Phase 1: source-manifest/, curriculum/
  labs/                                       # Jupyter notebooks, Phase 3+ as needed (e.g. ODE-03 numerical integration, ML-03 PyTorch cross-check)
  scripts/{ingest,validate}/
```

Rationale for splitting `questions/`+`solutions/` from `course/`: keeps solutions out of the bundle sent to the browser for the lesson page itself (fetched only on-demand when a check/review is requested), and matches the "don't show a complete solution before an attempt" rule structurally, not just by convention.

## Content collection schemas (Zod, via Astro content collections)

**Module** (`course` collection):
```ts
{
  id: string;              // e.g. "ML-03", matches CURRICULUM.md IDs — stable across file moves
  block: string;           // "ML"
  title: string;
  tier: 1 | 2 | 3 | 4;
  estimatedHours: number;
  prerequisites: string[]; // module IDs
  objectives: string[];
  sources: {
    sourceId: string;      // matches data/source-manifest/manifest.json source_id
    pages: string;         // "p28-36"
    role: "primary" | "supplementary" | "cross-reference";
  }[];
  externalSources?: { citation: string; note: string }[];
  concepts: string[];      // feeds the concept index
  notation: { symbol: string; meaning: string }[];  // feeds the notation box + notation index
  cheatsheetLinks: string[];
  obsidianLinks?: { path: string; confidence: "high"; note: string }[];  // only high-confidence, per Phase 1 rule
  nextModules: string[];
}
```

**Exercise** (`questions` collection, separate JSON per module):
```ts
{
  id: string;               // "{module-id}-ex{N}-{subpart}" or "new-{topic}-{N}"
  moduleId: string;
  objective: string;
  provenance: "source-adapted" | "newly-authored" | "external-adapted";
  sourceRef?: { sourceId: string; page: number; originalNumber: string };
  difficulty: "foundation" | "core" | "challenge";
  estimatedMinutes: number;
  prerequisites: string[]; // other exercise IDs, if sequenced
  answerType: "mcq" | "multi-select" | "short-text" | "numeric" | "symbolic" | "derivation" | "proof" | "code" | "diagram";
  hints: [string, string, string];  // exactly 3 tiers, per spec
  reviewCardIds?: string[];         // links to the Anki-export recall bank
}
```

**Solution/rubric** (`solutions` collection, matched 1:1 by exercise ID, fetched separately — see folder rationale above):
```ts
{
  exerciseId: string;
  checkMode: "deterministic" | "symbolic" | "rubric";
  deterministic?: { expected: string | number; tolerance?: number; unit?: string };
  symbolic?: { expectedExpr: string; equivalenceNotes?: string };
  rubric?: { criteria: { points: number; description: string }[]; commonErrors: string[] };
  fullSolution: string;   // never sent to the client until requested post-attempt
}
```

**Milestone exam**: same exercise schema, plus `{ masteryThreshold: number; retakeVariantOf?: string; remediationMap: { exerciseId: string; moduleIds: string[] }[] }`.

**Cheat sheet**: `{ id, title, relatedModules: string[], sections: { heading, definitions, equations, assumptions, commonMistakes, decisionRules }[], lessonAnchors: { moduleId, anchor }[] }` — bidirectional: lesson pages get an auto-generated "cheat sheet" sidebar link from `cheatsheetLinks`, cheat sheets link back via `lessonAnchors`.

## Exercise / grading component design

Layered per spec, dispatched by `answerType`:

1. **Deterministic** (`mcq`, `multi-select`, `numeric`, some `code`): pure client-side TS, instant feedback. Numeric checks use `{expected, tolerance, unit}`; unit mismatches are flagged separately from magnitude errors so you learn which one you got wrong. `code` exercises run against a small test harness (client-side for pure functions, or a notebook cell for anything needing NumPy/PyTorch — e.g. ML-03's PyTorch cross-check).
2. **Symbolic** (`symbolic`, some `derivation`): needs actual CAS equivalence checking (e.g. is your simplified Jacobian equal to the reference one). Per spec, this needs a small local grading service — proposed: a local Python+SymPy sidecar process (`scripts/grading/sympy_server.py`, started manually via a documented `npm run grading-server` command, talking to the Astro dev server over localhost only, never deployed). Runs only when you're actively using the site locally; not a background service, not exposed to a network.
3. **Rubric + Review with Claude** (`derivation`, `proof`, `short-text`, `diagram`): self-check against the rubric's criteria list, plus a "Review with Claude" button that assembles the structured packet (module/exercise ID, question, context, your answer, rubric, and the diagnose-first-error instruction from the spec) and copies it to your clipboard — no API key, you paste it into a chat yourself.
4. **Optional future API grading**: explicitly not built in v1 per your Phase 0 decision. If you change your mind later, the `checkMode` field already has room for a fourth `"api"` mode — but this stays out of scope unless you ask for it.

## Progress storage

- **IndexedDB** (not just localStorage) for durability with structured data — one object store keyed by exercise ID, storing `{ attempts: { timestamp, answer, selfGrade?, checkResult? }[], masteryStatus, lastReviewed }`, plus a module-level store for `{ status: "not-started" | "in-progress" | "mastered", timeSpent }`.
- Progress is **attempted-work-based**, not page-view-based, per spec: a module only shows progress once at least one exercise has a recorded attempt.
- **JSON export/import**: a flat, human-readable structure mirroring the IndexedDB stores, versioned (`{ schemaVersion, exportedAt, modules: {...}, exercises: {...} }`) so it survives schema changes gracefully (older exports get migrated on import, not rejected).
- **Anki export**: generated on-demand from the `reviewCardIds` linked in each exercise, output as TSV with the fields spec calls for (definitions, assumptions, distinctions, equations-with-conditions, failure modes) — not a live sync, just a downloadable snapshot.

## Site structure & navigation

- **Start here** page: entry diagnostic → recommended sequence start.
- **Linear route**: prev/next wired directly from `prerequisites`/`nextModules` fields — the canonical path is a topological sort of the module graph honoring block order from `CURRICULUM.md`, with Tier 3/4 modules explicitly rendered as "optional branch" side-links (visually distinct, e.g. a dashed connector on the roadmap) rather than inline in the main sequence.
- **Roadmap**: a single visual graph (block-level nodes, expandable to module-level), generated from the content collection at build time — not hand-maintained separately, so it can't drift from the actual module graph.
- **Indexes**: search (client-side, e.g. Pagefind or a simple built index — decide at implementation time based on bundle-size trade-off), concept index (aggregated from every module's `concepts[]`), notation index (aggregated from `notation[]`, this doubles as the cross-course notation-unification deliverable from the spec), source index (aggregated from `sources[]`, links back into `data/source-manifest/`).
- **Print/book export**: print stylesheet for individual modules/cheat sheets (CSS `@media print`) plus a build-time concatenation script producing one printable full-course document — no separate authoring format needed since content stays in MDX either way.

## What's deliberately NOT in v1 (reaffirming Phase 0 decisions)

No database, no accounts, no analytics, no deployment, no API keys anywhere in the repo (the SymPy sidecar is local-process-only, not a hosted service). Astro's static output plus client-side IndexedDB is sufficient for a fully local, private tool.

## Open question for you

The symbolic-checking sidecar (SymPy) is the one piece that isn't "purely static Astro" — it needs Python running locally alongside the dev server when you want symbolic-equivalence checking (e.g. verifying a Jacobian derivation). Everything else (deterministic checks, rubric self-check, Review-with-Claude) works with zero extra process. Fine to proceed with this, or would you rather symbolic exercises fall back to rubric-only self-check (simpler, no sidecar, slightly less automated)?

**Resolved**: proceeded with the sidecar as proposed (`scripts/grading/sympy_server.py`, `npm run grading-server`). It's been working throughout Phase 4 exactly as designed here: local-only, manually started, numeric-sampling-first equivalence checking.

## Implementation notes (retrospective, added after Phase 4 completion, 2026-08-14)

This document was never updated during Phase 4's actual production (unlike `CURRICULUM.md`, which got a production note after every batch) — everything above is still the original Phase 2 proposal, written before a single module existed. It held up well: every schema, grading tier, and progress-storage design described above matches what actually got built, with a few things worth recording explicitly since they were decided during implementation rather than here:

- **Milestone exams** ended up reusing the existing `questions`/`solutions` collections directly (exercises filed under a synthetic `moduleId` like `MATH-EXAM`) rather than a separate exercise-storage mechanism — this wasn't specified above at all (the "Milestone exam" schema note only added `masteryThreshold`/`retakeVariantOf`/`remediationMap` on top of the base exercise schema, which is exactly what got built) but the *reuse* decision meant zero new grading code was needed for exams.
- **Cheat sheets** are one per **block** (13 total), not one per module — a explicit user decision made when cheat sheets were actually built (batch 14-15), not specified here.
- **Search**: went with Pagefind (one of the two options this document left open), indexing the production build at `npm run build` time. The real-world consequence not anticipated here: Pagefind's index doesn't exist under `npm run dev`, only under `npm run build && npm run preview` — a genuine dev-workflow wrinkle, documented in `README.md`.
- **Print/book export**: built as a single Astro page (`/print`) rendering every module via `render()` in curriculum order with print CSS, rather than "a build-time concatenation script" as worded above — same practical outcome (one printable document), simpler implementation given Astro's own static rendering already does the concatenation.
- **Anki export**: built from `notation[]` (universal, all modules) plus a curated subset of exercises with populated `reviewCardIds`, output as a build-time-generated static `.tsv` (`src/pages/anki-export.tsv.ts`, an Astro endpoint) rather than fully "on-demand" — same effect (regenerated fresh on every build), simpler than generating it client-side.
- **Roadmap**: `/curriculum` ended up as a block-grouped list with a client-side filter box, not "a single visual graph" — a deliberately lighter-weight interpretation of this section's original ask, given the module count that eventually existed (69 modules) would make a literal node-graph visualization cluttered rather than useful.
- **`answerType: "code"`** is defined in the exercise schema (as speced above) but has **no grading/rendering implementation** in `ExerciseCard.astro` — this was never actually needed for Phase 4's content, but is now directly relevant to Phase 5 (see below).

**Phase 5 (not designed here)**: the user is scoping a second major phase — interactive/coding exercises (RL policy training, kinematics visualization) and possibly a second source corpus (Tedrake's MIT notes) and simulation/HF tooling (MuJoCo, LeRobot). Two pilots exist (uncommitted; see `PROJECT_STATE.md`): a three.js-based rotation visualizer and a client-side Q-learning grid-world trainer, both built as embedded interactive widgets directly in lesson `.mdx`, deliberately **not** using the dormant `code` `answerType`/grading path — that remains a real option for a future *graded* coding-exercise pattern if Phase 5 wants one, distinct from these exploratory (ungraded) demos. This document's schema/architecture sections above should be revisited once Phase 5 is actually scoped, the same way `CURRICULUM.md` will need a real Phase 5 curriculum design (new module IDs, source audit) rather than the placeholder note currently there.
