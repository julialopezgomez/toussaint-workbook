# Agent continuity and quality protocol

Status: **ACTIVE**
Purpose: preserve reasoning quality across long reviews, chat compression,
token limits, model changes, and parallel planning/review lanes without turning
the repository into a transcript archive.

## 1. The operating principle

The repository is the durable memory. Conversation context is a temporary
workspace.

A good handoff does not summarize everything that happened. It identifies:

- what is authoritative;
- what was actually completed and verified;
- what remains open or unverified;
- who may write which files;
- the exact next safe action and stop condition.

If a claim matters enough to affect curriculum structure, source selection,
mathematics, assessment, or implementation, it must survive in an appropriate
repository artifact—not only in chat.

## 2. Recovery after compaction or a fresh session

Treat any compacted summary as a map to evidence, not as evidence itself.

1. Read `AGENTS.md`, then `docs/agent/CURRENT_HANDOFF.md`.
2. Run `git status --short`; inspect diffs for every file in the assigned write
   scope.
3. Run `python3 scripts/validate/agent_context.py`.
4. Open the cited decision record(s), the active plan section(s), and the exact
   review/source/code artifacts needed for the next action.
5. Recompute or re-read exact hashes, counts, routes, and citations. Do not quote
   them from the compacted summary.
6. Write a four-line internal checkpoint before editing: objective, authority,
   write scope, stop condition.
7. If the handoff disagrees with repository evidence, repair the handoff and
   explain the discrepancy before substantive work.

Do not restart completed work merely because context was compacted. Verify its
artifact and continue from the next recorded boundary.

## 3. When to checkpoint or start a clean session

Replace `CURRENT_HANDOFF.md`:

- after a block review or approval gate;
- before a known token/rate limit;
- before changing model or agent;
- before switching from judgment-heavy planning to repetitive production;
- when file ownership changes;
- when a task will be paused with uncommitted work;
- immediately after discovering that the previous handoff is stale.

Start a clean session when the current session repeatedly:

- cites obsolete revisions or forgets an approval boundary;
- conflates planned coverage with present coverage;
- reopens settled work without new evidence;
- loses track of worktree ownership;
- gives inconsistent counts or cannot reproduce them;
- continues to make the same class of mistake after one correction and one
  explicit re-read.

Waiting for wall-clock time does not improve model quality. Pause only for a
rate limit, human fatigue, an external dependency, or a deliberately chosen
review boundary. A fresh session can remove distracting context, but only a
complete handoff prevents information loss.

## 4. Handoff format and size

`CURRENT_HANDOFF.md` is replaced, not appended. Keep it under **160 lines and
16 KiB**. It contains only:

- timestamp and baseline;
- active objective and approval boundary;
- authoritative files/revisions;
- completed and independently verified outputs;
- open findings, uncertainties, and unrun checks;
- write ownership and dirty-worktree cautions;
- next safe action and mandatory stop;
- model recommendation for that next action.

It must not contain:

- long narrative history;
- copied plan sections;
- full source excerpts;
- speculative findings stated as decisions;
- generated inventories;
- claims that exist only to save the next agent from opening the real evidence.

## 5. Quality checks for model output

### 5.1 Claim-to-evidence check

For every high-impact output, sample or enumerate its consequential claims:

| Claim type | Minimum verification |
|---|---|
| module/block/hour/count change | deterministic recount plus search for stale totals |
| prerequisite or curriculum route | graph/order check plus at least one direct file inspection |
| mathematical/theorem statement | primary source or standard authoritative source; assumptions stated |
| source completeness | section-level source disposition map, not only declared objectives |
| source/API recommendation | official current documentation, version/access date, maintenance/runtime constraints |
| citation/provenance repair | source locator and rendered/structured reference check |
| build/runtime claim | the relevant command or live test, not inference from code |
| visual teaching claim | static render or live view at the intended viewport |

### 5.2 Independent check

Use an independent pass for work that is expensive to reverse: curriculum
architecture, source-corpus selection, theorem corrections, assessment answer
keys, route changes, numerical derivations, and new runtime/dependency choices.

