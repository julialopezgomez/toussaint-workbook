# RLEARN-02 review — Imitation Learning

Review state: `APPROVED` / `RECONCILED`
Overall current-state status: **`CURRENTLY_PARTIAL`**
Baseline: `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
Primary source checked: `lecture-robotlearning`, pp35–56 (§1.6–1.7)

## Verdict

This module provides an effective compact map of imitation learning: behavior cloning, trajectory distributions, distribution shift, the compound-error motivation for DAgger, demonstration collection, and generative policy families. Its strongest teaching sequence—naive supervised formulation → state-distribution mismatch → DAgger—is clear, correctly reused downstream, and assessed again in the RLEARN milestone.

The declared 22-page source range is too compressed to call complete without clearer scope decisions. Dynamic time warping is absent; learned features/constraints are reduced to one sentence; a VAE motion-planning example is replaced rather than routed; diffusion training/sampling is only sketched; ALOHA/ACT omits action chunking and temporal ensembling; and the source's central GAN/VAE/diffusion tradeoff comparison is neither an objective nor an exercise. The page also states the behavior-cloning theorem without assumptions and overgeneralizes modern generative imitation as `p(u_t | x_t)` even while its own ACT example consumes observations and emits action sequences.

## Scope and curriculum role

| Field | Evidence |
|---|---|
| Tier / time | Tier 1, 4 hours (`RLEARN-02.mdx:5-6`) |
| Prerequisites | `ML-04`, `RL-04`, `RLEARN-01` (`:7`) |
| Readiness | Only `ML-04` empirical-risk minimization is checked (`:34-41`) |
| Declared next | `RLEARN-03` (`:24,138`) |
| Important dependents | `RLEARN-04/05/06/07/08`, `REV2`, `CAP` |
| Cheat sheet | BC objective and DAgger/distribution-shift summary |
| Milestone | `RLEARN-EXAM` Part 1 compares DAgger with offline-RL responses to distribution mismatch |
| Build/presentation evidence | Committed route built successfully; generated structure inspected; live appearance pending |

Evidence files: `src/content/course/RLEARN/RLEARN-02.mdx`, `src/content/questions/RLEARN-02.json`, `src/content/solutions/RLEARN-02.json`, `src/content/cheatsheets/rlearn.mdx`, `src/content/milestones/RLEARN-EXAM.mdx`, and the dependent `RLEARN-04` through `RLEARN-07` lessons.

The module is well placed after dynamics learning and before robot RL/offline RL. `RLEARN-04` explicitly reuses its distribution-shift model; `RLEARN-05` reuses GAN/GAIL; `RLEARN-06` reuses privileged teachers and diffusion; `RLEARN-07` develops Deep Visual Constraints; and `REV2` synthesizes privileged-teacher patterns. These are coherent dependents. The readiness check, however, does not verify the policy-gradient or robot-learning prerequisites declared in frontmatter.

## Rubric scores

| Category | Score / 3 | Evidence-based rationale |
|---|---:|---|
| Objective design | 2 | Clear BC/DAgger core; generative objective names formulations but omits comparison and modern sequence-policy mechanics. |
| Source fidelity | 1 | Many source concepts/case-study mechanisms are omitted or highly compressed without explicit routing. |
| Technical correctness | 2 | Core intuition is good; theorem assumptions and policy conditioning/output generalization need qualification. |
| Prerequisite readiness | 1 | Three prerequisites declared, one checked. |
| Sequence and links | 3 | Strong downstream reuse and milestone integration. |
| Exposition and layout | 2 | Clear storyline and useful landscape table; generative section is formula-dense and survey-like. |
| Visual pedagogy | 1 | No instructional figures despite source diagrams carrying much of the intuition. |
| Exercises and feedback | 2 | Five complete conceptual exercises; limited procedural/coding practice and no synthesis challenge. |
| Retrieval support | 1 | Four unkeyed retrieval prompts, three notation cards, zero exercise recall cards. |
| Reference usefulness | 2 | Good summary/cheat-sheet BC core; weak generative comparison/reference support. |

## Objective and teaching alignment

| Declared objective | Taught | Practised | Judgment |
|---|---|---|---|
| State BC and explain why it is not ordinary supervised learning | Lines 43–58, 71–79 | Exercises 2–3; retrieval 1–2 | `CURRENTLY_COVERED` |
| Derive compound error and explain DAgger | Lines 71–89 | Exercises 2–3; retrieval 2–3; milestone transfer | `CURRENTLY_PARTIAL`: result is stated, not derived, and assumptions are absent |
| State GAN/VAE/diffusion and IL instantiations | Lines 96–104 | Exercise 5; retrieval 4 | `CURRENTLY_PARTIAL`: formulas/roles present; tradeoffs and application mechanics thin |

The objective set itself is incomplete relative to the source and intended practical teaching. It should either include trajectory-distribution learning/data collection and comparative model selection, or explicitly label those sections as reference-only enrichment.

Inferred objectives are to distinguish four imitation-learning strategies, choose a demonstration-collection method, recognize privileged-teacher distillation, and understand why multimodality motivates generative policies. These occupy substantial lesson space and should be promoted to objectives or intentionally labelled supporting/reference material.

## Declared-source audit

The source range was rendered and inspected at key pages, including the GMM, distribution-shift, DAgger, privileged-teacher, generative-comparison, and ALOHA material.

| Source unit | Coverage | Finding |
|---|---|---|
| Behavior cloning and trajectory-distribution learning | Good core | GMM/ProMP and bottleneck intuition present. Dynamic time warping is absent. |
| Learned features and constraints | Very compressed | KPAM, neural descriptor fields, and Deep Visual Constraints collapse to one active-research sentence; only one branch is developed later. |
| Distribution-shift diagrams and compound-error result | Textually good | Explanation is clear, but the source's visual causal sequence is lost. |
| DAgger | Good core | Algorithmic idea and interactive-expert cost are stated; no pseudocode/rollout exercise. |
| Data collection and privileged teacher | Good survey | Modes and central tradeoff are present and assessed. |
| GAN | Partial | Formulation and GAIL mapping present; training behavior/mode-coverage tradeoffs not compared. |
| VAE | Partial | ELBO-style loss and ACT conditional VAE present; source motion-planning sampling example omitted. |
| Diffusion | Partial | Forward/reverse distributions present; objective, scheduler intuition, and iterative policy sampling not worked. |
| Generative-family comparison | Missing | Source asks about quality, efficiency, coverage, and ease; exercise only asks network count and role. |
| ALOHA/ACT | Partial | CVAE structure present; action chunking, temporal ensembling, and architecture/data details omitted. |
| Domain-adaptive IL | Compressed | Multi-page algorithm/case study becomes one paragraph; acceptable only if intentionally scoped as a glimpse. |

## Technical and provenance checks

- `RLEARN-02.mdx:79` labels the Ross et al. statement a theorem but omits assumptions and the relationship between surrogate loss and task cost. The original paper should be used for the final wording after benchmark approval.
- “No additional per-step mistakes needed” at `:79` is rhetorically misleading: compounding is precisely about the consequences and changed distribution generated by mistakes. The point should be made without implying subsequent behavior is error-free.
- `:98` says generative IL learns `p(u_t | x_t)` directly. Modern examples on the same page condition on observation history and generate action chunks/sequences; the notation should be introduced as the simplest case, not the definition.
- The module names Ross et al., GAIL, ACT/ALOHA, Diffusion Policy, and case-study papers, while frontmatter lists only the lecture notes. Existing source-mediated citation may satisfy the repository convention, but theorem and modern-method claims would be easier to verify if original papers were recorded as supporting sources.
- The source itself is a broad lecture survey. Compression is legitimate, but “adapted from pp35–56” should not imply every example/mechanism is covered.

## Exercise and retrieval audit

| Surface | Count | Classification / issue |
|---|---:|---|
| Embedded answered exercises | 5 | 1 recall, 4 application/explanation, 0 synthesis/challenge |
| End retrieval prompts | 4 | Broad, unkeyed; the fourth asks three model formulas at once |
| Matching solutions | 5/5 | Complete rubric solutions and useful hint chains |
| Notation export cards | 3 | Policy, epsilon, and model symbols |
| Exercise recall cards | 0 | Every `reviewCardIds` list is empty |
| Cheat-sheet support | BC/DAgger only | Generative models and data-collection distinctions largely absent |
| Milestone support | 1 integrated question/retake pair | Strong DAgger/offline-RL synthesis; no generative-policy assessment |

The exercises reward understanding but do not implement the recall-primary target. High-value short checks include: BC objective and distribution measure; the two expectations being contrasted; DAgger steps/required access; data-collection method distinctions; GAN/VAE/diffusion objective/strength/weakness; and state-conditioned versus history/action-chunk policy notation. A small synthesis task could select a method under expert-access, multimodality, latency, and compute constraints.

## Prioritized findings

| ID | Priority | Category | Finding and evidence | Status | Confidence |
|---|---|---|---|---|---|
| RLN02-01 | P1 | Objective/source completeness | The source's comparative GAN/VAE/diffusion learning goal is missing from objectives, exposition, and assessment. | `PLANNED_TO_ADDRESS` | verified |
| RLN02-02 | P1 | Technical | Compound-error theorem is stated without assumptions and with an overstrong explanatory sentence. | `PLANNED_TO_ADDRESS` | high; benchmark approved |
| RLN02-03 | P1 | Prerequisite readiness | `RL-04` and `RLEARN-01` are declared but not checked or named in readiness. | `PLANNED_TO_ADDRESS` | verified |
| RLN02-04 | P2 | Source fidelity | Dynamic time warping, VAE motion-planning sampling, and several feature/constraint mechanisms are absent from current content. | `PLANNED_TO_ADDRESS` | verified |
| RLN02-05 | P2 | Modern policy framing | `p(u_t | x_t)` is presented as generic generative IL despite history-conditioned, action-sequence policies on the same page. | `PLANNED_TO_ADDRESS` | verified |
| RLN02-06 | P2 | Practical completeness | Diffusion objective/sampling workflow and ACT action chunking/temporal ensembling are not taught. | `PLANNED_TO_ADDRESS` | verified |
| RLN02-07 | P2 | Visual pedagogy | High-value source figures for shift, DAgger, privileged teachers, model comparison, and ACT are omitted. | `PLANNED_TO_ADDRESS` | verified |
| RLN02-08 | P2 | Retrieval | No exercise recall cards; broad unkeyed retrieval prompts do not provide calibration. | `PLANNED_TO_ADDRESS` | verified |
| RLN02-09 | P2 | Assessment | Milestone tests DAgger but neither trajectory models nor generative IL; embedded set has no synthesis challenge. | `PLANNED_TO_ADDRESS` | verified |
| RLN02-10 | P3 | Provenance | Supporting original sources for theorem/current method claims are not represented in frontmatter. | `PLANNED_TO_ADDRESS` | high |

### Finding dispositions

| ID | Taxonomy | Why it matters | Proposed disposition | Curriculum scope | Human judgment? |
|---|---|---|---|---|---|
| RLN02-01 | 3 — incomplete objective | Naming three model families without comparing when/why to use them is not actionable understanding. | Add a comparison objective, explanation, and selection exercise. | Essential main route | Yes—expected depth |
| RLN02-02 | 1 — technical qualification | A theorem without conditions can be overgeneralized and the explanation can misstate the mechanism. | Verify against Ross et al.; state assumptions and a precise intuition. | Essential main route | No after source approval |
| RLN02-03 | 5 — prerequisite problem | Learners can enter without the policy/robot-learning concepts the module declares. | Add readiness prompts or remove prerequisites proven unnecessary. | Essential main route | Yes—prerequisite intent |
| RLN02-04 | 2 — declared-source omission | Silent compression makes near-total source coverage unverifiable. | Route feature/constraint work to `RLEARN-07`; decide whether DTW and motion-planning sampling belong here. | Relevant advanced / optional reference | Yes |
| RLN02-05 | 1 — technical overgeneralization | State-only, one-step notation misrepresents current sequence policies. | Present it as the simplest case and introduce history/action-chunk notation. | Essential main route | No |
| RLN02-06 | 2 — declared-source omission | Learners cannot connect formulas to how a modern policy is trained and executed. | Teach one compact diffusion workflow and ACT chunk/ensemble mechanism; deeper training may be a lab/advanced unit. | Essential modern practice / relevant advanced | Yes |
| RLN02-07 | 7 — layout/visual | The causal and architectural ideas are harder to understand in dense prose. | Reuse/redraw selected source diagrams with attribution. | Essential main route | Yes—figure selection |
| RLN02-08 | 8 — retrieval practice | Retention support is not proportional to the module's breadth. | Add keyed short recall and selective export cards. | Essential main route | Yes—system-wide volume |
| RLN02-09 | 8 — assessment | Current assessment validates one core thread but not model choice or practical policy structure. | Add one constrained method-selection synthesis item; assign generative mechanics to a lab/exam if approved. | Essential main route | Yes |
| RLN02-10 | 6 — provenance improvement | Direct theorem/method verification is difficult through one broad secondary note. | Record original papers as supporting sources while keeping the lecture note primary. | Optional reference / research orientation | Yes—citation policy |

## Presentation and tool recommendations

The source already supplies visual structures worth reusing or redrawing with attribution. Priority order:

1. a two-lane rollout showing expert-state versus learner-state distributions and compounding drift;
2. a DAgger loop diagram connecting rollout, expert query, aggregation, and retraining;
3. a comparison table/diagram for GAN, VAE, and diffusion across objective, networks, coverage/multimodality, stability, and inference cost;
4. an ACT diagram showing observation/history input, latent style, action chunk output, and temporal ensembling.

| Tool candidate | Learning problem | Why static material is insufficient | Form/placement | Compute | Accounts, hosting, maintenance | Simpler alternative |
|---|---|---|---|---|---|---|
| BC-versus-DAgger rollout lab | The state-distribution feedback loop and horizon scaling remain abstract. | Learners need to observe visited-state distributions change under their own policy errors. | Optional lab immediately after DAgger; link from `RLEARN-04` | CPU core; no GPU | No account/API; local or static-hosted notebook; maintain only a tiny environment | Source-derived rollout diagram plus hand-computed short trajectory |
| Multimodal conditional-policy lab | A deterministic mean action can be invalid when demonstrations are multimodal. | Sampling/averaging behavior becomes clear by fitting and plotting a small distribution. | Optional lab after generative comparison | CPU for 1-D core; optional GPU extension only | No paid account/key; local execution; framework version maintenance if neural extension retained | Static two-mode density and mean-action counterexample |

GPU work must be explicitly optional. The plan owns the learning destinations while exact runtime architecture remains correctly deferred to Gate D.

Provisional external resources: the original DAgger paper should verify the theorem statement, while a dated CS 285 lecture can offer optional modern reinforcement. Neither should replace the module or create a finalized external gap before corpus approval.

## Candidate restructuring (not authorized)

- **Add:** comparative model-selection objective, precise theorem conditions, modern sequence-policy notation, selected source diagrams, keyed recall.
- **Move/route:** explicitly route learned constraints/descriptor methods to `RLEARN-07`; consider a shared generative-policy lab.
- **Remove/narrow:** narrow the 22-page source-coverage claim or label compressed case studies as reference glimpses.
- **Merge/split:** if four hours cannot support both IL fundamentals and generative policy mechanics, split into a core BC/DAgger module and a later generative-policy module rather than further compressing both.

## Phase 5 plan reconciliation

Plan: `docs/plans/PHASE5_AUGMENTATION_PLAN.md`, revision 2.2, pinned SHA-256 `412b807536da6d90b1063ad800aadf5435a6e05eabe6e3cfcd6ea65ac308f2f3`.

| Findings | Plan owner | Mapping |
|---|---|---|
| RLN02-01/03/05 | Gate F0 | Absorbed: comparison objective/exercise, prerequisite readiness, and modern conditional/action-chunk notation are explicit repairs. |
| RLN02-02 | F0 after original-paper check | Absorbed. The review benchmark is now owner-approved, so the original DAgger-paper check is authorized. |
| RLN02-04 | F0 routing/scope | Fully disposed: feature/constraint work routes to `RLEARN-07`; DTW is an optional reference; the substituted VAE planning-sampler example is explicitly out of scope here and cross-routed to `PLAN-05`. |
| RLN02-06 | `DRL-07/08` plus forward route | Absorbed as deepening, provided F0 clearly states what is deferred. |
| RLN02-07/08/09 | F8 visual/retrieval/assessment pass | Absorbed; revision 2.1 provides measurable static-figure, keyed-recall, reference, and assessment criteria. |
| RLN02-10 | Gate B source-manifest work | Absorbed: original papers become structured supporting sources while the lecture notes remain primary. |

Current content remains `CURRENTLY_PARTIAL` until the owned work is implemented and re-reviewed. Reconciliation is complete; the explicit scope decisions do not claim current coverage.

Presentation verification is `STRUCTURE_VERIFIED`. A human should inspect the long data-collection paragraph, formula wrapping in the generative section, table readability, and any future diagrams at desktop and mobile widths.

## Human decisions required

- Decide whether this remains a four-hour survey or splits into an imitation-learning core plus a generative-policy module/lab.
- Decide which source examples are intentionally omitted, routed to `RLEARN-07`, or restored here.
- Approve the external original-paper check before finalizing theorem wording.
- Decide whether generative-family comparison and action-chunk policy mechanics are Tier 1 essentials.
- Approve the CPU-first lab concept only after expansion-plan reconciliation.
- Perform the marked desktop/mobile visual check.

While studying the module, the owner should also record: where the explanation became unclear; what felt assumed rather than taught; what felt repetitive or unnecessary; which example or figure was most useful; what should be recallable without notes afterward; whether an interactive tool would solve a real difficulty; and whether the module feels appropriately placed in the course.

No curriculum changes should be implemented from this draft until calibration is approved.
