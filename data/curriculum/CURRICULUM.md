# Phase 2 — Curriculum Design

Generated 2026-08-12. Derived from `data/source-manifest/AUDIT_REPORT.md` (source coverage) and its §6b priority tiers (confirmed by user, see `docs/decisions/0001-corpus-update-and-priorities.md`). This is the **planning artifact** for Gate 2 — it fixes IDs, sequencing, sources, and scope. Full lesson content (worked examples, hints, exercise text) is authored later, per module, in Phase 3 (pilot) and Phase 4 (batches).

## How to read this document

13 blocks, ~63 modules, one linear route. Each block table has columns: **ID** (stable, `{BLOCK}-{NN}`) · **Title** · **Source(s) & pages** (`p` = PDF page, `[html]` = also has a cleaner LaTeX source per the audit's §5b) · **Objective** (compressed to 1 line — full multi-part objectives are written when the module is authored) · **Prereqs** (module IDs) · **Hrs** (estimated study hours, calibrated to your stated rustiness/strengths from Phase 0 and the Edinburgh-teaching exception for core kinematics) · **Tier** (from §6b: 1=main route core, 2=main route but sequenced for dependency reasons, 3=optional branch, 4=reference-only branch).

**Mastery criteria policy** (stated once, not repeated 63 times): a module is "mastered" when you've completed its Core-tier exercises correctly (self-checked or Claude-reviewed per rubric) and can answer its retrieval questions without notes. Modules explicitly marked "derivation-heavy" additionally require completing at least one Challenge-tier derivation. Exact per-module mastery checklists are written at authoring time.

**Exercises used/created**: per the audit, **zero solutions exist anywhere in the source corpus**, so every exercise's rubric/solution is newly authored regardless of whether the question itself is source-adapted or new. Source-adapted exercises preserve original numbering in their provenance metadata (e.g. `lecture-maths-ex4-iii`).

**Obsidian connections**: your vault is mostly per-paper literature notes, not atomic concept notes, so most modules won't have a natural "connect to your notes" target. I've flagged the clear exceptions below at block level; the rest get resolved at authoring time by checking `Literature Notes/Definitions Database.md` and `References Database.md` for term overlap, per the project's original knowledge-mapping process — I won't force weak matches.

---

## Block Summary

| Block | Title | Tier | Modules | Est. hours | Key prereq blocks |
|---|---|---|---|---|---|
| MATH | Math Foundations Refresher | 1 | 6 | 15–18 | — |
| OPT | Optimization | 1 | 6 | 15–18 | MATH |
| PROB | Probability & Information Theory | 2 (sequenced early) | 6 | 12–15 | MATH |
| ODE | ODEs & Dynamical Systems Primer | 1 | 3 | 8–10 | MATH |
| KIN | Rigid-Body Rotations & Kinematics | 1 (revision-paced except quaternions) | 3 | 6–8 | MATH |
| DYN | Robot Dynamics & Control | 1 | 7 | 18–22 | MATH, ODE, KIN, OPT |
| PLAN | Path & Motion Planning | 1 | 4 | 9–11 | KIN, OPT |
| MANIP | Manipulation & Legged Locomotion Foundations | 2 | 2 | 4–5 | KIN, DYN |
| ML | ML & Autodiff Bridge | 1 | 7 | 17–20 | MATH, OPT, PROB |
| RL | Reinforcement Learning Foundations | 1 | 7 | 16–19 | PROB, ML |
| SYM | Symbolic Foundations for TAMP | 1/2 | 4 | 8–10 | — (light: PROB helps K4) |
| RLEARN | Robot Learning (capstone-adjacent) | 1 | 8 | 20–24 | DYN, PLAN, ML, RL, SYM, MANIP |
| CAP | Capstone: Research Bridge | 1 | 1 + final assessment | 6–8 | all of the above |

**Total: ~64 modules, ~154–188 estimated study hours** (roughly 4–5 months at 8–10 hrs/week, or however you choose to pace it — no deadline was set, so treat this purely as a sizing signal). Production happens in batches (Phase 4); you'll never face this whole list as a wall of unstarted content.

**Optional/reference-only branches** (reachable via links from the main route, not on it): LM Reasoning/RLHF & Explainable AI (off RL), SLAM & State Estimation (off PLAN), general Search/CSP beyond the MCTS prerequisite (off SYM). These get compact single-module treatments, not full sub-curricula.

---

## Block MATH — Math Foundations Refresher

Rationale: your Phase 0 background check flagged calculus/linear algebra as rusty, needing genuine step-by-step re-derivation rather than notation review. This block front-loads that, concrete-before-abstract (SVD gets an intuition-first pass via the short note before the fuller treatment).

| ID | Title | Source & pages | Objective | Prereqs | Hrs | Tier |
|---|---|---|---|---|---|---|
| MATH-00 | Taylor Expansion From Scratch | `lecture-maths` p14 (brief mention only) | Derive first- and second-order Taylor approximations from the definition of the derivative, not just recall the formulas | — | 2 | 1 |
| MATH-01 | Functions, Derivatives & the Chain Rule | `lecture-maths` p8–11 | Rebuild fluency computing partial/total derivatives and chain rules by hand, incl. computation-graph view | MATH-00 | 2.5 | 1 |
| MATH-02 | Gradients, Jacobians, Hessians & Taylor Expansion | `lecture-maths` p12–19 | Compute gradients/Jacobians/Hessians of vector-valued and matrix functions from scratch; numerically verify | MATH-01 | 3 | 1 |
| MATH-03 | Vector Spaces, Bases & Linear Maps | `lecture-maths` p21–30 | Reconstruct vector-space/basis/dual-space concepts and connect to matrices as coordinate representations | MATH-01 | 3 | 1 |
| MATH-04 | SVD & Eigendecomposition | `svd` [html] (intuition-first) → `lecture-maths` p31–39 + Ex.1–3 | Derive and interpret the SVD theorem geometrically; compute eigendecompositions by hand for small matrices | MATH-03 | 3 | 1 |
| MATH-05 | Covariant Gradient & Steepest Descent | `lecture-maths` p39–42 | Distinguish contravariant/covariant vectors; derive the steepest-descent direction under a metric | MATH-04 | 1.5 | 1 |

**Milestone**: Math Foundations Exam (see Assessment Schedule).

**Production note (Phase 4, post-batch-1)**: MATH-00 (Taylor Expansion From Scratch) was added after batch 1 shipped, once the user flagged that Taylor expansion was used as a derivation tool in both MATH-01 and MATH-02 without ever being taught from scratch. Inserted as "00" rather than renumbering MATH-01 through MATH-05, to avoid churning already-published IDs/cross-references for a late addition.

**Production note (Phase 4, batch 1)**: `lecture-maths` Exercises 4 and 5 (§2.7–2.8, "Backprop in a Neural Net") were originally scoped as MATH-02's own exercises but ended up used in [ML-03](/course/ML/ML-03) instead, since they fit thematically better alongside neural-network content and ML-03 was built first as a pilot. MATH-02 as actually authored uses newly-written exercises instead, covering the same gradient/Jacobian/Hessian mechanics without duplicating ML-03's material.

---

## Block OPT — Optimization

Rationale: Tier 1, directly matches your report's optimal-control formalism (Eq. 2.2) and current manipulation-planner work. `lecture-optimization` is the primary source (superset of `lecture-maths` Ch.4); its own exercises are used, cross-referenced against `lecture-maths`' unique ones.

| ID | Title | Source & pages | Objective | Prereqs | Hrs | Tier |
|---|---|---|---|---|---|---|
| OPT-01 | Unconstrained Optimization: Line Search & Newton | `lecture-optimization` p5–20; `lecture-maths` p47–58 | Derive gradient descent, backtracking line search, and the Newton direction; implement and compare | MATH-02 | 3 | 1 |
| OPT-02 | Gauss-Newton, Quasi-Newton & Conjugate Gradient | `lecture-optimization` p14–20 | Derive Gauss-Newton for least-squares; understand BFGS/CG as Hessian approximations | OPT-01 | 2.5 | 1 |
| OPT-03 | Constrained Optimization: KKT & the Lagrangian | `lecture-optimization` p21–34; `lecture-maths` p58–67 | Derive KKT conditions and the Lagrangian dual; solve small constrained problems on paper | OPT-01 | 3 | 1 |
| OPT-04 | Convex Problems, LP/QP, SQP & Log Barriers | `lecture-optimization` p23–29, p35–48 | Recognize/formulate LP/QP; derive log-barrier and augmented-Lagrangian methods | OPT-03 | 3 | 1 |
| OPT-05 | Stochastic & Blackbox Optimization | `lecture-optimization` p56–89 | Derive SGD/Adam convergence intuition; understand evolutionary/blackbox methods and the No-Free-Lunch theorem | OPT-02 | 2.5 | 1 |
| OPT-06 | Bayesian Optimization & Bandits | `lecture-optimization` p71–77; `lecture-ai` p45–51 (§1.4 Bandits/UCB1) | Derive UCB1 regret intuition; understand GP-based Bayesian optimization and acquisition functions | OPT-05, PROB-01 | 2.5 | 2 (bandits) / 1 (BayesOpt) |

**Milestone**: Optimization Exam. **Obsidian**: `antonova_Rethinking_2023` (differentiable optimization) and `amos_Differentiable_2019` (differentiable MPC) are high-confidence connections for OPT-04/OPT-01 respectively — flagged for linking at authoring time.

---

## Block PROB — Probability & Information Theory

Rationale: Tier 2 but sequenced early — OPT-06, DYN, ML, and RL all depend on it. `lecture-ai` §1.2 is now the primary source (most complete in corpus, confirmed in the audit); the short notes give first-principles motivation.

| ID | Title | Source & pages | Objective | Prereqs | Hrs | Tier |
|---|---|---|---|---|---|---|
| PROB-01 | Probability Foundations | `lecture-ai` p10–17 (§1.2 through Multivariate Distributions) | Rebuild fluency with Bayes' rule, joint/marginal/conditional distributions, standard distribution families | MATH-01 | 3 | 2 |
| PROB-02 | Monte Carlo & Sampling Methods | `lecture-ai` p18–19, p24–26 | Derive and implement rejection/importance sampling; understand particle approximations | PROB-01 | 2 | 2 |
| PROB-03 | Entropy, Cross-Entropy & KL Divergence | `entropy` [html] (primary); `lecture-ai` p12–14 | Derive entropy as expected surprise; connect cross-entropy to ML loss functions and KL to model error | PROB-01 | 2 | 2 |
| PROB-04 | Energy-Based Views & the Boltzmann Distribution | `energy` [html] | Derive the energy/probability correspondence from multiplicative-probability axioms | PROB-03 | 1.5 | 2 |
| PROB-05 | Gaussians: Identities & Manipulation | `gaussians` [html] (reference-style) | Derive and apply Gaussian product/marginal/conditional identities — this becomes a cheat-sheet-anchored module | PROB-01 | 2 | 2 |
| PROB-06 | Laplace Approximation, Variational Inference & Fisher Information | `lecture-maths` p92–96 | Derive the Laplace approximation as a 2nd-order Taylor expansion of log-probability; connect to Fisher information | PROB-05, MATH-02 | 1.5 | 2 |

**Milestone**: Probability Exam.

---

## Block ODE — ODEs & Dynamical Systems Primer

Rationale: the one confirmed gap — no source teaches this from first principles, and it's your stated weakest area, directly gating Block DYN. **Newly authored + externally sourced** (candidate: a standard ODE/dynamical-systems primer, to be finalized at authoring time — open question, see end of document).

| ID | Title | Source | Objective | Prereqs | Hrs | Tier |
|---|---|---|---|---|---|---|
| ODE-01 | First-Order ODEs: What They Are & How to Solve Them by Hand | External + newly authored | Solve separable and linear first-order ODEs manually; build the "what does a solution even mean" intuition | MATH-02 | 3 | 1 |
| ODE-02 | Linear Systems of ODEs, Eigenvalues & Stability | External + newly authored | Solve linear ODE systems via eigendecomposition (ties directly to MATH-04); connect eigenvalues to stability | ODE-01, MATH-04 | 3 | 1 |
| ODE-03 | Numerical Integration: Euler & RK4 | External + newly authored, coding lab | Implement and compare Euler/RK4 integrators; understand error accumulation — directly prepares robot-dynamics simulation | ODE-02 | 2 | 1 |

**Milestone**: folded into the DYN block's milestone rather than a standalone exam (ODE is a short, tightly-scoped primer, not a full course).

---

## Block KIN — Rigid-Body Rotations & Kinematics

Rationale: **revision-paced** per your Edinburgh Advanced Robotics teaching background — kept compact, exercises retained for genuine revision value — **except quaternions**, which stay full-length since you flagged that as your actual weak spot.

| ID | Title | Source & pages | Objective | Prereqs | Hrs | Tier |
|---|---|---|---|---|---|---|
| KIN-01 | 3D Rotations & Angular Velocity (revision) | `lecture-robotics` p14–17; `quaternions` [html] Appendix (Rodrigues' formula) | Refresh rotation matrices, SO(3), Rodrigues' formula, angular velocity — compact, exercise-forward | MATH-03 | 1.5 | 1 |
| KIN-02 | Quaternions: Exponential/Log Maps, Interpolation & Jacobians (full) | `quaternions` [html], full | Derive the quaternion exponential/log map, SLERP interpolation, and the angular Jacobian w.r.t. quaternion params | KIN-01 | 3 | 1 |
| KIN-03 | Forward/Inverse Kinematics & Jacobians (revision) | `robotkin` [html]; `lecture-robotics` p17–35 | Refresh forward-kinematics chaining, Jacobian construction, and IK as constrained optimization — compact | KIN-01, OPT-03 | 2.5 | 1 |

**Milestone**: folded into the DYN block's milestone (KIN is short and revision-paced by design).

---

## Block DYN — Robot Dynamics & Control

Rationale: Tier 1 core — directly matches your report's Chapter 2.2 (Trajectory Optimisation, MPC) almost equation-for-equation. This is where the ODE primer pays off.

| ID | Title | Source & pages | Objective | Prereqs | Hrs | Tier |
|---|---|---|---|---|---|---|
| DYN-01 | Deriving the Equations of Motion: Newton-Euler & Euler-Lagrange | `robotkin` [html] (both derivations) | Derive robot equations of motion two ways (Newton-Euler via Jacobians, Euler-Lagrange) and show they agree | KIN-03, ODE-02 | 3.5 | 1 |
| DYN-02 | PID & Point-Mass Control | `lecture-robotics` p37–41 | Derive the PD/PID closed-form solution; connect damping ratio/time-scale to gain choice | ODE-02 | 2 | 1 |
| DYN-03 | Inverse Dynamics & the Standard Control Stack | `lecture-robotics` p45–49; `robotkin` [html] (control stack) | Derive inverse dynamics from the equations of motion; understand the waypoint→reference-motion→controller stack | DYN-01, DYN-02 | 2.5 | 1 |
| DYN-04 | Optimal Control & Trajectory Optimization | `lecture-robotics` p90–91, p127–135 | Formulate and derive discrete-time optimal control (matches your report's Eq. 2.2 directly); connect to Gauss-Newton (OPT-02) | DYN-03, OPT-04 | 3 | 1 |
| DYN-05 | Splines & Motion Primitives | `splines` [html] | Derive the cubic-spline optimal-control solution; understand Hermite vs. B-spline parameterizations | DYN-04 | 2.5 | 1 |
| DYN-06 | Controllability & Stability | `lecture-robotics` p135–142 | Derive controllability rank conditions; connect Lyapunov-style stability to ODE-02's eigenvalue analysis | DYN-01, ODE-02 | 2.5 | 1 |
| DYN-07 | Model Predictive Control (MPC) | Synthesis module: `lecture-robotics` (optimal control) + your own report's Def. 3 as a direct cross-check | Derive the receding-horizon MPC formulation from DYN-04 and connect explicitly to your report's own notation | DYN-04, DYN-06 | 2.5 | 1 |

**Milestone**: Dynamics & Control Exam (also covers ODE + KIN as prerequisite material). **Obsidian**: `amos_Differentiable_2019` (differentiable MPC) is a strong match for DYN-07.

---

## Block PLAN — Path & Motion Planning

| ID | Title | Source & pages | Objective | Prereqs | Hrs | Tier |
|---|---|---|---|---|---|---|
| PLAN-01 | Configuration Space & Geometric Feasibility | `lecture-robotics` p52–67 | Formalize $C_\text{space}$/$C_\text{free}$/$C_\text{obs}$ — matches your report's Definition 1 exactly | KIN-03 | 2 | 1 |
| PLAN-02 | Sample-Based Path Finding (RRT/PRM family) | `lecture-robotics` p68–80 | Derive and compare sampling-based planners; understand completeness/optimality trade-offs | PLAN-01 | 2.5 | 1 |
| PLAN-03 | Non-Holonomic Systems | `lecture-robotics` p81–89; `robotkin` [html] (holonomic/non-holonomic constraints) | Distinguish holonomic/non-holonomic/integrable constraints; derive a simple non-holonomic example (car model) | PLAN-01, DYN-01 | 2 | 1 |
| PLAN-04 | Path Optimization | `lecture-robotics` p90–91 | Connect sampling-based paths to trajectory optimization (DYN-04) as a refinement step | PLAN-02, DYN-04 | 1.5 | 1 |

**Optional/reference branch (Tier 4, off this block)**: SLAM & State Estimation — `lecture-robotics` p93–125. Confirmed not needed for your work; kept as a single compact "know what it is" reference module, not a full sub-course. **Obsidian**: `ortiz-haro_iDbA_2025` (kinodynamic motion planning) is a strong match for PLAN-02/PLAN-04.

---

## Block MANIP — Manipulation & Legged Locomotion Foundations

Rationale: elevated per your correction — relevant despite the source's own "SKIPPED THIS TERM" label. Naturally light given how brief the source treatment is.

| ID | Title | Source & pages | Objective | Prereqs | Hrs | Tier |
|---|---|---|---|---|---|---|
| MANIP-01 | Grasping Fundamentals: Contacts & Force Closure | `lecture-robotics` p157–162 (brief intro); `lecture-robotlearning` p82 (Grasping Background/Contacts & Force Closure) | Understand contact modeling and the force-closure condition for stable grasps | DYN-01 | 2 | 2 |
| MANIP-02 | Legged Locomotion Basics | `lecture-robotics` p163–177 (brief intro) | Understand the basic gait/contact-sequencing view of legged locomotion | DYN-01, PLAN-03 | 2.5 | 2 |

**Obsidian**: `corberes_Complete_2025` (quadruped locomotion) is a strong match for MANIP-02; `zhu_Should_2025` (contact-rich manipulation) for MANIP-01.

---

## Block ML — ML & Autodiff Bridge

Rationale: this is the block that directly answers your Phase 0 ask (manual MLP-by-hand ↔ PyTorch). `lecture-ai` §1.1/§1.3 and `lecture-machinelearning` are now primary sources (audit finding — this used to be a gap requiring new authoring).

| ID | Title | Source & pages | Objective | Prereqs | Hrs | Tier |
|---|---|---|---|---|---|---|
| ML-01 | Computation Graphs & Automatic Differentiation | `lecture-ai` p5–9 (§1.1) | Derive forward/backward chain rule via computation graphs; connect to autograd | MATH-02 | 2.5 | 1 |
| ML-02 | Regression & Classical Supervised ML | `lecture-machinelearning` p12–34 | Derive least-squares regression and logistic regression from first principles | OPT-01, PROB-01 | 3 | 1 |
| ML-03 | Neural Networks: Manual Forward/Backward Pass ↔ PyTorch | `lecture-maths` p19–21 (Ex.4/5 Backprop); `lecture-ai` p28–36, p206–208 (Ex.1–2) | **Compute a small MLP's forward+backward pass entirely by hand, then reproduce it exactly in PyTorch line-by-line** | ML-01, ML-02 | 3.5 | 1 |
| ML-04 | Neural Network Architecture Essentials | `lecture-ai` p36–45 (CNN, LSTM, init, regularization, dropout, SGD) | Understand architectural building blocks and why each regularization trick exists | ML-03 | 2.5 | 1 |
| ML-05 | Kernelization & Gaussian Processes | `lecture-machinelearning` p50–53, p85–92; cross-ref `lecture-optimization` p67–70 | Derive the kernel trick; understand GPs as distributions over functions | ML-02, PROB-05 | 3 | 1 |
| ML-06 | Unsupervised Learning: PCA, Embeddings & Clustering | `lecture-machinelearning` p54–71 | Derive PCA via eigendecomposition (connects to MATH-04); understand clustering objectives | MATH-04, ML-02 | 2.5 | 1 |
| ML-07 | Advanced Topics: Ensembles, Bayesian NNs & No Free Lunch | `lecture-machinelearning` p72–84, p92–94 (Tier 3, optional) | Survey ensemble/local learning and Bayesian neural nets at a conceptual level | ML-04 | 2 | 3 |

**Milestone**: ML Foundations Exam. This is a strong pilot-module candidate for ML-03 — see the end of this document.

---

## Block RL — Reinforcement Learning Foundations

Rationale: Tier 1, `lecture-ai` Part 2 is now the primary source (rigorous, with convergence proofs — reduces reliance on the external Sutton & Barto supplement to optional depth, though it's still a great cross-check since your own report cites it).

| ID | Title | Source & pages | Objective | Prereqs | Hrs | Tier |
|---|---|---|---|---|---|---|
| RL-01 | MDPs, Value Functions & Bellman Equations | `lecture-ai` p67–71 | Formalize MDPs and derive the Bellman optimality equation — matches your report's Definition 5 exactly | PROB-01 | 2.5 | 1 |
| RL-02 | Value Iteration, Q-Iteration & Convergence | `lecture-ai` p71–72 | Derive value/Q-iteration and prove convergence | RL-01 | 2.5 | 1 |
| RL-03 | Model-Free RL: TD Learning & Q-Learning | `lecture-ai` p72–76 | Derive TD-learning and Q-learning updates, with convergence proof | RL-02 | 2.5 | 1 |
| RL-04 | Policy Gradient & Deep RL | `lecture-ai` p76–81; `lecture-robotlearning` p60–65 (robotics-flavored bridge) | Derive the policy gradient theorem; survey deep-RL tricks and robotics applications | RL-03, ML-04 | 3 | 1 |
| RL-05 | Exploration Strategies | `lecture-ai` p82–89 | Understand epsilon-greedy, R-Max, and Bayesian RL exploration strategies | RL-03 | 2 | 1 |
| RL-06 | Monte Carlo Tree Search & UCT | `lecture-ai` p52–66 (incl. compact tree-search prereq p112–121) | Derive UCT from basic tree search + UCB1 (OPT-06) — directly relevant to your MCTS-based literature | RL-02, OPT-06 | 2.5 | 2 |
| RL-07 | Decision Theory & Value Alignment (light touch) | `lecture-ai` p90–98 | Understand decision networks and the value-alignment framing at a conceptual level | RL-04 | 1.5 | 1 |

**Milestone**: RL Foundations Exam. **Optional/reference branch (Tier 3)**: LM Reasoning/RLHF & Explainable AI — `lecture-ai` p99–111.

---

## Block SYM — Symbolic Foundations for TAMP

Rationale: elevated per your correction — this directly feeds TAMP/Logic-Geometric Programs, matching your report's task-level/motion-level split (§2.1.3) and Toussaint's own long-horizon planning approach. Scoped narrowly: enough logic to understand FOL/PDDL, not general classical-AI breadth.

| ID | Title | Source & pages | Objective | Prereqs | Hrs | Tier |
|---|---|---|---|---|---|---|
| SYM-01 | Propositional Logic Essentials | `lecture-ai` p163–181 (scoped: syntax/semantics/inference basics only) | Understand propositional syntax/semantics/inference as the minimum needed for first-order logic | — | 1.5 | 2 |
| SYM-02 | First-Order Logic & Inference | `lecture-ai` p182–194 | Derive unification and forward/backward chaining for FOL | SYM-01 | 2.5 | 1 |
| SYM-03 | STRIPS, PDDL & Relational MDPs | `lecture-ai` p195–199 | Formalize STRIPS-style operators and PDDL, connecting symbolic actions to MDP transitions | SYM-02, RL-01 | 2.5 | 1 |
| SYM-04 | Probabilistic Relational Models & Markov Logic Networks | `lecture-ai` p199–205 | Understand PRMs/MLNs as a bridge between logic and probability | SYM-03, PROB-01 | 1.5 | 2 |

**Optional/reference branches (Tier 4, off this block)**: general CSP-solving techniques (`lecture-ai` p128–137) and graphical models beyond what SYM-04 needs (`lecture-ai` p138–162) — compact reference links, not full modules. A minimal tree-search treatment is instead placed in RL-06 where it's actually used (MCTS).

---

## Block RLEARN — Robot Learning (capstone-adjacent)

Rationale: the payoff block — `lecture-robotlearning`'s advanced/applied content has no equivalent elsewhere in the corpus and is the section most directly aligned with your own research and your advisor's work.

| ID | Title | Source & pages | Objective | Prereqs | Hrs | Tier |
|---|---|---|---|---|---|---|
| RLEARN-01 | Dynamics Learning | `lecture-robotlearning` p23–34 | Understand parameter estimation, dynamics regression, and residual dynamics learning | DYN-01, ML-04 | 2.5 | 1 |
| RLEARN-02 | Imitation Learning | `lecture-robotlearning` p35–56 | Derive behavior cloning; understand DAgger, distributional shift, and generative approaches (GAN/VAE/diffusion policies) | ML-04, RL-04 | 3 | 1 |
| RLEARN-03 | RL in Robotics: Reward Engineering & Deep RL Tricks | `lecture-robotlearning` p57–65 | Apply RL-04's foundations to robotics-specific reward design and data collection challenges | RL-04 | 2 | 1 |
| RLEARN-04 | Offline RL & Sim2Real | `lecture-robotlearning` p66–72 | Understand offline RL regularization and domain randomization for sim-to-real transfer | RLEARN-03 | 2.5 | 1 |
| RLEARN-05 | Inverse RL | `lecture-robotlearning` p73–80 | Derive max-margin and max-entropy IRL formulations | RL-04 | 2.5 | 1 |
| RLEARN-06 | Manipulation & Grasp Learning | `lecture-robotlearning` p81–87 | Connect MANIP-01's force-closure foundations to learned grasp-quality prediction | MANIP-01, RLEARN-01 | 2.5 | 1 |
| RLEARN-07 | Task and Motion Planning & Logic-Geometric Programs | `lecture-robotlearning` p88–99 | Synthesize SYM's symbolic tools with PLAN's motion planning into a full TAMP formulation — **the module most directly aligned with your research** | SYM-03, PLAN-02, OPT-04 | 3.5 | 1 |
| RLEARN-08 | Multi-Robot Learning (light touch) | `lecture-robotlearning` p100–114 (Tier 3, optional) | Survey Deep Sets/GNN/MARL approaches at a conceptual level | RLEARN-04 | 1.5 | 3 |

**Milestone**: Robot Learning Exam — the last milestone before the capstone. **Obsidian**: strong matches throughout — `peng_ASE_2022` (skill embeddings, RLEARN-02), `zhu_Should_2025` (RLEARN-06), `toussaint_NLP_2024` (RLEARN-07 — your advisor's own sampling-based TAMP paper), `dambrosio_ACHIEVING_2025` (RLEARN-03).

---

## Block CAP — Capstone: Research Bridge

Rationale: rather than an invented capstone project disconnected from your actual work, this connects the whole curriculum to your own CDT-D2AIR project (manipulation planning over convex decompositions of $C_\text{free}$, per your Year-1 report Chapter 5). It's framed as a synthesis/application exercise, not new taught content.

| ID | Title | Source | Objective | Prereqs | Hrs | Tier |
|---|---|---|---|---|---|---|
| CAP-01 | Research Bridge: Convex-Decomposition Manipulation Planning | Newly authored, scaffolded against your own report §5.1 (with your permission to reference it) | Walk through your own planner's pipeline (convex decomposition of $C_\text{free}$ → optimization-based planning) using the curriculum's own notation, as a self-check that the taught material actually transfers to your research | RLEARN-07, DYN-04, PLAN-01 | 3 | 1 |

Followed by the **Cumulative Final Assessment** (see below) — not a new module, the closing milestone of the whole route.

---

## Assessment Schedule

- **Entry diagnostic**: short, taken before MATH-01, to calibrate which Foundation-tier exercises can be skipped (e.g. if you're already comfortable with a specific derivative rule). Not a gate — informational only.
- **Lesson checks**: 1–2 quick retrieval questions inline after each module's core exposition (per the module-format spec) — not separately scheduled, built into every module.
- **Module mastery checks**: end of every module (per the mastery-criteria policy above).
- **Milestone examinations**: after each block, per the block tables above (MATH, OPT, PROB, DYN [covers ODE+KIN], ML, RL, RLEARN). PLAN/MANIP/SYM don't get standalone exams — their material is folded into the DYN and RLEARN milestones respectively, since they're shorter blocks that feed directly into those. Each milestone: conceptual explanation + derivation + calculation/modeling + one transfer-to-unfamiliar-example problem + a retake variant, per spec.
- **Cumulative reviews**: a short cumulative-review module inserted before RLEARN (reviewing MATH/OPT/PROB/DYN/KIN/ML/RL/SYM together, since RLEARN draws on all of them) and again before CAP.
- **Capstone**: CAP-01 (Research Bridge) followed by the **Cumulative Final Assessment** — mixed conceptual/derivation/modeling problems spanning the full route, with a remediation map linking any missed question back to its originating module.

---

## Open Decisions Before Phase 3 (Pilot)

1. **ODE external source**: I haven't picked a specific external ODE/dynamical-systems reference yet. Candidates: a standard engineering-math ODE text, or leaning on Lynch & Park's own background chapter (already an approved source) if it covers enough. I'll finalize this when I actually author Block ODE — flagging now so it's not a silent gap.
2. **Pilot module choice**: I'd propose **ML-03** (Neural Networks: Manual Forward/Backward Pass ↔ PyTorch) as the pilot — it's explicitly what you asked for in Phase 0, and structurally hits every pilot requirement (derivation, worked example, numeric + symbolic exercise, tiered hints, PyTorch cross-check, cheat-sheet link, mastery check). Alternative: **KIN-02** (Quaternions), your explicitly flagged weak spot, also derivation-rich. Let me know which you'd rather see first, or if you'd prefer a different module entirely.
3. Everything else in this document is presented for your approval — happy to adjust block boundaries, merge/split modules, or reorder before I lock this in and move to the technical architecture + pilot.