An independent pass means a fresh context or different model/agent that receives
the requirements and artifacts but not the first reviewer's conclusion. It must
be able to disagree. Ask it to look specifically for omissions, unsupported
assumptions, duplicated coverage, and false confidence.

For repetitive production, use risk-based sampling: validate the first item in
full, then at least one item per distinct pattern and every exceptional item.
Increase to full checking when one sampled item fails.

### 5.3 Performance regression signals

Do not judge quality from eloquence or file volume. Stop and recover if an agent:

- changes scope without naming an authority;
- replaces explicit source dispositions with broad “complete” claims;
- treats build success as content correctness;
- produces new totals without showing how they were recomputed;
- silently edits outside its ownership lane;
- adds optional material while mandatory repairs remain unowned;
- asks questions answered by the handoff or current decision records.

## 6. Model and agent selection

Choose by task phase, not prestige or remaining token allowance.

| Work | Recommended capability |
|---|---|
| curriculum architecture, source selection, theorem audit, ambiguous reconciliation | highest-capability model; high/extra-high reasoning |
| bounded but very hard single judgment | highest-capability model; max only when depth outweighs latency/usage |
| approved, patterned implementation and documentation | balanced workhorse; medium/high reasoning |
| deterministic extraction, formatting, inventories, repeated transforms | fast model; low/medium reasoning, with deterministic validation |
| final high-impact approval recommendation | independent fresh pass, preferably a different model family/session |

For the present workflow:

- Keep Claude Opus through Phase 5 plan reconciliation and the Gate B source
  proposal. Those are high-leverage judgment tasks.
- Switch to Sonnet after the owner approves the reconciled plan and Gate B, when
  work becomes source-manifest construction, patterned scaffolding, or batch
  production. Keep Opus—or an independent high-reasoning reviewer—for theorem
  repairs, the first example of each new module/lab pattern, and gate closure.
- In Codex, use Sol for the same open-ended/high-value work, Terra for routine
  implementation, and Luna only for clearly specified mechanical work. Use the
  lowest reasoning effort that passes the quality checks; increase it for
  multi-source tradeoffs or repeated check failures.
- Do not switch models in the middle of an unrecorded judgment. Finish or stop at
  a named boundary, update the handoff, then switch.

Using two agents is valuable when their roles are genuinely independent—for
example, Claude owns plan/source selection while Codex owns evidence review.
It is harmful when both edit the same files or inherit each other's untested
conclusions. The handoff must name ownership.

## 7. Documentation lifecycle

Use one document for one role:

- `AGENTS.md`: stable repository operating rules;
- `CLAUDE.md`: short Claude entry point only;
- `CURRENT_HANDOFF.md`: volatile resume packet, replaced in place;
- `docs/decisions/`: immutable approvals and reversals;
- `docs/plans/`: future work and gates;
- `docs/review/`: evidence about current content;
- `data/curriculum/`: currently implemented curriculum specification;
- `PROJECT_STATE.md`: historical ledger, not required startup context;
- generated JSON/inventories: machine evidence, never startup prose.

When a document becomes obsolete:

1. remove its current-status claim from startup instructions;
2. mark it `SUPERSEDED` and link the replacement, or move it to an archive when
   no stable links depend on the path;
3. update inbound references;
4. search for stale revisions, totals, status phrases, and open questions;
5. rerun the context validator.

Prefer deleting duplicated prose over synchronizing the same volatile fact in
several files. Preserve historical decisions; prune or archive narrative logs.

## 8. Boundary checklist

Before declaring a block, plan revision, or gate ready:

- [ ] Requested scope is complete and nothing beyond it was silently added.
- [ ] Decisions and present-vs-planned coverage are separated.
- [ ] Counts, hashes, routes, and source locators are reproduced.
- [ ] Mandatory findings have owners; optional items are labelled.
- [ ] Required deterministic, semantic, build, and visual checks are recorded.
- [ ] Unchecked items and uncertainties are explicit.
- [ ] Worktree ownership is intact.
- [ ] `CURRENT_HANDOFF.md` describes the next action and stop condition.
- [ ] `agent_context.py` passes or every warning is explained.
