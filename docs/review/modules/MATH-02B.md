# MATH-02B review — Matrix Calculus

Review state: `APPROVED` / `RECONCILED`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Primary source checked: `lecture-maths`, pp15–18 (§2.4–2.4.3)

## Verdict

This is a strong, useful applied module with unusually good derivation practice and clear connections to later robotics/ML. It is not source-complete as currently claimed: the objective, summary, and source note promise “Identities 2.3–2.5,” but the lesson stops after 2.4 and omits the six identities in 2.5, including Woodbury. That omission matters downstream because `ML-05` explicitly invokes Woodbury while attributing the ridge formula back to this module.

The other priority issue is curricular rather than topical: the lesson tells the learner that formal PSD/PD definitions come in `MATH-04`, but they are taught in `MATH-03B`. The page is derivation-rich but does not meet the recall-primary assessment target: eight answered exercises are almost entirely application/derivation, while five recall prompts have no answer key and no exercise recall cards are exported.

## Scope and curriculum role

| Field | Evidence |
|---|---|
| Tier / time | Tier 1, 5 hours (`MATH-02B.mdx:5-6`) |
| Prerequisite | `MATH-02`; readiness checks the quadratic-form gradient (`:7,40-47`) |
| Declared next | `MATH-03` (`:30,181`) |
| Important dependents | `KIN-03`, `DYN-03`, `ML-02`, `ML-05`, `OPT-06`, `MATH-04` |
| Cheat sheet | Math sheet includes quadratic-form gradient and ridge closed form, but not determinant/inverse identities |
| Milestone | `MATH-EXAM` Part 4 provides weighted-least-squares transfer and remediation to `MATH-02B` |
| Build/presentation evidence | Committed route built successfully; generated structure inspected; live appearance pending |

Evidence files: `src/content/course/MATH/MATH-02B.mdx`, `src/content/questions/MATH-02B.json`, `src/content/solutions/MATH-02B.json`, `src/content/cheatsheets/math.mdx`, and `src/content/milestones/MATH-EXAM.mdx`.

The prerequisite edge is appropriate. `MATH-02` explicitly routes matrix identities here and owns the finite-difference workflow from source §2.5, so that adjacent source material is not an omission. Downstream reuse is strong: `KIN-03` deliberately restates the Gauss–Newton form, `DYN-03` applies the same structure, and `ML-02/05` reuse ridge/logistic concepts.

## Rubric scores

| Category | Score / 3 | Evidence-based rationale |
|---|---:|---|
| Objective design | 2 | Specific and testable, but one objective promises absent content. |
| Source fidelity | 2 | Most declared material is covered accurately; Identities 2.5 are absent and the source claim overstates coverage. |
| Technical correctness | 2 | Core derivations are sound; `lambda > 0` needs qualification, one cross-reference is wrong, and source corrections are undisclosed. |
| Prerequisite readiness | 3 | Declared prerequisite is directly checked and sufficient. |
| Sequence and links | 2 | Strong downstream reuse; PSD/PD link is misdirected. |
| Exposition and layout | 2 | Clear progression and worked examples, but dense identity/shape material needs a compact shape aid. |
| Visual pedagogy | 2 | The source itself is equation-led; a shape table/worked dimension check would add more than decorative imagery. |
| Exercises and feedback | 3 | Eight complete exercises with hints and solutions, including numeric and synthesis work. |
| Retrieval support | 1 | Five unkeyed retrieval prompts, three notation cards, zero exercise recall cards. |
| Reference usefulness | 2 | Useful summary and cheat-sheet links, but the cheat sheet omits most of the module's identity toolkit. |

## Objective and teaching alignment

| Declared objective | Taught | Practised | Judgment |
|---|---|---|---|
| Solve matrix equations | Lines 49–61 | Exercises 1–4 | `CURRENTLY_COVERED` |
| Derive ridge normal equations | Lines 63–77 | Exercises 3–4; retrieval 1 | `CURRENTLY_COVERED` |
| Use Identities 2.3–2.5 | Lines 79–96 teach only 2.3–2.4 | Exercise 5 uses 2.3; no 2.5 practice | `CURRENTLY_PARTIAL` |
| Avoid ambiguous direct matrix derivatives | Lines 98–106 | Exercise 6; retrieval 3 | `CURRENTLY_COVERED` |
| Derive GP gradient and logistic Hessian | Lines 108–136 | Logistic numeric check; GP has no dedicated exercise | `CURRENTLY_PARTIAL` |
| Derive robotics Gauss–Newton update | Lines 138–148 | Exercise 8; retrieval 5 | `CURRENTLY_COVERED` |

