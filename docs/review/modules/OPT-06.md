# OPT-06 review — Bayesian Optimization & Bandits

Review state: `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Primary sources checked: `lecture-optimization`, pp71–77 §3.3; `lecture-ai`, pp45–51 §1.4

## Verdict

The module provides a compact and useful path from bandit uncertainty to GP-based global optimization, with five fully solved exercises. The GP conditioning explanation and acquisition comparison are particularly good.

The Bayesian-optimization convention is internally inconsistent: MPI/EI are written for minimization, but GP-UCB uses `μ+βσ` and is maximized, which favors large objective values. A minimization treatment needs lower confidence bound `μ-βσ` minimized (or its negation maximized). The GP posterior formulas also silently assume a zero prior mean, and UCB1's confidence/regret statements omit bounded/sub-Gaussian stationary-reward assumptions. The already verified PROB prerequisite ordering violation remains planned rather than current coverage.

## Rubric scores

| Category | Score / 3 | Rationale |
|---|---:|---|
| Objective design | 3 | Clear and well aligned with the major taught topics. |
| Source fidelity | 3 | Declared source topics and examples are represented. |
| Technical correctness | 1 | Minimization/UCB sign, zero-mean GP, and UCB assumptions require repair. |
| Prerequisite readiness | 1 | Readiness checks SGD rather than the two forward probability prerequisites. |
| Sequence and links | 1 | The live route reaches this module before PROB-01/05. |
| Exposition and layout | 3 | Strong conceptual bridge and compact formulas. |
| Visual pedagogy | 1 | Source GP sample/acquisition figures are omitted. |
| Exercises and feedback | 3 | Five varied, fully solved exercises. |
| Retrieval support | 1 | Four unkeyed prompts and 0/5 exports. |
| Reference usefulness | 2 | Useful formulas, but convention and numerical-solve assumptions need a safer table. |

## Prioritized findings

| ID | Priority | Finding | Integration status | Evidence / disposition |
|---|---|---|---|---|
| O06-01 | P1 | GP-UCB has the wrong sign/direction for the module's minimization convention. | `UNPLANNED_GAP` | `OPT-06.mdx:111-130`, cheat sheet. Use LCB `μ-βσ` with `argmin`, or define a maximized negative acquisition consistently; add a min/max convention table. |
| O06-02 | P1 | UCB1 confidence and logarithmic-regret claims omit their reward assumptions. | `UNPLANNED_GAP` | `:57-74`; `lecture-ai` p48 explicitly has outcomes in `[0,1]`. State stationary independent bounded/sub-Gaussian rewards and gap-dependent regret context; `β` is not a universal confidence guarantee. |
| O06-03 | P1 | GP posterior formulas omit the nonzero-mean correction. | `UNPLANNED_GAP` | `:78-92`. Either declare a zero-mean prior for the displayed equations or use `m(x)+kᵀ(K+σ²I)⁻¹(y-m(X))`. |
| O06-04 | P2 | The contextual-bandit ensemble paragraph overstates a heuristic as a direct UCB extension. | `UNPLANNED_GAP` | `:74`. Ensemble spread can be an uncertainty heuristic but is not automatically a calibrated confidence bound; cross-validation folds are not posterior samples. |
| O06-05 | P2 | Kernel/acquisition differentiability and numerical-solve conditions are absent. | `PENDING_PLAN_RECONCILIATION` | `:82,88-119`. State the valid `γ` range/convention, solve rather than invert, add jitter/conditioning, and qualify gradient/Hessian availability by kernel smoothness. `NUM-03` is the implementation owner once re-pinned. |
| O06-06 | P1 | The live sequence violates two declared prerequisites. | `PLANNED_TO_ADDRESS` | `PROB-01` and `PROB-05` occur after OPT. Phase 5 rev 2.2 explicitly swaps PROB before OPT and verified zero resulting violations. |
| O06-07 | P2 | GP and acquisition geometry is entirely textual. | `UNPLANNED_GAP` | Restore/redraw source pp74–75 panels showing kernel samples, posterior uncertainty, incumbent, and acquisition. An interactive is optional after static acceptance. |
| O06-08 | P2 | Retrieval/export coverage is absent. | `UNPLANNED_GAP` | Five answered exercises, four unkeyed prompts, 5/5 solutions, 0/5 card exports. Add keyed assumptions, GP-shape, and acquisition-choice recall. |

## Phase 5 reconciliation

The route defect is explicitly owned by revision 2.2. The UCB/GP repairs, static visual, retrieval work, and stable-solve bridge are not. The source material remains appropriate; no separate new BO module is justified.

Presentation verification: `STRUCTURE_VERIFIED`; representative source pages were visually checked and live desktop/mobile inspection remains deferred.
