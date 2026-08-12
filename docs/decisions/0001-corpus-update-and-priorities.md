# Decision Record 0001 — Corpus Update & Research-Aligned Priorities

Date: 2026-08-12 (same day as 0000, second pass after Phase 1 report was shown to user)

## Corpus addition
User added `Lecture-AI.pdf` (219pp, "Introduction to Artificial Intelligence") and `Lecture-MachineLearning.pdf` (139pp, "Introduction to Machine Learning") to `original notes/`, having forgotten them initially. Both extracted cleanly (PyMuPDF, text-based, no OCR needed — same pipeline as the original 11). Corpus is now **13 sources, 956 pages**. Full detail folded into `data/source-manifest/AUDIT_REPORT.md` (source inventory, concept/exercise inventory, prerequisite graph, coverage matrix all updated in place rather than appended separately).

Two consequences for the original Phase 1 gap analysis:
- `lecture-ai` Part 2 has rigorous RL foundations (Bellman optimality, Q-iteration/Q-learning with convergence proofs, model-based vs. model-free) — reduces reliance on the external Sutton & Barto supplement to "nice-to-have depth" rather than "required gap-filler."
- `lecture-machinelearning` fills what was flagged as needing newly-authored classical-ML content (regression, classification, kernels, PCA/clustering, ensembles, Bayesian ML/GPs).

The ODEs/dynamical-systems gap is unchanged — still needs external supplementation, unaffected by the new sources.

## Research-aligned prioritization
User shared their CDT-D2AIR Year-1 Final Scientific Report (`~/Downloads/Final_Scientific_Report_Julia Lopez Gomez.pdf`, 35pp) for grounding. Read in part (intro, theoretical background chapter, literature review structure — not the full literature review or later chapters). Confirmed:
- Title: "Learning Representations of Reachable Behaviour for Planning in Long-Horizon Robotics Tasks." Programme: CDT-D2AIR (Dependable and Deployable AI Robotics), joint Heriot-Watt/Edinburgh. Supervisor: Dr. Steve Tonneau.
- Research core: reachability-aware long-horizon planning, TAMP, trajectory optimization/optimal control, MPC, predictive/world models, model-based+model-free RL (standard MDP/Bellman/Q-function formalism, cites Sutton & Barto directly), goal-conditioned/universal policies, manifold representations/constrained sampling, compositional skill/motion-primitive learning.
- Current implementation: optimization-based manipulation planner over convex decompositions of C_free.
- This independently confirmed the earlier `Literature Notes/`-folder-based inference (trajectory/kinodynamic optimization, differentiable sim/MPC, contact-rich manipulation, sampling-based planning incl. advisor's own paper, MCTS/world models, applied RL) rather than contradicting it.

User's explicit corrections to the originally-proposed priority tiers:
1. **Grasping & legged locomotion** (`lecture-robotics` Ch.10–11, source-labeled "SKIPPED THIS TERM") — relevant, do not exclude. Reclassified included, Tier 2.
2. **SLAM/state estimation** (`lecture-robotics` Ch.7) — confirmed NOT needed ("I won't be doing it... good to know what it is"). Demoted to Tier 4, reference-only.
3. **Propositional/first-order logic, symbolic AI** — ARE relevant; Toussaint's long-horizon planning combines global symbolic planning with low-level motion planning (matches TAMP/Logic-Geometric Programs in `lecture-robotlearning` §1.12 and the user's own report's task-level/motion-level split). Elevated to Tier 1/2, scoped narrowly to what feeds TAMP (FOL, STRIPS/PDDL, relational probabilistic models/MLN, minimal propositional logic) — not general classical-AI breadth (general CSP-solving, puzzle-style logic stay Tier 4). Basic tree search (BFS/DFS/A*) kept as an MCTS prerequisite, Tier 2, since the user's literature includes MCTS-based work.
4. **Core rigid-body kinematics/rotations** — user taught Advanced Robotics at Edinburgh, is strong here (open-chain kinematics, Jacobians, rotation matrices) — pace as revision (keep exercises, don't over-expand exposition). **Exception: quaternions** — confirmed as the user's actual weak spot within this area, stays full-length.

Full 4-tier priority structure recorded in `data/source-manifest/AUDIT_REPORT.md` §6b, with corresponding coverage-matrix row updates.

## Status
This closes Phase 1 completely — corpus, coverage, and prioritization are all now confirmed by the user. Next action is Phase 2 (curriculum design + technical architecture), which should use §6b's tiers directly for block ordering without re-litigating them.
