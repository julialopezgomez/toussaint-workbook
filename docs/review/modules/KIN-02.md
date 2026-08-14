# KIN-02 review — Quaternions

Review state: `APPROVED` / `RECONCILED`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Primary source checked: `quaternions` PDF, all five pages

## Verdict

The module teaches a coherent useful core—unit quaternions, exponential/log maps, SLERP, and the unit-quaternion angular Jacobian—and its five exercises have complete feedback. However, it does not cover the “full note” claimed by its metadata/source note. Missing or only implicit material includes quaternion/matrix conversion and vector application, the double-cover equivalence `q ~ -q`, sign handling for shortest-path interpolation, integration on `S^3`, the general non-unit/non-tangent Jacobian treatment, world/body convention conversion, and random-rotation sampling.

The most important issue is conceptual: the lesson says rotations are represented “as `S^3`,” while unit quaternions actually **double-cover** `SO(3)`. The frontmatter and one exercise solution know this, and `PLAN-03` later relies on `q` and `-q` being the same rotation, but the lesson never teaches it. That gap weakens both the first objective and the SLERP claim.

## Scope and curriculum role

| Field | Evidence |
|---|---|
| Tier / time | Tier 1, 3 hours (`KIN-02.mdx:5-6`) |
| Prerequisite | `KIN-01`; readiness checks the axis-angle rotation matrix (`:7,40-47`) |
| Declared next | `KIN-03` (`:30,125`) |
| Important dependents | `KIN-03`, `PLAN-01`, `PLAN-03`, pose/trajectory work throughout DYN/PLAN |
| Cheat sheet | Exp/log and SLERP formulas; no double-cover/sign, differential integration, or Jacobian |
| Milestone | No dedicated KIN milestone exam; KIN content is not explicitly remediated in the DYN exam |
| Build/presentation evidence | Committed route built successfully; generated structure inspected; live appearance pending |

Evidence files: `src/content/course/KIN/KIN-02.mdx`, `src/content/questions/KIN-02.json`, `src/content/solutions/KIN-02.json`, `src/content/cheatsheets/kin.mdx`, plus the directly linked `KIN-01`, `KIN-03`, and `PLAN-03` modules.

`KIN-01` correctly supplies rotation matrices, rotation vectors, Rodrigues, and angular velocity. The module should explicitly route p5 appendix material back to it instead of claiming the entire note locally. `KIN-03` does not depend heavily on quaternion-specific derivations, but `PLAN-03` explicitly says the sign equivalence comes from `KIN-02`, exposing the teaching gap.

## Rubric scores

| Category | Score / 3 | Evidence-based rationale |
|---|---:|---|
| Objective design | 1 | Core objectives are testable but omit essential representation, integration, and convention concepts; first objective is imprecise. |
| Source fidelity | 1 | Several full sections of the claimed complete note are absent. |
| Technical correctness | 2 | Core formulas are sound at the unit/tangent level; shortest-path and double-cover conditions are missing. |
| Prerequisite readiness | 3 | `KIN-01` is appropriate and directly checked. |
| Sequence and links | 2 | Good placement and useful downstream links, but source routing and a downstream sign dependency are inconsistent. |
| Exposition and layout | 2 | Clear progression and good motivation; a cross-domain retrieval analogy is distracting. |
| Visual pedagogy | 1 | No lesson figure for a strongly spatial topic; source figures are limited, so a purposeful redraw is needed. |
| Exercises and feedback | 3 | Five varied, fully solved exercises including symbolic, numeric, and challenge work. |
| Retrieval support | 1 | Three unkeyed prompts, seven notation cards, only two exercise recall cards. |
| Reference usefulness | 2 | Core formulas are easy to revisit; conventions and edge cases are not. |

## Objective and teaching alignment