Inferred objectives are to type-check matrix expressions, recognize one regularized least-squares pattern across ML and robotics, and know when to fall back to elementwise derivatives. These are pedagogically valuable and should either become explicit objectives or remain clearly identified as supporting skills.

## Declared-source audit

The rendered source pages were checked as well as extracted text.

| Source unit | Coverage | Finding |
|---|---|---|
| §2.4 matrix warm-ups | Good | Four appear directly; the nonlinear robotics case appears as the capstone. |
| Ridge worked derivation | Good, with correction | Workbook uses the mathematically correct positive regularizer; source equation 36 appears to contain a negative sign. The correction should be disclosed. |
| Identities 2.3 | Good | General bilinear rule and useful special cases are taught. |
| Identities 2.4 | Good | Determinant and inverse derivatives are taught and used in the GP derivation. |
| Identities 2.5 | Missing | Six identities on source p17, including Woodbury, do not appear despite three coverage claims. |
| §2.4.1 matrix derivatives | Good | Elementwise fallback and representative identities are present. |
| §2.4.2 GP example | Good | The main calculation is present; it is not independently assessed. |
| §2.4.3 logistic example | Good | Gradient-to-Hessian chain is present and checked numerically. |

## Exercise and retrieval audit

| Surface | Count | Classification / issue |
|---|---:|---|
| Embedded answered exercises | 8 | 7 application/short derivation, 1 synthesis/challenge, 0 pure recall |
| End retrieval prompts | 5 | Recall/derivation cues, but no answer key |
| Matching solutions | 8/8 | Complete; seven rubric/deterministic derivations and one numeric checker |
| Notation export cards | 3 | Inverse-transpose, trace, determinant |
| Exercise recall cards | 0 | Every `reviewCardIds` list is empty |
| Cheat-sheet entries | 2 core entries | Quadratic gradient and ridge; no Identities 2.4/2.5 or Gauss–Newton form |
| Milestone coverage | 1 transfer pair | Strong synthesis; not a substitute for routine retrieval |

The module is excellent for working understanding but heavily misses the 60/30/10 recall-primary target if unkeyed prompts are not counted. A later implementation should add short answered recall for identities, assumptions, and shape conventions without removing the derivation set.

## Prioritized findings

| ID | Priority | Category | Finding and evidence | Status | Confidence |
|---|---|---|---|---|---|
| M02B-01 | P1 | Source/objective completeness | Identities 2.5 are promised at `:11,154,177` but absent; source p17 contains six identities including Woodbury. | `PLANNED_TO_ADDRESS` | verified |
| M02B-02 | P1 | Sequence/link | `:134` links formal PSD/PD definitions to `MATH-04`; the dedicated treatment is `MATH-03B`. | `PLANNED_TO_ADDRESS` | verified |
| M02B-03 | P2 | Technical qualification | `:77` says `lambda I` makes the matrix invertible without stating `lambda > 0`; the later Hessian paragraph does state that condition. | `PLANNED_TO_ADDRESS` | verified |
| M02B-04 | P2 | Numerical practice | Closed forms repeatedly display explicit matrix inversion. A practical note should distinguish mathematical notation from solving a linear system numerically. | `PLANNED_TO_ADDRESS` | high; benchmark approved |
| M02B-05 | P2 | Provenance | The workbook correctly changes the apparent source sign in the ridge solution but does not identify the correction. | `PLANNED_TO_ADDRESS` | high |
| M02B-06 | P2 | Retrieval | Core identity/assumption recall is unkeyed and omitted from exercise-card export. | `PLANNED_TO_ADDRESS` | verified |
| M02B-07 | P2 | Reference support | Cheat sheet represents only a small fraction of the module's promised identity toolkit. | `PLANNED_TO_ADDRESS` | verified |
| M02B-08 | P3 | Presentation | Add a matrix-shape table and one worked dimension/type check near Identities 2.3. | `PLANNED_TO_ADDRESS` | high |

### Finding dispositions

