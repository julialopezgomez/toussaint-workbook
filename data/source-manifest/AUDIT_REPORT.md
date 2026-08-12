# Phase 1 — Source Audit Report

Generated 2026-08-12, updated 2026-08-12 to add `Lecture-AI.pdf` and `Lecture-MachineLearning.pdf`. Source: `original notes/` (13 PDFs, TU Berlin, Marc Toussaint, Learning & Intelligent Systems Lab). All extraction is read-only; raw text lives in `data/source-manifest/raw-text/*.md`, one file per source, page boundaries preserved as `===== PAGE N =====` markers. Full machine-readable manifest: `data/source-manifest/manifest.json`.

## 1. Source Inventory

| ID | Title | Pages | TOC entries | Text quality | Notes |
|---|---|---|---|---|---|
| `lecture-maths` | Maths for Intelligent Systems | 104 | 145 | Excellent, text-based | Core math foundation course |
| `lecture-optimization` | Introduction to Optimization | 128 | 156 | Excellent, text-based | Full optimization course |
| `lecture-robotlearning` | Robot Learning | 137 | 133 | Excellent, text-based | Advanced/applied, most recent-feeling content |
| `lecture-robotics` | Introduction to Robotics | 201 | 49 | Excellent, text-based | Core robotics course |
| `energy` | Probabilities, Energy, Boltzmann & Partition Function | 3 | 3 | Excellent | Standalone note, undated author metadata |
| `entropy` | Entropy, Information, Cross-Entropy & ML as MDL | 2 | 3 | Excellent | Standalone note |
| `gaussians` | Gaussian Identities | 4 | 15 | Excellent | Reference/cheat-sheet-style note (2011, oldest source) |
| `quaternions` | Quaternions, Exponential Map, and Quaternion Jacobians | 5 | 7 | Excellent | Standalone note |
| `robotkin` | Robot Kinematics & Dynamics | 5 | 7 | Excellent | Standalone note, dense — background for Robot Learning + Robotics Lab |
| `splines` | Splines | 7 | 10 | Excellent | Standalone note |
| `svd` | Singular Value Decomposition | 2 | 0 (no embedded TOC, single flowing note) | Excellent | Standalone note |
| `lecture-ai` | Introduction to Artificial Intelligence | 219 | 246 | Excellent, text-based | Broadest, most modern source — ML+decisions, sequential decisions/RL (with convergence proofs), classical AI (search/CSP/logic/graphical models/HMM-Kalman/relational probabilistic models), LM reasoning/XAI |
| `lecture-machinelearning` | Introduction to Machine Learning | 139 | 40 | Excellent, text-based | Classical ML depth course — regression/classification/kernels/PCA/clustering/ensembles/probabilistic ML/GPs |

**Total: 956 pages across 13 sources.** No scanned/image-based pages detected (heuristic: 0 pages under 40 extracted characters in any source; average 900–3600 characters/page). **No OCR was necessary.** File hashes (SHA-256) recorded per source in `manifest.json` for future change detection — none of the source PDFs were modified during this audit.

**Systematic extraction artifact (not a content error):** internal LaTeX cross-references (`\ref`, `\eqref` to other equations/sections) render as literal `??` in the extracted text — this is a text-extraction limitation of stripped hyperref targets, not a defect in the source PDFs themselves (the PDFs display correct numbers when read visually). When a module cites a specific equation number, I will verify the true target against the live PDF at authoring time rather than trust the extracted `??`.

**Duplicate/overlapping material across sources** (full reasoning in §5 coverage matrix): the four short notes `gaussians`, `entropy`, `energy` overlap `lecture-maths` Ch. 5 (Probabilities & Information); `svd` overlaps `lecture-maths` §3.4–3.8; `quaternions` + `robotkin` overlap `lecture-robotics` Ch. 2–3 (Kinematics/Dynamics) and are explicitly referenced as background reading by `lecture-robotlearning` §1.3; `splines` is referenced directly by `robotkin` (footnote) as further reading; `lecture-optimization` is a full deep-dive superset of `lecture-maths` Ch. 4 (Optimization).

## 2. Concept Inventory (by source, section-level)

Derived from each PDF's embedded outline (LaTeX-generated, high confidence — not OCR-inferred). Full section trees below; sub-subsection granularity omitted here for brevity but present in `manifest.json` → `embedded_toc`.