| Declared objective | Taught | Practised | Judgment |
|---|---|---|---|
| Explain why rotations use `S^3` rather than a minimal chart | Motivation and exercise | Foundation explanation exercise | `CURRENTLY_PARTIAL`: singularities taught; double cover is not |
| Derive exp map and angular-velocity relation | Lines 57–77 | Derivation + symbolic exercises | `CURRENTLY_COVERED` |
| Compute SLERP by hand | Lines 79–89 | Numeric exercise | `CURRENTLY_PARTIAL`: no antipodal/sign handling |
| Derive `w = J(q) qdot` | Lines 91–97 | Challenge derivation | `CURRENTLY_PARTIAL`: only unit/tangent/body form |

Inferred objectives are to select a singularity-free orientation representation, compose relative rotations, and connect parameter velocity to physical angular velocity. Competent use also requires convention, normalization, and sign discipline; those inferred skills are currently under-taught.

## Declared-source audit

| Source unit | Coverage | Finding |
|---|---|---|
| p1 reference definitions and operations | Partial | Representation, inverse, and product appear; quaternion↔matrix conversion and vector application do not. |
| pp1–2 exp/log | Good | Main definition and half-angle relation are taught. |
| p2 SLERP | Partial | Formula is taught, but choosing consistent signs/shortest branch is not. |
| p3 integration on `S^3` | Partial | Differential identity is derived; the integration/update method is absent. |
| p4 angular Jacobian | Partial | Unit/tangent result is taught; general non-normalized/non-tangent treatment and world-coordinate map are absent. |
| p4 random rotations/Gaussian sampling | Missing | No coverage or route. |
| p5 Rodrigues/skew/angular velocity | Routed implicitly | `KIN-01` covers it, but frontmatter says pp1–4 “full note” and the source note says all definitions. |

The PDF has five pages, while frontmatter declares pp1–4 and simultaneously labels that range “full note” (`KIN-02.mdx:14`). This is a source-scope metadata error independent of any pedagogical scope decision.

## Technical and conceptual checks

- The unit-quaternion inverse and half-angle formulas are consistent with the source convention.
- The `qdot = q ∘ 1/2(0,w)` derivation is internally consistent for the chosen body-frame convention; convention should be named because left/right multiplication changes interpretation.
- The source rendering around the derivative appears easy to misread and may omit displayed half factors, while the prose states magnitude `1/2`; the workbook's factor is correct. A provenance note would prevent confusion.
- “Shortest path” SLERP is conditional on choosing the equivalent sign of the target quaternion that gives the shorter arc. The lesson does not state this.
- Normalized linear interpolation traces the same great-circle arc only after compatible sign/branch choice; the current unconditional wording at `:87` is too broad.

## Exercise and retrieval audit

| Surface | Count | Classification / issue |
|---|---:|---|
| Embedded answered exercises | 5 | 1 recall/conceptual foundation, 3 application/derivation, 1 synthesis/challenge |
| End retrieval prompts | 3 | Unkeyed; prompt 3 uses an unrelated sigmoid analogy |
| Matching solutions | 5/5 | Complete rubric, symbolic, and numeric feedback |
| Notation export cards | 7 | Strong formula-symbol coverage |
| Exercise recall cards | 2 | First conceptual exercise and one derivation; remaining core facts absent |
| Cheat-sheet support | 3 formula rows | Exp, log, SLERP only |
| Milestone support | 0 direct KIN exam items identified | Cross-block retention is not demonstrated |

The set is high quality but not recall-primary. Add short answered checks for `q ~ -q`, inverse/product order, exp/log domains, normalization, SLERP sign choice, and frame convention before adding more long derivations.

## Prioritized findings

