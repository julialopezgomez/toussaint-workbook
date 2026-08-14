# OPT block review — optimization foundations

Review state: `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Modules: `OPT-01`, `OPT-02`, `OPT-03`, `OPT-04`, `OPT-05`, `OPT-06`

Owner decision: approved 2026-08-14 in `docs/decisions/0007-opt-review-approved.md`. Open reconciliation item: incorporate the approved MATH and OPT deltas into the next Phase 5 plan revision and re-pin it before Gate B is finalized.

## Block verdict

The block has an effective conceptual route from local descent through structured curvature and constraints to stochastic and Bayesian optimization. Its 34 embedded exercises all have matching solutions, worked examples are frequent, and the modules form a useful compact reference.

It is not yet safe as the optimization foundation for the planned robotics expansion. Material theorem and algorithm conditions are repeatedly omitted or misstated: the metric-constrained steepest direction is not normalized, Wolfe conditions are conflated, Newton damping behavior is reversed, Gauss–Newton is treated as automatically invertible, KKT necessity is asserted without a constraint qualification, log-barrier and SQP claims are incorrect, stochastic-convergence assumptions are absent, and Bayesian optimization mixes minimization with a maximization-form UCB rule. The cheat sheet repeats several of these issues.

Completeness is also materially overstated. The source manifest calls `lecture-optimization` a full included course, but the implemented block silently omits differentiable optimization, most derivative-free optimization, and the structured/distributed section. Two omissions clear the approved relevance test as main-route additions: differentiating through an optimizer/KKT system and evaluation-budget-aware derivative-free search. LP relaxations and modern convex problem-class recognition fit compactly inside `OPT-04`; ADMM can remain an optional reference unless a later distributed or multi-robot module needs it; the source's reinforcement-learning overlap should be routed to the RL blocks rather than duplicated.

## Module disposition

| Module | Current status | Strongest element | Main reason it remains partial |
|---|---|---|---|
| `OPT-01` | `CURRENTLY_PARTIAL` | Step-size → direction → curvature progression | False normalized-direction task and unsafe Wolfe/Newton/damping claims |
| `OPT-02` | `CURRENTLY_PARTIAL` | Strong least-squares/BFGS/CG comparison | Rank, conditioning, curvature, and convergence conditions missing |
| `OPT-03` | `CURRENTLY_PARTIAL` | Geometric KKT motivation and hand-solves | KKT necessity, force balance, stationarity, and saddle claims are overbroad |
| `OPT-04` | `CURRENTLY_PARTIAL` | Useful convexity-to-constrained-algorithm bridge | Incorrect hierarchy/barrier/SQP statements and omitted LP relaxations |
| `OPT-05` | `CURRENTLY_PARTIAL` | Clear SGD-to-Adam progression | Convergence assumptions absent and title promises black-box methods not taught |
| `OPT-06` | `CURRENTLY_PARTIAL` | Compact GP/acquisition comparison | UCB convention is inconsistent; GP/bandit assumptions and prerequisites are incomplete |

Detailed evidence is in `docs/review/modules/OPT-*.md`.

## Source and objective completeness

| Source/objective area | Judgment | Recommended disposition |
|---|---|---|
| Unconstrained descent, Newton, approximate Newton, BFGS, and CG, pp5–20 | Mostly covered | Repair assumptions, signs, normalization, and numerical-solve guidance; restore selected static geometry |
| KKT, barriers, augmented Lagrangian, duality, convexity, LP/QP/SQP, pp21–44 | Mostly covered but technically unsafe | Apply theorem/algorithm repairs; add compact LP-relaxation and convex problem-class bridge |
| Implicit functions and differentiable optimization, pp44–48 | Not covered | Add focused main-route `OPT-04B` after KKT/convex foundations |
| Phase I, bound constraints, and primal-dual appendix, pp49–55 | Not covered | Integrate only compact feasible-start and primal-dual/KKT-system context where needed; keep the rest reference depth |
| SGD, adaptive methods, and No Free Lunch, pp56–70 | Mostly covered | Repair assumptions and route probability readiness explicitly |
| GP/Bayesian optimization and bandits, pp67–77 plus AI §1.4 | Mostly covered | Repair acquisition convention, prior-mean and confidence assumptions, and stable implementation guidance |
| Evolutionary and derivative-free optimization, pp77–88 | Not covered | Add focused main-route `OPT-05B`; do not reproduce every named heuristic |
| Factored programs and ADMM, pp89–102 | Not covered | Optional/reference route now; promote only if later distributed or multi-robot work establishes a concrete dependency |
| RL–optimization connection, pp103–109 | Not covered in OPT | Explicitly route to RL/RLEARN; avoid duplicate teaching |
| Source exercises, pp110–125 | Selectively represented at best | Reuse only exercises that add missing executable intuition or transfer; do not pursue line-by-line reproduction |

The objective sets are therefore incomplete relative to the declared “full optimization course” source treatment. This finding remains relevance-scoped: an omitted source item is not automatically a required lesson. The proposed owners reflect downstream robotics, ML, or research value rather than source-page coverage for its own sake.

## Essential repair batch

Treat these as mandatory implementation repairs rather than optional enrichment:

1. Correct the normalized metric-steepest direction, descent sign, damping/trust-region limits, and strictly-convex-quadratic condition in `OPT-01`.
2. Separate Armijo, weak Wolfe, and strong Wolfe conditions and describe a line search that can actually enforce the selected condition.
3. State rank/damping/conditioning requirements for Gauss–Newton; distinguish linear from nonlinear CG; add the BFGS curvature condition.
4. State a constraint qualification for KKT necessity; distinguish stationarity from minimization of the Lagrangian and qualify global saddle/duality claims.
5. Correct the convex/quasiconvex language, log-barrier domain/limit, barrier-gradient sign, convex-QP condition, and SQP Hessian/globalization treatment.
6. State the sampling, unbiasedness, variance, smoothness, step-size, and problem-class assumptions behind SGD and accelerated-rate claims; describe adaptive squared gradients as moments rather than Hessian diagonals.
7. Make Bayesian-optimization min/max conventions internally consistent; declare the GP mean convention and bandit confidence assumptions.
8. Prefer linear solves/factorizations to displayed computational inverses, qualify sparsity and cubic-cost claims, and connect implementation to the approved `NUM-03` proposal.
9. Repair prerequisite/readiness metadata, especially probability before `OPT-05`/`OPT-06`, and correct source-range/full-course claims.
10. Propagate all repairs into the OPT cheat sheet, exercises, solutions, milestone, and any downstream references.

## Relevance-scoped additions

| Addition | Recommended owner | Route/depth | Why it clears the relevance bar |
|---|---|---|---|
| LP relaxation, bounds/rounding/branch-and-bound intuition | `OPT-04` | Main, compact | Direct prerequisite for discrete planning, GCS, and the owner's convex-decomposition work |
| DCP-style composition plus QP/SOCP/SDP recognition | `OPT-04` | Main/reference, compact | Supports IRIS, GCS, control, and solver choice without a general convex-analysis detour |
| Implicit Function Theorem and differentiating KKT/argmin systems | New `OPT-04B` | Main, CPU-first | Directly supports differentiable MPC, optimization layers, system identification, and modern robot learning |
| Feasible-start/Phase-I and primal-dual context | `OPT-04`/`OPT-04B` | Advanced compact boxes | Explains practical solver initialization and the KKT linear systems already used downstream |
| Derivative-free optimization and evaluation-budget diagnostics | New `OPT-05B` | Main, CPU-first | Repairs the title/dependency gap, teaches CMA-ES already cited downstream, and complements BO for expensive/noisy objectives |
| Multiplier sensitivity/shadow-price interpretation | `OPT-03` | Optional reference box | Makes multipliers operationally meaningful without adding a proof-heavy detour |
| Newton decrement/stopping | `OPT-01` | Optional reference box | Adds an invariant stopping concept that links naturally to stable solves |

`OPT-04B` should cover IFT conditions, differentiating a root/KKT system, one small CPU exercise, and failure modes at singular/active-set-changing points. `OPT-05B` should cover random/multistart baselines, CMA-ES intuition, Nelder–Mead or pattern-search boundaries, and evaluation budgets. It need not inventory every evolutionary heuristic in the source.

## Exercises, retrieval, and milestone

The six modules contain 34 answered exercises: approximately 6 foundation, 21 core, and 7 challenge items, with 15 short-text, 9 derivation, and 10 numeric answers. All 34 have solutions. Only 10/34 declare `reviewCardIds`, however, and the 26 end-of-module retrieval prompts are unkeyed. The block therefore has good worked practice but weak answerable recall.

Recommended action: preserve the useful derivations and numerics, repair the false/underqualified prompts, and add a compact keyed layer for conditions, method selection, failure modes, and notation. Do not impose a card-per-exercise ratio.

`OPT-EXAM` needs a block-level correction:

- frontmatter claims `OPT-01` through `OPT-06`, but no main question assesses `OPT-06`;
- BFGS/CG, optimizer-choice/NFL/Adam, GP/acquisition, and several constrained-method objectives are absent;
- the claim that every question combines modules or transfers beyond a worked case is false for the direct SGD-bound substitution;
- Part 1's retake switches from Newton/SQP to Gauss–Newton and changes remediation ownership instead of measuring the same learning target;
- Part 1 repeats the incorrect objective-Hessian-only SQP formulation;
- Part 3 assesses an underqualified convergence theorem.

Keep the sound small KKT and constrained-least-squares derivations, align each retake with its original target, and rebalance the milestone after `OPT-04B`/`OPT-05B` scope is finalized.

## Cheat sheet and reference layer

The OPT cheat sheet is concise and useful, but it repeats unsafe current statements: KKT as an unconditional characterization, `JᵀJ` without rank/damping context, inverse-based Newton/GP formulas, objective-Hessian-only SQP, and the overbroad SGD bound. Its decision tree also recommends CMA-ES as though `OPT-06` teaches it. Repair these in the same pass as the modules and route CMA-ES to `OPT-05B`.

The official Boyd–Vandenberghe text is a suitable optional external reference and benchmark for convexity, duality, Newton/line-search assumptions, and problem-class recognition. It should supplement rather than replace self-contained teaching.

## Visual and interactive teaching plan

Static visuals are the acceptance bar. Five reusable concepts cover the block without one figure per topic:

1. poorly scaled contours with gradient, Newton/damped-Newton, and accepted line-search steps (`OPT-01`);
2. residual/factor sparsity plus conjugate directions on contours (`OPT-02`);
3. feasible set, active-gradient cone/equality span, and KKT force balance (`OPT-03`);
4. LP/polytope, central path, and local SQP model (`OPT-04`/`OPT-04B`);
5. noisy versus full-batch trajectories and GP posterior/acquisition geometry (`OPT-05`/`OPT-06`).

Optional CPU/browser tools may include a quadratic condition-number explorer, a constrained central-path/KKT explorer, a stochastic-trajectory sampler, and a one-dimensional BO explorer. Build only those that materially improve intuition after the static figures are accepted and bundle/runtime cost is measured. The two proposed modules should include executable CPU exercises even if no interactive is approved.

Presentation is `STRUCTURE_VERIFIED`, not `VISUALLY_VERIFIED`. Representative source pages were rendered and visually inspected; live desktop/mobile workbook inspection remains deferred.

## Phase 5 reconciliation

Plan revision 2.2 already owns the `PROB`-before-`OPT` route correction and contains later consumers such as trajectory optimization, IRIS, and GCS. The approved MATH decision also proposes `NUM-03`. Those items increase the importance of a correct OPT foundation but do not own its repairs.

Recommended plan delta before Gate B is finalized:

- extend F0 to all P1 factual/theorem/link/prerequisite repairs in this record and their cheat-sheet/exam propagation;
- add `OPT-04B` and `OPT-05B` to the route, source matrix, objectives, prerequisites, assessments, and acceptance criteria;
- add the compact `OPT-04` LP-relaxation/conic-recognition bridge;
- route ADMM as optional/deferred and the source's RL material to RL/RLEARN;
- extend F8 to OPT-wide keyed recall, milestone repair, and the five static visual concepts;
- connect stable solves, rank, conditioning, and GP jitter to approved `NUM-03`;
- correct the source manifest's “included directly/full optimization course” interpretation so omissions are explicitly taught, routed, or scoped out.

## Batched owner approval

Approved in full: the essential-repair batch, both new focused modules (`OPT-04B`, `OPT-05B`), the compact `OPT-04` relaxation/problem-class bridge, whole-block keyed recall, milestone/cheat-sheet corrections, and five static visual concepts. Interactives remain optional; ADMM remains optional/deferred; the RL overlap is routed to RL/RLEARN; live visual approval remains deferred.

Approval accepts the review baseline and required Phase 5 delta. It does not make the current block complete: implementation and re-review remain separate later stages.
