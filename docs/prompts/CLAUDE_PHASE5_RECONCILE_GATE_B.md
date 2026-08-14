# Claude prompt — reconcile MATH/OPT review decisions, then Gate B only

Use this in a fresh Claude Code session at the repository root. Use **Opus** for
this pass. This prompt supersedes the earlier unrun MATH-approval and Gate-B-start
prompts.

---

You are continuing the gated Phase 5 planning process for the Robotics & ML
Workbook. This is a high-impact curriculum-architecture and source-selection
task. Work autonomously within the scope below, verify rather than infer, and
stop at the stated approval boundary.

## 0. Rehydrate from repository evidence

Before editing anything:

1. Read `AGENTS.md` in full.
2. Read `CLAUDE.md`, `docs/agent/CURRENT_HANDOFF.md`, and
   `docs/agent/CONTINUITY_AND_QUALITY.md`.
3. Run:
   - `git status --short`
   - `python3 scripts/validate/agent_context.py`
   - `python3 scripts/validate/review_integrity.py`
4. Read these authoritative records in full:
   - `docs/decisions/0005-gate-a-approved.md`
   - `docs/decisions/0006-math-review-approved.md`
   - `docs/decisions/0007-opt-review-approved.md`
   - `docs/plans/PHASE5_AUGMENTATION_PLAN.md`
   - `docs/plans/GATE_A_BASELINE.md`
   - `docs/review/REVIEW_PROTOCOL.md`
   - `docs/review/blocks/MATH.md`
   - `docs/review/blocks/OPT.md`
   - `docs/review/CURRICULUM_COVERAGE.md`
   - `docs/review/REVIEW_INDEX.md`
5. Inspect the relevant parts of `data/curriculum/CURRICULUM.md`,
   `data/curriculum/ARCHITECTURE.md`, the current source manifest, and any code
   needed to verify plan claims. Do not load historical narrative merely for
   comfort; inspect it only when it is evidence for a claim.
6. State, before edits, your recovered objective, authority, write scope, active
   plan revision/hash, and mandatory stop condition.

If repository evidence differs from this prompt, follow the newest explicit
owner decision and report the discrepancy. Do not use chat memory for exact
counts, hashes, approvals, or source claims.

## 1. Fixed state and boundaries

- Gate A is owner-approved and closed. Do not reopen, repeat, or re-litigate it.
- The committed current-content baseline is
  `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`. Keep committed-baseline evidence
  separate from dirty-worktree context.
- The current plan is revision 2.2, but decisions 0006 and 0007 make its
  future-work thesis, counts, and foundation scope obsolete. Publish a new
  reconciled revision rather than editing history or rewriting decision 0005.
- The MATH and OPT reviews are approved findings. The modules remain
  `CURRENTLY_PARTIAL`; approval does not mean repairs already exist.
- The approved external benchmark corpus in `docs/review/` is review evidence,
  not automatic approval for the production source corpus.
- `docs/review/**` is owned by the independent Codex review lane. Read it but do
  not edit it in this pass.
- Codex is continuing with PROB independently. Do not invent, anticipate, or
  incorporate unapproved PROB findings. Instead, provide a controlled amendment
  mechanism for later approved block-review deltas.
- Do not modify current lessons, questions, solutions, cheat sheets, exams,
  current curriculum implementation, packages, interactive components, or
  runtime code. Do not ingest/download a production corpus. This pass is plan
  reconciliation and Gate B source recommendation only.
- Preserve all unrelated modified and untracked files. Do not stage, discard,
  overwrite, or commit them.
- Leave `RotationViz` and `GridWorldRL` paused and out of scope. Do not use them
  as justification for a runtime decision in this task.
- Do not change repository visibility or deploy anything.

Public teaching notes, including Marc Toussaint's, may be used as learning
sources. Clear credit, exact locators, and provenance remain required. Do not
block or derail source selection with a generic plagiarism/rights discussion;
do not make a new visibility/deployment decision in this pass.

