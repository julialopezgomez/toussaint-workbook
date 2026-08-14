# OPT-03 review — Constrained Optimization: KKT & the Lagrangian

Review state: `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Primary sources checked: `lecture-optimization`, pp21–23 and pp30–34; `lecture-maths`, pp58–67
External benchmark: Boyd & Vandenberghe, *Convex Optimization*, Chapter 5; accessed 2026-08-14

## Verdict

This is an approachable constrained-optimization introduction with an excellent geometric motivation, two correct hand-solves, and a useful weak/strong-duality bridge. All six exercises have complete feedback.

Its central theorem is not precise enough for its stated objective. KKT necessity for a local optimum requires a constraint qualification; it is not true “for any NLP.” The force balance is a cone of active inequality gradients plus the span of equality gradients, not the unrestricted span of all constraints. The page also blurs stationarity with minimizing the Lagrangian and claims optima are necessarily Lagrangian saddle points without the convexity/strong-duality assumptions that make that statement valid.

## Rubric scores

| Category | Score / 3 | Rationale |
|---|---:|---|
| Objective design | 2 | The right objectives, but “precisely” is not achieved without constraint qualifications. |
| Source fidelity | 3 | Declared topics and examples are represented; source shorthand needs correction. |
| Technical correctness | 1 | The unqualified KKT theorem and saddle/min-max claims are consequential. |
| Prerequisite readiness | 2 | Gradient readiness is checked; feasible-direction geometry and convexity assumptions are not. |
| Sequence and links | 3 | Correctly bridges unconstrained methods to OPT-04. |
| Exposition and layout | 3 | Strong geometric-to-algebraic progression. |
| Visual pedagogy | 1 | The source force-balance figure is omitted. |
| Exercises and feedback | 3 | Six aligned, fully solved exercises. |
| Retrieval support | 1 | Four unkeyed prompts and 2/6 exports. |
| Reference usefulness | 2 | Compact formulas, but unsafe as a theorem reference until assumptions are repaired. |

## Prioritized findings

| ID | Priority | Finding | Integration status | Evidence / disposition |
|---|---|---|---|---|
| O03-01 | P1 | KKT necessity is asserted for every NLP without a constraint qualification. | `UNPLANNED_GAP` | `OPT-03.mdx:62-68,123-128`. State a suitable introductory qualification such as LICQ/MFCQ and distinguish necessity from convex sufficiency. Include a small counterexample or warning box. |
| O03-02 | P1 | Force balance is described as an unrestricted span of all constraint gradients. | `UNPLANNED_GAP` | `:60,72`. Use only active inequalities, with nonnegative coefficients (a cone), plus the unrestricted span of equality gradients. |
| O03-03 | P1 | `min_x L` is equated with stationarity and optima are called necessary saddle points without strong-duality/convexity conditions. | `UNPLANNED_GAP` | `:83-89,123-128`. Use `∇_xL=0` for stationarity; reserve the global saddle/min-max statement for convex problems under strong duality. |
| O03-04 | P2 | Equality-constrained stationarity is presented as an unconstrained problem in `(x,κ)`. | `UNPLANNED_GAP` | `:89`. It is a root/stationarity system, not generally a minimization in both variables; clarify the saddle nature and second-order checks. |
| O03-05 | P2 | Multiplier sensitivity/“shadow price” is absent. | `UNPLANNED_GAP` | Boyd & Vandenberghe §5.6. A compact reference/application box would make multipliers operationally meaningful for robotics constraints; no full sensitivity proof is needed. |
| O03-06 | P2 | Geometric and recall support are thin. | `UNPLANNED_GAP` | Restore/redraw the source p22 force-balance figure and add keyed KKT-assumption/active-set/duality checks. Six answered exercises, four unkeyed prompts, 2/6 exports. |

## Phase 5 reconciliation

Revision 2.2 does not own these theorem repairs or the static KKT geometry. Later trajectory-optimization modules depend on correct KKT conditions and cannot substitute for repairing this foundation. The sensitivity box is optional reference depth; the theorem assumptions are essential main route.

Presentation verification: `STRUCTURE_VERIFIED`; representative source pages were visually checked and live desktop/mobile inspection remains deferred.
