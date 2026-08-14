# OPT-01 review — Unconstrained Optimization: Line Search & Newton

Review state: `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Primary sources checked: `lecture-optimization`, pp5–14 §§1.1–1.3; `lecture-maths`, pp47–58 §4.1
External benchmark: Boyd & Vandenberghe, *Convex Optimization* (official 2024 PDF), §§9.2 and 9.5; accessed 2026-08-14

## Verdict

This is a well-motivated and mostly source-complete optimization on-ramp. It gives line search, strong-convexity context, metric-dependent descent, Newton's method, a stable linear-solve example, damping, and seven exercises with full feedback. Its progression from step size to direction to curvature is excellent.

Several statements and one exercise nevertheless need mathematical repair. The unit-metric optimization problem has a normalized solution, but the exercise asks the learner to prove equality with the unnormalized direction. “Second Wolfe” is actually the strong Wolfe curvature condition, ordinary Armijo backtracking does not by itself enforce it, and the stated parameter restriction and conjugate-gradient dependency need qualification. The fallback paragraph gives the wrong sign for a descent direction and reverses how damping changes when forcing a small step. Finally, “one Newton step reaches the optimum for a quadratic” requires a strictly convex quadratic, not merely any second-order polynomial.

## Rubric scores

| Category | Score / 3 | Rationale |
|---|---:|---|
| Objective design | 2 | Strong and testable, but it requires a duplicated MATH-05 derivation and treats contextual design goals as universal optimizer requirements. |
| Source fidelity | 3 | The declared ranges are substantially represented; several source statements need explicit qualification rather than literal inheritance. |
| Technical correctness | 1 | Normalization, Wolfe terminology/algorithm, descent sign, damping limit, and general-quadratic claims need repair. |
| Prerequisite readiness | 3 | Taylor/Hessian readiness is directly checked; MATH-05 supplies the metric idea after its approved repair. |
| Sequence and links | 1 | It immediately repeats MATH-05 and conflates strong-Wolfe requirements with the linear conjugate-gradient treatment in OPT-02. |
| Exposition and layout | 3 | Clear, coherent, and concrete, with useful algorithm boxes and a worked solve. |
| Visual pedagogy | 1 | The source's high-value step-size, line-search, and Newton-direction figures are all omitted. |
| Exercises and feedback | 2 | Seven complete exercises with good variety; the metric derivation's requested equality is false under its own unit constraint. |
| Retrieval support | 1 | Five unkeyed prompts and only 2/7 card exports; no keyed direct-recall layer. |
| Reference usefulness | 2 | Summary and cheat sheet are useful but repeat overbroad Newton/Wolfe statements and omit an invariant stopping measure. |

## Prioritized findings

| ID | Priority | Finding | Integration status | Evidence / disposition |
|---|---|---|---|---|
| O01-01 | P1 | The unit-metric steepest-step exercise asks for the wrong equality. | `UNPLANNED_GAP` | `OPT-01-ex1c`, prompt/hints; `OPT-01.mdx:106-112`. Under `δᵀAδ=1`, the optimizer is `-A⁻¹g/√(gᵀA⁻¹g)`. Use equality with the normalized expression or state only proportional direction. |
| O01-02 | P1 | The lesson calls the absolute-value inequality the “2nd Wolfe condition” without distinguishing weak versus strong Wolfe, restricts `c₂<1/2` as though universal, and implies Armijo backtracking can enforce both conditions by shrinking. | `UNPLANNED_GAP` | `:88-102`; exercise hint `OPT-01-ex1b`. Name Armijo, weak Wolfe, and strong Wolfe separately; state `0<c₁<c₂<1` generally and explain the stricter nonlinear-CG convention. A strong-Wolfe search needs bracketing/zoom or bidirectional adjustment, not shrink-only Armijo backtracking. |
| O01-03 | P1 | The robust-Newton paragraph states the wrong descent sign and reverses the damping/trust-region limiting behavior. | `UNPLANNED_GAP` | `:181`. A descent direction satisfies `∇fᵀδ<0`; increasing `λ` makes the damped step small and gradient-like, while decreasing the trust-region radius makes its step small. Relaxing means `λ→0` or radius increasing. |
| O01-04 | P1 | “A quadratic reaches the optimum in one Newton step” is missing strict-convexity/PD conditions. | `UNPLANNED_GAP` | `:136,148,190`; `OPT-01-ex3` hints. For an invertible indefinite/negative-definite Hessian, Newton reaches the quadratic's stationary point, which may be a saddle/maximum. Keep the one-step optimum claim for strictly convex quadratics. |
| O01-05 | P1 | Metric steepest-descent is re-derived immediately after MATH-05 despite the approved ownership split. | `PENDING_PLAN_RECONCILIATION` | `:104-114`, `OPT-01-ex1c`; decision `0006` assigns the conceptual/invariance derivation to MATH-05 and application/recall to OPT-01. Replace this duplicate challenge derivation with a short recall/application task once the next Phase 5 revision absorbs the decision. |
| O01-06 | P2 | The opening and summary overgeneralize monotonicity, exponential convergence, and invariance as requirements for every good optimizer. | `UNPLANNED_GAP` | `:49-58,185-191`. Present them as desirable properties in the smooth deterministic setting. Later stochastic/momentum methods need not be monotone, and the stated rate requires global strong convexity/smoothness. Limit objective rescaling to positive constants and coordinate invariance to nonsingular affine/linear changes. |
| O01-07 | P2 | Generic Newton damping is labelled Levenberg–Marquardt without distinguishing its least-squares form. | `UNPLANNED_GAP` | `:174-181`. Use “damped/modified Newton”; reserve or qualify LM as the nonlinear-least-squares `JᵀJ+λI` case introduced with OPT-02. |
| O01-08 | P2 | The page omits three source visuals that carry the central intuition. | `UNPLANNED_GAP` | Source pp7–8 and p12 show gradient-size failure, Armijo geometry, and first-/second-order directions; the module has no figure import. Add static redraws/reuse before considering an interactive. |
| O01-09 | P2 | The recall layer is too sparse for the first optimization module. | `UNPLANNED_GAP` | Seven answered exercises (approximately 1 foundation, 4 application, 2 challenge), five unkeyed retrieval prompts, 7/7 solutions, and 2/7 card exports. Add keyed condition/assumption/failure-mode recall without adding more derivations. |
| O01-10 | P2 | The invariant stopping story is incomplete. | `UNPLANNED_GAP` | Boyd & Vandenberghe §9.5 introduces the Newton decrement as an affine-invariant measure and stopping criterion; current algorithm uses step infinity norm only (`:168`). Add a compact optional/reference box and connect implementation to stable solves/`NUM-03`; do not expand into convergence proofs. |

## Declared-source completeness

The primary range is substantially covered: optimizer desiderata, normalized-gradient/backtracking algorithm, Armijo/strong-Wolfe inequalities, the strong-convexity rate, metric steepest descent, coordinate behavior, Newton derivations, robust fallback, damping, and trust-region relation all appear. Source p14 begins the least-squares transition and is appropriately owned by OPT-02 rather than duplicated here.

The issue is source correction rather than wholesale omission. The workbook should explicitly improve on the source where it calls any second-order polynomial's stationary point an optimum, treats a proportional direction as an equality under a unit constraint, or uses locally idiosyncratic covariance/Wolfe terminology. The source figures are pedagogically material and should be restored or redrawn.

## Tool/resource recommendation

The required intervention is a static three-panel figure: Armijo acceptance geometry, poorly scaled gradient contours, and gradient versus Newton directions. An optional CPU/browser quadratic explorer could vary condition number and starting point while showing gradient, damped-Newton, and accepted line-search steps. It should reuse the MATH Hessian/SVD geometry assets and be built only after static acceptance and bundle checks.

The official Boyd–Vandenberghe Chapter 9 text and examples are suitable as an optional reference link and as the benchmark for affine invariance, decrement/stopping, and backtracking assumptions; they should not replace the workbook's self-contained explanation.

## Phase 5 reconciliation

Decision `0006-math-review-approved.md` already fixes the MATH-05/OPT-01 division and proposes `NUM-03`, but plan revision 2.2 predates that decision. O01-05 is therefore pending the next plan revision. O01-01/02/03/04/06/07/08/09/10 are not explicitly owned by revision 2.2 and must be considered in the OPT block reconciliation rather than assumed covered by generic F8 or NUM language.

## Batched human decisions

- Treat O01-01 through O01-04 as mandatory factual repairs.
- Apply the already approved MATH-05/OPT-01 ownership split.
- Approve the three static visual concepts; keep a quadratic explorer optional.
- Add keyed recall during the block pass and a compact Newton-decrement reference rather than another long proof.

Presentation verification: `STRUCTURE_VERIFIED`; source PDF pages were visually inspected, while live desktop/mobile inspection remains deferred.