| ID | Priority | Category | Finding and evidence | Status | Confidence |
|---|---|---|---|---|---|
| KIN02-01 | P1 | Objective/technical | The lesson does not explain the double cover `q ~ -q`; frontmatter names it and `PLAN-03` depends on it. | `PLANNED_TO_ADDRESS` | verified |
| KIN02-02 | P1 | Source fidelity | “Full note” claim conflicts with omitted conversion/application, integration, general Jacobian, sampling, and p5 material. | `PLANNED_TO_ADDRESS` | verified |
| KIN02-03 | P1 | Technical | SLERP's shortest-path claim lacks sign alignment/branch handling; normalized interpolation claim is correspondingly overbroad. | `PLANNED_TO_ADDRESS` | high; benchmark approved |
| KIN02-04 | P1 | Practical skill | Quaternion integration/renormalization on `S^3` is in the source but not taught or exercised. | `PLANNED_TO_ADDRESS` | verified |
| KIN02-05 | P2 | Scope | General angular Jacobian and world/body mapping are absent; decide Tier 1 core versus advanced/routed material. | `PLANNED_TO_ADDRESS` | verified |
| KIN02-06 | P2 | Source completeness | Quaternion↔matrix conversion and vector application are absent from current content. | `PLANNED_TO_ADDRESS` | verified |
| KIN02-07 | P2 | Visual pedagogy | The spatial/double-cover and SLERP ideas have no instructional figure or visual manipulation aid. | `PLANNED_TO_ADDRESS` | high |
| KIN02-08 | P2 | Retrieval | Recall support is sparse; retrieval question 3's sigmoid analogy obscures the direct quaternion identity. | `PLANNED_TO_ADDRESS` | verified |
| KIN02-09 | P2 | Assessment architecture | No direct milestone item tests quaternion competence or catches sign/convention errors. | `PLANNED_TO_ADDRESS` | verified |
| KIN02-10 | P3 | Enrichment | Random rotations/Gaussian sampling from the source is omitted; decide whether robotics simulation needs it here or later. | `INTENTIONALLY_OUT_OF_SCOPE` | verified |

### Finding dispositions

| ID | Taxonomy | Why it matters | Proposed disposition | Curriculum scope | Human judgment? |
|---|---|---|---|---|---|
| KIN02-01 | 3 — incomplete objective | Sign equivalence is foundational and already assumed downstream. | Teach the double cover before SLERP and assess it directly. | Essential main route | No on need; yes on presentation |
| KIN02-02 | 2 — declared-source omission | Source/objective metadata currently overstates completeness. | Correct the range and explicitly route, restore, or scope each omitted unit. | Essential main route | Yes—scope choices |
| KIN02-03 | 1 — technical qualification | A learner can interpolate along the wrong arc or mishandle antipodal endpoints. | Teach dot-product sign selection and branch/edge-case handling. | Essential main route | No after external confirmation |
| KIN02-04 | 2 — declared-source omission | Integration is how angular velocity actually updates simulated/controlled orientation. | Add one integration/update method with normalization and an exercise. | Essential main route | Yes—depth |
| KIN02-05 | 2 — declared-source omission | Optimizers can leave the tangent/unit assumptions used by the displayed Jacobian. | State assumptions in core; route full generalization to an advanced subsection/module if needed. | Essential assumptions; relevant advanced derivation | Yes |
| KIN02-06 | 2 — declared-source omission | Conversion/application is needed to connect the representation to existing rotation tools. | Add a concise route to `KIN-01` plus a conversion reference, or teach locally. | Essential main route/reference | Yes—location |
| KIN02-07 | 7 — layout/visual | The missing concept is geometric and hard to infer from equations alone. | Add the static double-cover/arc figure; consider the lab only after plan review. | Essential main route | Yes—design/tool |
| KIN02-08 | 8 — retrieval practice | Current retrieval does not secure conventions and sign rules. | Replace the cross-domain mnemonic with direct keyed recall and selective cards. | Essential main route | No on rewrite; yes on card volume |
| KIN02-09 | 8 — assessment | Quaternion mistakes may survive until much later applied work. | Add one integrated assessment or explicitly assign it to a later milestone. | Essential main route | Yes—assessment architecture |
| KIN02-10 | 9 — optional enrichment | Sampling matters for simulation but may exceed a three-hour core. | Route to a simulation/probability lab or mark intentionally out of scope. | Relevant advanced / optional reference | Yes |

## Presentation and tool recommendations

The highest-value static visual is a two-part figure: (1) antipodal points `q` and `-q` on `S^3` mapping to the same physical orientation; (2) long versus short interpolation arcs after target-sign selection. A second compact diagram could distinguish body-frame/right-multiplied and world-frame/left-multiplied angular updates.

