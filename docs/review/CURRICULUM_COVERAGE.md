# Curriculum coverage ledger

Status: **calibration, MATH, and OPT approved; next Phase 5 plan revision pending; PROB review next**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Expansion-plan reference: `docs/plans/PHASE5_AUGMENTATION_PLAN.md`, revision 2.2, SHA-256 `412b807536da6d90b1063ad800aadf5435a6e05eabe6e3cfcd6ea65ac308f2f3`

This ledger is the cross-module companion to individual review records. It answers the broader question that a module-only review cannot: whether the objectives, blocks, source ranges, assessments, and future plan collectively cover the intended learning programme.

## Coverage-unit schema

The full ledger should eventually contain one row per teachable unit, not merely one row per module. A unit may be a definition, derivation, algorithm, practical skill, conceptual distinction, or visual intuition.

| Field | Meaning |
|---|---|
| Coverage unit | Stable concept/skill name |
| Intended depth | Recall, application, or synthesis |
| Primary source evidence | Source ID plus page/section |
| Current teaching location | Module and section |
| Assessment location | Exercise, retrieval, exam, or none |
| Dependencies/dependents | What must precede/follow it |
| Current status | One allowed integration status |
| Plan owner | Stable expansion-plan item or pending |
| Human decision | Accept, change, defer, or out of scope |

## Calibration source-coverage seed

### MATH-02B

| Coverage unit | Source evidence | Current location/evidence | Status | Assessment |
|---|---|---|---|---|
| Matrix-equation warm-ups | `lecture-maths`, p15 §2.4 (i–vi) | Four warm-ups plus Gauss–Newton exercise; `MATH-02B.mdx:49-61,138-148` | `CURRENTLY_COVERED` | Exercises 1–4 and 8 |
| Ridge/Tikhonov normal equations | p15 §2.4 | Worked example; lines 63–77 | `CURRENTLY_COVERED` | Exercises 3–4; retrieval 1 |
| Identities 2.3 | p16 | Lines 79–96 | `CURRENTLY_COVERED` | Exercise 5; retrieval 2 |
| Identities 2.4 | p16 | Lines 91–120 | `CURRENTLY_COVERED` | Used in GP derivation; no focused recall answer |
| Identities 2.5, including Woodbury | p17 | Named in objectives/summary/source note but not taught | `UNPLANNED_GAP` | None |
| Scalar derivative with respect to a matrix | p17 §2.4.1 | Lines 98–106 | `CURRENTLY_COVERED` | Exercise 6; retrieval 3 |
| GP log-likelihood gradient | p17 §2.4.2 | Lines 108–120 | `CURRENTLY_COVERED` | No dedicated exercise |
| Logistic-regression Hessian | p18 §2.4.3 | Lines 122–136 | `CURRENTLY_COVERED` | Exercise 7; retrieval 4 |
| Finite-difference gradient checking | p18 §2.5, outside declared range | Routed to `MATH-02`; its source note explicitly owns it | `CURRENTLY_COVERED` | `MATH-02` implementation exercise |

### KIN-02

The source metadata says pp1–4 and “full note,” while the PDF has five pages. This boundary must be corrected before the ledger can claim full-source coverage.

