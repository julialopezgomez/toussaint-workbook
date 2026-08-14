# Workbook review index

Status: **calibration, Gate A, MATH, and OPT approved; Phase 5 update pending; PROB review next**
Committed baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Inventory: 15 blocks, 69 modules, 100 generated pages

## Review states

- `NOT_STARTED` — no evidence-based module record yet.
- `CALIBRATION_DRAFT` — AI review complete enough to calibrate the protocol.
- `HUMAN_REVIEW_PENDING` — owner decisions or live visual checks remain.
- `APPROVED` — owner accepts the record as the planning baseline.
- `PLAN_RECONCILIATION_PENDING` — current-state review approved; expansion mapping remains.
- `RECONCILED_WITH_OPEN_ITEMS` — findings have been mapped to a stable plan, but identified conflicts or unowned details remain.
- `RECONCILED` — every finding in the reviewed scope has a plan owner or an explicit scope disposition; implementation is still pending.

## Calibration artifacts

| Artifact | Purpose | State |
|---|---|---|
| [REVIEW_PROTOCOL.md](./REVIEW_PROTOCOL.md) | Rubric, evidence rules, exercise philosophy, workflow | `APPROVED` |
| [EXTERNAL_BENCHMARK_PROPOSAL.md](./EXTERNAL_BENCHMARK_PROPOSAL.md) | Controlled review corpus | `APPROVED` |
| [CURRICULUM_COVERAGE.md](./CURRICULUM_COVERAGE.md) | Cross-module/source/objective coverage ledger | MATH/OPT `APPROVED`; plan update pending; calibration `RECONCILED` |
| [MATH-02B review](./modules/MATH-02B.md) | Matrix-calculus calibration | `APPROVED` / `RECONCILED` |
| [KIN-02 review](./modules/KIN-02.md) | Quaternion calibration | `APPROVED` / `RECONCILED` |
| [RLEARN-02 review](./modules/RLEARN-02.md) | Imitation-learning calibration | `APPROVED` / `RECONCILED` |
| [Decision 0006](../decisions/0006-math-review-approved.md) | Owner approval and Phase 5 delta for the MATH block | `APPROVED` |
| [Decision 0007](../decisions/0007-opt-review-approved.md) | Owner approval and Phase 5 delta for the OPT block | `APPROVED` |

## Completed block-review artifacts

| Artifact | Scope | State |
|---|---|---|
| [MATH block review](./blocks/MATH.md) | Eight modules, source/objective coverage, exercises, cheat sheet, milestone, sequence, external gaps, and Phase 5 reconciliation | `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS` |
| [OPT block review](./blocks/OPT.md) | Six modules, source/objective coverage, exercises, cheat sheet, milestone, sequence, external gaps, and Phase 5 reconciliation | `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS` |

## Full module inventory

Tier is the current frontmatter tier. Two states distinguish a completed AI evidence record from the outstanding batched owner decision.

