# MATH-02 review — Gradients, Jacobians, Hessians & Taylor Expansion

Review state: `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Primary source checked: `lecture-maths`, pp12-15 and pp18-19
External benchmark: *Mathematics for Machine Learning*, §§5.2-5.8; accessed 2026-08-14

## Verdict

This is a useful and mostly well-constructed bridge from scalar calculus to optimization: shapes are explicit, the Jacobian/gradient convention is declared, finite differences are introduced as a verification workflow, and six exercises have complete feedback. It nevertheless contains one consequential optimization misconception: it describes positive semidefiniteness as precisely the condition making a stationary point a genuine local minimum. Positive definiteness is a sufficient second-order condition; a merely semidefinite Hessian is inconclusive without higher-order or neighbourhood information.

The page also declares the Hessian symmetric without stating the mixed-partial regularity assumption, and twice sends the learner to MATH-05 for eigendecomposition material that is actually in MATH-04. Finally, the objective promises implementing a numerical gradient check, but the current exercise only evaluates one component by hand. Phase 5's NUM-01 explicitly owns that executable step.

## Rubric scores

| Category | Score / 3 | Rationale |
|---|---:|---|
| Objective design | 2 | Strong objectives, but the coding objective is not currently fulfilled. |
| Source fidelity | 3 | Declared source units and finite-difference workflow are represented. |
| Technical correctness | 1 | PSD/minimum and Hessian-symmetry qualifications are consequential. |
| Prerequisite readiness | 3 | The chain rule is declared and directly checked. |
| Sequence and links | 1 | Two important eigendecomposition links point to MATH-05 instead of MATH-04. |
| Exposition and layout | 3 | Excellent definition-to-geometry-to-practice arc. |
| Visual pedagogy | 1 | Curvature classification has no contour/eigendirection figure. |
| Exercises and feedback | 2 | Six complete exercises, but “implementation” is currently a hand calculation. |
| Retrieval support | 1 | Four unkeyed prompts; only two exercises export cards and none is direct recall. |
| Reference usefulness | 2 | Strong summary/cheat sheet, but the incorrect PSD implication is repeated elsewhere. |

## Prioritized findings

| ID | Priority | Finding | Integration status | Evidence / disposition |
|---|---|---|---|---|
| M02-01 | P1 | PSD is presented as sufficient for a “genuine” local minimum; pointwise curvature is also blurred with convexity on a neighbourhood. | `UNPLANNED_GAP` | `MATH-02.mdx:81,87-91`. State PD/ND/indefinite tests and explicitly mark semidefinite cases inconclusive; distinguish local curvature at a point from convexity over a set. |
| M02-02 | P1 | “The Hessian is symmetric” omits the equality-of-mixed-partials condition. | `UNPLANNED_GAP` | `:78-83`; the cheat sheet at `math.mdx:37` already contains the missing `C²` caveat. Move the qualification into first teaching. |
| M02-03 | P1 | Eigendecomposition/characteristic-polynomial links target MATH-05, but the material is in MATH-04. | `UNPLANNED_GAP` | `:83,140`. Repair both links/text labels. |
| M02-04 | P1 | Objective 6 promises implementing a gradient/Jacobian check, but no code is executed. | `PLANNED_TO_ADDRESS` | Frontmatter `:13`; exercise `MATH-02-ex1b` is numeric tracing only. Phase 5 NUM-01 explicitly reuses this as its first executable lab. Keep an explicit forward route. |
| M02-05 | P2 | Fixed epsilon and absolute tolerance are shown without float-scale/epsilon-sweep guidance. | `PLANNED_TO_ADDRESS` | `:107-124`; NUM-01 owns float pitfalls and tolerance-based self-checks. The current module still needs a concise forward qualification. |
| M02-06 | P2 | Curvature and stationary-point classification need a static visual before any interactive. | `UNPLANNED_GAP` | `:76-91` has no figure. Add positive/negative/indefinite/semidefinite contour panels with Hessian eigendirections. |
| M02-07 | P2 | Recall support is not proportional to the module's foundational role. | `UNPLANNED_GAP` | Six answered application/derivation items, four unkeyed prompts at `:154-159`, two card exports. Add keyed definition, shape, assumption, and classification recall. |

Exercise inventory: 6 answered (approximately 0 direct recall, 6 application/short derivation, 0 synthesis), 4 unkeyed retrieval prompts, 6/6 solutions, 2/6 exercise-card exports.

## Tool recommendation

A 2D quadratic explorer could vary eigenvalues and rotate eigenvectors while showing contours, gradient arrows, and the Hessian. It is CPU/browser-only and useful for diagnosing semidefinite/indefinite cases. The required simpler alternative is a four-panel static contour figure; the future NUM-01 lab is the appropriate home for executable gradient checking.

## Phase 5 reconciliation

M02-04/05 are absorbed by NUM-01 if MATH-02 gains an honest forward route. M02-01/02/03/06/07 are not currently owned by revision 2.2 and remain gaps; future visualization or labs cannot substitute for repairing the mathematical statements.

## Batched human decisions

- Confirm the second-order-condition correction as mandatory before further optimization authoring.
- Approve static curvature panels; treat the interactive as optional enhancement.
- Extend the later retrieval pass beyond the three calibration modules to this foundational module.

Owner approved the recommended defaults in decision `docs/decisions/0006-math-review-approved.md`; the next Phase 5 plan revision must absorb the open items. Presentation verification: `STRUCTURE_VERIFIED`; live desktop/mobile inspection remains pending.
