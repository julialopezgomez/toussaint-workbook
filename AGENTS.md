# Agent operating rules

This file is the stable, repository-wide entry point for any coding or planning
agent. Keep it short. Volatile state belongs in
`docs/agent/CURRENT_HANDOFF.md`; detailed operating guidance belongs in
`docs/agent/CONTINUITY_AND_QUALITY.md`. The owner-facing schedule and copy-paste
instructions are in `docs/agent/STAGE_RUNBOOK.md`.

## Start and resume

Before substantive work:

1. Read `docs/agent/CURRENT_HANDOFF.md`.
2. Read only the decisions, plan sections, review records, and source files that
   the handoff identifies for the current task.
3. Run `git status --short` and inspect relevant diffs. Existing changes are
   user-owned unless the handoff explicitly assigns them to you.
4. Run `python3 scripts/validate/agent_context.py`.
5. State the active task, approval boundary, write scope, and authoritative
   revision before editing.

After chat compaction, a fresh session, a model switch, or any uncertainty about
exact numbers, repeat this sequence. A chat summary is navigation, not evidence.
Never recover hashes, counts, approvals, findings, or source claims from memory.

## Authority and document roles

Use this precedence for repository state:

1. the user's latest explicit instruction;
2. approved records in `docs/decisions/`;
3. current evidence in `docs/review/` for reviewed scope;
4. the active stable plan in `docs/plans/` for future work;
5. current curriculum and implementation;
6. `PROJECT_STATE.md` and other historical narrative.

Planned content is never evidence of current coverage. Review approval accepts
findings and dispositions; it does not mean that lessons have already been
repaired. Decision records are immutable historical records: supersede them
with a new record rather than silently rewriting them.

`docs/agent/CURRENT_HANDOFF.md` is a concise routing aid, not an authority. If it
conflicts with a decision, plan, review record, source file, or `git status`, fix
the handoff before continuing.

## Approval boundaries

- Do not author or repair curriculum content ahead of its approval gate.
- Gate A is closed; do not reopen or repeat it unless the owner explicitly does
  so in a new decision.
- A review benchmark corpus is not a production-source approval.
- Do not change repository visibility, deploy, add paid services, require API
  keys, or require an account without explicit current authorization.
- Publicly accessible teaching notes may be used as learning sources. Preserve
  clear credit and the repository's provenance labels. Do not turn source
  selection into a generic plagiarism debate.

## Source and content integrity

- `../original notes/` is read-only: never move, rename, overwrite, edit, or
  commit it. Approved Obsidian-vault content is also inspect-only.
- Never commit full extracted source text. Keep
  `data/source-manifest/raw-text/` and `html-text/` ignored.
- Source-derived claims, equations, examples, figures, and exercises need the
  locator and provenance required by the active source policy.
- Solutions and rubrics authored by this workbook must not be attributed to the
  source corpus.
- Relevance-scoped completeness is the standard: cover material that supports
  the learning route, later content, or the owner's research; explicitly route,
  defer, or omit the rest instead of silently claiming full coverage.

## Evidence and validation

- Separate the committed baseline from the dirty worktree in every report.
- Consequential factual, mathematical, source, route, and count claims require
  direct evidence. Prefer primary sources and exact locators.
- Do not treat a successful build as semantic, mathematical, citation, or visual
  validation.
- Run checks proportionate to the change and report what was not checked.
- For high-impact work, use the independent-check rules in
  `docs/agent/CONTINUITY_AND_QUALITY.md` before asking for approval.

## Editing and handoff

- Preserve unrelated worktree changes. Never discard or overwrite another
  agent's or the user's work.
- Follow the write ownership in `docs/agent/CURRENT_HANDOFF.md`. If ownership is
  unclear or overlapping, stop before editing the overlap.
- Keep stable instructions, current state, plans, evidence, and history in their
  separate document roles. Do not append session diaries to instruction files.
- At every block/gate boundary, before an expected context limit, and before a
  model/agent switch, replace the handoff with a concise evidence-based state
  packet and rerun the context validator.

## Standard project checks

- Context health: `python3 scripts/validate/agent_context.py`
- Review structure: `python3 scripts/validate/review_integrity.py`
- Phase 5 baseline reporter: `python3 scripts/validate/gate_a_baseline.py --no-write`
- Type/content check: `npx astro check`
- Production build: `npm run build`
- After changing display math, inspect for malformed `$$` delimiters and search
  built pages for actual `katex-error` output.

Do not run every expensive check mechanically. Choose the smallest set that can
falsify the claims changed by the task.