| Coverage unit | Source evidence | Current location/evidence | Status | Assessment |
|---|---|---|---|---|
| Quaternion representation, inverse, product | `quaternions`, p1 | Core notation and product taught | `CURRENTLY_COVERED` | Derivation/Jacobian exercises |
| Quaternion ↔ rotation-matrix conversion and vector application | p1 | Not taught; no explicit route | `UNPLANNED_GAP` | None |
| Exponential/logarithm maps | pp1–2 | Lines 57–77 | `CURRENTLY_COVERED` | Derivation and symbolic exercises |
| Double cover: `q` and `-q` | Necessary to the representation; implicit in source and explicit downstream | Concept named in frontmatter and solution, not explained in lesson | `CURRENTLY_PARTIAL` | Only implicit in exercise solution |
| SLERP and relative rotation | p2 | Lines 79–89 | `CURRENTLY_PARTIAL` | Numeric exercise; sign/antipodal handling absent |
| Quaternion differential equation and integration on `S^3` | p3 | Differential identity taught; integration procedure omitted | `CURRENTLY_PARTIAL` | Derivation only |
| Angular Jacobian: unit/tangent case | p4 | Lines 91–97 | `CURRENTLY_COVERED` | Challenge derivation |
| General Jacobian for non-normalized/non-tangent changes; world coordinates | p4 | Omitted | `UNPLANNED_GAP` | None |
| Random rotations and Gaussian sampling | p4 | Omitted | `UNPLANNED_GAP` | None |
| Rodrigues/skew/angular-velocity appendix | p5 | Taught in `KIN-01`, but source range and source note do not route it | `CURRENTLY_PARTIAL` | `KIN-01` exercises |

### RLEARN-02

| Coverage unit | Source evidence | Current location/evidence | Status | Assessment |
|---|---|---|---|---|
| Behavior cloning and trajectory distribution learning | `lecture-robotlearning`, pp35–40 | Lines 43–69 | `CURRENTLY_COVERED` | Exercise 1; retrieval 1 |
| Dynamic time warping for demonstrations | Source trajectory-learning discussion | Omitted | `UNPLANNED_GAP` | None |
| Feature/constraint learning from demonstrations | KPAM/descriptors/constraints in source | Compressed to one sentence; later `RLEARN-07` covers one branch without an explicit route here | `CURRENTLY_PARTIAL` | None |
| Distribution shift and compound error | pp41–42 | Lines 71–81 | `CURRENTLY_COVERED` | Exercises 2–3; retrieval 2 |
| DAgger algorithm and tradeoff | p43 | Lines 83–89 | `CURRENTLY_COVERED` | Retrieval 3; RLEARN exam |
| Demonstration collection modes and privileged teacher | pp44–46 | Lines 90–94 | `CURRENTLY_COVERED` | Exercise 4 |
| GAN, VAE, diffusion formulations | pp47–53 | Lines 96–104 | `CURRENTLY_PARTIAL` | Network-role exercise; diffusion training/sampling and comparative tradeoffs not assessed |
| Motion-planning sampling distribution as a VAE+IL example | Source example | Omitted; substituted with a newer manipulation case | `CURRENTLY_PARTIAL` | None |
| ALOHA/ACT architecture, action chunks, temporal ensembling | p54 | Conditional VAE summarized; chunking/ensembling mechanics omitted | `CURRENTLY_PARTIAL` | No applied exercise |
| Domain-adaptive imitation-learning case study | pp55–56 | One-paragraph summary | `CURRENTLY_PARTIAL` | None |

## Calibration objective audit

| Module | Objective-set judgment | Evidence |
|---|---|---|
| `MATH-02B` | `CURRENTLY_PARTIAL` | Objective 3 promises Identities 2.3–2.5 but 2.5 is absent. Objectives otherwise align with taught core and downstream use. Numerical practice should be checked externally: formulas use explicit inverses where implementation should normally solve a linear system. |
| `KIN-02` | `CURRENTLY_PARTIAL` | The objectives omit the double cover/sign choice, conversion/application, integration, and sampling content needed to represent the declared full note. The first objective's wording (“rotations live on S3”) is imprecise: unit quaternions double-cover `SO(3)`. |
| `RLEARN-02` | `CURRENTLY_PARTIAL` | Objectives capture BC/DAgger and name three generative families, but omit a comparison objective covering quality, coverage, efficiency, stability, and inference cost—the source explicitly motivates that comparison. Feature extraction and modern sequence-policy mechanics also lack explicit scope decisions. |

## Curriculum-level calibration findings

These are hypotheses to test across all 69 modules, not conclusions about the whole workbook yet.

