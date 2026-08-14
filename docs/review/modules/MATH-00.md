# MATH-00 review — Taylor Expansion From Scratch

Review state: `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Primary source checked: `lecture-maths`, p14 §2.3.3 (supplementary)
External benchmark: Deisenroth, Faisal & Ong, *Mathematics for Machine Learning* (official 2024-01-15 PDF), §§5.1.1, 5.8; accessed 2026-08-14

## Verdict

This is an effective two-hour on-ramp: it starts from a derivative, builds the first two Taylor terms, gives two numerical examples, and provides complete feedback for four exercises. Because the declared Toussaint source contains only a brief formula, the newly authored derivations are a legitimate expansion rather than a source omission.

The main weakness is conceptual boundary-setting. The page uses “Taylor expansion,” “Taylor approximation,” and “Taylor series” almost interchangeably and says additional orders typically shrink error, but never distinguishes a finite Taylor polynomial from an infinite series, explains when the series represents the function (analyticity), or introduces even qualitative remainder/error-order language. That matters because later robotics modules rely on knowing when a local linearization may be trusted.

## Rubric scores

| Category | Score / 3 | Rationale |
|---|---:|---|
| Objective design | 2 | Appropriate and testable, but “quantify error” is limited to one absolute-error calculation and omits error order/bounds. |
| Source fidelity | 3 | The supplementary source is accurately described as brief; new authorship is disclosed. |
| Technical correctness | 2 | First/second-order formulas are correct; approximation and convergence conditions are underqualified. |
| Prerequisite readiness | 3 | Assumed single-variable calculus is explicit and directly checked. |
| Sequence and links | 3 | Correctly prepares MATH-01/MATH-02 and later linearization. |
| Exposition and layout | 3 | Clear concrete-to-formal progression and manageable density. |
| Visual pedagogy | 1 | Tangent/quadratic approximation is inherently visual but has no plot. |
| Exercises and feedback | 3 | Four aligned exercises, all with complete solutions/checkers. |
| Retrieval support | 1 | Three unkeyed prompts; no answered pure-recall item. Two of four exercises export cards. |
| Reference usefulness | 2 | Good summary and cheat-sheet formula; validity conditions remain thin. |

## Coverage and findings

| ID | Priority | Finding | Integration status | Evidence / disposition |
|---|---|---|---|---|
| M00-01 | P1 | Taylor polynomial, Taylor series, and function equality are not distinguished; smoothness alone does not guarantee that a Taylor series equals the function. | `UNPLANNED_GAP` | `MATH-00.mdx:80-82`; external benchmark §§5.1.1/5.8 explicitly distinguishes polynomial, series, and analytic functions. Add a compact boundary box, not a proof-heavy detour. |
| M00-02 | P2 | Approximation error is calculated once but not characterized as local truncation behavior or tied to step size/derivative scale. | `UNPLANNED_GAP` | Objectives at `:11`; teaching at `:56-76`. Add an intuitive remainder/error-order explanation and one compare-step-size exercise. |
| M00-03 | P2 | The module lacks the most useful intuition figure: function, tangent, quadratic approximation, and error as the evaluation point moves. | `UNPLANNED_GAP` | No figure import; `:44-76` is entirely textual/equational. Static plot is the acceptance bar; an interactive slider is optional enrichment. |
| M00-04 | P2 | Recall support does not meet the approved recall-primary policy. | `UNPLANNED_GAP` | Four answered exercises are conceptual/application/derivation, while three retrieval prompts at `:93-97` are unkeyed. Add short keyed formula/meaning/validity checks; do not remove the derivations. |

Exercise inventory: 4 answered (approximately 0 direct recall, 3 application/short derivation, 1 synthesis), 3 unkeyed retrieval prompts, 4/4 solutions, 2/4 exercise-card exports.

## Tool recommendation

A lightweight CPU/browser plot could let the learner move the expansion point and evaluation offset while toggling orders 0/1/2. It directly teaches locality and error growth, needs no account or paid service, and can be embedded if bundle cost is negligible. The simpler and required alternative is one static three-curve plot plus an error-versus-step-size plot.

## Phase 5 reconciliation

Plan revision 2.2 does not explicitly own M00-01/02/03/04. NUM-01 may later provide executable numerical context, but planned execution is not current conceptual coverage and does not resolve the Taylor validity distinction.

## Batched human decisions

- Approve a short “polynomial versus series versus analytic function” boundary as essential main-route content.
- Decide whether the plot is static-only or gains an optional embedded slider.
- Approve adding keyed recall under the workbook-wide exercise pass rather than expanding this page's derivation count.

Owner approved the recommended defaults in decision `docs/decisions/0006-math-review-approved.md`; the next Phase 5 plan revision must absorb the open items. Presentation verification: `STRUCTURE_VERIFIED`; live desktop/mobile inspection remains pending.
