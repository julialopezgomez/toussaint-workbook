# MATH-01 review — Functions, Derivatives & the Chain Rule

Review state: `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Primary source checked: `lecture-maths`, pp5-11 and p19
External benchmark: *Mathematics for Machine Learning*, Chapter 5; accessed 2026-08-14

## Verdict

The chain-rule half is strong: the source figure is used well, partial versus total differentiation is explained concretely, and five complete exercises progress from interpretation to multi-path and robotics-flavoured differentiation. The declared notation range is only selectively covered, however. Several high-frequency source conventions—declaring symbols and index scope, `min` versus `argmin`, `→` versus `↦`, set-builder notation, and fixed-argument dot notation—are absent despite the objective promising fluent use of the course's core conventions.

Two source-derived statements also need correction rather than silent repetition: a degree-`p` spline is not automatically `C^{p-1}` without knot/continuity assumptions, and `exp(-l d^2)` corresponds to variance `1/(2l)` under the standard Gaussian convention, so calling its variance `1/l` is misleading.

## Rubric scores

| Category | Score / 3 | Rationale |
|---|---:|---|
| Objective design | 2 | Chain-rule objectives are complete; “core notation” is under-scoped relative to the declared source. |
| Source fidelity | 2 | Chain-rule material is faithful; the notation chapter is compressed without routing and two source claims need qualification. |
| Technical correctness | 2 | Main calculus is sound; spline smoothness and RBF width/variance are overgeneralized. |
| Prerequisite readiness | 3 | MATH-00 and ordinary derivative readiness are explicit and tested. |
| Sequence and links | 2 | Correct next route, but two future modules are described as already studied. |
| Exposition and layout | 3 | Strong progression, figure, worked example, and clear prose. |
| Visual pedagogy | 3 | The source chain-rule figure directly supports the algorithmic idea. |
| Exercises and feedback | 3 | Five varied, fully solved exercises. |
| Retrieval support | 1 | No answered direct-recall set; only two of five exercises export cards. |
| Reference usefulness | 2 | Summary is useful but omits much of the declared notation toolkit. |

## Prioritized findings

| ID | Priority | Finding | Integration status | Evidence / disposition |
|---|---|---|---|---|
| M01-01 | P1 | The learning objective and source range imply a core notation treatment, but several conventions used throughout later blocks are absent. | `UNPLANNED_GAP` | `MATH-01.mdx:9,53-63`; source pp6-8. Add a compact syntax table covering declaration/scope, set builder, maps, `min`/`argmin`, `inf`/`sup`, and fixed-argument notation; omit the source's philosophical prose if desired. |
| M01-02 | P1 | Spline continuity is stated as unconditional: “a spline of degree `p` is `C^{p-1}`.” | `UNPLANNED_GAP` | `:76`; continuity depends on knot multiplicity/construction. Qualify as the maximally smooth/simple-knot case and forward-link to DYN-05 rather than treating all splines alike. |
| M01-03 | P2 | The RBF “variance `1/l`” gloss does not match the usual Gaussian parameterization. | `UNPLANNED_GAP` | `:76`; replace “variance” with width/length-scale, or state the convention and `σ²=1/(2l)` for `exp(-d²/(2σ²))`. Add a source-correction note because the claim comes from p9. |
| M01-04 | P2 | Future modules are narrated as prior knowledge. | `UNPLANNED_GAP` | `:61` says the learner “saw” the notation in ML-03/KIN-02; `:112` says backprop was already met in ML-03. Rewrite both as forward pointers. |
| M01-05 | P2 | Durable recall is sparse for a definition- and notation-heavy module. | `UNPLANNED_GAP` | Three unkeyed prompts at `:149-153`; five answered exercises contain no direct notation-definition recall. Add keyed syntax/definition/chain-rule checks. |

Exercise inventory: 5 answered (approximately 1 conceptual recall, 2 application/short derivation, 2 synthesis/challenge), 3 unkeyed retrieval prompts, 5/5 solutions, 2/5 exercise-card exports.

## Tool recommendation

The existing static DAG is sufficient for first teaching. An optional small computation-graph tracer could highlight active forward and reverse paths and show accumulated derivatives after the learner edits local derivatives. It is CPU/browser-only, account-free, and should be added only if it remains simpler than a worked path table. A static path-contribution table is the preferred first improvement.

## Phase 5 reconciliation

Revision 2.2 does not explicitly own these findings. Later DRL/autodiff labs deepen chain-rule application but cannot repair missing foundation notation or incorrect future-tense sequencing.

## Batched human decisions

- Approve the compact notation table as essential main-route content.
- Approve correcting the two source-derived qualifications with explicit provenance notes.
- Keep the current five exercises and add recall at block level rather than lengthening the challenge set.

Owner approved the recommended defaults in decision `docs/decisions/0006-math-review-approved.md`; the next Phase 5 plan revision must absorb the open items. Presentation verification: `STRUCTURE_VERIFIED`; live desktop/mobile inspection remains pending.
