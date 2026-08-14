# MATH-03B review — Scalar Products, Metric Tensors & Orthonormal Bases

Review state: `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Primary source checked: `lecture-maths`, pp28-31 §3.3
External benchmark: *Mathematics for Machine Learning*, Chapter 3, especially §§3.2-3.8; accessed 2026-08-14

## Verdict

The module usefully fills a real hole in Toussaint's notes by spelling out PSD/PD and Sylvester's criterion, then connects inner products, metric tensors, orthonormal bases, duals, and projections. Its three exercises are strong applications with complete feedback.

The opening motivation nevertheless repeats the false implication that PSD alone makes a stationary point a genuine minimum, and overstates PSD/PD as universally making ridge, Gauss-Newton, and Newton “well-posed.” It also collapses an abstract scalar product into “a PD matrix,” despite the preceding module's coordinate-free distinction: an inner product is represented by an SPD Gram/metric matrix only after choosing a basis. The external benchmark additionally exposes a relevant missing bridge from orthonormal projection to projection onto a general full-rank basis and least squares.

## Rubric scores

| Category | Score / 3 | Rationale |
|---|---:|---|
| Objective design | 3 | Clear, testable, and appropriately scoped. |
| Source fidelity | 3 | Declared source content is covered; additions are disclosed. |
| Technical correctness | 1 | PSD/minimum and coordinate-free/matrix equivalence claims need correction. |
| Prerequisite readiness | 3 | MATH-03 concepts are explicitly checked. |
| Sequence and links | 2 | Correct placement; eigenvalue proof incorrectly points to MATH-05. |
| Exposition and layout | 2 | Clear, but abstract distinctions are sometimes collapsed too aggressively. |
| Visual pedagogy | 1 | A metric-induced geometry/projection topic has no figure. |
| Exercises and feedback | 3 | Three well-aligned, fully solved exercises. |
| Retrieval support | 1 | No exercise recall cards and no answered direct recall. |
| Reference usefulness | 2 | Strong formulas, but general projection and caveats are absent. |

## Prioritized findings

| ID | Priority | Finding | Integration status | Evidence / disposition |
|---|---|---|---|---|
| M03B-01 | P1 | PSD is again treated as sufficient for a genuine local minimum and well-posed Newton/Gauss-Newton steps. | `UNPLANNED_GAP` | `MATH-03B.mdx:33-35`; align with the corrected second-order conditions in MATH-02 and distinguish PSD, PD, invertibility, and regularization. |
| M03B-02 | P1 | “A scalar product is exactly a PD matrix viewed as a 2-form” confuses an abstract bilinear map with its basis-dependent coordinate matrix. | `UNPLANNED_GAP` | `:50-61,94-99`. Say that every finite-dimensional inner product has an SPD Gram/metric representation in a chosen basis. |
| M03B-03 | P1 | The PSD/eigenvalue proof is routed to MATH-05 rather than MATH-04. | `UNPLANNED_GAP` | `:59`; exercise `MATH-04-ex7` is the actual destination. |
| M03B-04 | P2 | Frontmatter notation uses `v≻0/v≽0` “for a matrix.” | `UNPLANNED_GAP` | `:25`; replace `v` with `M` or `G`. |
| M03B-05 | P1 | Projection is only taught for orthonormal columns; the general full-rank formula and its least-squares interpretation are absent across the current block. | `UNPLANNED_GAP` | `:86-90`; external benchmark §3.8 derives `B(BᵀB)^{-1}Bᵀ`. Teach here or explicitly route through MATH-04's pseudoinverse. |
| M03B-06 | P2 | Metric geometry lacks a visual explanation. | `UNPLANNED_GAP` | No figure; add a static Euclidean-circle versus `G`-unit-ellipse diagram with projected directions. |
| M03B-07 | P2 | Recall support is absent. | `UNPLANNED_GAP` | Three answered derivation/application items, four unkeyed prompts, zero card exports. Add keyed PD/PSD, Sylvester, metric, and projection recall. |

Exercise inventory: 3 answered (0 direct recall, 2 application/short derivation, 1 synthesis), 4 unkeyed retrieval prompts, 3/3 solutions, 0/3 exercise-card exports.

## Tool recommendation

A metric/projection explorer could show how a `G`-unit circle becomes an ellipse and how the steepest/projection direction changes. It is CPU/browser-only and account-free. The simpler required intervention is a static ellipse/orthogonality figure plus one general-basis projection example.

## Phase 5 reconciliation

Revision 2.2 does not own these repairs. NUM-02 may provide batched matrix practice but does not teach general projections or fix PSD logic. The general-projection/numerical-solve work is a candidate for an expanded NUM block, subject to the block-level decision.

## Batched human decisions

- Approve the PSD and coordinate-free corrections as mandatory.
- Decide whether general projection is added here or routed to a new numerical-linear-algebra module.
- Extend keyed recall to this module during the block-wide assessment pass.

Owner approved the recommended defaults in decision `docs/decisions/0006-math-review-approved.md`; the next Phase 5 plan revision must absorb the open items. Presentation verification: `STRUCTURE_VERIFIED`; live desktop/mobile inspection remains pending.