| ID | Question for the full audit | Calibration evidence | Status |
|---|---|---|---|
| COV-G01 | Are learning objectives derived from a complete source/block map, or only from the material selected for each page? | All three calibration records contain source concepts absent from their objective lists. The completed MATH audit independently confirms objective gaps in notation, mixed-basis maps, Identities 2.5, low-rank approximation, and covariance. | `PLANNED_TO_ADDRESS` |
| COV-G02 | Is “full note/range covered” used only when every concept is taught or explicitly routed? | Gate A found only two “full note” claims: `KIN-02` is a verified overclaim; `DYN-05` is nominated for semantic audit, not presumed defective. | `PLANNED_TO_ADDRESS` |
| COV-G03 | Does every declared prerequisite receive adequate readiness coverage? | Gate A found 32/67 prerequisite-bearing modules with fewer readiness widgets than prerequisite IDs. Semantic review now verifies mismatched or incomplete prerequisite metadata in `MATH-03` and `MATH-05`; the ratio remains only a screening signal. | `PLANNED_TO_ADDRESS` |
| COV-G04 | Can the learner retrieve core facts with an answer, not only an unanswered prompt? | Gate A found 322/361 exercises without `reviewCardIds`. In MATH, only 12/44 answered exercises export cards and 30 retrieval prompts are unkeyed, confirming a block-level recall gap without implying a rigid export ratio. | `PLANNED_TO_ADDRESS` |
| COV-G05 | Are source figures reused/redrawn when they carry causal or spatial meaning? | `RLEARN-02` drops several causal figures; MATH lacks static intuition figures for Taylor locality, Hessian classes, basis changes, metric geometry, and SVD rank collapse. | `PLANNED_TO_ADDRESS` |
| COV-G06 | Are downstream references evidence that the prerequisite was actually taught? | `PLAN-03` relies on an unexplained quaternion sign equivalence; MATH additionally contains repeated wrong routes to `MATH-05` and tests low-rank approximation before teaching it. | `PLANNED_TO_ADDRESS` |
| COV-G07 | Are source corrections and notation departures disclosed? | Calibration found undisclosed corrections. MATH also silently repeats source errors in spline smoothness and covariance normalization while silently correcting others. | `PLANNED_TO_ADDRESS` |
| COV-G08 | Do cheat sheets and exams cover the whole objective set rather than a small formula subset? | `MATH-EXAM` underrepresents notation, mixed-basis transformations, and projection/PD skills and assesses untaught low-rank approximation. Gate A separately finds milestone gaps for PLAN/MANIP/SYM. | `PLANNED_TO_ADDRESS` |

The completed OPT audit strengthens the same global findings: the block's declared “full optimization course” source scope silently omits differentiable and derivative-free optimization; probability prerequisites occur later in the live route; 26 retrieval prompts are unkeyed; no module imports a figure; and `OPT-EXAM` names all six modules while omitting `OPT-06` from substantive assessment. These are semantic confirmations, not mechanical-ratio failures.

## Approved external-gap findings

The benchmark corpus is approved. Findings remain relevance-scoped: they enter the curriculum only when they support later content, core learning, or the owner's research.

- `MATH-02B`: teach “solve the system; do not form the inverse” as the normal numerical implementation, with conditioning and regularization distinguished.
- `KIN-02`: explicitly teach `q ~ -q`, sign alignment/shortest-path SLERP, small-angle behavior, normalization, and convention discipline.
- `RLEARN-02`: qualify the compound-error theorem with its assumptions; distinguish state-only from history-conditioned/action-sequence policies; compare GAN/VAE/diffusion behavior rather than only network counts.

## Completed MATH block audit

The detailed block artifact is `docs/review/blocks/MATH.md`; seven new module records accompany the approved `MATH-02B` calibration record.