| Tool candidate | Learning problem | Why static material is insufficient | Form/placement | Compute | Accounts, hosting, maintenance | Simpler alternative |
|---|---|---|---|---|---|---|
| Quaternion pose/interpolation lab | Sign equivalence, path choice, speed, and norm drift are spatial/dynamic and easy to memorize incorrectly. | A static figure can show topology, but cannot reveal interpolation speed or accumulated integration drift under changed inputs. | Prefer an embedded lightweight lab after SLERP; separate optional lab if runtime size is material | CPU only; no GPU | No account/API/key; local/static hosting; small rendering dependency requires maintenance | Static double-cover/arc figure plus plotted angular distance versus time |

The plan owns a static F0 figure and a later optional visualization; exact runtime implementation remains correctly deferred to the runtime-architecture gate.

Provisional external resource: link selected sections of Solà's quaternion reference for convention-sensitive lookup and deeper derivations, while keeping the Tier 1 lesson self-contained. This awaits benchmark approval.

## Candidate restructuring (not authorized)

- **Add:** double cover/sign choice, explicit frame convention, integration, keyed recall, and a static geometric figure.
- **Move/route:** p5 Rodrigues material to the already-existing `KIN-01` coverage; sampling and general Jacobians may become advanced material.
- **Remove/narrow:** replace or narrow the unconditional “full note” and “shortest path” claims unless their missing conditions/content are restored.
- **Merge/split:** consider a core quaternion module plus an advanced integration/Jacobian/sampling unit only if the expansion plan makes the current three-hour scope untenable.

## Phase 5 plan reconciliation

Plan: `docs/plans/PHASE5_AUGMENTATION_PLAN.md`, revision 2.2, pinned SHA-256 `412b807536da6d90b1063ad800aadf5435a6e05eabe6e3cfcd6ea65ac308f2f3`.

| Findings | Plan owner | Mapping |
|---|---|---|
| KIN02-01/03/04 | Gate F0 | Absorbed: double cover, sign/antipodal handling, integration/renormalization, and keyed recall become repairs. |
| KIN02-02 | Gate F0 | Partly absorbed: metadata/source claim and p5 routing are fixed; other omitted units require the mappings below. |
| KIN02-05 | Gate F0 + optional reference | Absorbed for unit/tangent assumptions; full general Jacobian is explicitly optional. |
| KIN02-06 | Gate F0 | Absorbed: revision 2.1 verifies that `KIN-01` does not own this material and assigns both compact formulas to `KIN-02`. |
| KIN02-07 | F0 static figure + later quaternion visualization | Absorbed with the correct teach-first, visualize-second ordering. |
| KIN02-08 | Gate F0 + F8 | Absorbed: F0 rewrites the sigmoid-analogy prompt as direct keyed recall and names the convention targets; F8 separately governs card-export volume. |
| KIN02-09 | Milestone correction in §17.3 | Absorbed: add a real KIN remediation/assessment item to the DYN milestone. |
| KIN02-10 | Explicit scope decision | Intentionally out of scope; may re-enter only if later simulation randomization needs it. |

Current content remains `CURRENTLY_PARTIAL` until F0 and later deepening work are implemented and re-reviewed. All calibration findings now have explicit plan ownership or scope dispositions.

Presentation verification is `STRUCTURE_VERIFIED`. A human should check equation overflow, the density of the opening explanation, and whether a future visualization remains usable at mobile width.

## Human decisions required

- Decide which omitted source topics are core to this Tier 1 module, explicitly routed to `KIN-01`, or moved to an advanced quaternion unit.
- Confirm that double cover, sign alignment, normalization, integration, and convention naming are mandatory core skills.
- Decide whether KIN needs a small milestone or whether these skills will be tested in a later integrated exam.
- Approve or reject the proposed interactive intuition lab after plan reconciliation.
- Perform the marked desktop/mobile visual check.

While studying the module, the owner should also record: where the explanation became unclear; what felt assumed rather than taught; what felt repetitive or unnecessary; which example or figure was most useful; what should be recallable without notes afterward; whether an interactive tool would solve a real difficulty; and whether the module feels appropriately placed in the course.

No curriculum changes should be implemented from this draft until calibration is approved.
