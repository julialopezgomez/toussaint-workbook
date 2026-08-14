# MATH block review — mathematical foundations

Review state: `APPROVED` / `RECONCILED_WITH_OPEN_ITEMS`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Modules: `MATH-00`, `MATH-01`, `MATH-02`, `MATH-02B`, `MATH-03`, `MATH-03B`, `MATH-04`, `MATH-05`

Owner decision: approved 2026-08-14 in `docs/decisions/0006-math-review-approved.md`. Open reconciliation item: incorporate the approved delta into the next Phase 5 plan revision and re-pin it before Gate B is finalized.

## Block verdict

The block has a sound route and unusually complete worked feedback: it moves from scalar approximation through multivariable and matrix calculus to coordinate-free linear algebra, decompositions, and metric-dependent descent. All 44 embedded exercises have matching solutions. It is already useful as a course and reference.

It is not ready to serve as the unquestioned foundation for Phase 5. Several factual issues affect downstream optimization and robotics: PSD is twice treated as sufficient for a strict local-minimum conclusion, one vector-space axiom and linearity in the dual-space definition are missing, covariance/contravariance labels are reversed, covariance uses the feature count rather than sample count, and singular/indefinite cases are mishandled in the SVD and pseudoinverse discussion. These are repairs, not optional enrichment.

Completeness is also uneven. The source ranges leave out part of the notation system, mixed-domain/codomain basis transforms, Identities 2.5, and most of the covariance argument behind covariant gradient. Approved external comparison adds a few relevance-scoped essentials that the source itself does not teach sufficiently: affine spaces, general projection/least squares, Taylor validity, best low-rank approximation, and stable numerical linear algebra.

## Module disposition

| Module | Current status | Strongest element | Main reason it remains partial |
|---|---|---|---|
| `MATH-00` | `CURRENTLY_PARTIAL` | Concrete derivation and complete feedback | Polynomial/series/analyticity and approximation-validity boundary absent |
| `MATH-01` | `CURRENTLY_PARTIAL` | Chain-rule explanation and source figure | Declared notation range is only selectively taught; two qualifications need repair |
| `MATH-02` | `CURRENTLY_PARTIAL` | Shapes, derivatives, and finite-difference workflow | Incorrect PSD/local-minimum implication and broken eigendecomposition routes |
| `MATH-02B` | `CURRENTLY_PARTIAL` | Applied matrix-calculus derivations | Identities 2.5 absent despite objective/source claim; retrieval sparse |
| `MATH-03` | `CURRENTLY_PARTIAL` | Coordinate-free motivation and useful exercises | Definition errors and promised mixed-basis map representation absent |
| `MATH-03B` | `CURRENTLY_PARTIAL` | Useful PD/PSD and metric bridge | PSD logic repeated; general projection and geometric visual absent |
| `MATH-04` | `CURRENTLY_PARTIAL` | Strong SVD/PCA/pseudoinverse practice | Multiple singular/sign/normalization errors; low-rank theorem not taught |
| `MATH-05` | `CURRENTLY_PARTIAL` | Concise metric steepest-descent derivation | Source's covariance argument omitted; prerequisites and OPT division are wrong |

Detailed evidence is in `docs/review/modules/MATH-*.md`.

## Source and objective completeness

| Source/objective area | Judgment | Recommended disposition |
|---|---|---|
| Scalar Taylor construction | Covered at intended introductory depth | Retain; add a compact validity boundary and local-error intuition |
| Notation conventions, pp5–11 | Partial | Add a compact table for declaration/scope, set builder, maps, `min`/`argmin`, `inf`/`sup`, and fixed arguments |
| Multivariable calculus and finite differences | Mostly covered | Correct second-order qualifications; execute the promised gradient check in `NUM-01` |
| Matrix calculus, §§2.4–2.4.3 | Partial | Add Identities 2.5 or narrow and route the claim; keep the approved `NUM` numerical-practice route |
| Vector/dual/tensor and coordinate transforms | Partial | Repair definitions/table and teach one mixed input/output basis example |
| Scalar products and metric tensors | Covered at source depth | Add the externally justified general-projection bridge and correct coordinate-free wording |
| SVD/eigendecomposition/PCA/power method | Mostly covered | Repair technical statements and add best rank-`k` approximation |
| Numerical linear algebra, source §3.8 | Not covered | Add a focused CPU main-route `NUM-03`; do not overload the already dense SVD page |
| Covariant gradient, §§3.9.1–3.9.3 | Partial | Restore the coordinate-transformation/invariance argument that explains the title |

The objective sets are therefore not collectively complete relative to their declared sources. They also omit several externally supported skills that are important to later workbook content or the owner's robotics/polytope research. This is a relevance-scoped finding: source details without downstream, pedagogical, or research value may still be omitted if the omission is explicit.

## Essential repair batch

These do not require further content-scope judgment and should be treated as mandatory implementation repairs:

1. Correct the PSD/PD and second-order-condition statements in `MATH-02` and `MATH-03B`.
2. Add the mixed-partial regularity qualification for Hessian symmetry.
3. Repair the vector-space axiom list, dual-space definition, covariance/contravariance table, and matrix/covector notation.
4. Correct all `MATH-05` links that should point to `MATH-04`, plus the `MATH-02B` PSD/PD route to `MATH-03B`.
5. Correct the covariance denominator, pseudoinverse zero-mode rule, symmetric-indefinite SVD/eigen relation, and PSD/PD eigenvalue wording.
6. Qualify spline continuity, RBF width/variance, differentiability/linearity, and SPD/damping assumptions.
7. Correct future modules described as already studied and repair prerequisite metadata/readiness.
8. Add concise source-correction notes where the workbook intentionally departs from an apparent source error.