| Coverage unit | Current status | Proposed owner/disposition |
|---|---|---|
| Taylor polynomial/series/analyticity and local error | `UNPLANNED_GAP` | Compact main-route addition in `MATH-00` |
| Declared mathematical notation range | `CURRENTLY_PARTIAL` | Compact syntax/reference table in `MATH-01` |
| Correct second-order conditions and Hessian assumptions | `CURRENTLY_PARTIAL` | Mandatory repairs in `MATH-02`/`MATH-03B` |
| Matrix identities through source §2.5 | `CURRENTLY_PARTIAL` | Complete in `MATH-02B` or explicitly narrow/route |
| Vector/dual definitions and transformation conventions | `CURRENTLY_PARTIAL` | Mandatory repairs in `MATH-03` |
| Affine spaces and equality-constraint geometry | `UNPLANNED_GAP` | Compact addition in `MATH-03` |
| Mixed input/output basis representations | `UNPLANNED_GAP` | Teach and practise in `MATH-03` |
| General projection and least-squares bridge | `UNPLANNED_GAP` | Concept/formula in `MATH-03B`; implementation in numerical lab |
| Singular/sign-safe SVD, pseudoinverse, and PCA statements | `CURRENTLY_PARTIAL` | Mandatory repairs in `MATH-04` and math cheat sheet |
| Best rank-`k` approximation | `UNPLANNED_GAP` | Teach in `MATH-04` before existing exam use |
| Stable solves, conditioning, rank tolerance, QR/Cholesky | `UNPLANNED_GAP` | Recommended new main-route CPU module `NUM-03` |
| Covariant-gradient transformation/invariance | `CURRENTLY_PARTIAL` | Restore in `MATH-05`; remove duplicate derivation from `OPT-01` |
| Answered recall across MATH | `CURRENTLY_PARTIAL` | Extend F8 to whole block; no mechanical card ratio |
| MATH milestone coverage/remediation | `CURRENTLY_PARTIAL` | Correct claims/routes and rebalance after teaching repairs |

The owner approved this block review and the proposed dispositions in decision `docs/decisions/0006-math-review-approved.md`. The block remains `CURRENTLY_PARTIAL` pending implementation and re-review. Planned additions are not counted as current coverage; the next Phase 5 revision must incorporate and re-pin this delta before Gate B is finalized.

## Completed OPT block audit

The detailed block artifact is `docs/review/blocks/OPT.md`; all six module records and their proposed dispositions are owner-approved in decision `docs/decisions/0007-opt-review-approved.md`.

| Coverage unit | Current status | Proposed owner/disposition |
|---|---|---|
| Line search, metric descent, Newton, and damping | `CURRENTLY_PARTIAL` | Mandatory normalization, Wolfe, sign, limiting-behavior, and assumption repairs in `OPT-01` |
| Gauss–Newton, BFGS, and conjugate gradient | `CURRENTLY_PARTIAL` | Mandatory rank/conditioning/curvature/convergence repairs in `OPT-02`; implementation bridge to `NUM-03` |
| KKT, Lagrangian, and duality | `CURRENTLY_PARTIAL` | Add constraint qualification and correct cone/stationarity/saddle claims in `OPT-03` |
| Convex problems, LP/QP, barriers, and SQP | `CURRENTLY_PARTIAL` | Mandatory repairs plus compact LP-relaxation and problem-class bridge in `OPT-04` |
| Implicit functions and differentiable optimization | `UNPLANNED_GAP` | Recommended new main-route CPU module `OPT-04B` |
| Stochastic optimization and adaptive methods | `CURRENTLY_PARTIAL` | Repair assumptions, cost/unbiasedness claims, and probability readiness in `OPT-05` |
| Evolutionary/derivative-free optimization | `UNPLANNED_GAP` | Recommended focused main-route CPU module `OPT-05B` |
| Bayesian optimization and bandits | `CURRENTLY_PARTIAL` | Repair UCB convention, GP mean/numerics, assumptions, and route in `OPT-06` |
| Factored programs and ADMM | `UNPLANNED_GAP` | Optional/deferred unless a later distributed or multi-robot dependency justifies promotion |
| RL–optimization source overlap | `UNPLANNED_GAP` in OPT | Explicit route to RL/RLEARN; do not duplicate |
| Answered recall across OPT | `CURRENTLY_PARTIAL` | Extend F8 to the whole block; preserve derivations, add keyed conditions/method-choice recall |
| OPT milestone and cheat sheet | `CURRENTLY_PARTIAL` | Correct propagated errors, align retakes, and add genuine `OPT-06`/block coverage |

