# Claude entry point — Robotics & ML Workbook

Read `AGENTS.md` first and follow it as the canonical repository-wide operating
contract. Then read `docs/agent/CURRENT_HANDOFF.md` and the task-specific files
it names. Do not use this file as a project-status ledger.

## Claude-specific continuity

- After context compaction, a token-limit interruption, `/compact`, a resumed
  session, or a model switch, perform the full recovery checklist in
  `docs/agent/CONTINUITY_AND_QUALITY.md` before continuing.
- Exact approvals, hashes, counts, source decisions, and file ownership must be
  recovered from repository evidence, never from the conversation summary.
- Before reaching a usage limit, stop at a clean boundary and replace
  `docs/agent/CURRENT_HANDOFF.md`. Record completed outputs, unverified claims,
  the next safe action, and the exact approval boundary. Do not leave the next
  model to infer these from prose history.
- Do not edit `docs/review/**` while the independent review lane is assigned to
  Codex. Current ownership is recorded in the handoff.

## Current project shape

The Phase 4 committed baseline is a 69-module Astro/MDX workbook. Phase 5 is a
gated augmentation effort; the stable plan, approved decisions, and review
index—not this file—hold its current revision and status:

- `docs/plans/PHASE5_AUGMENTATION_PLAN.md`
- `docs/decisions/`
- `docs/review/REVIEW_INDEX.md`
- `docs/agent/CURRENT_HANDOFF.md`

`PROJECT_STATE.md` is a historical implementation ledger. Consult a relevant
section when needed, but do not load or extend the whole file merely to resume.
Volatile module counts, page counts, package inventory, and gate status are
deliberately not duplicated here.

## Core paths

- Modules: `src/content/course/{block}/{id}.mdx`
- Questions and solutions: `src/content/{questions,solutions}/{module-id}.json`
- Curriculum and architecture: `data/curriculum/`
- Plans and gate evidence: `docs/plans/`
- Independent review evidence: `docs/review/`
- Approval records: `docs/decisions/`
- Validation: `scripts/validate/`
- Read-only original corpus: `../original notes/`

## Commands

- Context health: `python3 scripts/validate/agent_context.py`
- Dev server: `npm run dev`
- Type/content check: `npx astro check`
- Production build: `npm run build`
- Local symbolic grader: `npm run grading-server`

Use the task-specific acceptance checks in the active plan/review record as well
as these general commands.