**`lecture-maths`** — Speaking Maths (notation) · Functions & Derivatives (partial/total derivatives, chain rule, gradient/Jacobian/Hessian, Taylor expansion, matrix derivatives, numerical gradient checking) · Linear Algebra (vector spaces, dual vectors, tensors, SVD, eigendecomposition, covariant gradient) · Optimization (line search, Newton/Gauss-Newton/quasi-Newton/BFGS/CG, KKT, Lagrangian, convex problems, LP/QP, blackbox/Bayesian optimization) · Probabilities & Information (Bayes rule, standard distributions, Gibbs/Boltzmann, entropy/KL, Laplace approximation, variational inference, Fisher information) · Appendix: Gaussian identities.

**`lecture-optimization`** — Unconstrained optimization (gradient descent, line search, Wolfe conditions, Newton/Gauss-Newton/Levenberg-Marquardt/trust regions/quasi-Newton/BFGS/CG) · Constrained optimization (KKT, log-barrier, augmented Lagrangian, Lagrangian duality, convex/LP/QP, simplex, SQP, implicit function theorem & differentiable optimization) · Further topics (SGD + variants incl. Adam, No-Free-Lunch theorem, Gaussian processes, Bayesian optimization, evolutionary/blackbox methods incl. CMA-ES, structured/factored programs, ADMM, RL–optimization connection).

**`lecture-robotlearning`** — Robotics essentials recap (forward/inverse kinematics, inverse dynamics, MPC) · ML essentials recap (supervised/unsupervised) · Dynamics learning (parameter estimation, regression, residual/observation-based models, data generation) · Imitation learning (behavior cloning, DAgger, GAN/VAE/diffusion policies) · Reinforcement learning (MDP, Bellman, Q-iteration, policy gradient, deep RL tricks, reward engineering) · Offline RL & Sim2Real (domain randomization, privileged teacher) · Inverse RL (max-margin, max-entropy, adversarial, preference-based) · Manipulation & grasp learning (force closure, grasp data) · TAMP & language (logic-geometric programs, LLMs in TAMP) · Multi-robot learning (deep sets, GNNs, MARL).

**`lecture-robotics`** — Kinematics (3D geometry, forward/inverse kinematics, multi-task) · Dynamics (PID, 1D point mass, mechanical system dynamics, dynamic control) · Path planning (sampling-based, non-holonomic systems) · Path optimization · Probabilities (basics, distributions) · Mobile robotics (state estimation, SLAM) · Control theory (optimal control, controllability, stability) · RL in robotics (brief) · Grasping / legged locomotion (both marked "SKIPPED THIS TERM" by the source itself — brief intros only).

