# Quality and session-wellness runbook

Status: **ACTIVE**
Audience: the owner and any Codex/Claude session working in this repository.

This is the practical schedule for the safeguards defined in `AGENTS.md` and
`CONTINUITY_AND_QUALITY.md`. “Agent wellness” means maintaining clean context,
bounded scope, and verifiable state. Models do not improve by resting; humans do.

## Command map

| Command | What it proves | When to run |
|---|---|---|
| `python3 scripts/validate/agent_context.py` | Startup files exist and stay concise; handoff matches active plan revision/hash | Session start/resume, after compaction/model switch, and at every gate/block boundary |
| `python3 scripts/validate/review_integrity.py` | Review index exactly matches the pinned baseline; started records and completed blocks are structurally complete | Before and after each block review/approval |
| `python3 scripts/validate/gate_a_baseline.py --no-write` | The approved Phase 4/Gate A mechanical baseline remains reproducible | Only when a later task claims the baseline changed or a final audit needs it; do not rerun Gate A as a decision |
| `npx astro check` | Astro/TypeScript/content-schema diagnostics | After implementation changes that can affect rendering/schema |
| `npm run build` | Production site builds | At implementation batch boundaries and before release/commit handoff |

Passing a command proves only its stated scope. It does not prove mathematical
truth, source completeness, pedagogy, live appearance, or runtime correctness.

## Stage 1 — start or resume a code session

Run the context checker on every:

- new Codex or Claude session;
- resumed session after a rate/token limit;
- conversation compaction;
- model or agent switch;
- gap long enough that another actor may have changed repository state;
- session where the plan, a decision, or the handoff changed since last read.

You normally do not need to run it yourself. Tell the agent to do it with this
copy-paste instruction:

> Read `AGENTS.md` and `docs/agent/CURRENT_HANDOFF.md`, run
> `python3 scripts/validate/agent_context.py`, inspect `git status --short` and
> relevant diffs, then state the active objective, authoritative revision,
> approval boundary, write scope, and stop condition before editing. If the
> checker fails or repository evidence conflicts with the handoff, repair the
> continuity state first and report the discrepancy.

Do not accept “I remember the previous session” as a substitute.

If the context checker:

- **passes:** proceed;
- **warns:** the agent must explain whether the warning is expected before work;
- **fails:** stop substantive work, repair the handoff/instructions/pin, rerun,
  and proceed only after it passes.

During one uninterrupted, healthy session, do not rerun it after every edit. Run
it again when an authoritative plan/hash or boundary state changes.

## Stage 2 — routine work inside a healthy session

The agent should keep a small working checkpoint in its reasoning:

1. current objective;
2. evidence being used;
3. files it owns;
4. next validation;
5. stop condition.

Ask for a recovery checkpoint if the agent begins to:

- quote incompatible counts or revisions;
- forget whether a finding is approved or implemented;
- confuse current and planned coverage;
- ask questions already answered by current decisions;
- edit outside its lane;
- repeat a corrected mistake;
- make source claims without locators;
- treat a build as proof of content correctness.

Recovery instruction:

> Stop editing. Re-read `AGENTS.md`, the current handoff, and the exact decision,
> plan, or review evidence governing this task. Rerun the context checker and
> restate objective, authority, write scope, completed evidence, and stop
> condition. Continue only if they are mutually consistent.

If the same failure recurs after recovery, end at a clean handoff and use a fresh
session or independent model.

## Stage 3 — before compaction, a rate limit, or a model switch

Do not let an agent start a new subtask when little context/usage remains. Use:

> Stop at the nearest clean boundary; do not begin another task. Replace
> `docs/agent/CURRENT_HANDOFF.md` with the exact completed outputs, evidence and
> hashes, outstanding uncertainties/unrun checks, dirty-file ownership, next
> safe action, model recommendation, and mandatory stop condition. Keep it under
> its size limit. Run `python3 scripts/validate/agent_context.py` and report the
> result.

After automatic compression, use the Stage 1 instruction. Do not ask the agent
to continue directly from the compressed summary.

Switch models only after the handoff passes. A model switch is a role boundary,
not a rescue for unrecorded work.

## Stage 4 — module and block review

At the start of a block:

```bash
python3 scripts/validate/agent_context.py
python3 scripts/validate/review_integrity.py
```