The Phase 5 revision 2.2 route swap addresses the forward `PROB` prerequisite violation but does not own the module repairs, new OPT modules, full-block retrieval, static visuals, or assessment corrections. Decision `0007` approves that delta for the next plan revision. Planned additions are not counted as current coverage.

## Expansion-plan reconciliation

| Plan revision | Proposed destination | Coverage units absorbed | Conflicts/duplication | Decision |
|---|---|---|---|---|
| Phase 5 rev 2.2 | F0 current-module repairs | Matrix identity/source corrections; quaternion concepts/integration/conversion/retrieval; IL theorem/objective/readiness repairs; milestone correction | None in calibration scope | Accepted; implementation remains pending |
| Phase 5 rev 2.2 | NUM, later visualization/lab modules | Numerical solving, quaternion intuition, BC/DAgger and generative-policy implementation | Future depth must not be counted as current coverage | Accepted as explicit deepening only |
| Phase 5 rev 2.2 | F8 retrieval/cheat-sheet/assessment pass | Calibration practice, static-figure, reference, and assessment findings | None; measurable criteria now distinguish static teaching from optional interactives | `RECONCILED` |
| Phase 5 rev 2.2 | Explicit routes/scope dispositions | General quaternion Jacobian and DTW optional; random rotations and the local VAE planning example explicitly out of scope; feature/constraint content routed | None; VAE planning-sampler connection is preserved through `PLAN-05` | Accepted |
| Next revision pending | MATH and OPT foundation stabilization | Decisions `0006` and `0007`: mandatory repairs, `NUM-03`, `OPT-04B`, `OPT-05B`, compact additions, retrieval, visuals, and assessment work | Revision 2.2's “not missing theory” thesis and 102-module/33-addition counts are now obsolete | Owner-approved delta; Claude incorporation and new hash pending |

## Gate A evidence audit

Gate A artifacts reviewed: `docs/plans/GATE_A_BASELINE.md` (SHA-256 `470046a5fa4036794c37434295cea67385e985ca9871c06413b964dddc1a45a4`), `docs/plans/gate-a-concept-depth-inventory.json` (`d29a5865c17af40c520f3dbef18f10ff8326bdc48a1ad63c7353c811e94e9bce`), and `scripts/validate/gate_a_baseline.py` (`f1bf926bc18301eb9f4d664d8f8bc027b2dc4fa4b6fc4343f4f5a44a1874bced`).

Useful verified evidence includes the 69/15/226 baseline counts, exercise three-way correspondence, current route violation, source-manifest hole, milestone gaps, answer-type gaps, solution leakage, deprecation hints, and bundle measurements. The correction pass resolves all four earlier evidence qualifications:

1. An isolated archive of baseline commit `dd2e871…` independently reproduces the 20,209-word result; the 20,218-word worktree is separately labelled and its nine-word delta explained.
2. The renamed inventory contains 308 declared concepts across all 69 modules and records the evidence-based module depth ceiling. Per-concept depths remain null with an explicit reason until semantic source review, avoiding fabricated judgments.
3. The reporter declares its write, supports `--no-write`, distinguishes `OK`, `REPRO`, `QUEUE`, and `FAIL`, and exits nonzero on a synthetic failure.
4. Readiness and Anki counts are expressly queues for semantic review, not ratio requirements or automatic failures.

Gate A is therefore **review-validated and owner-approved**. Decision record `docs/decisions/0005-gate-a-approved.md` closes the gate. Plan revision 2.2 corrected the two non-blocking UAC/SIM labels without changing the approved evidence or curriculum design.

The correct sequence is: approve this calibration → complete the current-state coverage audit → reconcile it with the expansion plan → decide additions, moves, and removals. The expansion design may proceed in parallel, but it should not be treated as evidence about what the current workbook covers.
