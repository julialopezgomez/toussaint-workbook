# Decision Record 0006 — MATH block review approved

Date: 2026-08-14

## Decision

The owner approved the evidence-based review of the complete current MATH block against the committed baseline `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`.

The approved review artifacts are:

- `docs/review/blocks/MATH.md`;
- `docs/review/modules/MATH-00.md` through `MATH-05.md`, including the previously approved `MATH-02B.md` calibration record;
- the MATH additions to `docs/review/CURRICULUM_COVERAGE.md` and `docs/review/REVIEW_INDEX.md`.

The block remains **`CURRENTLY_PARTIAL`**. Approval accepts the findings and their planning dispositions; it does not claim the present lessons are complete.

## Approved mandatory repairs

The following are required rather than optional enrichment:

1. Correct PSD/PD, stationary-point, Hessian-regularity, singular-value/eigenvalue, pseudoinverse, covariance-normalization, and differentiability qualifications.
2. Repair the vector-space axiom list, dual-space definition, covariance/contravariance table, notation errors, incorrect future/past wording, prerequisite metadata/readiness, and incorrect module routes.
3. Add concise provenance notes where the workbook corrects or qualifies a source-derived statement.
4. Repair the math cheat sheet and `MATH-EXAM` wherever they repeat an error, misattribute a prerequisite, overclaim coverage, or assess material before it is taught.

## Approved relevance-scoped additions

The owner approved the proposed content and locations in the MATH block record:

- Taylor polynomial/series/analyticity and qualitative local-error boundaries in `MATH-00`;
- a compact core-notation table in `MATH-01`;
- affine-space/equality-constraint geometry and mixed input/output basis transforms in `MATH-03`;
- general full-rank projection and its least-squares bridge in `MATH-03B`;
- Identities 2.5, especially Woodbury, in `MATH-02B`;
- Eckart–Young/best rank-`k` approximation in `MATH-04`;
- the coordinate-transformation/invariance argument in `MATH-05`;
- one new CPU-first main-route module, `NUM-03`, for stable solves, conditioning, numerical rank, QR, and Cholesky.

Small externally observed details may still be omitted under the approved relevance-scoped completeness rule when they do not support later content, core learning, or the owner's research, provided the scope decision is explicit.

## Approved teaching and assessment policy

- Keep all existing derivation/application exercises unless a later implementation review finds a concrete redundancy.
- Add a small keyed recall layer across all MATH modules; unanswered retrieval prompts do not count as recall feedback.
- Do not impose a mechanical card-per-exercise or card-per-prerequisite ratio.
- Correct and rebalance `MATH-EXAM` after the teaching repairs.
- Require five static intuition visuals: Taylor locality, Hessian classes, basis change, metric geometry, and SVD/rank collapse.
- Keep browser interactives optional and subject to a later value/runtime/bundle check. Reuse one metric tool across `MATH-03B` and `MATH-05` if built.
- Keep `MATH-05` as the conceptual/covariance owner; make `OPT-01` recall and apply it without repeating the full derivation.
- Defer live desktop/mobile presentation approval. Current evidence remains `STRUCTURE_VERIFIED`.

## Phase 5 reconciliation

The current stable augmentation plan is revision 2.2 (`412b807536da6d90b1063ad800aadf5435a6e05eabe6e3cfcd6ea65ac308f2f3`). It predates this full-block review and therefore does not yet textually own most findings.

The approved reconciliation delta for the next plan revision is:

| Destination | Required plan change |
|---|---|
| F0 | Expand from the three calibration modules to include all approved P1 factual, notation, link, prerequisite, source-qualification, cheat-sheet, and milestone repairs in MATH. |
| Foundation additions | Schedule the approved compact in-module additions before downstream Phase 5 authoring relies on them. The planner may group these with F0 but must not silently defer them to an unrelated advanced module. |
| F1 / NUM | Add `NUM-03` after the relevant MATH foundation and coordinate its route with `NUM-01`/`NUM-02`. |
| Visual work | Add the five static figures as acceptance requirements; interactives remain optional candidates. |
| F8 | Extend keyed retrieval/reference/assessment coverage to the whole MATH block and correct `MATH-EXAM`. |
| OPT integration | Preserve the approved `MATH-05`/`OPT-01` division of responsibility. |
| Gate B | Include the source needs created by these approved additions in production-corpus selection; the already approved review benchmark is evidence, not automatic production-corpus approval. |

This decision does **not** reopen Gate A. The Phase 5 plan should be revised and re-pinned before Gate B source selection is finalized, so Gate B evaluates the approved MATH/`NUM-03` source needs rather than an obsolete revision-2.2 scope.

## When the workbook changes

- **Now:** decision and review-state documentation are updated.
- **Next plan revision:** Claude incorporates this approved delta and publishes the new plan hash/revision before finalizing Gate B.
- **F0 implementation:** mandatory corrections and assigned compact foundation additions are authored and verified.
- **NUM implementation:** `NUM-03` is authored with the rest of the approved NUM route.
- **Visual/F8 implementation:** static figures, keyed recall, reference surfaces, and the milestone are completed and re-reviewed.

No lesson, exercise, cheat sheet, milestone, or application code was modified by recording this review decision.