Then follow `docs/review/REVIEW_PROTOCOL.md`. The reviewer must inspect the
committed baseline, declared source ranges, prerequisites/dependents, questions,
solutions, reference surfaces, and the block assessment—not just module prose.

Before presenting the batched block approval:

1. update every module record, the block record, coverage ledger, and review
   index together;
2. run `review_integrity.py`;
3. independently verify high-impact mathematical/source findings;
4. separate mandatory repairs, relevance-scoped additions, optional enrichment,
   and live visual decisions;
5. give the owner one batched approval prompt;
6. do not implement findings.

After owner approval:

1. create the decision record;
2. update review states and plan-reconciliation status;
3. update the handoff;
4. rerun both context and review-integrity checks.

The review checker may fail while a record and index are temporarily mid-edit.
That is acceptable only inside the same bounded edit; it must pass before the
review is handed to another agent or the owner.

## Stage 5 — plan revision and source gates

At plan/gate start and finish, run the context checker. Require:

- deterministic recounts for modules, blocks, hours, artifacts, and routes;
- a search for stale totals and superseded thesis language;
- a stable revision and SHA-256 in the handoff;
- an independent architecture/source review before owner approval;
- one approval decision before implementation proceeds.

For Gate B, source selection and source ingestion are separate. The proposal can
be complete while the production corpus remains unapproved.

After Claude publishes the reconciled Phase 5 plan, add a plan-consistency
validator based on that stable structure. Do not finalize it against revision
2.2. After Gate B approves the source schema/corpus, add a source-manifest
validator for identifiers, locators, versions/access dates, roles, and module
mappings.

## Stage 6 — implementation and repair batches

At each batch start:

1. run the context checker;
2. identify the approved finding/module IDs being implemented;
3. confirm the batch's source and file ownership;
4. select tests that can falsify the changed claims.

At each batch end, use the applicable checks:

- schema/link/citation/exercise-solution checks;
- executable numerical checks for equations and answer keys;
- `npx astro check` and `npm run build`;
- KaTeX-error checks when math changed;
- live desktop/mobile inspection when layout or interaction changed;
- CPU/GPU/runtime tests matching the artifact declaration;
- re-review against the approved finding list.

Use a high-capability model or independent reviewer for theorem-sensitive F0
repairs and the first example of each new module/lab pattern. Once that pattern
passes, a balanced model may produce the remaining batch with risk-based
sampling. One failed sampled item expands validation to the whole pattern.

## Stage 7 — commit, pause, or handoff boundary

Before asking to commit or handing work to another agent:

1. inspect `git status --short`, `git diff --stat`, and all owned diffs;
2. run the checks appropriate to the work, not merely the cheapest check;
3. report unrun checks and known limitations;
4. replace the current handoff and run the context checker;
5. verify no unrelated user/agent files were staged or modified.

Do not commit merely to create a checkpoint unless the owner requested it.

## Stage 8 — final curriculum confidence pass

After all planned repairs and additions are implemented:

1. rerun the complete block and whole-curriculum review;
2. run context, review-integrity, plan-consistency, source-manifest, schema,
   link/citation, exercise/solution, numerical, build, and runtime checks;
3. perform representative live visual checks across page/tool types;
4. independently audit theorem conditions, assessments, and source-section
   dispositions;
5. have the owner sample the course as a learner;
6. publish known omissions, update-sensitive areas, and the review date.

Only this post-implementation re-review supports the intended high-confidence
status. A plan or an approved finding list alone does not.

## Human wellness and review cadence

- Review one block at a time and make one batched decision; avoid dozens of
  interrupting micro-approvals.
- For dense mathematical/source review, use roughly 60–90 minute human review
  sessions, then take a break if attention is slipping. This helps the human,
  not the model.
- Stop when you are approving mechanically rather than evaluating tradeoffs.
- Prefer a fresh session at gate or role boundaries, not arbitrary daily resets.
- Rate limits are a natural checkpoint: require a valid handoff instead of
  squeezing in another partially completed task.

## Minimal owner routine

If you remember only four rules:

1. **New/resumed session:** ask for Stage 1 rehydration and a passing context
   check.
2. **Before a limit/switch:** demand a replace-in-place handoff and passing check.
3. **At a block/gate boundary:** require the relevant structural validator plus
   independent checking before approval.
4. **After implementation:** require re-review; never infer correctness from the
   plan or build alone.
