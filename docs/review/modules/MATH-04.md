# MATH-04 review — SVD, Eigendecomposition & the Power Method

Review state: `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Primary sources checked: `svd` pp1-2/HTML and `lecture-maths` pp31-38 §§3.4-3.7
External benchmark: *Mathematics for Machine Learning*, Chapter 4 and Chapter 10; accessed 2026-08-14

## Verdict

This is the strongest teaching page in the block for conceptual ambition: it gives an intuitive thin-SVD view, a meaningful source figure, pseudoinverse and PCA connections, and ten complete exercises including proofs. It also contains the block's clearest factual source inheritance error: the covariance normalization uses `1/n` after defining `m` samples and `n` features; it should use `1/m` for population-style data covariance (or `1/(m-1)` for the unbiased sample estimator).

The symmetric pseudoinverse formula writes `Λ^{-1}` without restricting inversion to nonzero eigenvalues, exactly where a pseudoinverse is needed for singular matrices. “SVD and eigendecomposition coincide” is also too broad for symmetric indefinite matrices, and the smallest-eigenvalue section calls PSD matrices an example of matrices with all positive eigenvalues. Finally, the module and milestone exam invoke best rank-`k` approximation without teaching the Eckart-Young result or approximation-error norm.

## Rubric scores

| Category | Score / 3 | Rationale |
|---|---:|---|
| Objective design | 2 | Broad and valuable; low-rank approximation is implied/tested but absent from objectives and teaching. |
| Source fidelity | 2 | Most source sections are represented; the source's covariance typo is silently repeated and §3.8 numerics are excluded. |
| Technical correctness | 1 | Covariance denominator, pseudoinverse zero modes, and PSD/PD wording require repair. |
| Prerequisite readiness | 3 | Orthonormality and PSD are explicitly checked. |
| Sequence and links | 3 | Correctly feeds MATH-05, ML/PCA, ODE, and later dynamics. |
| Exposition and layout | 2 | Coherent but very dense for seven hours; thin/full SVD and sign cases need a sharper table. |
| Visual pedagogy | 2 | The source figure is useful; ellipse/unit-circle intuition and low-rank visuals are still absent. |
| Exercises and feedback | 3 | Ten rigorous, fully solved exercises. |
| Retrieval support | 1 | Almost all work is derivation/proof; only two exercises export cards. |
| Reference usefulness | 2 | Strong summary but oversimplified SVD/eigen rules are repeated on the cheat sheet. |

## Prioritized findings

| ID | Priority | Finding | Integration status | Evidence / disposition |
|---|---|---|---|---|
| M04-01 | P1 | Covariance normalization divides by feature dimension `n`, not sample count `m`. | `UNPLANNED_GAP` | `MATH-04.mdx:120-124`; inherited from source p35. Correct to `1/m` (or explicitly discuss `1/(m-1)`) and disclose the source correction. |
| M04-02 | P1 | The symmetric pseudoinverse uses `Λ^{-1}` without excluding zero eigenvalues. | `UNPLANNED_GAP` | `:102-112`; define reciprocal only for nonzero singular/eigenvalues and zero otherwise; distinguish thin/full matrices and projector identities. |
| M04-03 | P1 | Symmetric SVD/eigendecomposition is described as coincident too broadly. | `UNPLANNED_GAP` | `:84-98,156-160`; for negative eigenvalues singular values are absolute values and `U` differs from `V` by signs. Repair lesson and `math.mdx:14,31,39,46,53`. |
| M04-04 | P1 | “All eigenvalues positive, e.g. PSD” confuses PSD with PD. | `UNPLANNED_GAP` | `:146-150`; use PD for strictly positive eigenvalues and explicitly handle a zero smallest eigenvalue. |
| M04-05 | P1 | Best low-rank approximation is tested by `MATH-EXAM` but never taught. | `UNPLANNED_GAP` | Intro `:41`; exam Part 3; external benchmark §§4.6/10.4. Add the Eckart-Young statement, Frobenius/spectral error, and a small truncation example. |
| M04-06 | P1 | Stable numerical linear algebra is absent: solve versus inverse, conditioning, rank tolerance, and QR/Cholesky are not owned by the current NUM plan. | `UNPLANNED_GAP` | Toussaint §3.8 on p38 and external benchmark §§2.3.4/4.3; Phase 5 NUM-01/02 cover reproducibility/vectorization only. Candidate: add NUM-03 or materially expand NUM-01/02. |
| M04-07 | P2 | The simultaneous smallest-eigenvalue iteration and eigenvalue recovery are too terse to execute safely. | `UNPLANNED_GAP` | `:146-152`; name the pre-normalization norm, convergence assumptions, and recommend standard library/inverse/shift-invert methods for practice. |
| M04-08 | P2 | Recall is sparse despite ten exercises. | `UNPLANNED_GAP` | Ten answered items are explanation/application/proof; five unkeyed prompts and two card exports. Add keyed formula/condition/choice recall without adding more proofs. |

Exercise inventory: 10 answered (approximately 1 conceptual recall, 4 application/short derivation, 5 synthesis/proof), 5 unkeyed retrieval prompts, 10/10 solutions, 2/10 exercise-card exports.

## Tool/resource recommendations

- An embedded unit-circle-to-ellipse SVD explorer would directly teach singular directions/values and rank collapse; CPU/browser-only, no account. Required fallback: three static panels for full rank, ill-conditioned, and rank-deficient maps.
- Link the approved MML PCA notebook as optional practice, while keeping the workbook explanation self-contained.
- Put executable stable-solve/conditioning work in a dedicated CPU numerical-linear-algebra lab rather than enlarging this already dense theory module.

## Phase 5 reconciliation

No revision-2.2 item explicitly repairs M04-01/02/03/04/05/07/08. NUM-01/02 only partially overlap M04-06 and cannot be counted as ownership until their objectives explicitly include stable solving/factorization/conditioning.

## Batched human decisions

- Approve the four factual corrections and low-rank theorem as mandatory.
- Approve adding a main-route `NUM-03` (recommended) or expanding NUM with stable linear algebra.
- Decide whether the SVD explorer is included after a static figure and bundle-budget check.

Owner approved the recommended defaults in decision `docs/decisions/0006-math-review-approved.md`; the next Phase 5 plan revision must absorb the open items. Presentation verification: `STRUCTURE_VERIFIED`; live desktop/mobile inspection remains pending.