| ID | Taxonomy | Why it matters | Proposed disposition | Curriculum scope | Human judgment? |
|---|---|---|---|---|---|
| M02B-01 | 2 — declared-source omission | A declared objective cannot be mastered; Woodbury is used later. | Teach and practise 2.5 here, or narrow the objective/source claim and explicitly route every identity. | Essential main route | Yes—choose location |
| M02B-02 | 5 — sequence/cross-reference | Learners following the link reach the wrong concept. | Change the destination to `MATH-03B` during implementation. | Essential main route | No |
| M02B-03 | 1 — factual qualification | The invertibility statement is false at `lambda = 0` and depends on regularizer assumptions. | State `lambda > 0` (or positive-definite regularizer). | Essential main route | No |
| M02B-04 | 4 — provisional external gap | Literal use of the displayed inverse encourages unstable/inefficient code. | Add a short numerical-practice note and, if approved, a shared lab. | Essential main route / modern practice | Yes—depth/location |
| M02B-05 | 6 — writing/provenance | Silent corrections make source comparison look inconsistent. | Add a concise source-correction note, preserving attribution. | Optional reference | No |
| M02B-06 | 8 — retrieval practice | Core knowledge is hard to retain despite strong derivation practice. | Add answerable recall items and selectively export durable cards. | Essential main route | Yes—system-wide policy |
| M02B-07 | 8 — retrieval/reference | The reference surface does not match the module's stated toolkit. | Add only the identities judged worth routine lookup/recall. | Essential main route | Yes—formula selection |
| M02B-08 | 7 — layout/visual | Shape errors are the module's stated major failure mode. | Add a static shape/convention table before considering a richer tool. | Essential main route | Yes—design review |

## Presentation and tool recommendations

The page has a sound pedagogical arc: algebra warm-up → ridge derivation → reusable identities → elementwise fallback → GP/logistic applications → robotics synthesis. The declared source pages are also mostly equations, so absence of a decorative figure is not a flaw. The most useful visual intervention would be a compact table showing input/output shapes under the row-Jacobian convention, plus color or annotation linking each term in one derivative to its dimensions.

| Tool candidate | Learning problem | Why static material is insufficient | Form/placement | Compute | Accounts, hosting, maintenance | Simpler alternative |
|---|---|---|---|---|---|---|
| Linear-solve and gradient-check notebook | Learner sees formulas but not conditioning, residuals, or implementation failure modes. | Conditioning and finite-difference error become intuitive only when parameters vary and residuals are measured. | Optional shared lab after `MATH-02B`, linked also from `ML-02` | CPU core; no GPU | No account/API; local or static-notebook hosting; light NumPy maintenance | Static worked table comparing inverse, solve, residual, and condition number |

The plan assigns this to the CPU-first NUM lab family; final embedded-versus-linked presentation is intentionally deferred to the runtime-architecture gate.

Provisional external resource: use *The Matrix Cookbook* only as a compact identity/convention cross-check and later reference link, not as a replacement for the module's explanations. This awaits benchmark approval.

## Candidate restructuring (not authorized)

- **Add:** Identities 2.5 or an explicit routed reference; keyed recall; shape/convention table.
- **Move/share:** numerical linear-solve lab across `MATH-02B` and `ML-02`.
- **Remove/narrow:** only narrow “2.3–2.5” claims if the owner intentionally excludes 2.5; do not silently leave the mismatch.
- **Merge/split:** no merge or split is justified by calibration evidence.

## Phase 5 plan reconciliation

Plan: `docs/plans/PHASE5_AUGMENTATION_PLAN.md`, revision 2.2, pinned SHA-256 `412b807536da6d90b1063ad800aadf5435a6e05eabe6e3cfcd6ea65ac308f2f3`.

| Findings | Plan owner | Mapping |
|---|---|---|
| M02B-01/02/03/05/08 | Gate F0 calibration repair | Absorbed: identity coverage, correct link/condition, correction note, and shape table are explicit repairs. |
| M02B-04 | F0 pointer plus `NUM-01/02` | Absorbed: mathematical formula remains here; numerical solve/conditioning practice deepens in NUM. |
| M02B-06/07 | F8 retrieval/cheat-sheet pass | Absorbed; revision 2.1 supplies measurable F8 acceptance criteria for keyed recall, reference coverage, and static figures. |

Current content remains `CURRENTLY_PARTIAL` until those plan items are implemented and re-reviewed. Reconciliation is complete; that status records plan ownership, not completed content.

Presentation verification is `STRUCTURE_VERIFIED`. The committed build succeeds, but a human should still inspect equation wrapping, callout density, and the exercise-card flow at desktop and mobile widths.

## Human decisions required

- Confirm that Identities 2.5 belong in `MATH-02B` rather than being explicitly routed to `ML-05` or a reference appendix.
- Decide whether numerical linear-algebra practice is core here or an attached lab.
- Approve the recall-counting rule that excludes unanswered retrieval prompts from the 60/30/10 balance.
- Perform the marked desktop/mobile visual check.
- After Claude's plan is stable, map findings 04, 06, 07, and 08 to exact plan items or leave them open.

While studying the module, the owner should also record: where the explanation became unclear; what felt assumed rather than taught; what felt repetitive or unnecessary; which example or figure was most useful; what should be recallable without notes afterward; whether an interactive tool would solve a real difficulty; and whether the module feels appropriately placed in the course.

No curriculum changes should be implemented from this draft until calibration is approved.
