# Workbook review protocol

Status: **owner-approved on 2026-08-14; plan reconciliation active**
Baseline: commit `dd2e8717f82dfcb77aff4b8c89aba258997f87fe` (Phase 4)
Calibration modules: `MATH-02B`, `KIN-02`, `RLEARN-02`

Approved operating defaults: relevance-scoped completeness; autonomous triage of minor/clearly resolved findings; human escalation for consequential scope, sequencing, or pedagogical choices; batched human review at block boundaries; and workbook-wide rather than rigid per-module exercise balance. Unanswered retrieval prompts do not count as fully supported recall practice.

## Purpose and boundaries

This protocol turns module review into a repeatable evidence process. It evaluates whether the workbook is a coherent start-to-finish course and a usable modular reference, without confusing the current curriculum with proposed expansion work.

Review is read-only with respect to curriculum and application code. Review records may be written under `docs/review/`; findings are recommendations, not permission to implement them. Public source material may be quoted or adapted with normal attribution, consistent with the repository's existing practice. Rights questions are not a review gate.

The committed Phase 4 tree is the current-state baseline. Uncommitted work is excluded from evidence. The expansion plan is a separate input and must be reconciled only after Claude has written it down in a stable, identifiable file.

## The three completeness tests

Every module receives three separate judgments. They must not be collapsed into one “complete/incomplete” verdict.

1. **Source completeness** — Does the module accurately cover its declared source range? This includes definitions, derivations, algorithms, examples, figures that carry instructional meaning, caveats, and exercises. If material is intentionally delegated elsewhere, the target module must be named and checked.
2. **Curriculum completeness** — Are the objectives themselves sufficient for the module's role? Are prerequisites available, terminology and notation consistent, cross-links correct, and downstream modules prepared? Does the block and overall curriculum cover what it claims to teach?
3. **External completeness** — Against an owner-approved benchmark corpus, is an important idea absent from both the workbook and its primary notes? External findings remain provisional until the corpus is approved.

## Fixed evidence hierarchy

Use evidence in this order:

1. committed module, question, solution, cheat-sheet, exam, and export files;
2. the exact source pages declared in module frontmatter, plus adjacent pages only when needed to resolve a boundary;
3. predecessor and dependent modules found by explicit links and concept reuse;
4. the generated committed site, including build integrity and markup structure;
5. owner-approved external sources;
6. reviewer inference, clearly labelled as such.

A finding must cite a file and line, source page/section, or approved external URL. “Standard practice” without a source is not enough for an external gap.

Mechanical checks are screening instruments, not semantic verdicts. A raw count such as “fewer readiness widgets than prerequisites” may nominate modules for review, but one well-designed check can cover multiple prerequisites and a soft prerequisite may not need its own widget. Likewise, an empty `reviewCardIds` list measures sparse exercise-to-Anki export, not total retrieval quality. Final findings require content-aware inspection of the complete learning loop.

## Review rubric

Score each category from 0–3. The score is an aid to judgment, not a substitute for the finding log.

| Category | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Objective design | Missing or misleading | Major objective gaps | Mostly sufficient; small gaps | Complete, testable, appropriately scoped |
| Source fidelity | Materially inaccurate | Major omissions | Minor omissions/overclaims | Accurate coverage or explicit routing |
| Technical correctness | Blocking errors | Several consequential issues | Minor qualifications needed | Checked and correct at intended level |
| Prerequisite readiness | Missing prerequisites | Significant assumed knowledge | Mostly ready | Declared, tested, and available |
| Sequence and links | Contradictory/broken | Important misrouting | Mostly coherent | Forward/backward links reinforce learning |
| Exposition and layout | Hard to follow | Uneven or overloaded | Clear with local improvements | Excellent progression and scanability |
| Visual pedagogy | Needed visuals absent | Weak/ornamental | Useful but incomplete | Visuals directly support spatial/algorithmic intuition |
| Exercises and feedback | Missing or unchecked | Poor alignment/feedback | Good but imbalanced | Complete, varied, answerable, objective-aligned |
| Retrieval support | No durable recall path | Sparse/accidental | Most core facts retrievable | Systematic spaced-recall coverage |
| Reference usefulness | Hard to revisit | Key facts buried | Good summaries/cheat sheet | Excellent module + block-level retrieval |

Each module receives:

- an overall status, not an averaged score;
- category scores with evidence;
- prioritized findings;
- explicit human decisions;
- a list of implementation candidates held for a later phase.

## Finding statuses and priorities

Classify every material finding as one of:

1. verified factual or mathematical error;
2. verified omission from a declared source;
3. incomplete or poorly scoped learning objective;
4. externally revealed gap in the declared source corpus;
5. prerequisite, sequence, notation, or cross-reference problem;
6. pedagogical or writing improvement;
7. layout or visual-design improvement;
8. exercise or retrieval-practice improvement;
9. optional enrichment;
10. subjective question requiring owner judgment.

Every finding row must record: evidence; why it matters; proposed disposition; curriculum scope (`essential main route`, `relevant advanced`, `optional reference`, or `outside intended scope`); integration status; priority; confidence; and whether human judgment is required.

Use exactly one integration status:

- `CURRENTLY_COVERED`
- `CURRENTLY_PARTIAL`
- `PLANNED_TO_ADDRESS` — only after a stable plan explicitly owns it
- `UNPLANNED_GAP`
- `INTENTIONALLY_OUT_OF_SCOPE`
- `PENDING_PLAN_RECONCILIATION`