| Block | Module | Tier | Title | Review state |
|---|---|---:|---|---|
| MATH | MATH-00 | 1 | Taylor Expansion From Scratch | `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS` |
| MATH | MATH-01 | 1 | Functions, Derivatives & the Chain Rule | `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS` |
| MATH | MATH-02 | 1 | Gradients, Jacobians, Hessians & Taylor Expansion | `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS` |
| MATH | MATH-02B | 1 | Matrix Calculus: Identities, Warm-Ups & Applied Examples | `APPROVED` / `RECONCILED` |
| MATH | MATH-03 | 1 | Vector Spaces, Dual Spaces & Coordinate Transformations | `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS` |
| MATH | MATH-03B | 1 | Scalar Products, Metric Tensors & Orthonormal Bases | `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS` |
| MATH | MATH-04 | 1 | SVD, Eigendecomposition & the Power Method | `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS` |
| MATH | MATH-05 | 1 | Covariant Gradient & Steepest Descent | `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS` |
| OPT | OPT-01 | 1 | Unconstrained Optimization: Line Search & Newton | `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS` |
| OPT | OPT-02 | 1 | Gauss-Newton, Quasi-Newton & Conjugate Gradient | `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS` |
| OPT | OPT-03 | 1 | Constrained Optimization: KKT & the Lagrangian | `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS` |
| OPT | OPT-04 | 1 | Convex Problems, LP/QP, SQP & Log Barriers | `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS` |
| OPT | OPT-05 | 1 | Stochastic & Blackbox Optimization | `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS` |
| OPT | OPT-06 | 2 | Bayesian Optimization & Bandits | `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS` |
| PROB | PROB-01 | 2 | Probability Foundations | `NOT_STARTED` |
| PROB | PROB-02 | 2 | Monte Carlo & Sampling Methods | `NOT_STARTED` |
| PROB | PROB-03 | 2 | Entropy, Cross-Entropy & KL Divergence | `NOT_STARTED` |
| PROB | PROB-04 | 2 | Energy-Based Views & the Boltzmann Distribution | `NOT_STARTED` |
| PROB | PROB-05 | 2 | Gaussians: Definition, Identities & Manipulation | `NOT_STARTED` |
| PROB | PROB-06 | 2 | Laplace Approximation, Variational Inference & Fisher Information | `NOT_STARTED` |
| ODE | ODE-01 | 1 | First-Order ODEs: What They Are & How to Solve Them by Hand | `NOT_STARTED` |
| ODE | ODE-02 | 1 | Linear Systems of ODEs, Eigenvalues & Stability | `NOT_STARTED` |
| ODE | ODE-03 | 1 | Numerical Integration: Euler & RK4 | `NOT_STARTED` |
| KIN | KIN-01 | 1 | 3D Rotations & Angular Velocity (revision) | `NOT_STARTED` |
| KIN | KIN-02 | 1 | Quaternions: Exponential/Log Maps, Interpolation & Jacobians | `APPROVED` / `RECONCILED` |
| KIN | KIN-03 | 1 | Forward/Inverse Kinematics & Jacobians (revision) | `NOT_STARTED` |
| DYN | DYN-01 | 1 | Deriving the Equations of Motion: Newton-Euler & Euler-Lagrange | `NOT_STARTED` |
| DYN | DYN-02 | 1 | PID & Point-Mass Control | `NOT_STARTED` |
| DYN | DYN-03 | 1 | Inverse Dynamics & the Standard Control Stack | `NOT_STARTED` |
| DYN | DYN-04 | 1 | Optimal Control & Trajectory Optimization | `NOT_STARTED` |
| DYN | DYN-05 | 1 | Splines & Motion Primitives | `NOT_STARTED` |
| DYN | DYN-06 | 1 | Controllability & Stability | `NOT_STARTED` |
| DYN | DYN-07 | 1 | Model Predictive Control (MPC) | `NOT_STARTED` |
| PLAN | PLAN-01 | 1 | Configuration Space & Geometric Feasibility | `NOT_STARTED` |
| PLAN | PLAN-02 | 1 | Sample-Based Path Finding: PRM & RRT | `NOT_STARTED` |
| PLAN | PLAN-03 | 1 | Non-Holonomic Systems | `NOT_STARTED` |
| PLAN | PLAN-04 | 1 | Path Optimization: From Sampled Paths to Smooth Trajectories | `NOT_STARTED` |
| MANIP | MANIP-01 | 2 | Grasping Fundamentals: Contacts & Force Closure | `NOT_STARTED` |
| MANIP | MANIP-02 | 2 | Legged Locomotion Basics | `NOT_STARTED` |
| ML | ML-01 | 1 | Computation Graphs & Automatic Differentiation | `NOT_STARTED` |
| ML | ML-02 | 1 | Regression & Classical Supervised ML | `NOT_STARTED` |
| ML | ML-03 | 1 | Neural Networks: Manual Forward/Backward Pass ↔ PyTorch | `NOT_STARTED` |
| ML | ML-04 | 1 | Neural Network Architecture Essentials | `NOT_STARTED` |
| ML | ML-05 | 1 | Kernelization & Bayesian Learning | `NOT_STARTED` |
| ML | ML-06 | 1 | Unsupervised Learning: PCA, Embeddings & Clustering | `NOT_STARTED` |
| ML | ML-07 | 3 | Advanced Topics: Ensembles, Bayesian NNs & No Free Lunch | `NOT_STARTED` |
| RL | RL-01 | 1 | MDPs, Value Functions & Bellman Equations | `NOT_STARTED` |
| RL | RL-02 | 1 | Value Iteration, Q-Iteration & Convergence | `NOT_STARTED` |
| RL | RL-03 | 1 | Model-Free RL: TD Learning & Q-Learning | `NOT_STARTED` |
| RL | RL-04 | 1 | Policy Gradient & Deep RL | `NOT_STARTED` |
| RL | RL-05 | 1 | Exploration Strategies | `NOT_STARTED` |
| RL | RL-06 | 2 | Monte Carlo Tree Search & UCT | `NOT_STARTED` |
| RL | RL-07 | 1 | Decision Theory & Value Alignment | `NOT_STARTED` |
| SYM | SYM-01 | 2 | Propositional Logic Essentials | `NOT_STARTED` |
| SYM | SYM-02 | 1 | First-Order Logic & Inference | `NOT_STARTED` |
| SYM | SYM-03 | 1 | STRIPS, PDDL & Relational MDPs | `NOT_STARTED` |
| SYM | SYM-04 | 2 | Probabilistic Relational Models & Markov Logic Networks | `NOT_STARTED` |
| REV1 | REV1-01 | 1 | Cumulative Review: The Foundations Stack | `NOT_STARTED` |
| RLEARN | RLEARN-00 | 1 | Robot Learning: Taxonomy & Landscape | `NOT_STARTED` |
| RLEARN | RLEARN-01 | 1 | Dynamics Learning | `NOT_STARTED` |
| RLEARN | RLEARN-02 | 1 | Imitation Learning | `APPROVED` / `RECONCILED` |
| RLEARN | RLEARN-03 | 1 | RL in Robotics: Reward Engineering & Deep RL Tricks | `NOT_STARTED` |
| RLEARN | RLEARN-04 | 1 | Offline RL & Sim2Real | `NOT_STARTED` |
| RLEARN | RLEARN-05 | 1 | Inverse RL | `NOT_STARTED` |
| RLEARN | RLEARN-06 | 1 | Manipulation & Grasp Learning | `NOT_STARTED` |
| RLEARN | RLEARN-07 | 1 | Task and Motion Planning & Logic-Geometric Programs | `NOT_STARTED` |
| RLEARN | RLEARN-08 | 3 | Multi-Robot Learning (light touch) | `NOT_STARTED` |
| REV2 | REV2-01 | 1 | Cumulative Review: Robot Learning | `NOT_STARTED` |
| CAP | CAP-01 | 1 | Research Bridge: Convex-Decomposition Manipulation Planning | `NOT_STARTED` |