**`lecture-ai`** — *Part 1, ML & Decisions*: computation graphs/autograd/chain rule/Jacobians · probabilities (sets/random variables, entropy/cross-entropy/KL, joint/marginal/conditional, Gaussians, Monte Carlo/rejection/importance sampling, Bernoulli/Binomial/Beta/Multinomial/Dirichlet/conjugate priors/Student-t/exponential family, frequentist vs Bayesian) · supervised ML (regression, classification, regularization, linear models, neural nets incl. CNN/LSTM/init/dropout/data augmentation/SGD) · bandits & UCB1 (exploration/exploitation, contextual bandits). *Part 2, Sequential Decisions*: MCTS/UCT, value iteration & Bellman optimality, Q-iteration/Q-learning **with convergence proofs**, model-free vs model-based RL, policy gradient, exploration (R-Max, Bayesian RL), decision theory & value alignment. *Part 3, Discussions*: LM reasoning & RL finetuning (SFT, chain-of-thought), explainable AI (Pearl's causal networks/do-calculus, sensitivity analysis). *Part 4, Classical Lectures*: search (BFS/DFS/A\*), CSPs, graphical models (Bayes nets, variable elimination, belief propagation, junction tree, Gibbs sampling), dynamic models (HMM, Kalman filter), propositional & first-order logic, relational probabilistic modelling (STRIPS/PDDL, probabilistic rules, Markov Logic Networks).

**`lecture-machinelearning`** — Regression · Classification & structured output (discriminative functions, loss functions, logistic regression, conditional random fields) · Neural networks (computation graphs, images/time series) · Kernelization · Unsupervised learning (PCA/embeddings, clustering) · Local & ensemble learning (lazy learning, bagging/boosting-style combination) · Probabilistic ML (Bayesian ridge/kernel/logistic regression, Gaussian processes, Bayesian neural nets, No Free Lunch) · Appendix: probability basics.

**Short notes**: `energy` — energy functions, Boltzmann distribution, partition function, physical motivation. `entropy` — entropy as expected surprise, cross-entropy as ML loss, KL divergence, relation to MDL. `gaussians` — Gaussian definitions (moment & canonical form), matrix identities, products/convolution/marginals/conditionals of Gaussians, entropy/KL of Gaussians. `quaternions` — SO(3)/S³ representation, exponential/log maps, interpolation (SLERP), angular Jacobian w.r.t. quaternion parameters, random rotation sampling, Rodrigues' formula. `robotkin` — articulated multibody systems, forward kinematics & Jacobians, holonomic/non-holonomic constraints, Newton-Euler dynamics, standard control stack (waypoint → reference motion → controller), inverse kinematics as NLP. `splines` — knots/waypoints/control points terminology, cubic spline as optimal-control solution, timing-optimal control, Hermite splines, B-splines (definition, matrix form, waypoint-passing, gradients). `svd` — matrix as row/column space, SVD theorem, rank-1 decomposition.

## 3. Exercise Inventory

All exercises are **problem statements without embedded solutions** — I found no answer keys in any source (one isolated "Solution:" in `lecture-optimization` p.14 is a worked *example* inside the exposition, not an answer to a numbered exercise). This means every exercise carried into the workbook will need an authored rubric/solution during Phase 3+ production, clearly marked as newly authored (not sourced).

| Source | Exercise sets | Approx. individual sub-problems | Page range |
|---|---|---|---|
| `lecture-maths` | 8 sets (Ex. 1–11, some numbers reused across chapters) | ~25 | pp.19–20, 42–46, 75–82, 94–96 |
| `lecture-optimization` | 9 sets (Exercises 1–9) | ~30 | pp.110–125 |
| `lecture-robotics` | 13 sets (Exercise 1–11, 13, extra) | ~13+ (mostly single multi-part problems) | pp.178–194 |
| `lecture-robotlearning` | 9 sets (Weekly Exercise 1–7, 9, 10) | ~27 | pp.115–129 — mixes literature-review prompts, math derivations, and hands-on coding/simulation tasks |
| `lecture-ai` | 6 sets (Exercise 1–6) | ~19 | pp.206–214 — includes exactly what you asked for in Phase 0: "Computation Graphs and Chain Rule," "PyTorch Autograd," "Cross entropy loss and its derivatives," "Neural Network basics" (Ex.1–2), plus bandits, decision trees, value iteration, TD-learning |
| `lecture-machinelearning` | 12 sets (Exercise 1–12) | ~30+ | pp.113–135 |

Exercise topics span exactly the concept inventory above (e.g. `lecture-maths` Exercise 4/5 = multivariate calculus + finite-difference gradient checking + manual MLP backprop by hand — directly relevant to the ML manual-computation goal you set in Phase 0). Stable exercise IDs will be assigned during curriculum design (Phase 2) as `{source_id}-ex{N}-{subpart}`, preserving the original numbering in provenance metadata.

## 4. Preliminary Prerequisite Graph (source/topic level, revised with `lecture-ai` + `lecture-machinelearning`)

Adding these two sources changes the picture in three important ways, discovered by reading their tables of contents against what was already planned:

- **`lecture-ai` §1.2 (Probabilities) is the most complete probability treatment in the whole corpus** — it has everything `lecture-maths` Ch.5 has, plus Beta/Multinomial/Dirichlet/conjugate priors, particle approximation, rejection/importance sampling, and an explicit frequentist-vs-Bayesian discussion that nothing else in the corpus covers. It becomes the primary Probability Foundations source; `entropy.pdf`/`energy.pdf`/`gaussians.pdf` remain valuable for their first-principles motivation and identities but are now clearly supplementary to this, not co-primary.
- **`lecture-ai` Part 2 (Sequential Decisions) has rigorous RL foundations already in the corpus** — Bellman optimality, Q-iteration/Q-learning *with convergence proofs*, model-based vs. model-free, exploration strategies (R-Max, Bayesian RL). This substantially reduces the need for the external Sutton & Barto supplement flagged in the original audit — it's now a nice-to-have for extra depth/exercises, not a hard gap-filler.
- **`lecture-machinelearning` fills the "ML Foundations Bridge" gap** the original audit flagged as needing newly authored content — it has the classical regression/classification/kernels/PCA/clustering/ensembles/Bayesian-ML depth that was otherwise going to have to be authored from scratch. Combined with `lecture-ai` §1.1 (computation graphs/autograd/chain rule/Jacobians) and §1.3 (neural nets) — whose exercises literally include "PyTorch Autograd" and "Neural Network basics" — this is a much stronger foundation for the manual-MLP-to-PyTorch bridge you asked for in Phase 0 than the corpus originally offered.

`lecture-ai` Part 4 ("Classical Lectures": search, CSP, graphical models, HMM/Kalman filter, propositional & first-order logic, relational probabilistic models/PDDL/MLN) is a genuinely different flavor of material — classical/symbolic AI rather than continuous optimization/learning. See §6b below for how I'd prioritize it against your actual research area rather than teaching it uniformly.

```
Math Foundations (calculus refresher, linear algebra, SVD)
   │  [lecture-maths Ch.1-3; svd.pdf as intuition primer]
   ├──────────────► Optimization
   │                  [lecture-optimization; lecture-maths Ch.4]
   │
   ├──────────────► Probability & Information Theory  (primary source upgraded)
   │                  [lecture-ai §1.2 as primary; entropy/energy/gaussians.pdf + lecture-maths Ch.5 supplementary]
   │
   ├──────────────► ODEs & Dynamics Primer  (still NOT covered in sources — external supplement still needed)
   │                  │
   │                  ▼
   ├──────────────► Rigid-Body Rotations & Kinematics
   │                  [quaternions.pdf, robotkin.pdf]
   │                  │
   │                  ▼
   │              Robotics Core: Kinematics → Dynamics → Path Planning → Control → Mobile/SLAM
   │                  [lecture-robotics, + splines.pdf feeding Path Planning/Control]
   │                  (optionally deepened by lecture-ai Part 4: graphical models + Kalman filter → state estimation/SLAM)
   │
   ├──────────────► ML Foundations (upgraded — classical ML now has a real primary source)
   │                  [lecture-machinelearning: regression/classification/kernels/PCA/clustering/GPs/Bayesian ML]
   │                  │
   │                  ▼
   │              Neural Nets & Autodiff Bridge (manual MLP/backprop ↔ PyTorch)
   │                  [lecture-ai §1.1 + §1.3; lecture-maths Ch.2 exercises]
   │                  │
   │                  ▼
   └──────────────► RL Foundations  (upgraded — rigorous treatment now in-corpus)
                      [lecture-ai Part 2 as primary; lecture-robotlearning §1.8 as robotics-flavored bridge;
                       external Sutton & Barto now optional depth, not a hard requirement]
                      │
                      ▼
                  Robot Learning (capstone-adjacent, applied — your literature's home turf)
                      [lecture-robotlearning, minus its own recap sections]
                      │
                      ▼
                  Cumulative Capstone
```

This will be refined into concrete blocks/modules with explicit IDs during Phase 2 (curriculum design) — shown here to surface the overall shape. The one clear remaining gap is ODEs/dynamics foundations (still true after adding these two sources).

## 5. Coverage Matrix (source section → disposition)

| Source section | Disposition | Reasoning |
|---|---|---|
| `lecture-maths` Ch.1–3 (Speaking Maths, Functions & Derivatives, Linear Algebra) | **Included directly** | Core, no better alternative in corpus; directly addresses your stated calculus/linalg rustiness |
| `lecture-maths` Ch.4 (Optimization) | **Merged** with `lecture-optimization` | `lecture-optimization` is the fuller treatment of the same material; `lecture-maths` Ch.4's unique exercises (6–10) are preserved, cross-referenced |
| `lecture-maths` Ch.5 (Probabilities & Information) | **Merged** with `entropy.pdf`/`energy.pdf`/`gaussians.pdf` | Short notes give better first-principles motivation; `lecture-maths` supplies the optimization-connection (Laplace approx, Fisher info, variational inference) the short notes lack |
| `lecture-maths` App. A (Gaussian identities) | **Duplicate** of `gaussians.pdf` | `gaussians.pdf` is the fuller, better-organized version; keep as canonical cheat-sheet source |
| `lecture-optimization` (all) | **Included directly** | Primary optimization treatment |
| `lecture-robotics` Ch.1–2 (Intro, Kinematics) | **Included directly**, supplemented | Needs `quaternions.pdf`/`robotkin.pdf` for full derivation depth given your stated dynamics weakness |
| `lecture-robotics` Ch.3 (Dynamics) | **Included directly**, supplemented | Same — this is the weakest-covered area relative to your background; will need external ODE supplement before this chapter |
| `lecture-robotics` Ch.4–5 (Path Planning/Optimization) | **Included directly**, supplemented by `splines.pdf` | |
| `lecture-robotics` Ch.6 (Probabilities) | **Merged**/used as gentler on-ramp | More elementary than `lecture-maths` Ch.5; sequenced first as applied motivation |
| `lecture-robotics` Ch.7 (Mobile Robotics/SLAM) | **Included, demoted to Tier 4 (reference-only)** — *revised per your correction* | Confirmed not needed for your work (absent from your report's entire vocabulary); keep as a compact "know what it is" reference, not a full module route |
| `lecture-robotics` Ch.8 (Control Theory) | **Included directly, Tier 1** | Needs ODE supplement (stability, controllability rely on linear systems theory not derived from scratch in-source); directly matches your report's optimal control/MPC formalism (§2.2) |
| `lecture-robotics` Ch.9 (RL in Robotics, brief) | **Used as prerequisite/remediation** pointer forward | Deferred to the dedicated RL Foundations + Robot Learning blocks, which treat this properly |
| `lecture-robotics` Ch.10–11 (Grasping, Legged Locomotion) | **Included directly, Tier 2** — *revised per your correction, no longer excluded* | Despite source's own "SKIPPED THIS TERM" label, you confirmed these are relevant (manipulation/locomotion literature, your own manipulation-planner project) |
| `lecture-robotics` Ch.12 (Exercises), Ch.13 (Bullet-point summaries) | **Included directly**, distributed into relevant modules | Bullet points double as seed material for cheat sheets |
| `robotkin.pdf`, `lecture-robotics` Ch.2 (Kinematics) | **Included directly**, core, but paced as **revision** — *revised per your correction* | You taught Advanced Robotics at Edinburgh — open-chain kinematics/Jacobians/rotation matrices are refresher-level for you; keep exercises for revision value but don't over-expand exposition |
| `quaternions.pdf` | **Included directly**, core, **full-length treatment** — *revised per your correction* | Explicitly flagged by you as your weaker spot within rotations; explicitly named prerequisite reading by `lecture-robotlearning` §1.3 and directly targets your Phase-0 dynamics/manual-derivation goal |
| `svd.pdf` | **Included directly**, sequenced as intuition-first lead-in to `lecture-maths` §3.4–3.8 | Concrete-before-abstract, per your rustiness and the pedagogy the project spec requires |
| `splines.pdf` | **Included directly** | Bridges Path Planning/Control; referenced directly by `robotkin.pdf` |
| `lecture-robotlearning` §1.3–1.4 (Robotics/ML Essentials recap) | **Duplicate** of material covered properly elsewhere | Terse recap; superseded by the dedicated Robotics Core and ML Foundations Bridge blocks |
| `lecture-robotlearning` §1.8 (RL recap: MDP, Bellman, policy gradient) | **Used as prerequisite/remediation** pointer, **merged** with external RL Foundations block | Too terse alone for someone who wants derivation-level RL understanding; needs Sutton & Barto rigor first, then this recap serves as the robotics-flavored bridge |
| `lecture-robotlearning` §1.5–1.7, 1.9–1.13 (Dynamics/Imitation/Offline RL/Sim2Real/Inverse RL/Manipulation/TAMP/Multi-Robot Learning) | **Included directly** | Advanced/applied content with no equivalent elsewhere in corpus — the clear capstone-block content |
| All exercise sets (all 4 original lecture PDFs) | **Included directly** (adapted) | Interleaved into relevant modules per spec; solutions/rubrics newly authored since none exist in source |
| `lecture-ai` §1.1 (Computation Graphs/Autograd), §1.3 (Supervised ML/Neural Nets) | **Included directly**, becomes primary source for the manual-MLP-to-PyTorch bridge | Directly answers your Phase 0 ask; exercises literally titled "PyTorch Autograd," "Neural Network basics" |
| `lecture-ai` §1.2 (Probabilities) | **Included directly**, promoted to primary probability source | Most complete probability treatment in corpus (see §4); `lecture-maths` Ch.5 becomes supplementary cross-reference rather than primary |
| `lecture-ai` §1.4 (Bandits & UCB1) | **Included directly** | New topic, ties into exploration (RL) and Bayesian optimization (`lecture-optimization` §3.3) |
| `lecture-ai` Part 2 (Sequential Decisions/RL, incl. MCTS/UCT) | **Included directly**, promoted to primary RL-foundations source | Rigorous, with convergence proofs — reduces the external-RL-supplement need flagged earlier; directly relevant to your RL/skill-learning literature (Peng ASE, D'Ambrosio table tennis) |
| `lecture-ai` Part 3 (LM Reasoning/RLHF, Explainable AI) | **Included directly**, but placed as an optional/advanced branch, not the main route | Modern and interesting, but not what your current literature is about — lower priority, see §6b |
| `lecture-ai` Part 4 §4.3–4.4 (Graphical Models, Dynamic Models/HMM/Kalman filter) | **Included directly**, elevated to medium-high priority | Directly underpins state estimation/SLAM (`lecture-robotics` Ch.7) and connects to sampling-based methods in your advisor's own NLP-sampling paper |
| `lecture-ai` Part 4 §4.6–4.7 (First-Order Logic, Relational Probabilistic Models/PDDL/MLN) | **Included directly, elevated to Tier 1/2** — *revised per your correction* | Directly feeds TAMP/Logic-Geometric Programs (`lecture-robotlearning` §1.12) and your report's own task-level/motion-level split (§2.1.3); you confirmed Toussaint's long-horizon planning work uses exactly this |
| `lecture-ai` §4.5 (Propositional Logic) | **Included directly, Tier 2** — *revised per your correction* | Kept as the minimum needed to understand FOL/PDDL, not full puzzle-solving depth |
| `lecture-ai` §4.1 (Search: BFS/DFS/A\*) | **Included, compact, Tier 2** — *revised per your correction* | Kept specifically as an MCTS/UCT prerequisite (`lecture-ai` §2.1) — your literature includes MCTS (Khorrambakht `WorldPlanner`) |
| `lecture-ai` §4.2 (CSP) | **Included, low priority, Tier 4, remediation-branch only** | General CSP-solving heuristics (variable/value ordering) have the weakest connection to your work — kept accessible, off the main route |
| `lecture-ai` Exercises | **Included directly** (adapted) | Solutions/rubrics newly authored |
| `lecture-machinelearning` (all, minus GP/No-Free-Lunch overlap) | **Included directly**, becomes primary classical-ML source | Fills the gap the original audit flagged as needing newly authored content |
| `lecture-machinelearning` §8.1 (GPs), §8.3 (No Free Lunch) | **Duplicate** of `lecture-optimization` §3.2/§3.4 (Gaussian Processes, No Free Lunch) | Cross-referenced, taught once — `lecture-optimization`'s treatment is in the optimization context, `lecture-machinelearning`'s in the probabilistic-ML context; pick whichever module comes first in the final sequence as canonical and link the other |
| `lecture-machinelearning` Appendix A (Probability Basics) | **Duplicate** of `lecture-ai` §1.2, which is now primary | Superseded, kept only as a second-pass review reference |
| `lecture-machinelearning` Exercises | **Included directly** (adapted) | Solutions/rubrics newly authored |

**Gaps requiring external supplementation** (per your approval): ODE/dynamical-systems foundations (none of the sources teach ODEs from first principles — assumed background); rigorous RL foundations (MDP/Bellman/convergence proofs) beyond `lecture-robotlearning`'s terse recap — candidate: Sutton & Barto; classical robot dynamics/kinematics textbook treatment for cross-checking `robotkin.pdf`'s condensed derivations — candidate: Lynch & Park *Modern Robotics*, and/or Siciliano et al. *Robotics: Modelling, Planning and Control* (please confirm this is the "Severiano's" you meant).

## 5b. HTML source upgrade for the 7 short notes

Marc Toussaint's teaching site (`https://www.user.tu-berlin.de/mtoussai/teaching/`) publishes `energy`, `entropy`, `gaussians`, `quaternions`, `robotkin` (`robotKin.html`), `splines`, and `svd` as HTML pages with **hand-authored MathJax/LaTeX source** (`$...$`, `\[...\]`), each linking back to the identical PDF ("[pdf version]"). This is strictly more reliable for exact math transcription than text reconstructed from the PDF's glyph layout — no Unicode-approximation risk, exact LaTeX. Confirmed via the teaching page's link list that the 4 large lecture PDFs (`Lecture-Maths`, `Lecture-Optimization`, `Lecture-RobotLearning`, `Lecture-Robotics`) have **no** HTML twin — PDF-only, consistent with what you said.

Fetched read-only and stored at `data/source-manifest/html-text/*.md` (LaTeX-preserved plain text) with an index at `data/source-manifest/html-sources.json`. Pipeline: `scripts/ingest/fetch_html_notes.py`. This **resolves extraction uncertainty #3 below for these 7 sources** — module authoring for these topics should use the HTML-sourced LaTeX as the primary transcription reference, with the PDF version cited for page numbers (provenance still points to the PDF + page, since that's the citable, paginated artifact; the HTML text is used only to double-check exact symbol accuracy).

## 6. Extraction Uncertainties Needing Review

1. **Cross-reference numbers (`??`)** — systematic, described above; will be resolved per-module at authoring time by checking the live PDF page image, not blocking the audit.
2. **`svd.pdf` has no embedded TOC** (single flowing note, unlike the other 6 short notes which do) — not an error, just means its structure isn't machine-extractable; I read it in full manually (§2 above reflects that).
3. **Matrix/tensor-heavy pages** (e.g. `lecture-maths` §3.2–3.4, `robotkin.pdf` Newton-Euler derivation, `quaternions.pdf` Jacobian derivation) extracted with correct symbols in every sample I visually spot-checked, but I have not rendered/visually inspected every one of the ~598 pages as images — I'll do a targeted visual pass (render + inspect) on any page a module actually draws an equation from, during Phase 3 authoring, per the project's provenance/accuracy rules, rather than front-loading all 598 pages now. **For the 7 short notes this is now resolved** via the HTML/LaTeX source (§5b) — remaining exposure is limited to the 4 large lecture PDFs, which have no HTML twin.
4. **PDF metadata is sparse** — the 7 short notes have no `title`/`author` in PDF metadata (author is only in the visible text, "Marc Toussaint"); the 4 lecture PDFs do have proper metadata titles (used in §1 table).

No pages were flagged as low-quality/scanned/OCR-needed — this is a clean, fully text-based corpus.

## 6b. Priority Tiers Informed by Your Research (revised after your corrections + Year-1 report)

Original signal came from `Literature Notes/` folder titles (permission granted in Phase 0). You then corrected and sharpened it, and attached your CDT-D2AIR Year-1 Final Scientific Report ("Learning Representations of Reachable Behaviour for Planning in Long-Horizon Robotics Tasks," supervised by Dr. Steve Tonneau), which I read in part (intro, theoretical background, literature review structure) to ground the vocabulary precisely rather than guess. Your actual research core: **reachability-aware long-horizon planning** — TAMP, trajectory optimization & optimal control, MPC, predictive/world models (learned dynamics, latent state-space models), model-based and model-free RL (you cite Sutton & Barto directly — confirms that source), goal-conditioned/universal policies, manifold representations & constrained sampling, and compositional skill/motion-primitive learning. Current implementation work: an optimization-based manipulation planner over convex decompositions of $C_\text{free}$. Explicit corrections from you, applied below:

- **Grasping and legged locomotion are relevant — do not exclude them** for having been "SKIPPED THIS TERM" in `lecture-robotics`. Your literature includes agile locomotion (Corbères) and contact-rich manipulation (Zhu) directly, and your own current project is a manipulation planner. **Reclassified from "excluded" to "included," elevated priority** — see coverage matrix update below.
- **SLAM is genuinely not needed** — confirmed by the fact that your report's entire theoretical vocabulary (motion planning, control, predictive models) never touches state estimation/SLAM. **Demoted to Tier 4 (reference-only)** — keep the concept accessible, don't build a full module route through it.
- **Propositional/first-order logic and symbolic AI are relevant, not classical-AI trivia** — Toussaint's own long-horizon planning work (which your TAMP/Logic-Geometric-Program material in `lecture-robotlearning` §1.12 already touches) combines global symbolic planning with low-level motion planning, exactly the task-level/motion-level split your own report describes (§2.1.3). **Elevated to Tier 1/2**, but scoped specifically to what feeds TAMP — first-order logic, STRIPS/PDDL, relational probabilistic models/MLN, and enough propositional logic to understand FOL — not full general-purpose search/CSP-solving depth. Tree search fundamentals (BFS/DFS/A\*) get a partial exception: your literature includes MCTS (Khorrambakht `WorldPlanner`), and `lecture-ai` builds MCTS/UCT directly on top of basic tree search, so a compact treatment of tree search as an MCTS prerequisite stays in Tier 2; general CSP-solving heuristics (variable/value ordering) stay in Tier 4.
- **Core rigid-body kinematics/rotations get shortened, not skipped** — you taught Advanced Robotics at Edinburgh, so open-chain kinematics, Jacobians, and rotation matrices are refresher-only for you: keep the exercises (good revision, per your ask) but don't over-expand the exposition. **Quaternions specifically stay full-length** — you flagged this as your weaker spot within that area.

Revised priority tiers:

- **Tier 1 (core, main route, do first):** Math Foundations (esp. gradients/Jacobians/Hessians, linear algebra) → Optimization (`lecture-optimization`, full) → ODEs/Dynamics primer (external, still the one real gap) → Rigid-Body Kinematics/Rotations, kept compact except quaternions (`robotkin` as revision-paced, `quaternions` full-length) → Robotics Core: Kinematics/Dynamics/Path Planning & Optimization/Control Theory incl. optimal control & MPC-adjacent material (`lecture-robotics` Ch.2–5,8) → Splines/motion primitives → ML/Autodiff Bridge (`lecture-ai` §1.1, §1.3; `lecture-machinelearning`) → RL Foundations with MDP/Bellman/Q-learning formalism (`lecture-ai` Part 2) → Robot Learning capstone, esp. dynamics learning, manipulation & grasp learning, TAMP/Logic-Geometric Programs (`lecture-robotlearning`) → Manipulation planning / convex decomposition context (your own current project — connects directly here).
- **Tier 2 (main route, sequenced early since Tier 1 depends on it):** Probability & Information Theory (`lecture-ai` §1.2 as primary + `entropy`/`energy`/`gaussians`) — needed for Bayesian optimization, GPs, model uncertainty; Bandits & UCB1 alongside Bayesian Optimization (`lecture-optimization` §3.3); **Symbolic/logic foundations for TAMP** — propositional logic basics, first-order logic, STRIPS/PDDL, relational probabilistic models/MLN (`lecture-ai` §4.5–4.7); **tree search fundamentals as an MCTS prerequisite** (`lecture-ai` §4.1, kept compact); **grasping & legged locomotion** (`lecture-robotics` Ch.10–11, despite "skipped this term" label — directly relevant to your manipulation/locomotion literature).
- **Tier 3 (optional branch, reachable but not blocking):** classical ML breadth beyond the Autodiff Bridge (kernels, PCA/clustering, ensemble learning, No Free Lunch); LM Reasoning/RLHF & Explainable AI (`lecture-ai` Part 3) — modern, tangential to current work.
- **Tier 4 (reference-only, lowest priority):** **SLAM & state estimation** (`lecture-robotics` §7.1–7.2) — confirmed not needed, keep as a compact "know what it is" reference, not a full module; general CSP-solving techniques and puzzle-style propositional logic beyond what FOL needs.

This tiering will directly drive block/module ordering in Phase 2.

## 7. What's Next (pending your approval)

This closes Phase 1 (now covering 13 sources / 956 pages). Nothing else has been generated yet — no curriculum, no modules, no site scaffolding beyond the extraction pipeline itself (`workbook/scripts/ingest/`, `workbook/data/source-manifest/`, `workbook/.venv/`). Open items for **Phase 2 (curriculum & technical architecture proposal)**:

- Confirm the "Severiano's" reference (Siciliano et al.?) and finalize the external-source shortlist.
- **Confirm or correct the §6b priority-tier read** — this now materially affects block ordering, so I want your sign-off before locking it in.
- Turn the preliminary prerequisite graph above into concrete blocks/modules with IDs, learning objectives, and time estimates, honoring the priority tiers.
- Decide exact placement of the ODE/dynamics-foundations gap-filling material (new block before Robotics Core, most likely).
- Present the Astro+TypeScript technical architecture in more detail (content collections schema, exercise/grading component design) for your sign-off before the pilot module.