Use priorities:

- **P0** — invalidates teaching, assessment, or build; resolve before use.
- **P1** — important missing/incorrect concept or broken sequence.
- **P2** — meaningful clarity, exercise, layout, or resource improvement.
- **P3** — polish or optional enrichment.

Confidence is `verified`, `high`, `medium`, or `hypothesis`. External conclusions are never above `high` until the benchmark corpus is approved.

## Exercise classification

The design target is approximately **60% recall, 30% application or short derivation, and 10% synthesis/challenge** across the usable learning loop—not necessarily inside every single page. Count only prompts with an answer or an explicit self-check path. Unanswered retrieval lists are valuable study cues but are reported separately because the learner cannot reliably calibrate an answer.

- **Recall**: state, identify, reproduce, distinguish, or execute one rehearsed step.
- **Application/short derivation**: select and apply a method, calculate, or explain a causal relationship.
- **Synthesis/challenge**: combine modules, derive a non-routine result, design, debug, or compare alternatives under constraints.

For each module record:

1. count embedded exercises by class and difficulty;
2. count end-of-module retrieval prompts separately;
3. verify every exercise has a matching solution/checker;
4. inspect `reviewCardIds` and notation cards for export coverage;
5. inspect block cheat sheets and milestone exams;
6. flag duplicated assessment as well as missing assessment.

## Module review procedure

1. **Pin the baseline.** Record commit, module file, declared hours/tier, sources, prerequisites, and next modules.
2. **Map objectives.** Decompose each objective into teachable claims and map each to exposition, exercise, summary, and later use.
3. **Audit the declared source.** Create a section-by-section ledger: covered, partial, routed elsewhere, or missing. Check equations and source-specific corrections.
4. **Audit technical content.** Recompute representative derivations or check against the source. Record assumptions, conventions, edge cases, and notation conflicts.
5. **Trace the curriculum graph.** Read direct prerequisites, named next modules, and meaningful dependents. Verify readiness checks match all declared prerequisites.
6. **Audit learning support.** Questions, solutions, hint progression, retrieval prompts, Anki export, cheat sheet, and milestone exam.
7. **Inspect presentation.** Check heading hierarchy, paragraph density, tables, callouts, figures, captions, equation overflow, code blocks, and navigation at desktop and mobile widths.
8. **Apply the external benchmark.** Only after owner approval. Separate source-note omissions from deliberate scope choices.
9. **Reconcile the expansion plan.** Convert a finding to `PLANNED_TO_ADDRESS` only when a plan item names an owner/location and preserves sequence/notation.
10. **Human sign-off.** The owner accepts, rejects, modifies, defers, or marks each P1/P2 finding out of scope.

For every proposed internal or external tool, also record: the learning problem; why prose/equations/static figures are insufficient; embed/link/optional-lab placement; CPU/GPU needs; account/API/hosting/maintenance implications; a simpler alternative; and likely curriculum location. No paid dependency may be required.

## Presentation verification levels

- `VISUALLY_VERIFIED`: rendered page inspected at representative desktop and mobile widths.
- `STRUCTURE_VERIFIED`: committed build and generated markup inspected; appearance still needs human/browser review.
- `NOT_VERIFIED`: no render/build evidence.

Calibration is currently `STRUCTURE_VERIFIED`: the committed site builds all 100 pages successfully and includes all three routes. Live desktop/mobile appearance remains a sign-off item because the browser-control surface was unavailable in the calibration session. Source PDFs were rendered and inspected page by page.

## Plan reconciliation contract

Record these fields before reconciling:

- plan file/path or immutable URL;
- plan revision/date;
- proposed block/module IDs and ordering;
- notation and prerequisite policy;
- proposed exercise/runtime/tooling architecture;
- explicit ownership of each existing finding.

For every finding, record one of:

- **absorbed** — exact plan item and destination;
- **superseded** — newer design addresses the same need differently;
- **still open** — plan does not address it;
- **conflict** — plan would duplicate, reorder, or contradict current material;
- **out of scope** — owner decision and rationale.

Do not delay the current-state audit until the plan is finished. Reviewing the baseline first prevents the expansion plan from hiding existing omissions. Do not finalize implementation priorities until reconciliation is complete.

## Human review workflow

The owner should review one calibration record at a time:

1. confirm source-scope interpretation;
2. accept or challenge the overall status and P1 findings;
3. approve the external benchmark corpus or request substitutions;
4. perform the marked live visual checks;
5. approve the rubric and exercise-counting rules;
6. only then authorize the remaining 66-module review.

The calibration passes when the owner agrees that two reviewers applying this protocol would identify substantially the same major gaps and assign similar priorities.

## Stopping and approval gates

- **Gate 1 — calibration stop:** after the protocol, benchmark proposal, coverage scaffold, index, and three calibration records. Do not review another module.
- **Gate 2 — protocol approval:** owner accepts or changes taxonomy, evidence threshold, scores, priorities, and exercise counting.
- **Gate 3 — benchmark approval:** owner approves a controlled external corpus before final external-completeness findings.
- **Gate 4 — plan import:** record a stable expansion-plan revision; do not guess it.
- **Gate 5 — reconciliation:** map current findings to plan items without converting planned work into current coverage.
- **Gate 6 — batch authorization:** owner explicitly authorizes review of the remaining modules and selects batch size/order.
- **Gate 7 — implementation authorization:** review findings alone never authorize content/code changes.