## 2. Task A — publish the reconciled Phase 5 plan revision

Revise `docs/plans/PHASE5_AUGMENTATION_PLAN.md` so it fully and explicitly owns
every approved delta in decisions 0006 and 0007.

At minimum:

### 2.1 Correct the plan thesis

Replace the broad claim that the workbook's defect is “not missing theory.” The
evidence now supports a narrower conclusion: the implementation/lab gap remains
large, and the reviewed MATH/OPT blocks also contain material foundation
correctness, qualification, routing, assessment, and relevance-scoped
completeness debt. Do not generalize the MATH/OPT verdict to unreviewed blocks.

### 2.2 Add a foundation-stabilization lane

Before downstream augmentation relies on these foundations, schedule all
approved mandatory MATH/OPT repairs:

- factual and notation corrections;
- theorem conditions and source qualifications;
- prerequisite/readiness and cross-module route repairs;
- propagation into exercises, solutions, cheat sheets, milestones, and
  downstream references;
- the approved compact in-module foundation additions;
- explicit repair-in-place versus deepen-elsewhere ownership.

Keep this lane distinct from optional enrichment and from later advanced-module
authoring. Give it gate placement, dependencies, outputs, acceptance criteria,
and a re-review requirement.

### 2.3 Integrate the approved new modules and ownership split

Add and route:

- `NUM-03` — stable solves, conditioning, numerical rank, QR, and Cholesky;
- `OPT-04B` — differentiable optimization via the IFT and root/argmin/KKT
  systems, including assumptions and failure modes;
- `OPT-05B` — derivative-free optimization, CPU-first and evaluation-budget
  aware.

Preserve `MATH-05` as the conceptual/covariance owner and `OPT-01` as the place
that recalls and applies it. Keep ADMM optional/deferred unless a concrete
downstream dependency emerges. Route source overlap with reinforcement learning
to RL/RLEARN rather than duplicating it inside OPT.

### 2.4 Integrate approved teaching surfaces

Own whole-block keyed recall for MATH and OPT, corrected/rebalanced MATH-EXAM and
OPT-EXAM coverage and retakes, and the five approved static-visual concepts for
each block. Static figures are the acceptance baseline. Browser interactives
remain optional and require later value/runtime/bundle approval; do not turn
them into mandatory widgets here.

### 2.5 Recalculate all consequences

Recompute, do not hand-edit by intuition:

- total modules, new additions, blocks, and hours;
- main-route versus optional totals;
- block/module tables and executive summaries;
- route positions and prerequisite edges;
- gate deliverables and acceptance criteria;
- stubs, file inventories, milestone/reference/visual totals;
- every downstream occurrence of an affected count or ID.

Search the entire plan for stale revision-2.2 counts and claims. If hours are
estimates, label the method and preserve arithmetic reproducibility. Add or use
a small deterministic planning check if that is the clearest way to prove
internal consistency, but do not modify application/runtime code.

### 2.6 Add a later-review amendment mechanism

Define how later owner-approved block reviews can add mandatory repairs, source
needs, or route changes without reopening Gate A or silently invalidating Gate
B. The mechanism must:

- accept only owner-approved review decisions;
- classify the delta as repair, compact addition, new module, source amendment,
  or explicit omission/deferment;
- evaluate dependency and source consequences;
- revise and re-pin the stable plan;
- reopen Gate B only for the affected source subset when necessary;
- keep implementation blocked until the affected approval is recorded.

Do not wait for every remaining block review before completing this plan pass.

## 3. Task B — Gate B source selection only

After Task A is internally consistent, conduct Gate B source selection against
the reconciled scope. Create a planning-owned Gate B proposal at a stable path,
preferably `docs/plans/GATE_B_SOURCE_SELECTION.md`. Do not ingest the selected
sources and do not author curriculum.

### 3.1 Evaluate source roles separately

Do not treat all sources as interchangeable. Evaluate at least:

