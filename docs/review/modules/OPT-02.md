# OPT-02 review — Gauss-Newton, Quasi-Newton & Conjugate Gradient

Review state: `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Primary source checked: `lecture-optimization`, pp14–20 §1.4
External benchmark: Boyd & Vandenberghe, *Convex Optimization* (official 2024 PDF), Chapters 9 and C; accessed 2026-08-14

## Verdict

The module gives a valuable progression from problem structure (Gauss-Newton), through learned curvature (BFGS), to gradient-only conjugate directions. The residual derivation, numeric least-squares example, trajectory structure, and six fully solved exercises are strong.

It under-specifies the conditions that make these algorithms safe. `JᵀJ` is only semidefinite in general, so the inverse, descent direction, and Riemannian-metric claims require full column rank or damping. Forming normal equations can square conditioning and introduce fill-in. BFGS needs the curvature condition `yᵀs>0` to preserve positive definiteness, while the conjugate-gradient finite-step claim requires a symmetric positive-definite quadratic and exact arithmetic/line search. These conditions belong in first teaching because the module presents implementable algorithms.

## Rubric scores

| Category | Score / 3 | Rationale |
|---|---:|---|
| Objective design | 2 | Good scope, but safety/rank/curvature conditions and the linear-vs-nonlinear CG distinction are absent. |
| Source fidelity | 3 | Declared source is thoroughly represented, including the robotics example. |
| Technical correctness | 1 | Rank, metric, sparsity, BFGS-curvature, and CG-convergence qualifications are material. |
| Prerequisite readiness | 2 | Newton is checked; matrix rank, least squares, and metric prerequisites are used but not checked. |
| Sequence and links | 2 | Good route, but it inherits the OPT-01 strong-Wolfe/CG ambiguity and needs `NUM-03`. |
| Exposition and layout | 3 | Clear method comparison and concrete examples. |
| Visual pedagogy | 1 | Source sparsity/path/CG contour figures are omitted. |
| Exercises and feedback | 3 | Six varied exercises, all with feedback. |
| Retrieval support | 1 | Four unkeyed prompts and 2/6 card exports. |
| Reference usefulness | 2 | Useful formulas but not enough conditions to choose or implement safely. |

## Prioritized findings

| ID | Priority | Finding | Integration status | Evidence / disposition |
|---|---|---|---|---|
| O02-01 | P1 | PSD is treated as sufficient for an invertible, descending Gauss-Newton step and a Riemannian metric. | `UNPLANNED_GAP` | `OPT-02.mdx:60-76,145-147`. Require full column rank for `JᵀJ≻0`; otherwise use damping, QR/SVD, or a pseudoinverse and call the pullback form degenerate rather than Riemannian. |
| O02-02 | P1 | “If `J` is sparse, so is `JᵀJ`” hides densification/fill-in and normal-equation conditioning. | `PENDING_PLAN_RECONCILIATION` | `:68-70`; source repeats the shorthand. Teach sparsity pattern dependence and `κ(JᵀJ)=κ(J)^2`; implementation belongs in approved `NUM-03`. |
| O02-03 | P1 | BFGS omits `yᵀs>0`, even though its update divides by this quantity and positive-definite preservation depends on it. | `UNPLANNED_GAP` | `:94-116`; connect to a correctly taught Wolfe line search in OPT-01 and distinguish BFGS's rank-two update from the preceding rank-one secant examples. |
| O02-04 | P1 | CG finite convergence lacks SPD/exact-arithmetic conditions and linear versus nonlinear CG is not clearly separated. | `UNPLANNED_GAP` | `:120-149`. Name the displayed Polak–Ribière method nonlinear CG; state that the `n`-step result reduces to the SPD quadratic/linear-CG case with exact line search and exact arithmetic. |
| O02-05 | P2 | Dense `O(n³)` cost is presented as universal. | `PENDING_PLAN_RECONCILIATION` | `:145`; qualify by structure, factorization, iterative solves, and Hessian-vector products; coordinate with `NUM-03`. |
| O02-06 | P2 | The page omits source visuals for factor sparsity, trajectory locality, and conjugate directions. | `UNPLANNED_GAP` | Source pp14,16,19; no figure import. Require at least a static sparse dependency/path diagram and CG contour panel. |
| O02-07 | P2 | Key conditions and method-selection facts lack keyed recall. | `UNPLANNED_GAP` | Six answered exercises, four unkeyed prompts, 6/6 solutions, 2/6 card exports. Add rank/damping, secant-curvature, and CG-condition recall. |

## Phase 5 reconciliation

The approved `NUM-03` delta is the correct implementation owner for stable least-squares solves, conditioning, factorization, and rank diagnosis, but plan revision 2.2 does not yet contain it. The mathematical qualifications remain local OPT-02 repairs. Static figures and full-block retrieval are also absent from revision 2.2.

Presentation verification: `STRUCTURE_VERIFIED`; representative source pages were visually checked and live desktop/mobile inspection remains deferred.
