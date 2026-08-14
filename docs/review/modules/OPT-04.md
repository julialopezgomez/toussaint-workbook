# OPT-04 review — Convex Problems, LP/QP, SQP & Log Barriers

Review state: `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Primary source checked: `lecture-optimization`, pp23–30 and pp35–44
External benchmark: Boyd & Vandenberghe, *Convex Optimization*, Chapters 2–5 and 11; accessed 2026-08-14

## Verdict

The module ambitiously connects convexity, LP/QP modeling, barriers, augmented Lagrangians, and SQP, and its five exercises all have feedback. The central-path/KKT connection is particularly valuable.

It contains several major errors. The stated convex–quasiconvex–unimodal hierarchy is false under the page's own “exactly one local minimum” definition. The log barrier is smooth on its strict-feasible domain; it does not become “non-smooth” for small `μ` or converge pointwise to an infeasible indicator. The exercise's barrier-gradient hints contradict themselves on sign. Most importantly, a general SQP subproblem uses the Hessian of the Lagrangian (or an approximation), not merely `∇²f`, and practical SQP needs a merit/filter and globalization rather than only one original-function query.

## Rubric scores

| Category | Score / 3 | Rationale |
|---|---:|---|
| Objective design | 2 | Valuable scope, but QP/SVM setup and Simplex are not actually practised. |
| Source fidelity | 2 | Main algorithms are covered; declared pp41–44 LP relaxations are omitted. |
| Technical correctness | 1 | Hierarchy, barrier, gradient-hint, QP, and SQP claims require repair. |
| Prerequisite readiness | 3 | KKT/complementarity is directly checked. |
| Sequence and links | 2 | Correct position, but future GCS/polytope work needs the omitted relaxation/modeling bridge. |
| Exposition and layout | 2 | Coherent for its breadth but too compressed to safely cover seven major topics. |
| Visual pedagogy | 1 | Central path, feasible polytope, and SQP local model have no figure. |
| Exercises and feedback | 2 | Complete feedback, but one sign derivation is internally inconsistent and objectives are under-assessed. |
| Retrieval support | 1 | Four unkeyed prompts and 2/5 exports. |
| Reference usefulness | 2 | Useful equations, but the cheat sheet repeats several overbroad claims. |

## Prioritized findings

| ID | Priority | Finding | Integration status | Evidence / disposition |
|---|---|---|---|---|
| O04-01 | P1 | The convex/quasiconvex/unimodal strict hierarchy is false under the given definition of unimodal. | `UNPLANNED_GAP` | `OPT-04.mdx:49-55,144-147`. Remove the nonstandard hierarchy or define a deliberately restricted 1D notion; teach convex and quasiconvex through epigraph/sublevel geometry instead. |
| O04-02 | P1 | The log-barrier limit and smoothness explanation is wrong. | `UNPLANNED_GAP` | `:73-95`. The barrier remains smooth on `g_i(x)<0`, is undefined outside that domain, and small `μ` leads to ill-conditioning near the boundary rather than non-smoothness. State the strictly feasible initialization requirement. |
| O04-03 | P1 | The barrier-gradient exercise contains opposite signs in adjacent steps. | `UNPLANNED_GAP` | `OPT-04-ex2` hints. For `-(1/t)log(-g)`, the contribution is `-(1/(tg))∇g`; repair the intermediate algebra and explanation. |
| O04-04 | P1 | The SQP Hessian is `∇²f` instead of the Hessian of the Lagrangian, and practical globalization is omitted. | `UNPLANNED_GAP` | `:136-150`; source p41 shares the simplification. Teach `∇²_{xx}L` or a BFGS approximation, plus merit/filter/trust-region or line-search context. Remove the one-query guarantee. |
| O04-05 | P1 | Convex QPs are restricted to `Q≻0`; PSD QPs are also convex. | `UNPLANNED_GAP` | `:61-69`. Use `Q⪰0` for convexity and `Q≻0` for strict convexity/unique unconstrained minimizer. |
| O04-06 | P1 | Declared source pp41–44 on integer LP relaxations is omitted. | `UNPLANNED_GAP` | Add a compact LP-relaxation/lower-bound/rounding/branch-and-bound bridge because it directly supports discrete planning and GCS/polytope work, or explicitly narrow the source claim. |
| O04-07 | P2 | The Simplex vertex claim and central-path duality-gap bound lack existence/convexity assumptions. | `UNPLANNED_GAP` | `:71,95`. Say an attained bounded LP has an optimal extreme point under the usual pointed/polyhedral conditions; state the convex barrier assumptions behind `mμ`. |
| O04-08 | P2 | The objective promises QP/SVM setup and Simplex understanding, but exercises test neither. | `UNPLANNED_GAP` | Five exercises cover convexity, barrier, LP recognition, central path, and AugLag only. Add one small QP formulation/solver-reading exercise; keep Simplex conceptual recall. |
| O04-09 | P2 | Visual and recall support are thin. | `UNPLANNED_GAP` | Restore/redraw central-path, polytope/LP, and SQP local-model figures; add keyed assumptions and method-selection recall. Four unkeyed prompts, 2/5 exports. |
| O04-10 | P2 | Modern convex modeling/problem-class recognition is absent. | `UNPLANNED_GAP` | Approved external benchmark Chapters 4–6 expose DCP-style composition and SOCP/SDP recognition. Add only a compact relevance-scoped bridge for later IRIS/GCS/control, not a general convex-analysis detour. |

## Phase 5 reconciliation

`PLAN-05` and UAC trajectory optimization make O04-06/10 more relevant, but they do not own the missing foundation. Revision 2.2 also does not own the factual repairs or full-block retrieval/figures. A compact convex-modeling/relaxation addition can remain inside OPT-04; splitting is justified only if the simultaneous differentiable-optimization source gap makes this page too dense.

Presentation verification: `STRUCTURE_VERIFIED`; representative source pages were visually checked and live desktop/mobile inspection remains deferred.