## Proposed review order

1. Owner reviews the three calibration records and approves or modifies the protocol.
2. Owner approves the external benchmark corpus.
3. Record Claude's stable expansion-plan path/revision and reconcile the calibration findings.
4. Incorporate approved decisions 0006 and 0007 into the next Phase 5 plan revision and re-pin the review before Gate B is finalized.
5. Continue the independent review in curriculum order: PROB → ODE → KIN → DYN → PLAN → MANIP → ML → RL → SYM → REV1 → RLEARN → REV2 → CAP.
6. At every block boundary, audit the cheat sheet, exam, source coverage, prerequisite edges, and cumulative retrieval balance before accepting the block.
7. After all blocks, perform an objective-level whole-curriculum pass and a second plan reconciliation; module records alone cannot establish global completeness.

## Build and visual-verification record

- A clean archive of the committed baseline was built, rather than the dirty working tree.
- `npm run build` succeeded: 100 pages, including all 69 module routes; Pagefind indexed 20,209 words.
- Generated markup and heading/exercise/table structure were inspected for the calibration pages.
- Source PDFs were rendered and visually checked across the declared ranges.
- Live desktop/mobile page appearance is `STRUCTURE_VERIFIED`, not `VISUALLY_VERIFIED`, and remains a human calibration action.

## Expansion-plan record

| Field | Value |
|---|---|
| Plan path/URL | `docs/plans/PHASE5_AUGMENTATION_PLAN.md` |
| Revision/date | Revision 2.2, 2026-08-14 |
| Pinned SHA-256 | `412b807536da6d90b1063ad800aadf5435a6e05eabe6e3cfcd6ea65ac308f2f3` |
| Reconciled by | Codex review process, 2026-08-14 |
| Calibration findings absorbed | All calibration findings assigned to F0, NUM, later visual/retrieval work, Gate B, or explicit scope decisions; see module records |
| Later approved deltas | Decisions 0006 and 0007 add MATH/OPT foundation stabilization, `NUM-03`, `OPT-04B`, and `OPT-05B`; incorporation is pending |
| Conflicts/duplicates | Revision 2.2's “not missing theory” thesis and 102-module/33-addition counts are obsolete after the approved MATH/OPT audits |
| Owner approval | Review defaults, benchmark corpus, calibration verdicts, and MATH/OPT block dispositions approved 2026-08-14 |

## Gate A review status

`GATE_A_BASELINE.md`, `gate-a-concept-depth-inventory.json`, and the reporter script were re-inspected after the correction pass. The committed baseline is independently reproduced from an isolated archive; the dirty-tree comparison is separately labelled; the 308-concept inventory covers all 69 modules without fabricating semantic per-concept depth; reporter status and exit behavior are honest; and readiness/Anki results are queues rather than automatic semantic failures.

Gate A is **review-validated and owner-approved**; decision record: `docs/decisions/0005-gate-a-approved.md`. Revision 2.2 contains only the two approved P3 label corrections and does not reopen the rev-2.1 evidence baseline. The already approved review benchmark corpus is not the same decision as Gate B's production source corpus.