## Relevance-scoped additions

| Addition | Recommended owner | Route/depth | Why it clears the relevance bar |
|---|---|---|---|
| Taylor polynomial vs series, analyticity, qualitative remainder | `MATH-00` | Main, compact | Prevents unjustified trust in local models used throughout robotics |
| Core notation table | `MATH-01` | Main/reference | Reused throughout all later blocks |
| Affine spaces/subspaces and equality-constraint geometry | `MATH-03` | Main, compact | Directly supports constraints, configuration spaces, and polytope research |
| Mixed input/output basis transforms | `MATH-03` | Main | Promised objective and source content; central to frame-aware robotics |
| General full-rank projection and least-squares link | `MATH-03B` | Main concept/formula | Connects metrics and orthogonality to estimation and optimization |
| Identities 2.5, especially Woodbury | `MATH-02B` | Main/reference | Already promised and used downstream by `ML-05` |
| Eckart–Young and rank-`k` error | `MATH-04` | Main | Already assessed by `MATH-EXAM`; important for PCA/compression |
| Stable solve, conditioning, numerical rank, QR, Cholesky | New `NUM-03` | Main CPU lab after `MATH-04`/`NUM-01` | Foundational implementation skill absent from Phase 5 rev 2.2 and relevant across optimization/ML/robotics |
| Covariance/invariance derivation | `MATH-05` | Main | Explains the module's title and prevents coordinate-dependent reasoning |

`NUM-03` is the only recommended new module from this block audit. It should complement, not duplicate, `NUM-01` reproducibility and `NUM-02` vectorization.

## Exercises, retrieval, and milestone

The block contains 44 answered exercises: approximately 10 foundation, 25 core application/derivation, and 9 challenge/synthesis items. Feedback coverage is excellent, but durable recall is not. Only 12/44 exercises declare `reviewCardIds`, and the 30 end-of-module retrieval prompts are unkeyed, so they do not count as answerable recall under the approved protocol.

Recommended action: retain the derivations, then add a small keyed recall layer for definitions, shapes, assumptions, formula selection, and failure conditions across every MATH module. This should extend Phase 5 F8 beyond the three calibration modules without imposing a mechanical card-per-prerequisite or card-per-exercise ratio.

`MATH-EXAM` also needs repair:

- its claim that every question combines at least two modules is false for Part 3;
- the substantive coverage underrepresents `MATH-01`, coordinate transforms from `MATH-03`, and projection/PD skills from `MATH-03B`;
- Part 1 attributes the vector/covector distinction to `MATH-03B` instead of `MATH-03` and omits the latter from remediation;
- Part 3 assesses best low-rank approximation before it is taught;
- Part 4 should route metric/PD prerequisites where relevant.

## Visual and interactive teaching plan

Static figures are the acceptance bar. Recommended reusable visuals are:

1. function/tangent/quadratic/error for `MATH-00`;
2. Hessian contour classes and eigendirections for `MATH-02`;
3. old/new bases with invariant geometric vector for `MATH-03`;
4. Euclidean circle versus metric ellipse, reused by `MATH-03B` and `MATH-05`;
5. unit circle to ellipse/rank collapse for `MATH-04`.

Optional browser interactives may add sliders or draggable bases after the corresponding static figure is accepted and the bundle/runtime budget is measured. One reusable metric explorer should serve both `MATH-03B` and `MATH-05`; separate bespoke tools would be unnecessary maintenance.

Presentation is `STRUCTURE_VERIFIED`, not `VISUALLY_VERIFIED`. Source PDF pages were rendered and inspected, but the available environment did not expose the in-app browser-control runtime for live desktop/mobile inspection. This does not block semantic findings; it leaves one later human visual-QA pass.

## Phase 5 reconciliation

Plan revision 2.2 explicitly owns calibration repairs in `MATH-02B`, the `MATH-02` executable gradient check through `NUM-01`, and later F8 work. It does not own most newly identified MATH repairs, full-block retrieval, the five static visual requirements, the exam corrections, or stable numerical linear algebra.

Recommended plan delta:

- extend Gate F0 to all P1 factual/link/prerequisite repairs in this record;
- add the compact in-module scope additions above before downstream authoring depends on them;
- add `NUM-03` to the NUM block and update its prerequisite/dependent map;
- extend F8's retrieval/reference/assessment pass to the whole MATH block;
- record the static visual set as acceptance criteria, with interactives optional;
- divide ownership so `MATH-05` teaches metric/covariance meaning and `OPT-01` recalls/applies it without repeating the full derivation.

## Batched owner approval

Approved in full: the essential-repair batch, the relevance-scoped additions and owners in the table, `NUM-03`, whole-block keyed recall, milestone corrections, five static visuals, and the `MATH-05`/`OPT-01` division. Interactives remain optional candidates subject to later runtime/value checks. Autonomous minor-item triage continues, and live presentation approval is deferred until the visual-QA pass.

This approval accepts the review baseline and required plan delta. The block does not become currently complete until implementation and re-review.
