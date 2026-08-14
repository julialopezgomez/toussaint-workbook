# MATH-03 review — Vector Spaces, Dual Spaces & Coordinate Transformations

Review state: `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Primary source checked: `lecture-maths`, pp21-31 §§3.1-3.3
External benchmark: *Mathematics for Machine Learning*, §§2.4-2.8; accessed 2026-08-14

## Verdict

This module has an excellent curricular purpose: it explains why vectors are not merely arrays and directly connects bases and duals to robot frames. The exercises on polynomial vector spaces, dual bases, and coordinate conversion are useful and fully solved. Three mathematical transcription/design defects prevent approval as-is, however: the vector-space definition omits distributivity over scalar addition; the displayed dual-space set omits the word “linear”; and the covariance/contravariance table reverses its labels relative to its own surrounding prose.

The declared objective also promises matrix representations in a chosen pair of input/output bases, but the lesson teaches only vector coordinates and the same-basis similarity transform `B^{-1}FB`. Toussaint p28 explicitly gives the mixed input/output cases. That missing skill is important for frame-aware robotics transformations.

## Rubric scores

| Category | Score / 3 | Rationale |
|---|---:|---|
| Objective design | 2 | Strong purpose, but the pair-of-bases objective is not taught or assessed. |
| Source fidelity | 2 | Most definitions appear; mixed-basis transformations are omitted and two definitions are mistranscribed. |
| Technical correctness | 1 | Missing axiom, non-linear dual-space set, and reversed variance labels are material errors. |
| Prerequisite readiness | 1 | Declared MATH-01 is not checked; actual matrix and MATH-02 concepts are used without being declared. |
| Sequence and links | 2 | Fits the route, but eigendecomposition is incorrectly assigned to MATH-05. |
| Exposition and layout | 2 | Motivating and coherent, but the tensor section is dense and terminology is unusually broad. |
| Visual pedagogy | 1 | Coordinate change is spatial but has no basis/frame diagram. |
| Exercises and feedback | 2 | Five complete exercises; no mixed-basis linear-map exercise. |
| Retrieval support | 1 | Four unkeyed prompts and two card exports; little keyed definition recall. |
| Reference usefulness | 2 | Useful summary, but it repeats the incomplete transform coverage. |

## Prioritized findings

| ID | Priority | Finding | Integration status | Evidence / disposition |
|---|---|---|---|---|
| M03-01 | P1 | Definition 3.1 omits `(α+β)v=αv+βv`. | `UNPLANNED_GAP` | `MATH-03.mdx:68-71`; the source also omits it, so add a disclosed external correction rather than silently preserving an incomplete axiom set. |
| M03-02 | P1 | `V*={f:V→R}` accidentally includes all functions, not only linear functionals. | `UNPLANNED_GAP` | `:112-120`; source p25 correctly includes “linear.” Repair the set definition. |
| M03-03 | P1 | The variance row labels columns “co-variant” and rows “contra-variant,” contradicting the adjacent vector/coordinate rows and later source treatment. | `UNPLANNED_GAP` | `:128-137`; vectors/components are contravariant and covectors/components covariant under the convention used in MATH-05. Replace the table with an explicitly transformation-based version. |
| M03-04 | P1 | General input/output basis changes are promised but not taught or exercised. | `UNPLANNED_GAP` | Objective `:14`; source p28 gives `[f]^{AB}=FB`, `[f]^{BA}=B^{-1}F`, and `[f]^{BB}=B^{-1}FB`; lesson `:141-163` only derives vector coordinates and same-basis similarity. Add one mixed-frame worked example/exercise. |
| M03-05 | P2 | Prerequisite metadata/readiness do not match actual dependencies. | `UNPLANNED_GAP` | Frontmatter declares MATH-01 (`:7`), readiness checks matrix inversion (`:43-50`), and lesson relies on MATH-02 gradients (`:41,110`). Declare the actual minimum prerequisites and check them semantically. |
| M03-06 | P1 | Eigendecomposition is routed to MATH-05 instead of MATH-04. | `UNPLANNED_GAP` | `:163`; correct the module name/link. |
| M03-07 | P2 | “k-form” is used for arbitrary multilinear maps, whereas many external texts reserve it for alternating covariant tensors. | `UNPLANNED_GAP` | `:96-124`; keep Toussaint's terminology only with a convention note so later differential-geometry reading is not confusing. |
| M03-08 | P2 | Recall and visual intuition are weak for basis transformation. | `UNPLANNED_GAP` | Five answered non-recall exercises; no figure. Add keyed definitions and a static old-basis/new-basis coordinate diagram. |

Exercise inventory: 5 answered (approximately 1 conceptual recall, 4 application/short derivation, 0 synthesis), 4 unkeyed retrieval prompts, 5/5 solutions, 2/5 exercise-card exports.

## Tool recommendation

A 2D basis-change explorer is high value: drag two basis vectors and a geometric vector, then display old/new coordinates and the invariant geometric object. It is CPU/browser-only, account-free, and relevant later to KIN frame transforms. The required simpler alternative is a two-panel basis/frame diagram plus a mixed-input/output matrix example.

## Phase 5 reconciliation

NUM-02 names MATH-03 as a prerequisite and adds shape/batching practice, but it does not own any of the definition or mixed-basis defects. Revision 2.2 has no explicit MATH-03 repair or basis visualization owner.

## Batched human decisions

- Approve all three definition/table corrections as mandatory.
- Decide whether mixed input/output basis changes remain here (recommended) or move to a clearly routed KIN frame module.
- Approve a static basis diagram first; optional interactive can follow runtime validation.

Owner approved the recommended defaults in decision `docs/decisions/0006-math-review-approved.md`; the next Phase 5 plan revision must absorb the open items. Presentation verification: `STRUCTURE_VERIFIED`; live desktop/mobile inspection remains pending.
