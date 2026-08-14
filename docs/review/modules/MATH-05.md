# MATH-05 review — Covariant Gradient & Steepest Descent

Review state: `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Primary source checked: `lecture-maths`, pp39-42 §3.9
External benchmark: *Mathematics for Machine Learning*, §§3.2, 5.2 and 7.1; accessed 2026-08-14

## Verdict

The module explains metric-dependent steepest descent clearly and gives a concise Lagrange-multiplier derivation plus complete feedback. Its declared source range, however, is mostly about how vector, covector, metric, and steepest-direction coordinates transform under a basis change; the module omits that central covariance calculation while retaining “covariant” in the title. It therefore teaches the formula but not the invariance argument that justifies the name.

Its prerequisite metadata also names MATH-04, which contributes almost nothing to the lesson, while omitting the actual dependencies MATH-02, MATH-03, and MATH-03B. The displayed directional-limit definition further claims linearity without stating differentiability strong enough to make the derivative a linear map. Finally, OPT-01 immediately repeats the same steepest-descent derivation, creating avoidable duplication.

## Rubric scores

| Category | Score / 3 | Rationale |
|---|---:|---|
| Objective design | 2 | Useful and testable, but omits the transformation/invariance objective implied by title/source. |
| Source fidelity | 1 | Definition/formula retained; most of §§3.9.2-3.9.3's covariance reasoning is omitted. |
| Technical correctness | 2 | Formula is correct; differentiability/linearity assumptions need qualification. |
| Prerequisite readiness | 1 | The declared prerequisite is largely irrelevant and actual dependencies are omitted. |
| Sequence and links | 1 | Immediate duplication with OPT-01; source transformation bridge is missing. |
| Exposition and layout | 3 | Short, focused, and easy to follow. |
| Visual pedagogy | 1 | Metric-dependent direction change has no geometry figure. |
| Exercises and feedback | 3 | Three aligned exercises with complete feedback. |
| Retrieval support | 2 | Two exercises export cards, but no direct keyed formula/assumption recall. |
| Reference usefulness | 2 | Compact summary; insufficient for coordinate-invariance lookup. |

## Prioritized findings

| ID | Priority | Finding | Integration status | Evidence / disposition |
|---|---|---|---|---|
| M05-01 | P1 | Actual prerequisites are not declared. | `UNPLANNED_GAP` | `MATH-05.mdx:7,33-48`; content depends on gradient, dual/covector, and metric material from MATH-02/03/03B, not SVD/power methods from MATH-04. Repair metadata/readiness while preserving route order. |
| M05-02 | P1 | The source's central coordinate-transformation/invariance derivation is omitted. | `UNPLANNED_GAP` | Source pp39-42 §§3.9.2-3.9.3; module `:42-58` jumps from differential to final metric formula. Add transformations of vector, covector, metric, and `G^{-1}∇f`, with one numeric rescaling example. |
| M05-03 | P1 | Directional-limit existence alone does not guarantee a linear derivative. | `UNPLANNED_GAP` | `:46-48`; require Fréchet differentiability (or state differentiability in the source's intended stronger sense) before calling `df|x` linear. |
| M05-04 | P2 | MATH-05 and OPT-01 teach and assess the same derivation back-to-back. | `UNPLANNED_GAP` | `MATH-05.mdx:50-70`; `OPT-01.mdx:104-114` and `OPT-01-ex1c`. Recommended: keep conceptual/invariance treatment here; let OPT-01 recall and apply it rather than re-derive it. |
| M05-05 | P2 | The phrase “natural gradient, preconditioning, and Gauss-Newton are all instances” needs conditions. | `UNPLANNED_GAP` | `:29-31,72-76`; metric/preconditioner matrices must have appropriate SPD/damping properties, and Gauss-Newton/Fisher matrices may be singular. Add a careful forward bridge, not a full treatment. |
| M05-06 | P2 | Metric geometry lacks a visual. | `UNPLANNED_GAP` | No figure; add a static contour/unit-ball comparison showing why equal `G`-length changes the selected direction. |

Exercise inventory: 3 answered (approximately 1 conceptual recall, 2 application/short derivation, 0 synthesis), 2 unkeyed retrieval prompts, 3/3 solutions, 2/3 exercise-card exports.

## Tool recommendation

The MATH-03B metric explorer can be reused here with a cost gradient overlay; changing `G` should visibly rotate/rescale the steepest unit direction. This avoids a second bespoke interactive. Static metric balls and direction arrows remain the required fallback.

## Phase 5 reconciliation

Revision 2.2 does not own these repairs. OPT-01 contains the missing coordinate-transformation result, but teaching it after MATH-05 does not make the current source claim complete and creates duplication instead of an explicit division of roles.

## Batched human decisions

- Approve the prerequisite correction and stronger differentiability qualification.
- Keep MATH-05 as the conceptual/invariance owner and reduce OPT-01 duplication (recommended), or merge this short module into OPT-01.
- Reuse one metric visual/tool across MATH-03B and MATH-05.

Owner approved the recommended defaults in decision `docs/decisions/0006-math-review-approved.md`; the next Phase 5 plan revision must absorb the open items. Presentation verification: `STRUCTURE_VERIFIED`; live desktop/mobile inspection remains pending.
