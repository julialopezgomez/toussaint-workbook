# Current agent handoff

Updated: 2026-08-14
Status: **ACTIVE — replace this file at the next block/gate/model boundary**

## Baseline and authority

- Committed Phase 4 baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`.
- Active Phase 5 plan: `docs/plans/PHASE5_AUGMENTATION_PLAN.md`, revision
  2.2, SHA-256
  `412b807536da6d90b1063ad800aadf5435a6e05eabe6e3cfcd6ea65ac308f2f3`.
- Gate A is closed and approved: `docs/decisions/0005-gate-a-approved.md`.
- MATH and OPT review dispositions are approved:
  `docs/decisions/0006-math-review-approved.md` and
  `docs/decisions/0007-opt-review-approved.md`.
- Revision 2.2 is now obsolete for future-work counts and foundation scope. It
  remains the historical approved Gate A successor until Claude publishes the
  reconciled next plan revision; do not rewrite decision 0005.

## Active objectives

Two coordinated lanes are active:

1. **Claude planning lane:** incorporate decisions 0006/0007 into the next
   Phase 5 plan revision, validate every changed count/route, then perform Gate
   B source selection only and stop for owner approval. No curriculum content,
   source ingestion, lab, or application authoring is authorized.
2. **Codex review lane:** continue the independent current-workbook review in
   curriculum order, starting with PROB. Findings enter `docs/review/**` and are
   batched for owner approval. Unapproved PROB findings must not be silently
   inserted into Claude's current plan revision.

## Approved planning delta awaiting incorporation

- Add a foundation-stabilization lane for mandatory MATH/OPT factual, theorem,
  notation, route, prerequisite, source-qualification, cheat-sheet, and exam
  repairs before downstream Phase 5 work relies on them.
- Add `NUM-03`, `OPT-04B`, and `OPT-05B`; recompute all affected module/block/hour
  totals, routes, prerequisites, stubs, and acceptance criteria.
- Add whole-block keyed recall and the approved MATH/OPT static-visual work.
- Preserve `MATH-05` as conceptual/covariance owner and `OPT-01` as recall/use.
- Keep ADMM optional/deferred; route optimization–RL overlap to RL/RLEARN.
- Expand Gate B source needs to cover the approved foundation repairs and new
  modules. The review benchmark is evidence only, not automatic production
  corpus approval.
- Add a controlled amendment mechanism so later approved block reviews can
  extend the plan/source corpus without invalidating Gate A or restarting Gate B.

## Current review state

- Calibration, Gate A, MATH, and OPT are owner-approved.
- MATH and OPT are `CURRENTLY_PARTIAL`; approval records findings, not repairs.
- PROB is the next block. No PROB block/module review record has yet been
  published or approved.
- Live visual approval remains deferred. Static structure evidence is not live
  desktop/mobile visual verification.
- The agent continuity protocol, stage runbook, context validator, and structural
  review validator are installed and currently pass with zero warnings.

## Write ownership and dirty worktree

- Claude may write `docs/plans/**`, a Gate B proposal, and planning-owned support
  artifacts required by the consolidated prompt.
- Codex may write `docs/review/**`, review decision records after owner approval,
  and this agent-protocol layer.
- Neither lane may modify current lesson/exercise/solution/cheat-sheet/exam
  content during planning/review.
- Existing modified/untracked application, curriculum, package, interactive,
  plan, review, and temporary files are user-owned or pre-existing. Inspect
  `git status` and relevant diffs; do not discard, stage, or overwrite them.
- `RotationViz` and `GridWorldRL` are paused prototypes and excluded from this
  review/plan implementation pass unless the owner explicitly reactivates them.

## Next safe actions and stop conditions

### Claude

Use `docs/prompts/CLAUDE_PHASE5_RECONCILE_GATE_B.md`. Stay on Opus for this pass.
Stop after publishing the reconciled plan revision and the Gate B source
recommendation with one batched owner-approval prompt. Do not ingest sources or
author content.

### Codex

Run both agent validators, audit PROB under `docs/review/REVIEW_PROTOCOL.md`,
then present one batched approval recommendation. Do not implement review
findings. Reconcile approved findings into the plan only after the planning lane
has a stable path/revision.

## Verification required at the next boundary

- Recompute the active plan SHA-256 and update this handoff after Claude's pass.
- Search all planning docs for stale module/addition/hour totals.
- Confirm Gate A remains closed and no decision record was rewritten.
- Confirm `docs/review/**` was not changed by the planning lane.
- Run `python3 scripts/validate/agent_context.py` and
  `python3 scripts/validate/review_integrity.py`; record any warnings.
