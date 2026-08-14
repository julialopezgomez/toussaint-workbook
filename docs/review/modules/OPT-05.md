# OPT-05 review — Stochastic & Blackbox Optimization

Review state: `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Primary source checked: `lecture-optimization`, pp56–64 §§3.1–3.2

## Verdict

The SGD half is a useful bridge to ML: it includes two sampling modes, a hand calculation, a convergence-proof skeleton, adaptive updates, momentum, Adam, and a careful interpretation of No Free Lunch. All five exercises have solutions.

The title is materially misleading because no black-box optimizer is taught. The block later cites CMA-ES, while the source's derivative-free chapter is absent. The convergence theorem also omits required assumptions/step-size restrictions, and several optimizer explanations overclaim: stochastic gradients are not automatically unbiased for arbitrary sampling, mini-batches are not always `n` times cheaper, squared-gradient accumulators are not generally diagonal Hessians, and the generic Nesterov formula does not by itself guarantee `O(1/k²)`.

## Rubric scores

| Category | Score / 3 | Rationale |
|---|---:|---|
| Objective design | 2 | SGD/NFL objectives are strong; “blackbox” appears only in the title. |
| Source fidelity | 3 | The declared pp56–64 content is represented. |
| Technical correctness | 1 | Convergence and adaptive-optimizer claims need material qualifications. |
| Prerequisite readiness | 1 | OPT-02 is not the key prerequisite; probability/expectation/variance and sampling assumptions are not checked. |
| Sequence and links | 1 | It claims black-box preparation for OPT-06 without teaching a derivative-free method. |
| Exposition and layout | 3 | Clear progression from basic SGD to practical optimizers and NFL. |
| Visual pedagogy | 1 | No noisy-trajectory, variance, or adaptive-scaling visual. |
| Exercises and feedback | 3 | Five useful, fully solved exercises. |
| Retrieval support | 1 | Five unkeyed prompts and 2/5 exports. |
| Reference usefulness | 2 | Good update formulas, but assumptions are too easy to miss. |

## Prioritized findings

| ID | Priority | Finding | Integration status | Evidence / disposition |
|---|---|---|---|---|
| O05-01 | P1 | The SGD convergence theorem is missing unbiasedness, bounded-variance/lower-bound, conditioning, and step-size assumptions. | `UNPLANNED_GAP` | `OPT-05.mdx:87-100`. State expectations conditionally on the iterate, use a variance bound, and name the step-size restriction used in the descent inequality. Distinguish nonconvex stationarity from convex/strongly-convex rates. |
| O05-02 | P1 | The module title and OPT-06 readiness claim black-box optimization that is not taught. | `UNPLANNED_GAP` | Title; `OPT-06.mdx:40`; source §3.4 pp77–88 is absent from the curriculum. Add a focused derivative-free module (recommended) or rename this module and route black-box methods explicitly. |
| O05-03 | P1 | Sampling/unbiasedness and cost claims are overgeneralized. | `UNPLANNED_GAP` | `:52-83`. Uniform iid sampling gives an unbiased single-sample estimate for an average objective; shuffled epochs require careful conditional language, and a batch of size `b` is roughly `n/b`, not always `n`, times cheaper. |
| O05-04 | P2 | RMSprop/Adagrad are described as diagonal-Hessian estimates and exactly scale invariant. | `UNPLANNED_GAP` | `:102-114`. Squared gradients are second moments, not Hessian diagonals; scaling is approximate and broken by epsilon/transients. Present preconditioning as intuition, not equality. |
| O05-05 | P1 | The Nesterov `O(1/k²)` claim lacks the algorithmic schedule and smooth-convex assumptions. | `UNPLANNED_GAP` | `:114`. Tie the rate to the specific accelerated-gradient method, not any fixed-lookahead momentum update. |
| O05-06 | P2 | Prerequisite/readiness metadata does not test the concepts actually needed. | `PENDING_PLAN_RECONCILIATION` | Replace the Gauss-Newton-only readiness with expectation, variance, gradient, and sampling checks; the planned PROB-before-OPT route makes this straightforward. |
| O05-07 | P2 | Recall and visual intuition are sparse. | `UNPLANNED_GAP` | Add keyed assumption/update-choice recall and a static noisy-vs-full-batch trajectory/variance panel. Five answered exercises, five unkeyed prompts, 2/5 exports. |

## Phase 5 reconciliation

Revision 2.2 fixes PROB-before-OPT at Gate C/D but does not repair this module or add derivative-free optimization. The source-completeness and downstream CMA-ES dependency support a new relevance-scoped `OPT-05B` module covering random/multistart baselines, CMA-ES intuition, Nelder–Mead/pattern search boundaries, and evaluation-budget diagnostics. It should be CPU-first and need not reproduce the entire source chapter.

Presentation verification: `STRUCTURE_VERIFIED`; representative source pages were visually checked and live desktop/mobile inspection remains deferred.
