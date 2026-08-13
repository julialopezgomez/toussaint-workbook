// Single source of truth for block ordering/titles/rationale across the site
// (homepage, roadmap page, module breadcrumbs). Mirrors data/curriculum/CURRICULUM.md's
// Block Summary table — update both together if a block's framing changes.
export interface BlockMeta {
  id: string;
  title: string;
  rationale: string;
}

export const BLOCKS: BlockMeta[] = [
  { id: 'MATH', title: 'Math Foundations Refresher', rationale: 'Rusty calculus/linear algebra, rebuilt step-by-step rather than reviewed.' },
  { id: 'OPT', title: 'Optimization', rationale: "Matches your report's optimal-control formalism and current manipulation-planner work." },
  { id: 'PROB', title: 'Probability & Information Theory', rationale: 'Sequenced early: OPT-06, DYN, ML, and RL all depend on it.' },
  { id: 'ODE', title: 'ODEs & Dynamical Systems Primer', rationale: 'The one confirmed corpus gap, and your stated weakest area; directly gates Block DYN.' },
  { id: 'KIN', title: 'Rigid-Body Rotations & Kinematics', rationale: 'Revision-paced except quaternions, your flagged actual weak spot.' },
  { id: 'DYN', title: 'Robot Dynamics & Control', rationale: "Matches your report's Chapter 2.2 (Trajectory Optimisation, MPC) almost equation-for-equation." },
  { id: 'PLAN', title: 'Path & Motion Planning', rationale: "Formalizes configuration-space feasibility, matching your report's Definition 1." },
  { id: 'MANIP', title: 'Manipulation & Legged Locomotion Foundations', rationale: "Elevated per your correction; kept light given the source's own brief treatment." },
  { id: 'ML', title: 'ML & Autodiff Bridge', rationale: 'Manual MLP-by-hand alongside PyTorch, directly answering your Phase 0 ask.' },
  { id: 'RL', title: 'Reinforcement Learning Foundations', rationale: 'Rigorous treatment with convergence proofs, cross-checked against Sutton & Barto.' },
  { id: 'SYM', title: 'Symbolic Foundations for TAMP', rationale: "Feeds TAMP/Logic-Geometric Programs directly, matching your report's task/motion-level split." },
  { id: 'RLEARN', title: 'Robot Learning (capstone-adjacent)', rationale: 'The payoff block: advanced/applied content most directly aligned with your own research.' },
  { id: 'CAP', title: 'Capstone: Research Bridge', rationale: 'Connects the whole curriculum to your own CDT-D2AIR project, as a synthesis exercise.' },
];

export const BLOCK_ORDER = BLOCKS.map((b) => b.id);

export const BLOCK_TITLES: Record<string, string> = Object.fromEntries(BLOCKS.map((b) => [b.id, b.title]));