- **Theory:** Tedrake's *Underactuated Robotics* and *Robotic Manipulation*;
- **Official API/tool documentation:** MuJoCo, Gymnasium, Drake where narrowly
  justified, PyTorch, Triton or the selected GPU-programming alternative, and
  LeRobot/Hugging Face components actually needed by the route;
- **Reference implementations:** CleanRL and/or Stable-Baselines3, selecting or
  limiting each by pedagogical role rather than accumulating libraries;
- **Original papers:** DQN, PPO, SAC, DAgger, AlphaZero/AlphaGo only at the depth
  the curriculum needs, behavior cloning, and Diffusion Policy;
- **Foundation sources created by decisions 0006/0007:** numerical linear
  algebra, differentiable optimization, derivative-free optimization, convex
  problem-class recognition, and authoritative references for mandatory
  theorem/condition repairs.

You may recommend better sources than the plan's candidates. Prefer primary and
official sources for factual/API claims and a small, coherent teaching corpus
over a long bibliography.

### 3.2 Required decision matrix

For every candidate, record:

- stable identifier and source role;
- exact title/author/maintainer;
- official URL and, where relevant, version/tag/commit and access date;
- chapters/sections/APIs mapped to concrete modules or repairs;
- what it uniquely adds and where it overlaps current/Tedrake/Toussaint material;
- authority and pedagogical suitability;
- runtime, hardware, account, cost, and maintenance constraints;
- citation/provenance locator strategy;
- decision: select, optional, defer, or reject, with rationale;
- fallback or substitution risk when the source/tool changes.

No paid API key or paid account may be required. Core labs must remain CPU-first;
GPU work must be explicitly labelled optional or justified as an advanced
requirement. The owner's GPU availability does not make GPU a prerequisite for
the core learning route.

### 3.3 Relevance-scoped completeness

Build a section-level disposition map for selected book/note sources. A source
is not “covered” merely because its title appears or because declared module
objectives are satisfied. Mark relevant sections as:

- teach here;
- route to an existing/future module;
- optional reference;
- intentionally omit, with relevance rationale.

Small facts may be omitted when they do not support the learning route, later
content, or the owner's robotics/planning/reachable-behaviour research. The
important requirement is an explicit, reviewable disposition—not maximal
inclusion.

### 3.4 Gate B output and stop

End with one concise, batched owner-approval prompt that separates:

- recommended production corpus;
- optional/deferred candidates;
- explicit rejections;
- any genuinely consequential choice that cannot be made from evidence;
- exact effects on runtime, cost/accounts, route, and maintenance.

Then stop. Do not begin source acquisition, manifest population, F0 repairs,
module/lab authoring, or Gate C.

## 4. Validation and handoff

Before reporting completion:

1. Verify the plan's revision history and status language.
2. Recompute the plan SHA-256 and record it in the Gate B proposal and
   `docs/agent/CURRENT_HANDOFF.md`.
3. Search for stale affected totals, obsolete thesis language, and references
   claiming Gate B is not started if the proposal now exists. Distinguish
   “proposal complete” from “corpus owner-approved.”
4. Confirm no decision record and no `docs/review/**` file changed.
5. Run `python3 scripts/validate/agent_context.py`,
   `python3 scripts/validate/review_integrity.py`, and any deterministic plan
   consistency check you created.
6. Inspect `git diff --stat` and the full diffs of every file you changed.
7. Replace `docs/agent/CURRENT_HANDOFF.md` with a concise boundary packet. Do not
   append a session diary.

In your final response, lead with the outcome, list changed files, give the new
plan revision/hash, summarize selected/optional/rejected source groups, state
checks and limitations, paste the single owner-approval prompt, and explicitly
confirm that you stopped before ingestion or authoring.

Do not switch to Sonnet during this pass. Recommend the switch only after the
owner approves the reconciled plan and Gate B, when the next work is patterned
source-manifest/scaffolding or batch production. Retain Opus or an independent
high-reasoning reviewer for theorem repairs, the first example of each new
module/lab pattern, and gate closure.
