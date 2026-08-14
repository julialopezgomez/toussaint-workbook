# Decision Record 0007 — OPT block review approved

Date: 2026-08-14

## Decision

The owner approved the evidence-based review of the complete current OPT block against the committed baseline `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`.

The approved review artifacts are:

- `docs/review/blocks/OPT.md`;
- `docs/review/modules/OPT-01.md` through `OPT-06.md`;
- the OPT additions to `docs/review/CURRICULUM_COVERAGE.md` and `docs/review/REVIEW_INDEX.md`.

The block remains **`CURRENTLY_PARTIAL`**. Approval accepts the findings and their planning dispositions; it does not claim that the current lessons are complete.

## Approved mandatory repairs

The owner requires all factual, theorem-condition, notation, prerequisite, source-qualification, cheat-sheet, and assessment repairs identified in the OPT block and module records. In particular:

1. Repair metric-direction normalization, Wolfe terminology/enforcement, descent signs, damping/trust-region limits, and Newton assumptions.
2. State Gauss–Newton rank/damping/conditioning requirements, BFGS curvature conditions, and linear/nonlinear CG convergence conditions.
3. State a constraint qualification for KKT necessity and correct force-balance, stationarity, saddle, and duality claims.
4. Correct convex/quasiconvex language, barrier domain/limit/sign claims, convex-QP assumptions, and SQP Hessian/globalization treatment.
5. State the assumptions behind stochastic gradients, SGD convergence, adaptive scaling, and accelerated rates.
6. Make Bayesian-optimization min/max conventions consistent and qualify GP prior-mean, numerical-solve, smoothness, and bandit-confidence claims.
7. Repair prerequisite/readiness metadata and propagate all corrections into exercises, solutions, the OPT cheat sheet, `OPT-EXAM`, and downstream references.
8. Correct the source-manifest interpretation so a “full optimization course” claim is used only when every material section is taught, explicitly routed, or given an approved scope disposition.

## Approved relevance-scoped additions

The owner approved:

- a compact `OPT-04` bridge covering LP relaxations, lower bounds/rounding/branch-and-bound intuition, and DCP-style QP/SOCP/SDP problem-class recognition;
- a new main-route, CPU-first `OPT-04B` module for the Implicit Function Theorem and differentiation through root, argmin, and KKT systems, including assumptions and active-set/singularity failure modes;
- a new main-route, CPU-first `OPT-05B` module for derivative-free optimization, including random/multistart baselines, CMA-ES intuition, a concise treatment of Nelder–Mead or pattern search, and evaluation-budget diagnostics;
- compact Phase-I/primal-dual context in `OPT-04`/`OPT-04B` where it supports practical solvers;
- optional reference boxes for multiplier sensitivity and the Newton decrement.

ADMM remains optional/deferred unless a concrete distributed or multi-robot dependency later justifies promotion. The source's reinforcement-learning overlap is routed to RL/RLEARN rather than duplicated inside OPT.

## Approved teaching and assessment policy

- Preserve useful derivation and numeric exercises; repair false or underqualified prompts and solutions.
- Add a small keyed recall layer across the whole OPT block, with no mechanical card-per-exercise ratio.
- Correct and rebalance `OPT-EXAM`, add genuine `OPT-06` coverage, and ensure retakes assess the same target as their original questions.
- Require five reusable static visual concepts covering line-search/Newton geometry, sparsity/conjugate directions, KKT force balance, LP/central-path/SQP geometry, and stochastic/GP-acquisition behavior.
- Keep browser interactives optional and subject to later value/runtime/bundle checks.
- Defer live desktop/mobile presentation approval. Current evidence remains `STRUCTURE_VERIFIED`.

## Phase 5 reconciliation

The current stable augmentation plan is revision 2.2 (`412b807536da6d90b1063ad800aadf5435a6e05eabe6e3cfcd6ea65ac308f2f3`). It predates the full MATH and OPT reviews and does not yet own most approved findings.

The required next-plan delta is:

| Destination | Required plan change |
|---|---|
| Plan thesis | Replace the claim that missing theory is not the workbook's defect with a qualified statement: MATH and OPT reveal material foundation correctness and completeness debt alongside the already verified implementation gap. Do not generalize beyond reviewed blocks. |
| F0 / foundation stabilization | Expand F0 to all approved P1 repairs and compact foundation additions in MATH and OPT, including cheat-sheet/exam propagation, before downstream Phase 5 authoring relies on them. |
| Route and module inventory | Add approved `NUM-03`, `OPT-04B`, and `OPT-05B`; recalculate all module/block/hour counts, route positions, prerequisite edges, stubs, acceptance criteria, and downstream references. |
| Source scope | Add the source needs created by MATH/OPT repairs and additions to Gate B. Preserve relevance-scoped completeness and explicitly route/defer omitted source sections. |
| Numerical integration | Connect stable solves, conditioning, numerical rank, and GP jitter to approved `NUM-03` without removing the mathematical conditions from OPT. |
| F8 | Extend keyed retrieval, reference, static-figure, cheat-sheet, and milestone work across both MATH and OPT. |
| Scope dispositions | Keep ADMM optional/deferred and route the optimization–RL overlap to RL/RLEARN. |

This decision does **not** reopen Gate A and does not approve Gate B's production corpus. Revision 2.2 should be superseded and re-pinned before Gate B source selection is finalized.

## Wider-curriculum consequence

Two consecutive full foundation-block audits found the same systemic pattern: source-coverage claims and objectives were authored from selected page content rather than a complete source/block disposition map; theorem assumptions were compressed out; errors propagated into cheat sheets and milestones; and planned advanced modules assume foundations that remain partial.

This is substantial enough to revise the Phase 5 architecture now, before Gate B is finalized, but it does **not** justify waiting for all remaining block reviews or rewriting current lessons immediately. The proportionate response is:

1. revise the plan now around a foundation-stabilization lane and the three approved new modules;
2. let Gate B select sources against that corrected scope, with an explicit amendment mechanism for later review-discovered needs;
3. keep implementation blocked until the relevant curriculum/source gates and F0 sequencing are approved;
4. continue the independent audit in parallel, beginning with PROB.

## When the workbook changes

- **Now:** decision and review-state documentation are updated.
- **Next plan revision:** Claude incorporates decisions 0006 and 0007, updates the plan architecture and counts, and publishes the new plan hash before completing the Gate B shortlist.
- **Gate B:** sources are proposed only; no lesson or code authoring is authorized.
- **F0/foundation implementation:** mandatory current-content repairs and assigned compact additions are authored and verified.
- **Later module/F8 work:** `NUM-03`, `OPT-04B`, `OPT-05B`, static figures, keyed recall, reference surfaces, and corrected assessments are implemented and re-reviewed.

No lesson, exercise, cheat sheet, milestone, source manifest, or application code was modified by recording this decision.
